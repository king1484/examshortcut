"""Readable rewrite of English > Sentence Rearrangement (all 5 subtopics).

Plain English, short sentences, tables for signals, one routine per question type.
Every fact from the old notes is kept; new pattern ids continue each subtopic's prefix.
Run: python sentence_rearrangement.py  (patches content/core/topics/english/sentence-rearrangement.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "sentence-rearrangement.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. PQRS method
# =====================================================================
SUBS["rearr-pqrs-method"] = dict(
    concept=(
        "A PQRS question shows sentence 1 (S1) and sentence 6 (S6) in place. The four middle parts P, Q, R, S are mixed up. "
        "You choose the right order from four letter strings, such as *QPSR*. "
        "Do not test every string. Tag each part, find two strong links, and remove the strings that break them."
    ),
    notes=r"""### The routine in five steps
Follow the same steps every time. Each step is short.

1. **Read S1 and S6.** S1 gives the topic. S6 shows where the thought must end.
2. **Tag each part** as Lead, Support, Turn or Close (see below).
3. **Find the links.** A pronoun and its noun, a cause and its effect, an *a* and its later *the*.
4. **Chain the links** and check the story against S1 and S6.
5. **Remove strings.** Each wrong string breaks one link. Kill it there.

> **Tip:** This cuts 24 possible orders down to about three checks. That is how you finish in 30 seconds.

### What each part is doing
Every middle part has one job. Give it a one-word role before you read the options.

- **Lead:** continues S1 with a general statement, or with a pronoun that points back to S1.
- **Support:** gives an example, a figure or a detail (*for example*, *in Kerala*).
- **Turn:** brings a contrast or a problem (*But*, *However*, *Yet*, *Sadly*).
- **Close:** gives a result, a solution or a lesson (*therefore*, *thus*, *that is why*).

Once every part has a role, only one or two orders are left.

### Signal words and where they sit
| Signal inside a part | Likely position |
|---|---|
| Full noun phrase, no pronoun, general | just after S1 |
| He, she, it, this, these | right after the part with its noun |
| But, However, Yet, Now | after the claim it contrasts |
| This has led to, As a result | after the cause |
| Thus, Hence, That is why | last, before S6 |
| One day, Last winter, Soon after | start of a time chain |

### Two skeletons that cover most items
**Argument skeleton:** Lead, then Support, then Turn, then Close.

*Solar power is spreading.* Panels light homes. As a result, children study. However, panels break down. Training technicians is therefore the next step.

**Problem skeleton:** Problem, then Cause, then Effect, then Response.

*Lakes are dying.* Sewage flows in. This fills them with weeds. Citizens now clean them.

The Response part nearly always sits just before S6, because S6 usually looks ahead.

> **Rule:** If the parts fit a skeleton, write the order down before you read the options.

### S1 and S6 hold the frame
- **S1 hook:** a part that starts with *Its route...*, *They do so because...* or *The name referred to...* can only follow S1. It fixes the first letter.
- **S6 pull-back:** S6 often points backwards. *It was the tastiest lunch...* needs a meal just before it. The part with the meal is the last letter.

With both ends fixed, only two orders remain for the middle two parts. One pair then decides.

### The two-pair lock
Most items are built so that two links settle everything. Say P-S is a pronoun pair and R-Q is an *as a result* pair. Then the answer must hold both blocks. Only *PSRQ* and *RQPS* are possible. S1 or S6 picks one.

