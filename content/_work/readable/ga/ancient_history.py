"""Readable rewrite of GA > Ancient History (all 9 subtopics).

Content lives in _ah_p1.py .. _ah_p3.py (dict S per part). Facts are kept as in the previous notes.
Run: python ancient_history.py  (patches content/core/topics/ga/ancient-history.json in place; idempotent)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[2]
TOPIC = ROOT / "core" / "topics" / "ga" / "ancient-history.json"

import _ah_p1, _ah_p2, _ah_p3, _ah_p4  # noqa: E402

S = {}
for part in (_ah_p1, _ah_p2, _ah_p3, _ah_p4):
    for k, v in part.S.items():
        assert k not in S, k
        S[k] = v

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
    print(f"{sid}: notes {len(n)} chars, {len(new['patterns'])} patterns (was {len(old)})")
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
