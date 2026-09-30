"""Readable rewrite of English > Direct & Indirect Speech (all 5 subtopics).

Plain English, short sentences, tables for word maps, one method per question type.
Every fact from the old notes is kept; new pattern ids continue each subtopic's prefix.
Run: python direct_indirect.py  (patches content/core/topics/english/direct-indirect.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "direct-indirect.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Reporting verbs
# =====================================================================
SUBS["narr-reporting-verb"] = dict(
    concept=(
        "*Direct speech* quotes the speaker's exact words inside inverted commas. "
        "*Indirect speech* (also called reported speech) tells the same words in your own sentence. "
        "The quotes and the comma go, a joining word like *that* comes in, and the reporting verb often changes. "
        "So the first job is to pick the right reporting verb and the right joining word."
    ),
    notes=r"""### What changes when you report speech
Direct: *She said to me, "I am tired."*
Indirect: *She told me that she was tired.*

Three things change every time:

1. The comma and the inverted commas go. A **connector** (joining word) takes their place.
2. The **reporting verb** often changes: *said to* becomes *told*.
3. A question loses its question order. It becomes a plain statement.

> **Rule:** Fix the reporting verb and the connector first. Then work on tense, pronouns and time words.

### Say and tell
- **Tell needs a listener:** told me, told us, told him.
- **Say needs no listener:** *He said that he was late.*
- **said to + person** becomes **told + person**: *He said to me* becomes *He told me*.

> **Watch:** *Said me* does not exist. *Told that he was late* (no listener) is also wrong in exam English. *Told to the staff* is wrong too. Write *told the staff*.

### The tone of the quote picks the verb
Read the quoted words and name their tone. Then pick the matching verb.

| Tone of the quote | Reporting verb | What follows |
|---|---|---|
| Statement | told / said | that |
| Yes/No question | asked | if / whether |
| Wh-question | asked | the wh-word itself |
| Order | ordered / told + person | to + V1 |
| Request (please, kindly) | requested | to + V1 |
| Advice | advised | to + V1 |
| Suggestion (let us) | suggested / proposed | V-ing, or that ... should |
| Hurrah! (joy) | exclaimed with joy | that |
| Alas! (sorrow) | exclaimed with sorrow | that |
| Wish or prayer | wished / prayed | that |

> **Tip:** A please-sentence reported with *ordered* is wrong, even if every tense is perfect. Exams plant exactly this.

### When the reporting verb is in the present
If the reporting verb is present (*says, asks, has said*) or future (*will say*), the tense inside the quote does not move.

*He says, "I am busy."* becomes *He says that he **is** busy.*

Only the pronoun changes here. An option with *was* or *would* is the planted fault. Watch for *says* quietly turned into *said*.

### One connector only
- Statements take **that**.
- Yes/No questions take **if** or **whether**. Never *that*.
- Orders, requests and advice take **to + base verb**. Never *that*.

Use exactly one connector. *Asked that if* and *told that to come* are always wrong.