> **Watch:** Wrong strings are not random. Each one usually swaps two neighbours, moves the Close part to the middle, or opens with a pronoun or connector part. Name the link each wrong string breaks.
""",
    tricks=[
        {"title": "Pairs before strings",
         "body": "Do not read the four strings first. Build two or three pairs from P, Q, R, S. Then see which strings keep them.",
         "example": {"q": "P: It sat down beside the principal. Q: A stray dog walked onto the stage. Which part opens?",
                     "steps": ["*It* in P needs a noun.", "Q names the dog.", "So Q comes first, and P follows it."],
                     "answer": "Q then P"}},
        {"title": "Frame test",
         "body": "After you chain the parts, read S1, your chain and S6 as one paragraph. If any *it*, *this* or *they* has no noun, the chain is wrong."},
        {"title": "Adjacent-swap check",
         "body": "Wrong strings usually swap two neighbours. Find the one swap in each wrong string and name the broken pair. That proves your answer."},
    ],
    mistakes=[
        mis("Reading all four strings against the whole paragraph.", "Find two strong links first, then remove strings that break them."),
        mis("Starting the chain with a pronoun part whose noun comes later.", "Put the part that names the noun first."),
        mis("Ignoring S6 when a middle part has *therefore* or *thus*.", "That part usually sits just before S6."),
        mis("Forcing the string you like.", "Remove strings one broken link at a time."),
        mis("Judging order by which part sounds nice alone.", "Judge by links: pronouns, *a* to *the*, cause to effect."),
    ],
    revision=[
        "Tag every part: Lead, Support, Turn, Close.",
        "Argument: Lead, Support, Turn, Close. Problem: Problem, Cause, Effect, Response.",
        "The S1 hook fixes the first part. The S6 pull-back fixes the last part.",
        "Two strong pairs usually decide the item.",
        "Every wrong string breaks a link. Name it.",
        "Read S1 + chain + S6 once as a check.",
    ],
    patterns=[
        pat("rpm1", "Argument skeleton (claim, support, turn, close)", "very common",
            "S1 makes a general claim. One part gives a detail or result, one starts with *However* or *Yet*, one carries *therefore* or *thus*.",
            ["Tag the parts: Lead, Support, Turn, Close.",
             "Put the Support after what it supports (look for *as a result*).",
             "Put the Turn after the good news it contradicts.",
             "Put the Close just before S6."],
            "Opinion paragraphs in exams almost always follow this order.",
            "S1: Solar power is spreading across Indian villages. P: However, the panels often break down within two years. Q: As a result, children can now study after dark. R: Training local technicians is therefore the next step. S: Panels on rooftops now light many homes. Choose the order of PQRS.",
            ["S is the Lead: it continues S1.", "Q is Support: *as a result* follows the lighting.",
             "P is the Turn: *However* contradicts the good news.", "R is the Close: *therefore* gives the remedy."],
            "SQPR"),
        pat("rpm2", "Problem skeleton (problem, cause, effect, response)", "common",
            "S1 states a problem such as dying lakes or stubble burning. The parts give a reason, a result with *This has...*, and a remedy.",
            ["Find the cause part. It explains S1 directly.", "Attach the effect to it (*This has filled...*).",
             "Attach the next result.", "Put the response last, before S6."],
            "A remedy cannot come before the harm it answers.",
            "S1: The town lake is dying. P: This has filled the water with weeds. Q: Citizens now clean it every Sunday. R: Untreated sewage flows into it through open drains. S: The weeds use up the oxygen, so the fish disappear. Choose the order of PQRS.",
            ["R is the cause: sewage flows in.", "P follows R: *This* means the sewage flowing in.",
             "S follows P: it names the weeds.", "Q is the response, so it goes last."],
            "RPSQ"),
        pat("rpm3", "S6 pull-back", "very common",
            "S6 starts with a pronoun, *such*, or a noun that needs an earlier mention (*It was the tastiest lunch...*).",
            ["Read S6 first and circle what it points back to.", "Find the part that supplies that noun.",
             "Make that part the last letter.", "Build the rest backwards from it."],
            "S6 is fixed, so what it refers to must come just before it.",
            "S1: Meena's class planned a farm visit. P: The children picked vegetables in the morning. Q: The farmer's wife cooked them over a wood fire. R: They reached the farm by bus at nine. S: At noon everyone sat down to a meal under a tree. S6: It was the tastiest lunch the school had ever served. Choose the order of PQRS.",
            ["*It* in S6 means the meal, so S is last.", "R comes first: they arrive.",
             "P follows: they pick vegetables.", "Q follows: the vegetables are cooked."],
            "RPQS"),
        pat("rpm4", "S1 hook", "common",
            "One part starts with words that only make sense straight after S1: *Its route...*, *The name referred to...*, *They do so because...*",
            ["Find the part whose first words point at S1's subject.", "Make it the first letter.",
             "Continue the chain from it using pairs."],
            "*The name* or *They do so* has nothing to refer to except S1.",
            "S1: Chess began in India as a game called chaturanga. P: These divisions were the infantry, cavalry, elephants and chariots. Q: The name referred to the four divisions of an ancient army. R: Over the centuries, the rules changed many times. S: The modern game looks quite different from the old one. Choose the order of PQRS.",
            ["*The name* means chaturanga in S1, so Q is first.", "P follows Q: *These divisions* are the four.",
             "R comes next: the rules changed.", "S ends with the modern game."],
            "QPRS"),
        pat("rpm5", "Two-pair lock", "common",
            "Two parts are tied by *this + noun* or pronouns. Another two are tied by *because of these* or *its price*.",
            ["Find the two strongest pairs and write them as blocks.", "Only two strings can hold both blocks.",
             "Use S1 or S6 to choose between them."],
            "Two unbreakable blocks cut 24 orders down to two.",
            "S1: A clay lamp is a simple thing. P: Its low price makes it popular with every family. Q: Because of these cheap materials, it costs very little. R: A potter uses only clay and water. S: Impressed by this demand, a city shop ordered a thousand lamps. Choose the order of PQRS.",
            ["*These cheap materials* in Q points to R: block RQ.", "*Its low price* in P follows Q's cost: block QP.",
             "*This demand* in S follows P's popularity.", "The blocks join into one chain."],
            "RQPS"),
        pat("rpm6", "Name the broken link in each wrong string", "common",
            "Four strings are offered and two of them look close to the right one.",
            ["Build the correct order first.", "Compare each string with it.",
             "Find the one swap or move that each string makes.", "Name the link it breaks and cross it out."],
            "The setter builds every wrong string by breaking one link. Finding the break proves the answer.",
            "Using the solar-power parts above. Options: (a) SQPR (b) SPQR (c) QSPR (d) RQPS. Which is right and why are the others wrong?",
            ["(a) keeps Lead, Support, Turn, Close.", "(b) puts the Turn before the Support it contradicts.",
             "(c) opens with *As a result*, which needs the lighting first.", "(d) opens with the Close part."],
            "(a) SQPR"),
    ],
)

# =====================================================================
# 2. Openers and closers
# =====================================================================
SUBS["rearr-openers-closers"] = dict(
    concept=(
        "The first and last parts of a jumble are the easiest to find. "
        "A part cannot open if it holds a pronoun, a connector, or a *the* with no earlier mention. "
        "A part closes well if it gives a result, a lesson or a look ahead. "
        "Fix the ends first. Then the middle is short work."
    ),
    notes=r"""### What can and cannot open
Some parts cannot come first, because they need something before them. These are quick eliminations.

