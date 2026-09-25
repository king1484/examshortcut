"""Phase-2 deep content for quant/mensuration-2d — polygons, scaling."""
from fractions import Fraction as F

from _lib import Sub


# ---------------- m2d-polygons ----------------

def build_polygons():
    S = Sub("m2d-polygons")

    S.notes = r"""### The regular-polygon toolkit
For a regular polygon of $n$ sides (side $a$):
- Exterior angle $= \frac{360^\circ}{n}$; interior angle $= 180^\circ - $ exterior.
- Interior angle sum $= (n-2) \times 180^\circ$ (any polygon).
- Diagonals $= \frac{n(n-3)}{2}$.
- Area $= n \times$ (area of the $n$ congruent isosceles triangles from the centre) $= \frac{1}{2} \times P \times \text{apothem}$, where $P = na$ and the apothem is the centre-to-side distance.

Angle chain: interior $150^\circ$ → ext $30^\circ$ → $n = 12$. Sum chain: sum $1080^\circ$ → $n = \frac{1080}{180} + 2 = 8$. Diagonal chain: $d = 20$ → $n(n-3) = 40$ → $n = 8$.

### The hexagon (the exam's favourite)
A regular hexagon is **six equilateral triangles**: side = radius of the circumscribed circle.
- Area $= 6 \times \frac{\sqrt3}{4}a^2 = \frac{3\sqrt3}{2}a^2$ — know as "6 equilateral pieces", faster than the formula.
- Long diagonal $= 2a$ (through the centre, two radii).
- Short diagonal $= a\sqrt3$ (skips one vertex).
- Hexagon side = radius: an equilateral triangle built on alternate vertices has side $a\sqrt3$.

### How the questions are built
- Given an interior/exterior angle → find $n$ (or the other angle).
- Given the sum of interior angles → find $n$, then each exterior angle $\frac{360^\circ}{n}$.
- Given diagonals → solve the quadratic-ish $n(n-3) = 2d$ by testing factors.
- Hexagon area from side, or side from area — pure equilateral work.
- Apothem questions: $K = \frac12 \times$ perimeter $\times$ apothem, often with $\sqrt3$ apothems for hexagons.

### The table worth memorising
| $n$ | Name | Interior angle | Diagonals |
|---|---|---|---|
| 5 | Pentagon | $108^\circ$ | 5 |
| 6 | Hexagon | $120^\circ$ | 9 |
| 7 | Heptagon | $\approx 128.57^\circ$ | 14 |
| 8 | Octagon | $135^\circ$ | 20 |
| 9 | Nonagon | $140^\circ$ | 27 |
| 10 | Decagon | $144^\circ$ | 35 |
| 12 | Dodecagon | $150^\circ$ | 54 |

Reading backwards from any column gives $n$ instantly: interior $144^\circ$ → decagon; 20 diagonals → octagon; interior $150^\circ$ → 12 sides. The exterior angle is always $\frac{360^\circ}{n}$ and the interior angles of ANY $n$-gon (regular or not) sum to $(n-2) \times 180^\circ$ — only the "each angle" phrasing requires regularity.

### Quick revision
- ext $= \frac{360}{n}^\circ$; int $= 180 -$ ext; sum $= (n-2) \times 180^\circ$.
- Diagonals $= \frac{n(n-3)}{2}$; solve by factor pairs.
- $K = \frac12 \times P \times$ apothem.
- Hexagon $= 6$ equilateral triangles: $K = \frac{3\sqrt3}{2}a^2$; long diagonal $2a$; short $a\sqrt3$.
"""

    S.pattern("m2d-pg-p1", "Hexagon as six equilateral triangles", "very common",
        "A regular hexagon's side given — area asked; or area/long-diagonal given — side asked.",
        r"K = 6 \times \frac{\sqrt3}{4}a^2 = \frac{3\sqrt{3}}{2}a^2",
        r"""1. Picture the 6 equilateral triangles of side $a$.
2. Area $= 6 \times \frac{\sqrt3}{4}a^2 = \frac{3\sqrt3}{2}a^2$; keep $\sqrt3$ symbolic.
3. Reverse: $a^2 = \frac{2K}{3\sqrt3}$.

Why: the centre joins to all vertices, and the hexagon's central angle of $60^\circ$ makes each piece equilateral.""",
        "Find the area of a regular hexagon of side 6 cm.",
        r"$K = \frac{3\sqrt3}{2} \times 36 = 54\sqrt{3}$ sq cm (six $\frac{\sqrt3}{4} \times 36 = 9\sqrt3$ pieces).")
    S.pattern("m2d-pg-p2", "Area from perimeter and apothem", "common",
        "Perimeter and apothem (centre-to-side distance) given — or both derived — area asked.",
        r"K = \frac{1}{2} \times P \times \text{apothem}",
        r"""1. Half of (perimeter × apothem) — one multiplication, no side counting.
2. For a hexagon the apothem is $\frac{\sqrt3}{2}a$; square-side shapes give integer apothems.
3. If the apothem arrives with $\sqrt3$, expect a $\sqrt3$ in the answer.

Why: the polygon splits into $n$ triangles of base (side) and height (apothem); their areas total exactly that formula.""",
        "A regular polygon has perimeter 72 cm and apothem 6 cm. Its area is:",
        r"$K = \frac12 \times 72 \times 6 = 216$ sq cm.")
    S.pattern("m2d-pg-p3", "Interior/exterior angles and the angle sum", "very common",
        "An interior angle, exterior angle, or the angle sum of a regular polygon given — find $n$ or the other angle.",
        r"\text{ext} = \frac{360^\circ}{n},\quad \text{int} = 180^\circ - \text{ext},\quad \text{sum} = (n-2) \times 180^\circ",
        r"""1. Whatever is given, route through the exterior angle: ext $= 180^\circ - $ int.
2. $n = \frac{360^\circ}{\text{ext}}$; from the sum: $n = \frac{\text{sum}}{180^\circ} + 2$.
3. Answer the quantity actually asked (each angle vs total sum vs $n$).

Why: exterior angles always total $360^\circ$ for any convex polygon — the cleanest hub of the three routes.""",
        "Find the measure of each interior angle of a regular octagon.",
        r"ext $= \frac{360}{8} = 45^\circ$; interior $= 180 - 45 = 135^\circ$.")
    S.pattern("m2d-pg-p4", "Counting diagonals", "common",
        "'How many diagonals does a polygon of n sides have?' — or reversed: given the diagonal count, find $n$.",
        r"d = \frac{n(n-3)}{2}",
        r"""1. Forward: substitute $n$; the product $n(n-3)$ is always even.
2. Reverse: set $n(n-3) = 2d$ and test factor pairs of $2d$ that differ by 3.
3. Sanity: triangle 0, square 2, pentagon 5, hexagon 9, octagon 20, decagon 35.

Why: each of the $n$ vertices connects to $n-3$ non-adjacent vertices, and every diagonal gets counted twice.""",
        "A polygon has 90 diagonals. The number of its sides is:",
        r"$n(n-3) = 180$: try $15 \times 12 = 180$ → $n = 15$.")
    S.pattern("m2d-pg-p5", "Hexagon diagonals and side relations", "occasional",
        "A hexagon's long/short diagonal related to its side, or a triangle built inside the hexagon.",
        r"\text{long diagonal} = 2a,\quad \text{short diagonal} = a\sqrt{3}",
        r"""1. Long diagonal = two radii through the centre: $2a$.
2. Short diagonal (skip one vertex) $= a\sqrt3$ — it is the side of the inscribed equilateral triangle.
3. Radius of the circumscribed circle = side $a$ — used for 'circle through hexagon corners' questions.

Why: the six $60^\circ$ centre angles make every such segment a chord whose length follows from an equilateral or 30-60-90 triangle.""",
        "The length of the longest diagonal of a regular hexagon of side 8 cm is:",
        r"$2a = 16$ cm (it passes through the centre, spanning two radii = two sides).")

    # ---- practice ----
    assert F(3, 2) * 36 == 54
    S.q("m2d-pg-p1", "medium", "The area of a regular hexagon of side $6$ cm is:",
        ["$54\\sqrt{3}$ sq cm", "$36\\sqrt{3}$ sq cm", "$72\\sqrt{3}$ sq cm", "$48\\sqrt{3}$ sq cm"], "$54\\sqrt{3}$ sq cm",
        r"""Six equilateral triangles of side 6: each has area $\frac{\sqrt3}{4} \times 36 = 9\sqrt3$.

Total $= 6 \times 9\sqrt3 = 54\sqrt3$ sq cm.""",
        r"$\frac{3\sqrt3}{2}a^2 = \frac{3\sqrt3}{2} \times 36 = 54\sqrt3$. Trap: $36\sqrt3$ (four triangles, not six).", 40)
    assert 6 * F(1, 4) * 16 == 24
    S.q("m2d-pg-p1", "easy", "A regular hexagon is made of six equilateral triangles. If each triangle has area $4\\sqrt{3}$ sq cm, the area of the hexagon is:",
        ["$24\\sqrt{3}$ sq cm", "$18\\sqrt{3}$ sq cm", "$30\\sqrt{3}$ sq cm", "$12\\sqrt{3}$ sq cm"], "$24\\sqrt{3}$ sq cm",
        r"""$6 \times 4\sqrt3 = 24\sqrt3$ sq cm (equivalently side $a$: $6 \times \frac{\sqrt3}{4}a^2 = 4\sqrt3 \Rightarrow a = 4$).""",
        r"Just multiply by 6: $24\sqrt3$. Trap: dividing by 6 or using 4 pieces.", 25)
    assert F(1, 2) * 72 * 6 == 216
    S.q("m2d-pg-p2", "easy", "A regular polygon has perimeter $72$ cm and apothem $6$ cm. Its area is:",
        ["$216$ sq cm", "$432$ sq cm", "$108$ sq cm", "$240$ sq cm"], "$216$ sq cm",
        r"""$K = \frac12 \times P \times \text{apothem} = \frac12 \times 72 \times 6 = 216$ sq cm.""",
        r"Half of $432$: $216$. Trap: $432$ (forgot the half).", 30)
    assert F(1, 2) * 60 * F(5 * 5, 2) == 375
    S.q("m2d-pg-p2", "medium", "The perimeter of a regular hexagon is $60$ cm (side $10$ cm) and its apothem is $5\\sqrt{3}$ cm. Its area is:",
        ["$150\\sqrt{3}$ sq cm", "$300\\sqrt{3}$ sq cm", "$75\\sqrt{3}$ sq cm", "$180\\sqrt{3}$ sq cm"], "$150\\sqrt{3}$ sq cm",
        r"""$K = \frac12 \times 60 \times 5\sqrt3 = 150\sqrt3$ sq cm.

(Check: $\frac{3\sqrt3}{2} \times 100 = 150\sqrt3$ ✓.)""",
        r"$\frac12 \times 60 \times 5\sqrt3 = 150\sqrt3$. Trap: $300\sqrt3$ (no halving).", 40)
    assert (8 - 2) * 180 == 1080 and 360 // 8 == 45
    S.q("m2d-pg-p3", "easy", "Each interior angle of a regular octagon is:",
        ["$135^\\circ$", "$150^\\circ$", "$120^\\circ$", "$140^\\circ$"], "$135^\\circ$",
        r"""ext $= \frac{360^\circ}{8} = 45^\circ$; interior $= 180^\circ - 45^\circ = 135^\circ$.""",
        r"$\frac{1080}{8} = 135^\circ$ by the sum route too. Trap: $150^\circ$ (that is the dodecagon).", 30)
    assert (10 - 2) * 180 == 1440 and 360 // 10 == 36
    S.q("m2d-pg-p3", "easy", "The sum of the interior angles of a regular decagon is:",
        ["$1440^\\circ$", "$1620^\\circ$", "$1800^\\circ$", "$1260^\\circ$"], "$1440^\\circ$",
        r"""$(n-2) \times 180^\circ = 8 \times 180^\circ = 1440^\circ$ (each angle $144^\circ$).""",
        r"$8 \times 180 = 1440$. Trap: $1800^\circ$ (used $n = 12$) or per-angle value $144^\circ$.", 30)
    assert 8 * 5 == 40 and F(40, 2) == 20
    S.q("m2d-pg-p4", "medium", "The number of diagonals of a regular octagon is:",
        ["$16$", "$20$", "$24$", "$18$"], "$20$",
        r"""$d = \frac{n(n-3)}{2} = \frac{8 \times 5}{2} = 20$.""",
        r"$\frac{8 \times 5}{2} = 20$. Trap: $16$ (counted each diagonal once but used $n-4$).", 35)
    assert 15 * 12 == 180 and F(180, 2) == 90
    S.q("m2d-pg-p4", "hard", "A polygon has $90$ diagonals. The number of sides of the polygon is:",
        ["$15$", "$12$", "$18$", "$13$"], "$15$",
        r"""$\frac{n(n-3)}{2} = 90 \Rightarrow n(n-3) = 180$.

Factor pairs of 180 differing by 3: $15 \times 12$ → $n = 15$.""",
        r"$15(15-3) = 180$ → 15 sides. Trap: $12$ (that gives 54 diagonals).", 50)
    assert 2 * 8 == 16
    S.q("m2d-pg-p5", "easy", "The length of the longest diagonal of a regular hexagon of side $8$ cm is:",
        ["$16$ cm", "$8\\sqrt{3}$ cm", "$12$ cm", "$8\\sqrt{2}$ cm"], "$16$ cm",
        r"""The longest diagonal passes through the centre: two radii $= 2a = 16$ cm.""",
        r"$2 \times 8 = 16$ cm. Trap: $8\sqrt3$ — that is the SHORT diagonal.", 30)
    assert 12 / 2 == 6 and F(3, 2) * 36 == 54
    S.q("m2d-pg-p5", "medium", "The longest diagonal of a regular hexagon is $12$ cm. The area of the hexagon is:",
        ["$54\\sqrt{3}$ sq cm", "$108\\sqrt{3}$ sq cm", "$36\\sqrt{3}$ sq cm", "$27\\sqrt{3}$ sq cm"], "$54\\sqrt{3}$ sq cm",
        r"""Longest diagonal $= 2a \Rightarrow a = \frac{12}{2} = 6$ cm.

$K = \frac{3\sqrt3}{2} \times 36 = 54\sqrt3$ sq cm.""",
        r"Side = half the long diagonal: $6$; area $\frac{3\sqrt3}{2} \times 36 = 54\sqrt3$. Trap: $108\sqrt3$ (took the diagonal as the side).", 45)
    return S


