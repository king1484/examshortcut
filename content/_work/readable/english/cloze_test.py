"""Readable rewrite of English > Cloze Test (all 5 subtopics).

Plain English, short sentences, tables for word lists, one method per blank type.
Every fact from the old notes is kept; old pattern ids are kept and new ids continue each prefix.
Run: python cloze_test.py  (patches content/core/topics/english/cloze-test.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "cloze-test.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Strategy
# =====================================================================
SUBS["cloze-strategy"] = dict(
    concept=(
        "A cloze test is one short passage with five numbered blanks. You choose the word that fits each blank. "
        "Every sentence in the passage gives clues, so a fixed method works better than a big vocabulary. "
        "Read the whole passage first, predict your own word, then match it with the options."
    ),
    notes=r"""### What a cloze test is
A cloze test is one short passage, usually 100 to 150 words long. Five words are removed and the blanks are numbered. Each question asks you to restore one blank.

> **Rule:** The passage is one connected piece. Every sentence limits what the blanks can be.

That is why a fixed method beats raw vocabulary.

### The five-step method
Use the same steps on every passage.

1. **Read the whole passage once.** Ignore the blanks as far as you can. Find the theme and the time frame: past story, general present or future plan.
2. **Find the tense anchor.** The opening sentences usually fix the tense that most verb blanks must follow.
3. **Predict your own word.** For each blank, decide what word the sentence needs before you look at the options.
4. **Match the options.** Pick the option closest to your word. If none matches, eliminate by grammar (number, tense, part of speech) and by logic.
5. **Read the finished passage.** It must sound like ordinary prose. A jarring blank is usually a wrong choice.

### Know the blank type
The type of blank tells you what to check first.

| Blank type | What decides the answer | First check |
|---|---|---|
| Verb form or tense | Time words nearby and the subject's number | Find the anchor word (yesterday, every day, since, by evening) |
| Connector | The logic between the two clauses | Ask: contrast, cause, result or addition? |
| Preposition or phrasal verb | The fixed partner of the neighbouring word | Find the verb, adjective or noun that governs it |
| Noun or vocabulary | Meaning that fits the sentence and the theme | Predict your own word first |
| Article or determiner | The sound of the next word, and whether the noun is known | Say the phrase aloud |

> **Tip:** Say the phrase aloud in your head. A wrong article or preposition often sounds odd.

### Plan your time
Keep to this budget for one passage.

- Under two minutes for the first full read.
- 20 to 30 seconds for each blank.
- 30 seconds for the final read-through.

Attempt the whole cloze set in one sitting. The passage stays in your short-term memory only while you work on it.

### Never solve a blank alone
Some options fit their own sentence but clash with the passage. They contradict its tense or its theme. Such an option is a planted trap.

> **Watch:** The final read-through exists to catch these traps. Do not skip it.

