"""Readable rewrite of English > Active & Passive Voice (all 5 subtopics).

Plain English, short sentences, tables for the tense rows, one method per question type.
Every example is a true grammar fact. Old pattern ids are kept; new ids continue each prefix.
Run: python active_passive.py  (patches content/core/topics/english/active-passive.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "active-passive.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Voice basics
# =====================================================================
SUBS["ap-basics"] = dict(
    concept=(
        "In the **active voice** the subject does the action. In the **passive voice** the subject receives it. "
        "Three moves turn any active sentence into a passive one: the object becomes the subject, "
        "the verb becomes *be + V3*, and the old subject goes behind *by*. "
        "Only verbs that take an object can be made passive."
    ),
    notes=r"""### What voice means
Voice tells you who is in front: the doer or the receiver.

- **Active:** *The chef prepared the meal.* The chef (doer) is the subject.
- **Passive:** *The meal was prepared by the chef.* The meal (receiver) is the subject.

Both sentences describe the same event. Only the order changes.

### The three moves
Use these moves for every conversion. Take *The postman rings the bell.*

1. **Object becomes subject.** Find the thing the verb acts on. *The bell* is the new subject.
2. **Verb becomes be + V3.** V3 is the past participle (written, prepared, rung). Keep the tense. *Rings* is simple present, so use *is*: *is rung*.
3. **Old subject goes behind by.** Use the object case: *by the postman*, *by him*, *by them*.

Result: *The bell is rung by the postman.*

> **Rule:** The tense never changes. Only the helping verb (*is, was, has been*) carries it. The main verb is always V3.

If the doer is vague (*someone, people, they*), drop the by-phrase. *Someone has stolen my purse* becomes *My purse has been stolen.*

### Pronouns change case
A subject pronoun turns into an object pronoun when it moves behind *by*. An object pronoun turns into a subject pronoun when it moves to the front.

| Subject form | Object form |
|---|---|
| I, we | me, us |
| he, she | him, her |
| they | them |

> **Example:** *He helps me.* becomes *I am helped by him.* Now *me* is the subject, so it becomes *I*. And *he* is behind *by*, so it becomes *him*.

*By he* and *us were invited* are never correct.

### Only some verbs have a passive
A passive needs an object to move to the front. Verbs with no object have no passive: *sleep, arrive, die, cry, go, laugh*. *The baby slept peacefully* cannot become passive.

- A verb plus a preposition can work as one unit. *They laughed at him* becomes *He was laughed at.*
- Stative verbs (*have, own, resemble, lack, suit, cost*) normally refuse the passive.

> **Watch:** Test the whole phrase, not the bare verb. *Laugh* alone fails. *Laugh at* works.

### The tense table
Learn this table as one block. Take *She writes a letter.*

| Tense | Active | Passive |
|---|---|---|
| Simple present | writes | is / are + V3 |
| Present continuous | is writing | is / are being + V3 |
| Present perfect | has written | has / have been + V3 |
| Simple past | wrote | was / were + V3 |
| Past continuous | was writing | was / were being + V3 |
| Past perfect | had written | had been + V3 |
| Simple future | will write | will be + V3 |
| Future perfect | will have written | will have been + V3 |
| Going to | is going to write | is going to be + V3 |

No row has *is been*, *will being*, or a bare V1 or V2 after *be*.

### Three checks on the options
1. **Did the tense change?** *Is written* for *wrote* is wrong. Compare the option with the table row.
2. **Is the verb after be a V3?** *Is wrote* and *must obeyed* are wrong.
3. **Is the pronoun case right?** *By he* and *us were invited* are wrong.

In a well-set question, each wrong option breaks exactly one of these checks. The right option breaks none.

