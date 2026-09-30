from _ge_common import SUBS, pat, mis, trick

# =====================================================================
# 3. Subject-verb agreement
# =====================================================================
SUBS["ge-subject-verb-agreement"] = dict(
    concept=(
        "A singular subject takes a singular verb. A plural subject takes a plural verb. "
        "That rule is easy. The trap is finding the **real subject**. "
        "Extra phrases often stand between the subject and its verb. Strike them out first."
    ),
    notes=r"""### Find the real subject
Cover every phrase that starts with *of, in, with* and similar words. What is left is the subject.

> **Example:** *The quality **of the apples** **is** poor.* The subject is *quality*, so the verb is singular.

These add-on words never change the subject's number: **as well as, along with, together with, with, besides, in addition to, rather than, accompanied by, including, like, no less than**. The verb agrees with the first subject.

*The minister, along with his aides, **was** present.*

### Joined subjects
| Joined by | Verb agrees with | Example |
|---|---|---|
| A **and** B | plural | Ravi and his sister **are** here. |
| A and B as one person or idea (one article) | singular | The secretary and treasurer **has** resigned. Bread and butter **is** my breakfast. |
| **each / every** before A and B | singular | Every boy and every girl **was** given a prize. |
| either ... or, neither ... nor, not only ... but also, or, nor | the **nearer** subject | Neither the teacher nor the students **were** late. |

### Always singular
- *Each, every, either, neither, everyone, someone, anyone, no one, nobody, everything* take a singular verb: *Each of the players **has** a kit.*
- *One of* + plural noun: singular. *One of my friends **is** a pilot.*
- *One of those* + plural noun + who: plural. *He is one of those people who **never give** up.*
- *The only one of ... who*: singular. *She is the only one of the girls who **has** passed.*
- *Many a* + singular noun: singular. *Many a man **has** tried.*
- *More than one* + singular noun: singular. *More than one student **was** absent.*
- An amount as one unit: singular. *Fifty rupees **is** too much. Ten km **is** a long way.*
- A gerund, an infinitive or a noun clause as subject: singular. *Walking **is** good exercise. What he said **was** false.*
- Titles and names, even with a plural form: *The United Nations **is** based in New York.*
- *A pair of, a series of, a set of* + plural noun: singular. *A pair of shoes **was** stolen.*

### Quantity words
- **A number of** = many, so plural. **The number of** = one figure, so singular. *A number of cars **were** towed. The number of cars **is** rising.*
- *Half, part, some, all, most, plenty, a lot, the rest, per cent, fractions* + **of X**: the verb agrees with X. *Half of the cake **is** eaten. Half of the guests **are** here.*
- *The* + adjective (a class of people): plural. *The rich **are** not always happy.*
- *There* or *here* + verb: the verb agrees with the noun that follows. *There **are** many reasons.*
- A relative pronoun takes the number of its owner word: *I, who **am** your friend, will help.*

### Collective nouns
Team, committee, jury, family, staff, audience, crowd, board and government are collective nouns.
- One body acting together: singular verb. *The team **is** strong.*
- Members acting separately: plural verb. *The team **are** arguing among themselves.*
- The matching pronoun follows the same choice (*its* or *their*).

### Quick lists
- **Singular:** news, mathematics, economics, measles, furniture, information, luggage, scenery.
- **Plural:** cattle, police, people, poultry, clergy, scissors, trousers, spectacles.
- **Depends on the noun after of:** all, some, most, half, a lot, plenty, the rest, two-thirds.

> **Tip:** In a divided-part item, the error is nearly always in the verb part. Strike the *of* or *as well as* phrase, then test the verb.
""",
    tricks=[
        trick("Strike-through method",
              "Draw a line through every phrase that starts with a preposition (of the boys, in the box, with his friends). Also strike every add-on phrase (as well as, along with, together with). What stays before the verb is the true subject.",
              "The captain, together with his players, ___ felicitated. (was / were)",
              ["Strike 'together with his players'.", "Now read: 'The captain ___ felicitated'.", "One captain, so singular: 'was'."],
              "was"),
        trick("Nearest subject for or / nor pairs",
              "For either ... or, neither ... nor, not only ... but also, or and nor, look only at the subject next to the verb. Put the plural subject second so the plural verb sounds natural.",
              "Either the players or the coach ___ responsible. (is / are)",
              ["Find the subject nearer the verb: 'the coach'.", "It is singular.", "Use 'is'."],
              "is"),
        trick("The number and a number",
              "*The number* is one figure, so it is singular. *A number* means many, so it is plural. Memory hook: A = Abundant."),
    ],
    mistakes=[
        mis("Matching the verb with the noun just before it: The list of items are ready.", "Match the head noun: The list of items is ready."),
        mis("Treating as well as or along with like and, and using a plural verb.", "The verb agrees with the first subject: The principal, as well as the teachers, was present."),
        mis("Using a plural verb after each, every, either or neither.", "Use a singular verb: Each of the girls was given a prize."),
        mis("Using a singular verb after one of those who.", "The who-clause describes the whole group: one of those people who never give up."),
        mis("Treating people, police and cattle as singular.", "They take a plural verb: The police are here."),
        mis("Using a plural verb for a sum of money or a distance treated as one amount.", "Use a singular verb: Fifty rupees is too much."),
    ],
    revision=[
        "Strike the of, with or as well as phrase; the head noun decides the verb.",
        "each, every, everyone, either, neither: singular verb.",
        "neither ... nor, either ... or: the verb follows the nearer subject.",
        "A number of: plural. The number of: singular.",
        "more than one, many a, amounts, mathematics, news, titles: singular.",
        "half, some, all, most + of X: the verb agrees with X.",
        "The error in a divided-part item usually sits in the verb part.",
    ],
    patterns=[
        pat("sva-p1", "Head noun before an 'of' phrase", "very common",
            "A phrase like the quality of, the list of, the bouquet of, or one of the sits before the verb.",
            ["Find the head noun: quality, list, bouquet, one.", "Ignore the phrase that starts with of.",
             "Match the verb to the head noun."],
            "The word 'of' begins a description, not a second subject.",
            "The bouquet of roses ___ on the table. (is / are / were / have)",
            ["The head noun is 'bouquet'.", "It is singular.", "Choose 'is'."],
            "is"),
        pat("sva-p2", "Each, every, one of: fixed singular", "very common",
            "The subject begins with each, every, everyone, everybody, either, neither or 'one of the ...'.",
            ["Check that the subject word is on the singular list.", "Choose the singular verb even if a plural noun follows 'of'.",
             "Reject the plural option that only sounds natural."],
            "These words point to members one at a time, so the verb stays singular.",
            "Each of the girls ___ given a certificate. (was / were / are / have)",
            ["The subject word is 'each'.", "'Each' is singular."],
            "was"),
        pat("sva-p3", "Nearer subject for neither ... nor", "common",
            "Two subjects are joined by neither ... nor, either ... or or not only ... but also, and they differ in number.",
            ["Find the subject nearer the verb.", "Match the verb to that subject alone.", "Ignore the farther subject."],
            "The nearer subject decides the verb, whatever the other subject is.",
            "Neither the manager nor the workers ___ present. (were / was / is / has)",
            ["The nearer subject is 'the workers'.", "It is plural.", "Choose 'were'."],
            "were"),
        pat("sva-p4", "Collective nouns and special singular subjects", "common",
            "The subject is a collective noun (committee, team), an -ics subject, 'more than one ...' or an amount (ten kilometres).",
            ["Check the special singular list.", "A group acting as one unit takes a singular verb.",
             "Ignore the plural look of the nearest noun."],
            "These subjects name one unit or one idea, whatever their shape.",
            "More than one student ___ selected. (was / were / have / are)",
            ["'More than one' is followed by a singular noun.", "The verb is singular."],
            "was"),
        pat("sva-p5", "A number of and the number of", "common",
            "The subject starts with 'a number of' or 'the number of' followed by a plural noun.",
            ["Read the first word: a or the.", "A number of means many, so use a plural verb.",
             "The number of means one figure, so use a singular verb."],
            "The word before 'number' shows whether you count many things or one figure.",
            "The number of cars on the road ___ rising every year. (is / are)",
            ["The phrase is 'the number of'.", "It stands for one figure.", "Use the singular 'is'."],
            "is"),
        pat("sva-p6", "Half, some, all + of X", "common",
            "The subject is half, some, all, most, a lot or a fraction followed by 'of' and a noun.",
            ["Find the noun after 'of'.", "Singular or uncountable noun: singular verb.", "Plural noun: plural verb."],
            "These words are only quantities; the noun after 'of' shows the number.",
            "Half of the guests ___ already here. (is / are)",
            ["The noun after 'of' is 'guests'.", "It is plural.", "Use 'are'."],
            "are"),
        pat("sva-p7", "The rich, and one of those who", "occasional",
            "The subject is 'the + adjective' (the rich, the poor) or the phrase 'one of those ... who'.",
            ["'The + adjective' names a class of people: plural verb.", "In 'one of those + plural noun + who', the who-clause is about the group.",
             "So use a plural verb after 'who'."],
            "The verb agrees with the group, not with the word 'one'.",
            "He is one of those students who ___ hard every day. (work / works)",
            ["'Who' stands for 'those students'.", "That group is plural.", "Use 'work'."],
            "work"),
    ],
)

