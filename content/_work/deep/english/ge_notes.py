# Notes + per-subtopic patterns for grammar-essentials (Phase 2 deep content).
S = {}


def P(id, name, freq, spot, logic, eq, es):
    return {"id": id, "name": name, "frequency": freq, "howToSpot": spot, "formula": None, "logic": logic,
            "example": {"q": eq, "solution": es}}


S["ge-parts-of-speech"] = {
"notes": """### Why parts of speech decide marks
Every error-spotting item is really asking *which word is doing the wrong job*. A noun sits where a verb should be, or an adjective where an adverb is needed. If you know the job each slot needs, the error announces itself.

### Uncountable nouns: the biggest trap family
These nouns have **no plural** and take **singular** verbs, and *much / little / a little* go with them:
information, advice, furniture, luggage, baggage, news, machinery, equipment, scenery, poetry, jewellery, hair, work, bread, money, traffic, progress.
- *She gave me many advices* → **some advice**.
- *The furnitures are new* → **the furniture is new**.
- *The news were shocking* → **the news was shocking**.
*Many* goes with countable plurals (many friends); *much* with uncountables (much time).

### Word-form families
Exams love slots that need one particular form of a family. Check what the slot **needs**:
| Needed | Signal in the sentence | Example |
|---|---|---|
| noun | after *the / his / of / key to* | hard work leads to **success** |
| adjective | before a noun, after *the / very* | his **courteous** behaviour |
| adverb | after an action verb, or modifying an adjective | spoke **harshly**; highly **successful** |
| verb | after the subject or a modal | he will **succeed** |

Common families: succeed–success–successful–successfully; courage–encourage–courageous; strength–strengthen–strong; beauty–beautify–beautiful; anger–angry–angrily.

### Adjective or adverb?
- After an **action verb**, use an adverb: *She sings beautifully.*
- After a **linking verb** (be, seem, look, feel, smell, taste, sound, appear), use an adjective: *The soup tastes good*, not *goodly*.
- Careful: *look* can do both — *He looked sad* (seemed) vs *He looked sadly at the dog* (gazed).

### Pronoun jobs
- **Subject** pronouns act: I, we, he, she, they. **Object** pronouns receive: me, us, him, her, them.
  *Between you and **me*** (after a preposition); *Rahul and **I** went* (as subject).
- **Possessive adjective** before a noun: its employees. **Its** never takes an apostrophe; *it's* = it is.
- *One... one's*; *each other* for two, *one another* for more than two (the classic exam pair).

### Quick revision
- Uncountables never take -s: information, advice, furniture, news, luggage, machinery.
- much + uncountable; many + countable plural.
- Slot decides the form: of/to/for + noun; before noun + adjective; action verb + adverb.
- Linking verbs take adjectives: tastes good, feels bad.
- Between you and me; its without apostrophe; each other (two), one another (many).
""",
"patterns": [
 P("pos-p1", "Uncountable noun trap", "very common",
   "A pluralised uncountable (advices, furnitures, informations) or a much/many mismatch.",
   "1. Ask: can I count this noun in units?\n2. Uncountable → no plural -s, singular verb, much/little.\n3. Rewrite the part and match the option that carries the uncountable form.\n\n*Why it works:* the exam reuses the same small list of uncountables every year.",
   "*Parts: She gave me / many useful advices / before the interview. / No error*", "**many useful advices** is the error — advice is uncountable → *some useful advice*."),
 P("pos-p2", "Word-form family choice", "very common",
   "A blank sits before a noun, after a preposition, or after an action verb; the four options are the four forms of one family.",
   "1. Decide what the slot needs: noun, adjective, adverb or verb.\n2. Find the signal (the/his/of → noun; before a noun → adjective; after an action verb → adverb).\n3. Pick the option with that form.\n\n*Why it works:* only one family member fits the slot's job.",
   "*Hard work is the key to ___.* (succeed/success/successful/successfully)", "'to' after key works as a preposition → noun → **success**."),
 P("pos-p3", "Linking verb + adjective", "common",
   "The verb is be, seem, look, feel, smell, taste or sound, and one option is an -ly adverb.",
   "1. Test the verb: can it be replaced by 'is/ seems'? Then it is a linking verb.\n2. Linking verb + adjective (describes the subject).\n3. Reject the adverb option.\n\n*Why it works:* the adjective describes the subject's state, not the manner of the verb.",
   "*The flowers smell ___.* (sweet/sweetly)", "Smell here = 'are when smelled' → adjective → **sweet**."),
 P("pos-p4", "Pronoun case and agreement", "common",
   "A pronoun follows a preposition (between you and ___), acts as subject, or must agree with its owner (the company and ___ decision).",
   "1. Find the pronoun's job: subject, object or owner.\n2. Object job or after a preposition → me/him/them; subject job → I/he/they.\n3. Owner job → its/his/their + noun, never it's.\n\n*Why it works:* case is fixed by the job, not by the sound.",
   "*Between you and ___, the plan is weak.* (me/I)", "After the preposition 'between' → object form → **me**."),
],
}

