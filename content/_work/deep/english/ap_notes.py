# Notes + per-subtopic patterns for active-passive (Phase 2 deep content).
S = {}

S["ap-basics"] = {
"notes": """### What voice means
In the **active voice** the subject does the action: *The chef prepared the meal.* In the **passive voice** the subject receives the action: *The meal was prepared by the chef.* Both sentences describe the same event — only the spotlight moves. Competitive exams (SSC, Railway, Banking) ask you to move that spotlight correctly, in under 30 seconds, twice per paper.

### The three moves — the whole method
1. **Object becomes subject.** Find the thing the verb acts on. In *The chef prepared the meal*, the meal is acted on, so *the meal* becomes the new subject.
2. **Verb becomes be + V3.** The main verb always turns into its past participle (V3: written, prepared, rung), and a helping verb *be* carries the original tense. *Prepared* is simple past, so *be* appears as *was*: *was prepared*. *Writes* is simple present, so *is written*. The tense never changes — only its carrier changes.
3. **Subject drops into a by-phrase.** The doer appears after *by*, in the object case: *by the chef, by him, by them*. When the doer is vague — *someone, people, they* — the by-phrase is usually dropped altogether.

Worked mini-example: *The postman rings the bell.* Object = the bell. Verb *rings* is simple present → *is rung*. Doer → *by the postman*. Result: *The bell is rung by the postman.*

### Pronouns swap their cases
Subject forms (I, he, she, we, they) become object forms (me, him, her, us, them) when they slide into the by-phrase. Object forms become subject forms when they move forward: *He helps me* → *I am helped by him*. Say the swap aloud once and the commonest option trap dies: *by he* and *us were invited* are impossible.

### Only transitive verbs can be passivised
A passive needs an object to promote. Verbs that take no object — *sleep, arrive, laugh, die, go, cry* — have no passive at all: *The baby slept peacefully* has no passive version, ever. This is a real exam type: *Select the sentence that cannot be changed into the passive voice* — the answer is the objectless verb. One refinement: verb + preposition can act as one transitive unit, so *They laughed at him* → *He was laughed at* is legal. Test the whole phrase, not the bare verb.

### The tense handover table (eight rows)
| Active | Passive |
|---|---|
| writes (simple present) | is / are + V3 |
| is writing (present continuous) | is / are being + V3 |
| has written (present perfect) | has / have been + V3 |
| wrote (simple past) | was / were + V3 |
| was writing (past continuous) | was / were being + V3 |
| had written (past perfect) | had been + V3 |
| will write (simple future) | will be + V3 |
| will have written (future perfect) | will have been + V3 |

Learn the rows as one block: the helping verb reproduces the original tense; the main verb is always V3. No row contains *is been*, *will being*, or a bare V1/V2 after *be*.

### Three instant elimination checks
1. **Tense changed?** *was written* offered for *wrote* — wrong.
2. **Wrong V-form after be?** *is wrote*, *is ringed*, *must obeyed* — wrong.
3. **Pronoun case broken?** *by he*, *us were invited* — wrong.
In a well-set item, each wrong option breaks exactly one of these rules; the correct option breaks none.

### Quick revision
- Three moves: object → subject; verb → be + V3 in the SAME tense; subject → by-phrase (dropped if vague).
- Pronoun mirror: he→him, she→her, they→them in the by-phrase; me→I when promoted to subject.
- No object → no passive: sleep, arrive, die, cry never passivise (but laugh AT him can).
- Vague agents (someone, they, people) usually vanish; the rest stay after by.
- Four fault classes to hunt in options: tense change, wrong V-form, missing being/been, pronoun case.
""",
"patterns": [
 {"id": "apb1", "name": "Three-move conversion with a pronoun swap", "frequency": "very common",
  "howToSpot": "A short declarative stem; the options are passive versions differing in the verb skeleton or in by he/by him.",
  "formula": None,
  "logic": "1. Find the object; promote it to subject.\n2. Rebuild the verb as be + V3, keeping the original tense exactly.\n3. Push the old subject behind by, in the object case.\n4. Re-agree is/are/was/were with the NEW subject.\n\n*Why it works:* every passive statement is built by these three moves and nothing else; the options differ only in which move was botched.",
  "example": {"q": "Select the passive form: *The peon rings the bell.*",
              "solution": "Object *the bell* → subject; *rings* (simple present) → **is rung**; doer → **by the peon**. Result: *The bell is rung by the peon.*"}},
 {"id": "apb2", "name": "Vague agent drops out", "frequency": "very common",
  "howToSpot": "The stem's subject is someone, people, they, one, or nobody-in-particular; the correct option carries no by-phrase while decoys drag 'by them/by people' along.",
  "formula": None,
  "logic": "1. Check whether the doer names a specific person or thing.\n2. Vague doers (someone, they, people) are dropped in the passive.\n3. Keep the tense row untouched; the by-phrase is the only casualty.\n\n*Why it works:* English omits agents that add no information; *My purse has been stolen* is idiomatic while *by someone* adds nothing.",
  "example": {"q": "Select the passive form: *Someone has switched off the fans.*",
              "solution": "Present perfect row → **have been switched off**; the vague agent *someone* is dropped: *The fans have been switched off.* Keeping 'by someone' is grammatical but never the keyed answer."}},
 {"id": "apb3", "name": "Pronoun-case elimination", "frequency": "common",
  "howToSpot": "The stem has pronouns on both sides (he...me, they...us) and the options tangle I/me, he/him, we/us in the two slots.",
  "formula": None,
  "logic": "1. Decide each pronoun's NEW job: mover-to-by-phrase takes object case; promoted pronoun takes subject case.\n2. Test each option's two pronoun slots independently — one correct slot does not save an option.\n3. Reject any option whose verb also moved.\n\n*Why it works:* *by he* and *me is helped* are impossible English, so case alone can finish the item.",
  "example": {"q": "Select the passive form: *They invited us to the wedding.*",
              "solution": "*We* is promoted (subject case, not *us*); *them* goes to the by-phrase: *We were invited to the wedding by them.*"}},
 {"id": "apb4", "name": "No-passive filter (objectless or stative verb)", "frequency": "occasional",
  "howToSpot": "The stem asks which sentence CANNOT be passivised (or which CAN); the options mix transitive and objectless verbs.",
  "formula": None,
  "logic": "1. Underline each option's verb and ask: does it act on a thing?\n2. Sleep, arrive, die, cry, go, laugh (alone) have no object → no passive.\n3. Stative verbs — have/own, resemble, lack, suit, cost — also refuse the passive in standard usage.\n\n*Why it works:* the passive promotes an object; where no object exists, the promotion is impossible, and the setter builds the whole item on that fact.",
  "example": {"q": "Which cannot be changed into the passive voice: *The baby slept peacefully* / *The mother woke the baby* / *The doctor examined the reports* / *The nurse weighed the newborn*?",
              "solution": "*Slept* takes no object, so *The baby slept peacefully* has no passive. The other three all have objects (the baby, the reports, the newborn) and passivise cleanly."}},
]}

