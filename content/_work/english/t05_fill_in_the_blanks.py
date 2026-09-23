from common import q, write_topic, md_table

FB = "Select the most appropriate option to fill in the blank.\n\n"

# ---------------------------------------------------------------- subtopics
coll_table = md_table(
    ["Verb + noun", "Adjective + noun", "Meaning"],
    [
        ["pay attention / compliments", "staunch supporter", "loyal follower"],
        ["strike a balance / a bargain", "soaring prices", "rising fast"],
        ["break the news / a record", "grave mistake / crisis", "very serious"],
        ["take place / pride / measures", "scathing attack", "bitterly critical"],
        ["make efforts / amends", "teeming millions", "crowds of people"],
        ["do business / justice / harm", "invaluable service", "too valuable to price"],
        ["commit a mistake / a crime", "abject poverty", "utter, hopeless"],
        ["reach a conclusion / a consensus", "conclusive evidence", "settling the issue"],
        ["cast a vote / a glance", "close scrutiny", "careful examination"],
        ["lay emphasis / claim / hands on", "level playing field", "fair conditions"],
        ["gain ground / momentum", "glaring error", "shockingly obvious"],
        ["bear fruit / a resemblance", "barren land / effort", "unproductive"],
    ],
)

phrasal_table = md_table(
    ["Phrasal verb", "Meaning", "Sentence cue"],
    [
        ["call off", "cancel", "the strike was called off"],
        ["put up with", "tolerate", "she cannot put up with noise"],
        ["carry out", "perform, execute", "carry out orders / a survey"],
        ["break out", "begin suddenly", "a fire broke out"],
        ["look into", "investigate", "the panel will look into it"],
        ["turn down", "reject", "he turned down the offer"],
        ["give in", "surrender", "the rebels finally gave in"],
        ["run out of", "exhaust the stock of", "we ran out of time"],
        ["do away with", "abolish", "the tax was done away with"],
        ["bring about", "cause to happen", "the reform brought about change"],
        ["cut down on", "reduce", "cut down on sugar"],
        ["stand by", "support; remain loyal", "she stood by her friend"],
    ],
)

confuse_table = md_table(
    ["Pair", "Meanings", "Correct use"],
    [
        ["affect / effect", "verb: influence / noun: result", "Rains **affect** crops; the **effect** was visible."],
        ["advice / advise", "noun (an advice) / verb (to advise)", "The doctor **advised** rest; follow his **advice**."],
        ["practice / practise", "noun (Indian English) / verb", "Daily **practice** helps; **practise** daily."],
        ["principal / principle", "chief, head / a rule", "**Principal** amount; a man of **principle**."],
        ["stationary / stationery", "not moving / writing materials", "a **stationary** van; office **stationery**."],
        ["loose / lose", "not tight / misplace", "a **loose** tooth; **lose** the keys."],
        ["site / sight / cite", "place / vision / quote", "a construction **site**; at first **sight**; **cite** a case."],
        ["complement / compliment", "completes / praise", "wine **complements** food; pay a **compliment**."],
        ["discreet / discrete", "careful / separate", "**discreet** enquiries; **discrete** units."],
        ["eligible / illegible", "qualified / unreadable", "**eligible** voters; **illegible** signature."],
        ["beside / besides", "next to / in addition to", "sat **beside** me; **besides** swimming."],
        ["assure / ensure / insure", "remove doubt / make certain / cover by policy", "**assure** the public; **ensure** safety; **insure** the car."],
        ["lie / lay", "recline (lie–lay–lain) / put (lay–laid)", "**lie** down; **lay** the pen on the table."],
    ],
)

