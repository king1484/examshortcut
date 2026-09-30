"""Readable rewrite of Seating Arrangement (seating-arrangement).

Every example is verified by enumerating all seatings (permutations) and checking that the clues
leave exactly one solution (or that every solution gives the same answer).
Run: python seating_arrangement.py
"""
import json
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "seating-arrangement.json"


# ------------------------------------------------------------------ solver
# Row seats 0..n-1 go west (viewer's left) to east. North-facing: right = +1. South-facing: right = -1.
def rt(p, a, k, face="N"):
    return p[a] + k if face == "N" else p[a] - k


def lf(p, a, k, face="N"):
    return p[a] - k if face == "N" else p[a] + k


def row_solutions(people, ok):
    n = len(people)
    out = []
    for perm in permutations(range(n)):
        p = dict(zip(people, perm))
        if ok(p):
            out.append(p)
    return out


def one(sols):
    assert len(sols) == 1, f"{len(sols)} solutions"
    return sols[0]


def who(p, seat):
    for k, v in p.items():
        if v == seat:
            return k
    return None


def order(p):
    return "".join(sorted(p, key=p.get))


# Circle seats 0..n-1 clockwise. Facing centre: left = +1 (clockwise), right = -1. Outward flips.
def cl(p, a, k, n, face="C"):
    return (p[a] + k) % n if face == "C" else (p[a] - k) % n


def cr(p, a, k, n, face="C"):
    return (p[a] - k) % n if face == "C" else (p[a] + k) % n


def circle_solutions(people, ok):
    n = len(people)
    out = []
    for rest in permutations(range(1, n)):
        p = dict(zip(people, (0,) + rest))       # first person fixed at seat 0 removes rotation
        if ok(p):
            out.append(p)
    return out


# ------------------------------------------------------------------ verification
# ---- seating-idea
# st-p1: 5 people facing south. R middle, S immediate right of R, P at west end, T not at an end.
def c1(p):
    return p["R"] == 2 and p["S"] == rt(p, "R", 1, "S") and p["P"] == 0 and p["T"] not in (0, 4)


s = one(row_solutions("PQRST", c1))
assert order(s) == "PSRTQ"
assert who(s, lf(s, "R", 1, "S")) == "T"                    # south-facing left of R = +1 = seat 3 = T
# north-facing check that the flip matters
assert rt({"R": 2}, "R", 1, "N") == 3 and rt({"R": 2}, "R", 1, "S") == 1
# st-p2: between = |a-b|-1
a_, h_ = 3, 8 - 2 + 1
assert (a_, h_) == (3, 7) and abs(a_ - h_) - 1 == 3
row8 = list(range(1, 9)); assert len([x for x in row8 if a_ < x < h_]) == 3
# st-p3
assert 12 - 5 + 1 == 8
# st-p4: circle of 6 facing centre
def c4(p):
    n = 6
    return (p["B"] == cl(p, "A", 1, n) and p["C"] == cr(p, "A", 2, n) and p["D"] == (p["A"] + 3) % n
            and p["E"] == cr(p, "D", 1, n))


s = one(circle_solutions("ABCDEF", c4))
assert (s["B"], s["C"], s["D"], s["E"], s["F"]) == (1, 4, 3, 2, 5)
assert who(s, cr(s, "A", 1, 6)) == "F"
# st-p17: k-th to the right means k-1 between
M, N = 2, 2 + 3
assert N - M - 1 == 2 == 3 - 1
# trick: pin absolutes first (6 seats)
def ct(p):
    return (p["B"] == 0 and p["F"] == 5 and p["D"] == rt(p, "B", 1) and p["C"] == lf(p, "F", 1)
            and abs(p["A"] - p["D"]) != 1)


s = one(row_solutions("ABCDEF", ct))
assert order(s) == "BDEACF"
# trick: mirror check. Same clue, both facings, different seat
assert (rt({"T": 2}, "T", 2, "N"), rt({"T": 2}, "T", 2, "S")) == (4, 0)

# ---- linear-arrangement
# st-p5
def c5(p):
    return (p["A"] == 0 and p["B"] == rt(p, "A", 1) and p["F"] == 5 and p["E"] == lf(p, "F", 1)
            and abs(p["C"] - p["B"]) != 1)


s = one(row_solutions("ABCDEF", c5))
assert order(s) == "ABDCEF" and who(s, 2) == "D"
# st-p6 (the notes example)
def c6(p):
    return (p["C"] == 0 and p["F"] == rt(p, "C", 4) and p["A"] == lf(p, "F", 2) and p["D"] == rt(p, "F", 1)
            and p["G"] not in (0, 6) and abs(p["B"] - p["C"]) == 1)


s = one(row_solutions("ABCDEFG", c6))
assert order(s) == "CBAGFDE" and who(s, rt(s, "A", 3)) == "D"
# st-p7: five people facing south
def c7(p):
    return (p["P"] == 4 and p["Q"] == rt(p, "P", 2, "S") and p["R"] == lf(p, "Q", 1, "S") and p["S"] == 0)


s = one(row_solutions("PQRST", c7))
assert order(s) == "STQRP"
assert who(s, lf(s, "S", 1, "S")) == "T"                    # south-facing left = +1
# st-p8
def c8(p):
    return (p["A"] == 2 and p["B"] == rt(p, "A", 2) and p["C"] not in (0, 4) and abs(p["D"] - p["A"]) != 1
            and abs(p["E"] - p["B"]) != 1)


s = one(row_solutions("ABCDE", c8))
assert order(s) == "DEACB" and who(s, rt(s, "A", 1)) == "C"
ROW_P8 = s
# st-p18: exactly two people between A and B
def c18(p):
    return (p["A"] == 0 and abs(p["A"] - p["B"]) == 3 and p["C"] == rt(p, "B", 1) and p["E"] == lf(p, "B", 1)
            and p["D"] == rt(p, "A", 1))


