"""Readable rewrite of English > Fill in the Blanks (all 6 subtopics).

Plain English, short sentences, tables for word lists, one method per blank type.
Every fact from the old notes/concept is kept; new pattern ids continue each subtopic's prefix.
Run: python fill_in_the_blanks.py  (patches content/core/topics/english/fill-in-the-blanks.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "fill-in-the-blanks.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Collocations
# =====================================================================
SUBS["fb-collocations"] = dict(
    concept=(
        "A *collocation* is a pair of words that English always uses together, like *pay attention* or *heavy rain*. "
        "In these blanks, most options fit the grammar. Only one option is the usual partner of the word next to the blank. "
        "So you pick the partner, not just a word with the right meaning."
    ),
    notes=r"""### What the blank really tests
Look at this blank: *Please ___ attention to the rules.* The options are give, do, make and pay.

All four fit the grammar. But English says only **pay attention**. The question tests the partner word, not the meaning.

> **Rule:** Find the word right next to the blank. Ask: "Which word does this one usually go with?"

- Blank **after a verb** → pick the verb's usual object (*break the news*, *take place*).
- Blank **before a noun** → pick the noun's usual adjective (*grave mistake*, *close scrutiny*).
- Blank **after a noun** → pick the noun's usual verb (*prices soar*).

### Verb + noun pairs
These swaps come up again and again. The last column shows the wrong verb that papers offer.

| Verb | Goes with | Wrong swap |
|---|---|---|
| pay | attention, a visit, a compliment, heed | give, do, make |
| take | place, a decision, a step, a risk, pride, measures | give, do |
| make | a mistake, progress, an effort, amends, a noise | do |
| do | harm, good, a favour, one's duty, business, justice | make |
| commit | a mistake, a crime, an error (formal) | did |
| keep / break | a promise, a secret / a promise, the news, a record | |
| catch | a cold, a thief, a signal | take |
| reach | a conclusion, a verdict, a consensus | arrive |
| meet / strike | a deadline, a requirement / a balance, a deal, a bargain | |
| cast / lay | a vote, a glance / emphasis, claim, hands on | |
| gain / bear | ground, momentum / fruit, a resemblance | |
| burst into | tears, laughter | |

> **Tip:** Learn each pair as one chunk, like "pay-attention". Never learn the verb alone.

### Adjective + noun pairs
The wrong options here are near-synonyms. *Strong rain*, *quick asleep* and *tight escape* look fine but are wrong.

| Pair | Meaning |
|---|---|
| heavy rain / traffic; strong wind / coffee / odour | usual pairs |
| fast asleep; sound sleep | deeply asleep |
| narrow escape / margin / victory; close shave / contest | only just |
| grave mistake / risk / crisis | very serious |
| solemn pledge / promise; stark contrast / reality | formal pairs |
| staunch supporter | loyal follower |
| soaring prices | prices rising fast |
| scathing attack | bitterly critical |
| abject poverty | utter, hopeless poverty |
| conclusive evidence | proof that settles the issue |
| glaring error | shockingly obvious error |
| close scrutiny | careful examination |
| teeming millions | huge crowds of people |
| invaluable service | too valuable to price |
| level playing field | fair conditions for all |
| barren land / effort | producing nothing |
| loud applause | usual pair |

### Pairs with a fixed preposition
Sometimes the sentence already gives the preposition. Then only one word completes the pair.

emphasis **on**, comply **with**, abide **by**, capable **of**, fond **of**, congratulate someone **on**, insist **on**, married **to**, superior **to**.

> **Watch:** *deal in* means trade (deal in cloth). *deal with* means handle (deal with a problem).

### Frozen pairs and formal tone
Some pairs never change: *null and void*, *part and parcel*, *safe and sound*, *first and foremost*. No word can be swapped in.

When two options are both real pairs, choose the neutral, formal one. *Hold talks* beats *hold chats*. *Offer condolences* is right; *give sorrows* is not English.

If two options still look right, read the whole sentence. The setter usually locks the answer with a preposition or a phrase elsewhere.

### How to practise
Learn ten pairs a day. Test yourself both ways: verb to partner, then partner to verb. Use each pair in a sentence of your own.

