# Phase 2 deep content: english / reading-comprehension. Idempotent (upsert by id). Run: py -3 reading-comprehension.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import load, save, QA, P, upsert_list, apply_subtopics, fill_group_passages, report

TOPIC = "reading-comprehension"
data = load(TOPIC)
before = {"subs": len(data["subtopics"]), "practice": len([q for q in data["practice"] if not q["id"].startswith("rc-")])}

# ---------------------------------------------------------------- notes + patterns
S = {}

S["rc-reading-strategy"] = {
"notes": r"""### What is a reading comprehension (RC)?
"Comprehension" means *understanding*. In an RC question you get a short passage (usually 200–350 words) and 4–6 questions on it. The exam is not testing your general knowledge. It is testing one skill: **can you find and understand what is written?** Every correct answer can be pointed to in the passage.

Think of RC like a train timetable. You do not memorise the whole timetable. You know where things are, and you go back to the right line when someone asks you a question.

### The 3-step routine
1. **Read the passage once, calmly (about 2 minutes).** Do not try to remember every fact. Just notice what each paragraph is doing.
2. **Read the questions.** Only the question line — not all the options yet.
3. **Go back to the exact lines** the question points to, answer from those lines, then look at the options.

### Paragraph mapping (the biggest time-saver)
After each paragraph, tell yourself its job in 3–5 words:
- Para 1: *problem — millets disappeared*
- Para 2: *why millets are useful now*
- Para 3: *what stops the revival*

Now a question like "What is the purpose of the second paragraph?" takes 5 seconds. A detail question also becomes quick, because you know which paragraph to search.

### Words that signal the passage structure
| Signal words | What they tell you |
|---|---|
| however, yet, but, still | the author is turning — the important point usually comes AFTER this word |
| because, since, as, due to | a reason — "why" questions are answered here |
| so, therefore, thus, as a result | a result or conclusion |
| for example, such as, consider | an example — it supports the point just before it |
| first, then, finally | a sequence or list |

### Question types you will meet
- **Main idea / title / purpose** — about the whole passage.
- **Detail** — "According to the passage…" — answer is written in one line.
- **Inference** — "It can be inferred…" — answer is one small step from a line.
- **Vocabulary in context** — meaning of a word *as used in the passage*.
- **Tone / attitude** — how the author feels.
- **Structure types** (this subtopic): statement combinations (I, II, III), paragraph purpose, "why does the author mention…", how the passage is organised, and "which question can be answered from the passage".

### Order of solving
Do the quick, local questions first: vocabulary (needs only one sentence), then detail, then inference, and main idea/tone last — by then you understand the passage best.

### Golden rules
- **Passage only.** If an option is true in real life but not in the passage, it is wrong.
- **Beware extreme words**: *always, never, only, all, completely*. Passages usually speak moderately.
- **Same words ≠ same meaning.** An option that copies passage words but changes their meaning is a trap.
- **Mark and move.** If one question is stuck for more than 40 seconds, mark it and come back.

### Time plan for 5 questions (about 6–7 minutes)
Read: 2 min → each question: 30–45 s → final check: 30 s.

### Quick revision
- Read passage first, questions next, then return to lines.
- Map each paragraph in a few words.
- "However/yet/but" = the key point follows.
- For statement-combination questions, judge each statement separately, then pick the matching option.
- For "why does the author mention X", ask what point X *supports*, not what X *is*.
- Never use outside knowledge; never choose an extreme option without extreme words in the passage.
""",
"patterns": [
 P("rc-p1", "Statement combination (Which of the statements I, II, III is/are true?)", "common",
   "The question lists two or three numbered statements and the options say 'Only I', 'Only I and III', 'All of these'.",
   "1. Check statement I against the passage: True, False or Not stated.\n2. Do the same for II and III, one at a time.\n3. 'Not stated' counts as NOT true.\n4. Pick the option that matches your T/F list exactly.\n\n*Why it works:* judging one short statement is easier than comparing four long options. Once you know one statement is false, you can cut every option that contains it.",
   "Passage: \"The pond was dug in 2015. It fills during the monsoon and supplies water to forty families till March.\"\nWhich is/are true? I. The pond fills in the monsoon. II. It supplies water all year. III. Forty families use it.\n(a) Only I (b) Only I and III (c) Only II and III (d) All of these",
   "I is stated → True. II: water lasts only *till March* → False. III is stated → True. So the answer is **(b) Only I and III**."),
 P("rc-p2", "Purpose or role of a paragraph", "common",
   "'The second paragraph mainly…', 'What role does the last paragraph play?', 'The purpose of paragraph 3 is to…'.",
   "1. Recall your paragraph map (3–5 words per paragraph).\n2. Ask: does this paragraph give a problem, a cause, an example, a solution, or a contrast?\n3. Choose the option that names that job for THIS paragraph — not the job of a neighbouring paragraph.\n\n*Why it works:* wrong options usually describe a different paragraph correctly.",
   "Para 1 says city buses are always late. Para 2 says this is because roads are jammed by parked cars. Para 3 suggests paid parking. The second paragraph mainly:\n(a) describes the problem (b) explains the cause of the problem (c) offers a solution (d) praises bus drivers",
   "Para 2 gives the *reason* buses are late (parked cars). Option (a) is para 1's job and (c) is para 3's job. Answer: **(b)**."),
 P("rc-p3", "Why does the author mention X? (function of an example)", "common",
   "'The author mentions … in order to…', 'Why does the author refer to…?', 'The example of … is given to show…'.",
   "1. Find X in the passage.\n2. Read the sentence BEFORE X — it usually states the point X supports.\n3. The answer names that point (to illustrate / to prove / to contrast), not a description of X itself.\n\n*Why it works:* examples never stand alone; they exist to support a claim nearby.",
   "\"Small savings add up. A tea-seller who keeps aside ₹20 a day has over ₹7,000 at the end of a year.\" Why is the tea-seller mentioned?",
   "The sentence before says 'Small savings add up'. The tea-seller is an example that *illustrates how small daily savings become a large sum*. He is not mentioned to talk about tea or about his income level."),
 P("rc-p4", "How is the passage organised? (structure)", "occasional",
   "'Which of the following best describes the organisation/structure of the passage?'",
   "1. Write the paragraph map in order: e.g. *past → present advantage → obstacle*.\n2. Read each option and check every part of it against your map, in the same order.\n3. Reject options with even one wrong part (e.g. 'no solution is offered' when a solution is given).",
   "Para 1: a village had no doctor. Para 2: a mobile clinic started visiting weekly. Para 3: child illness fell sharply. Best description?\n(a) A problem, a response, and its result (b) Two views compared (c) A theory rejected (d) A list of causes",
   "Map: problem → response (clinic) → result (less illness). Answer: **(a)**."),
 P("rc-p5", "Which question can be answered from the passage?", "occasional",
   "'The passage answers which of the following questions?', 'Which question can be answered using the information in the passage?'",
   "1. For each option, look for the exact information needed (a number, a name, a reason).\n2. If the passage gives only part of it, or nothing, reject it.\n3. The correct option is usually a *why* or *how* whose answer is clearly written.\n\n*Trap:* options asking for exact numbers, years or names that the passage never gives.",
   "Passage: \"The school started a kitchen garden so that children could eat fresh vegetables at lunch.\" Which question is answered? (a) How big is the garden? (b) Why did the school start a kitchen garden? (c) Who planted the first seed? (d) When was the school built?",
   "Only the reason is given ('so that children could eat fresh vegetables'). Answer: **(b)**."),
]}

S["rc-main-idea"] = {
"notes": r"""### What is the main idea?
The **main idea** (also called the *central idea* or *theme*) is the one big point the whole passage makes. Every paragraph helps to support it. A **title** is the main idea squeezed into a short heading. The **purpose** is *why* the author wrote the passage — to inform, to argue, to warn, to encourage.

Everyday example: a friend talks for five minutes about late trains, crowded coaches and dirty platforms. The main idea is not "trains are late". It is "*the railway service in our town is poor*". Each complaint supports that one point.

### Where to find it
- The **first paragraph** usually introduces the topic or problem.
- The **last paragraph** usually gives the author's conclusion or suggestion.
- Middle paragraphs give reasons, examples and data.

So the main idea = **topic (from the start) + the author's point about it (often at the end)**.

### The three tests for a correct main-idea option
1. **Covers the whole passage** — not just one paragraph or one example. (*Too narrow* = wrong.)
2. **Stays inside the passage** — does not add ideas the passage never discussed. (*Too broad* = wrong.)
3. **Matches the author's strength** — does not say *always, only, never* when the author was moderate. (*Too extreme* = wrong.)

### Worked example
Passage (short): *"Many old stepwells lie full of garbage. Yet a few towns that cleaned them found they still collect rainwater and raise groundwater. Reviving them costs little."*
- "Stepwells are full of garbage" → too narrow (only first line).
- "India faces a water crisis" → too broad (the passage talks only about stepwells).
- "Only stepwells can solve water shortage" → too extreme.
- "**Cleaning old stepwells is a cheap way to improve water supply**" → correct: covers all lines.

### Title questions
A good title is short, covers the whole passage and often shows both sides if the passage has both. Titles with a colon ("Gig Work: Freedom with a Price") are common right answers because they hold two halves of the idea.

**Title trap:** a catchy option that names only the *first example*. If the passage starts with a farmer's story but is really about water policy, "A Farmer's Story" is too narrow.

### Purpose questions
Look at the verbs the author uses:
| Author mainly… | Purpose word |
|---|---|
| gives facts, explains how something works | to inform / to explain |
| gives reasons for one side, says "should/must" | to argue / to persuade |
| points out a danger | to warn |
| praises something and asks readers to do it | to encourage |
| points out faults | to criticise |

If the passage is a neutral explanation, "to criticise" or "to persuade" is wrong even if the topic is serious.

### Paragraph main point
Some questions ask the main point of just one paragraph. Apply the same three tests, but to that paragraph only. Its first sentence (the *topic sentence*) usually states the point.

### Method (30–40 seconds)
1. Before looking at options, say the main idea in about ten words.
2. Remove options that are too narrow, too broad, or too extreme.
3. Between two survivors, pick the one that includes the author's conclusion.

### Quick revision
- Main idea = topic + author's point about it.
- Check first and last paragraphs first.
- Three killers: too narrow, too broad, too extreme.
- Title = whole passage in a few words; colon titles often fit two-sided passages.
- Purpose = why it was written: inform, argue, warn, encourage, criticise.
- Make your own summary before reading options.
""",
"patterns": [
 P("rc-p6", "Central idea / main theme of the passage", "very common",
   "'The central idea/main theme of the passage is…', 'The passage is primarily concerned with…', 'Which option sums up the passage?'",
   "1. Say the topic (from para 1) + the author's point (usually in the last para) in one line.\n2. Cut options that cover only one paragraph (too narrow).\n3. Cut options that talk about a bigger subject than the passage (too broad).\n4. Cut options with *only/always/never* the author did not use (too extreme).\n\n*Why it works:* the main idea must be supported by every paragraph, so partial or inflated options fail.",
   "\"Many families now buy bottled water. Yet a simple home filter gives safe water at a tenth of the cost, and it creates no plastic waste.\" The central idea is:\n(a) Bottled water is unsafe (b) Home filters are a cheaper, cleaner alternative to bottled water (c) Plastic waste is rising in India (d) All families should stop drinking water from taps",
   "Topic: bottled water. Author's point: a home filter is cheaper and creates no plastic. (a) is never said; (c) is too broad; (d) is extreme and unrelated. Answer: **(b)**."),
 P("rc-p7", "Most suitable title", "very common",
   "'Which of the following is the most appropriate/suitable title for the passage?'",
   "1. Build your ten-word summary first.\n2. Reject titles that name only an example from one paragraph.\n3. Reject dramatic titles that go beyond the author (e.g. 'The End of…', 'The Only Way…').\n4. Prefer the title that covers both the problem and the author's answer if the passage has both.",
   "A passage describes how a village built check dams, how its wells refilled and how farmers now grow two crops. Best title?\n(a) Check Dams Bring a Village Back to Life (b) How to Build a Wall (c) Farming in India (d) The Monsoon Always Fails",
   "(b) misses the effect, (c) is too broad, (d) is extreme and not discussed. (a) covers the action and the result. Answer: **(a)**."),
 P("rc-p8", "Author's primary purpose", "common",
   "'The author's main purpose is to…', 'The passage has been written mainly to…'.",
   "1. Notice the author's verbs: *explains* (inform), *should/must* (argue), *danger/risk* (warn), *praises + asks readers* (encourage).\n2. Match the purpose to the WHOLE passage, not to one sentence.\n3. Reject purposes that are too strong (demand, prove) if the author only suggests.",
   "\"Fifteen minutes of reading to a child each evening builds vocabulary. It needs no costly books — a folk tale works as well. Busy parents can surely spare this time.\" The author's purpose is to:\n(a) criticise schools (b) encourage parents to read or tell stories to children daily (c) sell children's books (d) compare folk tales",
   "The author explains a benefit and then urges parents ('can surely spare this time'). Answer: **(b)**."),
 P("rc-p9", "Main point of one paragraph / best summary", "common",
   "'The second paragraph is mainly about…', 'What is the main point of the last paragraph?', 'Which option best summarises…'",
   "1. Read the first sentence of that paragraph (the topic sentence).\n2. Check that the option fits every sentence in that paragraph.\n3. Reject options that describe another paragraph.",
   "Para 2: \"Discarded phones add to e-waste. Workers burn wires to get copper and breathe the fumes. New phones need fresh metals and energy.\" Para 2 is mainly about:\n(a) new phone features (b) the hidden costs of throwing gadgets away (c) the price of copper (d) government rules on repair",
   "Every sentence names a cost of discarding (waste, fumes, fresh resources). Answer: **(b)**."),
]}

