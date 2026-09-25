# -*- coding: utf-8 -*-
"""Notes, patterns and pyqPatterns for seating-arrangement.json (imported by seating-arrangement.py)."""
from _lib import P, PYQ

NOTES_IDEA = r"""### What a seating puzzle is
You get a group of people and a list of clues about where they sit. Your job is to rebuild the one seating that fits every clue, then answer questions such as "who sits second to the right of D?" or "how many people sit between P and T?". There is no trick of calculation here. The whole skill is reading each clue correctly and drawing it the same way every time.

### Left and right depend on the direction you face
This is the source of most wrong answers.
- **Facing north (the default in a row):** your left is the west end of the row, your right is the east end. Draw the row left to right on paper and the person's left is simply your left.
- **Facing south:** everything flips. The person's left is the east end, their right is the west end. If you draw the row as usual, a south-facing person's "right" is to your left on paper.
- **Rule of thumb:** if the question says "facing south" or "facing away from the viewer", draw a small down-arrow on every seat and read left and right from that arrow, not from your own hands.

### Circles
- **Facing the centre:** left = clockwise, right = anticlockwise.
- **Facing outward:** left = anticlockwise, right = clockwise.
- A circle has no ends and no fixed first seat. Place the first named person anywhere; every other seat is fixed relative to that one.
- "Opposite" exists only when the number of seats is even. With n seats, the person opposite is n ÷ 2 places away in either direction.

### Counting words
- **"Second to the right of X"** means one person sits between X and that seat.
- **"k-th to the left"** means k steps, so there are k − 1 people in between.
- **"Immediately between X and Y"** means X and Y are the two neighbours of the middle person.
- **"Between X and Y"** without "immediately" means somewhere strictly inside the stretch from X to Y.
- **Position from the ends:** in a row of n people, the person p-th from the left is (n − p + 1)-th from the right.
- **People between two seats** at positions a and b = |a − b| − 1.

### Worked example
Five people sit in a row facing north. T sits in the middle. U sits second to the right of T. V sits to the immediate left of T.
- Seats 1 to 5 from left: T = 3.
- U = 3 + 2 = 5 (right end). V = 2.
- Two seats remain: 1 and 4. If the question adds "W is not at an end", then W = 4 and X = 1.

Now turn the same row to face south. T is still in seat 3. U, "second to the right" of a south-facing T, is two seats to the west, so U = 1. V, "immediately left" of T, is at seat 4. One word changed and the whole answer changed.

### The three-step method
1. **Fix the frame.** Draw the seats first: a line of n boxes, or a circle with n marks. Write the facing direction on the frame.
2. **Place the sure clues first.** Ends, the middle seat, "k-th from the left end". These need no guessing.
3. **Attach the chains.** "A is left of B, B is second right of C" — hang each new person on someone already placed. Use negative clues ("not at an end", "not a neighbour of D") to kill the extra cases at the end.

### Quick revision
- North-facing row: person's left = your left. South-facing row: person's left = your right.
- Circle facing centre: left = clockwise. Facing outward: left = anticlockwise.
- k-th to the right means k − 1 people in between.
- p-th from left in a row of n = (n − p + 1)-th from right; people between seats a and b = |a − b| − 1.
- Draw the frame, place fixed clues, hang chains, then use the "not" clues.
"""

