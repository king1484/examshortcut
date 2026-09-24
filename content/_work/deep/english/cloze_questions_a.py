# Cloze practice questions, part A: strategy, grammar, vocab subtopics.
from _lib import QA

QS = []
SUB_S = "cloze-strategy"
SUB_G = "cloze-grammar-fit"
SUB_V = "cloze-vocab-fit"

# ------------------------------------------------- strategy: 3 passages x 4 blanks
PS1 = """Sunshine Public School used to buy tankers of water every summer. Last year it built a simple rainwater system: rain falling on the roof travels through pipes into a (1) ______ tank, where leaves and dust settle at the bottom. The cleaned water then runs into the school's old well, which had almost dried up. This summer the school did not order a single (2) ______, and the garden gate, once kept locked to protect the wilting plants, now stands open. The headmaster says the biggest change is in the students: they check the taps after (3) ______ and repair dripping ones the same day. 'The tank taught them what the (4) ______ never did — that water is counted, not limitless,' he says."""
QS += [
 QA("cloze-strategy-p01", SUB_S, "cls1", "Select the most appropriate option to fill in blank number (1).",
    ["storage", "parking", "prayer", "sports"],
    "The passage is about saving rainwater for use; the tank that receives roof water and lets dust settle is a **storage** tank. *Parking*, *prayer* and *sports* are school-world words, but none names a function a water tank can serve — reading the whole passage's theme (harvesting water) kills all three at once.",
    "Theme first: the story is water harvesting; keep only tank words that store water.", "easy", 40, PS1, "cloze-gs1"),
 QA("cloze-strategy-p02", SUB_S, "cls3", "Select the most appropriate option to fill in blank number (2).",
    ["ticket", "book", "tanker", "rule"],
    "The answer is sitting in the first sentence: the school 'used to **buy tankers** of water every summer'. This summer, with the new system, it ordered no **tanker**. The clue lies in a *neighbouring sentence*, not in the blank's own line — a reminder to read the passage around the blank.",
    "Look up: the first sentence already names the thing that is no longer ordered.", "medium", 40, group="cloze-gs1"),
 QA("cloze-strategy-p03", SUB_S, "cls2", "Select the most appropriate option to fill in blank number (3).",
    ["applause", "assembly", "gravity", "thunder"],
    "All four are nouns, so grammar cannot decide. Students check taps 'after (3) ___' and repair them 'the same day' — the blank needs a regular school event after which students move around the building: **assembly**. *Applause*, *gravity* and *thunder* are real words that fit the grammar and even the school world loosely, but only assembly is a daily event on a school timetable.",
    "Plug each option into the sentence; keep the one that names a daily school event.", "medium", 45, group="cloze-gs1"),
 QA("cloze-strategy-p04", SUB_S, "cls4", "Select the most appropriate option to fill in blank number (4).",
    ["plumber", "syllabus", "generator", "noticeboard"],
    "The tank 'taught them what the (4) ___ never did — that water is counted'. Only a **syllabus** is a thing that teaches in a school. The tempting *plumber* fits a water story locally, but re-reading shows the sentence is about a *lesson*, not a repair job — the plumber never set out to teach anything. The full-passage re-read catches this.",
    "Two options may fit locally; re-read the passage and keep the one that does not clash with the sentence's real point (teaching).", "hard", 50, group="cloze-gs1"),
]
PS2 = """When the textile mill in Erode added a night shift, hundreds of workers finished duty at two in the morning — and found every shop shut. Within months, a small night market appeared near the mill gate: tea stalls, a barber, a pharmacy and carts selling hot (1) ______. Traders say trust is their main (2) ______: goods are left on open shelves, and payments are dropped into a tin, yet nothing is ever missing. A doctor who volunteers at the market's first-aid desk notes that many workers come not to buy but to talk. 'The market sells food, but what it really (3) ______ is company,' he says. The corporation, which once fined the traders for blocking the road, has now built them a covered (4) ______ with lights and a water tap."""
QS += [
 QA("cloze-strategy-p05", SUB_S, "cls3", "Select the most appropriate option to fill in blank number (2).",
    ["capital", "rival", "advertisement", "uniform"],
    "The clause after the colon explains the claim: 'goods are left on open shelves, and payments are dropped into a tin, yet nothing is ever missing.' Trust works here like **capital** — an asset that produces income without investment. *Rival*, *advertisement* and *uniform* are trader-world words, but the following lines describe an asset at work, not a competitor, a promotion or a dress code.",
    "The colon promises an explanation — the answer is the word the explanation describes.", "hard", 50, PS2, "cloze-gs2"),
 QA("cloze-strategy-p06", SUB_S, "cls1", "Select the most appropriate option to fill in blank number (3).",
    ["paints", "sells", "measures", "imports"],
    "The doctor repeats the passage's controlling metaphor: a market **sells** — and this one sells food but really 'sells company'. *Paints*, *measures* and *imports* are grammatical verbs, but each breaks the selling idea the whole passage runs on. Reading the passage first tells you the writer is still inside the market metaphor.",
    "Theme check: the sentence plays on 'market → selling'; keep the verb that stays inside the metaphor.", "medium", 40, group="cloze-gs2"),
 QA("cloze-strategy-p07", SUB_S, "cls2", "Select the most appropriate option to fill in blank number (1).",
    ["negotiations", "mirrors", "contracts", "snacks"],
    "The list reads 'tea stalls, a barber, a pharmacy and carts selling hot ___'. The blank needs something the carts **sell** and workers on a night shift **eat**: hot **snacks**. *Negotiations*, *mirrors* and *contracts* are nouns that fit the grammar, but 'hot negotiations' or 'hot mirrors' is not a real collocation — plugging each option in rejects them instantly.",
    "Same part of speech for all four → test the collocation 'hot ___' and the verb 'selling'.", "easy", 35, group="cloze-gs2"),
 QA("cloze-strategy-p08", SUB_S, "cls4", "Select the most appropriate option to fill in blank number (4).",
    ["shelter", "warehouse", "courtroom", "stadium"],
    "The corporation 'built them a covered ___ with lights and a water tap' — a civic **shelter** for the market. *Warehouse* is the tempting local fit (covered, has lights), but re-reading the passage shows the frame: the corporation once fined the traders and is now *supporting* them — it provides public amenity, not goods storage. A courtroom or stadium cannot serve a row of food carts.",
    "Re-read before answering: the earlier fine shows the corporation's new role is welfare, so pick the civic option.", "medium", 45, group="cloze-gs2"),
]
PS3 = """Meena learnt to swim at thirty-eight, two years after her daughter did. At the first class she held the pool edge so hard that her fingers ached, and she (1) ______ the deep end as if it were a border between two countries. Her coach, a retired lifeguard, refused to teach strokes at first; for a week she only walked in the shallow water and blew bubbles. 'Fear leaves through the body, not the (2) ______,' he told her when she asked for a book on techniques. By the third month she could float, and floating, she says, changed everything: the moment the water held her, she stopped fighting it. Last month she swam the pool's full length, and her daughter, who once (3) ______ her from the gallery, now swims beside her. Meena's advice to adults is simple: begin this month, (4) ______ your age, and give the water ten patient sessions before you judge yourself."""
QS += [
 QA("cloze-strategy-p09", SUB_S, "cls4", "Select the most appropriate option to fill in blank number (2).",
    ["mind", "swimming pool", "coach", "daughter"],
    "She asked for a *book*, and the coach answered that fear leaves 'through the body, not the ___'. His point: fear is beaten by experience in the water (body), not by theory absorbed in the **mind**. *Swimming pool* and *coach* fit the local scene, but re-reading the anecdote shows the contrast is body versus thought, not body versus places or people.",
    "Re-read the anecdote around the quote — the 'book' line tells you the contrast is experience vs theory.", "hard", 50, PS3, "cloze-gs3"),
 QA("cloze-strategy-p10", SUB_S, "cls2", "Select the most appropriate option to fill in blank number (1).",
    ["feared", "painted", "measured", "renovated"],
    "She gripped the edge till her fingers ached and treated the deep end 'as if it were a border between two countries' — she **feared** it. All four options are past-tense verbs, so only meaning decides: a frightened beginner does not paint, measure or renovate the deep end.",
    "All options grammatical → read the simile ('as if it were a border') and choose the emotion it describes.", "medium", 35, group="cloze-gs3"),
 QA("cloze-strategy-p11", SUB_S, "cls1", "Select the most appropriate option to fill in blank number (3).",
    ["watched", "charged", "fined", "audited"],
    "The sentence sets a before-and-after: the daughter 'once ___ her from the gallery' and 'now swims beside her'. A person in a gallery **watches**. The passage's theme is a learning journey observed at a distance, so *watched* keeps the theme; *charged*, *fined* and *audited* belong to money and offices, a different world.",
    "The once…now frame is the passage's journey theme; pick the spectator verb that fits 'from the gallery'.", "medium", 40, group="cloze-gs3"),
 QA("cloze-strategy-p12", SUB_S, "cls3", "Select the most appropriate option to fill in blank number (4).",
    ["ignore", "count", "announce", "celebrate"],
    "The advice sentence ends 'give the water ten patient sessions before you judge yourself'. The surrounding lines — Meena learnt at thirty-eight; the coach preached patience — build one message: age must not decide whether an adult tries. So: '**ignore** your age'. *Count* is the tempting opposite (age is a number), but the passage never asks anyone to calculate; it asks them to start.",
    "Read the lines before and after the blank: patience and a 38-year-old learner point to one instruction.", "medium", 45, group="cloze-gs3"),
]

