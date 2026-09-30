"""Readable rewrite of Reasoning > Paper Folding & Cutting (fold-punch, layers-count).

Every answer is checked by simulation. The sheet is a 24 x 24 grid of integer points
(x right, y up, so 24 = "1 sheet"). A fold moves the points on one side of a line onto
the other side. A punch at a folded position opens a hole at every original point that
lands there. Creases (points on the fold line) never move, so a punch on a crease
automatically merges into one hole.
Run: python paper_folding_cutting.py (patches content/core/topics/reasoning/paper-folding-cutting.json)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "paper-folding-cutting.json"

S = 24
GRID = [(x, y) for x in range(S + 1) for y in range(S + 1)]


# ---------------------------------------------------------------- folds
def V(c, side):
    """Vertical crease x=c. side 'L': left part is folded over to the right. 'R': right part over to the left."""
    if side == "L":
        return lambda p: (2 * c - p[0], p[1]) if p[0] < c else p
    return lambda p: (2 * c - p[0], p[1]) if p[0] > c else p


def H(c, side):
    """Horizontal crease y=c. side 'T': top part folded down. 'B': bottom part folded up."""
    if side == "T":
        return lambda p: (p[0], 2 * c - p[1]) if p[1] > c else p
    return lambda p: (p[0], 2 * c - p[1]) if p[1] < c else p


def DIAG(kind, moving):
    """Diagonal creases of the whole sheet.
    'TLBR' = line from top-left to bottom-right: y = S - x.  'BLTR' = bottom-left to top-right: y = x.
    moving 'TR' / 'BL' / 'TL' / 'BR' names the half that is folded over."""
    if kind == "TLBR":
        refl = lambda p: (S - p[1], S - p[0])
        side = {"TR": lambda p: p[0] + p[1] > S, "BL": lambda p: p[0] + p[1] < S}[moving]
    else:
        refl = lambda p: (p[1], p[0])
        side = {"TL": lambda p: p[1] > p[0], "BR": lambda p: p[1] < p[0]}[moving]
    return lambda p: refl(p) if side(p) else p


def diag_line(a, b, moving_above):
    """Crease through points a and b (used for a folded square). Reflect points strictly on one side."""
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1

    def side(p):
        return (dx * (p[1] - y1) - dy * (p[0] - x1))

    def refl(p):
        # reflection over the line, exact integers for the 45-degree lines used here
        t = (dx * (p[0] - x1) + dy * (p[1] - y1))
        n = dx * dx + dy * dy
        fx = x1 + dx * t / n
        fy = y1 + dy * t / n
        rx, ry = 2 * fx - p[0], 2 * fy - p[1]
        assert rx == int(rx) and ry == int(ry)
        return (int(rx), int(ry))

    return lambda p: refl(p) if (side(p) > 0 if moving_above else side(p) < 0) else p


def run(p, folds):
    for f in folds:
        p = f(p)
    return p


def holes(punch, folds, pts=GRID):
    """Original points that end at the punch position."""
    return sorted(p for p in pts if run(p, folds) == punch)


def all_holes(punches, folds):
    out = []
    for P in punches:
        out += holes(P, folds)
    return sorted(set(out))


def layers(P, folds):
    return len(holes(P, folds))


CELLS = [(x, y) for x in range(1, S, 2) for y in range(1, S, 2)]      # cell centres (odd, odd)


def cut_cells(cells, folds):
    out = []
    for C in cells:
        out += holes(C, folds, CELLS)
    return sorted(set(out))


# ================================================================= verified numbers
# ---- fp-p1: half fold (left over right), punch near top-right
half = [V(12, "L")]
assert holes((20, 20), half) == [(4, 20), (20, 20)]                 # top-right and top-left, same height
# a horizontal fold keeps the left-right place
assert holes((6, 5), [H(12, "T")]) == [(6, 5), (6, 19)]
# ---- fp-p2: quarter fold; punch near the open corner
quarter = [V(12, "L"), H(12, "T")]                                    # folded square sits in x 12..24, y 0..12
q_open = holes((21, 3), quarter)
assert q_open == [(3, 3), (3, 21), (21, 3), (21, 21)]                 # one near each corner of the sheet
q_mid = holes((13, 11), quarter)                                      # near the centre (folded corner)
assert q_mid == [(11, 11), (11, 13), (13, 11), (13, 13)]              # clustered round the centre
# order matters not for the count: any punch off the creases gives 4
assert all(len(holes((x, y), quarter)) == 4 for x in range(13, 24, 2) for y in range(1, 12, 2))
# ---- fp-p3: diagonal fold, TL-BR line, top-right half moves over
dg = [DIAG("TLBR", "TR")]
assert holes((2, 12), dg) == [(2, 12), (12, 22)]                      # middle of left edge -> middle of top edge
assert holes((10, 14), dg) == [(10, 14)]                              # on the crease: one hole
# the swap rule for the other diagonal (BL-TR line): (x, y) -> (y, x)
assert holes((6, 2), [DIAG("BLTR", "TL")]) == [(2, 6), (6, 2)]
# ---- fp-p4: strip fold, left quarter over the next quarter
strip = [V(6, "L")]
assert len(holes((9, 10), strip)) == 2 and len(holes((18, 10), strip)) == 1
assert len(holes((9, 10), strip)) + len(holes((18, 10), strip)) == 3
# ---- fp-p5: quarter fold then diagonal of the folded square
folded_diag = quarter + [diag_line((12, 0), (24, 12), True)]          # crease y = x - 12, upper-left part folds over
h5 = holes((20, 3), folded_diag)
assert len(h5) == 8 and len(set(h5)) == 8
# three straight half folds also give 8
three = [V(12, "L"), H(12, "T"), V(18, "R")]
assert len(holes((19, 5), three)) == 8 or len(holes((17, 5), three)) == 8
assert layers((15, 5), three) == 8 or layers((17, 5), three) == 8
# ---- fp-p6: punch on crease
assert holes((12, 12), quarter) == [(12, 12)]                         # both creases: 1 hole
assert holes((18, 12), quarter) == [(6, 12), (18, 12)]                # one crease (horizontal): 2 holes
assert holes((12, 6), quarter) == [(12, 6), (12, 18)]                 # the other crease: 2 holes
assert holes((12, 5), half) == [(12, 5)]                              # on the single crease: 1 hole
# ---- fp-p7: cut a notch touching the fold
notch = [(13, 11), (15, 11), (13, 13), (15, 13)]                      # 4 cells against the crease x=12
open_cells = cut_cells(notch, half)
assert len(open_cells) == 8
xs = sorted({c[0] for c in open_cells})
assert xs == [9, 11, 13, 15]                                          # one block, twice as wide, no gap
assert all((23 - x, y) in [(a, b) for a, b in open_cells] or (24 - x, y) in open_cells for x, y in open_cells)
assert all((24 - x, y) in open_cells for x, y in open_cells)          # symmetric about the fold line
# a notch NOT touching the crease opens as two separate pieces
away = [(17, 11), (19, 11), (17, 13), (19, 13)]
oa = cut_cells(away, half)
assert len(oa) == 8 and sorted({c[0] for c in oa}) == [5, 7, 17, 19]  # a gap between x=8 and x=16
# ---- fp-p8: pick the right unfolded figure
r8 = holes((21, 3), quarter)


def quad(p):
    return (p[0] > 12, p[1] > 12)


def near_corner(p):
    return min(p[0], S - p[0]) < 6 and min(p[1], S - p[1]) < 6


opt1 = len(r8) == 4 and len({quad(p) for p in r8}) == 4 and all(near_corner(p) for p in r8)
opt2 = len(r8) == 2
opt3 = all(abs(p[0] - 12) < 4 and abs(p[1] - 12) < 4 for p in r8)
opt4 = len(r8) == 1
assert (opt1, opt2, opt3, opt4) == (True, False, False, False)

# ---- layers-count
# lc-p1 full folds
assert [layers((x, y), [V(12, "L")]) for x, y in [(13, 5)]] == [2]
# clean 3-fold: half, half, half with widths 24 -> 12 -> 6 -> 3
t3 = [V(12, "L"), H(12, "T"), V(18, "L")]
assert layers((19, 5), t3) == 8 and layers((21, 5), t3) == 8
assert layers((19, 5), t3) * 2 == 16                                  # 2 punches -> 16 holes
assert 2 * 2 ** 3 == 16
f4 = t3 + [H(6, "T")]
assert layers((19, 3), f4) == 16
# doubling table
assert [2 ** n for n in (1, 2, 3, 4)] == [2, 4, 8, 16]
# lc-p2 strip fold: left quarter on next quarter; 2 punches on doubled part, 1 on single part
assert layers((9, 5), strip) == 2 and layers((9, 17), strip) == 2 and layers((18, 11), strip) == 1
assert 2 * 2 + 1 * 1 == 5
# top quarter down, then half left over right
mixed = [H(18, "T"), V(12, "L")]
assert layers((13, 15), mixed) == 4 and layers((13, 5), mixed) == 2
assert 4 + 2 == 6
# lc-p3 crease
assert layers((12, 12), quarter) == 1 and layers((18, 12), quarter) == 2
# lc-p4 three-way fold
letter = [V(8, "L"), V(16, "R")]
assert layers((11, 5), letter) == 3 and layers((13, 5), letter) == 3
letter_half = letter + [H(12, "T")]
assert layers((11, 5), letter_half) == 6
assert 3 * 2 == 6
# lc-p5 fold count from steps: quarter fold, 2 punches
assert layers((21, 3), quarter) * 2 == 8
# lc-p6 fold then diagonal
assert layers((20, 3), folded_diag) == 8
# a diagonal of the plain sheet doubles as well
assert layers((3, 3), [DIAG("TLBR", "TR")]) == 2
# half then diagonal of a folded square: 4 layers under a point
# lc-p7 hole totals with a mix: quarter fold, one punch near open corner + one on a crease
tot = len(holes((21, 3), quarter)) + len(holes((18, 12), quarter))
assert tot == 6
# lc-p8: hole count check: 3 punches on 4 layers
assert 3 * layers((21, 3), quarter) == 12
assert 3 * 4 == 12
# a fold in half, then a strip fold of one quarter of the folded piece
combo = [V(12, "L"), H(18, "T")]
assert layers((13, 15), combo) == 4 and layers((13, 3), combo) == 2
# 1 -> 2 -> 4 -> 8 chain used in the tricks text
assert (1 * 2, 1 * 2 * 2, 1 * 2 * 2 * 2) == (2, 4, 8)
# letter fold then half fold, one punch: 6 holes
assert holes((11, 5), letter_half).__len__() == 6


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ================================================================= fold-punch
fp_concept = (
    "When a folded sheet is punched, the punch goes through every layer under it. "
    "To open the sheet, undo the folds in reverse order. "
    "Each unfold gives every hole a mirror copy across that fold line. "
    "Compare the positions of the holes with the options, not just their number."
)

fp_notes = r"""### What a punch does
A punch goes through every layer of paper under it. When you open the sheet, each layer shows its own hole.

