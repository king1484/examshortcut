from common import q, write_topic, md_table

SUBTOPICS = [
    {
        "id": "narr-reporting-verb",
        "title": "Reporting verbs and the mechanics of the shift",
        "concept": f"""Direct speech quotes the speaker's words inside inverted commas; indirect (reported) speech folds them into the reporter's sentence. Three mechanical changes always apply:

1. **Comma and quotes vanish; a connective appears.** Statements take **that**: He said, "I am tired" → He said **that** he was tired.
2. **The reporting verb fits the mood.** *said to* → **told** (+ listener) or said (+ that); a question → **asked** (never 'asked that' for yes/no — use if/whether); a command → **ordered/told/commanded**; advice → **advised**; request → **requested**; suggestion → **suggested/proposed**; warning → **warned**.
3. **Word order in questions becomes statement order** — auxiliary before subject dies: He said to her, "Where **do you live**?" → He asked her where **she lived**.

**Tone-fitting table:**

| Direct situation | Reporting verb | Pattern |
|---|---|---|
| Plain statement | said / told me | said that … / told me that … |
| Command | ordered, told, commanded | told/ordered + object + to + V1 |
| Advice | advised | advised + object + to + V1 |
| Request (please, kindly) | requested | requested + object + to + V1 |
| Negative command | forbade / told … not to | told + object + not to + V1 |
| Suggestion (Let us…) | suggested, proposed | suggested + V-ing / that … should |
| Exclamation (Hurrah!, Alas!) | exclaimed with joy/sorrow | exclaimed … that + statement |
| Wish (Good morning!) | wished | wished + object |
| Thanks | thanked | thanked + object (+ for …) |

**'Said me' does not exist** — said needs 'to' (said to me) or becomes told (told me). This one letter difference is the most planted distractor in the section.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Verb-tone match",
                "body": "Read the quoted words first for TONE: order, advice, request, question, joy, sorrow. Then pick the reporting verb that carries that tone — the verb choice alone often eliminates two options.",
            },
            {
                "title": "said-to vs told",
                "body": "said + to + person; told + person. Any 'said me' or 'told to me' option is dead on arrival.",
            },
            {
                "title": "Connective test",
                "body": "Statement → that. Yes/no question → if/whether (never that). Wh-question → the wh-word itself (never if).",
            },
        ],
        "mistakes": [
            "Writing 'He said me' — said never takes a direct listener.",
            "Using 'asked that' for a yes/no question instead of 'asked if'.",
            "Keeping inverted commas or a comma after the reporting verb.",
            "Choosing 'ordered' where the sentence asks politely — tone mismatch.",
        ],
    },
    {
        "id": "narr-tense-shift",
        "title": "Backshift: the tense conversion table",
        "concept": f"""When the reporting verb is in the past (said, told, asked — nearly always in SSC), every tense inside the quotes moves one step back:

| Direct (quoted) tense | Indirect tense | Example |
|---|---|---|
| Simple present (V1) | Simple past (V2) | "I **write**" → he **wrote** |
| Present continuous | Past continuous | "I **am writing**" → he **was writing** |
| Present perfect | Past perfect | "I **have written**" → he **had written** |
| Present perfect continuous | Past perfect continuous | "I **have been writing**" → he **had been writing** |
| Simple past (V2) | Past perfect | "I **wrote**" → he **had written** |
| Past continuous | Past perfect continuous (or past perfect) | "I **was writing**" → he **had been writing** |
| will | would | "I **will** come" → he **would** come |
| can | could | "I **can** help" → he **could** help |
| may | might | "I **may** come" → he **might** come |
| shall | should (with I/we) | "I **shall** go" → I **should** go |
| must | must / had to | "I **must** go" → he **must/had to** go |
| have to | had to | "I **have to** go" → he **had to** go |

**Verbs that NEVER backshift:** past perfect (had written stays had written), could, would, should, might, ought to, used to, should have. If the quote already uses one of these, the tense is settled — options changing it are wrong.

**The universal-truth exception:** scientific facts, habitual truths and proverbs **keep their tense** even after a past reporting verb: The teacher said that **the earth revolves** around the sun (not 'revolved'). Habitual actions with always/every day may also stay in the present. This exception appears in nearly every shift — one item, whole mark.""",
        "formulas": [],
        "tricks": [
            {
                "title": "One-step-back ladder",
                "body": "Recite the ladder: present→past, present cont.→past cont., perfect→past perfect, past→past perfect, will→would, can→could, may→might, must→had to.",
            },
            {
                "title": "Frozen-five",
                "body": "could, would, should, might, ought to never change. Spot one in the quote → that option's tense is already correct; any shift is an error.",
            },
            {
                "title": "Truth test",
                "body": "Is the quoted statement a fact of nature, a habit or a proverb? Then no backshift — said that the earth REVOLVES.",
            },
        ],
        "mistakes": [
            "Backshifting past perfect to something nonexistent (had had written).",
            "Forgetting the universal-truth exception and 'revolved' the sun.",
            "Backshifting 'must' to 'musted' — it becomes must or had to.",
            "Changing 'could' to 'can' in indirect speech — the frozen modals never move.",
        ],
    },
    {
        "id": "narr-pronouns-time-place",
        "title": "Pronouns, and the time/place word table",
        "concept": f"""**Pronouns change by who is speaking to whom** (the SONA logic): **first person follows the reporter**, **second person follows the listener**, **third person never changes**.

He said to me, "**I** will help **you** with **your** work" → He told me that **he** would help **me** with **my** work. (I → he: speaker; you → me: listener; your → my.)

He said to Ram, "**You** must bring **your** book" → He told Ram that **he** had to bring **his** book. (you → he: the listener Ram; your → his.)

**The time/place table** — every word anchored to the speaker's 'now and here' shifts to the reporter's distance:

| Direct | Indirect |
|---|---|
| now | then |
| today | that day |
| tonight | that night |
| yesterday | the previous day / the day before |
| tomorrow | the next day / the following day |
| the day after tomorrow | two days later |
| last week/month | the previous week/month |
| next week/month | the following week/month |
| ago | before / earlier |
| hence | thence |
| here | there |
| this | that |
| these | those |
| thus | so |
| come | go (when perspective shifts) |

**When the reporting verb is in the PRESENT** (says, is saying — rare in SSC but tested in Tier 2), neither tense nor time words change: He says, "I **am** busy **today**" → He says that he **is** busy **today**.""",
        "formulas": [],
        "tricks": [
            {
                "title": "SONA sweep",
                "body": "Mark the three pronoun anchors before touching anything else: 1st person → speaker, 2nd person → listener, 3rd person → unchanged. Most wrong options botch exactly one of these.",
            },
            {
                "title": "Yesterday/tomorrow pair",
                "body": "yesterday → the previous day; tomorrow → the next (following) day. The pair travels together — if one shifted and the option leaves the other, it's wrong.",
            },
            {
                "title": "Present-reporter exemption",
                "body": "Reporting verb 'says' (present) → nothing shifts: tense AND time words freeze. Check the reporting verb before applying any table.",
            },
        ],
        "mistakes": [
            "Leaving 'you' unchanged when the listener is named (Ram → he).",
            "Writing 'yesterday' or 'tomorrow' inside reported speech.",
            "Changing 'this' to 'the' instead of 'that'.",
            "Shifting tenses because the sentence 'looks indirect' even when the reporter says (present).",
        ],
    },
    {
        "id": "narr-questions-commands-exclamations",
        "title": "Questions, commands and exclamations",
        "concept": f"""Each sentence type has its own conversion skeleton:

**Yes/No questions:** asked + if/whether + statement order + backshift.
He said to me, "**Do you** know the answer?" → He asked me **if I knew** the answer. (The dummy 'do' vanishes; subject-auxiliary order flattens.)

**Wh-questions:** asked + wh-word + statement order + backshift.
She said to him, "**Where are you going**?" → She asked him **where he was going**.
He said to me, "**What did you eat**?" → He asked me **what I had eaten**.

**Commands/orders:** told/ordered + object + **to + V1** (negative: **not to** + V1).
The officer said to them, "Report immediately." → The officer ordered them **to report** immediately.
Mother said, "Don't touch the wire." → Mother told me **not to touch** the wire (or: **forbade me to touch**).

**Requests:** requested + object + to + V1. **Advice:** advised + object + to + V1.

**Let us (suggestion):** suggested + V-ing → He said, "Let us go for a walk" → He **suggested going** for a walk (or: suggested that they should go). **Let me (permission/allow):** requested to be allowed to → He said, "Let me sit here" → He requested that he might be allowed to sit there.

**Exclamations:** what/hurrah/alas/bravo carry the tone:
"Hurrah! We have won" → They **exclaimed with joy** that they had won.
"Alas! He is ruined" → He **exclaimed with sorrow** that he was ruined.
"Bravo! Well done" → They **applauded him, saying** that he had done well.
"Good morning" → wished; "Thank you" → thanked.

**Optatives (May God bless you):** prayed/wished — He said, "May you succeed!" → He **wished** that I might succeed.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Skeleton-first",
                "body": "Classify the quote (question/command/request/exclamation) and write its skeleton (asked if… / told … to … / exclaimed with joy that …). Then pour tense, pronoun and time-word shifts into the skeleton.",
            },
            {
                "title": "Do-support removal",
                "body": "Do/did in direct questions is a dummy — it disappears in indirect speech: 'Do you know' → if I knew, never 'if I did know'.",
            },
            {
                "title": "Exclamation-verb map",
                "body": "Hurrah → exclaimed with joy; Alas → exclaimed with sorrow; Bravo → applauded; Good morning → wished; Thank you → thanked. One-to-one map, no thinking needed.",
            },
        ],
        "mistakes": [
            "Keeping question order in reported questions ('asked where was I going').",
            "Using 'if' with a wh-question.",
            "Writing 'He ordered that I go' where the pattern is object + to + V1.",
            "Using 'exclaimed with joy' for an Alas! sentence — tone verb mismatch.",
        ],
    },
    {
        "id": "narr-strategy",
        "title": "Exam strategy: the four-check protocol",
        "concept": f"""Every narration item changes the quote in exactly four dimensions. Check them in order — each wrong option in the paper fails exactly one:

1. **Reporting verb + connective.** Tone-fit verb (asked/told/ordered/requested/exclaimed); that / if / wh-word connective. Kills options with 'said me', 'asked that' (for yes/no), missing if.
2. **Tense.** Backshift by the ladder — unless the quote is a universal truth or the reporting verb is present. Kills options with unchanged or over-shifted tenses.
3. **Pronouns.** SONA sweep: speaker, listener, unchanged third. Kills options where I/me/you/he are tangled.
4. **Time/place words.** yesterday → the previous day, tomorrow → the next day, here → there, this → that, now → then. Kills options that leave 'today' stranded in reported speech.

**Both directions appear:** direct→indirect dominates (3 of 4 items), but indirect→direct appears in every 4th shift or so — run the same four checks backwards (restore quotes, comma and question order, un-backshift past perfect to past simple, restore today/yesterday).

**Daily plan:** 10 conversions a day alternating statement/question/command types, written by hand. In a week the four checks run in parallel; in two, narration is a free mark. Tier 1 carries two narration items; Tier 2 carries more, often inside error-spotting.""",
        "formulas": [],
        "tricks": [
            {
                "title": "One-fault elimination",
                "body": "Name the fault of each wrong option — verb, tense, pronoun or time-word. If you can't name a fault, look again; if two options share none, you've misjudged the tone verb.",
            },
            {
                "title": "Reverse-mode anchors",
                "body": "Indirect→direct: the phrase 'the previous day' signals quotes needed with 'yesterday'; 'asked if' signals a yes/no question with inverted order and dummy 'do' if present tense returns.",
            },
            {
                "title": "Written drill",
                "body": "Narration lives in punctuation and word order — practise on paper, never orally; the hand catches what the ear forgives.",
            },
        ],
        "mistakes": [
            "Running checks out of order and fixing tense while leaving 'said me' intact.",
            "Un-backshifting 'had seen' to 'had seen' in direct speech (it must become saw).",
            "Forgetting the comma and quotes in indirect→direct answers.",
            "Assuming every tense shifts — the truth-sentence exception costs a mark when ignored.",
        ],
    },
]