S["ge-tenses"] = {
"notes": """### The four zones
English tenses divide time into four zones — simple, continuous, perfect, perfect continuous — across past, present and future. You do not need to chant twelve names; you need to know **which signal word demands which form**.

### Signal words: the fastest marks
| Signal | Tense it demands | Example |
|---|---|---|
| yesterday, ago, last year, in 2010 | simple past | She **moved** last year. |
| since + point of time | perfect (continuous) | I **have known** him since 2015. |
| for + period | perfect (continuous) | We **have lived** here for ten years. |
| just, already, yet, so far, recently | present perfect | He has **just left**. |
| now, look!, listen! | present continuous | Look! It **is raining**. |
| every day, usually, often | simple present | He **walks** to school every day. |
| tomorrow, next week | future | The results **will come** tomorrow. |

*Since* points at the **start** (since Monday, since 2019); *for* measures the **length** (for three days). Mixing them is a planted error.

### Two hard rules the exam loves
**1. No future inside a time or condition clause.** After *when, as soon as, before, after, until, if, unless*, use the **present** tense even when the meaning is future:
- *I will call you when I **reach** home* (not *will reach*).
- *If it **rains**, the match will be cancelled* (not *will rain*).
The future appears only in the **main** clause: will + V1.

**2. The earlier of two past actions takes the past perfect.**
- *The patient **had died** before the doctor **arrived**.*
- *The players **had left** the field before the rain **started**.*
Simple past for the later action; had + V3 for the earlier one.

### Perfect continuous: the 'duration up to now' tense
When an action began in the past and **is still running**, use has/have been + V-ing:
- *It **has been raining** since morning.*
- *The workers **have been working** on this bridge for two years.*
If the running action ended **before another past moment**, shift one step back: had been + V-ing — *He was exhausted because he **had been walking** for six hours.*

### How to attack an item
1. Underline the signal word (ago, since, tomorrow, as soon as, before).
2. Ask: is the action finished, running, or earlier than another action?
3. Match the form, then check the other clause of the sentence for agreement with the timeline.

### Quick revision
- ago/last/yesterday → simple past; since/for/just/already → perfect family.
- since + point, for + period.
- when/if/as soon as + present (never will) in the time clause.
- Earlier past action → had + V3.
- Still running → has/have been + V-ing; finished before a past point → had been + V-ing.
""",
"patterns": [
 P("ten-p1", "Signal word fixes the tense", "very common",
   "The sentence carries a time signal: yesterday, ago, last year, since, for, just, already, now, every day.",
   "1. Underline the signal word.\n2. Read its demanded tense off the signal table.\n3. Choose the option with that form and reject look-alike forms of neighbouring tenses.\n\n*Why it works:* each signal belongs to exactly one tense family.",
   "*She ___ to Chennai last year.* (moved/has moved/had moved/moves)", "last year → simple past → **moved**. 'Has moved' would need a since/for signal."),
 P("ten-p2", "No future in the time or if clause", "very common",
   "The sentence pairs a future main clause (will ...) with a clause beginning when/if/as soon as/until/unless/before.",
   "1. Spot the time/condition word.\n2. Inside that clause use the present tense even for future meaning.\n3. Keep will only in the main clause.\n\n*Why it works:* English treats the time clause as a timetable entry — present form, future sense.",
   "*I will call you when I ___ home.* (reach/will reach/reached/am reaching)", "Time clause → present → **reach**."),
 P("ten-p3", "Past perfect for the earlier past action", "common",
   "Two past actions with before/after/when joining them; the options mix had + V3 and V2.",
   "1. Put the two actions on a timeline.\n2. The earlier one gets had + V3; the later one gets simple past.\n3. Check the before/after direction before choosing.\n\n*Why it works:* the past perfect exists precisely to mark 'earlier past'.",
   "*The patient had died before the doctor ___.* (arrived/had arrived/arrives)", "Death happened first (already in past perfect) → doctor later → **arrived**."),
 P("ten-p4", "Perfect continuous with since/for", "common",
   "The sentence measures an action's duration (since morning, for two years) and the action is still going on.",
   "1. Confirm duration + still running → has/have been + V-ing.\n2. If the frame is past (was exhausted yesterday), step back to had been + V-ing.\n3. Reject plain continuous and simple forms.\n\n*Why it works:* only the perfect continuous family can carry 'from then until now'.",
   "*He was exhausted because he ___ for six hours.*", "Running before a past point → **had been walking**."),
],
}