S["ap-tense-tables"] = {
"notes": """### One row at a time
Every voice item is one row of the conversion table recited correctly. Identify the active tense, then produce its passive skeleton:

| Active | Passive | Example |
|---|---|---|
| writes | is / are + V3 | *Ram writes a story* → *A story is written by Ram* |
| is writing | is / are being + V3 | *Sita is drawing a map* → *A map is being drawn by Sita* |
| has written | has / have been + V3 | *They have caught the thief* → *The thief has been caught* |
| wrote | was / were + V3 | *The cook made dinner* → *Dinner was made by the cook* |
| was writing | was / were being + V3 | *The boys were flying kites* → *Kites were being flown by the boys* |
| had written | had been + V3 | *She had finished the work* → *The work had been finished by her* |
| will write | will be + V3 | *The PM will address the nation* → *The nation will be addressed by the PM* |
| will have written | will have been + V3 | *He will have completed it* → *It will have been completed* |

### The being/been slot rule
- **Continuous** in the active → **being**: *is being built, was being built, will be being built* (rare) — the word *being* only ever follows a continuous be or a modal's *be*.
- **Perfect** in the active → **been**: *has been taken, had been taken, will have been taken* — *been* only ever follows *have/had/will have*.
- **Modal** → plain **be**: *will be published, must be obeyed* — neither being nor been.

So *is been built* and *will being taken* are impossible; if an option contains them, kill it without reading further.

### Re-agreement: the new subject decides
After conversion, is/are, was/were, has/have must agree with the NEW subject, not the old one: *They have completed the projects* → *The projects **have** been completed* — the *have* of the active dies and *the projects* now govern. Setters plant one option that forgets to re-agree; sweep for it before anything else. *The clerk has filed the returns* → *The returns **have** been filed by the clerk* (not *has been*).

### Two nouns, two passives
Verbs that take two objects — *give, send, offer, grant, show, teach, tell, award* — produce two legal passives: *The teacher gave the students homework* → *The students were given homework* (person promoted) OR *Homework was given **to** the students* (thing promoted). The keyed answer usually promotes the person; the corrupted decoy drops the *to*: *Homework was given the students* is wrong.

### Tenses with no passive
Present perfect continuous (*has been writing*), past perfect continuous (*had been writing*) and future continuous (*will be writing*) have no passive row. When a stem uses one, the exam either avoids it or expects the nearest simple row. Do not invent *is being been written* — it does not exist.

### Stative verbs resist too
*A car is had by him* is not English. *Have/own/possess, resemble, lack, suit, fit, cost* normally refuse the passive. If a stem uses them, look for a *no passive possible* judgement rather than a conversion.

### Quick revision
- Perfect rows: has/have been, had been, will have been + V3. Continuous rows: is/are/was/were being + V3. Modals: be + V3, nothing between.
- being after continuous be; been after have/had; never is been, never will being.
- Re-agree with the NEW subject before checking anything else.
- Double-object verbs: person-promoted passive is keyed; the thing-promoted one must keep *to*.
- No passive: perfect continuous tenses; have/own/resemble/lack/suit.
""",
"patterns": [
 {"id": "apt1", "name": "Perfect-row passives (has/had/will have been + V3)", "frequency": "very common",
  "howToSpot": "The active verb is has written / had written / will have written; the options differ in been, the auxiliary, or the tense.",
  "formula": None,
  "logic": "1. Tag the active tense: present perfect, past perfect or future perfect.\n2. Produce its row: has/have been + V3, had been + V3, will have been + V3.\n3. Agree the auxiliary with the new subject; keep the by-agent in object case.\n\n*Why it works:* the perfect rows are the most-set rows in the paper, and every wrong option breaks exactly one cell (been dropped, tense shifted, agreement lost).",
  "example": {"q": "Select the passive form: *The workers have painted the gate.*",
              "solution": "Present perfect → **has/have been + V3**; new subject *the gate* is singular: *The gate has been painted by the workers.*"}},
 {"id": "apt2", "name": "Continuous-row passives (is/are/was/were being + V3)", "frequency": "very common",
  "howToSpot": "The active verb is is writing / was writing type; options juggle being, been and the bare participle.",
  "formula": None,
  "logic": "1. Continuous active → being row: is/are/was/were + being + V3.\n2. Match was/were to the new subject's number.\n3. Refuse *is been* and *is building*-type answers that drop the passive entirely.\n\n*Why it works:* being is the continuous marker; the moment the active is continuous, the passive must show being — options without it are dead.",
  "example": {"q": "Select the passive form: *The masons are laying the bricks.*",
              "solution": "Present continuous → **are being laid**: *The bricks are being laid by the masons.* 'Are laid' would claim a habitual act, not an ongoing one."}},
 {"id": "apt3", "name": "Re-agreement with the new subject", "frequency": "common",
  "howToSpot": "The active subject is plural (they, the workers) and the promoted object is singular (the gate, the trophy) — or the reverse; one option agrees with the OLD subject.",
  "formula": None,
  "logic": "1. Promote the object; note its number: singular or plural.\n2. Choose is/was/has for a singular new subject; are/were/have for a plural one.\n3. Only then check the rest of the row (been, V3, by-agent).\n\n*Why it works:* the helping verb follows its own subject, which changed; options built from the old subject's number are the planted fault.",
  "example": {"q": "Select the passive form: *The clerk has filed all the returns.*",
              "solution": "New subject *the returns* is plural → **have been filed**: *The returns have been filed by the clerk.* 'Has been filed' agrees with the clerk, not with the new subject."}},
 {"id": "apt4", "name": "being vs been slot discrimination", "frequency": "common",
  "howToSpot": "The options are identical except for the being/been word — e.g. is being repaired vs is been repaired vs was being repaired.",
  "formula": None,
  "logic": "1. Ask what the active tense is: continuous or perfect.\n2. Continuous → being; perfect → been; modal → neither.\n3. Check the auxiliary's tense matches the active exactly.\n\n*Why it works:* being and been live in fixed slots; swapping them is the single most planted voice error in the paper.",
  "example": {"q": "Select the passive form: *The engineers were repairing the bridge when we crossed.*",
              "solution": "Past continuous → **was being repaired**: *The bridge was being repaired when we crossed.* 'Was been repaired' puts been in a continuous slot — impossible."}},
 {"id": "apt5", "name": "Double-object verb: person-promoted passive", "frequency": "common",
  "howToSpot": "The stem has a person and a thing after verbs like give, grant, show, offer, award; one correct option promotes the person, decoys corrupt the other passive.",
  "formula": None,
  "logic": "1. Identify the indirect object (person) and direct object (thing).\n2. The keyed passive usually promotes the person: person + was/were + V3 + thing + by-agent.\n3. If an option promotes the thing instead, it must carry *to* before the person — without *to* it is broken.\n\n*Why it works:* both passives are legal, but the person-promoted one needs no preposition, so the setter corrupts the thing-promoted one by deleting *to*.",
  "example": {"q": "Select the passive form: *The principal granted Meena a scholarship.*",
              "solution": "Person promoted: *Meena was granted a scholarship by the principal.* 'A scholarship was granted Meena' is broken — the thing-promoted version needs *to*: *granted **to** Meena*."}},
]}

