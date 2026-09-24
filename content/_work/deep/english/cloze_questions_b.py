# Cloze practice questions, part B: connector-logic and prepositions-phrasals subtopics.
from _lib import QA

QS = []
SUB_C = "cloze-connector-logic"
SUB_P = "cloze-prepositions-phrasals"

# ------------------------------------------------- connector: 2 x 4 + 1 x 3 blanks
PC1 = """The tea stall outside the district hospital has become an unlikely reading point. The owner, Joseph, keeps a shelf of old magazines beside the stove, and customers read them (1) ______ their tea cools. His regulars first laughed at the shelf, (2) ______ today even senior nurses borrow his weeklies. Business has not suffered at all; (3) ______, some customers now order a second cup to finish an article. Nurses say they keep borrowing (4) ______ the magazines remind them of the hospital's own reading room."""
QS += [
 QA("cloze-connector-logic-p01", SUB_C, "clc4", "Select the most appropriate option to fill in blank number (1).",
    ["While", "Until", "Unless", "Before"],
    "Two actions happen at the same time: they read **while** the tea cools. *Until* would need the reading to stop when the tea cools, *unless* adds a condition, and *before* puts the reading earlier — none matches the picture of reading and cooling happening together.",
    "Two overlapping actions → while.", "easy", 35, PC1, "cloze-gc1"),
 QA("cloze-connector-logic-p02", SUB_C, "clc1", "Select the most appropriate option to fill in blank number (2).",
    ["so", "but", "because", "and"],
    "First they laughed at the shelf (−), now even nurses borrow from it (+): the two clauses point in opposite directions → contrast: **but**. *So* would make the laughing the cause of the borrowing, *because* reverses the logic, and *and* hides the turn the writer clearly makes.",
    "Mark each clause + or −; opposite signs → but/yet.", "easy", 35, group="cloze-gc1"),
 QA("cloze-connector-logic-p03", SUB_C, "clc3", "Select the most appropriate option to fill in blank number (3).",
    ["however", "therefore", "moreover", "otherwise"],
    "'Business has not suffered at all; (3) ___, some customers now order a second cup.' Both clauses push the same way (good, then even better), and the semicolon + comma asks for a linking adverb of addition: **moreover**. *However* turns the direction, *therefore* claims a result, *otherwise* adds a condition.",
    "Same direction + semicolon-comma → moreover / furthermore.", "medium", 40, group="cloze-gc1"),
 QA("cloze-connector-logic-p04", SUB_C, "clc2", "Select the most appropriate option to fill in blank number (4).",
    ["because", "until", "although", "unless"],
    "The nurses state their reason for borrowing: '___ the magazines remind them of the hospital's own reading room.' The second clause answers *why* they keep borrowing → **because**. *Until* and *unless* change the logic to time and condition, and *although* would need the borrowing to be surprising — it is not.",
    "If the clause after the blank answers 'why?', choose because/since.", "easy", 35, group="cloze-gc1"),
]
PC2 = """Sales of electric scooters doubled in the city last year, (1) ______ charging remains a headache for flat dwellers. A scooter left at a public charging point after nine at night may stay there (2) ______ morning. Makers are aware of the problem; (3) ______, they have begun bundling a portable charger with every new scooter. Buyers should still check their building's wiring first, (4) ______ old lines sometimes cannot carry the load of an overnight charge."""
QS += [
 QA("cloze-connector-logic-p05", SUB_C, "clc1", "Select the most appropriate option to fill in blank number (1).",
    ["so", "but", "because", "and"],
    "Sales doubled (+ growth) ___ charging is a headache (− problem): the second clause turns against the first → **but**. *So* would wrongly make charging trouble a *result* of rising sales being good news, and *because* reverses cause and effect.",
    "Good news vs bad news in one sentence → contrast.", "easy", 35, PC2, "cloze-gc2"),
 QA("cloze-connector-logic-p06", SUB_C, "clc4", "Select the most appropriate option to fill in blank number (2).",
    ["until", "since", "after", "by"],
    "The scooter is left at night and stays there up to a time limit: 'may stay there **until** morning'. *Since* needs a starting point ('since nine o'clock'), *after* would put its stay after the morning, and *by* fits a deadline ('finish by morning'), not a continuing state.",
    "A state continuing up to a point → until.", "medium", 40, group="cloze-gc2"),
 QA("cloze-connector-logic-p07", SUB_C, "clc3", "Select the most appropriate option to fill in blank number (3).",
    ["therefore", "nevertheless", "moreover", "instead"],
    "'Makers are aware of the problem; (3) ___, they have begun bundling a portable charger.' The second clause adds to the first (aware, and here is their further step) → addition: **moreover**. *Therefore* would make the bundling a logical conclusion of mere awareness, *nevertheless* signals contrast, *instead* signals replacement.",
    "Second clause extends the first → moreover; check the semicolon-comma frame.", "hard", 40, group="cloze-gc2"),
 QA("cloze-connector-logic-p08", SUB_C, "clc2", "Select the most appropriate option to fill in blank number (4).",
    ["because", "until", "unless", "while"],
    "'Check your building's wiring first, (4) ___ old lines sometimes cannot carry the load.' The second clause gives the *reason* for the advice → **because**. *Unless* would flip it into a condition with the wrong result, *until* is time, and *while* would mean the checking happens during the failing.",
    "Advice + reason behind it → because.", "medium", 35, group="cloze-gc2"),
]
PC3 = """The hill temple at Pachaimalai banned plastic bags five years ago, and the change began at the gate. (1) ______ the staff exchanged a cloth bag for every plastic one handed over at the gate, visitors slowly gave up carrying plastic altogether. (2) ______ the ban, monkeys used to scatter torn plastic along the paths; the slopes are clean now, and pilgrims often photograph them. The ban has even spread beyond the temple; (3) ______, the village panchayat passed a similar rule for its weekly market."""
QS += [
 QA("cloze-connector-logic-p09", SUB_C, "clc2", "Select the most appropriate option to fill in blank number (1).",
    ["Because", "Although", "Unless", "Until"],
    "The exchange scheme is the *cause* of the change: because every plastic bag was swapped for a cloth one, visitors stopped bringing plastic at all. The main clause ('visitors slowly gave up…') is the direct result of the scheme, so **Because** fits. *Although* would claim the scheme did not stop them — yet the visitors asked for the cloth bags themselves, which is the scheme working, not failing.",
    "Ask: is the main clause the working of the first clause (because) or a surprise against it (although)?", "hard", 45, PC3, "cloze-gc3"),
 QA("cloze-connector-logic-p10", SUB_C, "clc4", "Select the most appropriate option to fill in blank number (2).",
    ["Before", "After", "Although", "Because"],
    "'___ the ban, monkeys used to scatter torn plastic along the paths; the slopes are clean now.' The monkeys' habit belongs to the time **before** the ban — the second half states the present. *After* reverses the order, and the logic connectors cannot place events on a clock.",
    "'used to' marks a past habit; place it before the stated change.", "medium", 40, group="cloze-gc3"),
 QA("cloze-connector-logic-p11", SUB_C, "clc3", "Select the most appropriate option to fill in blank number (3).",
    ["moreover", "instead", "otherwise", "meanwhile"],
    "'The ban has even spread beyond the temple; (3) ___, the village panchayat passed a similar rule.' The panchayat rule is one more step in the same direction → addition: **moreover**. *Instead* would replace the temple ban, *otherwise* sets a condition, and *meanwhile* only says two things happened at the same time without adding the writer's point.",
    "'even spread beyond' signals a further, supporting point → moreover.", "hard", 45, group="cloze-gc3"),
]