Suppose the passage is a story in the past. An option in the present tense may look fine inside one sentence. It is still wrong.
""",
    tricks=[
        {"title": "Tense anchor first",
         "body": "Before you touch any blank, underline the time words: every morning, last month, by evening. Verb blanks obey these anchors.",
         "example": {"q": "The passage opens: *Every morning, before the city fully ___ ...* Options: awaken / awakens / awakened / is awaken.",
                     "steps": ["*Every morning* signals a habit, so use the simple present.", "*City* is singular, so the verb takes -s."],
                     "answer": "awakens"}},
        {"title": "Predict, then match",
         "body": "Cover the options with your hand. Read the sentence and think of your own word. Options are written around the right meaning, so a far-off option is usually wrong."},
        {"title": "The read-aloud finish",
         "body": "After you answer all five, read the passage as if someone else wrote it. Grammar errors and logic breaks become easy to hear. Re-check any blank where you stumble."},
    ],
    mistakes=[
        mis("Reading and solving one sentence at a time.", "Read the whole passage first. Fix the theme and the tense before any blank."),
        mis("Looking at the options before thinking of a word.", "Predict your own word first. Then match it with the options."),
        mis("Choosing an option that fits its own sentence but breaks the passage's tense or theme.", "Check every choice against the whole passage."),
        mis("Skipping the final read-through to save time.", "Keep 30 seconds to read the finished passage. It catches planted traps."),
        mis("Leaving the set half done and coming back later.", "Finish the whole cloze set in one sitting while the passage is fresh."),
    ],
    revision=[
        "Five steps: read the passage, find the tense anchor, predict a word, match options, read the finished passage.",
        "The opening sentences usually fix the tense for the verb blanks.",
        "Name the blank type first: verb, connector, preposition, vocabulary or article.",
        "Time budget: under 2 minutes to read, 20-30 seconds per blank, 30 seconds to check.",
        "An option that clashes with the passage's tense or theme is a planted trap.",
        "Attempt the whole cloze set in one sitting.",
    ],
    patterns=[
        pat("cls1", "Blank whose answer needs the passage's overall theme", "common",
            "The blank sentence is vague alone. The theme of the passage decides the word.",
            ["Read the whole passage and name its theme in three words.", "Read the blank sentence and say what idea is missing.",
             "Pick the option that fits both the sentence and the theme."],
            "The theme narrows four possible words to one.",
            "Passage: *The town's old lake was dirty for years. Volunteers now clean it every Sunday, so the water is (1) ___ again.* Options: clear / costly / crowded / silent.",
            ["Theme: cleaning a dirty lake.", "The result of cleaning is better water.", "*Clear* fits the theme. The other options do not."],
            "clear"),
        pat("cls2", "All four options grammatical: meaning decides", "very common",
            "Every option fits the grammar. The options are different words, not different forms.",
            ["Ignore grammar. It cannot help here.", "Say the missing idea in plain words.", "Choose the option that names that idea.",
             "Read the sentence again with your choice."],
            "When grammar is equal, only meaning can separate the options.",
            "*The librarian was so ___ that she never raised her voice, even when the hall was noisy.* Options: calm / angry / lazy / curious.",
            ["The librarian never raised her voice.", "The missing idea is a quiet, steady nature.", "Only *calm* fits."],
            "calm"),
        pat("cls3", "The clue sits in a neighbouring sentence", "very common",
            "The blank sentence alone is unclear. The next or the previous sentence explains it.",
            ["Read the sentence before and after the blank.", "Find the sentence that explains the blank.", "Choose the word that agrees with that explanation."],
            "Passage writers often put the clue next to the blank, not inside it.",
            "*Rohan ___ the first bus. The next one came only after an hour, so he reached late.* Options: missed / caught / drove / drew.",
            ["The next bus came after an hour.", "So he must have failed to get on the first bus.", "*Missed* fits."],
            "missed"),
        pat("cls4", "Option fits the sentence but clashes with the passage", "common",
            "Two options look right inside the sentence. One of them breaks the tense or the theme of the passage.",
            ["Test each option inside its own sentence.", "Find the tense anchor of the passage.", "Reject the option that clashes with it."],
            "This is the standard planted trap in cloze tests.",
            "*Last winter, a storm hit our village. It (1) ___ many roofs and trees.* Options: damages / damaged / will damage / damaging.",
            ["*Last winter* fixes the past.", "*Damages* fits a sentence alone but not this passage.", "*Damaged* keeps the past tense."],
            "damaged"),
        pat("cls5", "Verb blank fixed by a tense anchor", "very common",
            "A time word such as every morning, last year or by evening sits near the blank or at the start.",
            ["Underline the time word.", "Choose the tense it needs.", "Check the subject's number.", "Confirm the form with the options."],
            "One time word fixes the tense, so you can answer in seconds.",
            "*Every morning, Sita ___ the temple before school.* Options: goes / went / will go / gone.",
            ["*Every morning* signals a habit in the present.", "*Sita* is singular, so the verb takes -s.", "*Goes* fits."],
            "goes"),
    ],
)

# =====================================================================
# 2. Grammar fit
# =====================================================================
SUBS["cloze-grammar-fit"] = dict(
    concept=(
        "Most cloze blanks are won by grammar before vocabulary. Three or four of the five blanks usually follow a grammar rule. "
        "The passage fixes the time, the subject and the structure, and the blank must obey them. "
        "Check tense first, then agreement, then the form of the word."
    ),
    notes=r"""### What grammar blanks test
In most passages, three or four blanks depend on a grammar rule, not on word power. The passage sets the time, the subject and the structure. The blank must obey them.

> **Rule:** For every verb blank, run two checks. Does the tense match the passage? Does the form match the subject? An option that passes only one check is a planted distractor.

### Subject-verb agreement
Find the true subject. Ignore the words between it and the verb.

- Correct: The quality of the mangoes **is** poor. Wrong: *The quality of the mangoes are poor.* The subject is *quality*.
- Correct: The list of items **is** on the table. Wrong: *The list of items are on the table.*
- *Each, every, either, neither, everyone* and *one of* + plural noun take a singular verb.
- *A number of* takes a plural verb. *The number of* takes a singular verb.

> **Tip:** Delete the phrase between the subject and the blank. Read the short skeleton: *a group ___ discipline*.

### The time frame
The first sentence usually sets the tense. Every verb must stay inside that frame.

- Habit or general truth: simple present. *The shop **opens** at nine.*
- Past story: past forms. *When Arun was small, he **drafted** a reply.*
- *Yesterday, last year, ago* signal the past. *Now, still, these days, every morning* signal the present.
- *Since, for, already, yet* signal perfect forms.
- A habit inside a past story stays past: *Every evening he **made** new kites.*

Use a perfect form after *by evening* or *by the time* only when the sentence looks back from a later point. In plain story order, use the simple past.

### Verb forms after other words
Only a finite verb can be the main verb. After some words, a fixed form is compulsory.

