export interface StudyGuide {
  slug: string;
  title: string;
  description: string;
  audience: string;
  intro: string;
  sections: { id: string; title: string; body: string }[];
  checklist: string[];
  related: string[];
  published?: string;
}

export const GUIDE_DATE = '2026-10-09';

export const STUDY_GUIDES: StudyGuide[] = [
  {
    slug: 'percentages-base-value-and-successive-change',
    title: 'Percentage changes: choose the right base before using a shortcut',
    description: 'Understand percentage increase, successive changes, reverse percentages and percentage points with worked examples and a self-check.',
    audience: 'Arithmetic learners', published: '2026-10-10',
    intro: 'Most percentage errors begin before multiplication: the wrong number is chosen as the base. This lesson follows one idea through price changes, discounts and reverse questions. The examples are original study exercises, not recalled exam questions.',
    sections: [
      { id: 'base', title: 'Write the base beside the percentage', body: `A percentage compares a part with a base of 100. To find 15% of 240, calculate $240 × 15 ÷ 100 = 36$. Here 240 is the base.

When a value changes, the percentage change usually compares the difference with the **original** value. A price rises from 400 to 460. The increase is 60, so the percentage rise is $60 ÷ 400 × 100 = 15$.

If the price falls from 460 back to 400, the decrease is still 60, but its base is now 460. The percentage fall is $60 ÷ 460 × 100$, approximately 13.04%. Equal differences do not mean equal percentage changes when their bases differ.

Before calculating, write “percentage of ___” in the margin. If the question says profit as a percentage of cost, the base is cost. If it asks the discount on marked price, the base is marked price. Learn those definitions in [profit, loss and discount](/quant/profit-loss-discount/).` },
      { id: 'multipliers', title: 'Turn successive changes into multipliers', body: `A 20% increase retains the original 100% and adds 20%, so its multiplier is 1.20. A 20% decrease retains 80%, so its multiplier is 0.80.

Starting with 500, a 20% rise followed by a 20% fall gives $500 × 1.20 × 0.80 = 480$. This is a 20 decrease from the original 500, or 4% overall.

For signed changes $a$ and $b$, the combined percentage is $a + b + ab ÷ 100$. Use positive values for increases and negative values for decreases. With 20 and −20, the result is $20 - 20 - 4 = -4$.

The multiplier method is often easier to audit. For a 10% increase followed by a 10% decrease, $1.10 × 0.90 = 0.99$, a 1% decrease. This assumes that each change applies to the value produced by the previous change. If two discounts apply independently to the original price, read the wording before multiplying.` },
      { id: 'reverse', title: 'Reverse a change by division', body: `After a 25% increase, a fee is 750. The original fee is not 750 minus 25% of 750: that would use the wrong base.

Let the original fee be $x$. Then $1.25x = 750$, so $x = 750 ÷ 1.25 = 600$. Check forward: 25% of 600 is 150, and 600 + 150 is 750.

After a 20% discount, a book costs 640. Its marked price is $640 ÷ 0.80 = 800$. Check: 20% of 800 is 160, leaving 640.

A useful boundary check is that a positive increase makes the final value larger than the original; a discount makes it smaller. If your reverse answer violates this, examine the multiplier or division.` },
      { id: 'points', title: 'Distinguish percentage points from percentage change', body: `A test accuracy rate rises from 40% to 50%. The difference is **10 percentage points**. The relative increase in the rate is $10 ÷ 40 × 100 = 25\\%$.

These answer different questions. Percentage points subtract two rates. Percentage change divides the difference by the original rate. Do not say “10% increase” when the question asks for the relative change from 40% to 50%.

For a population of 200 students, 40% is 80 and 50% is 100. The increase of 20 students is 25% of the original 80, which confirms the relative calculation. This example assumes the population stays at 200.` },
      { id: 'practice', title: 'Check the idea with four short problems', body: `Try these with the answers covered:

1. A quantity rises from 800 to 920. Find its percentage increase.
2. A price of 1,000 receives successive discounts of 10% and 20%. Find the final price and overall discount.
3. A value is 900 after a 25% decrease. Find the original value.
4. An accuracy rate rises from 60% to 72%. Find the percentage-point difference and relative increase.

**Worked answers:** (1) $120 ÷ 800 × 100 = 15\\%$. (2) $1000 × 0.90 × 0.80 = 720$, so the discount is 28%. (3) $900 ÷ 0.75 = 1200$. (4) 12 percentage points; $12 ÷ 60 × 100 = 20\\%$ relative increase.

If you got a wrong answer, record the base you used in your [error notebook](/study-guides/error-notebook-for-exam-preparation/). Then retry with different numbers. Continue with the [percentage topic](/quant/percentage/) and put a closed-book review in the [revision planner](/revision-planner/).` },
    ],
    checklist: ['Name the base before multiplying.', 'Use multipliers for successive changes.', 'Divide to reverse an increase or decrease.', 'Keep percentage points separate from relative change.', 'Check the result by applying the change forward.'],
    related: ['maths-from-basics-for-competitive-exams', 'error-notebook-for-exam-preparation', 'revision-without-forgetting'],
  },
  {
    slug: 'reading-comprehension-find-evidence',
    title: 'Reading comprehension: choose an answer the passage can support',
    description: 'A practical reading-comprehension method with an original passage, worked main-idea and inference questions, and a review checklist.',
    audience: 'English and CAT learners', published: '2026-10-10',
    intro: 'A familiar topic can make a wrong option feel convincing. Reading comprehension asks what this passage supports, not everything you know about the topic. Work through the short original passage below, then use the same evidence-first method on longer texts.',
    sections: [
      { id: 'passage', title: 'Read for the author’s claim and its limits', body: `**Original practice passage**

When a neighbourhood library extended its evening hours for six weeks, attendance after 6 pm increased. The staff had also placed a notice about the new hours at a nearby bus stop. Some visitors said they came because the later closing time suited their work schedules; others had learned about the library from the notice. The trial cost more because a second staff member stayed late. The manager recommended continuing it for another month while recording the number of repeat visitors and the extra staffing cost. She did not claim that longer opening hours alone explained the increase.

The first sentence reports an observation: attendance increased during the trial. The next sentences describe two possible influences, visitor comments and a cost. The final recommendation is cautious: continue collecting evidence. The passage does not prove that one change caused the whole increase.

After reading, state the passage in one sentence: “An evening-hours trial increased attendance, but the manager wants more evidence before judging its value.” This summary keeps both the result and the limitation.` },
      { id: 'main-idea', title: 'Compare the scope of the main-idea options', body: `**Question:** Which statement best captures the passage?

A. Longer opening hours always improve a library’s performance.

B. A library trial showed promising attendance, but its causes and costs still need evaluation.

C. Advertising is the only reason people visit libraries.

D. Libraries should avoid employing extra staff.

**Answer: B.** It includes the attendance change and the manager’s qualified recommendation. A adds “always”, although the passage discusses one six-week trial. C turns one possible influence into the only cause. D converts a reported cost into advice the author never gives.

A main-idea answer should fit the whole passage. A detail such as the bus-stop notice is important evidence, but it is too narrow to replace the central point.` },
      { id: 'inference', title: 'Make the smallest inference the evidence allows', body: `**Question:** What can reasonably be inferred about the manager?

A. She knows that the notice had no effect.

B. She thinks the trial should be assessed using more than attendance alone.

C. She wants to close the library immediately.

D. She believes every visitor works late.

**Answer: B.** She asks for repeat-visitor counts and extra staffing cost, so her assessment goes beyond the current attendance increase. A conflicts with her refusal to isolate a cause. C conflicts with extending the trial. D takes comments from “some visitors” and applies them to everyone.

Inference is not free speculation. Ask whether the passage gives enough support for the answer without adding a new fact. “Some”, “all”, “may” and “must” change the strength of an option. Treat these words as part of the reasoning, not decorative language.` },
      { id: 'evidence', title: 'Use an evidence line to test close options', body: `For each candidate answer, identify the sentence that supports it. If there is no supporting sentence or clear combination of sentences, you may be relying on outside knowledge.

Suppose an option says “The trial proved that later closing alone caused attendance to rise.” The passage explicitly says the manager **did not claim** this. Another option might say “Staffing cost rose during the trial.” That follows directly from the sentence about a second staff member staying late.

For a vocabulary question, first identify the word’s role in that sentence. In this passage, “trial” means a limited experiment, not a court case. Replace the word with your proposed meaning and check whether the sentence still fits.

Tone questions also need evidence. Here the manager’s recommendation is cautious and investigative. “Angry” or “triumphant” would require language that the passage does not contain.` },
      { id: 'routine', title: 'Review the reason an option failed', body: `Use a 20-minute practice block: read a short passage for 5 minutes, answer its questions for 8 minutes, and spend 7 minutes reviewing. Adjust the timing to your level and target exam; this is a learning routine, not a universal test strategy.

Record one reason for each rejected option: too broad, too narrow, unsupported cause, reversed meaning, or stronger language than the passage. If you chose a wrong answer, write the evidence you overlooked. Avoid keeping only the option letter, which does not explain the error.

For longer CAT passages, map each paragraph’s role: introduce a claim, explain it, qualify it, offer evidence, or challenge an alternative. Do not assume that every paragraph states the author’s own opinion. Read attribution words such as “critics argue” carefully.

Continue with [reading comprehension](/english/reading-comprehension/), the [beginner English routine](/study-guides/english-for-competitive-exams-beginners/) and the [error notebook](/study-guides/error-notebook-for-exam-preparation/). Revisit this passage later and explain why each incorrect option fails without looking at the solutions.` },
    ],
    checklist: ['Summarise the passage with its limits intact.', 'Find evidence for the selected answer.', 'Check strong words such as always and only.', 'Keep inference smaller than speculation.', 'Review why the wrong options fail.'],
    related: ['english-for-competitive-exams-beginners', 'error-notebook-for-exam-preparation', 'study-with-job-or-college'],
  },
  {
    slug: 'maths-from-basics-for-competitive-exams',
    title: 'Weak in maths? Start competitive exam preparation from the basics',
    description: 'A practical maths learning order for SSC, Railway and Banking beginners, with worked examples and a two-week starter routine.',
    audience: 'Maths beginners',
    intro: 'If fractions, percentages or word problems feel difficult, start with the small skills those questions depend on. You do not need to finish an entire school textbook before opening an exam topic. Learn one skill, solve a few questions, then check whether you can explain the method without looking.',
    sections: [
      { id: 'find-the-gap', title: 'Find the exact skill you need to repair', body: `Try these three examples on paper before reading the answers:

1. What is three quarters of 80?
2. A price rises from 200 to 250. What is the percentage increase?
3. Two workers finish a job individually in 12 and 18 days. How long do they take together?

**Answers:** 60; 25%; 7.2 days.

For the first, divide 80 into four equal parts and take three: $80 ÷ 4 × 3 = 60$. For the second, divide the increase by the original price: $50 ÷ 200 × 100 = 25$.

For the third, assume 36 units of work. The workers complete 3 and 2 units daily. Together they finish 5 units daily, so the time is $36 ÷ 5 = 7.2$ days.

If the first example is unclear, repair fractions before percentages. If only the third is difficult, start with rates and [Time & Work](/quant/time-work/). This short check locates a gap; it does not measure your exam readiness.` },
      { id: 'learning-order', title: 'Learn in an order that reduces repeated effort', body: `| Stage | Learn | Why it comes here |
| --- | --- | --- |
| 1 | [Number system](/quant/number-system/), [simplification](/quant/simplification/), [HCF and LCM](/quant/hcf-lcm/) | Division, factors and fractions appear in later topics. |
| 2 | [Ratio](/quant/ratio-proportion/), [percentage](/quant/percentage/), [average](/quant/average/) | Learn how quantities relate and change. |
| 3 | [Profit and loss](/quant/profit-loss-discount/), [interest](/quant/interest/), [mixtures](/quant/mixture-alligation/) | Apply percentages and ratios to stories. |
| 4 | [Time and work](/quant/time-work/), [speed and distance](/quant/time-speed-distance/) | Build and compare rates. |
| 5 | [Algebra](/quant/algebra/), [geometry](/quant/geometry/), [mensuration](/quant/mensuration-2d/) | Follow your target exam's syllabus. |

This is a learning order, not a claim about marks or topic weightage. Check your [exam page](/exams/) before including advanced topics. CAT, Banking and SSC need different levels of depth.` },
      { id: 'daily-block', title: 'Use a 45-minute block that ends with evidence', body: `Spend 10 minutes on one lesson and its worked example. Close the example and rebuild its steps yourself.

Spend 20 minutes solving 8 to 12 questions from that subtopic. Begin without a timer if the idea is new. Use the [topic notes](/learn/) to find the matching practice set.

Spend 10 minutes reviewing every wrong answer and every guess. Write the first step that failed, rather than copying the whole solution.

Spend the final 5 minutes retrying yesterday's mistakes. If you still cannot choose the first step, return to the lesson. If the method is clear but calculation is slow, practise that calculation separately.

> **Tip:** Write units beside numbers. Days, kilometres and rupees often reveal whether your setup makes sense.` },
      { id: 'two-weeks', title: 'Try this two-week starter routine', body: `Use days 1–3 for fractions, factors and simplification. Use days 4–6 for ratio and percentages. On day 7, retry the questions you got wrong without seeing their solutions.

Use days 8–10 for average and profit/loss. Use days 11–13 for rates, starting with time and work. On day 14, mix questions from the topics you studied and explain the first step for each.

Move slower when needed. Two weeks is a starter routine, not a promise to finish maths. Keep English and your other exam subjects in small daily slots while rebuilding maths.

Add each completed topic to the [revision planner](/revision-planner/) so you return to it after a gap.` },
      { id: 'shortcuts', title: 'Add speed after the method is reliable', body: `A shortcut is useful when you know why it works and when it applies. For example, 25% means one quarter, so 25% of 360 is $360 ÷ 4 = 90$. This saves work because the fraction is exact.

Avoid memorising a trick whose conditions you cannot explain. First solve a small example by the standard method. Then use the shortcut on the same example and compare the answers.

Use the [formula sheet](/formula-sheet/) for recall after learning the topic. Reading a formula repeatedly is not the same as recognising when to use it.` },
    ],
    checklist: ['Identify the first unclear step, not just the wrong answer.', 'Finish one subtopic before collecting another course.', 'Explain a solved question with the solution closed.', 'Return to errors after a gap.', 'Build accuracy before shortening your time limit.'],
    related: ['error-notebook-for-exam-preparation', 'study-with-job-or-college', 'revision-without-forgetting'],
  },
  {
    slug: 'english-for-competitive-exams-beginners',
    title: 'English for competitive exams: a beginner routine you can follow daily',
    description: 'Learn grammar, vocabulary and reading comprehension with a 30-minute routine, original examples and clear ways to review mistakes.',
    audience: 'English beginners',
    intro: 'You can improve exam English without learning every grammar rule at once. Start with the kinds of mistakes you actually make. Study a small rule, apply it in a sentence, and return to it later. This guide focuses on written exam questions rather than spoken fluency.',
    sections: [
      { id: 'three-skills', title: 'Separate grammar, vocabulary and reading', body: `**Grammar** helps you judge how words fit together. **Vocabulary** helps you understand a word in context. **Reading** helps you follow what a passage says and supports.

Treat these as three small daily tasks. A long list of word meanings will not fix subject–verb agreement. Learning tense names will not automatically improve passage reading.

Start with [grammar essentials](/english/grammar-essentials/), [synonyms and antonyms](/english/synonyms-antonyms/), and [reading comprehension](/english/reading-comprehension/). Use your exam's syllabus to decide how much attention each needs.` },
      { id: 'grammar-example', title: 'Learn a rule through the mistake it prevents', body: `Consider: “The list of selected candidates **are** on the notice board.”

The subject is **list**, which is singular. “Of selected candidates” describes the list. The verb therefore becomes **is**: “The list of selected candidates is on the notice board.”

Now compare: “The selected candidates **are** waiting outside.” Here, the subject is **candidates**, which is plural.

When reviewing an agreement question, underline the subject and circle the verb. Write a new sentence with the same structure. This makes the rule usable beyond the original question.

Work through [error spotting](/english/error-spotting/) and [sentence improvement](/english/sentence-improvement/) one rule at a time.` },
      { id: 'vocabulary', title: 'Keep fewer words, with better context', body: `Choose five words from a passage or practice set. For each, record a plain meaning, one sentence and one contrasting word if useful.

Example: **reluctant** means unwilling or hesitant. “Ravi was reluctant to change his study plan.” A useful contrast is **willing**.

Next day, hide the meaning and explain the word aloud or on paper. Then read your sentence. If you remember only its Hindi translation but cannot use it, write another simple sentence.

Use the [vocab bank](/vocab/) and [idioms](/english/idioms-phrases/) as material for recall. Five words is a manageable starting choice, not a universal daily requirement. Reduce the number when reviews start piling up.` },
      { id: 'reading', title: 'Keep passage answers tied to evidence', body: `Read this original example: “The library extended its evening hours for one month. More students visited after work. The librarian said the trial would continue only if staffing remained available.”

**What can you conclude?** Evening access helped some students attend after work. **What cannot you conclude?** The longer hours are permanent, or every student prefers evenings.

For an inference question, choose what the passage supports. Do not add a stronger claim from your own knowledge. Words such as “all”, “always” and “only” deserve extra attention.

After each passage, write its main point in one sentence. For each wrong answer, locate the sentence that contradicts it or note the missing evidence.` },
      { id: 'routine', title: 'Use a 30-minute routine and a weekly review', body: `Spend 10 minutes learning one grammar rule and applying it to a few questions. Spend 10 minutes reading a short passage and explaining its main point. Spend 5 minutes recalling yesterday's vocabulary and 5 minutes recording one error.

Once a week, solve a mixed practice set. Separate the errors into rule gaps, unknown words and unsupported inferences. Use that list to choose next week's work.

Forgetting a word is a signal to review it, not to abandon the whole list. Use the [revision planner](/revision-planner/) for vocabulary groups or grammar topics. Keep the topic names specific, such as “subject–verb agreement”, rather than “all English”.` },
    ],
    checklist: ['Name the rule behind a grammar correction.', 'Use new words in original sentences.', 'Support passage answers with evidence.', 'Review guessed answers as well as wrong ones.', 'Choose next week’s work from your error list.'],
    related: ['error-notebook-for-exam-preparation', 'revision-without-forgetting', 'study-with-job-or-college'],
  },
  {
    slug: 'study-with-job-or-college',
    title: 'Prepare for government exams alongside a job or college',
    description: 'A realistic two-hour weekday study routine, a busy-day fallback and a weekly review system for working and college aspirants.',
    audience: 'Working and college aspirants',
    intro: 'Build your plan around hours you can repeat, not the longest day you once managed. A small weekday routine with a weekly review is easier to adjust when work, classes or travel change. Use this as a starting template and fit it to your actual week.',
    sections: [
      { id: 'time-budget', title: 'Count available time before choosing a timetable', body: `Write down your fixed commitments first: work or classes, travel, meals and sleep. Put study blocks into the gaps that remain.

For example, five weekdays at two hours each plus three hours on each weekend day gives 16 hours a week. That is a planning budget, not a guarantee of selection.

Choose one target [exam](/exams/) first. Shared subjects let you reuse learning, but exam-specific sections and difficulty still matter. Keep your syllabus beside the plan so you do not spend limited time on an irrelevant topic.` },
      { id: 'weekday', title: 'Give each weekday block one clear job', body: `| Minutes | Task | Finish with |
| --- | --- | --- |
| 45 | Your weakest subject: one lesson and its practice | An explanation of the method |
| 30 | A second subject | A small checked practice set |
| 20 | English reading or exam-relevant GK | A few recall prompts |
| 15 | Due revision | Closed-book answers |
| 10 | Error review and tomorrow's plan | One specific repair task |

These blocks total 120 minutes. You can split them across morning and evening. Put difficult learning in the slot when you are most alert.

“Finish maths” is too vague for an evening. “Learn successive percentage change and check ten questions” tells you where to start and stop.` },
      { id: 'rotation', title: 'Rotate subjects without abandoning the basics', body: `Use three weekday learning blocks for your weakest subject and two for the next weakness. Keep short reading and recall slots steady.

If maths is the gap, follow the [maths beginner route](/study-guides/maths-from-basics-for-competitive-exams/). If English is the gap, use the [English routine](/study-guides/english-for-competitive-exams-beginners/).

On one weekend block, revisit questions you missed during the week. On another, continue a lesson that needs uninterrupted time. Review your actual progress before filling every spare hour with new content.` },
      { id: 'busy-day', title: 'Keep a 20-minute fallback for unusually busy days', body: `Use 10 minutes to retry three old errors, 5 minutes to recall a formula or vocabulary group, and 5 minutes to decide the next study task.

The fallback maintains contact with your preparation. It does not replace your normal study blocks. If most days become fallback days, reduce the plan to match your schedule.

Avoid treating a missed evening as a debt that must be repaid through lost sleep. Move the unfinished task to the next suitable block and reduce lower-priority new work.` },
      { id: 'weekly-review', title: 'Measure work completed, not just hours watched', body: `At the end of the week, list the subtopics studied, questions checked, errors retried and reviews completed. Video hours alone do not show whether you can solve questions.

Choose one change for next week. For example: “I repeatedly lose signs in algebra, so two review blocks will focus on that.”

Use the [error notebook method](/study-guides/error-notebook-for-exam-preparation/) and [revision planner](/revision-planner/) to make those blocks concrete. Shorten the amount of new material when reviews become unmanageable.` },
    ],
    checklist: ['Choose repeatable slots after fixed commitments.', 'Set one outcome for each block.', 'Keep a busy-day fallback.', 'Check whether your plan matches the syllabus.', 'Review errors before adding more material.'],
    related: ['maths-from-basics-for-competitive-exams', 'english-for-competitive-exams-beginners', 'revision-without-forgetting'],
  },
  {
    slug: 'revision-without-forgetting',
    title: 'How to revise for competitive exams without only rereading notes',
    description: 'Turn notes into recall prompts, review them after a gap and use a free calendar planner to build a manageable revision routine.',
    audience: 'Students who keep forgetting',
    intro: 'A familiar page can feel easy even when you cannot recall its method later. Revision should reveal what you can produce with the notes closed. Then reopen the lesson to repair what was missing. This is a practical routine you can use with topics, formulas and vocabulary.',
    sections: [
      { id: 'recall', title: 'Close the notes before checking what you remember', body: `After learning percentages, write three prompts: “What is the base quantity?”, “How do I find percentage change?” and “Why does a 20% rise followed by a 20% fall not return to the start?”

Answer without looking. Then compare with the lesson. If you cannot explain the base quantity, review that idea before attempting a faster shortcut.

For vocabulary, recall a meaning and sentence. For reasoning, rebuild the diagram. For GK, answer a specific fact prompt. Choose a task that resembles the skill you need in questions.` },
      { id: 'gaps', title: 'Return after a gap, with a flexible schedule', body: `A convenient starting schedule is the next day, then 3, 7 and 14 days after learning. These are suggested reminders, not a scientifically fixed best interval for every student.

If you struggle at a review, repair the lesson and revisit it sooner. If a topic is easy across several reviews, give it a longer gap. Near an exam, adapt the schedule to the time available.

The [free revision planner](/revision-planner/) creates these dates and exports them to a calendar. It does not claim you have mastered a topic just because a reminder is complete.` },
      { id: 'example', title: 'Use a worked example to test the idea', body: `Start with a quantity of 100. A 20% rise makes it 120. A 20% fall from 120 subtracts 24, leaving 96. The total change is a 4% fall.

The second percentage acts on a new base. That is the idea worth recalling. Memorising “20 minus 20 equals zero” fails because it ignores the changed base.

For a review, change the starting quantity to 250. The same changes produce 300 and then 240, still a 4% fall. Explain why before opening [percentage notes](/quant/percentage/).

For a non-numeric topic, use an equivalent check: create a new sentence for a grammar rule or redraw a seating diagram from its clues.` },
      { id: 'backlog', title: 'Keep revision small enough to repeat', body: `Review due topics before starting more new topics. Give weak ideas more attention than facts you recall easily.

When a backlog builds, group related items. For example, review five percentage errors together instead of creating five large revision sessions. Keep a short prompt for each error.

If you keep forgetting the same step, rereading the whole chapter may be inefficient. Write a tiny worked example for that step and solve a similar question. Use the [error notebook](/study-guides/error-notebook-for-exam-preparation/) to record the repair.` },
      { id: 'weekly-check', title: 'Check whether revision changes your answers', body: `Once a week, retry a mixed group of old errors without solutions. Record which you solved independently, which you guessed, and which still needed help.

Use that result to adjust next week's reviews. A completed calendar entry records effort; an independent correct solution provides better evidence of progress.

Use [formulas](/formula-sheet/) as recall prompts and [topic practice](/learn/) to check application. Keep both parts: knowing a formula and choosing it in a question.` },
    ],
    checklist: ['Turn notes into specific questions.', 'Attempt recall before rereading.', 'Use review intervals as adjustable reminders.', 'Repair repeated gaps with small examples.', 'Check progress using independent answers.'],
    related: ['error-notebook-for-exam-preparation', 'current-affairs-revision-method', 'study-with-job-or-college'],
  },
  {
    slug: 'current-affairs-revision-method',
    title: 'How to study and revise current affairs for competitive exams',
    description: 'A focused method for choosing relevant current affairs, writing useful fact prompts and reviewing monthly notes without collecting endless PDFs.',
    audience: 'GK and current affairs learners',
    intro: 'Current affairs can turn into a growing folder of unread material. Give every item a purpose: understand the event, identify the fact your exam may ask, and practise recalling it. Follow your exam syllabus rather than assuming every headline needs equal attention.',
    sections: [
      { id: 'scope', title: 'Set the scope from your exam', body: `Check whether your target exam includes general awareness and which areas its syllabus names. Banking awareness, static GK and broad current affairs are different preparation needs.

There is no universal “last six months is enough” rule for every exam. Use the syllabus and past question patterns to choose a period, then extend it when a gap appears.

Open the [current affairs archive](/current-affairs/) for month-wise material. The archive is a collection of study notes, not a guarantee that every event from each month is covered.` },
      { id: 'fact-card', title: 'Write a fact card that can become a question', body: `For an event, record the following only when relevant:

| Field | Prompt |
| --- | --- |
| Event | What happened? |
| Person or institution | Who was involved? |
| Place | Where did it happen? |
| Date | Which date or year matters? |
| Exam fact | What could a short question ask? |
| Static connection | Which related concept should I understand? |

For example, an appointment can lead to a name-and-role prompt. A report can lead to its publishing organisation and subject. Do not invent a rank, amount or year when the note does not establish it.

If two sources conflict, mark the item for checking rather than memorising both versions.` },
      { id: 'routine', title: 'Use a small daily block and a larger weekly review', body: `Spend 10 minutes reading a few relevant items. Spend 5 minutes writing recall prompts and 5 minutes answering prompts from earlier days.

At the weekend, close the notes and answer the week's prompts. Check the answers, then keep the missed items for another review. The number of items matters less than whether you can recall the useful facts.

Use a monthly quiz to find gaps. Review the wrong answers and explain why each correct fact belongs to that event. Avoid using quiz accuracy alone as proof of complete coverage.` },
      { id: 'static-gk', title: 'Connect an event to one static concept', body: `A news item about a constitutional office may reveal a gap in [polity](/ga/polity/). An economic announcement may need a basic [economy](/ga/economy/) concept. A location can lead to [Indian geography](/ga/indian-geography/).

Read the relevant concept briefly, then return to the event. Do not let one headline become an entire day of unrelated reading.

Use the [static GK tables](/static-gk/) for structured recall. Keep current facts and stable background facts distinguishable in your notebook, since current roles and figures can change.` },
      { id: 'monthly-close', title: 'Finish a month by reducing it to retrievable facts', body: `Group missed prompts by category: appointments, awards, economy, science, sports or other syllabus areas. Delete duplicate prompts from your personal notes, and keep the version with enough context.

At month-end, identify which facts remain hard to recall. Schedule a review for those groups in the [revision planner](/revision-planner/). Do not repeatedly read the full month when only a small group is weak.

When using time-sensitive information for an application or decision, confirm it with the examining body or the relevant official announcement. Preparation notes support study; they do not replace official instructions.` },
    ],
    checklist: ['Choose scope from your exam syllabus.', 'Turn each relevant event into a clear prompt.', 'Keep unknown details marked for checking.', 'Recall older items before collecting more.', 'Connect current events to useful static concepts.'],
    related: ['revision-without-forgetting', 'study-with-job-or-college', 'error-notebook-for-exam-preparation'],
  },
  {
    slug: 'error-notebook-for-exam-preparation',
    title: 'Make an error notebook that helps you fix repeated exam mistakes',
    description: 'A reusable error-log template, a worked percentage example and a skip-versus-attempt method for reducing avoidable mistakes.',
    audience: 'Students repeating the same mistakes',
    intro: 'An error notebook should tell you what to do differently next time. Copying a long solution often hides the actual mistake. Record the failed step, the corrected rule and a question to retry. Include correct guesses: they still reveal uncertain understanding.',
    sections: [
      { id: 'template', title: 'Use six fields that lead to a repair', body: `| Field | What to write |
| --- | --- |
| Topic and question | Enough detail to find it again |
| My first wrong step | The exact line or choice that failed |
| Error type | Concept, calculation, reading, recall or time decision |
| Correct rule | One sentence that changes the method |
| Retry prompt | A question to solve with the solution closed |
| Review result | Independent answer, guess or still unclear |

Use paper or your [revision notebook](/revision/). Keep the note short enough to reread before practice. If you need the whole solution, link to the question rather than copying every line.` },
      { id: 'worked-log', title: 'Record why the answer went wrong', body: `**Question:** A price rises 20% and then falls 20%. What is the net change?

**My wrong step:** I cancelled the two percentages and answered zero.

**Error type:** Concept.

**Correct rule:** Each percentage uses the quantity immediately before that change.

**Correct working:** Start at 100. After the rise it is 120. After the fall it is 96. The net change is a 4% fall.

**Retry prompt:** Try a 10% rise followed by a 10% fall. Starting at 100 gives 110 and then 99: a 1% fall.

This entry points to the changed base, not just the final answer. Revisit [percentage](/quant/percentage/) if you cannot explain that step.` },
      { id: 'repair-type', title: 'Match the repair to the error type', body: `A concept gap needs a lesson and a fresh example. A calculation error needs the exact calculation repeated carefully. A reading error needs the condition you overlooked written clearly.

For recall errors, turn the fact or formula into a closed-book prompt. For time decisions, record when you should have moved on. The same “practise more” advice does not fix every error.

Example: if a speed question uses metres while time is in hours, write “convert units before comparing rates”. Then solve a question with different units. That is more useful than writing “silly mistake”.` },
      { id: 'skip', title: 'Use a clear reason to skip a question', body: `Before investing more time, ask: “Do I know a valid first step?” If not, mark the question and move on when the interface allows it. Return after securing questions you can solve.

If the method is clear but the calculation is long, compare the remaining time with the rest of the section. Use your own practice timing to set checkpoints. A single seconds-per-question rule does not fit every exam or question.

For a scoring scheme with reward $R$, penalty $P$ and probability $p$ of being correct, the expected score is $pR - (1-p)P$. It becomes positive when $p > P ÷ (R+P)$.

For an illustrative reward of 2 and penalty of 0.5, the threshold is 0.2. This mathematical threshold is not a blanket guessing recommendation: your probability estimate can be wrong, time has a cost, and your exam may use different rules. Confirm its marking scheme first.` },
      { id: 'review', title: 'Retry errors until the corrected method is independent', body: `After recording an error, try a similar question. Return later to the original question with its solution hidden.

If you solve it only because you remember the option, change the numbers or explain every step. For grammar, make another sentence. For reasoning, rebuild the diagram from the clues.

Keep repeated errors in the next review group. Move a repaired error to a longer interval once you can explain and apply the rule independently. Use the [revision planner](/revision-planner/) and [revision method](/study-guides/revision-without-forgetting/) for reminders.` },
    ],
    checklist: ['Record the first failed step.', 'Review correct guesses too.', 'Choose a repair that matches the error.', 'Retry with the solution hidden.', 'Use question evidence to decide the next topic.'],
    related: ['revision-without-forgetting', 'maths-from-basics-for-competitive-exams', 'english-for-competitive-exams-beginners'],
  },
];

export const getStudyGuide = (slug: string) => STUDY_GUIDES.find((guide) => guide.slug === slug);
