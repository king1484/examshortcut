"""Notes, patterns and topic PYQ patterns for reasoning/cube-dice.
Every number used in the notes and examples is re-checked by the models in
cube-dice.py (painting counts brute-forced, nets folded, dice views enumerated)."""
from _lib import P, PYQ

NOTES, PATTERNS = {}, {}

# ======================================================================= dice-positions
NOTES["dice-positions"] = r"""### What a view of a die tells you
A die has six faces, and each face has exactly **one** face opposite it; the other four touch it. A view of a die shows three faces that meet at one corner, so the three faces in any one view are **pairwise adjacent** — no two of them can ever be opposite.

### Rule 1: strike out the faces seen together
To find the face opposite X, list every face that appears in some view **together with X**. All of them touch X. If four different faces are struck out, exactly one face is left, and that face must be opposite X. This single rule settles most questions.
Example: X appears with A and B in one view, with C in a second and with D in a third. Faces A, B, C, D all touch X, so the sixth face is opposite X.

### Rule 2: two common faces
If two views share the **same two** faces, then the face left over in the first view is opposite the face left over in the second. Views (A, B, C) and (A, B, D): A and B are common, so C and D are opposite.

### Rule 3: common face in the same position
If one face is common to two views and sits in the **same position** in both (top in both, front in both, or right in both), then the faces in the other matching positions are opposite: front of view 1 with front of view 2, right with right. If the common face has **moved** to a different position, this rule does not apply — fall back on Rules 1 and 2.

### Rule 4: never together
Two faces that appear together in any single view can never be opposite. This is the quickest way to reject an option or a suggested pair.

### Standard die
A **standard** (ordinary) die has opposite faces adding to 7: 1 is opposite 6, 2 opposite 5, 3 opposite 4. Use this only when the question says the die is standard; a die showing letters has no sum rule.

### The working method
Keep a small table of opposite pairs and fill it in as you read the views. A die has exactly three opposite pairs, and each face is used once. A good order: apply Rule 2 first (it gives a whole pair at once), then Rule 3, then finish with Rule 1.

### Worked example
Three views show (P, Q, R), (R, S, P) and (Q, T, R), where the first letter is the front, second the top, third the right face. Views 1 and 2 share P and R, so the leftovers Q and S are opposite. Views 1 and 3 share Q and R in the **same positions** (front and right), so the matching positions give P opposite T. That leaves R opposite the sixth face U. All three pairs found.

### Common mistakes
- Calling two faces opposite just because they never appear together — you must strike out **four** faces first, or use Rule 2 or 3.
- Using Rule 3 when the common face sits in different positions in the two views.
- Applying the sum-7 rule to a die that is not stated to be standard.
- Forgetting that the answer must be a face of the same die: it must never appear together with the asked face.

### Quick revision
- A view shows three faces meeting at a corner; they are all adjacent.
- Rule 1: strike out every face seen with X; if four are gone, the last one is opposite.
- Rule 2: two common faces in two views → the two leftovers are opposite.
- Rule 3: common face in the same position → matching positions are opposite.
- Faces seen together are never opposite.
- Standard die: 1–6, 2–5, 3–4 (each pair sums to 7).
"""

PATTERNS["dice-positions"] = [
    P("dp-p1", "Adjacent-four (strike out)", "very common",
      "Three views of the same die; the asked face appears with four different faces across the views.",
      "Every face seen with X touches X. Strike out all of them; the only face never seen with X is opposite it.",
      "**Q.** 4 is seen with 1 and 2, then with 3 and 1, then with 5 and 3. What is opposite 4?",
      "4 has been seen with 1, 2, 3 and 5 — four faces. The only one left is **6**."),
    P("dp-p2", "Two common faces", "very common",
      "Two views repeat the same two faces; each view has one extra face.",
      "The two common faces touch both extras, so the two leftover faces are opposite each other.",
      "**Q.** Views show (A, B, C) and (A, B, D). What is opposite C?",
      "A and B are common to both views, so **D** is opposite C."),
    P("dp-p3", "Common face in the same position", "common",
      "Two views share exactly one face, and it sits in the same slot (both top, both front or both right).",
      "Matching positions hold opposite faces: front with front, top with top, right with right.",
      "**Q.** In both views A is on top; the front faces are B and C. What is opposite B?",
      "A is common and in the same position, so the front faces are opposite: **C**."),
    P("dp-p4", "Standard die (sum 7)", "common",
      "The question says 'ordinary' or 'standard' die and gives one or more face values.",
      "Opposite faces add to 7: 1–6, 2–5, 3–4. The three hidden faces sum to 21 minus the three shown.",
      "**Q.** A standard die shows 3 on top, 5 in front, 6 on the right. Sum of the hidden faces?",
      "Hidden faces are 4, 2 and 1: 21 − (3 + 5 + 6) = **7**.",
      formula=r"x + x^{*} = 7"),
    P("dp-p5", "Build the full opposite map", "occasional",
      "Three or more views; the question asks for a pair of opposite faces, or for the partner of the last face.",
      "Collect pairs with Rules 2 and 3 until two pairs are known; the two faces never yet paired form the third pair.",
      "**Q.** From the views you get A opposite D and B opposite E. What is opposite C?",
      "Only C and F are unpaired, so **F**."),
    P("dp-p6", "Which view is possible?", "occasional",
      "The opposite pairs of a labelled die are given in words; options are drawings of views.",
      "A real view never shows two opposite faces. Reject every option that shows a pair; a view with one face from each pair can always be turned up.",
      "**Q.** A is opposite D, B opposite E, C opposite F. Which view can be formed?",
      "The view showing A, B and C — one face from each opposite pair."),
]

