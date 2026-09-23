from common import q, write_topic, md_table

TENSE_T = """**The complete conversion table** — memorise as one block; every voice item is a row from it. Take the active sentence "She **writes** a letter":

| Tense | Active verb | Passive verb |
|---|---|---|
| Simple present | writes | is / are + V3 (a letter is written) |
| Present continuous | is writing | is / are being + V3 (is being written) |
| Present perfect | has written | has / have been + V3 (has been written) |
| Simple past | wrote | was / were + V3 (was written) |
| Past continuous | was writing | was / were being + V3 (was being written) |
| Past perfect | had written | had been + V3 (had been written) |
| Simple future | will write | will be + V3 (will be written) |
| Future perfect | will have written | will have been + V3 |
| Going to | is going to write | is going to be + V3 |

**Tenses with NO passive:** present perfect continuous (*has been writing*), past perfect continuous, future continuous (*will be writing*), and future perfect common usage limits. If the paper shows one of these, the conversion asks for the nearest allowed form — usually its simple counterpart. The 'being/been' skeleton is therefore: **be (in the tense of the main verb) + been (only after perfect or modal) + being (only after continuous or modal+be) + V3 always**."""

SUBTOPICS = [
    {
        "id": "ap-basics",
        "title": "Voice basics: the three moves",
        "concept": f"""Voice is a swap of stage positions: what received the action steps into the spotlight. **Three moves** convert any transitive sentence:

1. **Object becomes subject.** 'The chef *prepared* the meal' → '**The meal** …'
2. **Verb becomes be + V3**, with *be* carrying the original tense. Prepared (past) → **was** prepared; writes (present) → **is** written. The main verb is ALWAYS the past participle (V3) — never V1, never V2.
3. **Subject drops into a by-phrase** — and may vanish entirely when it is vague (someone, people, they) or unimportant: 'Someone has stolen my purse' → 'My purse has been stolen.'

**Pronoun cases swap too:** he↔him, she↔her, they↔them, I↔me, we↔us. 'He helps me' → 'I am helped by him.' In the options, a subject-slot *him* or an agent-slot *he* is an instant elimination.

**Only transitive verbs passivise.** Verbs without an object — *arrive, sleep, laugh, die, go* — have no passive at all. An option passivising 'The baby slept' does not exist in English, so the question never asks for one; but knowing this kills fake constructions in improvement items.

{TENSE_T}""",
        "formulas": [],
        "tricks": [
            {
                "title": "Tense handover",
                "body": "The helping verb must reproduce the ORIGINAL tense: wrote→was, writes→is, will write→will be, has written→has been. Any tense change in the options is an error planted on purpose.",
            },
            {
                "title": "V3-only law",
                "body": "After be/been/being, the main verb is always V3 (written, given, built). 'Is wrote', 'was wrote', 'is build' are impossible — eliminate on sight.",
            },
            {
                "title": "Pronoun mirror",
                "body": "Subject pronoun moves to by-phrase in object case (he→by him); object pronoun moves to subject slot in subject case (me→I).",
            },
        ],
        "mistakes": [
            "Changing the tense while converting (writing 'is written' for 'wrote').",
            "Keeping the active form in the by-phrase: 'by he' instead of 'by him'.",
            "Forgetting that the object of a preposition can also passivise ('They laughed at him' → 'He was laughed at').",
            "Trying to passivise intransitive verbs.",
        ],
    },
    {
        "id": "ap-tense-tables",
        "title": "Tense-by-tense conversions in action",
        "concept": f"""Work one row at a time. For each, keep the tense and change only the verb skeleton:

| Active | Passive |
|---|---|
| Ram **writes** a story | A story **is written** by Ram |
| Sita **is drawing** a map | A map **is being drawn** by Sita |
| They **have caught** the thief | The thief **has been caught** |
| The cook **made** dinner | Dinner **was made** by the cook |
| The boys **were flying** kites | Kites **were being flown** by the boys |
| She **had finished** the work | The work **had been finished** by her |
| The PM **will address** the nation | The nation **will be addressed** by the PM |
| He **will have completed** it | It **will have been completed** |

**Number agreement restarts in the passive.** The new subject decides is/are, was/were, has/have: 'They have completed **the projects**' → '**The projects have** been completed' — the *has* of the active dies. SSC always plants one option that forgets to re-agree.

**The two 'being/been' positions:** continuous tenses take **being** (is being built, was being built); perfect tenses take **been** (has been taken, had been taken, will have been taken). Modals take plain **be**: will/can/must/should/may + **be** + V3. Any 'is been built' or 'will being taken' is impossible.

**Verb groups that resist the table:** *have/own/possess, resemble, lack, suit, fit, become* are normally stative — 'A car is had by him' is not English. When a stem uses these, expect a 'no passive possible' or a restructured answer, not a mechanical conversion.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Row-recall",
                "body": "Identify the active tense, then recite its passive row: present cont. → is/are being + V3; past perf. → had been + V3; future → will be + V3. Options break exactly one cell of the row.",
            },
            {
                "title": "Re-agreement sweep",
                "body": "After converting, make is/are/was/were/has/have agree with the NEW subject — check this before anything else.",
            },
            {
                "title": "being vs been slot",
                "body": "Continuous in the active → being. Perfect in the active → been. Modal → neither (plain be).",
            },
        ],
        "mistakes": [
            "Writing 'is been' for a continuous passive (correct: is being).",
            "Writing 'is being' for a perfect passive (correct: has been).",
            "Keeping the active subject as subject ('The cook was made dinner by…').",
            "Forgetting by + object-case pronoun.",
        ],
    },
    {
        "id": "ap-modals-imperatives",
        "title": "Modals, imperatives, infinitives and questions",
        "concept": f"""**Modals:** will, shall, can, could, may, might, must, should, ought to → **modal + be + V3**.
'You must obey the rules' → 'The rules must be obeyed.' 'They can solve it' → 'It can be solved (by them).'

**Imperatives** convert with **Let**:
- Order: 'Shut the door' → 'Let the door be shut.'
- Advice: 'Help the poor' → 'Let the poor be helped.'
- Negative order: 'Do not touch the wire' → 'Let the wire not be touched' / 'The wire should not be touched.'
- Request with 'please': 'Please post this letter' → 'You are requested to post this letter.'

**Infinitives:** to write → **to be written** ('I want someone to write this' → 'I want this to be written'). **Gerunds:** writing → **being written** ('He likes people praising him' → 'He likes being praised').

**Questions:**
- **Who** asks → **By whom** + auxiliary + subject: 'Who wrote this?' → 'By whom was this written?' (The wh-word moves to front with *by whom*; the auxiliary then precedes the new subject — word order is the planted error.)
- **Whom/what** as object → normal passive with the wh-word as subject: 'Whom did you call?' → 'Who was called by you?' 'What did he buy?' → 'What was bought by him?'
- Yes/no questions keep inversion: 'Did she sing a song?' → 'Was a song sung by her?'

**Factitive and double-object verbs** (give, send, offer, teach, tell, show) have TWO passives: 'The teacher gave **the students** homework' → 'The students were given homework…' OR 'Homework was given to the students…'. Both are correct; papers use one as key and corrupt the other (dropping 'to' is the classic corruption).""",
        "formulas": [],
        "tricks": [
            {
                "title": "Let-anchor",
                "body": "An imperative stem (no subject, base verb) signals the Let + object + be + V3 answer. Any option without 'Let' or a modal cannot be right.",
            },
            {
                "title": "By whom inversion",
                "body": "Who→questions convert to 'By whom + was/were/is + new subject + V3'. Check the word order first — options scramble it.",
            },
            {
                "title": "Request formula",
                "body": "Please → 'You are requested to …'; order → 'Let … be …'; advice → 'You are advised to …' or '… should be …'.",
            },
        ],
        "mistakes": [
            "Converting 'Please help me' to 'Let me be helped' instead of 'You are requested to help me'.",
            "Writing 'By whom this was written?' — statement order in a question; it needs 'By whom was this written?'",
            "Dropping 'to' in the second passive of a double-object verb ('Homework was given the students').",
            "Using 'ought to be' wrongly as 'ought be' or 'ought to been'.",
        ],
    },
    {
        "id": "ap-passive-to-active",
        "title": "Reverse conversions: passive to active",
        "concept": f"""The reverse run appears in every shift. Move the by-agent (if any) into the subject slot, rebuild the tense from the passive skeleton, and give the old subject object position:

| Passive | Active |
|---|---|
| The letter **was written** by Sita | Sita **wrote** the letter |
| The road **is being repaired** | They **are repairing** the road |
| The work **had been finished** | She **had finished** the work |
| The results **will be declared** | The board **will declare** the results |
| The kite **was being flown** by the boy | The boy **was flying** the kite |

**Recover the tense from the FIRST auxiliary**, not the participle: was written → past simple (wrote); is being written → present continuous (is writing); has been written → present perfect (has written); had been written → past perfect (had written); will be written → future (will write).

**Missing agent:** when no by-phrase exists, supply *they/people/someone* — 'The thief was arrested' → 'They arrested the thief'. Papers accept the standard vague subject; the options differ only in verb form.

**Pronouns reverse too:** 'He was praised by them' → 'They praised **him**.' Watch the object case at the end — 'praised he' is the planted error.

**'Let' passives convert back to imperatives:** 'Let the door be shut' → 'Shut the door.'""",
        "formulas": [],
        "tricks": [
            {
                "title": "First-auxiliary tense",
                "body": "Read only the first auxiliary to fix the tense: was→past, is→present, has/had→perfect, will→future, is being→present continuous, was being→past continuous.",
            },
            {
                "title": "Agent hunt",
                "body": "Find the by-phrase; that noun/pronoun becomes the subject. No by-phrase → they/people/someone.",
            },
            {
                "title": "Object-case exit check",
                "body": "The final pronoun must be in object case: 'They praised him', not 'he'. Many options fail exactly here.",
            },
        ],
        "mistakes": [
            "Taking 'was being chased' back to 'chased' (losing the continuous: were chasing).",
            "Leaving the old subject in subject position ('The principal was praised him').",
            "Ending with a subject-case pronoun ('praised he').",
            "Changing tense on the way back (was written → has written).",
        ],
    },
    {
        "id": "ap-strategy",
        "title": "Exam strategy: the 20-second conversion protocol",
        "concept": f"""Voice items are worth one mark each in under 30 seconds — the purest formula topic in the paper. The protocol:

1. **Tag the voice.** Active stem → build passive; passive stem → build active.
2. **Fix the tense.** From the first auxiliary (active) or skeleton (passive). Say the row aloud: 'was writing → was being + V3'.
3. **Move the parts.** Object↔subject; subject→by-phrase (or they/people); pronouns swap case.
4. **Re-agree the verb** with its new subject.
5. **Eliminate the four classic faults** in options: wrong V-form (V1/V2 after be), broken being/been slot, unchanged tense, pronoun case error. In a well-set item each wrong option carries exactly one of these faults.

**Distribution reality:** roughly one active→passive and one passive→active per Tier 1 shift; Tier 2 adds voice items inside error-spotting and cloze. Tenses drawn are usually simple present, simple past, present perfect, present continuous and modals — master those five rows first, then add the rest.

**Daily plan:** 10 conversions a day, alternating directions, written not spoken. After a week, recite the eight-row table from memory; after two, the item needs only the row-recall plus the elimination sweep. Target: 100% accuracy, 25 seconds per item.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Fault-class elimination",
                "body": "Every wrong option breaks exactly one rule: V-form, being/been, tense, agreement, pronoun. Name the fault — the option dies by its name.",
            },
            {
                "title": "Five-row priority",
                "body": "Master simple present, simple past, present perfect, present continuous, modals first — they cover 80% of paper items.",
            },
            {
                "title": "Write, don't speak",
                "body": "Voice errors live on paper. Convert in writing daily; the hand learns the skeleton faster than the ear.",
            },
        ],
        "mistakes": [
            "Rushing the re-agreement check after conversion.",
            "Memorising conversions word-by-word instead of as tense rows.",
            "Ignoring pronoun case at the ends of sentences.",
            "Treating 'is been' as acceptable because it sounds like the continuous.",
        ],
    },
]

