# Phase 2 deep content: english / fill-in-the-blanks. Idempotent (upsert by id). Run: py -3 fill-in-the-blanks.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report
from fb_notes import S as SA
from fb_questions import QS_FB

TOPIC = "fill-in-the-blanks"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, SA)

QS = QS_FB()
new_ids = {q["id"] for q in QS}

# one-answer discipline: new stems must not repeat any existing stem, options must be 4 unique
old_stems = {q["q"].strip().lower() for q in data["practice"] + data["solvedExamples"] if q["id"] not in new_ids}
errs = []
for q in QS:
    if q["q"].strip().lower() in old_stems:
        errs.append(f"{q['id']}: stem duplicates an existing question")
    if len({o.strip().lower() for o in q["options"]}) != 4:
        errs.append(f"{q['id']}: options not 4 unique")
    if "(a)" in q["solution"] or "(b)" in q["solution"] or "option " in q["solution"].lower():
        errs.append(f"{q['id']}: solution references option letters")
if errs:
    print("ERRORS:", *errs, sep="\n - ")
    sys.exit(1)

upsert_list(data["practice"], QS)

data["pyqPatterns"] = [
 {"pattern": "Collocation blank (verb + noun)", "frequency": "very common", "subtopic": "fb-collocations",
  "howToSpot": "The blank is a verb before a noun such as attention, place, a mistake or a decision; the options are do / make / take / give / pay.",
  "approach": "Read the noun first and recall the fixed chunk: pay attention, take place, make a mistake, do harm, commit a crime. Say the whole chunk silently — only one option sounds natural with that noun.",
  "example": {"q": "The annual sports meet will ___ place in the second week of December.", "solution": "**take** place — the fixed chunk for an event happening; give, make and hold place are not idiomatic."}},
 {"pattern": "Collocation blank (adjective + noun / idiom)", "frequency": "common", "subtopic": "fb-collocations",
  "howToSpot": "The blank is an adjective before rain, escape, traffic or asleep, or it completes a frozen idiom (part and parcel, hold water); the options are near-synonyms.",
  "approach": "Fetch the fixed partner (heavy rain, narrow escape, fast asleep). Near-synonyms such as strong, thin or quick are planted because they mean almost the same thing but never partner the noun.",
  "example": {"q": "The bus driver had a ___ escape when the truck swerved into his lane.", "solution": "**narrow** escape — thin, slim and tight mean small but are not the partner of escape."}},
 {"pattern": "Confusable word (shape pair/triple)", "frequency": "very common", "subtopic": "fb-homonyms-confusables",
  "howToSpot": "The options are look-alikes: advice/advise, affect/effect, stationary/stationery, principal/principle, allusion/illusion.",
  "approach": "First work out which part of speech the slot needs (after a/the -> noun; after a subject, can or will -> verb), then the meaning (still vs paper, head vs rule). One clue word in the sentence always decides it.",
  "example": {"q": "Lack of sleep can seriously ___ a student's concentration.", "solution": "**affect** — a verb is needed after 'can', meaning influence; effect is usually the noun."}},
 {"pattern": "Phrasal verb blank", "frequency": "very common", "subtopic": "fb-phrasal-verbs",
  "howToSpot": "One verb (call, look, put, turn, give) is shown with the particle missing, or the options are four verb + particle combinations.",
  "approach": "Say the meaning the sentence needs in plain words (cancel, investigate, tolerate, postpone, emit), then choose the particle that gives that meaning. Watch for 'look forward to', where to is a preposition and takes V-ing.",
  "example": {"q": "Because of the cyclone warning, the fair was put ___ till next month.", "solution": "**off** — put off = postpone; 'till next month' confirms the delay."}},
 {"pattern": "Tense / verb-form blank", "frequency": "very common", "subtopic": "fb-verb-form-tense",
  "howToSpot": "Time anchors (since, for, by the time, when, if, had) surround the blank; the options are one verb in different tenses or forms.",
  "approach": "Circle the anchor. since/for -> perfect; earlier of two past events -> had + V3; if (type 1) -> simple present; Had + subject + V3 -> would have + V3; enjoy/deny -> V-ing; decide/refuse -> to + V1. Check agreement last (neither of / the number of -> singular).",
  "example": {"q": "Had she left home earlier, she ___ the flight.", "solution": "**would have caught** — the inverted type-3 condition needs would have + V3."}},
 {"pattern": "Connective / relative pronoun blank", "frequency": "very common", "subtopic": "fb-connectives-pronouns",
  "howToSpot": "The blank joins two clauses (although, because, yet) or a noun to a clause (who, whom, whose, which), or completes a hardly/no sooner frame.",
  "approach": "Name the relationship between the two sides (contrast, cause, result, time) and choose the connector with that meaning. Then check what follows: despite/because of take a noun, although/because take a clause. For pronouns: who = subject, whom = object or after a preposition, whose = possession.",
  "example": {"q": "The scientist to ___ the award was given belongs to Kerala.", "solution": "**whom** — a preposition needs the object form; 'to who' is ungrammatical."}},
 {"pattern": "Double blank (pair options)", "frequency": "common", "subtopic": "fb-double-blanks",
  "howToSpot": "Two blanks, and every option is a comma-joined pair: correlatives (neither, nor), fixed idioms (safe, sound) or range pairs (from, to).",
  "approach": "Test each whole pair in place. Remove pairs with mismatched partners first (neither ... or, hardly ... than). Then use the visible verb: both ... and takes a plural verb, while neither/either ... nor/or agree with the nearer subject. Read to the full stop before choosing.",
  "example": {"q": "___ the teachers ___ the principal was informed about the inspection.", "solution": "**Neither, nor** — the singular 'was' agrees with the nearer 'principal'; 'Both ... and' would need 'were'."}},
 {"pattern": "Correlative time frame (hardly / no sooner)", "frequency": "common", "subtopic": "fb-connectives-pronouns",
  "howToSpot": "The sentence opens with Hardly had, Scarcely had or No sooner had, and the blank is the second partner (or the auxiliary 'had').",
  "approach": "No sooner -> than; hardly / scarcely -> when. The first clause is in the past perfect (had + V3) and the second in the simple past. 'Then' is always a decoy.",
  "example": {"q": "No sooner had the rain stopped ___ the children ran out to play.", "solution": "**than** — the only partner of no sooner; 'when' belongs to hardly and scarcely."}},
]

save(TOPIC, data)
report(data, before, new_ids)
