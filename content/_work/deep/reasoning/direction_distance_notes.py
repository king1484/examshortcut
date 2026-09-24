"""Direction-distance topic: NOTES + PATTERNS (imported by direction-distance.py)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P  # noqa

NOTES = {}

NOTES["direction-idea"] = """### The one idea behind every distance question

Every direction question is a walk on a plain grid. North is up, East is right, and every sentence moves you by some amount. If you convert each sentence into a move on the grid, the answer stops being a puzzle and becomes arithmetic.

**Set up the grid.** Put the start at the origin and draw two axes: North up, East right. Give the walker a name and a pencil point. Each sentence of the question moves the point:
- "walks 5 km North" → 5 up.
- "turns left and walks 3 km" → depends on the way he was facing. If he was walking North, left is West → 3 to the left.
- "walks 5√2 km North-East" → 5 up **and** 5 right at the same time (a NE step of length k moves k/√2 in N and k/√2 in E; exams usually give it as k√2 so the split is exact).

**Displacement vs distance.** Two different numbers get swapped as options:
- *Distance travelled* = add every leg, ignoring direction.
- *Displacement (shortest distance)* = the straight line from start to finish.

**Shortest distance in one step.** Collect the net moves: net East = sum of rightward legs minus leftward legs; net North = sum of upward legs minus downward legs. Then

$$d = \\sqrt{(\\text{net E})^2 + (\\text{net N})^2}$$

**Cancellation comes first.** Before any square root, cancel opposite legs: 5 km N then 5 km S is zero movement. Most exam questions hide 2-3 such cancellations. Cancel, then apply the formula on what remains — often you land on a clean triple: 3-4-5, 5-12-13, 8-15-17, 7-24-25.

**Diagonal legs.** A leg of k√2 along NE splits into k N and k E; along NW it is k N and k W; SE is k S + k E; SW is k S + k W. So "5√2 NE then 5√2 NW" = 10 N exactly, because the East and West parts cancel.

**Do not rotate the map.** Keep North up on paper always, even when the walker turns. The walker turns; your page never does. Mixing these two is the top cause of wrong answers.

**Reading the question twice.** Four phrasings hide in this subtopic, and each wants a different number:
- "How far is he from the start?" → displacement (Pythagoras on the net legs).
- "How much distance did he cover/walk?" → sum of all legs.
- "How much shorter would a straight road be?" → total minus displacement.
- "In which direction is he from the start?" → the compass word of the net legs.

**Speed habits for the exam.** Write the legs as a running tally (+3 E, +4 N, −12 N) instead of drawing every metre; the tally is the net displacement with no diagram at all. Check the final root against the triples — if the legs net to 9 and 12, the triple 9-12-15 saves the square root. And keep answers in the option's own form: if options say 2√5, do not convert to 4.47.

### Quick revision
- Draw axes: N up, E right; start at the origin; one arrow per sentence.
- Cancel opposite legs first; then $d=\\sqrt{E^2+N^2}$ on the leftovers.
- Distance travelled = sum of legs; shortest distance = displacement — different options.
- k√2 along a diagonal = k on each of its two component directions.
- Know triples 3-4-5, 5-12-13, 8-15-17, 7-24-25 (and multiples) on sight."""

NOTES["final-direction"] = """### Where is he facing, and in what direction is the endpoint

Two different questions live in this subtopic, and they need different tools.

**Question type 1: final facing.** The walker starts facing some direction and turns. Only the turns matter — distances are decoration. Use the quarter-turn count:
- One right turn = +90° clockwise; one left turn = −90° (anticlockwise); "about turn"/180° = two quarter turns.
- Net turn = (rights − lefts) mod 4. Then read the result off the cycle **N → E → S → W → N** (clockwise).

Example: facing West, turns 90° anticlockwise then 270° clockwise. Net = −1 + 3 = +2 quarter turns → W + 2 = E. He faces East.