connective_table = md_table(
    ["Pair", "Fixed shape", "Trap option"],
    [
        ["Hardly / Scarcely ... when", "Hardly had she entered **when** the lights went out.", "**than** (belongs to no sooner)"],
        ["No sooner ... than", "No sooner had he sat down **than**...", "**when**"],
        ["Not only ... but also", "not only cheap **but also** durable", "but, and"],
        ["Both ... and", "**Both** the manager **and** his staff were present", "as well as"],
        ["Rather ... than", "would resign **rather than** apologize", "then"],
        ["Too ... to", "**too** weak **to** walk", "so, very"],
        ["So ... that", "**so** weak **that** he could not walk", "too"],
        ["Lest ... should", "run fast **lest** you **should** miss it", "or else"],
    ],
)

SUBTOPICS = [
    {
        "id": "fb-collocations",
        "title": "Collocation blanks: word partnerships that decide the answer",
        "concept": f"""A collocation is a pair of words that native usage glues together. When a blank sits beside a verb or an adjective, the answer is usually whatever that word *partners* with — not any word of similar meaning.

{coll_table}

**How to use the governor.** Identify the word immediately governing the blank:
- blank after a verb → the verb's usual object (*break the news*, *take place*);
- blank before a noun → the noun's usual adjective (*grave mistake*, *close scrutiny*);
- blank after a noun → its usual verb (*prices soar*, *attention pays*? — attention takes *pay*).

**Why collocation beats meaning.** 'made a mistake' and 'committed a mistake' both 'make sense', but SSC's standard answer follows the strongest partnership (*commit a mistake*, *commit a crime*). Similarly *reach* a conclusion (not *arrive* a conclusion), *pay* attention (not *give* attention), *heavy* rain (not *strong* rain).

**Register check.** When two partnerships both exist, the neutral-formal one fits SSC prose: *hold talks* beats *hold chats*; *offer condolences* beats *give sorrows* (which is not even an English partnership).

Build your pairing instinct in two weeks: one table of 10 pairs a day, and each pair immediately used in a sentence of your own. Recognition in the exam comes from *having produced* the pair once, not from having read it.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Governor-first reading",
                "body": "Read the sentence up to the blank, stop, and ask: 'What does this word usually take next?' Answer from memory, then look at the options — your answer is usually sitting there verbatim.",
                "example": {
                    "q": "The two leaders held detailed ___ on the border dispute.",
                    "solution": "'held detailed...' asks for a discussion noun → *deliberations*. Celebrations/medications are topic-inappropriate; 'reverberations' is sound.",
                },
            },
            {
                "title": "Topic veto",
                "body": "Collocation options in SSC are often same-suffix decoys (-tions, -ments). Kill them by topic first: a border dispute invites *talks/deliberations*, never *medications*.",
            },
            {
                "title": "Verb-object completeness",
                "body": "For verb blanks, complete the object in your head: 'attention is ___' → paid. If your completing verb is an option, mark it and move on.",
            },
        ],
        "mistakes": [
            "Choosing a synonym that breaks the partnership ('pay attention' → 'give attention').",
            "Being impressed by long words; the collocation answer is usually the ordinary word.",
            "Ignoring the preposition that follows the blank ('deliberations on', 'effect on').",
            "Confusing adjective–noun order: the blank's side tells you its part of speech.",
        ],
    },
    {
        "id": "fb-phrasal-verbs",
        "title": "Phrasal-verb blanks: verb + particle as one unit",
        "concept": f"""A phrasal verb is verb + particle(s) whose meaning is not the sum of its parts. Blanks here test whether you own the unit.

{phrasal_table}

**Two shapes of the blank.** Sometimes the particle is blanked ('call ___ the merger') and the verb is given; sometimes the whole unit is blanked among look-alike verbs ('___ up with the noise'). In both, the sentence's *action* decides:
- cancelling → call **off**;
- enduring → put **up with**;
- rejecting → turn **down**;
- abolishing → do away **with**.

**Particles carry direction.** *off* = cancel/away, *out* = erupt/distribute, *up* = appear/build, *down* = reject/reduce, *in* = surrender/enter. When two particles both look grammatical, this direction sense separates them.

**Transitive or not.** *Put up with* needs an object ('put up with the noise'); *give in* needs none ('the rebels gave in'). If the blank follows a ready object, a transitive unit is the answer; if the sentence ends at the blank, an intransitive one.

**Separable units.** 'called the meeting off' and 'called off the meeting' are both valid — so if the object sits between the blank's verb and particle, the unit is separable, and only that shape fits. Improvement items exploit this; fill-in items usually keep the unit intact.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Name the action, then match the unit",
                "body": "Say the sentence's action in one plain word (cancelled, tolerated, abolished), then pick the phrasal unit that translates it. The wrong particles translate other actions.",
                "example": {
                    "q": "The company had to call ___ the proposed merger after the audit.",
                    "solution": "Action = cancel → call **off**. *Call up* telephones, *call for* demands, *call out* shouts — different verbs entirely.",
                },
            },
            {
                "title": "Particle direction check",
                "body": "Ask what the sentence does to its object — kills it (off/out), raises it (up), lowers it (down), accepts it (in). Match the particle's direction to the verb's fate.",
            },
            {
                "title": "Simple-verb substitution",
                "body": "Replace each option with a one-word verb (call off = cancel). The option whose substitution keeps the sentence's meaning is the answer.",
            },
        ],
        "mistakes": [
            "Choosing the particle that follows the preposition logic of the first language.",
            "Mixing *put up with* (tolerate) with *put off* (postpone) because both contain 'put'.",
            "Reading only the clause containing the blank; the actor and time usually sit in the previous clause.",
            "Forgetting that 'break out' (war, fire, disease) has no passive — 'was broken out' is impossible.",
        ],
    },
    {
        "id": "fb-verb-form-tense",
        "title": "Verb-form and tense blanks",
        "concept": f"""When the blank is a verb, two checks decide: the **anchor** (time information in the sentence) and the **form demanded by the governing word**.

**Anchors → tenses:**
- *By the time X arrived, ...* → the earlier event is past perfect: *had burnt*.
- *since 2015 / for ten years* (continuing) → present perfect (continuous).
- *yesterday / last week* → simple past.
- *by next March* → future perfect: *will have completed*.

**Governing words → forms (the highest-yield list):**
- *look forward to + -ing* (to = preposition): *I look forward to **hearing** from you*.
- *used to + base* (past habit) vs *be used to + -ing* (accustomed): *He used to **swim***; *He is used to **swimming***.
- *had better / would rather + base*: *You had better **leave***.
- *avoid / enjoy / mind / finish / suggest + -ing*.
- *decide / plan / hope / refuse + to + base*.
- preposition + -ing: *insisted on **paying***, *afraid of **losing***.

**The preposition-to test** settles most -ing vs to-blank confusion: if the word before 'to' is a noun, pronoun or preposition-like verb (look forward, be accustomed, object), the 'to' is prepositional → *-ing* follows. If 'to' belongs to an infinitive (decide, refuse, hope), the base verb follows.

**Passive shapes** also appear: after *by the time*, a completed earlier event can be *had been + participle* when the subject receives the action (*had been evacuated*)."""
        ,
        "formulas": [],
        "tricks": [
            {
                "title": "Preposition-to test",
                "body": "Check what owns the 'to'. Owned by a preposition-verb or noun → -ing; owned by an infinitive verb → base form. This one test answers the largest tense-form family.",
                "example": {
                    "q": "I look forward to ___ from you soon. → hearing",
                    "solution": "'Forward to' is prepositional ('look forward to it'), so the -ing form follows: *hearing*.",
                },
            },
            {
                "title": "By-the-time ladder",
                "body": "Two events with 'by the time' → earlier verb in past perfect, later in simple past. Fit the blank to its rung of the ladder.",
            },
            {
                "title": "Verb-category lists",
                "body": "Memorise the three mini-lists: -ing verbs (avoid, enjoy, mind, suggest, finish), to-verbs (decide, hope, refuse, plan), base-after (had better, would rather, let, make).",
            },
        ],
        "mistakes": [
            "Choosing 'to hear' after 'look forward to' because 'to' feels infinitive.",
            "Using present perfect with a finished-time anchor.",
            "Writing 'used to + -ing' for past habits (that shape means 'accustomed').",
            "Ignoring the passive when the sentence's subject receives the action.",
        ],
    },
    {
        "id": "fb-connectives-pronouns",
        "title": "Connective and relative-pronoun blanks",
        "concept": f"""Connective blanks join two clauses; the relation between the clauses, not the meaning of any single word, is the answer.

{connective_table}

**The +/- test again:** give each clause a direction. Same directions → *so/therefore/and*; opposite → *but/yet/although*; explanation → *because/since*; outcome → *so/therefore*. For fixed pairs, both halves must appear: 'Hardly had... **when**', 'No sooner had... **than**' — the trap options simply swap the partners.

**Relative pronouns.** The blank joining a describing clause to its noun:
- person + subject role → **who** (*the leader **who** inspires*);
- person + object role → **whom** (*the leader **whom** everyone trusts* — test by rephrasing: *everyone trusts him*);
- possession → **whose**; things → **which/that**;
- place → **where**; time → **when**; reason → **why**.
The he/him substitution is foolproof: replace the pronoun's slot with he (→ who) or him (→ whom).

**Concessive pairs:** *Although/Though* pairs with *yet* (never *but*): 'Although it rained, **yet** the match continued' is standard formal usage; SSC accepts plain 'Although... the match continued' equally. *Despite/In spite of* take noun/-ing, never a full clause ('despite it rained' is wrong).""",
        "formulas": [],
        "tricks": [
            {
                "title": "Partner scan before choosing",
                "body": "Search the sentence for the other half of the pair. Seeing 'Hardly had' fixes the blank to *when*; seeing 'No sooner' fixes it to *than*. Zero deliberation needed.",
                "example": {
                    "q": "Hardly had she entered the room ___ the lights went out.",
                    "solution": "'Hardly had...' → partner **when**. *Than* belongs to 'No sooner'.",
                },
            },
            {
                "title": "He/him substitution for who/whom",
                "body": "Rephrase the clause with he/him: 'everyone trusts (him)' → whom; '(he) inspires everyone' → who. No ambiguity survives the substitution.",
            },
            {
                "title": "Despite/Although sorting",
                "body": "Full clause after the blank → Although/Though; noun or -ing → Despite/In spite of. The trap options swap these two families.",
            },
        ],
        "mistakes": [
            "Choosing 'than' after 'Hardly/Scarcely' because 'comparison' instinct fires.",
            "Using 'whom' as a clause subject ('the man whom came') — case is decided by the clause role, not by prestige.",
            "Joining a full clause with 'despite' or a bare noun with 'although'.",
            "Selecting 'which' for a person or 'who' for a thing under time pressure.",
        ],
    },
    {
        "id": "fb-homonyms-confusables",
        "title": "Confusable and homonym blanks",
        "concept": f"""These blanks offer four words of similar shape; only one fits both the grammar slot and the meaning.

{confuse_table}

**Two-step decision.**
1. **Part of speech.** *advise* (verb) vs *advice* (noun): find the sentence's verb — if it already has one, the blank is likely a noun, and vice versa. Same for *practice/practise*, *effect/affect* (noun vs verb).
2. **Meaning.** *stationary* (not moving) vs *stationery* (writing material); *principal* (chief) vs *principle* (rule). The sentence's context — a godown of paper goods, a bank's sums — picks one.

**Spelling-distinct pairs with one meaning slot:** *eligible* (qualified) vs *illegible* (unreadable); *discreet* (careful) vs *discrete* (separate); *complement* (completes) vs *compliment* (praise). Meaning decides alone.

**The assure/ensure/insure family** deserves its own memorisation: *assure* a person (remove doubt), *ensure* an outcome (make certain), *insure* a thing (insurance policy). 'The minister gave a solemn **assurance**' is the noun of *assure* — options include *insurance* to trap the shape-reader.

**Sound-alike traps in options** (affection, effectiveness, advices) exist to punish incomplete reading: reject them on grammar ('advices' is not a countable noun in standard English) and on meaning.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Slot first, meaning second",
                "body": "Decide noun/verb/adjective from the sentence frame; kill every option of the wrong class. Then choose by meaning among survivors — usually only two ever reach step two.",
                "example": {
                    "q": "The doctor ___ him to take complete rest. Options: advised / advice / advices / advise.",
                    "solution": "The sentence needs a finite past verb (subject 'doctor', no other verb) → **advised**. *Advice* is a noun, *advices* is not standard, *advise* is the wrong tense/number fit here.",
                },
            },
            {
                "title": "Context picture",
                "body": "Form a mental image of the sentence: a pile of paper in a godown → stationery; a parked van → stationary. The image picks the spelling instantly.",
            },
            {
                "title": "Triple-family cards",
                "body": "Make flash cards only for families of three or more: assure/ensure/insure, site/sight/cite, affect/effect/affective. Singles rarely appear in options.",
            },
        ],
        "mistakes": [
            "Choosing the familiar spelling ('affect') when the slot demands the noun ('effect').",
            "Reading 'advice/advise' as interchangeable because dictionaries mark the Indian-English overlap.",
            "Picking 'illegible' for eligibility contexts because the negative prefix sounds right.",
            "Missing that the sentence already has a verb, so the blank must be a noun.",
        ],
    },
    {
        "id": "fb-double-blanks",
        "title": "Double blanks: two gaps, one sentence",
        "concept": f"""Some items blank two positions in one sentence — a pair of connectors (*___ he was ill, ___ he came*), a structure pair (*too ... to*, *so ... that*), or two content words. Options are complete pairs.

**Method: anchor the solid blank first.** One of the two gaps is usually much easier — a structure pair whose second element is fixed (*too ___ to*), or a content word only one option can fit. Decide that gap, and the wrong pairs collapse:
- '*___ small ___ accommodate*' → the structure is *too + adj + to + verb* → **too, to**. 'So, that' would need a clause ('so small that it could not accommodate'), and the option's second element ('that') does not fit the blank before the bare verb.
- '*___ the manager ___ his assistants were present*' → plural *were* + two-part subject → **Both, and**. 'Neither, or' is not a pair; 'Either, or' would demand singular agreement.

**Agreement as a tiebreak.** The sentence's verb exposes the pair: plural verb → *both... and* (or a plural pair), singular verb → *either... or / neither... nor* (verb follows the nearer noun).

**Cross-check both halves.** After anchoring one blank, read the completed sentence aloud; if the second half jars, your anchor was the trap — the option pairs are built so that exactly one completes both halves naturally.

**Content-word pairs** (e.g. '*safe and sound*', '*part and parcel*') are fixed binomials — learn the common ones in pairs, never singly: *safe and sound, first and foremost, null and void, ways and means, pros and cons, part and parcel*.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Structure-pair recognition",
                "body": "too + adjective + to + base verb; so + adjective + that + clause; such + noun + that + clause; hardly...when; no sooner...than. Recognise the skeleton and both blanks fill at once.",
                "example": {
                    "q": "The room was ___ small ___ accommodate all the guests.",
                    "solution": "Adjective + bare verb after the second blank → *too small to accommodate*. 'So, that' would demand 'that it could not accommodate'.",
                },
            },
            {
                "title": "Verb-agreement tiebreak",
                "body": "Plural verb with two subjects → Both...and; singular verb → Either...or / Neither...nor (matching the nearer noun). The verb alone often fixes the pair.",
            },
            {
                "title": "Fixed binomial bank",
                "body": "Revise binomials in pairs: safe and sound, part and parcel, null and void, first and foremost, ways and means. Options split genuine binomials with a wrong partner — the genuine one is the answer.",
            },
        ],
        "mistakes": [
            "Solving blank two first when blank one is the structural anchor.",
            "Choosing 'so, that' where the second blank precedes a bare verb (structure mismatch).",
            "Matching plural 'Both...and' to a singular-verb sentence.",
            "Assembling a binomial that half-exists ('part and half') because the first half matched.",
        ],
    },
]

