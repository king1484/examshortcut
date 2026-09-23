from common import q, write_topic, md_table

ES = "The following sentence has been divided into parts. One of them contains an error. Select the part that contains the error.\n\n"

# ---------------------------------------------------------------- subtopics
check_table = md_table(
    ["Check", "Ask yourself", "Instant example"],
    [
        ["1. Subject–verb", "what is the TRUE subject, and how far is it from the verb?", "*The quality of the mangoes **were*** → subject = quality (singular)"],
        ["2. Tense", "is there a time anchor? do the clauses agree in time?", "***had** reached* before a later past event"],
        ["3. Article", "sound of the next word? specific or general?", "***an** university* → a university"],
        ["4. Preposition", "which word governs it, and what is its fixed partner?", "*insisted **for*** → insisted on"],
        ["5. Pronoun", "case (subject/object)? does it match its antecedent?", "*between you and **I*** → me"],
        ["6. Conjunction/correlative", "are both halves of the pair present and parallel?", "*No sooner did... **rang*** → ring"],
        ["7. Comparison / word choice", "double comparative? redundancy? wrong confusable?", "*more bigger*, *return back*"],
    ],
)

sva_table = md_table(
    ["Construction", "Rule", "SSC-style example"],
    [
        ["Each / every / either / neither / everyone / nobody", "always singular", "*Each of the boys **has** submitted his work.*"],
        ["Either... or / Neither... nor", "verb agrees with the NEARER subject", "*Neither the manager nor the employees **were** present.*"],
        ["as well as / along with / together with / in addition to", "verb follows the FIRST subject", "*The captain, as well as the players, **was** fined.*"],
        ["A number of + plural", "plural verb", "*A number of students **were** absent.*"],
        ["The number of + plural", "singular verb", "*The number of students **is** small.*"],
        ["One of the + plural noun + who/that", "plural verb (relative refers to the plural noun)", "*He is one of those officers who **work** late.*"],
        ["One of the + plural noun (no relative)", "singular verb for the main clause", "*One of my friends **is** going to London.*"],
        ["Uncountables (news, physics, economics)", "singular", "*The news **is** good.*"],
        ["Plural-form pairs (scissors, trousers)", "plural; 'a pair of' → singular", "*These trousers **are** new; a pair **is** enough.*"],
        ["Collective nouns", "unit → singular; members in disagreement → plural", "*The committee **has** decided; the jury **were** divided.*"],
        ["Amounts / distances / periods", "single quantity → singular", "*Ten kilometres **is** a long walk.*"],
        ["Titles of books / country names", "singular even if plural-looking", "*'Gulliver's Travels' **is** a satire.*"],
    ],
)

tense_table = md_table(
    ["Signal", "Required tense", "Trap"],
    [
        ["yesterday, last year, in 1998, ago", "simple past", "mixing with present perfect"],
        ["already, just, yet, ever, since, for, so far", "perfect (present, unless earlier past is meant)", "*when I reached, the train **had** already left*"],
        ["since + point of time / for + period", "perfect or perfect continuous", "*for ten years*, never *since ten years*"],
        ["when-clause / if-clause / as soon as (future meaning)", "simple present — no *will*", "*I will call you when the meeting **ends**.*"],
        ["earlier of two past actions", "past perfect; later action → simple past", "*The patient **had died** before the doctor came.*"],
        ["since + past clause", "present perfect in main clause", "*It **has been** raining since he left.*"],
        ["used to / would", "past habit", "not *use to*"],
    ],
)

prep_table = md_table(
    ["Governor", "Partner", "Governor", "Partner"],
    [
        ["insist", "on", "arrive", "at (a point) / in (a city)"],
        ["depend", "on", "angry", "with (person) / at (thing)"],
        ["apologise", "to (person) for (act)", "good", "at (skill) / for (health)"],
        ["married", "to", "different", "from"],
        ["prefer", "to", "senior / junior / superior / inferior", "to (never than)"],
        ["afraid / fond / aware / proud", "of", "reason / cause", "for / of"],
        ["solution / answer / key", "to", "influence / effect / impact", "on"],
        ["consist", "of", "deal / cope", "with"],
        ["congratulate", "on", "suffer", "from"],
        ["compare", "to (liken) / with (contrast)", "comply", "with"],
    ],
)