In the exam, say the full sentence silently. *Give attention to the rules* sounds wrong to a trained ear. If you hesitate, you never learnt that pair.
""",
    tricks=[
        {"title": "Answer before you look at the options",
         "body": "Read up to the blank and stop. Ask what the word before it usually takes. Say your answer, then find it among the options.",
         "example": {"q": "The two leaders held detailed ___ on the border dispute.",
                     "steps": ["'Held detailed ...' needs a noun for a formal discussion.",
                               "Deliberations fits. Celebrations and medications do not suit a border dispute.",
                               "Reverberations are echoes of sound, so they are out too."],
                     "answer": "deliberations"}},
        {"title": "Cut options by topic",
         "body": "Collocation options often share an ending (-tion, -ment). Remove the ones that do not suit the topic first. A border dispute invites talks or deliberations, never medications."},
        {"title": "Finish the phrase in your head",
         "body": "For a verb blank, turn the phrase around: 'attention is ___' gives 'paid'. If your word is an option, mark it and move on."},
    ],
    mistakes=[
        mis("Choosing a synonym that breaks the pair, such as 'give attention'.", "Pick the fixed partner: pay attention, take place, commit a crime."),
        mis("Choosing the longest or most impressive word.", "The collocation answer is usually an ordinary, everyday word."),
        mis("Ignoring the preposition after the blank ('___ on', '___ with').", "Let the preposition fix the chunk: emphasis on, comply with, abide by."),
        mis("Treating near-synonym adjectives as equal (strong rain, quick asleep).", "Learn the adjective with its noun: heavy rain, fast asleep, narrow escape."),
        mis("Answering after reading only half the sentence.", "Read to the full stop. A later phrase often decides between two real pairs."),
    ],
    revision=[
        "The word next to the blank decides the answer, not the general meaning.",
        "pay attention / heed; take place / a step; make a mistake / progress; do harm / good; commit a crime.",
        "heavy rain, strong wind, fast asleep, narrow escape, solemn pledge, stark contrast.",
        "abject poverty, staunch supporter, glaring error, conclusive evidence, close scrutiny.",
        "A given preposition fixes the pair: emphasis on, comply with, capable of, abide by.",
        "Frozen pairs never change: null and void, part and parcel, safe and sound.",
        "Say the finished sentence silently: the right pair sounds whole.",
    ],
    patterns=[
        pat("fbc1", "do / make / take / give / pay swap", "very common",
            "The blank is a verb before a noun like attention, place, a visit or a decision. The options are pay, give, do, make, take.",
            ["Read the noun after the blank.", "Recall its fixed verb: pay attention, take place, pay a visit, take a decision.",
             "Reject verbs that fit grammar but not usage (give attention, do a visit)."],
            "All five verbs fit the grammar, so only the fixed pair can decide.",
            "Please ___ attention to the instructions before the demo begins.",
            ["The noun after the blank is 'attention'.", "The fixed pair is 'pay attention'.", "Give, do and make attention are not used in English."],
            "pay"),
        pat("fbc2", "Adjective + noun pair", "very common",
            "The blank is an adjective before a noun such as rain, escape, sleep or pledge. The options are near-synonyms (heavy / strong, narrow / close).",
            ["Name the noun after the blank.", "Recall its fixed adjective: heavy rain, narrow escape, solemn pledge.",
             "Say each decoy aloud (strong rain, quick asleep) and reject it."],
            "The decoys are chosen because they almost sound right; only the fixed pair is correct.",
            "The trekkers were caught in ___ rain on the third day.",
            ["The noun is 'rain'.", "English says 'heavy rain'.", "Strong rain and powerful rain are not used."],
            "heavy"),
        pat("fbc3", "Illness and feeling reactions", "common",
            "The sentence is about falling ill or a sudden feeling (a cold, tears, laughter). The options are verbs like catch, burst, take, rush.",
            ["Name the event: falling ill, crying or laughing.", "Recall the chunk: catch a cold, burst into tears, burst into laughter.",
             "Reject word-for-word swaps like take a cold or rush into tears."],
            "These chunks are fixed; students who translate word for word pick the decoys.",
            "She ___ into tears when the results were announced.",
            ["The event is sudden crying.", "The fixed chunk is 'burst into tears'.", "Break, rush and dash into tears are not used."],
            "burst"),
        pat("fbc4", "Fixed expressions (break the news, a narrow escape)", "common",
            "The sentence is about giving news, escaping just in time or a similar event. One option completes a fixed expression.",
            ["Read the whole sentence to see the situation.", "Match it to the fixed expression: break the news, a narrow escape.",
             "Reject synonyms such as crack the news or thin escape."],
            "A fixed expression works like one word; half-remembered versions are the decoys.",
            "The manager had to ___ the news of the layoffs to the staff.",
            ["The situation is giving bad news.", "The fixed expression is 'break the news'.", "Crack, tear and split the news do not exist."],
            "break"),
        pat("fbc5", "reach / meet / strike + result nouns", "common",
            "The blank comes before a result noun (a balance, a deadline, a conclusion, a verdict). The options are verbs like strike, hit, meet, match.",
            ["Name the result noun.", "Recall the pair: strike a balance, meet a deadline, reach a conclusion, arrive at a decision.",
             "Check any preposition: meet a deadline takes none; arrive takes at."],
            "These verbs look alike, but each noun has one locked partner.",
            "The team worked over the weekend to ___ the submission deadline.",
            ["The result noun is 'deadline'.", "The fixed pair is 'meet a deadline'.", "Match, catch and equal a deadline are not used."],
            "meet"),
        pat("fbc6", "Word + fixed preposition", "common",
            "The preposition after the blank is printed (___ on, ___ with, ___ by). The options are words of similar meaning.",
            ["Read the preposition after the blank.", "Recall which option pairs with it: emphasis on, comply with, abide by, capable of.",
             "Reject options that need a different preposition."],
            "Each word takes its own preposition, so the printed preposition picks the word.",
            "All shops must ___ with the new safety rules by March.",
            ["The preposition after the blank is 'with'.", "'Comply with' is the fixed pair.", "Obey, follow and respect take no 'with'."],
            "comply"),
        pat("fbc7", "Formal adjective + noun (abject poverty)", "common",
            "The sentence is formal (news, reports). The blank is an adjective before poverty, error, supporter, evidence or a similar noun.",
            ["Name the noun after the blank.", "Recall its formal partner: abject poverty, glaring error, staunch supporter, conclusive evidence.",
             "Check the meaning fits the sentence (very bad, very obvious, loyal, settling)."],
            "Formal nouns have strong adjective partners, and the exam tests exactly these.",
            "Many families in the flooded district still live in ___ poverty.",
            ["The noun is 'poverty'.", "Its formal partner is 'abject' (utter, hopeless).", "Stark, grave and glaring do not pair with poverty here."],
            "abject"),
    ],
)

# =====================================================================
# 2. Phrasal verbs
# =====================================================================
SUBS["fb-phrasal-verbs"] = dict(
    concept=(
        "A *phrasal verb* is a verb plus a small word like *off*, *up* or *into*. Together they make a new meaning. "
        "*Call off* means cancel; it has nothing to do with calling. "
        "So first find the meaning the sentence needs, then pick the verb and small word that carry it."
    ),
    notes=r"""### One verb plus a small word
A phrasal verb is a verb plus a *particle* (a small word such as off, on, up, in, out, down). The pair works as one new word.

> **Example:** *The strike was called off.* Here "called off" means **cancelled**. *He gave in.* Here "gave in" means **surrendered**.

So the blank tests meaning. Read the sentence, say its meaning in one plain word, and pick the phrasal verb that means that.

### Same verb, different small words
This is the favourite question. One verb repeats; only the small word changes.

| Verb | Small word and meaning |
|---|---|
| call | **off** cancel; **on** urge, appeal to; **for** demand, need; **up** telephone; **in** summon, withdraw |
| look | **after** care for; **into** investigate; **forward to** wait with pleasure; **down upon** despise; **up to** admire; **for** search |
| put | **off** postpone; **up with** tolerate; **down** suppress; **across** communicate; **out** put out a fire |
| turn | **down** reject; **up** appear; **out** prove to be; **over** hand over |
| give | **in (to)** surrender; **up** quit; **away** reveal or donate; **off** send out (smell, heat) |

> **Rule:** When the options share one verb, ask: "Which meaning does this sentence need?"

### Other common phrasal verbs

| Phrasal verb | Meaning | Example |
|---|---|---|
| carry out | perform | carry out orders / a survey |
| break out | begin suddenly | a fire broke out |
| run out of | have none left | we ran out of time |
| do away with | abolish | the tax was done away with |
| bring about | cause | the reform brought about change |
| cut down on | reduce | cut down on sugar |
| stand by | support, stay loyal | she stood by her friend |
| come across | find by chance | I came across an old letter |

### What the small word often adds
The particle often gives a direction. Use it when two options both look possible.

- **off**: cancel, away (call off, put off)
- **out**: burst out, give out (break out, carry out)
- **up**: appear, build (turn up)
- **down**: reject, reduce (turn down, cut down)
- **in**: give way, enter (give in)

> **Watch:** This is a hint, not a law. Always test the full meaning in the sentence.

### The "to" that takes -ing
In three common phrases, *to* is a preposition, so an **-ing** form follows it.

- look forward to **meeting** you
- be used to **working** late
- object to **paying** extra

The blank may be the particle itself: *I am looking ___ to hearing from you* → **forward**.

### Where the object goes
- *Put up with* needs an object: put up with **the noise**. *Give in* needs none: the rebels **gave in**.
- A two-part verb can split around its object: *call the match off* or *call off the match*.
- A pronoun must go inside: *call it off*, never *call off it*.
- Three-part verbs never split: *put up with it*, *look down upon*, *get away with*, *run out of*.
- *Break out* (war, fire, disease) has no passive. "Was broken out" is wrong.

