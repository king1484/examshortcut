"""Order-ranking topic: NOTES + PATTERNS (imported by order-ranking.py)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P  # noqa

NOTES = {}

NOTES["order-idea"] = """### Rank, position and order: the three conversions

Every question here involves a line of people (or a stack of objects) and a rank measured from one end. Three facts convert anything into anything.

**Fact 1 — the two ends are mirrors.** In a row of T people, the person r-th from the left is $(T - r + 1)$-th from the right. Example: 10th from the left in a row of 40 → $40 - 10 + 1$ = 31st from the right. The +1 exists because the person is counted once at each end.

**Fact 2 — two ranks make the total.** If one person is a-th from one end and b-th from the other end, the row holds

$$T = a + b - 1$$

Again the −1: the person was counted in both numbers. Example: 9th from the left and 11th from the right → $9 + 11 - 1$ = 19 people.

**Fact 3 — a swap copies positions.** When two people interchange places, each simply takes over the other's seat. To find a new rank, convert the other person's rank into the same end first: Shyam 9th from the right in a row of 25 → $25 - 9 + 1$ = 17th from the left; after a swap, Ram sits 17th from the left.

**Stacks and rows of objects.** Books, boxes and shelves follow the same logic vertically: 'above' is like 'to the left'. The only new skill is assembling a scattered description into one ordered list — draw the order top to bottom as each sentence arrives, then read the asked slot.

**Facing direction changes everything.** A row facing north has its left and right in the usual sense; a row facing **south** has them swapped (their left is your right). Questions flag this deliberately — underline the facing word before using any left/right clue.

**People ahead vs behind.** In a queue of T, a person r-th from the front has $r - 1$ people ahead and $T - r$ behind. The −1 on 'ahead' (the person is not ahead of themselves) is the most common slip in the whole topic.

### Quick revision
- Mirror: r-th from one end = $(T - r + 1)$ from the other.
- Total: $T = a + b - 1$ for ranks a and b from opposite ends of the same person.
- Swap: convert both people to the same end; each takes the other's number.
- Ahead = r − 1; behind = T − r.
- Facing south flips left/right — read the facing word first.

**Why the formulas work (and why that matters).** Every shortcut in this topic is bookkeeping on one sentence: *a rank is one more than the number of people before you.* The mirror formula is that sentence counted from the other side (the people before you become the people after you, plus you); the total formula is the two before-counts overlapping on you, hence −1. When an exam twists the wording ('four people between them', 'equal number ahead and behind'), derive the equation from this sentence instead of memorising a new formula — it takes ten seconds and never breaks.

**The twisted variants worth pre-solving.** 'Equal ahead and behind' → $r - 1 = T - r$ → $T = 2r - 1$. 'k people between A and B, same end' → $b = a + k + 1$. 'A is exactly in the middle of an odd row' → $r = (T+1)/2$. Practise these three derivations once and the variants stop costing time."""

NOTES["rank-position"] = """### Single-person rank work

This subtopic drills the conversions one person at a time: one end to the other, two ends to the total, and the moving-queue variants where people join or leave.

**The mirror conversion.** From-rank r in a row of T: other end = $T - r + 1$. Practical route: rank from bottom = class size − rank from top + 1. A 23rd-from-the-top rank in a class of 60 is 38th from the bottom: $60 - 23 + 1 = 38$.

**The total from two ends.** When the question gives one person's rank from both ends, the class size pops out: $T = a + b - 1$. Sonu 14th from the left and 20th from the right → $14 + 20 - 1 = 33$ people. Sanity-check the answer: it must be at least as big as each rank.

**Queues that change size.** People joining the front shift everyone back; people leaving the front pull everyone forward. Rule: adjust the *number of people before the person* first, then add one.
- k people join **ahead** of you → new rank = old + k.
- k people **leave from ahead** of you → new rank = old − k.
- If the joiners/leavers are behind you, your rank does not change.

**People leaving mid-queue.** '5 people left the row from the left side': anyone to the right of them slides left by 5. A person 16th from the left becomes 11th. Anyone to the **left** of the departed block keeps their rank but the total shrinks.

**Ranks from both ends together.** Some questions hand you rank from the top *and* from the bottom of a class with a twist ('A is 12th from the top and 41st from the bottom; how many students are there?'). Same formula: $12 + 41 - 1 = 52$.