**Question type 2: direction of the endpoint from the start.** Here the walking path matters, the facing does not. Net the moves exactly as in distance questions (net E, net N) and read the compass of the point (net E, net N):
- E > 0, N = 0 → East; E < 0, N = 0 → West; N > 0, E = 0 → North; N < 0, E = 0 → South.
- Both nonzero → combined word: (E>0, N>0) North-East, (E>0, N<0) South-East, (E<0, N>0) North-West, (E<0, N<0) South-West.

"Direction of B from A" always means: stand at A, look at B, name the compass word. Reverse the pair and the word flips to its opposite (NE ↔ SW).

**Turns while walking.** Sentences like "walks 5 km, turns left, walks 3 km" need you to track facing leg by leg, because 'left' depends on the current facing. Walk it on paper: arrow out, turn the arrow, next arrow. After the final leg, the direction the last arrow points is the final facing; the straight line from the very start to the final point is the displacement direction.

**Backtracking.** "Turns back / retraces / returns" = 180°: the walker now faces the opposite direction and any new leg cancels the old one metre for metre.

**The two-second sanity check.** After computing, look at the sketch: a person who ended North and East of the start cannot be 'South-West' from it; a walker who never left the North-South line cannot be 'North-East'. Ten seconds of picture-checking catches most sign slips before they cost a mark.

**Mixed questions.** The hardest questions in this subtopic combine both tools: a walk with mid-path turns (facing tracked leg by leg) and then "in which direction is the endpoint from the start" (net the legs, ignore the facings). Do the two parts with two separate lists — an arrow chain for the facings and a leg tally for the displacement — and never try to read one off the other.

### Quick revision
- Final facing: net quarter turns = rights − lefts (mod 4), read on the N→E→S→W cycle.
- Endpoint direction: net (E, N) → one of the 8 compass words; ignore distances.
- "X from Y" = stand at Y, look at X; swapping the pair flips the word.
- Track facing leg by leg when turns come mid-walk; the page never rotates.
- 180° turn reverses both facing and direction of travel."""

NOTES["shadow-direction"] = """### Shadows: the sun does the pointing

A shadow question is a direction question where one arrow is drawn for you — by the sun. Learn the sun's positions and every question becomes a two-line solution.

**The two facts to memorise.**
- **Morning:** the sun is in the **East**, so every shadow points **West**.
- **Evening/sunset:** the sun is in the **West**, so every shadow points **East**.

At exactly noon the sun is overhead and shadows are shortest and ambiguous — good questions either avoid noon or make the ambiguity the answer.

**The four standard templates.**

*Template 1 — facing from the shadow.* "In the morning, a man's shadow falls in front of him." Shadow = West, and it is in front → he **faces West**. "Falls behind him" → he faces East. "Falls to his right" → his right side is West → he faces South. "To his left" → he faces North. (Check: face North — your left hand points West ✓.)

*Template 2 — shadow from the facing.* The reverse reading: the facing is given and the shadow's side is asked. Use the body map — facing North: left West, right East; facing South: left East, right West; facing East: left North, right South; facing West: left South, right North. Example: morning (shadow West) and the person faces South → per the body map, West is the right side → the shadow falls to their right.

*Template 3 — two people and one shadow.* "Back to back" questions: the shadow (a fixed compass direction at that hour) falls from one person onto the other. Place them on the compass, then use 'back to back' to fix both facings as opposite.

*Template 4 — shadow, then movement.* The person sees the shadow, walks toward/away from it or turns a stated number of degrees, and you must give the final facing. Decode the shadow into a compass direction first, convert the walk into normal direction language, then finish it as a plain final-facing question (net quarter turns on the N→E→S→W cycle).

**Common traps.** Mixing the morning and evening shadow directions is the #1 error — write "sun E → shadow W" before starting. Second trap: using the shadow as the person's facing — the shadow's direction and the person's facing are two different arrows, opposite when the shadow is in front/behind, perpendicular when left/right.