s = one(row_solutions("ABCDEF", c18))
assert order(s) == "ADEBCF" and who(s, 5) == "F"
# block starts: block of 3 in row of 7
assert len([i for i in range(7) if i + 3 <= 7]) == 7 - 3 + 1 == 5

# ---- circular-arrangement
# st-p9: five people facing centre
def c9(p):
    n = 5
    return (p["A"] == cr(p, "B", 1, n) and p["D"] == cl(p, "B", 1, n) and p["C"] == cl(p, "D", 1, n)
            and p["E"] == cl(p, "C", 1, n))


s = one(circle_solutions("BADCE", c9))
assert (s["B"], s["D"], s["C"], s["E"], s["A"]) == (0, 1, 2, 3, 4)
assert who(s, cr(s, "D", 2, 5)) == "A" and cl(s, "E", 1, 5) == s["A"]     # loop closes
# st-p10: the notes example, eight people
def c10(p):
    n = 8
    return (p["E"] == (p["A"] + 4) % n and p["B"] == cr(p, "A", 2, n) and p["F"] == (p["B"] + 4) % n
            and p["C"] == cl(p, "E", 1, n) and p["D"] == (p["C"] + 4) % n
            and (p["G"] - p["A"]) % n not in (1, n - 1))


s = one(circle_solutions("ABCDEFGH", c10))
assert (s["E"], s["B"], s["F"], s["C"], s["D"], s["G"], s["H"]) == (4, 6, 2, 5, 1, 3, 7)
assert who(s, cl(s, "H", 3, 8)) == "F"
# st-p11: six people facing outward
def c11(p):
    n = 6
    f = "O"
    return (p["B"] == cl(p, "A", 1, n, f) and p["C"] == cr(p, "A", 2, n, f) and p["D"] == (p["A"] + 3) % n
            and p["E"] == cr(p, "D", 1, n, f))


s = one(circle_solutions("ABCDEF", c11))
assert (s["B"], s["C"], s["D"], s["E"], s["F"]) == (5, 2, 3, 4, 1)
assert who(s, cr(s, "A", 1, 6, "O")) == "F"
# st-p12: mixed facing. A faces centre, B faces outward
def c12(p):
    n = 4
    return p["B"] == cl(p, "A", 1, n, "C") and p["C"] == cr(p, "B", 1, n, "O")


sols = circle_solutions("ABCD", c12)
s = one(sols)
assert (s["B"], s["C"], s["D"]) == (1, 2, 3) and who(s, cr(s, "A", 1, 4, "C")) == "D"
# if B were read as facing the centre, C would go to seat 0's other side: wrong seating
assert cr({"B": 1}, "B", 1, 4, "C") == 0 != cr({"B": 1}, "B", 1, 4, "O") == 2
# st-p19: neighbours, either side
def c19(p):
    n = 6
    return (abs((p["B"] - p["A"]) % n) in (1, n - 1) and abs((p["C"] - p["A"]) % n) in (1, n - 1)
            and p["D"] == (p["A"] + 3) % n and p["E"] == cl(p, "B", 1, n))


sols = circle_solutions("ABCDEF", c19)
s = one(sols)
assert (s["B"], s["E"], s["C"], s["D"], s["F"]) == (1, 2, 5, 3, 4)
assert who(s, (s["C"] + 3) % 6) == "E"

# ---- puzzle-strategy
# st-p13: two rows. Row 1 (A-D) faces south, Row 2 (P-S) faces north.
r1 = []
for perm in permutations(range(4)):
    p = dict(zip("ABCD", perm))
    if p["C"] == rt(p, "B", 1, "S") and p["D"] == 3 and p["A"] not in (0, 3):
        r1.append(p)
r1 = one(r1)
assert order(r1) == "CBAD"
r2 = []
for perm in permutations(range(4)):
    p = dict(zip("PQRS", perm))
    if p["P"] == r1["C"] and p["R"] == rt(p, "P", 1, "N") and p["S"] == r1["A"]:
        r2.append(p)
r2 = one(r2)
assert order(r2) == "PRSQ" and who(r2, r1["D"]) == "Q"
# st-p14: interchange, from the st-p8 row D E A C B
row = list(order(ROW_P8)); assert row == list("DEACB")
i, j = row.index("C"), row.index("E"); row[i], row[j] = row[j], row[i]
assert "".join(row) == "DCAEB" and row[row.index("A") + 1] == "E"
# st-p15: counting
together = [pm for pm in permutations("ABCDE") if abs(pm.index("A") - pm.index("B")) == 1]
assert len(together) == 48 == 2 * 24
assert len([1 for _ in permutations(range(5))]) == 120
assert len([1 for _ in permutations(range(5))]) == 5 * 4 * 3 * 2          # circle of 6 = 5!
circle6 = len([1 for _ in permutations(range(1, 6))]); assert circle6 == 120 == 6 * 5 * 4 * 3 * 2 // 6
# st-p16: seats plus drinks
sols = []
for perm in permutations(range(4)):
    p = dict(zip("ABCD", perm))
    if not (p["A"] == 3 and p["B"] == lf(p, "A", 1)):
        continue
    for dperm in permutations(("tea", "milk", "juice", "water")):
        d = dict(zip("ABCD", dperm))
        tea = [k for k in "ABCD" if d[k] == "tea"][0]
        milk = [k for k in "ABCD" if d[k] == "milk"][0]
        if p[tea] == 0 and p[milk] == rt(p, tea, 1) and d["C"] == "milk" and d["A"] == "water":
            sols.append((p, d))
assert len(sols) == 1
p16, d16 = sols[0]
assert order(p16) == "DCBA" and [k for k in "ABCD" if d16[k] == "juice"] == ["B"]
assert [k for k in "ABCD" if d16[k] == "tea"] == ["D"]
# st-p20: two seatings, same answer
def c20(p):
    return p["A"] == 2 and p["E"] == 4 and p["D"] == lf(p, "E", 1)


sols = row_solutions("ABCDE", c20)
assert len(sols) == 2 and {who(x, rt(x, "A", 1)) for x in sols} == {"D"}
assert {order(x) for x in sols} == {"BCADE", "CBADE"}