S["rc-detail-fact"] = {
"notes": r"""### What is a detail question?
A detail (or *factual*) question asks about something that is **written directly** in the passage: a fact, a reason, a number, a name, a feature. The stem often begins *"According to the passage…"* or *"The passage states that…"*.

These are the easiest marks in RC — but only if you go back and read the line. Memory is not enough, because the options are built to *almost* match the passage.

### Method: Locate → Read around → Say it → Match
1. **Locate.** Pick a keyword from the question — a name, number or unusual word (*stepwell, fat content, ten days*). Find it in the passage.
2. **Read around.** Read that sentence plus one before and one after. Answers often sit in the next sentence.
3. **Say it.** Put the answer in your own words before looking at the options.
4. **Match.** Choose the option that means the same as your words (options usually *paraphrase* — use different words with the same meaning).

### How wrong options are made
| Trap | Example (passage says "Most varieties need little water") |
|---|---|
| **Reversal** — opposite meaning | "Millets need a lot of water" |
| **Extreme** — changes *most* to *all* | "All millets need no water at all" |
| **Not stated** — sounds true, never said | "Millets are grown mainly in Punjab" |
| **Wrong part** — true detail from another paragraph, wrong for this question | a reason given for a different fact |

### Watch the small words (qualifiers)
*some / many / most / all*, *often / always*, *may / will*, *more / less*, *only*. One changed qualifier makes an option wrong.
- Passage: "Rich merchants and queens paid for **the finest** of them."
- Option: "**All** stepwells were paid for by queens." → wrong (two changes: *all* and *only queens*).

### Reason questions ("Why…?")
Look for **because, since, as, so that, due to, the reason is**. The answer is the clause after these words.
- Passage: "Less milk turned sour **because** it was cooled at once."
- Q: Why did less milk turn sour? → "It was cooled immediately."

### NOT / EXCEPT questions
"Which of the following is NOT mentioned…" or "…all of the following EXCEPT".
1. Circle NOT/EXCEPT so you do not forget it.
2. Tick each option you can find in the passage.
3. The one option you **cannot** find (or that is contradicted) is the answer.
Three options usually come from the same sentence or list — find that list and it is quick.

### Numbers and comparisons
If the passage gives numbers ("twelve households… over two hundred within four years"), check every number in the option. A common trap swaps the *before* and *after* figures.

### Quick revision
- Detail answers are WRITTEN in the passage — always go back to the line.
- Use a keyword to locate; read one sentence before and after.
- Answer in your own words first, then match the paraphrase.
- Traps: reversal, extreme, not stated, wrong paragraph.
- "Why" → look for *because / since / so that*.
- NOT/EXCEPT → tick the three that are present; the leftover is the answer.
- Check qualifiers and numbers word by word.
""",
"patterns": [
 P("rc-p10", "Direct detail ('According to the passage…')", "very common",
   "The stem asks what, when, how often, or what happened, usually with 'according to the passage'.",
   "1. Take the keyword from the question and find it.\n2. Read that sentence and the next one.\n3. Say the answer in your words, then pick the matching paraphrase.\n4. Double-check qualifiers (some/most/all).",
   "\"The library opens at 9 a.m. on weekdays and at noon on Sundays.\" According to the passage, when does the library open on Sundays?",
   "Keyword *Sundays* → 'at noon on Sundays'. Answer: **at 12 noon**."),
 P("rc-p11", "Reason / cause detail ('Why…?')", "very common",
   "'Why did…?', 'What was the reason for…?', 'According to the passage, … because…'.",
   "1. Find the event the question names.\n2. Look for *because, since, as, so that, due to* near it.\n3. The clause after that word is the answer. Match it with the option that gives the SAME reason, not a related fact.",
   "\"Travellers rested in the stepwell at noon because the air near the water stayed cool.\" Why did travellers rest there?",
   "The clause after *because*: the air near the water stayed cool. Answer: **because it was cool near the water**."),
 P("rc-p12", "NOT mentioned / EXCEPT", "common",
   "The stem contains NOT or EXCEPT (often in capitals).",
   "1. Circle NOT/EXCEPT.\n2. Find the list or sentence the options come from.\n3. Tick each option present in the passage.\n4. The one left (not present or contradicted) is the answer.",
   "\"The kit contains a torch, a whistle and a first-aid box.\" Which is NOT in the kit? (a) torch (b) whistle (c) rope (d) first-aid box",
   "Torch, whistle and first-aid box are listed. Rope is not. Answer: **(c) rope**."),
 P("rc-p13", "Which statement is true / correct? (qualifiers and numbers)", "common",
   "'Which of the following is true/correct according to the passage?' with four full-sentence options.",
   "1. Test each option against its line.\n2. Look hard at qualifiers (*all, only, every, most*) and numbers.\n3. An option with one wrong word is fully wrong.\n\n*Why it works:* setters make three options false by changing one small word each.",
   "\"The club began with 12 members and had 200 members four years later.\" Which is true? (a) It began with 200 members (b) It grew from 12 to 200 members in four years (c) It lost members (d) It has 12 members now",
   "(a) swaps the numbers, (c) reverses, (d) uses the old figure. Answer: **(b)**."),
]}

S["rc-inference"] = {
"notes": r"""### What is an inference?
To **infer** means to reach a conclusion from clues. The passage does not say it in words, but it is **clearly suggested**. If a detail is written on the page, an inference is *one small step* beyond the page.

Everyday example: your friend comes in with a wet umbrella and wet shoes. Nobody told you, but you can **infer** that it is raining outside. You cannot infer that "it will rain all week" — that is too big a step.

### Detail vs inference vs wrong
Passage: *"Harish's free solar pump let him water his fields for longer than the crop needed. Two years later, his borewell water had dropped."*
| Option | Type |
|---|---|
| "Harish watered his fields for longer than needed." | detail (written) |
| "Free power led Harish to over-use groundwater." | **inference** (one step) ✔ |
| "Solar pumps always destroy groundwater." | too big a step ✘ |
| "Harish will sell his land." | no support ✘ |

### The must-be-true test
For each option ask: *"If this were false, would the passage stop making sense?"*
- If yes → strong inference, likely correct.
- If the passage could still be true → the option is only a guess. Reject it.

### Types of inference questions
1. **"It can be inferred…" / "The passage suggests…"** — the general type.
2. **Implied meaning of a line** — "What does the author mean by '…'?" The answer explains the idea behind the words, often a figure of speech.
3. **Assumption** — something the author *takes for granted* without saying it. Without it, the argument would not work.
   - Argument: "Caterers cook extra food because running short is a disgrace."
   - Assumption: *leftover food is less embarrassing than running out*.
4. **Prediction / application** — "What is most likely to happen if…?" or "Which situation is most similar to…?" Use the passage's own logic on the new case.

### How to handle an assumption question
1. Find the conclusion (what the author wants you to accept).
2. Find the reason given.
3. Ask: what hidden link joins the reason to the conclusion? That link is the assumption.
4. Check: if the assumption were false, the conclusion would collapse.

### How to handle a prediction / application question
1. Say the passage's rule in simple words: *"extra sunshine now earns money instead of pumping more water."*
2. Apply that rule to the new situation.
3. Pick the option that follows the SAME rule. Reject options that need new information.

### Traps
- **Copied line**: an option that repeats a sentence word for word is a detail, not an inference. For "infer" questions, it is usually not the best answer.
- **Outside knowledge**: "Solar panels last 25 years" may be true, but if the passage does not support it, it is wrong.
- **Too extreme**: *all, always, never, must, completely*.
- **Added motive**: an option that says someone did something "deliberately" or "to hurt" when the passage gives no motive.

### Quick revision
- Inference = one small step from a line, never a big leap.
- Use the must-be-true test.
- Implied meaning → explain the idea behind the words.
- Assumption → hidden link between reason and conclusion.
- Prediction/application → apply the passage's rule to the new case.
- Reject: word-for-word copies, outside facts, extreme words, invented motives.
""",
"patterns": [
 P("rc-p14", "'It can be inferred from the passage that…'", "very common",
   "Stem uses infer, imply, suggest, 'most probably', or 'it can be concluded'.",
   "1. Find the line the question is about.\n2. Take ONE logical step from that line.\n3. Apply the must-be-true test to each option.\n4. Reject copies, extremes, and outside facts.",
   "\"The shop is crowded every morning since the government moved its forms online.\" What can be inferred?\n(a) Many people need help filling online forms (b) The government has closed all offices (c) The shop sells food (d) People dislike computers",
   "Crowd began when forms went online → people come for help with online forms. (b) is extreme, (c) unsupported, (d) contradicts (they come to use computers). Answer: **(a)**."),
 P("rc-p15", "Implied meaning of a quoted line", "common",
   "'What does the author mean by…?', 'The statement \"…\" implies that…'.",
   "1. Read the quoted line and the sentence around it.\n2. Ask what idea the line expresses (often figurative).\n3. Choose the option that explains the idea, not one that reads the words literally.",
   "\"Earlier, extra sunshine meant extra pumping. Now it means extra money.\" What is implied?",
   "Earlier, spare solar power was used to pump more water; now the farmer sells spare power. So: **surplus power now earns money instead of being spent on pumping**."),
 P("rc-p16", "Assumption behind a statement", "occasional",
   "'The author assumes that…', 'The statement is based on the assumption that…'.",
   "1. Separate reason and conclusion.\n2. Find the unstated link that makes the reason lead to the conclusion.\n3. Negate the option: if the argument breaks, it is the assumption.",
   "\"The road will reduce travel time, so traders will earn more.\" What is assumed?",
   "Link needed: saving travel time helps traders earn more (for example, they can sell more or reach markets sooner). If time saved did not matter to earnings, the conclusion would fail. Answer: **traders' earnings depend partly on travel time**."),
 P("rc-p17", "Prediction or application (most likely / most similar)", "occasional",
   "'If … happens, which is most likely?', 'Which of the following situations is most similar to…?'",
   "1. Write the passage's rule in one line.\n2. Apply it to the new case.\n3. The answer follows the same rule; reject options that need extra facts or go to extremes.",
   "Passage: volunteers collect untouched wedding food and give it to shelters. Most similar: (a) a shop raising prices (b) a bakery giving unsold bread to an orphanage (c) a family cooking less (d) a hotel adding new dishes",
   "Rule: surplus food is collected and given to people in need. Only (b) follows it. Answer: **(b)**."),
]}

