"""Readable rewrite of Direction & Distance (direction-distance).

Phase 3: plain English, one idea per section, grid method throughout.
Every example is re-walked by a tiny simulator below and asserted against the written answer.
Run: python direction_distance.py  (patches content/core/topics/reasoning/direction-distance.json)
"""
import json
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "direction-distance.json"

# ---------------------------------------------------------------- simulator
DIR = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
CW = "NESW"


def turn(h, q):
    """Turn q quarter-turns clockwise (negative = anticlockwise)."""
    return CW[(CW.index(h) + q) % 4]


def walk(h, moves, pos=(0, 0)):
    """moves: (cmd, km). cmd = N/E/S/W (walk that way), F (straight on), L/R (turn then walk), B (about turn then walk).
    Returns (position, final heading)."""
    x, y = pos
    for c, d in moves:
        if c in DIR:
            h = c
        elif c == "L":
            h = turn(h, -1)
        elif c == "R":
            h = turn(h, 1)
        elif c == "B":
            h = turn(h, 2)
        else:
            assert c == "F"
        x, y = x + DIR[h][0] * d, y + DIR[h][1] * d
    return (x, y), h


def dist(p, q=(0, 0)):
    s = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    r = isqrt(s)
    assert r * r == s, f"not a whole distance: sqrt({s})"
    return r


def word(p, q=(0, 0)):
    """Compass word of point p as seen from q."""
    dx, dy = p[0] - q[0], p[1] - q[1]
    ns = "North" if dy > 0 else "South" if dy < 0 else ""
    ew = "East" if dx > 0 else "West" if dx < 0 else ""
    return (ns + "-" + ew) if ns and ew else (ns or ew or "same place")


LEFT_OF = {"N": "W", "S": "E", "E": "N", "W": "S"}       # what lies on your left when you face the key
RIGHT_OF = {"N": "E", "S": "W", "E": "S", "W": "N"}
assert all(LEFT_OF[h] == turn(h, -1) and RIGHT_OF[h] == turn(h, 1) for h in CW)

# ---------------------------------------------------------------- checks: subtopic 1 (notes + patterns)
p, h = walk("N", [("N", 5), ("L", 3)])                     # notes: facing North, left = West
assert p == (-3, 5) and h == "W"
assert walk("S", [("S", 5), ("L", 3)])[1] == "E"           # facing South, left = East
p, _ = walk("N", [("E", 8), ("W", 6), ("E", 3)]);  assert p == (5, 0)                  # notes tally
p, _ = walk("N", [("N", 15), ("E", 9), ("S", 15)]);  assert p == (9, 0)                # notes cancel
p, _ = walk("N", [("E", 3), ("N", 4)]);  assert dist(p) == 5                           # notes triple
p, _ = walk("N", [("E", 5), ("N", 12)]); assert dist(p) == 13
p, _ = walk("N", [("E", 8), ("N", 15)]); assert dist(p) == 17
p, _ = walk("N", [("E", 7), ("N", 24)]); assert dist(p) == 25
assert (6, 8) == (2 * 3, 2 * 4) and dist((6, 8)) == 10 and dist((9, 12)) == 15
# diagonal: k*sqrt2 along NE gives k N and k E (k*sqrt2 squared = 2k^2 = k^2 + k^2)
for k in (5, 6, 8):
    assert 2 * k * k == k * k + k * k
# di-p1
p, _ = walk("N", [("E", 9), ("N", 12)]); assert dist(p) == 15
# di-p2: 15 W, 6 N, 15 E, 2 N
p, _ = walk("N", [("W", 15), ("N", 6), ("E", 15), ("N", 2)]); assert p == (0, 8) and dist(p) == 8
# di-p3: 8*sqrt2 NE -> (8, 8); then 2 W -> (6, 8)
p = (8, 8); p, _ = walk("N", [("W", 2)], pos=p); assert p == (6, 8) and dist(p) == 10
# NE 5*sqrt2 then NW 5*sqrt2 (notes)
assert (5, 5)[1] + (-5, 5)[1] == 10 and 5 + (-5) == 0
# di-p4 / di-p6
p, _ = walk("N", [("E", 9), ("N", 12)]); assert 9 + 12 == 21 and 21 - dist(p) == 6
# di-p5: 8 N, right (E) 6
p, h = walk("N", [("N", 8), ("R", 6)]); assert p == (6, 8) and h == "E" and dist(p) == 10
# trick 1: 20 m ... (12 E, 9 S)
p, _ = walk("N", [("E", 12), ("S", 9)]); assert dist(p) == 15
# trick 2: 24 N, 7 E
p, _ = walk("N", [("N", 24), ("E", 7)]); assert dist(p) == 25

