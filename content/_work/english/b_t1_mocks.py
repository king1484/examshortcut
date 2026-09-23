from common import q, write_mock

# =========================================================================
# MOCK 1 — Tier 1 full English section (25 Qs: cloze 5 + 15 singles + RC 5)
# =========================================================================

M1_CLOZE_PASSAGE = """India's urban water crisis is less about rainfall than about planning. Every monsoon, cities (1) ___ millions of litres of stormwater into the sea, and by April the same cities queue for water (2) ___ by tankers from distant reservoirs. Rooftop harvesting, compulsory on paper in many states, is ignored in practice because builders treat it as an (3) ___ expense. The cost of this neglect is (4) ___ every summer: borewells fail, tanker prices triple, and residents march to municipal offices. The remedy demands no new technology, only the discipline to enforce rules that already (5) ___."""

def cloze_q(n, options, answer, solution, shortcut=None, difficulty="easy"):
    stem = f"Select the most appropriate option to fill in blank number ({n})."
    if n == 1:
        return q(f"eng-m1-{n:02d}", stem, options, answer, solution, shortcut, difficulty,
                 "cloze-test", f"cloze-blank-{n}", 40, passage=M1_CLOZE_PASSAGE, group="m1-cloze")
    return q(f"eng-m1-{n:02d}", stem, options, answer, solution, shortcut, difficulty,
             "cloze-test", f"cloze-blank-{n}", 40, group="m1-cloze")