# ------------------------------------------------- grammar: 2 passages x 4 blanks
PG1 = """Last January, the terrace of Govind's house became a kite workshop. Every evening he and his elder son (1) ______ new kites out of bamboo strips and thin paper, while his daughter mixed the glue. By the second week the whole lane (2) ______ of gum and sawdust. On festival day (3) ______ sky above the lane was so full of kites that the birds kept their distance. Govind, who has flown kites since childhood, keeps his father's old spool in a wooden box, and he enjoys (4) ______ old kites to the children of the lane."""
QS += [
 QA("cloze-grammar-fit-p01", SUB_G, "clg2", "Select the most appropriate option to fill in blank number (1).",
    ["made", "make", "making", "maker"],
    "The anchor is 'Last January', and 'every evening' describes a repeated action inside that past period. Past narrative + habitual → simple past: **made**. *Make* breaks the time frame; *making* is not a finite verb and cannot be the main verb; *maker* is a noun.",
    "Find the time anchor first ('Last January') — then only past forms survive.", "easy", 35, PG1, "cloze-gg1"),
 QA("cloze-grammar-fit-p02", SUB_G, "clg1", "Select the most appropriate option to fill in blank number (2).",
    ["smelt", "smell", "smells", "smelling"],
    "The subject is 'the whole lane' — singular — and the passage is a past narrative ('Last January… became…'). Past + singular subject → **smelt**. *Smells* would fit a present habitual passage, *smell* lacks agreement, and *smelling* is not finite.",
    "Strip the sentence to 'the lane ___ of gum' to see the true singular subject.", "hard", 40, group="cloze-gg1"),
 QA("cloze-grammar-fit-p03", SUB_G, "clg4", "Select the most appropriate option to fill in blank number (3).",
    ["A", "An", "The", "Some"],
    "The noun phrase is '___ sky above the lane' — the phrase 'above the lane' makes the sky specific and there is only one sky above the lane. Definite → **The**. *A/An* would mean one of several skies; *Some* does not fit a unique noun.",
    "Unique or already-specified noun → the.", "easy", 30, group="cloze-gg1"),
 QA("cloze-grammar-fit-p04", SUB_G, "clg3", "Select the most appropriate option to fill in blank number (4).",
    ["showing", "show", "to show", "showed"],
    "The verb before the blank is **enjoys**, and *enjoy* is always followed by the -ing form: enjoys showing. 'Enjoys to show' is wrong English; *show* after 'enjoys' breaks the pattern, and *showed* would create two finite verbs with no joiner.",
    "Word before the blank decides the form: enjoy → -ing.", "medium", 35, group="cloze-gg1"),
]
PG2 = """Every morning before his duty, Ravi, a city bus driver, spends an hour in his small garden behind the staff quarter. He grows tomatoes in paint buckets because the soil in his yard (1) ______ too rocky for beds. His neighbours at first (2) ______ fun of the buckets, but now three of them copy the idea. Ravi says gardening has taught him (3) ______ patient, and patience is what city traffic demands. When a passenger once praised the chillies he carried in his bag, Ravi (4) ______ him a bucket of his own the very next day."""
QS += [
 QA("cloze-grammar-fit-p05", SUB_G, "clg1", "Select the most appropriate option to fill in blank number (1).",
    ["is", "are", "were", "be"],
    "Strip the sentence: 'the soil in his yard ___ too rocky'. The true subject is **soil** (singular; 'in his yard' is noise). The passage speaks in the present ('spends', 'grows'), so: **is**. *Are* is pulled by the nearby plural feel of 'buckets'; *were* breaks the present frame; *be* is not finite here.",
    "Cross out the phrase between subject and verb, then match number and tense.", "medium", 40, PG2, "cloze-gg2"),
 QA("cloze-grammar-fit-p06", SUB_G, "clg2", "Select the most appropriate option to fill in blank number (2).",
    ["made", "make", "making", "maker"],
    "'At first … but now' contrasts a finished past phase with the present: at first they **made** fun; now they copy. Past → **made**. *Make* would clash with 'at first', *making* is non-finite, and *maker* is a noun. (The collocation is 'make fun of'.)",
    "'At first' + 'but now' = past-versus-present contrast; the blank sits in the past half.", "medium", 35, group="cloze-gg2"),
 QA("cloze-grammar-fit-p07", SUB_G, "clg3", "Select the most appropriate option to fill in blank number (3).",
    ["to be", "being", "be", "been"],
    "**Teach someone** is followed by the to-infinitive: taught him **to be** patient. 'Taught him being patient' is wrong; a bare *be* cannot follow the object here; *been* needs 'has/had'.",
    "teach + object + to-infinitive — no meaning test needed, only the pattern.", "medium", 35, group="cloze-gg2"),
 QA("cloze-grammar-fit-p08", SUB_G, "clg4", "Select the most appropriate option to fill in blank number (4).",
    ["A", "An", "The", "Some"],
    "'Ravi ___ him a bucket of his own the very next day' — no bucket has been mentioned before, so it is a first mention, one of many: **A** bucket. *The* would claim a known, specific bucket; *An* fails before the consonant sound; *Some* does not fit a counted single gift.",
    "First mention, one of many → a/an; sound decides a vs an.", "medium", 35, group="cloze-gg2"),
]

