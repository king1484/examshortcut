import type { SectionId } from '@/lib/sections';

/* Plain, well-established study technique, written once per subject area. The pages that use it
   put this beside topic-specific facts (counts, question types, traps), never on its own. */
export const PRACTICE_HABIT: Record<SectionId, { attempt: string; review: string }> = {
  quant: {
    attempt: 'Before calculating, write the set-up in one line: what the base or unknown is, what is asked, and which formula or table fraction applies. Calculate only after that, and finish by checking whether the size of the answer is sensible.',
    review: 'For every wrong answer, redo the question from a blank page and note whether the slip was in reading, in the set-up, or in arithmetic. The three need different fixes.',
  },
  reasoning: {
    attempt: 'Build the structure first: a diagram, table, chain or coded list drawn from the statement. Most wrong answers in reasoning come from reading the options before the structure exists.',
    review: 'After a miss, redraw the structure without looking at the solution, then compare. If the drawing was right but the answer was wrong, the slip was in reading off the conclusion.',
  },
  english: {
    attempt: 'Read the whole sentence or passage once for sense, name the rule or the evidence that decides the answer, and only then eliminate options against it. Guessing by sound is the habit to break.',
    review: 'For each miss, write the rule or the evidence line in your own words, then make a fresh example sentence that uses it. Recognising the right answer later is not the same as being able to apply the rule.',
  },
  ga: {
    attempt: 'Treat every question as a fact lookup: answer from memory before reading the options, then check. If you had to guess, count the question as a miss even when the guess was right.',
    review: 'Turn each miss into a one-line fact card that also names the option you confused it with. Revisit the cards after a few days, not straight away.',
  },
  computer: {
    attempt: 'Answer from memory first, then confirm. Attach each term to what it does and where you meet it (for example, which key, menu or device), because exam options are usually plausible neighbours of the right term.',
    review: 'For each miss, note the correct term and the wrong term you chose, and write the difference in one line. Repeat the set after a gap to see whether the line stuck.',
  },
};

export const FORMULA_HABIT: Record<SectionId, string> = {
  quant: 'Cover the right-hand side of each formula and reproduce it from its name, then check. A formula you can only recognise on the page will not come back under exam pressure. For each one, also say aloud which words in a question should make you reach for it.',
  reasoning: 'These are rules and short relations, not long derivations. Say each one in your own words, then build one tiny example of your own and check it against the rule.',
  english: 'Rules are easier to hold with a counter-example. For each rule, write one correct sentence and one that breaks it, then explain what changed.',
  ga: 'Where a topic has numbers, units or laws, learn the statement together with one real quantity or example it describes, so the relation is not memorised as bare symbols.',
  computer: 'Wherever a rule or relation appears, pair it with the thing it describes (a unit, a key, a device) and say both together.',
};

export const EXAMPLE_HABIT: Record<SectionId, string> = {
  quant: 'Cover the solution and attempt the question on paper first. Compare your first line with the first line of the solution: most gaps show up there, not in the arithmetic. Where a shortcut route is shown, redo the question that way once and note what condition made the shortcut safe.',
  reasoning: 'Draw your own diagram or table before opening the solution, then compare structures, not just final answers. If your structure differs but your answer matches, find out why before moving on.',
  english: 'Decide on an answer and name the rule or evidence behind it before reading the explanation. Then check that the explanation rules out each wrong option, not only that it supports the right one.',
  ga: 'Say the answer and one supporting fact before opening the explanation. The explanation is useful mainly for the neighbouring facts it brings in, so read those twice.',
  computer: 'Answer from memory, then read the explanation for the related terms around the answer. Those neighbours are what the wrong options are usually made from.',
};
