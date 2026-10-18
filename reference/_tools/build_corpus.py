#!/usr/bin/env python3
"""Корпус из экспорта Telegram-топика: нормализованные сообщения + куски для чтения.

Обобщение reference/roast-analysis/_work/build_corpus.py на чаты без threads.json
и без транскрипций резюме: здесь только result.json.

Выход (в --work):
  messages.json       - сообщения по id, источник правды для validate/stats
  chunks/chunk-NN.txt - корпус кусками по ~50k символов, разрез по паузе в разговоре
  chunks/index.json   - какие id в каком куске
  krasavchik.txt      - все сообщения эталона с родителем и ответами на них

Пример:
  python3 reference/_tools/build_corpus.py \
      --chat reference/linkedin-bans-chat --root 72878 \
      --work reference/linkedin-bans-analysis/_work
"""
import argparse
import glob
import json
import os
from datetime import datetime

KRAS = "АйТи Красавчик"
CHUNK_CHARS = 50_000
GAP_SECONDS = 2 * 3600
SNIPPET = 150


def flat(text):
    if isinstance(text, str):
        return text
    return "".join(p if isinstance(p, str) else p.get("text", "") for p in (text or []))


def load(chat):
    raw = json.load(open(os.path.join(chat, "result.json"), encoding="utf-8"))
    msgs = {}
    for m in raw["messages"]:
        if m.get("type") != "message":
            continue
        msgs[m["id"]] = {
            "id": m["id"],
            "date": m["date"],
            "from": m.get("from") or "(без имени)",
            "reply_to": m.get("reply_to_message_id"),
            "text": flat(m.get("text", "")),
            "edited": m.get("edited", ""),
            "forwarded": m.get("forwarded_from", ""),
            "file": m.get("file_name") or ("[фото]" if m.get("photo") else ""),
            "reactions": sum(r.get("count", 0) for r in m.get("reactions", [])),
            "reaction_detail": " ".join(f"{r.get('emoji', '?')}{r.get('count', 0)}" for r in m.get("reactions", [])),
        }
    return raw.get("name", ""), msgs


def render(m, msgs, root):
    parts = [f"[{m['id']}]", m["date"][:16].replace("T", " "), m["from"]]
    if m["forwarded"]:
        parts.append(f"переслано от {m['forwarded']}")
    if m["file"]:
        parts.append(f"файл={m['file']}")
    if m["reactions"]:
        parts.append(f"реакции={m['reaction_detail']}")
    head = " | ".join(parts)
    rt = m["reply_to"]
    if rt is None or rt == root:
        ctx = ""
    elif rt in msgs:
        p = msgs[rt]
        snip = p["text"][:SNIPPET].replace("\n", " ") or p["file"] or "(вложение)"
        ctx = f"\n  ↩ [{rt}] {p['from']}: «{snip}»"
    else:
        ctx = f"\n  ↩ [{rt}] (нет в экспорте)"
    text = m["text"] if m["text"].strip() else "(без текста)"
    return f"{head}{ctx}\n  {text}\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chat", required=True, help="папка экспорта с result.json")
    ap.add_argument("--root", type=int, required=True, help="id корня форум-топика")
    ap.add_argument("--work", required=True, help="куда писать корпус")
    ap.add_argument("--author", default=KRAS, help="эталонный автор для выжимки")
    ap.add_argument("--chunk", type=int, default=CHUNK_CHARS)
    args = ap.parse_args()

    os.makedirs(os.path.join(args.work, "chunks"), exist_ok=True)
    name, msgs = load(args.chat)
    json.dump(msgs, open(os.path.join(args.work, "messages.json"), "w", encoding="utf-8"), ensure_ascii=False)
    ordered = sorted(msgs.values(), key=lambda m: (m["date"], m["id"]))
    print(f"{name}: {len(ordered)} сообщений, {sum(len(m['text']) for m in ordered)} символов, "
          f"{ordered[0]['date'][:10]} - {ordered[-1]['date'][:10]}, авторов {len({m['from'] for m in ordered})}")

    chunks, cur, size, prev = [], [], 0, None
    for m in ordered:
        t = datetime.fromisoformat(m["date"])
        gap = (t - prev).total_seconds() if prev else 0
        if cur and (size >= args.chunk and gap >= GAP_SECONDS or size >= args.chunk * 1.4):
            chunks.append(cur)
            cur, size = [], 0
        cur.append(m)
        size += len(m["text"])
        prev = t
    if cur:
        chunks.append(cur)

    for old in glob.glob(os.path.join(args.work, "chunks", "chunk-*.txt")):
        os.remove(old)
    index = []
    for i, ch in enumerate(chunks, 1):
        path = os.path.join(args.work, "chunks", f"chunk-{i:02d}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {name} - кусок {i}/{len(chunks)}: сообщений {len(ch)}, "
                    f"{ch[0]['date'][:10]} - {ch[-1]['date'][:10]}\n\n")
            f.write("\n".join(render(m, msgs, args.root) for m in ch))
        index.append({"chunk": i, "ids": [m["id"] for m in ch], "from": ch[0]["date"], "to": ch[-1]["date"],
                      "chars": sum(len(m["text"]) for m in ch)})
        print(f"chunk-{i:02d}: {len(ch):5} сообщений, {sum(len(m['text']) for m in ch):7} символов текста, "
              f"{os.path.getsize(path):8} байт, {ch[0]['date'][:10]} - {ch[-1]['date'][:10]}")
    json.dump(index, open(os.path.join(args.work, "chunks", "index.json"), "w"), ensure_ascii=False)
    total = sum(len(c) for c in chunks)
    assert total == len(msgs), (total, len(msgs))
    print(f"всего {total} сообщений в {len(chunks)} кусках")

    replies = {}
    for m in ordered:
        if m["reply_to"] in msgs and m["reply_to"] != args.root:
            replies.setdefault(m["reply_to"], []).append(m)
    with open(os.path.join(args.work, "krasavchik.txt"), "w", encoding="utf-8") as f:
        n = 0
        for m in ordered:
            if m["from"] != args.author:
                continue
            n += 1
            f.write(render(m, msgs, args.root))
            for r in replies.get(m["id"], []):
                if r["from"] != args.author:
                    snip = r["text"][:SNIPPET].replace("\n", " ")
                    f.write(f"  ⤷ ответ [{r['id']}] {r['from']}: «{snip}»\n")
            f.write("\n")
    print(f"krasavchik.txt: {n} сообщений автора «{args.author}»")


if __name__ == "__main__":
    main()