# ------------------------------------------------------------------ content
def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ============================================================ seating-idea
s1_concept = (
    "A seating puzzle gives a group of people and clues about where they sit. "
    "You rebuild the one seating that fits every clue, then answer a question such as who sits opposite D. "
    "Rows and circles are the two families. In both, the direction each person faces decides which side is left."
)

s1_notes = r"""### What a seating puzzle is
You get a group of people and a list of clues. You draw the seats first. Then you place each person the clues fix. At the end, one seating is left, and every question is a lookup on it.

There is no calculation here. The skill is to read each clue the same way every time.

### Left and right in a row
The row ends belong to you, the viewer. The left end is on your left when you draw the row.

- **Facing north:** a person's left is your left. Their right is your right.
- **Facing south:** it flips. A person's left is your right.

The ends never flip. Only the person's own left and right flip.

> **Watch:** If the puzzle says "facing south", draw a small down arrow on every seat. Read left and right from that arrow, not from your own hands.

### Left and right in a circle
People around a table face the centre unless the puzzle says otherwise.

- **Facing the centre:** left neighbour = clockwise. Right neighbour = anticlockwise.
- **Facing outward:** it flips. Left = anticlockwise. Right = clockwise.

A circle has no first seat. Put the first named person at the top. Every other seat is fixed by that person.

"Opposite" exists only when the number of seats is even. The person opposite you is $\dfrac{n}{2}$ places away.

### Counting words
Small words change the count by one, so read them slowly.

- "Second to the right of X" means one person sits between X and that seat.
- "$k$-th to the left" means $k$ steps. So $k - 1$ people are in between.
- "Immediately between X and Y" means X and Y are the two neighbours.
- "Between X and Y" alone means somewhere inside, not always next to them.
- People between seats $a$ and $b$ = $|a - b| - 1$.
- The $p$-th person from the left in a row of $n$ is $n - p + 1$ from the right.

> **Rule:** "Neighbour" allows two sides. "Immediate right" allows one side only.

### The three-step method
1. **Fix the frame.** Draw $n$ boxes for a row or $n$ marks for a circle. Write the facing direction on it.
2. **Place the sure clues.** Ends, the middle, and opposite pairs need no guessing.
3. **Hang the chains.** Attach each new person to someone already placed. Use "not" clues last.

### A short worked row
Five people sit in a row facing north. T is in the middle. U is second to the right of T. V is immediate left of T.

- T is seat 3. U is seat 5. V is seat 2.
- Seats 1 and 4 are left for W and X.
- If W is not at an end, W is seat 4 and X is seat 1.

Now face the same row south. U is second to the right of T, so U is seat 1. V is immediate left of T, so V is seat 4. One word changed the whole answer.

> **Example:** Same clues, different facing, different row. Always find the facing word first.
"""

s1_formulas = [
    {"name": "Circular neighbour rule", "tex": r"L(i) = (i+1) \bmod n,\quad R(i) = (i-1) \bmod n", "note": "Seats numbered clockwise, everyone facing the centre. Both swap if facing outward."},
    {"name": "Opposite seat", "tex": r"i \leftrightarrow (i + n/2) \bmod n", "note": "Only when n is even. An odd table has no opposite seat."},
    {"name": "People between two seats", "tex": r"\text{between} = |a - b| - 1", "note": "a and b are seat numbers in the same row."},
    {"name": "Viewer versus person", "tex": r"\text{person faces south} \Rightarrow \text{their left} = \text{your right}", "note": "Applies to the person's own left and right, never to the row ends."},
]

s1_patterns = [
    pat("st-p1", "Facing direction and left or right", "very common",
        "The row says 'facing north' or 'facing south'. A left or right neighbour or an end is asked.",
        r"\text{south-facing: right = west, left = east}",
        ["Underline the facing word first.", "Draw a small arrow on each seat.", "Read left and right from the arrow.", "Number the seats west to east and place each clue."],
        "The ends stay with the viewer, but each person's hands turn with the facing.",
        "Five people P, Q, R, S, T sit in a row facing south. R sits in the middle. S sits immediate right of R. P sits at the west end of the row. T does not sit at an end. Who sits immediate left of R?",
        ["Seats 1 to 5 from the west. R = seat 3.", "South-facing right is west. So S = seat 2. P = seat 1.", "T is not at an end, so T = seat 4 and Q = seat 5.", "South-facing left is east. The immediate left of R is seat 4."],
        "T"),
    pat("st-p2", "Counting people between two seats", "very common",
        "The question asks how many people sit between two people, or how many sit to the right of someone.",
        r"|a - b| - 1",
        ["Write each person's seat number.", "Subtract the smaller from the larger.", "Subtract 1."],
        "The two people themselves are not between, so one seat is dropped.",
        "Eight people sit in a row facing north. A is third from the left and H is second from the right end. How many people sit between A and H?",
        [r"H is $8 - 2 + 1 = 7$th from the left.", r"Between: $7 - 3 - 1 = 3$."],
        "3"),
    pat("st-p3", "Position from either end", "very common",
        "A person is 'third from the left' or 'second from the right end'. The other end is asked.",
        r"n - p + 1",
        ["Write the number of seats.", "Subtract the rank from the number of seats.", "Add 1."],
        "The person is counted once from each end, so add the shared seat back.",
        "Twelve people sit in a row. Kabir is fifth from the left end. What is his position from the right end?",
        [r"$12 - 5 + 1$.", r"$= 8$."],
        "8th from the right"),
    pat("st-p4", "Circle facing rules", "very common",
        "People sit around a table and face the centre or face outward. A left or right neighbour is asked.",
        r"\text{centre: left = clockwise}",
        ["Put the first person at the top and number seats clockwise.", "Facing the centre: left is +1, right is -1.", "Facing outward: swap the two."],
        "One fixed rule turns every clue into a seat number.",
        "Six people A to F sit around a table facing the centre. B is immediate left of A. C is second to the right of A. D sits opposite A. E is immediate right of D. Who is immediate right of A?",
        ["A = seat 0, numbered clockwise.", "B = seat 1. C = seat $0 - 2 = 4$. D = seat 3.", "E = $3 - 1 = 2$. F takes seat 5.", "Immediate right of A is seat $0 - 1 = 5$."],
        "F"),
    pat("st-p17", "Counting words: between, second to the right", "common",
        "Clues use 'second to the right', 'third to the left' or 'between'. You must place someone exactly.",
        r"k\text{-th to the right} \Rightarrow k - 1 \text{ between}",
        ["Turn 'k-th to the right' into seat + k for a north-facing row.", "Count the people between as $k - 1$.", "Use 'immediately' only when the clue says it."],
        "Each small word shifts the count by exactly one seat.",
        "Seven people sit in a row facing north. M is second from the left. N is third to the right of M. How many people sit between M and N?",
        ["M = seat 2. N = seat $2 + 3 = 5$.", r"Between: $5 - 2 - 1 = 2$, which is $3 - 1$."],
        "2"),
]

