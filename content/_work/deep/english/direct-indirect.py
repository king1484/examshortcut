# Phase 2 deep content: english / direct-indirect. Idempotent (upsert by id). Run: py -3 direct-indirect.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report
from di_notes import S as SA
from di_questions import QS_DI, check_rules, RULES

TOPIC = "direct-indirect"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, SA)

QS = QS_DI()
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ---------------- written rule check: one defensible answer per item ----------------
errs = check_rules()
by_id = {q["id"]: q for q in QS}
for qid, need, ban, _correct in RULES:
    q = by_id[qid]
    opts = [o.strip().lower() for o in q["options"]]
    if len(set(opts)) != 4:
        errs.append(f"{qid}: options not 4 unique")
    ci = q["answer"]
    c = opts[ci]
    for n in need:
        if n not in c:
            errs.append(f"{qid}: keyed option lacks {n!r}")
    for b in ban:
        if b in c:
            errs.append(f"{qid}: keyed option contains banned {b!r}")
    for i, o in enumerate(opts):
        if i == ci:
            continue
        fails = [n for n in need if n not in o]
        hits = [b for b in ban if b in o]
        if not fails and not hits:
            errs.append(f"{qid}: distractor {i} also satisfies the signature")

if errs:
    print("RULE ERRORS:")
    for e in errs:
        print(" -", e)
    sys.exit(1)
print(f"rule check OK for {len(RULES)} items")

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Direct to indirect (statement)", "frequency": "very common", "subtopic": "narr-tense-shift",
  "howToSpot": "A declarative quote after said/said to; the options are that-clauses differing in the tense rung (was vs had been), in the time word (today vs that day), or in said-to vs told.",
  "approach": "Convert the frame first: said to + listener becomes told + listener, add that. Then step every verb one rung down the ladder (am → was, wrote → had written, will → would), map pronouns by SONA, and shift the time words (today → that day, tomorrow → the next day, ago → before). Universal truths keep their tense.",
  "example": {"q": "Select the indirect form: 'He said, \"I bought a car yesterday.\"'", "solution": "*He said that he **had bought** a car **the previous day*** — bought steps to had bought and yesterday to the previous day; I follows the reporter (he)."}},
 {"pattern": "Direct to indirect (question)", "frequency": "very common", "subtopic": "narr-questions-commands-exclamations",
  "howToSpot": "The quote ends with a question mark; the options differ in the connector (if/whether vs that vs the wh-word), in statement vs question order, and in whether do/does/did survived.",
  "approach": "Yes/No question → asked + if/whether + statement order. Wh-question → asked + the wh-word alone + statement order. Kill do/does/did and land the tense on the main verb (Do you like → if I liked). The final mark is a full stop, never a question mark.",
  "example": {"q": "Select the indirect form: 'The stranger said to me, \"Can you show me the way to the station?\"'", "solution": "*The stranger asked me **if I could show him** the way to the station* — one connector, statement order, can → could, you/me remapped by SONA."}},
 {"pattern": "Direct to indirect (command/request/exclamation)", "frequency": "very common", "subtopic": "narr-questions-commands-exclamations",
  "howToSpot": "The quote is an order (bare verb), a please-sentence, advice, or carries Hurrah/Alas/What a; the options differ in the reporting verb (ordered/requested/advised/exclaimed) and in the to/not-to frame.",
  "approach": "Order → told/ordered + object + to + V1 (negative: not to V1). Request → requested + object + to + V1. Advice → advised + object + to + V1. Exclamation → match the emotion: Hurrah → exclaimed with joy that; Alas → exclaimed with sorrow that; What a + adj → exclaimed that it was very + adj. The tone verb decides the item before any tense does.",
  "example": {"q": "Select the indirect form: 'Mother said to me, \"Do not go out in the rain.\"'", "solution": "*Mother told me **not to go** out in the rain* — a negative order rides not before to; the mother's concern keeps the neutral told frame."}},
 {"pattern": "Reverse conversion: indirect to direct", "frequency": "common", "subtopic": "narr-strategy",
  "howToSpot": "The stem is already reported (told/asked + that/if/wh) and the options are quoted sentences differing in the quotes-and-comma frame, in the un-shift, and in question order.",
  "approach": "Rebuild the frame (said to + listener, comma, quotes), drop the connector, step the tense UP one rung (had + V3 → V2, would → will, had to → must), reverse the pronouns (told me he → 'I'), and restore question order and the ? for questions. Universal truths need no un-shift.",
  "example": {"q": "Select the direct form: 'He asked me if I was hungry.'", "solution": "*He said to me, **'Are you hungry?'*** — if dissolves into an auxiliary-led question, was steps back to are, I returns to you, and the question mark returns."}},
 {"pattern": "Reporting verb choice: say vs tell and tone verbs", "frequency": "common", "subtopic": "narr-reporting-verb",
  "howToSpot": "Options that keep said to, drop the listener after told, or swap the tone verb (requested vs ordered vs advised) while the tenses are identical.",
  "approach": "said to + person → told + person (tell never takes to, say never takes a listener). Then match the tone: please → requested; command → ordered; advice → advised; suggestion → suggested; Hurrah/Alas → exclaimed with joy/sorrow. A present frame (says/has said) freezes the quote's tense.",
  "example": {"q": "Select the indirect form: 'She said to me, \"I am very busy today.\"'", "solution": "*She **told me** that she was very busy that day* — said to me must become told me; keeping 'said to me that...' is the planted fault, as is an objectless 'told that...'"}},
 {"pattern": "Backshift ladder and the no-shift exceptions", "frequency": "very common", "subtopic": "narr-tense-shift",
  "howToSpot": "Options differing only in the verb phrase (was learning / had been learning / is learning) or a universal truth offered with rose instead of rises.",
  "approach": "One rung down for a past frame: present → past, past → past perfect, past continuous → past perfect continuous, will/can/may → would/could/might, must (duty) → had to. Refuse both neighbours: the untouched present (half-backshift) and the double-step past perfect (over-backshift). Exceptions: universal truths, present reporting verbs, and frozen forms (would rather, used to, could have) do not move.",
  "example": {"q": "Select the indirect form: 'The teacher said, \"The earth revolves around the sun.\"'", "solution": "*The teacher said that the earth **revolves** around the sun* — a universal truth keeps the present even inside said; 'revolved' is the classic planted backshift."}},
 {"pattern": "Pronoun and time-word mapping (SONA + the time table)", "frequency": "very common", "subtopic": "narr-pronouns-time-place",
  "howToSpot": "Options differing only in pronouns (to me / to you / to him) or in the time word (tomorrow vs the next day; ago vs before) — often paired with a shifted or unshifted verb.",
  "approach": "SONA: first person follows the reporter, second person follows the listener, third person never changes — and track gender before his/her. Time table: tomorrow → the next day, yesterday → the previous day, ago → before, now → then, today → that day, next → the following, last → the previous; this → that, here → there, come → go. Tense and time words must move together — a half-shift is always the planted option.",
  "example": {"q": "Select the indirect form: 'He said, \"The minister will visit our town tomorrow.\"'", "solution": "*He said that the minister **would** visit our town **the next day*** — will and tomorrow move as a pair; shifting only one is the standard decoy."}},
]

save(TOPIC, data)
report(data, before, new_ids)