S["ap-modals-imperatives"] = {
"notes": """### Modals: one row, no exceptions
Will, shall, can, could, may, might, must, should, ought to → **modal + be + V3**.
*You must obey the rules* → *The rules must be obeyed.* *They can solve it* → *It can be solved.* No *being*, no *been* after a modal: *must being obeyed* and *must been obeyed* are impossible. *Ought to* keeps its *to*: *The bill ought to be paid.*

### Imperatives: the Let anchor
An order has no subject and starts with a base verb. Convert with **Let + object + be + V3**:
- Order: *Shut the door* → *Let the door be shut.*
- Negative order: *Do not pluck the flowers* → *Let the flowers not be plucked* (or a modal version: *The flowers should not be plucked*).
- The verb after *be* is always V3: *Let the gate be opened*, never *be open* (adjective) or *be opening*.

### Requests, advice, warnings
The polite words change the skeleton, not the tense:
- **Please / kindly** → *You are requested to + V1*: *Please post this letter* → *You are requested to post this letter.*
- **Advice** (should/ought in sense) → *You are advised to + V1*: *Give up smoking* → *You are advised to give up smoking.*
- **Warning** (never, do not — danger) → *You are warned not to + V1.*
Learn the three openers as a chant: please → requested, advice → advised, danger → warned.

### Questions: three shapes
1. **Who** as doer → **By whom + auxiliary + subject + V3**: *Who broke the window?* → *By whom was the window broken?* Word order is the planted error: *By whom the window was broken?* is statement order, not question order.
2. **Whom/what** as receiver → the wh-word itself becomes the subject: *Whom did the manager appoint?* → *Who was appointed by the manager?* (whom becomes who in subject position).
3. **Yes/no question** → auxiliary first, new subject next: *Did she sing a song?* → *Was a song sung by her?*

### Infinitives and gerunds
- *to write* → **to be written**: *I want someone to compile the report* → *I want the report to be compiled.*
- *writing* (gerund) → **being written**: *He likes people praising him* → *He likes being praised.*
- After *likes, hates, remembers, wants* the being/to be forms are the keyed answers; decoys offer *been praised* (impossible after likes) or an active participle.

### Factitive and double-object verbs
*Give, send, offer, grant, show, teach, award* yield two passives (person-promoted and thing-promoted with *to*). *The guide showed the tourists the paintings* → *The tourists were shown the paintings by the guide* — clean; *The paintings were shown the tourists* — broken, needs *to the tourists*.

### Let me / Let us
- *Let us go* (suggestion) belongs to narration, not voice — do not force a Let-passive.
- *Let me sit here* (permission) → *I should be allowed to sit there* style answers; papers rarely test it in voice, more often in improvement.

### Quick revision
- Modal row: modal + be + V3 — no being, no been, no to (except ought to).
- Order → Let + object + be + V3; negative → Let ... not be ... or should not be.
- please → You are requested to; advice → You are advised to; danger → You are warned not to.
- Who-questions → By whom + aux + subject + V3; whom-questions → Who was V3 by ...?
- to write → to be written; people praising → being praised.
""",
"patterns": [
 {"id": "apm1", "name": "Modal + be + V3", "frequency": "very common",
  "howToSpot": "The stem carries will/can/must/should/ought to; options scatter being, been, bare V1 or V3 after the modal.",
  "formula": None,
  "logic": "1. Spot the modal; nothing between modal and be.\n2. Fixed row: modal + be + V3 — no being, no been.\n3. Keep the modal itself unchanged (must stays must; would for will is a decoy).\n\n*Why it works:* the modal row has zero variants, so any option that inserts being/been or drops be is instantly wrong.",
  "example": {"q": "Select the passive form: *You should check the receipts.*",
              "solution": "Modal row: **should be checked** — *The receipts should be checked.* 'Should checked' loses be; 'should being checked' and 'should been checked' break the slot."}},
 {"id": "apm2", "name": "Imperative → Let + object + be + V3", "frequency": "very common",
  "howToSpot": "The stem is a bare order starting with a base verb (Shut, Post, Switch off) and no subject; the right option starts with Let.",
  "formula": None,
  "logic": "1. Recognise the imperative (no subject, base verb).\n2. Skeleton: Let + object + be + V3.\n3. Reject options without Let (statements) and options with V1/V-ing after be.\n\n*Why it works:* Let is the standard passive carrier of a command; the exam always plants a statement-form decoy and a missing-be decoy.",
  "example": {"q": "Select the passive form: *Switch off the mobile.*",
              "solution": "Order → **Let the mobile be switched off.** 'Let the mobile switched off' drops be; 'The mobile is switched off' turns the order into a statement."}},
 {"id": "apm3", "name": "Negative imperative and warnings", "frequency": "common",
  "howToSpot": "The stem says Do not ... / Never ...; options must carry not in the right slot with the right skeleton (requested/advised/warned not to, or Let ... not be).",
  "formula": None,
  "logic": "1. Classify the tone: polite request (please...not) → requested not to; advice → advised not to; warning → warned not to.\n2. Bare negative order → Let + object + not + be + V3, or a modal version (should not be).\n3. Check the negative word sits before to: *not to smoke*, never *to not smoke* in keyed answers.\n\n*Why it works:* the negative travels with the reporting frame; options that drop the frame or misplace not fail at once.",
  "example": {"q": "Select the passive form: *Please do not smoke in the hall.*",
              "solution": "Polite negative request → *You are requested **not to smoke** in the hall.* The skeleton requested + not to + V1 keeps both the politeness and the prohibition."}},
 {"id": "apm4", "name": "Request formula: You are requested to", "frequency": "common",
  "howToSpot": "The stem contains please or kindly with a base verb; the keyed option begins You are requested to and decoys begin Let or use the noun request.",
  "formula": None,
  "logic": "1. See please/kindly → the request frame: You are requested to + V1.\n2. Keep the rest of the sentence word for word after to.\n3. Let-forms and is + V3 statements are decoys for a please-sentence.\n\n*Why it works:* please cannot survive inside a passive clause; English swaps it for the frame *you are requested to*, and the exam tests exactly that swap.",
  "example": {"q": "Select the passive form: *Kindly grant me a day's leave.*",
              "solution": "**You are requested to grant me a day's leave.** Nothing else changes: grant stays a base verb after to, and the listener's *me* is kept."}},
 {"id": "apm5", "name": "Question conversions (By whom / Who was)", "frequency": "common",
  "howToSpot": "The stem ends with a question mark; who-questions convert with By whom at the front, whom/what-questions promote the wh-word to subject.",
  "formula": None,
  "logic": "1. Decide the wh-word's job in the question: doer (who) or receiver (whom/what).\n2. Doer → By whom + auxiliary + new subject + V3 (+?).\n3. Receiver → the wh-word itself is promoted: *Who was appointed by the manager?*\n4. Check question word order — auxiliary BEFORE subject.\n\n*Why it works:* question conversions fail on word order far more often than on verb form; checking the order first settles the item.",
  "example": {"q": "Select the passive form: *Who broke the window?*",
              "solution": "**By whom was the window broken?** — By whom + was (past of the do-broken frame) + the window + broken. 'By whom the window was broken?' is statement order; 'Who was broken the window?' scrambles the roles."}},
 {"id": "apm6", "name": "Infinitive and gerund passives (to be / being + V3)", "frequency": "occasional",
  "howToSpot": "The stem has to + verb after want/like/hate, or a gerund with people/someone as its doer (people praising him); options offer to be, being, been forms.",
  "formula": None,
  "logic": "1. Infinitive: to + V1 → to + be + V3 (*to compile* → *to be compiled*).\n2. Gerund: V-ing → being + V3 (*praising him* → *being praised*).\n3. Reject been after like/want (been only follows have/had) and active forms that keep the old doer.\n\n*Why it works:* the passive marker (be/being) slides into the same slot the non-finite verb occupied; the tense frame of the sentence never moves.",
  "example": {"q": "Select the passive form: *He likes people praising him.*",
              "solution": "Gerund passive: *He likes **being praised**.* 'Likes been praised' is impossible (been needs have/had); 'likes to praise' reverses the meaning."}},
]}

