# Notes + per-subtopic patterns for direct-indirect (Phase 2 deep content).
S = {}

S["narr-reporting-verb"] = {
"notes": """### The reporting verb is the first word you write
Direct: *She said to me, 'I am tired.'* Indirect: *She told me that she was tired.* The comma and the inverted commas die; a connector takes their place; and the reporting verb itself often changes. Get the verb right and half the item is already done.

### say vs tell
- **tell needs a listener**: told me, told us, told him. Exam English never accepts *told that...* with no object after told.
- **say needs no listener**: *He said that...*
- **said to + listener becomes told + listener**: *He said to me* → *He told me*.
The giveaway: if the stem reads *said to someone*, the keyed option begins with told/asked/ordered-type verb plus that someone — never 'said to' kept as it is.

### The tone of the quote picks the verb
| Quote tone | Reporting verb | Connector |
|---|---|---|
| Statement | told / said | that |
| Yes/No question | asked | if / whether |
| Wh-question | asked | the wh-word itself |
| Order | ordered / told + object | to + V1 |
| Request (please, kindly) | requested | to + V1 |
| Advice | advised | to + V1 |
| Suggestion (let us) | suggested / proposed | V-ing, or that...should |
| Exclamation of joy (Hurrah) | exclaimed with joy | that |
| Exclamation of grief (Alas) | exclaimed with sorrow | that |
| Wish / prayer | wished / prayed | that |

Match tone to verb: a please-sentence keyed with *ordered* is wrong even when every tense inside is perfect. Exams plant exactly this — the correct tenses wrapped around the wrong verb.

### Present or future reporting verb: no backshift
If the reporting verb is present (says, asks, has said) or future (will say), the quote's tense does NOT move: *He says, 'I am busy.'* → *He says that he **is** busy.* An option offering *was* or *would* there is the planted fault. Papers also like the reporting verb swapped quietly: *says* keyed as *said*.

### Connector discipline
- Statements → **that**.
- Yes/No questions → **if** or **whether** (never both, never that).
- Orders, requests, advice → **to + base verb** (never that, never that...to).
Exactly one connector per sentence: *asked that if* and *told that to come* are impossible — each is a favourite wrong option.

### Other mechanics
- The inverted commas, the comma after the reporting verb, the capital letter of the quote and the question mark all disappear; the reported sentence ends with a full stop.
- The listener stays in the object case: told **me**, asked **him**, requested **her**.
- A listener after told is compulsory: *told the staff*, never *told to the staff*.
- With say + universal sentence, that is still the connector: *He said that honesty is the best policy.*

### Quick revision
- said to + person → told + person; tell always takes a listener, say never does.
- Tone map: statement → that; yes/no → if/whether; wh → the wh-word; order/request/advice → to + V1; Hurrah → exclaimed with joy; Alas → exclaimed with sorrow.
- Reporting verb in the present (says/asks/has said) → NO backshift inside.
- One connector only; that never pairs with if/whether/to.
- told takes its object directly: told the staff, not told to the staff.
""",
"patterns": [
 {"id": "nrv1", "name": "said to + listener becomes told + listener", "frequency": "very common",
  "howToSpot": "The stem reads 'X said to me/him/us, ...' with a statement; one option keeps 'said to', one drops the listener after told, and the keyed one reads told + listener + that.",
  "formula": None,
  "logic": "1. Spot said to + a person: that pair must become told + the person.\n2. Add the connector that and run the rest of the checks (tense ladder, pronouns, time words).\n3. Kill options that keep said to, or that use told with no listener, or told to + listener.\n\n*Why it works:* say never carries a listener while tell must — the exam plants one option that forgets each half.",
  "example": {"q": "Select the indirect form: *She said to me, 'I am very busy today.'*", "solution": "**She told me that she was very busy that day.** — said to me → told me; am → was; today → that day. Keeping 'said to me that...' is the planted fault."}},
 {"id": "nrv2", "name": "Tone decides the reporting verb", "frequency": "very common",
  "howToSpot": "The stem carries please/kindly (request), an order, advice, or a suggestion; the options use different verbs (requested/ordered/advised/suggested) with identical tenses.",
  "formula": None,
  "logic": "1. Classify the tone before touching anything else: please → requested; command → ordered; advice → advised; let us → suggested.\n2. Attach the right frame: requested/ordered/advised + object + to + V1; suggested + V-ing.\n3. Reject options whose tense work is fine but whose verb mismatches the tone.\n\n*Why it works:* tone-to-verb is a one-to-one map, so the verb alone can settle the item even before the tenses are compared.",
  "example": {"q": "Select the indirect form: *The doctor said to Father, 'Give up smoking.'*", "solution": "Advice tone → **The doctor advised Father to give up smoking.** 'Requested Father' softens a piece of advice into a favour; 'ordered Father' hardens it — both are planted."}},
 {"id": "nrv3", "name": "Present reporting verb: no backshift", "frequency": "common",
  "howToSpot": "The stem's frame is says / often says / has said / will say; one option backshifts the quote (is → was, will → would) and the keyed one leaves the tense untouched.",
  "formula": None,
  "logic": "1. Check the reporting verb's tense FIRST.\n2. Present or future frame → the quote's tense and time words stay exactly as spoken (only pronouns follow SONA).\n3. Also reject options that quietly swap says → said.\n\n*Why it works:* backshift exists to mark remoteness in time; a present reporting verb has none, so the ladder is not climbed.",
  "example": {"q": "Select the indirect form: *Ravi says, 'I do not like loud music.'*", "solution": "**Ravi says that he does not like loud music.** — says keeps the quote in the present: does not like, NOT did not like. Only the pronoun moves (I → he)."}},
 {"id": "nrv4", "name": "Connector discipline (one connector, right one)", "frequency": "common",
  "howToSpot": "Options that pair connectors (asked that if, told that to) or keep the do/does/did of the quote inside a reported question.",
  "formula": None,
  "logic": "1. Statement → that; yes/no question → if/whether; wh-question → the wh-word alone; order/request/advice → to + V1.\n2. Count the connectors in each option — exactly one is allowed.\n3. In reported questions, do/does/did of the direct quote must vanish, with the tense landing on the main verb.\n\n*Why it works:* English allows one subordinator per clause; stacking two (or keeping an auxiliary with nothing to carry) is always wrong.",
  "example": {"q": "Select the indirect form: *Priya asked me, 'Are you coming to the fair?'*", "solution": "**Priya asked me if I was coming to the fair.** — one connector (if), statement order after it. 'Asked me that if...' stacks two connectors; 'if was I coming' breaks the order."}},
]}

