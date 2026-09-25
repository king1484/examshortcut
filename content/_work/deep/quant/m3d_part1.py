"""Phase-2 deep content for quant/mensuration-3d — cube-cuboid, cylinder, cone."""
from fractions import Fraction as F

from _lib import Sub

PI = F(22, 7)


# ---------------- m3d-cube-cuboid ----------------

def build_cube():
    S = Sub("m3d-cube-cuboid")

    S.notes = r"""### The four numbers of a box
For a cuboid of dimensions $l \times b \times h$ (and a cube, where $l = b = h = a$):
| Quantity | Cuboid | Cube |
|---|---|---|
| Volume | $V = lbh$ | $a^3$ |
| Total surface area | $2(lb + bh + lh)$ | $6a^2$ |
| Lateral (4 walls) | $2h(l+b)$ | $4a^2$ |
| Diagonal | $\sqrt{l^2+b^2+h^2}$ | $a\sqrt{3}$ |
| Sum of edges | $4(l+b+h)$ | $12a$ |

These six pairs answer nearly every cube/cuboid question directly. The diagonal formula is the 2-D Pythagoras applied twice — it is the hypotenuse of a right triangle whose legs are a face diagonal and the third edge.

### Units and capacity
Volume in $\text{cm}^3$ converts to millilitres 1:1; $1\ \text{m}^3 = 10^6\ \text{cm}^3 = 1000$ litres. Tank and pit questions: compute $V$ in $\text{m}^3$, multiply by 1000 for litres. Reverse: a "capacity of 50000 litres" tank is $50\ \text{m}^3$. Area-based costs (painting, whitewashing) use the surface area asked — TOTAL for all faces, LATERAL for the four walls of a room (floor and ceiling excluded).

### Composite box work
- Cuboid cut into cubes: number of cubes $= \frac{lbh}{a^3}$ when $a$ divides all dimensions.
- Painting vs carpeting: carpeting is a floor area ($l \times b$); painting four walls is lateral area; painting a closed box is total area. Read which one is priced.
- Sum-of-edges questions: a frame or the total length of edges uses $4(l+b+h)$ — a different quantity from both area and volume.

### Reading the ask, a worked mini-case
"A room 10 m x 6 m x 4 m is to be whitewashed, including the ceiling at Rs 5 per sq m": whitewash covers four walls plus the ceiling (not the floor) $= 2h(l+b) + lb = 128 + 60 = 188$ sq m; cost $= 188 \times 5 = 940$. The same room carpeted is $lb = 60$ sq m; the same room painted fully outside is the TSA. One set of dimensions, four different answers — the exam is testing which surface you price.

### The cube number family
Cubes $1^3$ to $10^3$ (1, 8, 27, 64, 125, 216, 343, 512, 729, 1000) and their $6a^2$ (6, 24, 54, 96, 150, 216, 294, 384, 486, 600) cover most reverse questions at sight: TSA 294 → side 7 → diagonal $7\sqrt3$ in two steps. The 3-D diagonal triplets reuse the 2-D ones: edges $(3, 4, 12)$ give diagonal $13$ ($9 + 16 + 144 = 169$), and edges $(2, 3, 6)$ give diagonal $7$ ($4 + 9 + 36 = 49$).

### Quick revision
- $V = lbh = a^3$; TSA $= 2(lb+bh+lh) = 6a^2$; LSA $= 2h(l+b) = 4a^2$.
- Diagonal $\sqrt{l^2+b^2+h^2} = a\sqrt3$; edges $4(l+b+h) = 12a$.
- $1\ \text{m}^3 = 1000$ L; $1\ \text{cm}^3 = 1$ mL.
- Four walls of a room $= 2h(l+b)$; total incl. ceiling $= 2h(l+b) + lb$.
"""

    S.pattern("m3d-cb-p1", "Volume and surface area of cuboid/cube", "very common",
      "Dimensions given; volume or surface area (total/lateral) asked directly.",
      r"V = lbh;\quad \text{TSA} = 2(lb+bh+lh);\quad \text{LSA} = 2h(l+b)",
      r"""1. Read whether TOTAL (all 6 faces), LATERAL (4 walls) or VOLUME is asked.
2. Substitute; for a cube use the $a$-forms ($a^3$, $6a^2$, $4a^2$).
3. Keep factor form until the last step to avoid arithmetic slips.

Why: each quantity prices a different real thing — capacity, full paint, wall paint — so the ask determines the formula.""",
      "Find the total surface area of a cuboid 12 cm x 10 cm x 8 cm.",
      r"TSA $= 2(12{\cdot}10 + 10{\cdot}8 + 12{\cdot}8) = 2(120+80+96) = 592$ sq cm.")
    S.pattern("m3d-cb-p2", "Cube specifics: diagonal, lateral area, edges", "common",
      "A cube's face diagonal/body diagonal, lateral surface, or the total edge length is asked.",
      r"d = a\sqrt{3},\quad \text{LSA} = 4a^2,\quad \text{edges} = 12a",
      r"""1. Body diagonal: side times $\sqrt3$; face diagonal: side times $\sqrt2$ — do not mix them.
2. Lateral area (4 faces) vs total (6 faces): check the wording.
3. Edge-total questions (frames, wire along edges): $12a$.

Why: the body diagonal spans a face diagonal and the third edge ($a^2 + 2a^2 = 3a^2$), giving the clean $a\sqrt3$.""",
      "The length of the diagonal of a cube of side 6 cm is:",
      r"$d = a\sqrt3 = 6\sqrt3$ cm.")
    S.pattern("m3d-cb-p3", "Tank capacity in litres / volume cost", "very common",
      "A tank, pit or room's capacity asked in litres — or digging/painting cost from volume/area at a rate.",
      r"V(\text{m}^3) \times 1000 = \text{litres}",
      r"""1. Compute the volume in the stated units; convert BEFORE comparing to rates.
2. $1\ \text{m}^3 = 1000$ L; $1\ \text{cm}^3 = 1$ mL.
3. Cost = (area or volume) x rate — decide which from the wording.

Why: rates are quoted per litre/sq m/cu m, so the conversion is where marks are won or lost.""",
      "A tank is 1.5 m long, 1 m wide and 0.8 m deep. Its capacity in litres is:",
      r"$V = 1.5 \times 1 \times 0.8 = 1.2\ \text{m}^3 = 1200$ litres.")
    S.pattern("m3d-cb-p4", "Reverse: from volume/area back to a side", "common",
      "Volume (or surface area) of a cube given — the side, diagonal or edge-sum asked.",
      r"a = \sqrt[3]{V},\quad a = \sqrt{\text{TSA}/6}",
      r"""1. Cube: take the cube root of the volume for the side.
2. From surface area: divide by 6, take the square root.
3. Then answer the actual ask (diagonal $a\sqrt3$, edges $12a$, face area $a^2$).

Why: every cube quantity is a clean power of $a$, so any one of them rebuilds the whole box.""",
      "The volume of a cube is 343 cu cm. Its total surface area is:",
      r"$a = \sqrt[3]{343} = 7$; TSA $= 6 \times 49 = 294$ sq cm.")

    # ---- practice ----
    assert 8 * 6 * 4 == 192
    S.q("m3d-cb-p1", "easy", "The volume of a cuboid of dimensions $8$ cm $\\times$ $6$ cm $\\times$ $4$ cm is:",
        ["$192$ cu cm", "$184$ cu cm", "$208$ cu cm", "$168$ cu cm"], "$192$ cu cm",
        r"""$V = 8 \times 6 \times 4 = 192$ cu cm.""",
        r"$lbh = 192$. Trap: adding the dimensions ($18$) or $2(lb+bh+lh)$ when volume is asked.", 30)
    assert 2 * (120 + 80 + 96) == 592
    S.q("m3d-cb-p1", "medium", "The total surface area of a cuboid of dimensions $12 \\times 10 \\times 8$ cm is:",
        ["$592$ sq cm", "$496$ sq cm", "$560$ sq cm", "$640$ sq cm"], "$592$ sq cm",
        r"""TSA $= 2(lb + bh + lh) = 2(120 + 80 + 96) = 592$ sq cm.""",
        r"$2 \times 296 = 592$. Trap: $400$ — that is only $2(lb + bh)$, one face missed.", 40)
    assert 2 * 4 * (10 + 6) == 128
    S.q("m3d-cb-p1", "medium", "A room is $10$ m long, $6$ m wide and $4$ m high. The area of its four walls is:",
        ["$128$ sq m", "$96$ sq m", "$160$ sq m", "$240$ sq m"], "$128$ sq m",
        r"""Four walls $= 2h(l+b) = 2 \times 4 \times 16 = 128$ sq m.""",
        r"$2 \times 4 \times (10+6) = 128$. Trap: $240$ (that adds floor + ceiling: $128 + 120$) or $96$ (only $lb \times 2$).", 35)
    assert 4 * 49 == 196
    S.q("m3d-cb-p2", "easy", "The lateral surface area of a cube of side $7$ cm is:",
        ["$294$ sq cm", "$196$ sq cm", "$147$ sq cm", "$343$ sq cm"], "$196$ sq cm",
        r"""LSA $= 4a^2 = 4 \times 49 = 196$ sq cm.""",
        r"Four faces: $196$. Trap: $294$ (six faces) or $343$ (the volume).", 25)
    assert 12 * 5 == 60 and 4 * 5 * F(3, 1) == 60
    S.q("m3d-cb-p2", "medium", "The sum of the lengths of all edges of a cuboid is $100$ cm and its length, breadth and height are in the ratio $3:2:5$. The length of the cuboid is:",
        ["$7.5$ cm", "$5$ cm", "$12.5$ cm", "$10$ cm"], "$7.5$ cm",
        r"""Edges: $4(l+b+h) = 100 \Rightarrow l+b+h = 25$ cm.

Ratio $3:2:5$ → 10 parts = 25 → 1 part $= 2.5$ cm; length $= 3 \times 2.5 = 7.5$ cm.""",
        r"$l+b+h = 25$; 3 parts of 2.5 = $7.5$ cm. Trap: $10$ cm (the height's 5 parts).", 45)
    assert 3 * 3 * 3 + 4 ** 3 == 91
    S.q("m3d-cb-p2", "easy", "The length of the body diagonal of a cube of side $5$ cm is:",
        ["$5\\sqrt{2}$ cm", "$5\\sqrt{3}$ cm", "$10$ cm", "$15$ cm"], "$5\\sqrt{3}$ cm",
        r"""$d = a\sqrt{3} = 5\sqrt{3}$ cm.""",
        r"$5\sqrt3$ (body) vs $5\sqrt2$ (face) — the question says body/longest diagonal.", 25)
    assert F(3, 2) * 1 * 1 * F(8, 10) == F(12, 10) and F(12, 10) * 1000 == 1200
    S.q("m3d-cb-p3", "medium", "A rectangular tank is $1.5$ m long, $1$ m wide and $0.8$ m deep. Its capacity is:",
        ["$1,200$ litres", "$120$ litres", "$12,000$ litres", "$900$ litres"], "$1,200$ litres",
        r"""$V = 1.5 \times 1 \times 0.8 = 1.2\ \text{m}^3$.

Capacity $= 1.2 \times 1000 = 1200$ litres.""",
        r"$1.2\ \text{m}^3 \times 1000 = 1200$ L. Trap: $12{,}000$ (multiplied by 10,000).", 40)
    assert 10 * 8 * 2 == 160 and 160 * 5 == 800
    S.q("m3d-cb-p3", "medium", "A pit $10$ m long, $8$ m wide and $2$ m deep is dug. If the cost of digging is Rs $50$ per cu m, the total cost is:",
        ["Rs $8,000$", "Rs $1,600$", "Rs $4,000$", "Rs $800$"], "Rs $8,000$",
        r"""$V = 10 \times 8 \times 2 = 160\ \text{m}^3$.

Cost $= 160 \times 50 = 8000$.""",
        r"Volume first ($160$), then x 50: Rs $8{,}000$. Trap: Rs $1{,}600$ (area x rate).", 40)
    assert 6 * 6 * 6 == 216 and 6 * 36 == 216
    S.q("m3d-cb-p4", "medium", "The volume of a cube is $216$ cu cm. Its total surface area is:",
        ["$216$ sq cm", "$180$ sq cm", "$144$ sq cm", "$256$ sq cm"], "$216$ sq cm",
        r"""$a = \sqrt[3]{216} = 6$ cm.

TSA $= 6a^2 = 6 \times 36 = 216$ sq cm.""",
        r"$a=6$: $6 \times 36 = 216$. (Volume and TSA coincide at $a=6$ — coincidence, not a rule.)", 35)
    assert 7 * 7 * 7 == 343 and 6 * 49 == 294
    S.q("m3d-cb-p4", "hard", "The total surface area of a cube is $294$ sq cm. The length of its body diagonal is:",
        ["$7\\sqrt{3}$ cm", "$7\\sqrt{2}$ cm", "$7$ cm", "$14$ cm"], "$7\\sqrt{3}$ cm",
        r"""$6a^2 = 294 \Rightarrow a^2 = 49 \Rightarrow a = 7$ cm.

Diagonal $= 7\sqrt{3}$ cm.""",
        r"TSA → side → diagonal chain: $7\sqrt3$. Trap: $7\sqrt2$ (face diagonal).", 45)
    return S