- **A bare pronoun.** *He refused the offer* cannot open. Nobody knows who *he* is.
- **A connector.** *But*, *However*, *Therefore*, *So*, *And*, *Because* cannot open a thought.
- **A *the* on a first mention.** *The boy ran* cannot open. A boy must exist first.
- **A consequence phrase.** *This decision proved costly* cannot open. No decision exists yet.

**What can open:** a full noun phrase with a general or scene-setting statement, a time opener (*One day*, *Last winter*), or a definition.

> **Rule:** If two parts both look like openers, choose the more general one. Examples come after claims.

### The orphan test
Read each part as if it came straight after S1. A part fails if it holds:

- a pronoun whose noun is only in another part (*It sat down beside the principal*),
- a *this* or *these* plus a noun that S1 does not give (*This ability...*),
- a follow-on word such as *also*, *even*, *others*, *too*.

Usually two or three parts fail. The one that passes is the opener.

| Candidate opener | Verdict |
|---|---|
| It improves memory. | No. *It* hangs. |
| Reading improves memory. | Yes. Full noun, general. |
| But books are costly. | No. *But* cannot open. |
| Thus a reading habit pays for life. | No. Conclusion word. |
| That is why libraries matter. | Close only. |

### Connectors inside a PQRS item
A free paragraph cannot start with *However*. But in a PQRS item, S1 is already there. So a connector part can follow S1 directly.

*S1: Many students think maths is only for the gifted.* Then *However, this belief is not true* is the first part. *This belief* means S1.

> **Rule:** A connector follows the claim it turns on. If that claim is S1, the connector part comes first. If it is in another part, the connector comes right after that part.

### Closers and S6
A closing part usually carries a signal: *therefore*, *thus*, *hence*, *clearly*, *that is why*, *the next step*. Two checks confirm it.

1. It must follow everything it sums up. *Hence, experts warn the species could vanish* needs the threats listed first.
2. It must lead into S6. If S6 is itself a conclusion, the Close part prepares for it.

Other good closers are a lesson, a judgement, or a look ahead. *Such campaigns must continue* is one.

### General before specific
An example needs the claim it illustrates. *Each region cooks with what grows around it* comes before *In Kerala, for example...*

Words like *for example*, *in Punjab* and *during deep sleep* mark specific parts. They are never first.

### Order of work
1. Run the orphan test on all four parts. That gives the opener.
2. Look for signal words. That gives the closer.
3. Use one pair to order the two middle parts.

> **Tip:** Two parts often fail the orphan test for the same reason. Group them, then place the group after the opener.
""",
    tricks=[
        {"title": "Pronoun orphan test",
         "body": "A part that starts with he, she, it, they, this or these needs its noun earlier. If a string gives no earlier noun, cross it out."},
        {"title": "Connector ban",
         "body": "But, However, Therefore, Thus and So cannot open a free jumble. Two of four options often start with such parts. Cross them out. In a PQRS item, check whether S1 is the claim first."},
        {"title": "Ask what comes before S6",
         "body": "Read S6 and ask which sentence must come just before it. It is often the part with *Thus*, *That is why* or a summing-up judgement. Pin it, then build backwards."},
    ],
    mistakes=[
        mis("Opening with a *the* sentence whose noun appears nowhere before it.", "Open with the part that introduces the noun with *a* or a plain noun phrase."),
        mis("Treating a general claim and its example as interchangeable.", "Put the general claim first and the example after it."),
        mis("Missing that *Now* signals a present-time contrast.", "Place it after the past-time claim it contrasts."),
        mis("Putting *Thus...* in the middle of the chain.", "Put the concluding part last, before S6."),
        mis("Banning every connector part from the front, even in a PQRS item.", "Check S1. A connector can follow S1 directly when S1 is the claim it turns on."),
    ],
    revision=[
        "Orphan test: pronoun, this + noun, also, even, others cannot open.",
        "A connector follows the claim it turns on. That claim can be S1.",
        "Closers: therefore, thus, hence, clearly, that is why.",
        "A closer follows everything it sums up.",
        "General claim first. *For example* is never first.",
        "Order of work: opener, closer, one middle pair.",
    ],
    patterns=[
        pat("roc1", "Orphan test for the opener", "very common",
            "Two or three parts begin with pronouns or *this + noun*. Only one part brings in a new noun.",
            ["Read each part as if it came straight after S1.", "Cross out every part whose pronoun or *this + noun* has nothing to refer to.",
             "The part left is the opener.", "Attach the pronoun parts after it."],
            "A pronoun cannot come before its noun, so the part that brings the noun comes first.",
            "S1: The morning assembly began as usual. P: It sat down beside the principal. Q: Suddenly, a stray dog walked onto the stage. Which part follows S1?",
            ["*It* in P has no noun in S1.", "Q brings in the dog.", "So Q comes first and P follows it."],
            "Q then P"),
        pat("roc2", "Connector follows the claim it turns on", "common",
            "One part begins with *However*, *But* or *Yet*. S1 or another part states the claim it disputes.",
            ["Find the claim the connector answers (*this belief*, *the same device*).",
             "If the claim is S1, the connector part comes first.", "Otherwise place it after the part that makes the claim.",
             "Put its support right after it."],
            "A contrast needs something to contrast with, and that must come just before it.",
            "S1: Many students think maths is only for the gifted. P: However, this belief is not true. Q: A study of ordinary classrooms shows steady practice raises scores. R: Therefore, every child should be given time to practise. Choose the order of PQR.",
            ["*This belief* means S1's claim, so P is first.", "Q gives the support.", "R closes with *Therefore*."],
            "PQR"),
        pat("roc3", "Closing signal part", "very common",
            "One part has *hence*, *therefore*, *clearly* or *that is why*, or offers a solution. S6 is a final judgement.",
            ["Mark the part with the closing signal.", "Check that everything it sums up comes before it.",
             "Put it last, just before S6.", "Order the other parts."],
            "A conclusion depends on all the points before it, so it can only go at the end.",
            "S1: Traffic jams waste millions of hours. P: Building more roads only brought more cars. Q: Clearly, the answer lies in moving people, not vehicles. R: Cities first tried to fix the jams with wider roads. Choose the order of PQR.",
            ["R names the first fix.", "P shows that the fix failed.", "Q says *Clearly*, so it sums up and comes last."],
            "RPQ"),
        pat("roc4", "General before specific", "common",
            "One part makes a general claim. Others start with *for example*, *in Kerala*, *in Punjab* or name a single case.",
            ["Find the general claim.", "Place it before its examples.", "Pair the examples (*for example* ... *on the other hand*)."],
            "An example only makes sense after the claim it illustrates.",
            "S1: Indian food changes every few hundred kilometres. P: In Punjab, on the other hand, wheat breads are common. Q: Each region cooks with what grows around it. R: In Kerala, for example, coconut is used in many dishes. Choose the order of PQR.",
            ["Q is the general claim, so it goes first.", "R gives the first example (*for example*).",
             "P follows: *on the other hand* needs a first example before it."],
            "QRP"),
        pat("roc5", "Hidden follow-on words (also, even, others)", "common",
            "One part contains *others*, *even*, *also* or *too*, and another part names the first group or item.",
            ["Find the follow-on word.", "Ask what it follows: the first item, the first group.",
             "Place the first item before it."],
            "*Others* needs *some* before it, and *even* needs a first case before it.",
            "S1: Rural libraries are changing. P: Others have built study halls for exam students. Q: Many now lend e-books to their neighbours. Choose the order of PQ.",
            ["*Others* needs a first group.", "Q names the first group: many libraries lend e-books.", "So Q comes before P."],
            "QP"),
    ],
)

# =====================================================================
# 3. Mandatory pairs
# =====================================================================
SUBS["rearr-mandatory-pairs"] = dict(
    concept=(
        "A mandatory pair is two parts that must sit next to each other. "
        "Examples are a noun and its pronoun, or *a* and the later *the*. "
        "Most items are solved by finding two or three such pairs. Trust the strongest link first."
    ),
    notes=r"""### The pair types