NOTES_LINEAR = r"""### The frame
Number the seats 1 to n from the west (left) end for a north-facing row. Write the numbers under the boxes. Every clue then becomes a small equation on seat numbers, which is far safer than moving letters around in your head.

For north-facing people:
- "B is k-th to the right of A" → B = A + k.
- "B is k-th to the left of A" → B = A − k.
- "A is at an end" → A = 1 or A = n.
- "p-th from the right end" → seat n − p + 1.

For south-facing people the signs flip: "k-th to the right" → B = A − k.

### Order of attack
1. **Absolute clues** (ends, middle, "third from the left") go in first.
2. **Distance clues attached to a placed person** come next. "D is fourth to the right of C" with C at seat 1 gives D = 5 straight away.
3. **Floating chains.** If a clue links two people who are not yet placed, write the block (for example "P _ Q") on the side. Then slide it along the free seats to see where it fits.
4. **Negative clues last.** "Not at an end", "not a neighbour of", "not adjacent to" usually leave exactly one case standing.

### Worked example
Seven people C, A, B, D, E, F, G sit in a row facing north. C sits at the left end. F is fourth to the right of C. A is second to the left of F. D sits immediately right of F. G is not at an end. B is a neighbour of C.
- C = 1, F = 1 + 4 = 5, A = 5 − 2 = 3, D = 6.
- B neighbours C, so B = 2.
- Seats 4 and 7 remain for E and G. G is not at an end, so G = 4 and E = 7.
- Row: C B A G F D E. Third to the right of A is seat 6 = D.

### Case splitting
When a clue allows two places ("A sits at one of the ends"), draw **two rows** side by side, one per case, and carry both until a clue breaks one. Never guess one case and hope. The typical exam puzzle leaves 2 cases after the first few clues and one negative clue settles it.

### Blocks and gaps
- "X sits immediately between Y and Z" makes a three-seat block, but Y and Z can be on either side. Keep both orders open unless another clue fixes them.
- "Exactly two people sit between A and B" means |A − B| = 3. It does not tell you who is on the left.
- A block of size k in a row of n has n − k + 1 possible starting seats. List them quickly and strike out the ones that clash.

### Facing south
If everyone faces south, you can either use the flipped equations or draw the row from east to west so that the person's left becomes your left again. Choose one method and stick to it. Mixing them in the middle of a puzzle is the commonest source of a mirror-image answer.

### Negative clues work hard
"D is not a neighbour of A" looks weak, but in a nearly-full row it often removes a whole case. When two seats and two people are left, a single "not at an end" decides both.

### Answering the question
Read the question twice. "Second to the right of W" in a north-facing row is seat W + 2. "How many people sit between F and E" is |F − E| − 1, not |F − E|. The number of seats between two people and the number of people between them are the same only when the row is full.

### Quick revision
- North-facing: right = +k, left = −k on seat numbers. South-facing: signs flip.
- Absolute clues → attached distances → floating blocks → negative clues.
- Two possible places = two drawn rows; strike one out with a later clue.
- "Immediately between" = a 3-block with the ends swappable.
- People between = |a − b| − 1.
"""

NOTES_CIRCULAR = r"""### Fixing a circle
A circle has no first seat, so every arrangement can be rotated. Remove that freedom at once: put the first person named in a clue at the top of the circle. Now every other seat is fixed relative to that person.

Mark the direction on your drawing:
- **Facing the centre:** left neighbour = clockwise, right neighbour = anticlockwise.
- **Facing outward:** left neighbour = anticlockwise, right neighbour = clockwise.

A quick check: stand at the bottom of the circle facing the centre (north). Your left hand points west. Moving from the bottom towards the west side is the clockwise direction when the circle is seen from above.

### Opposite seats
With n seats (n even), the person opposite X is n ÷ 2 places away. In a circle of 6 it is 3 places, in a circle of 8 it is 4 places. "Opposite" clues are the strongest clues in a circle because they fix a seat exactly. Place them before "left" and "right" clues whenever you can.

With an odd number of seats there is no opposite. If a question with 5 or 7 people asks who is opposite someone, re-read it: it is probably a mistake of reading, not a trick.

### Counting both ways
In a circle there are two paths between any two people. "How many people sit between A and D?" usually means **along the shorter side**, or the question says "counting clockwise from A". In a circle of n, if D is k-th to the left of A, D is also (n − k)-th to the right of A.

### Worked example
Eight people A to H sit around a circle facing the centre. A sits opposite E. B is second to the right of A. F sits opposite B. C sits immediately left of E. D sits opposite C. G is not a neighbour of A.
- Put A at seat 0 and number seats 0 to 7 clockwise. E = 4 (opposite).
- Facing centre, right = anticlockwise. B = second right of A = seat 6. F = seat 2.
- C = immediate left of E = seat 5 (clockwise from 4). D = opposite C = seat 1.
- Seats 3 and 7 remain for G and H. Seat 7 neighbours A, so G = 3 and H = 7.
- Third to the left of H: 7 → 0 → 1 → 2, so it is F.

### Outward and mixed facing
If everyone faces outward, just swap the rule: left = anticlockwise. If some face the centre and some face outward, write a small arrow at each person as soon as you place them, and read each clue from **that person's** own direction. "Q is immediately right of P" depends on how P faces, not how Q faces.

### Neighbour clues
- "X is a neighbour of Y" or "X sits next to Y" does not tell you which side. Keep both until another clue decides.
- "X sits between Y and Z" in a circle normally means immediately between.
- "Y and Z are not neighbours" is the most useful clue for the last two seats.

### Couples and attributes
Some circle puzzles add a second layer: couples, colours, cities or professions. Solve the seats first with the position clues. Then fill the attribute grid, one row per person. The attribute clues that name a seat relation ("the person who likes red sits opposite B") should be applied only after the seats are fixed.

### Quick revision
- Fix the first person at the top; the circle cannot rotate after that.
- Facing centre: left = clockwise. Facing outward: left = anticlockwise.
- Opposite = n ÷ 2 places away; place opposite clues first.
- k-th left = (n − k)-th right in a circle of n.
- Mixed facing: read each clue from the named person's own direction.
"""

