"""Phase-2 deep content for quant/mensuration-2d — triangles, quads, circles."""
from fractions import Fraction as F

from _lib import Sub

PI = F(22, 7)


# ---------------- m2d-triangles ----------------

def build_triangles():
    S = Sub("m2d-triangles")

    S.notes = r"""### The four area routes (pick by what's given)
- **Base-height**: $K = \frac{1}{2} \times \text{base} \times \text{height}$ — any triangle, when the perpendicular height is known.
- **Equilateral**: $K = \frac{\sqrt{3}}{4}a^2$; also height $= \frac{\sqrt{3}}{2}a$. Reverse: from the area, $a^2 = \frac{4K}{\sqrt{3}}$.
- **Heron (three sides)**: $s = \frac{a+b+c}{2}$, $K = \sqrt{s(s-a)(s-b)(s-c)}$.
- **Right triangle**: $K = \frac{1}{2} \times \text{leg} \times \text{leg}$ — and this doubles as a Heron bypass whenever the sides form a Pythagorean family.

### The Heron bypass (memorised families)
Check for a triplet before touching Heron:
| Family | Area |
|---|---|
| (5,12,13) | 30 |
| (9,12,15) | 54 |
| (10,24,26) | 120 |
| (13,14,15) | 84 |
| (7,24,25) | 84 |
| (13,20,21) | 126 |

If the sides are a multiple of 3-4-5 or 5-12-13, the triangle is right-angled and the area is half the product of the two smaller sides. (13,14,15) is the classic non-right Heron example — its area 84 is worth memorising outright.

### Isosceles triangles
Given equal sides $a$ and base $b$: the height to the base is $h = \sqrt{a^2 - \left(\frac{b}{2}\right)^2}$, then $K = \frac{1}{2}bh$. These are engineered to give Pythagorean halves: (13,13,10) → h 12, K 60; (17,17,16) → h 15, K 120; (25,25,14) → h 24, K 168; (10,10,12) → h 8, K 48.

### Area links inside the triangle
- **Inradius**: $K = r \cdot s$, so $r = \frac{K}{s}$. For (13,14,15): $r = \frac{84}{21} = 4$.
- **A median divides the triangle into two equal areas** (same base halves, same height). A centroid therefore creates 6 triangles of equal area.
- **Altitude to the hypotenuse**: $\frac{1}{2}ab = \frac{1}{2}ch$ gives $h = \frac{ab}{c}$ for legs $a,b$ and hypotenuse $c$ — (6,8,10) → $h = 4.8$.

### How the questions combine these
A typical CGL question chains two of the routes: sides given → area via the triplet bypass → then inradius $r = K/s$; or isosceles sides → height via Pythagoras → area → then a median split halves it. Read the full question once before computing, note the LAST quantity asked, and work backwards from it to choose the shortest route. Unit discipline matters too: mixed units (m with cm) must be converted before any squaring, and answers in $\text{cm}^2$ asked from metre dimensions need the $\times 10^4$ conversion.

### Quick revision
- $K = \frac{1}{2}bh$; equilateral $\frac{\sqrt3}{4}a^2$, height $\frac{\sqrt3}{2}a$.
- Heron: $s$ first, then $\sqrt{s(s-a)(s-b)(s-c)}$; triplet sides → $\frac12 \times$ legs.
- Isosceles: $h = \sqrt{a^2 - (b/2)^2}$; know the (13,13,10), (17,17,16), (25,25,14) shapes.
- $r = K/s$; median halves the area; altitude to hypotenuse $h = \frac{ab}{c}$.
"""

    S.pattern("m2d-tr-p1", "Area from base-height / equilateral formula", "very common",
        "Base and height given directly — or 'equilateral triangle of side a' with area/perimeter/height asked.",
        r"K = \frac{1}{2}bh;\quad K_{\text{eq}} = \frac{\sqrt{3}}{4}a^2",
        r"""1. General triangle: halve the product of base and perpendicular height.
2. Equilateral: $\frac{\sqrt3}{4}a^2$ for area, $\frac{\sqrt3}{2}a$ for height, $3a$ for perimeter.
3. Reverse direction (area given → side) needs $a^2 = \frac{4K}{\sqrt3}$; keep the $\sqrt3$ untouched.

Why: the equilateral formula is just base-height with height forced to $\frac{\sqrt3}{2}a$ by the 60-60-60 angles.""",
        "Find the area of an equilateral triangle of side 12 cm.",
        r"$K = \frac{\sqrt3}{4} \times 12^2 = \frac{\sqrt3}{4} \times 144 = 36\sqrt{3}$ sq cm.")
    S.pattern("m2d-tr-p2", "Heron's formula (and the triplet bypass)", "very common",
        "Three sides given with no height; sides often form a Pythagorean family in disguise.",
        r"K = \sqrt{s(s-a)(s-b)(s-c)},\quad s = \frac{a+b+c}{2}",
        r"""1. Spot a triplet family first — then the triangle is right-angled and $K = \frac12 \times$ legs.
2. Otherwise compute $s$, then the four-factor product, then the root.
3. (13,14,15) → 84 is the standard non-right Heron answer worth knowing cold.

Why: Heron works on any triangle, but exam sides are chosen so either a triplet bypass or a clean square root appears.""",
        "Find the area of the triangle with sides 13 cm, 14 cm and 15 cm.",
        r"$s = 21$; $K = \sqrt{21 \cdot 8 \cdot 7 \cdot 6} = \sqrt{7056} = 84$ sq cm.")
    S.pattern("m2d-tr-p3", "Isosceles triangle area", "common",
        "Equal sides and base given — area asked; the numbers are built for a Pythagorean half-base.",
        r"h = \sqrt{a^2 - (b/2)^2},\quad K = \frac{1}{2}bh",
        r"""1. Halve the base; it is one leg of the right triangle formed by the height.
2. Get $h$ from the equal side as hypotenuse — check for (5,12,13), (8,15,17) halves.
3. Area $= \frac12 \times$ base $\times h$.

Why: the height to the base of an isosceles triangle is also its median, splitting the base into equal halves.""",
        "An isosceles triangle has equal sides of 17 cm and base 16 cm. Its area is:",
        r"$h = \sqrt{17^2 - 8^2} = \sqrt{289-64} = 15$; $K = \frac12 \times 16 \times 15 = 120$ sq cm.")
    S.pattern("m2d-tr-p4", "Inradius and median area-split", "common",
        "'The inradius of a triangle…' with sides given ($r = K/s$), or a median/centroid with the two area pieces asked.",
        r"K = r\,s \ \Rightarrow\ r = \frac{K}{s}",
        r"""1. Find the area first (triplet bypass or Heron).
2. Inradius $r = K/s$ — divide by the SEMI-perimeter, not the perimeter.
3. Median question: a median halves the area (equal base halves, same height).

Why: the incircle touches all three sides, and joining the incentre to the vertices splits the triangle into three triangles of height $r$ — their areas total $r \cdot s$.""",
        "The sides of a triangle are 13, 14 and 15 cm. Its inradius is:",
        r"$K = 84$ (Heron), $s = 21$: $r = \frac{84}{21} = 4$ cm.")
    S.pattern("m2d-tr-p5", "Altitude to the hypotenuse (area two ways)", "occasional",
        "A right triangle with the perpendicular drawn from the right angle to the hypotenuse; that altitude (or the area) is asked.",
        r"\frac{1}{2}ab = \frac{1}{2}ch \ \Rightarrow\ h = \frac{ab}{c}",
        r"""1. Compute the area the easy way: half the product of the legs.
2. The same area equals half × hypotenuse × the altitude to it.
3. So altitude $h = \frac{ab}{c}$; keep it as a fraction if it is not integral.

Why: the two legs and (hypotenuse + altitude) are two base-height pairs of the SAME triangle, so the areas are equal.""",
        "In a right triangle with legs 6 cm and 8 cm, find the length of the altitude drawn to the hypotenuse.",
        r"Hypotenuse $= 10$; area $= \frac12 \cdot 6 \cdot 8 = 24 = \frac12 \cdot 10 \cdot h \Rightarrow h = 4.8$ cm.")

    # ---- practice ----
    assert F(1, 2) * 15 * 8 == 60
    S.q("m2d-tr-p1", "easy", "The base of a triangle is $15$ cm and its corresponding height is $8$ cm. Its area is:",
        ["$60$ sq cm", "$120$ sq cm", "$46$ sq cm", "$70$ sq cm"], "$60$ sq cm",
        r"""$K = \frac12 \times 15 \times 8 = 60$ sq cm.""",
        r"$\frac12 \times 120 = 60$. Trap: $120$ (forgot the half).", 30)
    assert F(1, 4) * 144 == 36
    S.q("m2d-tr-p1", "easy", "The area of an equilateral triangle of side $12$ cm is:",
        ["$36\\sqrt{3}$ sq cm", "$72\\sqrt{3}$ sq cm", "$24\\sqrt{3}$ sq cm", "$48\\sqrt{3}$ sq cm"], "$36\\sqrt{3}$ sq cm",
        r"""$K = \frac{\sqrt3}{4} \times 12^2 = \frac{\sqrt3}{4} \times 144 = 36\sqrt{3}$ sq cm.""",
        r"$\frac{144}{4} = 36$; keep the $\sqrt3$. Trap: $72\sqrt3$ — that is $\frac{\sqrt3}{2}a^2$.", 30)
    assert 4 * 25 == 100 and 3 * 10 == 30
    S.q("m2d-tr-p1", "medium", "The area of an equilateral triangle is $25\\sqrt{3}$ sq cm. Its perimeter is:",
        ["$30$ cm", "$20$ cm", "$15$ cm", "$45$ cm"], "$30$ cm",
        r"""$\frac{\sqrt3}{4}a^2 = 25\sqrt3 \Rightarrow a^2 = 100 \Rightarrow a = 10$ cm.

Perimeter $= 3 \times 10 = 30$ cm.""",
        r"$a^2 = \frac{4K}{\sqrt3} = 100$ → $a = 10$, $P = 30$ cm. Trap: $20$ cm (side doubled, not tripled).", 40)
    assert 21 * 8 * 7 * 6 == 7056 and 84 * 84 == 7056
    S.q("m2d-tr-p2", "medium", "The sides of a triangle are $13$ cm, $14$ cm and $15$ cm. Its area is:",
        ["$70$ sq cm", "$84$ sq cm", "$90$ sq cm", "$78$ sq cm"], "$84$ sq cm",
        r"""$s = \frac{13+14+15}{2} = 21$.

$K = \sqrt{21 \times 8 \times 7 \times 6} = \sqrt{7056} = 84$ sq cm.""",
        r"(13,14,15) → 84, the standard Heron family. Trap: $70$ (wrong factor order).", 45)
    assert F(1, 2) * 10 * 24 == 120
    S.q("m2d-tr-p2", "medium", "The sides of a triangle are $10$ cm, $24$ cm and $26$ cm. Its area is:",
        ["$120$ sq cm", "$130$ sq cm", "$240$ sq cm", "$60$ sq cm"], "$120$ sq cm",
        r"""$10\text{-}24\text{-}26 = 5\text{-}12\text{-}13 \times 2$: right-angled, so skip Heron.

$K = \frac12 \times 10 \times 24 = 120$ sq cm.""",
        r"Triplet bypass: $\frac12 \times 240 = 120$. Trap: $130$ (used the hypotenuse as a leg).", 40)
    assert 17 ** 2 - 8 ** 2 == 225 and F(1, 2) * 16 * 15 == 120
    S.q("m2d-tr-p3", "hard", "An isosceles triangle has equal sides $17$ cm each and base $16$ cm. Its area is:",
        ["$120$ sq cm", "$136$ sq cm", "$110$ sq cm", "$128$ sq cm"], "$120$ sq cm",
        r"""Height $h = \sqrt{17^2 - 8^2} = \sqrt{225} = 15$ cm (8-15-17 halves).

$K = \frac12 \times 16 \times 15 = 120$ sq cm.""",
        r"Half-base 8 → 8-15-17 → $K = 120$. Trap: $136$ ($\frac12 \times 17 \times 16$ used a leg as height).", 50)
    assert 10 ** 2 - 6 ** 2 == 64 and F(1, 2) * 12 * 8 == 48
    S.q("m2d-tr-p3", "medium", "An isosceles triangle has equal sides of $10$ cm and base $12$ cm. Its area is:",
        ["$48$ sq cm", "$60$ sq cm", "$40$ sq cm", "$64$ sq cm"], "$48$ sq cm",
        r"""$h = \sqrt{10^2 - 6^2} = \sqrt{64} = 8$ cm (6-8-10 halves).

$K = \frac12 \times 12 \times 8 = 48$ sq cm.""",
        r"Half-base 6, height 8 → $\frac12 \times 96 = 48$. Trap: $60$ ($\frac12 \times 10 \times 12$).", 45)
    assert F(84, 21) == 4
    S.q("m2d-tr-p4", "medium", "The sides of a triangle are $13$ cm, $14$ cm and $15$ cm. Its inradius is:",
        ["$4$ cm", "$5$ cm", "$3$ cm", "$4.5$ cm"], "$4$ cm",
        r"""Area $= 84$ (Heron), semi-perimeter $s = 21$.

$r = \frac{K}{s} = \frac{84}{21} = 4$ cm.""",
        r"$r = K/s$ with $s$ SEMI-perimeter: $84/21 = 4$. Trap: $2$ cm (divided by the full perimeter 42).", 45)
    assert F(48, 2) == 24
    S.q("m2d-tr-p4", "medium", "$AD$ is a median of $\\triangle ABC$ whose area is $48$ sq cm. The area of $\\triangle ABD$ is:",
        ["$24$ sq cm", "$16$ sq cm", "$32$ sq cm", "$12$ sq cm"], "$24$ sq cm",
        r"""A median splits the triangle into two equal areas (equal base halves $BD = DC$, same height from $A$).

Area of $\triangle ABD = \frac{48}{2} = 24$ sq cm.""",
        r"Median → exactly half: $24$. Trap: $16$/$32$ (centroid $2:1$ applies to LENGTHS, not this split).", 40)
    assert F(6 * 8, 10) == F(24, 5) and F(24, 5) == F(48, 10)
    S.q("m2d-tr-p5", "hard", "In a right triangle with legs $6$ cm and $8$ cm, the altitude drawn from the right angle to the hypotenuse is:",
        ["$4.8$ cm", "$5$ cm", "$4.5$ cm", "$7$ cm"], "$4.8$ cm",
        r"""Hypotenuse $= 10$; area $= \frac12 \cdot 6 \cdot 8 = 24$.

$24 = \frac12 \cdot 10 \cdot h \Rightarrow h = \frac{48}{10} = 4.8$ cm.""",
        r"$h = \frac{ab}{c} = \frac{48}{10} = 4.8$ cm. Trap: $5$ (guessed the midpoint).", 55)
    assert 5 ** 2 + 12 ** 2 == 169 and F(1, 2) * 5 * 12 == 30
    S.q("m2d-tr-p5", "medium", "The hypotenuse of a right triangle is $13$ cm and one leg is $5$ cm. Its area is:",
        ["$32.5$ sq cm", "$30$ sq cm", "$60$ sq cm", "$25$ sq cm"], "$30$ sq cm",
        r"""Other leg $= \sqrt{13^2 - 5^2} = 12$ cm (5-12-13).

$K = \frac12 \times 5 \times 12 = 30$ sq cm.""",
        r"Missing leg 12 → $30$ sq cm. Trap: $32.5$ ($\frac12 \times 5 \times 13$ used the hypotenuse).", 40)
    return S