Learn these seven pair types. They cover most items.

| Pair type | Example | Rule |
|---|---|---|
| Noun, then pronoun | ...the crow. It flew away. | Pronoun follows its noun. |
| A, then The | ...a piece of bread. The bread was sweet. | *The* needs an earlier *a*. |
| Cause, then effect | ...machines replaced workers. This led to unemployment. | *This* or *As a result* follows the cause. |
| Contrast | ...banned plastic. Yet people use it. | *Yet*, *But*, *However* follow the claim. |
| General, then specific | Museums store history. Coins, weapons and paintings... | Example follows claim. |
| Question, then answer | Who will bell the cat? No one came forward. | Answer follows question. |
| Name, then role | ...the eldest villager. He told stories. | Role follows introduction. |

> **Tip:** Gender and number are free checks. *He* cannot point to *the boys*. *Its* cannot point to *workers*.

### The a-to-the rule
Once a noun appears with *a*, every later mention uses *the*. So find the part that mentions the noun first with *a*. It comes before every part with *the* plus the same noun.

*The old man left a small bag on the doorstep. The bag was full of gold coins.*

### This, that and these
*This decision*, *that scheme*, *these problems*. The word locks onto an earlier abstract noun. Find the noun. Find the pair.

### Not all links are equally strong
Rank the links you find. Trust the strong ones first.

| Strength | Link | Example |
|---|---|---|
| Very strong | Pronoun, then its only noun | a stray dog ... **It** sat down |
| Very strong | a + noun, then the + noun | **a small bag** ... **The bag** |
| Very strong | this/these/such + noun | a huge challenge ... **this challenge** |
| Strong | As a result, This has led to | sewage flows in ... **This has** filled |
| Strong | There, Here, Inside | moved abroad ... **There** she studied |
| Medium | But, Yet, However | fast messages ... **Yet** a letter... |
| Weak | Same topic, no grammar link | two parts about trains |

> **Rule:** The stronger link always wins. Never break a pronoun pair to please a weak topic link.

### Hidden pointers
Some pointer words are easy to miss.

- **also, too, as well:** the part is a second item and needs a first one.
- **Others, Some, the rest:** *Others have built study halls* needs *Many now lend e-books* before it.
- **Even:** *Even the principal could not keep a straight face* needs others laughing first.
- **the same, such, so many:** they point back to a noun or number already given.

### Pairs join into chains
If P-S is a pair and S-Q is a pair, then P-S-Q is one block of three. Pairs usually cover three of the four parts. One more fact places the last part. Write the blocks down as you find them.

### Checking a pair
Read the two parts together. A true pair reads as one smooth thought. A false pair makes you ask *which one?* or *what is this about?*