### Other small changes
- The inverted commas, the comma and the question mark all disappear.
- The capital letter of the quote is dropped. The reported sentence ends with a full stop.
- The listener stays in the object form: told **me**, asked **him**, requested **her**.
- With a general truth, *that* is still the connector: *He said that honesty is the best policy.*
""",
    tricks=[
        {"title": "Read the tone first",
         "body": "Before you touch tense or pronouns, name the tone of the quote: order, advice, request, question, joy or sorrow. The matching verb alone often removes two options.",
         "example": {"q": "The coach said to the players, 'Please arrive by six.' Which reporting verb fits?",
                     "steps": ["The word 'please' marks a request.", "A request takes 'requested + person + to + V1'.",
                               "'Ordered' is too harsh and 'advised' changes the meaning."],
                     "answer": "requested"}},
        {"title": "said to or told",
         "body": "Use *said to* + person, or *told* + person. Never mix them. Any option with *said me* or *told to me* is wrong."},
        {"title": "Connector test",
         "body": "Statement: that. Yes/No question: if or whether. Wh-question: the wh-word alone. Order, request, advice: to + V1."},
    ],
    mistakes=[
        mis("Writing 'He said me' or 'told to me'.", "Say 'said to me' or 'told me'. Tell takes its listener directly."),
        mis("Using 'asked that' for a yes/no question.", "Use 'asked if' or 'asked whether'."),
        mis("Keeping the inverted commas or the comma after the reporting verb.", "Remove them. Write the reported words as a plain clause."),
        mis("Using 'ordered' for a polite request.", "Match the tone: please = requested, advice = advised."),
        mis("Backshifting the tense when the reporting verb is 'says'.", "A present or future reporting verb means the tense stays the same."),
    ],
    revision=[
        "said to + person becomes told + person. Tell always has a listener; say does not.",
        "Statement: that. Yes/No: if or whether. Wh: the wh-word. Order, request, advice: to + V1.",
        "Hurrah: exclaimed with joy. Alas: exclaimed with sorrow.",
        "Present or future reporting verb (says, asks, will say): no tense change inside.",
        "Use one connector only. That never pairs with if, whether or to.",
        "Write told the staff, not told to the staff.",
    ],
    patterns=[
        pat("nrv1", "said to + listener becomes told + listener", "very common",
            "The quote is a statement. The stem has 'said to me / him / us'. One option keeps 'said to'; another drops the listener after told.",
            ["Spot 'said to' + a person. It must become told + that person.", "Add the connector 'that'.",
             "Then check tense, pronouns and time words.", "Reject options that keep 'said to', or use told with no listener."],
            "Say never takes a listener while tell must, so each wrong option forgets one of these.",
            "Select the indirect form: *She said to me, 'I am very busy today.'*",
            ["'Said to me' becomes 'told me'.", "Add 'that'.", "am becomes was; I becomes she; today becomes that day."],
            "She told me that she was very busy that day."),
        pat("nrv2", "Tone decides the reporting verb", "very common",
            "The quote has 'please' or 'kindly', an order, advice or a suggestion. The options differ mainly in the reporting verb.",
            ["Name the tone: please = request, command = order, advice, let us = suggestion.",
             "Attach the frame: requested / ordered / advised + person + to + V1; suggested + V-ing.",
             "Reject options whose tense is right but whose verb is the wrong tone."],
            "Each tone has one matching verb, so the verb can settle the answer before you compare tenses.",
            "Select the indirect form: *The doctor said to Father, 'Give up smoking.'*",
            ["The doctor is giving advice.", "Advice takes 'advised + person + to + V1'.",
             "'Requested' makes it a favour; 'ordered' makes it a command."],
            "The doctor advised Father to give up smoking."),
        pat("nrv3", "Present reporting verb: no backshift", "common",
            "The frame is 'says', 'often says', 'has said' or 'will say'. One option changes the tense; the right one keeps it.",
            ["Check the tense of the reporting verb first.", "Present or future frame: keep the tense of the quote.",
             "Change only the pronouns.", "Reject options that turn says into said."],
            "Backshift shows that time has passed. A present reporting verb has no gap in time, so nothing moves back.",
            "Select the indirect form: *Ravi says, 'I do not like loud music.'*",
            ["'Says' is present, so the tense stays.", "Only the pronoun changes: I becomes he.", "do not like stays as does not like."],
            "Ravi says that he does not like loud music."),
        pat("nrv4", "One connector, the right one", "common",
            "Options stack two connectors (asked that if, told that to). Or a reported question keeps do / does / did.",
            ["Match the type: statement = that; yes/no = if or whether; wh = the wh-word alone; order = to + V1.",
             "Count the connectors. Only one is allowed.",
             "In a reported question, remove do / does / did. The tense goes on the main verb."],
            "One clause takes one connector. Stacking two, or keeping a helper verb with nothing to do, is always wrong.",
            "Select the indirect form: *Priya asked me, 'Are you coming to the fair?'*",
            ["It is a yes/no question, so use 'if'.", "After 'if', use statement order: I was coming.",
             "'Asked me that if' has two connectors. 'If was I coming' has the wrong order."],
            "Priya asked me if I was coming to the fair."),
        pat("nrv5", "Suggestion with let us", "common",
            "The quote starts with 'Let us' or 'Let's'. Options mix suggested, ordered and told.",
            ["Spot 'Let us' or 'Let's'. It is a suggestion.", "Use 'suggested + V-ing' or 'suggested that they should + V1'.",
             "Reject 'ordered' and 'told', and reject 'suggested to go'."],
            "'Let us' invites the listener to join in. It is neither an order nor advice.",
            "Select the indirect form: *Meena said to us, 'Let us plant some trees.'*",
            ["'Let us' is a suggestion, so the verb is 'suggested'.", "Use the -ing form: planting.",
             "Or use 'that we should plant'."],
            "Meena suggested planting some trees."),
    ],
)

# =====================================================================
# 2. Tense shift
# =====================================================================
SUBS["narr-tense-shift"] = dict(
    concept=(
        "When the reporting verb is in the past (*said, told, asked*), every verb inside the quote moves **one step back** in time. "
        "*Am* becomes *was*. *Will* becomes *would*. *Wrote* becomes *had written*. "
        "There are two exceptions: a general truth keeps its tense, and some forms never move."
    ),
    notes=r"""### The ladder: one step back
This applies when the reporting verb is past: said, told, asked. Every verb steps down one rung.

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
| have to | had to |

> **Example:** *"I am writing a letter"* becomes *he said he **was writing** a letter*. *"I wrote it"* becomes *he said he **had written** it*.

### The ceiling
A quote already in the past perfect stays as it is. *"The train had left"* becomes *he said the train **had left***. The same holds for the past perfect continuous. There is no rung above it.

### Forms that never move
These are already one step from the present, so they do not shift again:

- would, could, should, might, ought to
- used to, had better, would rather

*"I would rather stay home"* becomes *he said he **would rather stay** home*. Only the pronouns around them change.

> **Rule:** If the quote already has one of these forms, copy it unchanged.

### General truths keep their tense
A fact of nature, a habit or a proverb is still true, so it does not move back.

*"The earth revolves around the sun"* becomes *the teacher said that the earth **revolves** around the sun*.

A moment-bound fact does shift: *"I am tired"* becomes *he said he was tired*.

### Two faults planted in options
- **Half-backshift:** the frame is *said*, but the quote still has *is, are, will* or *can*. This is the most common wrong option.
- **Over-backshift:** *"I am tired"* reported as *he had been tired*. That is two steps. Simple present goes to simple past only.

### Time words move with the tense
When the verb steps back, the time words step back too: tomorrow to the next day, now to then, ago to before. Never move one and leave the other.