S["narr-tense-shift"] = {
"notes": """### The ladder: one rung down
When the reporting verb is in the past — said, told, asked, nearly always in exams — every verb inside the quote steps ONE rung down:

| Direct | Indirect |
|---|---|
| am / is / are | was / were |
| write (V1) | wrote (V2) |
| is / are writing | was / were writing |
| has / have written | had written |
| wrote (V2) | had written |
| was / were writing | had been writing |
| will / shall | would / should |
| can | could |
| may | might |
| must (duty) | had to |

'I am writing a letter' → he said he **was writing** a letter. 'I wrote it' → he said he **had written** it.

### The ceiling: past perfect never climbs
A quote already in the past perfect stays where it is: 'The train had left' → he said the train **had left**. Same for the past perfect continuous. There is no fifth rung.

### Where the ladder is not used
- **Universal truths and habits of nature**: 'The earth revolves around the sun' → he said that the earth **revolves** around the sun.
- **Present or future reporting verb**: says/asks/will say → no change at all.
- **Unreal and fixed forms**: would, could, might, should, ought to, used to, had better, would rather — these are already one step from reality and do NOT shift again. 'I would rather stay home' → he said he **would rather stay** home.

### The two planted traps
- **Over-backshift**: 'I am tired' reported as *he said he had been tired* — one rung too far. Simple present steps to simple past, never straight to the past perfect.
- **Half-backshift**: the frame is said but the quote still carries is, are, will, can. This is the single commonest wrong option in the section.

### Time words travel with the tense
The backshift drags the time words along: tomorrow → the next day, now → then, ago → before. If an option backshifts the verb but keeps tomorrow — or shifts the time word but keeps is — kill it. Tense and time words move together or not at all; that pairing is itself a testable pattern.

### Modal specifics worth memorising
must for obligation → had to ('I must reach by six' → he said he **had to** reach by six); must for deduction can stay must. would rather, had better and used to are frozen — they never change shape, only the pronouns around them move.

### Quick revision
- One rung: am → was; write → wrote; was writing → had been writing; wrote → had written; will → would; can → could; may → might; must (duty) → had to.
- had + V3 is the ceiling: it stays had + V3.
- No shift for universal truths, present reporting verbs, and would/could/might/should/ought to/used to/had better/would rather.
- Over-backshift and half-backshift are the two planted faults — count the rungs.
- Verb moved? Time words must move too.
""",
"patterns": [
 {"id": "nts1", "name": "Present to past: the first rung", "frequency": "very common",
  "howToSpot": "The quote is in the simple present or present continuous; the options differ between was/were (correct rung) and had been (over-shift) or is/are (no shift).",
  "formula": None,
  "logic": "1. Confirm the reporting verb is past (said/told/asked).\n2. Step the quote down exactly one rung: am/is + V-ing → was/were + V-ing; V1 → V2.\n3. Refuse both neighbours: the unshifted present and the over-shifted past perfect continuous.\n\n*Why it works:* the first rung is the most-set row in the paper, and its two wrong neighbours are always planted.",
  "example": {"q": "Select the indirect form: *He said, 'I am learning German these days.'*", "solution": "**He said that he was learning German those days.** — am learning steps to was learning; these days → those days. 'Had been learning' climbs two rungs."}},
 {"id": "nts2", "name": "Past to past perfect: the second rung", "frequency": "very common",
  "howToSpot": "The quote uses a simple past or past continuous verb; options offer the unshifted past, the correct had-forms, or a present perfect.",
  "formula": None,
  "logic": "1. V2 inside a past frame → had + V3.\n2. was/were + V-ing → had been + V-ing (past continuous → past perfect continuous).\n3. Remember the ceiling: a quote already in the past perfect does not move.\n\n*Why it works:* the earlier-of-two-past-events rule carries over into reporting — the reported event must read as before the reporting.",
  "example": {"q": "Select the indirect form: *The watchman said, 'The lights were flickering all night.'*", "solution": "**The watchman said that the lights had been flickering all night.** — were flickering steps to had been flickering. 'Had flickered' changes the continuous to a completed act."}},
 {"id": "nts3", "name": "Modal shifts (will, can, may, must)", "frequency": "very common",
  "howToSpot": "The quote carries will/can/may/must; options swap in the unshifted modal, a neighbouring wrong modal, or the correct would/could/might/had to.",
  "formula": None,
  "logic": "1. Apply the modal row: will/shall → would/should; can → could; may → might; must (duty) → had to.\n2. Keep the rest of the verb phrase untouched (will visit → would visit, not had visited).\n3. Pair the modal check with the time word check in the same sweep.\n\n*Why it works:* each modal has exactly one partner one rung down; anything else (may → will, will → had) is a planted neighbour.",
  "example": {"q": "Select the indirect form: *She said, 'I can solve this puzzle.'*", "solution": "**She said that she could solve that puzzle.** — can → could. 'Can solve' refuses the shift; 'may solve' imports the wrong modal."}},
 {"id": "nts4", "name": "No backshift: universal truth", "frequency": "common",
  "howToSpot": "The quote states a law of nature, a proverb, or a permanent fact ('The sun rises in the east'); one option dutifully backshifts it (rose) and the keyed one keeps the present.",
  "formula": None,
  "logic": "1. Ask: is the statement true always, or only at the moment of speaking?\n2. Always-true → the tense stays put even inside a past frame.\n3. Moment-bound facts (I am tired) shift normally.\n\n*Why it works:* the backshift marks remoteness; a truth that has not stopped being true is not remote, so exams keep it in the present.",
  "example": {"q": "Select the indirect form: *The teacher said, 'The sun rises in the east.'*", "solution": "**The teacher said that the sun rises in the east.** — a law of nature keeps its present tense. 'Rose in the east' is the classic planted backshift."}},
 {"id": "nts5", "name": "Frozen forms: would rather, used to", "frequency": "occasional",
  "howToSpot": "The quote already contains would/could/used to/had better/would rather; the wrong options re-shift them (had used to, had rather) or break their shape.",
  "formula": None,
  "logic": "1. Spot the unreal/fixed form in the quote.\n2. Copy it unchanged — only the pronoun and time words around it move.\n3. Reject options that add had to them or convert their verb (used to swam).\n\n*Why it works:* these forms are already one step away from the real present; the ladder has no rung below them, so they freeze.",
  "example": {"q": "Select the indirect form: *She said, 'I used to swim every morning.'*", "solution": "**She said that she used to swim every morning.** — used to stays used to; only I → she moves. 'Had used to swim' invents an impossible extra rung."}},
]}