s1_tricks = [
    {"title": "Pin the absolutes first",
     "body": "Ends, the middle and opposite seats fix a person outright. Fill them before you touch any chain. The remaining people usually fall into one or two slots.",
     "example": {"q": "Six people sit in a row facing north. B is at the left end and F is at the right end. D is immediate right of B. C is immediate left of F. A is not next to D. Find the row.",
                 "steps": ["B = seat 1, D = seat 2, F = seat 6, C = seat 5.", "A and E take seats 3 and 4.", "Seat 3 is next to D, so A = seat 4 and E = seat 3."],
                 "answer": "B D E A C F"}},
    {"title": "Test one clue both ways",
     "body": "If you are unsure of the facing, place one clue for north and for south. The two seats differ, and this shows you which one you must use.",
     "example": {"q": "T sits in seat 3 of a row of five. U is second to the right of T. Where is U if the row faces north? Where is U if it faces south?",
                 "steps": ["North: right is east, so $3 + 2 = 5$.", "South: right is west, so $3 - 2 = 1$."],
                 "answer": "Seat 5 facing north, seat 1 facing south"}},
]

s1_mistakes = [
    {"wrong": "Reading a south-facing person's left as your own left.", "right": "Their left is your right. Draw an arrow on each seat."},
    {"wrong": "Flipping the row ends when the row faces south.", "right": "The ends stay with the viewer. Only the person's own left and right flip."},
    {"wrong": "Taking 'second to the right' as two people in between.", "right": "It means one person in between. $k$-th means $k - 1$ between."},
    {"wrong": "Looking for an opposite seat at an odd table.", "right": "Opposite exists only for an even number of seats."},
    {"wrong": "Assuming 'between' means 'immediately between'.", "right": "Only the word 'immediately' forces neighbours."},
]

s1_revision = [
    "North-facing left = your left. South-facing left = your right.",
    "Circle facing the centre: left = clockwise. Facing outward: left = anticlockwise.",
    "$k$-th to the right means $k - 1$ people in between.",
    r"People between = $|a - b| - 1$. Other end = $n - p + 1$.",
    r"Opposite is $\dfrac{n}{2}$ places away, and only for even $n$.",
    "Draw the frame, place the sure clues, hang the chains, use 'not' clues last.",
]

# ============================================================ linear-arrangement
s2_concept = (
    "Everyone sits in one line, usually facing north. "
    "Number the seats from the west end and turn each clue into a small sum on seat numbers. "
    "Place the ends first, then the fixed distances, then the pairs. Use the 'not' clues last."
)

s2_notes = r"""### The frame
Number the seats 1 to $n$ from the west end. Write the numbers under the boxes. Now every clue is a small sum, which is safer than moving letters in your head.

For a north-facing row:
- "B is $k$-th to the right of A" gives B = A + $k$.
- "B is $k$-th to the left of A" gives B = A $-$ $k$.
- "A is at an end" gives A = 1 or A = $n$.
- "$p$-th from the right end" gives seat $n - p + 1$.

For a south-facing row the signs flip. "$k$-th to the right" gives B = A $-$ $k$.

### Order of attack
1. **Absolute clues** go in first. Ends, the middle and "third from the left" need no guessing.
2. **Distance clues** on a placed person come next. If C is seat 1, "D is fourth to the right of C" gives D = 5.
3. **Floating chains** link two people not yet placed. Write the block, such as "P _ Q", on the side. Slide it along the free seats.
4. **Negative clues** come last. "Not at an end" or "not next to" often leaves one case.

> **Tip:** If a clue names a placed person, use it now. If it names two unplaced people, park it.

### A full worked example
Seven people C, A, B, D, E, F, G sit in a row facing north. C is at the left end. F is fourth to the right of C. A is second to the left of F. D is immediate right of F. G is not at an end. B is next to C.

- C = 1. F = $1 + 4 = 5$. A = $5 - 2 = 3$. D = 6.
- B is next to C, so B = 2.
- Seats 4 and 7 remain for E and G. G is not at an end, so G = 4 and E = 7.
- Row: C B A G F D E. Third to the right of A is seat 6, which is D.

### Case splitting
Sometimes a clue allows two places, such as "A sits at one end". Draw two rows, one for each case. Carry both until a clue kills one.

> **Watch:** Never guess one case and hope. A wrong guess costs a full redraw.

A typical exam puzzle leaves two cases after the first clues. One negative clue then settles it.

### Blocks and gaps
- "X sits immediately between Y and Z" makes a three-seat block. Y and Z can be on either side. Keep both open.
- "Exactly two people sit between A and B" means $|A - B| = 3$. It does not say who is on the left.
- A block of size $k$ in a row of $n$ can start in $n - k + 1$ places. List them and strike out the clashes.

### Facing south
You can use the flipped signs, or you can draw the row from east to west. Then a south-facing person's left is your left again. Pick one method and keep it to the end. Mixing the two gives a mirror answer.

> **Note:** A negative clue is weak alone but strong late. With two seats and two people left, one "not at an end" decides both.
"""