S["ge-subject-verb-agreement"] = {
"notes": """### The one rule behind every item
A verb agrees with its **real subject** in number: singular subject → singular verb (has, is, was, does), plural subject → plural verb (have, are, were, do). The whole subtopic is about finding the real subject when something stands between it and the verb.

### Rule 1: ignore the phrase before the verb
Words glued to the subject with *of, with, along with, as well as, together with, besides, in addition to, accompanied by* do **not** change its number:
- *The quality **of the mangoes** **was** good.* (subject = quality)
- *The principal, **as well as** the teachers, **was** present.* (subject = principal)
- *The list **of candidates** **has** been published.*
Cover the prepositional phrase with your finger and match the verb to what remains.

### Rule 2: each, every, everyone, either — always singular
- *Each **of the girls** **was** given a certificate.*
- *Every one **of the players** **was** praised.*
- *Neither answer **is** correct.*
Even when a plural noun follows *of*, the words each, every, everyone, everybody, anyone, either, neither keep the verb singular.

### Rule 3: neither...nor / either...or — the verb follows the NEARER subject
- *Neither the manager **nor the workers** **were** present.* (workers = plural, nearer)
- *Either Ram **or his brothers** **are** to blame.*
Think of it as proximity: the verb agrees with the subject closest to it.

### Rule 4: collective nouns and special singulars
- Collective nouns (committee, team, jury, family, audience) take a **singular** verb when the group acts as one: *The committee **announced** its decision.*
- Subjects ending in -ics (mathematics, physics, economics, politics as a field) are singular: *Mathematics **is** my favourite subject.*
- **More than one** + singular noun → singular verb: *More than one student **was** selected.*
- Amounts of money, distance, time as one unit → singular: *Ten kilometres **is** a long walk.*

### Finding the error fast
In divided-part items, the error is nearly always in the verb part. Read the first part, strike the *of/as well as* phrase, ask singular or plural, and test the verb. In fill-blank items, the options are usually has/have, is/are or was/were — the same test decides.

### Quick revision
- Cover of/with/as well as phrases; the head noun rules.
- each/every/everyone/either/neither (alone) → singular.
- neither...nor, either...or → verb follows the nearer subject.
- Committee, mathematics, more than one, ten kilometres → singular.
- The error part usually carries the verb.
""",
"patterns": [
 P("sva-p1", "Head noun before an 'of' phrase", "very common",
   "A phrase like *the quality of, the list of, the bouquet of, one of the* sits before the verb.",
   "1. Find the true head noun (quality, list, bouquet, one).\n2. Ignore the of-phrase entirely.\n3. Match the verb to the head noun's number.\n\n*Why it works:* of introduces a description, not a second subject.",
   "*The bouquet of roses ___ on the table.* (is/are/were/have)", "Head noun = bouquet (singular) → **is**."),
 P("sva-p2", "Each, every and one of: fixed singular", "very common",
   "The subject begins with each, every, everyone, everybody, either, neither, or 'one of the ...'.",
   "1. Confirm the subject word is on the singular list.\n2. Choose the singular verb even if a plural noun follows of.\n3. Reject the plural option that 'sounds' natural.\n\n*Why it works:* these words point to members one at a time, so English keeps the verb singular.",
   "*Each of the girls ___ given a certificate.* (was/were/are/have)", "Each → singular → **was**."),
 P("sva-p3", "Proximity rule for neither...nor / either...or", "common",
   "Two subjects are joined by neither...nor, either...or, or not only...but also, and they differ in number.",
   "1. Find the subject NEARER the verb.\n2. Match the verb to that subject alone.\n3. Ignore the farther subject completely.\n\n*Why it works:* the proximity rule overrides both subjects' individual numbers.",
   "*Neither the manager nor the workers ___ present.* (were/was/is/has)", "Nearer subject = workers (plural) → **were**."),
 P("sva-p4", "Collective nouns and special singular subjects", "common",
   "The subject is a collective noun (committee, team), an -ics subject, 'more than one ...', or an amount (ten kilometres).",
   "1. Check the special-singular list.\n2. Group acting as one unit → singular verb.\n3. Choose the singular form and ignore the plural look of the nearest noun.\n\n*Why it works:* these subjects name one unit or one idea, whatever their shape.",
   "*More than one student ___ selected.* (was/were/have/are)", "More than one → singular → **was** — a planted surprise."),
],
}