*But*, *Yet* and *However* are medium links, because the claim can sit in S1. Confirm with the content. *Yet a letter carries something a message cannot* contrasts with the speed of emails, so it follows the email part.
""",
    tricks=[
        {"title": "Noun-first scan",
         "body": "List the nouns and pronouns in P, Q, R, S. Circle each pronoun and each *the* noun. Draw an arrow to the part that brings in its noun. The arrows are the answer skeleton."},
        {"title": "This + noun hunt",
         "body": "For every *this + abstract noun*, find the part that holds that idea. The order is then forced."},
        {"title": "A-to-the cascade",
         "body": "The part with *a + noun* comes before every part with *the + same noun*. This orders many food and story passages at once.",
         "example": {"q": "P: The bread was sweet. Q: The crow found a piece of bread. Which is first?",
                     "steps": ["Q says *a piece of bread*.", "P says *the bread*.", "So Q comes first."],
                     "answer": "Q then P"}},
    ],
    mistakes=[
        mis("Breaking a noun-to-pronoun pair to fit a time marker.", "Keep the pronoun pair. It is a stronger link."),
        mis("Missing the second mention of a noun (*the bread* after *a piece of bread*).", "Scan every part for repeated nouns."),
        mis("Placing an effect before its cause because the cause reads well alone.", "Put *This*, *As a result* and *Therefore* parts after the cause."),
        mis("Ignoring number in a pronoun chain (*its* for *workers*).", "Match gender and number: *its* for one thing, *their* for many."),
        mis("Linking two parts only because they share a topic.", "Use grammar links: pronoun, *a* to *the*, *this + noun*, connector."),
    ],
    revision=[
        "Rank links: pronoun, a-to-the, this + noun, as a result, place word, then contrast, then topic.",
        "Hidden pointers: also, others, even, such, the same.",
        "Pairs join into blocks: PS + SQ = PSQ.",
        "Two or three blocks usually decide the item.",
        "Read the pair together. Check number and gender.",
        "The stronger link always wins.",
    ],
    patterns=[
        pat("rmp1", "Noun to pronoun or place-word pair", "very common",
            "One part names a person, animal or place. Another begins with *He*, *She*, *It* or *There* and points to it.",
            ["List each pronoun or place word.", "Find the only part that names what it refers to.",
             "Join those two parts as a block.", "Check gender and number."],
            "A pronoun must come after its noun, usually straight after.",
            "S1: Ravi found an injured sparrow. P: She cleaned its wing and gave it water. Q: He carried it to the science teacher. Choose the order of PQ.",
            ["*She* in P can only be the science teacher.", "Q brings in the teacher.", "So Q comes first."],
            "QP"),
        pat("rmp2", "A to the pair", "very common",
            "A noun appears with *a* or *an* in one part and with *the* in another (*a small bag* and *The bag*).",
            ["Scan for nouns that appear twice.", "The part with *a + noun* comes first.",
             "If the *the* part adds detail, place it directly after."],
            "English introduces a thing with *a* and refers back to it with *the*.",
            "P: The bag was full of gold coins. Q: The old man left a small bag on the doorstep. Choose the order of PQ.",
            ["Q says *a small bag*.", "P says *The bag*, so it refers back."],
            "QP"),
        pat("rmp3", "This or these plus an abstract noun", "common",
            "A part begins with *this challenge*, *this effort*, *this system* or *this decline*. Exactly one other part describes it.",
            ["Underline the noun after *this*.", "Find the part that describes that idea.", "Join them. A chain of *this* words can link three parts."],
            "*This + noun* sums up the idea just before it.",
            "P: This system shows every engine's position on a screen. Q: Keeping so many trains on time is a huge challenge. R: To meet this challenge, the railways track trains by satellite. Choose the order of PQR.",
            ["Q states the challenge.", "R says *this challenge* and names the satellite system.", "P says *This system*, so it follows R."],
            "QRP"),
        pat("rmp4", "Contrast pair (claim, then but, yet, however)", "common",
            "One part starts with *But*, *Yet* or *However* and contradicts something, such as speed against feeling.",
            ["Find what the contrast part contradicts.", "Place it right after the part that says that, or after S1 if S1 says it.",
             "Put the explanation of the contrast next."],
            "A contrast only makes sense straight after the claim it contradicts.",
            "P: Yet a letter carries something a message cannot. Q: The handwriting and the paper bring the writer closer. R: Emails reach people in seconds. Choose the order of PQR.",
            ["R makes the speed claim.", "P says *Yet*, so it contrasts with R.", "Q explains what the something is."],
            "RPQ"),
        pat("rmp5", "Question to answer pair", "occasional",
            "One part asks a question. Another gives a reply such as *Nobody came forward* or *Yes, it is*.",
            ["Find the question part.", "Find the part that answers it.", "Put the answer directly after the question."],
            "A reply makes no sense before the question it answers.",
            "S1: The mice held a meeting. P: Nobody came forward. Q: One young mouse asked, \"Who will tie a bell round the cat's neck?\" R: The meeting ended in silence. Choose the order of PQR.",
            ["Q asks the question.", "P answers it: nobody came forward.", "R gives the result."],
            "QPR"),
        pat("rmp6", "Hidden pointers (others, even, also)", "common",
            "Parts contain *others*, *even*, *also* or *too*, and the first item or group is in another part.",
            ["Find each pointer word.", "Find the first item it refers to.", "Place that item before it."],
            "A pointer word needs an earlier item to point to.",
            "S1: Many students found the exam hard. P: Others just sat quietly for a while. Q: Some left the hall in tears. R: Even the toppers admitted they were nervous. Choose the order of PQR.",
            ["*Others* in P needs *Some* in Q first.", "*Even the toppers* in R comes after both groups."],
            "QPR"),
    ],
)

# =====================================================================
# 4. Time sequence
# =====================================================================
SUBS["rearr-time-sequence"] = dict(
    concept=(
        "Story and history jumbles follow the clock. "
        "Use time words first, then tenses, then cause and effect. "
        "Number the events in order, and the letter string writes itself."
    ),
    notes=r"""### Time markers and where they sit