### A full example, step by step
*The clerk said, "I have finished the file, and I will send it tomorrow."*

1. The reporting verb is *said*, so the quote steps back.
2. *Have finished* becomes *had finished*.
3. *Will send* becomes *would send*.
4. *Tomorrow* becomes *the next day*. *I* becomes *he*.

Result: *The clerk said that he had finished the file and would send it the next day.*

### Which verbs to check
Look at every verb in the quote, not just the first. A quote with two verbs needs two shifts. Also check whether the reporting verb is past or present before you begin.

> **Watch:** *Must* for duty becomes *had to*. *"I must reach by six"* becomes *he said he had to reach by six*. *Must* for a guess can stay *must*.
""",
    tricks=[
        {"title": "Say the ladder aloud",
         "body": "Present goes to past. Present continuous goes to past continuous. Perfect goes to past perfect. Past goes to past perfect. Will goes to would. Can goes to could. May goes to might. Must (duty) goes to had to."},
        {"title": "Frozen five",
         "body": "Could, would, should, might and ought to never change. If the quote has one of these, its tense is already right. Any shift is an error.",
         "example": {"q": "Select the indirect form: *He said, 'I could swim well as a child.'*",
                     "steps": ["The quote has 'could', a frozen form.", "Only the pronoun changes: I becomes he.",
                               "'as a child' is not a time word that shifts."],
                     "answer": "He said that he could swim well as a child."}},
        {"title": "Truth test",
         "body": "Is the quote a law of nature, a habit or a proverb? Then do not backshift. Write: said that the earth revolves."},
    ],
    mistakes=[
        mis("Moving a past perfect verb up again (had had written).", "Past perfect is the ceiling. It stays the same."),
        mis("Backshifting a law of nature: 'the sun rose in the east'.", "A general truth keeps its present tense."),
        mis("Turning 'must' into 'musted'.", "Must (duty) becomes 'had to'. A guess can stay 'must'."),
        mis("Changing 'could' back to 'can' or forward to 'had could'.", "Could, would, should, might and ought to stay as they are."),
        mis("Shifting the verb but leaving 'tomorrow' or 'today' in the sentence.", "Move the tense and the time word together."),
    ],
    revision=[
        "One step back: am to was; write to wrote; was writing to had been writing; wrote to had written.",
        "will to would; can to could; may to might; must (duty) to had to.",
        "Past perfect stays past perfect.",
        "No shift for general truths, a present reporting verb, and would, could, should, might, ought to, used to, had better, would rather.",
        "Half-backshift and over-backshift are the two planted faults. Count the steps.",
        "If the verb moved, the time word must move too.",
    ],
    patterns=[
        pat("nts1", "Present to past: the first step", "very common",
            "The quote is in the simple present or present continuous. Options show was / were (correct), had been (too far) or is / are (no shift).",
            ["Confirm that the reporting verb is past.", "Step down once: am / is + V-ing becomes was / were + V-ing; V1 becomes V2.",
             "Reject the unshifted present and the over-shifted past perfect continuous."],
            "This first step is the most tested row. Its two wrong neighbours are always in the options.",
            "Select the indirect form: *He said, 'I am learning German these days.'*",
            ["'Am learning' steps to 'was learning'.", "'These days' becomes 'those days'.", "'Had been learning' is two steps."],
            "He said that he was learning German those days."),
        pat("nts2", "Past to past perfect: the second step", "very common",
            "The quote has a simple past or a past continuous verb. Options offer the unshifted past, the had-forms, or a present perfect.",
            ["Simple past (V2) becomes had + V3.", "Past continuous (was / were + V-ing) becomes had been + V-ing.",
             "A quote already in the past perfect does not move."],
            "The reported event must read as earlier than the act of reporting.",
            "Select the indirect form: *The watchman said, 'The lights were flickering all night.'*",
            ["'Were flickering' is past continuous.", "It steps to 'had been flickering'.", "'Had flickered' turns it into a finished act."],
            "The watchman said that the lights had been flickering all night."),
        pat("nts3", "Modal shifts (will, can, may, must)", "very common",
            "The quote has will, can, may or must. Options give the unshifted modal, a wrong neighbour, or the correct partner.",
            ["Use the row: will / shall to would / should; can to could; may to might; must (duty) to had to.",
             "Leave the rest of the verb phrase alone.", "Check the time word in the same sweep."],
            "Each modal has one partner one step back. Anything else is a planted neighbour.",
            "Select the indirect form: *She said, 'I can solve this puzzle.'*",
            ["'Can' steps to 'could'.", "'This' becomes 'that'.", "'May solve' brings in the wrong modal."],
            "She said that she could solve that puzzle."),
        pat("nts4", "No backshift: general truth", "common",
            "The quote is a law of nature, a proverb or a permanent fact. One option backshifts it; the right one keeps the present.",
            ["Ask: is this always true, or true only at the moment of speaking?", "Always true: keep the tense, even after 'said'.",
             "True only now (I am tired): shift as usual."],
            "Backshift marks a gap in time. A fact that is still true has no gap.",
            "Select the indirect form: *The teacher said, 'The sun rises in the east.'*",
            ["The sun rising in the east is a law of nature.", "So the present tense stays.", "'Rose in the east' is the planted backshift."],
            "The teacher said that the sun rises in the east."),
        pat("nts5", "Frozen forms: would rather, used to", "occasional",
            "The quote already has would, could, used to, had better or would rather. The wrong options shift them again.",
            ["Spot the frozen form in the quote.", "Copy it unchanged.", "Change only the pronouns and the time words around it.",
             "Reject 'had used to', 'had rather' and similar."],
            "These forms are already one step from the present, so there is no rung below them.",
            "Select the indirect form: *She said, 'I used to swim every morning.'*",
            ["'Used to' is a frozen form.", "Only the pronoun changes: I becomes she.", "'Had used to swim' does not exist."],
            "She said that she used to swim every morning."),
    ],
)

# =====================================================================
# 3. Pronouns and time/place words
# =====================================================================
SUBS["narr-pronouns-time-place"] = dict(
    concept=(
        "Pronouns change by who is speaking to whom. This is the **SONA** rule. "
        "**S**ubject-side words (first person) follow the reporter, **O**bject-side words (second person) follow the listener, "
        "and **N**o change for the third person. Words tied to the speaker's *now* and *here* also change. "
        "*Tomorrow* becomes *the next day* and *here* becomes *there*."
    ),
    notes=r"""### Pronouns: the SONA rule