S["ge-articles-determiners"] = {
"notes": """### A or An: trust the first SOUND
Choose a or an by the **sound** the next word begins with, never by its spelling:
- **an** before vowel sounds: an hour, an honest man, an heir, an M.A., an MLA, an X-ray.
- **a** before consonant sounds: a university, a European, a one-rupee coin, a unique idea.
*University* begins with the sound 'yu' (a consonant sound); *hour* begins with a silent h. That is the whole game, and the exam plants these exact words.

### Where THE is compulsory
1. **Second mention**: *A king came. **The** king was just.*
2. **Unique things**: the sun, the moon, the sky, the earth, the equator.
3. **Superlatives and ordinals**: the best novel, the first attempt, the only chance.
4. **Rivers, seas, mountain ranges, island groups, deserts**: the Ganga, the Himalayas, the Sahara.
5. **Directions**: the east, the north.
6. **The + adjective = the whole class**: *The rich are not always happy.*

### Where NO article goes (zero article)
- **Languages and subjects**: English, French, mathematics, history.
- **Meals**: have breakfast, at lunch, after dinner.
- **School, college, church, prison, hospital, bed** when used **for their purpose**: *He goes to school every day* (as a student) vs *He went to the school to meet the headmaster* (the building).
- **Man and mankind** in the sense of the human race: *Man is mortal.*
- **General plurals**: *Books are our best friends.*
Planted error: *The man is mortal* → drop *The*.

### Few, a few, little, a little
| Word | Sense | Used with |
|---|---|---|
| few / a few | hardly any / some | countable plurals (friends, days) |
| little / a little | hardly any / some | uncountables (time, hope, money) |
*A few friends* = some friends (positive); *few friends* = almost none (negative). The sentence's sense decides: *He is new in the city and has **few** friends here.*

### Attacking an item
1. Hear the first sound of the next word → a/an settles.
2. Look for the the-triggers: second mention, unique, superlative, rivers, the + adjective.
3. If a language, meal or purpose-building has an article, that part is the error.

One more exam habit: when the options are a/an/the/no-article, say the whole noun phrase aloud before marking. *an university* and *a hour* stumble on the tongue, and the ear catches what the eye forgives.

### Quick revision
- an hour, an MLA, an honest man; a university, a European, a one-rupee coin.
- the: second mention, unique things, superlatives, rivers, directions, the + adjective.
- no article: languages, meals, school-for-study, man (human race), general plurals.
- few/little = hardly any; a few/a little = some.
""",
"patterns": [
 P("art-p1", "A vs An by first sound", "very common",
   "The blank sits before a word whose spelling and sound disagree: hour, honest, heir, university, European, one-..., M.L.A., X-ray.",
   "1. Say the next word aloud and catch its first sound.\n2. Vowel sound → an; consonant sound → a.\n3. Reject the option chosen by spelling.\n\n*Why it works:* the rule is about sound flow, and the exam words are a fixed set.",
   "*She is ___ MLA from Bihar.* (an/a/the/one)", "MLA begins with the sound 'em' → **an**."),
 P("art-p2", "Compulsory THE", "very common",
   "The blank precedes a unique thing, a superlative, a river or range, a direction, or a second mention.",
   "1. Check the the-triggers: unique, superlative, second mention, geographical name, direction, adjective as class.\n2. If one fires, choose the.\n3. Otherwise consider a/an or zero.\n\n*Why it works:* the marks a specific, identified thing; each trigger identifies it.",
   "*___ Ganga is a holy river.* (The/A/An/No article)", "River names take the → **The Ganga**."),
 P("art-p3", "Zero article traps", "common",
   "An article sits before a language, a meal, a purpose-building, or 'man/mankind'; or the sentence compares school and the school.",
   "1. Ask if the noun is used for its purpose (go to school = study).\n2. Languages, meals and mankind take no article.\n3. In divided parts, the article-bearing part is the error.\n\n*Why it works:* purpose-use nouns behave like abstract ideas, not concrete places.",
   "*The man is mortal.* — improve the sentence.", "Man = the human race → **Man is mortal**; drop The."),
 P("art-p4", "Few / a few, little / a little", "common",
   "The blank precedes a countable plural (friends, days) or an uncountable (time, hope), and the options are few/a few/little/a little.",
   "1. Countable plural → few family; uncountable → little family.\n2. Read the sentence's sense: positive (some) → a few / a little; negative (almost none) → few / little.\n3. Match the option.\n\n*Why it works:* a makes the difference between 'some' and 'hardly any'.",
   "*Give me ___ time to think; I'm almost done.* (a little/little/the little/a few)", "Almost done → needs a short positive amount → **a little**."),
],
}