| After | Use | Example |
|---|---|---|
| enjoy, avoid, mind, finish, suggest, keep | -ing | He enjoys **showing** old kites. |
| decide, plan, hope, refuse, manage, teach someone | to + base form | Gardening has taught him **to be** patient. |
| a preposition | -ing | She is good at **solving** puzzles. |

A bare -ing word cannot be the main verb. Wrong: *A group developing its own discipline.* Correct: *A group **develops** its own discipline.*

### Articles
- *A / an* = first mention, or one of many. *He gave him **a** bucket the next day.*
- *The* = already known, or one of a kind. ***The** sky above the lane was full of kites.*
- No article for most general plural nouns. *Trees give shade.*
- Sound decides *a* or *an*, not spelling: *a university, an hour, a European.*

### Adjective or adverb, and pronouns
After a linking verb (*be, look, seem, feel, taste, smell, sound*), use an adjective. *The tree looks **attractive**.*

After an action verb, use an adverb. *She sings **beautifully**.*

A pronoun must match its noun in number and gender. Its case must fit its job.

- Correct: The committee published **its** report.
- Correct: Between you and **me**, the plan is weak.

> **Watch:** *Theirs* and *their's* never go before a noun. Use *their* or *its*.
""",
    tricks=[
        {"title": "Strip-to-subject",
         "body": "Delete every phrase between the subject and the verb blank. Then apply agreement to the short skeleton.",
         "example": {"q": "*A group that walks together ___ its own quiet discipline.* Options: develop / develops / developing / developed.",
                     "steps": ["Skeleton: *a group ___ discipline*.", "The subject is singular and the meaning is habitual present."],
                     "answer": "develops"}},
        {"title": "Only-one-past trick",
         "body": "In a past story, one option may be the only past form among present and -ing forms. The anchor already decided it. Mark it and move on."},
        {"title": "Say the article aloud",
         "body": "For an a/an blank, pronounce the first sound of the next word. It is *an hour* but *a university*. Sound decides it, not the first letter."},
    ],
    mistakes=[
        mis("Agreeing the verb with the nearest noun.", "Find the true subject. Ignore the words between it and the verb."),
        mis("Using a perfect tense such as *had joined* in a plain past story because *by evening* looks like an anchor.", "Use the simple past unless the sentence truly looks back from a later point."),
        mis("Choosing the base verb after a singular subject: *the city awaken*.", "Add -s to the simple present verb after a singular subject."),
        mis("Writing *an* before any word that starts with a vowel letter, such as *an one-rupee coin*.", "Go by sound. *One* starts with a consonant sound, so use *a one-rupee coin*."),
        mis("Using an adverb after *look* or *seem*.", "Use an adjective after a linking verb: *looks attractive*."),
    ],
    revision=[
        "Find the true subject first. Ignore the words between it and the verb.",
        "Fix the passage's time frame. Keep every verb inside it.",
        "enjoy, avoid, mind, finish + -ing. decide, plan, hope, refuse, manage + to + base form.",
        "Preposition + -ing: good at solving.",
        "a/an = first mention. the = known or one of a kind. Sound decides a or an.",
        "Linking verb + adjective. Action verb + adverb.",
        "A pronoun matches its noun in number and gender, with the right case.",
    ],
    patterns=[
        pat("clg1", "Subject-verb agreement blank", "very common",
            "A long phrase or a second noun sits between the subject and the verb blank.",
            ["Cut out the phrase between the subject and the blank.", "Read the short skeleton.", "Match the verb to the true subject."],
            "The trap noun sits nearest the blank, but it is not the subject.",
            "*The list of names ___ on the notice board.* Options: is / are / were / be.",
            ["Skeleton: *the list ___ on the board*.", "*List* is singular, so use *is*."],
            "is"),
        pat("clg2", "Tense / time-frame blank", "very common",
            "The passage opens with a time frame such as a past story or a habit.",
            ["Find the anchor in the opening lines.", "Choose the tense of that frame.", "Match the form to the subject."],
            "Every verb blank must stay inside the frame the passage set.",
            "*When Arun was young, he ___ kites every evening.* Options: makes / made / has made / making.",
            ["*Was young* sets a past story.", "An evening habit inside a past story stays past."],
            "made"),
        pat("clg3", "Verb form: gerund or infinitive after another word", "common",
            "The blank comes right after a verb such as enjoy, avoid, decide, plan or a preposition.",
            ["Find the word before the blank.", "Recall its pattern: -ing or to + base form.", "Pick the option in that pattern."],
            "A fixed word decides the form. Meaning does not help.",
            "*She avoids ___ the crowded market.* Options: to visit / visiting / visit / visited.",
            ["*Avoid* is followed by -ing.", "*Visiting* fits."],
            "visiting"),
        pat("clg4", "Article / determiner blank", "common",
            "The blank sits before a noun. The options are a, an, the or no article.",
            ["Say the next word aloud.", "Listen to its first sound.", "Then decide: is the noun known or one of many?"],
            "Sound decides a or an. Known nouns take the.",
            "*He waited for ___ hour outside the office.* Options: a / an / the / no article.",
            ["*Hour* starts with a vowel sound because *h* is silent.", "The noun is not a known one, so *an* fits."],
            "an"),
        pat("clg5", "Adjective or adverb blank", "common",
            "The blank comes after a verb. The options are two forms of one word, such as beautiful and beautifully.",
            ["Name the verb before the blank.", "Is it a linking verb (be, look, seem, feel)? Use an adjective.", "Is it an action verb? Use an adverb."],
            "The verb type decides which form fits.",
            "*The garden looks ___ in spring.* Options: beautiful / beautifully / beauty / beautify.",
            ["*Looks* is a linking verb here.", "A linking verb takes an adjective."],
            "beautiful"),
        pat("clg6", "Pronoun blank", "occasional",
            "The blank is a pronoun. Its noun sits earlier in the sentence.",
            ["Find the noun the pronoun refers to.", "Match its number and gender.", "Check the job: subject, object or possessive."],
            "A pronoun must agree with its noun and fit its case.",
            "*The committee has published ___ report.* Options: their / its / theirs / it's.",
            ["*Committee* is one body here, so it is singular.", "A possessive before a noun is needed: *its*."],
            "its"),
    ],
)

# =====================================================================
# 3. Vocabulary fit
# =====================================================================
SUBS["cloze-vocab-fit"] = dict(
    concept=(
        "A vocabulary blank gives four options that are all grammatically correct. Only the meaning of the sentence can decide. "
        "Say the missing idea in plain words first. Then pick the option that names it, and check its tone and its fixed partners."
    ),
    notes=r"""### What a vocabulary blank tests
