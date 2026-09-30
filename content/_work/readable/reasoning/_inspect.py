"""Dump structure of the 5 assigned reasoning topics (helper, not a rewrite)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[3] / "core" / "topics" / "reasoning"
for name in ["coding-decoding", "mathematical-operations", "statement-conclusion", "syllogism", "venn-diagrams"]:
    t = json.loads((root / f"{name}.json").read_text(encoding="utf-8"))
    print("=" * 12, name, "| title:", t["title"], "| subtopics:", len(t["subtopics"]))
    maxp = 0
    for s in t["subtopics"]:
        pats = s.get("patterns", [])
        ids = [p["id"] for p in pats]
        for i in ids:
            n = i.rsplit("-", 1)[-1]
            if n.isdigit():
                maxp = max(maxp, int(n))
        print(f"  {s['id']:34s} notes={len(s.get('notes','')):5d} concept={len(s.get('concept','')):4d} pats={len(pats):2d}")
        print(f"     pattern ids: {ids}")
        print(f"     keys: {sorted(s.keys())}")
    print("  MAX pattern number:", maxp)
    print("  practice:", len(t.get("practice", [])), "| solvedExamples:", len(t.get("solvedExamples", [])))
    # which patterns practice questions reference
    used = {}
    for q in t.get("practice", []):
        used.setdefault(q.get("pattern"), 0)
        used[q.get("pattern")] += 1
    print("  practice pattern refs:", used)
    print()
