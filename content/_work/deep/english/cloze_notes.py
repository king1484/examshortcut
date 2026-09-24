# Notes + patterns for cloze-test subtopics. Imported by cloze-test.py.
from _lib import P

S = {}

S["cloze-strategy"] = {
"notes": r"""### What is a cloze test?
A cloze test is a short passage — usually 80 to 150 words — in which several words are removed and numbered (1), (2), (3)… For every blank you get four options, and you pick the word that best fits **both the grammar and the meaning** of that place. SSC, Railway and Banking papers commonly ask 5 blanks from one passage, each blank as a separate question that shares the same story.

A cloze passage is like a wall with a few bricks missing. You cannot choose a brick by looking at the hole alone — you must look at the wall around it.

### The five-step routine
1. **Read the whole passage once**, ignoring the options. Fix the theme (a village lake, a new rule, an old memory) and the time frame (past story, present habit, future plan).
2. **Read the sentence with the blank twice** — the part before the blank and the part after it. The clue usually sits on one of these two sides.
3. **Try every option inside the full sentence**, never as a word alone. A word may look right on its own and break the sentence.
4. **Reject in two rounds.** First cut options that break a rule (wrong verb form, wrong agreement). Then cut options that are grammatical but do not fit the meaning.
5. **Re-read the finished passage** with your answers filled in. The whole thing must sound like natural English from the first line to the last.

### The four kinds of blanks
| Blank type | What decides the answer |
|---|---|
| Grammar (verb form, agreement, article, pronoun) | A rule: subject number, time frame, linking verb |
| Vocabulary (noun, verb, adjective choice) | Meaning and collocation |
| Connector (but, because, moreover) | The direction between two clauses |
| Preposition / phrasal verb | A fixed usage or the particle's meaning |

Most papers mix all four kinds in one passage, so one passage tests four small skills.

### Order of solving
Answer the easiest blank first, even if it is blank (5). A solved blank often makes its neighbours easier, because one more slot of the story is filled. Leave a stubborn blank for the last round; with most of the passage filled, it usually resolves itself. Mark skipped blanks on the question paper so you do not lose count.

### A worked blank
Blank: "The morning walk costs nothing and demands no equipment, (1) ______ very few people manage to continue it beyond a fortnight."
Options: because / yet / hence / so.
The first clause praises the walk (+), the second says few continue it (−). Opposite directions need a contrast word: **yet**. *So* and *hence* would wrongly make failure a result of the walk's simplicity, and *because* reverses the logic. This is the connector decision in action.

### Traps that cost marks
- **Right grammar, wrong meaning**: all four options may be verbs in the correct form; only one matches the sentence's sense.
- **Right meaning, wrong form**: the word you want appears in a wrong shape (*develop* instead of *develops*).
- **Local fit, passage clash**: an option may fit its own sentence and still contradict a line two sentences later — for example, a "problem" the passage has already solved.
- **Ignoring the time frame**: if the story is set in the past ("Last year…"), a present-tense option is wrong even if it sounds fine.

### Time plan
Five blanks should take four to five minutes. Never spend more than a minute on one blank in the first round.

### Quick revision
- Read the full passage before touching the options.
- Try each option inside the full sentence.
- Grammar blanks → rule; vocab blanks → meaning; connectors → clause direction; prepositions → fixed usage.
- Solve easy blanks first, re-read at the end.
- Two rounds of elimination: form first, then meaning.
""",
"patterns": [
 P("cls1", "Blank whose answer needs the passage's overall theme", "common",
   "Several options are grammatical and each could fit some sentence; only one continues the passage's controlling idea or metaphor.",
   "1. Read the whole passage and name its theme in five words.\n2. Ask which option keeps that theme running in this sentence.\n3. Cut options that are real words but belong to a different world (an office word in a farming story).\n\n*Why it works:* a cloze passage is one connected story; the writer keeps one metaphor or topic alive, and the blank is part of it.",
   "Passage about a night market: \"The market sells food, but what it really (1) ______ is company.\" (a) paints (b) sells (c) measures (d) imports",
   "The passage's metaphor is selling. \"Sells company\" continues it. Answer: **(b) sells**."),
 P("cls2", "All four options grammatical — meaning decides", "very common",
   "Every option is the same part of speech in the correct form, so no rule can cut them.",
   "1. Read the sentence and say its meaning in your own words.\n2. Put each option in the blank and read the full sentence.\n3. Keep the one that says what the sentence actually says; cut options that are merely about the same topic.\n\n*Why it works:* when grammar is equal, the setter is testing careful reading, not vocabulary size.",
   "\"Students check the taps after (1) ______ and repair dripping ones the same day.\" (a) applause (b) assembly (c) gravity (d) thunder",
   "Only *assembly* is a school event that happens before students could check taps. Answer: **(b) assembly**."),
 P("cls3", "The clue sits in a neighbouring sentence", "very common",
   "The blank's own sentence feels incomplete; the word that fits is confirmed one sentence earlier or later.",
   "1. Read the sentence before AND after the blank.\n2. Look for a repeated idea or word pair (tankers, then a single tanker again).\n3. Choose the option that completes that cross-sentence link.\n\n*Why it works:* cloze passages are short, so writers deliberately repeat or answer ideas one line apart.",
   "\"The school used to buy tankers of water every summer. … This summer it did not order a single (1) ______.\" (a) ticket (b) book (c) tanker (d) rule",
   "Sentence 1 sets the pair *buy tankers → order a single tanker*. Answer: **(c) tanker**."),
 P("cls4", "Option fits the sentence but clashes with the passage", "common",
   "Two options seem to fit the blank; re-reading another line shows one of them contradicts the story.",
   "1. Do not answer on the first plausible option.\n2. Re-read the full passage with each survivor filled in.\n3. Drop the option that clashes with a later or earlier line.\n\n*Why it works:* the setter places a 'local' option that ignores the whole story; the final re-read catches it.",
   "\"The tank taught them what the (1) ______ never did — that water is counted.\" The passage is about school students. (a) plumber (b) syllabus (c) generator (d) noticeboard",
   "Only a syllabus is something that *teaches* in a school. Re-reading shows the lesson is academic, not a plumbing job. Answer: **(b) syllabus**."),
]}

