# Phase 2 deep content: english / sentence-rearrangement. Idempotent (upsert by id).
# Run: py -3 sentence-rearrangement.py
# Written uniqueness proof: every item carries ordering constraints; this script enumerates all 24 orders and
# requires exactly one to satisfy them (the declared answer). Distractors are the nearest violating orders.
import sys, os, hashlib
from itertools import permutations
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report, QA
from rr_notes import S as SA
from rr_questions import ITEMS, PQRS, JUMBLE, FIRST, LAST

TOPIC = "sentence-rearrangement"
HEAD_PQRS = "Choose the correct order of the parts to make a meaningful sentence.\n\n"
HEAD_JUMBLE = "Rearrange the sentences P, Q, R and S to form a meaningful paragraph.\n\n"
HEAD_FIRST = "Sentences P, Q, R and S, when properly arranged, form a meaningful paragraph. Which sentence should come FIRST?\n\n"
HEAD_LAST = "Sentences P, Q, R and S, when properly arranged, form a meaningful paragraph. Which sentence should come LAST?\n\n"


def sat(order, c):
    """order: string over ABCD (logical ids); c: constraint token."""
    if c.startswith("^"):
        return order[0] == c[1]
    if c.endswith("$"):
        return order[-1] == c[0]
    if "-" in c:
        x, y = c.split("-")
        return order.index(x) + 1 == order.index(y)
    if "<" in c:
        x, y = c.split("<")
        return order.index(x) < order.index(y)
    raise ValueError(c)


def md5(s):
    return int(hashlib.md5(s.encode()).hexdigest(), 16)


data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}
apply_subtopics(data, SA)

errs = []
QS = []
num = Counter()
for it in ITEMS():
    num[it["sub"]] += 1
    qid = f"{it['sub']}-p{num[it['sub']]:02d}"
    lab = it["labels"]
    if sorted(lab) != list("PQRS") or len(it["parts"]) != 4:
        errs.append(f"{qid}: bad labels/parts")
        continue
    for c in it["cons"]:
        try:
            sat("ABCD", c)
        except Exception:
            errs.append(f"{qid}: bad constraint {c}")
    ok = ["".join(p) for p in permutations("ABCD") if all(sat("".join(p), c) for c in it["cons"])]
    if ok != ["ABCD"]:
        errs.append(f"{qid}: constraints admit {ok}")
        continue
    to_lab = dict(zip("ABCD", lab))
    by_label = {to_lab[k]: txt for k, txt in zip("ABCD", it["parts"])}
    body = " ".join(f"**{L}:** {by_label[L]}" for L in "PQRS")
    sol = it["sol"]
    for k in "ABCD":
        sol = sol.replace("{" + k + "}", f"**{to_lab[k]}**")
    sol = sol.replace("{ANS}", f"**{lab}**")
    if "{" in sol or "}" in sol:
        errs.append(f"{qid}: unrendered placeholder")
    kind = it["kind"]
    if kind in (PQRS, JUMBLE):
        if kind == PQRS:
            if not (it["s1"] and it["s6"]):
                errs.append(f"{qid}: PQRS item needs S1 and S6")
            q = HEAD_PQRS + f"**1.** {it['s1']} {body} **6.** {it['s6']}"
        else:
            q = HEAD_JUMBLE + body
        # distractors: violating orders, nearest first (constraints kept x2 + positions shared with the answer)
        cands = []
        for p in permutations("ABCD"):
            o = "".join(p)
            if o == "ABCD":
                continue
            score = 2 * sum(sat(o, c) for c in it["cons"]) + sum(a == b for a, b in zip(o, "ABCD"))
            cands.append((-score, md5(qid + o), "".join(to_lab[k] for k in o)))
        cands.sort()
        opts = [lab] + [c[2] for c in cands[:3]]
    else:
        q = (HEAD_FIRST if kind == FIRST else HEAD_LAST) + body
        ans = lab[0] if kind == FIRST else lab[-1]
        opts = [ans] + [L for L in "PQRS" if L != ans]
    QS.append(QA(qid, it["sub"], it["pat"], q, opts, sol, it["short"], it["diff"], it["t"]))

