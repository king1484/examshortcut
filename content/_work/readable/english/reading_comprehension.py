"""Readable rewrite of English > Reading Comprehension (all 6 subtopics).

Plain English, short sentences, tables for signal words and option types, one method per question type.
Every fact from the old notes is kept; new pattern ids continue the topic numbering (rc-p26 onward).
Run: python reading_comprehension.py  (patches content/core/topics/english/reading-comprehension.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "reading-comprehension.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Reading strategy
# =====================================================================
SUBS["rc-reading-strategy"] = dict(
    concept=(
        "A reading passage in an SSC paper has 250 to 350 words and 5 questions. You get about 6 to 8 minutes for the whole set. "
        "Speed comes from a fixed routine, not from reading faster. "
        "Read the passage once, read the questions, then go back to the exact lines. Every answer must be written in the passage."
    ),
    notes=r"""### What a reading comprehension question tests
*Comprehension* means understanding. You get a short passage and 4 to 6 questions on it. The exam does not test general knowledge. It tests one skill: can you find and understand what is written?

Every correct answer can be pointed to in the passage. Think of a train timetable. You do not learn it by heart. You know where things are, and you go back to the right line when someone asks.

### The three-step routine
1. **Read the passage once, calmly (about 2 minutes).** Do not try to remember facts. Notice what each paragraph does.
2. **Read the questions.** Read only the question lines at first. Do not study all the options yet.
3. **Go back to the exact lines** the question points to. Answer from those lines, then look at the options.

Read the passage first. Questions often say "the author" and "the passage". Most detail questions follow the order of the passage. One clean read lets you find things from memory.

### Paragraph mapping
After each paragraph, tell yourself its job in 3 to 5 words.

- Para 1: *problem, millets disappeared*
- Para 2: *why millets are useful now*
- Para 3: *what stops the revival*

> **Tip:** With this map, "What is the purpose of the second paragraph?" takes 5 seconds. Detail questions get quick too, because you know which paragraph to search.

### Signal words show the structure
| Signal words | What they tell you |
|---|---|
| however, yet, but, still | the author turns; the key point usually comes after |
| because, since, as, due to | a reason; "why" questions are answered here |
| so, therefore, thus, as a result | a result or a conclusion |
| for example, such as, consider | an example; it supports the point just before |
| first, then, finally | a sequence or a list |

### Question types you will meet
- **Main idea, title, purpose.** These are about the whole passage.
- **Detail.** "According to the passage..." The answer is written in one line.
- **Inference.** "It can be inferred..." The answer is one small step from a line.
- **Vocabulary in context.** The meaning of a word as used in the passage.
- **Tone and attitude.** How the author feels.
- **Structure questions.** These include statement combinations (I, II, III) and the purpose of a paragraph.
- **Author-move questions.** "Why does the author mention...", how the passage is organised, and "which question can be answered from the passage".

### Habits to drop
| Wrong habit | Why it fails | Do instead |
|---|---|---|
| Reading options before the passage | options plant false memories of facts | read the passage first |
| Re-reading a hard sentence again and again | it eats the clock | note the line, move on, return only if asked |
| Answering from outside knowledge | the paper marks what is written, not what is true | trace every answer to a line |
| Matching keywords only | options paraphrase, so keywords mislead | use a keyword to reach the line, then read the line |

### Order of solving and time plan
Do the quick, local questions first. Start with vocabulary, because it needs only one sentence. Then do detail, then inference. Leave main idea and tone for last. By then you understand the passage best.

> **Rule:** Time for a 5-question set: first read about 2 minutes, each question 20 to 45 seconds, final check about 30 seconds.

