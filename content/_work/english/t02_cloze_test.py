from common import q, write_topic, md_table

# ---------------------------------------------------------------- passages
CLOZE_A = """Every morning, before the city fully (1) ______, a quiet crowd gathers in the parks. Retired teachers, young joggers and mothers returning from the dairy booths share the same paths. The morning walk costs nothing and demands no equipment, (2) ______ very few people manage to continue it beyond a fortnight. Doctors point out that its benefits depend almost entirely on (3) ______; twenty minutes on Sunday cannot undo six days of sitting. Over the weeks, a regular walker begins to (4) ______ noticeable changes — lighter steps, deeper sleep and a steadier mood. Perhaps that is why a group that walks together (5) ______ its own quiet discipline: the ones who arrive late feel they have missed something worth keeping."""

CLOZE_B = """When Arun was small, his grandfather took him to the village post office every Saturday. The old man (1) ______ a reply to letters from his brother in Pune, and he insisted that Arun add a line of his own at the bottom. 'A letter carries your handwriting, and handwriting carries your (2) ______,' he would say. Years later, Arun, now a software engineer, still (3) ______ that yellow ink pen in his office drawer, though he rarely posts anything. Last month, when his office announced a drive to send handwritten notes to retired employees, Arun (4) ______ to write fifty of them himself. His colleagues laughed at first; later that day, half of them (5) ______ him at the desk, writing their own notes."""

CLOZE_C = """Concrete has conquered our cities, and the first casualty has been the tree. A mature tree on a street does more than look (1) ______: it drops the temperature of its surroundings, traps dust and softens the noise of traffic. Yet when roads are widened, it is usually the tree that (2) ______ way. Municipal budgets treat planting as decoration rather than (3) ______, so saplings are planted in a rush before elections and forgotten soon afterwards. Survival, not planting, is the real (4) ______; a sapling needs watering for three full summers before it can stand on its own. Cities that have understood this simple point now pay residents a small sum to (5) ______ the trees outside their homes — and their streets are visibly greener."""

# ---------------------------------------------------------------- subtopics
blank_table = md_table(
    ["Blank type", "What decides the answer", "First check"],
    [
        ["Verb form / tense", "time anchors in surrounding sentences + subject number", "find the anchor word (yesterday, every day, since, by evening)"],
        ["Connector", "the logical relation between the two clauses it joins", "ask: contrast, cause, result or addition?"],
        ["Preposition / phrasal verb", "fixed collocation of the neighbouring word", "identify the governing verb/adjective/noun"],
        ["Noun / vocabulary", "meaning that fits the sentence AND the passage theme", "predict your own word before reading options"],
        ["Article / determiner", "sound of the next word + which-inference (specific or not)", "say the phrase aloud"],
    ],
)

connector_table = md_table(
    ["Relation", "Connectors", "Mini-test"],
    [
        ["Contrast", "but, yet, however, although, whereas, still", "the two clauses pull in opposite directions"],
        ["Cause", "because, since, as, for", "second clause explains why the first is true"],
        ["Result", "so, therefore, hence, thus, consequently", "second clause is the outcome of the first"],
        ["Addition", "moreover, besides, also, and, furthermore", "second clause adds a parallel point"],
        ["Condition", "if, unless, provided", "one clause depends on the other happening"],
        ["Time", "when, while, before, after, until", "one clause fixes when the other happens"],
    ],
)

phrasal_table = md_table(
    ["Phrasal verb", "Meaning", "Fit in a sentence"],
    [
        ["give way to", "yield; be replaced by", "the old market gave way to a mall"],
        ["look after", "take care of", "residents look after the street trees"],
        ["look into", "investigate", "the committee will look into the complaint"],
        ["carry out", "perform, execute", "carry out a survey / an order"],
        ["put off", "postpone", "the match was put off till Sunday"],
        ["call off", "cancel", "the strike was called off"],
        ["break out", "begin suddenly (fire, war, disease)", "a fire broke out at night"],
        ["turn down", "reject", "she turned down the offer"],
        ["come across", "meet/find by chance", "I came across an old diary"],
        ["set up", "establish", "a clinic was set up in the village"],
    ],
)