NOTES_STRATEGY = r"""### How seating sets appear in exams
Seating questions come in sets of 3 to 5 questions on one puzzle. The first question takes the time; the others should take 10 to 20 seconds each if the puzzle is solved fully. So the real skill is solving the whole arrangement once and cleanly.

### Budget and order
1. **Read every clue once before drawing.** Count the people and seats. Note the facing direction. Look for clues that fix a seat outright.
2. **Build the frame** (row, circle or two rows) and write the direction on it.
3. **Place fixed clues, then chains, then negative clues.**
4. **Write the final arrangement neatly** before reading the questions. Most wrong answers in a set come from answering off a half-finished rough drawing.

### Two parallel rows
Two rows of m people face each other: row 1 faces south, row 2 faces north. The person at seat i of row 1 faces the person at seat i of row 2.
- A south-facing person's left is the east end. So "A is to the immediate right of B" in the south-facing row means A is one seat west of B.
- "P faces A" links the two rows directly: P and A share the same seat number.
- The two ends of both rows line up. "Sits at an end" in either row means seat 1 or seat m.

### Solve once, answer many
Typical follow-up questions:
- **Who sits k-th left/right of X** — read off the final drawing.
- **Which statement is true** — check each option against the drawing; exactly one should match.
- **If X and Y interchange seats** — swap only those two, keep everyone else, then read the new neighbour.
- **Odd one out** — four pairs of people; three share a relation (say, both at ends or both second to the right), one does not.

### Counting arrangements
A few questions ask "in how many ways" instead of "who".
- n people in a row: n! ways. With A and B together: treat AB as one block, (n − 1)! × 2.
- n people in a circle (rotations counted as the same): (n − 1)! ways.
- Fixed clues cut the count: each fixed seat removes a person and a seat from the free pool.
- Always list small cases if the numbers are small; it is quick and it catches double counting.

### Attribute grids
When each person also has a drink, city, colour or job, draw a grid: people down the side, seat and attribute across the top. Each clue either fixes a cell or rules one out. Seat clues and attribute clues work together: "the tea drinker sits at the left end" tells you the seat of the tea drinker, not the name. Tie the attribute to a name only when another clue joins them.

### Where time is lost
- Mirror images: reading a south-facing left as your own left.
- Assuming "between" means "immediately between".
- Forgetting that "neighbour" allows two sides.
- Treating "k-th to the left" as k people in between (it is k − 1).
- Answering from a case that a later clue had already struck out.

### Quick revision
- Read all clues, build the frame with the facing direction, then fill.
- Two rows: seat i of the south row faces seat i of the north row; south-facing left is east.
- Solve fully once; then each follow-up is a 15-second lookup.
- Circle of n: (n − 1)! arrangements; row: n!; a block of 2: (n − 1)! × 2 in a row.
- Attribute grid: people × (seat, attribute); fix names only when a clue joins them.
"""

P_IDEA = [
 P("st-p1", "Facing direction and left/right", "very common",
   "The question says 'facing north' or 'facing south' and asks for a left or right neighbour or an end.",
   "Facing north: person's left = the west end. Facing south: person's left = the east end. Draw a direction arrow on the row before placing anyone.",
   "Four people face south. Q is immediately right of P, R immediately left of P, S immediately right of Q. Who is at the western end?",
   "Facing south, right = west. From east to west: R, P, Q, S. So **S** is at the western end.",
   "south-facing: right = west, left = east"),
 P("st-p2", "Counting people between two seats", "very common",
   "Asks 'how many people sit between X and Y' or 'how many sit to the right of X'.",
   "Give every person a seat number. People between seats a and b = |a − b| − 1. People to the right of seat a in a row of n (facing north) = n − a.",
   "Five people in a row facing north: A at the left end, C fourth to the right of A. How many sit between A and C?",
   "A = 1, C = 5. Between = 5 − 1 − 1 = **3**.",
   "between = |a − b| − 1"),
 P("st-p3", "Position from either end", "common",
   "A person is described as 'third from the left' or 'second from the right end'.",
   "In a row of n, p-th from the left = (n − p + 1)-th from the right. Turn every such clue into a seat number first.",
   "Six people in a row: P is third from the left. What is P's position from the right?",
   "6 − 3 + 1 = **4th** from the right.",
   "from right = n − p + 1"),
 P("st-p4", "Circle facing rules", "very common",
   "People sit around a circle facing the centre or facing outward.",
   "Facing centre: left = clockwise, right = anticlockwise. Facing outward: the reverse. Fix the first person at the top to remove rotation.",
   "Four people sit around a table facing the centre. B is immediately left of A and C is opposite A. Who is immediately right of A?",
   "A at the top. B clockwise from A, C opposite A, the last seat (anticlockwise from A) is **D**.",
   "centre: left = clockwise"),
]