**Watch the units.** 'Rank' counts the person; 'people ahead/behind' does not. Convert explicitly: ahead = rank − 1; rank = ahead + 1. Questions swap these words between the question and the options on purpose.

### Quick revision
- Other end: $T - r + 1$. Two ends: $T = a + b - 1$.
- Joiners ahead: rank + k. Leavers ahead: rank − k. Changes behind you: no change.
- Mid-row exits: slide only people to the right of the exit block.
- ahead = rank − 1, behind = T − rank; convert words to numbers before computing.

**Two-sided puzzles.** Harder variants give a rank from one end plus a second fact ('he is exactly midway', 'there are 3 people between him and the front'). Convert the fact into a before-count first: 'midway' means ahead = behind; '3 between him and the front' means ahead = 4. Once the before-count is known, rank = before + 1 and the total follows if the other side is described.

**Class ranks vs rows.** The formulas are identical; only the words move (top/bottom instead of left/right, pass/fail groups at the ends). One warning: 'X failed' questions where 'rank from the bottom among failures' is asked — strip the failed students out of the total before mirroring. The formula never changes, but the total does."""

NOTES["between-overlapping"] = """### Counting between two people

Four shapes cover every 'how many between' question. Know which end each rank comes from — that decides the formula.

**Shape 1 — both ranks from the same end.** A is a-th and B is b-th from the left:

$$\\text{between} = |a - b| - 1$$

The gap shrinks by one because 'between' excludes both people. Example: 9th and 26th from the top → 16 between.

**Shape 2 — ranks from opposite ends.** Convert one rank to the shared end first, or use the total. In a row of T with P a-th from the left and Q b-th from the right:

$$\\text{between} = T - a - b$$

Example: row of 45, X 14th from the left, Y 18th from the right → $45 - 14 - 18 = 13$. If the total is not given, build it with $a + b - 1$ from any person who has both ranks.

**Shape 3 — the middle person.** Both from the same end a and b: the midpoint rank is $(a + b) / 2$ from that end. 9th and 21st from the left → the middle person is 15th from the left. If a + b is odd, the exact middle is a half-position — exams phrase those as 'immediately between', and the two neighbours are $(a+b-1)/2$ and $(a+b+1)/2$.

**Shape 4 — the overlap deduction.** The classic: 'Ram is 17th from the left, Shyam 9th from the right; after interchanging, Ram is 22nd from the left.' Ram takes Shyam's seat, keeping Shyam's from-right rank (9): total $= 22 + 9 - 1 = 30$. Then Shyam's old seat was $30 - 9 + 1 = 22$nd from the left, and the original gap is $22 - 17 - 1 = 4$. Overlap questions always split into: build the total first, then run a plain Shape 1 or 2 count.

**Sanity checks.** Between-counts can never be negative — a negative answer means the two ranks described the same person or the ranks were from ends you did not account for. And between + 2 ≤ total: the two people themselves exist too.

### Quick revision
- Same end: $|a-b| - 1$. Opposite ends (total T): $T - a - b$.
- Middle person (same end): $(a+b)/2$ from that end.
- Overlap puzzles: recover T first ($a' + b' - 1$), then count between.
- Convert every rank to the same end before subtracting; 'between' excludes both people.
- Negative gap = misread ends; stop and re-convert.

**A worked flow for exam speed.** Read the question once, labelling each rank with its end (L/R or T/B) and circling the total if present. Then one line of arithmetic:
- same end → subtract, drop 2 (|a−b| − 1);
- opposite ends → subtract from the total;
- no total → build it from any both-ends person (a + b − 1).
Under exam pressure the labelling step is what prevents the classic error of subtracting ranks that came from different ends.

**Between-counts with a twist.** Questions sometimes ask 'how many people do NOT lie between them' (= total − between − 2) or 'what fraction of the row lies between'. Both are one extra subtraction on the between-count — compute between first, always, then answer the actual question."""

NOTES["arrangement-comparison"] = """### 'Taller than, older than, scored more than': ranking from clues

These puzzles give scattered comparisons and ask for a slot: tallest, second oldest, least scorer. The method is always the same — merge the clues into one ordered line, then read it.

**The chain-building routine.**
1. Write each clue as an arrow: 'A is taller than B' → A > B.
2. Join arrows that share a head or tail into one long chain. A > B and B > D merges to A > B > D.
3. Where the chain is under-determined (two people never compared), the answer is 'cannot be determined' — but check the question first: many slots are fixed even when the full order is not.
4. Read the asked slot from the finished chain: tallest = left end, shortest = right end, second tallest = second from the left.