S["rc-vocab-context"] = {
"notes": r"""### What is vocabulary in context?
These questions give a word or phrase **from the passage** and ask its meaning *as used in the passage*. Many English words have more than one meaning. The passage decides which meaning is right.

Example: the word **bank**.
- *She deposited money in the bank.* → a place for money.
- *They sat on the bank of the river.* → the side of a river.
Both meanings are correct English, but only one fits each sentence.

### The plug-in test (use it every time)
1. Read the full sentence that contains the word.
2. Cover the word and think of your own simple word that fits.
3. Put each option in place of the word.
4. The right option keeps the sentence's meaning, grammar and tone.

Worked example: *"Buyers from three districts **haggled** cheerfully over prices."*
- Your own word: *bargained*.
- "quarrelled violently" — does not fit *cheerfully*. ✘
- "bargained" — fits perfectly. ✔

### Question types
1. **Synonym in context** — closest meaning.
2. **Antonym in context** — most nearly opposite. First find the meaning in the sentence, then take its opposite **once**.
   - *"It was a **modest** victory"* → modest = small → opposite = huge/sweeping. Not "proud" (that is the opposite of the *other* meaning of modest, "humble").
3. **Phrase or idiom meaning** — e.g. *did not take it lying down* = refused to accept without a fight; *cut corners* = skipped necessary steps to save time or money. Treat the phrase as one unit.
4. **Multiple-meaning word** — the setter picks a word whose common meaning is a trap: *shelved* (postponed, not put on a shelf), *craft* (skill, not a boat), *toll* (loss/damage, not a road tax).

### Keep the part of speech
If the word is a verb in the passage, the answer must work as a verb in that sentence. *"The board **shelved** the plan"* — *shelved* is a past-tense verb, so "postponed" fits; "a shelf" (noun) cannot.

### Watch the tone
Positive, negative or neutral? *"The traders **celebrated**"* is positive; an option like "mourned" breaks the tone even if you are unsure of meanings.

### Common multiple-meaning words in exam passages
| Word | Everyday meaning | Other meaning often used |
|---|---|---|
| shelve | put on a shelf | postpone, set aside |
| craft | handmade object / boat | skill, profession |
| toll | road tax | damage, loss of life |
| frank | — | honest, open |
| check | examine | stop, control ("check the spread") |
| sound | noise | healthy, reliable ("sound advice") |
| grave | burial place | serious ("a grave mistake") |
| novel | story book | new, original ("a novel idea") |
| bear | animal | tolerate / carry |
| fine | good | penalty; very thin |

### Speed tip
Vocabulary questions need only one sentence. Do them **first** in the RC set — 20 seconds each.

### Quick revision
- Meaning comes from the sentence, not from the dictionary's first meaning.
- Plug-in test: your own word first, then options.
- Antonym: find meaning in context, then flip once.
- Idioms/phrases: read as one unit; literal options are traps.
- Keep part of speech and tone.
- Do vocab questions first.
""",
"patterns": [
 P("rc-p18", "Synonym in context (closest meaning)", "very common",
   "'Which word is closest in meaning to X as used in the passage?', 'X most nearly means…'.",
   "1. Read the sentence with the word.\n2. Think of your own replacement word.\n3. Plug in each option; keep meaning, grammar and tone.\n4. Choose the option that works in the sentence, even if another option is a more common meaning.",
   "\"When the board finally **unveiled** its plan for a mall…\" Closest meaning: (a) hid (b) made public (c) cancelled (d) painted",
   "The board showed the plan to the public for the first time. Own word: *announced*. Answer: **(b) made public**."),
 P("rc-p19", "Antonym in context (most nearly opposite)", "common",
   "'Which word is most nearly OPPOSITE in meaning to X as used in the passage?'",
   "1. Find the word's meaning in the sentence first.\n2. Take the opposite of THAT meaning — only once.\n3. Reject options that are synonyms (setters include one) or opposites of a different meaning.",
   "\"Scientists are **frank** about the limits of their craft.\" Opposite: (a) honest (b) evasive (c) open (d) direct",
   "Frank = honest and open. Opposite = avoiding the truth. (a), (c), (d) are synonyms. Answer: **(b) evasive**."),
 P("rc-p20", "Meaning of a phrase or idiom in the passage", "common",
   "A quoted phrase: 'The phrase \"…\" means…', 'What does the author mean by \"…\"?'",
   "1. Treat the phrase as one unit.\n2. Use the sentence before and after to see what happened.\n3. Reject literal word-by-word options.",
   "\"Officials under pressure are tempted to **cut corners**.\" Meaning?",
   "Context: codes cost money; officials want quick results. So *cut corners* = **save time or money by skipping necessary steps** — not literally cutting anything."),
 P("rc-p21", "Multiple-meaning word (which sense is used?)", "common",
   "A familiar word whose everyday meaning is an option (shelved, craft, toll, check, sound).",
   "1. Assume the common meaning is a trap.\n2. Plug in each meaning; only one keeps the sentence sensible.\n3. Confirm part of speech.",
   "\"The board **shelved** the plan and repaired the roof instead.\" Shelved means: (a) arranged on shelves (b) put aside (c) sold (d) announced",
   "A plan cannot be placed on a shelf; the board dropped it for now. Answer: **(b) put aside**."),
]}

S["rc-tone-attitude"] = {
"notes": r"""### What is tone?
**Tone** is the author's feeling or manner in writing — the *voice* behind the words. The same fact can be written in different tones:
- Neutral: "The lake has become polluted."
- Critical: "Despite crores spent on brochures, the lake is still a sewer."
- Hopeful: "With a few drains, the lake can be clean again."

**Attitude** is the author's feeling towards one particular thing in the passage (a plan, a group, an idea).

### Where tone hides
Tone is carried by **describing words** (adjectives and adverbs) and by **contrast words**.
- *glossy brochures, grand plan, the cameras leave* → mocking the show.
- *"Surely a city that can spend crores on brochures can find money for a drain"* → sarcasm (saying something to point out a failure).
- *however, yet, but* → the part after it shows what the author really thinks.

### Common tone words and their meanings
| Tone word | Meaning | Sign in the passage |
|---|---|---|
| informative / objective / neutral | only gives facts | no praise, no blame |
| analytical | examines causes and effects | "because", "as a result", weighs points |
| critical | points out faults | *fails, merely, despite promises* |
| sarcastic / ironic | mocks by saying the opposite or exaggerating | *Surely…, what a grand plan* |
| appreciative / laudatory | praises | *remarkable, a model, succeeded* |
| optimistic / hopeful | expects good results | *can, will improve, promising* |
| pessimistic | expects bad results | *hopeless, bound to fail* |
| balanced | gives both sides fairly | *neither… nor, on one hand… on the other* |
| nostalgic | fondly remembers the past | *those were the days* |
| cautionary | warns | *risk, danger, before we…* |
| indifferent | does not care | rarely correct — authors write because they care |

### Method
1. Underline one evaluative phrase in each paragraph.
2. Is it positive, negative, or neutral? How strong?
3. Check the **last sentence** — it usually shows the final attitude.
4. Pick the tone word that matches both *direction* (positive/negative) and *strength* (mild/strong).

### Degree matters
If the author says online classes are "neither the saviour nor the failure" — the tone is **balanced**, not "angry" and not "celebratory". Extreme tone words (*furious, euphoric, hostile*) are usually wrong in exam passages.

### Serious topic ≠ emotional tone
A science passage about germs or earthquakes is still **informative** if it just explains. Do not call it "alarmed" because the subject is scary.

### "Author would agree" questions
These are inference questions about the author's opinion. The correct option matches what the author says **and** how strongly. If the author wants "sewage stopped before ceremonies", he would agree that *stopping sewage matters more than publicity* — not that "the lake can never be cleaned".

### "The passage is most likely taken from…"
Match style to source:
- facts + explanations, no opinion → science book / textbook / encyclopaedia
- opinion on a current issue with suggestions → newspaper editorial / opinion piece
- personal feelings in first person, dates → diary / memoir
- story with characters and dialogue → short story
- selling words (best, buy now) → advertisement

### Quick revision
- Tone = author's voice; attitude = feeling towards one thing.
- Look at adjectives, adverbs and what comes after *however/yet/but*.
- Match direction AND degree; avoid extreme tone words.
- Serious subject can still have a neutral tone.
- Quoted people's feelings are not the author's tone.
- Source questions: match the writing style to the type of text.
""",
"patterns": [
 P("rc-p22", "Tone of the passage", "common",
   "'The tone of the passage is…', 'Which word best describes the author's tone?'",
   "1. Collect the evaluative words (adjectives, adverbs, 'surely', 'merely').\n2. Decide direction (positive / negative / neutral) and strength.\n3. Confirm with the closing sentence.\n4. Reject extremes and tone words that fit only one line.",
   "\"The new bridge, built in record time and under budget, has cut the travel time of thousands of commuters.\" Tone: (a) critical (b) appreciative (c) sarcastic (d) indifferent",
   "'Record time', 'under budget', 'cut travel time' are praise. No mockery. Answer: **(b) appreciative**."),
 P("rc-p23", "Author's attitude towards a specific thing", "common",
   "'The author's attitude towards X is…', 'How does the author view…?'",
   "1. Find every line that mentions X.\n2. Note the words used with X (praise, doubt, blame).\n3. Summarise in one phrase and match; reject one-sided options if the author gives both sides.",
   "\"Online classes were a lifeline for children with laptops, and a blank screen for children without them.\" Attitude towards online classes?",
   "Positive for some, useless for others → the author sees them as **useful but dependent on access** — neither fully good nor fully bad."),
 P("rc-p24", "Author would agree / disagree with…", "common",
   "'With which statement would the author most likely agree?'",
   "1. Recall the author's main opinion (usually in the last lines).\n2. Pick the option that follows from it at the same strength.\n3. Reject options that are extreme, opposite, or about something the author never discussed.",
   "Author: \"Brochures are printed every year, but the sewage pipes are never diverted.\" The author would agree that:\n(a) brochures clean lakes (b) fixing sewage matters more than publicity (c) the lake cannot be saved (d) sewage is harmless",
   "The author criticises show without action. Answer: **(b)**."),
 P("rc-p25", "Type or source of the passage", "occasional",
   "'The passage is most likely taken from…', 'The passage is an example of…'.",
   "1. Is it facts only (textbook), opinion with suggestions (editorial), a story (fiction), personal feelings (diary), or selling (advertisement)?\n2. Match that style with the option.",
   "\"Honey resists decay because it has little water, is slightly acidic and contains an enzyme that produces hydrogen peroxide.\" Source?",
   "Only facts and explanation, no opinion or selling → **a science book or article**."),
]}