M1 = [
    cloze_q(1, ["flush", "drink", "sell", "freeze"], 0,
      "The image is of stormwater being (1) ___ INTO the sea — the wasted resource. 'Flush ... into' is the natural verb of wasted flow; drink, sell and freeze cannot take 'into the sea' meaningfully."),
    cloze_q(2, ["carried", "carry", "carrying", "carries"], 0,
      "The blank follows 'water' and precedes 'by tankers' — a reduced passive: water (which is) **carried** by tankers. The active form 'carry' would make 'water carry by tankers', which is ungrammatical."),
    cloze_q(3, ["avoidable", "avoid", "avoided", "avoiding"], 0,
      "The blank sits between 'an' and 'expense' — an adjective is needed. 'An avoidable expense' = a cost that could be skipped, matching 'ignored in practice'. The other three are verb forms and leave the sentence without an adjective."),
    cloze_q(4, ["visible", "vision", "visibly", "visibility"], 0,
      "'The cost of this neglect is ___' needs a complement adjective after 'is': **visible**. 'Visibly' is an adverb and cannot follow 'is'; vision and visibility are nouns that clash with 'the cost ... is'."),
    cloze_q(5, ["exist", "existed", "existence", "existing"], 0,
      "'Rules that already ___' — the relative clause needs a finite present verb: rules that already **exist**. Existed would break the present-time frame ('demands ... to enforce'); existence and existing are not finite verbs."),
    q("eng-m1-06", "Select the most appropriate synonym of the given word.\n\nLETHARGIC",
      ["sluggish", "cheerful", "alert", "honest"], 0,
      "Lethargic means drowsy and without energy — **sluggish**. Cheerful and alert are near-opposites; honest is unrelated.",
      "lethargy = lack of energy → sluggish.", "easy", "synonyms-antonyms", "synonym", 30),
    q("eng-m1-07", "Select the most appropriate antonym of the given word.\n\nOPTIMIST",
      ["pessimist", "nationalist", "ideal", "optimism"], 0,
      "An optimist expects the best; the opposite person-type is a **pessimist**. Nationalist and ideal are not person-opposites; optimism is the same family noun, not the opposite person.",
      "Opti- (best) vs pes- (worst): the pair is optimist–pessimist.", "easy", "synonyms-antonyms", "antonym", 30),
    q("eng-m1-08", "Select the most appropriate meaning of the given idiom.\n\nTo burn one's fingers",
      ["to suffer because of a hasty involvement", "to touch a hot stove", "to work near fire", "to lose one's gloves"], 0,
      "The picture: a hand poked into a fire too quickly gets scorched — **to suffer loss from acting rashly**, usually in money matters. The literal burn options are photographable decoys.",
      "Hasty hand → hasty involvement → burnt fingers.", "medium", "idioms-phrases", "idiom-meaning", 30),
    q("eng-m1-09", "Select the correctly spelt word.",
      ["Vacuum", "Vaccum", "Vacume", "Vacumm"], 0,
      "Vacuum has **double u** — vac-uum — from Latin 'vacuus' (empty). Each distractor drops or moves one of the two u's.",
      "vac + uum: two u's in a row.", "easy", "spelling", "spelling", 25),
    q("eng-m1-10", "Select the correctly spelt word.",
      ["Liaison", "Liason", "Liaisn", "Liaision"], 0,
      "Liaison keeps the first **i** even though it is silent in speech: lia-ison (French 'lier', to bind). Liason drops it; Liaision doubles it.",
      "liaison: l-i-a-i-s-o-n — count the two i's.", "hard", "spelling", "spelling", 30),
    q("eng-m1-11", "Select the most appropriate one word for the given expression.\n\nA place where money is coined",
      ["Mint", "Vault", "Treasury", "Stall"], 0,
      "Coins are manufactured at a **mint**. A vault stores valuables; a treasury stores state money; a stall sells goods — none of them coins money.",
      "mint = make coins (as in 'a mint-new coin').", "easy", "one-word-substitution", "ows", 25),
    q("eng-m1-12", "Select the most appropriate option to fill in the blank.\n\nThe manager was angry ___ the delay in the shipment.",
      ["about", "from", "into", "beneath"], 0,
      "'Angry **about**' takes a thing or situation (the delay); 'angry with' takes a person. From, into and beneath are not collocations of angry.",
      "angry with a person, angry about a thing.", "easy", "fill-in-the-blanks", "fill-blank", 25),
    q("eng-m1-13", "Select the most appropriate option to fill in the blank.\n\nThe meeting was called ___ because of the strike.",
      ["off", "out", "in", "up"], 0,
      "'Call off' = cancel. Call out (summon workers to strike), call in (invite) and call up (phone) do not fit 'because of the strike' cancelling the meeting.",
      "call off = cancel.", "easy", "fill-in-the-blanks", "phrasal-verb", 25),
    q("eng-m1-14", "Select the part of the sentence that has an error.\n\nThe news (a) are spreading (b) very fast (c) No error (d)",
      ["The news", "are spreading", "very fast", "No error"], 1,
      "'News' is a singular uncountable noun despite its -s ending: 'The news **is** spreading very fast.' The error is in part (b).",
      "News, mathematics, physics — -s form, singular verb.", "medium", "error-spotting", "error-spot", 35),
    q("eng-m1-15", "Select the part of the sentence that has an error.\n\nI met (a) an European (b) at the party (c) No error (d)",
      ["I met", "an European", "at the party", "No error"], 1,
      "'European' begins with the consonant sound 'y' (yu-), so it takes **a**, not 'an': 'a European.' The article must follow sound, not spelling.",
      "Article follows the SOUND: yu-ropean → a.", "medium", "error-spotting", "error-spot", 35),
    q("eng-m1-16", "Select the option that will improve the underlined part of the sentence.\n\nHe don't know the answer to this question.",
      ["He does not know", "He do not knew", "He is not knowing", "No improvement"], 0,
      "Third-person singular needs **does not**: 'He does not know.' B breaks the verb form; C wrongly makes a stative verb continuous; D accepts the error.",
      "he/she/it + does not + V1.", "easy", "sentence-improvement", "improvement", 25),
    q("eng-m1-17", "Select the option that expresses the given sentence in passive voice.\n\nThe farmers are harvesting the crop.",
      ["The crop is being harvested by the farmers.", "The crop is harvested by the farmers.", "The crop was being harvested by the farmers.", "The crop has been harvested by the farmers."], 0,
      "Present continuous → **is/are being + V3**; the new subject 'the crop' is singular → is being harvested. B drops the continuous; C shifts to past; D shifts to perfect.",
      "are harvesting → is being + V3.", "easy", "active-passive", "active-to-passive", 30),
    q("eng-m1-18", "Select the option that expresses the given sentence in indirect speech.\n\nShe said, \"I have lost my keys.\"",
      ["She said that she had lost her keys.", "She said that she has lost her keys.", "She said that she loses her keys.", "She told that she had lost her keys."], 0,
      "Present perfect → **past perfect** (had lost); I → she; my → her. B skips the backshift; C drops two tenses; D uses 'told' without a listener.",
      "have + V3 → had + V3 after a past reporter.", "easy", "direct-indirect", "narration", 30),
    q("eng-m1-19", "Choose the correct order of the parts to make a meaningful sentence.\n\n**1.** A little knowledge is a dangerous thing. **P:** He prescribed the wrong medicine. **Q:** The patient's condition worsened. **R:** A half-trained assistant ran the clinic. **S:** The owner suspended him immediately. **6.** Better no training than half training.",
      ["RPQS", "QRPS", "PQRS", "RSPQ"], 0,
      "**R** gives the half-trained assistant (the example S1 warns of) → **P** his wrong prescription → **Q** the worsening it caused → **S** the immediate suspension → S6's moral. RPQS.",
      "Cause chain: assistant → prescription → worsening → suspension.", "medium", "sentence-rearrangement", "rearrangement", 50),
    q("eng-m1-20", "Select the most appropriate option to fill in the blank.\n\nThe scissors ___ on the table.",
      ["are", "is", "was", "has been"], 0,
      "'Scissors' is a plural-only noun (like trousers, spectacles) — it always takes a **plural** verb: 'The scissors are on the table.'",
      "Twin-noun objects (scissors, trousers) are plural.", "easy", "grammar-essentials", "grammar-sva", 25),
]