# ---------------------------------------------------------------- patterns
PATTERNS = [
    {
        "pattern": "Collocation blank (single word)",
        "frequency": "very common",
        "howToSpot": "Blank sits beside a verb or adjective; options are same-suffix nouns/verbs of related meaning.",
        "approach": "Find the governor, recall its usual partner, veto decoys by topic and suffix.",
    },
    {
        "pattern": "Confusable word (shape pair/triple)",
        "frequency": "common",
        "howToSpot": "Options differ by spelling or suffix: advice/advise, effect/affect, stationery/stationary, eligible/illegible.",
        "approach": "Fix the part of speech from the frame first, then pick by meaning; reject non-standard forms outright.",
    },
    {
        "pattern": "Phrasal verb blank",
        "frequency": "common",
        "howToSpot": "Options are particles (off/out/up) or short verb units (look into, carry out) around a clear action.",
        "approach": "Name the action in plain words, then match the unit; check particle direction and transitivity.",
    },
    {
        "pattern": "Tense / verb-form blank",
        "frequency": "common",
        "howToSpot": "Blank is a verb; anchors like 'by the time', 'since', 'yesterday' or governing words like 'look forward to' are visible.",
        "approach": "Anchor fixes the tense; the preposition-to test fixes -ing vs base form.",
    },
    {
        "pattern": "Double blank (pair options)",
        "frequency": "occasional",
        "howToSpot": "Two blanks per sentence, options are pairs such as 'Both, and' / 'too, to' / 'Although, called off'.",
        "approach": "Anchor the easier gap (usually the structural half), let it eliminate pairs, then cross-check the second half.",
    },
    {
        "pattern": "Connective / relative pronoun blank",
        "frequency": "occasional",
        "howToSpot": "Blank joins two clauses (Hardly... ___, Although... ___) or a relative clause (the leader ___ everyone trusts).",
        "approach": "Use clause relation and fixed partners for connectives; he/him substitution for who/whom.",
    },
]