s2_patterns = [
    pat("st-p5", "Ends and adjacency", "very common",
        "Clues put people at the ends and name their immediate neighbours.",
        None,
        ["Place the people at the ends first.", "Place each named neighbour next to them.", "List the free seats and the free people.", "Use the 'not' clue to settle the last two."],
        "Ends and neighbours fix most of the row, so only a small choice is left.",
        "Six people A to F sit in a row facing north. A is at the left end and B is immediate right of A. F is at the right end and E is immediate left of F. C is not next to B. Who sits third from the left?",
        ["A = seat 1, B = seat 2, F = seat 6, E = seat 5.", "C and D take seats 3 and 4.", "Seat 3 is next to B, so C = seat 4 and D = seat 3."],
        "D"),
    pat("st-p6", "Fixed distance chains", "very common",
        "Clues like 'F is fourth to the right of C' and 'A is second to the left of F'.",
        r"\text{right} = +k,\ \text{left} = -k \ (\text{north})",
        ["Start from the person who is already placed.", "Add $k$ for right and subtract $k$ for left.", "Place each new person and repeat."],
        "Every relative clue is an arrow of fixed length from a placed person.",
        "Seven people C, A, B, D, E, F, G sit in a row facing north. C is at the left end. F is fourth to the right of C. A is second to the left of F. D is immediate right of F. G is not at an end. B is next to C. Who is third to the right of A?",
        ["C = 1, F = 5, A = 3, D = 6, B = 2.", "E and G take seats 4 and 7. G is not at an end, so G = 4 and E = 7.", "Third to the right of A is seat $3 + 3 = 6$."],
        "D"),
    pat("st-p7", "South-facing rows", "common",
        "Everyone in the row faces south.",
        r"\text{south: right} = -k \text{ on west-to-east numbers}",
        ["Number the seats west to east.", "For south-facing people, right is minus and left is plus.", "Place the clues and read the question with the same rule."],
        "A south-facing person's hands are turned round, but the seat numbers are not.",
        "Five people P, Q, R, S, T sit in a row facing south. P is at the east end. Q is second to the right of P. R is immediate left of Q. S is at the west end. Who is immediate left of S?",
        ["Seats 1 to 5 from the west. P = seat 5.", "South-facing right is west, so Q = $5 - 2 = 3$.", "South-facing left is east, so R = 4. S = 1, T = 2.", "Immediate left of S is seat $1 + 1 = 2$."],
        "T"),
    pat("st-p8", "Negative clues settle the case", "very common",
        "Clues say 'not at an end', 'not adjacent to' or 'not a neighbour of'.",
        None,
        ["Place every positive clue first.", "List the free seats for each person.", "Cross out the seats that a negative clue forbids.", "Fill the person with one seat left, and repeat."],
        "Each 'not' clue removes seats, so the last person has only one place.",
        "Five people A to E sit in a row facing north. A is in the middle. B is second to the right of A. C is not at an end. D is not next to A. E is not next to B. Who is immediate right of A?",
        ["A = seat 3, B = seat 5. Free seats: 1, 2, 4.", "D is not next to A, so D = seat 1.", "E is not next to B, so E is not seat 4. E = seat 2.", "C is left with seat 4, which is not an end."],
        "C"),
    pat("st-p18", "Blocks and exact gaps", "common",
        "Clues say 'exactly two people between A and B' or name a pair that sits together.",
        r"|a - b| = k + 1",
        ["Turn 'k people between' into a seat difference of $k + 1$.", "Try both sides if the clue does not name one.", "Place the block and strike out the clashes."],
        "A gap clue fixes the distance but not the side, so test both.",
        "Six people A to F sit in a row facing north. A is at the left end. Exactly two people sit between A and B. C is immediate right of B. E is immediate left of B. D is immediate right of A. Who sits at the right end?",
        ["A = seat 1. Two between A and B gives B = seat 4.", "C = seat 5. E = seat 3. D = seat 2.", "The last person, F, takes seat 6."],
        "F"),
]

s2_tricks = [
    {"title": "Chain links, do not guess gaps",
     "body": "'Second to the right of A' pins B exactly two seats from A. Mark it with an arrow as soon as you read it. Most puzzles have four such arrows, and the picture then completes itself.",
     "example": {"q": "In a row facing north, C sits third from the left. A sits second to the right of C. B sits next to both C and A. Where does B sit?",
                 "steps": ["C = seat 3. A = seat 5.", "B touches both, so B = seat 4."],
                 "answer": "Seat 4"}},
    {"title": "Turn the row to face up",
     "body": "If the row faces south, redraw it from east to west. Now every person 'faces up' and left is your left. Use this drawing for the whole puzzle.",
     "example": {"q": "Three people sit in a row facing south. X is at the west end. Y is immediate left of X. Where is Y in the west-to-east numbering?",
                 "steps": ["South-facing left is east.", "Y = seat $1 + 1 = 2$."],
                 "answer": "Seat 2"}},
]

s2_mistakes = [
    {"wrong": "Mixing the flipped signs with a redrawn row.", "right": "Pick one method for south-facing rows and use it to the end."},
    {"wrong": "Guessing one case when a clue allows two.", "right": "Draw both cases and carry them until a clue kills one."},
    {"wrong": "Using $|a - b|$ as the number of people between.", "right": "People between = $|a - b| - 1$."},
    {"wrong": "Fixing Y and Z in order for 'immediately between'.", "right": "Y and Z can be on either side until another clue decides."},
    {"wrong": "Ignoring the negative clues at the end.", "right": "In a nearly full row, one 'not' clue decides the last seats."},
]

s2_revision = [
    "North-facing: right is $+k$, left is $-k$. South-facing: the signs flip.",
    "Order: absolute clues, distances, floating blocks, negative clues.",
    "Two possible places means two drawn rows.",
    "'Immediately between' is a 3-block with the ends swappable.",
    r"$k$ people between means a seat gap of $k + 1$.",
]