PATTERNS = [
    {
        "pattern": "Direct to indirect (statement)",
        "frequency": "very common",
        "howToSpot": "A quoted statement; options are reported versions differing in tense, pronoun or time word.",
        "approach": "Four-check protocol: verb/connective → tense → pronouns → time words.",
    },
    {
        "pattern": "Direct to indirect (question)",
        "frequency": "common",
        "howToSpot": "A quoted question; options differ in if/wh-word and word order.",
        "approach": "Flatten to statement order, keep the wh-word or add if/whether, remove dummy do/did.",
    },
    {
        "pattern": "Direct to indirect (command/request/exclamation)",
        "frequency": "common",
        "howToSpot": "An order, please-request or Hurrah/Alas quote.",
        "approach": "Fit the skeleton: told+object+to+V1 / requested+object+to+V1 / exclaimed with joy/sorrow that …",
    },
    {
        "pattern": "Indirect to direct",
        "frequency": "occasional",
        "howToSpot": "A reported sentence; options restore quotes.",
        "approach": "Run the four checks backwards; rebuild punctuation, question order and original tenses.",
    },
    {
        "pattern": "Narration fault in error-spotting",
        "frequency": "occasional",
        "howToSpot": "A reported sentence with 'said me', stranded 'yesterday', or un-backshifted tense as the hidden error.",
        "approach": "Scan reported sentences for the four fault classes specifically.",
    },
]