### Quick revision
- Morning: sun East → **shadow West**. Evening: sun West → **shadow East**.
- Shadow in front → facing opposite the shadow; behind → facing the shadow's side of the sky.
- Shadow left → face N (morning) / S (evening); shadow right → face S (morning) / N (evening).
- Back to back = facings are exact opposites.
- Convert the shadow to a compass word first; then solve the rest as a normal direction question."""

NOTES["relative-position"] = """### Two people, one grid

Relative-position questions put two walkers (or a walker and a fixed object) on the same grid and ask how far apart they are, or in which direction one sits from the other. The method: give **each** person their own copy of the net-move bookkeeping, then compare.

**Positions first.** Fix the common start (or the named reference point) at the origin. Walk each person separately, netting their moves: person P ends at $(E_P, N_P)$, person Q at $(E_Q, N_Q)$.

**Distance between them.** The gap is just the distance between two grid points:

$$d = \\sqrt{(E_Q - E_P)^2 + (N_Q - N_P)^2}$$

Most exam numbers land on clean triples (3-4-5, 5-12-13) or on a single axis after cancellation. If both walkers move along one shared leg ("both then walk 12 km East"), that shared leg contributes **nothing** to the gap — it shifts both equally.

**Direction of one from the other.** Stand at the person the question names second: the arrow to the other person has components $\\Delta E = E_Q - E_P$, $\\Delta N = N_Q - N_P$. Read the compass word of $(\\Delta E, \\Delta N)$ exactly as in final-direction questions. Sanity-check with a rough sketch — the answer word must match what the picture shows.

**Fixed reference points.** Many questions measure everything from an object (a pole, a well, a house) that itself never moves. That is easier, not harder: the reference is the origin, and each object's position is its own net walk from it.

**Meeting points.** If two people start together and walk for the same time, they meet where their positions coincide; questions often ask the distance of the meeting point from the start — walk each to the meeting coordinates and apply the distance formula on either one.

**Two-person direction chains.** "A is 5 km East of B; B is 12 km North of C" — chain them from the asked pair: place C at the origin, put B at (0, 12), put A at (5, 12). Then any question about A and C is one distance formula: 13 km. Chained questions are just single-walker questions with an extra setup step.