> **Tip:** Say the tense row aloud first. Then read the options. Do not choose by what sounds smooth.
""",
    tricks=[
        {"title": "Tense handover",
         "body": "The helping verb must carry the original tense: wrote becomes was, writes becomes is, will write becomes will be, has written becomes has been. A changed tense in an option is a planted error.",
         "example": {"q": "Select the passive form: *The clerk wrote the report.*",
                     "steps": ["*Wrote* is simple past.", "The helping verb must be *was*.", "The main verb is V3: written."],
                     "answer": "The report was written by the clerk."}},
        {"title": "V3-only law",
         "body": "After be, been or being, the main verb is always V3 (written, given, built). Options like *is wrote* and *was build* are wrong on sight."},
        {"title": "Pronoun mirror",
         "body": "The subject pronoun becomes the object pronoun behind by (he becomes him). The object pronoun becomes the subject pronoun in front (me becomes I).",
         "example": {"q": "Select the passive form: *She helped me.*",
                     "steps": ["*Me* moves to the front, so it becomes *I*.", "*She* goes behind by, so it becomes *her*.", "*Helped* is simple past: *was helped*."],
                     "answer": "I was helped by her."}},
    ],
    mistakes=[
        mis("Changing the tense while converting, for example *is written* for *wrote*.", "Match the row: *wrote* becomes *was written*, *writes* becomes *is written*."),
        mis("Writing *by he* or *by they* in the by-phrase.", "Use the object case behind by: *by him*, *by them*."),
        mis("Writing *is wrote* or *was build* after be.", "The main verb after be is always V3: *is written*, *was built*."),
        mis("Trying to make a passive from *sleep, arrive, die, cry*.", "These verbs take no object, so they have no passive."),
        mis("Forgetting that verb + preposition can be passive: *They laughed at him*.", "Move the whole unit: *He was laughed at by them*."),
    ],
    revision=[
        "Three moves: object becomes subject; verb becomes be + V3 in the same tense; subject goes behind by.",
        "Vague doers (someone, people, they) usually disappear from the passive.",
        "he becomes him, she becomes her, they becomes them behind by. me becomes I in front.",
        "No object means no passive: sleep, arrive, die, cry.",
        "Stative verbs (have, own, resemble, lack, suit, cost) normally refuse the passive.",
        "Options break one rule each: tense, V3, being/been, or pronoun case.",
    ],
    patterns=[
        pat("apb1", "Three-move conversion with a pronoun swap", "very common",
            "A short active sentence. The options are passive versions that differ in the verb or in *by he / by him*.",
            ["Find the object and make it the subject.", "Rebuild the verb as be + V3 in the same tense.",
             "Put the old subject behind by, in the object case.", "Match is/are/was/were to the new subject."],
            "Every passive sentence uses these moves, and each wrong option botches one of them.",
            "Select the passive form: *The peon rings the bell.*",
            ["The object is *the bell*, so it becomes the subject.", "*Rings* is simple present, so use *is rung*.", "The doer goes behind by: *by the peon*."],
            "The bell is rung by the peon."),
        pat("apb2", "Vague agent drops out", "very common",
            "The active subject is someone, people, they or one. The right option has no by-phrase.",
            ["Check whether the doer is a named person or thing.", "If the doer is vague, drop it.", "Keep the tense row unchanged."],
            "English drops doers that add no information.",
            "Select the passive form: *Someone has switched off the fans.*",
            ["*Has switched off* is present perfect.", "The passive row is *have been + V3*, and the new subject *the fans* is plural.", "*Someone* is vague, so drop it."],
            "The fans have been switched off."),
        pat("apb3", "Pronoun-case elimination", "common",
            "Pronouns sit on both sides of the verb (he ... me, they ... us). The options mix I/me, he/him, we/us.",
            ["Decide each pronoun's new job.", "A pronoun moving behind by takes the object case.", "A pronoun moving to the front takes the subject case.",
             "Reject any option where either pronoun is wrong."],
            "*By he* and *me was helped* are impossible, so case alone can settle the question.",
            "Select the passive form: *They invited us to the wedding.*",
            ["*Us* moves to the front and becomes *we*.", "*They* goes behind by and becomes *them*.", "*Invited* is simple past: *were invited*."],
            "We were invited to the wedding by them."),
        pat("apb4", "Sentence that cannot be made passive", "occasional",
            "The question asks which sentence cannot be changed into the passive. The options mix verbs with and without objects.",
            ["Underline the verb in each option.", "Ask: does the verb act on a thing?", "A verb with no object (sleep, arrive, die) has no passive.",
             "Stative verbs like resemble also refuse the passive."],
            "The passive moves the object to the front. With no object, nothing can move.",
            "Which sentence cannot be changed into the passive voice? (a) *The baby slept peacefully.* (b) *The mother woke the baby.* (c) *The doctor examined the reports.* (d) *The nurse weighed the newborn.*",
            ["Option (a): *slept* has no object.", "Options (b), (c) and (d) have objects: the baby, the reports, the newborn.", "So only (a) has no passive."],
            "The baby slept peacefully."),
        pat("apb5", "Verb + preposition passive", "occasional",
            "The verb is followed by a preposition (laugh at, look after, rely on). The options move only the verb or the whole phrase.",
            ["Treat verb + preposition as one unit.", "The word after the preposition becomes the subject.", "Keep the preposition after the passive verb.",
             "Put the old subject behind by."],
            "The preposition stays with its verb, so the passive ends with it.",
            "Select the passive form: *The villagers relied on the doctor.*",
            ["*Relied on* works as one unit.", "*The doctor* becomes the subject.", "*Relied* is simple past: *was relied on*."],
            "The doctor was relied on by the villagers."),
    ],
)

# =====================================================================
# 2. Tense tables
# =====================================================================
SUBS["ap-tense-tables"] = dict(
    concept=(
        "Every voice question is one row of the tense table. First name the active tense. "
        "Then write its passive row. Then make *is/are, was/were, has/have* agree with the **new** subject. "
        "The words *being* and *been* sit in fixed places, and mixing them is the most common planted error."
    ),
    notes=r"""### One row at a time
Name the active tense. Then write the passive row for it.

| Active | Passive | Example |
|---|---|---|
| writes | is / are + V3 | *Ram writes a story.* becomes *A story is written by Ram.* |
| is writing | is / are being + V3 | *Sita is drawing a map.* becomes *A map is being drawn by Sita.* |
| has written | has / have been + V3 | *They have caught the thief.* becomes *The thief has been caught.* |
| wrote | was / were + V3 | *The cook made dinner.* becomes *Dinner was made by the cook.* |
| was writing | was / were being + V3 | *The boys were flying kites.* becomes *Kites were being flown by the boys.* |
| had written | had been + V3 | *She had finished the work.* becomes *The work had been finished by her.* |
| will write | will be + V3 | *The PM will address the nation.* becomes *The nation will be addressed by the PM.* |
| will have written | will have been + V3 | *He will have completed it.* becomes *It will have been completed.* |

