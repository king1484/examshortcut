"""Notes, patterns and topic PYQ patterns for reasoning/figure-series.
Every rule and worked example used in the notes is re-checked by the frame engine in
figure-series.py (see the NOTE_FACTS asserts there)."""
from _lib import P, PYQ

NOTES, PATTERNS = {}, {}

# =================================================================== movement-rotation
NOTES["movement-rotation"] = r"""### What the series asks
Four figures follow one after another by a fixed rule of **movement** or **rotation**. You must pick the fifth figure from the options. Nothing is counted or added here - something only **turns** or **slides** from frame to frame.

### Number the positions
Many frames place a small mark (a dot, a ring, a square) on the **border** of a square. Number the 8 border places **clockwise** starting from the top-left corner: 0 top-left corner, 1 top-middle, 2 top-right corner, 3 right-middle, 4 bottom-right corner, 5 bottom-middle, 6 bottom-left corner, 7 left-middle. A movement "one place clockwise" then means 0 → 1 → 2; "two places anticlockwise" means 0 → 6 → 4. With numbers, the answer is a small sum: next place = last place + step (mod 8).

### Arrows and directions
An arrow that turns is read by its **angle**. The 8 likely directions are up, up-right, right, down-right, down, down-left, left, up-left - 45 degrees apart. "90° clockwise" sends up → right → down; "45° anticlockwise" sends right → up-right → up. Write the direction under each frame, find the step, and turn once more for the answer.

### Shaded parts
A shaded quarter of the square moves around the four quarters: top-left → top-right → bottom-right → bottom-left is one step **clockwise** each time. The same numbering trick works with 4 places instead of 8.

### Two or three rules together
Harder series move two or three elements at once - say a shaded quarter, an arrow and a dot. **Read one element at a time** across all four frames, write its rule, then combine the rules for the answer. Never try to compare whole frames; each element obeys its own small rule.

### Method in the exam
1. Pick one element and follow it through all frames; note its rule (step size and direction).
2. Repeat for any other element.
3. Apply each rule once more to get the answer's element positions.
4. Match the options; reject any option that breaks even one rule.

### Worked example
An arrow points up, then up-right, then right, then down-right - it turns **45° clockwise** each step. One more turn of 45° clockwise points it **down**. In place-numbered form: a dot at place 0, 2, 4, 6 moves two places clockwise each step, so next is 6 + 2 = 8 → place 0, the **top-left corner**.

### Common mistakes
- Mixing up clockwise and anticlockwise after the second frame.
- Reading a 45° turn as 90° (the arrowheads are small - trace one frame at a time).
- In combined series, applying one rule to the wrong element.
- Forgetting that the movement repeats around the frame: place 7 + 1 = place 0, not place 8.

### Quick revision
- Border: 8 places numbered clockwise from the top-left corner; step is added mod 8.
- Arrows: 8 directions, 45° apart; note the turn per frame.
- Shaded quarter: 4 places; one quarter clockwise at a time.
- Combined series: solve one element at a time, then combine.
- The answer must satisfy **every** rule, not just one.
"""

PATTERNS["movement-rotation"] = [
    P("mr-p1", "Rotating arrow or line", "very common",
      "Each frame shows an arrow or a line at a different angle.",
      "Write the direction in each frame; find the constant turn (45, 90 or 135 degrees, clockwise or anticlockwise); turn once more.",
      "**Q.** An arrow points up, up-right, right, down-right. What comes next?",
      "45° clockwise each step; one more turn points it **down**.",
      formula=r"\theta_{next} = \theta_{last} + s"),
    P("mr-p2", "Element moving round the border", "very common",
      "A dot, ring or square sits on a different border place in every frame.",
      "Number the 8 border places clockwise from the top-left corner; find the step; add it to the last place (mod 8).",
      "**Q.** A dot at 0, 2, 4, 6 - where next?",
      "Two places clockwise each step: 6 + 2 = 8 → place 0, the top-left corner.",
      formula=r"p_{next} = (p_{last} + s) \bmod 8"),
    P("mr-p3", "Shaded part moving", "common",
      "A shaded quarter (or half) of the square jumps from frame to frame.",
      "The quarter moves around 4 places; read the direction from the first two frames and continue.",
      "**Q.** Shaded quarter: TL → TR → BR → BL. Next?",
      "One quarter clockwise each step; it returns to the **top-left**."),
    P("mr-p4", "Two or three rules together", "common",
      "Each frame carries two or three elements (shading, arrow, dot), each changing.",
      "Follow one element through all frames at a time; write each rule; apply every rule once more for the answer.",
      "**Q.** Shading moves anticlockwise and the arrow turns 90° clockwise. What is the fifth frame?",
      "Combine: shaded quarter from the shading rule, arrow direction from the turn rule - the answer satisfies both."),
]