# ---------------------------------------------------------------- checks: subtopic 2
assert turn("N", 1) == "E" and turn("E", 1) == "S" and turn("S", 1) == "W" and turn("W", 1) == "N"
assert [turn("N", -k) for k in (1, 2, 3, 4)] == ["W", "S", "E", "N"]
assert turn("W", -1 + 3) == "E"                                              # old example: kept
assert turn("S", 1 + 2 - 1) == "N"                                           # fd-p1 (right, about turn, left)
assert turn("E", 3) == "N" and turn("E", -1) == "N"                          # 270 clockwise = 90 anticlockwise
p, _ = walk("N", [("N", 6), ("E", 2), ("S", 9), ("E", 2)])                   # fd-p2
assert p == (4, -3) and word(p) == "South-East"
assert word((3, 4)) == "North-East" and word((-3, 4)) == "North-West"
assert word((3, -4)) == "South-East" and word((-3, -4)) == "South-West"
assert word((0, 4)) == "North" and word((-3, 0)) == "West"
assert word((0, 0), (3, 4)) == "South-West"                                  # reverse pair flips
p, h = walk("E", [("F", 5), ("R", 4), ("R", 3)])                             # fd-p3: E, right S, right W
assert h == "W"
p, h = walk("N", [("N", 8), ("B", 4), ("L", 3)])                             # fd-p4
assert p == (3, 4) and h == "E" and dist(p) == 5 and word(p) == "North-East"
p, h = walk("W", [("F", 4), ("R", 3), ("R", 4)])                             # fd-p5
assert p == (0, 3) and h == "E" and dist(p) == 3 and word(p) == "North"
p, h = walk("N", [("N", 5), ("B", 5)]); assert p == (0, 0)                   # notes: back the same distance
p, h = walk("E", [("F", 6), ("B", 2)]); assert p == (4, 0) and h == "W"      # notes: 6 E then back 2
# notes: facing North, turns right, walks 4, turns left, walks 3 -> (4, 3)
p, h = walk("N", [("R", 4), ("L", 3)]); assert p == (4, 3) and h == "N" and word(p) == "North-East"
# trick: facing East, left, left -> West
assert walk("E", [("L", 0), ("L", 0)])[1] == "W"

# ---------------------------------------------------------------- checks: subtopic 3 (shadows)
SUN = {"morning": "E", "evening": "W"}
SHADOW = {k: turn(v, 2) for k, v in SUN.items()}
assert SHADOW == {"morning": "W", "evening": "E"}


def facing(time, side):
    """Facing of a person whose shadow falls on `side` (front/back/left/right)."""
    s = SHADOW[time]
    if side == "front":
        return s
    if side == "back":
        return turn(s, 2)
    for f in CW:                                                            # find the facing that puts s on that side
        if (side == "left" and LEFT_OF[f] == s) or (side == "right" and RIGHT_OF[f] == s):
            return f


assert facing("morning", "front") == "W" and facing("morning", "back") == "E"
assert facing("morning", "left") == "N" and facing("morning", "right") == "S"
assert facing("evening", "front") == "E" and facing("evening", "back") == "W"
assert facing("evening", "left") == "S" and facing("evening", "right") == "N"
# sd-p1: morning, behind him -> East
assert facing("morning", "back") == "E"
# sd-p2: evening, in front of her -> East
assert facing("evening", "front") == "E"
# sd-p3: evening, shadow on her left -> South
assert facing("evening", "left") == "S"
# sd-p4: evening, walks away from shadow (faces West), turns 90 anticlockwise -> South
assert turn(turn(SHADOW["evening"], 2), -1) == "S"
# sd-p5: evening, A's shadow on his left -> A faces S, B back to back faces N; B's shadow (East) is on his right
a = facing("evening", "left"); b = turn(a, 2)
assert a == "S" and b == "N" and RIGHT_OF[b] == SHADOW["evening"]
# notes examples
assert facing("morning", "right") == "S" and LEFT_OF["S"] == "E" and RIGHT_OF["S"] == "W"
assert turn(facing("morning", "front"), 1) == "N"                            # old sd-p4 kept in trick
# trick: morning, shadow falls to his left, facing N; walks toward the shadow (W) and turns right -> N
assert facing("morning", "left") == "N"
assert turn(SHADOW["morning"], 1) == "N"

# ---------------------------------------------------------------- checks: subtopic 4 (relative position)
# notes: C is 5 E of A, A is 2 N of B -> C from B is North-East
B = (0, 0); A = (0, 2); C = (5, 2)
assert word(C, B) == "North-East" and word(B, C) == "South-West"
# rp-p1: Ravi 8 N, Sam 15 E
assert dist((0, 8), (15, 0)) == 17
# rp-p2: Meera 6 E and 10 S; Nisha 2 W and 7 S
meera, _ = walk("N", [("E", 6), ("S", 10)]); nisha, _ = walk("N", [("W", 2), ("S", 7)])
assert meera == (6, -10) and nisha == (-2, -7) and word(nisha, meera) == "North-West"
assert (nisha[0] - meera[0], nisha[1] - meera[1]) == (-8, 3)
# rp-p3: 9 E vs 9 W then both 20 N
a1, _ = walk("N", [("E", 9), ("N", 20)]); b1, _ = walk("N", [("W", 9), ("N", 20)])
assert dist(a1, b1) == 18
# rp-p4: P is 9 W of Q; Q is 12 S of R -> P from R
R_ = (0, 0); Q = (0, -12); P = (-9, -12)
assert dist(P, R_) == 15 and word(P, R_) == "South-West" and word(R_, P) == "North-East"
# rp-p5: 6 km/h North and 8 km/h East for 2 hours -> 12 N, 16 E -> 20
assert dist((0, 6 * 2), (8 * 2, 0)) == 20
# rp-p6 (kept old id space): opposite directions add, same direction subtracts: 45 km/h & 35 km/h, 3 hours
assert 3 * 45 + 3 * 35 == 240 and 3 * 45 - 3 * 35 == 30
# notes chain: A 5 E of B, B 12 N of C -> 13
assert dist((5, 12)) == 13
# trick: A is 5 N of B, C 5 E of A -> C from B is NE
assert word((5, 10), (0, 5 - 5)) == "North-East"
# notes: walk each person: P (3, 4) Q (-4, -3) gives 7*sqrt2 (kept out: not whole)
# old rp-p2 example
assert word((-6, 8), (6, -8)) == "North-West"

# ---------------------------------------------------------------- content helpers
def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


dfrac = lambda x: x.replace(r"\frac", r"\dfrac")

# ============================================================ subtopic 1: direction-idea
s1_concept = (
    "A direction question is a walk on a plain map. Put North at the top and East on the right. "
    "Turn every sentence into one small move, then find the straight line from start to finish. "
    "That line is the shortest distance, and it is not the same as the distance the person walked."
)