M1_RC_PASSAGE = """Modern economies run around the clock, but the human body does not. Shift workers — nurses, drivers, security guards, bakers — make up nearly a fifth of the workforce in industrialised countries, and they pay for the convenience of others with their health. Decades of research now link night shift work to disturbed sleep, weight gain, high blood pressure and even reduced resistance to infection. The reason is biological: a cluster of brain cells keeps a master clock that expects light at dawn and darkness at night. When exposure to bright light comes at midnight instead, the clock drifts out of alignment, and hormones that should rise at night rise at odd hours.

Yet economies cannot simply switch off. Hospitals, transport networks and power grids must run continuously. The sensible response, therefore, is not to abolish night work but to soften its costs. Some factories now rotate shifts forward — morning to evening to night — because forward rotation disturbs the body clock least. A few employers offer bright light during shifts and darkened rest rooms afterwards; both measurably improve alertness. Governments could help by treating shift work as a health issue, not merely a wage issue: regular medical checks, protection from arbitrary schedule changes and training in sleep hygiene would cost little.

The deeper problem is cultural. We admire the executive who answers email at 2 a.m. and mock the worker who naps. Until rest is treated as performance infrastructure — as serious as bandwidth or safety gear — the night shift will remain what it is today: the invisible subsidy that keeps the day shift comfortable."""

def m1_rc(n, qtext, options, answer, solution, shortcut=None, difficulty="medium", tsec=50):
    if n == 21:
        return q(f"eng-m1-{n}", qtext, options, answer, solution, shortcut, difficulty,
                 "reading-comprehension", f"rc-{n}", tsec, passage=M1_RC_PASSAGE, group="m1-rc")
    return q(f"eng-m1-{n}", qtext, options, answer, solution, shortcut, difficulty,
             "reading-comprehension", f"rc-{n}", tsec, group="m1-rc")