All four options fit the grammar. No rule can save you. Only the meaning of the sentence can.

> **Rule:** Say the missing idea in plain words first. Then find the option that names it.

Take this sentence. *Its benefits depend almost entirely on ___; twenty minutes on Sunday cannot undo six days of sitting.* The missing idea is doing it again and again. The answer is **regularity**.

### Where the clue sits
The clue is usually in the same sentence. Sometimes it is in the next one.

- Same sentence: the part after the semicolon above explains the answer.
- Next sentence: *The traders did not take the plan lying down. They collected signatures.* The second sentence shows that the first blank needs a word about resistance.

### Meaning, tone and register
Check three things, in this order.

1. **Meaning.** The word must make the sentence true to the passage.
2. **Tone.** Decide whether the sentence praises or blames. The word must carry the same feeling. *Doctors praised the ___ results* needs a positive word, so *remarkable* fits and *dreadful* does not.
3. **Register.** Cloze passages use neutral, slightly formal prose. Between two words of equal meaning, the neutral word wins. *Children* beats *kids*. *Begin* beats *kick off*.

> **Watch:** A word with perfect grammar and the wrong tone is a classic trap.

### Fixed pairs decide many blanks
Some words travel together so firmly that the pair is one unit.

| Verb | Common partners |
|---|---|
| take | advantage, pride, a decision |
| make | room, a mistake, progress |
| pay | attention, a fine, a visit |
| keep / break | a promise, records / a rule |

If the blank is half of such a pair, the pair decides. The other options fail at once. Correct: She **took** full advantage of the offer. Wrong: *She did full advantage of the offer.*

### Near-synonyms are not equal
Options are often close, such as *quality, standard, character, grade*. Test each against the exact noun in the sentence. The sentence *the quiet here has a different ___* wants **quality**. Quiet has a quality, not a standard or a grade.

### Elimination for vocabulary blanks
1. Mark each option: + (fits), - (wrong meaning), ? (possible).
2. Keep the + options. A ? option needs a clear clue, not hope.
3. If two options survive, plug both into the whole passage. The passage usually rejects one.