s1_notes = r"""### The four directions
Draw a map with **North at the top** and **East on the right**. South is at the bottom. West is on the left.

Between them sit four mixed directions: North-East, North-West, South-East and South-West. "Towards the sunrise" means East. "Towards the sunset" means West.

> **Rule:** Draw the map once, with North up. Never turn the page when the walker turns.

### Left and right belong to the walker
A left turn does not mean "West". It means "to the left of the way he faces now".

| The walker faces | Left is | Right is |
|---|---|---|
| North | West | East |
| South | East | West |
| East | North | South |
| West | South | North |

A man walks North and turns left. He now walks West. The same left turn from South would send him East.

> **Watch:** "Left = West" is true only when the walker faces North. Check the table for every turn.

### Turn each sentence into a move
Start at the middle of the map. Each sentence moves you. Keep a running tally on two lines: East-West and North-South.

- East and North count as plus.
- West and South count as minus.

Example: "8 km East, 6 km West, then 3 km East." The East-West line is $8 - 6 + 3 = 5$. He is 5 km East of the start.

### Cancel opposite legs first
A leg is one straight part of the walk. Two legs that go opposite ways on the same line cancel each other.

A man walks 15 km North, 9 km East, then 15 km South. The 15 North and 15 South cancel. Only 9 km East is left.

> **Tip:** Cancel first, then calculate. Most questions hide two or three cancellations.

### Shortest distance
The shortest distance is the straight line from start to finish. After cancelling, you have a net East move and a net North move. They are the two short sides of a right triangle.

$$d = \sqrt{(\text{net East})^2 + (\text{net North})^2}$$

Example: 3 km East and 4 km North gives $\sqrt{9 + 16} = 5$ km.

Most exam answers come from these number triples:

| Short sides | Straight line |
|---|---|
| 3 and 4 | 5 |
| 5 and 12 | 13 |
| 8 and 15 | 17 |
| 7 and 24 | 25 |

Doubles and triples also work: 6 and 8 give 10, and 9 and 12 give 15.

### Diagonal legs
A leg such as "5$\sqrt{2}$ km North-East" is a slanting step. It moves 5 km North and 5 km East at the same time.

- North-East: $k$ North and $k$ East.
- North-West: $k$ North and $k$ West.
- South-East: $k$ South and $k$ East.
- South-West: $k$ South and $k$ West.

Example: 5$\sqrt{2}$ km North-East, then 5$\sqrt{2}$ km North-West. The East and West parts cancel. The North parts add up to 10 km.

### Distance walked or shortest distance
Read the last line twice. Each phrase asks for a different number.

| The question asks | Find |
|---|---|
| How far is he from the start? | Straight line (Pythagoras) |
| How much distance did he walk? | Add all the legs |
| How much shorter is the direct path? | Total walked minus straight line |
| In which direction is he from the start? | Compass word of the net moves |

> **Watch:** The walked distance and the straight line are always two different options. Do not pick the wrong one.
"""

s1_formulas = [
    {"name": "Shortest distance", "tex": r"d = \sqrt{x^2 + y^2}", "note": "x = net East-West move, y = net North-South move, after cancelling."},
    {"name": "Number triples", "tex": r"3\text{-}4\text{-}5,\ 5\text{-}12\text{-}13,\ 8\text{-}15\text{-}17,\ 7\text{-}24\text{-}25", "note": "Doubles and triples of these also work: 6-8-10, 9-12-15."},
    {"name": "Diagonal leg", "tex": r"k\sqrt{2}\ \text{along NE} = k\ \text{North} + k\ \text{East}", "note": "The same rule holds for NW, SE and SW."},
]

s1_patterns = [
    pat("di-p1", "Straight line after two perpendicular legs", "very common",
        "The legs run North-South and East-West. The question asks how far he is from the starting point.",
        r"d = \sqrt{(\text{net East})^2 + (\text{net North})^2}",
        ["Write each leg as an East-West move or a North-South move.", "Cancel opposite legs and find the net East and net North.",
         "Look for a number triple (3-4-5, 5-12-13, 8-15-17).", "Otherwise apply the square root formula."],
        "The two net moves are the short sides of a right triangle. The straight line home is its longest side.",
        "A man walks 9 km East and then 12 km North. How far is he from the starting point?",
        ["Net moves: 9 km East and 12 km North.", "9 and 12 are 3 times 3 and 3 times 4.", r"Distance = $3 \times 5 = 15$ km."],
        "15 km"),
    pat("di-p2", "Legs that cancel out", "common",
        "The path doubles back. A leg North is followed by a leg South, or East by West.",
        None,
        ["Pair each leg with the leg that goes the opposite way.", "Cancel the pairs. Subtract the smaller from the larger.",
         "Use only what is left to find the distance."],
        "Only the start and the end matter. Retraced legs add nothing to the gap.",
        "A cyclist rides 15 km West, 6 km North, 15 km East and then 2 km North. How far is he from the starting point?",
        ["15 km West and 15 km East cancel.", r"North legs add up: $6 + 2 = 8$ km.", "Only 8 km North is left."],
        "8 km"),
    pat("di-p3", "Diagonal legs written with root 2", "common",
        "A leg is written as $k\\sqrt{2}$ km towards North-East, North-West, South-East or South-West.",
        r"k\sqrt{2}\ \text{diagonal} = k\ \text{on each of two sides}",
        ["Split each diagonal leg into two equal parts of $k$.", "Add up the East-West parts and the North-South parts.",
         "Find the straight line from the net moves."],
        "A diagonal step of $k\\sqrt{2}$ is the slanting side of a right triangle with two sides of $k$.",
        r"A man walks $8\sqrt{2}$ km North-East and then 2 km West. How far is he from the starting point?",
        ["North-East leg: 8 km East and 8 km North.", r"Then 2 km West: East part is $8 - 2 = 6$ km.", r"Net moves 6 and 8, so the distance is 10 km."],
        "10 km"),
    pat("di-p4", "Total distance walked", "common",
        "The question says \"how much distance did he cover or walk\" for a path that ends away from the start.",
        None,
        ["Ignore all directions.", "Add the length of every leg.", "Do not use Pythagoras."],
        "Distance walked counts every step. The straight line counts only the gap between start and end.",
        "A man walks 9 km East and then 12 km North. What total distance does he cover?",
        ["Add the two legs.", r"$9 + 12 = 21$ km."],
        "21 km"),
    pat("di-p5", "Left and right turns, then the gap", "very common",
        "The walker turns left or right in the middle of the walk. The straight-line distance is asked.",
        None,
        ["Note the way he faces at the start.", "After each turn, use the left-right table to find the new direction.",
         "Turn each leg into a North, South, East or West move.", "Find the net moves and the straight line."],
        "The map never turns, so each new direction must be found one turn at a time.",
        "Sanjay walks 8 km North. He turns right and walks 6 km. How far is he from the start?",
        ["Facing North, right is East.", "Moves: 8 km North and 6 km East.", "6 and 8 give the triple 6-8-10."],
        "10 km"),
    pat("di-p6", "How much shorter is the straight path", "occasional",
        "The question asks how much distance would be saved by walking straight instead.",
        r"\text{saved} = \text{total walked} - \text{straight line}",
        ["Add all the legs to get the total walked.", "Find the straight line by Pythagoras.", "Subtract the straight line from the total."],
        "The saving is the gap between the two numbers you already know how to find.",
        "A man walks 9 km East and then 12 km North. How much shorter is the direct path from start to finish?",
        ["Total walked: 9 + 12 = 21 km.", "Straight line: 15 km.", r"Saved: $21 - 15 = 6$ km."],
        "6 km"),
]