corr_table = md_table(
    ["Pair", "Correct shape", "Trap"],
    [
        ["No sooner... than", "*No sooner did the bell **ring** than...*", "using *when*, or past tense after *did*"],
        ["Hardly / Scarcely... when", "*Hardly had he **sat** down when...*", "using *than*"],
        ["Not only... but also", "parallel structures after both halves", "joining noun with clause"],
        ["Either... or / Neither... nor", "verb agrees with nearer subject", "verb agreeing with first subject"],
        ["Both... and", "*Both Ram **and** his brother...*", "*both... as well as*"],
        ["Lest... should", "*Work hard lest you **should** fail.*", "*lest... will not*"],
        ["Such... as / such... that", "*Such books as... / such a noise that...*", "mixing the two"],
        ["Whether... or", "*I asked whether he **would** come or not.*", "*whether... nor*"],
    ],
)

confuse_table = md_table(
    ["Pair", "Distinction", "Example"],
    [
        ["few / a few", "*few* = almost none (negative); *a few* = some (positive)", "*Few men are wise; a few students stayed back.*"],
        ["little / a little", "*little* = hardly any; *a little* = some", "*There is a little water left.*"],
        ["much / many", "*much* + uncountable; *many* + countable", "*much help, many friends*"],
        ["fewer / less", "*fewer* + countable; *less* + uncountable", "*fewer books, less sugar*"],
        ["elder / older", "*elder* only for family, no *than*; *older* with *than*", "*my elder brother; older than I*"],
        ["farther / further", "*farther* = distance; *further* = additional", "*further details*"],
        ["lie / lay", "*lie* (recline) — lay, lain; *lay* (put) — laid", "*He lay down; he laid the pen down.*"],
        ["return back / repeat again / revert back", "redundant pairs — drop the second word", "*He returned at midnight.*"],
    ],
)

