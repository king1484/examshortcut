from _ge_common import SUBS, pat, mis, trick

# =====================================================================
# 1. Parts of speech
# =====================================================================
SUBS["ge-parts-of-speech"] = dict(
    concept=(
        "Every word in a sentence does one of eight jobs. "
        "An error in grammar usually means a word is doing the wrong job. "
        "For example, a noun may stand where an adverb is needed. "
        "First find the job the slot needs. Then pick the word that does that job."
    ),
    notes=r"""### The eight jobs of a word
| Part of speech | Job | Example |
|---|---|---|
| Noun | names a person, place, thing or idea | **Honesty** pays. |
| Pronoun | replaces a noun | **She** called **us**. |
| Adjective | describes a noun or pronoun | a **brave** soldier |
| Verb | shows an action or a state | He **writes**. She **is** tired. |
| Adverb | describes a verb, adjective or adverb | runs **fast**, **very** tall |
| Preposition | links a noun to the rest of the sentence | sat **on** the wall |
| Conjunction | joins words or clauses | tea **or** coffee |
| Interjection | shows sudden feeling | **Alas!** He is gone. |

> **Rule:** Ask what the slot needs: noun, adjective, adverb or verb. Then choose the word of that type.

### Nouns that break the usual rules
| Group | Words | What to do |
|---|---|---|
| No plural (uncountable) | information, advice, furniture, luggage, baggage, equipment, machinery, scenery, poetry, jewellery, evidence, knowledge, traffic, bread | singular verb; count with *a piece of*: *two pieces of advice* |
| Always plural | scissors, trousers, spectacles, tongs, pliers, thanks, alms, premises, riches, outskirts, surroundings, belongings, proceeds | plural verb; *a pair of scissors* takes a singular verb |
| Singular form, plural meaning | cattle, police, people, poultry, clergy, gentry, vermin, peasantry | plural verb: *The police **are** here.* |
| Plural form, singular meaning | news, mathematics, physics, economics, civics, measles, mumps, billiards | singular verb: *The news **is** good.* |
| Same in singular and plural | sheep, deer, swine, series, species, aircraft | the verb or *a / two* shows the number |

### Collective nouns and the possessive
A collective noun names a group: team, committee, jury, family, audience, crowd, army.
- Group acts as one unit: singular verb. *The committee **has** approved the plan.*
- Members act separately: plural verb. *The jury **were** divided.*

The possessive shows ownership.
- Living things take *'s*: *the minister's car*. Non-living things take *of*: *the leg of the table*.
- Exceptions: time, distance, weight and personified things: *a day's leave, a stone's throw, the nation's pride*.
- One shop owned by both: *Ram and Shyam's shop*. Two shops: *Ram's and Shyam's shops*.

### Pronouns
| Situation | Use | Example |
|---|---|---|
| After a preposition (between, for, with, like) | object form | *between you and **me*** |
| After *than / as* | the form the hidden verb needs | *taller than **I** (am)*; *likes you more than **him*** |
| After *let* | object form | *Let **him and me** try.* |
| Complement of *be* (formal) | subject form | *It is **I**.* |
| Subject *one* | one's, oneself | *One must keep **one's** word.* |
| Order of persons | normal: 2nd, 3rd, 1st; admitting a fault: 1st, 2nd, 3rd | *You, he and I* / *I, you and he* |

- Words like *avail, absent, pride* need a -self pronoun: *He **availed himself of** the offer.*
- A -self pronoun is never a subject: *My friend and myself went* is wrong. Say *My friend and **I** went*.
- *Who* = subject (people). *Whom* = object (people). *Whose* = owner. *Which* = things.
- Use **that** after superlatives and after *all, only, same, none, nothing, everything*.
- *Either / neither* speak of two. *Any / none* speak of more than two. Traditional rule: *each other* (two), *one another* (more than two).
- A pronoun needs one clear owner and agrees with it: *Each of the girls brought **her** bag.*

### Adjectives
| Pair | Rule | Example |
|---|---|---|
| few / a few / the few | hardly any / some / all of the small number | *The few books he had were old.* |
| little / a little / the little | same idea, uncountable | *There is **little** hope.* |
| many / much | countable / uncountable | *many chairs, much furniture* |
| fewer / less | countable / uncountable | ***fewer** people, **less** sugar* |
| elder / older | *elder* is for family, before a noun, never with *than* | *my **elder** sister*; *older than me* |
| latest / latter | time / order | *the **latest** news; the **latter** half* |
| farther / further | distance / extra | *two km **farther**; **further** details* |

### Adverbs and word forms
- **too** = more than needed: *too weak **to** walk*. **very** = a high degree. **enough** comes after the word: *old **enough***.
- *Hardly, scarcely, barely, seldom, rarely* are already negative: *I can **hardly** hear.*
- Look-alikes: *hard* (with effort) and *hardly* (almost not); *late* and *lately* (recently); *near* and *nearly* (almost); *high* and *highly* (very much).
Match the slot to the word type. A noun follows *the, his, of*. An adjective sits before a noun. An adverb follows an action verb.

After an action verb use an adverb: *She sings **beautifully**.* After a linking verb (be, seem, look, feel, smell, taste, sound, appear, become, grow) use an adjective: *The soup tastes **good**.*

> **Watch:** *Look* works both ways. *He looked **sad*** (seemed). *He looked **sadly** at the dog* (gazed).
""",
    tricks=[
        trick("Cover the other name",
              "When a pronoun sits next to a noun (*Ravi and I / Ravi and me*), cover the noun. Read the sentence with the pronoun alone. The form that sounds right is the answer.",
              "The award was shared by Meena and ___. (I / me)",
              ["Cover 'Meena and'.", "'Shared by ___' needs an object form after the preposition 'by'.", "Say it: 'shared by me'."],
              "me"),
        trick("Scan every noun",
              "In an error-spotting sentence, circle each noun. Ask two questions. Can I count it? Is it one of the special groups (no plural, always plural, cattle-type)? Words like informations, furnitures and advices are favourite errors.",
              "He gave me some useful advices before the interview.",
              ["'Advice' has no plural.", "Write 'some useful advice'.", "To count it, say 'two pieces of advice'."],
              "advice"),
        trick("Few or a few: empty or half full",
              "*Few* and *little* mean the glass is nearly empty (a negative feeling). *A few* and *a little* mean there is something (a positive feeling). Let the rest of the sentence show the feeling.",
              "He had ___ friends in the new city, so he felt lonely. (few / a few)",
              ["Feeling lonely is a negative result.", "A negative feeling needs 'few' (hardly any)."],
              "few"),
        trick("Adjective order and word families",
              "Adjectives follow the order OSASCOMP: Opinion, Size, Age, Shape, Colour, Origin, Material, Purpose. Example: a beautiful small old round brown Indian wooden table. Some adjectives have no degrees: unique, perfect, ideal, complete, entire, round, square, supreme, universal. So *more unique* is wrong. Learn word families: succeed, success, successful, successfully; courage, encourage, courageous; strength, strengthen, strong; beauty, beautify, beautiful; anger, angry, angrily."),
        trick("Numbers with nouns",
              "After a definite number, *dozen, hundred, thousand, million, score, lakh, crore* and *pair* take no -s: *three dozen eggs, five hundred rupees*. But *dozens of eggs* and *hundreds of people* keep the -s. A number + noun used as an adjective takes a hyphen and the noun stays singular: *a five-year plan, a ten-rupee note, a two-hour delay*."),
        trick("Where adverbs go",
              "Frequency words go before the main verb but after *be*: *He always comes late. He is always late.* Use *very* with the plain adjective and with -ing adjectives (very tall, very interesting). Use *much* with comparatives and many -ed words (much taller, much obliged)."),
    ],
    mistakes=[
        mis("Making a no-plural noun plural: furnitures, informations, luggages, sceneries.", "Keep it singular: furniture, information, luggage, scenery."),
        mis("Using myself as a subject: Ravi and myself will attend.", "Use I: Ravi and I will attend."),
        mis("Writing elder than.", "With than, say older than: she is older than me."),
        mis("Using less with countable nouns: less mistakes.", "Use fewer with countable nouns: fewer mistakes."),
        mis("Adding a second negative to hardly or scarcely: I could not hardly breathe.", "Hardly is already negative: I could hardly breathe."),
        mis("Adding -s to dozen, hundred or lakh after a number: five hundreds rupees.", "Keep it plain after a number: five hundred rupees."),
    ],
    revision=[
        "Slot decides the word: noun after the, his, of; adjective before a noun; adverb after an action verb.",
        "No plural: information, advice, furniture, luggage, news, machinery, scenery.",
        "much + uncountable; many + countable plural; less + uncountable; fewer + countable.",
        "Linking verbs (seem, look, feel, taste) take an adjective: tastes good.",
        "Between you and me. Its has no apostrophe; it's means it is.",
        "each other for two, one another for more than two (traditional exam rule).",
        "Living things take 's; non-living things take of (leg of the table).",
    ],
    patterns=[
        pat("pos-p1", "Uncountable noun trap", "very common",
            "A no-plural noun appears with -s (advices, furnitures, informations), or with many instead of much.",
            ["Ask: can I count this noun one by one?", "If not, drop the -s and use a singular verb.",
             "Use much, little or some with it, not many.", "Pick the option with the singular form."],
            "The exam reuses the same short list of no-plural nouns every year.",
            "She gave me many useful advices before the interview. Which part is wrong?",
            ["'Advice' cannot be counted.", "It has no plural form.", "Correct: 'some useful advice'."],
            "many useful advices -> some useful advice"),
        pat("pos-p2", "Word-form family choice", "very common",
            "A blank sits before a noun, after a preposition or after an action verb. The four options are forms of one word.",
            ["Decide what the slot needs: noun, adjective, adverb or verb.", "Find the signal: the, his or of before it means noun.",
             "Before a noun means adjective. After an action verb means adverb.", "Pick the option with that form."],
            "Only one member of the family fits the job of the slot.",
            "Hard work is the key to ___. (succeed / success / successful / successfully)",
            ["'Key to' is followed by a noun.", "The noun of this family is 'success'."],
            "success"),
        pat("pos-p3", "Linking verb + adjective", "common",
            "The verb is be, seem, look, feel, smell, taste or sound, and one option is an -ly adverb.",
            ["Test the verb: can 'is' or 'seems' replace it?", "If yes, it is a linking verb.",
             "A linking verb takes an adjective.", "Reject the -ly adverb."],
            "The adjective describes the subject, not the way the action is done.",
            "The flowers smell ___. (sweet / sweetly)",
            ["'Smell' here means 'are sweet to the nose'.", "That is a linking verb.", "It takes the adjective 'sweet'."],
            "sweet"),
        pat("pos-p4", "Pronoun case and owner", "common",
            "A pronoun follows a preposition (between you and ___), acts as a subject, or must agree with its owner (its, their).",
            ["Find the job of the pronoun: doer, receiver or owner.", "Receiver or after a preposition: me, him, them.",
             "Doer: I, he, they.", "Owner: its, his, their, never it's."],
            "The job of the pronoun fixes its form, not the way it sounds.",
            "Between you and ___, the plan is weak. (me / I)",
            ["'Between' is a preposition.", "After a preposition use the object form."],
            "me"),
        pat("pos-p5", "many / much and fewer / less", "very common",
            "The blank sits before a noun, and the options mix many, much, fewer, less.",
            ["Can you count the noun? Chairs, people, errors: yes.", "Countable: many or fewer.",
             "Uncountable: much or less (furniture, sugar, time).", "Match the option."],
            "Each word is fixed to one kind of noun.",
            "There is ___ sugar in the tea than in the coffee. (fewer / less)",
            ["Sugar cannot be counted.", "An uncountable noun takes 'less'."],
            "less"),
        pat("pos-p6", "Look-alike adverbs and hardly", "common",
            "The options are hard / hardly, late / lately, near / nearly, high / highly. Or a negative word sits next to hardly.",
            ["Say the meaning: with effort, almost not, recently, almost, very much.",
             "hard = with effort; hardly = almost not.", "Hardly, scarcely and barely already mean 'almost not'.",
             "Never add not or n't to them."],
            "The -ly form is not always the adverb of the plain form; it often has a new meaning.",
            "The old man could ___ walk without a stick. (hard / hardly)",
            ["The meaning is 'almost not'.", "'Hardly' means almost not.", "'Hard' would mean 'with great effort'."],
            "hardly"),
        pat("pos-p7", "Verb after news, police, cattle", "common",
            "The subject is news, mathematics, police, people, cattle or scissors, and the options are is / are.",
            ["Match the noun to its group.", "news, mathematics, measles: singular verb.",
             "police, people, cattle, scissors: plural verb.", "Choose is or are to match."],
            "The shape of the word (with -s or without) does not decide the number.",
            "The news ___ good for the farmers. (is / are)",
            ["'News' looks plural but is singular.", "A singular subject takes 'is'."],
            "is"),
        pat("pos-p8", "Possessive: 's or of", "occasional",
            "A noun shows ownership, and the options mix 's forms with of forms.",
            ["Is the owner a living being? Use 's.", "Is the owner a non-living thing? Use of.",
             "Time, distance and weight take 's: a day's leave.", "Two owners of one thing: 's on the last name only."],
            "English marks ownership by 's for living things and by of for lifeless things.",
            "Which is correct? (a) the table's leg (b) the leg of the table",
            ["A table is not a living thing.", "Non-living things take 'of'."],
            "(b) the leg of the table"),
    ],
)

