"""Smoke test for chem_part1 + chem_part2 before running the driver."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import check_strings
from chem_part1 import build_matter, build_periodic
from chem_part2 import build_acids, build_metals, build_organic

subs = [build_matter(), build_periodic(), build_acids(), build_metals(), build_organic()]
check_strings({"subtopics": [{"id": s.id, "notes": s.notes, "patterns": s.patterns, "practice": s.questions} for s in subs]})
print("check_strings OK")
tot = 0
for s in subs:
    n = len(s.notes)
    tot += n
    ids = [p["id"] for p in s.patterns]
    use = {}
    for q in s.questions:
        use[q["pattern"]] = use.get(q["pattern"], 0) + 1
    assert 2500 <= n <= 5000, (s.id, n)
    assert len(s.questions) >= 12, (s.id, len(s.questions))
    assert all(v >= 2 for v in use.values()), (s.id, use)
    assert len(set(ids)) == len(ids)
    print(f"{s.id:22s} notes={n:4d} pats={len(ids)} qs={len(s.questions)} use={sorted(use.values())}")
print(f"avg notes {tot // len(subs)}")