apply_subtopics(data, S)

# ---------------------------------------------------------------- passages + practice
QS = []
sub = "rc-reading-strategy"
PS1 = """For most of the last century, rice and wheat pushed millets off Indian plates. Government buying, cheap ration-shop grain and the prestige attached to 'white' cereals made coarse grains look like food for the poor. Farmers followed the market, and the area under jowar, bajra and ragi shrank steadily.

Millets, however, carry advantages that matter more today than they did fifty years ago. Most varieties need a fraction of the water that paddy demands and can survive on rain alone, which makes them a natural fit for dry districts where groundwater is falling. They are rich in fibre and minerals, and their slow release of sugar suits a population in which diabetes is rising.

Reviving them is not simply a matter of telling people to eat better. A farmer in Karnataka who switched part of her land to ragi found that the nearest mill was forty kilometres away and that traders offered her less than the support price. Unless processing units, storage and assured buying reach the villages, the campaign for millets will remain a slogan in city supermarkets rather than a change in what farmers grow."""
QS += [
 QA("rc-reading-strategy-p01", sub, "rc-p2", "What is the main purpose of the second paragraph?",
    ["To show that millets suit present-day problems of water shortage and health", "To explain why millets lost their place in Indian diets", "To describe the difficulties farmers face in selling millets", "To prove that rice and wheat are harmful to health"],
    "Paragraph 2 opens with 'Millets, however, carry advantages that matter more today' and then gives two: low water need (dry districts) and health benefits (fibre, slow sugar release, diabetes). 'Why millets lost their place' is the job of paragraph 1, and 'difficulties in selling' is paragraph 3. The passage never says rice or wheat is harmful.",
    "Paragraph map: P1 = decline, P2 = advantages today, P3 = obstacles. The question names P2 → advantages.", "easy", 40, PS1, "rc-g-strat1"),
 QA("rc-reading-strategy-p02", sub, "rc-p3", "Why does the author mention the farmer in Karnataka?",
    ["To illustrate that without mills and assured buying, growing millets does not pay the farmer", "To show that ragi grows well only in Karnataka", "To prove that traders always cheat farmers", "To suggest that farmers should stop growing ragi"],
    "The sentence before the example says revival is 'not simply a matter of telling people to eat better', and the sentence after says processing units, storage and assured buying must reach villages. The farmer's story (distant mill, low price) illustrates exactly this obstacle. 'Only in Karnataka' and 'always cheat' are extreme and unsupported, and the author wants more millets grown, not less.",
    "An example supports the claim next to it. Read one sentence before and after the example.", "medium", 45, group="rc-g-strat1"),
 QA("rc-reading-strategy-p03", sub, "rc-p1", "Which of the following statements is/are true according to the passage?\n\nI. Most millet varieties can be grown with rainfall alone.\nII. The area under millets increased during the last century.\nIII. Traders offered the Karnataka farmer less than the support price.",
    ["Only I", "Only I and III", "Only II and III", "All of I, II and III"],
    "I — True: 'Most varieties … can survive on rain alone.'\nII — False: the area under millets 'shrank steadily'.\nIII — True: traders 'offered her less than the support price'.\nSo only I and III are true.",
    "Once you see II is false, cut every option containing II — only 'Only I' and 'Only I and III' remain; III is clearly stated.", "medium", 50, group="rc-g-strat1", answer=1),
 QA("rc-reading-strategy-p04", sub, "rc-p4", "Which of the following best describes how the passage is organised?",
    ["A past decline is described, present-day advantages are given, and a practical obstacle to revival is pointed out", "A problem is stated, its causes are listed, and no solution is offered", "Two opposing views are presented and the author refuses to choose between them", "A personal story is told first and general facts follow"],
    "Map: P1 — millets declined in the last century; P2 — their advantages today; P3 — the obstacle (no mills, low prices) and what is needed. The second option fails because P2 is about advantages, not causes, and P3 does suggest what is needed. There are no two opposing views, and the personal story comes last, not first.",
    "Check every part of an organisation option against your paragraph map, in order. One wrong part kills it.", "medium", 45, group="rc-g-strat1"),
]
PS2 = """Five years ago, a vegetable seller in a small town would have laughed at the idea of accepting payment through a phone. Today a printed QR code hangs from almost every cart, and many sellers say they no longer keep much change. The shift was driven by cheap smartphones, low-cost mobile data and a payment system that charges the small user nothing.

The benefits are easy to see. Money moves instantly, records are kept automatically, and a seller with a digital history of sales finds it easier to get a small loan from a bank. Shops no longer lose customers because they cannot break a ₹500 note.

Yet the change has left some people behind. Many older citizens, especially those who live alone, find the screens confusing and fear pressing the wrong button. Fraudsters have noticed this. Calls from fake 'bank officers' asking for a PIN have become common, and a single mistake can empty a pension account. Digital payments will be truly universal only when banks teach simple safety habits as actively as they advertise the convenience."""
QS += [
 QA("rc-reading-strategy-p05", sub, "rc-p5", "The passage provides an answer to which of the following questions?",
    ["Why do small sellers now find it easier to get bank loans?", "How much money do fraudsters steal from pension accounts each year?", "Which bank first introduced QR code payments?", "How many vegetable sellers in India use smartphones?"],
    "Paragraph 2 says 'a seller with a digital history of sales finds it easier to get a small loan'. So the loan question is answered. The passage gives no amount stolen, names no bank, and gives no count of sellers.",
    "Options asking for exact numbers, names or years are usually unanswerable — check them first and cut them.", "easy", 40, PS2, "rc-g-strat2"),
 QA("rc-reading-strategy-p06", sub, "rc-p1", "Which of the following is/are stated in the passage?\n\nI. The payment system charges small users nothing.\nII. Older citizens living alone are the only victims of fraud.\nIII. Many sellers say they no longer keep much change.",
    ["Only I", "Only II", "Only I and III", "Only II and III"],
    "I — stated: 'a payment system that charges the small user nothing'.\nII — not stated: the passage says older citizens are targeted, but 'the only victims' is an extreme claim it never makes.\nIII — stated: 'many sellers say they no longer keep much change'.\nAnswer: only I and III.",
    "The word 'only' in statement II is the red flag — the passage never limits fraud to one group.", "medium", 50, group="rc-g-strat2", answer=2),
 QA("rc-reading-strategy-p07", sub, "rc-p2", "The third paragraph mainly:",
    ["points out a group that has been left behind by the change and a danger it faces", "praises banks for teaching safety habits to older people", "explains how QR codes work", "argues that digital payments should be stopped for older people"],
    "Paragraph 3 begins 'Yet the change has left some people behind' and describes older citizens and the fraud risk. It says banks *should* teach safety habits — it does not praise them for already doing so. QR codes are not explained, and the author wants payments to become universal, not stopped.",
    "'Yet' at the start of a paragraph = a turn to the downside. The paragraph's job is the problem that follows.", "easy", 40, group="rc-g-strat2"),
 QA("rc-reading-strategy-p08", sub, "rc-p3", "Why does the author mention a ₹500 note?",
    ["To give an example of how digital payment removes the problem of giving change", "To show that prices in small towns have risen sharply", "To warn readers about fake currency notes", "To show that most customers carry only large notes"],
    "The ₹500 note appears in the paragraph on benefits: shops 'no longer lose customers because they cannot break a ₹500 note'. It illustrates the benefit that digital payment ends the need for change. Prices, fake notes and 'most customers' are never discussed.",
    "Ask which point the example supports — here, the list of benefits in paragraph 2.", "medium", 40, group="rc-g-strat2"),
]
PS3 = """Farmers in parts of Himachal Pradesh have begun renting beehives each spring. They place the boxes among their apple trees for a few weeks and return them after the flowers fade. The reason is simple: the wild bees that once did this work free of charge have become scarce.

Scientists point to several causes. Heavy use of pesticides kills bees directly, and orchards planted with a single crop leave few wild flowers to feed them once the fruit blossom is over. Warmer winters also disturb the match between flowering time and the insects' active season.

Renting hives helps, but it is costly, and the hired bees do not reach every orchard. Some villages have tried a cheaper approach: they leave strips of wild flowers along field edges and spray only in the evening, when bees are resting. Early results suggest that such steps bring wild pollinators back within a few seasons. The lesson is that nature's free services are free only as long as we protect them."""
QS += [
 QA("rc-reading-strategy-p09", sub, "rc-p4", "Which of the following best describes the structure of the passage?",
    ["A new practice is described, the reasons behind it are explained, and a cheaper remedy is suggested", "A scientific theory is stated and then rejected", "Two farming methods are compared and the older one is declared better", "A list of pesticides is given along with their effects"],
    "P1: farmers now rent beehives (new practice) because wild bees are scarce. P2: causes of the decline. P3: renting is costly; a cheaper approach (flower strips, evening spraying) is suggested. No theory is rejected, no older method is declared better, and no pesticides are named.",
    "Paragraph map in order → practice / causes / cheaper fix. Only one option follows that order.", "medium", 45, PS3, "rc-g-strat3"),
 QA("rc-reading-strategy-p10", sub, "rc-p5", "Which of the following questions can be answered from the passage?",
    ["Why do some villages spray pesticides only in the evening?", "How much does it cost to rent one beehive?", "Which apple variety needs the most bees?", "In which year did wild bees start declining?"],
    "The passage says villages spray 'only in the evening, when bees are resting' — that answers the 'why'. It calls renting 'costly' but gives no figure, names no apple variety, and gives no year.",
    "'Costly' is not a cost figure — questions asking 'how much' need a number in the passage.", "easy", 40, group="rc-g-strat3"),
 QA("rc-reading-strategy-p11", sub, "rc-p1", "Which of the following statements is/are true according to the passage?\n\nI. Pesticides are one reason for the decline of wild bees.\nII. Renting beehives is costly.\nIII. Single-crop orchards provide wild flowers for bees all year round.",
    ["Only I", "Only I and II", "Only II and III", "All of I, II and III"],
    "I — True: 'Heavy use of pesticides kills bees directly.'\nII — True: 'Renting hives helps, but it is costly.'\nIII — False: single-crop orchards 'leave few wild flowers' after the blossom — the opposite.\nAnswer: only I and II.",
    "III reverses the passage. Cut every option with III; between the two left, II is plainly stated.", "medium", 50, group="rc-g-strat3", answer=1),
 QA("rc-reading-strategy-p12", sub, "rc-p2", "What role does the second paragraph play in the passage?",
    ["It gives the causes behind the problem introduced in the first paragraph", "It describes the solution tried by some villages", "It questions whether wild bees are really scarce", "It explains how beehives are rented and returned"],
    "Paragraph 1 introduces the problem (wild bees are scarce). Paragraph 2 opens 'Scientists point to several causes' and lists pesticides, single-crop orchards and warmer winters. The villages' solution is in paragraph 3; renting is described in paragraph 1; nobody doubts the scarcity.",
    "The first sentence of a paragraph usually names its job: 'several causes'.", "easy", 35, group="rc-g-strat3"),
]