So the job is to find where each layer came from.

The fold line works like a mirror. A point on the folded-over part sits at the same distance from the line, on the other side.

> **Rule:** Open the folds in reverse order. Each unfold gives every hole a mirror copy across that fold line.

### The method
1. Read the folds in order. Mark the punch on the last drawing.
2. Undo the last fold first. Draw a mirror copy of every hole across that fold line.
3. Undo the fold before it in the same way.
4. Stop when the sheet is flat. Compare the positions of the holes with the options.

Each full fold doubles the holes. One fold gives 2 holes per punch, two folds give 4, three folds give 8.

### Where the copies go
- Vertical fold line: the copy keeps its height and moves to the other side.
- Horizontal fold line: the copy keeps its left-right place and moves up or down.
- Diagonal fold line: the copy swaps sides. A hole near the middle of the left edge gets a copy near the middle of the top edge.

Example: a sheet is folded left over right. A hole near the top-right corner gets a copy near the top-left corner, at the same height.

### Quarter fold
Fold in half, then in half again. Now there are 4 layers. One punch opens into 4 holes, one in each quarter.

- Punch near the open corner: the 4 holes sit near the 4 corners of the sheet.
- Punch near the folded corner: the 4 holes sit close together round the centre.

> **Tip:** The four holes are mirror images round both centre lines. If your figure is not symmetric, it is wrong.

