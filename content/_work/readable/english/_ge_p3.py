from _ge_common import SUBS, pat, mis, trick

# =====================================================================
# 6. Modals and conditionals
# =====================================================================
SUBS["ge-modals-conditionals"] = dict(
    concept=(
        "Modal verbs like can, may, must and should add a shade of meaning to the main verb. "
        "A conditional sentence joins an *if* clause to a result clause. "
        "The exam tests two things: the **form** after a modal, and the **matching of tenses** in a conditional."
    ),
    notes=r"""### What modals do
The modals are *can, could, may, might, will, would, shall, should, must, ought to, need, dare, used to*. Three facts hold for all of them.
- A modal is followed by the **base form** of the verb: *She can swim.* Never *She can swims* or *can to swim*.
- A modal takes no -s in the third person: *He must go.*
- To make a question, put the modal first: *Can you help?*

> **Watch:** *Ought to* and *used to* keep **to**. *You ought to go.* But after *must, can, may, should* there is no *to*.

### Meanings
| Modal | Use | Example |
|---|---|---|
| can / could | ability; could is past ability or polite request | *He can drive. Could you help me?* |
| may / might | permission; possibility (might is weaker) | *May I come in? It might rain.* |
| must | strong duty; strong logical certainty | *You must wear a helmet.* |
| have to | outside rule; needs tense forms | *I had to leave early.* |
| should / ought to | advice, moral duty | *You should sleep early.* |
| need | necessity; in questions and negatives it can act as a modal | *You need not come. Need I come?* |
| dare | courage; modal in negatives and questions | *He dare not speak.* |
| will / shall | future; shall with I and we for offers | *Shall I open the window?* |
| would | past habit, polite request | *He would visit every summer.* |
| used to | past habit or state, now stopped | *I used to smoke.* |

### Modals with the perfect
- **should have / ought to have + V3:** a duty not done. *You should have called.*
- **could have + V3:** a chance that was missed. *She could have won.*
- **must have + V3:** a certain guess about the past. *He must have missed the train.*
- **may / might have + V3:** a possible guess about the past. *They might have left.*
- **needn't have + V3:** did it, but it was not needed. *You needn't have come.*
- **would have + V3:** the result clause of a past unreal condition.

### Conditionals
| Type | If-clause | Result clause | Sense |
|---|---|---|---|
| Zero | present simple | present simple | general truth: *If you heat ice, it melts.* |
| First | present simple | will / can / may + base | real future: *If it rains, we will stay.* |
| Second | past simple (were for all subjects) | would / could / might + base | unreal present: *If I were rich, I would travel.* |
| Third | past perfect | would have + V3 | unreal past: *If she had studied, she would have passed.* |

- Use **were** for all persons in a second-conditional if-clause: *If I were you.*
- Do not use *will* or *would* in the if-clause itself. *If it rains* is right; *If it will rain* is wrong.
- **Unless** = if not, and it already carries the negative: *Unless you hurry, you will miss it.*
- Inverted forms drop *if*: *Had I known, I would have come. Were he here, he would help. Should you need help, call me.*
- **Wish** takes the past for the present and the past perfect for the past: *I wish I knew. I wish I had gone.*
- **As if / as though** with an unreal situation takes the past: *He talks as if he owned the place.*

> **Tip:** In a third conditional both halves look back. If either half looks forward or present, the tense is wrong.
""",
    tricks=[
        trick("Match the type by the if-clause",
              "Read only the if-clause. Present simple: use will or can in the result. Past simple: use would in the result. Past perfect: use would have + V3.",
              "If he had left earlier, he ___ the train. (would catch / would have caught / will catch)",
              ["The if-clause is past perfect.", "That is a third conditional.", "The result needs 'would have + V3': 'would have caught'."],
              "would have caught"),
        trick("Modal + base form",
              "After any modal the next verb is bare. If you see a modal followed by to, -s, -ing or -ed, that is the error. The only exceptions are ought to and used to."),
    ],
    mistakes=[
        mis("She can sings well.", "She can sing well. A modal takes the base form."),
        mis("You must to go now.", "You must go now."),
        mis("If it will rain, we will stay home.", "If it rains, we will stay home."),
        mis("If I would have money, I would buy a car.", "If I had money, I would buy a car."),
        mis("If I was you, I would apologise.", "If I were you, I would apologise."),
        mis("Unless you do not work hard, you will fail.", "Unless you work hard, you will fail."),
        mis("You needn't to come.", "You needn't come."),
    ],
    revision=[
        "Modal + bare verb; no -s; no to (except ought to and used to).",
        "must = duty or certainty; should = advice; may = permission or possibility.",
        "should have + V3 = duty not done; must have + V3 = certain guess about the past.",
        "First: if + present, will + base. Second: if + past, would + base. Third: if + past perfect, would have + V3.",
        "Use were for all subjects in the second conditional.",
        "No will or would inside the if-clause.",
        "Unless = if not; do not add a second negative.",
    ],
    patterns=[
        pat("mod-p1", "Modal + base form", "very common",
            "The sentence has can, may, must, should or will, and the next verb has -s, -ing, -ed or a to.",
            ["Find the modal.", "Look at the verb right after it.", "If it is not the bare verb, that is the error."],
            "Modals are helper verbs and carry the tense, so the main verb stays bare.",
            "She can ___ five languages. (speaks / speak / speaking / to speak)",
            ["The modal is 'can'.", "The verb after it must be bare: 'speak'."],
            "speak"),
        pat("mod-p2", "Shades of meaning", "common",
            "The blank sits in a sentence expressing duty, advice, permission, ability or a guess.",
            ["Name the meaning: strong duty, advice, permission, ability, guess.", "Match it: must, should, may, can, might.",
             "Choose the modal for that meaning."],
            "Each modal has one main job, and the stem tells you which job is needed.",
            "You ___ wear a seat belt; it is the law. (must / might / could / would)",
            ["The law is a strong duty.", "Strong duty takes 'must'."],
            "must"),
        pat("mod-p3", "Modal + have + V3", "common",
            "The sentence talks about the past and the options include should have, must have, could have, needn't have.",
            ["Find the clue: regret, certainty, missed chance or unneeded act.", "Match: should have (duty), must have (certain guess), could have (chance), needn't have (not needed).", "Choose the matching option."],
            "The perfect form after a modal points back to a past event.",
            "The road is wet, so it ___ rained last night. (must have / should have / would have)",
            ["The wet road is a clue for a certain guess.", "A certain guess about the past takes 'must have'."],
            "must have"),
        pat("mod-p4", "Conditional tense matching", "very common",
            "The sentence has an if-clause and a blank in the result clause, or the reverse.",
            ["Read the if-clause tense.", "Present simple: will + base. Past simple: would + base. Past perfect: would have + V3.",
             "Choose the option that matches."],
            "Each conditional type pairs one if-tense with one result form.",
            "If I ___ you, I would accept the offer. (am / was / were / be)",
            ["The result has 'would', so this is a second conditional.", "The if-clause takes 'were' for all persons."],
            "were"),
        pat("mod-p5", "Unless and inverted conditionals", "common",
            "The sentence has unless, or starts with Had, Were or Should in place of if.",
            ["Unless means if not, so keep the verb positive.", "Had + subject + V3 means if + past perfect.",
             "Should + subject + base means if + present."],
            "Dropping if and inverting the subject gives the same meaning.",
            "Unless you ___ hard, you will not pass. (study / do not study / will study / studied not)",
            ["'Unless' already means 'if not'.", "The verb must stay positive: 'study'."],
            "study"),
        pat("mod-p6", "Wish and as if", "common",
            "The sentence has wish, as if or as though, and the situation is unreal.",
            ["Present unreal wish: use the past (I wish I knew).", "Past unreal wish: use the past perfect (I wish I had gone).",
             "Use were for all persons in the unreal present."],
            "The unreal situation moves one step back in time.",
            "I wish I ___ the answer now. (know / knew / had known / will know)",
            ["The wish is about the present.", "The verb goes back one step: past 'knew'."],
            "knew"),
        pat("mod-p7", "Need, dare and used to", "occasional",
            "The sentence has need, dare or used to in a negative, a question or a habit.",
            ["Need and dare act as modals in negatives and questions, with no -s and no to.",
             "Used to is a past habit that has stopped.", "Check that the verb after it is bare."],
            "These three verbs switch between modal and ordinary use.",
            "You ___ come tomorrow; the meeting is cancelled. (needn't / don't need / needs not / need not to)",
            ["'Needn't' works as a modal.", "It is followed by a bare verb, so 'needn't come' is right."],
            "needn't"),
    ],
)