### Golden rules
- **Passage only.** An option that is true in real life but not in the passage is wrong.
- **Watch extreme words:** *always, never, only, all, completely*. Passages usually speak in a moderate way.
- **Same words do not mean the same meaning.** An option that copies passage words but changes their sense is a trap.
- **Mark and move.** If a question stays stuck for more than 40 seconds, mark it and come back.
""",
    tricks=[
        {"title": "Two-minute structure read",
         "body": "On the first read, do not hunt for facts. After each paragraph, say its job in three words. Facts are easy to find again. Structure is what saves time."},
        {"title": "Vocabulary first, main idea last",
         "body": "Answer the replace-the-word question and the line-specific details before the main-idea question. By then you have touched half the passage and the theme is clear.",
         "example": {"q": "A set has Q1 main idea, Q2 a detail from para 2, Q3 replace-the-word, Q4 inference, Q5 title. In what order do you attempt them?",
                     "steps": ["Q3 needs only one sentence, so it goes first.", "Q2 is a line-specific detail, so it comes next.", "Q4 inference follows, then the two theme questions Q1 and Q5."],
                     "answer": "Q3, Q2, Q4, Q1, Q5"}},
        {"title": "Line anchoring",
         "body": "Every detail question has a home line. Match a distinctive word from the question (a name, a number, an odd noun) to the passage. Read two lines around it. Choose the option that paraphrases those lines."},
    ],
    mistakes=[
        mis("Answering from general knowledge because the option sounds true in real life.", "Choose only what the passage says. Point to the line."),
        mis("Spending four minutes on the first read to understand everything.", "Use the first read only to map the passage. It should take about 2 minutes."),
        mis("Leaving reading comprehension for the last two minutes.", "The 5-question set is a high-value block. Give it a planned slot."),
        mis("Choosing an option because it copies words from the passage.", "Check that the meaning matches too. Copied words with a changed meaning are a trap."),
        mis("Studying all four options before reading the passage.", "Read the passage first, then only the question lines."),
    ],
    revision=[
        "Read the passage first, then the questions, then return to the lines.",
        "Map each paragraph in 3 to 5 words.",
        "However, yet, but: the key point follows.",
        "For statement-combination questions, judge each statement alone, then pick the matching option.",
        "For 'why does the author mention X', ask what point X supports, not what X is.",
        "Never use outside knowledge. Never pick an extreme option unless the passage uses extreme words.",
    ],
    patterns=[
        pat("rc-p1", "Statement combination (Which of statements I, II, III is true?)", "common",
            "The question lists two or three numbered statements. The options say 'Only I', 'Only I and III', 'All of these'.",
            ["Check statement I against the passage: True, False or Not stated.", "Do the same for II and III, one at a time.",
             "Count 'Not stated' as not true.", "Pick the option that matches your list exactly."],
            "Judging one short statement is easier than comparing four long options.",
            "Passage: \"The pond was dug in 2015. It fills during the monsoon and supplies water to forty families till March.\" Which is true? I. The pond fills in the monsoon. II. It supplies water all year. III. Forty families use it. (a) Only I (b) Only I and III (c) Only II and III (d) All of these",
            ["I is stated, so it is true.", "II says all year, but the water lasts only till March, so it is false.", "III is stated, so it is true."],
            "(b) Only I and III"),
        pat("rc-p2", "Purpose or role of a paragraph", "common",
            "'The second paragraph mainly...', 'What role does the last paragraph play?', 'The purpose of paragraph 3 is to...'.",
            ["Recall your paragraph map.", "Ask: does this paragraph give a problem, a cause, an example, a solution or a contrast?",
             "Choose the option that names that job for this paragraph, not for a neighbour."],
            "Wrong options usually describe another paragraph correctly.",
            "Para 1 says city buses are always late. Para 2 says roads are jammed by parked cars. Para 3 suggests paid parking. The second paragraph mainly: (a) describes the problem (b) explains the cause of the problem (c) offers a solution (d) praises bus drivers",
            ["Para 2 gives the reason buses are late: parked cars.", "Option (a) is the job of para 1.", "Option (c) is the job of para 3."],
            "(b) explains the cause of the problem"),
        pat("rc-p3", "Why does the author mention X? (function of an example)", "common",
            "'The author mentions ... in order to...', 'Why does the author refer to...?', 'The example of ... is given to show...'.",
            ["Find X in the passage.", "Read the sentence before X. It usually states the point X supports.",
             "Choose the option that names that point (to illustrate, to prove, to contrast), not a description of X."],
            "An example never stands alone. It supports a claim nearby.",
            "\"Small savings add up. A tea-seller who keeps aside Rs 20 a day has over Rs 7,000 at the end of a year.\" Why is the tea-seller mentioned?",
            ["The sentence before says small savings add up.", "The tea-seller shows how small daily savings become a large sum.", "He is not there to talk about tea or income."],
            "To illustrate that small daily savings grow into a large sum"),
        pat("rc-p4", "How is the passage organised? (structure)", "occasional",
            "'Which of the following best describes the organisation or structure of the passage?'",
            ["Write the paragraph map in order, for example past, present advantage, obstacle.", "Check every part of each option against your map, in the same order.",
             "Reject an option with even one wrong part."],
            "One wrong part, such as 'no solution is offered' when a solution is given, makes the whole option wrong.",
            "Para 1: a village had no doctor. Para 2: a mobile clinic started visiting weekly. Para 3: child illness fell sharply. Best description? (a) A problem, a response and its result (b) Two views compared (c) A theory rejected (d) A list of causes",
            ["Map: problem, response (the clinic), result (less illness).", "Only (a) follows this order."],
            "(a) A problem, a response and its result"),
        pat("rc-p5", "Which question can be answered from the passage?", "occasional",
            "'The passage answers which of the following questions?', 'Which question can be answered using the information in the passage?'",
            ["For each option, look for the exact information needed: a number, a name, a reason.", "If the passage gives only part of it, or nothing, reject the option.",
             "Prefer a why or how question whose answer is clearly written."],
            "Setters add options that ask for numbers, years or names that the passage never gives.",
            "Passage: \"The school started a kitchen garden so that children could eat fresh vegetables at lunch.\" Which question is answered? (a) How big is the garden? (b) Why did the school start a kitchen garden? (c) Who planted the first seed? (d) When was the school built?",
            ["The passage gives one thing: the reason.", "Size, planter and date are never mentioned."],
            "(b) Why did the school start a kitchen garden?"),
        pat("rc-p26", "Turning-point question (what comes after 'however'?)", "occasional",
            "'What does the author say in contrast to...?', 'The author's real view is...', a sentence with however, yet or but.",
            ["Find the signal word: however, yet, but.", "The part before it is the view being set aside.", "The part after it is the author's own point. Match the option to that part."],
            "The author puts the important point after the turn.",
            "\"Many people think the old bridge should be pulled down. However, engineers found it strong enough to serve for fifty more years.\" What is the author's view?",
            ["'Many people think' is the view being set aside.", "The point after 'however' is that the bridge is still strong."],
            "The old bridge is strong and can be kept in use"),
    ],
)

# =====================================================================
# 2. Main idea
# =====================================================================
SUBS["rc-main-idea"] = dict(
    concept=(
        "The main idea is the one big point the whole passage makes. The author keeps coming back to it. "
        "A title is the main idea squeezed into a short heading. The purpose is why the author wrote the passage. "
        "Check every option for three faults: too narrow, too broad and too extreme."
    ),
    notes=r"""### What the main idea is
The **main idea** (also called the *central idea* or *theme*) is the one big point the whole passage makes. Every paragraph helps to support it.

A **title** is the main idea squeezed into a short heading. The **purpose** is why the author wrote the passage: to inform, to argue, to warn or to encourage.

Take a friend who talks for five minutes about late trains, crowded coaches and dirty platforms. The main idea is not "trains are late". It is "the railway service in our town is poor". Each complaint supports that one point.

### Where to find it
- The **first paragraph** usually introduces the topic or the problem. The main idea often sits in its first or last sentence.
- The **last paragraph** usually gives the conclusion or a suggestion, and often repeats the main idea.
- **Middle paragraphs** give reasons, examples, data and objections. They are rarely the theme.

> **Rule:** Main idea = topic (from the start) + the author's point about it (often at the end).

### Three tests for the right option
1. **It covers the whole passage.** An option about one paragraph or one example is too narrow.
2. **It stays inside the passage.** An option that adds ideas the passage never argues is too broad.
3. **It matches the author's strength.** An option with *always, only, never* is too extreme when the author is moderate.

### Worked example
Passage: *"Many old stepwells lie full of garbage. Yet a few towns that cleaned them found they still collect rainwater and raise groundwater. Reviving them costs little."*

- "Stepwells are full of garbage." Too narrow. It covers only the first line.
- "India faces a water crisis." Too broad. The passage talks only about stepwells.
- "Only stepwells can solve water shortage." Too extreme.
- "Cleaning old stepwells is a cheap way to improve water supply." Correct. It covers every line.

### Option types and how to remove them
| Option type | What it looks like | How to remove it |
|---|---|---|
| Out of scope | true in real life, never said | ask where it is stated |
| Too extreme | uses *always, never, only, must, completely* | passages argue in a moderate way |
| Reversal | says the opposite of a stated line | re-read the line it is built on |
| Too narrow or too broad | one example, or ideas beyond the passage | it must cover the whole passage |
| Verbatim bait | copies a phrase but changes its use | theme options paraphrase, they rarely quote |

### Title questions
A good title is short and covers the whole passage. It often shows both sides when the passage has both. Titles with a colon, such as "Gig Work: Freedom with a Price", are often right because they hold two halves of the idea.

> **Watch:** A catchy title that names only the first example is wrong. If the passage opens with a farmer's story but is really about water policy, "A Farmer's Story" is too narrow.

Titles are noun phrases, like "The quiet comeback of the public library". Do not reject a title for having no verb. Reject it for the wrong scope.