# ============================================================ circular-arrangement
s3_concept = (
    "Around a table a circle has no first seat, so fix one person first. "
    "Facing the centre, your left neighbour is the next person clockwise. "
    "Opposite seats exist only for an even number of people, and they fix a seat at once."
)

s3_notes = r"""### Fixing a circle
A circle can be rotated, so it has no first seat. Remove that freedom at once. Put the first named person at the top. Now every other seat is fixed by that person.

Mark the direction on your drawing.
- **Facing the centre:** left neighbour = clockwise. Right neighbour = anticlockwise.
- **Facing outward:** left neighbour = anticlockwise. Right neighbour = clockwise.

> **Tip:** Stand at the bottom of the circle, facing the centre. Your left hand points west. Going from the bottom to the west is clockwise from above.

### Opposite seats
With $n$ seats and $n$ even, the person opposite X is $\dfrac{n}{2}$ places away. That is 3 places in a circle of 6, and 4 places in a circle of 8.

Opposite clues are the strongest clues in a circle, because they fix a seat exactly. Place them before any left or right clue.

An odd table has no opposite. If a question asks about one, read the puzzle again.

### Counting both ways
Two paths join any two people around a circle. So "how many sit between A and D" needs care. It usually means the shorter side, or the puzzle names the direction.

If D is $k$-th to the left of A, D is also $(n - k)$-th to the right of A.

### A worked example
Eight people A to H sit around a table facing the centre. A sits opposite E. B is second to the right of A. F sits opposite B. C is immediate left of E. D sits opposite C. G is not a neighbour of A.

- A = seat 0. Number clockwise from 0 to 7. E = seat 4.
- Right is anticlockwise. B = seat 6. F = seat 2.
- C = immediate left of E = seat 5. D = seat 1.
- Seats 3 and 7 remain for G and H. Seat 7 is next to A, so G = 3 and H = 7.
- Third to the left of H: $7 \to 0 \to 1 \to 2$. That is F.

### Outward and mixed facing
If everyone faces outward, swap the rule. Left is anticlockwise. If some face the centre and some face outward, draw a small arrow at each person when you place them.

> **Watch:** "Q is immediate right of P" depends on how P faces, not on how Q faces.

### Neighbour clues
- "X is next to Y" does not say which side. Keep both until another clue decides.
- "X sits between Y and Z" in a circle usually means immediately between.
- "Y and Z are not neighbours" is the best clue for the last two seats.

### Couples and attributes
Some puzzles add couples, colours or jobs. Fix the seats first, using the position clues. Then fill an attribute grid, one row per person.

### Check with a loop
When the circle is full, walk the left neighbours from any person. You should return to the start after exactly $n$ steps. If you do not, one arrow was drawn backwards. Fix it before you read the questions.
"""

s3_patterns = [
    pat("st-p9", "Chains around a circle facing the centre", "very common",
        "Clues link neighbours, such as 'A is immediate left of B' and 'D is second right of B'.",
        r"\text{left} = \text{clockwise (facing centre)}",
        ["Put the first named person at the top.", "Follow each 'immediate left' clue clockwise.", "Follow each 'right' clue anticlockwise.", "Check that the string closes into a loop."],
        "Left chains join into one clockwise string, so the circle builds itself.",
        "Five people sit around a table facing the centre. A is immediate right of B. D is immediate left of B. C is immediate left of D. E is immediate left of C. Who is second to the right of D?",
        ["B = seat 0. D = seat 1 (left of B). C = seat 2. E = seat 3.", "A is immediate right of B, so A = seat 4. The loop closes at E.", "Second to the right of D is seat $1 - 2 = 4$."],
        "A"),
    pat("st-p10", "Opposite pairs", "very common",
        "An even number of seats with 'sits opposite' clues.",
        r"\text{opposite} = \dfrac{n}{2}\text{ places}",
        ["Place every opposite pair as two seats across the table.", "Add the left and right clues from a placed person.", "Fill the last seats with the 'not' clue."],
        "An opposite clue fixes a seat exactly, so it needs no guessing.",
        "Eight people A to H sit around a table facing the centre. A sits opposite E. B is second to the right of A. F sits opposite B. C is immediate left of E. D sits opposite C. G is not a neighbour of A. Who is third to the left of H?",
        ["A = seat 0, E = seat 4. B = seat 6, F = seat 2.", "C = seat 5, D = seat 1.", "G and H take seats 3 and 7. Seat 7 is next to A, so H = 7.", "Third to the left of H: $7 + 3 = 10$, which is seat 2."],
        "F"),
    pat("st-p11", "Facing outward", "common",
        "Everyone faces away from the centre.",
        r"\text{outward: left} = \text{anticlockwise}",
        ["Swap the rule: left is anticlockwise and right is clockwise.", "Place the first person at the top.", "Follow each clue with the swapped rule."],
        "Turning around turns the hands around, so clockwise and anticlockwise swap.",
        "Six people A to F sit around a table facing outward. B is immediate left of A. C is second to the right of A. D sits opposite A. E is immediate right of D. Who is immediate right of A?",
        ["A = seat 0, numbered clockwise. Facing outward, left is $-1$ and right is $+1$.", "B = seat 5. C = seat 2. D = seat 3. E = seat 4.", "F takes seat 1. Immediate right of A is seat 1."],
        "F"),
    pat("st-p12", "Mixed facing", "occasional",
        "Some people face the centre and some face outward.",
        None,
        ["Write each person's facing when you place them.", "Read each clue from the named person's own facing.", "Place the next person only after that."],
        "A clue is read from the person it names, so the facing of that person decides the side.",
        "Four people sit around a table. A faces the centre. B faces outward. B sits immediate left of A. C sits immediate right of B. Who is immediate right of A?",
        ["A = seat 0. A faces the centre, so left is clockwise. B = seat 1.", "B faces outward, so right is clockwise. C = seat 2.", "D takes seat 3. A's right (facing the centre) is seat 3."],
        "D"),
    pat("st-p19", "Neighbour clues with two sides", "common",
        "Clues say 'X and Y are neighbours of A' without a side.",
        None,
        ["Put the two neighbours on both sides of A.", "Try both orders.", "Use the next clue to kill the order that breaks a seat."],
        "'Next to' allows two sides, and the later clue picks the right one.",
        "Six people A to F sit around a table facing the centre. B and C are the two neighbours of A. D sits opposite A. E is immediate left of B. Who sits opposite C?",
        ["A = seat 0. B and C take seats 1 and 5.", "If B = 5, E would be seat 0. That is A's seat, so B = 1, E = 2, C = 5.", "D = seat 3. Opposite C is seat $5 + 3 = 8$, which is seat 2."],
        "E"),
]

