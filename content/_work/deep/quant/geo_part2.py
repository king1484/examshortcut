"""Phase-2 deep content for quant/geometry — pythagoras, quad-poly, circles."""
from fractions import Fraction as F

from _lib import Sub


# ---------------- geo-pythagoras ----------------

def build_pyth():
    S = Sub("geo-pythagoras")

    S.notes = r"""### The theorem and how questions hide it
In a right triangle with the right angle at $C$: $a^2 + b^2 = c^2$, where $c$ is the **hypotenuse** (opposite the right angle — always the longest side). Every "ladder", "pole and wire", "man walks north then east" question is this equation with a story wrapped around it. Draw the right triangle, label the hypotenuse first, then substitute.

### The triplet arsenal (memorise cold)
| Family | Multiples you will meet |
|---|---|
| 3-4-5 | (6,8,10), (9,12,15), (12,16,20), (15,20,25), (18,24,30), (21,28,35) |
| 5-12-13 | (10,24,26), (15,36,39), (20,48,52) |
| 8-15-17 | (16,30,34) |
| 7-24-25 | (14,48,50) |
| 9-40-41, 20-21-29, 12-35-37, 28-45-53 | as-is |

A question saying "hypotenuse 26, one side 10" is really (10, 24, 26) — recognise the family and the third side appears without any squaring. Check leg ratios like $\frac{3}{4}$, $\frac{5}{12}$, $\frac{8}{15}$ for the same reason. Micro-example: diagonal 65 with one side 25 is the 5-12-13 family times 5, so the other side is 60 instantly. When the sides don't fit a family, square honestly — but always subtract the smaller square from the larger for a missing leg, and add them for a missing hypotenuse; writing the wrong direction is the most common slip in a rush.

### The converse (and the obtuse/acute test)
If $a^2 + b^2 = c^2$, the triangle is right-angled **at the side facing $c$**. If $a^2 + b^2 < c^2$, it is obtuse; if $a^2+b^2 > c^2$, acute. Classification questions are one comparison away — compute both squares, compare, name the triangle.

### Two formulas built on Pythagoras
- **Median to the hypotenuse** $= \frac{c}{2}$ — the right-angle vertex sits on the circle with the hypotenuse as diameter, so the hypotenuse midpoint is equidistant from all three vertices. Asked constantly, almost free.
- **Rectangle/square diagonals**: diagonal of $l \times b$ is $\sqrt{l^2+b^2}$; diagonal of a square of side $a$ is $a\sqrt{2}$, and diagonal $d$ gives side $= \frac{d}{\sqrt2}$.

### Standard question shells
- **Ladder**: length is the hypotenuse; wall height and ground distance are the legs.
- **Two poles with a rope/crow between tops**: horizontal gap is one leg, difference of heights is the other.
- **Displacement**: north-then-east legs; shortest distance back is the hypotenuse.
- **Diagonal of a field/room**: one leg known, diagonal known → other leg.

### Quick revision
- $a^2+b^2=c^2$; hypotenuse is opposite the right angle.
- Triplet families 3-4-5, 5-12-13, 8-15-17, 7-24-25 (+ multiples) — spot, don't compute.
- Converse: equality → right; $a^2+b^2<c^2$ → obtuse; $>$ → acute.
- Median to hypotenuse $= \frac{c}{2}$.
- Rectangle diagonal $\sqrt{l^2+b^2}$; square diagonal $a\sqrt2$.
"""

    S.pattern("geo-py-p1", "Ladder / two-leg Pythagoras stories", "very common",
        "A ladder against a wall, a pole with a guy-wire, walking north then east — any right-triangle story where the hypotenuse (or a leg) is missing.",
        r"a^2 + b^2 = c^2",
        r"""1. Draw the right triangle; the ladder/wire/displacement is the hypotenuse.
2. Identify the two knowns; the unknown is a leg ($\sqrt{c^2-a^2}$) or the hypotenuse ($\sqrt{a^2+b^2}$).
3. Match against a triplet family to skip the arithmetic.

Why: every shell is the same equation; only the story changes which side is which.""",
        "A 17 m ladder leans against a wall with its foot 8 m from the base. How high up the wall does it reach?",
        r"Leg $= \sqrt{17^2 - 8^2} = \sqrt{225} = 15$ m — the 8-15-17 family.")
    S.pattern("geo-py-p2", "Converse: classify the triangle", "common",
        "Three sides are given and the triangle must be identified as right/obtuse/acute, or 'is it right-angled?' is asked.",
        r"a^2 + b^2 \; \lessgtr \; c^2",
        r"""1. Square the two smaller sides; add.
2. Compare with the square of the largest side.
3. Equal → right; smaller → obtuse; larger → acute.

Why: the theorem is an if-and-only-if, so the inequality direction classifies the angle facing the longest side.""",
        "Sides 9 cm, 12 cm and 15 cm: what type of triangle is formed?",
        r"$9^2 + 12^2 = 81 + 144 = 225 = 15^2$ → right-angled (3-4-5 $\times 3$).")
    S.pattern("geo-py-p3", "Median to the hypotenuse", "common",
        "A median from the right angle (or to the hypotenuse) is mentioned; its length or the hypotenuse is asked.",
        r"m_c = \frac{c}{2}",
        r"""1. Right triangle + median to hypotenuse → the median is half the hypotenuse.
2. From the median, double for the hypotenuse; then Pythagoras gives any leg.

Why: the right-angle vertex lies on the circle whose diameter is the hypotenuse, and the circumcentre (hypotenuse midpoint) is equidistant from all three vertices.""",
        "In a right triangle the median drawn to the hypotenuse is $6.5$ cm. The hypotenuse is:",
        r"$c = 2 \times 6.5 = 13$ cm (a 5-12-13 hypotenuse, in fact).")
    S.pattern("geo-py-p4", "Rectangle and square diagonals", "very common",
        "Diagonal of a rectangle/field/room with one dimension missing, or a square's side from its diagonal.",
        r"d = \sqrt{l^2 + b^2};\quad a = \frac{d}{\sqrt{2}}",
        r"""1. The diagonal splits the rectangle into two right triangles — apply $a^2+b^2=c^2$.
2. Missing dimension: $\sqrt{d^2 - \text{known}^2}$.
3. Square: side $= \frac{d}{\sqrt2}$, or use the 1-1-$\sqrt2$ shape.

Why: the corner angles of a rectangle are right angles, so the diagonal is literally a hypotenuse.""",
        "The diagonal of a rectangular field is $65$ m and one side is $25$ m. The other side is:",
        r"$\sqrt{65^2 - 25^2} = \sqrt{4225 - 625} = \sqrt{3600} = 60$ m — the 25-60-65 family ($5\text{-}12\text{-}13 \times 5$).")
    S.pattern("geo-py-p5", "Triplet families in disguise", "common",
        "A ratio of legs ($3:4$, $5:12$…) with the hypotenuse given, or hypotenuse + one leg with area/perimeter asked.",
        r"(3k, 4k, 5k)",
        r"""1. Spot the family in the ratio or the given pair (e.g. 10 & 26 → 5-12-13 ×2).
2. Find $k$; write all three sides.
3. Answer the actual ask — perimeter, area, or the missing side.

Why: exam numbers almost always come from these families; recognising them turns a 60-second calculation into a 10-second recall.""",
        "The legs of a right triangle are in the ratio $3:4$ and the hypotenuse is $20$ cm. Its perimeter is:",
        r"Legs $3k, 4k$ with $5k = 20 \Rightarrow k = 4$: legs $12$ and $16$; perimeter $= 12+16+20 = 48$ cm.")

    # ---- practice ----
    assert 17 ** 2 - 8 ** 2 == 15 ** 2
    S.q("geo-py-p1", "easy", "A ladder $17$ m long leans against a vertical wall, its foot $8$ m from the base of the wall. How high does the ladder reach?",
        ["$15$ m", "$12$ m", "$13$ m", "$16$ m"], "$15$ m",
        r"""Height $= \sqrt{17^2 - 8^2} = \sqrt{289-64} = \sqrt{225} = 15$ m.""",
        r"8-15-17 family: $15$ m. Trap: $13$ m (grabbed the 5-12-13 family).", 35)
    assert 11 - 6 == 5 and 12 ** 2 + 5 ** 2 == 169
    S.q("geo-py-p1", "medium", "Two vertical poles of heights $6$ m and $11$ m stand $12$ m apart on level ground. The distance between their tops is:",
        ["$13$ m", "$14$ m", "$12.5$ m", "$17$ m"], "$13$ m",
        r"""Horizontal gap $12$ m, height difference $11-6 = 5$ m.

Distance $= \sqrt{12^2 + 5^2} = \sqrt{169} = 13$ m.""",
        r"Legs are (gap, height difference) $= (12, 5)$ → $13$ m. Trap: $17$ m (added heights).", 45)
    assert 9 ** 2 + 12 ** 2 == 225
    S.q("geo-py-p1", "medium", "A man walks $9$ m due north, then $12$ m due east. His shortest distance from the starting point is:",
        ["$21$ m", "$15$ m", "$13$ m", "$10.5$ m"], "$15$ m",
        r"""North and east legs are perpendicular: $\sqrt{9^2 + 12^2} = \sqrt{225} = 15$ m.""",
        r"9-12-15 = 3-4-5 ×3 → $15$ m. Trap: $21$ m (9+12, walking back along the path).", 35)
    assert 9 ** 2 + 12 ** 2 == 15 ** 2
    S.q("geo-py-p2", "easy", "Which of the following sets of sides forms a right-angled triangle?",
        ["$8, 13, 15$", "$9, 12, 15$", "$7, 12, 14$", "$6, 11, 13$"], "$9, 12, 15$",
        r"""$9^2 + 12^2 = 81 + 144 = 225 = 15^2$ ✓ (3-4-5 ×3).

The others fail: e.g. $8^2+13^2=233 \neq 225$.""",
        r"Test $a^2+b^2=c^2$; only $9,12,15$ satisfies it.", 35)
    assert 7 ** 2 + 9 ** 2 == 130 and 130 < 169
    S.q("geo-py-p2", "medium", "A triangle has sides $7$ cm, $9$ cm and $13$ cm. It is:",
        ["right-angled", "obtuse-angled", "acute-angled", "equilateral"], "obtuse-angled",
        r"""$7^2 + 9^2 = 49 + 81 = 130 < 13^2 = 169$.

The sum falls short, so the angle facing $13$ is obtuse.""",
        r"$130 < 169$ → obtuse. Trap: calling it right-angled without checking the inequality direction.", 40)
    assert 2 * 6.5 == 13
    S.q("geo-py-p3", "medium", "In a right-angled triangle, the median drawn from the right-angle vertex to the hypotenuse is $6.5$ cm. The length of the hypotenuse is:",
        ["$13$ cm", "$12$ cm", "$3.25$ cm", "$26$ cm"], "$13$ cm",
        r"""Median to the hypotenuse $= \frac{c}{2}$, so $c = 2 \times 6.5 = 13$ cm.""",
        r"$2 \times 6.5 = 13$ cm. Trap: $3.25$ (halved instead of doubled).", 40)
    assert 8 ** 2 + 15 ** 2 == 289
    S.q("geo-py-p3", "hard", "A right triangle has legs $8$ cm and $15$ cm. The length of the median from the right angle to the hypotenuse is:",
        ["$8.5$ cm", "$9$ cm", "$8$ cm", "$7.5$ cm"], "$8.5$ cm",
        r"""Hypotenuse $= \sqrt{64+225} = \sqrt{289} = 17$ cm.

Median to the hypotenuse $= \frac{17}{2} = 8.5$ cm.""",
        r"$c = 17$ (8-15-17), median $= \frac{17}{2} = 8.5$ cm. Trap: $9$ — it is exactly half of 17.", 50)
    assert 12 ** 2 + 16 ** 2 == 400
    S.q("geo-py-p4", "easy", "A rectangle is $12$ cm long and $16$ cm wide. The length of its diagonal is:",
        ["$20$ cm", "$28$ cm", "$18$ cm", "$22$ cm"], "$20$ cm",
        r"""$\sqrt{12^2 + 16^2} = \sqrt{400} = 20$ cm (3-4-5 ×4).""",
        r"$12\text{-}16\text{-}20$ family → $20$ cm. Trap: $28$ ($12+16$).", 30)
    assert 65 ** 2 - 25 ** 2 == 3600 and 60 ** 2 == 3600
    S.q("geo-py-p4", "medium", "The diagonal of a rectangular field is $65$ m and one of its sides is $25$ m. The other side is:",
        ["$60$ m", "$55$ m", "$40$ m", "$52$ m"], "$60$ m",
        r"""$\sqrt{65^2 - 25^2} = \sqrt{4225 - 625} = \sqrt{3600} = 60$ m.""",
        r"25-60-65 is 5-12-13 ×5 → $60$ m. Trap: $55$ ($65-10$, no squaring).", 40)
    assert 12 + 16 + 20 == 48 and F(12, 16) == F(3, 4)
    S.q("geo-py-p5", "easy", "The legs of a right triangle are in the ratio $3:4$ and the hypotenuse is $20$ cm. The perimeter of the triangle is:",
        ["$40$ cm", "$48$ cm", "$52$ cm", "$36$ cm"], "$48$ cm",
        r"""$5k = 20 \Rightarrow k = 4$: legs $12$ cm and $16$ cm.

Perimeter $= 12+16+20 = 48$ cm.""",
        r"$k=4$; $12k = 48$ cm. Trap: $52$ (legs $12+16$ plus $24$).", 35)
    assert 26 ** 2 - 10 ** 2 == 576 and 24 ** 2 == 576 and F(1, 2) * 10 * 24 == 120
    S.q("geo-py-p5", "hard", "The hypotenuse of a right triangle is $26$ cm and one leg is $10$ cm. The area of the triangle is:",
        ["$120$ sq cm", "$130$ sq cm", "$240$ sq cm", "$96$ sq cm"], "$120$ sq cm",
        r"""Other leg $= \sqrt{26^2 - 10^2} = \sqrt{576} = 24$ cm (10-24-26 = 5-12-13 ×2).

Area $= \frac12 \times 10 \times 24 = 120$ sq cm.""",
        r"Missing leg $24$; $\frac12 \times 240 = 120$. Trap: $130$ ($\frac12 \times 10 \times 26$ used the hypotenuse as a leg).", 50)
    return S