S["ap-passive-to-active"] = {
"notes": """### The reverse run
Passive → active appears in every second paper. The method mirrors the forward one: promote the agent, rebuild the tense from the passive skeleton, demote the old subject.

| Passive | Active |
|---|---|
| The letter was written by Sita | Sita **wrote** the letter |
| The road is being repaired | They **are repairing** the road |
| The work had been finished | She **had finished** the work |
| The results will be declared | The board **will declare** the results |
| The kite was being flown by the boy | The boy **was flying** the kite |

### Read the FIRST auxiliary, not the participle
The participle (written, repaired) never tells you the tense — every row ends in V3. The first auxiliary carries the tense:
- was/were + V3 → simple past (*was written* → *wrote*)
- is/are being + V3 → present continuous (*is being written* → *is writing*)
- was/were being + V3 → past continuous (*was being written* → *was writing*)
- has/have been + V3 → present perfect (*has been written* → *has written*)
- had been + V3 → past perfect (*had been written* → *had written*)
- will be + V3 → simple future (*will be written* → *will write*)
- will have been + V3 → future perfect (*will have been written* → *will have written*)
- modal + be + V3 → modal + V1 (*must be obeyed* → *must obey*)

### The agent hunt
- A by-phrase gives the new subject: *by Sita* → Sita. Keep the noun exactly; change only its position.
- No by-phrase → supply the standard vague subject **they** (or people): *The thief was arrested last night* → *They arrested the thief last night.* Papers accept they; the options differ only in verb form.
- Do not promote a noun that was not the agent: *The window was broken by the cricketer* → *The cricketer broke the window*, never *The window broke the cricketer*.

### The object-case exit
The old subject leaves through the object slot in object case: *She was praised by the teacher* → *The teacher praised **her*** (not she). *He was helped by his friends* → *His friends helped **him***. Any option ending *praised she / helped he* is dead on arrival.

### Continuous skeletons must come back continuous
*was being + V3* is past CONTINUOUS — the active must be *was/were + V-ing*: *The path was being cleared by volunteers* → *The volunteers were clearing the path.* The commonest decoy returns a simple past (*cleared*) and loses the ongoing sense; a second decoy changes tense to present perfect. Refuse both.

### Let-passives reverse to orders
*Let the door be shut* → *Shut the door.* *You are requested to post this letter* → *Please post this letter.* Reverse the frame word as well: requested signals please, advised signals should-giving, warned signals danger.

### Quick revision
- Agent becomes subject; no agent → they.
- Tense from the FIRST auxiliary: was → past, is being → present continuous, has been → present perfect, had been → past perfect, will be → future, modal be → modal + V1.
- Old subject exits in object case: praised her, helped him.
- being skeleton → V-ing active; never return a simple past for it.
- requested → please, Let ... be → bare order.
""",
"patterns": [
 {"id": "apa1", "name": "Tense recovery from the first auxiliary", "frequency": "very common",
  "howToSpot": "A be + V3 stem with a by-agent; the four active options differ in tense (has delivered / had delivered / is delivering / will deliver).",
  "formula": None,
  "logic": "1. Ignore the participle; read the first auxiliary.\n2. Map it: had been → had + V3; has been → has + V3; was being → was/were + V-ing; will be → will + V1.\n3. Move the by-agent to the subject slot and demote the old subject.\n\n*Why it works:* every passive row ends in V3, so only the auxiliary distinguishes the eight rows; reading it first fixes the tense in two seconds.",
  "example": {"q": "Select the active form: *The walls had been whitewashed by the masons.*",
              "solution": "had been + V3 → past perfect: *The masons **had whitewashed** the walls.* 'Have whitewashed' shifts to present perfect; 'were whitewashing' changes the aspect."}},
 {"id": "apa2", "name": "Missing agent: supply they", "frequency": "common",
  "howToSpot": "The passive has no by-phrase; the correct option begins with They (or People) and decoys use the old subject as doer or shift the tense.",
  "formula": None,
  "logic": "1. Confirm no by-phrase exists.\n2. Put the standard vague doer they before the rebuilt verb.\n3. Demote the passive's subject to object position, keeping the tense row.\n\n*Why it works:* English passives hide vague agents; converting back, they is the conventional stand-in, and the exam keys it every time.",
  "example": {"q": "Select the active form: *The results will be declared on Monday.*",
              "solution": "No agent → **They will declare the results on Monday.** will be + V3 → will + V1. 'The results will declare...' keeps the old subject as doer — reversed roles."}},
 {"id": "apa3", "name": "Object-case exit pronoun", "frequency": "common",
  "howToSpot": "The passive's subject is a pronoun (he, she, they, we); options end with the pronoun in both cases (praised her / praised she).",
  "formula": None,
  "logic": "1. Move the by-agent to the front; rebuild the tense.\n2. The old subject-pronoun leaves in OBJECT case: her, him, them, us.\n3. Scan the tail of every option for the pronoun first — it eliminates fastest.\n\n*Why it works:* case reversal is the mirror of the forward pronoun swap, and *praised she* is ungrammatical at a glance.",
  "example": {"q": "Select the active form: *She was praised by the teacher.*",
              "solution": "Agent first: *The teacher praised **her*** — was praised → praised (simple past), she → her (object case). 'Praised she' breaks the case; 'praises her' shifts the tense."}},
 {"id": "apa4", "name": "Continuous skeleton returns to V-ing", "frequency": "common",
  "howToSpot": "The stem is is/are/was/were being + V3; one option returns a plain past, another a perfect — only the V-ing option keeps the continuous.",
  "formula": None,
  "logic": "1. Spot being → the active MUST carry V-ing.\n2. Pick the auxiliary by tense: is being → is/are + V-ing; was being → was/were + V-ing.\n3. Agree the new auxiliary with the agent's number (workers → were).\n\n*Why it works:* being is the continuous marker in both voices; dropping it in the active silently changes the sentence's meaning, which the key never allows.",
  "example": {"q": "Select the active form: *The path was being cleared by the volunteers.*",
              "solution": "was being + V3 → **were clearing**: *The volunteers were clearing the path.* 'Were cleared' loses the ongoing sense; 'have cleared' changes the tense."}},
]}