# ---------------- m3d-cylinder ----------------

def build_cylinder():
    S = Sub("m3d-cylinder")

    S.notes = r"""### The three measures
For a cylinder of radius $r$, height $h$:
$$V = \pi r^2 h,\qquad \text{CSA (curved)} = 2\pi r h,\qquad \text{TSA} = 2\pi r(h + r)$$
The curved surface unrolls into a rectangle of width $2\pi r$ (the circumference) and height $h$ — that picture explains every formula. The two circular lids add $\pi r^2$ each for the total.

### Reverse and ratio work
- From volume: $h = \frac{V}{\pi r^2}$; from CSA: $r = \frac{\text{CSA}}{2\pi h}$.
- Changing dimensions: $V \propto r^2 h$, so doubling $r$ quadruples $V$, doubling $h$ doubles it; radius $\times 2$ AND height $\div 2$ leaves $V \times 2$. These multiplier questions are one-line proportion bookkeeping.

### Pipes, wells and flowing water
- **Hollow pipe (tube)**: metal volume $= \pi (R^2 - r^2) \times$ length — the annulus times the length.
- **Well/tank capacity**: compute $V$ in $\text{m}^3$; litres $= 1000 V$.
- **Water flow**: volume delivered per second $= \pi r^2 \times$ (speed); multiply by seconds for the total. Keep the speed units (cm/s) consistent with the radius units.

### Melting and recasting
Melting preserves VOLUME: a cylinder recast into a sphere/wire/spheres keeps $\pi r^2 h$ (with the same metal). Drawn-wire questions: the wire is a thin cylinder of equal volume; if the wire's radius is given as a decimal (0.1 cm etc.), be careful with the fourth power ($r^2$ on both sides).

### The 22/7 number family (with $r = 7$)
- $\pi r^2 = 154$ (base area), $2\pi r = 44$ (circumference).
- CSA $= 44h$: $h = 5 \to 220$, $h = 10 \to 440$, $h = 14 \to 616$.
- $V = 154h$: $h = 10 \to 1540$, $h = 5 \to 770$.
- Radii 14, 21, 3.5 work the same way: $r = 14 \Rightarrow \pi r^2 = 616$; $r = 3.5 \Rightarrow \pi r^2 = 38.5$.
Reverse questions hide in this family: volume 1540 with $r = 7$ is instantly $h = 10$.

### Two worked mini-cases
Pipe: outer R $= 5$, inner r $= 3$, length 14 — ring $= \frac{22}{7}(25 - 9) = \frac{352}{7}$; volume $= \frac{352}{7} \times 14 = 704$ cu cm. The ($R^2 - r^2$) factorises to $(R+r)(R-r) = 8 \times 2$ — sometimes faster.
Flow: a pipe of radius 2 cm delivers water at 10 cm/s for 60 s — volume $= \pi \times 4 \times 10 \times 60 = 2400\pi$ cu cm. Length delivered $=$ speed $\times$ time; the cross-section turns that length into volume.

### Quick revision
- $V = \pi r^2 h$; CSA $= 2\pi rh$; TSA $= 2\pi r(h+r)$.
- $V \propto r^2 h$: radius changes square, height changes linear.
- Pipe metal $= \pi(R^2 - r^2)L$; litres $= 1000 \times \text{m}^3$.
- Melting/recasting: volume is invariant.
"""

    S.pattern("m3d-cy-p1", "Volume / CSA / TSA of a cylinder", "very common",
      "Radius and height given (diameter given — halve it first!); one of volume, curved or total surface asked.",
      r"V = \pi r^2 h,\quad \text{CSA} = 2\pi rh,\quad \text{TSA} = 2\pi r(h+r)",
      r"""1. Identify WHICH measure is asked: capacity → $V$, lateral/curved → CSA, closed drum → TSA.
2. Substitute with $\pi = 22/7$; the memorised (7 → 22, 154, 616) family speeds this up.
3. Keep $\pi$ symbolic until the last multiplication.

Why: the three measures price different real objects (content, label, full metal sheet) — the wording picks the formula.""",
      "Find the volume of a cylinder of radius 7 cm and height 10 cm.",
      r"$V = \frac{22}{7} \times 49 \times 10 = 1540$ cu cm.")
    S.pattern("m3d-cy-p2", "Reverse: solve for the missing dimension", "common",
      "Volume or CSA given with one dimension — the other asked.",
      r"h = \frac{V}{\pi r^2},\quad r = \frac{\text{CSA}}{2\pi h}",
      r"""1. Write the formula; substitute the two knowns.
2. Solve the linear equation for the missing dimension.
3. Sanity-check the size against the given measure.

Why: each formula is linear in $h$ and quadratic in $r$ — solving for $h$ is direct algebra, solving for $r$ means a division then a root.""",
      "The volume of a cylinder is 1540 cu cm and its radius is 7 cm. Its height is:",
      r"$h = \frac{1540}{\frac{22}{7} \times 49} = \frac{1540}{154} = 10$ cm.")
    S.pattern("m3d-cy-p3", "Hollow pipe and well capacity", "common",
      "A pipe/tube with outer and inner radii — metal volume; or a well/tank — capacity in litres.",
      r"V_{\text{metal}} = \pi (R^2 - r^2) L;\quad \text{litres} = 1000 \times \text{m}^3",
      r"""1. Pipe: the cross-section is a ring — $\pi(R^2 - r^2)$ — stretched over length $L$.
2. Well: volume $\pi r^2 h$ in $\text{m}^3$, then $\times 1000$ for litres.
3. Watch units: radii in cm with length in m must be matched first.

Why: a hollow solid is the difference of two full solids; a well is just a fat cylinder priced by capacity.""",
      "A cylindrical well has radius 1.4 m and depth 5 m. Its capacity in litres is:",
      r"$V = \frac{22}{7} \times 1.96 \times 5 = 30.8\ \text{m}^3$ → $30{,}800$ litres.")
    S.pattern("m3d-cy-p4", "Dimension-change multipliers", "common",
      "'Radius doubled, height halved' — by what factor does the volume/surface change?",
      r"V' = \pi (kr)^2 (mh) = k^2 m\, V",
      r"""1. Write the volume as $\pi r^2 h$; apply the factor to each symbol.
2. $r \times k$ contributes $k^2$; $h \times m$ contributes $m$.
3. Multiply the contributions; for CSA ($\propto rh$) the factors enter linearly.

Why: radius appears squared in the volume, so its changes compound — the most-tested multiplier fact of the subtopic.""",
      "The radius of a cylinder is doubled and its height is halved. Its volume becomes:",
      r"$V' = \pi (2r)^2 \cdot \frac{h}{2} = 4 \times \frac12 \pi r^2 h = 2V$ — doubled.")

    # ---- practice ----
    assert F(22, 7) * 49 * 10 == 1540
    S.q("m3d-cy-p1", "easy", "The volume of a cylinder of radius $7$ cm and height $10$ cm is (take $\\pi = 22/7$):",
        ["$1540$ cu cm", "$770$ cu cm", "$440$ cu cm", "$3080$ cu cm"], "$1540$ cu cm",
        r"""$V = \pi r^2 h = \frac{22}{7} \times 49 \times 10 = 1540$ cu cm.""",
        r"$22 \times 7 \times 10 = 1540$. Trap: $770$ (dropped the $r^2$ to $r$).", 30)
    assert 2 * F(22, 7) * 7 * 5 == 220
    S.q("m3d-cy-p1", "easy", "The curved surface area of a cylinder of radius $7$ cm and height $5$ cm is (take $\\pi = 22/7$):",
        ["$220$ sq cm", "$440$ sq cm", "$110$ sq cm", "$154$ sq cm"], "$220$ sq cm",
        r"""CSA $= 2\pi rh = 2 \times \frac{22}{7} \times 7 \times 5 = 220$ sq cm.""",
        r"$44 \times 5 = 220$. Trap: $154$ — that is a $\pi r^2$ piece (one lid).", 25)
    assert 2 * F(22, 7) * 7 * (7 + 7) == 616
    S.q("m3d-cy-p1", "medium", "A closed cylindrical drum has radius $7$ cm and height $7$ cm. Its total surface area is (take $\\pi = 22/7$):",
        ["$616$ sq cm", "$440$ sq cm", "$308$ sq cm", "$924$ sq cm"], "$616$ sq cm",
        r"""TSA $= 2\pi r(h + r) = 2 \times \frac{22}{7} \times 7 \times 14 = 616$ sq cm.""",
        r"$2\pi r(h+r) = 44 \times 14 = 616$. Trap: $308$ (one lid only).", 35)
    assert F(1540, 154) == 10
    S.q("m3d-cy-p2", "medium", "The volume of a cylinder is $1540$ cu cm and the radius of its base is $7$ cm. Its height is (take $\\pi = 22/7$):",
        ["$10$ cm", "$7$ cm", "$14$ cm", "$5$ cm"], "$10$ cm",
        r"""$h = \frac{V}{\pi r^2} = \frac{1540}{\frac{22}{7} \times 49} = \frac{1540}{154} = 10$ cm.""",
        r"$1540 / 154 = 10$ cm. Trap: $5$ cm (used $2\pi r$ instead of $\pi r^2$).", 35)
    assert 2 * F(22, 7) * F(8, 1) == F(352, 7) and F(352, 7) * 7 == 352
    S.q("m3d-cy-p2", "medium", "The curved surface area of a cylinder is $352$ sq cm and its height is $8$ cm. Its radius is (take $\\pi = 22/7$):",
        ["$7$ cm", "$14$ cm", "$3.5$ cm", "$10$ cm"], "$7$ cm",
        r"""$2\pi rh = 352 \Rightarrow r = \frac{352 \times 7}{2 \times 22 \times 8} = 7$ cm.""",
        r"$r = \frac{352}{2\pi \times 8} = 7$ cm. Trap: $14$ (forgot the 2 in $2\pi rh$).", 40)
    assert F(22, 7) * (25 - 9) * 14 == 704
    S.q("m3d-cy-p3", "hard", "An iron pipe is $14$ cm long and has an outer radius of $5$ cm and an inner radius of $3$ cm. The volume of iron in the pipe is (take $\\pi = 22/7$):",
        ["$704$ cu cm", "$1100$ cu cm", "$396$ cu cm", "$880$ cu cm"], "$704$ cu cm",
        r"""$V = \pi (R^2 - r^2) L = \frac{22}{7} \times (25 - 9) \times 14 = \frac{22}{7} \times 16 \times 14 = 704$ cu cm.""",
        r"Ring $\times$ length: $22/7 \times 16 \times 14 = 704$. Trap: $1100$ (ignored the hollow core).", 50)
    assert F(22, 7) * F(196, 100) * 5 == F(154, 5) and F(154, 5) * 1000 == 30800
    S.q("m3d-cy-p3", "medium", "A cylindrical well has a radius of $1.4$ m and a depth of $5$ m. The water it can hold, in litres, is (take $\\pi = 22/7$):",
        ["$30,800$ litres", "$3,080$ litres", "$30,000$ litres", "$15,400$ litres"], "$30,800$ litres",
        r"""$V = \frac{22}{7} \times (1.4)^2 \times 5 = \frac{22}{7} \times 1.96 \times 5 = 30.8\ \text{m}^3$.

Litres $= 30.8 \times 1000 = 30{,}800$.""",
        r"$30.8\ \text{m}^3 \times 1000 = 30{,}800$ L. Trap: $3{,}080$ (slipped a factor of 10 in $1.4^2$).", 45)
    assert F(4, 1) * F(1, 2) == 2
    S.q("m3d-cy-p4", "medium", "The radius of a cylinder is doubled and its height is halved. Its volume becomes:",
        ["$2$ times", "$4$ times", "$1$ time (unchanged)", "$8$ times"], "$2$ times",
        r"""$V' = \pi (2r)^2 \left(\frac{h}{2}\right) = \frac{4}{2}\pi r^2 h = 2V$.""",
        r"$k^2 m = 4 \times \frac12 = 2$: doubled. Trap: 'unchanged' (the $r^2$ and $h$ effects don't cancel).", 40)
    assert F(9, 4) * 2 == F(9, 2)
    S.q("m3d-cy-p4", "hard", "The radius of a cylinder is increased by $50\\%$ and its height is decreased by $20\\%$. Its volume changes by about:",
        ["$+80\\%$", "$+50\\%$", "$+30\\%$", "$+100\\%$"], "$+80\\%$",
        r"""$r' = 1.5r$, $h' = 0.8h$: $V' = (1.5)^2 \times 0.8 \, V = 2.25 \times 0.8\, V = 1.8\,V$.

Increase $= 80\%$.""",
        r"$1.5^2 \times 0.8 = 1.8$ → $+80\%$. Trap: $+50\%$ (applied $1.5 \times 0.8 = 1.2$, missing a radius power).", 50)
    return S