- **First person (I, we, my, our)** follows the **reporter**. The reporter is the subject outside the quotes.
- **Second person (you, your)** follows the **listener**. The listener is the person spoken to, usually the object of the reporting verb.
- **Third person (he, she, it, they)** never changes.

> **Example:** *He said to me, "I will explain the sum to you."* becomes *He told me that **he** would explain the sum to **me**.* The I is the speaker (he). The you is the listener (me).

More examples:
- *Sita said to Gita, "You are late."* becomes *Sita told Gita that **she** was late.* The you is Gita.
- *The guests said, "We enjoyed it."* becomes *The guests said that **they** had enjoyed it.*

> **Tip:** Say the two anchors aloud first: who is the reporter, who is the listener. Check the speaker's gender too. A woman's I becomes *she*.

### Time words
Learn this as one block.

| Direct | Indirect |
|---|---|
| now | then |
| today | that day |
| tonight | that night |
| tomorrow | the next day / the following day |
| yesterday | the previous day / the day before |
| last week / last night | the previous week / the previous night |
| next month / next Monday | the following month / the following Monday |
| ago | before |
| hence | thence |
| thus | so |

### Place words and pointing words

| Direct | Indirect |
|---|---|
| this | that |
| these | those |
| here | there |
| come | go |
| bring | take |

*Meet me here tomorrow morning* becomes *he asked me to meet him **there** the next morning*.

*Come* becomes *go* only when the reporter stands in a different place from the speaker.

### Tense and time words move together
> **Watch:** *Would visit ... tomorrow* is wrong. The modal moved but the time word did not. *Will visit ... the next day* is wrong too.

In a well-set item, one option shifts only the verb, one shifts only the time word, and one shifts both. The one that shifts both is the answer.

### Present reporting verb
If the reporting verb is present, neither the tense nor the time words change.

*He says, "I am busy today."* becomes *He says that he is busy today.*

### A full example, step by step
*Anil said to Beena, "I will bring your book here tomorrow."*

1. Reporter: Anil. Listener: Beena.
2. *I* becomes *he*. *Your* becomes *her*.
3. *Will bring* becomes *would bring*. *Here* becomes *there*.
4. *Tomorrow* becomes *the next day*.

Result: *Anil told Beena that he would bring her book there the next day.*