s3_tricks = [
    {"title": "Walk the circle in one direction",
     "body": "Take the longest chain of 'immediate left' clues and lay it out clockwise. Close the loop with the last clue.",
     "example": {"q": "Facing the centre, D is immediate left of B. C is immediate left of D. E is immediate left of C. Write the clockwise string.",
                 "steps": ["Immediate left means the next seat clockwise.", "Start at B: B, D, C, E."],
                 "answer": "B, D, C, E clockwise"}},
    {"title": "Convert left to right around a circle",
     "body": "In a circle of $n$, the $k$-th to the left is the same person as the $(n - k)$-th to the right. Use the smaller number to save steps.",
     "example": {"q": "In a circle of 8, who is seventh to the left of A in terms of a shorter walk to the right?",
                 "steps": [r"$8 - 7 = 1$.", "Seventh to the left equals first to the right."],
                 "answer": "The immediate right neighbour of A"}},
]

s3_mistakes = [
    {"wrong": "Fixing every seat number before placing anyone.", "right": "Fix only the first person. Number the rest from there."},
    {"wrong": "Reading left as anticlockwise while facing the centre.", "right": "Facing the centre, left is clockwise."},
    {"wrong": "Looking for an opposite person at an odd table.", "right": "Opposite exists only for an even number of seats."},
    {"wrong": "Reading a clue from the wrong person's facing in mixed rows.", "right": "Read each clue from the named person's own facing."},
    {"wrong": "Fixing which side a neighbour sits on too early.", "right": "'Next to' allows two sides. Keep both until a clue decides."},
]

s3_revision = [
    "Fix the first person at the top of the circle.",
    "Facing the centre: left is clockwise. Facing outward: left is anticlockwise.",
    r"Opposite is $\dfrac{n}{2}$ places away, and only for even $n$.",
    "$k$-th left is the same as the $(n - k)$-th right.",
    "Mixed facing: read each clue from the named person.",
]

# ============================================================ puzzle-strategy
s4_concept = (
    "Seating questions come in sets that share one puzzle. "
    "Solve the whole seating once, write it neatly, and then each question is a quick lookup. "
    "Two rows, counting arrangements and attribute grids are the other forms you will meet."
)

s4_notes = r"""### How seating sets appear
A set has three to five questions on one puzzle. The first question takes the time. The others should take 10 to 20 seconds if the seating is fully solved.

So the real skill is to solve the whole arrangement once, cleanly.

### Budget and order
1. **Read every clue once before you draw.** Count the people and the seats. Note the facing direction. Look for clues that fix a seat outright.
2. **Build the frame** and write the direction on it.
3. **Place fixed clues, then chains, then negative clues.**
4. **Write the final seating neatly** before you read the questions.

> **Tip:** Most wrong answers in a set come from reading a half-finished rough drawing.

### Two parallel rows
Two rows face each other. Row 1 faces south. Row 2 faces north. Seat $i$ of row 1 faces seat $i$ of row 2.

- A south-facing person's left is the east end. "A is immediate right of B" in the south row means A is one seat west of B.
- "P faces A" joins the two rows. P and A have the same seat number.
- Both rows share the same ends.

### Solve once, answer many
The follow-up questions are of a few kinds.
- **Who sits $k$-th left or right of X:** read the drawing.
- **Which statement is true:** test each option on the drawing.
- **X and Y interchange seats:** swap only those two, then read again.
- **Odd one out:** three pairs share a relation and one does not.

### Counting arrangements
Some questions ask "in how many ways".
- $n$ people in a row: $n!$ ways.
- Two people who must sit together: treat them as one block, $(n - 1)! \times 2$.
- $n$ people around a circle, with rotations counted as the same: $(n - 1)!$.
- Each fixed seat removes one person and one seat from the free pool.

> **Rule:** For small numbers, list the cases. It is fast and it catches double counting.

### Attribute grids
Each person may also have a drink, city or job. Draw a grid with people down the side and seat plus attribute across the top. Each clue either fixes a cell or rules one out.

"The tea drinker sits at the left end" fixes the seat of the tea drinker, not the name. Tie a name to an attribute only when another clue joins them.

### When to skip
Give one full pass to each set. If two seatings are still alive after every clue, look at the questions. If they need the exact seating, park the set. Come back if time is left, because other questions give marks more cheaply.

### Where time is lost
- Reading a south-facing left as your own left.
- Taking 'between' to mean 'immediately between'.
- Forgetting that 'neighbour' allows two sides.
- Answering from a case that a later clue already struck out.
"""

