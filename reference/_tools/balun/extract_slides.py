#!/usr/bin/env python3
"""Постраничная выгрузка PDF курса: текстовый слой без водяного знака + PNG каждой страницы.

usage: python3 -I extract_slides.py --pdf <file.pdf> --lesson 01 --out reference/balun-sd

Пишет:
  <out>/slides/<lesson>/page-NNN.png
  <out>/text/<lesson>-slides.raw.md   "## Слайд N" + текстовый слой; пометка, если слой пуст
                                      или на странице есть растровые картинки (их дочитывают по PNG)
"""
import argparse
import re
import subprocess
from pathlib import Path

WATERMARK = re.compile(r"^\s*СКАЧАНО С WWW\.SW\.BAND.*$", re.M | re.I)


def run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def pages(pdf: Path) -> int:
    m = re.search(r"^Pages:\s+(\d+)", run("pdfinfo", str(pdf)), re.M)
    return int(m.group(1))


def image_pages(pdf: Path) -> set[int]:
    out = run("pdfimages", "-list", str(pdf)).splitlines()[2:]
    return {int(line.split()[0]) for line in out if line.split()[2] == "image"}


def page_text(pdf: Path, n: int) -> str:
    txt = run("pdftotext", "-layout", "-f", str(n), "-l", str(n), str(pdf), "-")
    txt = WATERMARK.sub("", txt)
    lines = [l.rstrip() for l in txt.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True, type=Path)
    ap.add_argument("--lesson", required=True)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--dpi", default="110")
    a = ap.parse_args()

    png_dir = a.out / "slides" / a.lesson
    png_dir.mkdir(parents=True, exist_ok=True)
    run("pdftoppm", "-r", a.dpi, "-png", str(a.pdf), str(png_dir / "page"))
    # pdftoppm нумерует page-1/page-01/page-001 по числу страниц - приводим к NNN
    for p in png_dir.glob("page-*.png"):
        num = int(p.stem.split("-")[1])
        p.rename(png_dir / f"page-{num:03d}.png")

    n = pages(a.pdf)
    imgs = image_pages(a.pdf)
    out = [f"# Урок {a.lesson}: текстовый слой слайдов\n", f"Источник: `{a.pdf.name}`, страниц: {n}\n"]
    for i in range(1, n + 1):
        txt = page_text(a.pdf, i)
        flags = []
        if not txt:
            flags.append("НЕТ ТЕКСТОВОГО СЛОЯ")
        if i in imgs:
            flags.append("ЕСТЬ КАРТИНКА")
        flag = f"  <!-- {', '.join(flags)} -->" if flags else ""
        out.append(f"## Слайд {i}{flag}\n\n![](../slides/{a.lesson}/page-{i:03d}.png)\n\n{txt}\n")
    (a.out / "text").mkdir(parents=True, exist_ok=True)
    (a.out / "text" / f"{a.lesson}-slides.raw.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{a.lesson}: {n} pages, {len(imgs)} with images, "
          f"{sum(1 for i in range(1, n + 1) if not page_text(a.pdf, i))} empty")


if __name__ == "__main__":
    main()
