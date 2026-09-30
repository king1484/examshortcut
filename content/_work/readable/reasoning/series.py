"""Rewrite reasoning/series.json (Phase 3 readable lessons). Run from repo root or anywhere."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from series_part1 import SERIES_IDEA, NUMBER_SERIES
from series_part2 import LETTER_SERIES, ALPHANUM, WRONG, LETTER_BLANK

TOPIC = Path(__file__).resolve().parents[4] / "content/core/topics/reasoning/series.json"
SUBS = {"series-idea": SERIES_IDEA, "number-series": NUMBER_SERIES, "letter-series": LETTER_SERIES,
        "alphanumeric-series": ALPHANUM, "wrong-number": WRONG, "letter-blank-series": LETTER_BLANK}

dfrac = lambda x: x.replace(r"\frac", r"\dfrac")
data = json.loads(TOPIC.read_text(encoding="utf-8"))
all_ids = [p_["id"] for s in SUBS.values() for p_ in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "duplicate pattern id"
for sub in data["subtopics"]:
    new = SUBS.pop(sub["id"])
    old_ids = {p_["id"] for p_ in sub.get("patterns", [])}
    new_ids = {p_["id"] for p_ in new["patterns"]}
    assert old_ids <= new_ids, (sub["id"], old_ids - new_ids)
    notes = new["notes"].strip() + "\n"
    assert 2500 <= len(notes) <= 5000, (sub["id"], len(notes))
    sub["concept"] = new["concept"]
    sub["notes"] = notes
    sub["patterns"] = new["patterns"]
    sub["mistakes"] = [{k: dfrac(v) for k, v in m_.items()} for m_ in new["mistakes"]]
    sub["revision"] = [dfrac(r) for r in new["revision"]]
    sub["tricks"] = new["tricks"]
    sub["formulas"] = new["formulas"]
    print(f"{sub['id']}: {len(notes)} chars, {len(new['patterns'])} patterns (was {len(old_ids)})")
assert not SUBS, list(SUBS)
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("series updated")
