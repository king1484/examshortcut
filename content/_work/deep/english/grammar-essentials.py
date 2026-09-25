# Phase 2 deep content: english / grammar-essentials. Idempotent (upsert by id). Run: py -3 grammar-essentials.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report
from ge_notes import S
from ge_questions import QS_GE

TOPIC = "grammar-essentials"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, S)

QS = QS_GE()
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ---------------- light structural check: old ids intact, stems unique per subtopic ----------------
old_ids = [q["id"] for q in data["practice"] if q["id"] not in new_ids]
expected_old = {"eng-grammar-p%02d" % i for i in range(1, 16)}
missing = expected_old - set(old_ids)
if missing:
    print("MISSING OLD IDS:", sorted(missing))
    sys.exit(1)
stems = set()
for q in QS:
    key = q["q"].split("  ")[-1].split("\n")[-1]
    if key in stems:
        print("duplicate stem:", q["id"])
        sys.exit(1)
    stems.add(key)
print(f"structure OK: {len(old_ids)} old ids intact, {len(QS)} new items, stems unique")

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Error spotting in divided sentence parts", "frequency": "very common", "subtopic": "ge-subject-verb-agreement",
  "howToSpot": "The sentence is split by slashes into four parts; one part holds a grammar fault and the other three are clean.",
  "approach": "Test the usual suspects in order: verb agreement with the real subject (cover of/as well as phrases), tense after signal words, article by sound, fixed preposition, modal + base verb. The part whose correction you can state is the error.",
  "example": {"q": "The principal, as well as the teachers, / were present / at the annual function / held last Friday.", "solution": "Cover 'as well as the teachers': subject = principal (singular) → 'were present' is the error; it should be **was present**."}},
 {"pattern": "Fill in the blank: verb form and tense", "frequency": "very common", "subtopic": "ge-tenses",
  "howToSpot": "A sentence with one blank where all four options are verb forms (V1/V2/V3, had been, has been, will be).",
  "approach": "Find the signal word (ago, since, tomorrow, as soon as, before) and decide whether the action is finished, running, or earlier than another action. Read the tense row off the signal, and never put will inside a time or if clause.",
  "example": {"q": "My uncle ___ in Canada since 2019.", "solution": "since + still living → present perfect continuous: **has been living**."}},
 {"pattern": "Sentence improvement (substitute the highlighted segment)", "frequency": "very common", "subtopic": "ge-modals-conditionals",
  "howToSpot": "A segment is printed in bold and the options are possible substitutes, often including 'No substitution required'.",
  "approach": "State the correct form first, then look for it among the options. If the bold segment is already right, choose no substitution — but only after testing agreement, tense sequence and modal + base verb rules.",
  "example": {"q": "If you **would have told** me earlier, I would have helped you.", "solution": "Third conditional if-clause takes had + V3: **had told**."}},
 {"pattern": "Question tag selection", "frequency": "common", "subtopic": "ge-comparison-question-tags",
  "howToSpot": "A full sentence with a trailing comma sits before the blank; the options are auxiliary + pronoun pairs.",
  "approach": "Copy the sentence's auxiliary, flip the polarity (positive sentence → negative tag), and replace the subject with its pronoun. For special sentences use the fixed tags: Let's → shall we, command → will you, I am → aren't I, nobody → they.",
  "example": {"q": "Nobody called while I was out, ___", "solution": "Nobody → they, and the clause is positive → **did they?**"}},
 {"pattern": "Choosing the grammatically correct sentence", "frequency": "common", "subtopic": "ge-comparison-question-tags",
  "howToSpot": "Four complete sentences differ in one grammar point each — comparison form, tag, preposition or verb form.",
  "approach": "Name the point under test and apply its rule to all four: one marker per comparison, than any other inside the group, fixed preposition pairs, no will in the if-clause. The sentence that survives every rule wins.",
  "example": {"q": "(a) Everest is highest peak... (b) Everest is higher than any other peak in the world. (c) Everest is more high... (d) Everest is the most higher...", "solution": "**(b)** — comparative + than any other, exactly one marker."}},
 {"pattern": "Fixed preposition and conjunction fill", "frequency": "very common", "subtopic": "ge-prepositions-conjunctions",
  "howToSpot": "The blank follows an adjective, noun or verb (fond, good, angry, insist) or completes a pair begun by no sooner / hardly / not only.",
  "approach": "Recall the governing word's fixed pair (fond of, good at, angry at a thing) or the correlative's partner (no sooner...than, hardly...when). Reject the preposition that fits the meaning generally but not this word.",
  "example": {"q": "She is not capable ___ handling the project alone.", "solution": "The fixed pair is capable **of** + V-ing."}},
 {"pattern": "Article and determiner choice", "frequency": "common", "subtopic": "ge-articles-determiners",
  "howToSpot": "The blank sits before a noun whose a/an/the/zero choice is tested — often hour, MLA, university, a superlative, or a school/meals context.",
  "approach": "Hear the first sound for a/an (an hour, an MLA; a university, a one-rupee coin). Check the the-triggers: second mention, unique things, superlatives, rivers, directions. Zero article with languages, meals and purpose-use nouns like school.",
  "example": {"q": "He waited for ___ hour at the bus stop.", "solution": "'Hour' begins with a silent h, vowel sound → **an** hour."}},
 {"pattern": "Word-form (part of speech) choice", "frequency": "common", "subtopic": "ge-parts-of-speech",
  "howToSpot": "All four options are forms of one family (succeed/success/successful/successfully) and the blank has a fixed slot job.",
  "approach": "Decide the job the slot needs: after the/of/his → noun; before a noun → adjective; after an action verb → adverb; after a modal → verb. Uncountables (advice, furniture, information) never take -s.",
  "example": {"q": "Hard work is the key to ___.", "solution": "Noun needed after 'the key to' → **success**."}},
 {"pattern": "Non-finites and inversion items", "frequency": "common", "subtopic": "ge-non-finites-inversion",
  "howToSpot": "Either the blank follows a set verb or preposition (avoid, enjoy, look forward to, made him), or the sentence opens with No sooner / Hardly / Never / Not only.",
  "approach": "Non-finites: preposition or gerund-list verb → V-ing; to-list verbs (promise, decide) → to + V1; make/let/see/hear → bare V1. Inversion: negative opener → auxiliary before subject, with the fixed partner than/when.",
  "example": {"q": "No sooner the bell rang / than the students / rushed out / of the classroom. Find the error.", "solution": "Negative opener needs inversion: 'No sooner **had the bell rung**' — the first part is the error."}},
]

save(TOPIC, data)
report(data, before, new_ids)