# ======================================================================= cube-nets
NOTES["cube-nets"] = r"""### What a net is
An unfolded cube is a **net** of six squares. When it is folded, the printed side lands on the **outside**. Two squares that share an edge in the net are always **adjacent** on the cube — they can never be opposite.

### Rule 1: skip one in a straight line
In any straight row or column of the net, faces with **exactly one square between them** are opposite: 1st with 3rd, 2nd with 4th. A row of four gives two opposite pairs at once.

### Rule 2: ends of a Z (or S)
Four squares forming a **Z** shape (two and two, offset by one) have their two **end** squares opposite. This covers the pairs that no straight line gives you.

### Rule 3: pair them all
A cube has exactly three opposite pairs. Find pairs with the two rules above; the two squares left unpaired must form the last pair. As a check, every face appears in exactly one pair.

### Testing 'which cube can be formed?'
Options show a cube with three visible faces (front, top, right).
1. **Reject opposite pairs first.** If two faces shown on an option cube are opposite in the net, that cube is impossible.
2. **Check the corner order.** The three remaining options show the same three faces; only the order around their shared corner differs. Fold the net mentally: fix one face as the front, see which neighbour rises to the top and which swings to the right. Only one of the two possible orders matches — the other is the mirror image and cannot be formed.

### How to fold in your head
Choose the square that you want as the **front**. Every square attached to it folds up along the shared edge: the one above the front becomes the **top**, the one to the right becomes the **right** face, and a square two steps away in a line lands **opposite**. Track one neighbour at a time instead of the whole net.

### Worked example
A net has the row L, M, N and the column K, M, O with J below O. Skip one in the row: L opposite N. Skip one in the column: K opposite O. Left over: M and J, so M is opposite J. To test a cube showing K on top, M in front, N on the right: fold with M facing you — K (above M in the net) comes over the top, and N (right of M) swings to the right, so this cube **can** be formed. Its mirror, with L on the right, cannot.

### Common mistakes
- Treating squares that only touch at a **corner** in the net as opposite — corner-touching says nothing direct.
- Accepting a cube that shows an opposite pair (the commonest error; always do the rejection pass first).
- Reversing the order of the three faces around the corner — the mirror order of a real cube can never be formed.
- Forgetting that when a row bends around the net, the skip-one rule still applies only within one straight line.

### Quick revision
- Edge-touching squares are adjacent; opposite faces never touch.
- In a row or column, skip one square: 1st ↔ 3rd, 2nd ↔ 4th.
- Ends of a Z of four squares are opposite.
- Three pairs in total; the leftovers pair up.
- Which-cube questions: reject opposite pairs, then compare the corner order.
"""

PATTERNS["cube-nets"] = [
    P("cn-p1", "Opposite faces in a row", "very common",
      "A net with a straight row or column of three or four labelled squares.",
      "Faces with exactly one square between them in the same line are opposite.",
      "**Q.** A net has the row A, B, C. What is opposite A?",
      "Skip one square: **C** is opposite A.",
      formula=r"\text{1st} \leftrightarrow \text{3rd}"),
    P("cn-p2", "Ends of a Z shape", "very common",
      "The net bends: two squares, a step sideways, two more squares.",
      "In a Z (or S) of four squares the two end squares are opposite.",
      "**Q.** A net has the Z path P, Q, R, S. What is opposite P?",
      "The ends of the Z are opposite: **S**."),
    P("cn-p3", "Find all three pairs", "common",
      "The question asks which pair of faces is opposite, or for the partner of the last face.",
      "Pair up rows and Zs first; the two squares left over are the third pair.",
      "**Q.** Row A, B, C, D with E above B and F below C. Which faces are opposite?",
      "A–C and B–D from the row; the leftovers **E and F** are opposite."),
    P("cn-p4", "Which cube can be formed?", "very common",
      "A net is drawn; the options are four cubes showing three faces each.",
      "Reject cubes showing an opposite pair; then fold the net around the front face and match the order of the remaining two faces.",
      "**Q.** Net: column K, M, O, J with L left of M and N right of M. Which cube can be formed?",
      "Reject any cube with K–O, M–J or L–N together. The cube with K on top, M in front and N on the right folds correctly; its mirror, with L on the right, does not."),
    P("cn-p5", "Which cube cannot be formed?", "occasional",
      "Same setup, but the question asks for the impossible cube.",
      "Three options fold correctly; the impossible one either shows an opposite pair or has the mirror-image corner order.",
      "**Q.** Net with A, B, C in a row and D below B. Which cube cannot be formed?",
      "The one showing A and C together — they are opposite in the net."),
]