S["ge-prepositions-conjunctions"] = {
"notes": """### Prepositions: time and place
| Preposition | Time | Place |
|---|---|---|
| **at** | exact time: at 6 o'clock, at noon | exact point: at the bus stop, at the door |
| **on** | days and dates: on Monday, on 15 August | surface: on the table, on the wall |
| **in** | months, years, seasons, parts of day: in May, in 1998, in the morning | enclosed or large areas: in the room, in Bengaluru, in India |

Since vs for: *since* + starting point (since 2019, since Monday); *for* + length (for five years, for a week).

### Fixed prepositions: learn as pairs
The exam tests which preposition a particular adjective, noun or verb **demands**. Memorise the pair, not the logic:
| Word | Pair |
|---|---|
| afraid, capable, fond, accused, proud, ashamed | **of** |
| good, bad, skilled, brilliant | **at** |
| angry **at** a thing; angry **with** a person | at / with |
| married, engaged, similar, senior, junior, preferable | **to** |
| abide, comply | **by** |
| listen | **to** |
| wait, prepare, apologise | **for** |
| insist, depend, congratulate ... on | **on** |
Note *senior to* (not senior than) and *prefer tea to coffee* (not than).

### Between and among
- **between** for two (or clearly separate items): *divided between the two winners*.
- **among** for more than two treated as a mass: *distributed among the villagers*.

### Correlative conjunctions: fixed partners
Each of these works only with its partner; mixing the partners is the classic planted error:
- **No sooner ... than**: *No sooner had the bell rung **than** the students rushed out.*
- **Hardly / Scarcely ... when**: *Hardly had the match started **when** it began to rain.*
- **Not only ... but also** (both parts join parallel words): *She is not only intelligent **but also** hardworking.*
- **Neither ... nor; either ... or; both ... and** (both...and never takes a negative).
Remember: *no sooner* and *hardly* open with an inversion (had + subject) in written exam English.

### Attack method
1. Find the word the preposition hangs on (adjective, noun, verb) and recall its fixed pair.
2. For time/place, locate the exactness: point → at, day → on, month/enclosure → in.
3. For conjunctions, complete the pair mentally first, then choose the option that supplies it.

### Quick revision
- at 6 / on Monday / in May; at the door / on the table / in Bengaluru.
- since + point, for + period.
- fond of, good at, angry at a thing, angry with a person, senior to, prefer to.
- between = two, among = many.
- No sooner...than; Hardly...when; Not only...but also.
""",
"patterns": [
 P("pre-p1", "at / on / in for time and place", "very common",
   "The blank precedes or follows a clock time, a day, a month, a city or a surface.",
   "1. Classify the expression: exact point, day/date, month/large area, surface.\n2. at → point, on → day/surface, in → month/enclosure.\n3. Choose the matching option.\n\n*Why it works:* the three prepositions partition time and space by precision.",
   "*We reached the airport ___ 6 o'clock.* (at/on/in/by)", "Exact clock time → **at**."),
 P("pre-p2", "Fixed preposition after a word", "very common",
   "An adjective, noun or verb (fond, good, angry, insist, married) is followed by the blank.",
   "1. Find the governing word.\n2. Recall its fixed pair from the pair list.\n3. Reject the prepositions that fit general meaning but not this word.\n\n*Why it works:* these are conventions, and the exam reuses the same pairs.",
   "*Ravi is very good ___ mathematics.* (at/in/on/for)", "good demands **at** for a skill."),
 P("pre-p3", "Between / among and since / for confusables", "common",
   "Two or more parties share something, or a time span starts or lasts.",
   "1. Count the sharers: two → between, many → among.\n2. Point of start → since; length → for.\n3. Choose accordingly.\n\n*Why it works:* each pair splits one idea by number or shape of the span.",
   "*The prize was divided ___ the two winners.* (between/among/in/into)", "Two winners → **between**."),
 P("pre-p4", "Correlative conjunction pairs", "very common",
   "A sentence opens with no sooner, hardly, scarcely or not only, and the blank is the second half of the pair.",
   "1. Recall the fixed partner: no sooner...than; hardly/scarcely...when; not only...but also.\n2. Eliminate mixed partners (no sooner...when is the classic trap).\n3. Choose the partner word.\n\n*Why it works:* correlatives are welded pairs; the first half dictates the second.",
   "*No sooner did the bell ring ___ the students rushed out.* (than/when/then/that)", "No sooner demands **than**."),
],
}