sub = "rc-main-idea"
PM1 = """A generation ago, a broken radio in an Indian home went to the repair shop at the corner, and a torn shirt went back to the tailor. Today many products are designed so that they cannot be opened without breaking them, spare parts are hard to find, and a repair often costs almost as much as a new item. So we throw things away.

This habit has a cost that the price tag hides. Every discarded phone or mixer adds to a growing pile of electronic waste, much of it handled by informal workers who burn wires to recover copper and breathe the fumes. Making a replacement also uses fresh metals, plastic and energy.

Some governments have started to push back. A few now require companies to sell spare parts for several years and to share repair manuals with independent shops. Such rules do not force anyone to repair, but they make repair a real choice again. The humble repairman, it turns out, may be as important to a clean future as the solar panel."""
QS += [
 QA("rc-main-idea-p01", sub, "rc-p6", "Which of the following best expresses the central idea of the passage?",
    ["Products that are hard to repair create hidden waste, and rules that make repair possible again can help", "Old radios were of better quality than modern phones", "Informal workers should be banned from handling electronic waste", "Solar panels are the most important part of a clean future"],
    "P1: products are now hard to repair, so we throw them away. P2: this creates hidden costs (e-waste, fumes, fresh resources). P3: rules on spare parts and manuals make repair a choice again. The first option joins all three. The quality of old radios is never compared; banning workers is never proposed; and the passage says the repairman may be *as* important as the solar panel — not that solar panels are the most important.",
    "Topic from P1 + author's point from the last paragraph = main idea.", "medium", 45, PM1, "rc-g-main1"),
 QA("rc-main-idea-p02", sub, "rc-p7", "Which of the following is the most suitable title for the passage?",
    ["Bringing Repair Back: A Quiet Step Towards Less Waste", "The Life of an Indian Tailor", "How Copper Is Recovered from Wires", "Why Solar Energy Is Cheaper Than Coal"],
    "The passage is about the loss of repair culture, its waste cost and rules that revive repair. The first title covers both the action (bringing repair back) and the benefit (less waste). The tailor is a one-line example, copper recovery is one detail of P2, and solar vs coal costs are never discussed.",
    "Reject titles built on one example or one detail — a title must cover every paragraph.", "easy", 35, group="rc-g-main1"),
 QA("rc-main-idea-p03", sub, "rc-p9", "The second paragraph is mainly about:",
    ["the hidden environmental and health costs of throwing things away", "the rules made by governments to support repair", "the high price of new phones and mixers", "the skills of repair-shop owners"],
    "P2 begins 'This habit has a cost that the price tag hides' and lists e-waste, fumes breathed by workers, and fresh resources used for replacements. Government rules are P3. Prices of new items and repairmen's skills are not the subject of P2.",
    "The topic sentence ('a cost that the price tag hides') names the paragraph's point.", "easy", 35, group="rc-g-main1"),
]
PM2 = """Parents often wait for school to teach their children to read. Yet research on early learning keeps pointing to what happens before school begins. Children who are read to at home, even for fifteen minutes a day, arrive in class knowing more words, listening for longer and treating books as a pleasure rather than a task.

The effect does not depend on expensive books or educated parents. A grandmother telling a folk tale in Bhojpuri, a father reading the Sunday newspaper aloud, an older sister acting out a story with funny voices — each gives the child the same things: new words, the rhythm of sentences and the habit of paying attention.

Busy families may feel they have no time to spare. But fifteen minutes is shorter than most television serials. If every home set aside that small window each evening, schools would receive children who are ready not just to read, but to want to read."""
QS += [
 QA("rc-main-idea-p04", sub, "rc-p8", "The author's main purpose in writing the passage is to:",
    ["encourage families to read or tell stories to young children every day", "criticise schools for failing to teach reading", "compare the quality of television serials with books", "prove that educated parents raise better readers"],
    "The author explains the benefit of daily reading at home, says any family member can do it, and ends by urging homes to 'set aside that small window each evening'. That is encouragement. Schools are not criticised; TV serials are only a time comparison; and P2 says the effect does NOT depend on educated parents.",
    "Look at how the passage ends — 'If every home set aside…' is a call to action ⇒ purpose = encourage.", "easy", 40, PM2, "rc-g-main2"),
 QA("rc-main-idea-p05", sub, "rc-p6", "The central idea of the passage is that:",
    ["a short daily habit of reading or storytelling at home prepares children to learn and enjoy reading", "only expensive picture books help children learn new words", "grandmothers are better storytellers than parents", "children should watch less television and read more newspapers"],
    "Every paragraph supports one point: fifteen minutes of reading/storytelling at home (P1), by anyone and without cost (P2), prepares children to read and want to read (P3). 'Only expensive books' contradicts P2; grandmothers are one example, not compared with parents; newspapers are an example and TV is only a time comparison.",
    "Main idea must be supported by all paragraphs — here the '15 minutes at home' idea appears in P1 and P3 and is widened in P2.", "medium", 45, group="rc-g-main2"),
 QA("rc-main-idea-p06", sub, "rc-p9", "What is the main point of the second paragraph?",
    ["Any family member, in any language, can give a child the benefits of stories", "Reading aloud helps only when parents are highly educated", "Folk tales are more useful than newspapers", "Children learn best from their older sisters"],
    "P2's topic sentence: 'The effect does not depend on expensive books or educated parents.' The three examples (grandmother in Bhojpuri, father with a newspaper, sister acting a story) all give 'the same things'. So anyone, in any language, can help. The second option reverses the topic sentence; the last two pick one example and rank it, which the passage never does.",
    "When a paragraph lists several examples that 'all give the same things', its point is what they share.", "medium", 40, group="rc-g-main2"),
]
PM3 = """Indian cities spend large sums on flyovers, yet the most common journey in any city begins and ends on foot. Even people who drive walk to the parking spot, and bus and metro users walk at both ends of every trip. Despite this, footpaths are often broken, blocked by parked vehicles or taken over by shops, forcing walkers onto the road beside fast traffic.

The result is dangerous. Pedestrians form a large share of those killed on Indian roads, and the elderly, children and people with disabilities suffer the most. Poor footpaths also push people who could walk into cars and two-wheelers, which adds to the very traffic the flyovers were built to ease.

Good walking space is cheap compared with a flyover. A level, continuous footpath with shade, lighting and safe crossings can be built across an entire neighbourhood for the cost of a few hundred metres of elevated road. A city that wants fewer cars should begin by respecting the people who are not in one."""
QS += [
 QA("rc-main-idea-p07", sub, "rc-p7", "Which title best suits the passage?",
    ["Walking Matters: Why Cities Must Fix Their Footpaths", "Flyovers: The Only Answer to City Traffic", "A History of Road Accidents in India", "How Metro Rail Changed Indian Cities"],
    "The passage argues that walking is the most common journey, that poor footpaths are dangerous and add to traffic, and that good footpaths are cheap. The first title covers all of this. The second reverses the author's view, the third is too broad (and the passage gives no history), and metro rail is only mentioned in passing.",
    "Two-part colon titles fit argument passages: topic + the author's demand.", "easy", 35, PM3, "rc-g-main3"),
 QA("rc-main-idea-p08", sub, "rc-p8", "The passage has been written mainly to:",
    ["argue that cities should give walkers safe, continuous footpaths", "demand that all flyovers be demolished", "report the exact number of people killed on Indian roads", "explain how a flyover is constructed"],
    "The author builds a case (walking is common, neglect is dangerous, fixes are cheap) and ends with 'should begin by respecting the people who are not in one' — an argument for better footpaths. The passage never asks for flyovers to be demolished, gives no exact death count ('a large share' only), and does not explain construction.",
    "'should' in the last line = the author is arguing for something. Purpose = argue/persuade.", "medium", 40, group="rc-g-main3"),
 QA("rc-main-idea-p09", sub, "rc-p6", "Which of the following sums up the passage best?",
    ["Neglecting footpaths endangers walkers and worsens traffic, while fixing them is cheap and effective", "Pedestrians cause most road accidents by walking on the road", "Shops should be removed from all city roads", "Metro users walk more than car owners do"],
    "The summary must hold P1 (walking is common but footpaths are neglected), P2 (danger + more traffic) and P3 (fixing is cheap). Only the first option has all three. The second blames pedestrians, which the passage never does — they are *forced* onto the road. The third is too narrow and extreme; the fourth is a comparison the passage does not make.",
    "Summary = one clause per paragraph joined together. Count the paragraphs your option covers.", "hard", 45, group="rc-g-main3"),
]