Story, incident and history jumbles run on the clock. These markers fix the order.

| Marker | Position signal |
|---|---|
| One day, Long ago, In 1947, Last winter | earliest event |
| Soon, Then, After that, Meanwhile | next events |
| By midnight, By dawn, Within a week | result time of an ongoing event |
| The next morning, The following day | day boundary |
| Now, Today, These days | present contrast, near the end |
| Ever since, Since then | after the turning point |

> **Tip:** Build the timeline before you touch the options. Number the events, for example: flood, homes flooded, villagers moved, boats ferried, rescue arrived. Then write the letters in that order.

### Three layers of time
A story gives time clues at three levels. Use as many as you need.

1. **Markers:** dates and time words (*Last December*, *That night*, *By dawn*, *Today*).
2. **Tense:** past perfect (*had left*) for earlier events, simple past for the main events, present for the end.
3. **Cause and effect:** the fire must start before the engines arrive.

Markers are the most reliable. Use tense when markers are missing. Use cause and effect when tense does not help.

### Relative markers need an anchor
*Eleven years later*, *A few days later* and *On the eighth day* count from an earlier event. They cannot come first. Find the event they count from. Place them after it.

*Eleven years later* needs *In 2008*. *The restart* needs *half-time*.

### By-phrases close a phase
*By dawn, the flames had been put out.* *By the final whistle, we had won.*

A by-phrase shows where a stretch of action ended. So it follows the actions inside that stretch. Wrong options often put it first.

> **Watch:** *By midnight* caps the flooding. It comes after the flooding sentence, never before.

### Flashbacks in the past perfect
*When Anil reached the station, the platform was empty. The express had left ten minutes earlier. He had missed it because he had overslept.*

The past perfect parts explain the scene. The story then returns to the simple past. Keep the flashback parts together, straight after the scene they explain. A past-perfect event placed after the simple-past event it caused is wrong.

### Process and instruction passages
Recipes and application steps use **First, Next or Then, After that, Finally**. When markers are missing, ask what each step needs. You cannot book an appointment before you register. Officials cannot check documents before the appointment exists.