### Being or been
Two small words cause many errors. Each has one fixed place.

- **Continuous tense** in the active means **being**: *is being built, was being built.*
- **Perfect tense** in the active means **been**: *has been taken, had been taken, will have been taken.*
- **Modal** (will, can, must) means plain **be**: *will be published, must be obeyed.*

> **Rule:** *Being* follows a continuous *be*. *Been* follows *have* or *had*. Never write *is been* or *will being*.

### Agree with the new subject
After you convert, the new subject decides *is/are, was/were, has/have*. The old subject no longer matters.

*They have completed the projects.* The new subject is *the projects*. So write *The projects have been completed.*

*The clerk has filed the returns.* The new subject is plural. So write *The returns have been filed by the clerk*, not *has been*.

> **Watch:** Every set of options has one choice that agrees with the old subject. Check agreement first.

### Verbs with two objects
Give, send, offer, grant, show, teach and award take two objects: a person and a thing. So they have two passives.

*The teacher gave the students homework.*

- Person first: *The students were given homework.*
- Thing first: *Homework was given to the students.*

The person-first form is usually the keyed answer. The thing-first form needs *to*. *Homework was given the students* is wrong.

### Tenses that have no passive row
Present perfect continuous (*has been writing*), past perfect continuous (*had been writing*) and future continuous (*will be writing*) have no passive row in these exams. If a question uses one, look for the nearest simple form. Do not invent *is being been written*.

### Stative verbs
*Have, own, possess, resemble, lack, suit, fit* and *cost* are normally stative. They describe a state, not an action. *A car is had by him* is not English. When a question uses one of these verbs, look for a "no passive possible" answer.
""",
    tricks=[
        {"title": "Row recall",
         "body": "Name the active tense. Then say its passive row: present continuous is is/are being + V3, past perfect is had been + V3, future is will be + V3. Each wrong option breaks one cell of the row.",
         "example": {"q": "Select the passive form: *The workers had painted the gate.*",
                     "steps": ["*Had painted* is past perfect.", "The row is *had been + V3*.", "The new subject is *the gate*."],
                     "answer": "The gate had been painted by the workers."}},
        {"title": "Agreement sweep",
         "body": "After converting, check is/are, was/were and has/have against the NEW subject before anything else."},
        {"title": "Being or been in one look",
         "body": "Continuous in the active gives being. Perfect in the active gives been. A modal gives plain be."},
    ],
    mistakes=[
        mis("Writing *is been* for a continuous passive.", "Use *is being*: *The bridge is being repaired*."),
        mis("Writing *is being* for a perfect passive.", "Use *has been*: *The bridge has been repaired*."),
        mis("Keeping the old subject's number: *The returns has been filed*.", "The new subject decides: *The returns have been filed*."),
        mis("Promoting the person and keeping the old subject: *The cook was made dinner by...*", "Move only one object to the front: *Dinner was made by the cook*."),
        mis("Dropping *to* in the thing-first passive: *Homework was given the students*.", "Write *Homework was given to the students*."),
        mis("Trying to passivise *have, own, resemble, suit*.", "These stative verbs normally have no passive."),
    ],
    revision=[
        "Perfect rows: has/have been, had been, will have been + V3.",
        "Continuous rows: is/are/was/were being + V3.",
        "Modals: modal + be + V3, with nothing between.",
        "being follows a continuous be. been follows have or had. Never is been, never will being.",
        "The new subject decides is/are, was/were, has/have.",
        "Two-object verbs: person-first passive is keyed; thing-first needs *to*.",
        "No passive row: present perfect continuous, past perfect continuous, future continuous.",
    ],
    patterns=[
        pat("apt1", "Perfect-row passives (has/had/will have been + V3)", "very common",
            "The active verb is *has written*, *had written* or *will have written*. The options differ in *been*, the helping verb or the tense.",
            ["Name the active tense: present, past or future perfect.", "Write its row: has/have been, had been, will have been + V3.",
             "Match the helping verb to the new subject.", "Keep the doer behind by, in the object case."],
            "Perfect rows are set most often, and each wrong option breaks one cell.",
            "Select the passive form: *The workers have painted the gate.*",
            ["*Have painted* is present perfect.", "The row is *has/have been + V3*.", "The new subject *the gate* is singular, so use *has*."],
            "The gate has been painted by the workers."),
        pat("apt2", "Continuous-row passives (is/are/was/were being + V3)", "very common",
            "The active verb is *is/are/was/were + V-ing*. The options mix *being*, *been* and the bare participle.",
            ["Continuous in the active means *being* in the passive.", "Match is/are or was/were to the new subject.", "Reject options that drop *being*."],
            "*Being* marks the continuous tense. Without it, the tense has changed.",
            "Select the passive form: *The masons are laying the bricks.*",
            ["*Are laying* is present continuous.", "The row is *is/are being + V3*.", "The new subject *the bricks* is plural, so use *are*."],
            "The bricks are being laid by the masons."),
        pat("apt3", "Re-agreement with the new subject", "common",
            "The active subject is plural and the object is singular, or the reverse. One option agrees with the old subject.",
            ["Move the object to the front and note its number.", "Singular subject: is, was, has. Plural subject: are, were, have.", "Then check the rest of the row."],
            "The helping verb follows its own subject, and the subject has changed.",
            "Select the passive form: *The clerk has filed all the returns.*",
            ["The new subject is *all the returns*, which is plural.", "*Has filed* is present perfect: *have been + V3*.", "*Has been filed* would agree with the old subject."],
            "All the returns have been filed by the clerk."),
        pat("apt4", "Being or been slot", "common",
            "The options are the same except for *being* and *been* (is being repaired / is been repaired).",
            ["Name the active tense: continuous or perfect.", "Continuous means being. Perfect means been. Modal means neither.", "Check that the helping verb has the same tense as the active verb."],
            "*Being* and *been* have fixed places, so swapping them is a common planted error.",
            "Select the passive form: *The engineers were repairing the bridge when we crossed.*",
            ["*Were repairing* is past continuous.", "The row is *was/were being + V3*.", "The new subject *the bridge* is singular, so use *was*."],
            "The bridge was being repaired when we crossed."),
        pat("apt5", "Two-object verb: person-first passive", "common",
            "The sentence has a person and a thing after give, grant, show, offer or award. One option starts with the person.",
            ["Find the person and the thing.", "The keyed passive moves the person to the front.", "If an option moves the thing first, it must keep *to* before the person."],
            "Both passives are correct. The setter breaks the thing-first one by deleting *to*.",
            "Select the passive form: *The principal granted Meena a scholarship.*",
            ["The person is *Meena*. The thing is *a scholarship*.", "Person first: *Meena was granted a scholarship by the principal.*", "*A scholarship was granted Meena* has no *to*, so it is broken."],
            "Meena was granted a scholarship by the principal."),
        pat("apt6", "Verbs that refuse the passive", "occasional",
            "The question asks which sentence cannot be made passive. One option uses have, own, resemble, lack or suit.",
            ["Underline each option's verb.", "Stative verbs (resemble, lack, suit, have) do not passivise.", "Verbs with a normal object do."],
            "A stative verb describes a state, so no receiver can move to the front.",
            "Which sentence cannot be changed into the passive voice? (a) *The manager signed the letter.* (b) *The girl resembles her mother.* (c) *The clerk typed the notice.* (d) *Rahul opened the door.*",
            ["*Signed, typed* and *opened* are action verbs with objects.", "*Resembles* is a stative verb.", "*Her mother resembles by the girl* is not English."],
            "The girl resembles her mother."),
    ],
)

# =====================================================================
# 3. Modals, imperatives, infinitives, questions
# =====================================================================
SUBS["ap-modals-imperatives"] = dict(
    concept=(
        "Modals (will, can, must, should) follow one row: **modal + be + V3**. "
        "Orders use **Let + object + be + V3**. Requests, advice and warnings use "
        "*You are requested / advised / warned to*. Questions start with *By whom* or move the question word to the front."
    ),
    notes=r"""### Modals have one row
