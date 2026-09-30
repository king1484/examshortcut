"""Shared helpers for the computer-topic readable rewrites (Phase 3)."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # .../content
TOPICS = ROOT / "core" / "topics" / "computer"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


def apply(filename, SUBS):
    path = TOPICS / filename
    data = json.loads(path.read_text(encoding="utf-8"))
    assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
    bad = [(k, len(v["notes"].strip()) + 1) for k, v in SUBS.items() if not 2200 <= len(v["notes"].strip()) + 1 <= 5000]
    assert not bad, ("notes length out of range", bad)
    for sub in data["subtopics"]:
        new = SUBS[sub["id"]]
        old_ids = {p["id"] for p in sub.get("patterns", [])}
        new_ids = [p["id"] for p in new["patterns"]]
        assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
        assert len(new_ids) == len(set(new_ids)), sub["id"]
        n = new["notes"].strip() + "\n"
        assert 2200 <= len(n) <= 5000, (sub["id"], len(n))
        assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
        for p in new["patterns"]:
            assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
        for ln in long_lines(n + "\n" + new["concept"]):
            print("  long:", sub["id"], ln[:90])
        sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
                   revision=new["revision"], patterns=new["patterns"])
    all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
    assert len(all_ids) == len(set(all_ids)), "pattern id clash"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    for s in data["subtopics"]:
        print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