Choose the plain option over the fancy one. If two options are real phrasal verbs, test each in the sentence and let meaning decide.
""",
    tricks=[
        {"title": "Say the meaning in one word, then match",
         "body": "Put the sentence's action in one plain word: cancelled, tolerated, abolished. Then pick the phrasal verb that means that word.",
         "example": {"q": "The company had to call ___ the proposed merger after the audit.",
                     "steps": ["The action is 'cancel'.", "Cancel = call off.",
                               "Call up = telephone, call for = demand, call out = shout."],
                     "answer": "off"}},
        {"title": "Swap in a one-word verb",
         "body": "Replace each option with a one-word verb (call off = cancel, turn down = reject). The option whose swap keeps the meaning is right."},
        {"title": "Use the direction of the small word",
         "body": "Ask what happens to the object: stopped or removed (off, out), raised (up), lowered or refused (down), accepted (in). Match that to the particle."},
    ],
    mistakes=[
        mis("Picking the particle your first language would use.", "Learn each phrasal verb as one unit with its English meaning."),
        mis("Mixing 'put up with' (tolerate) and 'put off' (postpone) because both start with 'put'.", "Say the meaning first, then choose: tolerate = put up with, postpone = put off."),
        mis("Reading only the clause with the blank.", "Read the whole sentence; the doer and the reason are often in the other clause."),
        mis("Writing 'was broken out' for a fire or a war.", "Break out has no passive: 'a fire broke out'."),
        mis("Writing 'look forward to meet you'.", "The 'to' here is a preposition: look forward to meeting you."),
    ],
    revision=[
        "A phrasal verb is verb + small word with a new meaning: call off = cancel.",
        "call off cancel; call on urge; call for demand; call up telephone.",
        "look after care for; look into investigate; look up to admire; look down upon despise.",
        "put off postpone; put up with tolerate; turn down reject; give in surrender.",
        "look forward to / be used to / object to + -ing.",
        "Pronouns go inside two-part verbs (call it off); three-part verbs never split.",
        "Test each option in the sentence; meaning decides, not familiarity.",
    ],
    patterns=[
        pat("fbp1", "Same verb, different small words", "very common",
            "One verb repeats in all options (called off / called on / called for / called up). Only the particle changes.",
            ["Say the meaning the sentence needs in one word.", "Match it to the particle: cancel = off, demand = for, telephone = up, urge = on.",
             "Read the finished sentence once to confirm."],
            "Each particle turns the same verb into a different word, so only meaning can choose.",
            "The board meeting has been ___ because the chairman is unwell.",
            ["The meeting will not happen, so the meaning is 'cancelled'.", "Cancelled = called off.",
             "Called for = demanded; called up = telephoned."],
            "called off"),
        pat("fbp2", "look-family blanks", "very common",
            "The verb 'look' comes before the blank, or the options are look after / into / forward to / up to / down upon.",
            ["Decide the meaning: care for, investigate, wait eagerly, admire or despise.",
             "Pick the matching particle: after, into, forward to, up to, down upon.",
             "If you choose 'forward to', check that an -ing form or a noun follows."],
            "'Look' is the most tested phrasal verb because its particles give five everyday meanings.",
            "A three-member committee will look ___ the ragging complaint.",
            ["A committee checks a complaint, so the meaning is 'investigate'.", "Investigate = look into.",
             "Look after would mean the committee takes care of the complaint."],
            "into"),
        pat("fbp3", "put-family blanks", "common",
            "The sentence is about postponing, tolerating, stopping or explaining. The options are put off / put up with / put down / put across.",
            ["Decide the meaning: postpone, tolerate, suppress or communicate.", "Match: off, up with, down, across.",
             "For 'put up with', check that an object follows 'with'."],
            "'Put up with' is a three-part verb, and students often stop at 'put up'.",
            "The workers refused to put ___ the unsafe conditions any longer.",
            ["The workers will not bear the conditions, so the meaning is 'tolerate'.", "Tolerate = put up with.",
             "The object 'the unsafe conditions' follows 'with'."],
            "up with"),
        pat("fbp4", "Mixed common phrasal verbs", "common",
            "The options are four different phrasal verbs (turned down / turned up / carried out / gave in). Only one fits the sentence.",
            ["Say the meaning the sentence needs: reject, perform, surrender, begin suddenly.",
             "Map it: reject = turn down, perform = carry out, surrender = give in, begin suddenly = break out.",
             "Check the words after the blank: an object, a 'to', or nothing."],
            "With different verbs the options cannot be confused by shape; meaning and the words around the blank decide.",
            "The college turned ___ his application because the marks card was incomplete.",
            ["The college refused the application, so the meaning is 'rejected'.", "Rejected = turned down.",
             "Turned up would mean the application appeared."],
            "down"),
        pat("fbp5", "look forward to / be used to / object to + -ing", "common",
            "The blank comes right after 'look forward to', 'be used to' or 'object to'. The options mix the base verb and the -ing form.",
            ["Spot the phrase ending in 'to'.", "Remember that this 'to' is a preposition.", "Pick the -ing form."],
            "A preposition is followed by a noun or an -ing form, never by a base verb.",
            "The villagers objected to ___ extra for the new water connection.",
            ["The phrase is 'objected to'.", "Here 'to' is a preposition.", "So the -ing form follows: 'paying'."],
            "paying"),
        pat("fbp6", "break and run families", "occasional",
            "The options share 'break' or 'run' with different particles (break out / break down / break into; run out of / run into / run over).",
            ["Decide the meaning: begin suddenly, stop working, enter by force; have none left, meet by chance, hit with a vehicle.",
             "Match: break out, break down, break into; run out of, run into, run over.",
             "Check the subject: fires and wars break out; machines break down."],
            "Each particle gives the verb a separate meaning, and the subject of the sentence usually points to it.",
            "Our bus broke ___ on the highway, so we reached the venue late.",
            ["A bus that stops working has 'broken down'.", "Break out is for fires, wars and diseases.",
             "Break into means enter by force."],
            "down"),
    ],
)

# =====================================================================
# 3. Verb form and tense
# =====================================================================
SUBS["fb-verb-form-tense"] = dict(
    concept=(
        "When the blank is a verb, two things decide the answer. "
        "First, the **time words** in the sentence (since, yesterday, by the time) pick the tense. "
        "Second, the **word just before the blank** can fix the form: -ing, to + verb, or the plain verb."
    ),
    notes=r"""### Read the time words first
Circle the time words before you look at the options. They pick the tense for you.

> **Example:** *He ___ in this office since 2019.* "Since 2019" means the action started then and is still going. Answer: **has been working**.

Useful time words: since, for, by the time, already, yet, yesterday, before, after, when, if, until. The wrong options are real verb forms, just from the wrong tense.

### Time word to tense

| Time words | Tense | Example |
|---|---|---|
| since 2015 / for ten years (still going) | present perfect (continuous) | has worked / has been working |
| yesterday / last week / in 2010 | simple past | went |
| two past events, one earlier | earlier one: had + V3 | the train had left before we reached |
| by + past time | had + V3 | by 2020 he had retired |
| by + future time | will have + V3 | by next March we will have completed it |

V3 means the past participle (gone, taken, written).

### Two past events
The earlier event takes **had + V3**. The later event takes the **simple past**.

- *By the time the fire brigade arrived, the shed **had burnt** down.*
- If the subject receives the action, use **had been + V3**: *the building **had been evacuated***.
- **Hardly / Scarcely had ... when** and **No sooner had ... than** follow the same order.

> **Watch:** No sooner goes with **than**. Hardly and scarcely go with **when**. Never mix them.

