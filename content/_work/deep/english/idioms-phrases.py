# Phase 2 deep content: english / idioms-phrases. Idempotent (upsert by id). Run: py -3 idioms-phrases.py
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, upsert_list, apply_subtopics, report
from idioms_notes import S
from idioms_questions import QS_ID, TARGET

TOPIC = "idioms-phrases"
data = load(TOPIC)
before = {"subs": 5, "practice": 15}

apply_subtopics(data, S)
# keep the new subtopic next to the strategy block, before it
order = ["idiom-literal-trap", "idiom-animal-body", "idiom-colour-food", "idiom-situations-people",
         "idiom-phrasal-verbs", "idiom-strategy"]
data["subtopics"].sort(key=lambda s: order.index(s["id"]) if s["id"] in order else 99)

QS = QS_ID()
new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ---------------- no idiom asked twice (existing practice + solved + new practice) ----------------
EXISTING = {
    "eng-id-p01": "once in a blue moon", "eng-id-p02": "burn the midnight oil", "eng-id-p03": "a white elephant",
    "eng-id-p04": "beat about the bush", "eng-id-p05": "bite the bullet", "eng-id-p06": "turn a deaf ear",
    "eng-id-p07": "in hot water", "eng-id-p08": "make both ends meet", "eng-id-p09": "achilles' heel",
    "eng-id-p10": "spill the beans", "eng-id-p11": "pull someone's leg", "eng-id-p12": "at the drop of a hat",
    "eng-id-p13": "keep the wolf from the door", "eng-id-p14": "smell a rat", "eng-id-p15": "hit the nail on the head",
}
SOLVED = {"eng-id-s01": "smell a rat", "eng-id-s02": "a blessing in disguise", "eng-id-s03": "pass the buck"}
errs = []
for q in data["practice"]:
    if q["id"] not in EXISTING and q["id"] not in TARGET:
        errs.append(f"no target recorded for {q['id']}")
allt = dict(EXISTING)
allt.update(TARGET)
c = Counter(allt.values())
for t, n in c.items():
    if n > 1:
        errs.append(f"idiom asked {n} times in practice: {t}")
for qid, t in TARGET.items():
    if t in SOLVED.values():
        errs.append(f"{qid}: repeats a solved-example idiom {t}")
# the target must appear in the question text (guards against a mis-typed target)
by_id = {q["id"]: q for q in data["practice"]}
for qid, t in allt.items():
    key = t.replace("someone's", "").replace("one's", "").split()[-1].strip("'")
    if key not in by_id[qid]["q"].lower() and key not in by_id[qid]["options"][by_id[qid]["answer"]].lower():
        errs.append(f"{qid}: target word {key!r} not found in the question")
if errs:
    print("DEDUP ERRORS:")
    for e in errs:
        print(" -", e)
    sys.exit(1)