**Marks and scores.** 'Scored more' behaves exactly like 'taller'. Beware the reversed words: 'fewer than', 'younger than', 'less than' point the arrow the other way. Convert every clue into > arrows pointing at the *better/bigger/older* person before merging.

**Under-determined traps.** Five clues about four people can still leave a free pair: 'A > B, C > D' says nothing about A vs C. If the question asks for the tallest and only one candidate can possibly top the chain (everyone else has someone above them), the answer stands even without a total order. Rule: fix the slot, not necessarily the list.

**Objects in columns and shelves.** 'The red box is above the blue box' is a comparison with the arrow pointing up. Stack the chain top to bottom and read positions ('third from the top') exactly as you read 'second tallest'.

**Facing pairs.** Two people facing **each other** (like a north-facing and a south-facing person) have opposite left/right directions: the north-facing person's left is the south-facing person's right. Draw the two arrows before using any such clue.

### Quick revision
- Every clue → an arrow toward the bigger/older/better; join arrows into one chain.
- Read the slot: tallest = chain head, Nth = Nth from the head.
- Reversed words (less, younger, fewer, shorter) flip the arrow — convert first.
- A slot is answerable when only one person can fill it, even if the whole order is open.
- Stacks: 'above' is the arrow; facing pairs have mirrored left/right.

**Extraction habits that prevent wrong chains.** Rewrite every clue as a two-symbol line before thinking: 'Sunil is younger than Vijay' → S < V. Keep the inequality signs pointing the same way throughout (bigger/older/higher on the left). Most wrong answers here come from reading a reversed sentence ('younger than', 'fewer than', 'below') in its surface direction — the rewrite step makes the reversal visible.