# ---------------------------------------------------------------- solved examples
SE = [
    q("eng-fb-s01", FB + "The manager managed to ___ a balance between the two demanding clients.",
      ["strike", "knock", "break", "pull"], 0,
      "The fixed partnership is **strike a balance** (= find a middle position). *Knock/break/pull a balance* are not English partnerships — the options are ordinary verbs placed to test pairing memory, not meaning.",
      "Recall the partnership, not the dictionary: balance → strike.",
      "easy", "fb-collocations", "collocation", 30),
    q("eng-fb-s02", FB + "The villagers could no longer put ___ with the erratic power supply.",
      ["up", "on", "off", "in"], 0,
      "The sentence needs 'tolerate': **put up with**. *Put on* wears, *put off* postpones, *put in* installs — each particle builds a different verb. The cue 'could no longer' + a nuisance noun demands the tolerate-unit.",
      "Name the action (tolerate) and match the unit: tolerate = put up with.",
      "easy", "fb-phrasal-verbs", "phrasal verb", 30),
    q("eng-fb-s03", FB + "___ the students ___ the teacher was aware of the change in schedule.",
      ["Both, and", "Either, or", "Neither, or", "Not only, but"], 1,
      "The verb *was* is singular. 'Both...and' demands a plural verb (*were*), and 'Neither, or' is not a pair. With *Either...or*, the verb agrees with the nearer subject — *the teacher* (singular) → **was**, exactly as the sentence reads. 'Not only, but' is incomplete without 'also'.",
      "Verb agreement decides the pair: singular was after a two-part subject → Either...or (nearer subject singular).",
      "medium", "fb-double-blanks", "double blank with agreement", 35),
]

