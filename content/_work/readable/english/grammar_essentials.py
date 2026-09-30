"""Readable rewrite of English > Grammar Essentials (all 8 subtopics).

Subtopic content lives in _ge_p1.py (parts of speech, tenses), _ge_p2.py, _ge_p3.py.
Run: python grammar_essentials.py          (patches content/core/topics/english/grammar-essentials.json)
     python grammar_essentials.py --check  (dry run, prints lengths only)
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "grammar-essentials.json"

from _ge_common import SUBS  # noqa: E402
import _ge_p1  # noqa: E402,F401
try:
    import _ge_p2  # noqa: E402,F401
    import _ge_p3  # noqa: E402,F401
except ImportError as e:
    print("missing part:", e)

CHECK = "--check" in sys.argv


def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


data = json.loads(TOPIC.read_text(encoding="utf-8"))
if not CHECK:
    assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
for sub in data["subtopics"]:
    if sub["id"] not in SUBS:
        continue
    new = SUBS[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in new["patterns"]]
    assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
    assert len(new_ids) == len(set(new_ids))
    n = new["notes"].strip() + "\n"
    print(sub["id"], "notes", len(n), "sections", len(re.findall(r"^### ", n, re.M)), "patterns", len(new_ids))
    if not (2500 <= len(n) <= 5000): print("  LENGTH OUT OF RANGE")
    assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
    for p in new["patterns"]:
        assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:90])
    if not CHECK:
        sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
                   revision=new["revision"], patterns=new["patterns"])
if not CHECK:
    all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
    assert len(all_ids) == len(set(all_ids)), "pattern id clash"
    TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written")