sub = "rc-detail-fact"
PD1 = """Long before piped water reached the towns of Gujarat and Rajasthan, people built stepwells. A stepwell is a deep pit lined with stone, with flights of steps leading down to the water. As the level fell during the dry months, people simply walked further down to reach it. Many stepwells had shaded platforms at each level, and because the air near the water stayed cool, travellers rested there during the hottest hours of the day.

The wells were more than water tanks. Rich merchants and queens paid for the finest of them and decorated the walls with carvings of gods, dancers and animals, so that fetching water became a visit to a public space. Women, who did most of the water carrying, met and talked there.

Most stepwells fell into disuse in the twentieth century. Hand pumps and taps made them unnecessary, and many were filled with rubbish. In recent years a few towns have cleaned their old wells and found that they still collect rainwater well enough to raise the water level in nearby borewells."""
QS += [
 QA("rc-detail-fact-p01", sub, "rc-p10", "According to the passage, what did people do when the water level in a stepwell fell?",
    ["They walked further down the steps to reach the water", "They dug a new well nearby", "They waited for the monsoon before drawing water", "They carried water from the nearest town"],
    "Paragraph 1: 'As the level fell during the dry months, people simply walked further down to reach it.' None of the other actions is mentioned.",
    "Keyword 'level fell' → the same sentence gives the answer.", "easy", 30, PD1, "rc-g-det1"),
 QA("rc-detail-fact-p02", sub, "rc-p11", "Why did travellers rest in stepwells during the hottest hours of the day?",
    ["Because the air near the water stayed cool", "Because food was sold on the platforms", "Because the carvings were pleasant to look at", "Because the towns had no other buildings"],
    "The reason is given with 'because': 'because the air near the water stayed cool, travellers rested there during the hottest hours'. Food is never mentioned; carvings are described in another paragraph and are not given as the reason; the last option is invented.",
    "Why-question → find 'because' near the keyword 'travellers'.", "easy", 30, group="rc-g-det1"),
 QA("rc-detail-fact-p03", sub, "rc-p12", "Which of the following is NOT mentioned in the passage as a feature of stepwells?",
    ["Wooden roofs covering the whole well", "Flights of steps leading down to the water", "Carvings of gods, dancers and animals", "Shaded platforms at each level"],
    "Steps, carvings and shaded platforms are all described. Wooden roofs are never mentioned, so that is the answer.",
    "NOT question: tick the three you can find; the leftover is the answer.", "easy", 35, group="rc-g-det1"),
 QA("rc-detail-fact-p04", sub, "rc-p13", "Which of the following statements is true according to the passage?",
    ["A few towns found that their cleaned wells still help raise the water level in nearby borewells", "All stepwells were paid for by queens", "Every old stepwell has now been cleaned", "Stepwells were used only by travellers"],
    "The last sentence says 'a few towns have cleaned their old wells and found that they still collect rainwater well enough to raise the water level in nearby borewells' — the first option matches. 'All … by queens' changes 'rich merchants and queens paid for the finest of them'. 'Every … cleaned' changes 'a few towns'. 'Only by travellers' ignores the women who fetched water.",
    "Three wrong options each change one qualifier: all, every, only. Qualifier words are the trap.", "medium", 45, group="rc-g-det1"),
]
PD2 = """When the women of Rampur formed a milk cooperative, only twelve households joined. Each morning they brought their milk to a single shed, where it was measured, tested for fat and poured into a shared cooling tank. Before this, a private trader had collected milk from their doorsteps, paid a fixed low price regardless of quality, and often delayed payment for weeks.

The cooperative changed three things. Payment was now linked to the fat content, so families that fed their animals well earned more. Money was paid every ten days, directly into bank accounts opened in the women's own names. And because the milk was cooled at once, less of it turned sour on the way to the dairy.

Within four years the membership had grown to over two hundred households. The members say the biggest change is not the extra income but the confidence: women who once stayed silent at village meetings now keep the cooperative's accounts and argue with officials about prices."""
QS += [
 QA("rc-detail-fact-p05", sub, "rc-p10", "How often did the cooperative pay its members?",
    ["Every ten days", "Every day", "Once a month", "After several weeks"],
    "Paragraph 2: 'Money was paid every ten days.' 'After several weeks' describes the old private trader, who 'often delayed payment for weeks' — a trap from a different part of the passage.",
    "Watch for details that belong to the OLD system (the trader) — they are placed as distractors.", "easy", 30, PD2, "rc-g-det2"),
 QA("rc-detail-fact-p06", sub, "rc-p11", "According to the passage, why did less milk turn sour after the cooperative was formed?",
    ["Because the milk was cooled immediately in a shared tank", "Because milk was collected from doorsteps", "Because families fed their animals better", "Because fewer households sold milk"],
    "'Because the milk was cooled at once, less of it turned sour on the way to the dairy.' Doorstep collection was the old system; feeding animals well is linked to higher fat and pay, not to souring; membership actually grew.",
    "The answer is the clause after 'because' in the same sentence as 'sour'.", "medium", 35, group="rc-g-det2"),
 QA("rc-detail-fact-p07", sub, "rc-p12", "The passage mentions all of the following as changes brought by the cooperative EXCEPT:",
    ["free cattle feed for member families", "payment linked to the fat content of milk", "payment into bank accounts in the women's own names", "immediate cooling of the milk"],
    "The three changes listed in paragraph 2 are fat-linked payment, payment every ten days into the women's own accounts, and immediate cooling. Free cattle feed is never mentioned — families that fed animals well earned more, but nobody gave them feed.",
    "EXCEPT: find the list ('changed three things') and tick; the unticked option is the answer.", "medium", 40, group="rc-g-det2"),
 QA("rc-detail-fact-p08", sub, "rc-p13", "Which of the following is correct according to the passage?",
    ["Membership grew from twelve to over two hundred households in about four years", "The cooperative began with over two hundred households", "The private trader paid more for milk with a higher fat content", "The members say the extra income is the biggest change"],
    "Paragraph 1 gives twelve households at the start; paragraph 3 says 'within four years the membership had grown to over two hundred'. The second option swaps the numbers; the third reverses the trader's 'fixed low price regardless of quality'; the fourth reverses 'the biggest change is not the extra income but the confidence'.",
    "For number options, check both the before and after figure; swapped figures are the commonest trap.", "hard", 45, group="rc-g-det2"),
]

sub = "rc-inference"
PI1 = """The small hill town had one bus a day to the district headquarters. It left at six in the morning and came back at seven in the evening, so anyone who needed to visit a government office lost a full day's wages for a task that might take twenty minutes. When the state began offering its certificates and forms online, the town's only cyber café suddenly had a queue outside it every morning.

The owner, a retired schoolteacher, charges ₹20 for filling a form and printing it. He says his busiest customers are elderly farmers applying for pensions and young people applying for jobs. 'Most of them have phones,' he says, 'but a small screen and a forty-page form do not go together.'"""
QS += [
 QA("rc-inference-p01", sub, "rc-p14", "It can be inferred from the passage that the online services became popular in the town mainly because:",
    ["they saved people a full day's trip to the district headquarters", "people enjoyed spending time at the cyber café", "the online forms were shorter than the paper forms", "the café owner was a retired schoolteacher"],
    "Stated: a visit to the government office cost a full day's wages because of the single bus. Stated: once forms went online, the café had a queue. One step: people could now finish the task in town and avoid the costly trip. Nothing suggests people enjoy the café for its own sake; the form is called 'forty-page', so it is not short; the owner's background does not explain the demand.",
    "Join two stated facts (costly trip + queue after online forms) — the link between them is the inference.", "medium", 45, PI1, "rc-g-inf1"),
 QA("rc-inference-p02", sub, "rc-p15", "What does the café owner imply when he says, 'a small screen and a forty-page form do not go together'?",
    ["Long forms are hard to fill on a phone, so people still need his computer and help", "Phones are too expensive for most people in the town", "The government should print forms on paper only", "Young people do not know how to use phones"],
    "He first says 'Most of them have phones' and then 'but…'. So owning a phone is not enough: a long form is difficult on a small screen, which is why they come to him. He says most customers DO have phones, so cost is not the issue; he makes no demand about paper forms; and he blames the screen size, not the users' skill.",
    "The clause after 'but' carries the speaker's point.", "medium", 40, group="rc-g-inf1"),
 QA("rc-inference-p03", sub, "rc-p16", "The statement that a visitor to a government office 'lost a full day's wages' assumes that:",
    ["the visitors would otherwise have been working and earning that day", "government offices pay visitors for their time", "the bus fare is equal to one day's wages", "government work always takes the whole day"],
    "Losing a day's wages only makes sense if the person would have earned money that day by working. That hidden link is the assumption. The passage says the task 'might take twenty minutes', which contradicts 'always takes the whole day'; the bus fare is never discussed; offices paying visitors is absurd and unsupported.",
    "Negation test: if the visitors would not have been working anyway, 'lost wages' collapses — so that is the assumption.", "hard", 50, group="rc-g-inf1"),
]
PI2 = """When Harish replaced his diesel pump with a solar one, his monthly fuel bill fell to zero. For the first time, he could water his fields in the afternoon without worrying about cost, and he did — often for longer than the crop needed. Two years later, the water in his borewell had dropped by several metres.

His neighbours noticed. Some of them have now joined a scheme under which farmers can sell spare solar electricity to the power company instead of using it to pump more water. Harish says the payment is small but steady. 'Earlier, extra sunshine meant extra pumping,' he says. 'Now it means extra money.'"""
QS += [
 QA("rc-inference-p04", sub, "rc-p14", "Which of the following can be inferred from the passage?",
    ["Free power encouraged Harish to pump more water than his crop needed", "Solar pumps always damage groundwater", "Harish's neighbours dislike solar pumps", "Diesel pumps are designed to use less water than solar pumps"],
    "Stated: fuel cost fell to zero, and he watered 'for longer than the crop needed'; later his borewell dropped. One step: the absence of cost led to over-pumping. 'Always damage' is extreme (the neighbours use solar pumps and sell power instead). Nothing says the neighbours dislike solar pumps. Pump design is not discussed — the diesel pump simply cost money to run.",
    "Reject 'always' at once; then pick the option that links two stated lines.", "medium", 45, PI2, "rc-g-inf2"),
 QA("rc-inference-p05", sub, "rc-p17", "If the scheme described in the second paragraph spreads widely, which of the following is most likely to happen?",
    ["Less groundwater will be pumped out, since spare power can earn money instead", "Farmers will stop growing crops altogether", "Power companies will stop buying electricity from farmers", "Diesel pumps will become popular again"],
    "The scheme lets farmers sell spare electricity 'instead of using it to pump more water'. If many farmers join, less extra pumping will happen, so less groundwater will be drawn. Nothing suggests farmers stop farming; the scheme is the power company buying electricity, so it stopping is the opposite; there is no reason to return to paid diesel.",
    "State the passage's rule (spare power → money, not pumping) and apply it to 'many farmers'.", "medium", 45, group="rc-g-inf2"),
 QA("rc-inference-p06", sub, "rc-p15", "What does Harish mean when he says, 'Now it means extra money'?",
    ["Surplus solar power is now sold instead of being spent on extra pumping", "He has started a business selling solar panels", "Sunny days make his crops fetch higher prices", "The power company pays him more than he earns from farming"],
    "The contrast is with 'Earlier, extra sunshine meant extra pumping'. Now the extra power is sold to the power company under the scheme. He sells electricity, not panels; crop prices are not discussed; and he calls the payment 'small but steady', so 'more than farming' is unsupported.",
    "Read the quoted line together with the line it contrasts with ('Earlier…').", "easy", 35, group="rc-g-inf2"),
]
PI3 = """At a large wedding in the city, caterers often cook for a hundred more guests than are invited, because running short of food is seen as a disgrace to the host family. Much of the extra food is thrown away by midnight.

A group of young volunteers now offers a simple service. Families call a helpline before the wedding, and a van arrives after dinner to collect untouched food, which is taken to night shelters within two hours. The volunteers insist on one rule: they will not accept food that has already been served on plates."""
QS += [
 QA("rc-inference-p07", sub, "rc-p16", "The caterers' practice of cooking for extra guests is based on the assumption that:",
    ["having leftover food is less embarrassing for the host than running out of food", "every invited guest will bring extra people", "night shelters will take all the extra food", "guests prefer to eat after midnight"],
    "They cook extra 'because running short of food is seen as a disgrace'. For this to make sense, wasting food must be seen as the lesser problem — that is the hidden assumption. Nothing says guests bring others; the shelters come in only with the volunteers' later service; eating after midnight is invented.",
    "Assumption = the unstated belief that makes the reason ('shortage is a disgrace') lead to the action (cook extra).", "hard", 50, PI3, "rc-g-inf3"),
 QA("rc-inference-p08", sub, "rc-p14", "It can be inferred that the volunteers refuse food that has already been served on plates most probably because:",
    ["such food may not be safe or hygienic to give to others", "plates are too heavy to carry in the van", "the host family wants to keep that food", "night shelters accept only sweets"],
    "The volunteers collect only 'untouched food' for night shelters within two hours. Food already served on someone's plate may be half-eaten or unclean, so the natural inference is a concern for safety and hygiene. The other reasons have no support in the passage.",
    "The word 'untouched' in the previous sentence is the clue.", "medium", 40, group="rc-g-inf3"),
 QA("rc-inference-p09", sub, "rc-p17", "Which of the following situations is most similar to the volunteers' service?",
    ["A bakery giving its unsold bread at closing time to a children's home", "A shop raising prices during a festival", "A family cooking less food for a small party", "A school collecting fees in advance"],
    "The service collects surplus food that would be wasted and gives it to people in need. The bakery does the same thing with unsold bread. Cooking less food reduces waste in a different way (prevention, not redistribution); the other two have nothing to do with surplus food.",
    "Write the rule: 'surplus food → people in need'. Only one option follows both halves.", "easy", 35, group="rc-g-inf3"),
]

