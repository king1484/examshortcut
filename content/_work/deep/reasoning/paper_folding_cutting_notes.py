"""Notes, patterns and topic PYQ patterns for reasoning/paper-folding-cutting.
Every number used in the notes and examples is re-checked by the simulator in
paper-folding-cutting.py (see the NOTE_FACTS asserts there)."""
from _lib import P, PYQ

NOTES, PATTERNS = {}, {}

# ======================================================================= fold-punch
NOTES["fold-punch"] = r"""### What happens when you fold and punch
A punch goes through **every layer** of paper under it. When the sheet is opened, each layer shows its own hole. So the job is to find **where each layer came from**.

The fold line acts like a mirror. A point on the part that was folded over lands at the **same distance on the other side** of the fold line. Opening the fold sends it back. So every unfold gives each hole a **mirror copy** across that fold line.

### The method: unfold in reverse order
1. Read the folds in order and mark the final punch position(s).
2. Undo the **last** fold first. For every hole that lies on the part that was folded over, draw its mirror copy across that fold line.
3. Undo the fold before it in the same way, and so on, until the sheet is fully open.
4. Now compare **positions**, not just the number of holes.

Each full fold doubles the holes: 1 fold gives 2 holes per punch, 2 folds give 4, 3 folds give 8.

### Where the copies go
- **Vertical fold line** (left-right fold): the copy keeps its **height** and moves to the other side. A hole near the top-right gets a partner near the top-left.
- **Horizontal fold line** (top-bottom fold): the copy keeps its **left-right position** and moves up or down.
- **Diagonal fold** along the line from top-left to bottom-right: a point at (x, y) goes to **(y, x)**. A hole near the middle of the top edge gets a partner near the middle of the right edge.
- **Other diagonal** (top-right to bottom-left) on a square of side s: (x, y) goes to (s − y, s − x).

### Quarter fold
Folding in half and then in half again makes 4 layers. One punch unfolds into **4 holes**, one in each quarter, placed like mirror images around the two centre lines. If the punch is near the folded corner (the centre of the sheet), the 4 holes cluster near the centre. If it is near the open corners, they sit near the 4 corners of the sheet.

### Partial (strip) folds
If only a strip is folded over, only the part of the sheet under that strip has two layers. A punch **inside** the doubled strip makes 2 holes; a punch **outside** it makes only 1 hole. This is the most common trap in option questions.

### Punch on a fold line
A punch placed **exactly on a crease** does not make two separate holes across that crease; the two copies meet at the same spot and open as **one hole on the crease**. A punch at the centre of a sheet folded into quarters (where both creases meet) opens as just **1 hole**. A punch on only one crease of a quarter fold opens as **2 holes**.

### Cutting instead of punching
Cutting works the same way. A notch cut from a folded edge opens into a shape that is **symmetric about that fold line**. A cut on a corner where two folds meet repeats in all four quarters. Draw the cut piece, then mirror it across each fold line in reverse order.

### Common traps
- **Rotating instead of reflecting:** copies must be mirror images across the fold line, not a half turn of the flap.
- Undoing folds in the **original** order instead of the reverse order.
- Forgetting the **last** unfold, which halves the true count.
- Doubling a punch that lies outside a folded strip.

### Worked example
A sheet is folded left over right, then top down onto the bottom, and punched once near the bottom-right corner of the folded piece. Undo the top-down fold: a copy appears near the top-right. Undo the left-right fold: both holes get copies on the left. Result: **4 holes**, one near each corner of the sheet.

### Quick revision
- A punch goes through all layers; each layer gives one hole.
- Unfold in **reverse** order; each unfold **mirrors** the holes across that fold line.
- Vertical fold keeps height, horizontal fold keeps left-right position, main diagonal swaps x and y.
- Full folds: 1 → 2 → 4 → 8 holes per punch.
- Strip fold: double only the punches inside the strip.
- Punch on a crease: the copies merge into one hole on that crease.
"""