# ---------------- m2d-quads ----------------

def build_quads():
    S = Sub("m2d-quads")

    S.notes = r"""### Rectangle and square
- Rectangle: $K = l \times b$, $P = 2(l+b)$, diagonal $d = \sqrt{l^2+b^2}$.
- Square: $K = a^2 = \frac{d^2}{2}$, $P = 4a$, $d = a\sqrt2$.
The rectangle questions rarely hand you both $l$ and $b$; they hand two of $\{K, P, d\}$ and expect the pair. The fastest trick: for a rectangle, $d^2 = (l+b)^2 - 2K$, and $d^2 = (l-b)^2 + 2K$ — so from $P$ and $d$ you get $l+b$ and then $K = \left(\frac{l+b}{2}\right)^2 - \left(\frac{d}{2}\right)^2$. Memorised example: $P = 34$, $d = 13$ → $l+b = 17$ → sides 12 and 5 → $K = 60$.

### Rhombus
Diagonals bisect at right angles:
$$K = \frac{1}{2}d_1 d_2,\qquad \text{side} = \sqrt{\left(\frac{d_1}{2}\right)^2 + \left(\frac{d_2}{2}\right)^2},\qquad P = 4 \times \text{side}$$
Half-diagonals are engineered as triplets: (10, 24) → side 13; (16, 12) → side 10. Diagonal-ratio questions: write $d_1 = 5k$, $d_2 = 12k$, put into $K = \frac12 d_1 d_2$, find $k$.

### Parallelogram
$K = \text{base} \times \text{height}$ (height is perpendicular to that base). A second form used when two adjacent sides and the included angle $\theta$ are known: $K = ab\sin\theta$. The $30^\circ$/$150^\circ$ pair ($\sin = \frac12$) is the favourite: sides 10, 8 at $30^\circ$ → $K = 40$.

### Trapezium
$$K = \frac{1}{2}(a+b)\,h$$
Height-from-area: $h = \frac{2K}{a+b}$. If the parallel sides differ by $d$: write them $a$ and $a+d$; then $K = (a + \frac{d}{2})h$ solves for $a$ directly.

### How the questions chain these
Watch the compound shells: a rectangle with $P = 34$ and $d = 13$ needs BOTH the half-perimeter and the diagonal — the triplet (5, 12, 13) finishes it in one glance, while the algebra route $K = \left(\frac{l+b}{2}\right)^2 - \left(\frac{d}{2}\right)^2 = 8.5^2 - 6.5^2 = 60$ works when no triplet fits. For a rhombus the usual chain is three steps: diagonals → side (Pythagoras on the halves) → perimeter ($\times 4$), or area → missing diagonal → side. With a ratio of diagonals, never guess the diagonals themselves — introduce $k$, use the area equation, then finish. Trapezium reverse questions hide the height: from $K$, $a$, $b$ get $h = \frac{2K}{a+b}$, and if the slant sides matter, drop perpendiculars to build a right triangle with half the difference $\frac{b-a}{2}$.

### Quick revision
- Square: $K = \frac{d^2}{2}$; rectangle: $d^2 = (l+b)^2 - 2K$.
- Rhombus: $K = \frac12 d_1d_2$; side from half-diagonal triplet.
- Parallelogram: $bh$ or $ab\sin\theta$ ($30°$ → half).
- Trapezium: $\frac12(a+b)h$; sides differing by $d$: $K = (a + \frac{d}{2})h$.
"""

    S.pattern("m2d-qd-p1", "Rectangle from two of {area, perimeter, diagonal}", "very common",
        "Two of perimeter/diagonal/area given; the missing sides, the area or the perimeter asked.",
        r"d^2 = (l+b)^2 - 2K",
        r"""1. From the perimeter get $l+b$; from the diagonal get $d$.
2. Use $(l-b)^2 = d^2 - (l+b)(l-b)$… fastest is $K = \left(\frac{l+b}{2}\right)^2 - \left(\frac{d}{2}\right)^2$.
3. Or spot the family: $P = 34, d = 13$ → $l+b=17$, and 5-12-13 gives sides 5, 12.

Why: the diagonal and the two sides form a right triangle, and $l+b$ pins the half-perimeter — two facts squeeze out both sides.""",
        "The perimeter of a rectangle is 34 cm and its diagonal is 13 cm. Its area is:",
        r"$l+b = 17$; the 5-12-13 triplet fits ($5+12=17$, diag 13) → $K = 60$ sq cm.")
    S.pattern("m2d-qd-p2", "Rhombus: diagonals ↔ area ↔ perimeter", "very common",
        "Diagonals given (or area + one diagonal, or area + diagonal ratio); side/perimeter/area asked.",
        r"K = \frac{1}{2}d_1 d_2;\quad \text{side} = \sqrt{(d_1/2)^2 + (d_2/2)^2}",
        r"""1. Halve the diagonals; they form a right triangle with the side as hypotenuse.
2. Triplet in halves: (10, 24) → 13; (16, 12) → 10; (48, 14) → 25.
3. Ratio form: set $d_1 = mk$, $d_2 = nk$; feed $\frac12 d_1 d_2 = K$; find $k$; then the side.

Why: diagonals of a rhombus bisect at $90^\circ$ — every rhombus metric is Pythagoras on the quarters.""",
        "The diagonals of a rhombus are in the ratio 5 : 12 and its area is 120 sq cm. Its perimeter is:",
        r"$\frac12 \cdot 5k \cdot 12k = 30k^2 = 120 \Rightarrow k = 2$: diagonals 10, 24 → side 13 → $P = 52$ cm.")
    S.pattern("m2d-qd-p3", "Parallelogram area (base-height or ab·sinθ)", "common",
        "Base and height given — or two adjacent sides with the included angle ($30^\\circ$, $60^\\circ$, $90^\\circ$ favourites).",
        r"K = b\,h = ab\sin\theta",
        r"""1. With a height given: multiply base × height.
2. With sides $a, b$ and angle $\theta$: $K = ab\sin\theta$.
3. Memorise $\sin 30^\circ = \frac12$, $\sin 60^\circ = \frac{\sqrt3}{2}$, $\sin 90^\circ = 1$.

Why: dropping a perpendicular turns the parallelogram into a rectangle of the same base and height $b\sin\theta$.""",
        "Two adjacent sides of a parallelogram are 10 cm and 8 cm and the angle between them is $30^\\circ$. Its area is:",
        r"$K = 10 \times 8 \times \sin 30^\circ = 80 \times \frac12 = 40$ sq cm.")
    S.pattern("m2d-qd-p4", "Square diagonal and trapezium area", "common",
        "A square's diagonal with the area asked ($K = d^2/2$), or a trapezium with parallel sides/height/area mixed.",
        r"K_{\text{sq}} = \frac{d^2}{2};\quad K_{\text{trap}} = \frac{1}{2}(a+b)h",
        r"""1. Square: halve the SQUARE of the diagonal — no $\sqrt2$ gymnastics needed.
2. Trapezium: average the parallel sides, multiply by height.
3. Sides differ by $d$? Write $a, a+d$; then $K = \left(a + \frac{d}{2}\right)h$ solves directly.

Why: the square's diagonal splits it into two right-isosceles triangles of area $\frac{d^2}{4}$ each.""",
        "The parallel sides of a trapezium differ by 8 cm and its height is 6 cm. If its area is 96 sq cm, the longer parallel side is:",
        r"$\frac12(2a+8) \cdot 6 = (a+4) \cdot 6 = 96 \Rightarrow a = 12$; longer side $= 20$ cm.")

    # ---- practice ----
    assert 5 + 12 == 17 and 5 * 12 == 60 and 5 ** 2 + 12 ** 2 == 169
    S.q("m2d-qd-p1", "medium", "The perimeter of a rectangle is $34$ cm and the length of its diagonal is $13$ cm. The area of the rectangle is:",
        ["$65$ sq cm", "$60$ sq cm", "$56$ sq cm", "$70$ sq cm"], "$60$ sq cm",
        r"""$l + b = \frac{34}{2} = 17$; with diagonal 13, the sides are the 5-12-13 pair ($5+12 = 17$).

Area $= 5 \times 12 = 60$ sq cm.""",
        r"$K = 8.5^2 - 6.5^2 = 72.25 - 42.25 = 60$. Trap: $65$ ($\frac12 \times 13 \times ...$ — diagonal is not a height).", 50)
    assert 12 * 16 == 192 and 12 ** 2 + 16 ** 2 == 400 and 2 * 28 == 56
    S.q("m2d-qd-p1", "medium", "The area of a rectangle is $192$ sq cm and its diagonal is $20$ cm. Its perimeter is:",
        ["$56$ cm", "$52$ cm", "$60$ cm", "$58$ cm"], "$56$ cm",
        r"""Sides must multiply to 192 and satisfy $l^2 + b^2 = 400$: the 12-16-20 triplet works ($12 \times 16 = 192$).

$P = 2(12 + 16) = 56$ cm.""",
        r"3-4-5 ×4: sides 12, 16 → $56$ cm. Trap: testing $l=16, b=13$ etc. without the triplet check.", 50)
    assert 5 ** 2 + 12 ** 2 == 169 and F(1, 2) * 10 * 24 == 120
    S.q("m2d-qd-p2", "medium", "One diagonal of a rhombus is $10$ cm and its side is $13$ cm. The area of the rhombus is:",
        ["$120$ sq cm", "$130$ sq cm", "$240$ sq cm", "$110$ sq cm"], "$120$ sq cm",
        r"""Half-diagonals 5 and $x$ with hypotenuse 13: $x = 12$, so the other diagonal is $24$.

$K = \frac12 \times 10 \times 24 = 120$ sq cm.""",
        r"5-12-13 halves → $d_2 = 24$ → $120$ sq cm. Trap: $130$ ($\frac12 \times 10 \times 26$).", 45)
    assert F(1, 2) * 5 * 2 * 12 * 2 == 120 and 4 * 13 == 52
    S.q("m2d-qd-p2", "medium", "The diagonals of a rhombus are in the ratio $5:12$ and its area is $120$ sq cm. The perimeter of the rhombus is:",
        ["$52$ cm", "$48$ cm", "$56$ cm", "$60$ cm"], "$52$ cm",
        r"""$d_1 = 5k$, $d_2 = 12k$: $\frac12 \times 60k^2 = 120 \Rightarrow k^2 = 4 \Rightarrow k = 2$.

Diagonals 10 and 24 → side 13 → perimeter $52$ cm.""",
        r"$30k^2 = 120$ → $k = 2$; 5-12-13 halves → $52$ cm. Trap: $48$ (side 12 from one diagonal).", 55)
    assert F(120, 15) == 8
    S.q("m2d-qd-p3", "easy", "The area of a parallelogram is $120$ sq cm and its base is $15$ cm. Its height is:",
        ["$8$ cm", "$9$ cm", "$7.5$ cm", "$10$ cm"], "$8$ cm",
        r"""$h = \frac{K}{b} = \frac{120}{15} = 8$ cm.""",
        r"$120/15 = 8$ cm. Trap: dividing the diagonal or a side instead of the base.", 30)
    assert 10 * 8 * F(1, 2) == 40
    S.q("m2d-qd-p3", "medium", "Two adjacent sides of a parallelogram are $10$ cm and $8$ cm and the angle between them is $30^\\circ$. Its area is:",
        ["$80$ sq cm", "$40$ sq cm", "$40\\sqrt{3}$ sq cm", "$20$ sq cm"], "$40$ sq cm",
        r"""$K = ab\sin\theta = 10 \times 8 \times \sin 30^\circ = 80 \times \frac12 = 40$ sq cm.""",
        r"$\sin 30^\circ = \frac12$: $40$ sq cm. Trap: $80$ (treated it as a rectangle) or $40\sqrt3$ (used $60^\circ$).", 45)
    assert F(100, 2) == 50
    S.q("m2d-qd-p4", "easy", "The diagonal of a square is $10$ cm. The area of the square is:",
        ["$100$ sq cm", "$50$ sq cm", "$50\\sqrt{2}$ sq cm", "$25$ sq cm"], "$50$ sq cm",
        r"""$K = \frac{d^2}{2} = \frac{100}{2} = 50$ sq cm.""",
        r"Half of $d^2$: $50$. Trap: $100$ (side taken as the diagonal) or $50\sqrt2$ (kept an extra $\sqrt2$).", 30)
    assert F(96, 6) == 16 and 12 + 20 == 32 and F(1, 2) * 32 * 6 == 96
    S.q("m2d-qd-p4", "medium", "The parallel sides of a trapezium differ by $8$ cm and the perpendicular distance between them is $6$ cm. If the area is $96$ sq cm, the longer parallel side is:",
        ["$20$ cm", "$16$ cm", "$12$ cm", "$24$ cm"], "$20$ cm",
        r"""Sides $a$ and $a+8$: $\frac12(a + a + 8) \times 6 = (a+4) \times 6 = 96 \Rightarrow a + 4 = 16$.

$a = 12$, longer side $= 20$ cm.""",
        r"$(a+4) \times 6 = 96$ → $a = 12$ → longer $20$ cm. Trap: $12$ — that is the SHORTER side.", 45)
    return S


