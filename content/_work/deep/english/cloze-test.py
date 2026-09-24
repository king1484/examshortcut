# Phase 2 deep content: english / cloze-test. Idempotent (upsert by id). Run: py -3 cloze-test.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, fill_group_passages, report
from cloze_notes import S
from cloze_questions_a import QS as QS_A
from cloze_questions_b import QS as QS_B

TOPIC = "cloze-test"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, S)

QS = QS_A + QS_B
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# existing cross-subtopic groups: give every member the passage so per-subtopic quizzes work
added = fill_group_passages(data)
print("passages copied onto existing/new group members:", added)

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Verb form / tense blank", "frequency": "very common", "subtopic": "cloze-grammar-fit",
  "howToSpot": "The options are the same verb in different shapes (made/make/making) or tenses. Usually two or three of the five blanks in a passage are of this kind.",
  "approach": "Find the time anchor of the passage ('Last January', 'every morning', 'now') and keep only forms that stay inside that frame. Then check the subject: a singular subject needs the -s form in the present. A bare -ing form can never be the finite verb of a sentence.",
  "example": {"q": "'Last January the terrace became a workshop. Every evening he and his son (1) ______ new kites.' Options: made/make/making/maker.", "solution": "Past anchor 'Last January' + habitual 'every evening' → simple past: made. 'Make' breaks the frame; 'making' is not finite."}},
 {"pattern": "Connector blank (contrast / reason / addition / time)", "frequency": "very common", "subtopic": "cloze-connector-logic",
  "howToSpot": "The blank sits between two clauses, or at the start of a second sentence that comments on the first. Options are words like but, because, moreover, until.",
  "approach": "Compress each side of the blank into + or − (or cause/effect). Opposite directions → but/yet/although; a clause answering 'why' → because/since; a second supporting point after a semicolon → moreover; events on a clock → while/until/before. Then read the joined sentence aloud to confirm.",
  "example": {"q": "'Business has not suffered at all; (1) ______, some customers now order a second cup.' Options: however/therefore/moreover/otherwise.", "solution": "Both clauses push the same way and the punctuation asks for a linking adverb → moreover."}},
 {"pattern": "Preposition / phrasal verb blank", "frequency": "very common", "subtopic": "cloze-prepositions-phrasals",
  "howToSpot": "The options are single prepositions (to/for/on) or particles (off/up/out) after a verb, adjective or fixed phrase.",
  "approach": "Most of these blanks are fixed pairs: ashamed of, respond to, depend on, apply to (organisation) / for (post), in spite of, according to. For phrasal verbs, say the needed meaning in plain words first ('postpone' → put off), then match the particle.",
  "example": {"q": "'He is not ashamed (1) ______ his timetable.' Options: of/for/with/from.", "solution": "Fixed pair ashamed of → of. The other three do not exist with ashamed."}},
 {"pattern": "Noun / word choice by meaning", "frequency": "very common", "subtopic": "cloze-vocab-fit",
  "howToSpot": "All four options are grammatical in the blank; the sentence's meaning and the clue in a neighbouring clause must decide.",
  "approach": "Say the sentence's message in your own words, then keep the option that names exactly that idea. The clue is usually in the same sentence (often after a colon or semicolon); sometimes the next sentence confirms it. Cut options from the same broad field that do not match the precise idea.",
  "example": {"q": "'The quiet here has a different (1) ______ from the quiet of their homes, where the television mutters.' Options: price/quality/length/colour.", "solution": "The next clause describes the character of the quiet → quality."}},
 {"pattern": "Collocation blank (verb + fixed noun)", "frequency": "common", "subtopic": "cloze-vocab-fit",
  "howToSpot": "The blank completes a set phrase such as take advantage, make room, pay attention, keep a promise.",
  "approach": "Read the noun after the blank and recall its fixed partner verb. Do not translate from your mother tongue — the make/do/take swap is the classic trap. If two options seem possible, only the conventional partner is accepted in the exam.",
  "example": {"q": "'The students (1) ______ full advantage of the extended hours.' Options: make/do/take/give.", "solution": "take (full) advantage of — 'do advantage' and 'make advantage' are not English."}},
 {"pattern": "Subject-verb agreement blank", "frequency": "common", "subtopic": "cloze-grammar-fit",
  "howToSpot": "The options differ only in number or person (is/are, gives/give), and the sentence has a long phrase between the subject and the verb, or an each/every/one-of structure.",
  "approach": "Cross out the words between the true subject and the verb, find the subject's number, then match the verb and the passage's time frame. 'The soil in his yard ___ too rocky' → soil is singular → is.",
  "example": {"q": "'A group of volunteers ___ its own discipline.' Options: develop/develops/developing/had developed.", "solution": "True subject 'a group' is singular and the passage is in general present → develops."}},
 {"pattern": "Article / determiner blank", "frequency": "common", "subtopic": "cloze-grammar-fit",
  "howToSpot": "The options are a, an, the (or their capital forms) before a noun.",
  "approach": "First mention or one of many → a/an (an before a vowel sound). Already known, already specified by a phrase, or one of a kind → the. General plural or uncountable idea often needs no article, so reject both when the noun is generic.",
  "example": {"q": "'On festival day (1) ______ sky above the lane was full of kites.' Options: A/An/The/Some.", "solution": "'The sky above the lane' is one specific sky → The."}},
 {"pattern": "Word whose answer needs the whole passage (theme / local-fit traps)", "frequency": "common", "subtopic": "cloze-strategy",
  "howToSpot": "The options all fit the grammar and most fit the general topic; the correct one continues the passage's controlling idea, or the tempting one clashes with a line elsewhere.",
  "approach": "Read the full passage before answering and name its theme. Keep the option that stays inside the story's world and metaphor. Before finalising, re-read the passage with your answers — a locally fitting option that contradicts another line must go.",
  "example": {"q": "'The market sells food, but what it really (1) ______ is company.' Options: paints/sells/measures/imports.", "solution": "The passage's metaphor is selling → sells. The other verbs break the metaphor that runs through the whole passage."}},
]

save(TOPIC, data)
report(data, before, new_ids)