# =================================================================== addition-change
NOTES["addition-change"] = r"""### What changes here
Instead of moving, the figures **add or remove** something: more strokes each frame, one new dot per frame, or a growing count together with a small extra detail that alternates. The rule is about **how many**, not about where a mark slides.

### Counting strokes
Many series draw 1, 3, 5... simple strokes inside the square. Count them in every frame and write the row of numbers: 1, 3, 5 → the step is **+2**, so the next frame has 7. The step can be negative (4, 3, 2 → 1) - subtraction is as common as addition.

### Dots added round the frame
A very frequent series adds **one dot per frame at the next corner**, going clockwise: top-left; then top-right; then bottom-right; then the last corner. After the fourth frame the answer holds **one dot in every corner**. Watch the starting corner and the direction - both can change between questions.

### A second rule
Often the count grows while a small detail **alternates**: an arrow flips up, down, up, down, or a mark swaps between two shapes. Two rules never interact - find the count rule, find the alternating rule, and the answer must satisfy **both**. Options usually break exactly one of the two: right count with wrong detail, or right detail with wrong count.

### Method in the exam
1. Count the main element in every frame; write the number row.
2. Find the step (+1, +2, −1...). Apply it once more.
3. If any detail differs between frames (arrow, shading, shape), write its row too - it usually alternates.
4. Choose the option that fits every row.

### Worked example
Strokes: 1, 3, 5 - **two more** each step, so the next frame has **7**. With a second rule, say the arrow alternates up, down, up: the answer would need 7 strokes **and** a downward arrow. An option with 7 strokes and an upward arrow breaks the second rule; an option with 5 strokes and a downward arrow breaks the first.

### Common mistakes
- Reading +1 when the real step is +2 (count every frame, don't guess).
- Missing a stroke hidden behind the frame border.
- Taking an option that fits the count but ignores the alternating detail.
- In dot series, forgetting which corner comes next and adding the dot at the wrong one.

### Quick revision
- Write the count row: 1, 3, 5 → step +2 → next 7.
- Steps can be negative: 4, 3, 2 → 1.
- Dot series: one new dot at the next corner clockwise; four corners then full.
- Second rule (alternating arrow or shape) must hold along with the count.
- Options break exactly one rule each - check both before answering.
"""

PATTERNS["addition-change"] = [
    P("ac-p1", "Growing count", "very common",
      "Frames show 1, 2, 3... simple strokes or marks; the options differ only in how many.",
      "Count in every frame, find the constant step (+1, +2 or −1), apply it once more.",
      "**Q.** Strokes: 1, 3, 5. What comes next?",
      "Step +2: next frame has **7** strokes.",
      formula=r"a_{n} = a_{n-1} + s"),
    P("ac-p2", "Dots added round the frame", "common",
      "Each frame adds one dot at the next corner of the square.",
      "Note the starting corner and the direction; each frame the new dot appears at the next corner; the fourth frame has all four corners.",
      "**Q.** Dots at TL; TL and TR; TL, TR and BR. Next?",
      "**4 dots, one in every corner** (the new one at the bottom-left)."),
    P("ac-p3", "Count plus alternating detail", "common",
      "The count grows while an arrow or mark alternates (up/down, or two shapes).",
      "Two independent rules: continue the count row, continue the alternation; the answer satisfies both.",
      "**Q.** Strokes 1, 2, 3, 4 with an arrow alternating up, down, up, down. Next?",
      "**5 strokes** with the arrow **up**."),
    P("ac-p4", "Shrinking count with a moving marker", "occasional",
      "The stroke count falls each frame while a dot or ring slides round the border.",
      "Continue the count row downwards; read the marker's border step separately; combine both.",
      "**Q.** Strokes 5, 4, 3, 2 and a dot moving one place clockwise. Next?",
      "**1 stroke**, with the dot at the next border place.",
      formula=r"a_{n} = a_{n-1} - s"),
]

# =================================================================== topic PYQ patterns
PYQS = [
    PYQ("Rotating arrow or line", "very common",
        "An arrow or line at a different angle in every frame.",
        "Write the direction per frame; find the constant turn; turn once more for the answer.",
        "movement-rotation",
        "**Q.** Arrow: up, up-right, right, down-right - next?",
        "45° clockwise each step → points **down**."),
    PYQ("Element moving round the border", "very common",
        "A dot, ring or square on a different border place each frame.",
        "Number the 8 border places clockwise from the top-left corner; add the step (mod 8).",
        "movement-rotation",
        "**Q.** Dot at places 0, 2, 4, 6 - next?",
        "Place 0, the top-left corner."),
    PYQ("Shaded part moving", "common",
        "A shaded quarter shifts around the square.",
        "The quarter circles the 4 places; read the direction from frames 1-2 and continue.",
        "movement-rotation",
        "**Q.** TL → TR → BR → BL - next?",
        "Back to the top-left."),
    PYQ("Two or three rules together", "common",
        "Shading, arrow and dot all change from frame to frame.",
        "Solve one element at a time; the answer satisfies every rule.",
        "movement-rotation",
        "**Q.** Shading anticlockwise + arrow 90° clockwise - fifth frame?",
        "Apply both rules once more and combine."),
    PYQ("Growing count", "very common",
        "Strokes or marks increase by a fixed step.",
        "Write the count row and extend it one term.",
        "addition-change",
        "**Q.** Strokes 1, 3, 5 - next?",
        "7."),
    PYQ("Dots added round the frame", "common",
        "One new dot at the next corner each frame.",
        "Follow the corners in order; the fourth frame has all four corners dotted.",
        "addition-change",
        "**Q.** TL; TL+TR; TL+TR+BR - next?",
        "4 dots, one in every corner."),
    PYQ("Count with a second rule", "common",
        "A growing or shrinking count plus an alternating arrow or mark.",
        "Extend the count row and the alternation separately; the answer fits both.",
        "addition-change",
        "**Q.** Strokes 1, 2, 3, 4 with the arrow alternating up/down - next?",
        "5 strokes with the arrow up."),
]