# =====================================================================
# 2. Tenses
# =====================================================================
SUBS["ge-tenses"] = dict(
    concept=(
        "A tense shows when an action happens and whether it is finished, running or earlier than another action. "
        "You do not need to chant all twelve names. "
        "You need to know which **signal word** asks for which form. "
        "Underline the signal word first, then choose the verb form."
    ),
    notes=r"""### The 12 tenses at a glance
V1 is the base verb, V2 the past form, V3 the past participle (gone, taken).

| Tense | Form | Signal words | Example |
|---|---|---|---|
| Simple present | V1 / V1+s | always, usually, every day | The sun **rises** in the east. |
| Present continuous | is / am / are + V-ing | now, at present, look! | She **is writing** a report. |
| Present perfect | has / have + V3 | just, already, yet, ever, never, so far | I **have finished** my work. |
| Present perfect continuous | has / have been + V-ing | since, for, how long | He **has been waiting** for two hours. |
| Simple past | V2 | yesterday, ago, last year, in 2010 | We **met** him last week. |
| Past continuous | was / were + V-ing | when, while, at 8 pm yesterday | I **was reading** when you called. |
| Past perfect | had + V3 | before, after, already (in the past) | The train **had left** before we reached. |
| Past perfect continuous | had been + V-ing | for, since (in the past) | She **had been working** there for ten years. |
| Simple future | will / shall + V1 | tomorrow, next week, soon | I **will call** you tomorrow. |
| Future continuous | will be + V-ing | at this time tomorrow | We **will be travelling** at noon. |
| Future perfect | will have + V3 | by, by the time, by then | By March they **will have completed** it. |
| Future perfect continuous | will have been + V-ing | for ... by | By June he **will have been teaching** for 20 years. |

### Since and for
*Since* gives the start point (since Monday, since 2019). *For* gives the length (for three days). Both usually need a perfect tense.

- *I **have lived** here **since** 2019.* *I **have lived** here **for** six years.*
- *I live here since 2019* is wrong.
- Action still running: has / have been + V-ing. *It **has been raining** since morning.*
- A running action that ended before a past moment: had been + V-ing. *He was tired because he **had been walking** for six hours.*

> **Rule:** A definite past time word (yesterday, last week, in 2010) forbids the present perfect. *I **saw** him yesterday.* Not *I have seen him yesterday*.

### No future after time and if words
After *when, if, unless, until, till, before, after, as soon as, once, in case*, use the **present** tense. The meaning is still future.

- *I will call you when he **arrives**.* Not *will arrive*.
- *If it **rains**, the match will be cancelled.*
- *By the time* + present gives the future perfect: *By the time you **arrive**, I **will have left**.*
- *By the time* + past gives the past perfect: *By the time we **arrived**, the show **had begun**.*

> **Tip:** Strike out *will* in any clause that starts with when, if, unless or until. *Will* belongs only in the main clause.

### Two past actions
The earlier action takes **had + V3**. The later action takes the simple past.

- *The patient **had died** before the doctor **came**.*
- Hardly, scarcely or no sooner: past perfect first, simple past second. *No sooner **had** I **reached** the station **than** the train **left**.*
- *It is two years since* + simple past: *It is two years since he **left** the job.*
- *It is time / high time / about time* + subject + past form: *It is high time we **left**.*

### Sequence of tenses
A past main verb pulls the other clause into the past.

- *He said that he **was** busy.*
- Exception: universal truths and habits stay in the present. *The teacher said that water **boils** at 100 degrees Celsius.*

### Verbs that avoid the continuous
Some verbs describe states, not actions. They are not used in the -ing tenses: know, believe, understand, like, love, hate, want, prefer, own, possess, belong, contain, consist, seem, mean, see, hear, smell (when involuntary).

- *I **know** him.* Not *I am knowing him*.

Keep one time frame in a sentence unless the meaning changes. *She **opened** the door and **saw** a stranger.* Not *and sees a stranger*.

> **Watch:** Look for the signal word before you read the options. Then check the other clause for the same timeline.
""",
    tricks=[
        trick("Scan for the signal word",
              "Underline the time signal before reading the options. Since or for gives a perfect tense. Yesterday, ago or last gives the simple past. By + future time gives the future perfect. When, if or as soon as with future meaning gives the simple present.",
              "She ___ in this bank for eight years now. (work)",
              ["'For eight years now' means the action began in the past.", "It is still going on.", "Use the present perfect continuous."],
              "has been working"),
        trick("No will after when or if",
              "If a clause starts with when, if, unless, until or as soon as and talks about the future, remove will from that clause. Will stays in the main clause only.",
              "Unless you will apologise, she will not speak to you again. Which part is wrong?",
              ["'Unless' starts a condition clause.", "A condition clause takes the simple present.", "Correct: 'Unless you apologise'."],
              "will apologise -> apologise"),
    ],
    mistakes=[
        mis("Using the present perfect with a past time word: has gone yesterday.", "Use the simple past: went yesterday."),
        mis("Using will in an if or when clause: If it will rain.", "Use the present: If it rains, we will stay in."),
        mis("Writing since two years.", "Since needs a start point; for needs a length: for two years, since 2022."),
        mis("Using a state verb in the -ing form: I am understanding the problem.", "Use the simple form: I understand the problem."),
        mis("Changing a universal truth to the past in reported speech: said that the earth moved round the sun.", "Keep the present: said that the earth moves round the sun."),
        mis("Using the simple past for both of two past events.", "Give the earlier event had + V3: The train had left before we reached."),
    ],
    revision=[
        "ago, last, yesterday: simple past. since, for, just, already: perfect family.",
        "since + start point; for + length of time.",
        "when, if, unless, until, as soon as + present tense, never will.",
        "Earlier past action: had + V3. Later past action: simple past.",
        "Still running: has / have been + V-ing. Ended before a past moment: had been + V-ing.",
        "By the time + present: will have + V3. By the time + past: had + V3.",
        "State verbs (know, like, want, own) do not take -ing.",
    ],
    patterns=[
        pat("ten-p1", "Signal word fixes the tense", "very common",
            "The sentence has a time signal: yesterday, ago, last year, since, for, just, already, now, every day.",
            ["Underline the signal word.", "Read its tense from the table.", "Pick the option with that form.",
             "Reject look-alike forms from the next tense."],
            "Each signal belongs to one tense family.",
            "She ___ to Chennai last year. (moved / has moved / had moved / moves)",
            ["'Last year' is a finished past time.", "A finished past time takes the simple past."],
            "moved"),
        pat("ten-p2", "No future in the time or if clause", "very common",
            "A future main clause (will ...) is joined to a clause starting with when, if, as soon as, until, unless or before.",
            ["Spot the time or condition word.", "Use the present tense in that clause, even for future meaning.",
             "Keep will only in the main clause."],
            "English uses the present form for a future event inside a time clause.",
            "I will call you when I ___ home. (reach / will reach / reached / am reaching)",
            ["'When' starts a time clause.", "A time clause takes the simple present."],
            "reach"),
        pat("ten-p3", "Past perfect for the earlier past action", "common",
            "Two past actions are joined by before, after or when. The options mix had + V3 and V2.",
            ["Put the two actions on a timeline.", "Give the earlier one had + V3.", "Give the later one the simple past.",
             "Check the direction of before or after."],
            "The past perfect exists to mark the earlier of two past events.",
            "The patient had died before the doctor ___. (arrived / had arrived / arrives)",
            ["The death happened first and already uses had + V3.", "The doctor came later.", "The later action takes the simple past."],
            "arrived"),
        pat("ten-p4", "Perfect continuous with since / for", "common",
            "The sentence measures how long an action lasted (since morning, for two years) and the action was running.",
            ["Check that a duration is given and the action is running.", "If it runs up to now: has / have been + V-ing.",
             "If the frame is in the past: had been + V-ing.", "Reject the simple and plain continuous forms."],
            "Only the perfect continuous carries the idea 'from then until now'.",
            "He was exhausted because he ___ for six hours. (walked / had been walking / has walked)",
            ["The walking ran up to a past moment (the exhaustion).", "That needs 'had been' + V-ing."],
            "had been walking"),
        pat("ten-p5", "It is time / since + simple past", "common",
            "The sentence has 'It is (high) time' or 'It is two years since'.",
            ["Spot 'It is time' or 'since' after a length of time.", "Use the simple past after it.",
             "Reject the present or the future form."],
            "These two frames are fixed: the verb after them is in the simple past.",
            "It is high time we ___ for the station. (leave / left / will leave)",
            ["'It is high time' asks for the past form.", "The subject is 'we'."],
            "left"),
        pat("ten-p6", "By the time", "occasional",
            "The sentence starts or joins with 'By the time'. The options mix will have + V3 and had + V3.",
            ["Read the verb after 'by the time'.", "Present verb there: main verb is will have + V3.",
             "Past verb there: main verb is had + V3."],
            "The tense after 'by the time' decides the tense of the main clause.",
            "By the time we arrived, the show ___. (had begun / will have begun / has begun)",
            ["'Arrived' is past.", "The show started earlier.", "The earlier action takes had + V3."],
            "had begun"),
        pat("ten-p7", "State verbs stay simple", "occasional",
            "One option puts know, understand, like, want or own in the -ing form.",
            ["Check if the verb is a state (know, believe, like, want, own).", "State verbs are not used in -ing tenses.",
             "Pick the simple form."],
            "These verbs describe a state of mind or ownership, not an action in progress.",
            "I ___ the answer to this question. (know / am knowing)",
            ["'Know' is a state verb.", "State verbs do not take -ing."],
            "know"),
    ],
)