M1 += [
    m1_rc(21, "What is the central idea of the passage?",
      ["Night work cannot be abolished, so its health costs should be managed deliberately.", "Night shift work should be abolished to protect workers.", "Only hospital staff suffer from disturbed body clocks.", "The human body clock can be adjusted at will."], 0,
      "The passage states night work must continue ('economies cannot simply switch off') and then spends two paragraphs on softening its costs — the thesis is **manage, don't abolish**. B contradicts the passage; C narrows it wrongly; D reverses the biological finding.",
      "Thesis lives in the pivot sentence: 'not to abolish but to soften its costs'.", "medium", 50),
    m1_rc(22, "According to the passage, shift workers make up nearly a fifth of the workforce in —",
      ["industrialised countries", "hospitals only", "developing economies", "government offices"], 0,
      "The opening line fixes the figure: 'nearly a fifth of the workforce in **industrialised countries**.' The other options replace the stated scope.",
      "Detail questions: return to the exact line and match nouns.", "easy", 45),
    m1_rc(23, "It can be inferred from the passage that factories rotate shifts forward because —",
      ["forward rotation disturbs the body clock the least", "workers prefer night duty first", "it saves electricity", "backward rotation is illegal"], 0,
      "The passage gives the reason in the same sentence: forward rotation is used '**because** forward rotation disturbs the body clock least.' B, C and D supply plausible but unstated motives.",
      "Because-clause = the inference gift: quote it back.", "medium", 50),
    m1_rc(24, "The phrase 'soften its costs' as used in the passage means —",
      ["reduce the harmful effects of night work", "make night work cheaper for employers", "lengthen night shifts gradually", "raise the wages of night workers"], 0,
      "The costs in question are the health harms listed earlier; softening them = **reducing the damage**. Wages are explicitly called insufficient ('not merely a wage issue'), and shift length is not discussed.",
      "Replace the phrase with its context: costs = health harms.", "medium", 45),
    m1_rc(25, "The author's attitude toward shift workers can best be described as —",
      ["sympathetic concern", "complete indifference", "open hostility", "light amusement"], 0,
      "The author catalogues their health costs, proposes protections and calls them an 'invisible subsidy' — concern for an unfairly burdened group, i.e. **sympathetic concern**. Mocking is attributed to culture, not to the author.",
      "Tone = verdict on the subject: protections proposed → sympathy.", "medium", 45),
]

# =========================================================================
# PYQ 2025 — Tier 1 pattern mirror (25 Qs: cloze 5 + 15 singles + RC 5)
# =========================================================================

PYQ_CLOZE_PASSAGE = """Doctors now describe sitting as the new smoking, and the comparison is not entirely (1) ___. Hours of uninterrupted sitting slow the circulation, dull the muscles and confuse the metabolism that movement keeps sharp. The trouble is that modern work is built around the chair: screens, meetings and commutes all (2) ___ stillness. Exercise routines sold as the cure assume a willpower that most tired people cannot (3) ___. A simpler prescription is emerging from research: break up the sitting. Standing for two minutes every half hour, walking during phone calls, taking stairs instead of lifts — these small acts do not (4) ___ gym membership, but studies credit them with real gains in energy, mood and blood sugar. The body, it seems, is less impressed by the (5) ___ of occasional heroic workouts than by the rhythm of frequent light movement."""

def pyq_cloze(n, options, answer, solution, shortcut=None, difficulty="medium", tsec=40):
    stem = f"Select the most appropriate option to fill in blank number ({n})."
    if n == 1:
        return q(f"eng-pyq-{n:02d}", stem, options, answer, solution, shortcut, difficulty,
                 "cloze-test", f"cloze-blank-{n}", 40, passage=PYQ_CLOZE_PASSAGE, group="pyq-cloze")
    return q(f"eng-pyq-{n:02d}", stem, options, answer, solution, shortcut, difficulty,
             "cloze-test", f"cloze-blank-{n}", tsec, group="pyq-cloze")

