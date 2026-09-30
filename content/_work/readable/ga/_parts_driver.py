"""Shared driver: merge SUBS dicts from part modules into one topic JSON.

Only subtopics present in the parts are replaced, so a topic can be rewritten part by part.
Old pattern ids must all survive; notes are normalised to end with one newline.
"""
import importlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FIELDS = ("concept", "notes", "patterns", "mistakes", "revision", "tricks")


def run(topic_id, part_names):
    topic = ROOT / "core" / "topics" / "ga" / f"{topic_id}.json"
    subs = {}
    for name in part_names:
        if not (HERE / f"{name}.py").exists():
            print(f"(part {name} not written yet)")
            continue
        mod = importlib.import_module(name)
        for k, v in mod.SUBS.items():
            assert k not in subs, f"{k} defined twice"
            subs[k] = v
    data = json.loads(topic.read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in data["subtopics"]}
    assert set(subs) <= set(by_id), set(subs) - set(by_id)
    all_ids = [p["id"] for sid, s in by_id.items() for p in (subs[sid] if sid in subs else s)["patterns"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate pattern id in topic"
    for sid, new in subs.items():
        sub = by_id[sid]
        old = {p["id"] for p in sub.get("patterns", [])}
        assert old <= {p["id"] for p in new["patterns"]}, (sid, "lost pattern ids", old)
        new = dict(new, notes=new["notes"].strip() + "\n")
        sub.update({f: new[f] for f in FIELDS if f in new})
        print(f"{sid}: notes {len(new['notes'])} chars, {len(new['patterns'])} patterns (was {len(old)})")
    with open(topic, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    missing = set(by_id) - set(subs)
    if missing:
        print("not yet rewritten:", sorted(missing))