S["ap-strategy"] = {
"notes": """### Why this is the cheapest topic in the paper
Voice items are worth one mark each in under 30 seconds, and every item is a row of one table. There is no inference, no vocabulary, no context — only the row and the three moves. With the eight rows memorised, the section becomes marks on demand.

### The 20-second protocol
1. **Tag the voice.** Active stem → build passive; passive stem → build active.
2. **Fix the tense.** From the first auxiliary (active) or the first auxiliary of the be + V3 skeleton (passive). Say the row aloud: *was writing → was being + V3*.
3. **Move the parts.** Object ↔ subject; subject → by-phrase (or they if missing); pronouns swap case.
4. **Re-agree the verb** with its NEW subject.
5. **Eliminate by fault class** — every wrong option in a well-set item breaks exactly one rule.

### The four fault classes (name them, kill them)
| Fault class | What it looks like | Example |
|---|---|---|
| Wrong V-form after be | V1 or V2 where V3 belongs | *is wrote*, *must obeyed*, *is ringed* |
| being/been slot broken | been after continuous be; being after have | *is been built*, *has being taken* |
| Tense change | row swapped to another tense | *was written* offered for *wrote*; *would be* for *will be* |
| Pronoun case / agreement | by he; us were; has been for a plural new subject | *The returns has been filed* |

A fifth, rarer fault: role reversal — *The judge was acquitted by the accused* for *The judge acquitted the accused*.

### Where the marks actually come from
Roughly one active→passive and one passive→active per Tier 1 shift; Tier 2 adds voice items inside error-spotting, cloze and sentence improvement. The tenses drawn are usually simple present, simple past, present perfect, present continuous and modals — master those five rows first, then add past perfect and future perfect. Imperatives (Let) and By-whom questions appear about once every two or three shifts.

### When two options both look clean
Compare them on ONE dimension at a time, in this order: (1) tense row, (2) being/been, (3) agreement with the new subject, (4) pronoun case, (5) agent kept or dropped. One of the two will break a dimension — the other survives. Never choose by what sounds smoother; sound is what the wrong options are engineered to exploit (*is been* sounds exactly like *is being* at speed).

### Daily drill that actually works
Ten conversions a day, written by hand, alternating directions: five statement rows, two modals, two imperatives, one question. After a week, recite the eight-row table from memory before starting. After two, run only the fault-class sweep on practice papers. Target: 100% accuracy, 25 seconds per item. Voice rewards drilling more than reading — errors live on paper, not in the ear.

### Quick revision
- Protocol: tag voice → fix tense row → move parts → re-agree → eliminate by fault class.
- Fault classes: wrong V-form, being/been slot, tense change, case/agreement, role reversal.
- Five-row priority: simple present, simple past, present perfect, present continuous, modals.
- Two clean options? Test one dimension at a time — tense first.
- Write daily; voice is a hand skill, not an ear skill.
""",
"patterns": [
 {"id": "aps1", "name": "One clean option: fault-class elimination", "frequency": "very common",
  "howToSpot": "Four passive options for one stem; each wrong one breaks a different rule (V-form, being/been, tense) and only one is clean.",
  "formula": None,
  "logic": "1. Build the correct row yourself BEFORE reading the options.\n2. Scan options for the four faults: V-form, being/been, tense, agreement.\n3. Name each option's fault; the option with no nameable fault is the answer.\n\n*Why it works:* items are engineered as one clean + three single-fault options; naming faults is faster than admiring sentences.",
  "example": {"q": "Select the passive form: *They are constructing a new library.*",
              "solution": "Row: present continuous → **is being constructed**: *A new library is being constructed by them.* Decoys: is been constructed (slot), is constructing (active), was being constructed (tense)."}},
 {"id": "aps2", "name": "Tense-trap discrimination among near-identical options", "frequency": "common",
  "howToSpot": "All four options share the same words and differ only in the auxiliary chain (is cooked / was cooked / has been cooked / is being cooked).",
  "formula": None,
  "logic": "1. Fix the active tense first and say its row aloud.\n2. Match the option whose auxiliary chain reproduces that row exactly.\n3. Refuse rows that are grammatical but from a DIFFERENT tense — grammar is not the test, the row is.\n\n*Why it works:* the setter builds three grammatical-looking rows from neighbouring tenses; only row-faithfulness separates them.",
  "example": {"q": "Select the passive form: *The peon was ringing the bell.*",
              "solution": "Past continuous → **was being rung**: *The bell was being rung by the peon.* 'Was rung' (simple past row) and 'is being rung' (present continuous row) are both grammatical — but from the wrong rows."}},
 {"id": "aps3", "name": "Identify the voice of a given sentence", "frequency": "occasional",
  "howToSpot": "The stem asks which sentence is in the passive (or active) voice; options are four complete sentences, usually about the same event.",
  "formula": None,
  "logic": "1. Look for the be/have been + V3 skeleton → passive; plain V1/V2/V-ing with a doer before the object → active.\n2. Continuous actives (was reading) are still ACTIVE — V-ing after be is not a passive.\n3. A by-phrase confirms the passive but is not required (agents can be dropped).\n\n*Why it works:* the item tests recognition, not conversion; the decoy is always the continuous active that superficially resembles a passive.",
  "example": {"q": "Which sentence is in the passive voice: *The window was broken by the cricketer* / *The cricketer broke the window* / *The cricketer was breaking the window* / *The cricketer has broken the window*?",
              "solution": "*The window was broken by the cricketer* — be + V3 with the receiver as subject. The others keep the cricketer as doer, so they remain active however their tenses differ."}},
 {"id": "aps4", "name": "Combined skeletons (modal + perfect, future perfect, question + perfect)", "frequency": "occasional",
  "howToSpot": "The stem stacks two features — will have written, must not violate, Who has written — so the answer needs two rules applied in order.",
  "formula": None,
  "logic": "1. Peel the outer frame first: modal stays, perfect adds been, question adds inversion/By whom.\n2. Rows: will have written → will have been + V3; must not violate → must not be + V3; Who has written → By whom has ... been written.\n3. Apply pronoun and agreement checks last.\n\n*Why it works:* stacked items are just two rows worn at once; solving the outer frame first prevents mid-sentence panic.",
  "example": {"q": "Select the passive form: *They will have published the magazine by March.*",
              "solution": "Future perfect row: **will have been published** — *The magazine will have been published by March.* 'Will be published' drops the perfect; 'will have published' keeps the active."}},
]}
