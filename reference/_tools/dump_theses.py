#!/usr/bin/env python3
"""Печатает тезисы по категории для ручной склейки в правила.

  dump_theses.py --work <dir> --cat verify            # все тезисы категории
  dump_theses.py --work <dir> --cat verify --since 2025-07
  dump_theses.py --work <dir> --stats                 # сводка по категориям
  dump_theses.py --work <dir> --outcomes              # только тезисы с исходом
"""
import argparse
import collections
import json
import os


def load(work):
    with open(os.path.join(work, "theses.jsonl"), encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--cat")
    ap.add_argument("--since")
    ap.add_argument("--country")
    ap.add_argument("--author")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--outcomes", action="store_true")
    ap.add_argument("--grep")
    args = ap.parse_args()
    ts = load(args.work)

    if args.stats:
        by_cat = collections.Counter(t["category"] for t in ts)
        print(f"тезисов {len(ts)}, сообщений {len({t['msg_id'] for t in ts})}, авторов {len({t['author'] for t in ts})}")
        for cat, n in by_cat.most_common():
            sub = [t for t in ts if t["category"] == cat]
            res = collections.Counter(t["outcome"] for t in sub)
            fresh = sum(1 for t in sub if t["date"] >= "2025-07")
            authors = len({t["author"] for t in sub})
            print(f"{cat:12} {n:4}  авторов {authors:3}  свежих {fresh:4}  исходы: "
                  + ", ".join(f"{k}={v}" for k, v in res.most_common()))
        return

    sel = ts
    if args.cat:
        sel = [t for t in sel if t["category"] == args.cat]
    if args.since:
        sel = [t for t in sel if t["date"] >= args.since]
    if args.country:
        sel = [t for t in sel if t.get("country") == args.country]
    if args.author:
        sel = [t for t in sel if args.author.lower() in t["author"].lower()]
    if args.outcomes:
        sel = [t for t in sel if t.get("outcome") not in (None, "не проверено")]
    if args.grep:
        g = args.grep.lower()
        sel = [t for t in sel if g in t["claim"].lower() or g in t["quote"].lower()]

    for t in sel:
        extra = [t.get("state", ""), t.get("outcome", "")]
        if t.get("country"):
            extra.insert(0, t["country"])
        if t.get("stance") == "против":
            extra.append(f"против {t.get('against_msg')}")
        if t.get("reactions"):
            extra.append(t["reaction_detail"])
        print(f"[{t['msg_id']}] {t['date'][:10]} {t['author']} · {t['category']} · "
              + " · ".join(x for x in extra if x))
        print(f"   {t['claim']}")
        print(f"   «{t['quote']}»")
    print(f"--- {len(sel)} тезисов, авторов {len({t['author'] for t in sel})}, "
          f"сообщений {len({t['msg_id'] for t in sel})}")


if __name__ == "__main__":
    main()