S["cloze-grammar-fit"] = {
"notes": r"""### Grammar blanks: what is really tested
In most cloze passages, three or four of the five blanks are decided by a grammar rule, not by word power. The passage fixes a setting — time, subject, structure — and the blank must obey it. Learn the six checks below and most grammar blanks answer themselves.

### 1. Subject-verb agreement
Find the true subject — the noun the verb belongs to — and ignore the words packed between it and the verb.
- Correct: The quality of the mangoes **is** poor. Incorrect: The quality of the mangoes **are** poor. (subject = quality)
- Correct: Every one of the players **was** tired. Incorrect: Every one of the players **were** tired. (*each, every, either, neither, one of + plural noun* take a singular verb)
- Correct: The list of items **is** on the table. Incorrect: The list of items **are** on the table.

### 2. The time frame (tense)
The first sentence usually sets the tense for the whole passage, and every verb must stay inside that frame.
- "When Arun was small…" → past narrative → Correct: he **drafted** a reply. Incorrect: he **drafts** a reply.
- Habits and general truths → simple present: Correct: The shop **opens** at nine. Incorrect: The shop **opened** at nine (in a habitual passage).
- Signal words: *yesterday, last year, ago* → past; *now, still, these days, every morning* → present; *since, for, already, yet* → perfect forms.
- But a habit inside a past story can stay past: "Every evening he **made** new kites" (past habit of that story).

### 3. Verb forms: finite, gerund, infinitive
Only a finite verb can act as the main verb. After certain words, a non-finite form is compulsory:
- *enjoy, avoid, mind, finish, suggest, keep* + **-ing**: Correct: He enjoys **showing** old kites. Incorrect: He enjoys **to show** old kites.
- *decide, plan, hope, refuse, manage, teach someone* + **to + base form**: Correct: Gardening has taught him **to be** patient. Incorrect: Gardening has taught him **being** patient.
- *preposition + -ing*: Correct: She is good **at solving** puzzles. Incorrect: She is good **at to solve** puzzles.
- A bare -ing form cannot serve as the finite verb: Incorrect: A group **developing** its own discipline. Correct: A group **develops** its own discipline.

### 4. Articles: a, an, the
- **a/an** = first mention or one of many: He gave him **a** bucket the very next day.
- **the** = already known, or one of a kind: **The** sky above the lane was full of kites.
- No article for most plural or general nouns: Correct: **Trees give shade.** Incorrect: **The trees give shade** (when trees in general are meant).
- a + consonant sound, an + vowel sound: **a university** (yoo-sound), **an hour** (silent h).

### 5. Adjective or adverb?
After a linking verb (*be, look, seem, feel, taste, smell, sound*) use an adjective:
- Correct: The tree looks **attractive**. Incorrect: The tree looks **attractively**.
- After an action verb use an adverb: Correct: She sings **beautifully**.

### 6. Pronouns
A pronoun must match its noun in number and gender, and its case must fit the job — subject (*I, he, they*), object (*me, him, them*), possessive (*my, his, their*).
- Correct: The committee published **its** report. Incorrect: The committee published **their's** report.
- Correct: Between you and **me**, the plan is weak. Incorrect: Between you and **I**, the plan is weak.

### Quick revision
- Find the true subject first; ignore the words between it and the verb.
- Fix the passage's time frame, then keep every verb inside it.
- enjoy/avoid + -ing; decide/refuse/teach + to; preposition + -ing.
- a/an = first mention; the = known or one-of-a-kind.
- Linking verb + adjective; action verb + adverb.
- Pronoun = same number and gender as its noun, right case for the job.
""",
"patterns": [
 P("clg1", "Subject-verb agreement blank", "very common",
   "The options are forms of the same verb (give/gives/gave) and the sentence has a long subject phrase or an each/every/one-of structure.",
   "1. Cross out the phrase between the subject and the verb.\n2. Ask: is the true subject singular or plural?\n3. Match the verb, then check the passage's time frame (present or past).\n\n*Why it works:* the setter hides the subject behind a prepositional phrase so that the nearest noun misleads you.",
   "\"The soil in his yard (1) ______ too rocky for beds.\" (a) is (b) are (c) were (d) be",
   "True subject = soil (singular), passage is in present → **is**. *Are* is pulled by the nearby plural feel; *were* breaks the present frame."),
 P("clg2", "Tense / time-frame blank", "very common",
   "The options are the same verb in different tenses and the passage has a clear anchor: 'Last January', 'now', 'every morning'.",
   "1. Find the time anchor of the sentence or passage.\n2. Past anchor → simple past; habit in the story → past habitual; present anchor (now, still) → simple present.\n3. Never let one verb drift out of the passage's frame.\n\n*Why it works:* narratives hold one tense; a wrong-tense option sounds fine alone but breaks the story.",
   "\"Last January the terrace became a workshop. Every evening he and his son (1) ______ new kites.\" (a) made (b) make (c) making (d) maker",
   "Anchor 'Last January' → past narrative, habitual 'every evening' → simple past: **made**. *Make* breaks the frame; *making* is not finite."),
 P("clg3", "Verb form: gerund or infinitive after another word", "common",
   "The blank follows a verb like enjoy/avoid or decide/teach, or follows a preposition.",
   "1. Identify the word before the blank.\n2. enjoy, avoid, mind, finish, suggest → -ing form.\n3. decide, hope, refuse, manage, teach someone → to + base form.\n4. After a preposition → -ing form.\n\n*Why it works:* these verbs and prepositions fix the form of the next verb; no meaning decision is needed.",
   "\"He enjoys (1) ______ old kites to the children of the lane.\" (a) showing (b) show (c) to show (d) showed",
   "*Enjoy* takes the -ing form: **showing**. 'Enjoys to show' is wrong in English."),
 P("clg4", "Article / determiner blank", "common",
   "The options are a, an, the (or their capital forms) before a noun.",
   "1. Ask if the noun is already known or one of a kind → the.\n2. First mention, one of many → a/an (an before a vowel SOUND).\n3. General plural or uncountable idea → no article, so pick the option that works as a zero article if offered.\n\n*Why it works:* article choice follows three simple conditions; the sentence usually makes one condition obvious.",
   "\"On festival day (1) ______ sky above the lane was so full of kites that the birds kept their distance.\" (a) A (b) An (c) The (d) Some",
   "There is one sky above the lane and the phrase adds 'above the lane' (already specific): **The**. 'A sky' would mean one of several skies."),
]}