Will, shall, can, could, may, might, must, should and ought to all follow **modal + be + V3**.

- *You must obey the rules.* becomes *The rules must be obeyed.*
- *They can solve it.* becomes *It can be solved.*
- *Ought to* keeps its *to*: *The bill ought to be paid.*

> **Rule:** Nothing goes between the modal and *be*. *Must being obeyed* and *must been obeyed* are wrong.

### Orders use Let
An order has no subject and starts with a base verb. Convert it with **Let + object + be + V3**.

- Order: *Shut the door.* becomes *Let the door be shut.*
- Negative order: *Do not pluck the flowers.* becomes *Let the flowers not be plucked.* You can also write *The flowers should not be plucked.*
- The verb after *be* is always V3. Write *Let the gate be opened*, never *be open* or *be opening*.

### Requests, advice and warnings
Polite words change the frame. The rest of the sentence stays the same.

| Active sentence | Passive frame | Example |
|---|---|---|
| please / kindly | You are requested to + V1 | *Please post this letter.* becomes *You are requested to post this letter.* |
| advice | You are advised to + V1 | *Give up smoking.* becomes *You are advised to give up smoking.* |
| danger, warning | You are warned not to + V1 | *Never touch the wire.* becomes *You are warned not to touch the wire.* |

> **Tip:** Please means requested. Advice means advised. Danger means warned.

### Questions come in three shapes
1. **Who as doer.** Use *By whom + auxiliary + new subject + V3*. *Who broke the window?* becomes *By whom was the window broken?*
2. **Whom or what as receiver.** The question word becomes the subject. *Whom did the manager appoint?* becomes *Who was appointed by the manager?*
3. **Yes/no question.** Put the helping verb first. *Did she sing a song?* becomes *Was a song sung by her?*

> **Watch:** Question order puts the helping verb before the subject. *By whom the window was broken?* is statement order and is wrong.

### Infinitives and gerunds
- **Infinitive:** *to write* becomes *to be written*. *I want someone to compile the report* becomes *I want the report to be compiled.*
- **Gerund:** *writing* becomes *being written*. *He likes people praising him* becomes *He likes being praised.*

After *like, hate, want* use *being* or *to be*. Never use *been* there.

### Verbs with two objects
*Give, send, offer, teach, show* and *tell* have two passives. *The guide showed the tourists the paintings* becomes:

- *The tourists were shown the paintings by the guide.* (clean)
- *The paintings were shown to the tourists.* (needs *to*)