SUBTOPICS = [
    {
        "id": "es-checklist",
        "title": "The master checklist: SVA → tense → article → preposition",
        "concept": f"""An error-spotting item gives you four parts of one sentence and asks which part is faulty. Do not hunt vaguely — audit the sentence in a fixed order, because SSC errors follow the same priority ladder in almost every shift.

{check_table}

**Why an order matters:** about two-thirds of all errors live in checks 1–4. Sweeping in this order catches them before you waste time on stylistic doubts. Also, only ONE part is wrong — the moment one check convicts a part, stop and verify it once, then mark.

**How to verify before marking:** rewrite the sentence correctly in your head. The corrected version must sound like ordinary formal English. If your 'correction' needs restructuring two parts, you have probably misread the sentence; re-run the checklist.

**Where the error usually hides:** the verb part (finite verbs attract agreement and tense errors), the part containing a preposition or article, and the opening part (pronoun case, connectors). Descriptive tail phrases ('of the pending bill') are rarely the answer — they are usually innocent scenery.

**Timing:** 20–25 seconds per question. Read once at normal speed (your ear catches half the errors), then audit with the checklist for the rest.""",
        "formulas": [],
        "tricks": [
            {
                "title": "The 7-step sweep",
                "body": "Verb first: find the subject, check number. Then tense anchors. Then a/an/the by sound. Then preposition partners. Only then pronouns, pairs, and word choice.",
                "example": {
                    "q": "One of my friends / are going / to London / next week.",
                    "solution": "Check 1 (SVA): true subject = 'one' (singular) → 'is going'. Part 2 is the error. Later checks never run.",
                },
            },
            {
                "title": "Strip the middle",
                "body": "Delete phrases between subject and verb ('of my friends', 'of the mangoes', 'as well as the players') and read the bare skeleton — agreement errors become loud.",
            },
            {
                "title": "No-error discipline",
                "body": "When the paper offers 'No error', choose it only after the full sweep; do not pick it because the sentence 'sounds fine' at speed. Roughly one in five such items hides a sneaky SVA or preposition error.",
            },
        ],
        "mistakes": [
            "Agreeing the verb with the noun nearest to it instead of the true subject.",
            "Marking the part that merely sounds clumsy — awkward is not always wrong.",
            "Overlooking the error in the FIRST part because the eye starts hunting in the middle.",
            "Finding two 'errors' and freezing: re-check the second one; usually it is standard usage you misjudged.",
        ],
    },
    {
        "id": "es-sva",
        "title": "Subject–verb agreement errors",
        "concept": f"""Agreement errors are the single largest error family in SSC English. The trap is always the same: words are inserted between the true subject and the verb.

{sva_table}

**The strip method:** delete every prepositional phrase, 'as well as' cluster, and relative clause between subject and verb, then test number. *The quality of the mangoes **were** not up to the mark* → strip 'of the mangoes' → *the quality ... were* → wrong; *the quality ... was*.

**Relative-clause verbs:** the verb after *who/which/that* agrees with the noun the pronoun points back to. *He is one of those officers who **work** late* (officers work), but *He is the only officer who **works** late* (the only officer).

**Interrupting positives:** *along with, together with, as well as, in addition to, accompanied by, and not* — none of these creates a plural subject. The verb follows the original subject.

**Watch the passive voice too:** agreement errors also appear in passives — *The letters **was** delivered* → *were delivered*.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Subject hunt backwards",
                "body": "From the verb, walk backwards past 'of...' phrases until you hit a noun or pronoun without a preposition in front — that is the subject that decides the verb.",
            },
            {
                "title": "Proximity rule flash",
                "body": "See *neither/nor* or *either/or* with two subjects? The verb matches the second (nearer) subject. Check that, and the item usually collapses instantly.",
                "example": {
                    "q": "Neither the manager nor / the employees was / present at / the meeting.",
                    "solution": "Nearer subject 'employees' is plural → *were present*. Part 2 carries the error.",
                },
            },
            {
                "title": "Quantity is singular",
                "body": "Sums of money, distances, time spans and weights take a singular verb even in plural form: 'Ten kilometres **is** a long walk', 'Five hundred rupees **was** the fine'.",
            },
        ],
        "mistakes": [
            "Using a plural verb after 'each/every/either' joined to a noun ('Each of the boys have...').",
            "Taking 'a number of' and 'the number of' as the same (plural vs singular).",
            "Making 'news, mathematics, physics' plural because they end in -s.",
            "Agreeing with 'one of the + plural noun' and writing 'who works' — the relative refers to the plural noun.",
        ],
    },
    {
        "id": "es-tense",
        "title": "Tense and sequence-of-tenses errors",
        "concept": f"""Tense errors come in four reliable shapes.

{tense_table}

**Anchor discipline:** every sentence carries its time information in anchor words. Locate the anchor first; the verb must obey it. *Since ten years* is a double failure — *since* demands a point of time (*since 2015*) and a ten-year span needs *for*.

**Two past events:** the earlier one takes past perfect, the later simple past. But do not demand perfect forms where plain sequence is meant — after *before/after* the perfect is optional if the order is already clear.

**Future-in-clauses:** after *when, before, after, until, as soon as, if* referring to the future, English uses present tense — *I will call you when the meeting **ends*** — never *will end*.

**Reported-speech spillover:** in error-spotting, a reporting verb in the past (*asked, said*) forces backshift in the reported clause: *He asked why he **had** failed*, not *why did he fail* (word order also reverts to statement order).

**Perfect-continuous partners:** *has/have been + -ing* pairs with *since/for*: *She has been working here **for** ten years*.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Underline every anchor",
                "body": "Circle yesterday/ago/since/for/by the time/when/next week before judging any verb. Most tense questions answer themselves once the anchors are visible.",
                "example": {
                    "q": "When I reached / the station, the train / already left / without a whistle.",
                    "solution": "Two past events: reaching came after the train's leaving → earlier event needs past perfect: *had already left*. Part 3.",
                },
            },
            {
                "title": "Will-check",
                "body": "Scan for *will* inside a *when/if/until* clause with future meaning — SSC plants this trap repeatedly.",
            },
            {
                "title": "Since/for sorting",
                "body": "*Since* + starting point (since Monday, since 2019, since childhood); *for* + duration (for ten years, for a week). Wrong partner = wrong part.",
            },
        ],
        "mistakes": [
            "Using present perfect with a finished-time anchor ('I have met him yesterday').",
            "Backshifting only half a sentence: 'He said he **will** come' → 'would come'.",
            "Choosing past perfect wherever two past verbs appear, even in simple chronological narration.",
            "Writing 'since + duration' because it sounds formal.",
        ],
    },
    {
        "id": "es-article-preposition",
        "title": "Article and preposition errors",
        "concept": f"""**Articles.** Three decisions cover everything:
- *a/an* — chosen by the FIRST SOUND of the next word, not its letter: *a university, a European, a one-rupee coin* (yu/w sounds); *an hour, an honest man, an MLA, an x-ray* (vowel sounds, silent h).
- *the* — for a specific/known noun, a unique thing (*the sun*), a superlative (*the best*), an ordinal (*the first*), and a noun restricted by the phrase after it (*the girl in blue*).
- zero article — before most proper nouns, meals, languages, abstract nouns in general use, and school/college/hospital in their purpose sense (*go to school*).

**Prepositions.** SSC tests fixed partners, not spatial logic. When you see a preposition, find its governor (the verb, adjective or noun it hangs on) and recall the pair.

{prep_table}

**Common placements:** *arrive AT a station, IN a city*; *consists OF*; *die OF a disease, FROM a wound*; *deprived OF*; *capable OF*; *different FROM*; *prefer X TO Y*; *abide BY*; *accordING TO* (never *according with*).

**Double-check the whole part:** prepositions often sit quietly at the end of a long part ('...in a garden near an university') — read prepositions individually instead of skimming the part as a whole.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Say it aloud",
                "body": "Articles are sound decisions. Pronounce the phrase — 'an university' fails the ear immediately ('yu' sound), 'a honest man' likewise.",
                "example": {
                    "q": "The children / were playing / in a garden / near an university.",
                    "solution": "'University' begins with the *yu* consonant sound → *a university*. Part 4.",
                },
            },
            {
                "title": "Governor chant",
                "body": "Underline the word the preposition depends on and recite its partner: insist—on, angry—with (person), prefer—to, married—to. Wrong partner = the answer.",
            },
            {
                "title": "The-with-superlative scan",
                "body": "Superlative adjectives and ordinals demand *the*: 'the most intelligent girl', 'the first attempt'. A bare superlative is a hidden article error.",
            },
        ],
        "mistakes": [
            "Choosing *an* before words starting with a vowel LETTER that sounds like a consonant (university, union, one).",
            "Using *than* after senior/junior/superior/inferior/prefer instead of *to*.",
            "Saying 'angry on him' or 'consists in students' from literal translation.",
            "Inserting *the* before 'school/hospital/home' in the purpose sense ('go to the school' when meaning 'attend').",
        ],
    },
    {
        "id": "es-pronoun-conjunction",
        "title": "Pronoun and correlative-conjunction errors",
        "concept": f"""**Pronoun case.** Subject forms (I, he, she, we, they, who) do the action; object forms (me, him, her, us, them, whom) receive it or follow a preposition:
- after prepositions: *between you and **me***, *for him and **me***;
- after *let*: *Let him and me try*;
- comparing with a hidden verb: *She is taller than **I** (am)*.

**Pronoun–antecedent agreement:** *each, everyone, somebody, nobody, either* take singular pronouns (*Each of the boys... his assignment*). Collective nouns take *it* (as units) or *they* (as members).

**Unnecessary pronouns:** *My friend he came... / The book, it is...* — a pronoun duplicating the subject is an error.

**Correlative pairs.** The classic SSC items:

{corr_table}

**Parallelism under pairs:** whatever follows *not only* must match in form what follows *but also* (noun with noun, clause with clause). *She not only sings but also dances* — parallel verbs. Mixing forms is itself the planted error.

**No sooner forms:** with *did* → base verb (*No sooner did the bell **ring** than...*); with *had* → past participle (*No sooner had the bell **rung** than...*). Both shapes are standard; mixing shapes is not.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Preposition + I? Kill it",
                "body": "Any 'between you and I', 'for he and I' construction is wrong in standard English — object form after a preposition, every time.",
                "example": {
                    "q": "Between you and I, / the new manager / has no / practical experience.",
                    "solution": "Preposition takes object form → *between you and me*. Part 1.",
                },
            },
            {
                "title": "Did + base form",
                "body": "After *did/does/do*, the verb loses its tense: *No sooner did the bell ring*. A past form after *did* is a guaranteed error.",
            },
            {
                "title": "Partner visibility test",
                "body": "Cover the sentence except the pair words. If one half of a correlative appears without its partner, or with the wrong partner (*hardly... than*), that part is the error.",
            },
        ],
        "mistakes": [
            "Using *whom* as a subject or *who* after a preposition ('to who').",
            "Writing 'one of my friend' (plural noun needed) or 'between him and she'.",
            "Pairing *hardly/scarcely* with *than* and *no sooner* with *when* — the two pairs are swapped.",
            "Making 'everyone... their' the error without noticing the paper accepts singular *their* in informal use — SSC's answer key follows *his/her*; mark accordingly when options force a choice.",
        ],
    },
    {
        "id": "es-comparison-wordchoice",
        "title": "Comparison, redundancy and confusable-word errors",
        "concept": f"""**Comparison rules.**
- Double comparative/superlative is always wrong: *more bigger, most fastest*.
- Compare like with like: *The climate of Shimla is better than **that of** Delhi* (climate vs climate, not climate vs city).
- *than any other + singular* when the subject belongs to the group: *Mumbai is bigger than **any other** city in India* — without *other*, Mumbai is compared with itself.
- Latin comparatives take *to*, never *than*: *senior, junior, superior, inferior, prior, prefer* → *to*.
- *elder* takes no *than* and applies within families; *older than* everywhere else.

**Redundancy.** English rejects pairs that repeat one idea: *return back, repeat again, revert back, final conclusion, close proximity, sufficient enough, cooperate together, mutual friendship between the two*. Strike the second word.

**Confusables:**

{confuse_table}

**Word-order errors** also land here: in embedded questions the statement order returns — *He asked why he **had failed***, not *why did he fail*. And adverbs of frequency precede the main verb but follow *be*: *He always is* → *He is always*.""",
        "formulas": [],
        "tricks": [
            {
                "title": "-er/-more clash scan",
                "body": "Look for *more* glued to a comparative (*more bigger*) or *most* glued to a superlative — instant error, no further thought needed.",
                "example": {
                    "q": "Delhi is / more bigger / than Agra / in area.",
                    "solution": "*bigger* is already comparative; *more* doubles it → Part 2. Correct: *Delhi is bigger than Agra*.",
                },
            },
            {
                "title": "Back-and-forth redundancy hunt",
                "body": "Two-word pairs where the second word repeats the first are planted answers: return BACK, repeat AGAIN, revert BACK. Train the eye to flinch at them.",
            },
            {
                "title": "that-of insertion test",
                "body": "In comparisons of two nouns' qualities, the second noun needs *that of/those of*: 'The roads of Delhi are wider than **those of** Patna'. Missing *those of* = comparison error.",
            },
        ],
        "mistakes": [
            "Writing 'Mumbai is bigger than any city in India' and missing the missing *other*.",
            "Using *than* after prefer/senior/junior because 'than' compares — these five take *to* only.",
            "Treating 'a little/a few' as errors — they are positive forms; *little/few* alone are the negative ones.",
            "Flagging standard phrases as redundant because they are long ('in spite of the fact that' is wordy but not the marked error in SSC items).",
        ],
    },
]