PATTERNS = [
    {
        "pattern": "Active to passive (statement)",
        "frequency": "very common",
        "howToSpot": "A declarative sentence; options are four passive versions.",
        "approach": "Fix the tense row, move object to subject, re-agree, choose by-fault-class elimination.",
    },
    {
        "pattern": "Passive to active (statement)",
        "frequency": "very common",
        "howToSpot": "A be + V3 sentence with by-agent; options are four active versions.",
        "approach": "Agent becomes subject; recover tense from the first auxiliary; end with object-case pronoun.",
    },
    {
        "pattern": "Imperative or request conversion",
        "frequency": "common",
        "howToSpot": "A stem without a subject ('Open the gate', 'Please help me').",
        "approach": "Order → Let + object + be + V3; request → You are requested to …",
    },
    {
        "pattern": "Interrogative conversion",
        "frequency": "common",
        "howToSpot": "A question stem; who-questions become by-whom items.",
        "approach": "Keep the question word first (By whom…), then auxiliary, then subject — check word order before verb form.",
    },
    {
        "pattern": "Voice fault inside error-spotting",
        "frequency": "occasional",
        "howToSpot": "An error-spotting sentence hiding 'is been' or a case error in a by-phrase.",
        "approach": "Run the being/been slot test and the pronoun-case test on every voice structure you meet.",
    },
]