*The paintings were shown the tourists* is broken.
""",
    tricks=[
        {"title": "Let anchor",
         "body": "An order (no subject, base verb) points to Let + object + be + V3. An option with no Let and no modal cannot be right.",
         "example": {"q": "Select the passive form: *Switch off the mobile.*",
                     "steps": ["It is an order with a base verb.", "Use Let + object + be + V3.", "*Switch off* becomes *switched off*."],
                     "answer": "Let the mobile be switched off."}},
        {"title": "By whom first",
         "body": "Who-questions become *By whom + was/were/is + new subject + V3*. Check the word order first, because options scramble it."},
        {"title": "Frame words",
         "body": "Please gives *You are requested to*. Advice gives *You are advised to*. A warning gives *You are warned not to*."},
    ],
    mistakes=[
        mis("Changing *Please help me* into *Let me be helped*.", "Use the request frame: *You are requested to help me*."),
        mis("Writing *By whom this was written?*", "Use question order: *By whom was this written?*"),
        mis("Dropping *to* in the second passive of a two-object verb: *Homework was given the students*.", "Write *Homework was given to the students*."),
        mis("Putting *being* or *been* after a modal: *must been obeyed*.", "Write modal + be + V3: *must be obeyed*."),
        mis("Writing *Let the gate be open*.", "After *be*, use V3: *Let the gate be opened*."),
    ],
    revision=[
        "Modal row: modal + be + V3. No being, no been. Ought to keeps its to.",
        "Order: Let + object + be + V3. Negative: Let ... not be ... or should not be.",
        "please: You are requested to. advice: You are advised to. danger: You are warned not to.",
        "Who question: By whom + auxiliary + new subject + V3.",
        "Whom or what question: the question word becomes the subject (Who was appointed...?).",
        "Yes/no question: helping verb first (Was a song sung by her?).",
        "to write becomes to be written. people praising becomes being praised.",
    ],
    patterns=[
        pat("apm1", "Modal + be + V3", "very common",
            "The sentence has will, can, must, should or ought to. The options add being, been or drop be.",
            ["Spot the modal and keep it unchanged.", "Use the fixed row: modal + be + V3.", "Reject options with being, been or a missing be."],
            "The modal row has no variants, so any option that changes it is wrong.",
            "Select the passive form: *You should check the receipts.*",
            ["*Should* is a modal and stays.", "Use *should be + V3*.", "The new subject is *the receipts*."],
            "The receipts should be checked."),
        pat("apm2", "Order becomes Let + object + be + V3", "very common",
            "The sentence is a bare order with a base verb and no subject. The right option starts with Let.",
            ["Spot the order (no subject, base verb).", "Write Let + object + be + V3.", "Reject options with no Let, and options with V1 or V-ing after be."],
            "Let is the standard passive frame for an order.",
            "Select the passive form: *Post this letter today.*",
            ["It is an order with a base verb.", "The object is *this letter*.", "Use Let + object + be + V3."],
            "Let this letter be posted today."),
        pat("apm3", "Negative order and warning", "common",
            "The sentence says *Do not ...* or *Never ...*. The options must keep *not* in the right place.",
            ["Decide the tone: request, advice or warning.", "Use requested / advised / warned not to + V1.", "For a bare negative order, use Let + object + not + be + V3.",
             "Put *not* before *to*: *not to smoke*."],
            "The negative travels with the frame, so options that drop the frame fail.",
            "Select the passive form: *Please do not smoke in the hall.*",
            ["It is a polite request.", "Use *You are requested not to + V1*.", "Keep the rest: *smoke in the hall*."],
            "You are requested not to smoke in the hall."),
        pat("apm4", "Request: You are requested to", "common",
            "The sentence has *please* or *kindly* and a base verb. The right option starts with *You are requested to*.",
            ["Spot please or kindly.", "Start with *You are requested to*.", "Keep the rest of the sentence word for word.", "Treat Let-forms as decoys."],
            "*Please* cannot stay in a passive clause, so the frame *requested to* replaces it.",
            "Select the passive form: *Kindly grant me a day's leave.*",
            ["*Kindly* signals a request.", "Use *You are requested to + V1*.", "Keep *grant me a day's leave*."],
            "You are requested to grant me a day's leave."),
        pat("apm5", "Question conversions (By whom / Who was)", "common",
            "The sentence ends with a question mark. A who-question needs *By whom*. A whom or what question moves the question word to the front.",
            ["Decide the question word's job: doer or receiver.", "Doer: By whom + auxiliary + new subject + V3.", "Receiver: the question word becomes the subject.",
             "Check that the helping verb comes before the subject."],
            "Most errors here are word-order errors, not verb-form errors.",
            "Select the passive form: *Who broke the window?*",
            ["*Who* is the doer, so start with *By whom*.", "*Broke* is simple past: *was + V3*.", "The new subject is *the window*."],
            "By whom was the window broken?"),
        pat("apm6", "Infinitive and gerund passives", "occasional",
            "The sentence has *to + verb* after want, or a gerund after like or hate. The options offer to be, being and been.",
            ["Infinitive: to + V1 becomes to be + V3.", "Gerund: V-ing becomes being + V3.", "Reject *been* after like or want.", "Reject options that keep the old doer."],
            "The passive marker takes the same slot the active verb held.",
            "Select the passive form: *He likes people praising him.*",
            ["*Praising* is a gerund.", "The gerund passive is *being + V3*.", "The doer *people* drops out."],
            "He likes being praised."),
        pat("apm7", "Advice and warning frames", "occasional",
            "The sentence gives advice (Give up, Avoid) or a danger warning (Never touch). The options use advised or warned.",
            ["Advice: You are advised to + V1.", "Warning about danger: You are warned not to + V1.", "Keep the rest of the sentence unchanged."],
            "The frame word matches the tone: requested, advised or warned.",
            "Select the passive form: *Never touch the live wire.*",
            ["*Never touch* is a warning about danger.", "Use *You are warned not to + V1*.", "Keep *touch the live wire*."],
            "You are warned not to touch the live wire."),
    ],
)

# =====================================================================
# 4. Passive to active
# =====================================================================
SUBS["ap-passive-to-active"] = dict(
    concept=(
        "To go back from passive to active, move the doer to the front and rebuild the tense. "
        "Read the **first helping verb**, not the participle, to find the tense. "
        "If no doer is given, use *they*. The old subject leaves in the object case."
    ),
    notes=r"""### The reverse run