# ======================================================================= painted-cubes
NOTES["painted-cubes"] = r"""### The picture to keep in mind
A big cube of side **n** (made of n × n × n unit cubes) is painted on the outside and then cut into n³ unit cubes. A small cube keeps paint only on the faces that were on the **surface** of the big cube. Its position decides how many of its faces are painted.

### The four counts
- **3 faces painted — corners.** A corner cube touches three faces of the big cube. There are always **8**, whatever n is.
- **2 faces painted — edges.** Each of the 12 edges holds n cubes, but the 2 ends are corners, leaving **n − 2** per edge: 12(n − 2).
- **1 face painted — face centres.** On each face, the cubes not on any edge form an (n − 2) × (n − 2) block: 6(n − 2)².
- **0 faces painted — the core.** Peeling one layer from every side leaves an (n − 2) × (n − 2) × (n − 2) block: (n − 2)³.

### Why (n − 2) everywhere
A cube on an edge but not at a corner has lost 2 of its edge-mates to the corners; a face block has lost its border ring. Always subtract 2 before squaring or cubing — using n instead of (n − 2) is the classic error.

### The total check
8 + 12(n − 2) + 6(n − 2)² + (n − 2)³ = n³. Test with n = 3: 8 + 12 + 6 + 1 = 27. Test with n = 4: 8 + 24 + 24 + 8 = 64. If your four counts do not add to n³, something is wrong.

### Combined questions
- **At least one face painted:** everything except the core, n³ − (n − 2)³.
- **At least two faces painted:** corners plus edges, 8 + 12(n − 2).
- Adding the counts of two classes is enough — no new formulas are needed.

### Working backwards
Sometimes a count is given and n is asked. Divide: if exactly-two cubes number 12(n − 2) = 24, then n − 2 = 2 and n = 4. If exactly-one cubes number 6(n − 2)² = 54, then (n − 2)² = 9 and n = 5. Then answer the real question with n.

### Cuboid a × b × c
The same positions, with each edge keeping its own leftover:
- corners: **8**;
- edges: 4[(a − 2) + (b − 2) + (c − 2)];
- face centres: 2[(a − 2)(b − 2) + (b − 2)(c − 2) + (c − 2)(a − 2)];
- core: (a − 2)(b − 2)(c − 2).
These hold when every side is at least 2. Check: 5 × 4 × 3 gives edges 4(3 + 2 + 1) = 24 and core 3 × 2 × 1 = 6.

### Common mistakes
- Writing n instead of (n − 2) inside the formulas.
- Counting 8 corners as 12(n − 2) + 8 twice, or forgetting that corners are never counted among edge cubes.
- Adding the four counts and expecting n³ − something: they must total exactly n³.
- For a cuboid, using n − 2 with a single n instead of each side's own (side − 2).

### Quick revision
- 3 painted: 8 (corners, any size).
- 2 painted: 12(n − 2) (edges).
- 1 painted: 6(n − 2)² (face centres).
- 0 painted: (n − 2)³ (core).
- Check: the four counts add to n³.
- At least one: n³ − (n − 2)³; at least two: 8 + 12(n − 2).
"""