# ------------------------------------------------- prepositions/phrasals: 3 x 4 blanks
PP1 = """Every June the municipal office on the fourth floor turns into a monsoon war room. The control room answers complaints round the clock (1) ______ the monsoon, and staff keep sandbags ready for the low-lying ward. The executive engineer insists that drains must be desilted (2) ______ the first showers arrive, not after them. Contractors who delay the work are fined (3) ______ of repeated warnings. Residents can now report a blocked drain by phone, and the office responds (4) ______ every complaint within a day."""
QS += [
 QA("cloze-prepositions-phrasals-p01", SUB_P, "clp2", "Select the most appropriate option to fill in blank number (1).",
    ["during", "within", "since", "among"],
    "The control room answers complaints round the clock **during** the monsoon — right through that period. *Within* needs a length ('within a month'), *since* needs a starting point with a perfect tense, and *among* takes a plural group, not a season.",
    "Period through which something continues → during.", "easy", 35, PP1, "cloze-gp1"),
 QA("cloze-prepositions-phrasals-p02", SUB_P, "clp2", "Select the most appropriate option to fill in blank number (2).",
    ["before", "after", "since", "during"],
    "The sentence ends 'not after them', so the blank must be the opposite: drains are desilted **before** the first showers arrive. The sentence itself gives the contrast pair, which makes this a free mark if you read to the end of the clause.",
    "Read to the end of the clause — 'not after them' hands you the answer.", "easy", 30, group="cloze-gp1"),
 QA("cloze-prepositions-phrasals-p03", SUB_P, "clp4", "Select the most appropriate option to fill in blank number (3).",
    ["due", "in spite", "instead", "ahead"],
    "The fixed phrase is **in spite of** repeated warnings = although they were warned many times. *Due of* does not exist (*due to* has no 'of'); 'fined instead of repeated warnings' and 'ahead of repeated warnings' make no sense — the sentence concedes the warnings and still imposes the fine.",
    "'___ of' + a concession meaning → in spite of.", "hard", 40, group="cloze-gp1"),
 QA("cloze-prepositions-phrasals-p04", SUB_P, "clp1", "Select the most appropriate option to fill in blank number (4).",
    ["to", "for", "on", "at"],
    "The fixed pair is **respond to**: 'the office responds to every complaint'. *Respond for*, *respond on* and *respond at* are not English. Spot the verb before the blank and its partner preposition follows automatically.",
    "respond → to. Learn the pair.", "easy", 30, group="cloze-gp1"),
]
PP2 = """Suresh delivers parcels by day and studies for the bank examination by night. He is not ashamed (1) ______ his timetable: thirty minutes of maths on the bus, an hour of English after dinner. His wife manages the accounts of a small jeweller, and the couple rarely watch television (2) ______ Sundays. Suresh has applied (3) ______ three banks so far and keeps a diary of every exam date. His friends laugh at the diary, but he says a man who cannot put (4) ______ small pleasures for a year does not deserve a big one."""
QS += [
 QA("cloze-prepositions-phrasals-p05", SUB_P, "clp1", "Select the most appropriate option to fill in blank number (1).",
    ["of", "for", "with", "from"],
    "The fixed pair is **ashamed of**: 'not ashamed of his timetable'. *Ashamed for*, *ashamed with* and *ashamed from* are not English. The adjective before the blank fixes the preposition.",
    "ashamed → of.", "easy", 30, PP2, "cloze-gp2"),
 QA("cloze-prepositions-phrasals-p06", SUB_P, "clp2", "Select the most appropriate option to fill in blank number (2).",
    ["in", "on", "at", "within"],
    "'The couple rarely watch television ___ Sundays.' Sundays are days of the week, and days take **on**: on Sunday, on Sundays. *In* takes longer periods (in June), *at* takes clock points (at 8 p.m.), *within* takes a length of time.",
    "Day of the week → on.", "easy", 30, group="cloze-gp2"),
 QA("cloze-prepositions-phrasals-p07", SUB_P, "clp1", "Select the most appropriate option to fill in blank number (3).",
    ["to", "for", "on", "at"],
    "**Apply to** an organisation, **apply for** a post. The blank is followed by 'three banks' — organisations — so: **to**. ('He has applied for the clerical post' would use *for*, because a post is the thing requested.)",
    "Organisation after the blank → apply to; post → apply for.", "medium", 40, group="cloze-gp2"),
 QA("cloze-prepositions-phrasals-p08", SUB_P, "clp3", "Select the most appropriate option to fill in blank number (4).",
    ["off", "down", "up", "in"],
    "Needed meaning: delay or postpone enjoying small pleasures → **put off**. *Put down* means place or write, *put up* means erect (or tolerate, with 'with'), *put in* means install or invest. The particle decides the meaning, so decide the meaning first.",
    "Translate the need ('postpone') → put off.", "medium", 40, group="cloze-gp2"),
]
PP3 = """The lake behind the sugar mill had become a grey pond that smelled (1) ______ chemicals. Three years ago the villagers formed a committee and decided to set (2) ______ a small fund for desilting the lake bed. Fish returned the following spring. The committee now guards the lake strictly: anyone caught dumping waste must pay a fine, and cattle are kept away (3) ______ the shallow edge by a low stone fence. (4) ______ the committee's records, the lake has not gone dry even once since the desilting."""
QS += [
 QA("cloze-prepositions-phrasals-p09", SUB_P, "clp1", "Select the most appropriate option to fill in blank number (1).",
    ["of", "with", "from", "by"],
    "The fixed pair is **smell of**: 'a grey pond that smelled of chemicals' = had the smell of chemicals. *Smelled with*, *smelled from* and *smelled by* are not English in this sense.",
    "smell → of (like taste of, reek of).", "easy", 30, PP3, "cloze-gp3"),
 QA("cloze-prepositions-phrasals-p10", SUB_P, "clp3", "Select the most appropriate option to fill in blank number (2).",
    ["up", "off", "out", "in"],
    "Needed meaning: start or establish something → **set up** a fund. *Set off* means begin a journey or trigger, *set out* means set forth or present, *set in* means begin and settle (of weather or decay). The villagers created the fund, so 'set up'.",
    "'Create a fund' → set up.", "easy", 35, group="cloze-gp3"),
 QA("cloze-prepositions-phrasals-p11", SUB_P, "clp2", "Select the most appropriate option to fill in blank number (3).",
    ["from", "off", "at", "beyond"],
    "The fixed expression is **(keep) away from**: cattle are kept away **from** the shallow edge. 'Away off', 'away at' and 'away beyond' are not the idiom; the sentence already supplies 'away', and 'away' pairs with *from*.",
    "away → from. Read the whole phrase around the blank.", "medium", 35, group="cloze-gp3"),
 QA("cloze-prepositions-phrasals-p12", SUB_P, "clp4", "Select the most appropriate option to fill in blank number (4).",
    ["According", "Owing", "In spite", "Along"],
    "The sentence cites a source of information: '___ the committee's records, the lake has not gone dry…' The phrase for quoting a source is **according to**. *Owing to* means because of (and would make the records the cause of the lake's health), *in spite of* contradicts the logic, *along the records* is not a phrase.",
    "Blank + 'the records' + a reported fact → According to.", "hard", 45, group="cloze-gp3"),
]