S["narr-pronouns-time-place"] = {
"notes": """### Pronouns: the SONA rule
- **First person (I, we, my, our) follows the reporter** — the subject outside the quotes.
- **Second person (you, your) follows the listener** — the person addressed, usually the object of the reporting verb.
- **Third person (he, she, it, they) never changes.**

*He said to me, 'I will explain the sum to you.'* → He told me that **he** would explain the sum to **me**. The I belongs to the speaker (he), the you to the listener (me). Say the two anchors aloud — reporter and listener — and the mapping writes itself.

Worked grid: *Sita said to Gita, 'You are late.'* → Sita told Gita that **she** was late (you = the listener Gita). *The guests said, 'We enjoyed it.'* → The guests said that **they** had enjoyed it (we = the speakers themselves). Track the speaker's gender too: a female speaker's I becomes **she**, not he.

### The time table — learn it as one block
| Direct | Indirect |
|---|---|
| now | then |
| today | that day |
| tonight | that night |
| tomorrow | the next day / the following day |
| yesterday | the previous day / the day before |
| last night / last week | the previous night / the previous week |
| ago | before |
| hence | thence |
| next Monday / next month | the following Monday / the following month |
| thus | so |

### The place and demonstrative table
| Direct | Indirect |
|---|---|
| this | that |
| these | those |
| here | there |
| come | go |
| bring | take |

*Meet me here tomorrow morning* → he asked me to meet him **there** **the next** morning. Note come → go shifts only when the speaker's viewpoint moves: reporting 'I will come' from elsewhere turns come into go.

### The pairing rule (the real test)
Tense and time words move TOGETHER. An option that writes *would visit ... tomorrow* — modal shifted, time word left — is wrong, and so is *will visit ... the next day*. In a well-set item, one wrong option shifts the verb only, one shifts the time word only, and one shifts both. The one that shifts both is the answer.

### Three pronoun traps planted in options
- Keeping **you/your** inside a told-me sentence — the listener was ignored.
- **Random promotion**: I turned into the wrong person (he instead of she, or her instead of me).
- **Number slips**: we → he instead of they.

### Quick revision
- SONA: 1st person → reporter's subject; 2nd person → the listener; 3rd person untouched.
- tomorrow → the next day; yesterday → the previous day; ago → before; now → then; today → that day; next → the following; last → the previous.
- this → that; these → those; here → there; come → go; bring → take.
- Tense shifted but time word kept (or the reverse) = planted fault; both move together.
- Check the speaker's gender before writing his/her.
""",
"patterns": [
 {"id": "npt1", "name": "SONA pronoun mapping", "frequency": "very common",
  "howToSpot": "The quote has I/we/you/my/your and the options differ only in the pronouns (to me / to you / to him; she was / you were).",
  "formula": None,
  "logic": "1. Name the reporter (subject outside the quotes) — first-person words take its shape.\n2. Name the listener (object of said to/told) — second-person words take its shape.\n3. Third-person words copy straight across; check gender and number before finalising.\n\n*Why it works:* every pronoun in the quote has exactly one anchor — reporter or listener — so the mapping is mechanical, not a matter of taste.",
  "example": {"q": "Select the indirect form: *He said to me, 'I will explain the sum to you.'*", "solution": "**He told me that he would explain the sum to me.** — I anchors to the reporter (he); you anchors to the listener (me). 'To you' forgets the listener; 'that I would explain' swaps the speaker."}},
 {"id": "npt2", "name": "tomorrow / next → the next / the following", "frequency": "very common",
  "howToSpot": "The quote says tomorrow, next week, next Monday; options keep the word as it is or convert it to the next/the following.",
  "formula": None,
  "logic": "1. Scan the quote for forward-pointing time words: tomorrow, next + unit.\n2. Convert: tomorrow → the next day (or the following day); next Monday → the following Monday.\n3. Confirm the verb shifted too (will → would) — the pair must move together.\n\n*Why it works:* forward words are anchored to the day of speaking; once reported later, the anchor moves, so the word must move with it.",
  "example": {"q": "Select the indirect form: *Mother said, 'I will prepare your favourite dish tomorrow.'*", "solution": "**Mother said that she would prepare my favourite dish the next day.** — will → would AND tomorrow → the next day; your → my (the listener is the reporter)."}},
 {"id": "npt3", "name": "yesterday / ago / last → the previous / before", "frequency": "very common",
  "howToSpot": "The quote says yesterday, ago, last night/week; options keep ago/last or use the previous/the day before/the night before.",
  "formula": None,
  "logic": "1. Scan for backward-pointing words: yesterday, ago, last + unit.\n2. Convert: yesterday → the previous day; two years ago → two years before; last Sunday → the previous Sunday.\n3. Check the verb took its step (V2 → had + V3) — ago and ago-keeping options are the planted faults.\n\n*Why it works:* backward words measure from the day of speaking; from the reporter's later vantage point the same gap reads as 'before'.",
  "example": {"q": "Select the indirect form: *The old man said, 'I bought this house forty years ago.'*", "solution": "**The old man said that he had bought that house forty years before.** — bought → had bought; ago → before; this → that. Keeping 'forty years ago' is the planted half-shift."}},
 {"id": "npt4", "name": "here / this / come → there / that / go", "frequency": "common",
  "howToSpot": "The quote contains place words or demonstratives (here, this, these, come, bring); options differ in whether they shifted.",
  "formula": None,
  "logic": "1. Underline this/these/here/come/bring in the quote.\n2. Shift: this → that, these → those, here → there, come → go, bring → take (viewpoint moves to the reporter's place).\n3. Watch the double-that trap: said **that that** mango tree — the conjunction that followed by the demonstrative that is correct English.\n\n*Why it works:* the reporter speaks from a different place than the original speaker, so near-pointing words must become far-pointing ones.",
  "example": {"q": "Select the indirect form: *Grandmother said, 'This mango tree was planted by my grandfather.'*", "solution": "**Grandmother said that that mango tree had been planted by her grandfather.** — this → that; my → her; was planted → had been planted. The double 'that that' is correct, not a typo."}},
]}

