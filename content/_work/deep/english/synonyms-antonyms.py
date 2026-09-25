# Phase 2 deep content: english / synonyms-antonyms. Idempotent (upsert by id). Run: py -3 synonyms-antonyms.py
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report
from sa_notes import S
from sa_questions import QS_SA, TARGET

TOPIC = "synonyms-antonyms"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len(data["practice"])}

apply_subtopics(data, S)

QS = QS_SA()
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ---------------- no headword asked twice (existing practice + solved + new practice) ----------------
EXISTING = {
    "eng-sa-p01": "abundant", "eng-sa-p02": "futile", "eng-sa-p03": "imminent",
    "eng-sa-p04": "notorious", "eng-sa-p05": "indispensable", "eng-sa-p06": "mitigate",
    "eng-sa-p07": "vigilant", "eng-sa-p08": "squander", "eng-sa-p09": "tenacious",
    "eng-sa-p10": "lucid", "eng-sa-p11": "humble", "eng-sa-p12": "punctual",
    "eng-sa-p13": "transparent", "eng-sa-p14": "liberty", "eng-sa-p15": "virtue",
}
SOLVED = {"eng-sa-s01": "benevolent", "eng-sa-s02": "frugal", "eng-sa-s03": "cordial"}
errs = []
for q in data["practice"]:
    if q["id"] not in EXISTING and q["id"] not in TARGET:
        errs.append(f"no target recorded for {q['id']}")
allt = dict(EXISTING)
allt.update(TARGET)
c = Counter(allt.values())
for t, n in c.items():
    if n > 1:
        errs.append(f"headword asked {n} times in practice: {t}")
for qid, t in TARGET.items():
    if t in SOLVED.values():
        errs.append(f"{qid}: repeats a solved-example headword {t}")
# the headword must appear in the question text (guards a mis-typed target)
by_id = {q["id"]: q for q in data["practice"]}
for qid, t in TARGET.items():
    if t not in by_id[qid]["q"].lower():
        errs.append(f"{qid}: headword {t!r} not found in the question")
if errs:
    print("DEDUP ERRORS:")
    for e in errs:
        print(" -", e)
    sys.exit(1)
print(f"dedup OK: {len(allt)} distinct headwords across practice")

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Direct synonym ('nearest in meaning')", "frequency": "very common", "subtopic": "syn-elimination",
  "howToSpot": "A bare capitalised word with four options; the command says 'nearest in meaning'.",
  "approach": "Say the word's meaning in one plain word, then run the filters in order: part of speech, class of idea, degree, charge (positive or negative). Strike options that fail any filter and pick the survivor closest in strength and tone.",
  "example": {"q": "Select the word which is nearest in meaning to the given word.  LUCID", "solution": "**Clear**. Lucid writing is easy to understand; 'dull' and 'lengthy' are class mismatches."}},
 {"pattern": "Direct antonym ('most opposite in meaning')", "frequency": "very common", "subtopic": "ant-prefix-flip",
  "howToSpot": "A bare capitalised word; the command says 'most opposite'. At least one option is a synonym of the stem.",
  "approach": "Strike every synonym of the stem first — in an antonym question they are always wrong. Then name the scale the word sits on and choose the option at the other end, not merely a different word.",
  "example": {"q": "Select the word which is most opposite in meaning to the given word.  HUMBLE", "solution": "**Proud**. Modest would be a synonym; proud sits at the other end of the same scale."}},
 {"pattern": "Root-based decoding of an unfamiliar word", "frequency": "common", "subtopic": "syn-root-word-method",
  "howToSpot": "The stem word is long or technical-looking but contains a known prefix or root (mal-, bene-, chron-, spect-, port-).",
  "approach": "Split the word into prefix + root + suffix, translate the pieces, and assemble a plain meaning. Match that meaning to the options, and check the part of speech of the ending (-ous, -tion, -ness).",
  "example": {"q": "Select the word which is nearest in meaning to the given word.  TENACIOUS", "solution": "**Persistent** — tenax = holding firmly; one who holds on does not give up."}},
 {"pattern": "Prefix-flip false antonym", "frequency": "common", "subtopic": "ant-prefix-flip",
  "howToSpot": "An option built by flipping the stem's prefix (flammable, valuable, interested) seems to be the opposite.",
  "approach": "Never build the opposite by adding or removing a prefix. Recall the stem's real meaning from memory (invaluable = extremely valuable; inflammable = burns easily), then choose the option that truly reverses it.",
  "example": {"q": "Select the word which is most opposite in meaning to the given word.  INVALUABLE", "solution": "**Worthless**. Invaluable means priceless; 'valuable' is the shape trap that means the same, not the opposite."}},
 {"pattern": "Synonym or antonym of a word inside a sentence", "frequency": "common", "subtopic": "syn-ant-strategy",
  "howToSpot": "The key word appears in CAPITALS inside a full sentence, and the options are meanings or opposites of that use.",
  "approach": "Read the whole sentence and paraphrase the capitalised word in one plain word — the context fixes which sense is being tested. Then apply the usual filters to your paraphrase, not to the printed word.",
  "example": {"q": "His IMMINENT arrival made everyone hurry. (nearest in meaning)", "solution": "**About to happen** — the sentence shows the arrival is just ahead, so 'overdue' and 'unexpected' fail the context."}},
 {"pattern": "Synonym with degree or connotation trap", "frequency": "common", "subtopic": "syn-elimination",
  "howToSpot": "Two options share the right class of idea but differ in strength or tone (serious vs vital; well known vs notorious).",
  "approach": "Place the stem word on its scale and note its charge. Extreme stems take extreme answers; negative stems take negative answers. Choose the option matching both, and reject the weaker or wrongly toned survivor.",
  "example": {"q": "Select the word which is nearest in meaning to the given word.  NOTORIOUS", "solution": "**Infamous** — both are negative fame. 'Famous' has the right class but the wrong charge."}},
 {"pattern": "Vocabulary hidden inside cloze and fill-in items", "frequency": "common", "subtopic": "syn-ant-strategy",
  "howToSpot": "A cloze blank or a fill-in item whose four options are near-synonyms; the mark depends on vocabulary plus context.",
  "approach": "Fix the tone and part of speech the sentence needs, remove options of the wrong charge or form, then test the survivors in the blank. Choose the one that collocates naturally with the surrounding words.",
  "example": {"q": "Fill in: *The chairman's speech was ___ and everyone understood the plan.* (lucid / illegal / lucidly / limp)", "solution": "**Lucid** — an adjective is needed before the noun, and 'understood the plan' confirms the clear sense."}},
 {"pattern": "Mixed-direction drill items", "frequency": "occasional", "subtopic": "syn-ant-strategy",
  "howToSpot": "A run of items alternates between 'nearest in meaning' and 'most opposite' for the same word bank.",
  "approach": "Read the command word before the stem and say the required direction aloud (same or reverse). Apply the matching strike rule: synonyms are wrong for opposites, opposites are wrong for synonyms. Most errors here are direction errors, not knowledge errors.",
  "example": {"q": "Most opposite to SPARSE", "solution": "**Dense**. Thinly scattered is the meaning — a synonym decoy — while dense sits at the other end of the same scale."}},
]

save(TOPIC, data)
report(data, before, new_ids)