S["cloze-vocab-fit"] = {
"notes": r"""### Vocabulary blanks: meaning in context
A vocabulary blank gives four options that are all grammatically correct. No rule can save you here — only the sentence's meaning can. The skill is reading the sentence closely enough that the missing word almost appears by itself.

### Where the clue sits
Usually in the same sentence; sometimes in the next one.
- Same sentence: "Benefits depend almost entirely on (1) ______; twenty minutes on Sunday cannot undo six days of sitting." The clause after the semicolon *defines* the answer — the idea of doing something again and again → **regularity**.
- Next sentence: "The traders did not take the plan lying down. They collected signatures…" The second sentence tells you the first blank needs a resistance word.

### Collocations decide many blanks
Some words travel together so firmly that the pair is one unit:
- **take** advantage, **take** pride, **take** a decision
- **make** room, **make** a mistake, **make** progress
- **pay** attention, **pay** a fine, **pay** a visit
- **keep** a promise, **keep** records, **break** a rule
If the blank is half of such a pair, the collocation decides, and the other three options die at once — however sensible they sound alone. Correct: She **took** full advantage of the offer. Incorrect: She **did** full advantage of the offer.

### The tone test
Decide whether the sentence praises or blames, hopes or fears. The word must carry the same feeling.
- "Doctors praised the ___ results" → positive: **remarkable**, not *dreadful*.
- "Officials are tempted to ___ corners" → negative: **cut**, not *decorate*.
A grammatically perfect option with the wrong tone is a classic trap.

### Near-synonyms are not equal
Options are often close: *quality / standard / character / grade*, or *preserve / protect / defend*. Compare them against the exact noun in the sentence: "the quiet here has a different ___" → quiet has a **quality**, not a standard or grade. When two options both fit, check which one the passage's level of language matches — a plain narrative does not suddenly use an official word.

### The elimination method for vocab blanks
1. Mark each option + (fits), − (wrong meaning), ? (possible).
2. Keep the + options; a ? option must be justified by a clear clue, not by hope.
3. If two survive, plug both into the WHOLE passage — the passage usually rejects one.

### Worked example
Blank: "Pleased by the response, the corporation has sanctioned two more fans, and the students (1) ______ full advantage of the extended hours." Options: make / do / take / give.
The collocation is **take advantage of**. Answer: take. *Do* and *make* are the classic Indian-English trap for this pair.

### Quick revision
- Vocab blanks are decided by meaning, collocation and tone — not by grammar.
- The clue is usually in the same sentence; read the next one too.
- Learn pairs: take advantage, make room, pay attention, keep a promise.
- Match the sentence's feeling: praise word in a praising line.
- Near-synonyms: test each against the exact noun in the sentence.
- Two survivors → plug both into the whole passage.
""",
"patterns": [
 P("clv1", "Noun choice by context", "very common",
   "All four options are singular/plural nouns that fit the grammar; the sentence's meaning and the surrounding idea pick one.",
   "1. Say the sentence's message in your own words.\n2. Ask which noun names that message exactly.\n3. Cut nouns that belong to the topic but not to this sentence.\n\n*Why it works:* the setter chooses three nouns from the same broad field; only one matches the precise idea.",
   "\"Regulars say the quiet here has a different (1) ______ from the quiet of their homes.\" (a) price (b) quality (c) length (d) colour",
   "The passage contrasts two kinds of quiet — their character differs. Quiet has a **quality**, not a price or length. Answer: **(b) quality**."),
 P("clv2", "Verb choice by context", "very common",
   "Four verbs, all grammatical after the subject; meaning and the object of the verb decide.",
   "1. Find the verb's object and the sentence's logic.\n2. Ask what action the story describes here.\n3. Plug each verb in with its object and keep the one that makes a real action.\n\n*Why it works:* wrong verbs are from the same field but name a different action (publish vs preserve).",
   "\"The librarian has also begun to (1) ______ old newspapers for a small archive.\" (a) publish (b) preserve (c) repair (d) translate",
   "The archive keeps old papers safe → **preserve**. Publishing makes new copies; repairing fixes damage; translating changes language — none is 'store for the future'."),
 P("clv3", "Adjective choice by tone and contrast", "common",
   "Four adjectives fit before the noun; the sentence's feeling or a contrast word (once…now, but) picks one.",
   "1. Look for a contrast signal (once, now, but, although).\n2. Choose the adjective that sits on the other side of the contrast.\n3. Check the tone: praise line → positive adjective.\n\n*Why it works:* contrast sentences demand opposite poles; only one option stands opposite the stated pole.",
   "\"The reading hall, once half (1) ______, is now full by eight o'clock.\" (a) painted (b) carpeted (c) empty (d) furnished",
   "Contrast: once half ___ → now full. The opposite of full is **empty**. Painted/carpeted/furnished do not stand against 'full'."),
 P("clv4", "Collocation blank (verb + fixed noun)", "common",
   "The blank completes a set phrase: take advantage, make room, pay attention, keep a promise.",
   "1. Read the noun that follows the blank.\n2. Recall the fixed partner verb for that noun.\n3. Do not translate from your mother tongue — Indian English often swaps make/do/take.\n\n*Why it works:* collocations are conventions, not logic; only the conventional partner is correct.",
   "\"The traders now (1) ______ room for her boards every Sunday morning.\" (a) do (b) take (c) make (d) give",
   "The fixed phrase is **make room for** = clear space for. 'Do room', 'take room' are not English; 'give room' would need 'to someone' in a different sense."),
]}