# ---------------- m2d-scaling ----------------

def build_scaling():
    S = Sub("m2d-scaling")

    S.notes = r"""### The master rule: areas scale as the SQUARE
If every length of a figure is multiplied by $k$ (sides doubled, "similar figures", map scales, photo enlargements):
- lengths, perimeters, diagonals → $\times k$
- **areas → $\times k^2$**

Going backwards (area ratio → length ratio) needs the square root. Perimeter ratio $p:q$ → area ratio $p^2:q^2$; area ratio $a:b$ → perimeter ratio $\sqrt a : \sqrt b$. This single rule answers most of the subtopic.

### Percentage side-changes
Side $+x\%$ → area $+\left(2x + \frac{x^2}{100}\right)\%$. Memorise the common pair: $+20\% \to +44\%$, $-10\% \to -19\%$. A negative change is a DECREASE in area, still computed as $k = (1 - \frac{x}{100})^2$: $0.9^2 = 0.81$ → $-19\%$.

### Cost, paint, tiles, grass
Any "cost of carpeting/painting/fencing" question scales with the QUANTITY it prices:
- paint/carpet/grass → area → $k^2$.
- fencing/border → perimeter → $k$.
If the side triples, an area-based cost becomes $9 \times$; a fence cost becomes $3 \times$.

### Maps, models, photos
Map scale $1:n$ means lengths on the map are $\frac{1}{n}$ of reality, so **areas are $\frac{1}{n^2}$**. Actual area $=$ map area $\times n^2$ (watch the unit conversion: $1\ \text{m}^2 = 10^4\ \text{cm}^2$, $1\ \text{ha} = 10^4\ \text{m}^2$). Photo enlarged "to 250% of original" means $k = 2.5$ → area $\times 6.25$.

### Same perimeter, different areas
Of all shapes with a given perimeter, the **circle encloses the most area**; among rectangles, the square wins. Wire-bending questions: a wire of length $L$ bent into a square gives side $\frac{L}{4}$, into a circle gives $r = \frac{L}{2\pi}$ — the circle's area is bigger (for $L = 44$: square $121$, circle $154$).

### A worked chain and the two traps
Typical chain: perimeters $3:5$ → sides $3:5$ → areas $9:25$ → if the larger area is 200, the smaller is $200 \times \frac{9}{25} = 72$. Trap one: applying the linear ratio to areas (giving $120$ here) — the most common wrong option offered. Trap two: forgetting that a DECREASE also squares: $-10\%$ on the side is $0.9^2 = 0.81$, i.e. $-19\%$ (the recovery term $\frac{x^2}{100}$ stops it from being $-20\%$). And when volumes appear (boxes, tanks), the law is $k^3$ — that belongs to mensuration-3d, but a 2-D question offering a $k^3$-style answer is bait, not a route.

### Quick revision
- Lengths $\times k$; areas $\times k^2$; reverse needs $\sqrt{\ }$.
- Side $+x\%$ → area $+\left(2x + \frac{x^2}{100}\right)\%$; $+20\% \to 44\%$, $-10\% \to -19\%$.
- Area costs (paint/carpet) scale $k^2$; fence costs scale $k$.
- Map $1:n$: areas $\times \frac{1}{n^2}$. Photo to 250% → area $\times 6.25$.
- Same perimeter: circle area > square area.
"""

    S.pattern("m2d-sc-p1", "Linear scale → area scale", "very common",
        "'Sides doubled/tripled', 'similar figures with perimeter ratio p : q' — new area or area ratio asked.",
        r"K' = k^2 K,\quad \frac{K_1}{K_2} = \left(\frac{P_1}{P_2}\right)^2",
        r"""1. Read off the linear factor $k$ (or the perimeter ratio).
2. Square it for areas.
3. Reverse direction (area ratio given → side/perimeter ratio) takes the root.

Why: area is the product of two lengths, so the factor enters twice.""",
        "The perimeters of two similar figures are in the ratio 3 : 5. If the larger area is 200 sq cm, the smaller area is:",
        r"Area ratio $= 9 : 25$; smaller $= 200 \times \frac{9}{25} = 72$ sq cm.")
    S.pattern("m2d-sc-p2", "Cost / tiles / carpet scaling", "common",
        "Painting, carpeting, tiling or paving costs quoted for one size — the figure's side changes — new cost asked.",
        r"\text{cost} \propto \text{area} \Rightarrow \text{cost}' = k^2 \times \text{cost}",
        r"""1. Decide what the cost is proportional to: paint/carpet/tiles → AREA; fencing → PERIMETER.
2. Find the linear factor $k$ between the sizes.
3. Multiply the cost by $k^2$ (or $k$ for fencing).

Why: unit costs multiply a quantity — the question is only whether that quantity is 2-D or 1-D.""",
        "Carpeting a square room of side 5 m costs Rs 600. The cost of carpeting a square room of side 15 m is:",
        r"$k = 3$ → cost $\times 9$: $600 \times 9 = 5400$.")
    S.pattern("m2d-sc-p3", "Percentage change in side → change in area", "very common",
        "'Side increased by x%' / 'side decreased by x%' — percentage change in area asked.",
        r"\text{area change} = \pm 2x + \frac{x^2}{100} (\%); \text{ (for decrease: } -2x + \frac{x^2}{100})",
        r"""1. Write the linear multiplier: $1 + \frac{x}{100}$ or $1 - \frac{x}{100}$.
2. Square it: that is the area multiplier.
3. Convert to a percentage change; a decrease in side still yields the $+\frac{x^2}{100}$ term ($0.9^2 = 0.81$ → $-19\%$).

Why: $(1 \pm \epsilon)^2 = 1 \pm 2\epsilon + \epsilon^2$ — the square of the small term is the famous 'extra' effect.""",
        "If each side of a square is increased by 20%, the percentage increase in its area is:",
        r"$1.2^2 = 1.44$ → $44\%$ increase ($2 \times 20 + \frac{400}{100} = 44$).")
    S.pattern("m2d-sc-p4", "Maps, models and photo enlargements", "common",
        "A map scale 1 : n with an area measured on the map — actual area asked; or a photo enlarged/shrunk — new area asked.",
        r"\text{actual area} = \text{map area} \times n^2",
        r"""1. Map scale is LINEAR: $1:n$ → areas are $1:n^2$.
2. Multiply the map area by $n^2$; then convert units ($1\,\text{m}^2 = 10^4\,\text{cm}^2$).
3. Photos: 'enlarged to 250%' → $k = 2.5$ → area $\times 6.25$.

Why: both directions are the same square law; only the wording (shrink vs enlarge) changes whether $k$ is below or above 1.""",
        "On a map of scale 1 : 5000, a plot measures 4 sq cm. Its actual area is:",
        r"$4 \times 5000^2 = 10^8$ sq cm $= 10{,}000$ sq m (1 ha).")
    S.pattern("m2d-sc-p5", "Same perimeter: square vs circle", "occasional",
        "A wire/rope of fixed length bent into a square and a circle — areas (or their difference) asked.",
        r"\text{square: } a = \frac{L}{4};\quad \text{circle: } r = \frac{L}{2\pi};\quad K_{\text{circle}} > K_{\text{square}}",
        r"""1. Square: side $= \frac{L}{4}$, area $= \frac{L^2}{16}$.
2. Circle: $r = \frac{L}{2\pi}$, area $= \frac{L^2}{4\pi}$ — always the bigger one.
3. For $L = 44$ ($\pi = 22/7$): square $121$, circle $154$, difference $33$.

Why: the circle is the maximal-area shape for a given perimeter — the isoperimetric fact exams love.""",
        "A wire 44 cm long is bent into a circle. The area enclosed is (take π = 22/7):",
        r"$r = \frac{44}{2 \times 22/7} = 7$ cm; area $= \frac{22}{7} \times 49 = 154$ sq cm.")

    # ---- practice ----
    assert 5 * 2 * 5 * 2 == 100 and 25 * 4 == 100
    S.q("m2d-sc-p1", "easy", "The area of a square is $25$ sq cm. If each side is doubled, the new area is:",
        ["$100$ sq cm", "$50$ sq cm", "$75$ sq cm", "$625$ sq cm"], "$100$ sq cm",
        r"""Side doubles → $k = 2$ → area $\times k^2 = 4$.

New area $= 25 \times 4 = 100$ sq cm (side $10$).""",
        r"$k^2 = 4$: $25 \times 4 = 100$. Trap: $50$ (doubled the area, not squared the factor).", 25)
    assert F(9, 25) * 200 == 72
    S.q("m2d-sc-p1", "medium", "The perimeters of two similar triangles are in the ratio $3:5$. If the area of the larger triangle is $200$ sq cm, the area of the smaller triangle is:",
        ["$120$ sq cm", "$72$ sq cm", "$80$ sq cm", "$60$ sq cm"], "$72$ sq cm",
        r"""Area ratio $= 3^2 : 5^2 = 9 : 25$.

Smaller area $= 200 \times \frac{9}{25} = 72$ sq cm.""",
        r"$\left(\frac35\right)^2 = \frac{9}{25}$: $200 \times \frac{9}{25} = 72$. Trap: $120$ (linear ratio applied to area).", 40)
    assert 600 * 9 == 5400
    S.q("m2d-sc-p2", "medium", "Carpeting a square room of side $5$ m costs Rs $600$. The cost of carpeting a square room of side $15$ m (same rate) is:",
        ["Rs $1,800$", "Rs $5,400$", "Rs $3,600$", "Rs $2,400$"], "Rs $5,400$",
        r"""Side triples ($k = 3$) → area $\times 9$ → cost $\times 9$.

$600 \times 9 = 5400$.""",
        r"Area-based cost scales $k^2$: $600 \times 9 = 5400$. Trap: $1800$ (scaled by $k$, not $k^2$).", 40)
    assert 80 * 4 == 320
    S.q("m2d-sc-p2", "easy", "It takes $80$ identical tiles to cover a square floor. If the side of the floor is doubled (tiles unchanged), the number of tiles needed is:",
        ["$160$", "$320$", "$240$", "$640$"], "$320$",
        r"""Side doubles → area (and tile count) $\times 4$: $80 \times 4 = 320$ tiles.""",
        r"$k^2 = 4$: $320$. Trap: $160$ (doubled the count).", 25)
    assert F(144, 100) == F(36, 25)
    S.q("m2d-sc-p3", "medium", "If each side of a square is increased by $20\\%$, the percentage increase in its area is:",
        ["$40\\%$", "$44\\%$", "$20\\%$", "$48\\%$"], "$44\\%$",
        r"""$1.2^2 = 1.44$ → area up by $44\%$.

(Formula: $2x + \frac{x^2}{100} = 40 + 4 = 44$.)""",
        r"$2(20) + \frac{20^2}{100} = 44\%$. Trap: $40\%$ (forgot the $x^2$ term).", 35)
    assert F(81, 100) == F(81, 100)
    S.q("m2d-sc-p3", "medium", "If each side of a square is decreased by $10\\%$, the percentage decrease in its area is:",
        ["$20\\%$", "$19\\%$", "$21\\%$", "$10\\%$"], "$19\\%$",
        r"""$0.9^2 = 0.81$ → area becomes $81\%$ → decrease of $19\%$.

(Formula: $2x - \frac{x^2}{100} = 20 - 1 = 19$.)""",
        r"$2(10) - \frac{10^2}{100} = 19\%$. Trap: $20\%$ (straight doubling, missing the $+x^2$ correction).", 35)
    assert 4 * 5000 * 5000 == 100000000 and F(100000000, 10000) == 10000
    S.q("m2d-sc-p4", "hard", "On a map drawn to the scale $1 : 5000$, a rectangular plot measures $4$ sq cm. The actual area of the plot is:",
        ["$10{,}000$ sq m", "$2{,}000$ sq m", "$100{,}000$ sq m", "$1{,}000$ sq m"], "$10{,}000$ sq m",
        r"""Areas scale as $n^2$: actual area $= 4 \times 5000^2 = 10^8$ sq cm.

$10^8$ sq cm $= \frac{10^8}{10^4} = 10{,}000$ sq m (= 1 hectare).""",
        r"$4 \times 25{,}000{,}000$ sq cm → $10{,}000$ sq m. Trap: forgetting the unit conversion (answering $10^8$).", 55)
    assert F(25, 4) * 40 == 250
    S.q("m2d-sc-p4", "medium", "A photograph is enlarged so that each dimension becomes $250\\%$ of the original. If the original photo's area is $40$ sq cm, the enlarged area is:",
        ["$100$ sq cm", "$250$ sq cm", "$160$ sq cm", "$625$ sq cm"], "$250$ sq cm",
        r"""$k = 2.5$ → area $\times k^2 = 6.25$.

$40 \times 6.25 = 250$ sq cm.""",
        r"$2.5^2 = 6.25$: $40 \times 6.25 = 250$. Trap: $100$ ($40 \times 2.5$, linear factor).", 40)
    assert F(44, 4) == 11 and 11 * 11 == 121 and F(44, 2) * F(7, 22) == 7 and F(22, 7) * 49 == 154 and 154 - 121 == 33
    S.q("m2d-sc-p5", "hard", "A wire $44$ cm long is bent into a square, and an equal wire into a circle. The difference between the areas enclosed (take $\\pi = 22/7$) is:",
        ["$33$ sq cm", "$11$ sq cm", "$44$ sq cm", "$22$ sq cm"], "$33$ sq cm",
        r"""Square: side $11$ → area $121$ sq cm. Circle: $r = \frac{44}{2 \times 22/7} = 7$ → area $154$ sq cm.

Difference $= 154 - 121 = 33$ sq cm.""",
        r"Circle $154$ − square $121$ = $33$. Trap: $11$ (difference of sides/radii, not areas).", 55)
    assert 6 * 6 == 36 and 9 * 9 == 81 and 81 - 36 == 45
    S.q("m2d-sc-p5", "medium", "Two squares have perimeters $24$ cm and $36$ cm. The difference of their areas is:",
        ["$45$ sq cm", "$60$ sq cm", "$12$ sq cm", "$39$ sq cm"], "$45$ sq cm",
        r"""Sides $6$ and $9$; areas $36$ and $81$.

Difference $= 81 - 36 = 45$ sq cm.""",
        r"Sides from perimeters first: $6, 9$ → $81 - 36 = 45$. Trap: $12$ (difference of perimeters squared, $6^2$).", 40)
    return S