# ---------------- m3d-cone ----------------

def build_cone():
    S = Sub("m3d-cone")

    S.notes = r"""### The cone formulas and the slant triplet
For a right circular cone of radius $r$, height $h$, slant $l$:
$$l = \sqrt{r^2 + h^2},\qquad V = \frac{1}{3}\pi r^2 h,\qquad \text{CSA} = \pi r l,\qquad \text{TSA} = \pi r(l + r)$$
The curved surface unrolls into a sector of radius $l$ — that is why $l$ (not $h$) appears in CSA and TSA. Almost every cone question is built on a Pythagorean $(r, h, l)$ triplet, with $(7, 24, 25)$ dominating exams and $(3, 4, 5)$-multiples next. Memorise the whole 7-24-25 family at $\pi = 22/7$:
| given | CSA | TSA | Volume |
|---|---|---|---|
| $r=7, h=24, l=25$ | $550$ | $704$ | $1232$ |

The base circle is always $\pi r^2 = 154$ here, so TSA $= 550 + 154$. A question tripling the size triples nothing — every length scales linearly, areas by $k^2$, volume by $k^3$.

### Reverse routes
- From CSA: $l = \frac{\text{CSA}}{\pi r}$, then $h = \sqrt{l^2 - r^2}$.
- From volume: $h = \frac{3V}{\pi r^2}$ — the factor 3 moving to the top is the classic slip; $r = \sqrt{\frac{3V}{\pi h}}$ likewise.
- Conical heap questions: base circumference first — $r = \frac{C}{2\pi}$ (C $= 44$ m gives $r = 7$ m directly with $\pi = 22/7$).
- Tent questions: canvas $=$ CSA only (no floor). Painted/covered-including-base: add $\pi r^2$.

### Recasting and inscribed relations
Melting preserves volume: a cone recast into a sphere satisfies $\frac{1}{3}\pi r^2 h = \frac{4}{3}\pi R^3$, so $R^3 = \frac{r^2 h}{4}$ — and $r^2 h$ is chosen divisible by 4 in every exam instance. A cone melted into $n$ similar cones divides every length by $\sqrt[3]{n}$ ($n = 27 \Rightarrow$ height $\div 3$).
Solids on the same base with height equal to the radius: $\text{cone} : \text{hemisphere} : \text{cylinder} = \frac13\pi r^3 : \frac23\pi r^3 : \pi r^3 = 1 : 2 : 3$. The largest cone inscribed in a cylinder (same base, same height) holds exactly $\frac13$ of the cylinder.

### Frustum preview
Cutting a cone parallel to its base leaves a frustum: $V = \frac{\pi h}{3}(R^2 + r^2 + Rr)$ — the bucket/tumbler shape, worked in the prism-pyramid subtopic. If instead the TOP piece is asked, it is a smaller similar cone: subtract, or use the similarity ratio directly.

### Quick revision
- $l = \sqrt{r^2+h^2}$; CSA $= \pi r l$; TSA $= \pi r(l + r)$; $V = \frac13 \pi r^2 h$.
- Triplet $(7, 24, 25)$: CSA $550$, TSA $704$, $V$ $1232$, base $154$.
- From $V$: $h = \frac{3V}{\pi r^2}$ (mind the 3). From $C$: $r = \frac{C}{2\pi}$.
- Recast cone → sphere: $R^3 = \frac{r^2 h}{4}$; into $n$ similar cones: lengths $\div \sqrt[3]{n}$.
- Same base & height ($h = r$): cone : hemisphere : cylinder $= 1:2:3$.
"""

    S.pattern("m3d-co-p1", "Slant height + CSA/TSA with a triplet", "very common",
      "Radius and height given; curved or total surface asked — the $(r, h, l)$ triplet makes $l$ instant.",
      r"l = \sqrt{r^2+h^2},\quad \text{CSA} = \pi r l,\quad \text{TSA} = \pi r(l+r)",
      r"""1. Get $l$ from the triplet (7-24-25, 3-4-5 multiples) before any algebra.
2. CSA $= \pi r l$; TSA adds the base: $\pi r(l + r)$.
3. Announce the triplet out loud in the solution — it is the whole speed play.

Why: the curved surface is a sector of radius $l$; the exam numbers are chosen so $l$ is a triplet member.""",
      "The radius of a cone is 7 cm and its height is 24 cm. Its curved surface area is:",
      r"$l = 25$ (7-24-25); CSA $= \frac{22}{7} \times 7 \times 25 = 550$ sq cm.")
    S.pattern("m3d-co-p2", "Volume of a cone (and reverse)", "very common",
      "Volume asked from $r, h$ — or volume given with a dimension asked (mind the factor 3).",
      r"V = \frac{1}{3}\pi r^2 h;\quad h = \frac{3V}{\pi r^2}",
      r"""1. Third of the cylinder volume with the same base and height.
2. Reverse: $h = \frac{3V}{\pi r^2}$ — bring the 3 up top.
3. Keep $\pi = 22/7$ till the end; thirds cancel cleanly with the 22/7 family.

Why: a cone fills a cylinder of the same base and height exactly one-third — the definition, not just a formula.""",
      "The volume of a cone is 132 cu cm and its base radius is 3 cm. Its height is:",
      r"$h = \frac{3 \times 132 \times 7}{22 \times 9} = 14$ cm.")
    S.pattern("m3d-co-p3", "Recasting: cone into sphere/spheres", "common",
      "A metallic cone melted and recast — the target solid's dimension asked.",
      r"\frac{1}{3}\pi r^2 h = \frac{4}{3}\pi R^3 \Rightarrow R^3 = \frac{r^2 h}{4}",
      r"""1. Equate volumes; $\frac{\pi}{3}$ cancels both sides for the cone→sphere case.
2. Solve $R^3 = \frac{r^2 h}{4}$ (or sum the volumes for multiple targets).
3. Take the cube root; the numbers are built to be perfect cubes.

Why: melting is volume-invariant; only the shape of the volume changes.""",
      "A solid metallic cone of radius 6 cm and height 24 cm is melted into a sphere. The radius of the sphere is:",
      r"$\frac13 \pi \cdot 36 \cdot 24 = \frac43 \pi R^3 \Rightarrow R^3 = 216 \Rightarrow R = 6$ cm.")
    S.pattern("m3d-co-p4", "Cone vs cylinder/hemisphere volume ratios", "common",
      "'A cone, hemisphere and cylinder stand on the same base and have the same height' — ratio or one volume asked.",
      r"\text{cone}:\text{hemisphere}:\text{cylinder} = 1:2:3 \ \ (h = r)",
      r"""1. Same base (radius $r$) and height $h = r$: volumes are $\frac13\pi r^3, \frac23\pi r^3, \pi r^3$.
2. Ratio $1 : 2 : 3$; the max cone in a cylinder is $\frac13$ of it.
3. Scale the ratio to the given volume and read off the asked piece.

Why: each volume is a fixed fraction of the cylinder's — the geometry does the dividing for you.""",
      "A cylinder and a cone have equal bases and equal heights. If the cylinder's volume is 120 cu cm, the cone's volume is:",
      r"Cone $= \frac13 \times 120 = 40$ cu cm.")
    S.pattern("m3d-co-p5", "Conical heap / tent (word problems)", "common",
      "A heap of grain (from base circumference) or a conical tent (canvas = CSA) with real-world wording.",
      r"r = \frac{C}{2\pi};\quad \text{canvas} = \pi r l",
      r"""1. Heap: circumference → radius → volume $\frac13\pi r^2 h$.
2. Tent: canvas covers the CURVED surface only — $\pi r l$, no base.
3. Compute $l$ via the triplet; watch metre/cm mixing.

Why: a heap has no lid and a tent has no floor — the physical object tells you which formula is 'the surface'.""",
      "A conical tent has base radius 7 m and slant height 25 m. The canvas required to make it (sq m) is:",
      r"CSA $= \frac{22}{7} \times 7 \times 25 = 550$ sq m of canvas.")

    # ---- practice ----
    assert 7 ** 2 + 24 ** 2 == 625 and F(22, 7) * 7 * 25 == 550
    S.q("m3d-co-p1", "medium", "The radius of a cone is $7$ cm and its height is $24$ cm. Its curved surface area is (take $\\pi = 22/7$):",
        ["$550$ sq cm", "$704$ sq cm", "$528$ sq cm", "$616$ sq cm"], "$550$ sq cm",
        r"""$l = \sqrt{7^2 + 24^2} = 25$ (7-24-25).

CSA $= \pi r l = \frac{22}{7} \times 7 \times 25 = 550$ sq cm.""",
        r"$l = 25$ first; $\pi r l = 550$. Trap: using $h=24$ in CSA → $528$.", 40)
    assert F(1, 3) * F(22, 7) * 49 * 24 == 1232
    S.q("m3d-co-p1", "medium", "The radius of a cone is $7$ cm and its height is $24$ cm. Its volume is (take $\\pi = 22/7$):",
        ["$1232$ cu cm", "$3696$ cu cm", "$2464$ cu cm", "$1848$ cu cm"], "$1232$ cu cm",
        r"""$V = \frac13 \pi r^2 h = \frac13 \times \frac{22}{7} \times 49 \times 24 = 1232$ cu cm.""",
        r"$\frac{1}{3} \times 22 \times 7 \times 24 = 1232$. Trap: $3696$ (forgot the third).", 40)
    assert 550 + F(22, 7) * 49 == 704
    S.q("m3d-co-p1", "hard", "The radius of a cone is $7$ cm and its height is $24$ cm. Its total surface area is (take $\\pi = 22/7$):",
        ["$704$ sq cm", "$550$ sq cm", "$646$ sq cm", "$754$ sq cm"], "$704$ sq cm",
        r"""$l = 25$; CSA $= 550$. Base $= \pi r^2 = \frac{22}{7} \times 49 = 154$.

TSA $= 550 + 154 = 704$ sq cm.""",
        r"$\pi r(l + r) = 22 \times 32 = 704$. Trap: $550$ (CSA only — the tent answer, not this one).", 50)
    assert F(22, 7) * 7 * 10 == 220
    S.q("m3d-co-p2", "easy", "The radius of a cone is $7$ cm and its slant height is $10$ cm. Its curved surface area is (take $\\pi = 22/7$):",
        ["$220$ sq cm", "$440$ sq cm", "$154$ sq cm", "$264$ sq cm"], "$220$ sq cm",
        r"""CSA $= \pi r l = \frac{22}{7} \times 7 \times 10 = 220$ sq cm.""",
        r"$\pi r l$: $220$. Trap: squaring the slant or using $r^2$.", 30)
    assert 3 * 132 * 7 == 2772 and F(2772, 198) == 14
    S.q("m3d-co-p2", "medium", "The volume of a cone is $132$ cu cm and its base radius is $3$ cm. Its height is (take $\\pi = 22/7$):",
        ["$14$ cm", "$12$ cm", "$21$ cm", "$7$ cm"], "$14$ cm",
        r"""$h = \frac{3V}{\pi r^2} = \frac{3 \times 132 \times 7}{22 \times 9} = 14$ cm.""",
        r"Bring the 3 up: $\frac{3 \times 132}{\frac{22}{7} \times 9} = 14$ cm. Trap: $21$ (used $\frac{V}{\pi r^2}$ without the 3).", 40)
    assert F(1, 3) * 36 * 24 == 288 and F(4, 3) * 216 == 288
    S.q("m3d-co-p3", "hard", "A solid metallic cone of radius $6$ cm and height $24$ cm is melted and recast into a sphere. The radius of the sphere is (take $\\pi = 22/7$):",
        ["$6$ cm", "$8$ cm", "$12$ cm", "$4$ cm"], "$6$ cm",
        r"""$\frac13 \pi (36)(24) = \frac43 \pi R^3 \Rightarrow R^3 = \frac{36 \times 24}{4} = 216 \Rightarrow R = 6$ cm.""",
        r"$R^3 = \frac{r^2 h}{4} = 216$ → $R = 6$ cm. Trap: $8$ (set $R^3 = r^2 h$ without the 4).", 55)
    assert F(120, 3) == 40
    S.q("m3d-co-p4", "medium", "A cylinder and a cone have equal base radii and equal heights. If the volume of the cylinder is $120$ cu cm, the volume of the cone is:",
        ["$60$ cu cm", "$30$ cu cm", "$40$ cu cm", "$36$ cu cm"], "$40$ cu cm",
        r"""Same base and height: cone $= \frac13 \times$ cylinder $= \frac{120}{3} = 40$ cu cm.""",
        r"One-third: $40$. Trap: $60$ (half) — the hemisphere gets that slot.", 35)
    assert F(2, 3) * 300 == 200
    S.q("m3d-co-p4", "medium", "A cone, a hemisphere and a cylinder stand on equal bases and have the same height. If the volume of the cylinder is $300$ cu cm, the volume of the hemisphere is:",
        ["$200$ cu cm", "$150$ cu cm", "$100$ cu cm", "$250$ cu cm"], "$200$ cu cm",
        r"""Same base (radius $r$) and height $h = r$: volumes are $\frac13\pi r^3$, $\frac23\pi r^3$, $\pi r^3$ — ratio $1:2:3$ (cone : hemisphere : cylinder).

Cylinder (3 parts) $= 300$ → 1 part $= 100$; hemisphere $= 2 \times 100 = 200$ cu cm.""",
        r"$\frac{2}{3} \times 300 = 200$. Trap: $100$ (that is the cone's share) or $150$ (splitting $300$ in half).", 40)
    assert F(1, 3) * F(22, 7) * 25 * 21 == 550
    S.q("m3d-co-p2", "easy", "The radius of the base of a cone is $5$ cm and its height is $21$ cm. Its volume is (take $\\pi = 22/7$):",
        ["$550$ cu cm", "$770$ cu cm", "$660$ cu cm", "$825$ cu cm"], "$550$ cu cm",
        r"""$V = \frac13 \times \frac{22}{7} \times 25 \times 21 = \frac{22}{7} \times 25 \times 7 = 550$ cu cm.""",
        r"The 21 and the 7 cancel: $\frac13 \times 21 = 7$. Trap: $770$ (dropped the third).", 30)
    assert 27 == 3 ** 3 and 18 / 3 == 6
    S.q("m3d-co-p3", "medium", "A large metallic cone of height $18$ cm is melted and recast into $27$ small solid cones, each similar in shape to the original. The height of each small cone is:",
        ["$6$ cm", "$3$ cm", "$9$ cm", "$2$ cm"], "$6$ cm",
        r"""Equal shapes: volume ratio $27 = 3^3$ → linear ratio $\sqrt[3]{27} = 3$.

Height $= \frac{18}{3} = 6$ cm.""",
        r"$\sqrt[3]{27} = 3$, so every length divides by 3: $6$ cm. Trap: $2$ cm (dividing by 9, a square root).", 45)
    assert 44 * F(7, 44) == 7 and F(1, 3) * F(22, 7) * 49 * 3 == 154
    S.q("m3d-co-p5", "medium", "A heap of wheat is in the shape of a cone. Its base circumference is $44$ m and its height is $3$ m. The volume of the heap is (take $\\pi = 22/7$):",
        ["$154$ cu m", "$231$ cu m", "$308$ cu m", "$462$ cu m"], "$154$ cu m",
        r"""$r = \frac{44 \times 7}{44} = 7$ m.

$V = \frac13 \pi r^2 h = \frac13 \times \frac{22}{7} \times 49 \times 3 = 154$ cu m.""",
        r"Circumference → $r = 7$; then a third: $154$. Trap: $462$ (full cylinder volume).", 40)
    assert F(22, 7) * 7 * 25 * 2 == 1100
    S.q("m3d-co-p5", "medium", "A conical tent has a base radius of $7$ m and a slant height of $25$ m. If canvas costs Rs $2$ per sq m, the cost of the canvas needed to make the tent is (take $\\pi = 22/7$):",
        ["Rs $1,100$", "Rs $550$", "Rs $2,200$", "Rs $1,232$"], "Rs $1,100$",
        r"""Canvas covers the curved surface only: CSA $= \pi r l = \frac{22}{7} \times 7 \times 25 = 550$ sq m.

Cost $= 550 \times 2 = 1100$.""",
        r"CSA $550 \times$ Rs $2$ = Rs $1{,}100$. Trap: Rs $1{,}232$ — that is the volume number, a different measure.", 40)
    return S