SE = [
    q("eng-ap-s01", "Select the option that expresses the given sentence in passive voice.\n\nThe chef had prepared the meal.",
      ["The meal had been prepared by the chef.", "The meal has been prepared by the chef.", "The meal was prepared by the chef.", "The meal had prepared by the chef."], 0,
      "Active tense = **past perfect** (had + V3). Its passive row is **had been + V3**: 'The meal had been prepared by the chef.' Option B shifts tense to present perfect; Option C drops to simple past; Option D loses 'been'.",
      "Past perfect row: had + V3 → had been + V3. Tense never changes.",
      "easy", "ap-tense-tables", "row recall", 30),
    q("eng-ap-s02", "Select the option that expresses the given sentence in passive voice.\n\nThey are building a new bridge.",
      ["A new bridge is being built by them.", "A new bridge is been built by them.", "A new bridge is building by them.", "A new bridge was being built by them."], 0,
      "Present continuous → passive row **is/are being + V3**. The new subject 'a new bridge' is singular, so **is** being built. Option B commits the classic 'is been' error (been belongs to perfect tenses); C uses V1; D changes tense to past.",
      "Continuous → being, never been: is being + V3.",
      "easy", "ap-tense-tables", "being/been slot", 30),
    q("eng-ap-s03", "Select the option that expresses the given sentence in active voice.\n\nThe thief was being chased by the police.",
      ["The police were chasing the thief.", "The police were chased the thief.", "The police was chasing the thief.", "The police had chased the thief."], 0,
      "'was being + V3' is the **past continuous passive** → active is **was/were + V-ing**. The new subject 'police' is plural → **were chasing**. Option B writes V2 after 'were'; C breaks number; D changes tense.",
      "was being + V3 → were + V-ing (past continuous back-conversion).",
      "medium", "ap-passive-to-active", "first-auxiliary tense", 35),
]

