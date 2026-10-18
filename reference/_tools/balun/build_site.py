#!/usr/bin/env python3
"""Сборка страниц Docusaurus из карты курса и текстов.

usage: python3 -I build_site.py <balun-sd dir>

1. text/_whisper/NN.json -> text/NN-transcript.md  (абзацы по ~60 с с таймкодом)
2. map/course-map.md -> site/docs/<NN-slug>/<MM-slug>.md

Формат карты:
  ## 01 · Название урока            -> категория урока, тело до первой ### - index.md урока
  ### 01.03 · Название темы         -> страница темы
  <!-- slides: 4-12, 15; video: 00:05:10-00:21:00 -->   (оба поля необязательны)
  ...markdown темы (идеи, mermaid, вопросы)...
К странице темы дописываются текст слайдов из text/NN-slides.md и фрагмент расшифровки.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
TEXT, SITE = ROOT / "text", ROOT / "site"
DOCS = SITE / "docs"

TRANSLIT = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                    "a b v g d e e zh z i y k l m n o p r s t u f h ts ch sh sch _ y _ e yu ya".split()))


def slug(s: str) -> str:
    s = "".join(TRANSLIT.get(c, c) for c in s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def hms(t: float) -> str:
    t = int(t)
    return f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"


def secs(s: str) -> int:
    h, m, x = (int(p) for p in s.split(":"))
    return h * 3600 + m * 60 + x


# ---------- 1. расшифровки ----------

def build_transcripts() -> dict[str, list[tuple[float, float, str]]]:
    out = {}
    for j in sorted((TEXT / "_whisper").glob("*.json")):
        nn = j.stem
        segs = [(s["start"], s["end"], s["text"].strip()) for s in json.loads(j.read_text())["segments"]]
        segs = [s for s in segs if s[2]]
        out[nn] = segs
        paras, cur, start = [], [], None
        for a, b, t in segs:
            if start is None:
                start = a
            cur.append(t)
            if b - start >= 60:
                paras.append(f"**[{hms(start)}]** {' '.join(cur)}")
                cur, start = [], None
        if cur:
            paras.append(f"**[{hms(start)}]** {' '.join(cur)}")
        (TEXT / f"{nn}-transcript.md").write_text(
            f"# Урок {nn}: расшифровка видео\n\nАвтоматическая (mlx-whisper large-v3-turbo), "
            f"возможны ошибки в терминах. Длина: {hms(segs[-1][1])}.\n\n" + "\n\n".join(paras) + "\n",
            encoding="utf-8")
    return out


def transcript_range(segs, rng: str) -> str:
    a, b = (secs(x) for x in rng.split("-"))
    lines, buf, start = [], [], None
    for s, e, t in segs:
        if e < a or s > b:
            continue
        if start is None:
            start = s
        buf.append(t)
        if e - start >= 45:
            lines.append(f"**[{hms(start)}]** {' '.join(buf)}")
            buf, start = [], None
    if buf:
        lines.append(f"**[{hms(start)}]** {' '.join(buf)}")
    return "\n\n".join(lines)


# ---------- 2. слайды ----------

def load_slides(nn: str) -> dict[int, str]:
    f = TEXT / f"{nn}-slides.md"
    if not f.exists():
        return {}
    body = f.read_text(encoding="utf-8").split("\n## Структура урока")[0]
    res = {}
    for part in re.split(r"\n(?=## Слайд \d+)", body):
        m = re.match(r"## Слайд (\d+)\.?\s*(.*)", part)
        if m:
            text = part.split("\n", 1)[1] if "\n" in part else ""
            # картинка слайда - из static/slides
            text = re.sub(r"!\[\]\(\.\./slides/", "![](/slides/", text)
            res[int(m.group(1))] = (m.group(2).strip(), text.strip())
    return res


def parse_ranges(s: str) -> list[int]:
    out = []
    for p in s.split(","):
        p = p.strip()
        if "-" in p:
            a, b = p.split("-")
            out += range(int(a), int(b) + 1)
        elif p:
            out.append(int(p))
    return out


def esc_mdx(s: str) -> str:
    """Текст слайдов - не MDX: экранируем { } < вне код-блоков."""
    parts = re.split(r"(```.*?```)", s, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = parts[i].replace("{", "\\{").replace("}", "\\}")
        parts[i] = re.sub(r"<(?![!/a-zA-Z])", "&lt;", parts[i])
        parts[i] = re.sub(r"<(?!/?(details|summary|br)\b|!--)", "&lt;", parts[i])
    return "".join(parts)


# ---------- 3. карта -> docs ----------

def build_docs(transcripts) -> int:
    cmap = (ROOT / "map" / "course-map.md").read_text(encoding="utf-8")
    for old in DOCS.glob("*"):
        if old.is_dir():
            for f in old.rglob("*"):
                f.unlink()
            old.rmdir()
        else:
            old.unlink()
    lessons = re.split(r"\n(?=## \d\d )", cmap)
    intro = lessons.pop(0)
    (DOCS / "index.md").write_text(
        "---\nslug: /\nsidebar_position: 0\ntitle: О курсе\n---\n\n" + re.sub(r"^# .*\n", "", intro).strip() + "\n",
        encoding="utf-8")
    (DOCS / "map.md").write_text("---\nslug: /map\nsidebar_position: 99\ntitle: Карта целиком\n---\n\n"
                                 + esc_mdx(re.sub(r"<!--.*?-->", "", cmap.split("\n", 1)[1])), encoding="utf-8")
    n_topics = 0
    for li, block in enumerate(lessons):
        head, *topics = re.split(r"\n(?=### \d\d\.\d\d )", block)
        m = re.match(r"## (\d\d) · (.+)", head)
        nn, title = m.group(1), m.group(2).strip()
        ldir = DOCS / f"{nn}-{slug(title)}"
        ldir.mkdir(parents=True)
        (ldir / "_category_.json").write_text(json.dumps(
            {"label": f"{int(nn)}. {title}", "position": li + 1, "link": {"type": "doc", "id": f"{slug(title)}/index"}},
            ensure_ascii=False), encoding="utf-8")
        lbody = head.split("\n", 1)[1].strip() if "\n" in head else ""
        hw = TEXT / f"{nn}-homework.md"
        hw_md = f"\n\n## Домашнее задание\n\n<details><summary>Текст ДЗ</summary>\n\n{esc_mdx(hw.read_text(encoding='utf-8'))}\n\n</details>\n" if hw.exists() else ""
        (ldir / "index.md").write_text(
            f"---\ntitle: \"{int(nn)}. {title}\"\nsidebar_position: 0\n---\n\n{lbody}{hw_md}", encoding="utf-8")
        slides = load_slides(nn)
        for ti, t in enumerate(topics):
            th, tbody = (t.split("\n", 1) + [""])[:2]
            tm = re.match(r"### (\d\d)\.(\d\d) · (.+)", th)
            ttitle = tm.group(3).strip()
            meta = re.search(r"<!--\s*(.*?)\s*-->", tbody)
            sl, vid = [], None
            if meta:
                for kv in meta.group(1).split(";"):
                    k, _, v = kv.partition(":")
                    if k.strip() == "slides":
                        sl = parse_ranges(v)
                    elif k.strip() == "video":
                        vid = v.strip()
                tbody = tbody.replace(meta.group(0), "")
            src = []
            if sl:
                src.append(f"слайды {meta.group(1).split('slides:')[1].split(';')[0].strip()}")
            if vid:
                src.append(f"видео {vid}")
            page = [f"---\ntitle: \"{ttitle}\"\nsidebar_position: {ti + 1}\n---\n",
                    f"# {ttitle}\n", f"_Урок {int(nn)} · {' · '.join(src)}_\n" if src else "", tbody.strip(), ""]
            if sl and slides:
                page.append("## Слайды\n")
                for k in sl:
                    if k in slides:
                        stitle, stext = slides[k]
                        page.append(f"<details><summary>Слайд {k}. {esc_mdx(stitle)}</summary>\n\n{esc_mdx(stext)}\n\n</details>\n")
            if vid and nn in transcripts:
                tr = transcript_range(transcripts[nn], vid)
                if tr:
                    page.append(f"## Из лекции\n\n<details><summary>Расшифровка {vid}</summary>\n\n{esc_mdx(tr)}\n\n</details>\n")
            if tbody.count("```mermaid") > 1:
                # Docusaurus 3.10 молча не рисует вторую схему на странице - объединяй в одну через subgraph
                print(f"WARN {nn}.{tm.group(2)}: больше одной mermaid-схемы на странице")
            (ldir / f"{tm.group(2)}-{slug(ttitle)}.md").write_text("\n".join(page), encoding="utf-8")
            n_topics += 1
    return n_topics


if __name__ == "__main__":
    tr = build_transcripts()
    print(f"transcripts: {sorted(tr)}")
    if (ROOT / "map" / "course-map.md").exists():
        print(f"topics: {build_docs(tr)}")