### Biography and history
Lives run in date order. Also look for pointer words. *There she earned a doctorate* needs the part that names the place. *Her second mission* needs the first one. Exam biographies skip years, so use *first*, *second*, *later* and *then* as well as dates.
""",
    tricks=[
        {"title": "Timeline first",
         "body": "Write the four to six events as a numbered list. Then map the numbers to the letters. The string writes itself.",
         "example": {"q": "P: Villagers were moved to boats. Q: Heavy rain flooded the homes. R: By midnight, the water had reached the roofs. Order?",
                     "steps": ["Rain and flooding come first: Q.", "Then the rescue action: P.", "*By midnight* caps the flooding phase."],
                     "answer": "QRP"}},
        {"title": "Tense radar",
         "body": "Past perfect is earlier. Past continuous is background. Simple past is the main story line. Use tense when time words are missing."},
        {"title": "By-time capping",
         "body": "*By midnight* and *By dawn* close the phase they describe. They follow the event chain and never open it."},
    ],
    mistakes=[
        mis("Placing *Now* or *Today* early in a story that ends in the present.", "Put present-time parts last."),
        mis("Ordering the parts by how they are listed.", "Order them by when the events happened."),
        mis("Ignoring *The next morning*.", "Treat it as a day boundary. Put it after everything from the day before."),
        mis("Letting a result-time phrase such as *By dawn* open the chain.", "Put it after the actions it sums up."),
        mis("Putting a past-perfect flashback after the event it explains.", "Keep flashback parts together, straight after the scene."),
    ],
    revision=[
        "Use markers first, then tense, then cause and effect.",
        "*Eleven years later* and *a few days later* need an earlier event before them.",
        "By-phrases come after the actions they sum up.",
        "Past perfect means flashback. Keep those parts together.",
        "Processes: each step needs the step before it.",
        "Present-time parts (*Today*, *Now*) come last.",
    ],
    patterns=[
        pat("rts1", "Explicit time and date markers", "very common",
            "Parts carry dates or time words: *In 2008*, *Eleven years later*, *In August 2023*, *As soon as they reached*.",
            ["Underline every time word.", "Put fixed dates in order.", "Attach each relative marker after its anchor.",
             "Place unmarked parts by cause and effect."],
            "The markers put the events in order before you read the options.",
            "P: Eleven years later, its lander crashed on the surface. Q: In 2008, an Indian probe reached the moon. R: Scientists studied the failure closely. S: In 2023, a third mission landed safely. Choose the order of PQRS.",
            ["Q is the earliest date.", "P counts from 2008, so it follows Q.", "R studies the crash, so it follows P.", "S has the latest date."],
            "QPRS"),
        pat("rts2", "By-phrases and day boundaries", "common",
            "One part begins with *By dawn*, *By the final whistle* or *By midnight*, or with *That night* or *The next morning*.",
            ["Find the actions the by-phrase sums up.", "Place the by-phrase after them.",
             "Place day-boundary parts after everything from the day before.", "Check that S6 continues from the last part."],
            "A by-phrase describes the result of the actions before it, so it cannot come first.",
            "S1: A fire broke out late on Saturday night. P: Shopkeepers rushed out with buckets. Q: Engines arrived within twenty minutes. R: By dawn, the flames were out. S: Later that morning, officials counted the damage. Choose the order of PQRS.",
            ["People nearby act first: P.", "The engines arrive next: Q.", "*By dawn* sums up the firefighting: R.", "*Later that morning* comes after dawn: S."],
            "PQRS"),
        pat("rts3", "Tense as a clock (past perfect flashback)", "common",
            "Parts mix *had + V3* with simple past and present. There are few time words.",
            ["Past perfect parts are earlier events. Keep them together in order.", "Simple past parts continue the main story.",
             "Present-tense parts (*Today...*) come last."],
            "Tense shows the order of events even without time words.",
            "S1: The old fort stood silent. P: Over time, the trade route moved elsewhere. Q: Today only tourists climb its walls. R: A king had built it on a hill. S: Armies had attacked it many times. Choose the order of PQRS.",
            ["R and S are past perfect: they come first.", "R (built) comes before S (attacked).", "P is simple past: it continues the story.", "Q is present: it comes last."],
            "RSPQ"),
        pat("rts4", "Process steps", "common",
            "The passage explains how to do something, such as apply for a passport, with *First*, *Next*, *Then*, *Finally* or steps that depend on each other.",
            ["Use *First* and *Finally* to fix the ends.", "For steps without markers, ask what each step needs before it.",
             "A step that mentions something (the appointment) follows the step that creates it."],
            "Each step depends on the one before it, so the order is forced.",
            "P: At the appointment, officials check the documents. Q: The applicant first registers on the portal. R: A police verification follows. S: After paying the fee, the applicant books an appointment. Choose the order of PQRS.",
            ["Q is first: register.", "S comes next: pay and book.", "P needs the appointment, so it follows S.", "R follows the check."],
            "QSPR"),
        pat("rts5", "Biography with pointer words", "occasional",
            "Parts tell one person's life. Some start with *There*, *Her second...* or *Later*.",
            ["Find the pointer words (*There*, *second*, *later*).", "Find the part each one needs.",
             "Use dates or *first*, *second*, *then* to place the rest."],
            "Exam biographies skip years, so pointer words are more reliable than dates.",
            "S1: Rekha grew up in a small town in Kerala. P: There she earned a doctorate in marine biology. Q: After school, she left for Australia. R: Her first research trip took her to the Andaman Sea. S: Her second trip went much deeper. Choose the order of PQRS.",
            ["Q names the country.", "P says *There*, so it follows Q.", "R is the first trip.", "S is the second trip, so it follows R."],
            "QPRS"),
    ],
)

# =====================================================================
# 5. Strategy
# =====================================================================
SUBS["rearr-strategy"] = dict(
    concept=(
        "Rearrangement is a free mark if you use a fixed routine. "
        "You do not need to understand the whole paragraph. You only need to rule out three wrong strings. "
        "Use layers of elimination, and test only the part where the last two strings differ."
    ),
    notes=r"""### Time budget
Tier 1 gives about one rearrangement item per shift. Attempt it in 35 to 45 seconds. Tier 2 adds longer paragraph jumbles of five or six sentences and sentence-order items. Allow 60 to 75 seconds there.

### A 40-second routine
1. **Read S1 and S6 (5 s).** Note the subject and what S6 refers back to.
2. **Tag the parts (15 s).** Mark pronouns, *this + noun*, connectors, time words and closing signals.
3. **Fix one end and one pair (10 s).** Use the orphan test for the opener, or the S6 pull-back for the closer. Add the strongest pair.
4. **Eliminate (10 s).** Cross out every string that breaks that end or pair. Usually one is left.

> **Tip:** You do not need certainty about the whole paragraph. Option strings share starts and ends, so partial certainty still reaches one string.

### Layers of elimination
1. Which parts can open? Ban pronoun and connector openers. This kills about two options.
2. Which pair is mandatory (noun to pronoun)? This kills one or two more.
3. Check the survivor against S6.

### Jumbles with no fixed ends
Without S1 and S6, you lose both clamps. So:

- Find the **independent sentence**: no pronoun pointing back, no connector, no *this + noun*, no *also*. It opens.
- Find the **strongest pair** (*a* to *the*, pronoun, *this + noun*) and extend the chain from the opener.
- The **closer** has a conclusion signal, or a *this + noun* that sums up the whole problem (*close this gap*).

Setters often write two sentences that look independent. Choose the more general one, or the one the other refers to.

### First-sentence and last-sentence questions
Some papers ask only which sentence comes first or last. Do not arrange all four.

- **First:** apply the orphan test to every sentence. The one that passes is the answer. If two pass, the more general wins.
- **Last:** find the sentence that sums up, or completes the final step of a story or process. Check that nothing else must follow it.

This takes 20 to 30 seconds.

### When two strings survive
Say you have *QRPS* and *QPRS*. Find the parts in different positions (here R and P). Test only those neighbours. Does P's *But it has also* need R's *This has made life easier* before it? One small check is faster than rereading the paragraph.

> **Watch:** Wrong options often keep the right opener and closer and swap two middle parts. Check the middle pair even when both ends match.

### Odd-sentence-out
Four sentences share a theme. The fifth touches it but never uses its key noun. Mark each sentence's key noun. The one without it is the odd one.