# ------------------------------------------------- vocab: 2 passages x 4 blanks
PV1 = """The corporation library on Gandhi Road now stays open till eleven at night. The change began when a clerk noticed students reading under the streetlight after closing time. The reading hall, once half (1) ______, is now full by eight o'clock. Regulars say the quiet here has a different (2) ______ from the quiet of their homes, where the television mutters in every room. The librarian has also begun to (3) ______ old newspapers for a small archive that students use to trace how an issue developed. Pleased by the response, the corporation has sanctioned two more fans, and the students (4) ______ full advantage of the extended hours."""
QS += [
 QA("cloze-vocab-fit-p01", SUB_V, "clv3", "Select the most appropriate option to fill in blank number (1).",
    ["painted", "carpeted", "empty", "furnished"],
    "The sentence is a contrast: 'once half ___ … is now full by eight o'clock.' The word standing against *full* is **empty**. *Painted*, *carpeted* and *furnished* are real hall improvements, but none is the opposite of full — the contrast signal (once…now) decides.",
    "Contrast frame (once X → now Y): pick the option that is the opposite pole of Y.", "easy", 35, PV1, "cloze-gv1"),
 QA("cloze-vocab-fit-p02", SUB_V, "clv1", "Select the most appropriate option to fill in blank number (2).",
    ["price", "quality", "length", "colour"],
    "The regulars compare two kinds of quiet — library quiet and home quiet where 'the television mutters'. The sentence says the library quiet has a different ___ : the word for the *character* of a thing is **quality**. Quiet has no price, length or colour here; the next clause describes its nature, not its cost or duration.",
    "Ask what the following clause describes (the character of the quiet) and name it.", "hard", 45, group="cloze-gv1"),
 QA("cloze-vocab-fit-p03", SUB_V, "clv2", "Select the most appropriate option to fill in blank number (3).",
    ["publish", "preserve", "repair", "translate"],
    "The librarian collects old newspapers 'for a small archive'. The action an archive needs is **preserve** — keep old copies safe. *Publish* creates new copies, *repair* fixes damage, *translate* changes the language; none means 'store for the future'.",
    "Match the verb to the purpose word in the sentence ('for an archive').", "medium", 40, group="cloze-gv1"),
 QA("cloze-vocab-fit-p04", SUB_V, "clv4", "Select the most appropriate option to fill in blank number (4).",
    ["make", "do", "take", "give"],
    "The fixed collocation is **take (full) advantage of** — 'the students take full advantage of the extended hours'. *Do advantage* and *make advantage* are not English; *give* would need a different structure ('give someone an advantage'). This is the classic make/do/take trap.",
    "Noun after the blank → recall its fixed verb: advantage → take.", "medium", 35, group="cloze-gv1"),
]
PV2 = """Every Sunday, Farida sets up chessboards in the park behind the market and teaches whoever stops to watch. What began as a pastime has become a small (1) ______: forty children from the nearby lanes attend her free class. She insists that chess does not (2) ______ talent alone; it rewards habit. 'A (3) ______ player who studies one game a day will soon beat a player who plays ten games carelessly,' she says. The market traders, who once asked her to move away, now (4) ______ room for her boards every Sunday morning."""
QS += [
 QA("cloze-vocab-fit-p05", SUB_V, "clv1", "Select the most appropriate option to fill in blank number (1).",
    ["institution", "accident", "complaint", "excuse"],
    "'What began as a pastime has become a small ___: forty children … attend her free class.' A regular, established activity with forty regulars is a small **institution**. *Accident*, *complaint* and *excuse* carry negative or unrelated meanings that clash with the proud, growth story of the passage.",
    "The colon lists the evidence (forty regulars) — the blank must name an established, grown activity.", "hard", 40, PV2, "cloze-gv2"),
 QA("cloze-vocab-fit-p06", SUB_V, "clv2", "Select the most appropriate option to fill in blank number (2).",
    ["require", "refuse", "print", "pardon"],
    "'Chess does not ___ talent alone; it rewards habit.' The verb must mean 'need/demand': **require**. The sentence then balances talent against habit. *Refuse*, *print* and *pardon* are verbs, but 'chess refuses talent' or 'chess prints talent' says nothing the second clause can support.",
    "The clause after the semicolon ('it rewards habit') tells you the verb means 'need'.", "easy", 35, group="cloze-gv2"),
 QA("cloze-vocab-fit-p07", SUB_V, "clv3", "Select the most appropriate option to fill in blank number (3).",
    ["patient", "wealthy", "noisy", "absent"],
    "The contrast inside the quote: a ___ player who studies ONE game a day beats one who plays ten games CARELESSLY. The winning quality is **patient** study — the opposite of careless speed. *Wealthy*, *noisy* and *absent* have nothing to do with how one studies a game.",
    "Find the stated opposite (careless) and choose the word on the other pole.", "medium", 40, group="cloze-gv2"),
 QA("cloze-vocab-fit-p08", SUB_V, "clv4", "Select the most appropriate option to fill in blank number (4).",
    ["do", "take", "make", "give"],
    "The fixed phrase is **make room for** = clear space for someone: the traders now 'make room for her boards'. *Do room* and *take room* are not English; *give room* would need a different sense ('give way to'). Collocation decides.",
    "room → make (make room for). Learn the pair, not the logic.", "medium", 35, group="cloze-gv2"),
]