### Strip folds
Sometimes only a strip is folded over. Only the paper under the strip has two layers.

- Punch inside the doubled strip: 2 holes.
- Punch outside the strip: 1 hole.

This is the most common trap in option questions. Check where the flap lies before you double.

### Punch on a fold line
A punch exactly on a crease does not make two holes across that crease. The two copies meet at the same place, so one hole opens on the crease.

- Quarter fold, punch at the centre where both creases meet: 1 hole.
- Quarter fold, punch on one crease only: 2 holes.

> **Watch:** Count only the folds whose crease does not pass through the punch.

### Cutting instead of punching
Cutting works the same way. A cut piece opens into a shape that is symmetric about the fold line.

A notch cut with one side on the fold opens into one block, twice as wide. A notch cut away from the fold opens into two separate pieces.

### Worked example
A square sheet is folded left over right, then top over bottom. It is punched once near the open corner of the folded square.

Undo the top-over-bottom fold: a copy appears above the first hole. Undo the left-over-right fold: both holes get copies on the left. The result is 4 holes, one near each corner of the sheet.
"""

fp_formulas = []

fp_tricks = [
    {
        "title": "Reflect, do not rotate",
        "body": "Each unfold is a mirror. The copy is at the same distance from the fold line, on the other side. A half turn of the flap is wrong.",
        "example": {
            "q": "A sheet is folded left over right and punched near the top-right corner. Where are the holes after unfolding?",
            "steps": ["The fold line is vertical, so height stays the same.", "The copy is on the left, at the same distance from the fold line."],
            "answer": "One hole near the top-right and one near the top-left, at the same height",
        },
    },
    {
        "title": "Count first, then check positions",
        "body": "Holes = punches times layers under each punch. Use the count to remove wrong options, then check positions.",
        "example": {
            "q": "A sheet is folded in half twice and punched once away from the creases. How many holes?",
            "steps": [r"Layers: $2 \times 2 = 4$.", "One punch goes through 4 layers."],
            "answer": "4 holes",
        },
    },
]

fp_mistakes = [
    {"wrong": "Undoing the folds in the original order.", "right": "Undo the last fold first. Work backwards."},
    {"wrong": "Turning the flap half a turn instead of reflecting it.", "right": "Copy each hole as a mirror image across the fold line."},
    {"wrong": "Doubling a punch that lies outside a folded strip.", "right": "Only the paper under the strip has two layers. Check where the flap lies."},
    {"wrong": "Making 2 or 4 holes for a punch that sits on a crease.", "right": "Copies across a crease through the punch land on the same spot. They merge into one hole."},
    {"wrong": "Checking only the number of holes.", "right": "Two options can have the same number of holes. Check the positions too."},
]

fp_revision = [
    "A punch goes through all layers. Each layer makes one hole.",
    "Unfold in reverse order. Each unfold mirrors the holes across that fold line.",
    "Vertical fold keeps height. Horizontal fold keeps left-right place.",
    "Full folds: 1, 2, 4, 8 holes per punch.",
    "Strip fold: double only the punches under the strip.",
    "Punch on a crease: the copies merge into one hole.",
]

fp_patterns = [
    pat("fp-p1", "Single half fold, then punch", "very common",
        "One dashed line through the middle of the sheet and one arrow. One or two punches on the folded half.",
        None,
        ["Note the fold line and the punch.", "Reflect the hole across the fold line.", "Keep the copy at the same distance from the line."],
        "Each punch goes through 2 layers, so it makes 2 holes: the one you see and its mirror copy.",
        "A square sheet is folded left over right and punched once near the top-right corner. Where are the holes after unfolding?",
        ["The fold line is vertical, so height stays the same.", "The mirror copy is on the left side, same distance from the line."],
        "One hole near the top-right corner and one near the top-left corner"),
    pat("fp-p2", "Quarter fold, then punch", "very common",
        "Two folds: one half onto the other, then the result halved again at right angles.",
        r"H = p \times 2^{n}",
        ["Undo the second fold first: copy the hole across the second crease.", "Undo the first fold: copy both holes across the first crease.", "You now have 4 holes, mirror images round both centre lines."],
        "There are 4 layers under the punch, so one punch makes 4 holes.",
        "A square sheet is folded in half left over right, then in half top over bottom. It is punched once near the open corner of the folded square. How many holes are there, and where?",
        ["Layers: $2 \\times 2 = 4$.", "The open corner of the folded square is a corner of the sheet.", "The mirror copies land near the other three corners."],
        "4 holes, one near each corner of the sheet"),
    pat("fp-p3", "Diagonal fold", "common",
        "A dashed line from corner to corner. The folded sheet is a triangle.",
        None,
        ["Draw the diagonal line.", "Reflect the hole across it. Distance to the line stays the same.", "A hole near the middle of one edge moves to the middle of the neighbouring edge."],
        "The diagonal is the mirror. Edges that meet at the corner on the line swap places.",
        "A square sheet is folded along the diagonal from top-left to bottom-right. The top-right half is folded over. A punch is made near the middle of the left edge of the folded triangle. Where is the second hole?",
        ["The mirror line runs from top-left to bottom-right.", "The left edge and the top edge meet at the top-left corner and swap places.", "The mirror copy is at the same distance from the corner, along the top edge."],
        "Near the middle of the top edge"),
    pat("fp-p4", "Strip (partial) fold", "common",
        "The dashed line is not through the middle. Only a narrow strip is folded over.",
        None,
        ["Mark the part of the sheet the flap covers.", "Punches inside the covered part make 2 holes.", "Punches outside it make 1 hole."],
        "Only the covered part has two layers. The rest is still one layer.",
        "The left quarter of a sheet is folded over to the right, on top of the second quarter. One punch is made on the doubled part and one on the single part. How many holes are there after unfolding?",
        ["Doubled part: 2 layers, so 2 holes.", "Single part: 1 layer, so 1 hole."],
        "3 holes"),
    pat("fp-p5", "Three folds", "occasional",
        "Three folding steps: often a quarter fold followed by a diagonal fold, or three half folds.",
        r"H = p \times 2^{3}",
        ["Write the layers after each fold: 2, 4, 8.", "Undo the last fold first, then the second, then the first.", "Check that the 8 holes are mirror images round every crease."],
        "Each full fold doubles the layers. Three folds make 8 layers.",
        "A sheet is folded in half, then in half again, then along a diagonal of the folded square. One punch is made away from every crease. How many holes are there?",
        [r"Layers: $2 \times 2 \times 2 = 8$."],
        "8 holes"),
    pat("fp-p6", "Punch on a fold line", "occasional",
        "The punch sits exactly on an edge of the folded piece where the paper bends.",
        None,
        ["Find which creases pass through the punch.", "Do not double for those creases.", "Double for every other fold."],
        "Copies across a crease through the punch land on the same spot, so they merge.",
        "A sheet folded into quarters is punched at the folded corner, which is the centre of the sheet. How many holes are there?",
        ["Both creases pass through the punch.", "No fold doubles it."],
        "1 hole, at the centre"),
    pat("fp-p7", "Cut a shape from the fold", "common",
        "A small piece is cut out of the folded paper, often a notch or a corner.",
        None,
        ["Draw the cut shape on the folded paper.", "Undo the last fold: mirror the shape across that crease.", "A shape touching the crease joins its copy into one piece."],
        "Cutting goes through every layer, just as a punch does. The opened shape is symmetric about each crease.",
        "A square sheet is folded in half, left over right. A small square notch is cut with one side along the fold line. After unfolding, how many separate cut-outs are there, and how wide is the cut-out compared with the notch?",
        ["The notch touches the crease, so it joins its mirror copy.", "The copy is on the other side of the crease and is the same size."],
        "One cut-out, twice as wide as the notch"),
    pat("fp-p8", "Pick the correct opened figure", "very common",
        "The folded sheet and punch are drawn. Four opened sheets are given as options.",
        None,
        ["Count the layers. Remove options with the wrong number of holes.", "Check the symmetry: the holes must mirror across every crease.", "Check the positions, near a corner or near the centre."],
        "A correct opened figure is symmetric about every fold line.",
        "A square sheet is folded in half left over right, then in half top over bottom. One punch is made near the open corner. Which opened figure is correct? (1) four holes, one near each corner of the sheet (2) two holes near the top corners (3) four holes close together near the centre (4) one hole near the bottom-right corner",
        ["Two folds give 4 layers, so 4 holes. Options 2 and 4 are wrong.", "The punch is near the open corner, a corner of the sheet, not the centre. Option 3 is wrong."],
        "Option 1"),
]

# ================================================================= layers-count
lc_concept = (
    "Many questions only ask how many holes or layers. "
    "Count the layers under each punch. "
    "A full fold doubles the layers everywhere. A strip fold doubles them only under the strip."
)

lc_notes = r"""### Count first
Many questions only ask how many holes appear, or how many layers a punch goes through. Even in figure questions, counting first removes wrong options fast.