### If-sentences
- **Type 1 (real future):** If + simple present, then will + V1. *If it rains, we will stay in.* "Will" never goes in the if-part.
- **Type 3 (past that did not happen):** *Had I known*, then **would have + V3**. *Had I known, I would have helped.*

### -ing, to + verb, or the plain verb
The word before the blank often fixes the form.

| Word before the blank | Form | Example |
|---|---|---|
| enjoy, avoid, deny, mind, finish, suggest | V-ing | he denied **taking** the file |
| want, decide, agree, refuse, hope, plan | to + V1 | she refused **to sign** |
| any preposition (in, on, of, without) | V-ing | insisted on **paying** |
| had better, would rather, let, make | V1 | you had better **leave** |
| look forward to, be used to, object to | V-ing | I look forward to **hearing** from you |

- **used to + V1** is a past habit: *He used to swim.*
- **be used to + V-ing** means "accustomed to": *He is used to swimming.*
- Negative forms: **not to + V1** and **not + V-ing**.

> **Tip:** Ask who owns the "to". If a phrase like look forward to or object to owns it, use -ing. If a verb like decide or hope owns it, use the base verb.

### Agreement blanks
Sometimes the blank is just is / are or has / have. Then agreement decides, not tense.

- **Each of / every one of / either of / neither of** + plural noun → singular verb. *Each of the players **has** a kit.*
- **A number of** + plural → plural verb. **The number of** + plural → singular verb.
- A collective noun acting as one unit takes a singular verb: *The jury **has** reached its verdict.*

### Remove wrong options in order
1. Remove forms that clash with the time word (a present form next to "yesterday").
2. Remove forms that break a fixed pattern ("will" in an if-part, "to" after deny).
3. Remove agreement errors ("have" after "each of").
4. From what is left, choose ongoing (has been working) or finished (has worked) to suit the sentence.
""",
    tricks=[
        {"title": "Who owns the 'to'?",
         "body": "If 'to' belongs to a phrase like look forward to or object to, it is a preposition, so use -ing. If it belongs to a verb like decide or hope, use the base verb.",
         "example": {"q": "I look forward to ___ from you soon.",
                     "steps": ["'Look forward to' owns the 'to'.", "You can say 'look forward to it', so 'to' is a preposition.",
                               "A preposition takes the -ing form."],
                     "answer": "hearing"}},
        {"title": "The by-the-time ladder",
         "body": "With 'by the time' and two past events, the earlier event takes had + V3 and the later one takes simple past. Put the blank on its step of the ladder."},
        {"title": "Three short verb lists",
         "body": "Learn three lists. -ing after: avoid, enjoy, mind, suggest, finish. to + verb after: decide, hope, refuse, plan. Plain verb after: had better, would rather, let, make."},
    ],
    mistakes=[
        mis("Writing 'to hear' after 'look forward to'.", "That 'to' is a preposition: look forward to hearing."),
        mis("Using the present perfect with a finished time (has gone yesterday).", "With yesterday, last week or in 2010, use the simple past: went."),
        mis("Writing 'used to + -ing' for a past habit.", "Past habit = used to + V1 (used to swim). Be used to + -ing means 'accustomed'."),
        mis("Putting 'will' in the if-part of a type 1 sentence.", "If + simple present, will + V1: If it rains, we will stay."),
        mis("Making the verb agree with the nearest plural noun after 'each of'.", "Each of / neither of + plural noun still takes a singular verb."),
        mis("Using an active form when the subject receives the action.", "Use the passive: the building had been evacuated."),
    ],
    revision=[
        "Circle the time words first; they pick the tense.",
        "since / for (still going) → has + V3 or has been + V-ing.",
        "Two past events → earlier had + V3, later simple past.",
        "No sooner ... than; hardly / scarcely ... when.",
        "If + present, will + V1. Had I known → would have + V3.",
        "deny / enjoy / avoid + V-ing; decide / refuse / hope + to + V1; preposition + V-ing.",
        "had better / would rather / let / make + V1.",
        "each of / neither of → singular verb; a number of → plural; the number of → singular.",
    ],
    patterns=[
        pat("fbt1", "since / for with perfect tenses", "very common",
            "The sentence has since 2019, for a decade or all morning. The options mix simple present, present perfect and past perfect.",
            ["Spot 'since' or 'for'.", "If the action is still going, use has / have been + V-ing.",
             "If only the completed amount matters, use has / have + V3.", "If the whole frame is in the past, move back to had + V3."],
            "Since and for mark the perfect tenses, and the options differ only in tense.",
            "He ___ in this office since 2019.",
            ["'Since 2019' shows the action began then.", "He is still working there, so the action is ongoing.",
             "Use the present perfect continuous."],
            "has been working"),
        pat("fbt2", "Past perfect + simple past", "very common",
            "The sentence has Hardly had ... when, or two past events joined by before / when. The blank is the second verb.",
            ["Find the had + V3 event; it is the earlier one.", "Give the later event the simple past.",
             "Reject had + V3 for the later event."],
            "The past perfect only marks the earlier of two past events, so it cannot be used for both.",
            "The guests had hardly settled when the lights ___ out.",
            ["'Had settled' is the earlier event.", "The lights going out came later.", "Later event = simple past: went."],
            "went"),
        pat("fbt3", "If-sentences", "common",
            "The sentence starts with 'If' or with an inverted 'Had I ...'. Options put 'will' in the if-part or mix would / would have.",
            ["Identify the type: real future (type 1) or a past that did not happen (type 3).",
             "Type 1: If + simple present, main part will + V1.", "Type 3: Had + subject + V3, main part would have + V3."],
            "Each type is a fixed two-part pattern, and the wrong options come from another type.",
            "Had I known about the schedule change, I ___ accordingly.",
            ["'Had I known' means 'If I had known', a past that did not happen.", "That is type 3.",
             "The main part takes would have + V3."],
            "would have planned"),
        pat("fbt4", "-ing or to + verb after a fixed verb", "very common",
            "The blank follows a verb like deny, enjoy, avoid, suggest, or want, decide, refuse, hope. The options are 'to + V1' and 'V-ing'.",
            ["Read the verb just before the blank.", "-ing group: enjoy, avoid, deny, suggest, mind, finish, and every preposition.",
             "to + verb group: want, decide, agree, refuse, hope, plan."],
            "The first verb decides the form of the second, so no meaning test is needed.",
            "He denied ___ the confidential file.",
            ["The verb before the blank is 'denied'.", "Deny takes the -ing form.", "'Denied to take' is the planted wrong option."],
            "taking"),
        pat("fbt5", "Agreement blanks (each of, the number of)", "common",
            "The subject is each of / either of / the number of + a plural noun, and the options are has / have or is / are.",
            ["Find the main word of the subject: each, either, the number.", "These are singular, so pick has / is / was.",
             "Remember: a number of + plural noun takes a plural verb."],
            "The plural noun is a distraction; the verb agrees with the main word.",
            "Each of the shortlisted candidates ___ to bring the original certificates.",
            ["The main word is 'each', which is singular.", "'Candidates' is only part of the phrase 'of the candidates'.",
             "Singular verb: has."],
            "has"),
        pat("fbt6", "used to / be used to / had better", "common",
            "The blank follows used to, is used to, had better or would rather. The options mix V1, V-ing and to + V1.",
            ["used to (past habit) → V1.", "be used to (accustomed) → V-ing.", "had better / would rather → V1 without 'to'."],
            "Each of these phrases takes one fixed form, so spotting the phrase gives the answer.",
            "After ten years in Shimla, she is used to ___ in the cold.",
            ["The phrase is 'is used to', meaning 'accustomed to'.", "Here 'to' is a preposition.", "So the -ing form follows."],
            "working"),
        pat("fbt7", "by + future time", "occasional",
            "The sentence has 'by next month', 'by 2030' or 'by the time you arrive'. The options mix will + V1 and will have + V3.",
            ["Spot 'by' + a future time.", "The action will be complete before that time.", "Use will have + V3."],
            "'By' a future point means finished before it, which is the future perfect.",
            "By next March, the workers ___ the new flyover.",
            ["'By next March' is a future deadline.", "The work will be complete before then.", "Use the future perfect."],
            "will have completed"),
    ],
)

# =====================================================================
# 4. Connectives and pronouns
# =====================================================================
SUBS["fb-connectives-pronouns"] = dict(
    concept=(
        "A *connective* is a joining word like *although*, *because* or *therefore*. "
        "The blank asks how two parts of a sentence are linked: contrast, cause, result, addition or time. "
        "Relative pronouns like *who*, *whom* and *which* join a describing part to a noun."
    ),
    notes=r"""### Name the link first
