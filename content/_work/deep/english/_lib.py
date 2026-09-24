# Shared helpers for the English deep-content build scripts.
import json, os, re, sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TOPICS = os.path.join(ROOT, "content", "core", "topics", "english")

CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
BANNED = re.compile(r"https?://|www\.|Source:|Testbook|Adda|Oliveboard|BYJU|Kiran|Arihant|IndiaBix|Wren|Neetu", re.I)


def load(topic):
    with open(os.path.join(TOPICS, topic + ".json"), encoding="utf-8") as f:
        return json.load(f)


def save(topic, data):
    with open(os.path.join(TOPICS, topic + ".json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")


def Q(id, sub, pat, q, options, answer, solution, shortcut=None, diff="medium", t=45, passage=None, group=None):
    d = {"id": id, "q": q, "figure": None, "options": options, "answer": answer, "solution": solution,
         "shortcut": shortcut, "difficulty": diff, "subtopic": sub, "pattern": pat, "timeSec": t}
    if group:
        d["group"] = group
    if passage:
        d["passage"] = passage
    return d


def P(id, name, freq, spot, logic, eq, es):
    return {"id": id, "name": name, "frequency": freq, "howToSpot": spot, "formula": None, "logic": logic,
            "example": {"q": eq, "solution": es}}


def upsert_list(lst, items, key="id"):
    idx = {x[key]: i for i, x in enumerate(lst)}
    for it in items:
        if it[key] in idx:
            lst[idx[it[key]]] = it
        else:
            idx[it[key]] = len(lst)
            lst.append(it)


def apply_subtopics(data, subs):
    """subs: {sub_id: {notes, patterns, [full new subtopic fields]}}. Adds new subtopics if missing."""
    existing = {s["id"]: s for s in data["subtopics"]}
    for sid, add in subs.items():
        if sid in existing:
            s = existing[sid]
            for k, v in add.items():
                if k in ("id", "title", "concept", "formulas", "tricks", "mistakes") and k in s:
                    continue  # never overwrite existing core fields
                s[k] = v
        else:
            s = {"id": sid}
            s.update(add)
            data["subtopics"].append(s)
            existing[sid] = s


def fill_group_passages(data):
    """Copy a group's passage onto members that lack it, so per-subtopic quizzes (which filter by subtopic)
    still show the passage when a group spans several subtopics."""
    added = 0
    for arr in ("practice", "solvedExamples"):
        by = {}
        for q in data.get(arr, []):
            if q.get("group") and q.get("passage"):
                by.setdefault(q["group"], q["passage"])
        for q in data.get(arr, []):
            if q.get("group") and not q.get("passage") and q["group"] in by:
                q["passage"] = by[q["group"]]
                added += 1
    return added


def walk_strings(o, path=""):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from walk_strings(v, path + "." + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk_strings(v, f"{path}[{i}]")


def check(data, new_ids, notes_range=(2500, 5000)):
    errs = []
    subs = [s["id"] for s in data["subtopics"]]
    pat_ids = []
    for s in data["subtopics"]:
        n = len(s.get("notes", ""))
        if not (notes_range[0] <= n <= notes_range[1]):
            errs.append(f"{s['id']}: notes length {n}")
        ps = s.get("patterns", [])
        if not (4 <= len(ps) <= 8):
            errs.append(f"{s['id']}: {len(ps)} patterns")
        for p in ps:
            pat_ids.append(p["id"])
            for k in ("id", "name", "frequency", "howToSpot", "logic", "example"):
                if not p.get(k):
                    errs.append(f"pattern {p.get('id')} missing {k}")
            if p["frequency"] not in ("very common", "common", "occasional"):
                errs.append(f"pattern {p['id']} bad frequency")
        if "###" in s.get("notes", "") and re.search(r"^#{1,2} ", s["notes"], re.M):
            errs.append(f"{s['id']}: notes use h1/h2")
        if "### Quick revision" not in s.get("notes", ""):
            errs.append(f"{s['id']}: notes lack '### Quick revision'")
    if len(set(pat_ids)) != len(pat_ids):
        errs.append("duplicate pattern ids")
    pat_set = set(pat_ids)
    pat_of_sub = {p["id"]: s["id"] for s in data["subtopics"] for p in s.get("patterns", [])}
    allq = data["solvedExamples"] + data["practice"]
    ids = [q["id"] for q in allq]
    if len(set(ids)) != len(ids):
        errs.append("duplicate question ids: " + str([i for i, c in Counter(ids).items() if c > 1]))
    texts = Counter()
    for q in data["practice"]:
        if q["id"] not in new_ids:
            continue
        if len(q["options"]) != 4 or len(set(o.strip().lower() for o in q["options"])) != 4:
            errs.append(f"{q['id']}: options not 4 unique")
        if not (isinstance(q["answer"], int) and 0 <= q["answer"] <= 3):
            errs.append(f"{q['id']}: bad answer")
        if q["subtopic"] not in subs:
            errs.append(f"{q['id']}: bad subtopic")
        if q["pattern"] not in pat_set:
            errs.append(f"{q['id']}: pattern {q['pattern']} not a pattern id")
        elif pat_of_sub[q["pattern"]] != q["subtopic"]:
            errs.append(f"{q['id']}: pattern {q['pattern']} belongs to {pat_of_sub[q['pattern']]}")
        if q["difficulty"] not in ("easy", "medium", "hard"):
            errs.append(f"{q['id']}: bad difficulty")
        texts[(q.get("passage") or "")[:0] + q["q"] + "|" + "|".join(q["options"])] += 1
    for k, c in texts.items():
        if c > 1:
            errs.append("duplicate question text: " + k[:80])
    # groups: first member carries passage, all members share a subtopic (new groups)
    groups = defaultdict(list)
    for q in data["practice"]:
        if q.get("group"):
            groups[q["group"]].append(q)
    for g, qs in groups.items():
        if not qs[0].get("passage"):
            errs.append(f"group {g}: first member lacks passage")
    # pattern usage by NEW practice questions
    use = Counter(q["pattern"] for q in data["practice"] if q["id"] in new_ids)
    for p in pat_ids:
        if use[p] < 2:
            errs.append(f"pattern {p} used by {use[p]} new practice questions")
    per_sub = Counter(q.get("subtopic") for q in data["practice"])
    for s in subs:
        if per_sub[s] < 12:
            errs.append(f"{s}: only {per_sub[s]} practice questions")
    for path, sv in walk_strings(data):
        if CTRL.search(sv):
            errs.append(f"control char at {path}")
        if BANNED.search(sv):
            errs.append(f"banned text at {path}: {BANNED.search(sv).group(0)}")
    return errs, use, per_sub


def report(data, before, new_ids):
    errs, use, per_sub = check(data, new_ids)
    print(f"\n{data['id']}: subtopics {before['subs']} -> {len(data['subtopics'])}, practice {before['practice']} -> {len(data['practice'])}, pyqPatterns {len(data['pyqPatterns'])}")
    print(f"{'subtopic':32} {'notes':>6} {'pats':>4} {'practice':>8}")
    tot = 0
    for s in data["subtopics"]:
        n = len(s.get("notes", ""))
        tot += n
        print(f"{s['id']:32} {n:>6} {len(s.get('patterns', [])):>4} {per_sub[s['id']]:>8}")
    print("notes avg:", tot // len(data["subtopics"]))
    diff = Counter(q["difficulty"] for q in data["practice"] if q["id"] in new_ids)
    print("new question difficulty mix:", dict(diff))
    print("pattern usage (new):", dict(use))
    if errs:
        print("\nERRORS:")
        for e in errs:
            print(" -", e)
        sys.exit(1)
    print("checks OK")


def autopos(qid):
    import hashlib
    return int(hashlib.md5(qid.encode()).hexdigest(), 16) % 4


def QA(id, sub, pat, q, opts, solution, shortcut=None, diff="medium", t=45, passage=None, group=None, answer=None):
    """opts[0] is the correct option unless `answer` is given; it is moved to a deterministic position."""
    if answer is None:
        pos = autopos(id)
        o = list(opts[1:])
        o.insert(pos, opts[0])
        return Q(id, sub, pat, q, o, pos, solution, shortcut, diff, t, passage, group)
    return Q(id, sub, pat, q, list(opts), answer, solution, shortcut, diff, t, passage, group)