sub = "rc-vocab-context"
PV1 = """The old market on the riverbank had seen better days. Its roof leaked, its lanes were narrow, and the municipal board had twice proposed pulling it down. Yet every Sunday the place came alive. Farmers arrived before dawn with baskets of greens, potters spread their wares on the ground, and buyers from three districts haggled cheerfully over prices.

When the board finally unveiled a plan for a shiny new mall on the site, the traders did not take it lying down. They collected signatures, met the local legislator and argued that the market fed hundreds of families. The board, keen to avoid a public row, shelved the plan and instead agreed to repair the roof. It was a modest victory, but the traders celebrated it as if they had won a war."""
QS += [
 QA("rc-vocab-context-p01", sub, "rc-p18", "Which word is closest in meaning to **haggled** as used in the passage?",
    ["bargained", "quarrelled violently", "complained", "gossiped"],
    "Buyers 'haggled cheerfully over prices' — they argued about the price in a friendly way to get a better deal, i.e. bargained. 'Quarrelled violently' clashes with 'cheerfully'; complaining and gossiping are not about fixing a price.",
    "Plug in: 'buyers bargained cheerfully over prices' — perfect fit.", "easy", 25, PV1, "rc-g-voc1"),
 QA("rc-vocab-context-p02", sub, "rc-p20", "The phrase **did not take it lying down** means that the traders:",
    ["refused to accept the plan without a fight", "were too tired to respond", "stood outside the board office all night", "agreed quietly to move elsewhere"],
    "The next sentence shows what they did: collected signatures, met the legislator and argued their case. So they resisted instead of accepting the plan quietly. The idiom has nothing to do with lying down literally.",
    "Idiom → read what the people did next; the actions define the phrase.", "easy", 30, group="rc-g-voc1"),
 QA("rc-vocab-context-p03", sub, "rc-p21", "In the passage, the word **shelved** means:",
    ["put aside for the time being", "arranged neatly on shelves", "sold to a private buyer", "announced publicly"],
    "The board 'shelved the plan and instead agreed to repair the roof' — it dropped or postponed the mall plan. A plan cannot be placed on a shelf, and it was not sold or announced (it had already been unveiled).",
    "Common meaning (on a shelf) is the trap; 'instead' shows the plan was set aside.", "easy", 30, group="rc-g-voc1"),
 QA("rc-vocab-context-p04", sub, "rc-p19", "Which word is most nearly OPPOSITE in meaning to **modest** as used in 'a modest victory'?",
    ["huge", "humble", "small", "shy"],
    "Here 'modest' means small or limited — the traders only got the plan shelved and the roof repaired, 'but' they celebrated as if they had won a war. The opposite of small is huge. 'Small' is a synonym; 'humble' and 'shy' relate to the other meaning of modest (a modest person), not to this sentence.",
    "Find the meaning in THIS sentence (small) and flip it once (huge).", "medium", 35, group="rc-g-voc1"),
 QA("rc-vocab-context-p05", sub, "rc-p18", "The word **unveiled** as used in the passage is closest in meaning to:",
    ["presented to the public", "hid from view", "cancelled", "decorated"],
    "The board 'unveiled a plan for a shiny new mall' — it made the plan known for the first time. 'Hid' is the opposite, 'cancelled' happens later (shelved), and 'decorated' does not fit a plan.",
    "Un-veil = remove the cover → show. Then check it fits the sentence.", "easy", 25, group="rc-g-voc1"),
]
PV2 = """Scientists who study earthquakes are frank about the limits of their craft. They can say which regions are prone to strong tremors and roughly how often such tremors occur, but they cannot yet predict the day or the hour. What they can do is reduce the toll. Buildings that follow earthquake codes sway without collapsing, and a school drill that teaches children to 'drop, cover and hold' can save lives in the first few seconds.

The trouble is that codes cost money and drills take time, while a big earthquake may not come for decades. Officials under pressure to show quick results are tempted to cut corners. When the ground finally shakes, the price of those saved rupees is paid in lives."""
QS += [
 QA("rc-vocab-context-p06", sub, "rc-p21", "The word **craft** in the passage refers to:",
    ["a skill or field of work", "a boat or an aircraft", "a clever trick to deceive people", "a handmade object"],
    "'The limits of their craft' — the scientists' craft is earthquake science, i.e. their skill or field of work. The other meanings of 'craft' (vessel, cunning, handicraft) do not fit scientists who 'can say which regions are prone to tremors'.",
    "Plug in: 'the limits of their field of work' — only this sense makes sense.", "medium", 30, PV2, "rc-g-voc2"),
 QA("rc-vocab-context-p07", sub, "rc-p19", "Which of the following is most nearly OPPOSITE in meaning to **frank** as used in the passage?",
    ["evasive", "honest", "open", "direct"],
    "Scientists are 'frank about the limits' — they say openly what they cannot do. Frank = honest, open, direct (three synonyms placed as traps). The opposite is evasive — avoiding a clear answer.",
    "Three options mean the same thing; the odd one out is the antonym.", "easy", 25, group="rc-g-voc2"),
 QA("rc-vocab-context-p08", sub, "rc-p20", "What does the phrase **cut corners** mean in the passage?",
    ["save time or money by skipping necessary steps", "design buildings with rounded corners", "take the shortest road", "reduce the size of rooms"],
    "Context: codes cost money, drills take time, and officials want quick results. They are tempted to skip these costly steps — then 'the price of those saved rupees is paid in lives'. So 'cut corners' = do something cheaply or quickly by ignoring what is needed. The literal options are traps.",
    "'Saved rupees' in the next sentence confirms the meaning: saving money by skipping safety.", "medium", 35, group="rc-g-voc2"),
 QA("rc-vocab-context-p09", sub, "rc-p21", "Which of the following can best replace **toll** in 'What they can do is reduce the toll'?",
    ["damage and loss of life", "tax paid on a highway", "ringing of a bell", "number of earthquakes"],
    "Scientists cannot predict the quake, but they can reduce its harm — safe buildings and drills 'save lives'. So 'toll' here means the damage and deaths caused. Highway tax and bell-ringing are other meanings of the word; scientists cannot reduce the number of earthquakes.",
    "The next sentence (buildings don't collapse, drills save lives) tells you what is being reduced.", "hard", 40, group="rc-g-voc2"),
]

sub = "rc-tone-attitude"
PT1 = """Every few years the city announces a grand plan to clean its lake. Consultants are hired, glossy brochures are printed, and a minister arrives to plant a sapling on the bank. Then the cameras leave. The sewage pipes that empty into the water are never diverted, the encroachments on the shore are never removed, and the lake grows a little greener each summer. Surely a city that can spend crores on brochures can find the money to lay a single drain."""
QS += [
 QA("rc-tone-attitude-p01", sub, "rc-p22", "The tone of the passage is best described as:",
    ["critical and sarcastic", "admiring", "neutral and factual", "hopeful"],
    "'Grand plan', 'glossy brochures', 'Then the cameras leave' and the final 'Surely a city that can spend crores on brochures can find the money…' mock the show-without-action. That is criticism with sarcasm. There is no praise (admiring), the author clearly judges (not neutral), and nothing hopeful is said.",
    "A line starting with 'Surely…' that points out an obvious failure is a sarcasm signal.", "easy", 35, PT1, "rc-g-tone1"),
 QA("rc-tone-attitude-p02", sub, "rc-p23", "The author's attitude towards the city's clean-up plans is one of:",
    ["disappointment at their show without real action", "strong approval", "complete indifference", "fear"],
    "Each plan brings consultants, brochures and ceremonies, but sewage and encroachments remain and the lake gets greener. The author is unhappy that plans are all show. He clearly cares (not indifferent) and does not approve; nothing expresses fear.",
    "List what the author says about the plans: brochures, cameras, 'never diverted' — all negative.", "medium", 35, group="rc-g-tone1"),
 QA("rc-tone-attitude-p03", sub, "rc-p24", "With which of the following statements would the author most likely agree?",
    ["Stopping sewage from entering the lake matters more than publicity events", "Brochures and ceremonies are the best way to clean a lake", "The lake cannot be cleaned by any means", "Consultants should be paid more for their work"],
    "The author contrasts spending on brochures with the unbuilt drain and says a single drain can surely be afforded. He believes real work (diverting sewage) matters more than publicity. The second option is the reverse; the third is pessimism he does not show — he thinks one drain is affordable; consultants' pay is not discussed.",
    "The author's opinion sits in the last line; pick the option that restates it at the same strength.", "medium", 40, group="rc-g-tone1"),
]
PT2 = """Honey does not spoil easily because of three properties. It contains very little water, so the microbes that cause decay cannot grow in it. It is slightly acidic. And bees add an enzyme that slowly produces small amounts of hydrogen peroxide, a substance that kills germs. If honey is left open to damp air, however, it can absorb moisture and begin to ferment."""
QS += [
 QA("rc-tone-attitude-p04", sub, "rc-p22", "The tone of the passage is:",
    ["informative", "humorous", "critical", "nostalgic"],
    "The passage only explains three scientific reasons and one exception. There are no jokes, no faults pointed out and no fond memories of the past — it simply informs.",
    "Facts + explanation + no evaluative words = informative/neutral.", "easy", 25, PT2, "rc-g-tone2"),
 QA("rc-tone-attitude-p05", sub, "rc-p25", "The passage is most likely taken from:",
    ["a general science book or article", "a political speech", "a personal diary", "a newspaper advertisement for honey"],
    "It gives an impersonal, factual explanation of why honey resists decay, including a weakness (it can ferment in damp air). There is no persuasion (speech), no personal feeling or first person (diary), and no selling language — an advertisement would not point out a weakness.",
    "Neutral explanation of a natural process → science writing.", "easy", 30, group="rc-g-tone2"),
 QA("rc-tone-attitude-p06", sub, "rc-p24", "Which statement would the author most likely agree with?",
    ["Honey keeps well mainly because of its natural properties, but it should be kept closed", "Honey can never go bad under any conditions", "The hydrogen peroxide in honey makes it harmful to eat", "Honey should be stored in damp places"],
    "The author lists the natural properties that stop decay and then warns ('however') that honey left open to damp air can ferment — so it should be kept closed. 'Never go bad' ignores the 'however' sentence; the passage calls the peroxide germ-killing, not harmful, and only in small amounts; damp storage is exactly what the passage warns against.",
    "The 'however' sentence limits the claim — options that ignore it (never, any conditions) are wrong.", "medium", 40, group="rc-g-tone2"),
]
PT3 = """Online classes kept lakhs of students connected to their teachers when schools were shut. For a child in a city flat with a laptop and steady internet, they were a lifeline. For a child in a village sharing one phone among three siblings, they were often a blank screen. Online learning is neither the saviour its promoters claim nor the failure its critics describe. It is a tool, and like any tool it helps only those who can reach it. Before schools make it a permanent part of teaching, they must first make sure that every child has a device and a connection."""
QS += [
 QA("rc-tone-attitude-p07", sub, "rc-p22", "Which word best describes the tone of the passage?",
    ["balanced", "angry", "celebratory", "indifferent"],
    "The author shows both sides — a lifeline for some, a blank screen for others — and says online learning is 'neither the saviour … nor the failure'. That is a balanced tone. No anger or celebration is expressed, and the author cares enough to recommend action, so not indifferent.",
    "'neither … nor' weighing both sides = balanced.", "easy", 30, PT3, "rc-g-tone3"),
 QA("rc-tone-attitude-p08", sub, "rc-p23", "The author's attitude towards online learning is that it is:",
    ["a useful tool whose benefit depends on access to devices and internet", "a complete failure that should be stopped", "the best form of education for every child", "unimportant and not worth discussing"],
    "'It is a tool, and like any tool it helps only those who can reach it.' The author accepts its value but ties it to access. The second and third options are the extreme views of critics and promoters that the author rejects; the author obviously thinks it worth discussing.",
    "The author's own sentence ('It is a tool…') states the attitude — match it.", "medium", 35, group="rc-g-tone3"),
 QA("rc-tone-attitude-p09", sub, "rc-p25", "The passage is most likely an extract from:",
    ["an opinion piece in a newspaper on education", "a user manual for a laptop", "a short story for children", "a science textbook chapter on how the internet works"],
    "It discusses a current public issue, judges both sides and ends with a recommendation ('schools … must first make sure…'). That is the style of an opinion piece or editorial. A manual gives instructions, a story has characters and plot, and a textbook would explain technology without taking a position.",
    "Opinion + recommendation on a public issue = editorial / opinion piece.", "medium", 30, group="rc-g-tone3"),
 QA("rc-tone-attitude-p10", sub, "rc-p23", "How does the author view the claims made by both the promoters and the critics of online learning?",
    ["Both sets of claims are exaggerated", "The promoters are right and the critics are wrong", "The critics are right and the promoters are wrong", "Both sets of claims are fully correct"],
    "'Neither the saviour its promoters claim nor the failure its critics describe' — the author rejects both extreme claims. So both are exaggerated. The two one-sided options and 'both fully correct' contradict the 'neither … nor' sentence.",
    "'neither X nor Y' rejects both X and Y.", "hard", 40, group="rc-g-tone3"),
]