# ---------------------------------------------------------------- patterns
PATTERNS = [
    {
        "pattern": "Subject–verb agreement error",
        "frequency": "very common",
        "howToSpot": "A verb separated from its subject by 'of...', 'as well as...', or a relative clause; each/either/neither constructions; a number of vs the number of.",
        "approach": "Strip the interrupting phrases, find the true subject, apply number — proximity rule for or/nor pairs.",
    },
    {
        "pattern": "Tense / sequence error",
        "frequency": "very common",
        "howToSpot": "Anchors like yesterday, since, for + period, already, when-clause with future meaning, or two past events in one sentence.",
        "approach": "Underline anchors, then fit each verb to its anchor; earlier-of-two past events takes past perfect; no 'will' in time clauses.",
    },
    {
        "pattern": "Article error",
        "frequency": "common",
        "howToSpot": "a/an before vowel-letter-but-consonant-sound words (university, one, European) or the reverse (hour, honest, MBA); missing 'the' before superlatives/unique nouns.",
        "approach": "Pronounce the phrase; apply the sound rule, then check specificity for 'the'.",
    },
    {
        "pattern": "Preposition error",
        "frequency": "common",
        "howToSpot": "A fixed-partner verb/adjective/noun followed by a preposition that feels off: insisted for, angry on, good in (skill), consists from.",
        "approach": "Find the governor, recall the standard pair, and compare letter by letter.",
    },
    {
        "pattern": "Pronoun / correlative-pair error",
        "frequency": "common",
        "howToSpot": "Pronoun after a preposition in subject form; duplicated subject pronoun; one half of no sooner/hardly/not only with a wrong or absent partner.",
        "approach": "Apply case rules for pronouns; verify both halves of any correlative and the verb form after did/had.",
    },
    {
        "pattern": "Comparison / redundancy error",
        "frequency": "occasional",
        "howToSpot": "more + -er, most + -est, missing other in any-other comparisons, than after Latin comparatives, pairs like return back.",
        "approach": "Scan for doubled comparison markers, then check that both sides of the comparison are the same kind of thing.",
    },
]