SE = [
    q("eng-narr-s01", "Select the option that expresses the given sentence in indirect speech.\n\nHe said, \"I am writing a letter.\"",
      ["He said that he was writing a letter.", "He said that he is writing a letter.", "He said that he has written a letter.", "He said that him was writing a letter."], 0,
      "Reporting verb 'said' is past → backshift present continuous to **past continuous** (was writing), and the pronoun I → **he** (speaker). B skips the backshift; C jumps two steps; D uses the object-case 'him' as subject.",
      "Past reporter → one step back: am writing → was writing; I → he.",
      "easy", "narr-tense-shift", "backshift ladder", 30),
    q("eng-narr-s02", "Select the option that expresses the given sentence in indirect speech.\n\nShe said to him, \"Where are you going?\"",
      ["She asked him where he was going.", "She asked him where was he going.", "She asked him that where he was going.", "She asked him where he is going."], 0,
      "Wh-question → keep the wh-word, flatten to **statement order** (where he was — not 'was he'), backshift (are → was), you → he. B keeps question order; C doubles the connective ('that' with a wh-word); D skips the backshift.",
      "Wh-word + statement order + backshift. 'that' never accompanies a wh-word.",
      "easy", "narr-questions-commands-exclamations", "skeleton first", 30),
    q("eng-narr-s03", "Select the option that expresses the given sentence in indirect speech.\n\nThe teacher said to the students, \"The earth revolves around the sun.\"",
      ["The teacher told the students that the earth revolves around the sun.", "The teacher told the students that the earth revolved around the sun.", "The teacher said to the students that the earth had revolved around the sun.", "The teacher told to the students that the earth revolves around the sun."], 0,
      "A **universal truth keeps its tense** even after a past reporting verb — 'revolves' stays. said to + listener → **told** + listener. B wrongly backshifts; C over-shifts to past perfect; D writes 'told to'.",
      "Truth test: facts of nature freeze — revolves, not revolved.",
      "medium", "narr-tense-shift", "truth exception", 35),
]