> **Example:** *The corporation has sanctioned two more fans, and the students (1) ___ full advantage of the extended hours.* Options: make / do / take / give. The pair is *take advantage of*. Answer: take. *Do* and *make* are the classic traps here.
""",
    tricks=[
        {"title": "Name the missing idea",
         "body": "Before you look at the options, say what the sentence lacks, for example: it needs the idea of consistency. Then choose the option that says it.",
         "example": {"q": "*Its benefits depend almost entirely on ___; twenty minutes on Sunday cannot undo six days of sitting.*",
                     "steps": ["The second part says one long walk cannot make up for daily sitting.", "The missing idea is doing it regularly."],
                     "answer": "regularity"}},
        {"title": "Fixed pairs to bank",
         "body": "Learn common pairs: gain momentum, pay attention, take measures, reach a decision, bear fruit, meet a deadline, break the news, strike a balance. Cloze verbs and nouns often come from such pairs."},
        {"title": "Polarity check",
         "body": "Mark the sentence + or - before you choose. A praising sentence rejects negative words, even when they are grammatically perfect."},
    ],
    mistakes=[
        mis("Choosing a word that fits the topic of the passage but not the meaning of the sentence.", "Match the idea missing in this sentence, not the general topic."),
        mis("Ignoring fixed pairs and picking a near-synonym.", "If the blank is half of a pair, take the usual partner: *pay attention*, not *give attention*."),
        mis("Picking a big dictionary word when the passage is written in simple language.", "Choose the neutral word that matches the passage's level."),
        mis("Reading only the blank sentence.", "The clue may sit in the next sentence. Read one line further."),
        mis("Choosing a word with the wrong feeling.", "Mark the sentence as praise or blame first. Then match the word."),
    ],
    revision=[
        "Vocabulary blanks are decided by meaning, tone and fixed pairs, not by grammar.",
        "Say the missing idea in plain words before you read the options.",
        "The clue is usually in the same sentence. Read the next one too.",
        "Learn pairs: take advantage, make room, pay attention, keep a promise.",
        "Match the sentence's feeling: a praise word in a praising line.",
        "Near-synonyms: test each against the exact noun in the sentence.",
        "If two options survive, plug both into the whole passage.",
    ],
    patterns=[
        pat("clv1", "Noun choice by context", "very common",
            "The blank is a noun. The rest of the sentence describes what the noun means.",
            ["Read the part of the sentence that explains the blank.", "Say the missing idea in plain words.", "Choose the noun that names that idea."],
            "Explanations next to the blank point to the word.",
            "*Its benefits depend almost entirely on ___; twenty minutes on Sunday cannot undo six days of sitting.* Options: regularity / equipment / luck / medicine.",
            ["One Sunday walk cannot undo six days of sitting.", "So benefits need daily effort, which means regularity."],
            "regularity"),
        pat("clv2", "Verb choice by context", "very common",
            "The blank is a verb. The sentence tells you the result or the direction of the action.",
            ["Find the subject and the object.", "Decide what the subject does to the object.", "Choose the verb with that meaning."],
            "The subject and the object show what the action must be.",
            "*Heavy traffic ___ movement in the city.* Options: hinders / helps / invites / rewards.",
            ["Heavy traffic slows people down.", "*Hinders* means makes movement harder."],
            "hinders"),
        pat("clv3", "Adjective choice by tone and contrast", "common",
            "The sentence has a word such as but, yet or although. The blank must have the tone the sentence needs.",
            ["Mark the first part + or -.", "If a contrast word follows, the blank has the opposite sign.", "Choose the adjective with that tone."],
            "A contrast word flips the tone, and the blank must follow it.",
            "*The room was small, but the view from its window was ___.* Options: magnificent / dull / cramped / ordinary.",
            ["*Small* is a weak point (-).", "*But* flips the tone, so the blank is positive.", "*Magnificent* is the only positive option."],
            "magnificent"),
        pat("clv4", "Collocation blank (verb + fixed noun)", "common",
            "The blank is a verb before a noun such as advantage, attention or progress.",
            ["Look at the noun after the blank.", "Recall its usual verb.", "Reject the near-synonyms."],
            "A fixed pair decides at once. The other options fail even if they sound sensible.",
            "*Students should ___ full advantage of the library.* Options: make / do / take / give.",
            ["The noun is *advantage*.", "English says *take advantage of*."],
            "take"),
        pat("clv5", "Tone check: praise or blame", "very common",
            "The sentence praises or criticises something. The options mix positive and negative words.",
            ["Decide whether the sentence praises or blames.", "Cross out options with the opposite feeling.", "Pick the best of the rest."],
            "A word with the wrong feeling is wrong even when its meaning is close.",
            "*Doctors praised the ___ results of the trial.* Options: remarkable / dreadful / doubtful / regrettable.",
            ["*Praised* makes the sentence positive.", "Only *remarkable* is positive."],
            "remarkable"),
        pat("clv6", "Near-synonym blank", "occasional",
            "Two or three options mean almost the same. They differ in how they pair with the noun.",
            ["Take the exact noun in the sentence.", "Test each option with that noun.", "Keep the one that is natural."],
            "Close words are not interchangeable. The noun decides.",
            "*The quiet in this lane has a special ___.* Options: quality / standard / grade / degree.",
            ["The noun *quiet* has a *quality*.", "A standard or a grade does not describe quiet."],
            "quality"),
    ],
)

# =====================================================================
# 4. Connector logic
# =====================================================================
SUBS["cloze-connector-logic"] = dict(
    concept=(
        "A connector blank is a logic question. The connector must name the exact link between the clause before it and the clause after it. "
        "Decide the direction first: opposite, cause, result, addition or time. Then choose the word."
    ),
    notes=r"""### What a connector blank tests
A connector joins two clauses. Your job is to find the **direction** between them. The connector is logic written as one word.

> **Rule:** Split the sentence at the blank. Ask how clause B behaves toward clause A.

### Step 1: find the two clauses
Give each side a sign. Use + for a good point and - for a bad point.

- *The walk costs nothing (+), ___ very few continue it (-).* The signs are opposite, so this is contrast.
- *It rained heavily, ___ the match was cancelled.* B is the outcome of A, so this is result.
- *Prices rose, ___ wages stayed flat.* B adds a parallel point, so this is addition.
- *She finished her homework, ___ the lights went out.* One event follows the other, so this is time.