S["ge-modals-conditionals"] = {
"notes": """### Modals: the base-verb rule
After a modal — can, could, may, might, shall, should, will, would, must — the main verb is always the **base form (V1)**: never to + V1, never -s, never -ing.
- *He can **speak** three languages* (not speaks).
- *You should **consult** a doctor* (not to consult).
- *She need not **say** anything* (need not + V1).

### What each modal means
| Modal | Main job | Example |
|---|---|---|
| can / could | ability; could = past or polite | I can swim. Could you help me? |
| may / might | permission; possibility | May I come in? It might rain. |
| should | duty, advice, criticism of the past (should have + V3) | You should apologise. |
| must | strong obligation; strong deduction (must have + V3) | You must wear a helmet. |
| used to | past habit, now stopped | I used to play cricket every evening. |

### Perfect modals: look back at the past
modal + have + V3 judges or deduces a **past** action:
- **must have** + V3 → sure deduction: *The road is wet; it **must have rained**.*
- **should have** + V3 → it was right but not done: *You **should have taken** my permission.*
- **could have** + V3 → it was possible but did not happen: *He **could have won** with more practice.*

### Conditionals: the four patterns
| Type | If-clause | Main clause | Example |
|---|---|---|---|
| Zero | simple present | simple present | If you heat ice, it melts. |
| First (real) | simple present | will + V1 | If it rains, the match **will be** postponed. |
| Second (unreal present) | simple past | would + V1 | If I **were** you, I **would apologise**. |
| Third (unreal past) | had + V3 | would have + V3 | If he **had prepared** well, he **would have passed**. |

The planted errors: *will* in the if-clause, *was* for the second conditional (exam answer: **were**), and *would* in the third conditional's if-clause (correct: had + V3).

### Attack method
1. Spot the modal or the if-clause first.
2. Apply the base-verb rule, or read off the conditional row.
3. For perfect modals ask: is the speaker deducing the past (must have) or finding fault with it (should have)?

The two rules that settle most items in seconds: after any modal, the next verb is bare V1; and whatever the if-clause takes, the main clause never repeats it. If the if-clause has *had + V3*, the main clause must show *would have*; if the if-clause already says *would*, the sentence is wrong by default.

### Quick revision
- Modal + V1 always: can speak, should consult, need not say.
- must have = sure past deduction; should have = past fault; could have = missed possibility.
- First: if + present, will + V1. Second: if + past, would + V1 (were). Third: if + had V3, would have + V3.
- used to = past habit.
""",
"patterns": [
 P("mod-p1", "Modal + base verb", "very common",
   "A modal is present and the options offer to + V1, V1, V-ing or V-s forms.",
   "1. Confirm a modal (can, should, must, need not) governs the verb.\n2. Strip everything but the base form V1.\n3. Reject to-infinitives and -s/-ing forms.\n\n*Why it works:* modals themselves carry the tense, so the main verb stays bare.",
   "*You should ___ a doctor immediately.* (consult/to consult/consulting/consults)", "should + V1 → **consult**; 'to consult' is the planted error."),
 P("mod-p2", "Perfect modal of judgement", "common",
   "The sentence looks back at a past action (the road is wet; you look exhausted) and the options are must/should/could + have.",
   "1. Ask the speaker's purpose: deduce surely (must have), find fault (should have), note a missed chance (could have).\n2. Match the option.\n3. Keep have + V3 after the modal.\n\n*Why it works:* the three perfect modals split the past into three speaker attitudes.",
   "*You ___ have taken my permission before using my laptop.*", "Fault-finding about the past → **should have taken**."),
 P("mod-p3", "Conditional sentence patterns", "very common",
   "An if-clause is present and the options mix will, would, had + V3 and would have + V3.",
   "1. Decide reality: true/likely (first), imaginary present (second), imaginary past (third).\n2. Read off the row: present + will; past + would; had + V3 + would have + V3.\n3. Use were (not was) in the second conditional.\n\n*Why it works:* each conditional is a fixed two-part formula; one half decides the other.",
   "*If I ___ you, I would apologise at once.* (were/was/am/had been)", "Unreal present → second conditional → **were**."),
 P("mod-p4", "Modal choice: permission, habit, possibility", "common",
   "The sentence is a polite request, a past habit, or a prediction with varying certainty.",
   "1. Request → may/can; past habit → used to; certainty ladder: must > may/might > could.\n2. Match the politeness or certainty level the sentence signals.\n3. Reject modals of the wrong strength.\n\n*Why it works:* modals encode the speaker's certainty and politeness, so the sentence's tone picks one.",
   "*When I was young, I ___ play cricket every evening.* (used to/am used to/was used to/use to)", "Stopped past habit → **used to**."),
],
}

