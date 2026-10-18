#!/usr/bin/env python3
"""Проверка тезисов и сборка theses.jsonl для чатов без веток.

Запуск:
  validate_theses.py --work <dir> --schema bans [NN|all]

Проверяет: валидный JSON, msg_id существует и из своего куска, цитата - дословная
подстрока текста сообщения, категория/состояние/исход/позиция из словаря.
Автора, дату и реакции подставляет по messages.json.
"""
import argparse
import glob
import json
import os
import re
import sys

SCHEMAS = {
    "bans": {
        "category": {"register", "location", "network", "verify", "ban", "recover",
                     "activity", "multiacc", "premium", "jobsearch", "profile"},
        "state": {"новый", "чистый", "под верификацией", "забаненный", "любой"},
        "outcome": {"сработало", "не сработало", "частично", "не проверено"},
    },
    "taxes": {
        "category": {"status", "jurisdiction", "tax", "banking", "payments", "contract",
                     "employer", "risk", "relocation", "negotiation"},
        "state": {"в рф", "релокант", "уже за рубежом", "любой"},
        "outcome": {"сработало", "не сработало", "частично", "не проверено"},
    },
}
STANCES = {"за", "против"}


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def check_file(path, msgs, schema, chunk_ids=None):
    good, errors = [], []
    for ln, raw in enumerate(open(path, encoding="utf-8"), 1):
        raw = raw.strip()
        if not raw:
            continue
        try:
            t = json.loads(raw)
        except json.JSONDecodeError as e:
            errors.append(f"{ln}: не JSON ({e})")
            continue
        mid = str(t.get("msg_id"))
        m = msgs.get(mid)
        if not m:
            errors.append(f"{ln}: нет сообщения {mid}")
            continue
        if chunk_ids is not None and int(mid) not in chunk_ids:
            errors.append(f"{ln}: сообщение {mid} не из этого куска")
            continue
        errs = []
        q = norm(t.get("quote"))
        if not q or q not in norm(m["text"]):
            errs.append("quote не дословная подстрока текста сообщения")
        if len(q) > 300:
            errs.append(f"quote длиннее 300 символов ({len(q)})")
        for field in ("category", "state", "outcome"):
            if t.get(field) not in schema[field]:
                errs.append(f"{field}={t.get(field)!r}")
        if t.get("stance") not in STANCES:
            errs.append(f"stance={t.get('stance')!r}")
        if not norm(t.get("claim")):
            errs.append("пустой claim")
        if errs:
            errors.append(f"{ln}: msg {mid}: " + "; ".join(errs))
            continue
        t["quote"] = q
        t.update(author=m["from"], date=m["date"], reactions=m["reactions"],
                 reaction_detail=m["reaction_detail"])
        good.append(t)
    return good, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--schema", required=True, choices=sorted(SCHEMAS))
    ap.add_argument("what", nargs="?", default="all")
    args = ap.parse_args()
    work, schema = args.work, SCHEMAS[args.schema]
    msgs = json.load(open(os.path.join(work, "messages.json"), encoding="utf-8"))
    index = {c["chunk"]: set(c["ids"]) for c in json.load(open(os.path.join(work, "chunks", "index.json")))}

    if args.what != "all":
        n = int(args.what)
        good, errors = check_file(os.path.join(work, f"theses-{n:02d}.jsonl"), msgs, schema, index[n])
        covered = {int(t["msg_id"]) for t in good}
        print(f"кусок {n}: тезисов {len(good)}, сообщений с тезисами {len(covered)} из {len(index[n])}, ошибок {len(errors)}")
        print("\n".join(errors))
        sys.exit(1 if errors else 0)

    all_good, bad = [], 0
    for path in sorted(glob.glob(os.path.join(work, "theses-[0-9][0-9].jsonl"))):
        n = int(re.search(r"theses-(\d+)", path).group(1))
        good, errors = check_file(path, msgs, schema, index.get(n))
        bad += len(errors)
        print(f"{os.path.basename(path)}: тезисов {len(good)}, ошибок {len(errors)}")
        for e in errors:
            print("  ", e)
        all_good += good
    all_good.sort(key=lambda t: (t["date"], int(t["msg_id"])))
    for i, t in enumerate(all_good, 1):
        t["tid"] = f"T{i:04d}"
    with open(os.path.join(work, "theses.jsonl"), "w", encoding="utf-8") as f:
        for t in all_good:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    covered = {int(t["msg_id"]) for t in all_good}
    print(f"итого: тезисов {len(all_good)}, сообщений с тезисами {len(covered)}, "
          f"без тезисов {len(msgs) - len(covered)}, ошибок {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