### Step 2: pick the family, then the word
| Relation | Connectors | Mini-test |
|---|---|---|
| Contrast | but, yet, however, although, whereas, still, while | The clauses pull in opposite directions |
| Cause | because, since, as, for | B explains why A is true |
| Result | so, therefore, hence, thus, consequently | B is the outcome of A |
| Addition | moreover, besides, also, and, furthermore | B adds a parallel point |
| Condition | if, unless, provided | One clause depends on the other |
| Time | when, while, before, after, until | One clause fixes when the other happens |

> **Tip:** The most common exam item is praise followed by a limit. *The walk costs nothing and needs no equipment, ___ very few people continue it.* The blank needs *yet* or *but*.

### Step 3: use the punctuation clue
- After a full stop or a semicolon, a linking word plus a comma is used: **however, moreover, therefore, otherwise**. Example: *Business has not suffered; **moreover**, some customers order a second cup.*
- A single comma joining two clauses takes **but, yet, so, for, and**.
- A blank at the start of a second sentence often looks back at the whole first sentence.

### Pairs and confusions
Some connectors come in pairs: *not only ... but also*, *either ... or*, *neither ... nor*, *both ... and*, *no sooner ... than*, *hardly ... when*, *lest ... should*. If you see one half outside the blank, only its partner fits.

- **but or so:** *The shop is small, ___ it is always full.* Use *but*. *The road was cleared, ___ traffic flowed again.* Use *so*.
- **because or although:** *___ it rained, the match went on.* Use *Although*, because the result is surprising. *___ it rained, the match was cancelled.* Use *Because*.
- **while** has two meanings: time (*read while the tea cools*) and contrast (*cities grew rich, while villages lagged*).
- **until** shows an action running up to a point: *He waited until morning.*

> **Watch:** *However* and *therefore* need commas around them. *Yet, but* and *so* join clauses directly after a comma.
""",
    tricks=[
        {"title": "Opposite-direction test",
         "body": "Give each clause a + or - sign. Same signs point to addition or result. Opposite signs point to contrast.",
         "example": {"q": "*The walk costs nothing and demands no equipment (+), ___ very few people continue it (-).*",
                     "steps": ["The signs are + then -.", "Opposite signs need a contrast word."],
                     "answer": "yet / but"}},
        {"title": "Partner hunt",
         "body": "Scan the sentence for the other half of a pair. If you see *not only*, the blank must be *but also*. No further thinking is needed."},
        {"title": "Comma tell",
         "body": "A pattern like *clause, ___ clause* with a one-word slot wants yet, but, so, for or and. Options like however and therefore fit the pattern *clause. ___, clause* instead."},
    ],
    mistakes=[
        mis("Mixing up result (*so*) and cause (*because*).", "Ask which clause explains which. The reason follows *because*. The outcome follows *so*."),
        mis("Using *although* where a plain *but* is needed.", "*Although* starts a subordinate clause. It cannot join two full clauses as *but* does."),
        mis("Choosing a connector that fits the sentence but reverses the paragraph's argument.", "Check the choice against the flow of the whole passage."),
        mis("Marking *and* as always safe.", "In a contrast context, *and* destroys the writer's point."),
    ],
    revision=[
        "A connector shows the direction between two clauses. Find both clauses first.",
        "Contrast: but, yet, however, although, whereas.",
        "Result: so, therefore, hence. Reason: because, since, as.",
        "Addition: moreover, besides. Time: when, while, until, before.",
        "Full stop or semicolon + comma: however, moreover, therefore, otherwise.",
        "because = normal result. although = surprising result.",
        "Read the full joined sentence aloud to test your choice.",
    ],
    patterns=[
        pat("clc1", "Contrast connector (but, yet, although, whereas)", "very common",
            "One clause is good and the other is bad, or one is expected and the other is surprising.",
            ["Give each clause a + or - sign.", "If the signs are opposite, choose a contrast word.", "Check that the word fits the punctuation."],
            "Opposite signs mean the second clause pulls against the first.",
            "*The walk costs nothing, ___ very few people continue it.* Options: yet / so / because / and.",
            ["The first clause is good (+).", "The second is a limit (-).", "Only *yet* shows contrast."],
            "yet"),
        pat("clc2", "Reason connector (because, since, as)", "very common",
            "The second clause explains why the first clause is true.",
            ["Ask: does one clause explain the other?", "The explaining clause follows *because*.", "Read both clauses with your choice."],
            "A reason connector links an event to its cause.",
            "*The match was cancelled ___ it rained heavily.* Options: because / although / but / so.",
            ["Rain is the reason for the cancellation.", "*Because* introduces the reason."],
            "because"),
        pat("clc3", "Addition connector (moreover, furthermore, besides)", "common",
            "The second sentence adds one more point in the same direction.",
            ["Check that both clauses have the same sign.", "Pick an addition word.", "Use the punctuation: semicolon, word, comma."],
            "The writer is building up one point, not turning against it.",
            "*Business has not suffered; ___, some customers now order a second cup.* Options: moreover / otherwise / unless / until.",
            ["Both parts are good news.", "The second adds to the first.", "*Moreover* adds a point."],
            "moreover"),
        pat("clc4", "Time connector (while, until, before, after, when)", "common",
            "One clause tells when or for how long the other happens.",
            ["Find the two events.", "Decide their order: before, after, together or up to a point.", "Choose the time word for that order."],
            "Time words place two events on one timeline.",
            "*Please wait here ___ the doctor arrives.* Options: until / unless / although / because.",
            ["Waiting continues up to the doctor's arrival.", "*Until* shows this."],
            "until"),
        pat("clc5", "Result connector (so, therefore, hence)", "common",
            "The second clause is the outcome of the first.",
            ["Ask: did the first clause cause the second?", "Choose *so* or *therefore*.", "Check the punctuation."],
            "A result connector shows what followed from a cause.",
            "*The road was cleared, ___ traffic flowed again.* Options: so / but / because / although.",
            ["Clearing the road caused the flow.", "The second clause is the result."],
            "so"),
        pat("clc6", "Pair connector (not only ... but also)", "occasional",
            "One half of a pair, such as not only, either or neither, is outside the blank.",
            ["Spot the half that is already there.", "Recall its partner.", "Choose it."],
            "Correlative pairs always come as a set.",
            "*He is not only honest ___ also hardworking.* Options: but / and / or / nor.",
            ["*Not only* is already in the sentence.", "Its partner is *but also*."],
            "but"),
        pat("clc7", "Linking word after a full stop", "common",
            "The blank starts a new sentence and a comma follows it.",
            ["Read the sentence before the blank.", "Decide how the new sentence relates to it.", "Choose the linking adverb."],
            "Sentence-starting connectors look back at the whole earlier sentence.",
            "*The plan looked perfect. ___, it failed on the first day.* Options: However / Because / So / Unless.",
            ["The plan looked good.", "It failed, which is the opposite.", "*However* shows contrast."],
            "However"),
    ],
)

# =====================================================================
# 5. Prepositions and phrasal verbs
# =====================================================================
SUBS["cloze-prepositions-phrasals"] = dict(
    concept=(
        "Preposition blanks are about fixed pairs. The word before or after the blank decides the answer. "
        "Phrasal verbs are a verb plus a small word, and the small word changes the meaning. "
        "Find the governing word, recall its partner, and never translate from your own language."
    ),
    notes=r"""### Preposition blanks