S["cloze-connector-logic"] = {
"notes": r"""### Connector blanks: one logic decision
A connector blank joins two clauses, and your only job is to find the **direction** between them: same way or opposite way, cause or result, one event after another. The connector is logic written as a single word.

### Step 1: find the two clauses
Read the words on both sides of the blank and compress each side into a sign:
- "The walk costs nothing **(+)**, ___ very few continue it **(−)**" → opposite directions → contrast.
- "It rained heavily **(+cause)**, ___ the match was cancelled **(−result)**" → cause and result.
- "Prices rose **(point 1)**, ___ wages stayed flat **(point 2)**" → the writer adds a second, parallel point.
- "She finished her homework **(event 1)**, ___ the lights went out **(event 2)**" → time order or overlap.

### Step 2: pick the family, then the word
| Family | Direction | Members often seen |
|---|---|---|
| Contrast | the two clauses pull apart | but, yet, however, whereas, although, while |
| Result | A happened, so B happened | so, therefore, hence, thus, as a result |
| Reason | B is why A happened | because, since, as, for |
| Addition | a second, supporting point | moreover, furthermore, besides, also, in addition |
| Time | events in order or overlap | when, while, before, after, until, as soon as |
| Condition | one depends on the other | if, unless, provided |

### Step 3: use the punctuation clue
- A semicolon or full stop, then a comma after the blank → a linking adverb: **however, moreover, therefore, otherwise**. ("Business has not suffered; **moreover**, some customers order a second cup.")
- A comma inside one sentence joining two clauses → **but, so, because, and**.
- Beginning of a second sentence → the connector often looks back at the whole first sentence.

### Common confusions
- **but vs so**: "The shop is small, ___ it is always full." → but (opposite). "The road was cleared, ___ traffic flowed again." → so (result).
- **because vs although**: "___ it rained, the match went on." → Although (surprising result). "___ it rained, the match was cancelled." → Because (normal result).
- **while**: two meanings — time overlap ("read **while** the tea cools") and contrast ("cities grew rich, **while** villages lagged").
- **until**: an action continues up to a time point: "He waited **until** morning."

### Method in the exam
1. Read both sides of the blank; write + or − over each.
2. Same direction → addition, result or time; opposite → contrast; effect needs a cause → reason.
3. Try the chosen word: the finished sentence must sound like something a newspaper would print.

### Quick revision
- Connector = the direction between two clauses; find the clauses first.
- Contrast: but, yet, however, although, whereas. Result: so, therefore, hence. Reason: because, since. Addition: moreover, besides. Time: when, while, until, before.
- Semicolon + comma → however/moreover/therefore/otherwise.
- because vs although: normal result vs surprising result.
- Test the word by reading the full joined sentence aloud.
""",
"patterns": [
 P("clc1", "Contrast connector (but, yet, although, whereas)", "very common",
   "The clause before and after the blank point in opposite directions, or the second clause surprises you after the first.",
   "1. Compress each clause to a sign: + or −, advantage or disadvantage.\n2. Opposite signs → contrast family.\n3. Choose the member that fits the punctuation: mid-sentence comma → but/yet/although; new sentence → however; two parallel facts → whereas.\n\n*Why it works:* contrast is the commonest single logic in short passages; every other option breaks one side of the pair.",
   "\"His regulars first laughed at the shelf, (1) ______ today even senior nurses borrow his weeklies.\" (a) so (b) but (c) because (d) and",
   "Laughed (−) → borrow now (+): opposite directions → **but**. *So* would make laughing the cause of borrowing."),
 P("clc2", "Reason connector (because, since, as)", "very common",
   "One clause gives the cause and the other the effect; the blank sits before the cause part (or the question 'why?' fits between the clauses).",
   "1. Ask which clause answers 'why' for the other.\n2. If the blank introduces the why-clause → because/since/as.\n3. Reject result words (so, therefore) — they would reverse the direction.\n\n*Why it works:* learners confuse reason and result; the test is which clause could be the answer to 'why'.",
   "\"Nurses borrow the weeklies (1) ______ the magazines remind them of the hospital's own reading room.\" (a) unless (b) although (c) because (d) until",
   "The second clause explains the borrowing: **because**. *Although* needs a surprise, not a reason."),
 P("clc3", "Addition connector (moreover, furthermore, besides)", "common",
   "The second sentence or clause adds another point of the same kind — usually after a semicolon, then a comma.",
   "1. Check that both clauses push the same way (both benefits or both problems).\n2. Semicolon + comma → linking adverb: moreover, furthermore, in addition.\n3. Reject contrast and result words; the writer is agreeing with himself, not turning.\n\n*Why it works:* passages list two or three supports for one claim; the addition connector is the join.",
   "\"Business has not suffered at all; (1) ______, some customers now order a second cup to finish an article.\" (a) however (b) therefore (c) moreover (d) otherwise",
   "Same direction (business fine, then even better) → **moreover**. *However* turns, *therefore* claims a result."),
 P("clc4", "Time connector (while, until, before, after, when)", "common",
   "The two clauses describe events placed on a clock — overlapping, or one ending at a point.",
   "1. Ask how the two events sit in time: together, one before the other, or up to a limit.\n2. Overlapping actions → while/when; continues up to a point → until; earlier vs later → before/after.\n3. Plug the word in and check the clock reading of the sentence.\n\n*Why it works:* time words are precise; each option places the events differently, and only one matches the story.",
   "\"A scooter left at a public charging point after nine at night may stay there (1) ______ morning.\" (a) until (b) since (c) after (d) by",
   "The scooter waits from night up to a limit point: **until** morning. *Since* needs a starting point, *after* reverses the order."),
]}