s1_tricks = [
    {"title": "Two-line tally",
     "body": "Keep one running total for East-West and one for North-South. Write West and South as minus. The two totals are the whole answer, with no drawing needed.",
     "example": {"q": "A man walks 8 km East, 6 km West and then 3 km East. How far is he from the start, and in which direction?",
                 "steps": [r"East-West: $8 - 6 + 3 = 5$.", "North-South: 0."],
                 "answer": "5 km, East"}},
    {"title": "Spot the triple",
     "body": "If the two net moves are 3 and 4, or 5 and 12, or 8 and 15, or 7 and 24 (or their multiples), the answer is the third number. No square root is needed.",
     "example": {"q": "A woman walks 24 km North and then 7 km East. How far is she from the start?",
                 "steps": ["24 and 7 are the short sides of the 7-24-25 triple."],
                 "answer": "25 km"}},
]

s1_mistakes = [
    {"wrong": "Adding all the legs when the question asks how far he is from the start.", "right": "Cancel the legs, then use the straight-line formula. Add all the legs only for 'distance walked'."},
    {"wrong": "Treating 'left' as West every time.", "right": "Find which way he faces first. Facing South, left is East."},
    {"wrong": "Turning the page when the walker turns.", "right": "Keep North at the top all the time. Only the walker turns."},
    {"wrong": r"Splitting a $k\sqrt{2}$ diagonal leg into $k\sqrt{2}$ on each side.", "right": r"A $k\sqrt{2}$ diagonal leg is $k$ on each side."},
    {"wrong": "Forgetting to cancel opposite legs.", "right": "Pair North with South and East with West before any square root."},
]

s1_revision = [
    "North is up and East is right. The page never turns.",
    "Left and right depend on the way the walker faces.",
    "Tally East-West and North-South. West and South are minus.",
    "Cancel opposite legs before any calculation.",
    r"Straight line: $\sqrt{(\text{East})^2 + (\text{North})^2}$.",
    "Learn the triples: 3-4-5, 5-12-13, 8-15-17, 7-24-25.",
    r"A diagonal leg of $k\sqrt{2}$ is $k$ on each of its two sides.",
]

# ============================================================ subtopic 2: final-direction
s2_concept = (
    "Two kinds of question live here. One asks which way a person faces after some turns. "
    "The other asks in which direction the end point lies from the start. "
    "Write the direction after every turn, and never trust your memory over three turns."
)

s2_notes = r"""### Which way is he facing now
Only the turns matter here. The distances are decoration.

A right turn of 90 degrees moves you one step **clockwise** on this circle: North, East, South, West, and back to North. A left turn moves one step the other way.

| Start facing | After a right turn | After a left turn |
|---|---|---|
| North | East | West |
| East | South | North |
| South | West | East |
| West | North | South |

> **Rule:** Right is one step clockwise. Left is one step back. An about-turn (180 degrees) is two steps.

### Count the quarter-turns
One quarter-turn is 90 degrees. Count rights as plus and lefts as minus. Add them.

Example: facing West, a man turns 90 degrees anticlockwise, then 270 degrees clockwise. That is $-1 + 3 = +2$ quarter-turns. Two steps clockwise from West is **East**.

Four quarter-turns bring you back to where you started. So cross out 4 whenever it appears.

> **Tip:** 270 degrees clockwise is the same as 90 degrees anticlockwise. Both end in the same place.

### Which direction is the end point
Now the path matters and the facing does not. Find the net East move and the net North move. Then read the compass from their signs.

| East move | North move | Direction |
|---|---|---|
| plus | plus | North-East |
| minus | plus | North-West |
| plus | minus | South-East |
| minus | minus | South-West |

If one move is zero, use one word only. A net move of 4 km North and 0 East is simply **North**.

"Direction of B from A" means: stand at A, look at B. Swap the two people and the answer flips. North-East becomes South-West.

### Turns in the middle of a walk
"Walks 5 km, turns left, walks 3 km." The word "left" depends on the way he walks now. So track the direction leg by leg.

Example: a man walks North, turns right and walks 4 km, then turns left and walks 3 km. Right of North is East. Left of East is North. He moves 4 km East and 3 km North. He ends **North-East** of the start.

### Turning back
"Turns back", "returns" and "about-turn" all mean 180 degrees. He now faces the opposite way.

A man walks 6 km East, then turns back and walks 2 km. He faces West. He is $6 - 2 = 4$ km East of the start.

> **Watch:** The end direction and the facing direction are two different answers. Read which one the question wants.

### Questions that ask both
A hard question gives turns and then asks the direction of the end point. Keep two lists.

1. List one: the direction he faces after each turn.
2. List two: the net East and North moves.

Do not read one list from the other. A quick picture check helps. If he ended North and East of the start, he cannot be South-West.
"""