Both sides of the blank are complete. The blank only shows how they are linked.

> **Example:** *___ he had practised for weeks, he forgot his lines.* The second part goes against the first, so the link is contrast. Answer: **Although**.

Give each part a direction. Same direction → *and, so, therefore*. Opposite direction → *but, yet, although*. Second part explains the first → *because, since*.

### Words that come in pairs
When the sentence shows one half of a pair, the other half is fixed.

| Pair | Example | Wrong partner |
|---|---|---|
| No sooner ... than | No sooner had he sat down **than** the phone rang. | when |
| Hardly / Scarcely ... when | Hardly had she entered **when** the lights went out. | than |
| Not only ... but also | not only cheap **but also** strong | but, and |
| Both ... and | **Both** the manager **and** his staff were present. | as well as |
| Either ... or; Neither ... nor | **Neither** he **nor** I | or with neither |
| Rather ... than | He would resign **rather than** apologise. | then |
| too ... to | **too** weak **to** walk | so, very |
| so / such ... that | **so** weak **that** he could not walk | too |
| as ... as; between ... and; from ... to | **as** tall **as**; **between** you **and** me | |
| Lest ... should | Run fast **lest** you **should** miss the bus. | or else |

### Contrast and cause: check what follows
Many wrong options are right in meaning but wrong in grammar. Look at what comes after the blank.

| Word | What follows | Example |
|---|---|---|
| although / though / even though | a full clause | although it rained |
| despite / in spite of | a noun or -ing | despite the rain |
| because | a full clause | because it rained |
| because of / owing to / due to | a noun | because of the rain |

> **Watch:** *Despite it rained* and *although the rain* are both wrong.

Although never pairs with *but*. Older books allow *yet* in the second part; a plain comma is always safe.

### Linking words between sentences
- **however**: contrast; use it after a full stop or a semicolon.
- **therefore / hence / consequently**: a result or conclusion.
- **moreover / besides**: one more point.
- **otherwise**: what happens if not.

### Relative pronouns

| Noun and its job in the clause | Pronoun | Example |
|---|---|---|
| person who does the action | who | the leader **who** inspires us |
| person who receives the action | whom | the leader **whom** everyone trusts |
| owner of something | whose | a girl **whose** bag was lost; a house **whose** roof leaks |
| thing | which / that | the book **which** / **that** I lent you |
| place / time / reason | where / when / why | the town **where** I grew up |
| "the thing that" (no noun before) | what | tell me **what** you need |

> **Tip:** Rewrite the clause with he or him. "Everyone trusts **him**" → **whom**. "**He** inspires us" → **who**.

After a comma, use *which* or *who*; *that* never follows a comma.

