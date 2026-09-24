# Phase 2 deep content: english / sentence-improvement. Idempotent (upsert by id). Run: py -3 sentence-improvement.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, fill_group_passages, report
from si_notes_a import S as SA
from si_notes_b import S as SB
from si_questions_a import QS as QS_A
from si_questions_b import QS as QS_B
from si_questions_c import QS as QS_C

TOPIC = "sentence-improvement"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, SA)
apply_subtopics(data, SB)

QS = QS_A + QS_B + QS_C
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# SI has no passage groups; run for uniformity
added = fill_group_passages(data)
print("passages copied onto existing/new group members:", added)

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Tense fix (anchor-based)", "frequency": "very common", "subtopic": "si-tense-sequence",
  "howToSpot": "The bold part is a verb and the sentence carries a visible time anchor — already, yesterday, by the time, every morning, since 2015.",
  "approach": "Circle the anchor and read off the required form: ago and yesterday demand simple past; the earlier of two past events takes had + participle; habits take the simple present; a since/for phrase with a continuing action takes has been -ing. Then reject options that shift tense again without a second event.",
  "example": {"q": "When I reached the station, the train (already left). Options: had already left / has already left / No substitution required / already leaves.", "solution": "The leaving happened before the reaching, so the earlier event takes the past perfect: had already left."}},
 {"pattern": "Agreement fix", "frequency": "very common", "subtopic": "si-agreement",
  "howToSpot": "The bold part holds a helper verb (was/were, has/have) sitting after an 'of…' phrase, an as-well-as phrase, or a one-of / each-of / neither-of opener.",
  "approach": "Cross out the interrupting phrase and find the true subject; match the helper to it and leave the participle untouched. For either…or and not only…but also, agree with the nearer subject; a number of takes a plural verb, the number of a singular one.",
  "example": {"q": "The captain, as well as the openers, (were) blamed for the collapse. Options: was / No substitution required / have been / are.", "solution": "'As well as' only adds information — the subject stays the captain: was blamed."}},
 {"pattern": "Reported-speech repair", "frequency": "common", "subtopic": "si-tense-sequence",
  "howToSpot": "A past reporting verb (asked, told, enquired, wanted to know) is followed by a bold part in question order, an unshifted tense, or 'that why / that whether'.",
  "approach": "Push the direct sentence through two machines: backshift the tense one step, and restore statement order (subject before helper). Keep exactly one connective — asked why, asked whether; 'that' never joins a wh-word.",
  "example": {"q": "The teacher asked the boy (why was he) late again. Options: why he was / No substitution required / why is he / that why he was.", "solution": "Indirect questions take statement order plus backshift: why he was late again."}},
 {"pattern": "Comparison repair", "frequency": "common", "subtopic": "si-comparison-structure",
  "howToSpot": "The bold part shows a doubled marker (more better), a bare place after 'than' (than Delhi), a Latin comparative with than (senior than), or the wrong degree for the announced count (the most useful of the two).",
  "approach": "Cut the doubled marker; compare like with like using that of / those of; give Latin comparatives and prefer their partner to; count the items — of the two takes the comparative, of all takes the superlative.",
  "example": {"q": "The streets of Mysuru are cleaner than (Bangalore). Options: those of Bangalore / that of Bangalore / No substitution required / Bangalore's streets.", "solution": "Streets must be compared with streets, plural: those of Bangalore."}},
 {"pattern": "Preposition / word-pair fix", "frequency": "very common", "subtopic": "si-precision-fixes",
  "howToSpot": "The bold part is a small word after a verb or adjective (approve for, insisted for) and the options swap prepositions, or the sentence contains an echo like revert back / repeat again.",
  "approach": "Treat verb + preposition as one memorised chunk — approve of, insist on, fond of, comply with — and pick the partner. For echoes, the repair is a subtraction: return, repeat and revert already contain the idea of back or again, so the correct option is the shorter one.",
  "example": {"q": "Please (revert back) to my mail by Friday. Options: revert to / No substitution required / revert back to / reversing to.", "solution": "Revert already means come back — cut the echo: revert to my mail."}},
 {"pattern": "Article / small-word fix", "frequency": "common", "subtopic": "si-precision-fixes",
  "howToSpot": "The bold part is an article + noun (a honest, an useful) or a single twin word in the wrong job (advise for advice, effect for affect).",
  "approach": "Say the next word aloud: vowel sound → an (an hour, an MLA), consonant sound → a (a university). For twins, decide the slot's part of speech: advice is the noun and advise the verb, affect the verb and effect the noun — then keep the change to one word.",
  "example": {"q": "The temple was built near (a ancient) trading route. Options: No substitution required / an ancient / a ancients / the ancients.", "solution": "Ancient begins with a vowel sound: an ancient trading route."}},
 {"pattern": "Inversion repair (no sooner / hardly / negative adverbs)", "frequency": "common", "subtopic": "si-structure-inversion",
  "howToSpot": "The sentence opens with No sooner, Hardly/Scarcely, Never or Seldom, and the bold part keeps statement order, uses the wrong partner (than vs when), or mismatches helper and verb.",
  "approach": "Recall the fixed frames: no sooner…THAN and hardly/scarcely…WHEN both force helper-first order (no sooner had he left / no sooner did he leave); fronted never and seldom invert with the helper or do-support (never have I seen, seldom do we see). Test order, partner word and helper-verb match as three separate checks.",
  "example": {"q": "No sooner (the train had left) the platform than the TTE began checking tickets. Options: had the train left / No substitution required / the train left / the train had leave.", "solution": "No sooner demands inversion: no sooner had the train left than…"}},
 {"pattern": "Dangling modifier / structure repair", "frequency": "occasional", "subtopic": "si-structure-inversion",
  "howToSpot": "The sentence begins with an -ing or being phrase whose doer is missing or impossible (Being a rainy day, the mela…; Having eaten our lunch, the train…), or a list and a not only…but also pair mix shapes.",
  "approach": "Ask who performs the opener's action; that doer must be the main subject, or the opener needs its own subject (It being a rainy day). For lists, make every item copy the first item's shape — uniform -ing items or paired adjectives.",
  "example": {"q": "(Being a rainy day), the mela was cancelled by the committee. Options: It being a rainy day / No substitution required / Being rainy day / Been a rainy day.", "solution": "The mela cannot be a rainy day: give the opener its own subject — It being a rainy day."}},
 {"pattern": "No-substitution discipline", "frequency": "common", "subtopic": "si-elimination",
  "howToSpot": "The bold part already passes every rule — a correct tense, a correct pair, a correct article — while every option quietly breaks one.",
  "approach": "Run the full check on the bold part before touching the options; if it survives its own rules, choose No substitution required without inventing work. Papers plant two or three correct originals per set to punish both the over-fixers and the blind pickers.",
  "example": {"q": "She (has been teaching) in this school since 2015. Options: teaches / is teaching / No substitution required / has taught.", "solution": "Perfect continuous with since 2015 and still continuing is exactly right: No substitution required."}},
]

save(TOPIC, data)
report(data, before, new_ids)
