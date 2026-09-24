# Phase 2 deep content: english / error-spotting. Idempotent (upsert by id). Run: py -3 error-spotting.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, fill_group_passages, report
from es_notes_a import S as SA
from es_notes_b import S as SB
from es_questions_a import QS as QS_A
from es_questions_b import QS as QS_B
from es_questions_c import QS as QS_C

TOPIC = "error-spotting"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, SA)
apply_subtopics(data, SB)

QS = QS_A + QS_B + QS_C
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ES has no passage groups; run anyway for uniformity (copies 0 here)
added = fill_group_passages(data)
print("passages copied onto existing/new group members:", added)

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Subject-verb agreement error", "frequency": "very common", "subtopic": "es-sva",
  "howToSpot": "A verb separated from its subject by 'of...', 'as well as...', 'along with...'; one of / each of / neither of; either...or and neither...nor; a number of vs the number of.",
  "approach": "Cover the interrupting phrase with a finger and find the true subject; then match the verb's number. For or/nor pairs use the nearer subject; for one-of/each-of/every structures keep the verb singular no matter what plural noun follows.",
  "example": {"q": "'The number of accidents on this highway / have fallen / after the new signals were installed.' Find the error.", "solution": "'The number of' names a single count → singular: the number **has fallen**. The plural 'accidents' next to the verb is the decoy."}},
 {"pattern": "Tense and time-anchor error", "frequency": "very common", "subtopic": "es-tense",
  "howToSpot": "Time words sit in one part (ago, since 2019, by the time, as soon as, yesterday) while the verb in another part does not match them, or a when/if/until clause carries will.",
  "approach": "Circle every anchor word first, then check each verb against its anchor: ago and yesterday demand simple past; since + point and for + length; the earlier of two past events takes had + participle; a when/if/until clause about the future uses the simple present with no will.",
  "example": {"q": "'I will return your camera / as soon as / I will reach / home tomorrow.' Find the error.", "solution": "The as-soon-as clause takes the simple present: as soon as I **reach** home. Will belongs only in the main clause."}},
 {"pattern": "Verb form error (gerund vs infinitive)", "frequency": "very common", "subtopic": "es-verbs-structure",
  "howToSpot": "One verb follows another (denied to have, enjoys to, capable to handle) or a preposition is followed by to + verb (look forward to see).",
  "approach": "Recall the fixed group of the first word: enjoy, avoid, deny, suggest and every preposition take the -ing form; want, decide, agree, refuse take to + verb. 'Look forward to' ends in a preposition, so -ing follows it.",
  "example": {"q": "'She denied to have / taken the file, / but the register / proved otherwise.' Find the error.", "solution": "Deny takes -ing: she denied **having taken** the file. The infinitive after denied is the error."}},
 {"pattern": "Article error (a / an / the)", "frequency": "common", "subtopic": "es-article-preposition",
  "howToSpot": "The suspect part contains a/an/the before a noun, a superlative with a instead of the, or an abbreviation like MLA/ university where the first sound differs from the first letter.",
  "approach": "Say the next word aloud: vowel sound → an (an hour, an MLA), consonant sound → a (a university, a European). A superlative or a one-of-a-kind noun needs the; general plurals and meals need no article at all.",
  "example": {"q": "'She reached the hall / an hour late / because of / a MLA's convoy.' Find the error.", "solution": "MLA begins with the vowel sound 'em' → **an MLA's convoy**. Note that 'an hour' is correct because the h is silent."}},
 {"pattern": "Preposition pair error", "frequency": "very common", "subtopic": "es-article-preposition",
  "howToSpot": "A verb, adjective or noun sits next to a preposition that looks plausible but breaks its fixed pair: accused for, insist for, comply by, angry on, jump into conclusions.",
  "approach": "Treat the verb/adjective + preposition as one memorised chunk: accuse of, insist on, comply with, angry with (person), capable of, prefer to, jump to conclusions. Where two partners exist (apply to an office, apply for a post), the noun after the blank chooses.",
  "example": {"q": "'The coach did not agree / with the umpire's decision, / but he complied / by the rules.' Find the error.", "solution": "The frozen pair is comply **with**. 'Comply by' borrows the by of 'abide by' — that is the decoy."}},
 {"pattern": "Pronoun and connective error", "frequency": "common", "subtopic": "es-pronoun-conjunction",
  "howToSpot": "A subject-form pronoun after a preposition (between you and I), a relative clause with the wrong case (the lawyer who we met), its/it's, or a reported question welded to 'that' (asked that why, that whether).",
  "approach": "Objects after prepositions and after let take me/him/them. For who/whom, substitute he (→ who) or him (→ whom); possession is whose even for buildings. A reported question keeps only one connective: asked why, wanted to know whether.",
  "example": {"q": "'Mother wanted to know / that whether / I had locked / the back door.' Find the error.", "solution": "A reported yes/no question takes **whether** (or if) alone; 'that whether' stacks two connectives. The part to pick is 'that whether'."}},
 {"pattern": "Comparison error", "frequency": "common", "subtopic": "es-comparison-wordchoice",
  "howToSpot": "Double comparatives (more better), a superlative for exactly two items, a best without the, superior/senior with than, or a member compared with its own group without any other.",
  "approach": "One shape only (-er or more, never both). Two things take the comparative (the shorter of the two); Latin comparatives (superior, senior, junior, prior, preferable) take to; when a thing is compared with its own group, insert other/any other so it is not compared with itself.",
  "example": {"q": "'The summer of Nagpur / is harsher than / any city / in Maharashtra.' Find the error.", "solution": "Nagpur is itself a city of Maharashtra — it cannot be harsher than itself: harsher than **any other city** in Maharashtra."}},
 {"pattern": "Redundancy and word-choice error", "frequency": "common", "subtopic": "es-comparison-wordchoice",
  "howToSpot": "A doubled idea (returned back, repeat again, both of you two) or a swapped twin (advise for advice, effect for affect, loose for lose) in an otherwise clean sentence.",
  "approach": "Ask of each word whether a neighbour already says it — return, repeat and revert carry 'back/again' inside them, so cut the extra word. For twins, decide the job: advice (noun) vs advise (verb), affect (verb) vs effect (noun), lose (misplace) vs loose (not tight).",
  "example": {"q": "'This year's harvest / is more better / than the last one's, / thanks to the rains.' Find the error.", "solution": "'More better' doubles the comparative — better is already comparative. The part to pick is 'is more better'."}},
 {"pattern": "Question tag and structure error", "frequency": "occasional", "subtopic": "es-verbs-structure",
  "howToSpot": "A statement ends with a short tag (isn't it? after they have...) or a sentence mixes shapes in a list, uses would have inside an if-clause, or puts an adjective where an adverb belongs.",
  "approach": "The tag repeats the statement's helping verb, flips sign, and ends in a matching pronoun — hidden negatives (never, rarely, hardly) flip to a positive tag. In conditionals, would have never enters the if-clause; in lists, every item copies the first item's shape; action verbs take adverbs, linking verbs take adjectives.",
  "example": {"q": "'Suresh rarely / misses his morning walk, / doesn't he? / his neighbour asked.' Find the error.", "solution": "Rarely makes the statement negative, so the tag must be positive: **does he?** 'Doesn't he' fails to flip the sign."}},
]

save(TOPIC, data)
report(data, before, new_ids)
