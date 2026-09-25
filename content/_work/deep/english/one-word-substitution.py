# Phase 2 deep content: english / one-word-substitution. Idempotent (upsert by id). Run: py -3 one-word-substitution.py
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report
from ows_notes import S
from ows_questions import QS_OWS, TARGET

TOPIC = "one-word-substitution"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, S)

QS = QS_OWS()
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ---------------- no word asked twice (existing practice + solved + new practice) ----------------
EXISTING = {
    "eng-ows-p01": "bibliophile", "eng-ows-p02": "somniloquist", "eng-ows-p03": "democracy",
    "eng-ows-p04": "ambidextrous", "eng-ows-p05": "apiary", "eng-ows-p06": "fratricide",
    "eng-ows-p07": "extempore", "eng-ows-p08": "astronomer", "eng-ows-p09": "claustrophobia",
    "eng-ows-p10": "epitaph", "eng-ows-p11": "arbitrator", "eng-ows-p12": "pride (lions)",
    "eng-ows-p13": "omnipresent", "eng-ows-p14": "antidote", "eng-ows-p15": "inevitable",
}
SOLVED = {"eng-ows-s01": "regicide", "eng-ows-s02": "apiary", "eng-ows-s03": "antidote"}
errs = []
for q in data["practice"]:
    if q["id"] not in EXISTING and q["id"] not in TARGET:
        errs.append(f"no target recorded for {q['id']}")
allt = dict(EXISTING)
allt.update(TARGET)
c = Counter(allt.values())
for t, n in c.items():
    if n > 1:
        errs.append(f"word asked {n} times in practice: {t}")
for qid, t in TARGET.items():
    if t in SOLVED.values():
        errs.append(f"{qid}: repeats a solved-example word {t}")
# the target must appear in the question text or the correct option (guards a mis-typed target)
by_id = {q["id"]: q for q in data["practice"]}
for qid, t in TARGET.items():
    q = by_id[qid]
    key = t.split()[-1]
    if key not in q["q"].lower() and key not in q["options"][q["answer"]].lower():
        errs.append(f"{qid}: target {key!r} not found in the question or answer")
if errs:
    print("DEDUP ERRORS:")
    for e in errs:
        print(" -", e)
    sys.exit(1)