S["ge-comparison-question-tags"] = {
"notes": """### Degrees of comparison: three patterns
- **Positive**: as + adjective + as — *Ram is **as tall as** Shyam.* The negative: not as/so ... as.
- **Comparative**: adjective-er / more + adjective + **than** — *taller than, more useful than*.
- **Superlative**: the + adjective-est / most + adjective + of/in — *the tallest **in** the class*.

Two planted errors cover most questions:
1. **Double comparative** — *more costlier, more better* are always wrong: one marker only (costlier OR more costly).
2. **Wrong partner** — a comparative must carry *than*; a superlative carries *the* and a group (in the class, of all).

### 'Than any other' constructions
When the subject belongs to the group it is compared with, use **any other** so the subject is not compared with itself:
- *Mount Everest is higher than **any other** peak in the world.*
- *Delhi is larger than **any other** city in Haryana* — wait, check membership: if the subject is NOT in the group, plain 'any' works: *The Yamuna is longer than any river in Haryana* only if the Yamuna is not a Haryana river. Ask: is the subject inside the group? Inside → any other; outside → any.

### Question tags: the mirror rule
A tag copies the sentence's auxiliary, flips its **polarity**, and ends with a matching pronoun:
- *She sings well, **doesn't she**?* (positive sentence → negative tag; sings needs does)
- *They haven't finished, **have they**?* (negative → positive tag)
The pronoun replaces the subject: nobody → **they**, everybody → **they**, this/that → **it**, these/those → **they**.

### Special tags to memorise
| Sentence | Tag |
|---|---|
| Let's go for a walk | shall we? |
| Open the window | will you? |
| I am late | aren't I? |
| Nobody called | did they? |
| Nothing happened | did it? |
| He has a car (possession, Indian usage) | doesn't he? |

Note *I am → aren't I* — the only place English drops 'am not I'.

### Attack method
1. For comparison items, count the markers (more + -er = error) and check than/the + group.
2. For tags, name the auxiliary, flip it, and swap the subject for its pronoun — in that order, every time.

In divided-part items the comparison error hides in the first half (*Gold is more costlier...*), while the tag error, when it appears, is always the last part. Scan the first part for double markers and the last part for the tag, and you cover both question types in one pass.

### Quick revision
- as...as / -er than / the -est in; never more + -er together.
- Subject inside the group → than any other.
- Tag = auxiliary copy + polarity flip + subject pronoun.
- Let's → shall we; imperative → will you; I am → aren't I; nobody → they.
""",
"patterns": [
 P("cmp-p1", "One marker only (no double comparative)", "very common",
   "An option or a part reads more + -er (more costlier, more better) or a superlative with more.",
   "1. Count the markers of comparison in the phrase.\n2. Two markers (more + -er) → error.\n3. Keep exactly one: costlier / more costly / the costliest.\n\n*Why it works:* English never stacks the two ways of forming a comparative.",
   "*Parts: Gold is more costlier / than silver, / but both are / widely used.*", "**Gold is more costlier** is the error → Gold is costlier."),
 P("cmp-p2", "Than any other construction", "common",
   "A superlative-style comparison names the group the subject belongs to, and the options are any / any other / all other.",
   "1. Ask: is the subject a member of the group?\n2. Member → exclude itself: any other.\n3. Outsider → plain any is fine.\n\n*Why it works:* a thing cannot be taller than itself, so the exam forces 'other'.",
   "*Mount Everest is higher than ___ peak in the world.* (any other/any/all other/others)", "Everest is a peak → **any other** peak."),
 P("cmp-p3", "Standard question tags", "very common",
   "A complete sentence with a comma sits before the blank; the options are auxiliary + pronoun pairs.",
   "1. Name the sentence's auxiliary (does, have, is, will).\n2. Flip the polarity: positive sentence → negative tag.\n3. Replace the subject with its pronoun.\n\n*Why it works:* every regular tag is just these three operations.",
   "*She sings well, ___?* (doesn't she/isn't she/does she/won't she)", "sings → does; positive → negative → **doesn't she**."),
 P("cmp-p4", "Special tags: let's, imperative, I am, nobody", "common",
   "The sentence is a let's suggestion, a command, an I am statement, or has nobody/nothing as subject.",
   "1. Match the sentence type to the special-tag table.\n2. let's → shall we; command → will you; I am → aren't I.\n3. nobody/everybody → they; nothing → it.\n\n*Why it works:* these five tags are fixed idioms; there is no rule to derive them from.",
   "*I am late, ___?* (aren't I/amn't I/not I/don't I)", "The fixed tag for I am → **aren't I**."),
],
}