S["narr-questions-commands-exclamations"] = {
"notes": """### Four skeletons, four connectors
- **Yes/No question**: asked + **if/whether** + statement order. 'Do you like filter coffee?' → He asked me **if I liked** filter coffee. The do/does/did of the quote dies and its tense lands on the main verb.
- **Wh-question**: asked + **the wh-word itself** + statement order. 'Where are you going?' → She asked me **where I was going**. The wh-word replaces if/whether — never both.
- **Command**: told / ordered + object + **to + V1**. 'Shut the door.' → He told me **to shut** the door. Negative: **not to** + V1. 'Do not shout.' → told him **not to shout**.
- **Request** (please, kindly): requested + object + to + V1. **Advice**: advised + object + to + V1. **Suggestion** (let us): suggested + V-ing, or proposed that they should go.

### Exclamations: read the emotion word first
| Direct marker | Reported frame |
|---|---|
| Hurrah! | exclaimed with joy that |
| Alas! | exclaimed with sorrow that |
| Bravo! | applauded him/her, saying that |
| What a / How + adjective | exclaimed that it was **very** + adjective |
| Good morning / Good night | wished (good night) |
| May you... (blessing/prayer) | prayed / wished that |

'What a beautiful view!' → He **exclaimed that it was a very** beautiful view. The exclamation mark becomes a full stop; the intensity moves into the word very.

### The statement-order test kills half the wrong options
After the connector, English is statement order: asked where he **had gone**, never *where had he gone*; asked if she **was coming**, never *if was she coming*. Combine it with the connector test — asked **that if** he was coming stacks two subordinators and dies on sight. These two faults together account for most planted wrong options in question items.

### Punctuation dies quietly
The question mark and the exclamation mark both become a full stop; the quotes and the comma vanish. An option that ends a reported question with a question mark is wrong even when every word in it is perfect — sweep the last character before the final option check.

### Verb choices that signal the type
asked (questions), ordered/told (commands), requested (please), advised (advice), suggested (let us), exclaimed (exclamations), wished/prayed (greetings, blessings). If the stem is a please-sentence and the option keys *ordered*, the item is over regardless of the tenses.

### Quick revision
- Yes/No → asked + if/whether + statement order; Wh → asked + wh + statement order; never that, never both, no do/does/did.
- Command → told/ordered + object + to + V1; negative → not to + V1; request → requested; advice → advised; let us → suggested + V-ing.
- Hurrah → exclaimed with joy; Alas → exclaimed with sorrow; What a → exclaimed that it was very.
- Reported questions and exclamations end in a full stop.
- Statement order after the connector — sweep every option for inverted auxiliaries first.
""",
"patterns": [
 {"id": "nqc1", "name": "Yes/No question → asked + if/whether", "frequency": "very common",
  "howToSpot": "The quote is answerable by yes or no (Do you...? Is there...? Can you...?); options differ in if/that and in the order after the connector.",
  "formula": None,
  "logic": "1. Detect the yes/no shape (an auxiliary or do leads the quote).\n2. Frame: asked + listener + if/whether + statement order, with do/does/did removed and the tense landed on the main verb.\n3. Reject that-connectors, inverted orders (if was he), and retained do-forms.\n\n*Why it works:* if/whether is the only subordinator that reports a closed question; everything else either mislabels the question or breaks the order.",
  "example": {"q": "Select the indirect form: *My aunt said to me, 'Do you like filter coffee?'*", "solution": "**My aunt asked me if I liked filter coffee.** — do dies, liked carries the past; you → I (listener = reporter). 'If did I like' keeps the do and inverts the order."}},
 {"id": "nqc2", "name": "Wh-question → asked + wh + statement order", "frequency": "very common",
  "howToSpot": "The quote opens with why/where/when/what/who/how; the wrong options invert the auxiliary (why did I) or stack that before the wh-word.",
  "formula": None,
  "logic": "1. Copy the wh-word as the connector — nothing before it (no that).\n2. Restore statement order: wh + subject + verb, backshifted one rung.\n3. Delete do/does/did; the past lands on the main verb (do you want → I wanted).\n\n*Why it works:* a reported wh-question is a noun clause in statement shape; keeping the question order is the single most planted fault in the section.",
  "example": {"q": "Select the indirect form: *The interviewer asked me, 'Why do you want this job?'*", "solution": "**The interviewer asked me why I wanted that job.** — do dies (want → wanted); you → I; this → that. 'Why did I want' keeps both the do and the inversion."}},
 {"id": "nqc3", "name": "Command → told/ordered + object + to + V1", "frequency": "very common",
  "howToSpot": "The quote is a bare order, often negative (Do not...); options differ in to/not to placement, or keep the imperative verb bare.",
  "formula": None,
  "logic": "1. Positive order: ordered/told + object + to + V1.\n2. Negative order: not goes BEFORE to — not to make a noise.\n3. this/these in the order shift to that/those; the tone verb must match (order, not request).\n\n*Why it works:* the infinitive is the only frame that reports an order; the negative particle always sits outside the to, never inside the verb phrase.",
  "example": {"q": "Select the indirect form: *The teacher said to the boys, 'Do not make a noise in the library.'*", "solution": "**The teacher ordered the boys not to make a noise in the library.** — the negative rides before to; make stays a base verb. 'Not making' breaks the frame; dropping not reverses the order."}},
 {"id": "nqc4", "name": "Request and advice frames", "frequency": "common",
  "howToSpot": "The quote carries please/kindly (request) or advice sense (Give up..., Always speak...); the options verb between requested/advised/ordered.",
  "formula": None,
  "logic": "1. please/kindly → requested + object + to + V1.\n2. Advice → advised + object + to + V1 (always/never ride before the verb: advised him always to speak...).\n3. The listener is compulsory and in the object case: requested the doctor, never requested to the doctor.\n\n*Why it works:* requests and advice share the to-infinitive frame with orders; only the reporting verb separates them, so the verb is where the item is decided.",
  "example": {"q": "Select the indirect form: *The patient said to the doctor, 'Please prescribe a milder tablet.'*", "solution": "**The patient requested the doctor to prescribe a milder tablet.** — please → requested; the doctor is the object of requested, not of a stray to. 'Ordered the doctor' hardens a plea into a command."}},
 {"id": "nqc5", "name": "Exclamation → exclaimed with joy/sorrow that", "frequency": "common",
  "howToSpot": "The quote carries Hurrah/Alas/What a/How; options differ in joy/sorrow, in exclaimed vs said, and in the very-conversion of What a.",
  "formula": None,
  "logic": "1. Read the emotion word: Hurrah → with joy; Alas → with sorrow; Bravo → applauded...saying.\n2. Frame: exclaimed with joy/sorrow + that + statement (backshifted).\n3. What a/How + adjective → it was very + adjective; the exclamation mark becomes a full stop.\n\n*Why it works:* the reported frame must carry the same emotion as the quote; joy and sorrow are the classic planted swap.",
  "example": {"q": "Select the indirect form: *The players said, 'Hurrah! We have clinched the series.'*", "solution": "**The players exclaimed with joy that they had clinched the series.** — joy for Hurrah; have clinched → had clinched. 'With sorrow' reverses the emotion; 'said with joy' loses the exclamation frame."}},
]}