### Purpose questions
Look at the verbs the author uses.

| The author mainly... | Purpose word |
|---|---|
| gives facts, explains how something works | to inform, to explain |
| gives reasons for one side, says should or must | to argue, to persuade |
| points out a danger | to warn |
| praises something and asks readers to do it | to encourage |
| points out faults | to criticise |

A neutral explanation is never "to criticise" or "to persuade", even if the topic is serious.

### Method for a whole passage or one paragraph
1. Before you look at the options, say the main idea in about ten words.
2. Remove options that are too narrow, too broad or too extreme.
3. Between two options that remain, pick the one that includes the author's conclusion.

For one paragraph, use the same tests on that paragraph only. Its first sentence, the *topic sentence*, usually states the point.
""",
    tricks=[
        {"title": "First and last sentence sketch",
         "body": "Read the opening and closing sentences of the passage, plus the first sentence of each middle paragraph. This skeleton usually states or implies the theme. Build your ten-word summary from it before you read the options.",
         "example": {"q": "Opening: 'Critics announced the death of the public library. The prediction has aged badly.' Closing: 'Libraries are one of the few public institutions succeeding in both worlds.' What is the theme?",
                     "steps": ["The opening says libraries were written off.", "It adds that this prediction was wrong.", "The closing praises libraries for doing well."],
                     "answer": "Libraries remain vital public institutions, not relics"}},
        {"title": "Count the mentions",
         "body": "The idea the author repeats in different words across paragraphs is the theme. If an option's core idea appears in only one paragraph, it is a detail, not the theme."},
        {"title": "Title versus theme wording",
         "body": "Titles are noun phrases. Theme options are full claims. Judge both by scope, not by grammar."},
    ],
    mistakes=[
        mis("Picking a title that names only the first paragraph's example.", "Pick the title that covers the whole passage."),
        mis("Choosing the broadest-sounding option.", "An option with no support in the passage is a trap, not a strength."),
        mis("Confusing the author's closing suggestion with the theme.", "A suggestion supports the idea. It is not the whole idea."),
        mis("Selecting an option because its words appear in the passage.", "Theme options paraphrase. Check the meaning, not the words."),
    ],
    revision=[
        "Main idea = topic + the author's point about it.",
        "Check the first and last paragraphs first.",
        "Three killers: too narrow, too broad, too extreme.",
        "A title is the whole passage in a few words. Colon titles often fit two-sided passages.",
        "Purpose = why it was written: inform, argue, warn, encourage, criticise.",
        "Make your own summary before you read the options.",
    ],
    patterns=[
        pat("rc-p6", "Central idea or main theme of the passage", "very common",
            "'The central idea or main theme of the passage is...', 'The passage is primarily concerned with...', 'Which option sums up the passage?'",
            ["Say the topic (from para 1) and the author's point (usually in the last para) in one line.", "Remove options that cover only one paragraph.",
             "Remove options about a bigger subject than the passage.", "Remove options with only, always or never that the author did not use."],
            "The main idea must be supported by every paragraph, so partial or inflated options fail.",
            "\"Many families now buy bottled water. Yet a simple home filter gives safe water at a tenth of the cost, and it creates no plastic waste.\" The central idea is: (a) Bottled water is unsafe (b) Home filters are a cheaper, cleaner alternative to bottled water (c) Plastic waste is rising in India (d) All families should stop drinking tap water",
            ["Topic: bottled water. Author's point: a home filter is cheaper and makes no plastic.", "(a) is never said.", "(c) is too broad. (d) is extreme and unrelated."],
            "(b)"),
        pat("rc-p7", "Most suitable title", "very common",
            "'Which of the following is the most appropriate or suitable title for the passage?'",
            ["Build your ten-word summary first.", "Reject titles that name only an example from one paragraph.",
             "Reject dramatic titles that go past the author, such as 'The End of...' or 'The Only Way...'.", "Prefer the title that covers both the problem and the answer if the passage has both."],
            "A title must cover the whole passage, no more and no less.",
            "A passage describes how a village built check dams, how its wells refilled and how farmers now grow two crops. Best title? (a) Check Dams Bring a Village Back to Life (b) How to Build a Wall (c) Farming in India (d) The Monsoon Always Fails",
            ["(b) misses the effect.", "(c) is too broad.", "(d) is extreme and not discussed."],
            "(a)"),
        pat("rc-p8", "Author's primary purpose", "common",
            "'The author's main purpose is to...', 'The passage has been written mainly to...'.",
            ["Notice the author's verbs: explains (inform), should or must (argue), danger or risk (warn), praises and asks readers (encourage).",
             "Match the purpose to the whole passage, not to one sentence.", "Reject purposes that are too strong, such as demand or prove, if the author only suggests."],
            "The purpose is the reason for the whole passage, and the verbs give it away.",
            "\"Fifteen minutes of reading to a child each evening builds vocabulary. It needs no costly books; a folk tale works as well. Busy parents can surely spare this time.\" The author's purpose is to: (a) criticise schools (b) encourage parents to read or tell stories to children daily (c) sell children's books (d) compare folk tales",
            ["The author explains a benefit.", "Then the author urges parents: 'can surely spare this time'.", "That is encouragement."],
            "(b)"),
        pat("rc-p9", "Main point of one paragraph or best summary", "common",
            "'The second paragraph is mainly about...', 'What is the main point of the last paragraph?', 'Which option best summarises...'",
            ["Read the first sentence of that paragraph, the topic sentence.", "Check that the option fits every sentence in that paragraph.", "Reject options that describe another paragraph."],
            "A paragraph has one point, and all its sentences support it.",
            "Para 2: \"Discarded phones add to e-waste. Workers burn wires to get copper and breathe the fumes. New phones need fresh metals and energy.\" Para 2 is mainly about: (a) new phone features (b) the hidden costs of throwing gadgets away (c) the price of copper (d) government rules on repair",
            ["Sentence 1 names waste, sentence 2 names fumes, sentence 3 names fresh resources.", "Each one is a cost of discarding."],
            "(b)"),
        pat("rc-p27", "What would the author discuss next?", "occasional",
            "'The paragraph that follows most likely deals with...', 'What is the author likely to write about next?'",
            ["Find the last paragraph's job: problem, cause, or one solution among several.", "Ask what a reader would want to know next.",
             "Choose the option that continues the same line of thought, not a new topic."],
            "Passages move in steps. The next step follows from the last line.",
            "The last paragraph says: \"Rainwater tanks are one way to save water at home. Another way is to fix leaking taps.\" What comes next? (a) Other simple ways to save water at home (b) A history of taps (c) The cost of buying a car (d) Why rain falls",
            ["The passage is listing ways to save water.", "The list has just begun, so more ways should follow."],
            "(a)"),
    ],
)

# =====================================================================
# 3. Detail
# =====================================================================
SUBS["rc-detail-fact"] = dict(
    concept=(
        "Detail questions ask what the passage says, line by line. The answer is written in the passage. "
        "The options paraphrase it, and the wrong options are built around it. "
        "Use the method: locate a keyword, read around it, say the answer in your own words, then match."
    ),
    notes=r"""### What a detail question is