> **Rule:** Holes after unfolding = the layers under each punch, added up.

### Full folds
A full fold lays one half exactly on the other half. The layers double everywhere.

| Full folds | Layers | Holes from 1 punch |
|---|---|---|
| 1 | 2 | 2 |
| 2 | 4 | 4 |
| 3 | 8 | 8 |
| 4 | 16 | 16 |

With $p$ punches and $n$ full folds, holes $= p \times 2^{n}$.

A diagonal fold of a square, or of a folded square, is also a full fold. The two halves match exactly.

### Strip folds
If only a strip is folded over, the layers double only under the strip. Work punch by punch.

- Punch under the strip: the old layers doubled.
- Punch outside the strip: the old layers.

Example: fold the left quarter over the second quarter. Then punch 2 holes on the doubled part and 1 on the single part. Holes: $2 \times 2 + 1 \times 1 = 5$.

### Three-way fold
Fold a sheet into three equal strips, like a letter. Every part now has 3 layers. Fold that in half and you have 6.

> **Watch:** Not every layer count is a power of 2. A three-way fold gives 3.

### Punch on a crease
A punch exactly on a crease joins the two layers that meet there. The copies merge into one hole.

- Quarter fold, punch on one crease: 2 holes, not 4.
- Quarter fold, punch where both creases meet: 1 hole.