### Pronoun faults planted in options
- Keeping *you* or *your* in a told-me sentence. The listener was ignored.
- Wrong person: *he* instead of *she*, or *her* instead of *me*.
- Wrong number: *we* becomes *he* instead of *they*.
""",
    tricks=[
        {"title": "SONA sweep",
         "body": "Mark the three anchors before you change anything. First person goes to the reporter. Second person goes to the listener. Third person stays. Most wrong options break exactly one of these.",
         "example": {"q": "Select the indirect form: *Ravi said to Sunil, 'You must bring your notes.'*",
                     "steps": ["The listener is Sunil, so 'you' becomes 'he'.", "'Your' becomes 'his'.", "must (duty) becomes had to."],
                     "answer": "Ravi told Sunil that he had to bring his notes."}},
        {"title": "Yesterday and tomorrow pair",
         "body": "Yesterday becomes the previous day. Tomorrow becomes the next day. If the option shifts the verb but keeps the old time word, it is wrong."},
        {"title": "Check the reporting verb first",
         "body": "If the reporting verb is 'says' (present), nothing shifts: not the tense, not the time words. Only the pronouns follow SONA."},
    ],
    mistakes=[
        mis("Leaving 'you' unchanged when the listener is named.", "Second person becomes the listener: Ram becomes he."),
        mis("Keeping 'yesterday' or 'tomorrow' inside reported speech.", "Write the previous day and the next day."),
        mis("Changing 'this' to 'the'.", "This becomes that, and these becomes those."),
        mis("Shifting tenses when the reporting verb is present.", "With says or asks, tense and time words stay as spoken."),
        mis("Changing a third-person pronoun.", "He, she, it and they never change."),
    ],
    revision=[
        "SONA: first person follows the reporter, second person follows the listener, third person stays.",
        "now to then; today to that day; tomorrow to the next day; yesterday to the previous day.",
        "ago to before; last to the previous; next to the following.",
        "this to that; these to those; here to there; come to go; bring to take.",
        "Tense and time word move together. If only one moved, the option is wrong.",
        "Check the speaker's gender before writing his or her.",
    ],
    patterns=[
        pat("npt1", "SONA pronoun mapping", "very common",
            "The quote has I, we, you, my or your. Options differ mainly in the pronouns (to me / to you / to him).",
            ["Name the reporter, the subject outside the quotes. First-person words follow it.",
             "Name the listener, the object of said to / told. Second-person words follow it.",
             "Copy third-person words. Check gender and number."],
            "Every pronoun in the quote has one anchor, so the mapping is mechanical.",
            "Select the indirect form: *He said to me, 'I will explain the sum to you.'*",
            ["I is the speaker, so it becomes 'he'.", "You is the listener, so it becomes 'me'.", "will becomes would."],
            "He told me that he would explain the sum to me."),
        pat("npt2", "tomorrow / next becomes the next / the following", "very common",
            "The quote says tomorrow, next week or next Monday. Options keep the word or change it.",
            ["Scan for forward words: tomorrow, next + a unit of time.",
             "Change: tomorrow to the next day; next Monday to the following Monday.", "Check that the verb moved too (will to would)."],
            "These words are measured from the day of speaking. When the report is made later, the anchor moves.",
            "Select the indirect form: *Mother said, 'I will prepare your favourite dish tomorrow.'*",
            ["Will becomes would.", "Tomorrow becomes the next day.", "Mother is the reporter, so 'I' becomes 'she'. 'Your' becomes 'my'."],
            "Mother said that she would prepare my favourite dish the next day."),
        pat("npt3", "yesterday / ago / last becomes the previous / before", "very common",
            "The quote says yesterday, ago or last night / week. Options keep ago or last, or use the previous / the day before.",
            ["Scan for backward words: yesterday, ago, last + a unit of time.",
             "Change: yesterday to the previous day; two years ago to two years before; last Sunday to the previous Sunday.",
             "Check the verb: V2 becomes had + V3."],
            "Backward words also count from the day of speaking. Later, the same gap reads as 'before'.",
            "Select the indirect form: *The old man said, 'I bought this house forty years ago.'*",
            ["Bought becomes had bought.", "Ago becomes before.", "This becomes that."],
            "The old man said that he had bought that house forty years before."),
        pat("npt4", "here / this / come becomes there / that / go", "common",
            "The quote has place words or pointing words (here, this, these, come, bring). Options differ in whether they moved.",
            ["Underline this, these, here, come and bring.", "Change: this to that; these to those; here to there; come to go; bring to take.",
             "'Said that that' is correct English when the second 'that' points at something."],
            "The reporter stands in a different place, so near words become far words.",
            "Select the indirect form: *Grandmother said, 'This mango tree was planted by my grandfather.'*",
            ["This becomes that.", "Was planted becomes had been planted.", "My becomes her."],
            "Grandmother said that that mango tree had been planted by her grandfather."),
        pat("npt5", "Third person stays and gender check", "common",
            "The quote names a third person (he, she, they). Options change these pronouns or give the speaker the wrong gender.",
            ["Copy every third-person pronoun as it is.", "Change only I / we and you / your.", "Check the gender of the speaker for I and my."],
            "Third-person words already point to someone outside the conversation, so the reporter's view makes no difference.",
            "Select the indirect form: *Kavita said to Rohan, 'I have met your brother, and he is very helpful.'*",
            ["I is Kavita, so it becomes 'she'.", "Your is Rohan's, so it becomes 'his'.", "He stays 'he'. Have met becomes had met."],
            "Kavita told Rohan that she had met his brother and he was very helpful."),
    ],
)

# =====================================================================
# 4. Questions, commands and exclamations
# =====================================================================
SUBS["narr-questions-commands-exclamations"] = dict(
    concept=(
        "Each sentence type has its own skeleton. "
        "A **question** becomes *asked + if / wh-word + statement order*. "
        "A **command** becomes *told / ordered + person + to + verb*. "
        "An **exclamation** becomes *exclaimed with joy / sorrow that ...*. "
        "Pick the skeleton first. Then fill it with the tense, pronoun and time-word changes."
    ),
    notes=r"""### Four skeletons
- **Yes/No question:** asked + **if / whether** + statement order.
  *"Do you like filter coffee?"* becomes *He asked me **if I liked** filter coffee.*
  The do / does / did of the quote goes. Its tense lands on the main verb.
- **Wh-question:** asked + **the wh-word** + statement order.
  *"Where are you going?"* becomes *She asked me **where I was going**.*
  Never add *if* to a wh-question.
- **Command:** told / ordered + person + **to + V1**.
  *"Shut the door."* becomes *He told me **to shut** the door.*
  A negative command uses **not to**: *"Do not shout."* becomes *told him **not to shout***.
- **Request and advice:** requested / advised + person + to + V1.

> **Rule:** After the connector, write statement order. Say *asked where he had gone*, never *asked where had he gone*.

### Suggestions and permission
- **Let us** (suggestion): *suggested + V-ing*. *"Let us go for a walk"* becomes *He suggested going for a walk*. Or use *suggested that they should go*.
- **Let me** (asking permission): *"Let me sit here"* becomes *He requested that he might be allowed to sit there*.

### Exclamations
Read the emotion word first.