### Myself, themselves, each other
- Use a reflexive (myself, themselves) when the doer and receiver are the same: *The children decorated the hall **themselves**.*
- Use **each other / one another** when two sides act on each other.
- *Theirselves, themself* and *hisself* are not standard English.
""",
    tricks=[
        {"title": "Find the other half of the pair",
         "body": "Scan the sentence for the first half of a pair. 'Hardly had' fixes the blank as 'when'. 'No sooner had' fixes it as 'than'.",
         "example": {"q": "Hardly had she entered the room ___ the lights went out.",
                     "steps": ["The sentence starts with 'Hardly had'.", "Hardly pairs with 'when'.",
                               "'Than' belongs to 'No sooner'."],
                     "answer": "when"}},
        {"title": "He / him test for who / whom",
         "body": "Rewrite the clause as a sentence. If 'he' fits, use who. If 'him' fits, use whom."},
        {"title": "Clause or noun after the blank?",
         "body": "A full clause (subject + verb) after the blank needs although / though. A noun or -ing form needs despite / in spite of."},
    ],
    mistakes=[
        mis("Choosing 'than' after Hardly or Scarcely.", "Hardly / Scarcely go with 'when'; only No sooner goes with 'than'."),
        mis("Using 'whom' as the subject of the clause ('the man whom came').", "The subject of the clause is 'who': the man who came."),
        mis("Putting a full clause after 'despite' or a bare noun after 'although'.", "despite + noun (despite the rain); although + clause (although it rained)."),
        mis("Using 'which' for a person or 'who' for a thing.", "who / whom for people; which / that for things."),
        mis("Using 'that' after a comma.", "After a comma, use which (things) or who (people)."),
    ],
    revision=[
        "Name the link first: contrast, cause, result, addition or time.",
        "No sooner ... than; hardly / scarcely ... when; not only ... but also; both ... and.",
        "too + adjective + to + V1; so + adjective + that + clause; lest ... should.",
        "although + clause; despite / in spite of + noun or -ing.",
        "because + clause; because of / owing to / due to + noun.",
        "who does, whom receives, whose owns; which after a comma, never that.",
        "themselves, not theirselves; each other for two sides acting on each other.",
    ],
    patterns=[
        pat("fbn1", "No sooner ... than / Hardly ... when", "very common",
            "The sentence begins with No sooner had, Hardly had or Scarcely had. The blank is the second half; options are than, when, then, that.",
            ["Read the first half.", "No sooner → than. Hardly / Scarcely → when.", "Reject 'then' and 'that'; they are never partners here."],
            "These pairs are fixed; every other option belongs to a different pattern.",
            "No sooner had the bell rung ___ the students rushed out.",
            ["The first half is 'No sooner had'.", "Its fixed partner is 'than'.", "'When' belongs to hardly / scarcely."],
            "than"),
        pat("fbn2", "Relative pronoun (who / whom / whose / which)", "very common",
            "The blank joins a noun to a describing clause. The options are who, whom, whose, which, that.",
            ["Find the noun before the blank: person or thing?", "Find the pronoun's job in the clause: doer, receiver or owner.",
             "Doer → who (people) / which (things). Receiver → whom. Owner → whose."],
            "Rewriting the clause as a small sentence shows the pronoun's job at once.",
            "The engineer ___ designed the bridge won a national award.",
            ["The noun is 'engineer', a person.", "The engineer designed the bridge, so he is the doer.", "Doer + person = who."],
            "who"),
        pat("fbn3", "Contrast and cause words", "very common",
            "Two full clauses sit on either side of the blank. The options are although, because, therefore, however and similar words.",
            ["Label the link: the second part goes against the first (contrast), explains it (cause) or follows from it (result).",
             "Contrast + clause → although / though. Cause → because. Result → therefore / so.",
             "Check the grammar after the word: despite needs a noun, not a clause."],
            "Once both parts are read, the link is clear, and each option stands for one link.",
            "___ he had rehearsed for weeks, he forgot his lines on stage.",
            ["Rehearsing should help, but he still forgot: contrast.", "A full clause follows the blank.", "Contrast + clause = Although."],
            "Although"),
        pat("fbn4", "Possessive and reflexive pronouns", "common",
            "The options differ by an apostrophe or ending: whose / who's, its / it's, themselves / theirselves.",
            ["If a noun follows and shows ownership, use whose or its (no apostrophe).",
             "Expand who's to 'who is' and it's to 'it is' and test.", "Same doer and receiver → themselves, myself (never theirselves or hisself)."],
            "The apostrophe forms sound the same, so expanding them settles the choice.",
            "The athlete, ___ dedication is well known, trains at dawn.",
            ["'Dedication' belongs to the athlete, so we need ownership.", "Whose shows ownership.",
             "'Who's dedication' would mean 'who is dedication', which makes no sense."],
            "whose"),
        pat("fbn5", "despite / although: check what follows", "common",
            "The blank starts a contrast. What comes after the blank is either a noun phrase or a full clause.",
            ["Look at the words after the blank.", "Noun phrase or -ing → despite / in spite of.", "Full clause (subject + verb) → although / though / even though."],
            "The two families mean the same; only the grammar after them differs.",
            "___ the heavy downpour, the match went on.",
            ["'The heavy downpour' is a noun phrase with no verb.", "A noun phrase takes despite or in spite of.",
             "Although would need a clause: 'although it rained heavily'."],
            "Despite"),
        pat("fbn6", "however / therefore / moreover / otherwise", "common",
            "The blank starts a new sentence or follows a semicolon. The options are linking words such as however, therefore, moreover, otherwise.",
            ["Read the sentence before the blank and the one after it.", "Label the link: contrast, result, one more point, or 'if not'.",
             "Pick however (contrast), therefore (result), moreover (addition) or otherwise (if not)."],
            "These words link whole sentences, and each one carries a single type of link.",
            "Carry an umbrella; ___, you will get wet on the way.",
            ["The second part says what happens if you do not carry an umbrella.", "'If not' = otherwise.",
             "However would signal contrast, which does not fit."],
            "otherwise"),
        pat("fbn7", "lest ... should", "occasional",
            "The sentence contains 'lest', and the blank comes after the subject that follows it. The options include should, will, would, not.",
            ["Spot 'lest' (meaning 'so that ... not').", "Use 'should' + V1 after the subject.", "Do not add 'not'; lest is already negative."],
            "Lest carries its own 'not', and standard exam grammar pairs it with should.",
            "Walk carefully lest you ___ slip on the wet floor.",
            ["'Lest' means 'so that you do not'.", "It takes should + V1.", "'Should not slip' would make a double negative."],
            "should"),
    ],
)

# =====================================================================
# 5. Confusables
# =====================================================================
SUBS["fb-homonyms-confusables"] = dict(
    concept=(
        "Some words look or sound almost the same but mean different things, like *advice* and *advise*. "
        "The options give you such a pair or group. "
        "First find what kind of word the blank needs (noun, verb or adjective). Then choose by meaning."
    ),
    notes=r"""### Two steps: word type, then meaning
Confusable blanks give words that differ by one letter or one sound.

> **Example:** *The doctor gave me sound ___.* After "sound" we need a noun. **advice** is the noun; **advise** is the verb.

1. **Word type.** Does the blank need a noun, a verb or an adjective? If the sentence already has its verb, the blank is often a noun.
2. **Meaning.** If two options are the same word type, ask what the sentence must say. Find the clue word.

> **Rule:** After a, the, his or an adjective → noun. After to, will, did or a subject → verb.

### Noun and verb twins
In British and Indian spelling, many pairs end in **-ce** for the noun and **-se** for the verb.

| Noun | Verb | Example |
|---|---|---|
| advice | advise | follow his **advice**; doctors **advise** rest |
| practice | practise | daily **practice** helps; **practise** daily |
| licence | license | a driving **licence**; **licensed** premises |
| belief / proof | believe / prove | a strong **belief**; **prove** it |
| bath | bathe | take a **bath**; **bathe** the child |
| effect (result) | affect (influence) | the **effect** was clear; rains **affect** crops |

*Effect* can also be a verb meaning "bring about" (effect a change). *Advice* has no plural; "advices" is wrong.

### Meaning twins

| Word | Meaning | Word | Meaning |
|---|---|---|---|
| lose | misplace, fail to win | loose | not tight |
| stationary | not moving | stationery | paper, pens |
| principal | chief, head; also the loan amount | principle | a rule or belief |
| complement | completes | compliment | praise |
| discreet | careful | discrete | separate |
| eligible | qualified | illegible | cannot be read |
| beside | next to | besides | in addition to |
| censure | formal rebuke | censor | ban or cut content |
| continual | repeated, with breaks | continuous | without a break |
| practical | useful in practice | practicable | workable |
| personnel | staff | personal | private |

> **Tip:** stationERy = papER. principLE = ruLE.

### Groups of three
- **site** (place), **sight** (vision), **cite** (quote): a building *site*, at first *sight*, *cite* a case.
- **allusion** (reference), **illusion** (false picture), **elusion** (escape).
- **assure** a person (remove doubt), **ensure** a result (make certain), **insure** a thing (buy a policy). The noun of assure is *assurance*: a solemn *assurance*.
- **lie** (recline): lie, lay, lain. **lay** (put something down): lay, laid, laid. *Lie down*; *lay the pen on the table*.

### Decoys that are not real words
Some options are wrong forms: *advices*, *affection* in place of *effect*, *effectively* in place of *effect*. Remove them by grammar first, then by meaning.