**When options expose the shortcut.** If two options share a person ('C' and 'C is second oldest'), the chain probably pins that person; test the slot directly: can anyone else occupy slot 2? If nobody can, stop building the chain and mark the answer — total order is a luxury, the slot is the requirement."""

PATTERNS = {}

PATTERNS["order-idea"] = [
    P("oi-p1", "Rank flips between the two ends", "very common",
        "One rank and the total are given; the same person's rank from the other end is asked.",
        "1. Other end = total − rank + 1.\n2. Keep the +1: the person sits at both counts.\n3. For queues: ahead = rank − 1, behind = total − rank.\n\n*Why it works:* the two counts meet at the same person.",
        "**In a row of 40 students, Ravi is 10th from the left. What is his position from the right?**",
        "$40 - 10 + 1$ = **31st** from the right.", None),
    P("oi-p2", "Total from two opposite ranks", "very common",
        "One person's rank from both ends is given; the size of the row/class is asked.",
        "1. Total = a + b − 1.\n2. Sanity-check: total ≥ each rank.\n3. Works for rows, queues and class ranks alike.\n\n*Why it works:* the person was counted once in each rank; subtract the double count.",
        "**A student is 23rd from the left and 12th from the right. How many students are in the row?**",
        "$23 + 12 - 1$ = **34**.", None),
    P("oi-p3", "Interchange of positions", "common",
        "Two people swap places; a new rank after the swap is asked.",
        "1. Convert the partner's rank to the asked end (mirror if needed).\n2. The swapper now holds exactly that converted number.\n3. The other person takes the first person's old number.\n\n*Why it works:* a swap is a copy of positions between two people.",
        "**In a row of 25, Ram is 8th from the left and Shyam is 9th from the right. They swap places. What is Ram's new position from the left?**",
        "Shyam's seat: $25 - 9 + 1$ = 17th from the left → Ram now **17th**.", None),
    P("oi-p4", "Assembling a scattered stack or row", "common",
        "Objects/friends described by above-below or left-right clues; a slot or extreme is asked.",
        "1. Convert each clue into order arrows (above = >).\n2. Merge into one list, drawing as you read.\n3. Read the asked slot off the finished list.\n\n*Why it works:* scattered clues describe one total order; drawing recovers it.",
        "**Red is above Blue; Green is below Blue but above White; Yellow is at the bottom. Which box is at the top?**",
        "Red > Blue > Green > White > Yellow → top = **Red**.", None),
]

PATTERNS["rank-position"] = [
    P("rp-p1", "Rank from the other end", "very common",
        "Class/queue size known; rank from top/left/front given; the mirror rank is asked.",
        "1. Apply total − rank + 1.\n2. Read the end words carefully (top↔bottom, left↔right, front↔back).\n\n*Why it works:* the two counts meet at the same person.",
        "**In a class of 60, Neha ranks 23rd from the top. What is her rank from the bottom?**",
        "$60 - 23 + 1$ = **38th**.", None),
    P("rp-p2", "Total from two ranks", "very common",
        "One person's rank from both ends is given; the total is asked.",
        "1. Add the ranks, subtract 1.\n2. Check the total is not smaller than either rank.\n\n*Why it works:* the shared person is counted twice.",
        "**Sonu is 14th from the left and 20th from the right in a row. How many people are in the row?**",
        "$14 + 20 - 1$ = **33**.", None),
    P("rp-p3", "Queue joining and leaving", "common",
        "People join or leave a queue; the person's new position is asked.",
        "1. Count only people **ahead**: rank = (people ahead) + 1.\n2. k join ahead → +k; k leave from ahead → −k.\n3. Changes behind the person never move their rank.\n\n*Why it works:* a rank is one more than the number of people ahead.",
        "**In a queue of 35, Moni is 12th. If 8 people ahead of her leave, what is her new position?**",
        "$12 - 8$ = **4th**.", None),
    P("rp-p4", "Rank after people leave mid-row", "common",
        "Some people exit from one side of a standing row; a survivor's new rank is asked.",
        "1. If the exits are to the person's left, subtract the count.\n2. If they are to the right, the rank from the left is unchanged.\n3. Recompute the total if it is asked.\n\n*Why it works:* survivors slide toward the emptied side.",
        "**A is 16th from the left in a row of 40. If 5 people leave from the left end, what is A's new rank from the left?**",
        "The 5 departed were all ahead of A → $16 - 5$ = **11th**.", None),
]

PATTERNS["between-overlapping"] = [
    P("bo-p1", "Between, same end", "very common",
        "Both ranks measured from the same end (top, left, front).",
        "1. Between = |a − b| − 1.\n2. 'Between' excludes both named people.\n3. Absolute value: either rank may be bigger.\n\n*Why it works:* the gap between two positions minus the two endpoints.",
        "**R ranks 9th from the top and S ranks 26th from the top. How many students are between them?**",
        "$|26 - 9| - 1$ = **16**.", None),
    P("bo-p2", "Between, opposite ends", "very common",
        "One rank from the left/top, the other from the right/bottom, total known.",
        "1. Between = total − rank1 − rank2.\n2. If no total is given, build one from a both-ends person first.\n3. Negative result = you misread the ends.\n\n*Why it works:* subtract both people and the ends from the row.",
        "**In a row of 45, X is 14th from the left and Y is 18th from the right. How many people are between them?**",
        "$45 - 14 - 18$ = **13**.", None),
    P("bo-p3", "Middle person between two ranks", "common",
        "'Who/which position is exactly in the middle of A and B?'",
        "1. Convert both ranks to the same end.\n2. Middle position = (a + b) / 2 from that end.\n3. Odd sum → the two immediate neighbours share the middle; read the options.\n\n*Why it works:* the midpoint of two positions is their average.",
        "**A is 9th from the left and B is 21st from the left. Which position is exactly in the middle?**",
        "$(9 + 21)/2$ = **15th from the left**.", None),
    P("bo-p4", "Overlap: swap reveals the total", "common",
        "A swap or second measurement exposes a rank the row never stated; count between in the original line.",
        "1. The swapped person keeps the partner's from-end rank: total = new rank + partner's rank − 1.\n2. Convert everyone to one end.\n3. Between = |a − b| − 1 as usual.\n\n*Why it works:* the swap pins a second measurement to the same seat, fixing the row size.",
        "**Ram is 17th from the left, Shyam 9th from the right. After interchanging, Ram is 22nd from the left. How many students sat between them originally?**",
        "Total $= 22 + 9 - 1 = 30$. Shyam's old seat = $30 - 9 + 1 = 22$nd from the left. Between = $22 - 17 - 1$ = **4**.", None),
]

PATTERNS["arrangement-comparison"] = [
    P("ac-p1", "Height/size chain to a slot", "very common",
        "'A is taller than B...' — find the tallest, shortest or an exact slot.",
        "1. Write each clue as an arrow toward the taller.\n2. Merge into one chain; read slot from the end.\n3. If a pair is never compared but only one person can top the chain, that person is the answer.\n\n*Why it works:* 'taller than' is a total-order arrow; chains merge head to tail.",
        "**A is taller than B; C is taller than A; D is shorter than B. Who is the shortest?**",
        "C > A > B > D → shortest = **D**.", None),
    P("ac-p2", "Marks ranking", "very common",
        "'Scored more/less than' clues; highest, lowest or Nth scorer is asked.",
        "1. Convert 'scored less' clues so all arrows point toward more marks.\n2. Merge; read the slot from the top end.\n3. Double-check nobody outside the chain could beat the head.\n\n*Why it works:* scores order exactly like heights.",
        "**A scored more than B; C scored less than D; B scored more than D. Who scored the least?**",
        "A > B > D > C → least = **C**.", None),
    P("ac-p3", "Age ranking", "common",
        "'Older/younger than' clues about three to six people.",
        "1. Point every arrow at the older person.\n2. Merge and read: oldest at the head, youngest at the tail.\n3. Watch 'younger' — it reverses the sentence's surface order.\n\n*Why it works:* ages are another total order.",
        "**Rahul is older than Vijay; Sunil is younger than Vijay; Anil is older than Rahul. Who is the youngest?**",
        "Anil > Rahul > Vijay > Sunil → youngest = **Sunil**.", None),
    P("ac-p4", "Stacked objects and shelves", "common",
        "Boxes/books/subjects with above-below clues; a slot from the top or bottom is asked.",
        "1. Treat 'above' as > pointing upward.\n2. Build the stack top to bottom on paper.\n3. Slots: Nth from the top = Nth of the list; from the bottom = mirror.\n\n*Why it works:* vertical stacks obey the same order logic as lines.",
        "**Civics is below Geography; History is below Economics but above Geography; Political Science is at the bottom. Which subject is third from the top?**",
        "Economics > History > Geography > Civics > Political Science → third = **Geography**.", None),
]

PYQS = [
    ("Rank conversion at the two ends", "very common", "order-idea",
     "A rank from one end plus a total; the other end is asked.",
     "Mirror: total − rank + 1; queues: ahead = rank − 1, behind = total − rank.",
     "**In a queue of 60, S is 21st from the front. How many people are behind her?**",
     "$60 - 21$ = **39** behind."),
    ("Two ranks to the total", "very common", "rank-position",
     "One person's rank from both ends; class size asked.",
     "Add the ranks and subtract 1; the shared person was counted twice.",
     "**A is 9th from the left and 11th from the right. How many people are in the row?**",
     "$9 + 11 - 1$ = **19**."),
    ("Counting between two ranks", "very common", "between-overlapping",
     "'How many between A and B' with ranks from the same or opposite ends.",
     "Same end: |a − b| − 1. Opposite ends with total T: T − a − b. Convert ends before subtracting.",
     "**P is 11th from the left and Q is 9th from the right in a row of 30. How many sit between?**",
     "$30 - 11 - 9$ = **10**."),
    ("The middle person", "common", "between-overlapping",
     "'Who is exactly in the middle of A and B?'",
     "Convert to the same end; the midpoint is (a + b) / 2 from that end.",
     "**Manish is 14th from the left; Rakesh is 8th from the right in a row of 35. Who is midway between them?**",
     "Rakesh = $35 - 8 + 1 = 28$th from the left; midway = $(14 + 28)/2$ = **21st from the left**."),
    ("Comparison chain to a named slot", "very common", "arrangement-comparison",
     "Taller/older/more-marks clues; tallest, youngest or Nth is asked.",
     "Arrows toward the bigger/older/better; merge into a chain; read the slot; reversed words flip the arrow.",
     "**M > N; O < N; P > M; Q < O. Who is second highest?**",
     "P > M > N > O > Q → second highest = **M**."),
    ("Scattered stack assembly", "common", "arrangement-comparison",
     "Above/below clues for boxes, books or shelves; a slot is asked.",
     "Above = arrow up; stack the chain on paper; read 'Nth from top' directly off the list.",
     "**Red above Blue; Green below Blue but above White; Yellow at the bottom. Which is second from the top?**",
     "Red, Blue, Green, White, Yellow → second = **Blue**."),
]