PYQ = [
    pyq_cloze(1, ["fair", "rare", "late", "loud"], 0,
      "'Not entirely ___' — the comparison to smoking is called mostly but not wholly justified: **fair**. Rare, late and loud have no bearing on whether a comparison is justified."),
    pyq_cloze(2, ["demand", "disturb", "deny", "double"], 0,
      "Work 'is built around the chair', so screens, meetings and commutes all **demand** stillness. Disturb and deny reverse the logic; double is ungrammatical here ('double stillness' adds nothing the frame supports)."),
    pyq_cloze(3, ["summon", "suffer", "swallow", "scatter"], 0,
      "To call up willpower from within is to **summon** it — the collocation 'summon the willpower' fits 'cannot summon'. The other three verbs do not collocate with willpower."),
    pyq_cloze(4, ["require", "admire", "expire", "enquire"], 0,
      "Small acts 'do not ___ gym membership' — they **require** no membership. Admire, expire and enquire are sound-alike decoys from the -quire family.",
      "-quire trap set: pick by meaning, not by sound.", "medium", 40),
    pyq_cloze(5, ["drama", "drumbeat", "drowsiness", "drainage"], 0,
      "The sentence contrasts 'the ___ of occasional heroic workouts' with 'the rhythm of frequent light movement' — showiness vs regularity: **drama**. Drumbeat would support rhythm rather than contrast with it; drowsiness and drainage do not describe workouts' appeal."),
    q("eng-pyq-06", "Select the most appropriate synonym of the given word.\n\nOBLIGATORY",
      ["compulsory", "optional", "voluntary", "doubtful"], 0,
      "Obligatory = required, **compulsory**. Optional and voluntary are antonyms; doubtful is unrelated.",
      "obligation → something forced → compulsory.", "easy", "synonyms-antonyms", "synonym", 25),
    q("eng-pyq-07", "Select the most appropriate antonym of the given word.\n\nTRANSPARENT",
      ["opaque", "clear", "bright", "fragile"], 0,
      "Transparent lets light through; **opaque** blocks it — the standard antonym pair. Clear is a synonym; brightness and fragility are unrelated properties.",
      "trans- (through) vs op- (blocking): transparent–opaque.", "easy", "synonyms-antonyms", "antonym", 25),
    q("eng-pyq-08", "Select the most appropriate meaning of the given idiom.\n\nTo bite the dust",
      ["to be defeated", "to dust the furniture", "to ride a horse fast", "to dig the ground"], 0,
      "Fallen warriors bite the dust — **to fail or be defeated**. The literal dust options are photographable decoys.",
      "Falling face-down = losing.", "easy", "idioms-phrases", "idiom-meaning", 25),
    q("eng-pyq-09", "Select the correctly spelt word.",
      ["Vaccinate", "Vacinate", "Vaccenate", "Vacinete"], 0,
      "Vaccinate has **double c**: vac-cinate (from 'vaccine'). Vacinate drops a c; the other two also distort the ending.",
      "vaccine → vaccinate: keep the cc.", "easy", "spelling", "spelling", 25),
    q("eng-pyq-10", "Select the correctly spelt word.",
      ["Lieutenant", "Leftenant", "Lieutenent", "Lieutinent"], 0,
      "The spelling is **lieutenant**: l-i-e-u-t-e-n-a-n-t. The pronunciation ('lef-') is a spoken quirk; the letters never change.",
      "Write it as lieu + tenant — 'place-holder', its old meaning.", "medium", "spelling", "spelling", 30),
    q("eng-pyq-11", "Select the most appropriate one word for the given expression.\n\nOne who writes the life history of another person",
      ["Biographer", "Autobiographer", "Bibliographer", "Cartographer"], 0,
      "**Biographer** writes another's life; an autobiographer writes his own; a bibliographer lists books; a cartographer draws maps.",
      "bio (life) + grapher (writer); auto = self.", "easy", "one-word-substitution", "ows", 25),
    q("eng-pyq-12", "Select the most appropriate option to fill in the blank.\n\nHe was accused ___ theft by his employer.",
      ["of", "for", "with", "about"], 0,
      "'Accused **of**' is the fixed collocation: accused of theft, murder, cheating. The other prepositions do not collocate with accuse.",
      "accuse of, charge with, suspect of.", "easy", "fill-in-the-blanks", "fill-blank", 25),
    q("eng-pyq-13", "Select the most appropriate option to fill in the blank.\n\nThe soldiers marched ___ enemy territory at dawn.",
      ["into", "in", "at", "onto"], 0,
      "Movement to the inside of an area takes **into**: marched into territory. 'In' marks position, not movement; 'at' gives a point; 'onto' needs a surface.",
      "movement + area = into.", "easy", "fill-in-the-blanks", "preposition", 25),
    q("eng-pyq-14", "Select the part of the sentence that has an error.\n\nOne should do (a) his duty (b) sincerely (c) No error (d)",
      ["One should do", "his duty", "sincerely", "No error"], 1,
      "'One' must be followed by **one's**, never his/her/their, when no person is specified: 'One should do one's duty sincerely.'",
      "one ... one's — the chain never breaks.", "medium", "error-spotting", "error-spot", 30),
    q("eng-pyq-15", "Select the part of the sentence that has an error.\n\nThe flowers (a) smells sweet (b) in the garden at dawn (c) No error (d)",
      ["The flowers", "smells sweet", "in the garden at dawn", "No error"], 1,
      "Plural subject 'flowers' needs the plural verb **smell**: 'The flowers smell sweet.' (Smell here is a linking verb taking an adjective.)",
      "SVA sweep: flowers plural → smell.", "medium", "error-spotting", "error-spot", 30),
    q("eng-pyq-16", "Select the option that will improve the underlined part of the sentence.\n\nThis design is more unique than that one.",
      ["This design is unique", "This design is most unique", "This design is very more unique", "No improvement"], 0,
      "'Unique' means one of a kind — a quality that cannot be graded, so no comparative or superlative is possible: 'This design is unique.'",
      "Absolutes (unique, perfect, complete) reject more/most.", "medium", "sentence-improvement", "improvement", 30),
    q("eng-pyq-17", "Select the option that expresses the given sentence in passive voice.\n\nThey will have finished the work by Friday.",
      ["The work will have been finished by them by Friday.", "The work will have finished by them by Friday.", "The work will been finished by them by Friday.", "The work would have been finished by them by Friday."], 0,
      "Future perfect → **will have been + V3**: 'The work will have been finished by them.' B drops 'been' after will have; C drops 'have'; D shifts the modal to would.",
      "will have + V3 → will have been + V3.", "medium", "active-passive", "active-to-passive", 35),
    q("eng-pyq-18", "Select the option that expresses the given sentence in active voice.\n\nA letter is being written by Ravi.",
      ["Ravi is writing a letter.", "Ravi writes a letter.", "Ravi has written a letter.", "Ravi was writing a letter."], 0,
      "'Is being + V3' is the present continuous passive → active **is + V-ing**: 'Ravi is writing a letter.' B drops the continuous; C and D change the tense.",
      "is being + V3 → is + V-ing.", "easy", "active-passive", "passive-to-active", 30),
    q("eng-pyq-19", "Select the option that expresses the given sentence in indirect speech.\n\nHe said, \"The sun rises in the east.\"",
      ["He said that the sun rises in the east.", "He said that the sun rose in the east.", "He said that the sun had risen in the east.", "He said that the sun is rising in the east."], 0,
      "A universal truth **keeps its tense** even after a past reporting verb: 'The sun rises in the east.' B and C wrongly backshift; D breaks the habitual present.",
      "Truth test: facts of nature freeze.", "medium", "direct-indirect", "narration", 30),
    q("eng-pyq-20", "Choose the correct order of the parts to make a meaningful sentence.\n\n**1.** Teamwork begins with trust. **P:** Members who trust one another share information freely. **Q:** Information sharing prevents costly duplication of work. **R:** Duplicated work, after all, wastes both time and money. **S:** Trust, once broken, is hard to rebuild. **6.** Hence, protect trust above every other resource.",
      ["PQRS", "QPRS", "PRQS", "PSRQ"], 0,
      "**P** develops S1 (trust → sharing) → **Q** (sharing → no duplication) → **R** (why duplication matters) → **S** (the warning about broken trust) just before S6's 'Hence'. PQRS.",
      "Chain the referents: information → duplication → waste; S's warning precedes Hence.", "medium", "sentence-rearrangement", "rearrangement", 50),
]

