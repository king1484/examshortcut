# Phase 2 deep content: english / spelling. Idempotent (upsert by id).
# Run: py -3 spelling.py
# Correctness guard: each item's correct option must be in CANON (hand-checked standard spellings, valid in
# both British and US English); no distractor may be a CANON word or a dictionary-listed variant (VARIANTS).
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report, QA
from sp_notes import S as SA
from sp_questions import ITEMS, CANON, VARIANTS, C, W, S, PL

TOPIC = "spelling"
STEM = {C: "Select the correctly spelt word.", W: "Select the wrongly spelt word."}
T = {"easy": 25, "medium": 35, "hard": 45}

data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}
apply_subtopics(data, SA)

errs = []
QS = []
num = Counter()
for sub, pat, kind, extra, opts, sol, short, diff in ITEMS:
    num[sub] += 1
    qid = f"{sub}-p{num[sub]:02d}"
    if kind == C:
        q = STEM[C]
        if opts[0].lower() not in CANON:
            errs.append(f"{qid}: answer not canonical")
        for o in opts[1:]:
            if o.lower() in CANON or o.lower() in VARIANTS:
                errs.append(f"{qid}: distractor {o} is a real spelling")
    elif kind == W:
        q = STEM[W]
    elif kind == S:
        q = "Identify the misspelt word in the following sentence.\n\n*" + extra + "*"
        words = {w.strip(".,").lower() for w in extra.split()}
        for o in opts:
            if o.lower() not in words:
                errs.append(f"{qid}: option {o} not in sentence")
    elif kind == PL:
        q = f"Select the correct plural of '{extra}'."
        for o in opts[1:]:
            if o.lower() in VARIANTS:
                errs.append(f"{qid}: distractor {o} is an accepted plural")
    QS.append(QA(qid, sub, pat, q, opts, sol, short, diff, T[diff]))

new_ids = {q["id"] for q in QS}
old_keys = {(q["q"].strip().lower(), tuple(sorted(o.lower() for o in q["options"])))
            for q in data["practice"] + data["solvedExamples"] if q["id"] not in new_ids}
old_words = {q["options"][q["answer"]].lower() for q in data["practice"] + data["solvedExamples"]
             if q["id"] not in new_ids and q.get("options")}
for q in QS:
    if (q["q"].strip().lower(), tuple(sorted(o.lower() for o in q["options"]))) in old_keys:
        errs.append(f"{q['id']}: duplicates an existing question")
    if q["q"] == STEM[C] and q["options"][q["answer"]].lower() in old_words:
        errs.append(f"{q['id']}: answer word already tested")
    if len({o.strip().lower() for o in q["options"]}) != 4:
        errs.append(f"{q['id']}: options not 4 unique")
    low = q["solution"].lower()
    if "(a)" in low or "(b)" in low or "option " in low:
        errs.append(f"{q['id']}: solution references option letters")
if errs:
    print("ERRORS:", *errs, sep="\n - ")
    sys.exit(1)

upsert_list(data["practice"], QS)

data["pyqPatterns"] = [
 {"pattern": "Choose the correctly spelt word", "frequency": "very common", "subtopic": "spell-strategy",
  "howToSpot": "Four spellings of one word; find the correct one.",
  "approach": "Find the differing letter-spot, apply the relevant rule (c-test, stress-doubling, suffix family), else recall from the bank.",
  "example": {"q": "Select the correctly spelt word: Accommodation / Accomodation / Acommodation / Accommodasion",
              "solution": "Accommodation — the options differ only in the doubles; the word needs both cc and mm."}},
 {"pattern": "Find the wrongly spelt word", "frequency": "common", "subtopic": "spell-strategy",
  "howToSpot": "Four different words are given; one of them is misspelt.",
  "approach": "Check each word against its doubles, ie/ei pair, ending and silent letters. Three pass; the one that fails is the answer.",
  "example": {"q": "Select the wrongly spelt word: Existance / Occasion / Believe / Truly",
              "solution": "Existance — exist goes with existent, so the noun is existence."}},
 {"pattern": "Spelling inside a sentence", "frequency": "occasional", "subtopic": "spell-strategy",
  "howToSpot": "A sentence is given and four of its words are the options; one is misspelt.",
  "approach": "Ignore the meaning and check each listed word on its own. British forms (colour, organised) are correct in Indian exams.",
  "example": {"q": "The committee could not reach a concensus on the budget.",
              "solution": "concensus -> consensus (related to consent)."}},
 {"pattern": "Plural/derived form spelling", "frequency": "occasional", "subtopic": "spell-strategy",
  "howToSpot": "The question asks for the plural of a Latin or Greek noun, or for a derived form of a given word.",
  "approach": "Classical plurals: -on -> -a, -is -> -es, -us -> -i, -um -> -a. Never add -s to a plural that is already classical (criterias).",
  "example": {"q": "Select the correct plural of 'analysis'.",
              "solution": "analyses — -is becomes -es, as in crisis -> crises."}},
 {"pattern": "ie or ei (the c-test)", "frequency": "very common", "subtopic": "spell-ie-rule",
  "howToSpot": "The options differ only in the order of i and e.",
  "approach": "Say the word. 'ee' sound: ie, but ei straight after c. 'ay' sound: ei. Check the exception list (seize, weird, foreign, leisure). c sounding 'sh' keeps ie (efficient, species).",
  "example": {"q": "Perceive / Percieve / Perceeve / Persieve",
              "solution": "Perceive — the 'ee' pair follows c, so ei."}},
 {"pattern": "Doubling before a suffix (stress rule)", "frequency": "common", "subtopic": "spell-doubling",
  "howToSpot": "The options differ in whether the last consonant of the base is doubled before -ed, -ing, -able or -ance.",
  "approach": "Double only if the last syllable of the base is stressed and the suffix starts with a vowel: regrettable, forgotten. Otherwise do not: budgeted, galloped.",
  "example": {"q": "Budgeted / Budgetted / Buddgeted / Budgeeted",
              "solution": "Budgeted — the stress is on BUD-, so the t stays single."}},
 {"pattern": "Suffix family (-ance/-ence, -able/-ible, final e)", "frequency": "common", "subtopic": "spell-suffix-endings",
  "howToSpot": "The options differ only in the last few letters.",
  "approach": "Match -ance with -ant and -ence with -ent; complete-word stems take -able; drop a final e before a vowel suffix except after soft c or g (noticeable).",
  "example": {"q": "Perseverance / Perseverence / Perseverrance / Persevearance",
              "solution": "Perseverance — persevere + ance, with one r."}},
 {"pattern": "Silent letters and -ceed/-cede words", "frequency": "common", "subtopic": "spell-trap-words",
  "howToSpot": "The word has a silent letter (Wednesday, psychology) or ends in the 'seed' sound.",
  "approach": "Recall the silent letter by saying the word as spelt. Only proceed, succeed and exceed end in -ceed; only supersede ends in -sede; the rest end in -cede.",
  "example": {"q": "Supersede / Superseed / Supersead / Superceed",
              "solution": "Supersede — the only -sede verb."}},
]

save(TOPIC, data)
report(data, before, new_ids)
print("answer positions:", dict(Counter(q["answer"] for q in QS)))
print("difficulty:", dict(Counter(q["difficulty"] for q in QS)))