# ---------------------------------------------------------------- solved examples
SE = [
    q("eng-es-s01", ES + "The quality of the mangoes / imported from Maharashtra / were not / up to the mark.",
      ["The quality of the mangoes", "imported from Maharashtra", "were not", "up to the mark."],
      2,
      "The true subject is *quality* (singular); 'of the mangoes' is an interrupting phrase and 'imported from Maharashtra' a reduced relative clause — neither changes the number. Singular subject → *was not up to the mark*. Checklist position: check 1 (SVA) convicts part 3 before any later check runs.",
      "Strip the middle: 'the quality ___' → was. Agreement first, always.",
      "easy", "es-sva", "SVA with intervening phrase", 30),
    q("eng-es-s02", ES + "I will call you / when the meeting / will end / this evening.",
      ["I will call you", "when the meeting", "will end", "this evening."],
      2,
      "In a time clause (*when, before, until, as soon as, if*) pointing to the future, English uses the simple present: *when the meeting **ends***. The *will* belongs only in the main clause ('I will call you'). Checklist position: check 2 (tense anchors) — the anchor is the future main clause.",
      "No *will* after when/if/until. Present tense carries the future meaning in the clause.",
      "easy", "es-tense", "tense in time clause", 30),
    q("eng-es-s03", ES + "No sooner did / the bell rang / than the students / rushed out of the class.",
      ["No sooner did", "the bell rang", "than the students", "rushed out of the class."],
      1,
      "*No sooner* pairs with *than* (part 3 is correct), and after auxiliary *did* the main verb must be the base form: *No sooner did the bell **ring***. Part 2's past form *rang* duplicates the tense that *did* already supplies. Checklist position: check 6 (correlative pairs and verb shape).",
      "See 'did' → expect the base verb. 'No sooner... rang' is a planted duplicate-tense error.",
      "medium", "es-pronoun-conjunction", "correlative + verb form", 35),
]