PYQ_RC_PASSAGE = """When city buses and metro coaches are designed for the average male commuter, half the population is quietly designed out. Women's journeys differ from men's in a pattern transport planners call 'trip chaining': a mother may travel from home to a school, from the school to a workplace, and from the workplace to a market before returning home — three short linked trips where a man makes one direct one. Fare systems that charge per boarding punish exactly this pattern, and buses that run every forty minutes turn a chain of errands into a day's work.

Evidence from several cities shows what happens when services are rethought. Where frequencies improved and fares were made transfer-friendly, women's ridership rose sharply; where stations were lit and staffed, women reported feeling safer travelling after dark, and employment among them measurably increased. Safety, it turns out, is not a separate department from economics: a woman who avoids an evening shift to dodge an unsafe platform is a worker the labour market loses.

None of this requires exotic technology. It requires counting women's trips, pricing transfers sensibly, lighting stations and employing staff — most of it cheaper than the flyovers that dominate transport budgets. What stands in the way is imagination: planners still picture a single commuter moving between home and office at fixed hours. The city that plans for the chained trip instead will find it has planned for children, for the elderly, for anyone whose day is a chain rather than a line."""

def pyq_rc(n, qtext, options, answer, solution, shortcut=None, difficulty="medium", tsec=50):
    if n == 21:
        return q(f"eng-pyq-{n}", qtext, options, answer, solution, shortcut, difficulty,
                 "reading-comprehension", f"rc-{n}", tsec, passage=PYQ_RC_PASSAGE, group="pyq-rc")
    return q(f"eng-pyq-{n}", qtext, options, answer, solution, shortcut, difficulty,
             "reading-comprehension", f"rc-{n}", tsec, group="pyq-rc")

