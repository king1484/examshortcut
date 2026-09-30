"""Readable rewrite of GA > Physics (all 6 subtopics).

Content lives in _ph_a.py .. _ph_c.py (dict S per part). Facts are kept as in the previous notes.
Run: python physics.py  (patches content/core/topics/ga/physics.json in place; idempotent)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[2]
TOPIC = ROOT / "core" / "topics" / "ga" / "physics.json"

import _ph_a, _ph_b, _ph_c  # noqa: E402

S, FN = {}, {}
for part in (_ph_a, _ph_b, _ph_c):
    for k, v in part.S.items():
        assert k not in S, k
        S[k] = v
    FN.update(part.FNOTES)

data = json.loads(TOPIC.read_text(encoding="utf-8"))
by_id = {s["id"]: s for s in data["subtopics"]}
assert set(S) == set(by_id), (set(S) ^ set(by_id))
new_ids = [p["id"] for s in S.values() for p in s["patterns"]]
assert len(new_ids) == len(set(new_ids)), "duplicate pattern id"
for sid, new in S.items():
    sub = by_id[sid]
    old = {p["id"] for p in sub.get("patterns", [])}
    assert old <= {p["id"] for p in new["patterns"]}, (sid, old)
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sid, len(n))
    sub.update(concept=new["concept"], notes=n, patterns=new["patterns"], mistakes=new["mistakes"],
               revision=new["revision"], tricks=new["tricks"])
    notes = FN.get(sid, {})
    for f in sub.get("formulas", []):
        if f["name"] in notes and not f.get("note"):
            f["note"] = notes[f["name"]]
        elif f["name"] in notes and f["name"] in ("Kilowatt-hour",):
            pass
    print(f"{sid}: notes {len(n)} chars, {len(new['patterns'])} patterns (was {len(old)})")
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