# ---------------- geo-quad-poly ----------------

def build_quadpoly():
    S = Sub("geo-quad-poly")

    S.notes = r"""### The polygon angle toolkit (all of it is two formulas)
For a regular polygon of $n$ sides: each **exterior** angle $= \frac{360^\circ}{n}$, and each **interior** angle $= 180^\circ - \text{exterior} = \frac{(n-2) \times 180^\circ}{n}$.
Total interior sum $= (n-2) \times 180^\circ$; sum of exterior angles (any polygon) $= 360^\circ$.
Number of diagonals $= \frac{n(n-3)}{2}$.
Almost every polygon question is: given one quantity (interior angle, exterior angle, sum, diagonals), recover $n$. Work through the exterior angle — it is the fastest hub: interior $150^\circ$ → ext $30^\circ$ → $n = 12$.

### Parallelogram family
- **Parallelogram**: opposite sides parallel and equal; diagonals bisect each other; **adjacent angles are supplementary**, opposite angles equal. If $\angle A = k\angle B$, then $k\angle B + \angle B = 180^\circ$.
- **Rectangle**: parallelogram + all $90^\circ$; diagonals equal and bisect each other.
- **Rhombus**: parallelogram + all sides equal; diagonals **bisect at $90^\circ$** (not equal). Side $= \sqrt{\left(\frac{d_1}{2}\right)^2 + \left(\frac{d_2}{2}\right)^2}$; area $= \frac12 d_1 d_2$.
- **Square**: all of the above; diagonal $= a\sqrt2$.
- **Trapezium**: one pair of parallel sides $a, b$; area $= \frac12 (a+b)h$; the segment joining the midpoints of the non-parallel sides (midsegment) $= \frac{a+b}{2}$.

### Cyclic quadrilaterals
All four vertices on one circle → **opposite angles are supplementary**: $\angle A + \angle C = \angle B + \angle D = 180^\circ$. Ratio questions: the opposite pairs' ratio parts must each total the same count (e.g. $2:3:4:3$ works since $2+4 = 3+3 = 6$); solve $k$ from $180^\circ$, then answer the asked angle. The exterior angle of a cyclic quad equals the interior opposite angle — the same fact re-stated.

### The two standard computation shells
1. **Rhombus from diagonals**: halves of the diagonals form a right triangle with the side as hypotenuse — a triplet family in half-size. E.g. diagonals 10, 24 → halves 5, 12 → side 13.
2. **Rhombus area ↔ diagonal**: area $= \frac12 d_1 d_2$ gives the missing diagonal, then the side from the halves.

### Quick revision
- Regular $n$: ext $= \frac{360}{n}^\circ$, interior $= 180 - $ ext; sum $= (n-2) \times 180^\circ$; diagonals $= \frac{n(n-3)}{2}$.
- Parallelogram: adjacent angles sum to $180^\circ$; opposite angles equal.
- Rhombus: side $= \sqrt{(\frac{d_1}{2})^2 + (\frac{d_2}{2})^2}$; area $= \frac12 d_1 d_2$; diagonals ⊥ bisect.
- Cyclic quad: opposite angles sum to $180^\circ$.
- Trapezium area $= \frac12 (a+b)h$; midsegment $= \frac{a+b}{2}$.
"""

    S.pattern("geo-qp-p1", "Regular polygon: angle ↔ number of sides", "very common",
        "A regular polygon's interior/exterior angle, angle sum, or diagonal count is given — find $n$ (or another of these).",
        r"\text{ext} = \frac{360^\circ}{n},\quad \text{int} = 180^\circ - \text{ext},\quad d = \frac{n(n-3)}{2}",
        r"""1. Convert the given interior angle to exterior: $180^\circ - $ interior.
2. $n = \frac{360^\circ}{\text{ext}}$; or from the sum, $n = \frac{\text{sum}}{180^\circ} + 2$; or solve $d = \frac{n(n-3)}{2}$.
3. Answer what was asked — sometimes it is another angle, not $n$.

Why: all polygon quantities are functions of $n$, and the exterior angle is the quickest bridge between them.""",
        "Each interior angle of a regular polygon is $150^\\circ$. How many sides has it?",
        r"Exterior $= 180 - 150 = 30^\circ$; $n = \frac{360}{30} = 12$.")
    S.pattern("geo-qp-p2", "Rhombus from its diagonals", "very common",
        "Diagonals of a rhombus given (or area + one diagonal) — side, perimeter, or the other diagonal asked.",
        r"s = \sqrt{\left(\frac{d_1}{2}\right)^2 + \left(\frac{d_2}{2}\right)^2},\quad K = \frac{d_1 d_2}{2}",
        r"""1. Halve both diagonals; they form a right triangle whose hypotenuse is the side.
2. Spot the half-size triplet: diagonals 10, 24 → 5-12-13 → side 13.
3. Area given instead? $d_2 = \frac{2K}{d_1}$ first, then the side.

Why: diagonals of a rhombus bisect at right angles — the geometry is literally Pythagoras with half-diagonals.""",
        "The diagonals of a rhombus are $10$ cm and $24$ cm. Its perimeter is:",
        r"Half-diagonals $5, 12$ → side $= 13$; perimeter $= 4 \times 13 = 52$ cm.")
    S.pattern("geo-qp-p3", "Parallelogram angles (adjacent supplementary)", "very common",
        "Adjacent angles of a parallelogram are given as a ratio or as $\\angle A = k\\angle B$ — find one angle, or an opposite/related one.",
        r"\angle A + \angle B = 180^\circ",
        r"""1. Set the adjacent relation: ratio $a:b$ → angles $\frac{a}{a+b} \times 180^\circ$ and $\frac{b}{a+b} \times 180^\circ$.
2. Opposite angles equal the ones found; adjacent differ by $180^\circ -$.
3. Read the letter asked — opposite vs adjacent flips the answer.

Why: a pair of parallel sides makes each pair of adjacent angles co-interior, hence supplementary.""",
        "Two adjacent angles of a parallelogram are in the ratio $1:3$. The larger angle is:",
        r"$\frac{3}{4} \times 180^\circ = 135^\circ$ (the smaller is $45^\circ$).")
    S.pattern("geo-qp-p4", "Cyclic quadrilateral opposite angles", "common",
        "Four vertices on a circle; one angle or the ratio of angles given — a missing angle asked.",
        r"\angle A + \angle C = \angle B + \angle D = 180^\circ",
        r"""1. Identify the opposite pair of the given angle; subtract from $180^\circ$.
2. For ratios, check which ratio parts form opposite pairs; each pair sums to $180^\circ$.
3. The exterior angle at one vertex equals the interior opposite angle — a shortcut when a side is produced.

Why: opposite angles of a cyclic quad subtend complementary arcs totalling the full circle, so the inscribed angles sum to $180^\circ$.""",
        "In a cyclic quadrilateral $ABCD$, $\\angle A = 70^\\circ$. The angle $\\angle C$ is:",
        r"$\angle C = 180^\circ - 70^\circ = 110^\circ$ ($A$ and $C$ are opposite).")
    S.pattern("geo-qp-p5", "Trapezium area and midsegment", "common",
        "Parallel sides and height given (or area + parallel sides) — area, height, or the midsegment asked.",
        r"K = \frac{1}{2}(a+b)h,\quad m = \frac{a+b}{2}",
        r"""1. Add the parallel sides; halve; multiply by height for the area.
2. Height from area: $h = \frac{2K}{a+b}$.
3. Midsegment (midpoints of the slanted sides) is just $\frac{a+b}{2}$ — no height needed.

Why: a trapezium is the average of its parallel sides times the height — the triangle-and-rectangle split proves it.""",
        "A trapezium has parallel sides $13$ cm and $17$ cm and area $105$ sq cm. Its height is:",
        r"$h = \frac{2 \times 105}{13+17} = \frac{210}{30} = 7$ cm.")

    # ---- practice ----
    assert 360 // 30 == 12 and 180 - 150 == 30
    S.q("geo-qp-p1", "easy", "Each interior angle of a regular polygon is $150^\\circ$. The number of sides of the polygon is:",
        ["$10$", "$12$", "$15$", "$8$"], "$12$",
        r"""Exterior angle $= 180^\circ - 150^\circ = 30^\circ$; $n = \frac{360^\circ}{30^\circ} = 12$.""",
        r"$\frac{360}{30} = 12$. Trap: $15$ — that came from forgetting interior + exterior $= 180^\circ$.", 35)
    assert (8 - 2) * 180 == 1080
    S.q("geo-qp-p1", "medium", "The sum of the interior angles of a regular polygon is $1080^\\circ$. Each exterior angle of the polygon is:",
        ["$60^\\circ$", "$45^\\circ$", "$40^\\circ$", "$30^\\circ$"], "$45^\\circ$",
        r"""$n = \frac{1080}{180} + 2 = 8$ sides.

Exterior angle $= \frac{360^\circ}{8} = 45^\circ$ (interior $135^\circ$).""",
        r"$n = 8$; ext $= \frac{360}{8} = 45^\circ$. Trap: $135^\circ$ — that is the interior.", 40)
    assert 5 ** 2 + 12 ** 2 == 169 and 4 * 13 == 52
    S.q("geo-qp-p2", "medium", "The diagonals of a rhombus are $10$ cm and $24$ cm. The perimeter of the rhombus is:",
        ["$52$ cm", "$48$ cm", "$68$ cm", "$44$ cm"], "$52$ cm",
        r"""Half-diagonals $5$ and $12$; side $= \sqrt{25 + 144} = 13$ cm.

Perimeter $= 4 \times 13 = 52$ cm.""",
        r"5-12-13 in halves → side 13 → $52$ cm. Trap: $68$ (mis-halved the diagonals).", 45)
    assert F(1, 2) * 12 * 16 == 96 and 6 ** 2 + 8 ** 2 == 100
    S.q("geo-qp-p2", "hard", "The area of a rhombus is $96$ sq cm and one diagonal is $12$ cm. The perimeter of the rhombus is:",
        ["$40$ cm", "$44$ cm", "$48$ cm", "$36$ cm"], "$40$ cm",
        r"""$\frac12 \times 12 \times d_2 = 96 \Rightarrow d_2 = 16$ cm.

Half-diagonals $6, 8$ → side $= 10$ cm → perimeter $40$ cm.""",
        r"$d_2 = \frac{2 \times 96}{12} = 16$; 6-8-10 → $40$ cm. Trap: $48$ (side $12$ from one full diagonal).", 55)
    assert F(3, 4) * 180 == 135 and F(1, 4) * 180 == 45
    S.q("geo-qp-p3", "easy", "Two adjacent angles of a parallelogram are in the ratio $1:3$. The larger angle measures:",
        ["$120^\\circ$", "$135^\\circ$", "$150^\\circ$", "$100^\\circ$"], "$135^\\circ$",
        r"""Adjacent angles sum to $180^\circ$: larger $= \frac{3}{4} \times 180^\circ = 135^\circ$ (smaller $45^\circ$).""",
        r"$\frac{3}{1+3} \times 180 = 135^\circ$. Trap: $120^\circ$ (ratio taken against the wrong total).", 35)
    assert 120 + 60 == 180
    S.q("geo-qp-p3", "medium", "In parallelogram $ABCD$, $\\angle A = 2\\angle B$. The measure of $\\angle C$ is:",
        ["$60^\\circ$", "$90^\\circ$", "$120^\\circ$", "$135^\\circ$"], "$120^\\circ$",
        r"""$\angle A + \angle B = 180^\circ \Rightarrow 3\angle B = 180^\circ \Rightarrow \angle B = 60^\circ$, $\angle A = 120^\circ$.

$\angle C = \angle A = 120^\circ$ (opposite angles equal).""",
        r"$\angle B = 60^\circ$, so $\angle C = \angle A = 120^\circ$. Trap: $60^\circ$ — that is $\angle B$ and $\angle D$.", 40)
    assert 180 - 70 == 110
    S.q("geo-qp-p4", "medium", "$ABCD$ is a cyclic quadrilateral and $\\angle A = 70^\\circ$. The measure of $\\angle C$ is:",
        ["$110^\\circ$", "$70^\\circ$", "$20^\\circ$", "$100^\\circ$"], "$110^\\circ$",
        r"""Opposite angles of a cyclic quadrilateral are supplementary: $\angle C = 180^\circ - 70^\circ = 110^\circ$.""",
        r"$180 - 70 = 110^\circ$. Trap: $70^\circ$ (opposite angles are NOT equal — that is parallelograms).", 35)
    assert 2 + 4 == 6 and 3 + 3 == 6 and 6 * 30 == 180 and max(60, 90, 120, 90) == 120
    S.q("geo-qp-p4", "hard", "The angles of a cyclic quadrilateral are in the ratio $2:3:4:3$ (in order). The largest angle of the quadrilateral is:",
        ["$120^\\circ$", "$90^\\circ$", "$100^\\circ$", "$135^\\circ$"], "$120^\\circ$",
        r"""Opposite pairs must each sum to $180^\circ$: parts $2+4 = 6$ and $3+3 = 6$ ✓, so $6k = 180 \Rightarrow k = 30^\circ$.

Angles $60^\circ, 90^\circ, 120^\circ, 90^\circ$ — largest $120^\circ$.""",
        r"$k = \frac{180}{6} = 30$; largest part is $4k = 120^\circ$. Trap: $135^\circ$ (those parts don't close a cyclic quad).", 55)
    assert F(1, 2) * 30 * 8 == 120
    S.q("geo-qp-p5", "medium", "A trapezium has parallel sides of $12$ cm and $18$ cm and the perpendicular distance between them is $8$ cm. Its area is:",
        ["$120$ sq cm", "$144$ sq cm", "$96$ sq cm", "$150$ sq cm"], "$120$ sq cm",
        r"""Area $= \frac12 (12 + 18) \times 8 = \frac12 \times 30 \times 8 = 120$ sq cm.""",
        r"$15 \times 8 = 120$. Trap: $144$ (used one parallel side × height).", 40)
    assert F(2 * 105, 30) == 7
    S.q("geo-qp-p5", "medium", "The area of a trapezium is $105$ sq cm and its parallel sides measure $13$ cm and $17$ cm. Its height is:",
        ["$7$ cm", "$6$ cm", "$8$ cm", "$7.5$ cm"], "$7$ cm",
        r"""$\frac12 \times 30 \times h = 105 \Rightarrow h = \frac{210}{30} = 7$ cm.""",
        r"$h = \frac{2 \times 105}{30} = 7$ cm. Trap: $3.5$ (forgot to double the area).", 40)
    return S