# =====================================================================
# 7. Comparison and question tags
# =====================================================================
SUBS["ge-comparison-question-tags"] = dict(
    concept=(
        "Adjectives and adverbs have three degrees: positive, comparative and superlative. "
        "A question tag is the short question added to a statement, like *isn't it?*. "
        "Both follow strict patterns, so learn the pattern and check it."
    ),
    notes=r"""### The three degrees
| Degree | Use | Example |
|---|---|---|
| Positive | equal or plain | *as tall as, so tall as* |
| Comparative | two things | *taller than, more careful than* |
| Superlative | three or more | *the tallest, the most careful* |

- Short words add -er and -est: *tall, taller, tallest*.
- Long words (three or more syllables) use *more* and *most*.
- Two-syllable words: -y words add -er (*happier*); most others use *more*.
- Never use both: *more better, most cleverest* are wrong.
- Irregular forms: **good/well - better - best; bad/ill - worse - worst; far - farther/further - farthest/furthest; little - less - least; much/many - more - most; old - older/elder - oldest/eldest**.

### Rules for comparatives
- The comparative takes **than**, not *then* or *from*. *She is taller than I am.*
- Compare like with like: *The climate of Shimla is cooler than **that** of Delhi.* Not *than Delhi*.
- Add *other* or *else* when a thing is compared with its own group: *Ravi is taller than any **other** boy in the class.*
- Do not add *other* to a superlative: *He is the best of all boys.*
- Latin comparatives take **to**: *senior, junior, superior, inferior, prior, preferable to*.
- **Elder / eldest** are used for family members only. *Older* works for anyone.
- **Later / latest** speak of time. **Latter / last** speak of order.
- **Farther** is distance. **Further** is more or additional: *further details*.
- **Double comparative:** *The more you practise, the better you get.*
- **Superlative sense in other forms:** *No other city is as big as Mumbai. Mumbai is bigger than any other city.*

### Question tags
A tag repeats the helper verb of the statement with the opposite polarity.
- **Positive statement, negative tag:** *She sings well, doesn't she?*
- **Negative statement, positive tag:** *He is not late, is he?*
- The tag uses a pronoun, not a noun: *Ravi is here, isn't **he**?*
- The tag verb copies the helper: *is, are, was, has, will, can*. If there is no helper, use **do, does, did**.

### Special cases
| Statement | Tag |
|---|---|
| I am | aren't I? |
| Let's | shall we? |
| Let us (asking permission) | will you? |
| Imperative (command) | will you? |
| Do (request) | won't you? |
| There is / are | isn't there? / aren't there? |
| Nobody, none, no one, neither, nothing | positive tag with **they** (it for nothing): *Nobody called, did they?* |
| Everybody, someone, anyone | they: *Everyone came, didn't they?* |
| Hardly, seldom, never, rarely, barely, few, little | positive tag: *He seldom lies, does he?* |
| Must (necessity) | needn't: *You must go, needn't you?* |
| Used to | didn't (or usedn't) |
| Had better | hadn't |
| Ought to | shouldn't |
| Would rather | wouldn't |
| I have (main verb, possession) | haven't or don't |

> **Tip:** A word with a negative meaning such as *hardly* or *seldom* makes the statement negative. So the tag is positive.

### Comparison of like parts
The two sides of *than* or *as* must be the same kind: a person with a person, a noun with a noun.
- Wrong: *Her handwriting is better than Sita.* Right: *than **that of** Sita* or *than **Sita's***.
""",
    tricks=[
        trick("Flip the polarity",
              "Read the statement. Note whether it is positive or negative. Then use the helper verb with the opposite sign and a pronoun. Command? Use will you. Let's? Use shall we.",
              "She has never lied to you, ___? (has she / hasn't she / does she / didn't she)",
              ["'Never' makes the statement negative.", "The tag must be positive.", "The helper is 'has': 'has she'."],
              "has she"),
        trick("Watch than, that of and other",
              "When a comparison feels odd, check two things. First: are two like things compared (use *that of* or *those of*)? Second: does the comparison come from the same group (add *other*)?"),
    ],
    mistakes=[
        mis("She is more cleverer than her sister.", "She is cleverer than her sister."),
        mis("This is the most best book.", "This is the best book."),
        mis("He is taller than any boy in the class.", "He is taller than any other boy in the class."),
        mis("The climate of Goa is better than Delhi.", "The climate of Goa is better than that of Delhi."),
        mis("He is senior than me.", "He is senior to me."),
        mis("Nobody came, didn't they?", "Nobody came, did they?"),
        mis("I am late, amn't I?", "I am late, aren't I?"),
    ],
    revision=[
        "Never use more or most with an -er or -est word.",
        "Comparative takes than; Latin comparatives (senior, junior, superior, inferior, prior) take to.",
        "Add other when comparing with the rest of the same group.",
        "Compare like with like: that of, those of.",
        "Question tag: opposite polarity, helper verb, pronoun.",
        "I am - aren't I; Let's - shall we; command - will you; there is - isn't there.",
        "Nobody, hardly, seldom, never: statement is negative, tag is positive.",
    ],
    patterns=[
        pat("cmp-p1", "Double comparative or superlative", "very common",
            "A sentence has more or most beside an -er or -est word, or beside an irregular comparative.",
            ["Spot more or most.", "Check the next word.", "If it already has -er or -est, or is irregular, delete more or most."],
            "One degree marker is enough.",
            "She is more cleverer than her brother. Which words are wrong?",
            ["'Cleverer' is already a comparative.", "'More' repeats it."],
            "more"),
        pat("cmp-p2", "Than, to, and like with like", "very common",
            "A comparison uses than, to, or compares something with a place or a person's belongings.",
            ["Latin comparative (senior, junior, superior, prefer): use to.", "Other comparatives: use than.",
             "Check that both sides of than are alike; use that of or those of."],
            "Two things compared must be the same type.",
            "The population of India is larger than ___ of the USA. (that / those / it / the)",
            ["Population is compared with population.", "'Population' is singular, so use 'that'."],
            "that"),
        pat("cmp-p3", "Any other and superlative sense", "common",
            "A comparative sentence has 'any', or a superlative sentence has 'other'.",
            ["Is the thing part of the group it is compared with?", "If yes, use 'any other' with the comparative.",
             "Do not put 'other' in a superlative."],
            "A thing cannot be compared with itself.",
            "Mount Everest is higher than ___ mountain in the world. (any other / any / other)",
            ["Everest is itself a mountain.", "So the comparison needs 'any other'."],
            "any other"),
        pat("cmp-p4", "Question tag polarity", "very common",
            "A statement ends in a comma and a short blank like ___?",
            ["Is the statement positive or negative?", "Use the opposite in the tag.", "Copy the helper verb, or do/does/did, plus a pronoun."],
            "The tag asks the listener to confirm the statement.",
            "You have finished the work, ___? (haven't you / have you / don't you / do you)",
            ["The statement is positive.", "The tag is negative with helper 'have': 'haven't you'."],
            "haven't you"),
        pat("cmp-p5", "Special tag cases", "common",
            "The statement is a command, Let's, I am, there is, nobody or hardly/never/seldom.",
            ["Command: will you. Let's: shall we. I am: aren't I.", "There: isn't there.",
             "Nobody, no one, hardly, seldom: positive tag."],
            "These forms have fixed tags that do not follow the plain pattern.",
            "Let's go for a walk, ___? (shall we / will we / don't we / won't we)",
            ["The statement begins with 'Let's'.", "'Let's' takes 'shall we'."],
            "shall we"),
        pat("cmp-p6", "Elder / older, later / latter, farther / further", "common",
            "The blank sits between two similar-looking comparatives.",
            ["Family members: elder. Anyone: older.", "Time: later. Order: latter.", "Distance: farther. Extra or more: further."],
            "Each pair has a narrow, fixed use.",
            "My ___ brother is an engineer. (elder / older / oldest)",
            ["'Brother' is a family member.", "'Elder' is used for family members."],
            "elder"),
        pat("cmp-p7", "Positive, comparative, superlative conversion", "occasional",
            "A sentence is to be changed from one degree to another with the same meaning.",
            ["Superlative: no other X is as ... as Y.", "Comparative: Y is ... than any other X.",
             "Positive: not so ... as."],
            "The same fact can be said in all three degrees.",
            "Change to comparative: Delhi is the biggest city in north India.",
            ["The superlative means the city is bigger than all others.", "Use 'any other' with the comparative."],
            "Delhi is bigger than any other city in north India."),
    ],
)