### Daily plan
Do five rearrangements a day. Write the pairs before you check the answers. After two weeks, tagging openers, connectors and *this + noun* becomes automatic.
""",
    tricks=[
        {"title": "Layered elimination",
         "body": "Layer 1: the opener ban. Layer 2: the mandatory pair. Layer 3: the S6 check. Each layer is one question. Two layers usually finish the item."},
        {"title": "Local-difference test",
         "body": "The two surviving strings differ in one place. Isolate that part and test only its two neighbours.",
         "example": {"q": "Survivors: QRPS and QPRS. R: This has made life easier. P: But it has also created chances for fraud. Which is right?",
                     "steps": ["The strings differ only in R and P.", "*But it has also* needs the benefit before it.", "R gives the benefit."],
                     "answer": "QRPS"}},
        {"title": "Odd-sentence radar",
         "body": "For odd-one-out items, mark each sentence's key noun. Four share it. The odd one only orbits it."},
    ],
    mistakes=[
        mis("Spending 90 seconds building the full chain.", "Two eliminations often finish the item. Stop when one string is left."),
        mis("Refusing to mark an answer without full certainty.", "Elimination already gives you the string. Mark it."),
        mis("Reading the options before reading P, Q, R, S.", "Read the parts first, then use the options to eliminate."),
        mis("In odd-one-out, choosing the least familiar sentence.", "Choose the sentence that lacks the key noun."),
        mis("Treating a dated sentence (*In August 2023...*) as the natural opener.", "Check its anchors. It may end the story."),
        mis("Linking two parts because they share a topic.", "Trust grammar links: pronoun, *a* to *the*, *this + noun*, connector."),
    ],
    revision=[
        "Routine: read S1 and S6, tag the parts, fix one end and one pair, eliminate.",
        "No fixed ends: independent sentence first, strongest pair next, summary last.",
        "First or last question: orphan test for first, summary or final step for last.",
        "Two strings left: test only the parts that differ.",
        "Grammar links beat topic similarity.",
        "A dated part can be an ending, not an opener.",
    ],
    patterns=[
        pat("rst1", "Paragraph jumble with no fixed ends", "common",
            "Four sentences labelled P, Q, R, S with no S1 or S6. The options are four-letter strings.",
            ["Find the independent sentence (no pronoun, connector, *this + noun* or *also*). It opens.",
             "Attach the strongest pair to it.", "Put the summary or *this + noun* sentence last."],
            "Without S1 and S6, the opener must be the one sentence that needs nothing before it.",
            "P: At the same time, many families go hungry. Q: Every year, millions of tonnes of food are wasted. R: Better cold storage could close this gap. S: Much of it rots in storage. Choose the order of PQRS.",
            ["Q is the only independent sentence.", "S follows: *it* means the wasted food.", "P adds the contrast.", "R closes: *this gap*."],
            "QSPR"),
        pat("rst2", "Which sentence comes first?", "common",
            "The options are just the labels P, Q, R, S, and the question asks for the opening sentence.",
            ["Apply the orphan test to each sentence.", "Cross out any sentence with a pronoun, *this + noun*, a connector or a relative time marker.",
             "The sentence left is the answer."],
            "You only need the opener, so arranging the other three wastes time.",
            "P: Their destination was Dandi. Q: On reaching the sea, he picked up salt. R: In 1930, Gandhiji set out from Sabarmati Ashram. S: This simple act inspired millions. Which sentence is first?",
            ["P says *Their*, which points back.", "Q says *he*, which points back.", "S says *This act*, which points back.", "R brings in Gandhiji."],
            "R"),
        pat("rst3", "Which sentence comes last?", "common",
            "The options are just the labels, and the question asks for the closing sentence.",
            ["Look for a sentence that sums up or completes the last step.", "Check that nothing else points back to it.",
             "Confirm by building the chain backwards."],
            "The last sentence refers back to others, but nothing refers back to it.",
            "P: Others follow this trail and carry the food home. Q: Each colony divides its work. R: When a worker finds food, it leaves a trail. S: Ants are very organised. Which sentence is last?",
            ["*This trail* in P needs R before it.", "Nothing refers back to P.", "The chain is S, Q, R, P."],
            "P"),
        pat("rst4", "Two strings left: test only the difference", "very common",
            "You have ruled out two strings. The remaining two differ only in the positions of two neighbouring parts.",
            ["Write the two strings one above the other.", "Find the two parts that swap places.",
             "Test only that link: does one point back to the other?"],
            "The right string and the closest wrong one differ at one point. Testing that point decides the item.",
            "Survivors: QRPS and QPRS. R: This has made life easier. P: But it has also created chances for fraud. Which is right?",
            ["The strings differ in R and P.", "*But it has also* needs a benefit before it.", "R gives the benefit, so R comes first."],
            "QRPS"),
        pat("rst5", "Odd sentence out", "occasional",
            "Five sentences are given. One does not belong to the paragraph.",
            ["Find the key noun that most sentences share.", "Mark which sentences use it.", "The sentence without it is the odd one."],
            "The odd sentence touches the theme but never uses its key noun.",
            "P: Elephants live in herds led by an old female. Q: Elephants use low sounds to talk over long distances. R: A calf stays with its mother for years. S: Tigers hunt mostly alone at night. Which sentence is the odd one out?",
            ["The key noun is *elephants*.", "P and Q name elephants.", "R is about a calf in the same herd theme.", "S is about tigers."],
            "S"),
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