**Word order matters.** "Direction of A from B" and "direction of B from A" are opposite answers. Same for "A is East of B" (A sits on B's East) versus "B is East of A". Underline the reference person in every sentence before placing anyone — in chains, the person named *after* 'of' is the reference for that sentence.

**When the answer is a word plus a number.** Many questions ask "how far and in which direction" together. Compute the number first (gap formula), then the word (compass of the difference), and match the pair against the options as a unit — options often pair the correct distance with a wrong direction to catch half-solvers.

### Quick revision
- Walk each person separately from the same origin; end with $(E, N)$ per person.
- Gap: $\\sqrt{(\\Delta E)^2 + (\\Delta N)^2}$; shared legs cancel.
- "Direction of X from Y": compute $(E_X - E_Y, N_X - N_Y)$, read the compass word.
- Chains ("A of B, B of C"): place the last person at the origin and stack the offsets.
- Verify every answer against a rough sketch — the picture catches sign slips."""

PATTERNS = {}

PATTERNS["direction-idea"] = [
    P("di-p1", "Pythagoras on net displacement", "very common",
        "Legs on two perpendicular axes (N/S and E/W) and a question about the straight-line (shortest) distance from start to finish.",
        "1. Cancel opposite legs (N vs S, E vs W).\n2. Net the leftovers: E = right − left, N = up − down.\n3. Apply $d=\\sqrt{E^2+N^2}$.\n4. Match against standard triples (3-4-5, 5-12-13) before computing.\n\n*Why it works:* the net legs are the sides of a right triangle whose hypotenuse is the straight line home.",
        "**A man walks 3 km East, then 4 km North. How far is he from the start?**",
        "Net (3 E, 4 N) → $\\sqrt{9+16}=5$ km — the 3-4-5 triple.", "\\sqrt{(\\text{net E})^2+(\\text{net N})^2}"),
    P("di-p2", "Cancellation of retraced legs", "common",
        "The path visibly doubles back (N then S, E then W) before asking the shortest distance.",
        "1. Pair every leg with its opposite and delete both.\n2. What survives is the whole answer — often a single leg.\n3. Only then compute distance.\n\n*Why it works:* displacement only cares where you start and end; retraced legs are a net zero.",
        "**A man walks 10 km East, 4 km North, then 10 km West. How far is he from the start?**",
        "10 E cancels 10 W → net 4 N → **4 km**.", None),
    P("di-p3", "Diagonal legs with √2 splits", "common",
        "Legs stated as k√2 along North-East / North-West / South-East / South-West.",
        "1. Replace each k√2 diagonal with k on each of its two component directions.\n2. Net the components as usual.\n3. Simplify the final root; keep it in √ form if the options do.\n\n*Why it works:* a NE step of length k√2 has equal N and E components of exactly k.",
        "**A man walks 5√2 km NE, then 5√2 km NW. How far is he from the start?**",
        "NE: 5 N + 5 E. NW: 5 N + 5 W. E and W cancel → 10 N → **10 km**.", None),
    P("di-p4", "Distance travelled vs displacement", "common",
        "'How much distance did he cover / travel?' asked for a path that ends away from the start.",
        "1. Distance travelled = add every leg, directions ignored.\n2. Displacement = straight-line gap (Pythagoras).\n3. Read the question word twice: 'cover' ≠ 'away from'.\n\n*Why it works:* the two numbers differ by exactly the shortcut the walker failed to take.",
        "**A man walks 3 km East and 4 km North. What is the total distance he covered?**",
        "3 + 4 = **7 km** (the shortest gap would be 5 km — a different option).", None),
]

PATTERNS["final-direction"] = [
    P("fd-p1", "Net quarter-turns for final facing", "very common",
        "A start facing plus a list of turns (left/right/180°); question: which direction is he facing now?",
        "1. Right = +1 quarter turn, left = −1, 180° = +2 (or −2, same thing mod 4).\n2. Sum the turns mod 4.\n3. Move that many steps on the clockwise cycle N → E → S → W.\n\n*Why it works:* each quarter turn is 90° and the four compass points close a cycle.",
        "**Facing West, a man turns 90° anticlockwise, then 270° clockwise. Which direction is he facing?**",
        "Net = −1 + 3 = +2 quarter turns → W + 2 = **East**.", None),
    P("fd-p2", "Endpoint direction from the start", "very common",
        "A walking path; question asks the direction of the final point from the starting point (not the facing).",
        "1. Net the legs into (E, N) — facing never matters here.\n2. Zero in one component → pure N/S/E/W; both nonzero → combined NE/NW/SE/SW word.\n3. Sign check: E>0 = East, N>0 = North.\n\n*Why it works:* 'direction of the endpoint from start' is the compass word of the displacement vector.",
        "**A woman walks 4 km North and 3 km East. In which direction is she from her start?**",
        "Net (3 E, 4 N) → **North-East**.", None),
    P("fd-p3", "Left/right turns mid-walk", "common",
        "'Walks 5 km, turns left, walks 3 km...' — the turn word is relative to the current walking direction.",
        "1. Track the current heading arrow leg by leg.\n2. 'Left' = 90° anticlockwise of the current arrow; 'right' = 90° clockwise.\n3. Draw each leg as a new arrow, then answer from the drawing.\n\n*Why it works:* the walker rotates; only the arrow chain on paper keeps the geometry honest.",
        "**Walking North, Ravi turns left and walks 3 km, then turns left again and walks 5 km. Which direction is the last leg?**",
        "N → left → W → left → **South**.", None),
    P("fd-p4", "About-turn and return legs", "common",
        "'Turns back / retraces his path / returns' appears in the middle of a walk.",
        "1. A 180° turn flips the facing to its opposite.\n2. New legs after the flip cancel old legs along the same line.\n3. Final facing = opposite of the direction before the flip.\n\n*Why it works:* retracing walks the same line in the opposite sense.",
        "**A man walks 6 km East, then turns back and walks 2 km. Which direction is he facing, and how far is he from the start?**",
        "Facing flips E → **West**; position 6 − 2 = **4 km East** of the start.", None),
]

PATTERNS["shadow-direction"] = [
    P("sd-p1", "Morning shadow (sun East → shadow West)", "very common",
        "'Early morning / at sunrise' plus a shadow position: front, back, left or right of a person.",
        "1. Write the anchor: morning → **shadow points West**.\n2. Place the shadow: front = facing West, back = facing East.\n3. Left/right: shadow West on the left → facing North; on the right → facing South.\n\n*Why it works:* the shadow is a fixed compass arrow; the body's sides rotate around it.",
        "**Early morning, a man's shadow falls exactly in front of him. Which direction is he facing?**",
        "Morning shadow = West; in front → he faces **West**.", None),
    P("sd-p2", "Evening shadow (sun West → shadow East)", "very common",
        "'Evening / at sunset' with the same front/back/left/right shadow placement.",
        "1. Write the anchor: evening → **shadow points East**.\n2. Front → facing West; back → facing East.\n3. Left → facing South; right → facing North (check with the body: face South, your right is West, so East is left).\n\n*Why it works:* same mechanics as morning with the shadow arrow flipped 180°.",
        "**At sunset, a woman's shadow falls behind her. Which direction is she facing?**",
        "Evening shadow = East; it falls on her back, so she faces the opposite → **West**.", None),
    P("sd-p3", "Shadow to facing inference", "common",
        "The shadow's side (front/back/left/right) is given and the person's facing is asked — or the reverse.",
        "1. Convert the shadow to a compass arrow for that hour.\n2. Use the body map: N→left W/right E; S→left E/right W; E→left N/right S; W→left S/right N.\n3. Pick the facing that puts the shadow on the stated side.\n\n*Why it works:* exactly four facings exist; only one puts the shadow arrow on the required side.",
        "**In the morning, Manish's shadow falls to his right. Which direction is he facing?**",
        "Morning shadow = West; facing South, the right hand points West → he faces **South**.", None),
    P("sd-p4", "Shadow, then movement or turn", "occasional",
        "The person walks toward/away from the shadow or turns by 90°/180° after reading it; final facing is asked.",
        "1. Decode the shadow into a compass direction for that hour.\n2. Translate 'walks toward/away from the shadow' into normal direction language.\n3. Finish with net quarter turns on N → E → S → W.\n\n*Why it works:* after the conversion the question is an ordinary final-facing problem.",
        "**Morning: a man walks towards his shadow for 5 km, then turns 90° clockwise. Which direction is he facing now?**",
        "Morning shadow = West → he walked West facing West; +1 quarter turn → W + 1 = **North**.", None),
]

PATTERNS["relative-position"] = [
    P("rp-p1", "Distance between two walkers", "very common",
        "Two people walk from the same (or related) start points; the gap between them is asked.",
        "1. Walk each person to their own (E, N) from the shared origin.\n2. Gap $=\\sqrt{(E_2-E_1)^2+(N_2-N_1)^2}$.\n3. Shared equal legs cancel; look for a clean triple.\n\n*Why it works:* the gap is ordinary point-to-point distance between two grid coordinates.",
        "**Amit walks 3 km E and 4 km N; Sumit walks 4 km W and 3 km S from the same point. How far apart are they?**",
        "A (3, 4), B (−4, −3): gap $=\\sqrt{49+49}=7\\sqrt2 \\approx 9.9$ km.", "\\sqrt{(\\Delta E)^2+(\\Delta N)^2}"),
    P("rp-p2", "Direction of one person from another", "very common",
        "'In which direction is B from A?' after one or both walked.",
        "1. Compute $\\Delta E = E_B - E_A$, $\\Delta N = N_B - N_A$.\n2. Read the compass word of $(\\Delta E, \\Delta N)$.\n3. Sketch check: the answer must match the rough picture.\n\n*Why it works:* 'B from A' = the vector from A's position to B's, named by compass.",
        "**P walks 6 km E and 8 km S; Q walks 6 km W and 8 km N from the same start. In which direction is Q from P?**",
        "P (6, −8), Q (−6, 8): $\\Delta$ = (−12, +16) → West and North → **North-West**.", None),
    P("rp-p3", "Shared legs and meeting geometry", "common",
        "Both walkers cover a common leg, or one walks parallel to the other at a fixed offset.",
        "1. Note that a shared identical leg shifts both equally — it changes neither the gap nor the relative direction.\n2. Compute positions after the shared leg and apply the gap formula.\n\n*Why it works:* subtracting the two position vectors cancels the common part.",
        "**Two friends start together; one walks 5 km N, the other 5 km S; then both walk 12 km E. How far apart are they?**",
        "The 12 E is shared → gap stays vertical: 5 + 5 = **10 km**.", None),
    P("rp-p4", "Chained offsets from a reference", "occasional",
        "'A is 5 km East of B; B is 12 km North of C' — questions about the unconnected pair.",
        "1. Place the last-named person at the origin.\n2. Stack each offset in order to get every position.\n3. Answer distance/direction between the asked pair with the standard tools.\n\n*Why it works:* chained offsets are vector addition; the chain ends when every person has coordinates.",
        "**A is 5 km East of B; B is 12 km North of C. How far is A from C?**",
        "C (0, 0), B (0, 12), A (5, 12) → $\\sqrt{25+144}=13$ km.", None),
]

PYQS = [
    ("Net-displacement shortest distance", "very common", "direction-idea",
     "Legs on N/S and E/W axes; 'how far is he from the start?'",
     "Cancel opposite legs, net the rest, apply $\\sqrt{E^2+N^2}$; match 3-4-5 / 5-12-13 triples.",
     "**A man walks 9 km East, then 12 km North. How far is he from the start?**",
     "$\\sqrt{81+144}=15$ km (9-12-15 = 3×(3-4-5))."),
    ("Total distance vs displacement", "common", "direction-idea",
     "'How much distance did he cover?' for a bent path.",
     "Cover = add every leg; away-from-start = displacement. Never mix the two numbers.",
     "**Walks 3 km E, 4 km N, then 3 km W. Distance covered?**",
     "3 + 4 + 3 = **10 km** (displacement would be 4 km)."),
    ("Final facing after turns", "very common", "final-direction",
     "A start facing and a list of left/right/180° turns.",
     "Net quarter turns (right +, left −) mod 4, read on the clockwise cycle N → E → S → W.",
     "**Facing South, a man turns left, left, left. Which direction is he facing?**",
     "−3 ≡ +1 quarter turn → S + 1 = **West**."),
    ("Direction of the endpoint from the start", "very common", "final-direction",
     "A walk; the compass word of the final point from the start is asked.",
     "Net (E, N); both nonzero → combined word; one zero → pure word. Facing is irrelevant.",
     "**Walks 3 km S, 3 km E, 3 km N. Direction of the endpoint from the start?**",
     "Net (3 E, 0 N) → **East**."),
    ("Morning/evening shadow facing", "common", "shadow-direction",
     "Time of day plus where the shadow falls relative to a person.",
     "Anchor first: morning shadow West, evening shadow East; then front/behind = opposite facing, left/right via the body map.",
     "**In the evening, a man's shadow falls in front of him. Which direction is he facing?**",
     "Evening shadow = East; in front → facing **West**."),
    ("Two walkers: gap and direction", "very common", "relative-position",
     "Two people walk from a common start; distance apart or 'direction of B from A'.",
     "Walk each to (E, N); gap by $\\sqrt{(\\Delta E)^2+(\\Delta N)^2}$; direction = compass word of (ΔE, ΔN) from the named person.",
     "**A walks 4 km N and 3 km E; B stays at the start. Direction of A from B?**",
     "A (3, 4) from origin → **North-East**."),
]