| Direct marker | Reported frame |
|---|---|
| Hurrah! | exclaimed with joy that |
| Alas! | exclaimed with sorrow that |
| Bravo! | applauded him, saying that |
| What a / How + adjective | exclaimed that it was a very + adjective |
| Good morning / Good night | wished him a good morning |
| Thank you | thanked him |
| May you ... (a blessing) | prayed / wished that |

*"What a beautiful view!"* becomes *He exclaimed that it was a very beautiful view.* The exclamation mark becomes a full stop. The strong feeling moves into the word *very*.

### A full example, step by step
*Rekha said to him, "What did you buy yesterday?"*

1. It is a wh-question, so the verb is *asked* and the connector is *what*.
2. Use statement order: *what he bought*. Then step back: *bought* becomes *had bought*.
3. *You* becomes *he*. *Yesterday* becomes *the day before*.

Result: *Rekha asked him what he had bought the day before.*

### Punctuation
The question mark and the exclamation mark both become a full stop. An option that ends a reported question with a question mark is wrong, even if every word is right.

> **Watch:** Two faults appear in most wrong options: the question order kept after the connector, and two connectors stacked. Look for them first.

### Which verb goes with which type
asked (questions), ordered or told (commands), requested (please), advised (advice), suggested (let us), exclaimed (exclamations), wished or prayed (greetings and blessings).

> **Tip:** If the stem is a please-sentence and the option says *ordered*, reject it. The tense inside does not matter.
""",
    tricks=[
        {"title": "Skeleton first",
         "body": "Name the type of the quote. Then write its skeleton: asked if ... / told ... to ... / exclaimed with joy that ... Pour the tense, pronoun and time-word changes into the skeleton."},
        {"title": "Remove the helper do",
         "body": "In a direct question, do / does / did is only a helper. It vanishes in indirect speech. 'Do you know' becomes 'if I knew', never 'if I did know'.",
         "example": {"q": "Select the indirect form: *The clerk said to me, 'Do you know the way?'*",
                     "steps": ["It is a yes/no question, so use 'asked me if'.", "'Do' goes. 'Know' becomes 'knew'.", "You becomes I."],
                     "answer": "The clerk asked me if I knew the way."}},
        {"title": "Exclamation map",
         "body": "Hurrah: exclaimed with joy. Alas: exclaimed with sorrow. Bravo: applauded. Good morning: wished. Thank you: thanked."},
    ],
    mistakes=[
        mis("Keeping question order in a reported question: 'asked where was I going'.", "Use statement order: asked where I was going."),
        mis("Using 'if' with a wh-question.", "A wh-question uses its wh-word alone."),
        mis("Writing 'He ordered that I go' for a command.", "Use person + to + V1: He ordered me to go."),
        mis("Using 'exclaimed with joy' for an Alas! sentence.", "Match the emotion: Alas means sorrow."),
        mis("Ending a reported question with a question mark.", "A reported question ends with a full stop."),
    ],
    revision=[
        "Yes/No: asked + if or whether + statement order. Wh: asked + wh-word + statement order.",
        "Never use that with a question, never both if and a wh-word, and drop do / does / did.",
        "Command: told or ordered + person + to + V1. Negative: not to + V1.",
        "Request: requested. Advice: advised. Let us: suggested + V-ing.",
        "Hurrah: exclaimed with joy. Alas: exclaimed with sorrow. What a: exclaimed that it was a very ...",
        "Reported questions and exclamations end with a full stop.",
    ],
    patterns=[
        pat("nqc1", "Yes/No question becomes asked + if / whether", "very common",
            "The quote can be answered by yes or no (Do you ...? Is there ...? Can you ...?). Options differ in if / that and in word order.",
            ["Spot the auxiliary or 'do' at the start of the quote.", "Use asked + person + if / whether + statement order.",
             "Remove do / does / did. Put the tense on the main verb.", "Reject 'that', inverted order and a kept 'do'."],
            "Only if / whether reports a yes/no question. Every other connector changes the meaning or breaks the order.",
            "Select the indirect form: *My aunt said to me, 'Do you like filter coffee?'*",
            ["The quote is a yes/no question, so use 'asked me if'.", "'Do' goes; 'like' becomes 'liked'.", "You becomes I."],
            "My aunt asked me if I liked filter coffee."),
        pat("nqc2", "Wh-question becomes asked + wh-word + statement order", "very common",
            "The quote starts with why, where, when, what, who or how. Wrong options invert the helper (why did I) or put that before the wh-word.",
            ["Keep the wh-word as the connector. Put nothing before it.", "Use statement order: wh-word + subject + verb.",
             "Remove do / does / did. Step the tense back."],
            "A reported wh-question is a clause in statement shape. Keeping question order is the most planted fault.",
            "Select the indirect form: *The interviewer asked me, 'Why do you want this job?'*",
            ["The wh-word 'why' stays.", "'Do' goes; 'want' becomes 'wanted'.", "You becomes I; this becomes that."],
            "The interviewer asked me why I wanted that job."),
        pat("nqc3", "Command becomes told / ordered + person + to + V1", "very common",
            "The quote is a bare order, often negative (Do not ...). Options differ in where 'not' and 'to' sit.",
            ["Positive order: ordered / told + person + to + V1.", "Negative order: put 'not' before 'to' (not to make).",
             "Change this / these to that / those.", "Match the verb to the tone: an order, not a request."],
            "The to-infinitive is the frame for an order. The negative sits outside the 'to'.",
            "Select the indirect form: *The teacher said to the boys, 'Do not make a noise in the library.'*",
            ["It is a negative order: 'ordered the boys'.", "Put 'not to' before the verb.", "'Make' stays as a base verb."],
            "The teacher ordered the boys not to make a noise in the library."),
        pat("nqc4", "Request and advice frames", "common",
            "The quote has 'please' or 'kindly' (request), or it gives advice (Give up ..., Always speak ...). Options switch between requested, advised and ordered.",
            ["Please or kindly: requested + person + to + V1.", "Advice: advised + person + to + V1.",
             "Put always and never before the verb: advised him always to speak the truth.",
             "The listener follows the verb directly: requested the doctor, never requested to the doctor."],
            "Requests, advice and orders all use to + V1. Only the reporting verb tells them apart.",
            "Select the indirect form: *The patient said to the doctor, 'Please prescribe a milder tablet.'*",
            ["'Please' shows a request.", "Use 'requested the doctor to prescribe'.", "'Ordered' would turn the request into a command."],
            "The patient requested the doctor to prescribe a milder tablet."),
        pat("nqc5", "Exclamation becomes exclaimed with joy / sorrow that", "common",
            "The quote has Hurrah, Alas, What a or How. Options differ in joy / sorrow, in exclaimed / said, and in the 'very' change.",
            ["Read the emotion: Hurrah is joy; Alas is sorrow; Bravo is applauded.", "Use exclaimed with joy / sorrow + that + a statement, one step back.",
             "What a / How + adjective becomes 'it was a very + adjective'.", "The exclamation mark becomes a full stop."],
            "The reported verb must carry the same feeling as the quote. Swapping joy and sorrow is the classic trap.",
            "Select the indirect form: *The players said, 'Hurrah! We have clinched the series.'*",
            ["Hurrah shows joy: 'exclaimed with joy'.", "We becomes they.", "Have clinched becomes had clinched."],
            "The players exclaimed with joy that they had clinched the series."),
        pat("nqc6", "Greetings, thanks and blessings", "occasional",
            "The quote is a greeting (Good morning), thanks (Thank you) or a blessing (May you succeed).",
            ["Greeting: wished + person + the greeting.", "Thanks: thanked + person.",
             "Blessing: wished / prayed + that + person + might + V1."],
            "These short quotes have fixed reporting verbs and no tense to shift.",
            "Select the indirect form: *The guest said to the host, 'Thank you.'*",
            ["'Thank you' is thanks.", "The verb is 'thanked'.", "The host is the object of the verb."],
            "The guest thanked the host."),
    ],
)

# =====================================================================
# 5. Exam strategy
# =====================================================================
SUBS["narr-strategy"] = dict(
    concept=(
        "Every narration question changes the quote in four ways. "
        "Check them in this order: the connector, the reporting verb, the tense, then the pronouns and time words. "
        "In a well-set question, each wrong option fails exactly one check. "
        "Questions also come in reverse: you must turn indirect speech back into direct speech."
    ),
    notes=r"""### The four-check method