# ---------------- m2d-circles ----------------

def build_circles():
    S = Sub("m2d-circles")

    S.notes = r"""### The π machinery (use $\pi = \frac{22}{7}$ unless told otherwise)
$$C = 2\pi r,\qquad K = \pi r^2$$
Reverse routes appear constantly: from circumference $r = \frac{C}{2\pi}$; from area $r = \sqrt{\frac{K}{\pi}}$. Keep the favourite radii at hand: $r = 7$ → $C = 44$, $K = 154$; $r = 14$ → $C = 88$, $K = 616$; $r = 21$ → $C = 132$, $K = 1386$.

### Sector and arc
For angle $\theta$ at the centre:
$$\text{sector area} = \frac{\theta}{360} \times \pi r^2,\qquad \text{arc length} = \frac{\theta}{360} \times 2\pi r$$
Sector area is just the full area scaled by $\frac{\theta}{360}$ — the same fraction scales the circumference into the arc. Semi-circle, quarter-circle, $60^\circ$ slice: halve, quarter, sixth.

### Ring (annulus) and wheel
- Ring: $K = \pi(R^2 - r^2) = \pi(R+r)(R-r)$ — factorise before multiplying.
- Wheel: one revolution covers one circumference. Revolutions $= \frac{\text{distance}}{\text{circumference}} = \frac{d}{\pi D}$ where $D$ is the wheel's diameter. Convert units first (cm vs m) — the classic trap.

### Circles inside and outside squares
- Circle **inscribed** in a square of side $a$: diameter $= a$, so $r = \frac{a}{2}$.
- Circle **circumscribed** about the square: diameter $=$ diagonal $= a\sqrt2$, so $r = \frac{a}{\sqrt2}$ and $K = \pi \cdot \frac{a^2}{2} = \frac{\pi a^2}{2}$ — exactly double the inscribed circle's area ($\frac{\pi a^2}{4}$). That 2 : 1 ratio is asked as often as the areas themselves.

### Composite shapes and costs
Compound figures are assembled from these pieces: a window of rectangle plus semicircle has perimeter $=$ (two widths + length) + half-circumference, and area $=$ rectangle + $\frac12\pi r^2$ — always add PERIMETER pieces for fencing/border costs and AREA pieces for carpeting/painting costs. Fencing a circular park: cost $= 2\pi r \times$ rate per metre. Ploughing/circular path questions use the ring area with a rate: cost $= \pi(R^2 - r^2) \times$ rate per sq m. Keep the pieces separate until the last step — merging them early is where sign and factor errors happen. A worked minute-example: a circular park of radius 35 m with a 7 m wide path outside → ring area $= \frac{22}{7} \times 42 \times 28 = 3696$ sq m; at Rs 10 per sq m the path costs Rs 36,960.

### Quick revision
- $C = 2\pi r$, $K = \pi r^2$; $(7, 44, 154)$, $(14, 88, 616)$, $(21, 132, 1386)$.
- Sector/arc: multiply by $\frac{\theta}{360}$.
- Ring: $\pi(R+r)(R-r)$; wheel revolutions $= \frac{\text{distance}}{\pi D}$.
- Inscribed in square: $r = a/2$; circumscribed: $r = a/\sqrt2$ (areas in ratio $1:2$).
"""

    S.pattern("m2d-ci-p1", "Area and circumference, forward and reverse", "very common",
        "Radius/diameter given — or circumference/area given with the other quantity asked.",
        r"C = 2\pi r,\quad K = \pi r^2",
        r"""1. Forward: substitute $r$ (halve the diameter first — the classic slip).
2. Reverse: $r = \frac{C}{2\pi}$ from circumference, $r = \sqrt{K/\pi}$ from area.
3. Use the memorised set: (7→44, 154), (14→88, 616), (21→132, 1386).

Why: both formulas are functions of $r$ alone, so every question is a one-step conversion through $r$.""",
        "The circumference of a circle is 132 cm. Its area is:",
        r"$r = \frac{132 \times 7}{44} = 21$ cm; $K = \frac{22}{7} \times 441 = 1386$ sq cm.")
    S.pattern("m2d-ci-p2", "Sector area and arc length", "very common",
        "An angle at the centre with the radius given — sector area or arc length asked (or reversed).",
        r"\frac{\theta}{360}\pi r^2,\quad \frac{\theta}{360} 2\pi r",
        r"""1. Reduce the fraction $\frac{\theta}{360}$ first: $90°$ → $\frac14$, $60°$ → $\frac16$, $72°$ → $\frac15$.
2. Sector area: the fraction × full area; arc: the fraction × full circumference.
3. Reverse: $\theta = \frac{\text{arc}}{2\pi r} \times 360°$.

Why: the sector is a proportional slice of the circle — one fraction does everything.""",
        "Find the arc length of a sector of angle $72^\\circ$ in a circle of radius $35$ cm.",
        r"$\frac{72}{360} = \frac15$; arc $= \frac15 \times 2 \times \frac{22}{7} \times 35 = \frac15 \times 220 = 44$ cm.")
    S.pattern("m2d-ci-p3", "Ring (annulus) area and wheel revolutions", "common",
        "Two concentric circles (path/border) — area of the ring; or a wheel covering a distance — number of revolutions.",
        r"K = \pi(R^2 - r^2) = \pi(R+r)(R-r);\quad \text{revs} = \frac{d}{\pi D}",
        r"""1. Ring: factorise $R^2 - r^2 = (R+r)(R-r)$ before multiplying by $\pi$.
2. Wheel: one revolution = one circumference $\pi D$; convert distance and diameter to the SAME units.
3. Revolutions $= \frac{\text{distance}}{\pi D}$.

Why: the ring is the difference of two circle areas; a rolling wheel lays down its circumference per turn.""",
        "A wheel of diameter 70 cm rolls a distance of 231 m. The number of revolutions it makes is:",
        r"$C = \frac{22}{7} \times 0.7 = 2.2$ m; revs $= \frac{231}{2.2} = 105$.")
    S.pattern("m2d-ci-p4", "Circles inscribed in / circumscribed about squares", "common",
        "A circle inside a square (touching sides) or around it (through corners); radius or area asked.",
        r"r_{\text{in}} = \frac{a}{2},\quad r_{\text{out}} = \frac{a}{\sqrt{2}}",
        r"""1. Inscribed: diameter = side of square → $r = \frac{a}{2}$, $K = \frac{\pi a^2}{4}$.
2. Circumscribed: diameter = diagonal → $r = \frac{a\sqrt2}{2} = \frac{a}{\sqrt2}$, $K = \frac{\pi a^2}{2}$.
3. Ratio fact: circumscribed area : inscribed area $= 2 : 1$.

Why: the inscribed diameter spans opposite sides; the circumscribed diameter spans opposite corners (the diagonal).""",
        "A circle is inscribed in a square of side 14 cm. The area of the circle is:",
        r"$r = 7$ cm; $K = \frac{22}{7} \times 49 = 154$ sq cm.")

    # ---- practice ----
    assert 2 * F(22, 7) * 7 == 44
    S.q("m2d-ci-p1", "easy", "The circumference of a circle of radius $7$ cm is (take $\\pi = 22/7$):",
        ["$44$ cm", "$22$ cm", "$154$ cm", "$88$ cm"], "$44$ cm",
        r"""$C = 2\pi r = 2 \times \frac{22}{7} \times 7 = 44$ cm.""",
        r"$2 \times 22 = 44$ cm (the 7s cancel). Trap: $154$ — that is the AREA.", 25)
    assert F(132 * 7, 44) == 21 and F(22, 7) * 441 == 1386
    S.q("m2d-ci-p1", "medium", "The circumference of a circle is $132$ cm. Its area is (take $\\pi = 22/7$):",
        ["$1386$ sq cm", "$1296$ sq cm", "$1440$ sq cm", "$1462$ sq cm"], "$1386$ sq cm",
        r"""$r = \frac{C}{2\pi} = \frac{132 \times 7}{44} = 21$ cm.

$K = \frac{22}{7} \times 21^2 = \frac{22}{7} \times 441 = 1386$ sq cm.""",
        r"132 → r 21 (the favourite triple) → area 1386. Trap: $1296$ ($36^2$ from $r=36$).", 40)
    assert F(1, 4) * F(22, 7) * 196 == 154
    S.q("m2d-ci-p2", "medium", "The area of a sector of a circle of radius $14$ cm with central angle $90^\\circ$ is (take $\\pi = 22/7$):",
        ["$154$ sq cm", "$616$ sq cm", "$77$ sq cm", "$308$ sq cm"], "$154$ sq cm",
        r"""$\frac{90}{360} = \frac14$: sector $= \frac14 \times \frac{22}{7} \times 196 = \frac14 \times 616 = 154$ sq cm.""",
        r"Quarter of 616 = 154. Trap: $616$ (full circle) or $308$ (half).", 35)
    assert F(72, 360) == F(1, 5) and F(1, 5) * 2 * F(22, 7) * 35 == 44
    S.q("m2d-ci-p2", "medium", "The length of the arc of a sector of angle $72^\\circ$ in a circle of radius $35$ cm is (take $\\pi = 22/7$):",
        ["$44$ cm", "$40$ cm", "$55$ cm", "$22$ cm"], "$44$ cm",
        r"""$\frac{72}{360} = \frac15$; circumference $= 2 \times \frac{22}{7} \times 35 = 220$ cm.

Arc $= \frac15 \times 220 = 44$ cm.""",
        r"$\frac15$ of 220 = 44 cm. Trap: $176$ — that's the remaining major arc.", 40)
    assert F(22, 7) * (14 + 7) * (14 - 7) == 462
    S.q("m2d-ci-p3", "medium", "Two concentric circles have radii $14$ cm and $7$ cm. The area of the ring between them is (take $\\pi = 22/7$):",
        ["$462$ sq cm", "$616$ sq cm", "$154$ sq cm", "$770$ sq cm"], "$462$ sq cm",
        r"""$K = \pi(R^2 - r^2) = \frac{22}{7} \times (196 - 49) = \frac{22}{7} \times 147 = 462$ sq cm.

(Equivalently $616 - 154$.)""",
        r"$\frac{22}{7} \times 147 = 462$. Trap: $770$ ($\pi(R+r)^2$, squaring the sum).", 40)
    assert F(22, 7) * F(7, 10) == F(11, 5) and F(231, 1) / F(11, 5) == 105
    S.q("m2d-ci-p3", "hard", "A wheel of diameter $70$ cm rolls a distance of $231$ m. The number of complete revolutions it makes is (take $\\pi = 22/7$):",
        ["$105$", "$115$", "$95$", "$110$"], "$105$",
        r"""Circumference $= \pi D = \frac{22}{7} \times 0.7 = 2.2$ m.

Revolutions $= \frac{231}{2.2} = 105$.""",
        r"$231 \div 2.2 = 105$. Trap: forgetting cm→m (getting 10500) or using $r=70$ cm.", 55)
    assert F(22, 7) * 49 == 154
    S.q("m2d-ci-p4", "easy", "A circle is inscribed in a square of side $14$ cm. The area of the circle is (take $\\pi = 22/7$):",
        ["$154$ sq cm", "$616$ sq cm", "$308$ sq cm", "$77$ sq cm"], "$154$ sq cm",
        r"""Inscribed: diameter = side, so $r = 7$ cm.

$K = \frac{22}{7} \times 49 = 154$ sq cm.""",
        r"$r = 7$ → 154. Trap: $308$ — that is the circumscribed circle ($r = 7\sqrt2$).", 30)
    assert F(1, 2) * F(22, 7) * 196 == 308
    S.q("m2d-ci-p4", "medium", "A circle is circumscribed about a square of side $14$ cm. The area of the circle is (take $\\pi = 22/7$):",
        ["$308$ sq cm", "$154$ sq cm", "$616$ sq cm", "$224$ sq cm"], "$308$ sq cm",
        r"""Circumscribed: diameter = diagonal $= 14\sqrt2$, so $r^2 = \frac{(14\sqrt2)^2}{4} = 98$.

$K = \frac{22}{7} \times 98 = 308$ sq cm (double the inscribed case).""",
        r"$K = \frac{\pi a^2}{2} = \frac{22}{7} \times 98 = 308$. Trap: $154$ (inscribed value).", 45)
    return S
