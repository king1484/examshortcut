"""Print the lesson fields (not practice) of a topic file, for rewrite sourcing."""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[3] / "core" / "topics" / "reasoning"
name = sys.argv[1]
t = json.loads((root / f"{name}.json").read_text(encoding="utf-8"))
for s in t["subtopics"]:
    print("#" * 100)
    print("SUBTOPIC", s["id"], "|", s.get("title"))
    for k in ["concept", "notes", "formulas", "tricks", "mistakes", "revision", "patterns"]:
        v = s.get(k)
        if v is None:
            continue
        print(f"\n----- {k} -----")
        print(json.dumps(v, ensure_ascii=False, indent=1))