Run the checks in this order.

1. **Connector:** that / if or whether / the wh-word / to + V1. It must match the type. There must be exactly one.
2. **Reporting verb:** *said to + person* becomes *told* or *asked*. The tone must match: requested, ordered, advised, exclaimed, suggested.
3. **Tense:** one step back for a past reporting verb. Past perfect stays. General truths stay. Would, could, might, should and used to stay.
4. **Pronouns and time words:** SONA for pronouns. Tomorrow becomes the next day. This becomes that. Here becomes there.

> **Tip:** Start with the connector. It is the fastest check. You can often kill two options in five seconds without reading a verb.

### Reverse conversion: indirect to direct
Do the same steps backwards.

1. Put the reporting verb back with its comma and inverted commas: *told me* becomes *said to me, "..."*.
2. Remove the connector. *That* goes. *If / whether* becomes a question that starts with a helper verb (*Are you ...?*). A wh-word stays, but question order returns.
3. Step the tense up one rung: had + V3 becomes V2; was + V-ing becomes is / am + V-ing; would becomes will; could becomes can; had to becomes must.
4. Reverse the pronouns.
5. Restore the punctuation: a question mark for a question, an exclamation mark for an exclamation.

> **Example:** *The teacher told the students that the earth revolves around the sun.*
> Direct: *The teacher said to the students, "The earth revolves around the sun."*
> A general truth was never shifted, so it needs no un-shifting.

> **Watch:** Un-shift past perfect to the simple past: *had seen* becomes *saw*. Do not leave it as *had seen* in direct speech.

### Faults that appear most often
1. Question order kept: *asked if was he coming*.
2. Half-backshift: *said that he is busy*.
3. Time word left behind: *would visit tomorrow*.
4. Told with no listener, or *requested to the doctor*.
5. Two connectors: *asked that why*, *told that to come*.
6. A reported question that still ends with a question mark.
7. Wrong tone verb: please reported as ordered; Hurrah reported as sorrow.

### The 25-second routine
1. Read the direct sentence. Name its type: statement, yes/no, wh, command, request or exclamation.
2. Write the skeleton in your head: *asked if + statement order*, or *ordered + person + not to + V1*.
3. Compare each option with the skeleton, one check at a time.
4. The first option that passes all four checks wins.