new_ids = {q["id"] for q in QS}
old_stems = {q["q"].strip().lower() for q in data["practice"] + data["solvedExamples"] if q["id"] not in new_ids}
for q in QS:
    if q["q"].strip().lower() in old_stems:
        errs.append(f"{q['id']}: stem duplicates an existing question")
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
 {"pattern": "PQRS rearrangement with fixed S1 and S6", "frequency": "very common", "subtopic": "rearr-pqrs-method",
  "howToSpot": "Sentence 1 and sentence 6 are given; the four middle parts are labelled P, Q, R, S and the options are four-letter strings.",
  "approach": "Read S1 and S6 first. Tag the parts (Lead, Support, Turn, Close), find the two strongest pairs, fix the first or last part, then remove every string that breaks a pair. Usually one string is left.",
  "example": {"q": "S1: Stubble burning chokes north India every winter. Parts: farmers burn the straw / the smoke drifts to the cities / this thick smog sends thousands to hospital / some states now pay for straw-cutting machines. S6: Subsidies for such machines must be extended.",
              "solution": "Cause -> 'The smoke' -> 'This thick smog' -> response; S6's 'such machines' puts the response part last."}},
 {"pattern": "Paragraph jumble (no fixed ends)", "frequency": "common", "subtopic": "rearr-strategy",
  "howToSpot": "Four to six sentences with no S1 or S6; options are letter strings.",
  "approach": "Find the one independent sentence (no pronoun, connector, 'this + noun' or 'also') — it opens. Attach pairs to it and put the summary or 'this + noun' sentence last.",
  "example": {"q": "P: Their numbers, however, have been falling. Q: Pesticides are the main reason for this decline. R: Farmers planting hedges are helping to reverse it. S: Honeybees help produce a third of our food.",
              "solution": "S is the only independent sentence -> P ('Their') -> Q ('this decline') -> R ('reverse it'): SPQR."}},
 {"pattern": "Opener: orphan test and the connector rule", "frequency": "very common", "subtopic": "rearr-openers-closers",
  "howToSpot": "Several parts begin with a pronoun, 'this + noun' or a connector; only one introduces a new noun.",
  "approach": "Read each part as if it came straight after S1. Remove the ones whose pronoun or 'this + noun' has nothing to refer to in S1. A However/But part may open only when it answers S1 itself.",
  "example": {"q": "S1: Many people believe that eating fat makes you fat. Which part follows S1: 'However, this belief is only partly true' or 'What it does not need is excess sugar'?",
              "solution": "'This belief' is S1's claim, so the However part follows S1; 'What it does not need' needs 'the body needs...' before it."}},
 {"pattern": "Closer: conclusion signal and S6 pull-back", "frequency": "very common", "subtopic": "rearr-openers-closers",
  "howToSpot": "One part carries therefore / hence / clearly, or S6 begins with a pronoun, 'such' or 'these'.",
  "approach": "Circle what S6 points back to — the part that supplies it is last. A part with a conclusion signal comes after everything it sums up.",
  "example": {"q": "S6: Such a response has encouraged the colony to open a reading corner. Which part is last: 'Within a month, two hundred people had borrowed books' or 'Volunteers arranged the books on these shelves'?",
              "solution": "'Such a response' = two hundred borrowers, so the borrowing part is last."}},
 {"pattern": "Mandatory pair (pronoun, a -> the, this + noun, contrast)", "frequency": "very common", "subtopic": "rearr-mandatory-pairs",
  "howToSpot": "Two parts are joined by a pointer: It/She/There, a bag -> the bag, this problem, Yet/But, also/others/too.",
  "approach": "Write each pair as a block (PS, SQ -> PSQ). Trust grammar links over topic links; two or three blocks usually leave one string.",
  "example": {"q": "Parts: 'the traveller left a small clay pot on the doorstep' / 'Inside the pot, the farmer found a bag of seeds'.",
              "solution": "'a small clay pot' -> 'the pot': the 'a' part must come directly before the 'the' part."}},
 {"pattern": "Time chain (markers, by-phrases, tense)", "frequency": "common", "subtopic": "rearr-time-sequence",
  "howToSpot": "Parts carry dates, 'later', 'that evening', 'By Wednesday morning', or mix past perfect with simple past.",
  "approach": "Place fixed dates in order; attach each relative marker to its anchor. By-phrases come after the actions they sum up. Past perfect parts are flashbacks; present tense ('Today') is last.",
  "example": {"q": "Parts: 'Within hours, trucks were stuck' / 'Army teams reached them that evening' / 'By Wednesday morning, a lane was cleared' / 'Later that day, vehicles were escorted down'.",
              "solution": "hours -> evening -> by Wednesday morning -> later that day."}},
 {"pattern": "Which sentence comes first / last", "frequency": "common", "subtopic": "rearr-strategy",
  "howToSpot": "Options are single labels (P, Q, R, S) and the question asks only for the first or the last sentence.",
  "approach": "First: the sentence that passes the orphan test (more general if two pass; check for hidden pointers like 'similarly'). Last: the sentence that points back to others but that nothing points back to.",
  "example": {"q": "P: He buried it in a hole. Q: A miser bought a lump of gold. R: Every night he dug it up. S: A thief, who had been watching him, stole the gold. Which is last?",
              "solution": "S — the thief had watched the nightly digging, and nothing refers back to the theft."}},
 {"pattern": "Odd sentence out", "frequency": "occasional", "subtopic": "rearr-strategy",
  "howToSpot": "Five sentences are given and one does not belong to the paragraph formed by the others.",
  "approach": "Build the chain of pairs among the sentences; the one that links to none of them (a new topic, or a different time and person) is the odd one.",
  "example": {"q": "Sentences on UPI payments, QR codes at stalls, scanning to pay, overspending — and one on the history of coins in the Mughal era.",
              "solution": "The Mughal-coins sentence has no pointer to or from the others and belongs to a different time — it is the odd one."}},
 {"pattern": "Sentence order inside a cloze / paragraph completion", "frequency": "occasional", "subtopic": "rearr-strategy",
  "howToSpot": "A paragraph has a missing sentence or a sentence to be placed at a gap; options are sentences or positions.",
  "approach": "Apply the same links: the missing sentence must pick up the pronoun or 'this + noun' after the gap and continue the idea before it.",
  "example": {"q": "Gap between 'Emails reach people in seconds.' and 'The handwriting brings the writer closer.'",
              "solution": "The gap needs a contrast that introduces what the handwriting explains: 'Yet a letter carries something a message cannot.'"}},
]

save(TOPIC, data)
report(data, before, new_ids)
ans_pos = Counter(q["answer"] for q in QS)
print("answer positions:", dict(ans_pos))
print("answer strings:", Counter(q["options"][q["answer"]] for q in QS if len(q["options"][q["answer"]]) == 4).most_common(5))