S["narr-strategy"] = {
"notes": """### The four-check protocol (run it in this order)
1. **Connector**: that / if-whether / the wh-word / to + V1 — must match the sentence type, and there must be exactly one.
2. **Reporting verb**: said to + listener → told/asked; the tone must match (requested vs ordered vs advised vs exclaimed vs suggested).
3. **Tense ladder**: one rung down for a past frame; past perfect stays; universal truths stay; would/could/might/should/used to freeze.
4. **Pronouns + time/place**: SONA mapping; the tomorrow→the next day family; this→that, here→there.

Work in this order because connector faults are the cheapest to see — you can kill two options in five seconds without reading a verb. In a well-set item every wrong option breaks exactly one check, so name the check that killed it.

### Reverse conversion (indirect → direct)
1. Put the reporting verb back with its comma and quotes: told me → said to me, '...'
2. Remove the connector: that disappears; if/whether becomes an auxiliary-led question (Are you...?); the wh-word stays but question order returns.
3. Step the tense back UP one rung: had + V3 → V2; was + V-ing → is/am + V-ing; would → will; could → can; had to → must.
4. Reverse the pronouns (SONA backwards): told me he → 'I'; told her that she → 'you'.
5. Restore the final punctuation: ? for questions, ! for exclamations.

*Told the students that the earth revolves around the sun* → **said to the students, 'The earth revolves around the sun.'** Note the universal truth did not need un-shifting — that is exactly why the exam picks it.

### Planted faults, ranked by how often they appear
1. Statement order broken: *asked if was he coming*.
2. Half-backshift: *said that he is busy*.
3. Tense shifted but the time word left behind: *would visit tomorrow*.
4. told with no object, or requested **to** the doctor.
5. Connector stacking: *asked that why*, *told that to come*.
6. Stray punctuation: a reported question still ending in a question mark.
7. Wrong tone verb: please keyed as ordered; Hurrah keyed as sorrow.

### The 25-second routine
Read the direct sentence and name its TYPE before touching the options — statement, yes/no, wh, command, request, exclamation. Pre-write the skeleton in your head: *asked if + was...* or *ordered + object + not to...*. Then match options against the skeleton, one check at a time, first match to all four checks wins. Ten items a day for a week makes the ladder automatic; after that the section is free marks.

### Quick revision
- Four checks in order: connector → reporting verb → tense ladder → pronouns/time.
- Reverse: quotes and comma back, connector out, tense up one rung, pronouns back, punctuation restored.
- Top faults: inverted order after the connector, half-backshift, time word left behind, object-less told, double connector, stray question mark.
- Name the sentence TYPE first; pre-write the skeleton; then read the options.
- Every wrong option breaks exactly one check — name it and move on.
""",
"patterns": [
 {"id": "nst1", "name": "Four-check elimination on a full item", "frequency": "very common",
  "howToSpot": "A straightforward statement item where each wrong option fails a different check — one keeps said to, one skips the backshift, one keeps yesterday.",
  "formula": None,
  "logic": "1. Connector first: told + listener + that is mandatory for a statement with a named listener.\n2. Tense ladder: every verb steps one rung (was → had been).\n3. Time words: yesterday → the previous day.\n4. Pronouns: SONA (I → he, my → his/her).\n\n*Why it works:* running the checks in a fixed order turns a four-way comparison into four yes/no questions, each settled in a glance.",
  "example": {"q": "Select the indirect form: *The manager said to the clerk, 'You were absent yesterday.'*", "solution": "**The manager told the clerk that he had been absent the previous day.** — told (not said to); were → had been; yesterday → the previous day; you → he. Each wrong option drops exactly one of these."}},
 {"id": "nst2", "name": "Reverse conversion (indirect to direct)", "frequency": "common",
  "howToSpot": "The stem is already reported and the options are direct quotes; they differ in quotes/comma, in the un-shift, and in question order.",
  "formula": None,
  "logic": "1. Rebuild the frame: said to + listener, comma, quotes.\n2. Drop the connector; for reported questions, restore auxiliary-first order and the question mark.\n3. Step the tense up one rung (had + V3 → V2; would → will); frozen forms (revolves for a truth) stay.\n4. Reverse the pronouns before closing the quote.\n\n*Why it works:* the direct form must reproduce what the speaker plausibly said — every reported-layer word (that, had, would) has to dissolve back.",
  "example": {"q": "Select the direct form: *The teacher told the students that the earth revolves around the sun.*", "solution": "**The teacher said to the students, 'The earth revolves around the sun.'** — quotes return, that vanishes, and the universal truth keeps its present. 'That the earth...' left inside quotes is the planted fault."}},
 {"id": "nst3", "name": "Connector-stacking and modal-question faults", "frequency": "common",
  "howToSpot": "Polite questions (Shall I...?, Could you...?) reported with that if, or with the modal kept as will/can.",
  "formula": None,
  "logic": "1. Shall I...? (seeking instruction) → asked + if + should/might + V1; Could you...? → asked + if + could + V1.\n2. Exactly one connector; now/then-type shifts ride along (now → then).\n3. The modal must step down (will → would, can → could), never stay put and never leap to must.\n\n*Why it works:* polite-question items stack three checks at once — connector, modal, time word — so each option fails a different one.",
  "example": {"q": "Select the indirect form: *The clerk said to the manager, 'Shall I close the register now?'*", "solution": "**The clerk asked the manager if he should close the register then.** — Shall I → if he should; now → then. 'That if' stacks connectors; 'if he will close' skips the modal shift."}},
 {"id": "nst4", "name": "Statement-order and punctuation sweep", "frequency": "common",
  "howToSpot": "Wh-question items where two options share every word but one inverts the auxiliary (when would the rains vs when the rains would) or keeps a final question mark.",
  "formula": None,
  "logic": "1. After the wh-word, demand subject + verb: asked when the rains WOULD come.\n2. Kill inverted orders (when would the rains come) instantly.\n3. Sweep the final character: a reported question ends in a full stop, never a question mark.\n\n*Why it works:* order and punctuation faults are invisible when reading for meaning, so they must be checked mechanically, word-position by word-position.",
  "example": {"q": "Select the indirect form: *The child asked her mother, 'When will the rains come?'*", "solution": "**The child asked her mother when the rains would come.** — will steps to would and moves AFTER the subject; the question mark becomes a full stop. Both faults sit in the decoys."}},
 {"id": "nst5", "name": "Modal + time-word double check", "frequency": "common",
  "howToSpot": "Items where the quote carries a modal (may, could have) AND a time word (next week, yesterday); wrong options fix one and forget the other.",
  "formula": None,
  "logic": "1. Handle the modal first: may → might; could have stays could have (frozen).\n2. Handle the time word second: next week → the following week; yesterday → the previous day.\n3. Verify BOTH moved — the partial-shift option is the planted trap.\n\n*Why it works:* setters split the shift across two dimensions; candidates who check only the tense fall for the untouched time word.",
  "example": {"q": "Select the indirect form: *The coach said, 'The trials may be postponed till next week.'*", "solution": "**The coach said that the trials might be postponed till the following week.** — may → might AND next week → the following week. Either shift alone is the planted half-answer."}},
]}