new_ids = {q["id"] for q in QS}
upsert_list(data["practice"], QS)

# ---------------------------------------------------------------- fixes to existing solutions (letter references were scrambled)
FIX = {
 "eng-rc-s01": "The passage contrasts a recurring crisis with a weakening official response: promises made, token steps taken, and the real measures announced 'with less conviction than the last'. **(b)** covers the whole passage at the author's level of criticism. (a) is too extreme — stubble burning and bus fleets are named alongside industry, so industry is not the *sole* source. (c) is contradicted — filters are the *token* step, not the effective one. (d) mentions wind only as the event that ends each episode, not as the cause.",
 "eng-rc-s03": "One step from the line: branches in poor areas are small, small branches are closed first, and those areas need libraries most → the most-needed branches face the highest closure risk — **(d)**. (a) adds a motive ('deliberately want to hurt') — the passage blames budgets, not malice. (b) goes outside the line; nothing is said about rich neighbourhoods lacking libraries. (c) turns 'often the first' into 'all… eventually', an extreme the passage never supports.",
 "eng-rc-p01": "Para 1 explains how city building materials and design create the heat island; para 2 gives its uneven consequences; para 3 argues that local design measures work and ends 'can plan itself out of one'. **(c)** covers this. (a) narrows to one solution although the passage lists several, and 'only' is extreme. (b) reverses the passage — cities are hotter than villages, and deforestation is not discussed. (d) exaggerates beyond the passage and blames global warming, which para 1 explicitly limits.",
 "eng-rc-p04": "The plan 'has become a model studied by other developing countries' and is cited to support the claim that local measures 'can lower local temperatures measurably within a single season'. The one-step inference: the author holds it up as a working, practical example — **(b)**. (a) brings in foreign aid, which is never mentioned. (c) narrows the plan's scope, which the passage describes broadly (warnings plus roof subsidies). (d) contradicts the passage's praise.",
 "eng-rc-p06": "The passage's two halves: flexibility is real (para 1), but risk and legal exclusion fall on workers (paras 1–2), and rules must catch up (para 3). **(a)** compresses exactly this. (b) is contradicted — the author says such work 'will grow'. (c) is never discussed; the factory comparison is about which laws exist, not what employees prefer. (d) narrows to the example in the opening sentence.",
 "eng-rc-p09": "The sentence lists what is missing: no minimum wage for waiting hours, no paid leave, pension contributions fully self-funded. *Cushions* here means softens the blow — so a sick gig worker has no paid buffer, **(a)**. (c) and (d) contradict the sentence — paid leave and compensation are exactly what is missing. (b) misreads 'cushion' as a job duty; nothing about training appears.",
 "eng-rc-p13": "The line says smaller branches in poorer neighbourhoods are 'precisely those that need them most' and are 'often the first to be marked for closure'. The one-step inference: closures hit the most dependent communities — **(c)**. (a) reverses the geography — poor, not wealthy, areas hold the small branches at risk. (b) is the opposite — closures affect the people who use and need libraries. (d) separates staff from users without any basis.",
 "eng-rc-p14": "Critics believed the internet had made 'buildings full of books redundant' — unnecessary, a thing whose job was over; the next sentence ('The prediction has aged badly') confirms that critics expected libraries to become useless. So redundant = **(d) outdated and no longer needed**. (a) cost is never linked to the word. (b) plays on the idea of duplicate copies, which the passage does not discuss. (c) 'protected by law' has nothing to do with the critics' claim.",
}
for arr in ("solvedExamples", "practice"):
    for q in data[arr]:
        if q["id"] in FIX:
            q["solution"] = FIX[q["id"]]

added = fill_group_passages(data)
print("passages copied onto existing group members:", added)

# ---------------------------------------------------------------- topic-level pyqPatterns (rewritten, richer)
data["pyqPatterns"] = [
 {"pattern": "Central theme / main idea of the passage", "frequency": "very common", "subtopic": "rc-main-idea",
  "howToSpot": "The stem says 'the central idea/main theme of the passage', 'the passage is primarily concerned with' or 'which option sums up the passage'. Almost every RC set has one such question.",
  "approach": "Before reading the options, say the topic (from the first paragraph) and the author's point (usually in the last lines) in about ten words. Then remove options that cover only one paragraph, options that talk about a bigger subject, and options with extreme words like only/always.",
  "example": {"q": "A passage says people throw away gadgets because repair is hard, that this creates e-waste, and that new rules on spare parts can make repair possible again. Central idea?", "solution": "Hard-to-repair products create hidden waste, and rules that make repair possible can reduce it. Options about only e-waste workers or only solar power are too narrow or off-topic."}},
 {"pattern": "Most suitable title", "frequency": "very common", "subtopic": "rc-main-idea",
  "howToSpot": "The stem asks for 'the most appropriate/suitable title'. Options are short headings.",
  "approach": "A title is the main idea in a few words. It must cover every paragraph. Reject titles built on the first example, dramatic titles the author would not use, and titles about a bigger subject. Two-part titles with a colon often fit passages that give a problem and a solution.",
  "example": {"q": "A passage: city footpaths are broken, this is dangerous and adds to traffic, and good footpaths are cheap. Best title?", "solution": "'Walking Matters: Why Cities Must Fix Their Footpaths' — covers problem and demand. 'A History of Road Accidents' is too broad."}},
 {"pattern": "Factual detail ('According to the passage')", "frequency": "very common", "subtopic": "rc-detail-fact",
  "howToSpot": "The stem asks what, when, how often or why something happened, usually beginning 'According to the passage'. The answer is written in one or two lines.",
  "approach": "Take a keyword from the question, find it in the passage and read the sentence before and after. Say the answer in your own words, then match the option that paraphrases it. Check small words like all/most/only and every number.",
  "example": {"q": "Passage: 'Money was paid every ten days, directly into bank accounts.' The old trader 'delayed payment for weeks'. How often did the cooperative pay?", "solution": "Every ten days. 'After several weeks' describes the old trader — a trap from another line."}},
 {"pattern": "NOT / EXCEPT detail question", "frequency": "common", "subtopic": "rc-detail-fact",
  "howToSpot": "The stem contains NOT or EXCEPT, often in capital letters: 'Which is NOT mentioned…', 'all of the following EXCEPT'.",
  "approach": "Circle the NOT/EXCEPT first. Find the list or sentence that three options come from and tick each one you can see in the passage. The option you cannot find, or that the passage contradicts, is the answer.",
  "example": {"q": "Passage lists steps, carvings and shaded platforms as stepwell features. Which is NOT mentioned: steps, carvings, platforms, wooden roofs?", "solution": "Wooden roofs — the only feature not in the passage."}},
 {"pattern": "Inference ('It can be inferred / the author implies')", "frequency": "common", "subtopic": "rc-inference",
  "howToSpot": "The stem uses infer, imply, suggest, 'most probably' or 'what does the author mean by'. The answer is not written word for word.",
  "approach": "Take the line the question points to and go one small step further. Use the must-be-true test: if the option were false, would the passage stop making sense? Reject word-for-word copies, outside facts, extreme words and invented motives.",
  "example": {"q": "Passage: a farmer's solar pump made water free, he watered longer than needed, and his borewell dropped. What can be inferred?", "solution": "Free power encouraged him to over-pump groundwater. 'Solar pumps always damage groundwater' is too extreme."}},
 {"pattern": "Word or phrase meaning in context (synonym / antonym / idiom)", "frequency": "very common", "subtopic": "rc-vocab-context",
  "howToSpot": "The stem quotes a word or phrase from the passage and asks its meaning, a synonym or an antonym 'as used in the passage'.",
  "approach": "Read only the sentence with the word. Think of your own simple word, then plug each option into the sentence. The right option keeps meaning, grammar and tone. For antonyms, find the meaning in context first and then flip it once. For idioms, read the phrase as one unit.",
  "example": {"q": "'The board shelved the plan and instead agreed to repair the roof.' Meaning of shelved?", "solution": "Put aside / postponed. 'Arranged on shelves' is the everyday meaning and a trap."}},
 {"pattern": "Author's tone, attitude or opinion", "frequency": "common", "subtopic": "rc-tone-attitude",
  "howToSpot": "The stem asks for the tone of the passage, the author's attitude towards something, or which statement the author would agree with.",
  "approach": "Collect the describing words (glossy, surely, merely, lifeline) and decide if they are positive, negative or neutral and how strong. Confirm with the last sentence. Match both direction and degree; extreme tone words are rarely right, and a serious topic can still have a neutral tone.",
  "example": {"q": "'Surely a city that can spend crores on brochures can find the money to lay a single drain.' Tone?", "solution": "Critical and sarcastic — it mocks spending on show instead of real work."}},
 {"pattern": "Structure questions: statements I-II-III, paragraph purpose, why the author mentions X", "frequency": "common", "subtopic": "rc-reading-strategy",
  "howToSpot": "Options like 'Only I and III'; stems like 'The second paragraph mainly…' or 'Why does the author mention…?'",
  "approach": "For statement questions, mark each statement True/False/Not stated separately and cut options containing a false one. For paragraph purpose, use your paragraph map. For 'why mention X', read the sentence before X — the example supports that point.",
  "example": {"q": "Passage: 'Small savings add up. A tea-seller who saves ₹20 a day has over ₹7,000 in a year.' Why is the tea-seller mentioned?", "solution": "To illustrate that small daily savings grow into a large sum — the point in the sentence before the example."}},
]

save(TOPIC, data)
report(data, before, new_ids)