P_LINEAR = [
 P("st-p5", "Ends and adjacency", "very common",
   "Clues put people at the ends and name immediate neighbours.",
   "Place the end people first, then hang immediate neighbours on them. The last one or two seats are settled by elimination.",
   "Five people face north. A and E sit at the ends, A not at the right end. B is immediately right of A and C immediately left of E. Who is second to the left of E?",
   "A B _ C E; D takes seat 3. Second left of E (seat 5) is seat 3 = **D**."),
 P("st-p6", "Fixed distance chains", "very common",
   "Clues like 'F is fourth to the right of C', 'A is second to the left of F'.",
   "Turn each clue into seat arithmetic (+k right, −k left for north-facing) and follow the chain from the first fixed person.",
   "C at the left end of a 7-seat row; F fourth right of C; A second left of F. Where is A?",
   "C = 1, F = 5, A = **3**.",
   "right = +k, left = −k (north)"),
 P("st-p7", "South-facing rows", "common",
   "All people in the row face south.",
   "Flip the signs: k-th to the right = k seats towards the west. Or draw the row east-to-west so the person's left is your left.",
   "Five people face south. C is in the middle and A is second to the right of C. At which seat from the west is A?",
   "Right of a south-facing person = west. A = 3 − 2 = seat **1** (the western end).",
   "south: right = −k on west-to-east numbering"),
 P("st-p8", "Negative clues settle the case", "common",
   "Clues say 'not at an end', 'not adjacent to', 'not a neighbour of'.",
   "Place positive clues first, keep all cases open, then apply each 'not' clue to strike cases out. The last two seats are almost always decided by one such clue.",
   "Five people face north. B at the right end, C second left of B, A not at an end, D not adjacent to C, E not adjacent to B. Who is immediately right of C?",
   "B = 5, C = 3. Left: 1, 2, 4. D not next to C → D = 1. E not next to B → E = 2. A = 4. Right of C = **A**."),
]

P_CIRC = [
 P("st-p9", "Chains around a circle facing the centre", "very common",
   "Clues link neighbours ('A is immediately left of B', 'D is second right of B').",
   "Fix one person, then walk clockwise for 'left' and anticlockwise for 'right'. Fill the remaining seat last.",
   "Five people face the centre. A is immediately left of B, C is immediately left of A, D is immediately right of B. Who is immediately right of D?",
   "Clockwise from B: A, C. Anticlockwise from B: D. Five seats → clockwise B A C E D. Right of D (anticlockwise) is **E**.",
   "left = clockwise (facing centre)"),
 P("st-p10", "Opposite pairs", "very common",
   "Even number of seats with 'sits opposite' clues.",
   "Opposite = n ÷ 2 places away. Place all opposite pairs first; they pin seats exactly.",
   "Six people face the centre. A opposite B, C opposite D, E immediately left of A, C immediately left of E. Who is second to the left of F?",
   "Clockwise from A: A E C B F D. Second left of F: F → D → **A**.",
   "opposite = n/2 places"),
 P("st-p11", "Facing outward", "common",
   "Everyone faces away from the centre.",
   "Left = anticlockwise, right = clockwise. Write this on the frame before starting.",
   "Five people face outward. C is second to the right of A. Moving clockwise from A, where is C?",
   "Outward: right = clockwise. C is **two seats clockwise** from A."),
 P("st-p12", "Mixed facing", "occasional",
   "Some people face the centre and some face outward.",
   "Mark an arrow at each person. Read every clue from the named person's own direction.",
   "In a circle of 4, A faces the centre and B faces outward. B is immediately left of A. Where is B?",
   "A faces the centre, so A's left is clockwise: B is one seat **clockwise** from A."),
]