# =====================================================================
# 4. Articles and determiners
# =====================================================================
SUBS["ge-articles-determiners"] = dict(
    concept=(
        "Articles are the small words a, an and the. "
        "Choose **a or an by the first sound** of the next word, not by its spelling. "
        "Use **the** for a particular or unique thing. Some nouns take no article at all. "
        "Small words like few, little, each and every are determiners and also decide marks."
    ),
    notes=r"""### A or an: go by the first sound
| Use **an** (vowel sound) | Use **a** (consonant sound) |
|---|---|
| an hour, an honest man, an heir, an honour | a university, a unit, a European, a useful tip |
| an MLA, an MBA, an SP, an X-ray, an LLB | a one-day match, a one-way street, a ewe, a union |
| an FIR, an NGO, an 8-year-old | a U-turn, a uniform, a hotel (the h is sounded) |

Letters whose names start with a vowel sound: A, E, F, H, I, L, M, N, O, R, S, X. So we say *an F-grade, an M.Sc., an S-bend*.

> **Tip:** Say the next word aloud. *University* begins with the sound "yu", so use **a**. *Hour* begins with a vowel sound, so use **an**.

### When to use a or an
- First mention of one countable thing: *I saw **a** cat.*
- A job or class: *She is **a** doctor.*
- A rate: *60 km **an** hour, twice **a** week, Rs 50 **a** kilo.*
- Fixed phrases: *what **a** sight, such **a** fool, quite **a** crowd, half **an** hour, **a** few, **a** little, **a** lot of, in **a** hurry, as **a** rule, at **a** loss.*

### When to use the
| Use | Example |
|---|---|
| Already mentioned or specific | *I bought a pen. **The** pen leaks.* |
| Unique things | *the sun, the moon, the sky, the earth* |
| Superlatives and ordinals | *the best, the first, the last, the only, the same* |
| Rivers, seas, oceans, canals, gulfs | *the Ganga, the Arabian Sea, the Suez Canal* |
| Mountain ranges, island groups, deserts | *the Himalayas, the Andamans, the Thar* |
| Holy books, epics, newspapers, famous buildings | *the Gita, the Ramayana, the Hindu, the Taj Mahal* |
| Countries with plural names or Republic, Union, States | *the USA, the UK, the Netherlands, the Maldives* |
| Musical instruments | *She plays **the** sitar.* |
| Adjective for a whole class | *the rich, the poor, the blind* |
| A whole species | ***The** tiger is a national animal.* |
| Double comparative | ***The** more you read, **the** better you write.* |
| A proper noun used as a common noun | *Kalidas is **the** Shakespeare of India.* |
| Directions | *in **the** north* (but *go north*) |

### When to use no article
- Names of people, cities, most countries, single mountains and single lakes: *Mount Everest, Lake Chilika, India*.
- Languages and school subjects: *He speaks Hindi. Physics is hard.*
- Meals, games and most diseases: *have lunch, play cricket, suffer from malaria*. But: *a heavy lunch, the flu, a cold*.
- General abstract and material nouns: *Honesty is the best policy. Gold is costly.* But: *the gold of Kolar*.
- *Man* meaning mankind: *Man is mortal.*
- School, church, hospital, prison, bed, college used for their main purpose: *go to school*. But: *went to the school to meet the principal*.
- Fixed phrases: *by bus, by train, at night, next week, last year, by chance, in time*.

### Determiners
| Word | Goes with | Note |
|---|---|---|
| each | singular, a group of two or more | *each side of the road* |
| every | singular, three or more as a whole | *every student* |
| some / any | some: positive and offers; any: negative and questions | *Would you like some tea?* |
| much / little / less | uncountable | *much time, less water* |
| many / few / fewer | countable plural | *many books, fewer errors* |

*Few / a few* and *little / a little*: *few* and *little* mean hardly any. *A few* and *a little* mean some. *He is new here and has **few** friends.*
""",
    tricks=[
        trick("Say it aloud",
              "For a or an, whisper the next word. A vowel sound (on-est, em-el-ay, ex-ray) needs **an**. A y or w sound (you-niversity, won-day) needs **a**.",
              "He is ___ one-eyed man and ___ honest worker. (a / an)",
              ["'One' sounds like 'won', a consonant sound: a one-eyed man.", "'Honest' sounds like 'on-est': an honest worker."],
              "a, an"),
        trick("The geography rule of thumb",
              "Plural names, water and chains take **the**: the Alps, the Ganga, the Indian Ocean, the Andamans. A single peak, a single lake, a city or most countries take no article: Mount Abu, Lake Dal, Delhi, Nepal."),
    ],
    mistakes=[
        mis("Choosing a or an by spelling: an university, a hour, an European.", "Go by sound: a university, an hour, a European."),
        mis("Using the with meals, games and languages: play the cricket, the English is easy.", "Leave out the: play cricket, English is easy."),
        mis("Dropping the before superlatives or same and only.", "Use the: the best, the same, the only."),
        mis("Using the with a single mountain or lake: the Mount Everest.", "Use no article: Mount Everest."),
        mis("Leaving out a in rates and fixed phrases: twice week, in hurry.", "Write: twice a week, in a hurry."),
    ],
    revision=[
        "an hour, an MLA, an honest man; a university, a European, a one-rupee coin.",
        "the: second mention, unique things, superlatives, rivers, ranges, directions, the + adjective.",
        "no article: languages, meals, games, most diseases, man (mankind), general plurals.",
        "go to school, church, hospital, bed: no article when used for their purpose.",
        "few, little = hardly any; a few, a little = some.",
        "each: two or more; every: three or more as a whole.",
    ],
    patterns=[
        pat("art-p1", "A or an by first sound", "very common",
            "The blank sits before a word whose spelling and sound disagree: hour, honest, heir, university, European, one-, MLA, X-ray.",
            ["Say the next word aloud.", "Catch its first sound.", "Vowel sound: an. Consonant sound: a.",
             "Reject the option chosen by spelling."],
            "The rule is about sound, and the exam words are a small fixed set.",
            "She is ___ MLA from Bihar. (an / a / the / one)",
            ["'MLA' is said 'em-el-ay'.", "It starts with a vowel sound.", "Use 'an'."],
            "an"),
        pat("art-p2", "Compulsory the", "very common",
            "The blank comes before a unique thing, a superlative, a river or range, a direction or a second mention.",
            ["Check the triggers: unique, superlative, second mention, geographical name, direction, adjective for a class.",
             "If one fires, choose the.", "If none fires, think of a, an or no article."],
            "'The' marks one specific thing, and each trigger names such a thing.",
            "___ Ganga is a holy river. (The / A / An / No article)",
            ["'Ganga' is a river.", "River names take 'the'."],
            "The"),
        pat("art-p3", "Zero article traps", "common",
            "An article sits before a language, a meal, a purpose-building, or 'man' meaning mankind.",
            ["Ask: is the noun used for its purpose (go to school means to study)?", "Languages, meals and mankind take no article.",
             "In a divided sentence, the part with the wrong article is the error."],
            "Nouns used for their purpose behave like general ideas, not like particular places.",
            "The man is mortal. Improve the sentence.",
            ["'Man' here means the human race.", "The human race takes no article.", "Correct: 'Man is mortal'."],
            "Man is mortal"),
        pat("art-p4", "Few / a few, little / a little", "common",
            "The blank sits before a countable plural (friends, days) or an uncountable noun (time, hope), and the options are few, a few, little, a little.",
            ["Countable plural: few family. Uncountable: little family.", "Read the feeling: positive means some, so a few or a little.",
             "Negative means almost none, so few or little.", "Match the option."],
            "The small word 'a' turns 'hardly any' into 'some'.",
            "Give me ___ time to think; I am almost done. (a little / little / the little / a few)",
            ["'Time' is uncountable.", "'Almost done' is positive: you need some time.", "Use 'a little'."],
            "a little"),
        pat("art-p5", "Article before a rate or a fixed phrase", "common",
            "The sentence has a rate (per hour, per week) or a phrase like in a hurry, as a rule, what a sight.",
            ["Spot the rate or the fixed phrase.", "Rates and these phrases use a or an.", "Check the sound of the next word for a or an."],
            "These are fixed phrases with the article built in.",
            "The car travels at 60 km ___ hour. (a / an / the / no article)",
            ["A rate takes 'a' or 'an'.", "'Hour' starts with a vowel sound.", "Use 'an'."],
            "an"),
        pat("art-p6", "Geographical names", "common",
            "The blank comes before a river, sea, mountain range, island group, desert, lake, single peak or city.",
            ["Ask: is it plural, water or a chain?", "If yes, use the.", "If it is one peak, one lake, a city or most countries, use no article."],
            "English marks groups, chains and water bodies with 'the' and single places without it.",
            "We trekked in ___ Himalayas last summer. (the / a / no article)",
            ["The Himalayas are a mountain range.", "A range takes 'the'."],
            "the"),
        pat("art-p7", "Each, every, some, any", "occasional",
            "The blank comes before a noun and the options are each, every, some, any.",
            ["Each: one of two or more, seen one by one. Every: all of three or more.",
             "Some: positive sentences and offers. Any: negatives and questions.", "Match the option to the sentence type."],
            "Determiners also have fixed jobs by sentence type.",
            "Would you like ___ tea? (some / any)",
            ["This is an offer.", "Offers take 'some'."],
            "some"),
    ],
)