A detail (or *factual*) question asks about something written directly in the passage. It can be a fact, a reason, a number, a name or a feature. The stem often begins *"According to the passage..."* or *"The passage states that..."*.

These are the easiest marks in reading comprehension. But you must go back and read the line. Memory is not enough, because the options are built to almost match the passage.

### The four-step method
1. **Locate.** Pick a keyword from the question: a name, a number or an unusual word (*stepwell, fat content, ten days*). Find it in the passage.
2. **Read around.** Read that sentence, plus one before and one after. The answer often sits in the next sentence.
3. **Say it.** Put the answer in your own words before you look at the options.
4. **Match.** Choose the option with the same meaning as your words. Options usually paraphrase.

> **Tip:** Cover the options after you locate the line. Answer aloud in your own words, then uncover. This one habit defeats most engineered wrong options.

### How wrong options are made
Suppose the passage says "Most varieties need little water".

| Trap | Example option |
|---|---|
| **Reversal** (opposite meaning) | "Millets need a lot of water" |
| **Extreme** (changes *most* to *all*) | "All millets need no water at all" |
| **Not stated** (sounds true, never said) | "Millets are grown mainly in Punjab" |
| **Wrong part** (a true detail from another paragraph) | a reason given for a different fact |

### Watch the small words
Qualifiers are words like *some, many, most, all, often, always, may, will, more, less, only*. One changed qualifier makes an option wrong.

- Passage: "Rich merchants and queens paid for **the finest** of them."
- Option: "**All** stepwells were paid for by queens."
- This option is wrong twice: *all* is too strong, and *only queens* is not stated.

### Reason questions
A "Why...?" question is answered after words like **because, since, as, so that, due to, the reason is**. The clause after these words is the answer.

- Passage: "Less milk turned sour **because** it was cooled at once."
- Question: Why did less milk turn sour?
- Answer: It was cooled immediately.

### NOT and EXCEPT questions
The stem says "Which of the following is NOT mentioned..." or "...all of the following EXCEPT".

1. Circle NOT or EXCEPT so you do not forget it.
2. Tick each option you can find in the passage.
3. The one you cannot find, or that the passage contradicts, is the answer.

> **Watch:** Three options usually come from the same sentence or list. Find that list and the question is quick.

### Numbers and comparisons
Check every number in an option. Take the passage: "twelve households... over two hundred within four years".

A common trap swaps the *before* and *after* figures. Another trap drops a word like *particularly*. If the passage says night-time heat is *particularly* dangerous, an option saying "day-time heat is the real danger" is reversed.
""",
    tricks=[
        {"title": "Paraphrase before you look",
         "body": "After you locate the line, cover the options and answer in your own words. Then uncover and match.",
         "example": {"q": "'Why is night-time heat more dangerous than day heat?' (from a passage on heat islands)",
                     "steps": ["Your own words: the body repairs itself during sleep, so hot nights harm health.", "Now match. Any option about air conditioners or daytime labour is off the line."],
                     "answer": "Hot nights stop the body from recovering during sleep"}},
        {"title": "Reversal scan",
         "body": "Before you mark a detail option, check its direction words: only, always, all, may, often, some, can, cannot. Wrong options flip these while keeping the same topic words."},
        {"title": "Option pairing",
         "body": "When two options say the same thing in different words, both are wrong. A fact has one meaning. Remove the pair, then judge the other two."},
    ],
    mistakes=[
        mis("Stopping at the line with the keyword.", "Read one sentence before and after. The answer may be in the next sentence."),
        mis("Choosing an option because it sounds authoritative, such as 'studies show...'.", "Pick it only if the passage cites that study."),
        mis("Missing NOT or EXCEPT in the stem and marking the true statement.", "Circle NOT or EXCEPT first. The answer is the odd one out."),
        mis("Ignoring qualifiers like mainly, only and some.", "Compare every qualifier with the passage. Detail questions turn on these words."),
    ],
    revision=[
        "Detail answers are written in the passage. Always go back to the line.",
        "Use a keyword to locate. Read one sentence before and after.",
        "Answer in your own words first, then match the paraphrase.",
        "Wrong options: reversal, extreme, not stated, wrong paragraph.",
        "Why questions: look for because, since, so that.",
        "NOT or EXCEPT: tick the three that are present. The leftover is the answer.",
        "Check qualifiers and numbers word by word.",
    ],
    patterns=[
        pat("rc-p10", "Direct detail ('According to the passage...')", "very common",
            "The stem asks what, when, how often or what happened, usually with 'according to the passage'.",
            ["Take the keyword from the question and find it.", "Read that sentence and the next one.", "Say the answer in your words, then pick the matching paraphrase.", "Double-check qualifiers such as some, most, all."],
            "The answer is written in the passage. You only need to find it.",
            "\"The library opens at 9 a.m. on weekdays and at noon on Sundays.\" According to the passage, when does the library open on Sundays?",
            ["The keyword is Sundays.", "The line says 'at noon on Sundays'."],
            "At 12 noon"),
        pat("rc-p11", "Reason or cause detail ('Why...?')", "very common",
            "'Why did...?', 'What was the reason for...?', 'According to the passage, ... because...'.",
            ["Find the event the question names.", "Look for because, since, as, so that or due to near it.", "The clause after that word is the answer.", "Match it with the option that gives the same reason, not a related fact."],
            "A cause is always tied to its event by a linking word.",
            "\"Travellers rested in the stepwell at noon because the air near the water stayed cool.\" Why did travellers rest there?",
            ["The event is resting at noon.", "The clause after 'because' is: the air near the water stayed cool."],
            "Because it was cool near the water"),
        pat("rc-p12", "NOT mentioned or EXCEPT", "common",
            "The stem contains NOT or EXCEPT, often in capitals.",
            ["Circle NOT or EXCEPT.", "Find the list or sentence the options come from.", "Tick each option that is present in the passage.", "The one left, absent or contradicted, is the answer."],
            "Three options are true to the passage. Only one is not.",
            "\"The kit contains a torch, a whistle and a first-aid box.\" Which is NOT in the kit? (a) torch (b) whistle (c) rope (d) first-aid box",
            ["Torch, whistle and first-aid box are all listed.", "Rope is not listed."],
            "(c) rope"),
        pat("rc-p13", "Which statement is true? (qualifiers and numbers)", "common",
            "'Which of the following is true or correct according to the passage?' with four full-sentence options.",
            ["Test each option against its line.", "Look hard at qualifiers such as all, only, every, most, and at numbers.", "Treat an option with one wrong word as fully wrong."],
            "Setters make three options false by changing one small word in each.",
            "\"The club began with 12 members and had 200 members four years later.\" Which is true? (a) It began with 200 members (b) It grew from 12 to 200 members in four years (c) It lost members (d) It has 12 members now",
            ["(a) swaps the numbers.", "(c) reverses the trend.", "(d) uses the old figure."],
            "(b)"),
        pat("rc-p28", "Complete the statement using the passage", "occasional",
            "A sentence with a blank or a dash, such as 'According to the passage, the school garden was started ___'.",
            ["Read the start of the sentence and find its keyword in the passage.", "Read the line and say the ending in your own words.", "Choose the option that finishes the sentence with that meaning and stays grammatical."],
            "The passage supplies the ending. The options only reword it.",
            "\"The ferry runs every hour, but it stops when the river is in flood.\" The ferry service ___ (a) runs only in floods (b) is hourly but stops in floods (c) runs twice a day (d) never stops",
            ["'Every hour' gives hourly.", "'Stops when the river is in flood' gives the exception."],
            "(b) is hourly but stops in floods"),
    ],
)

# =====================================================================
# 4. Inference
# =====================================================================
SUBS["rc-inference"] = dict(
    concept=(
        "To infer is to reach a conclusion from clues. The passage does not say it in words, but it clearly suggests it. "
        "A detail is written on the page. An inference is one small step beyond the page. "
        "Use the must-be-true test: if the option were false, the passage would stop making sense."
    ),
    notes=r"""### What an inference is