print(f"dedup OK: {len(allt)} distinct idioms/phrases across practice")

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Meaning of a common idiom", "frequency": "very common", "subtopic": "idiom-literal-trap",
  "howToSpot": "One idiom is given on its own and you must choose its meaning from four options. At least one option simply repeats the idiom's words.",
  "approach": "Cross out every literal option first. Then ask what the picture in the idiom stands for and choose that meaning. Put your answer back into a short sentence to check that it reads naturally.",
  "example": {"q": "Select the most appropriate meaning of the idiom: *To throw in the towel*", "solution": "A towel thrown into a boxing ring stops the fight → **to admit defeat and give up**. 'Clean up after a game' is the literal decoy."}},
 {"pattern": "Idiom used inside a sentence", "frequency": "common", "subtopic": "idiom-literal-trap",
  "howToSpot": "The idiom is printed in bold inside a sentence, and the options are possible meanings.",
  "approach": "Decide from the sentence whether the situation is good or bad news. Remove options with the wrong tone, then test the survivors in place of the idiom.",
  "example": {"q": "*The minister's promise **ended in smoke**.* Meaning?", "solution": "A promise that ends in smoke disappears → **came to nothing**."}},
 {"pattern": "Animal and body-part idioms", "frequency": "very common", "subtopic": "idiom-animal-body",
  "howToSpot": "The idiom contains an animal (bull, rat, crocodile, wolf) or a body part (ear, eye, neck, feet, hand).",
  "approach": "Use the animal's fixed character (crocodile = fake, bull = bold) or the body part's job (ear = listen, neck = risk). This decodes most such idioms even if you only half remember them.",
  "example": {"q": "Meaning of *Crocodile tears*", "solution": "Crocodile = fake → **pretended sorrow**."}},
 {"pattern": "Colour and food idioms, including look-alike twins", "frequency": "common", "subtopic": "idiom-colour-food",
  "howToSpot": "A colour (red, blue, green, white, black) or a food (cake, nut, potato, apple) appears in the idiom; often one option is the meaning of a twin idiom.",
  "approach": "Recall the colour's feeling or the food's judgement. Watch the three reds: see red (angry), red tape (official delay), red-letter day (happy day). Cross out the twin idiom's meaning.",
  "example": {"q": "Meaning of *Red tape*", "solution": "**Too many official rules causing delay**. 'A memorable day' is the twin (red-letter day)."}},
 {"pattern": "Fill in the blank with an idiom", "frequency": "common", "subtopic": "idiom-situations-people",
  "howToSpot": "A sentence has a blank and the four options are idioms.",
  "approach": "Name what the sentence needs (running away, a lower role, a small fuss, a joyful day). Choose the idiom from that family and read the sentence again to check grammar.",
  "example": {"q": "*Seeing the police, the pickpocket ___.* (took to his heels / broke the ice / kept his chin up / turned a deaf ear)", "solution": "The thief escapes → **took to his heels**."}},
 {"pattern": "Idioms from stories and legends", "frequency": "occasional", "subtopic": "idiom-situations-people",
  "howToSpot": "A name or story object appears: Achilles, Pandora, Hercules, Midas, a Trojan horse, belling the cat.",
  "approach": "Recall the one-line story and turn its key point into a general meaning. Options that retell the story literally are wrong.",
  "example": {"q": "Meaning of *Achilles' heel*", "solution": "The hero could be wounded only at his heel → **a weak point in a strong person or system**."}},
 {"pattern": "Replace the phrase with an idiom", "frequency": "common", "subtopic": "idiom-strategy",
  "howToSpot": "Words in a sentence are in bold; the options are idioms that might replace them.",
  "approach": "Restate the bold words in two or three plain words, then pick the idiom that has exactly that meaning. The other options are real idioms with different meanings.",
  "example": {"q": "*The workers **were dismissed from their jobs**.*", "solution": "Dismissed → **got the sack**."}},
 {"pattern": "Complete the idiom / opposite of an idiom", "frequency": "occasional", "subtopic": "idiom-strategy",
  "howToSpot": "Either one word of a fixed idiom is missing, or the stem asks for the option opposite in meaning.",
  "approach": "Idioms are frozen, so only the original word completes them (a spade a **spade**). For opposites, write the meaning first, then reverse it; the option that repeats the meaning is the trap.",
  "example": {"q": "Opposite of *To keep one's chin up*", "solution": "Meaning = stay cheerful; opposite = **to lose heart**."}},
 {"pattern": "Phrasal verbs: meaning and particle", "frequency": "common", "subtopic": "idiom-phrasal-verbs",
  "howToSpot": "A verb with a particle (call off, put up with, give up) is asked for meaning, or a blank follows a verb and the options are up/off/out/down/in.",
  "approach": "Use the particle's idea: off = cancel/stop, out = finish/remove, down = refuse/fail, after = care/resemble, into = investigate. Test each option in the sentence.",
  "example": {"q": "*Our car broke ___ on the highway.*", "solution": "Machines stop working → **down**."}},
]

save(TOPIC, data)
report(data, before, new_ids)