# ---------------------------------------------------------------- practice
PRACTICE = [
    q("eng-fb-p01", FB + "The two leaders held detailed ___ on the border dispute.",
      ["deliberations", "celebrations", "medications", "reverberations"], 0,
      "'Held detailed ___ on a dispute' asks for the discussion partnership: **deliberations**. The other options share the -tion shape but belong to wrong topics — parties celebrate, patients take medication, sound reverberates.",
      "Governor-first: 'held detailed ___ on' → deliberations on.",
      "easy", "fb-collocations", "collocation", 30),
    q("eng-fb-p02", FB + "The new taxation policy will have a far-reaching ___ on small traders.",
      ["effect", "affect", "affection", "effectiveness"], 0,
      "After the article *a* the blank must be a noun, and the meaning is 'result': **effect**. *Affect* is the verb; *affection* is fondness; *effectiveness* needs no 'a far-reaching' frame and changes the meaning.",
      "Slot first: a ___ → noun → effect.",
      "easy", "fb-homonyms-confusables", "confusable", 30),
    q("eng-fb-p03", FB + "The company had to call ___ the proposed merger after the audit report.",
      ["off", "out", "up", "for"], 0,
      "Action = cancel: **call off**. *Call up* telephones, *call out* challenges/announces, *call for* demands — none survives the substitution test.",
      "Substitute 'cancel' — the surviving particle is off.",
      "easy", "fb-phrasal-verbs", "phrasal verb", 30),
    q("eng-fb-p04", FB + "The retired professor could not put ___ with the constant construction noise.",
      ["up", "on", "in", "across"], 0,
      "Tolerate = **put up with**, a three-word unit whose object follows ('with the noise'). *Put on/off/in/across* build other meanings — wear, postpone, install, communicate.",
      "Nuisance + 'could not' → tolerate → put up with.",
      "easy", "fb-phrasal-verbs", "phrasal verb", 30),
    q("eng-fb-p05", FB + "By the time the firefighters arrived, the wooden shed ___ to ashes.",
      ["had burnt", "has burnt", "was burning", "has been burning"], 0,
      "'By the time + past event' makes the blank the earlier of two past actions → past perfect: **had burnt**. Present-perfect options clash with the past anchor, and 'was burning' describes a mid-process rather than the completed ruin.",
      "By-the-time ladder: earlier event → had + participle.",
      "easy", "fb-verb-form-tense", "past perfect", 30),
    q("eng-fb-p06", FB + "I look forward to ___ from you at the earliest.",
      ["hearing", "hear", "be heard", "have heard"], 0,
      "'Look forward to' is prepositional ('forward to it'), so the -ing form follows: **hearing**. The other options serve an infinitive or passive slot that this frame does not have.",
      "Preposition-to test → -ing.",
      "easy", "fb-verb-form-tense", "verb form after preposition-to", 30),
    q("eng-fb-p07", FB + "___ it rained heavily throughout the day, the final match was not ___.",
      ["Although, called off", "Because, called on", "Although, called up", "Because, called out"], 0,
      "The clauses contrast (rain vs the match happening) → concession: **Although** — this eliminates both 'Because' pairs. A match that is not played is **called off**; *called on* visits, *called up* telephones. Only the first pair completes both halves.",
      "Anchor the connective (contrast → Although), then match the phrasal to the meaning.",
      "medium", "fb-double-blanks", "double blank", 40),
    q("eng-fb-p08", FB + "Hardly had the chief guest taken his seat ___ the curtains rose.",
      ["when", "than", "then", "that"], 0,
      "'Hardly had...' partners with **when**: 'Hardly had X happened when Y happened'. *Than* belongs exclusively to 'No sooner...than'.",
      "Partner scan: Hardly → when.",
      "easy", "fb-connectives-pronouns", "fixed pair", 30),
    q("eng-fb-p09", FB + "The paediatrician ___ the mother to complete the full course of medicine.",
      ["advised", "advice", "advices", "advising"], 0,
      "The sentence needs a finite past verb after its subject: **advised**. *Advice* is a noun, *advices* is not standard English, *advising* cannot serve alone as the verb.",
      "Frame first: subject + blank + object → finite verb → advised.",
      "easy", "fb-homonyms-confusables", "confusable", 30),
    q("eng-fb-p10", FB + "All the ___ items — pens, registers and markers — were locked in the storeroom.",
      ["stationery", "stationary", "stationerily", "stationer"], 0,
      "Pens, registers and markers are writing materials: **stationery**. *Stationary* means not moving — the items may be stationary too, but the apposition with the list pins the meaning to the writing-materials word.",
      "Context picture: pens and registers → stationery.",
      "easy", "fb-homonyms-confusables", "confusable", 30),
    q("eng-fb-p11", FB + "The union leader ___ every worker trusts was re-elected without a contest.",
      ["whom", "whose", "which", "what"], 0,
      "Rephrase the clause: 'every worker trusts (him)' — object role, person → **whom**. *Whose* shows possession, *which* serves things, *what* does not introduce such relative clauses.",
      "He/him substitution: trusts him → whom.",
      "medium", "fb-connectives-pronouns", "relative pronoun", 35),
    q("eng-fb-p12", FB + "The Principal congratulated the debate team ___ winning the national championship.",
      ["on", "for", "at", "with"], 0,
      "The fixed partnership is **congratulate on**: 'congratulated the team on winning'. The -ing after the blank is exactly what this frame expects.",
      "Governor chant: congratulate—on.",
      "easy", "fb-collocations", "verb + preposition", 25),
    q("eng-fb-p13", FB + "The auditorium was ___ small ___ accommodate the entire graduating batch.",
      ["too, to", "so, that", "very, to", "too, for"], 0,
      "Adjective + bare verb after the second blank → the *too + adj + to + base verb* structure: **too small to accommodate**. 'So, that' would need a full clause ('so small that it could not accommodate'), 'very' forms no pair, and 'too, for' needs a noun after 'for'.",
      "Recognise the skeleton: too + adj + to + verb.",
      "medium", "fb-double-blanks", "double blank structure", 35),
    q("eng-fb-p14", FB + "___ the manager ___ his assistants were responsible for the filing error.",
      ["Both, and", "Either, or", "Neither, or", "Not only, but"], 0,
      "The verb *were* is plural, and 'Both...and' is the only listed pair that takes plural agreement. 'Either, or' would agree with the nearer subject (*assistants* — plural!) — but the pair 'Neither, or' is invalid English, and 'Not only, but' is incomplete without 'also'.",
      "Verb agreement tiebreak: plural were with a full two-part subject → Both...and.",
      "medium", "fb-double-blanks", "double blank with agreement", 40),
    q("eng-fb-p15", FB + "The minister gave a solemn ___ that the pending project would be cleared within a month.",
      ["assurance", "insurance", "endurance", "abundance"], 0,
      "A solemn statement meant to remove doubt is an **assurance** — the noun partner of *assure*. *Insurance* covers risk by policy, *endurance* is the power to bear hardship, *abundance* is plenty — none fits 'gave a solemn ___ that'.",
      "Assure/ensure/insure family: person reassured → assurance.",
      "medium", "fb-homonyms-confusables", "confusable family", 30),
]

topic = {
    "id": "fill-in-the-blanks",
    "sectionId": "english",
    "title": "Fill in the Blanks",
    "order": 5,
    "importance": "high",
    "avgQuestions": {"tier1": 3, "tier2": 5},
    "summary": "One sentence, one or two blanks, four options — decided almost always by a collocation, a phrasal unit, a tense anchor or a confusable pair, not by dictionary size. Every blank has a governor (a word beside it) that dictates the answer; finding that governor first is the whole technique.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