English fixes a preposition to many verbs, adjectives and nouns. Logic rarely helps, because the pair is a convention.

> **Rule:** Find the word that governs the blank. Then recall its fixed partner.

- depend **on**, insist **on**, congratulate **on**
- afraid **of**, fond **of**, aware **of**
- good **at**, angry **with** (a person) or **at** (a thing), married **to**
- reason **for**, solution **to**, influence **on**, rise **in**

### Fixed pairs to learn
| Governing word | Correct pair | Wrong pair to avoid |
|---|---|---|
| ashamed | ashamed **of** | ashamed for |
| respond | respond **to** | respond on |
| apply (an organisation) | apply **to** a bank | apply on |
| apply (a post) | apply **for** a post | apply to a post |
| depend | depend **on** | depend from |
| prevent | prevent **from** + -ing | prevent to |
| insist | insist **on** + -ing | insist to |
| smell | smell **of** garlic | smell with |
| arrive | arrive **at** a place, **in** a city | arrive to |
| married | married **to** | married with |
| according | according **to** records | according with |
| in spite | in spite **of** | in spite from |

*Different from* is the standard form in formal writing.

### Time and place words
- **at** a clock time or a point: at 6 p.m., at noon, at night, at the gate.
- **on** a day or a date: on Sunday, on 15 August. Also a surface: on the table.
- **in** a long period or an enclosed space: in June, in 2019, in the morning, in the room, in India.
- *Since* gives a point in time (since 2020). *For* gives a length (for five years).

> **Watch:** It is *in 2024* but *on 15 August 2024*.

### Phrasal verbs: the particle is the meaning
A phrasal verb is a verb plus a particle. The particle changes the meaning.

| Phrasal verb | Meaning |
|---|---|
| look after / look into | take care of / investigate |
| look down upon / look up to | despise / admire |
| put off / put up with | postpone / tolerate |
| call off / turn down | cancel / reject |
| set up / set out | establish / begin a journey |
| carry out / carry on | perform / continue |
| give way to | yield, be replaced by |
| break out / come across | begin suddenly / meet by chance |

The particle also carries a direction. *Up* often means completing. *Off* suggests cancelling or leaving. *Out* suggests eruption or giving out. *Down* suggests rejecting or writing.