S["ge-non-finites-inversion"] = {
"notes": """### Non-finites: the three shapes
A non-finite verb does not change with tense or subject. Three shapes exist:
1. **Infinitive**: to + V1 — *He promised **to finish** the work.*
2. **Gerund** (-ing used as a noun): *He avoided **answering** the question.*
3. **Participle** (-ing/-V3 used as an adjective): *the **broken** chair; **Seeing** the snake, she fainted.*

### Gerund after prepositions and set verbs
After any **preposition**, the verb takes -ing: *fond of **reading**; insisted on **paying**; interested in **learning**; before **leaving***.
After these verbs, the next verb is a **gerund**: enjoy, avoid, mind, finish, suggest, keep, practise, stop, deny, admit, consider.
*Look forward to* ends in a preposition *to*, so it takes -ing too: *I look forward to **meeting** you* (not to meet).

### Infinitive after set verbs
After these verbs, use **to + V1**: promise, decide, agree, hope, plan, refuse, learn, afford, manage, want, offer.
**Remember + to** = duty ahead (*Remember to switch off the lights*); **remember + -ing** = memory of the past (*I remember switching it off yesterday*).

### Bare infinitive (no to)
After **make, let, hear, see, watch, feel** (and after modals): *The teacher made the boy **recite** the poem; Let him **do** what he wants.* Passive voice restores *to*: *He was made **to recite** it.*

### Inversion after negative openers
When a sentence opens with a negative or restrictive adverbial, the **auxiliary jumps before the subject**:
- *No sooner **had she seen** the snake **than** she fainted.*
- *Hardly/Scarcely **had he sat down when** the phone rang.*
- *Never **have I seen** such a sunset.*
- *Not only **did he apologise**, but he also paid for the damage.*
The pattern is: opener + auxiliary + subject + main verb. *No sooner* pairs with **than**; *hardly/scarcely* pair with **when**. Mixed partners (No sooner...when) are the planted error.

### Attack method
1. For non-finite items, find the governing word: preposition → -ing; set verb → its listed pattern.
2. For inversion items, check the opener. Negative opener → auxiliary first, and verify the partner word (than/when).

A quick self-test before marking: cover the options and say the sentence aloud. *look forward to meet* and *No sooner the bell rang* both jar on the ear — the spoken check catches most gerund and inversion slips faster than any rule recall.

### Quick revision
- Preposition + V-ing; look forward to meeting.
- enjoy/avoid/mind/finish/suggest + V-ing; promise/decide/agree + to V1.
- remember to = duty ahead; remember -ing = past memory.
- make/let/hear/see + bare V1.
- Negative opener → auxiliary before subject; no sooner...than, hardly...when.
""",
"patterns": [
 P("nfi-p1", "Gerund after prepositions and set verbs", "very common",
   "The blank follows a preposition (of, on, in, to after look forward) or a set verb (avoid, enjoy, mind, finish, keep).",
   "1. Find the governing word.\n2. Preposition or set verb → next verb takes -ing.\n3. Reject to + V1 options.\n\n*Why it works:* a preposition needs a noun, and the -ing form is the verb turned noun.",
   "*He avoided ___ the question.* (answering/to answer/answer/answered)", "avoid + gerund → **answering**."),
 P("nfi-p2", "Infinitive vs gerund by set verb or meaning", "very common",
   "The governing verb is from the to-list (promise, decide, agree) or remember/stop/forget, where the form changes the meaning.",
   "1. Check the verb against the two lists.\n2. remember/forget + to = duty ahead; + -ing = past memory.\n3. Choose the matching form.\n\n*Why it works:* the two lists are short, fixed and endlessly recycled.",
   "*He promised ___ the work by Friday.* (to finish/finishing/finish/finished)", "promise + to-infinitive → **to finish**."),
 P("nfi-p3", "Bare infinitive after make, let, see, hear", "common",
   "The sentence has make/let/hear/see/watch followed by an object and the blank.",
   "1. Confirm the causative/perception verb.\n2. Object + bare V1 — no to, no -ing.\n3. If the sentence is passive, restore to (was made to recite).\n\n*Why it works:* these verbs take the plain base form; every other verb family takes to or -ing.",
   "*The teacher made the boy ___ the poem.* (recite/to recite/reciting/recited)", "make + object + bare infinitive → **recite**."),
 P("nfi-p4", "Inversion after negative openers", "very common",
   "The sentence opens with No sooner, Hardly, Scarcely, Never or Not only — or one part contains the un-inverted subject-first order.",
   "1. Confirm the negative opener.\n2. Order: opener + auxiliary + subject + main verb (No sooner had she seen...).\n3. Check the partner: no sooner...than; hardly/scarcely...when.\n\n*Why it works:* the negative opener demands inversion, and each opener carries its fixed partner.",
   "*Never ___ such a beautiful sunset.* (have I seen/I have seen/I saw/did I saw)", "Negative opener → **have I seen** — auxiliary before subject."),
],
}