# =====================================================================
# 8. Non-finites and inversion
# =====================================================================
SUBS["ge-non-finites-inversion"] = dict(
    concept=(
        "Non-finite verb forms are the infinitive (to go), the gerund (going) and the participle (going, gone). "
        "They do not show tense or number by themselves. "
        "Inversion means putting the helper verb before the subject, as in questions and after some negative words."
    ),
    notes=r"""### Infinitive and gerund
Some verbs are followed by an infinitive, some by a gerund, and a few by either.
| Follows | Verbs |
|---|---|
| **to + verb** | want, hope, decide, plan, promise, refuse, manage, afford, offer, learn, fail, agree, wish |
| **-ing** | enjoy, avoid, finish, mind, practise, suggest, deny, admit, consider, postpone, imagine, keep, escape |
| **either** (meaning same) | begin, start, like, love, hate, continue, prefer |
| **either** (meaning changes) | stop, remember, forget, try, regret |

- *He stopped **to smoke*** = he paused in order to smoke. *He stopped **smoking*** = he quit.
- *I remember **meeting** him* = I recall it. *Remember **to post** it* = do not forget the task.
- After a **preposition**, use the gerund: *She is fond **of singing**.* *He left **without saying** goodbye.*
- **To** as a preposition needs a gerund: *look forward to meeting, used to waking early, object to paying, be accustomed to working*.
### Bare infinitive and fixed patterns
- After **let, make, see, hear, help** the bare infinitive follows: *She made me **laugh**.* But in the passive the *to* returns: *I was made **to** laugh.*
- After **modal verbs, had better, would rather** use the bare verb.
- *It is worth, no use, no good, cannot help, be busy* + gerund: *It is no use **crying**.*
- The **split infinitive** puts a word between *to* and the verb (*to quickly run*). Exams prefer the unsplit form.

### Participles and their subjects
- **Present participle (-ing)** shows an action at the same time: *Walking home, I met him.*
- **Past participle (V3)** has a passive or completed sense: *Tired of waiting, she left.*
- A participle phrase at the start must belong to the subject that follows. Otherwise it dangles.
  - Wrong: *Walking down the street, the rain started.* Right: *Walking down the street, **I** felt the rain.*
- Perfect participle **having + V3**: *Having finished the work, he left.*

> **Watch:** After a participle phrase, ask "who did that action?" The subject of the main clause must answer.

### Inversion
Inversion puts the helper before the subject: *Rarely **have I seen** such a view.*
- **Questions:** *Where **did he go**?* The helper is before the subject.
- **Negative openers** force inversion: **never, rarely, seldom, hardly, scarcely, barely, no sooner, nowhere, little, not only, not until, under no circumstances, on no account, at no time**.
  - *Never **have I seen** such a crowd.*
  - *No sooner **had he left** than it rained.*
  - *Not only **did she sing**, but she also danced.*
  - *Hardly **had I sat** when the phone rang.*
- **So / neither / nor** agreement: *He likes tea, and **so do I**. She cannot swim, and **neither can he**.*
- **Conditional inversion:** *Had I known, ... Were he here, ... Should you need, ...*
- **Only + adverb** at the start: *Only then **did I realise** my mistake. Only after dinner **did she speak**.*
- Do **not** invert an embedded question: *I asked where he went.* Not *where did he go*.

> **Tip:** A sentence starting with a negative word and followed by the subject and then the verb is nearly always wrong.
""",
    tricks=[
        trick("Preposition then -ing",
              "If the word before the blank is a preposition (of, in, at, without, after, before, by, about), the verb must end in -ing. Watch for to in look forward to and used to: it is a preposition there.",
              "She is looking forward to ___ you soon. (see / seeing / saw / seen)",
              ["'Look forward to' has 'to' as a preposition.", "A preposition takes a gerund: 'seeing'."],
              "seeing"),
        trick("Negative start means flip",
              "When a sentence opens with never, rarely, hardly, no sooner, not only or not until, flip the first helper before the subject. If there is no helper, add do, does or did."),
    ],
    mistakes=[
        mis("She enjoys to dance.", "She enjoys dancing."),
        mis("He is interested to learn music.", "He is interested in learning music."),
        mis("I look forward to meet you.", "I look forward to meeting you."),
        mis("Hardly he had left when it rained.", "Hardly had he left when it rained."),
        mis("Never I have seen such a crowd.", "Never have I seen such a crowd."),
        mis("Walking down the road, the rain began.", "Walking down the road, I felt the rain begin."),
        mis("She asked where did he go.", "She asked where he went."),
    ],
    revision=[
        "enjoy, avoid, finish, mind, suggest, deny, practise + gerund.",
        "want, hope, decide, refuse, manage, promise + to + verb.",
        "After a preposition use -ing; look forward to, used to, object to take -ing.",
        "let, make, see, hear + bare infinitive; the passive of make adds to.",
        "stop, remember, forget, try change meaning with the form.",
        "A participle phrase must match the subject that follows it.",
        "Negative openers (never, hardly, no sooner, not only) force inversion.",
        "So do I / neither can he: invert the helper verb.",
    ],
    patterns=[
        pat("nfi-p1", "Verb + infinitive or gerund", "very common",
            "The blank follows a verb such as enjoy, avoid, hope, decide, mind or suggest.",
            ["Find the main verb.", "Check the verb list: gerund group or infinitive group.", "Choose -ing or to + verb accordingly."],
            "Each verb selects its own pattern, and the exam uses a fixed core set.",
            "She avoided ___ to him. (to talk / talking / talk / talked)",
            ["'Avoid' takes a gerund.", "Choose 'talking'."],
            "talking"),
        pat("nfi-p2", "Preposition + gerund", "very common",
            "The blank comes right after a preposition, including 'to' in look forward to and used to.",
            ["Identify the preposition.", "Remember that a preposition is followed by a noun or gerund.", "Change to -ing form."],
            "A preposition needs a noun-like word after it.",
            "He left without ___ goodbye. (say / to say / saying / said)",
            ["'Without' is a preposition.", "The verb must be a gerund: 'saying'."],
            "saying"),
        pat("nfi-p3", "Dangling participles", "common",
            "A sentence begins with an -ing or -ed phrase followed by a comma and a subject.",
            ["Ask who did the action in the phrase.", "Does the subject after the comma answer that?",
             "If not, change the subject or rewrite the phrase."],
            "The opening phrase describes the noun right after the comma.",
            "Reading the newspaper, the tea got cold. What is wrong?",
            ["The tea did not read the newspaper.", "The phrase and the subject do not match."],
            "The participle dangles; a person must be the subject: Reading the newspaper, I let the tea go cold."),
        pat("nfi-p4", "Inversion after negative openers", "very common",
            "A sentence opens with never, hardly, no sooner, rarely, not only, seldom or little.",
            ["Spot the negative opener.", "Put the helper verb before the subject.", "If no helper exists, add do, does or did."],
            "English flips the subject and the helper after such openers.",
            "Hardly ___ the class begun when the bell rang. (had / has / did / was)",
            ["'Hardly' opens the sentence, so invert.", "The past perfect helper 'had' comes before the subject."],
            "had"),
        pat("nfi-p5", "Bare infinitive after let, make, see, hear", "common",
            "The blank follows let, make, see, hear or help, with an object between.",
            ["Spot the verb.", "In the active, use the bare verb (no to).", "In the passive, add to."],
            "These verbs are followed by an object and a bare infinitive.",
            "The teacher made the boy ___ the answer. (repeat / to repeat / repeating)",
            ["'Made' is followed by a bare infinitive.", "Choose 'repeat'."],
            "repeat"),
        pat("nfi-p6", "Stop, remember, forget, try", "common",
            "The blank follows stop, remember, forget, try or regret and both forms look possible.",
            ["Read the meaning.", "Verb + to: a purpose or a task ahead.", "Verb + -ing: an action already done or an experiment."],
            "The form tells the reader whether the action is past or still to come.",
            "Please remember ___ the letter on your way. (to post / posting)",
            ["It is a task still ahead.", "Use 'to post'."],
            "to post"),
        pat("nfi-p7", "So, neither and nor agreement", "occasional",
            "A second clause starts with so, neither or nor and refers to the first clause.",
            ["Positive first clause: so + helper + subject.", "Negative first clause: neither or nor + helper + subject.",
             "Copy the helper of the first clause."],
            "The reply agrees or disagrees with the first clause and flips the helper.",
            "She can swim, and so ___ her brother. (can / does / is / will)",
            ["The first clause has 'can'.", "Copy it: 'so can her brother'."],
            "can"),
    ],
)