# ---------------------------------------------------------------- practice
PRACTICE = [
    q("eng-es-p01", ES + "One of my friends / are going / to London / next week.",
      ["One of my friends", "are going", "to London", "next week."], 1,
      "The subject is *one*, not *friends*: 'one of my friends **is** going'. The phrase 'of my friends' merely modifies *one*.",
      "Strip 'of my friends': 'one ___' → is.",
      "easy", "es-sva", "one of + plural noun", 30),
    q("eng-es-p02", ES + "Neither the manager nor / the employees was / present at / the monthly meeting.",
      ["Neither the manager nor", "the employees was", "present at", "the monthly meeting."], 1,
      "With *neither... nor*, the verb agrees with the nearer subject — *employees* (plural) → **were** present. *Was* wrongly agrees with the distant singular subject.",
      "Or/nor pair → match the second subject.",
      "easy", "es-sva", "proximity agreement", 30),
    q("eng-es-p03", ES + "Each of the boys / have submitted / his assignment / well before the deadline.",
      ["Each of the boys", "have submitted", "his assignment", "well before the deadline."], 1,
      "*Each* is invariably singular: 'Each of the boys **has** submitted'. Note that part 3 (*his*) is correct — a singular pronoun after *each* is exactly what standard grammar wants.",
      "'Each of ___' → singular verb, even though the nearest noun is plural.",
      "easy", "es-sva", "each + singular verb", 30),
    q("eng-es-p04", ES + "The captain, as well as / the players, were / congratulated by / the cricket board.",
      ["The captain, as well as", "the players, were", "congratulated by", "the cricket board."], 1,
      "*As well as* does not build a plural subject; the verb follows the first subject, *the captain* → **was** congratulated. If the sentence meant both equally, it would use *and*.",
      "'As well as' is a intruder, not a conjunction of number — verb follows subject one.",
      "medium", "es-sva", "as well as agreement", 35),
    q("eng-es-p05", ES + "When I reached / the platform, the train / already left / under a thick cover of fog.",
      ["When I reached", "the platform, the train", "already left", "under a thick cover of fog."], 2,
      "Two past events in sequence: the train's leaving happened before the reaching → earlier event takes past perfect: *the train **had already left***. Signal words: *when I reached* + *already*.",
      "'Already' + earlier past action → had + participle.",
      "easy", "es-tense", "past perfect sequence", 30),
    q("eng-es-p06", ES + "She has been / working in this college / since ten years / and enjoys every day of it.",
      ["She has been", "working in this college", "since ten years", "and enjoys every day of it."], 2,
      "*Since* takes a point of time (*since 2015*); a duration takes **for**: *for ten years*. The perfect continuous 'has been working' is itself correct with either partner — the partner is what failed.",
      "Since = starting point, for = length. 'Since ten years' breaks the pair.",
      "easy", "es-tense", "since vs for", 30),
    q("eng-es-p07", ES + "The children / were playing / in a garden / near an university.",
      ["The children", "were playing", "in a garden", "near an university."], 3,
      "*University* begins with the consonant sound *yu*, so it takes **a**: 'near a university'. The article follows sound, not spelling.",
      "Sound, not letter: yu-words take 'a'.",
      "easy", "es-article-preposition", "a/an by sound", 25),
    q("eng-es-p08", ES + "Sita is / the most intelligent / girl in / a class.",
      ["Sita is", "the most intelligent", "girl in", "a class."], 3,
      "A noun made specific by the superlative phrase and the limiting phrase 'in...' takes **the**: *the most intelligent girl in the class*. 'A class' leaves the noun unidentified and unidiomatic.",
      "Superlative + limiting phrase → the.",
      "easy", "es-article-preposition", "the with superlative", 25),
    q("eng-es-p09", ES + "The professor / was visibly angry / on the students / for their repeated excuses.",
      ["The professor", "was visibly angry", "on the students", "for their repeated excuses."], 2,
      "*Angry* takes **with** a person and **at** a thing: 'angry with the students'. *On* is not a partner of *angry* in standard usage.",
      "Governor chant: angry—with (person), at (thing).",
      "easy", "es-article-preposition", "adjective + preposition", 25),
    q("eng-es-p10", ES + "He insisted / for immediate payment / of the two months' / pending electricity bill.",
      ["He insisted", "for immediate payment", "of the two months'", "pending electricity bill."], 1,
      "*Insist* pairs with **on**: 'insisted on immediate payment'. Part 3's possessive (*two months'*) is correct as a time-denoting possessive.",
      "Insist—on. Recall the pair, not the meaning.",
      "easy", "es-article-preposition", "verb + preposition", 25),
    q("eng-es-p11", ES + "Between you and I, / the newly appointed / manager has no / practical field experience.",
      ["Between you and I,", "the newly appointed", "manager has no", "practical field experience."], 0,
      "A preposition takes object forms: *between you and **me***. *I* is a subject form and cannot follow *between*.",
      "Preposition + I is always the error; flip it mentally: 'between me'.",
      "easy", "es-pronoun-conjunction", "pronoun case", 25),
    q("eng-es-p12", ES + "Hardly had / the chief guest arrived / than the power / went off.",
      ["Hardly had", "the chief guest arrived", "than the power", "went off."], 2,
      "*Hardly/Scarcely* pair with **when**; *no sooner* pairs with *than*. The sentence mixes the two pairs: 'Hardly had... **when** the power went off'.",
      "Two fixed pairs: hardly...when, no sooner...than. Swapped partners = the answer.",
      "medium", "es-pronoun-conjunction", "correlative pair", 35),
    q("eng-es-p13", ES + "Mumbai is / more bigger / than any other city / in the state.",
      ["Mumbai is", "more bigger", "than any other city", "in the state."], 1,
      "*Bigger* is already comparative; adding *more* creates a double comparative: *Mumbai is bigger than any other city in the state*. Part 3 is correct — *any other* is exactly what the comparison needs, since Mumbai itself belongs to the group of cities.",
      "Double comparative = instant conviction: -er and 'more' cannot coexist.",
      "easy", "es-comparison-wordchoice", "double comparative", 25),
    q("eng-es-p14", ES + "The exhausted traveller / returned back / to the hotel / a little after midnight.",
      ["The exhausted traveller", "returned back", "to the hotel", "a little after midnight."], 1,
      "*Return* already contains the idea of coming back; *back* is redundant: *returned to the hotel*. Redundant pairs are planted answers — return back, repeat again, revert back.",
      "Hear the pair: return + back repeats one idea. Strike the second word.",
      "easy", "es-comparison-wordchoice", "redundancy", 25),
    q("eng-es-p15", ES + "The interviewer asked / my friend that why / he had left / his previous job.",
      ["The interviewer asked", "my friend that why", "he had left", "his previous job."], 1,
      "After *asked*, the reported clause drops **that** when the question word *why* introduces it: 'asked my friend why he had left'. *That* and *why* cannot introduce the same clause. (The backshift to *had left* in part 3 is correct.)",
      "In indirect questions, the wh-word alone introduces the clause — 'asked that why' doubles the introducer.",
      "medium", "es-comparison-wordchoice", "connective in reported question", 35),
]

topic = {
    "id": "error-spotting",
    "sectionId": "english",
    "title": "Error Spotting",
    "order": 3,
    "importance": "high",
    "avgQuestions": {"tier1": 2, "tier2": 4},
    "summary": "A sentence is split into parts and one part carries a grammatical fault. Errors cluster in a short list — agreement, tense, articles, prepositions, pronouns, correlative pairs and comparison — so a fixed audit order (SVA → tense → article → preposition → pronoun → pairs → word choice) converts this into the most mechanical scoring topic in the section.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