To **infer** means to reach a conclusion from clues. The passage does not say it in words, but it clearly suggests it.

Your friend comes in with a wet umbrella and wet shoes. Nobody told you, but you infer that it is raining outside. You cannot infer that "it will rain all week". That is too big a step.

If an option can be pointed to as a sentence in the passage, it is a detail. If it is the unavoidable next step from a stated sentence, it is an inference.

### Detail, inference or wrong
Passage: *"Harish's free solar pump let him water his fields for longer than the crop needed. Two years later, his borewell water had dropped."*

| Option | Type |
|---|---|
| "Harish watered his fields for longer than needed." | detail (written) |
| "Free power led Harish to over-use groundwater." | **inference** (one step) |
| "Solar pumps always destroy groundwater." | too big a step |
| "Harish will sell his land." | no support |

### The must-be-true test
For each option ask: *"If this were false, would the passage stop making sense?"*

- If yes, it is a strong inference and likely correct.
- If the passage could still stand, the option is only a guess. Reject it.

> **Rule:** A correct inference is one stated idea plus one small logical step. If you need two steps, extra facts or a jump in scale (one city to all countries), reject it.

**Distance control.** Take the line: "she cannot afford the electricity that cooling demands".

- "Cooling appliances are of limited use to the poorest residents." Small step. Good.
- "Her city will ban air conditioners." Large step. Wrong.
- "She cannot afford electricity." Word for word. This is a detail, not an inference.

### Types of inference questions
1. **"It can be inferred..." or "The passage suggests..."** This is the general type.
2. **Implied meaning of a line.** "What does the author mean by '...'?" Explain the idea behind the words, often a figure of speech.
3. **Assumption.** Something the author takes for granted without saying it.
4. **Prediction or application.** "What is most likely to happen if...?" or "Which situation is most similar to...?"

### How to handle an assumption question
1. Find the conclusion, what the author wants you to accept.
2. Find the reason given.
3. Ask what hidden link joins the reason to the conclusion. That link is the assumption.
4. Test it. If the assumption were false, the conclusion would collapse.

> **Example:** "Caterers cook extra food because running short is a disgrace." The assumption is that leftover food is less embarrassing than running out.

**Prediction questions.** Follow these steps.

1. Say the passage's rule in simple words: "extra sunshine now earns money instead of pumping more water".
2. Apply that rule to the new situation.
3. Pick the option that follows the same rule. Reject options that need new information.

**Author intent.** For "Why does the author mention Ahmedabad's plan?", give the point of the surrounding argument. Here it is that heat action is affordable and already working. Wrong options describe what the example literally is, not what it does.