# ---------------- geo-circles ----------------

def build_circles():
    S = Sub("geo-circles")

    S.notes = r"""### Chord, distance, right triangle
A perpendicular from the centre to a chord **bisects** it. So radius $r$, distance $d$ from centre, and half-chord form a right triangle:
$$\left(\frac{c}{2}\right)^2 + d^2 = r^2$$
Two chords are equal iff they are equidistant from the centre; longer chords sit closer to the centre. Every chord question is: given two of $\left(\frac{c}{2}, d, r\right)$, get the third — usually a half-size triplet (chord 24, $d$ 9, $r$ 15 → 9-12-15).

### Tangent and secant power facts
- Tangent ⊥ radius at the point of contact; tangents from an external point are **equal**.
- **Tangent–secant**: $\text{tangent}^2 = \text{external part} \times \text{whole secant}$.
- **Intersecting chords** (inside): the products of the parts are equal: $a \times b = c \times d$.
These 'power of a point' identities answer two-step questions in one line each. Micro-example: tangent 10, external secant part 5 → whole secant $= \frac{10^2}{5} = 20$, internal part 15. The equal-tangents fact also drives the 'two tangents from P, find the perimeter of the small triangle' shells: both tangent lengths are equal, so the perimeter is just twice one tangent plus the chord.

### Where the 90 degrees come from
The chord theorem, the tangent-radius perpendicular, and the semicircle angle are all Pythagoras or Thales in costume — when a question mixes a chord with an angle at the circumference, first convert the angle to a centre angle (double it), because the centre angle tells you the arc, and the arc tells you where the chord sits.

### Counting common tangents
For two circles with radii $r_1 \ge r_2$, centre distance $d$:
| Configuration | Common tangents |
|---|---|
| Separate ($d > r_1 + r_2$) | 4 (2 direct + 2 transverse) |
| Externally tangent ($d = r_1 + r_2$) | 3 |
| Intersecting ($|r_1 - r_2| < d < r_1+r_2$) | 2 |
| Internally tangent ($d = r_1 - r_2$) | 1 |
| One inside the other ($d < r_1 - r_2$) | 0 |

Memorise the countdown 4-3-2-1-0 against the configuration — the question is only 'which case?'.

### Angles in circles
- Angle at the centre $= 2 \times$ angle at the circumference on the same arc: $\angle BOC = 2\angle BAC$.
- Angles in the **same segment** are equal.
- **Angle in a semicircle is $90^\circ$** (diameter as one side).
- Cyclic quadrilateral: opposite angles supplementary (details in the quad subtopic).
- Equal chords subtend equal angles at the centre.

### Quick revision
- $\left(\frac{c}{2}\right)^2 + d^2 = r^2$ — perpendicular from centre bisects the chord.
- Tangent$^2$ = external × whole secant; $a\cdot b = c \cdot d$ for crossing chords.
- Common tangents: separate 4, external touch 3, intersecting 2, internal touch 1, nested 0.
- $\angle BOC = 2\angle BAC$; same segment equal; semicircle $90^\circ$.
- Tangents from an external point are equal; tangent ⊥ radius.
"""

    S.pattern("geo-ci-p1", "Chord–distance–radius right triangle", "very common",
        "A chord's length, the radius, or its distance from the centre is missing; 'perpendicular from the centre' is stated or implied.",
        r"\left(\frac{c}{2}\right)^2 + d^2 = r^2",
        r"""1. Halve the chord — the perpendicular from the centre bisects it.
2. Apply Pythagoras with $r$ as hypotenuse.
3. Watch for half-size triplets: (9,12,15), (8,15,17), (5,12,13).

Why: the perpendicular-to-chord theorem plus Pythagoras is the whole mechanism; only the missing slot changes.""",
        "A circle of radius $15$ cm has a chord $9$ cm from the centre. The length of the chord is:",
        r"Half-chord $= \sqrt{15^2 - 9^2} = \sqrt{144} = 12$; chord $= 24$ cm (9-12-15).")
    S.pattern("geo-ci-p2", "Tangent–secant and intersecting chords", "common",
        "A tangent and a secant from an external point, or two chords crossing inside the circle, with segment lengths given/asked.",
        r"t^2 = a \cdot (a + b),\quad a b = c d",
        r"""1. External point: square the tangent; equate to external part × WHOLE secant.
2. Inside crossing: equate the products of the two pairs of parts.
3. Solve the single resulting equation; answer the exact segment asked.

Why: both are the same 'power of a point' — the product of distances along any line through the point is constant.""",
        "From an external point $P$, a tangent of length $10$ cm and a secant are drawn. If the external part of the secant is $5$ cm, the whole secant is:",
        r"$10^2 = 5 \times \text{whole} \Rightarrow$ whole $= 20$ cm (internal part $15$ cm).")
    S.pattern("geo-ci-p3", "Counting common tangents", "common",
        "Two circles with given radii and centre distance — 'how many common tangents?'",
        r"d \gtrless r_1 + r_2,\quad d \gtrless r_1 - r_2",
        r"""1. Compare $d$ with $r_1 + r_2$ and $r_1 - r_2$.
2. Map to the case: $d > r_1{+}r_2$ → 4; equal → 3; between → 2; $d = r_1 - r_2$ → 1; less → 0.

Why: transverse tangents exist only when the circles don't overlap; each threshold (touching outside, overlapping, touching inside) removes tangents one at a time.""",
        "Two circles of radii $6$ cm and $2$ cm have centres $4$ cm apart. The number of common tangents is:",
        r"$d = 4 = 6 - 2$: internally tangent → exactly $1$ common tangent.")
    S.pattern("geo-ci-p4", "Centre angle vs circumference angle", "very common",
        "$O$ is the centre; an angle at the centre or at the circumference on the same arc is given — find the other, or use a semicircle.",
        r"\angle BOC = 2\angle BAC",
        r"""1. Confirm both angles subtend the SAME arc (or chord).
2. Centre angle $= 2 \times$ circumference angle; same-segment angles are equal.
3. Diameter side → angle in the semicircle is $90^\circ$ instantly.

Why: the inscribed angle holds half the central angle's arc — Thales' result covers the diameter case.""",
        "In a circle with centre $O$, $\\angle BOC = 120^\\circ$ subtending arc $BC$. The angle $\\angle BAC$ at the circumference is:",
        r"$\angle BAC = \frac{120^\circ}{2} = 60^\circ$.")

    # ---- practice ----
    assert 15 ** 2 - 9 ** 2 == 144
    S.q("geo-ci-p1", "easy", "A circle has radius $15$ cm. A chord is drawn at a distance of $9$ cm from the centre. The length of the chord is:",
        ["$12$ cm", "$24$ cm", "$18$ cm", "$6$ cm"], "$24$ cm",
        r"""Half-chord $= \sqrt{15^2 - 9^2} = \sqrt{144} = 12$ cm; chord $= 2 \times 12 = 24$ cm.""",
        r"9-12-15 in halves → chord $24$ cm. Trap: $12$ cm is the HALF-chord.", 35)
    S.questions[-1]["figure"] = ('<svg viewBox="0 0 220 200" width="220" stroke="currentColor" fill="none">'
        '<circle cx="110" cy="100" r="75"/>'
        '<line x1="110" y1="100" x2="158.9" y2="141.4"/>'
        '<line x1="35" y1="156" x2="185" y2="156"/>'
        '<line x1="110" y1="100" x2="110" y2="156" stroke-dasharray="4 3"/>'
        '<text x="150" y="170" dx="4" dy="12" fill="currentColor" stroke="none" font-size="13" font-family="sans-serif">24</text>'
        '<text x="78" y="132" dx="-6" dy="4" fill="currentColor" stroke="none" font-size="13" font-family="sans-serif">9</text>'
        '</svg>')
    assert 10 ** 2 - 8 ** 2 == 36
    S.q("geo-ci-p1", "medium", "A chord of length $16$ cm is drawn in a circle of radius $10$ cm. Its distance from the centre is:",
        ["$6$ cm", "$8$ cm", "$4$ cm", "$2$ cm"], "$6$ cm",
        r"""Half-chord $8$: $d = \sqrt{10^2 - 8^2} = \sqrt{36} = 6$ cm.""",
        r"$\sqrt{100-64} = 6$ cm. Trap: $8$ cm (the half-chord).", 40)
    assert 10 ** 2 == 5 * 20 and 20 - 5 == 15
    S.q("geo-ci-p2", "medium", "From an external point $P$, a tangent $PT = 10$ cm and a secant $PAB$ are drawn to a circle. If $PA = 5$ cm, the length of the chord $AB$ (the internal part) is:",
        ["$20$ cm", "$15$ cm", "$25$ cm", "$10$ cm"], "$15$ cm",
        r"""$PT^2 = PA \times PB \Rightarrow 100 = 5 \times PB \Rightarrow PB = 20$ cm.

$AB = PB - PA = 20 - 5 = 15$ cm.""",
        r"Whole secant $20$, so internal part $15$ cm. Trap: $20$ cm — that is $PB$, not $AB$.", 45)
    assert 6 * 8 == 4 * 12
    S.q("geo-ci-p2", "hard", "Two chords $AB$ and $CD$ intersect inside a circle at $X$. If $AX = 6$ cm, $XB = 8$ cm and $CX = 4$ cm, the length of $XD$ is:",
        ["$12$ cm", "$10$ cm", "$16$ cm", "$14$ cm"], "$12$ cm",
        r"""Intersecting chords: $AX \cdot XB = CX \cdot XD \Rightarrow 48 = 4 \times XD \Rightarrow XD = 12$ cm.""",
        r"$\frac{6 \times 8}{4} = 12$ cm. Trap: $16$ cm ($4 + 12$, the whole chord).", 50)
    assert 10 > 3 + 5
    S.q("geo-ci-p3", "easy", "Two circles of radii $3$ cm and $5$ cm have their centres $10$ cm apart. The number of common tangents is:",
        ["$3$", "$2$", "$4$", "$1$"], "$4$",
        r"""$d = 10 > 3 + 5 = 8$: the circles are separate → $4$ common tangents ($2$ direct + $2$ transverse).""",
        r"Separate circles → 4 tangents. Trap: 3 — that needs the circles to touch externally.", 35)
    assert 6 - 2 == 4
    S.q("geo-ci-p3", "medium", "Two circles of radii $6$ cm and $2$ cm have centres $4$ cm apart. The number of common tangents to the two circles is:",
        ["$2$", "$3$", "$0$", "$1$"], "$1$",
        r"""$d = 4 = r_1 - r_2 = 6 - 2$: the circles touch internally → exactly $1$ common tangent.""",
        r"Internal touch → 1. Trap: $3$ (external touch needs $d = 8$) or $0$ (nested needs $d < 4$).", 45)
    S.q("geo-ci-p4", "easy", "$AB$ is a diameter of a circle and $C$ is any point on the circle ($C \\neq A, B$). The angle $\\angle ACB$ is:",
        ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$180^\\circ$"], "$90^\\circ$",
        r"""The angle in a semicircle is a right angle (Thales): $\angle ACB = 90^\circ$.""",
        r"Diameter → $90^\circ$, always. Trap: $180^\circ$ (the diameter's own measure at the centre).", 30)
    assert F(120, 2) == 60
    S.q("geo-ci-p4", "medium", "In a circle with centre $O$, the chord $BC$ subtends $\\angle BOC = 120^\\circ$ at the centre. The angle $\\angle BAC$ subtended by the same chord at a point $A$ on the major arc is:",
        ["$120^\\circ$", "$30^\\circ$", "$60^\\circ$", "$90^\\circ$"], "$60^\\circ$",
        r"""Centre angle $= 2 \times$ circumference angle: $\angle BAC = \frac{120^\circ}{2} = 60^\circ$.""",
        r"Halve it: $60^\circ$. Trap: $30^\circ$ (divided twice) or $120^\circ$ (same-segment mix-up).", 35)
    return S