s2_formulas = [
    {"name": "Clockwise cycle", "tex": r"N \to E \to S \to W \to N", "note": "Every right turn moves one step along this circle."},
    {"name": "Anticlockwise cycle", "tex": r"N \to W \to S \to E \to N", "note": "Every left turn moves one step along this circle."},
    {"name": "Reading the end point", "tex": r"(x>0,\ y>0) \Rightarrow \text{North-East}", "note": "x is the net East move and y is the net North move. Their signs give the compass word."},
]

s2_patterns = [
    pat("fd-p1", "Net quarter-turns for the final facing", "very common",
        "A starting direction and a list of turns are given. The question asks which way he faces now.",
        None,
        ["Count a right turn as +1, a left turn as -1 and an about-turn as 2.", "Add them up and drop any 4.", "Move that many steps clockwise from the start."],
        "Each turn is a quarter of a full circle, and four quarters bring you home.",
        "A man faces South. He turns 90 degrees clockwise, then 180 degrees, then 90 degrees anticlockwise. Which way does he face now?",
        ["Turns: +1, +2, -1.", "Total: +2.", "Two steps clockwise from South: West, then North."],
        "North"),
    pat("fd-p2", "Direction of the end point from the start", "very common",
        "A path is given. The question asks in which direction the finish is from the starting point.",
        None,
        ["Find the net East-West move and the net North-South move.", "Look at the sign of each.", "Join the two words. Use one word if a move is zero."],
        "The direction of the end point is the compass word of the net move.",
        "Priya walks 6 km North, 2 km East, 9 km South and then 2 km East. In which direction is she from the starting point?",
        ["East-West: 2 + 2 = 4 km East.", "North-South: 6 - 9 = 3 km South.", "East and South make South-East."],
        "South-East"),
    pat("fd-p3", "Left and right turns in the middle", "common",
        "The path has turns such as \"turns left\" or \"turns right\", and the final direction is asked.",
        None,
        ["Write the direction he faces at the start.", "After each turn, write the new direction. Overwrite the old letter.", "The last letter is the final direction."],
        "The words left and right change meaning with every turn, so only a written chain is safe.",
        "Walking East, Arun turns right, walks 4 km, and then turns right again. Which way does he face now?",
        ["Start: East.", "Right turn: South.", "Right turn again: West."],
        "West"),
    pat("fd-p4", "Turning back and returning", "common",
        "The path says \"turns back\", \"returns\" or \"retraces\" in the middle.",
        None,
        ["An about-turn makes him face the opposite direction.", "A new leg after it cancels part of the old one.", "Finish the rest of the path and find the net moves."],
        "Turning back sends him along the same line the other way, so the new leg reduces the gap.",
        "A man walks 8 km North, turns back and walks 4 km, and then turns left and walks 3 km. How far and in which direction is he from the start?",
        ["Turning back: he faces South and walks 4 km. North-South: 8 - 4 = 4 km North.", "Left of South is East. He walks 3 km East.", "Net moves 3 East and 4 North give 5 km, towards North-East."],
        "5 km, North-East"),
    pat("fd-p5", "Facing and end point together", "occasional",
        "A path with several turns is given. It asks for the distance and direction from the start.",
        None,
        ["Track the facing after each turn in list one.", "Turn each leg into a North, South, East or West move.", "Find the net moves, then the distance and the compass word."],
        "The turns give the direction of each leg. The legs then give the net move.",
        "Deepa faces West and walks 4 km. She turns right and walks 3 km, and then turns right again and walks 4 km. How far and in which direction is she from the start?",
        ["West 4 km, then right turn: North 3 km, then right turn: East 4 km.", "East-West: 4 West and 4 East cancel.", "Only 3 km North is left."],
        "3 km, North"),
]

s2_tricks = [
    {"title": "Write the direction after every turn",
     "body": "After each turn, write one letter: N, E, S or W. Overwrite the old letter. Three written letters are safer than one long chain in your head.",
     "example": {"q": "Facing West, a man turns 90 degrees clockwise and then 180 degrees anticlockwise. Which way does he face?",
                 "steps": ["West, then 90 clockwise: North.", "180 either way: South."],
                 "answer": "South"}},
    {"title": "Reverse the pair, flip the word",
     "body": "If B is North-East of A, then A is South-West of B. The mixed words flip together.",
     "example": {"q": "B is 3 km East and 4 km North of A. In which direction is A from B?",
                 "steps": ["B from A is North-East.", "Reverse the pair: A from B is South-West."],
                 "answer": "South-West"}},
]

s2_mistakes = [
    {"wrong": "Using 'left = West' without checking which way he faces.", "right": "Check the table of turns. Left of South is East."},
    {"wrong": "Counting an about-turn as one quarter-turn.", "right": "An about-turn is two quarter-turns, 180 degrees."},
    {"wrong": "Giving the facing when the question asks the direction from the start.", "right": "Underline the last line. 'Facing' and 'direction from the start' are different answers."},
    {"wrong": "Reading the end direction from the distances instead of the net moves.", "right": "Use the signs of the net East and North moves."},
    {"wrong": "Forgetting to flip the answer when the pair is reversed.", "right": "North-East becomes South-West when the two people swap places."},
]