PYQ += [
    pyq_rc(21, "What is the central idea of the passage?",
      ["Transport designed around the single male commute fails women, though practical fixes are cheap and known.", "Women should avoid public transport in the evening.", "Flyovers are the best use of transport budgets.", "Trip chaining is a pattern found only among mothers."], 0,
      "The passage diagnoses male-default design, shows the trip-chaining mismatch, then argues the fixes are simple and cheap. B contradicts the passage's aim; C reverses the budget point; D overstates — the passage uses a mother as an example, not a rule.",
      "Thesis = problem + fix: 'designed out' + 'cheaper than flyovers'.", "medium", 50),
    pyq_rc(22, "In the passage, 'trip chaining' refers to —",
      ["several short linked journeys made in a single day", "tying luggage to the roof of a bus", "a fare system based on the number of boardings", "a direct journey between home and office"], 0,
      "The passage defines it through the mother's example: home → school → workplace → market, 'three short linked trips'. C describes per-boarding fares, the thing that *punishes* chaining; D is the male-pattern journey the passage contrasts it with.",
      "Defined-in-place terms: the dash after the colon carries the definition.", "easy", 45),
    pyq_rc(23, "According to the passage, where stations were lit and staffed, —",
      ["women felt safer after dark and their employment increased", "bus fares were reduced sharply", "men stopped travelling at night", "planners built new flyovers"], 0,
      "The evidence sentence: women 'reported feeling safer travelling after dark, and employment among them measurably increased.' B, C and D are not linked to lighting and staffing anywhere in the passage.",
      "Detail = locate the 'where stations were lit' clause and read forward.", "easy", 45),
    pyq_rc(24, "It can be inferred that per-boarding fare systems are criticised in the passage because they —",
      ["penalise journeys that involve several stops", "are too expensive for single direct trips", "cannot be used on metro coaches", "were designed for children and the elderly"], 0,
      "Charging per boarding punishes the multi-stop chained trip that women typically make — that is the explicit logic ('punish exactly this pattern'). A single direct trip pays once and is unaffected, so B fails; C and D invert the design history.",
      "Pronoun 'this pattern' points back at trip chaining — the answer sits there.", "medium", 50),
    pyq_rc(25, "The expression 'exotic technology' as used in the passage suggests something —",
      ["unusual and elaborate", "foreign-made", "inexpensive", "digitally operated"], 0,
      "'None of this requires exotic technology' means the needed fixes are ordinary and simple — 'exotic' here = **unusual and elaborate**, not imported. The contrast with 'cheaper than the flyovers' confirms the sense of elaborate expense.",
      "Context defines the word: fixes are plain, so exotic = fancy.", "medium", 45),
]

if __name__ == "__main__":
    write_mock("t1-mock-1", M1, 25)
    write_mock("t1-pyq-2025", PYQ, 25)