PATTERNS["fold-punch"] = [
    P("fp-p1", "Single half fold, then punch", "very common",
      "One dashed line through the middle of the sheet and one arrow. One or two punches on the folded half.",
      "Each punch makes 2 holes: the one you see and its mirror copy across the fold line, at the same distance on the other side.",
      "**Q.** A square sheet is folded left over right and punched once near the top-right corner. Where are the holes after unfolding?",
      "One hole near the top-right and one near the top-left, both at the same height."),
    P("fp-p2", "Quarter fold, then punch", "very common",
      "Two folds: first one half onto the other, then the result halved again at right angles.",
      "4 layers under the punch, so 4 holes per punch. Undo the second fold first, then the first. The 4 holes are mirror images around both centre lines.",
      "**Q.** A sheet folded into quarters is punched once near the open corner of the folded square. How many holes, and where?",
      "4 holes, one near each corner of the sheet.",
      formula=r"H = p \times 2^{n}"),
    P("fp-p3", "Diagonal fold", "common",
      "A dashed line from corner to corner. The folded sheet is a triangle.",
      "Reflect across the diagonal. For the diagonal from top-left to bottom-right, (x, y) goes to (y, x): a hole near the top edge gets a partner near the left or right edge.",
      "**Q.** A square is folded along the diagonal from top-left to bottom-right, the top-right half moving over. A punch is made near the middle of the bottom edge. Where is the second hole?",
      "Near the middle of the left edge. (x, y) becomes (y, x)."),
    P("fp-p4", "Strip (partial) fold", "common",
      "The dashed line is not through the middle. Only a narrow strip is folded over.",
      "Only the part covered by the strip has 2 layers. Punches in the covered part make 2 holes; punches elsewhere make 1 hole.",
      "**Q.** The left quarter of a sheet is folded over to the right. One punch is made on the doubled part and one on the single part. How many holes?",
      "2 + 1 = 3 holes."),
    P("fp-p5", "Three folds", "occasional",
      "Three folding steps: usually a quarter fold followed by a diagonal fold, or three half folds.",
      "8 layers under a punch away from the creases. Undo the diagonal (last) fold first, then the two straight folds.",
      "**Q.** A sheet is folded in half, then in half again, then along a diagonal. One punch is made. How many holes?",
      "2 × 2 × 2 = 8 holes.",
      formula=r"H = p \times 2^{3}"),
    P("fp-p6", "Punch on a fold line", "occasional",
      "The punch mark sits exactly on an edge of the folded piece where the paper bends.",
      "Copies across that crease land on the same spot, so they merge into one hole on the crease. Count only the folds whose crease does not pass through the punch.",
      "**Q.** A sheet folded into quarters is punched exactly at the folded corner (the centre of the sheet). How many holes?",
      "Only 1 hole, at the centre, because both creases pass through the punch."),
]

# ======================================================================= layers-count
NOTES["layers-count"] = r"""### Count first, then check positions
Many questions only ask **how many holes** appear, or how many layers of paper a punch goes through. Even in figure questions, counting first removes most wrong options quickly.

**Rule:** holes after unfolding = the sum, over all punches, of the **number of layers** under that punch.

### Full folds
A full fold lays one half exactly on the other half, so the number of layers **doubles everywhere**:

| Full folds | Layers | Holes from 1 punch |
|---|---|---|
| 1 | 2 | 2 |
| 2 | 4 | 4 |
| 3 | 8 | 8 |
| 4 | 16 | 16 |

So with p punches and n full folds: $H = p \times 2^{n}$. A diagonal fold of a square or of a folded square also counts as a full fold, because the two halves match exactly.

### Partial folds
If only a strip is folded over, layers double **only inside the strip**. Work punch by punch:
- punch inside the doubled strip: 2 layers (or double what was there before);
- punch outside it: the old number of layers.

Example: the top quarter is folded down, then the whole sheet is folded in half left over right. Where the flap lies the paper has 2 × 2 = 4 layers; below the flap it has 2. One punch in each part gives 4 + 2 = 6 holes.

### Three-way (letter) fold
A sheet folded into three equal strips, like a letter going into an envelope, has **3 layers** everywhere. Folding that in half again gives 6 layers. Not every count is a power of 2.

### Punches on a crease
A punch exactly on a crease joins the two layers that meet there, so the copies merge into one hole. Count the folds whose crease does **not** pass through the punch, and double only for those.
- Quarter fold, punch on one crease: 2 holes (not 4).
- Quarter fold, punch at the point where both creases meet: 1 hole.

### Doubling chain
Write the count as you read each step: 1 → 2 → 4 → 8. For a strip fold, write two chains, one for the doubled part and one for the single part. Multiply by the punches in each part and add.

### Common mistakes
- Adding 2 for each fold instead of doubling.
- Doubling a punch that is outside a folded strip.
- Counting 4 holes for a punch that sits on a crease.
- Thinking layers must be a power of 2 after a three-way fold.

### Quick revision
- Holes = sum of the layers under each punch.
- n full folds, p punches: H = p × 2ⁿ.
- Strip fold: double only inside the strip.
- Three-way fold: 3 layers; then halved: 6 layers.
- Crease punch: do not double for a crease through the punch.
"""