s2_revision = [
    "Right turn: one step clockwise on N, E, S, W. Left turn: one step back.",
    "An about-turn is two steps. Four quarter-turns are a full circle.",
    "Net quarter-turns = rights minus lefts.",
    "Direction of the end point: signs of the net East and North moves.",
    "'B from A' means stand at A and look at B. Reversing the pair flips the word.",
    "Track the facing leg by leg when turns come in the middle.",
    "Facing and end direction are two different answers.",
]

# ============================================================ subtopic 3: shadow-direction
s3_concept = (
    "The sun fixes the direction of every shadow. In the morning the sun is in the East, so shadows point West. "
    "In the evening the sun is in the West, so shadows point East. "
    "Turn the shadow words into a sentence about which way the person faces, then finish the question."
)

s3_notes = r"""### The sun points the shadow
A shadow always falls away from the sun. So the sun does the pointing for you.

| Time | Sun is in the | Shadow points |
|---|---|---|
| Morning (sunrise) | East | West |
| Evening (sunset) | West | East |

At noon in India, the shadow points roughly North. Most questions avoid noon.

> **Rule:** Write "morning: shadow West" or "evening: shadow East" before you read anything else.

### Where the shadow falls on the body
A person faces some direction. The shadow can fall in front, behind, on the left or on the right.

- Shadow in front: he faces the same way as the shadow.
- Shadow behind: he faces the opposite way.
- Shadow on the left or right: he faces a direction at right angles to the shadow.

Example: morning, shadow falls in front of him. The shadow points West, so he faces **West**. If it falls behind him, he faces East.

### Left and right shadows
Use the body map. It tells you what lies on the left and right for each facing.

| He faces | Left is | Right is |
|---|---|---|
| North | West | East |
| South | East | West |
| East | North | South |
| West | South | North |

Example: morning, shadow falls on his right. The shadow points West. West is on his right when he faces South. So he faces **South**.

> **Tip:** For a morning shadow, left means facing North and right means facing South. For an evening shadow, left means South and right means North.

### Two people, back to back
Back to back means the two people face opposite ways. Find one person's facing from the shadow. The other faces the opposite way.

Example: evening, Rohit's shadow falls on his left. The shadow points East. So Rohit faces South. His partner stands back to back with him, so he faces **North**.

### Four pictures to learn
Most questions use only these four. Learn them by heart.

| Time | Shadow falls | He faces |
|---|---|---|
| Morning | in front | West |
| Morning | behind | East |
| Evening | in front | East |
| Evening | behind | West |

The left and right cases follow from the body map above.

### Shadow and then a movement
Some questions add a walk or a turn. Do it in three steps.

1. Turn the shadow into a compass direction for that time.
2. Turn "towards" or "away from the shadow" into a plain direction.
3. Finish with quarter-turns on the circle North, East, South, West.

Example: evening, a man walks away from his shadow. The shadow points East, so he walks West. He then turns 90 degrees anticlockwise and faces **South**.

> **Watch:** The shadow is not the direction he faces. Read which of the two the question asks for.
"""

s3_patterns = [
    pat("sd-p1", "Morning shadow", "very common",
        "The time is early morning or sunrise. The shadow is in front, behind, left or right of a person.",
        None,
        ["Write: morning, shadow West.", "Front means he faces West. Behind means he faces East.", "Left means he faces North. Right means he faces South."],
        "The shadow is a fixed compass arrow. The person turns to put it on the stated side.",
        "At sunrise, a man's shadow falls exactly behind him. Which way is he facing?",
        ["Morning: the shadow points West.", "The shadow is behind him, so he faces the opposite way.", "Opposite of West is East."],
        "East"),
    pat("sd-p2", "Evening shadow", "very common",
        "The time is evening or sunset. The shadow is in front, behind, left or right of a person.",
        None,
        ["Write: evening, shadow East.", "Front means he faces East. Behind means he faces West.", "Left means he faces South. Right means he faces North."],
        "It is the same rule as morning, with the shadow arrow turned around.",
        "One evening, Ramesh's shadow falls exactly in front of him. Which way is he facing?",
        ["Evening: the shadow points East.", "The shadow is in front, so he faces the same way."],
        "East"),
    pat("sd-p3", "Left or right shadow to facing", "common",
        "The shadow falls to the left or right of the person, and his facing is asked.",
        None,
        ["Write the shadow direction for that time.", "Look at the body map. Find the facing that puts that direction on the stated side.", "Check by holding out your hand."],
        "Only one of the four facings puts the shadow on the stated side.",
        "In the evening, Neha's shadow falls on her left. Which way is she facing?",
        ["Evening: the shadow points East.", "When she faces South, her left is East.", "So she faces South."],
        "South"),
    pat("sd-p4", "Shadow, then a walk or a turn", "common",
        "The person walks towards or away from the shadow, or turns by 90 or 180 degrees, and the final direction is asked.",
        None,
        ["Turn the shadow into a compass direction.", "Turn 'towards' or 'away' into a direction. Away means the opposite.", "Finish the turns with quarter-turns."],
        "After the first step, it is an ordinary final-facing question.",
        "In the evening, Kiran walks away from his shadow. He then turns 90 degrees anticlockwise. Which way does he face now?",
        ["Evening: the shadow points East.", "Away from it means he walks West.", "Anticlockwise from West is South."],
        "South"),
    pat("sd-p5", "Two people back to back", "occasional",
        "Two people stand back to back, and one shadow position is given. The other person's facing or shadow side is asked.",
        None,
        ["Find the first person's facing from his shadow.", "Back to back means the other person faces the opposite way.", "Use the body map to place the shadow for the second person."],
        "Back to back fixes the second person's facing at once.",
        "In the evening, Rohit and Mohit stand back to back. Rohit's shadow falls on his left. Which way does Mohit face?",
        ["Evening: the shadow points East. East is on Rohit's left when he faces South.", "Mohit faces the opposite way to Rohit.", "Opposite of South is North."],
        "North"),
]