### Option types to remove
- **Copied line.** An option that repeats a sentence word for word is a detail. For "infer" questions it is usually not the best answer.
- **Outside knowledge.** "Solar panels last 25 years" may be true. If the passage does not support it, it is wrong.
- **Too extreme.** Words like *all, always, never, must, completely*.
- **Added motive.** An option that says someone acted "deliberately" or "to hurt" when the passage gives no motive.
""",
    tricks=[
        {"title": "One-step rule",
         "body": "Correct inference = stated idea plus one logical step. Two steps, extra facts or a change of scale means reject.",
         "example": {"q": "Passage: 'A workforce that cannot plan a month ahead cannot borrow, train or save with confidence.' Which is a valid inference?",
                     "steps": ["One step: insecure income blocks long-term commitments.", "'Gig work will soon be banned' needs an outside assumption, so it fails."],
                     "answer": "Insecure income stops workers from making long-term commitments"}},
        {"title": "Verbatim is a verdict",
         "body": "In an inference question, an option that repeats passage wording without adding a step is wrong by definition. Cross it out first."},
        {"title": "Extremity filter",
         "body": "Inferences with only, never, must or inevitably are almost always one step too far. Moderate options (may, tends to, is likely) fit the must-be-true test better."},
    ],
    mistakes=[
        mis("Bringing in real-world facts to justify an option.", "Use only what the passage supports."),
        mis("Treating a copied line as an inference.", "A copied line is a detail. An inference adds one step."),
        mis("Inferring the author's personal life or politics from a neutral, informational passage.", "Stay with what the text shows."),
        mis("Choosing an inference so weak it could follow from any passage.", "It must follow from this passage."),
    ],
    revision=[
        "Inference = one small step from a line, never a big leap.",
        "Use the must-be-true test.",
        "Implied meaning: explain the idea behind the words.",
        "Assumption: the hidden link between reason and conclusion.",
        "Prediction or application: apply the passage's rule to the new case.",
        "Reject word-for-word copies, outside facts, extreme words and invented motives.",
    ],
    patterns=[
        pat("rc-p14", "'It can be inferred from the passage that...'", "very common",
            "The stem uses infer, imply, suggest, 'most probably' or 'it can be concluded'.",
            ["Find the line the question is about.", "Take one logical step from that line.", "Apply the must-be-true test to each option.", "Reject copies, extremes and outside facts."],
            "The right option is the unavoidable next step from what is written.",
            "\"The shop is crowded every morning since the government moved its forms online.\" What can be inferred? (a) Many people need help filling online forms (b) The government has closed all offices (c) The shop sells food (d) People dislike computers",
            ["The crowd began when forms went online.", "So people come for help with online forms.", "(b) is extreme, (c) is unsupported, (d) goes against the passage."],
            "(a)"),
        pat("rc-p15", "Implied meaning of a quoted line", "common",
            "'What does the author mean by...?', 'The statement \"...\" implies that...'.",
            ["Read the quoted line and the sentence around it.", "Ask what idea the line expresses. It is often figurative.", "Choose the option that explains the idea, not one that reads the words literally."],
            "A quoted line usually stands for a bigger idea.",
            "\"Earlier, extra sunshine meant extra pumping. Now it means extra money.\" What is implied?",
            ["Earlier, spare solar power ran the pump for more water.", "Now the farmer sells the spare power."],
            "Surplus power now earns money instead of being spent on pumping"),
        pat("rc-p16", "Assumption behind a statement", "occasional",
            "'The author assumes that...', 'The statement is based on the assumption that...'.",
            ["Separate the reason from the conclusion.", "Find the unstated link that makes the reason lead to the conclusion.", "Negate the option. If the argument breaks, it is the assumption."],
            "An argument fails without its hidden link.",
            "\"The road will reduce travel time, so traders will earn more.\" What is assumed?",
            ["Reason: the road saves travel time. Conclusion: traders earn more.", "The link is that saved time helps traders earn more, for example by reaching markets sooner.", "If time saved did not matter to earnings, the conclusion would fail."],
            "Traders' earnings depend partly on travel time"),
        pat("rc-p17", "Prediction or application (most likely, most similar)", "occasional",
            "'If ... happens, which is most likely?', 'Which of the following situations is most similar to...?'",
            ["Write the passage's rule in one line.", "Apply it to the new case.", "The answer follows the same rule. Reject options that need extra facts or go to extremes."],
            "The new case must follow the same logic as the passage.",
            "Passage: volunteers collect untouched wedding food and give it to shelters. Most similar: (a) a shop raising prices (b) a bakery giving unsold bread to an orphanage (c) a family cooking less (d) a hotel adding new dishes",
            ["Rule: surplus food is collected and given to people in need.", "Only (b) follows this rule."],
            "(b)"),
        pat("rc-p29", "Which statement cannot be concluded?", "occasional",
            "'Which of the following cannot be inferred?', 'Which is definitely NOT supported by the passage?'",
            ["Test each option with the must-be-true test.", "Mark options that follow from a line as supported.", "The option with no support, or a contradiction, is the answer."],
            "Three options follow from the passage. One does not.",
            "\"Riya walks to school because the bus stop is far, and she leaves early to avoid the noon heat.\" Which cannot be inferred? (a) Riya's school is reachable on foot (b) The bus stop is far from her home (c) She dislikes noon heat (d) Riya's school has no walls",
            ["(a), (b) and (c) follow from the lines.", "Nothing in the passage mentions the school walls."],
            "(d)"),
    ],
)

# =====================================================================
# 5. Vocabulary in context
# =====================================================================
SUBS["rc-vocab-context"] = dict(
    concept=(
        "These questions give a word or phrase from the passage and ask its meaning as used there. "
        "Many English words have more than one meaning, and the sentence decides which one is right. "
        "Only one sentence matters, so do these questions first."
    ),
    notes=r"""### What vocabulary in context means
In SSC reading comprehension you are asked the meaning of a word **as used in the passage**. This can differ from the common meaning. The question is local, and only one sentence matters.

Take the word **bank**.

- *She deposited money in the bank.* It means a place for money.
- *They sat on the bank of the river.* It means the side of a river.

Both meanings are correct English. Only one fits each sentence.

### The plug-in test
Use it on every such question.

1. Read the full sentence that contains the word.
2. Cover the word and think of your own simple word that fits.
3. Put each option in place of the word.
4. The right option keeps the sentence's meaning, grammar and tone.

Worked example: *"Buyers from three districts **haggled** cheerfully over prices."*

- Your own word: *bargained*.
- "quarrelled violently" does not fit *cheerfully*.
- "bargained" fits perfectly.

> **Tip:** Words are rarely synonyms in isolation. They are synonyms in this sentence.

### Question types
1. **Synonym in context.** The closest meaning.
2. **Antonym in context.** The most nearly opposite. First find the meaning in the sentence, then take its opposite **once**. In *"It was a **modest** victory"*, modest means small, so the opposite is huge or sweeping. It is not "proud", which is the opposite of the other meaning, "humble".
3. **Phrase or idiom meaning.** Treat the phrase as one unit. *Did not take it lying down* means refused to accept without a fight. *Cut corners* means skipped necessary steps to save time or money.
4. **Multiple-meaning word.** The common meaning is the trap.
   - *shelved* means postponed, not put on a shelf.
   - *craft* means skill, not a boat.
   - *toll* means loss or damage, not a road tax.

### Expect the shift
Setters choose words with a double life.

- *cushions* an illness means protects against its impact, not bedroom cushions.
- *dipped* means declined briefly, not dipped into water.
- *interest* in banking is a charge. *Interest* in reading is curiosity.

If one option matches the dictionary meaning and another matches the sentence, the sentence wins.

### Keep the part of speech and the tone
If the word is a verb in the passage, the answer must work as a verb. In *"The board **shelved** the plan"*, *shelved* is a verb, so "postponed" fits. A noun such as "a shelf" cannot.

Also keep the tone. *"The traders **celebrated**"* is positive. An option like "mourned" breaks the tone even if you are unsure of the meanings. In a critical sentence, choose the critical option.

### Multiple-meaning words to know
| Word | Everyday meaning | Meaning often used in passages |
|---|---|---|
| shelve | put on a shelf | postpone, set aside |
| craft | handmade object, boat | skill, profession |
| toll | road tax | damage, loss of life |
| frank | not listed | honest, open |
| check | examine | stop, control ("check the spread") |
| sound | noise | healthy, reliable ("sound advice") |
| grave | burial place | serious ("a grave mistake") |
| novel | story book | new, original ("a novel idea") |
| bear | animal | tolerate, carry |
| fine | good | penalty, very thin |