The method mirrors the forward one. Move the doer to the front, rebuild the tense, and move the old subject behind the verb.

| Passive | Active |
|---|---|
| The letter was written by Sita. | Sita wrote the letter. |
| The road is being repaired. | They are repairing the road. |
| The work had been finished. | She had finished the work. |
| The results will be declared. | The board will declare the results. |
| The kite was being flown by the boy. | The boy was flying the kite. |

### Read the first helping verb
The participle never tells you the tense. Every passive row ends in V3. The first helping verb shows the tense.

| Passive | Active tense | Example |
|---|---|---|
| was/were + V3 | simple past | *was written* becomes *wrote* |
| is/are being + V3 | present continuous | *is being written* becomes *is writing* |
| was/were being + V3 | past continuous | *was being written* becomes *was writing* |
| has/have been + V3 | present perfect | *has been written* becomes *has written* |
| had been + V3 | past perfect | *had been written* becomes *had written* |
| will be + V3 | simple future | *will be written* becomes *will write* |
| will have been + V3 | future perfect | *will have been written* becomes *will have written* |
| modal + be + V3 | modal + V1 | *must be obeyed* becomes *must obey* |

> **Rule:** Being means continuous. If the passive has *being*, the active must have V-ing.

### Find the doer
- A by-phrase gives the new subject. *By Sita* becomes *Sita*. Keep the noun. Change only its place.
- No by-phrase? Use *they* (or *people*). *The thief was arrested last night* becomes *They arrested the thief last night.*
- Do not reverse the roles. *The window was broken by the cricketer* becomes *The cricketer broke the window*. It never becomes *The window broke the cricketer*.

### The old subject leaves in the object case
The old subject moves behind the verb, so a pronoun takes the object form.

- *She was praised by the teacher.* becomes *The teacher praised her.*
- *He was helped by his friends.* becomes *His friends helped him.*

> **Watch:** An option that ends *praised she* or *helped he* is wrong at once. Check the last word first.

### Continuous passives return to V-ing
*Was being + V3* is past continuous. The active must use *was/were + V-ing*.

*The path was being cleared by volunteers.* becomes *The volunteers were clearing the path.*

Two decoys are common. One returns the simple past (*cleared*) and loses the ongoing sense. The other changes the tense to present perfect. Reject both.

### Let and requested go back
- *Let the door be shut.* becomes *Shut the door.*
- *You are requested to post this letter.* becomes *Please post this letter.*