# =====================================================================
# 5. Prepositions and conjunctions
# =====================================================================
SUBS["ge-prepositions-conjunctions"] = dict(
    concept=(
        "A preposition links a noun to the rest of the sentence. A conjunction joins words or clauses. "
        "Most questions test fixed pairs, like *fond of* or *no sooner ... than*. "
        "You cannot work these out by logic. Learn them as pairs and match the partner."
    ),
    notes=r"""### Time and place
| Word | Time | Place |
|---|---|---|
| **at** | exact point: at 6 pm, at noon, at night | point or address: at the gate |
| **on** | days and dates: on Monday, on 15 August | surface or street: on the table |
| **in** | months, years, seasons, parts of day: in May, in 2025 | enclosed area, city, country: in Delhi |
| **by** | not later than: by 5 pm | beside or means: by the window, by train |
| **till / until** | up to a time: wait till 5 | |
| **since / for** | start point / length, with perfect tenses | |
| **between / among** | two / more than two | between the banks, among the villagers |
| **beside / besides** | next to / in addition to | sat beside me; besides English he knows Tamil |
| **into / in** | movement inside / position | jumped into the pool; swimming in the pool |

### Fixed prepositions
| Pair | Sense |
|---|---|
| abide by, comply with | follow a rule |
| accede to, insist on, depend on, rely on | agree; demand; trust |
| accuse of, guilty of, charge with | blame for a crime |
| afraid of, capable of, fond of, proud of, sure of, aware of | fear; able; like; pride; certain; knowing |
| angry with (person), angry at (thing) | anger |
| agree with (person), to (proposal), on (point) | agreement |
| apologise to (person) for (act) | say sorry |
| good at, weak in, succeed in, interested in | skill; achieve; keen |
| married to, similar to, indifferent to, addicted to, acquainted with | link |
| prevent, refrain, abstain from | stop |
| die of (disease), die from (cause) | death |
| differ from (thing), differ with (view) | disagree |
| divide into (parts), divide among (people) | share |
| senior, junior, superior, inferior, prior to; prefer X to Y | comparison |
| tired of (bored), tired from (exhausted) | fatigue |
| wait for (someone), wait on (serve) | waiting |
| deal in (goods), deal with (handle) | trade; handle |
| part with (thing), part from (person) | give up; leave |
| object to + V-ing, congratulate on, deprive of, eligible for | fixed |

**No preposition after these verbs:** discuss (the plan), describe, reach (the station), enter (the room), marry (someone), attack, resemble, request, order, answer (a question), comprise, emphasise, investigate.

> **Watch:** *Discuss about, reach at* and *comprises of* are wrong. Say *consists of* or *is composed of*.

### Joining pairs
| Pair | Example |
|---|---|
| either ... or / neither ... nor | *Neither he nor I knew.* |
| both ... and | *both Ravi **and** Sita* (not *as well as*) |
| not only ... but also | *She **not only** sings **but also** dances.* |
| whether ... or | *whether you like it **or** not* |
| no sooner ... than | *No sooner had he left **than** it rained.* |
| hardly / scarcely / barely ... when, before | *Hardly had I sat **when** the phone rang.* |
| though / although ... yet (or nothing) | *Though he is poor, he is honest.* Never *though ... but*. |
| so ... that / such ... that | *so tired **that** he slept* |
| such ... as / the same ... as | *such books **as** these* |
| lest ... should | *Walk carefully **lest** you **should** fall.* |
| rather ... than | *I would rather walk **than** wait.* |
| as ... as / not so ... as | *not so tall **as** his brother* |

### Errors to watch
- Two conjunctions for one job: *Although ... but, Because ... so, Since ... therefore* are wrong. Use one.
- *Unless, until, lest* and *till* already carry a negative: *Unless you do not work* is wrong.
- Say *The reason ... is that*, not *because*.
- Do not mix pairs: *Scarcely ... than* and *No sooner ... when* are wrong.
- Keep the joined parts alike: *He plays **not only** cricket **but also** football.* Not *He not only plays cricket but also football*.
""",
    tricks=[
        trick("Find the partner",
              "When you see hardly, scarcely, no sooner, not only, neither, either, both, whether, lest or though, look ahead for its fixed partner. A wrong or missing partner is very often the error.",
              "Scarcely had the match started than it began to rain heavily. Which word is wrong?",
              ["'Scarcely' pairs with 'when' or 'before'.", "'Than' belongs to 'no sooner'."],
              "than -> when"),
        trick("Group prepositions by meaning",
              "Stopping: prevent, refrain, abstain, desist **from**. Dependence: depend, rely, count **on**. Skill: good, expert, adept **at**; proficient **in**. Latin comparatives: senior, junior, superior, inferior, prior, prefer **to**. One group takes one preposition."),
    ],
    mistakes=[
        mis("Adding a preposition after discuss, reach, enter, resemble, request or comprise.", "Use no preposition: discuss the plan, reach the station."),
        mis("Using between for more than two people or things.", "Use among for more than two: among the villagers."),
        mis("Writing prefer X than Y.", "Write prefer X to Y."),
        mis("Using though ... but, because ... so or both ... as well as.", "Use one conjunction, or the true pair: both ... and."),
        mis("Adding not after unless, lest or until.", "These words already carry a negative: Unless you hurry, you will miss the bus."),
        mis("Using since with a length of time: since three days.", "Use for with a length: for three days."),
    ],
    revision=[
        "at 6, on Monday, in May; at the door, on the table, in Bengaluru.",
        "since + start point; for + length of time.",
        "fond of, good at, angry at a thing, angry with a person, senior to, prefer to.",
        "between = two, among = more than two.",
        "No sooner ... than; hardly / scarcely ... when; not only ... but also.",
        "No preposition after discuss, reach, enter, resemble, comprise.",
        "Unless, lest, until already carry a negative.",
    ],
    patterns=[
        pat("pre-p1", "at / on / in for time and place", "very common",
            "The blank comes before a clock time, a day, a month, a city or a surface.",
            ["Classify the word: exact point, day or date, month or large area, surface.", "at: point. on: day or surface. in: month or enclosed area.",
             "Choose the matching option."],
            "The three words split time and space by how exact they are.",
            "We reached the airport ___ 6 o'clock. (at / on / in / by)",
            ["'6 o'clock' is an exact time.", "An exact time takes 'at'."],
            "at"),
        pat("pre-p2", "Fixed preposition after a word", "very common",
            "An adjective, noun or verb (fond, good, angry, insist, married) is followed by the blank.",
            ["Find the governing word.", "Recall its fixed pair.", "Reject the prepositions that fit the meaning but not this word."],
            "These pairs are conventions, and the exam reuses the same ones.",
            "Ravi is very good ___ mathematics. (at / in / on / for)",
            ["'Good' is followed by 'at' when it means skill.", "Choose 'at'."],
            "at"),
        pat("pre-p3", "Between / among and since / for", "common",
            "Two or more parties share something, or a time span starts or lasts.",
            ["Count the sharers: two means between, more than two means among.", "A start point means since. A length means for.",
             "Choose the option that fits."],
            "Each pair splits one idea by number or by the shape of the span.",
            "The prize was divided ___ the two winners. (between / among / in / into)",
            ["There are two winners.", "Two parties take 'between'."],
            "between"),
        pat("pre-p4", "Joining pairs", "very common",
            "A sentence opens with no sooner, hardly, scarcely or not only, and the blank is the second half of the pair.",
            ["Recall the fixed partner: no sooner ... than; hardly, scarcely ... when; not only ... but also.",
             "Eliminate mixed partners.", "Choose the partner word."],
            "These pairs are welded together; the first half fixes the second.",
            "No sooner did the bell ring ___ the students rushed out. (than / when / then / that)",
            ["'No sooner' needs 'than'.", "Choose 'than'."],
            "than"),
        pat("pre-p5", "No preposition after the verb", "common",
            "The verb is discuss, reach, enter, resemble, describe, marry or comprise, and one option adds a preposition.",
            ["Spot the verb.", "Check the no-preposition list.", "Reject the option with 'about', 'at' or 'of'."],
            "These verbs already carry the meaning of the preposition.",
            "The committee will discuss ___ the new rules tomorrow. (about / on / no word)",
            ["'Discuss' takes its object directly.", "Add no word."],
            "no word"),
        pat("pre-p6", "Latin comparatives with to", "common",
            "The sentence compares two things with senior, junior, superior, inferior, prior or prefer, and one option uses than.",
            ["Spot the Latin comparative.", "It takes 'to', never 'than'.", "Choose the option with 'to'."],
            "Words like senior and prefer come from Latin comparatives that already contain the idea of 'than'.",
            "She is senior ___ me in the office. (than / to / from / over)",
            ["'Senior' is a Latin comparative.", "It takes 'to'."],
            "to"),
        pat("pre-p7", "Two conjunctions for one job", "occasional",
            "The sentence has although or because and a second linking word such as but or so.",
            ["Spot the first conjunction (although, because, since).", "Look for a second one in the other clause.",
             "Delete the second one."],
            "One link needs one conjunction.",
            "Although he was tired, but he finished the work. Which word is wrong?",
            ["'Although' already joins the two parts.", "'But' repeats the job."],
            "but"),
    ],
)