### Doubling chain
Write the layers as you read each fold: 1, 2, 4, 8.

For a strip fold, write two chains. One is for the doubled part and one for the single part. Multiply by the punches in each part and add.

> **Tip:** Check every punch for a crease before you multiply.

Then the opened sheet needs a check. The holes must be mirror images round every crease. If a hole has no partner across a crease that passed under it, the count is wrong.

### Diagonal folds
Fold a folded square along its diagonal. The two halves match, so the layers double again.

A punch inside the triangle goes through all the layers. Two straight folds and a diagonal give $2 \times 2 \times 2 = 8$.

If the punch is on the diagonal crease, that fold does not double it.

### Worked example
A sheet is folded in half, and in half again. Then 3 holes are punched through all the layers.

Layers: 2 after the first fold, 4 after the second. Holes: $3 \times 4 = 12$.

If only the left quarter had been folded over first, only punches inside that doubled quarter would double. The count would be smaller.
"""

lc_formulas = [
    {"name": "Holes after full half-folds", "tex": r"H = p \times 2^{n}", "note": "p punches through n full half-folds."},
    {"name": "Layers after full half-folds", "tex": r"L = 2^{n}", "note": "Each full fold doubles the layers."},
]

lc_tricks = [
    {
        "title": "Doubling chain",
        "body": "Write 1, 2, 4, 8 as you read each full fold. Multiply by the number of punches at the end.",
        "example": {
            "q": "A sheet is folded in half three times. Two punches are made. How many holes?",
            "steps": [r"Layers: $2^3 = 8$.", r"Holes: $2 \times 8 = 16$."],
            "answer": "16",
        },
    },
    {
        "title": "Multiply the steps",
        "body": "Each step multiplies the layers: a half fold by 2, a three-way fold by 3.",
        "example": {
            "q": "A sheet is folded into three equal strips and then in half. How many layers are there?",
            "steps": [r"$3 \times 2 = 6$."],
            "answer": "6",
        },
    },
]

lc_mistakes = [
    {"wrong": "Adding 2 layers for each fold.", "right": "Each full fold doubles the layers. Multiply by 2, do not add 2."},
    {"wrong": "Doubling a punch that is outside a folded strip.", "right": "Only the paper under the strip is doubled. Work punch by punch."},
    {"wrong": "Counting 4 holes for a punch that sits on a crease.", "right": "Do not double for a crease that passes through the punch."},
    {"wrong": "Thinking the layers are always a power of 2.", "right": "A three-way fold gives 3 layers, and folding it in half gives 6."},
    {"wrong": "Forgetting to multiply by the number of punches.", "right": "Holes = punches times layers. Multiply at the end."},
]

lc_revision = [
    "Holes = the layers under each punch, added up.",
    r"$n$ full folds, $p$ punches: $H = p \times 2^{n}$.",
    "Strip fold: double only under the strip.",
    "Three-way fold: 3 layers. Then in half: 6 layers.",
    "Crease punch: do not double for a crease through the punch.",
    "Diagonal fold of a square: counts as a full fold.",
]

lc_patterns = [
    pat("lc-p1", "Holes after full folds", "very common",
        "Text only: folded in half n times, p holes punched.",
        r"H = p \times 2^{n}",
        ["Count the full folds, n.", r"Layers $= 2^{n}$.", "Multiply by the number of punches."],
        "Every full fold doubles the layers, so each punch becomes $2^{n}$ holes.",
        "A sheet is folded in half three times and 2 holes are punched. How many holes are there after unfolding?",
        [r"Layers: $2^{3} = 8$.", r"Holes: $2 \times 8 = 16$."],
        "16"),
    pat("lc-p2", "Holes after a strip fold", "common",
        "Only a strip or a quarter of the sheet is folded over, and the punches are in different parts.",
        None,
        ["Mark the part the flap covers.", "Layers there: doubled. Layers elsewhere: unchanged.", "Add the layers under every punch."],
        "The strip is the only doubled part, so each punch must be counted by where it lies.",
        "The left quarter of a sheet is folded onto the second quarter. Two punches are made on the doubled part and one on the single part. How many holes are there?",
        [r"Doubled part: $2 \times 2 = 4$.", r"Single part: $1 \times 1 = 1$.", r"$4 + 1 = 5$."],
        "5"),
    pat("lc-p3", "Punch on a crease", "occasional",
        "The question says the punch is on a fold line or at the folded corner.",
        None,
        ["Find the creases through the punch.", "Do not double for them.", "Double for the other folds."],
        "Copies across a crease through the punch merge into one.",
        "A sheet is folded in half twice to make quarters. A punch is made exactly on the crease that runs across the middle of the folded piece, away from the other crease. How many holes are there?",
        ["Only one crease passes through the punch. It does not double.", "The other fold doubles once.", r"$1 \times 2 = 2$."],
        "2"),
    pat("lc-p4", "Number of layers", "common",
        "The question asks for layers or thickness at a point, or a three-way fold appears.",
        None,
        ["List each step: half fold is 2, three-way fold is 3.", "Multiply the factors."],
        "Each fold multiplies the layers by its own factor.",
        "A sheet is folded into three equal strips and then folded in half. How many layers of paper are there?",
        [r"Three-way fold: 3 layers.", r"Half fold: $3 \times 2 = 6$."],
        "6"),
    pat("lc-p5", "Hole count from a folding figure", "common",
        "The folding steps are drawn and the options are numbers.",
        None,
        ["Read each step as a full fold, a strip fold or a diagonal fold.", "Count the layers under each punch mark.", "Add the layers for all the punches."],
        "The count depends only on the layers, so you do not need to draw the opened sheet.",
        "A sheet is folded into quarters. Two punches are made, neither on a crease. How many holes are there?",
        [r"Layers: $2 \times 2 = 4$.", r"Holes: $2 \times 4 = 8$."],
        "8"),
    pat("lc-p6", "Fold, then a diagonal fold", "occasional",
        "A folded square is folded again along its diagonal, giving a triangle.",
        None,
        ["Count the layers of the folded square.", "The diagonal fold doubles them, because the two halves match.", "A punch inside the triangle goes through all of them."],
        "A diagonal of a square is a full fold, so it doubles the layers.",
        "A sheet is folded in half, and in half again. The folded square is folded along its diagonal. One punch is made away from every crease. How many holes are there?",
        [r"Layers: $2 \times 2 = 4$.", r"Diagonal fold: $4 \times 2 = 8$."],
        "8"),
    pat("lc-p7", "Mixed punches on and off creases", "occasional",
        "A quarter fold, with one punch near the open corner and one on a crease.",
        None,
        ["Count the layers for each punch separately.", "Punch off the creases: 4 layers.", "Punch on one crease: 2 layers.", "Add the holes."],
        "Each punch has its own layer count. A crease removes one doubling.",
        "A sheet is folded into quarters. One punch is made near the open corner. Another is made on one crease, away from the other crease. How many holes are there in all?",
        [r"Open corner punch: $4$ holes.", r"Crease punch: $2$ holes.", r"$4 + 2 = 6$."],
        "6"),
]

# ================================================================= patch
dfrac = lambda s: s.replace(r"\frac", r"\dfrac")
blocks = {
    "fold-punch": (fp_concept, fp_notes, fp_formulas, fp_tricks, fp_mistakes, fp_revision, fp_patterns),
    "layers-count": (lc_concept, lc_notes, lc_formulas, lc_tricks, lc_mistakes, lc_revision, lc_patterns),
}

data = json.loads(TOPIC.read_text(encoding="utf-8"))
frozen = json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                    ensure_ascii=False, sort_keys=True)
seen = set()
for sub in data["subtopics"]:
    if sub["id"] not in blocks:
        continue
    concept, notes, formulas, tricks, mistakes, revision, patterns = blocks[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in patterns]
    assert old_ids <= set(new_ids), "never drop a pattern id"
    assert not (seen & set(new_ids)) and len(new_ids) == len(set(new_ids))
    seen |= set(new_ids)
    assert 2500 <= len(notes) <= 5000, f"{sub['id']} notes {len(notes)} chars"
    assert 4 <= len(mistakes) <= 8 and 4 <= len(revision) <= 9
    mistakes = [{k: dfrac(v) for k, v in m.items()} for m in mistakes]
    revision = [dfrac(r) for r in revision]
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)
    print(f"{sub['id']}: notes {len(notes)} chars, {len(old_ids)} -> {len(patterns)} patterns")

assert json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                  ensure_ascii=False, sort_keys=True) == frozen
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("paper-folding-cutting.json patched")