print(f"dedup OK: {len(allt)} distinct one-word substitutes across practice")

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "One who ... (person words)", "frequency": "very common", "subtopic": "ows-people-words",
  "howToSpot": "The stem begins 'One who...' or 'A person who...' and names a job, habit or nature; all four options are person words.",
  "approach": "Underline the exact detail in the stem — the object of the job (maps, children, dictionary) or the habit (drinks, wastes money, easily fooled). Then match the option that owns exactly that detail, and reject the partner word (widow/widower, miser/spendthrift) planted among the options.",
  "example": {"q": "Select the option that can substitute the given group of words: *One who eats too much*", "solution": "**Glutton**. Gullible (easily cheated) and spendthrift (wastes money) are other person words that describe different habits."}},
 {"pattern": "Killing words (-cide family)", "frequency": "very common", "subtopic": "ows-suffix-families",
  "howToSpot": "The stem says 'The killing of ...' and may or may not name a special victim (mother, brother, king, infant, race).",
  "approach": "Match the victim to its root: mater = mother, pater = father, frater = brother, geno = race. If no special victim is named, the general word homicide is right. All four options are usually -cide words, so the victim decides.",
  "example": {"q": "Select the option that can substitute the given group of words: *The killing of an infant*", "solution": "**Infanticide**. Genocide would need a whole race as the victim; homicide names no victim at all."}},
 {"pattern": "Fear and study words (-phobia / -logy)", "frequency": "very common", "subtopic": "ows-suffix-families",
  "howToSpot": "'An abnormal fear of ...' points to a -phobia word; 'The study of ...' or 'The science of ...' points to a -logy word.",
  "approach": "Fix the family first (fear or study), then match the root to the thing feared or studied: hydro = water, acro = heights, ornitho = birds, entomo = insects, seismo = earthquakes. Watch the entomology/etymology twin.",
  "example": {"q": "Select the option that can substitute the given group of words: *The study of birds*", "solution": "**Ornithology**. Entomology is insects — one letter group apart, which is exactly the confusion the examiner tests."}},
 {"pattern": "A place where ... / A group of ...", "frequency": "very common", "subtopic": "ows-places-collections",
  "howToSpot": "The stem names a stored thing or resident ('A place where bees are kept') or a collection ('A group of wolves').",
  "approach": "Find the key noun and recall its fixed partner: bees → apiary, grain → granary, coins → mint, monks → monastery, wolves → pack, lions → pride, islands → archipelago. Check the one-letter traps (apiary/aviary) and the partner-place traps (monastery/convent) before marking.",
  "example": {"q": "Select the option that can substitute the given group of words: *A place where birds are kept*", "solution": "**Aviary**. Apiary (bees) differs by one letter and is always planted beside it."}},
 {"pattern": "Government and rule words (-cracy / -archy)", "frequency": "common", "subtopic": "ows-government-science",
  "howToSpot": "'Government by ...' or 'Rule by ...' followed by the ruler — the people, the rich, officials, God, a king, nobody.",
  "approach": "Name the ruler in the stem and match it: people → democracy, rich → plutocracy, officials → bureaucracy, God → theocracy, one person → autocracy, a few → oligarchy, none → anarchy. The first part of each word names the ruler.",
  "example": {"q": "Select the option that can substitute the given group of words: *Government by officials*", "solution": "**Bureaucracy**. The ruler here is the office machinery, not the people (democracy) or the rich (plutocracy)."}},
 {"pattern": "Literary, speech and time words", "frequency": "common", "subtopic": "ows-government-science",
  "howToSpot": "The stem is about a poem, speech, tomb writing, life story, or about how often something happens.",
  "approach": "Decide what the writing does (mourns → elegy, praises → eulogy, marks a tomb → epitaph, own life → autobiography). For frequency apply the counting rule: -ennial counts years (biennial = every two years), -annual counts times per year (biannual = twice a year).",
  "example": {"q": "Select the option that can substitute the given group of words: *A speech praising a person who has died*", "solution": "**Eulogy**. It praises; an elegy mourns. The two are always planted together."}},
 {"pattern": "Medical words (anti- / -demic)", "frequency": "common", "subtopic": "ows-strategy",
  "howToSpot": "The stem is about a medicine (against poison, germs, pain) or about a disease's spread (one area, the whole world, always present).",
  "approach": "For medicines, fix the job: against poison → antidote, kills bacteria inside → antibiotic, cleans wounds outside → antiseptic, removes feeling → anaesthetic. For diseases fix the spread: one area now → epidemic, the world → pandemic, always in one area → endemic.",
  "example": {"q": "Select the option that can substitute the given group of words: *A disease spreading rapidly in one area*", "solution": "**Epidemic**. Pandemic would need many countries; endemic is the constant-presence word, not rapid spread."}},
 {"pattern": "Correctly spelt one-word substitute", "frequency": "occasional", "subtopic": "ows-strategy",
  "howToSpot": "The stem says 'Select the correctly spelt word ...' and all four options are the same word in different spellings.",
  "approach": "Recall the word from the meaning, then break it into syllables and check each part against the options. Watch the classic slips: ie/ei order, -ent/-ant endings, single or double letters (convalescent, atheist, obsolete).",
  "example": {"q": "Correctly spelt word for *one who walks in his sleep*: somnambulist / somnambulyst / somnabulist / somnambulast", "solution": "**Somnambulist** — somn (sleep) + ambul (walk) + ist. Only the -ist ending and the u after ambul are correct."}},
]

save(TOPIC, data)
report(data, before, new_ids)