### Why these are easy marks
Only one word of each pair means what the sentence needs. Read carefully once. Find the clue word (shop, head, rule, praise, rebuke) before you look at the options.
""",
    tricks=[
        {"title": "Word type first, meaning second",
         "body": "Decide noun, verb or adjective from the sentence. Remove every option of the wrong type. Usually only two options are left for the meaning check.",
         "example": {"q": "The doctor ___ him to take complete rest. (advised / advice / advices / advise)",
                     "steps": ["The sentence has no other verb, so the blank is a past-tense verb.",
                               "Advice is a noun and 'advices' is not standard.", "Advise is present tense; the sentence is in the past."],
                     "answer": "advised"}},
        {"title": "Picture the sentence",
         "body": "Make a quick mental picture. A shop full of paper and pens → stationery. A parked van → stationary."},
        {"title": "Learn the groups of three",
         "body": "Make flash cards for groups: assure / ensure / insure, site / sight / cite, allusion / illusion / elusion. These appear together in options."},
    ],
    mistakes=[
        mis("Choosing the more familiar 'affect' when the slot needs a noun.", "After a / an / the, use the noun 'effect'."),
        mis("Treating advice and advise as the same word.", "advice = noun, advise = verb. Check the slot."),
        mis("Picking 'illegible' when the sentence is about being qualified.", "Qualified = eligible. Illegible = cannot be read."),
        mis("Missing that the sentence already has its verb.", "If the verb is already there, the blank is usually a noun."),
        mis("Choosing a form that does not exist, such as 'advices'.", "Advice has no plural. Remove non-standard forms first."),
    ],
    revision=[
        "Word type first (noun / verb / adjective), then meaning.",
        "advice, practice, licence = nouns; advise, practise, license = verbs.",
        "affect = verb (influence); effect = noun (result).",
        "lose = misplace; loose = not tight. stationary = still; stationery = paper.",
        "principal = chief or head; principle = rule. complement completes; compliment praises.",
        "assure a person, ensure a result, insure a thing.",
        "censure = rebuke; censor = ban. continual = with breaks; continuous = unbroken.",
    ],
    patterns=[
        pat("fbh1", "Noun and verb twins (-ce / -se)", "very common",
            "The options are advice / advise, practice / practise or licence / license. Look at the word just before the blank.",
            ["Decide the word type: after a / the / an adjective → noun; after to / a subject → verb.",
             "Pick the matching twin: advice (noun), advise (verb).", "Read the phrase back: 'sound advice', 'advise someone'."],
            "The twins sound alike and differ only in word type, which the neighbouring word shows.",
            "The dietician gave me sound ___ on portion control.",
            ["'Sound' is an adjective, so a noun follows.", "The noun is 'advice'.", "'Advise' is a verb and cannot follow an adjective."],
            "advice"),
        pat("fbh2", "lose / loose and affect / effect", "very common",
            "The sentence is about misplacing, tightness, influence or results. The options are the look-alikes plus related words.",
            ["lose = fail to keep; loose = not tight.", "affect = verb (influence); effect = noun (result).",
             "Will / can before the blank → verb; a / an / the before it → noun."],
            "These pairs are one letter apart, so the word before the blank must decide.",
            "The new timings will ___ train schedules across the zone.",
            ["'Will' is followed by a verb.", "The meaning is 'influence'.", "The verb for influence is 'affect'."],
            "affect"),
        pat("fbh3", "stationary / stationery and principal / principle", "common",
            "The sentence is about an office, a shop, movement, rules or the head of an institution. The options are the twin spellings.",
            ["Paper and pens → stationery. Not moving → stationary.", "Rule or belief → principle. Head, chief or loan amount → principal.",
             "Use the memory hooks: stationERy = papER; principLE = ruLE."],
            "The twins differ by one letter but have unrelated meanings; the clue word forces the choice.",
            "The office buys its ___ from the shop near the station.",
            ["An office buys paper and pens.", "Paper and pens = stationery.", "Stationary means 'not moving'."],
            "stationery"),
        pat("fbh4", "censure / censor and allusion / illusion", "common",
            "The sentence is about parliament, films, books, references or appearances. The options are these look-alikes.",
            ["Formal rebuke → censure. Ban or cut content → censor.", "Reference → allusion. False picture → illusion. Escape → elusion.",
             "Match the clue word (House, film, poem, mirage) to the meaning."],
            "Both pairs are formal words, so only the exact meaning separates them.",
            "The House ___ the minister for his careless remark.",
            ["The House scolded the minister formally.", "A formal rebuke = censure.", "Censor is for films and books, not for people's conduct."],
            "censured"),
        pat("fbh5", "assure / ensure / insure", "common",
            "The options are assure, ensure and insure (or their nouns). The sentence is about promises, results or insurance.",
            ["Is a person being told not to worry? → assure.", "Is a result being made certain? → ensure.",
             "Is a thing covered by a policy? → insure."],
            "All three sound alike, but each has its own object: a person, a result or a thing.",
            "Please ___ that all windows are shut before you leave the lab.",
            ["The sentence asks you to make a result certain.", "Make certain = ensure.", "Assure needs a person; insure needs a policy."],
            "ensure"),
        pat("fbh6", "continual / continuous and practical / practicable", "occasional",
            "The options are adjective pairs with the same root: continual / continuous, practical / practicable, personal / personnel.",
            ["continual = repeated with breaks; continuous = without a break.", "practical = useful in real life; practicable = workable, can be done.",
             "personal = private; personnel = staff."],
            "The shared root makes the pair look equal; the exact meaning in the sentence decides.",
            "The ___ hum of the generator kept us awake all night.",
            ["The hum did not stop even once.", "Without a break = continuous.", "Continual would mean it stopped and started again."],
            "continuous"),
        pat("fbh7", "beside / besides and lie / lay", "occasional",
            "The options are beside / besides, or forms of lie and lay (lie, lay, lain, laid).",
            ["beside = next to; besides = in addition to.", "lie (recline): lie, lay, lain. lay (put down): lay, laid, laid.",
             "If there is an object being put somewhere, use lay."],
            "Each word in the pair has one meaning, and the sentence always shows which.",
            "___ English, she can speak Tamil and Bengali.",
            ["The sentence adds more languages to English.", "In addition to = besides.", "Beside means 'next to'."],
            "Besides"),
    ],
)

# =====================================================================
# 6. Double blanks
# =====================================================================
SUBS["fb-double-blanks"] = dict(
    concept=(
        "Some questions have two blanks in one sentence. Each option gives a pair of words, one for each blank. "
        "Fill the easier blank first. The wrong pairs then drop out, and you test the last one or two pairs in both blanks."
    ),
    notes=r"""### Two blanks, one choice
The options are complete pairs, such as *both ... and* or *null and void*. You must test the whole pair in the sentence.

> **Example:** *The room was ___ small ___ hold all the guests.* After the second blank comes a plain verb (hold). Only **too ... to** fits: *too small to hold*.

A pair can fit the first blank and fail the second. That is exactly where the trap sits.

### Fill the easier blank first
One blank is usually much easier. It may be half of a fixed pair, or a word only one option can fit.

1. Decide the easy blank.
2. Remove every pair that does not match it.
3. Test what is left in both blanks.
4. Read the whole sentence aloud. If the second half sounds wrong, your first choice was the trap.

### Pairs fixed by the verb
With joining pairs, the verb in the sentence often decides alone.

| Pair | Verb | Example |
|---|---|---|
| Both ... and | plural | **Both** the pilot **and** the co-pilot **were** honoured. |
| Either ... or / Neither ... nor | agrees with the nearer subject | **Neither** the boys **nor** the coach **was** told. |
| Not only ... but also | the second part adds new information | **not only** fast **but also** safe |

> **Tip:** Read the verb that is not blanked. "Were honoured" points to both ... and. "Was told" points to either or neither.

### Structure pairs
- **too** + adjective + **to** + V1: *too tired to walk*.
- **so** + adjective + **that** + clause: *so tired that she could not walk*.
- **such** + noun + **that** + clause: *such a noise that nobody slept*.
- **Hardly / Scarcely ... when**; **No sooner ... than**. These never cross.
- **from ... to** marks a range: *from Monday to Friday*. **between ... and** links exactly two items.

