"""Shared builder: collects month modules m<YYYY>_<MM>.py and merges into content/core/current-affairs/<year>.json.

Each month module defines:
  ITEMS = [(date, category, headline, detail, [examFacts...]), ...]
  QUIZ  = [(q, [4 options], answer_index, solution, difficulty, pattern), ...]
Existing months in the JSON that we don't have a module for are kept untouched.
"""
import calendar
import glob
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
OUT_DIR = os.path.join(ROOT, "content", "core", "current-affairs")
CATS = {"national", "international", "economy", "sports", "awards", "appointments", "science",
        "defence", "environment", "schemes", "reports", "days", "obituaries", "books", "states"}


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_month(year, mm, mod):
    key = f"{year}-{mm:02d}"
    items = []
    for it in mod.ITEMS:
        date, cat, head, detail, facts = it
        assert cat in CATS, (key, cat, head)
        assert date.startswith(key), (key, date, head)
        assert 1 <= len(facts) <= 3, (key, head)
        items.append({"date": date, "category": cat, "headline": head, "detail": detail,
                      "examFacts": list(facts)})
    items.sort(key=lambda x: x["date"])
    quiz = []
    for i, q in enumerate(mod.QUIZ, 1):
        text, opts, ans, sol, diff, pat = q
        assert len(opts) == 4 and len(set(opts)) == 4, (key, text)
        assert 0 <= ans <= 3 and diff in ("easy", "medium", "hard") and pat in CATS, (key, text)
        quiz.append({"id": f"ca-{key}-q{i:02d}", "q": text, "options": list(opts), "answer": ans,
                     "solution": sol, "shortcut": None, "difficulty": diff, "subtopic": key,
                     "pattern": pat, "timeSec": 20})
    return {"month": key, "label": f"{calendar.month_name[mm]} {year}", "items": items, "quiz": quiz}


def build(year):
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"{year}.json")
    data = {"year": year, "months": []}
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            data = json.load(f)
    months = {m["month"]: m for m in data.get("months", [])}
    for path in sorted(glob.glob(os.path.join(HERE, f"m{year}_*.py"))):
        mm = int(os.path.basename(path)[6:8])
        m = build_month(year, mm, load(path))
        months[m["month"]] = m
    data = {"year": year, "months": [months[k] for k in sorted(months)]}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    with open(out, encoding="utf-8") as f:
        json.load(f)
    for m in data["months"]:
        print(m["month"], "items", len(m["items"]), "quiz", len(m["quiz"]))