### Speed tip
Vocabulary questions need only one sentence. Do them first in the set, about 20 seconds each. For phrases, read one line before and one after. Figurative phrases get their meaning from the argument around them.
""",
    tricks=[
        {"title": "Own words first",
         "body": "Cover the options and replace the word with your own simple word. Then find the option that matches your word. This removes the dictionary-meaning bait.",
         "example": {"q": "'...no paid leave cushions an illness.' What does cushions mean here?",
                     "steps": ["Own word: softens or protects against.", "'Protects from the effects of' matches.", "'Provides comfort in the home' is the dictionary bait."],
                     "answer": "Protects from the effects of"}},
        {"title": "Tone match",
         "body": "The substitute must keep the sentence's attitude. In a critical sentence, choose the critical option. A neutral synonym that drains the criticism is wrong."},
        {"title": "Two-line rule for phrases",
         "body": "For phrase-meaning questions, read one line before and one line after. Figurative phrases get their meaning from the surrounding argument, not from the words."},
    ],
    mistakes=[
        mis("Picking the option with the word's most common meaning when the sentence needs another sense.", "Test each option in the sentence. The sentence decides."),
        mis("Changing the part of speech while plugging in, such as a noun option in a verb slot.", "Keep the same part of speech as the passage word."),
        mis("Choosing an opposite for an antonym question because it merely sounds negative.", "Find the meaning first, then flip it once."),
        mis("Reading five lines around the word.", "Context questions need the sentence, or at most the sentence and its neighbour."),
    ],
    revision=[
        "Meaning comes from the sentence, not from the dictionary's first meaning.",
        "Plug-in test: your own word first, then the options.",
        "Antonym: find the meaning in context, then flip it once.",
        "Idioms and phrases: read as one unit. Literal options are traps.",
        "Keep part of speech and tone.",
        "Do vocabulary questions first.",
    ],
    patterns=[
        pat("rc-p18", "Synonym in context (closest meaning)", "very common",
            "'Which word is closest in meaning to X as used in the passage?', 'X most nearly means...'.",
            ["Read the sentence with the word.", "Think of your own replacement word.", "Plug in each option, keeping meaning, grammar and tone.", "Choose the option that works in the sentence, even if another option is a more common meaning."],
            "The passage decides the meaning, not the dictionary's first entry.",
            "\"When the board finally **unveiled** its plan for a mall...\" Closest meaning: (a) hid (b) made public (c) cancelled (d) painted",
            ["The board showed the plan to the public for the first time.", "Own word: announced."],
            "(b) made public"),
        pat("rc-p19", "Antonym in context (most nearly opposite)", "common",
            "'Which word is most nearly OPPOSITE in meaning to X as used in the passage?'",
            ["Find the word's meaning in the sentence first.", "Take the opposite of that meaning, once only.", "Reject synonyms (setters include one) and opposites of a different meaning."],
            "Flipping twice, or flipping the wrong meaning, gives a wrong answer.",
            "\"Scientists are **frank** about the limits of their craft.\" Opposite: (a) honest (b) evasive (c) open (d) direct",
            ["Frank means honest and open.", "The opposite is avoiding the truth.", "(a), (c) and (d) are synonyms."],
            "(b) evasive"),
        pat("rc-p20", "Meaning of a phrase or idiom in the passage", "common",
            "A quoted phrase: 'The phrase \"...\" means...', 'What does the author mean by \"...\"?'",
            ["Treat the phrase as one unit.", "Use the sentence before and after to see what happened.", "Reject literal word-by-word options."],
            "A phrase often means something different from its separate words.",
            "\"Officials under pressure are tempted to **cut corners**.\" What does it mean?",
            ["The context is that codes cost money and officials want quick results.", "Nothing is literally being cut."],
            "Save time or money by skipping necessary steps"),
        pat("rc-p21", "Multiple-meaning word (which sense is used?)", "common",
            "A familiar word whose everyday meaning is an option (shelved, craft, toll, check, sound).",
            ["Assume the common meaning is a trap.", "Plug in each meaning. Only one keeps the sentence sensible.", "Confirm the part of speech."],
            "Setters pick words whose common meaning does not fit.",
            "\"The board **shelved** the plan and repaired the roof instead.\" Shelved means: (a) arranged on shelves (b) put aside (c) sold (d) announced",
            ["A plan cannot be placed on a shelf.", "The board dropped it for now."],
            "(b) put aside"),
        pat("rc-p30", "Unknown word: guess from the clues around it", "common",
            "A word you have never seen. The sentence has a clue such as 'but', 'and', 'like' or an example.",
            ["Find the clue: a contrast word (but, yet) or an example after the word.", "Decide if the word is positive or negative from the clue.",
             "Choose the option with the same direction and a matching meaning."],
            "The sentence often explains a hard word for you.",
            "\"Unlike his generous brother, Kiran was **parsimonious** and never gave a rupee.\" Parsimonious means: (a) very kind (b) unwilling to spend (c) careless (d) proud",
            ["'Unlike his generous brother' shows a contrast.", "'Never gave a rupee' shows the meaning."],
            "(b) unwilling to spend"),
    ],
)

# =====================================================================
# 6. Tone and attitude
# =====================================================================
SUBS["rc-tone-attitude"] = dict(
    concept=(
        "Tone questions ask how the author speaks, not what the author says. Tone is the author's feeling or manner. "
        "Attitude is the author's feeling towards one thing in the passage. "
        "Tone lives in adjectives, adverbs and contrast words, not in the facts themselves."
    ),
    notes=r"""### What tone is
**Tone** is the author's feeling or manner in writing, the voice behind the words. The same fact can be written in different tones.

- Neutral: "The lake has become polluted."
- Critical: "Despite crores spent on brochures, the lake is still a sewer."
- Hopeful: "With a few drains, the lake can be clean again."

**Attitude** is the author's feeling towards one particular thing in the passage, such as a plan, a group or an idea.

### Where tone hides
Tone is carried by **describing words** (adjectives and adverbs) and by **contrast words**.

- *glossy brochures, grand plan, the cameras leave* mock the show.
- "Surely a city that can spend crores on brochures can find money for a drain" is sarcasm. It says one thing to point out a failure.
- *however, yet, but* mark the turn. The part after them shows what the author really thinks.

### Common tone words
| Tone word | Meaning | Sign in the passage |
|---|---|---|
| informative, objective, neutral | only gives facts | no praise, no blame |
| analytical | examines causes and effects | because, as a result, weighs points |
| critical | points out faults | *fails, merely, despite promises* |
| sarcastic, ironic | mocks by saying the opposite or exaggerating | *Surely..., what a grand plan* |
| appreciative, laudatory | praises | *remarkable, a model, succeeded* |
| optimistic, hopeful | expects good results | *can, will improve, promising* |
| pessimistic | expects bad results | *hopeless, bound to fail* |
| balanced | gives both sides fairly | *neither... nor, on one hand... on the other* |
| nostalgic | fondly remembers the past | *those were the days* |
| cautionary | warns | *risk, danger, before we...* |
| indifferent | does not care | rarely correct; authors write because they care |

### Method
1. Underline one evaluative phrase in each paragraph.
2. Decide if each is positive, negative or neutral, and how strong.
3. Check the **last sentence**. It usually shows the final attitude.
4. Pick the tone word that matches both direction and strength.

> **Tip:** The clause after *but, however* or *yet* carries the author's real position. The clause before it is the position being set aside.

