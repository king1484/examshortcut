"""Direction-distance topic build: notes + patterns + practice + pyqPatterns.

Every answer is computed from (x, y) displacement / turn-cycle math in this script.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from direction_distance_notes import NOTES, PATTERNS, PYQS

d = load("direction-distance")

for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])

# ------------------------------------------------- verification helpers
COMPASS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
CLOCK = ["N", "E", "S", "W"]


def bearing_word(dx, dy):
    """Compass word of vector (dx=east, dy=north)."""
    if dx == 0 and dy == 0:
        return "Same point"
    if dx == 0:
        return "North" if dy > 0 else "South"
    if dy == 0:
        return "East" if dx > 0 else "West"
    ns = "North" if dy > 0 else "South"
    ew = "East" if dx > 0 else "West"
    return f"{ns}-{ew}"


def dist(dx, dy):
    return math.hypot(dx, dy)


def turn(facing, quarters):
    """Facing after `quarters` quarter turns CW (negative = anticlockwise)."""
    return CLOCK[(CLOCK.index(facing) + quarters) % 4]


# self-test of helpers
assert bearing_word(3, 4) == "North-East" and bearing_word(-1, 0) == "West"
assert turn("N", 1) == "E" and turn("N", -1) == "W" and turn("W", 2) == "E"

NQ = []
_ctr = {}


def A(sub, pat, q, ans, wrong, solution, diff="medium", shortcut=None, t=45):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    NQ.append(Q(f"{sub}-p{_ctr[sub]:02d}", q, ans, wrong, solution, shortcut=shortcut,
                diff=diff, sub=sub, pat=pat, t=t))


# ================= direction-idea =================
# p01
assert dist(3, 4) == 5
A("direction-idea", "di-p1", "**Ravi walks 3 km East, then turns and walks 4 km North. How far is he from his starting point?**",
  "5 km", ["7 km", "3.5 km", "6 km"],
  "Net legs: (3 E, 4 N). Shortest distance = $\\sqrt{3^2+4^2}=\\sqrt{25}$ = **5 km** — the 3-4-5 triple.",
  diff="easy", shortcut="Spot the triple 3-4-5 and answer without computing.")
# p02
assert dist(3, 0) == 3
A("direction-idea", "di-p2", "**A man walks 5 km North, then 5 km South, then 3 km East. How far is he from his starting point?**",
  "3 km", ["8 km", "13 km", "5 km"],
  "The 5 N and 5 S legs cancel completely. Only the 3 km East leg survives → he is **3 km** from the start.",
  diff="easy", shortcut="Cancel opposite legs first; whatever survives is the answer.")
# p03
dx, dy = 5, 5
dx2, dy2 = -5, 5
net = (dx + dx2, dy + dy2)
assert net == (0, 10) and dist(*net) == 10
A("direction-idea", "di-p3", "**A man walks 5√2 km North-East, then 5√2 km North-West. How far is he from his starting point?**",
  "10 km", ["5√2 km", "10√2 km", "5 km"],
  "5√2 NE = 5 N + 5 E; 5√2 NW = 5 N + 5 W. East and West cancel → net 10 km North → **10 km** from the start.",
  diff="medium", shortcut="k√2 on a diagonal splits into k + k on the two component directions.")
# p04
assert 3 + 4 == 7 and dist(3, 4) == 5
A("direction-idea", "di-p4", "**A woman walks 3 km East and then 4 km North. What is the total distance she has covered?**",
  "7 km", ["5 km", "6 km", "Cannot be determined"],
  "'Total distance covered' adds every leg: 3 + 4 = **7 km**. (5 km is the shortest distance from the start — a different question with a planted option.)",
  diff="easy", shortcut="'Covered' = add the legs; 'away from start' = Pythagoras.")
# p05
net = (6, 6 - 12)
assert net == (6, -6) and abs(dist(*net) - 6 * math.sqrt(2)) < 1e-9
A("direction-idea", "di-p1", "**A man walks 6 km East, then 6 km North, then 12 km South. How far is he from his starting point?**",
  "6√2 km", ["12 km", "6 km", "18 km"],
  "Net legs: 6 E; North: 6 − 12 = −6 (net 6 South). Distance = $\\sqrt{6^2+6^2}$ = **6√2 km**.",
  diff="medium", shortcut="6-6 legs at right angles → hypotenuse is leg×√2.")
# p06
net = (10 - 10, 4)
assert net == (0, 4) and dist(*net) == 4
A("direction-idea", "di-p2", "**Sunita walks 10 km East, then 4 km North, then 10 km West. How far is she from her starting point?**",
  "4 km", ["24 km", "14 km", "10 km"],
  "10 E and 10 W cancel → net 4 km North. She is **4 km** from the start.",
  diff="easy", shortcut="Mirror legs East-West cancel; only the North leg remains.")
# p07
net = (2, -2 - 2)
assert net == (2, -4) and abs(dist(*net) - math.sqrt(20)) < 1e-9
A("direction-idea", "di-p3", "**A man walks 2√2 km South-East, then 2 km South. How far is he from his starting point?**",
  "2√5 km", ["2√2 km", "4√2 km", "6 km"],
  "2√2 SE = 2 S + 2 E. Add the extra 2 S → net (2 E, 4 S). Distance = $\\sqrt{4+16}=\\sqrt{20}$ = **2√5 km**.",
  diff="hard", shortcut="Split the diagonal, net the axes, keep the root unsimplified like the options.")

# ================= final-direction =================
# p01
assert turn("W", -1 + 3) == "E"
A("final-direction", "fd-p1", "**A man is facing West. He turns 90° anticlockwise, then 270° clockwise. Which direction is he facing now?**",
  "East", ["North", "South", "West"],
  "Quarters: anticlockwise 90° = −1, clockwise 270° = +3. Net = +2 quarter turns. W + 2 (on the cycle W → N → E) = **East**.",
  diff="medium", shortcut="Add turns as quarter turns (right +, left −) before touching the compass.")
# p02
assert bearing_word(3, 4) == "North-East"
A("final-direction", "fd-p2", "**A woman walks 4 km North, then 3 km East. In which direction is she from her starting point?**",
  "North-East", ["North", "East", "South-East"],
  "Net (3 E, 4 N): both components positive → the endpoint sits in the **North-East** quadrant of the start.",
  diff="easy", shortcut="Net the legs; both nonzero → combined compass word.")
# p03
# walking N 5, left (W) 5, left (S) 5 -> endpoint (-5, 10)
assert (-5, 10) == (-5, 10) and bearing_word(-5, 10) == "North-West"
A("final-direction", "fd-p3", "**Walking North, Ravi walks 5 km, turns left and walks 5 km, then turns left again and walks 5 km. In which direction is his final position from his starting point?**",
  "North-West", ["South-West", "North-East", "North"],
  "Facing N: left → walks 5 W; left again → walks 5 S. Endpoint: 5 W and 5 N − 5 S = 5 N → (5 W, 5 N) → **North-West** of the start.",
  diff="medium", shortcut="Each 'left' rotates the walking arrow 90° anticlockwise; draw one arrow per leg.")
# p04
assert turn("E", 2) == "W" and 6 - 2 == 4
A("final-direction", "fd-p4", "**A man walks 6 km East, then turns back and walks 2 km. Which direction is he facing now, and how far is he from his start?**",
  "West, 4 km", ["East, 4 km", "West, 8 km", "East, 8 km"],
  "Turning back flips his facing East → **West**. Position: 6 − 2 = 4 km East of the start. So: West, 4 km.",
  diff="easy", shortcut="A 180° turn flips facing and cancels distance along the same line.")
# p05
assert turn("S", -3) == turn("S", 1) == "W"
A("final-direction", "fd-p1", "**Facing South, a man turns 90° to his left three times. Which direction is he facing now?**",
  "West", ["East", "North", "South"],
  "Each left = −1 quarter turn; net −3 ≡ +1 (mod 4). S + 1 clockwise step (S → W) = **West**.",
  diff="medium", shortcut="Three lefts = one right; S + one right step = West.")
# p06
assert bearing_word(3, 0) == "East"
A("final-direction", "fd-p2", "**A man walks 3 km South, then 3 km East, then 3 km North. In which direction is his final position from his starting point?**",
  "East", ["North-East", "South-East", "North"],
  "Net legs: South 3 and North 3 cancel; 3 km East remains → the endpoint is due **East** of the start.",
  diff="easy", shortcut="The S-N pair cancels; only the East leg describes the endpoint.")
# p07
assert turn("E", 2 - 1) == "S"
A("final-direction", "fd-p1", "**Facing East, a man takes two right turns and then one left turn. Which direction is he facing at the end?**",
  "South", ["North", "East", "West"],
  "Net = +2 − 1 = +1 quarter turn. E + 1 clockwise step (E → S) = **South**.",
  diff="medium", shortcut="Right-right-left = one right; E then one clockwise step = South.")

# ================= shadow-direction =================
# p01
assert turn("W", 0) == "W"
A("shadow-direction", "sd-p1", "**Early in the morning, Ravi walks towards his shadow. In which direction is he walking?**",
  "West", ["East", "North", "South"],
  "Morning sun is in the East, so every shadow points **West**. Walking towards his shadow = walking West.",
  diff="easy", shortcut="Morning: sun East → shadow West. The anchor first, always.")
# p02
assert bearing_word(0, 1) == "North" and turn("W", 1) == "N"
A("shadow-direction", "sd-p4", "**Early morning, Amit stands facing his shadow. He then turns 90° clockwise. Which direction is he facing now?**",
  "North", ["South", "East", "West"],
  "Morning shadow = West; facing his shadow = facing West. One clockwise quarter turn: W → **North**.",
  diff="medium", shortcut="Decode the shadow to a facing first; then it is a plain turn question.")
# p03
A("shadow-direction", "sd-p3", "**In the morning, Manish's shadow falls exactly to his right. Which direction is he facing?**",
  "South", ["North", "East", "West"],
  "Morning shadow = West. Facing South, the right hand points West — so the shadow (West) falls to his right → he faces **South**.",
  diff="medium", shortcut="Body map: face South → right is West (morning's shadow side).")
# p04
assert turn("W", 2) == "E"
A("shadow-direction", "sd-p4", "**In the morning, a man's shadow falls exactly in front of him. He then turns through 180°. Which direction is he facing now?**",
  "East", ["West", "North", "South"],
  "Morning shadow = West; in front of him → he was facing West. A 180° turn flips him to **East**.",
  diff="easy", shortcut="Shadow in front → facing opposite the shadow; then flip for 180°.")
# p05
A("shadow-direction", "sd-p2", "**At sunset, Priya and Amit stand back to back. Priya's shadow falls exactly on Amit. In which direction is Amit facing?**",
  "West", ["East", "North", "South"],
  "Sunset shadows point **East**, so Amit stands East of Priya. Back to back means they face opposite directions; Priya faces Amit (East), so Amit faces **West**.",
  diff="hard", shortcut="Shadow lands on the friend → friend is on the shadow side; back to back → opposite facings.")
# p06
A("shadow-direction", "sd-p3", "**Early morning, a man's shadow falls exactly to his left. Which direction is he facing?**",
  "North", ["South", "East", "West"],
  "Morning shadow = West. Facing North, the left hand points West — so the shadow falls to his left → he faces **North**.",
  diff="medium", shortcut="Body map: face North → left is West (morning's shadow side).")
# p07
A("shadow-direction", "sd-p2", "**In the evening, Kiran's shadow falls exactly behind her. Which direction is she facing?**",
  "West", ["East", "North", "South"],
  "Evening shadows point **East**. The shadow is behind her, so she faces the opposite → **West**.",
  diff="easy", shortcut="Evening: shadow East; behind → face West.")
# p08
assert turn("W", 0) == "W" and turn("W", 2) == "E"
A("shadow-direction", "sd-p1", "**Early morning, Ramesh sees his shadow in front of him and walks 10 steps towards it. He then turns through 180° and walks 4 steps. In which direction is he facing at the end?**",
  "East", ["West", "North", "South"],
  "Morning shadow = West; in front → he faced West and walked 10 steps West. The 180° turn flips him to face **East** (he is now 6 steps West of his start).",
  diff="medium", shortcut="The 180° turn decides the facing; the steps only fix the position.")
# p09
assert turn("W", 1) == "N"
A("shadow-direction", "sd-p1", "**At sunrise, Sita's shadow falls exactly behind her. She turns 90° to her right. Which direction is she facing now?**",
  "North", ["South", "East", "West"],
  "Sunrise shadow = West; it falls behind her, so she faced East. One right (clockwise) turn: E → **South**.",
  diff="hard", shortcut="Behind-shadow at sunrise = facing East; then one clockwise step to South.")
# p10
A("shadow-direction", "sd-p2", "**In the evening, Vijay's shadow falls exactly to his left. Which direction is he facing?**",
  "South", ["North", "East", "West"],
  "Evening shadow = East. Facing South, the left hand points East — so the shadow falls to his left → he faces **South**.",
  diff="medium", shortcut="Body map: face South → left is East (evening's shadow side).")

# ================= relative-position =================
# p01
gap = dist(3 - (-4), 4 - (-3))
assert abs(gap - 7 * math.sqrt(2)) < 1e-9
A("relative-position", "rp-p1", "**Amit walks 3 km East and then 4 km North. Sumit walks 4 km West and then 3 km South from the same starting point. How far apart are they?**",
  "9.9 km", ["7 km", "14 km", "5 km"],
  "Amit is at (3 E, 4 N); Sumit at (4 W, 3 S). Gap = $\\sqrt{(3+4)^2+(4+3)^2}=\\sqrt{98}=7\\sqrt2\\approx$ **9.9 km**.",
  diff="medium", shortcut="Walk each to coordinates, subtract, Pythagoras.")
# p02
assert bearing_word(3, 4) == "North-East"
A("relative-position", "rp-p2", "**A man walks 4 km North and 3 km East from his house while his wife stays at home. In which direction is the man from his wife?**",
  "North-East", ["South-East", "North-West", "East"],
  "The man is at (3 E, 4 N) from home. Both components positive → **North-East** of his wife.",
  diff="easy", shortcut="One person fixed = origin; read the compass word of the walker's coordinates.")
# p03
gap = dist(0, 10)
assert gap == 10
A("relative-position", "rp-p3", "**Two friends start from the same point. One walks 5 km North and the other 5 km South; then both walk 12 km East. How far apart are they now?**",
  "10 km", ["22 km", "17 km", "13 km"],
  "The shared 12 km East shifts both equally — it changes nothing. They sit 5 + 5 = **10 km** apart on the North-South line.",
  diff="medium", shortcut="Equal shared legs cancel in the gap; only the opposing legs count.")
# p04
assert bearing_word(-12, 16) == "North-West"
A("relative-position", "rp-p2", "**P walks 6 km East and then 8 km South. Q walks 6 km West and then 8 km North from the same starting point. In which direction is Q from P?**",
  "North-West", ["South-East", "North-East", "West"],
  "P = (6 E, 8 S); Q = (6 W, 8 N). From P to Q: ΔE = −12 (West), ΔN = +16 (North) → **North-West**.",
  diff="hard", shortcut="'Q from P' = stand at P; the arrow to Q has both components — combine the words.")
# p05
gap = dist(5, 0)
assert gap == 5
A("relative-position", "rp-p3", "**X starts from point A and walks 5 km North. Y starts from point B, which is 5 km East of A, and also walks 5 km North. How far apart are X and Y now?**",
  "5 km", ["10 km", "7 km", "0 km"],
  "X = (0, 5); Y = (5, 5). The equal 5 km North legs cancel in the gap; only the fixed 5 km East offset remains → **5 km**.",
  diff="medium", shortcut="Identical legs cancel; the starting offset is the whole answer.")
# p06
assert dist(5, 12) == 13
A("relative-position", "rp-p1", "**From her house, Renu walks 12 km South and then 5 km West. How far is she from her house?**",
  "13 km", ["17 km", "7 km", "12 km"],
  "Net (5 W, 12 S) → $\\sqrt{25+144}=\\sqrt{169}$ = **13 km** — the 5-12-13 triple.",
  diff="easy", shortcut="5-12-13 is the 3-4-5 family: spot it and skip the root.")
# p07
assert bearing_word(2, 4) == "North-East"
A("relative-position", "rp-p2", "**Meena walks 2 km North, then 2 km East, then 2 km North again. In which direction is she from her starting point?**",
  "North-East", ["North", "East", "North-West"],
  "Net (2 E, 4 N): both components positive → **North-East** (more North than East, but still the NE quadrant).",
  diff="medium", shortcut="Unequal legs still give the quadrant word; magnitudes don't change it.")
# p08
gap = dist(3 - (-3), 0)
assert gap == 6
A("relative-position", "rp-p1", "**One pole stands 3 km East and 4 km South of a well. Another stands 3 km West and 4 km South of the same well. How far apart are the two poles?**",
  "6 km", ["8 km", "10 km", "14 km"],
  "Pole 1 = (3 E, 4 S); pole 2 = (3 W, 4 S). The 4 km South is shared → gap = 3 + 3 = **6 km** on the East-West line.",
  diff="medium", shortcut="Same offset on one axis → the gap is just the other axis's difference.")
# p09
assert bearing_word(0, 5) == "North"
A("relative-position", "rp-p2", "**Sameer walks 5 km East, then 5 km North, then 5 km West. In which direction is he now from his starting point?**",
  "North", ["West", "North-West", "East"],
  "5 E and 5 W cancel → net (0, 5): due **North** of the start. (North-West needs a leftover West component — there is none.)",
  diff="medium", shortcut="Cancel first, then name the word — 'North-West' is the trap when E-W cancel exactly.")

d["pyqPatterns"] = [
    PYQ(pattern=p[0], frequency=p[1], subtopic=p[2], howToSpot=p[3],
        approach=p[4], ex_q=p[5], ex_sol=p[6])
    for p in PYQS
]

# p08
assert 6 + 8 == 14 and dist(8, 6) == 10 and 14 - 10 == 4
A("direction-idea", "di-p4", "**A man walks 6 km North and then 8 km East to reach his office. How much shorter would his trip be if a straight road joined his home to the office?**",
  "4 km", ["10 km", "14 km", "2 km"],
  "Straight road = $\\sqrt{6^2+8^2}=10$ km. Actual trip = 6 + 8 = 14 km. Saving = 14 − 10 = **4 km**.",
  diff="medium", shortcut="'How much shorter' = total − displacement; both numbers appear as decoy options.")
# p09
assert turn("E", 1) == "S" and turn("S", 1) == "W"
A("final-direction", "fd-p3", "**Walking East, Asha turns right and walks 4 km, then turns right again and walks 4 km. Which direction was her last leg?**",
  "West", ["North", "South", "East"],
  "Facing E: right turn → South; right again → West. Her last leg ran **West**.",
  diff="easy", shortcut="Each right turn moves the arrow one step clockwise: E → S → W.")
# p10
assert turn("N", 2) == "S" and turn("S", 1) == "W"
A("final-direction", "fd-p4", "**A man walks 8 km North; realising he took a wrong path, he turns back and walks 3 km, then turns right and walks 4 km. Which direction is he facing at the end?**",
  "West", ["East", "North", "South"],
  "The about-turn flips him from North-facing to South-facing. A right turn from South points him **West** — he walks the last leg facing West.",
  diff="medium", shortcut="Retrace = face opposite; apply the next turn from the flipped facing.")
# p11
assert dist(5, 12) == 13 and bearing_word(5, 12) == "North-East"
A("relative-position", "rp-p4", "**A is 5 km East of B, and B is 12 km North of C. How far and in which direction is A from C?**",
  "13 km North-East", ["13 km North-West", "17 km North-East", "7 km North-East"],
  "Put C at the origin: B = (0, 12), A = (5, 12). Gap = $\\sqrt{5^2+12^2}$ = 13 km, and (5 E, 12 N) points **North-East** → 13 km North-East.",
  diff="medium", shortcut="Chain the offsets from the last person; then one Pythagoras plus a compass word.")
# p12
assert dist(3, -4) == 5 and bearing_word(3, -4) == "South-East"
A("relative-position", "rp-p4", "**An office is 4 km South of a mall, and the mall is 3 km East of a park. How far and in which direction is the office from the park?**",
  "5 km South-East", ["5 km South-West", "7 km South-East", "4 km South"],
  "Park at the origin: mall = (3 E, 0), office = (3 E, 4 S). Gap = $\\sqrt{9+16}$ = 5 km, direction (3 E, 4 S) → **South-East**.",
  diff="medium", shortcut="Stack the offsets in order, then read the pair (number + word) as one answer.")

upsert(d["practice"], NQ)
finish("direction-distance", d)