SUBTOPICS = [
    {
        "id": "cloze-strategy",
        "title": "What a cloze test is and how to attack it",
        "concept": f"""A cloze test is one short passage — usually 100–150 words — in which 5 words have been removed and numbered. Each question asks you to restore one blank. The passage is a *network*: every sentence you read constrains what the blanks can be, which is why cloze rewards a fixed method far more than raw vocabulary.

**The 5-step SSC method:**
1. Read the whole passage once, ignoring the blanks as far as possible. Fix the theme and the time frame (past narrative? general present? future plan?).
2. Note the tense anchor: the opening sentences usually fix the tense that most verb blanks must follow.
3. For each blank, *predict your own word* from the sentence's meaning before looking at the options.
4. Match options against your prediction; when none match, fall back to elimination by grammar (number, tense, part of speech) and logic.
5. After marking all five, read the completed passage once — it must sound like ordinary prose. Any jarring blank is usually a wrong choice.

{blank_table}

**Time budget:** under two minutes for the full read, 20–30 seconds per blank, 30 seconds for the final read-through. Attempt cloze in one sitting — the passage lives in your short-term memory only while the set is open.

**Never solve blanks in isolation.** An option that fits its own sentence but contradicts the passage's tense or theme is a planted trap; the final read-through exists to catch exactly this.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Tense anchor first",
                "body": "Before touching any blank, underline the time expressions: 'Every morning...', 'Last month...', 'by evening'. Verb blanks and even prepositions obey these anchors.",
                "example": {
                    "q": "Passage opens 'Every morning, before the city fully ___' — options: awaken / awakens / awakened / is awaken.",
                    "solution": "Anchor 'every morning' = habitual present; subject 'city' = singular → awakens.",
                },
            },
            {
                "title": "Predict, then match",
                "body": "Cover the options with your hand, read the sentence, and whisper your own word. Options are written to include your word's exact meaning — anything far from it is usually wrong.",
            },
            {
                "title": "The read-aloud finish",
                "body": "After answering all five, read the passage silently as if it were written by someone else. Grammar errors and logic breaks become audible — re-check any blank where you stumble.",
            },
        ],
        "mistakes": [
            "Answering blank by blank without reading the full passage first — you lose every cross-blank clue.",
            "Changing tense midway: a past-tense narrative forces past forms on later verb blanks.",
            "Choosing a word that fits the sentence's topic but not its logic (e.g. a cause-word where a contrast is needed).",
            "Spending equal time on every blank; easy grammar blanks take 15 seconds, bank that time for the vocabulary blank.",
        ],
    },
    {
        "id": "cloze-grammar-fit",
        "title": "Grammar inside the passage: tense, agreement, articles",
        "concept": f"""Most cloze blanks are won by grammar before vocabulary. Three systems matter.

**Tense.** The passage's opening fixes its time frame. A habitual opening ('Every morning...') demands simple present for habitual verbs; a past narrative ('When Arun was small...') demands past forms for events inside the story; 'still ___' with a present meaning demands present perfect or simple present, never past. Watch result words like *by evening / by the time*, which often need perfect forms — but only when the sentence truly looks back from a later point, not in simple narrative sequence.

**Subject–verb agreement.** SSC hides the subject between the blank and its neighbours: 'a group that walks together ___ its own discipline' — the subject is *a group* (singular), not *walks* or *discipline*. Strip the phrase to 'a group ___' and choose. Plurals to watch: *each, every, either, neither, everyone* → singular; *a number of* → plural, *the number of* → singular.

**Articles and determiners.** *A/an* is decided by sound, not spelling: *a university, an hour, a European, an MLA*. *The* appears when the noun is already known, unique, or specified by the phrase after it.

**Two-step verification for verb blanks:** (1) Does the tense match the passage anchor? (2) Does the form match the subject? An option passing only one test is a designed distractor.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Strip-to-subject",
                "body": "Delete every phrase between the subject and the verb blank, then apply agreement to the bare skeleton.",
                "example": {
                    "q": "'A group that walks together ___ its own quiet discipline.' Options: develop / develops / developing / developed(no context).",
                    "solution": "Skeleton: 'a group ___ discipline' → singular + habitual present → develops.",
                },
            },
            {
                "title": "Only-one-past trick",
                "body": "When a narrative blank offers just one past-tense option among present/gerund forms, the anchor already decided it — mark it and move on without re-reading the paragraph.",
            },
            {
                "title": "Say the article aloud",
                "body": "For a/an blanks, pronounce the *next word's first sound*: 'an hour' but 'a university'. Silent letters and 'yu' sounds decide it, not the first letter.",
            },
        ],
        "mistakes": [
            "Agreeing the verb with the nearest noun instead of the true subject.",
            "Using a perfect tense ('had joined') where plain narrative past is required, because 'by evening' looks like a perfect anchor.",
            "Choosing the base verb form after a singular subject ('the city awaken').",
            "Picking 'an' before words beginning with a vowel letter that is pronounced as a consonant ('a one-rupee coin').",
        ],
    },
    {
        "id": "cloze-vocab-fit",
        "title": "Vocabulary blanks: meaning, register and collocation",
        "concept": f"""Vocabulary blanks ask which *word* completes the sentence. Two filters decide, in order:

**1. Meaning filter.** The word must make the sentence true to the passage's logic. Read the sentence, note what idea is missing ('benefits depend on ___; twenty minutes on Sunday cannot undo six days of sitting' → the missing idea is *consistency*), then find the option naming that idea (*regularity*).

**2. Register filter.** SSC passages are written in neutral, slightly formal prose. Between two words of equal meaning, the neutral-formal one wins: *children* beats *kids*, *assistance* beats *a helping hand*, *begin* beats *kick off*. Slangy, poetic or babyish options are decoration.

**Collocation filter (often decisive).** Some words are only valid beside their partners: *gain momentum* (not *obtain momentum*), *pay attention* (not *give attention*), *heavy rain* (not *strong rain*), *do homework* (not *make homework*). When two options both fit the meaning, the collocation decides.

**Positive/negative fit.** Check the sentence's emotional direction. 'does more than look ___' in a passage praising trees wants a positive word (*attractive*); a criticism wants a negative one. An option of the wrong polarity is wrong regardless of meaning.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Name the missing idea",
                "body": "Before looking down, say what the sentence lacks in plain words: 'it needs the idea of CONSISTENCY here'. Then choose the option that says it — this defeats look-alike distractors.",
                "example": {
                    "q": "'...its benefits depend almost entirely on ___; twenty minutes on Sunday cannot undo six days of sitting.'",
                    "solution": "Missing idea = doing it regularly → regularity (not equipment, luck or medicine).",
                },
            },
            {
                "title": "Collocation pairs to bank",
                "body": "Memorise high-frequency pairs: gain momentum, pay attention, take measures, reach a decision, bear fruit, meet a deadline, break the news, strike a balance. Cloze nouns and verbs revolve around them.",
            },
            {
                "title": "Polarity check",
                "body": "Mark the sentence + or − before choosing. A praising sentence rejects negative words even when they are grammatically perfect.",
            },
        ],
        "mistakes": [
            "Choosing a word that fits the passage's *topic* instead of the sentence's *meaning*.",
            "Overlooking fixed pairs and choosing a near-synonym that no native writer would put in that slot.",
            "Selecting a big dictionary word when the passage's simple register wants the simple word.",
            "Forgetting that the same blank may be constrained by the NEXT sentence, not just its own.",
        ],
    },
    {
        "id": "cloze-connector-logic",
        "title": "Connector blanks: contrast, cause, result, addition",
        "concept": f"""A connector blank is a logic question in disguise. The option must name the exact relation between the clause before and the clause after.

**Two-clause test.** Split the sentence at the blank and ask how clause B behaves toward clause A:
- B pulls *against* A → contrast: **yet, but, however, although, still, whereas**.
- B explains *why* A is true → cause: **because, since, as**.
- B is the *outcome* of A → result: **so, therefore, hence, thus**.
- B *adds* a parallel point → addition: **moreover, besides, also, and**.

{connector_table}

**Signature SSC item:** praise followed by limitation. 'The walk costs nothing and demands no equipment, ___ very few people continue it' — the second clause concedes a limit, so *yet/but* is required; *so* or *because* breaks the logic. Train your ear on this pattern: it appears in nearly every paper.

**Placement grammar.** *However* and *therefore* need a comma and usually start a new sentence or clause ('..., however,'), while *yet/but/so* join clauses directly after a comma. If the blank sits between two clauses joined by a comma, the joining connector is grammatically safer.

**Double-connector pairs:** *not only... but also*, *either... or*, *neither... nor*, *both... and*, *no sooner... than*, *hardly... when*, *lest... should*. If one half appears outside the blank, only its partner can fill the blank.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Opposite-direction test",
                "body": "Give each clause a + or − sign. Same signs → addition/result connector; opposite signs → contrast connector.",
                "example": {
                    "q": "'The walk costs nothing and demands no equipment (+), ___ very few people continue it (−).'",
                    "solution": "+ then − → contrast → yet/but. 'So' or 'because' would need matching directions.",
                },
            },
            {
                "title": "Partner hunt",
                "body": "Scan the sentence for the other half of a correlative pair. Seeing 'not only' fixes the blank to 'but also' — zero thinking needed.",
            },
            {
                "title": "Comma tell",
                "body": "'clause, ___ clause' with a single-word slot wants *yet/but/so/for/and*. Options like 'however/therefore' fit 'clause. ___, clause' patterns instead.",
            },
        ],
        "mistakes": [
            "Confusing result (*so*) with cause (*because*) — read which clause explains which.",
            "Choosing 'although' where a plain 'but' is needed: *although* cannot join two independent clauses without restructuring.",
            "Ignoring the passage's flow: a connector that fits the sentence but reverses the paragraph's argument is wrong.",
            "Marking 'and' as always safe; in a concession context it destroys the author's point.",
        ],
    },
    {
        "id": "cloze-prepositions-phrasals",
        "title": "Preposition and phrasal-verb blanks",
        "concept": f"""Preposition blanks are pure collocation memory: the word before or after the blank dictates the answer.

**Find the governor.** The preposition belongs to a nearby verb, adjective or noun:
- depend **on**, insist **on**, congratulate **on**;
- afraid **of**, fond **of**, aware **of**;
- good **at**, angry **with** (person) / **at** (thing), married **to**;
- reason **for**, solution **to**, influence **on**, rise **in**.
Identify the governor, then recall its fixed partner — never translate meaning word by word.

**Phrasal-verb blanks** test verb + particle as one unit. The same verb changes meaning with each particle, so read the sentence's demand first, then match the unit: caring for trees → *look after*; investigating a complaint → *look into*; a road replacing a market → *give way to*.

{phrasal_table}

**Particles with a logic of their own:** *up* often completes (*finish, appear, build*), *off* suggests cancellation or departure, *out* suggests eruption or distribution, *down* suggests rejection or recording. When two options are grammatically possible, this direction sense breaks the tie.

**Preposition after 'different':** *different from* is the standard form in formal prose. **Preposition after 'compare'**: *compared to* (liken) vs *compared with* (examine differences) — in SSC usage both survive, but *compared to* is the safer default for similarity.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Governor chant",
                "body": "Underline the word governing the blank and recite its pair: depend—on, afraid—of, good—at, solution—to. Ten pairs cover most paper prepositions.",
                "example": {
                    "q": "'...now pay residents a small sum to ___ the trees outside their homes.' Options: look after / look into / look down upon / look up to.",
                    "solution": "Paying someone to care for trees → look after. *Look into* investigates, the other two are about respect/contempt.",
                },
            },
            {
                "title": "Particle direction sense",
                "body": "Ask what the sentence does to the object: cancels it (*call off*), rejects it (*turn down*), erects it (*set up*). The particle encodes the action's direction.",
            },
            {
                "title": "Substitute the simple verb",
                "body": "Replace the phrasal option with a one-word verb in your head: look after = tend. The sentence must keep its meaning with the substitution; if not, that phrasal is wrong.",
            },
        ],
        "mistakes": [
            "Choosing a preposition by intuition from Hindi rather than by the English governor.",
            "Splitting a phrasal verb: 'give way' needs its particle; 'gives way' without 'to' can also be the trap depending on the sentence.",
            "Mixing *between* and *among* — two items take *between*, an indefinite group takes *among*.",
            "Using *in* for years vs *on* for dates: 'in 2024' but 'on 15 August 2024'.",
        ],
    },
]

# ---------------------------------------------------------------- patterns
PATTERNS = [
    {
        "pattern": "Verb-form / tense blank",
        "frequency": "very common",
        "howToSpot": "Blank follows a singular/plural subject; options are forms of the same verb (awaken, awakens, awakened, awakening).",
        "approach": "Find the passage's time anchor, strip the sentence to subject + blank, then apply tense and agreement in that order.",
    },
    {
        "pattern": "Connector blank",
        "frequency": "very common",
        "howToSpot": "Blank sits at a clause boundary, often after a comma; options are yet/but/so/because/although class words.",
        "approach": "Split the clauses, give each a +/− direction, and pick the relation word that matches; check for a correlative partner elsewhere in the sentence.",
    },
    {
        "pattern": "Preposition / phrasal-verb blank",
        "frequency": "common",
        "howToSpot": "Options are prepositions (in/on/at) or short verb phrases (look after, give in); a verb/adjective sits next to the blank.",
        "approach": "Identify the governing word and recall its fixed partner; for phrasals, substitute a simple verb to test the meaning.",
    },
    {
        "pattern": "Noun / vocabulary blank",
        "frequency": "common",
        "howToSpot": "Options are unrelated words (regularity, equipment, luck, medicine); the sentence has a clear missing idea.",
        "approach": "Name the missing idea in plain words first, then match meaning, register and polarity — collocation breaks ties.",
    },
    {
        "pattern": "Article / determiner blank",
        "frequency": "occasional",
        "howToSpot": "Options are a/an/the; the blank precedes a noun or adjective + noun.",
        "approach": "Say the phrase aloud for a/an (sound rule); choose 'the' only when the noun is identified, unique or already mentioned.",
    },
    {
        "pattern": "Pronoun / relative-pronoun blank",
        "frequency": "occasional",
        "howToSpot": "Options are who/whom/whose/which/that; the blank introduces a clause describing a noun.",
        "approach": "Person + subject role → who; person + object role → whom; possession → whose; thing → which/that. Test by replacing with he/him.",
    },
]

# ---------------------------------------------------------------- solved examples
SE = [
    q("eng-cloze-s01",
      "Select the most appropriate option to fill in blank number (1).",
      ["awaken", "awakens", "awakened", "awakening"],
      1,
      "The anchor 'Every morning' fixes habitual simple present, and the subject 'the city' is singular, so the verb takes -s: **awakens**. *Awaken* is the plural/base form, *awakened* is a finished past that clashes with the habitual present of the whole passage, and *awakening* cannot serve as the finite verb after 'the city fully'.",
      "Time anchor first, agreement second: 'Every morning' + singular subject leaves exactly one form.",
      "easy", "cloze-grammar-fit", "verb form blank", 30,
      passage="Every morning, before the city fully (1) ______, a quiet crowd gathers in the parks. Retired teachers, young joggers and mothers returning from the dairy booths share the same paths.",
      group="cloze-se1"),
    q("eng-cloze-s02",
      "Select the most appropriate option to fill in blank number (2).",
      ["so", "because", "yet", "hence"],
      2,
      "Clause A is positive (the walk costs nothing, demands nothing); clause B is negative (very few continue it). Opposite directions demand a contrast connector: **yet**. *So* and *hence* announce a result and need both clauses pointing the same way; *because* would claim that the walk's cheapness is the *reason* few continue it — the opposite of the intended meaning.",
      "Give the two clauses +/− signs: plus then minus = contrast connector (yet/but).",
      "easy", "cloze-connector-logic", "connector blank", 30,
      passage="The morning walk costs nothing and demands no equipment, (2) ______ very few people manage to continue it beyond a fortnight.",
      group="cloze-se2"),
    q("eng-cloze-s03",
      "Select the most appropriate option to fill in blank number (5).",
      ["look into", "look after", "look down upon", "look up to"],
      1,
      "The city pays residents a small sum so that they will *take care of* the trees outside their homes: **look after**. *Look into* means investigate (a complaint), *look down upon* means regard as inferior, and *look up to* means admire — none names the action that keeps trees alive. Substituting the simple verb *tend* confirms the choice.",
      "Phrasal test: swap in the simple verb (tend). Only one option keeps the sentence's meaning.",
      "medium", "cloze-prepositions-phrasals", "phrasal verb blank", 30,
      passage="Cities that have understood this simple point now pay residents a small sum to (5) ______ the trees outside their homes — and their streets are visibly greener.",
      group="cloze-se3"),
]

# ---------------------------------------------------------------- practice
PRACTICE = [
    # ---- Cloze A: morning walk (5 blanks)
    q("eng-cloze-p01", "Select the most appropriate option to fill in blank number (1).",
      ["awaken", "awakens", "awakened", "awakening"], 1,
      "'Every morning' sets habitual present and 'the city' is singular, so the finite verb takes -s: **awakens**. *Awakened* would break the habitual frame, *awaken* lacks agreement, and *awakening* is not a finite verb form.",
      "Anchor + skeleton: 'every morning' + 'the city ___' → simple present with -s.",
      "easy", "cloze-grammar-fit", "verb form blank", 30,
      passage=CLOZE_A, group="cloze-pa"),
    q("eng-cloze-p02", "Select the most appropriate option to fill in blank number (2).",
      ["so", "because", "yet", "hence"], 2,
      "The clauses move in opposite directions — the walk demands nothing (+), yet few sustain it (−). Contrast is required: **yet**. *So/hence* would wrongly make continuation scarce a *result* of the walk's simplicity; *because* reverses the logic entirely.",
      "+ clause, − clause → contrast word (yet/but).",
      "easy", "cloze-connector-logic", "connector blank", 30,
      group="cloze-pa"),
    q("eng-cloze-p03", "Select the most appropriate option to fill in blank number (3).",
      ["equipment", "luck", "regularity", "medicine"], 2,
      "The clause after the semicolon supplies the meaning: twenty minutes on Sunday cannot undo six days of sitting — benefits depend on doing it **regularly**. The noun naming that idea is *regularity*. *Equipment* contradicts the earlier line that the walk demands no equipment; luck and medicine are outside the sentence's logic.",
      "Name the missing idea first ('consistency'), then match — the option echoing the next clause is the answer.",
      "easy", "cloze-vocab-fit", "noun blank", 35,
      group="cloze-pa"),
    q("eng-cloze-p04", "Select the most appropriate option to fill in blank number (4).",
      ["abandon", "postpone", "experience", "imagine"], 2,
      "The list that follows — lighter steps, deeper sleep, steadier mood — names changes the walker actually feels: a regular walker begins to **experience** noticeable changes. *Abandon* and *postpone* contradict the praise, and *imagine* breaks the factual tone the passage maintains about doctors' findings.",
      "Let the appositive list decide: the verb must introduce real, felt changes.",
      "easy", "cloze-vocab-fit", "verb-choice blank", 35,
      group="cloze-pa"),
    q("eng-cloze-p05", "Select the most appropriate option to fill in blank number (5).",
      ["develop", "develops", "developing", "had developed"], 1,
      "Strip the sentence to its skeleton: 'a group ___ its own quiet discipline'. The subject *a group* is singular and the passage speaks in general present, so: **develops**. *Develop* lacks agreement; *developing* cannot serve as the finite verb; *had developed* drags in a past perfect that has no anchor in this habitual, timeless statement.",
      "Skeleton test: 'a group ___' → singular present, -s form.",
      "medium", "cloze-grammar-fit", "subject-verb agreement blank", 35,
      group="cloze-pa"),

    # ---- Cloze B: grandfather's letters (5 blanks)
    q("eng-cloze-p06", "Select the most appropriate option to fill in blank number (1).",
      ["draft", "drafts", "drafted", "drafting"], 2,
      "The passage is a past narrative ('When Arun was small... every Saturday'), so the habitual action inside it takes simple past: **drafted**. Only one option is a past form; *draft/drafts* break the time frame and *drafting* is not a finite verb.",
      "Narrative-past passage: find the only past-tense option and verify the subject is singular.",
      "easy", "cloze-grammar-fit", "tense blank", 30,
      passage=CLOZE_B, group="cloze-pb"),
    q("eng-cloze-p07", "Select the most appropriate option to fill in blank number (2).",
      ["presence", "punctuality", "pressure", "payment"], 0,
      "The grandfather argues that a letter carries your handwriting and handwriting carries your **presence** — your self, personally there on the page. *Punctuality, pressure, payment* are abstract nouns that fit the grammar but destroy the sentimental logic: the point is that a handwritten letter carries the writer himself.",
      "Meaning filter: the sentence defines handwriting as a stand-in for the person — choose the word meaning 'the person there'.",
      "medium", "cloze-vocab-fit", "noun blank", 35,
      group="cloze-pb"),
    q("eng-cloze-p08", "Select the most appropriate option to fill in blank number (3).",
      ["keep", "kept", "keeps", "keeping"], 2,
      "'Years later, Arun, now a software engineer, still ___ that pen' — the sentence describes Arun's present habit (note *now*, *still*), with singular subject Arun: **keeps**. *Kept* would clash with 'now/still'; *keep* lacks agreement; *keeping* is not finite.",
      "'Still + now' marks a living present habit → simple present with -s.",
      "easy", "cloze-grammar-fit", "tense blank", 30,
      group="cloze-pb"),
    q("eng-cloze-p09", "Select the most appropriate option to fill in blank number (4).",
      ["volunteer", "volunteers", "volunteered", "volunteering"], 2,
      "'Last month' anchors the event in finished past time, and the subject Arun is singular: **volunteered**. The other options are present, base or non-finite forms that cannot sit after a past-time adverbial in this narrative.",
      "Time adverbial decides: 'last month' + singular subject → volunteered.",
      "easy", "cloze-grammar-fit", "tense blank", 30,
      group="cloze-pb"),
    q("eng-cloze-p10", "Select the most appropriate option to fill in blank number (5).",
      ["join", "joins", "joined", "joining"], 2,
      "The narrative continues in simple past sequence ('His colleagues laughed at first; later that day, half of them ___ him'): **joined**. It is the only finite past form; *joins* breaks the frame, *join* lacks agreement with 'half of them' in past narrative, and *joining* cannot act as the verb.",
      "Narrative sequence: second event after 'laughed' takes plain past — no perfect needed in simple storytelling.",
      "easy", "cloze-grammar-fit", "tense blank", 30,
      group="cloze-pb"),

    # ---- Cloze C: trees in cities (5 blanks)
    q("eng-cloze-p11", "Select the most appropriate option to fill in blank number (1).",
      ["attractive", "attracted", "attraction", "attractively"], 0,
      "After the linking verb *look* (here 'does more than look'), an **adjective** is required: look attractive. *Attractively* is an adverb and cannot follow a linking verb; *attracted* is a verb form and *attraction* a noun, neither of which fits 'look ___' in the sense 'appear'.",
      "Linking-verb test: look/sound/seem + adjective, never adverb.",
      "medium", "cloze-grammar-fit", "adjective after linking verb", 35,
      passage=CLOZE_C, group="cloze-pc"),
    q("eng-cloze-p12", "Select the most appropriate option to fill in blank number (2).",
      ["give", "gives", "gave", "giving"], 1,
      "The subject of the blank is 'the tree' (singular) and the passage argues in general present: 'it is usually the tree that **gives** way'. *Give* lacks agreement, *gave* would need a past anchor the paragraph does not have, and *giving* is non-finite. The collocation is 'give way (to)' = yield.",
      "Skeleton: 'the tree that ___ way' → singular present -s.",
      "medium", "cloze-grammar-fit", "subject-verb agreement blank", 35,
      group="cloze-pc"),
    q("eng-cloze-p13", "Select the most appropriate option to fill in blank number (3).",
      ["infrastructure", "entertainment", "souvenir", "ceremony"], 0,
      "The contrast is 'decoration rather than ___', and the passage argues trees are functional city assets — cooling, dust-trapping, noise-softening. The noun for functional city assets is **infrastructure**. *Entertainment, souvenir, ceremony* fit the grammar but belong to no part of the argument.",
      "Contrast frame 'X rather than Y' wants Y from the same serious category as the argument — trees as urban equipment.",
      "medium", "cloze-vocab-fit", "noun blank", 35,
      group="cloze-pc"),
    q("eng-cloze-p14", "Select the most appropriate option to fill in blank number (4).",
      ["test", "festival", "holiday", "gift"], 0,
      "'Survival, not planting, is the real ___' — the sentence says the difficult part is keeping saplings alive (three summers of watering). The word for the demanding part is **test**. *Festival/holiday/gift* carry celebratory meanings that clash with 'needs watering for three full summers'.",
      "The clause after the semicolon glosses the blank: hard ongoing work → test.",
      "easy", "cloze-vocab-fit", "noun blank", 35,
      group="cloze-pc"),
    q("eng-cloze-p15", "Select the most appropriate option to fill in blank number (5).",
      ["look after", "look into", "look down upon", "look up to"], 0,
      "The city pays residents to *take care of* the trees outside their homes: **look after**. *Look into* means investigate; *look down upon* means despise; *look up to* means admire. Only *look after* names an action whose absence would leave streets un-green and whose payment makes civic sense.",
      "Substitute 'tend' — the option surviving the substitution wins.",
      "easy", "cloze-prepositions-phrasals", "phrasal verb blank", 35,
      group="cloze-pc"),
]

topic = {
    "id": "cloze-test",
    "sectionId": "english",
    "title": "Cloze Test",
    "order": 2,
    "importance": "high",
    "avgQuestions": {"tier1": 5, "tier2": 5},
    "summary": "One short passage with five numbered blanks, attempted as a single set — 5 marks that reward method over memory. Most blanks are decided by the passage's tense anchor, clause logic or a fixed collocation, so a trained routine converts cloze into the most reliable scoring block in the English section.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