s3_tricks = [
    {"title": "Change the shadow into a facing first",
     "body": "Before any other step, rewrite the sentence as a facing sentence. Morning and shadow behind him means he faces East. Evening and shadow in front means he faces East.",
     "example": {"q": "In the morning, a boy's shadow falls on his left. Which way does he face?",
                 "steps": ["Morning shadow points West.", "West is on his left when he faces North."],
                 "answer": "North"}},
]

s3_mistakes = [
    {"wrong": "Using the evening shadow direction in a morning question.", "right": "Write 'morning: shadow West' or 'evening: shadow East' first."},
    {"wrong": "Giving the shadow's direction when the question asks the person's facing.", "right": "The shadow and the facing are two different arrows. Answer the one asked."},
    {"wrong": "Forgetting that left and right change when the facing changes.", "right": "Use the body map for each facing."},
    {"wrong": "Treating back to back as facing the same way.", "right": "Back to back means the two people face opposite ways."},
    {"wrong": "Treating 'away from the shadow' as the shadow's direction.", "right": "Away from it means the opposite direction."},
]

s3_revision = [
    "Morning: sun East, shadow West. Evening: sun West, shadow East.",
    "Shadow in front: same direction. Shadow behind: opposite direction.",
    "Morning: shadow left means facing North. Shadow right means facing South.",
    "Evening: shadow left means facing South. Shadow right means facing North.",
    "Back to back: the two facings are opposite.",
    "Turn the shadow into a facing, then solve the rest as a normal direction question.",
]

# ============================================================ subtopic 4: relative-position
s4_concept = (
    "Some questions place two people, or a person and a fixed object, on the same map. "
    "Put the reference person at the middle of the map first. Then place everyone else, one sentence at a time. "
    "The distance and direction between any two people are then read straight off the picture."
)

s4_notes = r"""### Place the reference first
Two statements can link three people. "C is 5 km East of A. A is 2 km North of B. In which direction is C from B?"

The question asks about **B**. So put B at the middle of the map. Then hang the others on B.

1. B is at the middle.
2. A is 2 km North of B.
3. C is 5 km East of A, so C is 5 km East and 2 km North of B.

C is **North-East** of B.

> **Rule:** Put the person named after "from" at the middle of the map. Everyone else hangs off that person.

### Give every person a position
Put the common start at the middle of the map. Walk each person alone. Write each end point as (East, North).

Example: Amit ends at (3, 4). Sumit ends at (-4, -3). West and South are minus.

### Distance between two people
The gap between two people is the straight line between their two end points.

$$d = \sqrt{(\text{East gap})^2 + (\text{North gap})^2}$$

The East gap is the difference of their East numbers. The North gap is the difference of their North numbers.

Example: Ravi walks 8 km North. Sam walks 15 km East. Ravi is at (0, 8) and Sam is at (15, 0). The gaps are 15 and 8, so the distance is 17 km.

### Direction of one person from another
"Direction of B from A" means: stand at A, look at B. Find the East gap and the North gap from A to B. Read the compass word from their signs.

> **Watch:** "A is East of B" and "B is East of A" give opposite pictures. Underline the person named after "of". That person is the reference.

Reverse the pair and the word flips. If C is North-East of B, then B is South-West of C.

### Shared legs cancel
Suppose both people walk the same leg, such as "then both walk 20 km North". That leg moves both of them by the same amount. It does not change the gap between them.

Example: one walks 9 km East and the other walks 9 km West. Then both walk 20 km North. The gap stays 18 km.

### Chains of positions
"P is 9 km West of Q. Q is 12 km South of R." Start at the last person, R, at the middle of the map. Q is 12 km South of R. P is 9 km West of Q. So P is 9 West and 12 South of R.

Distance from R to P: 9 and 12 give the triple, so 15 km. Direction of P from R: South-West.

### Speed and time
Two people who walk at different speeds move different distances. Distance = speed times time. Then place both on the map.

Example: one walks North at 6 km per hour and the other walks East at 8 km per hour for 2 hours. They are 12 km North and 16 km East. The gap is 20 km.

> **Tip:** Questions often ask "how far and in which direction". Find both. Options often pair the right distance with the wrong direction.
"""

s4_formulas = [
    {"name": "Distance between two points", "tex": r"d = \sqrt{(\Delta E)^2 + (\Delta N)^2}", "note": "Delta E is the East gap and Delta N is the North gap between the two people."},
    {"name": "Distance from speed and time", "tex": r"\text{distance} = \text{speed} \times \text{time}", "note": "Use it first when two people walk at different speeds."},
]