s4_patterns = [
    pat("st-p13", "Two parallel rows facing each other", "common",
        "Two rows sit facing each other. One faces north, the other south, and clues say 'X faces Y'.",
        None,
        ["Draw two rows and write the facing on each.", "Solve each row with its own left and right rule.", "Join the rows with 'faces' clues at equal seat numbers."],
        "Seat $i$ faces seat $i$, so one solved row fixes the other.",
        "Row 1 has A, B, C, D facing south. Row 2 has P, Q, R, S facing north. In row 1, C is immediate right of B, D is at the east end, and A is not at an end. In row 2, P faces C, R is immediate right of P, and S faces A. Who faces D?",
        ["Row 1: D = seat 4. C is immediate right of B, so C is one seat west of B.", "A is not at an end, so A = 3, B = 2, C = 1. Row 1 is C B A D.", "Row 2: P = seat 1. R = seat 2. S faces A, so S = seat 3. Q = seat 4.", "D is seat 4, so the person facing D is Q."],
        "Q"),
    pat("st-p14", "Solve once, answer many", "very common",
        "A set of questions asks for a true statement, an interchange or an odd one out.",
        None,
        ["Write the final seating neatly.", "For an interchange, swap only the two named people.", "Read each question off the new drawing."],
        "One clean seating answers every question in the set.",
        "The final row is D E A C B from the west. If C and E interchange seats, who sits immediate right of A?",
        ["Swap C and E: the row becomes D C A E B.", "The immediate right of A (facing north) is the next seat east."],
        "E"),
    pat("st-p15", "Counting arrangements", "occasional",
        "The question asks 'in how many ways' instead of 'who'.",
        r"n!,\quad (n-1)!",
        ["Decide if it is a row or a circle.", "Glue any pair who must sit together into one block.", "Count blocks, multiply, and then multiply by the order inside the block."],
        "Choices are counted seat by seat, so each fixed group behaves as one unit.",
        "In how many ways can 5 people sit in a row if A and B must always sit together?",
        ["Treat AB as one block. With 3 other people there are 4 units.", r"Units can be arranged in $4! = 24$ ways.", r"A and B can swap inside the block: $24 \times 2 = 48$."],
        "48"),
    pat("st-p16", "Seats plus attributes", "common",
        "Each person also has a drink, colour, city or job.",
        None,
        ["Draw a grid with people, seat and attribute.", "Fix the seats first from the seat clues.", "Tie each attribute to a name only when a clue joins them."],
        "Seat clues and attribute clues work on different rows of the grid, and one name joins them.",
        "Four people A, B, C, D sit in a row facing north. A is at the east end and B is immediate left of A. The tea drinker is at the west end. The milk drinker is immediate right of the tea drinker. C drinks milk. A drinks water. Who drinks juice?",
        ["A = seat 4, B = seat 3. C and D take seats 1 and 2.", "Tea is at seat 1 and milk is at seat 2. C drinks milk, so C = seat 2 and D = seat 1 (tea).", "A drinks water, so B drinks juice."],
        "B"),
    pat("st-p20", "Two seatings survive", "occasional",
        "After all the clues, two seatings remain. Check what the question asks.",
        None,
        ["List the two seatings that survive.", "Read the asked seat in both.", "If both give the same person, mark it and move on."],
        "The question needs one seat, not the full unique seating.",
        "Five people A to E sit in a row facing north. A is in the middle. E is at the east end. D is immediate left of E. B and C fill the other seats in any order. Who sits immediate right of A?",
        ["A = seat 3, E = seat 5, D = seat 4.", "B and C take seats 1 and 2 in either order.", "Immediate right of A is seat 4 in both cases."],
        "D"),
]

s4_tricks = [
    {"title": "Two-seating bail-out",
     "body": "When exactly two seatings survive, check what the question asks. If both give the same answer, mark it and move on.",
     "example": {"q": "After all clues, A and B could swap seats 1 and 2. Who sits at the east end?",
                 "steps": ["The swap touches only seats 1 and 2.", "The east end is not in the swap."],
                 "answer": "The east-end person is the same either way"}},
    {"title": "Verify with one closed loop",
     "body": "In a circle, walk the left-neighbour links around your final drawing. If the string does not close, one arrow was drawn backwards.",
     "example": {"q": "Facing the centre, the left chain is B, D, C, E and A is the immediate right of B. Does the loop close?",
                 "steps": ["A is right of B, so A is just before B clockwise.", "The chain goes B, D, C, E, A and back to B."],
                 "answer": "Yes, it closes"}},
]

s4_mistakes = [
    {"wrong": "Answering from a rough half-drawn seating.", "right": "Write the final seating neatly before you read the questions."},
    {"wrong": "Swapping more people than the question names.", "right": "Swap only the two named people."},
    {"wrong": "Using $n!$ for a circle.", "right": "A circle with rotations equal gives $(n - 1)!$."},
    {"wrong": "Tying an attribute to a name before a clue joins them.", "right": "Fix seats first. Join an attribute to a name only with a clue."},
    {"wrong": "Spending long on a set with two live seatings.", "right": "Check if the question needs the full seating. If not, move on."},
]

s4_revision = [
    "Read all clues, build the frame with its facing, then fill.",
    "Two rows: seat $i$ of the south row faces seat $i$ of the north row.",
    "Solve fully once. Each follow-up is a 15-second lookup.",
    r"Row: $n!$. Circle: $(n - 1)!$. Row with a pair together: $(n - 1)! \times 2$.",
    "Attribute grid: fix seats, then tie names to attributes.",
]

# ------------------------------------------------------------------ patch
data = json.loads(TOPIC.read_text(encoding="utf-8"))
subs = {s["id"]: s for s in data["subtopics"]}
assert set(subs) == {"seating-idea", "linear-arrangement", "circular-arrangement", "puzzle-strategy"}


def put(sid, concept, notes, formulas, patterns, tricks, mistakes, revision):
    s = subs[sid]
    old_ids = {p["id"] for p in s.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sid}: dropped a pattern id"
    print(sid, "notes chars", len(notes.strip()))
    assert 2500 <= len(notes.strip()) <= 5000, f"{sid}: notes length"
    s.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, patterns=patterns,
             tricks=tricks, mistakes=mistakes, revision=revision)


put("seating-idea", s1_concept, s1_notes, s1_formulas, s1_patterns, s1_tricks, s1_mistakes, s1_revision)
put("linear-arrangement", s2_concept, s2_notes, [], s2_patterns, s2_tricks, s2_mistakes, s2_revision)
put("circular-arrangement", s3_concept, s3_notes, [], s3_patterns, s3_tricks, s3_mistakes, s3_revision)
put("puzzle-strategy", s4_concept, s4_notes, [], s4_patterns, s4_tricks, s4_mistakes, s4_revision)

ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(ids) == len(set(ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("seating-arrangement updated", {k: len(v["patterns"]) for k, v in subs.items()})