### Method for these blanks
1. Read the word before the blank and the phrase after it.
2. If a fixed pair exists, the pair decides.
3. For a phrasal verb, say the needed meaning first. Then match the particle.
4. For time and place, classify the noun: point, day or period.

> **Tip:** Replace the phrasal verb with one simple verb in your head. *Look after* becomes *tend*. If the meaning breaks, the option is wrong.
""",
    tricks=[
        {"title": "Governor chant",
         "body": "Underline the word that governs the blank and say its partner: depend on, afraid of, good at, solution to. About ten pairs cover most exam prepositions.",
         "example": {"q": "*Residents are paid a small sum to ___ the trees outside their homes.* Options: look after / look into / look down upon / look up to.",
                     "steps": ["Paying someone to care for trees.", "*Look after* means take care of.", "*Look into* means investigate."],
                     "answer": "look after"}},
        {"title": "Particle direction sense",
         "body": "Ask what the sentence does to the object. Does it cancel it (call off), reject it (turn down) or build it (set up)? The particle shows the direction of the action."},
        {"title": "Substitute the simple verb",
         "body": "Replace the phrasal verb with a one-word verb in your head. The sentence must keep its meaning. If it does not, that option is wrong."},
    ],
    mistakes=[
        mis("Choosing a preposition by feel, or from your mother tongue.", "Find the English governing word and recall its fixed partner."),
        mis("Breaking a phrasal verb: *give way* without *to* when the sentence needs *give way to*.", "Treat verb + particle as one unit and check what follows."),
        mis("Mixing *between* and *among*.", "Use *between* for two items. Use *among* for a group."),
        mis("Writing *on* for a year or *in* for a date.", "It is *in 2024* but *on 15 August 2024*."),
        mis("Accepting a phrasal verb only because it contains a familiar verb.", "State the needed meaning first. Then choose the particle."),
    ],
    revision=[
        "Fixed pairs decide: ashamed of, respond to, depend on, married to, according to, in spite of.",
        "apply to an organisation. apply for a post.",
        "at a point, on a day, in a period or an enclosure.",
        "For a phrasal verb, decide the meaning first, then the particle.",
        "look after (care for) is not look into (investigate).",
        "Two items take between. A group takes among.",
        "Never translate a preposition from your mother tongue.",
    ],
    patterns=[
        pat("clp1", "Preposition after a verb or adjective (fixed pair)", "very common",
            "The blank comes right after a verb or adjective such as fond, depend, afraid or good.",
            ["Find the word before the blank.", "Recall its fixed partner.", "Choose that preposition."],
            "The pair is a convention, so meaning does not help.",
            "*She is fond ___ classical music.* Options: of / at / with / to.",
            ["The governing word is *fond*.", "The fixed pair is *fond of*."],
            "of"),
        pat("clp2", "Preposition of time or place", "very common",
            "The blank comes before a time or a place word.",
            ["Classify the noun: clock point, day or date, long period, enclosed place.", "Match: at, on, in.", "Check the options."],
            "Each type of noun has its own preposition.",
            "*The class starts ___ 9 a.m.* Options: at / on / in / by.",
            ["*9 a.m.* is a clock point.", "A clock point takes *at*."],
            "at"),
        pat("clp3", "Phrasal verb blank", "very common",
            "The blank is a verb plus a particle. Several options share the same verb.",
            ["Say in plain words what the sentence needs.", "Match that meaning with one option.", "Reject options that share only the verb."],
            "The particle changes the meaning of the verb.",
            "*Residents are paid a small sum to ___ the trees outside their homes.* Options: look after / look into / look down upon / look up to.",
            ["The sentence needs the idea of taking care.", "*Look after* means take care of."],
            "look after"),
        pat("clp4", "Preposition inside a fixed phrase", "common",
            "The blank is inside a set phrase such as in spite of or according to.",
            ["Spot the fixed phrase.", "Recall the exact wording.", "Choose the missing word."],
            "Fixed phrases never change their small words.",
            "*They played in spite ___ the rain.* Options: of / from / with / to.",
            ["The blank sits inside a set phrase.", "The fixed phrase is *in spite of*."],
            "of"),
        pat("clp5", "Preposition before -ing (prevent from, insist on)", "common",
            "The blank sits before a verb ending in -ing, after a word like prevent, insist or good.",
            ["Find the governing verb or adjective.", "Recall its preposition.", "Keep -ing after the preposition."],
            "A preposition is followed by -ing, and the governing word fixes the preposition.",
            "*The guard prevented him ___ entering the hall.* Options: from / to / of / for.",
            ["The pair is *prevent ... from*.", "*Entering* is the -ing form after it."],
            "from"),
        pat("clp6", "Apply to or apply for", "occasional",
            "The blank follows apply. The options are to and for.",
            ["Ask: is the next word an organisation or a post?", "An organisation takes *to*.", "A post takes *for*."],
            "The same verb takes different prepositions with different nouns.",
            "*She applied ___ the post of clerk.* Options: for / to / on / at.",
            ["The next word is a post.", "A post takes *for*."],
            "for"),
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