> **Note:** Practise on paper, not by speaking. Narration is about punctuation and word order. The ear forgives what the hand catches.
""",
    tricks=[
        {"title": "Name the fault",
         "body": "For each wrong option, name its fault: verb, tense, pronoun or time word. If you cannot name it, look again. If two options share no fault, you may have misread the tone verb."},
        {"title": "Reverse-mode clues",
         "body": "In indirect to direct, 'the previous day' means the quote had 'yesterday'. 'Asked if' means the quote was a yes/no question with the helper verb first."},
        {"title": "Write ten a day",
         "body": "Convert ten sentences a day by hand. Mix statements, questions and commands. In a week the four checks run together."},
    ],
    mistakes=[
        mis("Fixing the tense but leaving 'said me' in place.", "Run the checks in order: connector, then reporting verb, then tense, then pronouns and time."),
        mis("Writing 'had seen' unchanged in direct speech.", "Step up one rung: had seen becomes saw."),
        mis("Forgetting the comma and inverted commas in an indirect to direct answer.", "Rebuild the frame: said to him, \"...\""),
        mis("Assuming every tense shifts.", "General truths keep their tense. Missing this costs a mark."),
        mis("Skipping the punctuation check.", "Look at the last character. A reported question ends with a full stop."),
    ],
    revision=[
        "Four checks in order: connector, reporting verb, tense, pronouns and time words.",
        "Reverse: put back the quotes and comma, remove the connector, step the tense up, reverse the pronouns, restore the punctuation.",
        "Top faults: question order kept, half-backshift, time word left behind, told with no listener, two connectors, a stray question mark.",
        "Name the type of sentence first. Write its skeleton. Then read the options.",
        "Each wrong option breaks one check. Name it and move on.",
    ],
    patterns=[
        pat("nst1", "Four-check elimination on a full question", "very common",
            "A plain statement question where each wrong option fails a different check. One keeps 'said to', one skips the backshift, one keeps 'yesterday'.",
            ["Connector: a statement with a named listener needs told + person + that.", "Tense: every verb steps down once (were becomes had been).",
             "Time words: yesterday becomes the previous day.", "Pronouns: apply SONA."],
            "A fixed order turns a four-way comparison into four quick yes/no checks.",
            "Select the indirect form: *The manager said to the clerk, 'You were absent yesterday.'*",
            ["'Said to' becomes 'told'; add 'that'.", "'Were' becomes 'had been'.", "Yesterday becomes the previous day; you becomes he."],
            "The manager told the clerk that he had been absent the previous day."),
        pat("nst2", "Reverse conversion: indirect to direct", "common",
            "The stem is reported speech and the options are direct speech. They differ in quotes and comma, in the un-shift, and in question order.",
            ["Rebuild the frame: said to + person, comma, inverted commas.", "Drop the connector. For a reported question, put the helper verb first and add the question mark.",
             "Step the tense up one rung. Keep a general truth as it is.", "Reverse the pronouns before closing the quote."],
            "The direct speech must be what the speaker could really have said. Every reported word (that, had, would) has to go.",
            "Select the direct form: *The teacher told the students that the earth revolves around the sun.*",
            ["Add 'said to the students' and a comma.", "Drop 'that'.", "The earth revolves is a general truth. It stays in the present."],
            "The teacher said to the students, \"The earth revolves around the sun.\""),
        pat("nst3", "Polite questions with shall, could", "common",
            "The quote is a polite question (Shall I ...? Could you ...?). Options add 'that if', or keep will / can.",
            ["Shall I ...? (asking what to do) becomes asked + if + I / he + should + V1.", "Could you ...? becomes asked + if + could + V1.",
             "Use one connector. Shift now to then.", "Never keep will or can, and never jump to must."],
            "Polite questions test three checks at once: the connector, the modal and the time word.",
            "Select the indirect form: *The clerk said to the manager, 'Shall I close the register now?'*",
            ["Use 'asked the manager if'.", "'Shall I' becomes 'he should'.", "'Now' becomes 'then'."],
            "The clerk asked the manager if he should close the register then."),
        pat("nst4", "Word order and punctuation sweep", "common",
            "A wh-question where two options use the same words, but one inverts the helper (when would the rains) or ends with a question mark.",
            ["After the wh-word, put the subject first, then the verb.", "Reject options like 'when would the rains come' at once.",
             "Check the last character. It must be a full stop."],
            "Order and punctuation faults are easy to miss when you read for meaning, so check them by position.",
            "Select the indirect form: *The child asked her mother, 'When will the rains come?'*",
            ["Keep 'when' as the connector.", "Will becomes would, and it moves after the subject.", "The question mark becomes a full stop."],
            "The child asked her mother when the rains would come."),
        pat("nst5", "Modal and time word together", "common",
            "The quote has a modal (may, could have) and a time word (next week, yesterday). Wrong options fix only one.",
            ["Do the modal first: may becomes might; could have stays could have.", "Do the time word second: next week becomes the following week.",
             "Check that both moved."],
            "Setters split the shift across two places. A candidate who checks only the tense falls for the untouched time word.",
            "Select the indirect form: *The coach said, 'The trials may be postponed till next week.'*",
            ["May becomes might.", "Next week becomes the following week.", "Either change alone is the planted half-answer."],
            "The coach said that the trials might be postponed till the following week."),
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
    print(sub["id"], "notes", len(n), "old patterns", len(old_ids), "new", len(new_ids))
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
