# Phase 2 deep content: english / active-passive. Idempotent (upsert by id). Run: py -3 active-passive.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report
from ap_notes import S as SA
from ap_questions import QS_AP, check_rules, RULES

TOPIC = "active-passive"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, SA)

QS = QS_AP()
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ---------------- written rule check: one defensible answer per item ----------------
errs = check_rules()  # correct option satisfies its own need/ban signature
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
 {"pattern": "Statement conversion: active to passive", "frequency": "very common", "subtopic": "ap-tense-tables",
  "howToSpot": "A declarative stem in the active voice with a transitive verb; the options are be + V3 skeletons that differ in the auxiliary chain, in being/been, or in agreement with the new subject.",
  "approach": "Name the active tense and say its passive row aloud (was writing → was being + V3). Promote the object to subject, rebuild the verb from the row, re-agree is/are/was/were/has/have with the NEW subject, and move the doer behind by in the object case. Then eliminate options by fault: wrong form after be, being/been swapped, tense row changed, agreement lost.",
  "example": {"q": "Select the passive form: 'The workers have painted the gate.'", "solution": "Present perfect row → has/have been + V3; new subject 'the gate' is singular: *The gate **has been painted** by the workers.* 'Have been painted' agrees with the old subject — the planted fault."}},
 {"pattern": "Statement conversion: passive to active", "frequency": "very common", "subtopic": "ap-passive-to-active",
  "howToSpot": "The stem already shows be/have been + V3 and asks for the active; the options differ in the active verb's tense (gave / has given / had given / gives).",
  "approach": "Ignore the participle — every passive row ends in V3. Read the FIRST auxiliary to fix the tense (had been → past perfect, was → simple past, is being → present continuous, will be → future). Promote the by-agent to subject; if there is no agent, start with They. Let the old subject exit in the object case (she → her, we → us).",
  "example": {"q": "Select the active form: 'The walls had been whitewashed by the masons.'", "solution": "had been + V3 → past perfect: *The masons **had whitewashed** the walls.* 'Have whitewashed' shifts the row to present perfect — the commonest decoy."}},
 {"pattern": "Imperative conversion: the Let structure", "frequency": "common", "subtopic": "ap-modals-imperatives",
  "howToSpot": "The stem is an order: a base verb with no subject ('Shut the door', 'Do not pluck the flowers'); the keyed option begins with Let.",
  "approach": "Use Let + object + be + V3 for the order; for a negative order put not after the object (Let the flowers not be plucked) or switch to a modal version (should not be plucked). Reject options without Let (they turn the order into a statement) and any form after be that is not V3.",
  "example": {"q": "Select the passive form: 'Switch off the mobile.'", "solution": "*Let the mobile **be switched off**.* 'Let the mobile switched off' drops be; 'The mobile is switched off' is a statement, not the order."}},
 {"pattern": "Request and advice frames", "frequency": "common", "subtopic": "ap-modals-imperatives",
  "howToSpot": "The stem carries please or kindly (request), advice in command form, or a warning (Do not drink and drive); the keyed option opens with You are requested / advised / warned.",
  "approach": "Swap the polite word for its frame — please/kindly → You are requested to, advice → You are advised to, danger → You are warned not to — and keep a base verb after to. The negative sits before to: requested **not to smoke**. Everything else in the sentence crosses unchanged.",
  "example": {"q": "Select the passive form: 'Please post this letter today itself.'", "solution": "*You are **requested to post** this letter today itself.* The letter cannot be made the requested party, and 'to posting' breaks the frame."}},
 {"pattern": "Interrogative conversions", "frequency": "common", "subtopic": "ap-modals-imperatives",
  "howToSpot": "The stem ends with a question mark; who, whom or what leads it. The options differ mainly in word order (By whom was... vs By whom the... was) and in who/whom choice.",
  "approach": "Decide the wh-word's job first. Doer (who) → By whom + auxiliary + new subject + V3, with question order (auxiliary before subject). Receiver (whom/what) → the wh-word itself is promoted to subject: Who was appointed by the manager? Check the order before the verb — order faults outnumber verb faults here.",
  "example": {"q": "Select the passive form: 'Who broke the window?'", "solution": "*By whom **was the window broken**?* 'By whom the window was broken?' is statement order; 'Who was broken the window' scrambles who did what."}},
 {"pattern": "Vague agent handling", "frequency": "common", "subtopic": "ap-basics",
  "howToSpot": "The stem's subject is someone, people, they or one; one option keeps 'by someone/by them' and the keyed one drops it; the rest of the sentence is identical.",
  "approach": "Vague agents add no information, so drop them; keep specific agents (the gardener, everyone, the committee). Dropping the agent never changes the tense row — convert first, drop last. If two options differ only in the by-phrase, the shorter (agent-less) one is keyed.",
  "example": {"q": "Select the passive form: 'Someone has switched off the fans.'", "solution": "*The fans **have been switched off**.* Present perfect row with the vague someone dropped; 'by someone' is grammatical but never the keyed answer."}},
 {"pattern": "being vs been slot trap", "frequency": "very common", "subtopic": "ap-tense-tables",
  "howToSpot": "Options identical except for the slot word: is being repaired / is been repaired / was being repaired — or the stem is continuous and one option lacks being altogether.",
  "approach": "being belongs only to continuous rows (is/are/was/were being + V3); been belongs only to perfect rows (has/have/had/will have been + V3); a modal takes plain be with neither. Fix the active tense first, then pick the slot word — never by ear, because is been and is being sound alike at speed.",
  "example": {"q": "Select the passive form: 'The engineers were repairing the bridge.'", "solution": "Past continuous → *The bridge **was being repaired*** — being marks the continuous; 'was been repaired' puts been in a continuous slot and is impossible."}},
 {"pattern": "Voice fault inside a sentence (error-spotting and improvement)", "frequency": "occasional", "subtopic": "ap-strategy",
  "howToSpot": "The item is not a conversion but a sentence with an embedded voice fault: is been built, must obeyed, by he, a plural new subject with has been, or a passive built from an objectless verb.",
  "approach": "Sweep for the four fault classes in order: (1) wrong verb form after be (V1/V2 where V3 belongs), (2) being/been in the wrong slot, (3) tense row changed or agreement lost with the new subject, (4) pronoun case or role reversal. The part that breaks a class is the error.",
  "example": {"q": "'The new scheme has being launched / by the government / without much publicity.' Find the error.", "solution": "Present perfect needs been, not being: has **been** launched. 'Has being launched' puts being in a perfect slot — the classic voice fault."}},
]

save(TOPIC, data)
report(data, before, new_ids)