The frame word tells you the tone: requested means please, advised means advice, warned means danger.
""",
    tricks=[
        {"title": "First helping verb",
         "body": "Read only the first helping verb. Was means past. Is means present. Has or had means perfect. Will means future. Is being and was being mean continuous.",
         "example": {"q": "Select the active form: *The walls had been whitewashed by the masons.*",
                     "steps": ["*Had been + V3* is past perfect.", "The doer is *the masons*.", "Past perfect active: *had + V3*."],
                     "answer": "The masons had whitewashed the walls."}},
        {"title": "Doer hunt",
         "body": "The by-phrase gives the new subject. No by-phrase means *they*, *people* or *someone*."},
        {"title": "Object-case check",
         "body": "The last pronoun must be in the object case: *praised him*, not *praised he*. Many options fail exactly here."},
    ],
    mistakes=[
        mis("Taking *was being chased* back to *chased*.", "Keep it continuous: *were chasing*."),
        mis("Leaving the old subject in the subject slot: *The principal was praised him*.", "Move it behind the verb in the object case."),
        mis("Ending with a subject pronoun: *praised he*.", "Use the object pronoun: *praised him*."),
        mis("Changing the tense on the way back: *was written* becomes *has written*.", "Read the first helping verb. *Was* means simple past: *wrote*."),
        mis("Reversing the roles: *The window broke the cricketer*.", "The by-phrase noun is the doer: *The cricketer broke the window*."),
    ],
    revision=[
        "The doer becomes the subject. If there is no doer, use they.",
        "Read the first helping verb: was, is being, has been, had been, will be, modal be.",
        "The old subject leaves in the object case: praised her, helped him.",
        "being in the passive means V-ing in the active.",
        "modal + be + V3 goes back to modal + V1.",
        "requested means please. Let ... be ... means a bare order.",
    ],
    patterns=[
        pat("apa1", "Tense recovery from the first helping verb", "very common",
            "A passive sentence with a by-phrase. The active options differ only in tense.",
            ["Ignore the participle and read the first helping verb.", "Map it: had been to had + V3, has been to has + V3, was being to was/were + V-ing, will be to will + V1.",
             "Move the by-phrase noun to the subject slot.", "Put the old subject after the verb."],
            "Every passive row ends in V3, so only the helping verb shows the tense.",
            "Select the active form: *The walls had been whitewashed by the masons.*",
            ["*Had been + V3* is past perfect.", "The doer is *the masons*.", "Past perfect active: *had + V3*."],
            "The masons had whitewashed the walls."),
        pat("apa2", "Missing doer: supply they", "common",
            "The passive has no by-phrase. The right option starts with *They* and keeps the tense.",
            ["Check that there is no by-phrase.", "Put *they* in front of the rebuilt verb.", "Move the passive subject to the object slot."],
            "Passives often hide a vague doer. *They* is the usual stand-in.",
            "Select the active form: *The results will be declared on Monday.*",
            ["*Will be + V3* is simple future.", "There is no doer, so use *they*.", "Active: *will + V1*."],
            "They will declare the results on Monday."),
        pat("apa3", "Object-case pronoun at the end", "common",
            "The passive subject is a pronoun (he, she, they, we). The options end with the pronoun in both cases.",
            ["Move the by-phrase noun to the front and rebuild the tense.", "The old subject pronoun leaves in the object case: him, her, them, us.",
             "Scan the last word of each option first."],
            "This is the mirror of the forward pronoun swap.",
            "Select the active form: *She was praised by the teacher.*",
            ["*Was praised* is simple past.", "The teacher is the doer.", "*She* becomes *her* in the object slot."],
            "The teacher praised her."),
        pat("apa4", "Continuous passive returns to V-ing", "common",
            "The passive has *is/are/was/were being + V3*. One option is a plain past and another is a perfect. Only the V-ing option is right.",
            ["Spot *being*: the active must have V-ing.", "Match the helping verb to the tense and to the doer's number.", "Keep the rest of the sentence."],
            "Dropping the continuous in the active changes the meaning.",
            "Select the active form: *The path was being cleared by the volunteers.*",
            ["*Was being + V3* is past continuous.", "The doer *the volunteers* is plural: *were + V-ing*.", "The old subject *the path* moves after the verb."],
            "The volunteers were clearing the path."),
        pat("apa5", "Let and requested frames go back", "occasional",
            "The passive starts with *Let ... be* or *You are requested / advised / warned to*. The active options are orders or requests.",
            ["Let ... be + V3 goes back to a bare order.", "*Requested to* goes back to *please*.", "Keep the object and the rest of the sentence."],
            "The frame words are only the passive form of an order or request.",
            "Select the active form: *You are requested to post this letter.*",
            ["*Requested to* means the sentence is a polite request.", "Use *please*.", "Keep the verb and the object."],
            "Please post this letter."),
    ],
)

# =====================================================================
# 5. Exam strategy
# =====================================================================
SUBS["ap-strategy"] = dict(
    concept=(
        "A voice question takes under 30 seconds. Use the same five steps every time: tag the voice, fix the tense, move the parts, "
        "re-agree the verb, and remove the options that break a rule. "
        "Each wrong option usually breaks exactly one rule."
    ),
    notes=r"""### Why this topic is quick marks
Every voice question is one row of one table. There is no vocabulary and no guessing. Learn the rows and the marks are easy.

### The five-step protocol
1. **Tag the voice.** Active stem means build a passive. Passive stem means build an active.
2. **Fix the tense.** Read the first helping verb. Say the row aloud: *was writing* becomes *was being + V3*.
3. **Move the parts.** Object and subject swap places. The old subject goes behind by, or becomes *they* if missing. Pronouns change case.
4. **Re-agree the verb.** Match is/are, was/were, has/have to the new subject.
5. **Remove faulty options.** Name each fault.

> **Tip:** Build the correct sentence yourself before you read the options.

### The four fault classes
| Fault | What it looks like | Example |
|---|---|---|
| Wrong V-form after be | V1 or V2 where V3 belongs | *is wrote, must obeyed, is ringed* |
| Broken being/been slot | been after a continuous be, being after have | *is been built, has being taken* |
| Tense change | the row is from another tense | *was written* for *writes* |
| Case or agreement | wrong pronoun form, or wrong verb number | *by he, The returns has been filed* |

A fifth, rarer fault is a role reversal. *The judge was acquitted by the accused* is the wrong passive of *The judge acquitted the accused.*

### Where the marks come from
Most papers set about one active-to-passive and one passive-to-active question. Voice items also appear inside error spotting and sentence improvement.

The tenses used most are simple present, simple past, present perfect, present continuous and modals. Master these five rows first. Then add past perfect and future perfect.

Orders (Let) and By-whom questions appear less often.

### When two options both look right
Compare them on one point at a time, in this order.

1. Tense row.
2. *Being* or *been*.
3. Agreement with the new subject.
4. Pronoun case.
5. Doer kept or dropped.

One of the two options will break a point. Never choose by which one sounds smoother. Wrong options are built to sound right. *Is been* sounds like *is being* when you read fast.