PATTERNS["painted-cubes"] = [
    P("pc-p1", "Three faces painted (corners)", "very common",
      "Cube painted and cut; the question asks for cubes with all three / three or more painted faces.",
      "Only the 8 corner cubes have three painted faces, for every side length.",
      "**Q.** A cube of side 7 is painted and cut into unit cubes. How many have three painted faces?",
      "Always **8**."),
    P("pc-p2", "Two faces painted (edges)", "very common",
      "Asks for exactly-two cubes after cutting a painted cube of side n.",
      "Each of the 12 edges keeps n − 2 non-corner cubes: 12(n − 2).",
      "**Q.** Side 5, painted, cut. How many cubes have exactly two painted faces?",
      "12 × (5 − 2) = **36**.",
      formula=r"12(n-2)"),
    P("pc-p3", "One face painted (face centres)", "very common",
      "Asks for exactly-one cubes.",
      "Each face keeps an (n − 2) × (n − 2) block away from the edges: 6(n − 2)².",
      "**Q.** Side 6, painted, cut. How many cubes have exactly one painted face?",
      "6 × 4² = **96**.",
      formula=r"6(n-2)^{2}"),
    P("pc-p4", "No face painted (core)", "common",
      "Asks for completely unpainted cubes.",
      "Strip one layer from each side; the hidden core is (n − 2)³.",
      "**Q.** Side 5, painted, cut. How many cubes have no painted face?",
      "(5 − 2)³ = **27**.",
      formula=r"(n-2)^{3}"),
    P("pc-p5", "Combined counts", "common",
      "Asks for 'at least one', 'at least two', or the sum of two classes.",
      "At least one = n³ − (n − 2)³. At least two = 8 + 12(n − 2). Otherwise add the wanted classes.",
      "**Q.** Side 4, painted, cut. How many cubes have at least two painted faces?",
      "8 + 12 × 2 = **32**.",
      formula=r"n^{3} - (n-2)^{3}"),
    P("pc-p6", "Painted cuboid", "occasional",
      "The block is a × b × c, not a cube.",
      "Corners 8; edges 4[(a−2)+(b−2)+(c−2)]; face centres 2[(a−2)(b−2)+(b−2)(c−2)+(c−2)(a−2)]; core (a−2)(b−2)(c−2).",
      "**Q.** A 5 × 4 × 3 cuboid, painted and cut. How many cubes have exactly two painted faces?",
      "4 × (3 + 2 + 1) = **24**."),
    P("pc-p7", "Find n from a count", "occasional",
      "A count of painted cubes is given; the side n (or another count) is asked.",
      "Invert the formula: divide by 12 (edges) or by 6 and square-root (faces), add 2 to get n, then compute what is asked.",
      "**Q.** 36 cubes have exactly two painted faces. How many have exactly one?",
      "12(n − 2) = 36 gives n = 5, so 6 × 3² = **54**."),
]

# ======================================================================= topic PYQ patterns
PYQS = [
    PYQ("Opposite face from two/three positions", "very common",
        "Two or three drawings of the same die; ask the face opposite X.",
        "Strike out the faces seen with X, or use the two-common-faces / same-position rules.",
        "dice-positions",
        "**Q.** Two views share A and B; the other faces are C and D. Opposite of C?",
        "D."),
    PYQ("Standard die (sum 7)", "occasional",
        "The die is stated to be standard or ordinary.",
        "Opposite pairs 1–6, 2–5, 3–4; hidden faces sum to 21 minus the shown three.",
        "dice-positions",
        "**Q.** A standard die shows 2, 3 and 6. Sum of the hidden faces?",
        "21 − 11 = 10."),
    PYQ("Possible view of a labelled die", "occasional",
        "Opposite pairs are given in words; options are views.",
        "A view can never show two opposite faces; pick the option with one face from each pair.",
        "dice-positions",
        "**Q.** A–D, B–E, C–F are pairs. Which view is possible?",
        "The one showing A, B, C."),
    PYQ("Opposite faces in a net", "very common",
        "An unfolded sheet of six labelled squares.",
        "Skip one in a line; ends of a Z; leftovers form the last pair.",
        "cube-nets",
        "**Q.** Row A, B, C, D. Opposite of B?",
        "D."),
    PYQ("Which cube can be formed", "common",
        "Net in the question, four cubes in the options.",
        "Reject cubes showing an opposite pair; then match the corner order by folding.",
        "cube-nets",
        "**Q.** Which of the four cubes can be made from the net?",
        "The only one without an opposite pair and with the correct corner order."),
    PYQ("Which cube cannot be formed", "occasional",
        "Same figures, reversed question.",
        "Three options are formable; the impossible one shows an opposite pair or a mirrored corner.",
        "cube-nets",
        "**Q.** Which cube cannot be made?",
        "The one whose three faces run in the reverse order around the corner."),
    PYQ("Painted cube cut into n³ pieces", "very common",
        "A painted cube of side n is cut into unit cubes.",
        "Use 8 / 12(n − 2) / 6(n − 2)² / (n − 2)³ and the n³ total check.",
        "painted-cubes",
        "**Q.** Side 4, painted, cut. How many cubes have two painted faces?",
        "12 × 2 = 24."),
    PYQ("Painted cuboid", "common",
        "The block is a × b × c.",
        "Edges 4[(a−2)+(b−2)+(c−2)]; core (a−2)(b−2)(c−2); corners 8.",
        "painted-cubes",
        "**Q.** 5 × 4 × 3, painted, cut. Cubes with no painted face?",
        "(3)(2)(1) = 6."),
]