PRACTICE = [
    q("eng-ap-p01", "Select the option that expresses the given sentence in passive voice.\n\nShe writes a letter.",
      ["A letter is written by her.", "A letter is wrote by her.", "A letter was written by her.", "A letter is being written by her."], 0,
      "Simple present → **is/are + V3**. 'A letter is written by her.' B uses V2 ('wrote') after is; C changes tense to past; D changes aspect to continuous.",
      "Simple present row: is/are + V3.",
      "easy", "ap-basics", "row recall", 25),
    q("eng-ap-p02", "Select the option that expresses the given sentence in passive voice.\n\nThe gardener is watering the plants.",
      ["The plants are being watered by the gardener.", "The plants are being water by the gardener.", "The plants is being watered by the gardener.", "The plants are watered by the gardener."], 0,
      "Present continuous → **are being + V3** with the plural new subject 'the plants'. B uses V1; C fails number agreement (is for plants); D drops 'being', turning it into simple present.",
      "are being + V3 — check the V3 and the number both.",
      "easy", "ap-tense-tables", "row recall", 30),
    q("eng-ap-p03", "Select the option that expresses the given sentence in passive voice.\n\nThey have completed the project.",
      ["The project has been completed by them.", "The project has completed by them.", "The project has being completed by them.", "The project have been completed by them."], 0,
      "Present perfect → **has/have been + V3**. The new subject 'the project' is singular → **has been completed**. B drops 'been'; C wrongly uses 'being' in a perfect slot; D agrees the verb with 'they' instead of the new subject.",
      "Perfect row: has/have been + V3; agree with the NEW subject.",
      "easy", "ap-tense-tables", "row recall", 30),
    q("eng-ap-p04", "Select the option that expresses the given sentence in passive voice.\n\nSomeone has stolen my purse.",
      ["My purse has been stolen.", "My purse has stolen.", "My purse was stolen by someone.", "My purse is stolen by someone."], 0,
      "Present perfect passive: 'My purse has been stolen.' The vague agent **someone** is dropped. B misses 'been'; C and D change the tense.",
      "Vague agents (someone/they) vanish in the passive.",
      "easy", "ap-basics", "agent drop", 25),
    q("eng-ap-p05", "Select the option that expresses the given sentence in passive voice.\n\nOpen the gate.",
      ["Let the gate be opened.", "The gate is opened.", "The gate be opened.", "Let the gate be open."], 0,
      "An imperative converts with **Let + object + be + V3**: 'Let the gate be opened.' B produces a statement, not an order; C lacks the auxiliary; D uses the adjective 'open' instead of V3 'opened'.",
      "Imperative anchor: Let + object + be + V3.",
      "easy", "ap-modals-imperatives", "Let anchor", 25),
    q("eng-ap-p06", "Select the option that expresses the given sentence in passive voice.\n\nYou must obey the rules.",
      ["The rules must be obeyed.", "The rules must be obey.", "The rules must been obeyed.", "The rules must being obeyed."], 0,
      "Modal row: **modal + be + V3** — 'The rules must be obeyed.' B uses V1; C uses 'been' after a modal (been only follows have/will have); D uses 'being' where plain 'be' is required.",
      "Modal row: modal + be + V3 — no being, no been.",
      "easy", "ap-modals-imperatives", "modal row", 25),
    q("eng-ap-p07", "Select the option that expresses the given sentence in passive voice.\n\nWho taught you English?",
      ["By whom were you taught English?", "Who was taught you English?", "By whom you were taught English?", "Whom were taught English by you?"], 0,
      "Who-questions passivise to **By whom + auxiliary + subject**: 'By whom were you taught English?' B keeps 'who' instead of 'by whom'; C uses statement word order; D scrambles the clause entirely.",
      "Who → By whom + aux + subject; word order is the trap.",
      "medium", "ap-modals-imperatives", "by-whom order", 35),
    q("eng-ap-p08", "Select the option that expresses the given sentence in active voice.\n\nThe novel was written by Premchand.",
      ["Premchand wrote the novel.", "Premchand was written the novel.", "Premchand has written the novel.", "Premchand had written the novel."], 0,
      "'was written' → simple past active: **wrote**. B keeps the passive verb; C and D both shift the tense (present perfect, past perfect).",
      "was + V3 → past simple (V2).",
      "easy", "ap-passive-to-active", "first-aux tense", 25),
    q("eng-ap-p09", "Select the option that expresses the given sentence in active voice.\n\nThe letter will be posted by the clerk.",
      ["The clerk will post the letter.", "The clerk will posted the letter.", "The clerk will be posting the letter.", "The clerk would post the letter."], 0,
      "'will be + V3' → future simple active: **will post**. B uses V2 after will; C keeps passive 'be' inside the active; D shifts the modal.",
      "will be + V3 → will + V1.",
      "easy", "ap-passive-to-active", "first-aux tense", 25),
    q("eng-ap-p10", "Select the option that expresses the given sentence in active voice.\n\nHe was praised by the principal.",
      ["The principal praised him.", "The principal praised he.", "The principal was praised him.", "The principal praises him."], 0,
      "Agent → subject ('the principal'); 'was praised' → simple past **praised**; old subject moves to object case: **him**. B ends in subject-case 'he'; C keeps the passive 'was'; D changes tense to present.",
      "By-agent becomes subject; final pronoun in object case.",
      "easy", "ap-passive-to-active", "pronoun case", 25),
    q("eng-ap-p11", "Select the option that expresses the given sentence in passive voice.\n\nThe teacher gave the students homework.",
      ["The students were given homework by the teacher.", "The students was given homework by the teacher.", "The homework was given the students by the teacher.", "The students are given homework by the teacher."], 0,
      "Double-object verb: either object can lead. 'The students were given homework by the teacher' is correct (plural → were). B breaks number; C drops the preposition 'to' ('given the students' needs 'given to the students'); D changes tense.",
      "give offers two passives; the indirect-object one keeps 'were given'.",
      "medium", "ap-tense-tables", "double object", 35),
    q("eng-ap-p12", "Select the option that expresses the given sentence in passive voice.\n\nThe committee will announce the results.",
      ["The results will be announced by the committee.", "The results will announced by the committee.", "The results will being announced by the committee.", "The results would be announced by the committee."], 0,
      "Simple future → **will be + V3**. B loses 'be'; C uses 'being' after a modal; D shifts the modal (would).",
      "Future row: will be + V3.",
      "easy", "ap-tense-tables", "row recall", 25),
    q("eng-ap-p13", "Select the option that expresses the given sentence in active voice.\n\nThe road is being repaired by the workers.",
      ["The workers are repairing the road.", "The workers are repaired the road.", "The workers is repairing the road.", "The workers have repaired the road."], 0,
      "'is being + V3' → present continuous: **are repairing** (plural subject). B writes V3 after are; C fails number; D changes tense to perfect.",
      "is being + V3 → are + V-ing.",
      "easy", "ap-passive-to-active", "first-aux tense", 25),
    q("eng-ap-p14", "Select the option that expresses the given sentence in passive voice.\n\nPlease help the poor.",
      ["You are requested to help the poor.", "Let the poor helped.", "The poor are helped.", "You are request to help the poor."], 0,
      "A 'please' request converts to **You are requested to + V1**. B drops 'be' in the Let-form and loses the request tone; C gives a statement of fact; D writes the noun 'request' where V3 'requested' is needed.",
      "please → You are requested to …; order → Let … be …",
      "medium", "ap-modals-imperatives", "request formula", 30),
    q("eng-ap-p15", "Select the option that expresses the given sentence in passive voice.\n\nThe gardener had planted the saplings.",
      ["The saplings had been planted by the gardener.", "The saplings have been planted by the gardener.", "The saplings had planted by the gardener.", "The saplings were planted by the gardener."], 0,
      "Past perfect → **had been + V3**: 'The saplings had been planted by the gardener.' B shifts to present perfect; C drops 'been'; D drops to simple past.",
      "had + V3 → had been + V3.",
      "easy", "ap-tense-tables", "row recall", 25),
]

topic = {
    "id": "active-passive",
    "sectionId": "english",
    "title": "Active & Passive Voice",
    "order": 10,
    "importance": "medium",
    "avgQuestions": {"tier1": 2, "tier2": 3},
    "summary": "Two voice conversions per shift, built from an eight-row tense table and five named fault classes. Learn the table once — simple present to future perfect, being vs been slots, modal + be + V3, the Let-anchor for imperatives and By-whom order for questions — and both directions (active→passive, passive→active) become 25-second kills.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