s4_patterns = [
    pat("rp-p1", "Distance between two walkers", "very common",
        "Two people start from the same place and walk in different directions. The gap between them is asked.",
        r"d = \sqrt{(\Delta E)^2 + (\Delta N)^2}",
        ["Put the start at the middle of the map.", "Find each person's end point as (East, North).", "Find the East gap and the North gap.", "Use the triples or the square root."],
        "The gap is just the distance between two points on the map.",
        "Two boys start from the same point. Ravi walks 8 km North and Sam walks 15 km East. How far apart are they?",
        ["Ravi is at (0, 8) and Sam is at (15, 0).", "The gaps are 15 East and 8 North.", "15 and 8 give the triple 8-15-17."],
        "17 km"),
    pat("rp-p2", "Direction of one person from another", "very common",
        "The question asks in which direction one person is from another after both have walked.",
        None,
        ["Find both end points from the same start.", "Take the reference person as the middle.", "Find the East gap and the North gap from the reference to the other person.", "Read the compass word from the two signs."],
        "\"B from A\" is the arrow from A to B, and the signs of the gaps name it.",
        "From the same point, Meera walks 6 km East and 10 km South. Nisha walks 2 km West and 7 km South. In which direction is Nisha from Meera?",
        ["Meera is at (6, -10). Nisha is at (-2, -7).", "From Meera to Nisha: 8 km West and 3 km North.", "West and North make North-West."],
        "North-West"),
    pat("rp-p3", "Shared legs", "common",
        "Both people walk the same leg, or one walks parallel to the other.",
        None,
        ["Put the two people on the map after their own first legs.", "A leg both walk in the same way does not change the gap.", "Find the gap after the first legs."],
        "The same leg moves both people equally, so it drops out when you subtract.",
        "Two friends start together. One walks 9 km East and the other 9 km West. Then both walk 20 km North. How far apart are they?",
        ["After the first legs the East gap is 9 + 9 = 18 km.", "The 20 km North leg is shared, so the North gap stays 0.", "The gap is 18 km."],
        "18 km"),
    pat("rp-p4", "Chain of positions", "occasional",
        "Sentences such as 'A is East of B, B is North of C' link people. The pair not named together is asked.",
        None,
        ["Put the last person of the chain at the middle.", "Add each sentence's move one at a time.", "Find the distance and direction of the asked pair."],
        "Chained moves add up like the legs of a walk.",
        "P is 9 km West of Q. Q is 12 km South of R. How far and in which direction is P from R?",
        ["R is at the middle. Q is 12 km South of R.", "P is 9 km West of Q, so P is 9 West and 12 South of R.", "9 and 12 give 15. West and South make South-West."],
        "15 km, South-West"),
    pat("rp-p5", "Different speeds for the same time", "common",
        "Two people move at given speeds for some hours. The gap between them is asked.",
        r"\text{distance} = \text{speed} \times \text{time}",
        ["Find each person's distance = speed times time.", "Put both on the map from the common start.", "Find the gap from the two positions."],
        "Distance from speed and time turns the question into a plain map problem.",
        "From a crossing, Ajay cycles North at 6 km per hour and Bala cycles East at 8 km per hour. How far apart are they after 2 hours?",
        [r"Ajay: $6 \times 2 = 12$ km North.", r"Bala: $8 \times 2 = 16$ km East.", "12 and 16 are 4 times 3 and 4 times 4, so the gap is 4 times 5."],
        "20 km"),
]

s4_tricks = [
    {"title": "Start from the person named after 'from'",
     "body": "For \"direction of C from B\", draw B first at the middle. The chain then hangs off B. The answer is simply where C lands.",
     "example": {"q": "A is 5 km North of B. C is 5 km East of A. In which direction is C from B?",
                 "steps": ["B at the middle. A is 5 km above B.", "C is 5 km to the right of A. So C is 5 East and 5 North of B."],
                 "answer": "North-East"}},
]

s4_mistakes = [
    {"wrong": "Drawing A first when B is the reference person.", "right": "Put the person named after 'from' at the middle first."},
    {"wrong": "Giving 'C from B' when the question asked 'B from C'.", "right": "Underline the reference person in every sentence."},
    {"wrong": "Adding two distances that need Pythagoras.", "right": "Use the straight-line formula when the two moves are at right angles."},
    {"wrong": "Counting a leg both people walk as part of the gap.", "right": "A shared leg does not change the gap."},
    {"wrong": "Mixing up speed and distance.", "right": "Find distance = speed times time first, then place the person."},
]

s4_revision = [
    "Put the reference person at the middle of the map.",
    "Write each person's end point as (East, North).",
    r"Gap: $\sqrt{(\Delta E)^2 + (\Delta N)^2}$.",
    "'B from A': stand at A, look at B. Reversing the pair flips the word.",
    "A leg that both people walk does not change the gap.",
    "Chains: start at the last person and add each move.",
    "Speed times time gives distance.",
]

# ---------------------------------------------------------------- patch
data = json.loads(TOPIC.read_text(encoding="utf-8"))
subs = {s["id"]: s for s in data["subtopics"]}
assert set(subs) == {"direction-idea", "final-direction", "shadow-direction", "relative-position"}
all_ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]


def put(sid, concept, notes, formulas, patterns, tricks, mistakes, revision):
    s = subs[sid]
    old_ids = {p["id"] for p in s.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sid}: dropped a pattern id"
    assert 2500 <= len(notes.strip()) <= 5000, f"{sid}: notes {len(notes)} chars"
    mistakes = [{k: dfrac(v) for k, v in m.items()} for m in mistakes]
    revision = [dfrac(r) for r in revision]
    s.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, patterns=patterns,
             tricks=tricks, mistakes=mistakes, revision=revision)


put("direction-idea", s1_concept, s1_notes, s1_formulas, s1_patterns, s1_tricks, s1_mistakes, s1_revision)
put("final-direction", s2_concept, s2_notes, s2_formulas, s2_patterns, s2_tricks, s2_mistakes, s2_revision)
put("shadow-direction", s3_concept, s3_notes, [], s3_patterns, s3_tricks, s3_mistakes, s3_revision)
put("relative-position", s4_concept, s4_notes, s4_formulas, s4_patterns, s4_tricks, s4_mistakes, s4_revision)

new_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(new_ids) == len(set(new_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("direction-distance updated:", {sid: (len(subs[sid]['notes']), len(subs[sid]['patterns'])) for sid in subs})