P_STRAT = [
 P("st-p13", "Two parallel rows facing each other", "very common",
   "Two rows; one faces north, the other south; 'X faces Y' clues.",
   "Seat i of the south-facing row faces seat i of the north-facing row. South-facing left = east. Use 'faces' clues to jump between rows.",
   "Row 1 (A, B, C) faces south, row 2 (P, Q, R) faces north. B is in the middle of row 1, A immediately right of B, R faces A. Q is not at an end. Who faces P?",
   "B = 2, A = 1 (right of south-facing = west). R = 1, Q = 2, P = 3. Seat 3 of row 1 is **C**."),
 P("st-p14", "Solve once, answer many", "very common",
   "A set of questions: true statement, interchange, odd one out.",
   "Finish the whole arrangement neatly first. Then check each option against the final drawing; for 'interchange' swap only the two named people.",
   "Five people face north: P Q R T S. If P and T swap seats, who is immediately left of P?",
   "After the swap: T Q R P S. Left of P = **R**."),
 P("st-p15", "Counting arrangements", "occasional",
   "Asks 'in how many ways' instead of 'who'.",
   "Row: n!. Circle: (n − 1)!. A block of two in a row: (n − 1)! × 2. Remove every fixed person and seat before counting.",
   "In how many ways can 4 people sit in a row if A and B must sit together?",
   "Block AB: 3! × 2 = **12**.",
   "row n!, circle (n − 1)!"),
 P("st-p16", "Seats plus attributes", "common",
   "Each person also has a drink, colour, city or job.",
   "Grid: people down, seat and attribute across. Fix seats first; join attribute to name only when a clue links them.",
   "Four people in a row: A at the left end drinks something; the milk drinker sits immediately right of A; C drinks juice at the right end; B drinks coffee. What does A drink?",
   "Milk is seat 2 (not A); juice is C, coffee is B. A drinks **tea**."),
]

PYQS = [
 PYQ("Linear row facing north", "very common",
     "One row of 5–8 people, all facing north; ends and distance clues.",
     "Number seats 1..n from the left; right = +k, left = −k; ends first, chains next, 'not' clues last.",
     "linear-arrangement",
     "Six people face north. D is at the left end, B is fourth to the right of D and E is immediately left of B. How many people sit between D and E?",
     "D = 1, B = 5, E = 4. Between D and E = 4 − 1 − 1 = **2**."),
 PYQ("Row facing south", "common",
     "All people face south; left/right asked.",
     "Flip the signs, or draw the row east-to-west.",
     "linear-arrangement",
     "Five people face south. R in the middle, V immediately right of R. On which side of R is V, seen from the north?",
     "South-facing right = west, so V is on the **west** side of R."),
 PYQ("Circle facing the centre", "very common",
     "6–8 people around a table facing the centre; opposite and neighbour clues.",
     "Fix one person at the top; left = clockwise; place opposites first.",
     "circular-arrangement",
     "Six people face the centre: A sits opposite D and B is second to the right of A. Is B a neighbour of D?",
     "Seats 0–5 clockwise: A = 0, D = 3; right = anticlockwise, so B = 4. **Yes** — B is immediately left of D."),
 PYQ("Circle facing outward or mixed", "common",
     "Some or all face outward.",
     "Arrow at each person; outward left = anticlockwise.",
     "circular-arrangement",
     "Five people face outward. Q is immediately left of P. Which way from P is Q?",
     "Outward left = anticlockwise, so Q is **one seat anticlockwise** from P."),
 PYQ("Two rows facing each other", "very common",
     "Two rows of 4–6; 'faces' clues link rows.",
     "Seat i faces seat i; south-facing row reads left = east.",
     "puzzle-strategy",
     "Row 1 faces south, row 2 faces north. P is at the left end of row 2. Whom does P face?",
     "P sits at seat 1 (west end). P faces seat 1 of row 1, which is the **right end** for the south-facing row 1."),
 PYQ("Set of follow-up questions", "very common",
     "3–5 questions share one puzzle: true statement, interchange, odd one out.",
     "Solve fully once, write the final arrangement, then answer each by lookup.",
     "puzzle-strategy",
     "Row: D F A C E B facing north. Which is true: (a) E at an end (b) F right of D?",
     "E is at seat 5 (not an end); F is at seat 2, immediately right of D. **(b)** is true."),
 PYQ("Seats with attributes", "common",
     "Each person has a second property (city, colour, drink).",
     "Fix seats first, then fill a people × attribute grid.",
     "puzzle-strategy",
     "Four in a row; the tea drinker is at the left end, and B drinks coffee. Can B be at the left end?",
     "No — the left end holds the tea drinker and B drinks coffee."),
 PYQ("Counting from ends and between", "common",
     "Asks positions from an end or how many sit between two people.",
     "p-th from left = (n − p + 1)-th from right; between = |a − b| − 1.",
     "seating-idea",
     "In a row of 7, K is 3rd from the left. What is K's position from the right?",
     "7 − 3 + 1 = **5th**."),
]