PRACTICE = [
    q("eng-narr-p01", "Select the option that expresses the given sentence in indirect speech.\n\nShe said to me, \"I will meet you tomorrow.\"",
      ["She told me that she would meet me the next day.", "She told me that she will meet me the next day.", "She told me that she would meet you the next day.", "She said me that she would meet me the next day."], 0,
      "said to me → told me; will → **would**; you → **me** (listener); tomorrow → **the next day**. B skips the backshift; C leaves 'you' unconverted; D writes the impossible 'said me'.",
      "Four checks: told + would + me + next day.",
      "easy", "narr-pronouns-time-place", "SONA + time", 30),
    q("eng-narr-p02", "Select the option that expresses the given sentence in indirect speech.\n\nHe said, \"I bought a car yesterday.\"",
      ["He said that he had bought a car the previous day.", "He said that he bought a car the previous day.", "He said that he has bought a car yesterday.", "He said that he had bought a car yesterday."], 0,
      "Simple past → **past perfect** (had bought); yesterday → **the previous day**. B stops at simple past; C keeps 'yesterday'; D shifts tense but strands 'yesterday' — both dimensions must move.",
      "Past → past perfect, and yesterday travels to 'the previous day'.",
      "easy", "narr-tense-shift", "ladder + time", 30),
    q("eng-narr-p03", "Select the option that expresses the given sentence in indirect speech.\n\nMother said to me, \"Do not go out in the rain.\"",
      ["Mother told me not to go out in the rain.", "Mother said me not to go out in the rain.", "Mother told me to not going out in the rain.", "Mother told me don't go out in the rain."], 0,
      "Negative command → **told + object + not to + V1**. B uses 'said me'; C breaks the to-structure; D keeps the direct form 'don't'.",
      "Negative order skeleton: told + me + not to + go.",
      "easy", "narr-questions-commands-exclamations", "command skeleton", 25),
    q("eng-narr-p04", "Select the option that expresses the given sentence in indirect speech.\n\nThe stranger said to me, \"Can you show me the way to the station?\"",
      ["The stranger asked me if I could show him the way to the station.", "The stranger asked me that I could show him the way to the station.", "The stranger asked me if I can show him the way to the station.", "The stranger asked me if I could show me the way to the station."], 0,
      "Yes/no question → **asked + if** + statement order + backshift (can → could); you → I (listener), me → him (speaker). B uses 'that' with a yes/no question; C skips the backshift; D tangles the two pronouns.",
      "if/whether for yes/no; can → could; pronouns swap by SONA.",
      "medium", "narr-questions-commands-exclamations", "yes/no skeleton", 35),
    q("eng-narr-p05", "Select the option that expresses the given sentence in indirect speech.\n\nThey said, \"Hurrah! We have won the trophy.\"",
      ["They exclaimed with joy that they had won the trophy.", "They exclaimed with sorrow that they had won the trophy.", "They said with joy that they have won the trophy.", "They exclaimed with joy that they would win the trophy."], 0,
      "Hurrah → **exclaimed with joy**; present perfect → past perfect; we → they. B inverts the tone; C keeps the un-shifted 'have won'; D changes the tense to would.",
      "Hurrah = joy, Alas = sorrow; then backshift the tense.",
      "easy", "narr-questions-commands-exclamations", "exclamation map", 25),
    q("eng-narr-p06", "Select the option that expresses the given sentence in direct speech.\n\nHe asked me if I was hungry.",
      ["He said to me, \"Are you hungry?\"", "He said to me, \"You are hungry.\"", "He said to me, \"Was I hungry?\"", "He said to me, \"Are I hungry?\""], 0,
      "'asked if' = yes/no question → restore quotes, question order and **present tense** (was → are), you as listener. B states instead of asking; C reverses the pronouns; D writes the impossible 'Are I'.",
      "Reverse: if + was → Are you …? with question mark.",
      "medium", "narr-strategy", "reverse checks", 35),
    q("eng-narr-p07", "Select the option that expresses the given sentence in indirect speech.\n\nShe said, \"I have finished my work.\"",
      ["She said that she had finished her work.", "She said that she has finished her work.", "She said that she finished her work.", "She said that she had finish her work."], 0,
      "Present perfect → **past perfect**: had finished; I → she; my → her. B skips the backshift; C drops to simple past; D breaks the participle.",
      "have finished → had finished.",
      "easy", "narr-tense-shift", "ladder", 25),
    q("eng-narr-p08", "Select the option that expresses the given sentence in indirect speech.\n\nHe said to me, \"Please lend me your pen.\"",
      ["He requested me to lend him my pen.", "He requested me to lend me your pen.", "He ordered me to lend him my pen.", "He said to me please to lend him my pen."], 0,
      "Please → **requested**; to lend + him (speaker) + my (listener). B leaves both pronouns direct; C mismatches tone (ordered for a request); D has no sentence structure.",
      "please sets the verb: requested; then him + my.",
      "easy", "narr-questions-commands-exclamations", "request skeleton", 30),
    q("eng-narr-p09", "Select the option that expresses the given sentence in indirect speech.\n\nThey said, \"We shall visit Agra next month.\"",
      ["They said that they would visit Agra the following month.", "They said that they will visit Agra the following month.", "They said that they would visit Agra next month.", "They said that they should visit Agra the following month."], 0,
      "shall → **would** (with we/they in the past frame); next month → **the following month**. B skips the modal backshift; C strands 'next month'; D swaps shall for should, changing meaning.",
      "shall → would; next → the following.",
      "medium", "narr-pronouns-time-place", "modal + time", 30),
    q("eng-narr-p10", "Select the option that expresses the given sentence in indirect speech.\n\nThe doctor said to the patient, \"Give up smoking.\"",
      ["The doctor advised the patient to give up smoking.", "The doctor advised to the patient to give up smoking.", "The doctor advised the patient giving up smoking.", "The doctor said to the patient to giving up smoking."], 0,
      "Advice command → **advised + object + to + V1**. B adds a stray 'to' after advised; C drops the infinitive; D both breaks structure and keeps 'said to' where the tone verb fits.",
      "advice skeleton: advised + object + to + give.",
      "easy", "narr-questions-commands-exclamations", "advice skeleton", 25),
    q("eng-narr-p11", "Select the option that expresses the given sentence in indirect speech.\n\nHe said, \"Alas! I am ruined.\"",
      ["He exclaimed with sorrow that he was ruined.", "He exclaimed with joy that he was ruined.", "He said with sorrow that he is ruined.", "He exclaimed with sorrow that he is ruined."], 0,
      "Alas → **exclaimed with sorrow**; am → was (backshift); I → he. B inverts the tone; C leaves the tense; D strands 'is'.",
      "Alas = sorrow; am → was.",
      "easy", "narr-questions-commands-exclamations", "exclamation map", 25),
    q("eng-narr-p12", "Select the option that expresses the given sentence in direct speech.\n\nShe said that she had seen him the day before.",
      ["She said, \"I saw him yesterday.\"", "She said, \"I had seen him yesterday.\"", "She said, \"I have seen him yesterday.\"", "She said, \"I saw him the previous day.\""], 0,
      "'the day before' → **yesterday**; past perfect → **simple past** (saw) when the time anchor is restored; she → I, him stays. B keeps 'had seen' inside quotes; C pairs present perfect with yesterday (impossible); D leaves reported time words in a quote.",
      "Reverse ladder: had + V3 → V2 when the anchor returns as yesterday.",
      "hard", "narr-strategy", "reverse ladder", 40),
    q("eng-narr-p13", "Select the option that expresses the given sentence in indirect speech.\n\nHe said to her, \"What did you eat for breakfast?\"",
      ["He asked her what she had eaten for breakfast.", "He asked her what she ate for breakfast.", "He asked her what did she eat for breakfast.", "He asked her what she has eaten for breakfast."], 0,
      "Wh-question: keep 'what', flatten order, **past simple → past perfect** (did … eat → had eaten), you → she. B under-shifts; C keeps question order with dummy 'did'; D mis-shifts to present perfect.",
      "did + eat → had eaten; statement order after 'what'.",
      "medium", "narr-questions-commands-exclamations", "wh skeleton", 35),
    q("eng-narr-p14", "Select the option that expresses the given sentence in indirect speech.\n\nRam said to Shyam, \"You must bring your book tomorrow.\"",
      ["Ram told Shyam that he had to bring his book the next day.", "Ram told Shyam that he musted bring his book the next day.", "Ram told Shyam that he had to bring his book tomorrow.", "Ram told Shyam that you had to bring his book the next day."], 0,
      "must → **had to**; you → **he** (the listener Shyam); your → his; tomorrow → **the next day**. B invents 'musted'; C strands 'tomorrow'; D leaves 'you' in place.",
      "must → had to; listener's pronouns follow Shyam.",
      "medium", "narr-pronouns-time-place", "SONA + must", 35),
    q("eng-narr-p15", "Select the option that expresses the given sentence in indirect speech.\n\nThe boys said, \"Let us play football.\"",
      ["The boys suggested playing football.", "The boys suggested to play football.", "The boys told that they played football.", "The boys asked if they played football."], 0,
      "'Let us' = suggestion → **suggested + V-ing** (or suggested that they should play). B breaks the gerund pattern; C misreads it as a statement; D misreads it as a question.",
      "Let us → suggested + V-ing.",
      "medium", "narr-questions-commands-exclamations", "let-us skeleton", 30),
]

topic = {
    "id": "direct-indirect",
    "sectionId": "english",
    "title": "Direct & Indirect Speech",
    "order": 11,
    "importance": "medium",
    "avgQuestions": {"tier1": 2, "tier2": 3},
    "summary": "Two narration items per shift, all built from four moving parts: reporting verb, backshift ladder, pronoun anchors and the time/place word table. Statement, question, command, request and exclamation each have one fixed skeleton — learn the skeletons plus the exceptions (universal truths, frozen modals) and narration becomes a formula topic, both directions.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
