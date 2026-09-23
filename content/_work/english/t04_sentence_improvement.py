from common import q, write_topic, md_table

SI = "Select the most appropriate option to substitute the highlighted segment in the given sentence. If no substitution is required, select 'No substitution required'.\n\n"

# ---------------------------------------------------------------- subtopics
ladder_table = md_table(
    ["Rung", "Question", "What it kills"],
    [
        ["1. Verb form & tense", "is the highlighted verb the right form for its anchor and helper?", "tense clashes (with 'yesterday'), wrong form after did/have, non-finite where finite is needed"],
        ["2. Agreement", "does the verb match the TRUE subject?", "plural verbs after 'each', 'one of', 'the list of', 'as well as'"],
        ["3. Structure", "is word order and pairing standard (inversion, that of, correlative pairs)?", "broken inversions, mixed pairs, compared-with-itself errors"],
        ["4. Word choice & idiom", "is the preposition/word the fixed partner?", "insisted for, angry on, return back"],
        ["5. Economy", "does any option say the same thing in fewer, cleaner words?", "redundant add-ons — but beware over-pruning"],
    ],
)

# ---------------------------------------------------------------- subtopics
SUBTOPICS = [
    {
        "id": "si-elimination",
        "title": "The elimination ladder: how to choose in 20 seconds",
        "concept": f"""Sentence improvement gives you a sentence with one highlighted segment and four substitutes (often including 'No substitution required'). You are not hunting for the *best-sounding* English — you are hunting for the option that survives every grammatical test the original failed.

**Work the ladder top to bottom; eliminate as you descend:**

{ladder_table}

**The three-option rule:** in most items, two options die instantly on rung 1 (wrong verb form) or rung 2 (agreement). That leaves a pair; rung 3 or 4 separates them. Practise announcing WHY an option dies — 'fails agreement', 'breaks the pair', 'wrong preposition partner' — and the ladder becomes automatic.

**'No substitution required' discipline:** before accepting it, run rungs 1–3 once. It is correct in roughly a quarter of such items — a real option, not a decoy. But never choose it because the sentence merely sounds acceptable; if the highlighted verb disagrees with its subject, 'sounds fine' is irrelevant.

**When two options both seem right:** prefer the one that is *closer to the original in meaning*. The exam improves grammar, not the writer's ideas. An option that subtly changes who did what, or adds information, is wrong even if its grammar is clean.

**Timing:** 20–30 seconds. Read the full sentence first — the part BEFORE the highlight usually carries the anchor (yesterday, did, each, no sooner) that decides everything.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Anchor before options",
                "body": "Find the time word or helper verb near the highlight ('yesterday', 'did', 'each of the'), decide what the verb must look like, then pick the option matching YOUR form.",
                "example": {
                    "q": "She **has met** him yesterday evening. Options: met / has meet / was met / No substitution required.",
                    "solution": "Anchor 'yesterday' = finished past → simple past 'met'. Option 1; the other two fail rung 1 outright.",
                },
            },
            {
                "title": "Death-note elimination",
                "body": "In your head, tag every option with its fatal flaw before choosing: 'plural verb', 'breaks inversion', 'wrong partner'. If no option has a flaw, the answer is 'No substitution required'.",
            },
            {
                "title": "Meaning guard",
                "body": "Between two grammatical survivors, choose the one that preserves the original meaning word for word — the exam rewards accuracy, not elegance.",
            },
        ],
        "mistakes": [
            "Choosing a grammatical option that changes the meaning (active↔passive swap, added agents).",
            "Picking 'No substitution required' because the sentence sounds natural at speed.",
            "Improving a part that was never highlighted — only the bold segment may change.",
            "Overlooking the anchor in the unhighlighted part of the sentence.",
        ],
    },
    {
        "id": "si-tense-sequence",
        "title": "Tense and sequence fixes",
        "concept": f"""A large share of improvement items highlight a verb whose tense contradicts a visible anchor.

**Anchor → required form:**
- *yesterday, last week, in 2010, ago* → simple past; any perfect form is wrong.
- *since/for + still true* → perfect or perfect continuous: *has been living since 2015* (not *is living* / *lived*).
- *already/just* with an earlier past event → past perfect: *had left*.
- *when/if/until* with future meaning → simple present in the clause, *will* in the main clause only.
- reported speech after a past reporting verb → backshift AND statement word order: *asked why I **had left*** (not *why did I leave*).

**Test the pair, not the word:** tense errors are relative. The highlighted verb must agree in time with its neighbour. Read the whole sentence across the highlight, never the highlight alone.

**Continuous vs simple:** continuous forms need an ongoing frame. *She **was cooking** when the guests arrived* is right; *She **cooked** when the guests arrived* changes the meaning (two sequential events). Improvement questions exploit exactly this contrast — pick the form that preserves the original meaning.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Yesterday test",
                "body": "See a finished-time anchor? Kill every perfect and continuous option instantly — one survivor usually remains.",
                "example": {
                    "q": "The train **has left** before we reached the station.",
                    "solution": "Both events are past; the earlier needs past perfect → *had left*. 'Has left' is present perfect — dead on rung 1.",
                },
            },
            {
                "title": "Backshift + straight order",
                "body": "In reported questions after *asked/told*, two things must change: tense backshifts and the question flips to statement order ('why he had left'). Each option usually breaks exactly one of the two — check both.",
            },
            {
                "title": "Since/for health check",
                "body": "'Since 2015 / for ten years' demands a perfect form with *been* if the action continues. Options without *have/has been* die at once.",
            },
        ],
        "mistakes": [
            "Choosing present perfect with 'yesterday/last year' because it 'sounds formal'.",
            "Backshifting tense but keeping question order (or vice versa) in reported speech.",
            "Replacing a correct perfect with simple past when 'since/for' is present.",
            "Changing continuous to simple (or back) and silently altering the meaning.",
        ],
    },
    {
        "id": "si-agreement",
        "title": "Agreement and verb-form fixes",
        "concept": f"""When the highlighted segment is (or contains) a verb, run the agreement audit: find the TRUE subject.

**Interrupters that never change number:** *of the..., as well as, along with, together with, in addition to, accompanied by, and not, besides*. The verb follows the first, real subject:
- *The list of candidates **was** displayed* (list).
- *One of the students **has** won* (one).
- *The captain, as well as the players, **was** fined* (captain).

**Always-singular subjects:** *each, every, everyone, everybody, either, neither, nobody, one*. Always-plural in effect: *cattle, police, people*.

**Verb form after helpers:** after *did/does/do* → base form; after *have/has/had* → past participle; after *be* → *-ing* (continuous) or participle (passive). Improvement items highlight the wrong slot of this chain: *did he **arrived*** → *did he arrive*.

**There is/there are:** the verb agrees with the noun AFTER it — *There **is** a temple and two shops* is acceptable SSC usage when the first noun governs; but standard items usually keep simple agreement with the real subject, so audit that noun first.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Cover the phrase, read the skeleton",
                "body": "Physically cover 'of the candidates'-type phrases with a finger and read what remains: 'The list ___ displayed'. The agreeing verb is now obvious.",
                "example": {
                    "q": "One of the students **have** won the quiz. Options: has / were / are / No substitution required.",
                    "solution": "Skeleton: 'One ___ won' → has. Plural options die on rung 2.",
                },
            },
            {
                "title": "Helper-chain audit",
                "body": "did → base, have → participle, be → -ing/participle. When the highlight contains a helper, check the partner form first — that is where the planted error lives.",
            },
            {
                "title": "Two-subject sentence check",
                "body": "If two subjects are joined by *and*, the verb is plural — unless the pair names one thing ('bread and butter **is**'). SSC plants singular verbs before such pairs.",
            },
        ],
        "mistakes": [
            "Agreeing with the nearest noun instead of the head subject.",
            "Writing a participle where the base form belongs after *did*.",
            "Choosing a passive-looking option that adds or deletes an agent and changes meaning.",
            "Marking plural verbs correct after 'each of the + plural noun' because the plural noun is nearer.",
        ],
    },
    {
        "id": "si-comparison-structure",
        "title": "Comparison and structural fixes",
        "concept": f"""**Comparison fixes.** Two recurring shapes:
1. Double marker: *more better, most fastest* → drop the extra word (*better, fastest*).
2. Unlike things compared: *The climate of Shimla is cooler than **Delhi*** → compare climate with climate: ***that of* Delhi**. Singular possession → *that of*; plural → *those of*. This tiny pronoun is one of SSC's favourite right answers.

**Structural fixes** are about standard shapes:
- Inversion after negative openers: *Hardly **had I reached**... when...*, *No sooner **did he arrive** than...*, *Not only **did she sing**, but she also danced*. The highlighted segment is usually the un-inverted half.
- Correlative pairs kept parallel: *not only + verb ↔ but also + verb*; *both... and*; *either... or*.
- Dangling modifiers: an *-ing* opener must describe the subject that follows. *Walking through the park, the flowers attracted the child* → the child must become the subject: *Walking through the park, **the child was attracted by the flowers***.
- Word order in embedded questions: *He asked **why I had left*** (statement order).

**The repair must be minimal.** Among options that fix the fault, SSC's key is the smallest correct change. An option that rewrites half the sentence is usually there to distract.""",
        "formulas": [],
        "tricks": [
            {
                "title": "that-of insertion",
                "body": "When two possessive phrases are compared and only the second is highlighted, 'that of / those of' is almost always the answer. Check number: singular → that of, plural → those of.",
                "example": {
                    "q": "The roads of Bhopal are wider than **Indore**. Options: those of Indore / that of Indore / Indore's roads are / No substitution required.",
                    "solution": "Roads (plural) vs roads → *those of Indore*.",
                },
            },
            {
                "title": "Negative-opener flip",
                "body": "See *Hardly/No sooner/Not only/Little* at sentence start? Expect auxiliary-before-subject order in the highlighted part: 'had I reached', 'did he arrive'. Un-inverted options die on rung 3.",
            },
            {
                "title": "-ing opener ownership",
                "body": "Ask WHO is doing the -ing action. The sentence's main subject must be that doer; if not, pick the option that makes the doer the subject.",
            },
        ],
        "mistakes": [
            "Choosing 'than that of' when the comparison is not possessive at all.",
            "Inverting a clause that has no negative opener.",
            "Fixing a dangling modifier by moving the modifier instead of changing the subject.",
            "Treating 'No substitution required' as wrong whenever the sentence looks plain — plain and correct are different things.",
        ],
    },
    {
        "id": "si-precision-fixes",
        "title": "Precision fixes: articles, prepositions, pronouns, word choice",
        "concept": f"""Some highlights contain no verb at all — the fault is a wrong *small word* or a wrong *word pair*.

**Articles:** sound decides *a/an* (*an hour, a university, an MLA*); specificity decides *the* (*the same, the most intelligent, the Ganga*). Improvement items usually highlight the article-plus-noun together: *She is **a honest** woman* → *an honest woman*.

**Prepositions:** recall the governor's fixed partner — *insist on, apologize to... for, angry with (person), good at, married to, prefer to, depend on, consist of*. The wrong partner is planted; the right partner is the answer.

**Pronoun case:** after prepositions → object form (*between you and **me***); as reflexive only when the subject and object are the same person (*She cooked herself lunch*) — *myself* cannot replace *me/I* in ordinary sentences, a favourite decoy.

**Word choice and redundancy:**
- redundant pairs die: *return back → return*, *repeat again → repeat*, *revert back → revert*.
- confusables flip meaning: *few/a few, little/a little, much/many, fewer/less* — the improvement item asks which one the sentence's logic needs ('There is **a little** water left' = some, positive).
- *elder* (family, no *than*) vs *older than*; *farther* (distance) vs *further* (additional).

**One-word economy:** between two correct options, the standard written form wins — *because* over *due to the fact that*, *although* over *despite of the fact that* ('despite of' is itself wrong: *despite* or *in spite of*).""",
        "formulas": [],
        "tricks": [
            {
                "title": "Small-word sweep",
                "body": "Read ONLY the small words in the highlight (a/an/the, in/on/at, I/me/myself). A wrong one usually stands alone in its wrongness — fix it and finish.",
                "example": {
                    "q": "She is **a honest** woman. Options: an honest / the honest / honest / No substitution required.",
                    "solution": "Vowel sound 'o' in *honest* → *an honest woman*. 'Honest' alone would leave 'She is honest woman' — ungrammatical.",
                },
            },
            {
                "title": "myself firewall",
                "body": "Reflexives never replace plain object pronouns. Any option offering *myself* where *me* belongs is a decoy — kill it on sight.",
            },
            {
                "title": "Redundancy flinch",
                "body": "Train on the fatal pairs: return back, repeat again, revert back, final conclusion. When one appears highlighted, the shorter option is the key.",
            },
        ],
        "mistakes": [
            "Choosing 'the' before a superlative-less unique noun or dropping it where it belongs.",
            "Picking 'myself' as a polite-sounding substitute for 'me'.",
            "Correcting *few* to *a few* (or back) without reading whether the sentence means 'some' or 'hardly any'.",
            "Writing 'despite of' — the standard forms are *despite* and *in spite of*.",
        ],
    },
    {
        "id": "si-structure-inversion",
        "title": "Structural fixes: inversion, dangling modifiers, parallelism",
        "concept": """Some highlights fail not in tense or agreement but in *sentence architecture*. Three shapes cover the exam.

**Inversion after negative openers.** When *Hardly, Scarcely, No sooner, Not only, Little, Never, Rarely* opens the sentence, the auxiliary jumps before the subject:
- *Hardly **had I reached** the office when...* (past perfect pairs with *when*);
- *No sooner **did he arrive** than...* (base form after *did*, partner *than*);
- *Not only **did she sing**, but she also danced* (parallel verbs on both halves).
The un-inverted order ('I had reached', 'he arrived') is the planted fault.

**Dangling modifiers.** An *-ing* or participle opener must describe the sentence's main subject. *Walking through the garden, **the flowers** fascinated the boy* — flowers cannot walk. The repair makes the true doer the subject: *Walking through the garden, the boy was fascinated by the flowers*. Reject fixes that merely move the opener around; the subject must change.

**Parallelism under pairs and lists.** *Not only X but also Y* needs X and Y in the same grammatical shape (verb with verb, noun with noun, clause with clause). The same holds for *either... or*, *neither... nor*, *both... and*, and for item lists (*reading, writing, and to speak* → *speaking*).

**Embedded-question order.** Inside a reported question the statement order returns: *He asked **why I had left***, never 'why did I leave'. Improvement items highlight exactly this stretch.

Each of these fixes is a *shape*, not a judgement call — memorise the four shapes and the correct option announces itself.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Opener triggers flip",
                "body": "Negative word first? Then expect 'auxiliary + subject': had I reached, did he arrive, did she sing. Choose the option in flipped order with the right partner (when/than).",
                "example": {
                    "q": "No sooner he **arrived** than the power failed. → did he arrive",
                    "solution": "*No sooner* + inversion + base form after *did* + *than*: the full shape must be present, not part of it.",
                },
            },
            {
                "title": "Who is doing the -ing?",
                "body": "Name the doer of the opening action; if the main subject is not that doer, pick the option that promotes the doer to subject.",
            },
            {
                "title": "Shape-match across pairs",
                "body": "Cover the pair words and compare the shapes on both sides: 'not only [verbed] ... but also [verb]' — any mismatch in form is the fault being tested.",
            },
        ],
        "mistakes": [
            "Inverting a clause with no negative opener, or forgetting to invert when there is one.",
            "Pairing 'Hardly... than' or 'No sooner... when' — the partners are fixed.",
            "Fixing a dangling modifier by rewording the opener instead of changing the subject.",
            "Ignoring parallelism: 'not only cheap but also it lasts long' mixes adjective with clause.",
        ],
    },
]

# ---------------------------------------------------------------- patterns
PATTERNS = [
    {
        "pattern": "Tense-form substitution",
        "frequency": "very common",
        "howToSpot": "Highlighted verb + a visible time anchor (yesterday, since, already, when-clause) or a reporting verb before it.",
        "approach": "Anchor decides the form; kill options failing the anchor, then check statement order for reported speech.",
    },
    {
        "pattern": "Agreement substitution",
        "frequency": "common",
        "howToSpot": "Highlighted verb after 'each of', 'one of', 'the list of', 'as well as', or an and-pair naming one thing.",
        "approach": "Strip interrupters to the true subject; choose the matching verb form.",
    },
    {
        "pattern": "'No substitution required' items",
        "frequency": "common",
        "howToSpot": "One option reads 'No substitution required' while the sentence is already standard.",
        "approach": "Run rungs 1–3 of the ladder once; if no option holds a flaw, accept the original confidently.",
    },
    {
        "pattern": "Comparison repair",
        "frequency": "common",
        "howToSpot": "Highlighted segment inside a than-comparison; options include 'that of / those of' variants or de-doubled comparatives.",
        "approach": "Compare like with like (insert that of / those of) and remove double markers.",
    },
    {
        "pattern": "Preposition / pronoun / article fix",
        "frequency": "common",
        "howToSpot": "Highlight contains a small word: a/an/the, in/on/for, I/me/myself, or a wrong word pair (return back).",
        "approach": "Recall the governor's fixed partner or the sound rule; kill reflexive-pronoun decoys.",
    },
    {
        "pattern": "Structural repair (inversion, dangling modifier, parallelism)",
        "frequency": "occasional",
        "howToSpot": "Negative opener (Hardly/No sooner/Not only), an -ing opener followed by a non-doer subject, or unparallel not-only/but-also halves.",
        "approach": "Apply the standard shape: invert after the opener, make the -ing doer the subject, match forms across pairs.",
    },
]

# ---------------------------------------------------------------- solved examples
SE = [
    q("eng-si-s01", SI + "She **has met** him yesterday evening.",
      ["met", "has meet", "was met", "No substitution required"], 0,
      "The anchor *yesterday evening* fixes finished past time, so the simple past **met** is required; present perfect (*has met*) cannot sit beside a finished-time adverbial. *Has meet* is doubly wrong (no third form), and *was met* turns the meaning into a passive. Ladder: rung 1 kills three options in one stroke.",
      "Finished-time anchor (yesterday) → simple past. One check, three options dead.",
      "easy", "si-tense-sequence", "anchor-based tense fix", 30),
    q("eng-si-s02", SI + "The climate of Shimla is cooler than **Delhi**.",
      ["that of Delhi", "Delhi's climate is", "those of Delhi", "No substitution required"], 0,
      "A comparison must compare like with like: climate with climate. *That of Delhi* = 'the climate of Delhi' — singular *that* matches singular *climate*. *Those of* is plural and cannot replace a singular noun's possession, and 'Delhi's climate is' produces a doubled clause ('the climate ... is cooler than Delhi's climate is') that changes the structure. Ladder: rung 3 (standard structural shape).",
      "Two possessive phrases compared + only the second highlighted → 'that of' (singular) / 'those of' (plural).",
      "medium", "si-comparison-structure", "that-of comparison fix", 35),
    q("eng-si-s03", SI + "He has been working in this office **since** 2015 without a single complaint.",
      ["for", "from", "by", "No substitution required"], 3,
      "*Since* + a point of time (*2015*) with a continuing perfect continuous is exactly standard: rungs 1–4 find no fault. *For* takes durations (*for eight years*), *from* needs a endpoint framing and no perfect, *by* marks deadlines. When the original is standard, **No substitution required** is the answer — and it must be chosen with the same confidence as any other option.",
      "If every rung finds no flaw, mark 'No substitution required' and move on — do not second-guess.",
      "easy", "si-tense-sequence", "no-substitution discipline", 30),
]

# ---------------------------------------------------------------- practice
PRACTICE = [
    q("eng-si-p01", SI + "The list of selected candidates **were** displayed on the notice board.",
      ["was", "were being", "have", "No substitution required"], 0,
      "The true subject is *list* (singular); 'of selected candidates' is an interrupter. → *was displayed*. Plural options fail agreement; the original fails too.",
      "Cover 'of the candidates': 'the list ___' → was.",
      "easy", "si-agreement", "agreement fix", 30),
    q("eng-si-p02", SI + "One of the students **have** won the inter-college quiz.",
      ["has", "were", "are", "No substitution required"], 0,
      "*One* is the subject: 'One of the students **has** won'. The plural noun *students* sits inside the interrupting phrase.",
      "Skeleton 'one ___' → has.",
      "easy", "si-agreement", "one-of agreement fix", 30),
    q("eng-si-p03", SI + "This new road is **more better** than the old one.",
      ["better", "more good", "good", "No substitution required"], 0,
      "*Better* is already comparative; *more* doubles the marker. → *better than the old one*. 'More good' repeats the fault, and 'good' destroys the comparison entirely.",
      "Double comparative: delete the extra marker, keep the comparative.",
      "easy", "si-comparison-structure", "double comparative fix", 25),
    q("eng-si-p04", SI + "The roads of Bhopal are wider than **Indore**.",
      ["those of Indore", "that of Indore", "Indore's roads are", "No substitution required"], 0,
      "Compare roads with roads: plural noun → **those of Indore**. *That of* is singular and wrong here; 'Indore's roads are' creates a doubled clause; 'No substitution required' leaves an unlike comparison.",
      "Plural possession compared → those of; singular → that of.",
      "medium", "si-comparison-structure", "those-of comparison fix", 35),
    q("eng-si-p05", SI + "She insisted **for** paying the full fare before boarding.",
      ["on", "at", "with", "No substitution required"], 0,
      "*Insist* takes **on**: 'insisted on paying'. The gerund after the preposition is correct, so only the partner is at fault.",
      "Governor chant: insist—on.",
      "easy", "si-precision-fixes", "preposition partner fix", 25),
    q("eng-si-p06", SI + "After serving abroad for a decade, he **returned back** to his hometown.",
      ["returned", "return back", "was returned", "No substitution required"], 0,
      "*Return* already means 'come back'; *back* is redundant → **returned**. 'Was returned' changes the meaning to a passive (someone sent him).",
      "Redundant pair: return + back → keep the simple verb.",
      "easy", "si-precision-fixes", "redundancy fix", 25),
    q("eng-si-p07", SI + "Between you and **I**, this welfare scheme has several loopholes.",
      ["me", "us", "myself", "No substitution required"], 0,
      "A preposition takes object forms: *between you and **me***. *Myself* is a reflexive and cannot replace *me* — a favourite decoy.",
      "Preposition + I → flip to me; never accept 'myself' as a fix.",
      "easy", "si-precision-fixes", "pronoun case fix", 25),
    q("eng-si-p08", SI + "My grandmother is **a honest** and hardworking woman.",
      ["an honest", "the honest", "a honestly", "No substitution required"], 0,
      "*Honest* begins with a vowel sound (the h is silent): **an honest**. 'The honest' over-specifics the generic sentence; 'a honestly' is wrong twice (article and part of speech).",
      "Silent-h words take 'an'.",
      "easy", "si-precision-fixes", "article fix", 25),
    q("eng-si-p09", SI + "No sooner he **arrived** than the power supply failed.",
      ["did he arrive", "he did arrive", "had he arrive", "No substitution required"], 0,
      "*No sooner* at the start demands inversion + *than*: **did he arrive** (base form after *did*). 'Had he arrive' mixes the *had* inversion with a base form, and 'he did arrive' is not inverted.",
      "No sooner → did + subject + base verb + than.",
      "medium", "si-structure-inversion", "inversion fix", 35),
    q("eng-si-p10", SI + "Hardly **I had reached** the office when the fire alarm went off.",
      ["had I reached", "did I reached", "I had reach", "No substitution required"], 0,
      "*Hardly* opening the sentence forces auxiliary-first order: **had I reached** (past perfect pairs with *when*). 'Did I reached' pairs *did* with a past form; 'I had reach' keeps statement order and breaks the participle.",
      "Hardly/Scarcely at sentence start → had + subject + participle.",
      "medium", "si-structure-inversion", "inversion fix", 35),
    q("eng-si-p11", SI + "Walking through the garden, **the flowers** fascinated the little boy.",
      ["the little boy was fascinated by the flowers", "the little boy fascinated the flowers", "the flowers were fascinating", "No substitution required"], 0,
      "The *-ing* opener (*walking*) must describe the main subject. Flowers cannot walk, so the boy must become the subject: *Walking through the garden, **the little boy was fascinated by the flowers***. 'The little boy fascinated the flowers' reverses who fascinated whom; 'the flowers were fascinating' keeps the dangling structure; 'No substitution required' leaves it unfixed.",
      "-ing opener: ask WHO walks — make that doer the subject.",
      "medium", "si-structure-inversion", "dangling modifier fix", 40),
    q("eng-si-p12", SI + "The manager asked me **why did I** leave my previous job without notice.",
      ["why I had", "why had I", "that why I", "No substitution required"], 0,
      "After the past reporting verb *asked*, an indirect question needs statement order + backshift: **why I had** left. 'Why had I' backshifts nothing and keeps question order; 'that why I' wrongly glues *that* to *why*; the original commits both faults.",
      "Reported question: tense backshifts AND word order straightens.",
      "medium", "si-tense-sequence", "reported speech fix", 35),
    q("eng-si-p13", SI + "He has been living in Chennai **since** 2015 and has no plans to move.",
      ["for", "from", "by", "No substitution required"], 3,
      "*Since* + point of time with a continuing perfect is standard: rungs 1–4 find no fault. *For* needs a duration (*for nine years*), *from* and *by* do not pair with this perfect. → **No substitution required**.",
      "Since = point, for = span. The original is standard; trust it.",
      "easy", "si-tense-sequence", "no-substitution discipline", 30),
    q("eng-si-p14", SI + "Neither of the two answers **were** acceptable to the examiner.",
      ["was", "have been", "are", "No substitution required"], 0,
      "*Neither* is singular → **was** acceptable. 'Have been' and 'are' repeat the plural fault; the original fails agreement.",
      "Neither/either/each → singular verb, always.",
      "easy", "si-agreement", "neither agreement fix", 30),
    q("eng-si-p15", SI + "My elder brother is **two years senior** than me in service.",
      ["senior to", "more senior than", "senior of", "No substitution required"], 0,
      "Latin comparatives (*senior, junior, superior, inferior, prior*) take **to**, never *than*: *two years senior to me*. 'More senior than' doubles the comparison; 'senior of' is not a form.",
      "senior/junior/superior/inferior/prefer + to. Memorise the family of five.",
      "medium", "si-comparison-structure", "senior-to fix", 30),
]

topic = {
    "id": "sentence-improvement",
    "sectionId": "english",
    "title": "Sentence Improvement",
    "order": 4,
    "importance": "high",
    "avgQuestions": {"tier1": 2, "tier2": 4},
    "summary": "One highlighted segment per sentence must be corrected — or left alone ('No substitution required'). The same fault families recur as error-spotting (agreement, tense, comparison, prepositions, inversion), so the elimination ladder — verb form, agreement, structure, word choice, economy — resolves most items in under thirty seconds.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