> **Watch:** *From* never pairs with *and*. *Between* never pairs with *to*.

### Pairs fixed by meaning
Some pairs are chosen by sense, not grammar. The words after the second blank usually confirm the meaning. So read to the full stop before you choose.

*___ his age ___ his poor health could stop him; he finished the marathon.* The ending shows nothing stopped him, so **Neither ... nor** fits.

### Two-word fixed expressions
These are single ideas written as two words joined by *and*. Learn them as pairs, never one half.

| Expression | Meaning |
|---|---|
| null and void | no longer valid |
| part and parcel | an essential part |
| safe and sound | unhurt |
| first and foremost | most importantly |
| odds and ends | small leftover items |
| done and dusted | completely finished |
| one and all | everyone |
| ways and means | methods |
| pros and cons | points for and against |

All the options may be real expressions. Only one matches the sentence's meaning.

Among pairs that survive, pick the exact one, not the one that just sounds grand.
""",
    tricks=[
        {"title": "Spot the structure",
         "body": "Learn the skeletons: too + adjective + to + V1; so + adjective + that + clause; such + noun + that + clause; hardly ... when; no sooner ... than. Once you see the skeleton, both blanks fill at once.",
         "example": {"q": "The room was ___ small ___ accommodate all the guests.",
                     "steps": ["After the second blank comes a plain verb, 'accommodate'.",
                               "too + adjective + to + V1 fits: 'too small to accommodate'.",
                               "'So ... that' would need a clause: 'so small that it could not accommodate'."],
                     "answer": "too, to"}},
        {"title": "Let the verb decide",
         "body": "Plural verb with two subjects → Both ... and. Singular verb → Either ... or / Neither ... nor, agreeing with the nearer noun."},
        {"title": "Learn fixed expressions in pairs",
         "body": "Revise safe and sound, part and parcel, null and void, first and foremost, ways and means together. Options often join a real first half to a wrong second half."},
    ],
    mistakes=[
        mis("Solving the hard blank first.", "Start with the blank that has a fixed partner or an obvious answer."),
        mis("Choosing 'so ... that' when a plain verb follows the second blank.", "A plain verb after the blank needs 'too ... to'."),
        mis("Using 'Both ... and' with a singular verb.", "Both ... and takes a plural verb; neither / either take the verb of the nearer subject."),
        mis("Accepting a half-real expression such as 'part and half'.", "Check both halves: the expression is 'part and parcel'."),
        mis("Stopping at the second blank.", "Read to the full stop; the ending often confirms the meaning."),
    ],
    revision=[
        "Test the whole pair in both blanks, never one word alone.",
        "Fill the easier blank first, then check the other.",
        "Both ... and → plural verb; either / neither → verb agrees with the nearer subject.",
        "too + adjective + to + V1; so + adjective + that + clause.",
        "from ... to; between ... and; no sooner ... than; hardly ... when.",
        "null and void, part and parcel, safe and sound, first and foremost: fixed pairs.",
    ],
    patterns=[
        pat("fbd1", "Both / either / neither pairs", "very common",
            "Two blanks surround two nouns, and one verb is visible. The options are both ... and, either ... or, neither ... nor, not only ... but also.",
            ["Check the visible verb: plural → both ... and; singular → either / neither.",
             "Check the meaning: none of them → neither ... nor; one of them → either ... or.",
             "Read the ending if two pairs still fit."],
            "The pair decides the verb's number, so the visible verb often gives the answer.",
            "___ the pilot ___ the co-pilot were honoured for the emergency landing.",
            ["The verb 'were honoured' is plural.", "A plural verb goes with 'both ... and'.",
             "Neither / either would need 'was' here."],
            "Both, and"),
        pat("fbd2", "Two-word fixed expressions", "common",
            "The options are whole expressions (null and void, part and parcel, safe and sound). The sentence is about validity, importance or safety.",
            ["Name the sentence's message: cancelled, essential, unhurt or finished.",
             "Match it: null and void; part and parcel; safe and sound; done and dusted.",
             "Reject real expressions that mean something else."],
            "Every option is a real expression, so only meaning separates them.",
            "The old agreement was declared ___ after the merger.",
            ["The agreement stopped being valid.", "No longer valid = null and void.", "Part and parcel would mean the agreement is essential."],
            "null and void"),
        pat("fbd3", "from ... to and between ... and", "common",
            "The sentence gives a time range or links exactly two parties. The options are preposition pairs.",
            ["A start and an end → from ... to.", "Exactly two parties → between ... and.", "Reject mixed pairs such as from ... and or between ... to."],
            "These pairs are fixed by usage; the wrong options mix partners that never go together.",
            "The summer sale runs ___ 1 May ___ 15 May.",
            ["1 May is the start and 15 May is the end.", "A range takes 'from ... to'.", "'Between ... to' mixes two pairs."],
            "from, to"),
        pat("fbd4", "No sooner ... than / Hardly ... when", "common",
            "The sentence starts with a blank followed by 'had'. The options pair no sooner, hardly or scarcely with than, when or then.",
            ["No sooner → than. Hardly / Scarcely → when.", "Reject any pair with 'then' or 'that'.",
             "Check the tenses: had + V3 first, simple past second."],
            "The pair is learnt as one unit, and the options only test whether you know it whole.",
            "___ had the plane touched down ___ the passengers began clapping.",
            ["The options mix no sooner and hardly with than and when.", "Correct pairs are 'No sooner ... than' and 'Hardly ... when'.",
             "Only 'No sooner, than' appears as a correct pair among the options."],
            "No sooner, than"),
        pat("fbd5", "too ... to and so ... that", "common",
            "Two blanks sit around an adjective. Look at what follows the second blank: a plain verb or a full clause.",
            ["Plain verb after the second blank → too ... to.", "Full clause (subject + verb) → so ... that.",
             "Noun after the first blank → such ... that."],
            "The words after the second blank show which structure the sentence is built on.",
            "The tea was ___ hot ___ I could not drink it at once.",
            ["After the second blank comes a full clause: 'I could not drink it'.", "A clause needs 'so ... that'.",
             "'Too ... to' would need a plain verb: 'too hot to drink'."],
            "so, that"),
        pat("fbd6", "Two content words with a contrast or link", "common",
            "Both blanks need meaning words (adjectives, nouns or verbs). A word like but, though or and joins the two parts.",
            ["Find the joining word: but / though means the two blanks go opposite ways; and means the same way.",
             "Fill the blank with a clearer clue first.", "Check that the second word of the pair has the right direction."],
            "The joining word tells you whether the pair should agree or contrast, which removes most options.",
            "The speech was ___, but the minister's actions were ___. (a) bold, timid (b) bold, brave (c) timid, cautious (d) short, brief",
            ["'But' shows the two blanks must contrast.", "Only 'bold, timid' is a pair of opposites.",
             "The other pairs are similar in meaning."],
            "bold, timid"),
    ],
)


# ---------------------------------------------------------------------
def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


data = json.loads(TOPIC.read_text(encoding="utf-8"))
assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
for sub in data["subtopics"]:
    new = SUBS[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in new["patterns"]]
    assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
    assert len(new_ids) == len(set(new_ids))
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sub["id"], len(n))
    assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
    for p in new["patterns"]:
        assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:80])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