### Degree matters
Suppose the author says online classes are "neither the saviour nor the failure". The tone is **balanced**, not angry and not celebratory. Extreme tone words (*furious, euphoric, hostile*) are usually wrong in exam passages.

Match the strength, not just the direction. *Sceptical* is not *hostile*. *Cautiously optimistic* is not *confident*.

**A serious topic is not an emotional tone.** A science passage about germs or earthquakes is still **informative** if it only explains. Do not call it "alarmed" because the subject is scary. Words like *sarcastic, pessimistic, passionate* are wrong for a neutral passage.

> **Watch:** The feelings of people quoted in the passage are not the author's tone.

### Attitude towards one thing
For "the attitude of the author towards gig platforms", collect every line about that thing. Note the verbs used with it, such as *celebrate, warn, can be applied now*. Then sum up. The author may be critical of the rules but not of flexibility itself. One-sided options, fully supportive or fully hostile, fail.

**Author would agree.** These are inference questions about the author's opinion. The correct option matches what the author says and how strongly. If the author wants "sewage stopped before ceremonies", the author would agree that stopping sewage matters more than publicity. The author would not agree that "the lake can never be cleaned".

Authors of SSC passages usually take measured positions. Options that make the author desperate, euphoric or completely dismissive almost never fit.

### Source of the passage
Match the style to the type of text.

- Facts and explanations, no opinion: a science book, textbook or encyclopaedia.
- Opinion on a current issue with suggestions: a newspaper editorial or opinion piece.
- Personal feelings in first person, with dates: a diary or memoir.
- A story with characters and dialogue: a short story.
- Selling words (best, buy now): an advertisement.
""",
    tricks=[
        {"title": "Adjective audit",
         "body": "Sweep the passage for adjectives and adverbs that carry feeling, such as quietly, badly, remarkable, merely, confident. Three of them in the same direction fix the tone.",
         "example": {"q": "Passage words: 'quietly getting hotter', 'turn bedrooms into ovens', 'plan itself out of one'. What is the tone?",
                     "steps": ["The first two phrases show the problem is real.", "The last phrase offers a way out.", "So the author is concerned but hopeful, not alarmed or dismissive."],
                     "answer": "Concerned and optimistic"}},
        {"title": "However counts double",
         "body": "The clause after but, however or yet carries the author's real position. Tone and opinion questions key off the second half."},
        {"title": "Degree matching",
         "body": "Match intensity as well as direction. Pick the option at the same temperature as the passage."},
    ],
    mistakes=[
        mis("Calling a fact-heavy passage sarcastic because its subject is unpleasant.", "Judge the author's words, not the subject. Facts only means informative."),
        mis("Reading the tone of people quoted in the passage as the author's own tone.", "Find the author's own evaluative words."),
        mis("Choosing an extreme tone word such as outraged or euphoric when the passage argues in a moderate way.", "Choose the option at the same strength as the passage."),
        mis("Forgetting that a balanced or analytical option is often correct when the author gives both sides.", "Check whether both sides are weighed before you pick a one-sided tone."),
    ],
    revision=[
        "Tone is the author's voice. Attitude is the feeling towards one thing.",
        "Look at adjectives, adverbs and what comes after however, yet, but.",
        "Match direction and degree. Avoid extreme tone words.",
        "A serious subject can still have a neutral tone.",
        "Quoted people's feelings are not the author's tone.",
        "Source questions: match the writing style to the type of text.",
    ],
    patterns=[
        pat("rc-p22", "Tone of the passage", "common",
            "'The tone of the passage is...', 'Which word best describes the author's tone?'",
            ["Collect the evaluative words: adjectives, adverbs, 'surely', 'merely'.", "Decide direction (positive, negative, neutral) and strength.", "Confirm with the closing sentence.", "Reject extremes and tone words that fit only one line."],
            "Tone is built from many small word choices, not from one line.",
            "\"The new bridge, built in record time and under budget, has cut the travel time of thousands of commuters.\" Tone: (a) critical (b) appreciative (c) sarcastic (d) indifferent",
            ["'Record time', 'under budget' and 'cut travel time' are all praise.", "There is no mockery."],
            "(b) appreciative"),
        pat("rc-p23", "Author's attitude towards a specific thing", "common",
            "'The author's attitude towards X is...', 'How does the author view...?'",
            ["Find every line that mentions X.", "Note the words used with X: praise, doubt, blame.", "Sum up in one phrase and match it.", "Reject one-sided options if the author gives both sides."],
            "Attitude is about one topic, so only lines about that topic count.",
            "\"Online classes were a lifeline for children with laptops, and a blank screen for children without them.\" What is the attitude towards online classes?",
            ["They are positive for some children.", "They are useless for others."],
            "Useful, but dependent on access; neither fully good nor fully bad"),
        pat("rc-p24", "Author would agree or disagree with...", "common",
            "'With which statement would the author most likely agree?'",
            ["Recall the author's main opinion, usually in the last lines.", "Pick the option that follows from it at the same strength.", "Reject options that are extreme, opposite, or about something the author never discussed."],
            "It is an inference question about the author's opinion.",
            "Author: \"Brochures are printed every year, but the sewage pipes are never diverted.\" The author would agree that: (a) brochures clean lakes (b) fixing sewage matters more than publicity (c) the lake cannot be saved (d) sewage is harmless",
            ["The author criticises show without action.", "So fixing the cause matters more than publicity."],
            "(b)"),
        pat("rc-p25", "Type or source of the passage", "occasional",
            "'The passage is most likely taken from...', 'The passage is an example of...'.",
            ["Decide the style: facts only, opinion with suggestions, a story, personal feelings, or selling.", "Match that style with the option.", "Reject options whose style clashes, for example a story for a fact-only passage."],
            "Each type of text has its own style.",
            "\"Honey resists decay because it has little water, is slightly acidic and contains an enzyme that produces hydrogen peroxide.\" Source?",
            ["The passage has only facts and explanation.", "It has no opinion and no selling."],
            "A science book or article"),
        pat("rc-p31", "Sarcasm or irony in a quoted line", "occasional",
            "'What is the author's tone in the line \"...\"?', a line that praises where blame is meant.",
            ["Read the line with its neighbours.", "Ask if the words say one thing while the facts say the opposite.", "If so, choose sarcastic or ironic. If the words match the facts, choose the plain tone."],
            "Sarcasm praises on the surface but criticises underneath.",
            "\"What a grand plan: the drain is still blocked, but the ribbon-cutting was lovely.\" The tone of this line is: (a) appreciative (b) sarcastic (c) neutral (d) nostalgic",
            ["'Grand plan' and 'lovely' sound like praise.", "The blocked drain shows the plan failed.", "So the praise is meant as mockery."],
            "(b) sarcastic"),
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