PATTERNS["layers-count"] = [
    P("lc-p1", "Holes after full folds", "very common",
      "Text only: 'folded in half n times', 'p holes punched'.",
      "Every full fold doubles the layers, so each punch becomes 2ⁿ holes.",
      "**Q.** A sheet is folded in half three times and 2 holes are punched. How many holes after unfolding?",
      "2 × 2³ = 16.",
      formula=r"H = p \times 2^{n}"),
    P("lc-p2", "Holes after a strip fold", "common",
      "Only a strip or a quarter of the sheet is folded over, and punches are in different parts.",
      "Find the layers in each part separately (doubled only where the flap lies). Add the layers under each punch.",
      "**Q.** The left quarter of a sheet is folded onto the next quarter. 2 punches are made on the doubled part and 1 on the single part. Holes?",
      "2 × 2 + 1 × 1 = 5."),
    P("lc-p3", "Punch on a crease", "occasional",
      "The question says the punch is made exactly on a fold line or at the folded corner.",
      "Copies across a crease through the punch merge. Double only for creases that do not pass through the punch.",
      "**Q.** A sheet folded into quarters is punched exactly at the folded corner. Holes?",
      "1 hole: both creases pass through the punch."),
    P("lc-p4", "Number of layers", "common",
      "Asked for layers or thickness at a point, or a three-way fold appears.",
      "Doubling for full folds; a three-way fold gives 3 layers; multiply the factors of each step.",
      "**Q.** A sheet is folded into three equal strips and then folded in half. How many layers?",
      "3 × 2 = 6."),
    P("lc-p5", "Hole count from a figure", "common",
      "Folding steps are drawn; the options are numbers.",
      "Read each drawn step as full, strip or diagonal; count layers under each punch mark; add.",
      "**Q.** The figure shows a quarter fold and 2 punches. How many holes?",
      "2 × 4 = 8, unless a punch sits on a crease."),
]

# ======================================================================= topic PYQ patterns
PYQS = [
    PYQ("Single fold, punch", "very common",
        "One half fold, one or two punches, four figure options.",
        "Mirror each punch across the fold line; same height for a vertical fold.",
        "fold-punch",
        "**Q.** Folded left over right, punched once near the top-right. Holes after unfolding?",
        "2 holes at the same height, one near each side."),
    PYQ("Quarter fold, punch", "very common",
        "Two folds at right angles, then a punch.",
        "Undo the second fold, then the first; 4 holes per punch placed symmetrically about both centre lines.",
        "fold-punch",
        "**Q.** Folded into quarters and punched once near the open corner. How many holes?",
        "4, one near each corner of the sheet."),
    PYQ("Diagonal fold", "common",
        "A corner-to-corner fold makes a triangle.",
        "Reflect across the diagonal: (x, y) → (y, x) for the top-left to bottom-right diagonal.",
        "fold-punch",
        "**Q.** Folded along the main diagonal, punched near the middle of the bottom edge. Where is the other hole?",
        "Near the middle of the left edge."),
    PYQ("Strip (partial) fold", "occasional",
        "The fold line is not through the centre.",
        "Double only punches inside the folded strip.",
        "fold-punch",
        "**Q.** Left quarter folded over; punches on the doubled and the single part. Holes?",
        "2 + 1 = 3."),
    PYQ("Three folds", "occasional",
        "Quarter fold followed by a diagonal, or three half folds.",
        "8 holes per punch; undo the last fold first.",
        "fold-punch",
        "**Q.** Halved, halved again, then folded along a diagonal; one punch. Holes?",
        "8."),
    PYQ("Punch on a crease", "occasional",
        "The punch mark is on the edge where the paper bends.",
        "Copies across that crease merge into one hole.",
        "fold-punch",
        "**Q.** Quarter fold punched at the folded corner. Holes?",
        "1."),
    PYQ("Hole count only", "common",
        "Text question: number of folds and number of punches.",
        "H = p × 2ⁿ for full folds; adjust for strip folds and crease punches.",
        "layers-count",
        "**Q.** Folded in half three times, 2 punches. Holes?",
        "16."),
    PYQ("Layers after a three-way fold", "occasional",
        "The sheet is folded into three equal strips.",
        "3 layers; each later full fold doubles it.",
        "layers-count",
        "**Q.** Folded into three strips, then in half. Layers?",
        "6."),
    PYQ("Cut and unfold", "common",
        "A shape is cut from a folded edge or corner instead of a punch.",
        "The cut opens into a shape symmetric about each fold line; mirror it in reverse order.",
        "fold-punch",
        "**Q.** A half-circle is cut from the folded edge of a sheet folded once. What opens out?",
        "A full circle centred on the crease."),
]