> **Watch:** A clean-sounding option can still have the wrong tense row. Sound is not the test. The row is.

### Daily practice
Write ten conversions a day: five plain statements, two modals, two orders and one question. Alternate directions. Write them by hand.

After a week, say the eight rows from memory before you start. Aim for full accuracy in about 25 seconds per question.
""",
    tricks=[
        {"title": "Name the fault",
         "body": "Every wrong option breaks one rule: V-form, being/been, tense, agreement or pronoun. Name the fault and the option is out.",
         "example": {"q": "Select the passive form: *They are constructing a new library.*",
                     "steps": ["*Are constructing* is present continuous.", "The row is *is/are being + V3*.", "The new subject *a new library* is singular."],
                     "answer": "A new library is being constructed by them."}},
        {"title": "Five-row priority",
         "body": "Learn simple present, simple past, present perfect, present continuous and modals first. They cover most of the questions."},
        {"title": "Write it, do not just say it",
         "body": "Voice errors hide on paper. Convert sentences in writing every day. The hand learns the pattern faster than the ear."},
    ],
    mistakes=[
        mis("Skipping the re-agreement check after conversion.", "Always match is/are, was/were, has/have to the new subject."),
        mis("Learning conversions word by word.", "Learn them as tense rows."),
        mis("Ignoring the pronoun at the end of the sentence.", "Check the case of every pronoun. It is the fastest way to remove an option."),
        mis("Accepting *is been* because it sounds like *is being*.", "Continuous means *being*. Perfect means *been*."),
        mis("Choosing the smoothest-sounding option.", "Compare tense row first, then being/been, then agreement, then case."),
    ],
    revision=[
        "Protocol: tag the voice, fix the tense row, move the parts, re-agree, remove faulty options.",
        "Fault classes: wrong V-form, being/been slot, tense change, case or agreement, role reversal.",
        "Five rows first: simple present, simple past, present perfect, present continuous, modals.",
        "Two clean options? Test one point at a time, starting with tense.",
        "Build your own answer before you read the options.",
        "Write conversions daily. Voice is a hand skill.",
    ],
    patterns=[
        pat("aps1", "One clean option: fault elimination", "very common",
            "There are four passive options. Each wrong one breaks a different rule (V-form, being/been, tense) and one is clean.",
            ["Build the correct passive yourself before reading the options.", "Scan each option for the four faults.", "Name each option's fault.", "The option with no fault is the answer."],
            "Questions have one clean option and three single-fault options.",
            "Select the passive form: *They are constructing a new library.*",
            ["*Are constructing* is present continuous.", "The row is *is/are being + V3*.", "*Is been constructed* has a broken slot; *was being constructed* changes the tense."],
            "A new library is being constructed by them."),
        pat("aps2", "Tense trap among near-identical options", "common",
            "All four options use the same words. They differ only in the helping verb chain (is cooked / was cooked / has been cooked / is being cooked).",
            ["Fix the active tense first and say its row aloud.", "Pick the option that reproduces that row exactly.", "Reject rows from other tenses, even if they are grammatical."],
            "The setter builds correct-looking rows from neighbouring tenses. Only the row separates them.",
            "Select the passive form: *The peon was ringing the bell.*",
            ["*Was ringing* is past continuous.", "The row is *was/were being + V3*.", "*Was rung* is simple past; *is being rung* is present continuous."],
            "The bell was being rung by the peon."),
        pat("aps3", "Identify the voice of a sentence", "occasional",
            "The question asks which sentence is passive (or active). The four options describe the same event.",
            ["Look for be/been + V3 with the receiver as subject.", "V-ing after be is still active.", "A by-phrase helps, but it is not required."],
            "The decoy is the continuous active, which looks like a passive.",
            "Which sentence is in the passive voice? (a) *The window was broken by the cricketer.* (b) *The cricketer broke the window.* (c) *The cricketer was breaking the window.* (d) *The cricketer has broken the window.*",
            ["Option (a) has the receiver *the window* as subject.", "Its verb is was + V3.", "In the other options the cricketer is the doer."],
            "The window was broken by the cricketer."),
        pat("aps4", "Combined skeletons", "occasional",
            "The sentence stacks two features, such as will have written or a question with a perfect tense.",
            ["Peel the outer frame first.", "Modal stays. Perfect adds been. A question adds inversion.", "Apply pronoun and agreement checks last."],
            "A stacked item is two rows at once. Solving the outer frame first keeps you calm.",
            "Select the passive form: *They will have published the magazine by March.*",
            ["*Will have published* is future perfect.", "The row is *will have been + V3*.", "The new subject is *the magazine*."],
            "The magazine will have been published by March."),
        pat("aps5", "Role-reversal decoy", "occasional",
            "The options use the same words but swap who does what. One option says the receiver did the action.",
            ["Find the doer and the receiver in the stem.", "The doer goes behind by in the passive.", "Reject the option that makes the receiver the doer."],
            "A role reversal keeps the grammar clean, so only the meaning exposes it.",
            "Select the passive form: *The judge acquitted the accused.*",
            ["The doer is *the judge*. The receiver is *the accused*.", "*Acquitted* is simple past: *was acquitted*.", "*The judge was acquitted by the accused* reverses the roles."],
            "The accused was acquitted by the judge."),
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