S["cloze-prepositions-phrasals"] = {
"notes": r"""### Preposition blanks: fixed pairs
English fixes a preposition to many verbs, adjectives and nouns, and logic rarely helps — the pair is a convention. The blank is usually the second half of such a pair, so your real task is to spot the first half and recall its partner.

### High-frequency fixed pairs
| First half | Correct pair | Wrong pair to avoid |
|---|---|---|
| ashamed | ashamed **of** | ashamed for |
| respond | respond **to** | respond on |
| apply (organisation) | apply **to** a bank | apply on |
| apply (post) | apply **for** a post | apply to a post |
| depend | depend **on** | depend from |
| prevent | prevent **from** + -ing | prevent to |
| insist | insist **on** + -ing | insist to |
| smell / taste | smell **of** garlic | smell with |
| arrive | arrive **at** a place, **in** a city | arrive to |
| married | married **to** | married with |
| according | according **to** records | according with |
| in spite | in spite **of** | in spite from |

### Prepositions of time: in, on, at
- **at** a clock or point: at 6 p.m., at noon, at night.
- **on** a day or date: on Sunday, on 15 August, on Sunday morning.
- **in** a longer period: in June, in 2019, in the morning, in winter.
- Duration with *since/for* with perfect tenses: since 2020 (point), for five years (length).

### Prepositions of place
- **at** a point on the map: at the bus stop, at the gate.
- **in** an enclosed space or area: in the room, in Erode, in India.
- **on** a surface or line: on the table, on the riverbank, on the wall.
- *away from*, *out of*, *into* show direction: cattle kept **away from** the edge.

### Phrasal verbs: the particle is the meaning
A phrasal verb = verb + particle, and the particle changes the meaning completely:
- **look after** = take care of; **look into** = investigate; **look down upon** = despise; **look up to** = admire.
- **put off** = postpone; **put down** = place / write; **put up with** = tolerate.
- **set up** = establish; **set out** = begin a journey; **set aside** = save or discard.
- **carry out** = perform; **carry on** = continue.
In the exam, translate the sentence's need into a meaning ("take care of the trees") and then find the phrasal verb with that meaning — never accept a phrasal verb just because it contains a familiar verb.

### Method for these blanks
1. Read the word before the blank (verb/adjective/noun) and the phrase after it.
2. If a fixed pair exists, the pair decides — no meaning test needed.
3. If it is a phrasal verb, state the needed meaning first, then match the particle.
4. For time/place, classify the noun: clock/point → at, day → on, period/enclosure → in.

### Quick revision
- Fixed pairs decide: ashamed of, respond to, depend on, married to, according to, in spite of.
- apply **to** an organisation, apply **for** a post.
- at a point, on a day, in a period or enclosure.
- Phrasal verb: decide the meaning first, then the particle (look after ≠ look into).
- Never translate prepositions from your mother tongue.
""",
"patterns": [
 P("clp1", "Preposition after a verb or adjective (fixed pair)", "very common",
   "The blank follows a word like ashamed, respond, insist, smell and the options are single prepositions.",
   "1. Identify the word before the blank.\n2. Recall its fixed preposition (ashamed of, respond to, insist on).\n3. Check the object after the blank — some words take different prepositions for different objects (apply TO a bank, apply FOR a post).\n\n*Why it works:* the pair is a convention; once you spot the first half, only one option survives.",
   "\"The office responds (1) ______ every complaint within a day.\" (a) to (b) for (c) on (d) at",
   "The fixed pair is **respond to**: responds to every complaint. *Respond for/on/at* are not English."),
 P("clp2", "Preposition of time or place", "very common",
   "The blank sits before a clock time, a day, a period or a place, and the options are in/on/at/by/since/during type words.",
   "1. Classify the noun after the blank: point of time → at; day or date → on; longer period → in; duration up to a limit → until/by; through a period → during.\n2. For places: point → at, enclosure/area → in, surface/line → on.\n3. Plug in the word and read the sentence as a full statement.\n\n*Why it works:* the noun's kind forces the preposition; the other options break the classification.",
   "\"Suresh and his wife rarely watch television (1) ______ Sundays.\" (a) in (b) on (c) at (d) within",
   "Sundays = a day → **on**. *In* takes periods, *at* takes clock points, *within* takes a length of time."),
 P("clp3", "Phrasal verb blank", "very common",
   "The options are the same verb with different particles (put off/down/up) or different phrasal verbs with near meanings.",
   "1. Say the needed meaning in plain words ('postpone small pleasures').\n2. Match each option's meaning: put off = postpone, put down = place/write, put up with = tolerate.\n3. Choose the phrasal verb whose meaning equals your plain-words version.\n\n*Why it works:* the particle carries the meaning; translating the sentence first stops you from being hypnotised by the main verb.",
   "\"A man who cannot put (1) ______ small pleasures for a year does not deserve a big one.\" (a) off (b) down (c) up (d) in",
   "Needed meaning: postpone enjoying them → **put off**. *Put down* = place, *put up* = erect/tolerate (with 'with')."),
 P("clp4", "Preposition inside a fixed phrase", "common",
   "The blank is part of a set phrase: in spite of, according to, on behalf of, in charge of, with the help of.",
   "1. Read the phrase after the blank (…of repeated warnings, …the committee's records).\n2. Recall the complete phrase: in spite OF, according TO, on behalf OF.\n3. Check that the completed phrase fits the sentence's logic (concession, source of information, representation).\n\n*Why it works:* the phrase is one unit; half of it is given, so the other half is fixed.",
   "\"Contractors who delay the work are fined (1) ______ of repeated warnings.\" (a) due (b) in spite (c) instead (d) ahead",
   "**In spite of** repeated warnings = although they were warned many times. *Due of* is not English ('due to' has no 'of'), and 'fined instead of warnings' or 'ahead of warnings' makes no sense here — the sentence concedes the warnings and still fines."),
]}
