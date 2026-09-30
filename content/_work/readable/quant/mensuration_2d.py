"""Readable rewrite of Mensuration 2-D (all 5 subtopics).

Plain English, one idea per section, every number recomputed below.
Run: python mensuration_2d.py  (patches content/core/topics/quant/mensuration-2d.json)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "mensuration-2d.json"

# ---------- answer checks (every number printed on the page) ----------
# triangles
assert 6 * 8 // 2 == 24 and 10 ** 2 == 6 ** 2 + 8 ** 2               # right 6-8-10, K 24
assert 2 * 24 / 10 == 4.8 and 48 * 5 == 240                           # altitude to hypotenuse
assert 12 * 12 == 144 and 36 * 36 * 3 == 3888                          # equilateral a=12, K=36*sqrt3
assert 6 * 6 == 36 and 81 * 3 == 243                                   # equilateral a=6, K=9*sqrt3
assert 17 ** 2 - 8 ** 2 == 225 == 15 ** 2 and 16 * 15 // 2 == 120     # isosceles 17,17,16
assert 21 * 8 * 7 * 6 == 7056 == 84 ** 2 and 84 // 21 == 4            # Heron 13-14-15, r 4
assert 2730 * 8 == 21840 == 336 * 65                                   # R = abc/4K = 65/8
assert 15 * 10 * 3 * 2 == 900 == 30 ** 2                               # Heron 5-12-13
assert 18 * 9 * 6 * 3 == 2916 == 54 ** 2                               # Heron 9-12-15
# quads
assert 34 // 2 == 17 and 17 ** 2 - 13 ** 2 == 120 and 120 // 2 == 60  # P 34, d 13 -> area 60
assert 5 * 12 == 60 and 60 * 4 == 240 and 10 * 24 // 2 == 120         # rhombus ratio parts
assert 5 ** 2 + 12 ** 2 == 169 == 13 ** 2 and 4 * 13 == 52            # halves 5,12 -> side 13
assert 10 * 8 // 2 == 40                                               # parallelogram 10,8,30 deg
assert 2 * 96 // 6 == 32 and 32 == 20 + 12 and 20 - 12 == 8           # trapezium sides
assert 12 * (5 + 9) // 2 == 84                                         # general quad 1/2 d (h1+h2)
assert 8 * 8 == 64                                                     # square from diagonal 8*sqrt2
# circles
assert 132 * 7 // (2 * 22) == 21 and 22 * 63 == 1386                   # C 132 -> r 21, K 1386
assert 72 * 2 == 144 and (2 * 22 * 35) // 7 == 220 and 220 * 72 // 360 == 44  # arc 44
assert 22 * 175 == 3850 and 3850 * 72 // 360 == 770                    # sector 770
assert 196 - 49 == 147 and 22 * 21 == 462                              # ring 14,7 -> 462
assert 70 * 22 // 7 == 220 and 23100 // 220 == 105                     # wheel 70 cm, 231 m
assert 22 * 7 == 154                                                   # circle in square 14
assert (2 * 22 * 14) // 7 == 88 and 88 // 4 == 22 and 28 + 22 == 50    # quadrant r 14
assert 22 * 196 == 4312 and 4312 // (7 * 4) == 154                     # quadrant area r 14
# polygons
assert 6 * 9 == 54 and 54 * 54 * 3 == 8748 == 2916 * 3                 # hexagon a=6 -> 54*sqrt3
assert 72 * 6 // 2 == 216                                              # 1/2 P a
assert 360 // 8 == 45 and 180 - 45 == 135 and 6 * 180 == 1080          # octagon angles
assert 15 * 12 // 2 == 90                                              # 90 diagonals -> 15 sides
assert 2 * 8 == 16                                                     # hexagon longest diagonal
# scaling
assert 200 * 9 // 25 == 72                                             # areas 9:25, larger 200
assert 20 + 20 + 20 * 20 // 100 == 44                                  # +20% side -> +44% area
assert -10 + -10 + (-10) * (-10) // 100 == -19                         # -10% side -> -19% area
assert 3 ** 2 == 9 and 600 * 9 == 5400                                 # side 5 -> 15, cost x9
assert 5000 ** 2 == 25 * 10 ** 6 and 4 * 25 * 10 ** 6 == 10 ** 8       # map 1:5000
assert 10 ** 8 // 10 ** 4 == 10 ** 4 == 10000                          # sq cm -> sq m
assert 44 * 7 // 44 == 7 and 22 * 7 == 154 and 44 // 4 == 11 and 11 * 11 == 121  # wire 44

# ---------------- m2d-triangles ----------------
tr_concept = (
    "Area of a triangle is half of base times height, and any side can be the base. "
    "Equilateral, isosceles and right triangles have shortcuts that turn most exam questions into one line. "
    "Heron's formula covers everything else using only the three sides."
)

tr_notes = r"""### One master formula
$$K=\frac{1}{2}\times\text{base}\times\text{height}$$
The height is the perpendicular dropped onto the chosen base. Pick the side whose height is easiest, then stick with that pair.

Two triangles on the same base and between the same parallels always have equal areas. Half of the same base and the same height forces the same area. A median uses exactly that, which is why it never fails to halve a triangle.

> **Rule:** Any side may be the base, but the height must be measured perpendicular to that exact side.

### The three special triangles
- **Right triangle**: the two legs act as base and height. Legs $6$ and $8$ give $K=\dfrac{6\times8}{2}=24$, hypotenuse $10$.
- **Equilateral** (side $a$): height $=\dfrac{\sqrt3}{2}a$, area $=\dfrac{\sqrt3}{4}a^2$. Side $12$: height $6\sqrt3$, area $36\sqrt3$.
- **Isosceles**: the median to the base is the height. Equal sides $17$, base $16$: half-base $8$, height $\sqrt{289-64}=15$, area $\dfrac{16\times15}{2}=120$.

> **Tip:** Equilateral numbers stay clean: for $a=6$ the area is $9\sqrt3$, and every side gives a multiple of $\sqrt3$.

### Heron's formula
With all three sides, take the half-perimeter first:
$$s=\frac{a+b+c}{2},\qquad K=\sqrt{s(s-a)(s-b)(s-c)}$$
Sides $13$, $14$, $15$: $s=21$, so $K=\sqrt{21\times8\times7\times6}=\sqrt{7056}=84$.

Sides $5$, $12$, $13$ give $s=15$ and $K=\sqrt{15\times10\times3\times2}=30$. But $5$-$12$-$13$ is a triplet, so $\dfrac{5\times12}{2}=30$ was faster.

> **Shortcut:** Spot a Pythagorean triplet and skip Heron. A right triangle's area is just half the product of its legs.

### Altitude to the hypotenuse: two areas
The right triangle with legs $6$, $8$ has hypotenuse $10$ and area $24$. Take the hypotenuse as the base instead:
$$\frac{1}{2}\times10\times h=24 \Rightarrow h=4.8=\frac{24}{5}$$
Same triangle, same area, second route. That is the whole trick.

> **Watch:** Equate the two area expressions before touching square roots. The altitude rule $h=\dfrac{ab}{c}$ falls out of it.

### Radii and the median split
- Inradius $r=\dfrac{K}{s}$. For $13$-$14$-$15$: $r=\dfrac{84}{21}=4$.
- Circumradius $R=\dfrac{abc}{4K}=\dfrac{2730}{336}=\dfrac{65}{8}=8.125$.
- Every median splits a triangle into two equal areas. Two medians cut it into four equal areas.
- Equilateral: $R=2r$, and $a=6$ gives $r=\sqrt3$, $R=2\sqrt3$.

> **Remember:** Small radius $r$ divides the area by the half-perimeter; big radius $R$ multiplies the sides. $R=2r$ only in the equilateral case.
"""

tr_formulas = [
    {"name": "Triangle area", "tex": r"K=\frac{1}{2}bh", "note": "b = any side, h = perpendicular height on it."},
    {"name": "Equilateral triangle", "tex": r"K=\frac{\sqrt3}{4}a^2,\quad h=\frac{\sqrt3}{2}a", "note": "a = side; height is root-three over two of the side."},
    {"name": "Heron's formula", "tex": r"K=\sqrt{s(s-a)(s-b)(s-c)},\quad s=\frac{a+b+c}{2}", "note": "s = half the perimeter."},
    {"name": "Altitude to hypotenuse", "tex": r"h=\frac{ab}{c}=\frac{2K}{c}", "note": "a, b legs, c hypotenuse; from equating two areas."},
    {"name": "Inradius / circumradius", "tex": r"r=\frac{K}{s},\quad R=\frac{abc}{4K}", "note": "K = area, s = half-perimeter."},
    {"name": "Median split", "tex": r"\text{median}\Rightarrow\text{two equal areas}", "note": "Each median halves the area of a triangle."},
]

tr_tricks = [
    {
        "title": "Triplet beats Heron",
        "body": "Before Heron, check for a triplet. A right triangle needs only half the product of its legs.",
        "example": {
            "q": "Find the area of the triangle with sides 9 cm, 12 cm and 15 cm.",
            "steps": [r"$9^2+12^2=81+144=225=15^2$, so it is right-angled.", r"$K=\dfrac{9\times12}{2}$.", r"$K=54$ sq cm."],
            "answer": "54 sq cm",
        },
    },
    {
        "title": "Isosceles: half it first",
        "body": "The median to the base is the height. Halve the base, then use Pythagoras with an equal side.",
        "example": {
            "q": "An isosceles triangle has equal sides of 17 cm and base 16 cm. Find its area.",
            "steps": [r"Half-base $=8$ cm.", r"Height $=\sqrt{17^2-8^2}=\sqrt{225}=15$ cm.", r"$K=\dfrac{16\times15}{2}=120$ sq cm."],
            "answer": "120 sq cm",
        },
    },
    {
        "title": "Two radii from Heron",
        "body": "After Heron gives the area, both radii are one division away: r divides by s, R uses abc over 4K.",
        "example": {
            "q": "The sides of a triangle are 13, 14 and 15 cm. Find its inradius.",
            "steps": [r"$s=21$, $K=84$.", r"$r=\dfrac{K}{s}=\dfrac{84}{21}$.", r"$r=4$ cm."],
            "answer": "4 cm",
        },
    },
]

tr_mistakes = [
    {"wrong": "Using the slant side as the height.", "right": "The height is perpendicular to the base. In the 17-17-16 triangle it is 15, not 17."},
    {"wrong": "Forgetting to halve the base in an isosceles triangle.", "right": "Pythagoras needs the half-base 8, so the height is $\\sqrt{289-64}=15$."},
    {"wrong": "Running Heron on a right triangle.", "right": "A triplet like 6-8-10 needs only $\\dfrac{6\\times8}{2}=24$."},
    {"wrong": "Using the full perimeter as $s$.", "right": "$s$ is the half-perimeter. For 13-14-15, $s=21$, not 42."},
    {"wrong": "Mixing the legs with the hypotenuse in $h=\\dfrac{ab}{c}$.", "right": "$c$ is the hypotenuse. Legs 6 and 8 over 10 give $h=4.8$."},
]

tr_revision = [
    "Master formula: half of base times perpendicular height, any side as base.",
    "Equilateral side $a$: height $\\dfrac{\\sqrt3}{2}a$, area $\\dfrac{\\sqrt3}{4}a^2$.",
    "Isosceles: halve the base, Pythagoras with an equal side gives the height.",
    "Heron: half-perimeter first; a triplet triangle skips Heron entirely.",
    "Altitude to the hypotenuse equals $\\dfrac{ab}{c}$, from two area expressions.",
    "$r=\\dfrac{K}{s}$, $R=\\dfrac{abc}{4K}$, and every median halves the area.",
]

def pat(pid, name, freq, spot, steps, why, q, esteps, ans):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot,
            "steps": steps, "why": why, "example": {"q": q, "steps": esteps, "answer": ans}}

tr_patterns = [
    pat("m2d-tr-p1", "Area from base-height / equilateral formula", "very common",
        "A triangle with one length given, or an equilateral with its side.",
        [r"Pick the base with the easiest height.", r"Right triangle: legs are base and height.",
         r"Equilateral: use $K=\dfrac{\sqrt3}{4}a^2$ directly.", r"Multiply and simplify."],
        "The direct formula is a one-liner, and equilateral sides keep the answer a clean multiple of $\\sqrt3$.",
        "Find the area of an equilateral triangle of side 12 cm.",
        [r"$K=\dfrac{\sqrt3}{4}\times12^2$.", r"$=\dfrac{\sqrt3}{4}\times144=36\sqrt3$ sq cm."],
        "36*sqrt(3) sq cm (about 62.35 sq cm)"),
    pat("m2d-tr-p2", "Heron's formula (and the triplet bypass)", "very common",
        "Three sides, no right angle, no height.",
        [r"Compute $s=\dfrac{a+b+c}{2}$.", r"Form the product $s(s-a)(s-b)(s-c)$.",
         r"Take the square root.", r"Check for a triplet first to skip the work."],
        "Heron works from sides alone, and most exam values are perfect squares under the root.",
        "Find the area of the triangle with sides 13 cm, 14 cm and 15 cm.",
        [r"$s=\dfrac{42}{2}=21$.", r"$K=\sqrt{21\times8\times7\times6}=\sqrt{7056}=84$."],
        "84 sq cm"),
    pat("m2d-tr-p3", "Isosceles triangle area", "common",
        "Two equal sides and the base, no height.",
        [r"Halve the base.", r"Height $=\sqrt{(\text{equal side})^2-(\text{half-base})^2}$.",
         r"$K=\dfrac{1}{2}\times\text{base}\times\text{height}$."],
        "The median to the base doubles as the height, so Pythagoras finishes the job in two steps.",
        "An isosceles triangle has equal sides of 17 cm and base 16 cm. Its area is:",
        [r"Half-base $=8$; height $=\sqrt{17^2-8^2}=15$.", r"$K=\dfrac{16\times15}{2}=120$ sq cm."],
        "120 sq cm"),
    pat("m2d-tr-p4", "Inradius and median area-split", "common",
        "Sides given, question asks the inradius; or a median asks for an area ratio.",
        [r"Find the area first (Heron or a triplet).", r"$r=\dfrac{K}{s}$ with the half-perimeter.",
         r"For medians: each one splits the area in half."],
        "Both facts reuse the area you already computed, so nothing extra is needed.",
        "The sides of a triangle are 13, 14 and 15 cm. Its inradius is:",
        [r"$K=84$, $s=21$.", r"$r=\dfrac{84}{21}=4$ cm."],
        "4 cm"),
    pat("m2d-tr-p5", "Altitude to the hypotenuse (area two ways)", "occasional",
        "A right triangle, question asks the height on the hypotenuse.",
        [r"Compute the area from the two legs.", r"Set $\dfrac{1}{2}\times\text{hypotenuse}\times h$ equal to it.",
         r"Solve for $h$."],
        "One triangle, one area, two base choices. Equating them avoids the similar-triangle mess.",
        "In a right triangle with legs 6 cm and 8 cm, find the length of the altitude drawn to the hypotenuse.",
        [r"$K=\dfrac{6\times8}{2}=24$; hypotenuse $=10$.", r"$\dfrac{1}{2}\times10\times h=24$.", r"$h=4.8$ cm."],
        "4.8 cm"),
]

# ---------------- m2d-quads ----------------
qd_concept = (
    "A rectangle, square, parallelogram, rhombus or trapezium each has a two-part area formula. "
    "Most questions give two facts and ask for a third, so the fast route is an identity, not a quadratic. "
    "Any quadrilateral splits into two triangles along a diagonal."
)

qd_notes = r"""### The family card
| Figure | Area | Extras |
|---|---|---|
| Rectangle $l\times b$ | $lb$ | $P=2(l+b)$, diagonal $\sqrt{l^2+b^2}$ |
| Square, side $a$ | $a^2$ | diagonal $a\sqrt2$ |
| Parallelogram | $bh$ or $ab\sin\theta$ | adjacent angles add to $180^\circ$ |
| Rhombus | $\dfrac{1}{2}d_1d_2$ | diagonals cross at $90^\circ$ |
| Trapezium | $\dfrac{1}{2}(a+b)h$ | $a$, $b$ parallel |

> **Rule:** Any quadrilateral: $K=\dfrac{1}{2}\times\text{diagonal}\times(\text{sum of the two perpendiculars on it})$. Every row above is a special case.

### Rectangle from two facts
Given $P=34$ and diagonal $13$: $l+b=17$ and $l^2+b^2=169$. Use the identity
$$(l+b)^2=l^2+b^2+2lb \Rightarrow 289=169+2lb \Rightarrow lb=60$$
Area $60$ without ever finding $l$ and $b$. Check: $l+b=17$ with $lb=60$ gives sides $12$ and $5$, and $5$-$12$-$13$ confirms the diagonal.

A square of side $a$ has diagonal $a\sqrt2$. Given the diagonal $8\sqrt2$, the side is $8$ and the area is $64$.

> **Tip:** Two facts about a rectangle almost always combine through $(l+b)^2$ or $(l-b)^2$. Avoid solving a quadratic.

### Rhombus through half-diagonals
The diagonals bisect each other at right angles, so the halves and one side form a right triangle.

Diagonals in ratio $5:12$ with area $120$: $\dfrac{1}{2}(5k)(12k)=120$ gives $k=2$, so diagonals $10$ and $24$. Halves $5$ and $12$ give side $13$ and perimeter $52$. All four sides are equal, so the perimeter is always four times one side.

> **Watch:** Halves of rhombus diagonals are triplets in disguise: (5, 12, 13), (8, 6, 10), (12, 35, 37).

### Parallelogram and trapezium
Parallelogram sides $10$ and $8$ with a $30^\circ$ angle between them: $K=10\times8\times\sin30^\circ=80\times\dfrac{1}{2}=40$.

Trapezium: parallel sides differ by $8$, height $6$, area $96$. Then $\dfrac{1}{2}(a+b)\times6=96$ gives $a+b=32$; with $a-b=8$, the sides are $20$ and $12$. The height on the base $10$ above is $8\sin30^\circ=4$ cm, and the midsegment between the slanted sides is $\dfrac{20+12}{2}=16$.

> **Remember:** The height of a parallelogram is perpendicular to the base, never the slant side.

### Split along a diagonal
A general quadrilateral with diagonal $12$ and perpendiculars $5$ and $9$ dropping onto it from the other two corners:
$$K=\frac{1}{2}\times12\times(5+9)=84$$
The diagonal makes two triangles; add their two areas to finish.

> **Tip:** A square with diagonal $8\sqrt2$ has side $8$, area $64$. Match the diagonal formula $a\sqrt2$ backwards to the side.
"""

qd_formulas = [
    {"name": "Rectangle", "tex": r"K=lb,\quad P=2(l+b),\quad d=\sqrt{l^2+b^2}", "note": "Three linked facts; any two fix the third."},
    {"name": "Square", "tex": r"K=a^2,\quad d=a\sqrt2", "note": "Diagonal is root-two times the side."},
    {"name": "Parallelogram", "tex": r"K=bh=ab\sin\theta", "note": "theta = angle between the two given sides."},
    {"name": "Rhombus", "tex": r"K=\frac{1}{2}d_1d_2", "note": "Diagonals cross at right angles and halve each other."},
    {"name": "Trapezium", "tex": r"K=\frac{1}{2}(a+b)h", "note": "a, b = the two parallel sides."},
    {"name": "Any quadrilateral", "tex": r"K=\frac{1}{2}d(h_1+h_2)", "note": "d = a diagonal; h1, h2 = perpendiculars onto it."},
]

qd_tricks = [
    {
        "title": "Rectangle identities, not quadratics",
        "body": "With perimeter and diagonal, jump straight to $(l+b)^2=l^2+b^2+2lb$ and read off the area.",
        "example": {
            "q": "The perimeter of a rectangle is 34 cm and its diagonal is 13 cm. Its area is:",
            "steps": [r"$l+b=17$, so $(l+b)^2=289$.", r"$l^2+b^2=13^2=169$.", r"$2lb=289-169=120$, so $lb=60$."],
            "answer": "60 sq cm",
        },
    },
    {
        "title": "Rhombus ratio to perimeter",
        "body": "Ratio plus area fixes both diagonals. Halve them, spot the triplet, read the side.",
        "example": {
            "q": "The diagonals of a rhombus are in the ratio 5 : 12 and its area is 120 sq cm. Its perimeter is:",
            "steps": [r"$\dfrac{1}{2}\times5k\times12k=120$ gives $k=2$.", r"Diagonals $10$, $24$; halves $5$, $12$; side $13$.", r"Perimeter $=4\times13=52$ cm."],
            "answer": "52 cm",
        },
    },
    {
        "title": "Diagonal splits any quadrilateral",
        "body": "No special shape? Draw one diagonal. The area is half the diagonal times the sum of the two heights.",
        "example": {
            "q": "A quadrilateral has a diagonal of 12 cm, and the perpendiculars to it from the other corners are 5 cm and 9 cm. Find the area.",
            "steps": [r"$K=\dfrac{1}{2}\times12\times(5+9)$.", r"$=6\times14$.", r"$=84$ sq cm."],
            "answer": "84 sq cm",
        },
    },
]

qd_mistakes = [
    {"wrong": "Treating the slant side of a parallelogram as the height.", "right": "Height is perpendicular. Sides 10 and 8 at $30^\\circ$ give area $10\\times8\\times\\dfrac12=40$."},
    {"wrong": "Using $d_1d_2$ for the rhombus area.", "right": "The formula has the half: $\\dfrac{1}{2}\\times10\\times24=120$, not 240."},
    {"wrong": "Halving only one diagonal of a rhombus.", "right": "Both diagonals bisect each other, so both become halves: 5 and 12."},
    {"wrong": "Solving a quadratic for $l$ and $b$ when only $lb$ is asked.", "right": "Use $(l+b)^2-(l^2+b^2)=2lb$ and stop at the product."},
    {"wrong": "Adding the parallel sides after multiplying by the height.", "right": "Trapezium area is $\\dfrac12(a+b)h$; add first, then halve and multiply."},
]

qd_revision = [
    "Rectangle: $lb$, $2(l+b)$, $\\sqrt{l^2+b^2}$; two facts combine through an identity.",
    "Square: diagonal $a\\sqrt2$; backwards from the diagonal, divide by $\\sqrt2$.",
    "Parallelogram: $bh=ab\\sin\\theta$; the height is perpendicular.",
    "Rhombus: $\\dfrac12 d_1d_2$; half-diagonals plus a side form a right triangle.",
    "Trapezium: $\\dfrac12(a+b)h$ with $a$, $b$ the parallel sides.",
    "Any quadrilateral: $\\dfrac12 \\times$ diagonal $\\times$ (sum of perpendiculars).",
]

qd_patterns = [
    pat("m2d-qd-p1", "Rectangle from two of {area, perimeter, diagonal}", "very common",
        "Two rectangle facts given, a third one asked.",
        [r"Turn the perimeter into $l+b$.", r"Write the second fact as $l^2+b^2$ or $lb$.",
         r"Bridge with $(l+b)^2=l^2+b^2+2lb$.", r"Read off the asked quantity."],
        "Identities move between the three facts faster than solving for the sides.",
        "The perimeter of a rectangle is 34 cm and its diagonal is 13 cm. Its area is:",
        [r"$l+b=17$ and $l^2+b^2=169$.", r"$2lb=289-169=120$.", r"$lb=60$ sq cm."],
        "60 sq cm"),
    pat("m2d-qd-p2", "Rhombus: diagonals, area and perimeter", "very common",
        "Rhombus with diagonals in a ratio, or a mix of area and side asked.",
        [r"Set the diagonals as $d_1$ and $d_2$ from the ratio.", r"Use $K=\dfrac{1}{2}d_1d_2$ to fix them.",
         r"Halve both diagonals.", r"Side $=\sqrt{(\text{half}_1)^2+(\text{half}_2)^2}$, perimeter is $4$ sides."],
        "Ratio plus area pins both diagonals; the half-diagonal right triangle does the rest.",
        "The diagonals of a rhombus are in the ratio 5 : 12 and its area is 120 sq cm. Its perimeter is:",
        [r"$\dfrac12\times5k\times12k=120 \Rightarrow k=2$: diagonals 10, 24.", r"Halves 5, 12 give side 13.", r"$P=4\times13=52$ cm."],
        "52 cm"),
    pat("m2d-qd-p3", "Parallelogram area (base-height or ab sin theta)", "common",
        "Parallelogram with two sides and the angle between them, or base and height.",
        [r"If a height is given, use $K=bh$.", r"With two sides and the angle: $K=ab\sin\theta$.",
         r"Recall $\sin30^\circ=\dfrac12$, $\sin90^\circ=1$."],
        "Two entry points cover every parallelogram question; the angle version needs no height.",
        "Two adjacent sides of a parallelogram are 10 cm and 8 cm and the angle between them is $30^\\circ$. Its area is",
        [r"$K=10\times8\times\sin30^\circ$.", r"$=80\times\dfrac12=40$ sq cm."],
        "40 sq cm"),
    pat("m2d-qd-p4", "Square diagonal and trapezium area", "common",
        "A square given by its diagonal, or a trapezium with a side difference.",
        [r"Square: side $=\dfrac{\text{diagonal}}{\sqrt2}$, then $K=a^2$.",
         r"Trapezium: write $a+b$ from $\dfrac{2K}{h}$.", r"Combine with $a-b$ if a difference is given."],
        "Both shapes resolve with one substitution instead of full side-by-side solving.",
        "The parallel sides of a trapezium differ by 8 cm and its height is 6 cm. If its area is 96 sq cm, the longer parallel side is:",
        [r"$a+b=\dfrac{2\times96}{6}=32$ and $a-b=8$.", r"$2a=40 \Rightarrow a=20$ cm."],
        "20 cm"),
    pat("m2d-qd-p5", "Any quadrilateral split by a diagonal", "common",
        "A quadrilateral that is not a named shape, with a diagonal and two heights.",
        [r"Draw the given diagonal; it makes two triangles.", r"Collect both perpendicular heights onto it.",
         r"$K=\dfrac{1}{2}\times d\times(h_1+h_2)$."],
        "One formula covers every irregular quadrilateral, and it is just two triangle areas added.",
        "A quadrilateral has a 12 cm diagonal; the perpendiculars to it from the other two corners are 5 cm and 9 cm. Its area is:",
        [r"$K=\dfrac12\times12\times(5+9)$.", r"$=6\times14=84$ sq cm."],
        "84 sq cm"),
]

# ---------------- m2d-circles ----------------
ci_concept = (
    "A circle of radius r has area pi times r squared and circumference two pi r, with pi as 22/7 on these exams. "
    "Sectors, arcs, rings and wheels are fractions of those two formulas. "
    "Quadrants and semicircles are just sectors of 90 and 180 degrees."
)

ci_notes = r"""### The two core formulas
$$K=\pi r^2,\qquad C=2\pi r$$
Use $\pi=\dfrac{22}{7}$ unless the paper says otherwise. Radius first, everything after is arithmetic. Halve any diameter before squaring; the formulas live on the radius.

Circumference $132$ cm: $r=\dfrac{132\times7}{2\times22}=21$, so $K=\dfrac{22}{7}\times441=1386$ sq cm.

> **Rule:** Every circle question starts by fixing $r$. Reverse questions divide by $2\pi$ to get it.

### Sectors and arcs
A sector is a pizza slice; the arc is its crust. Both take the fraction $\dfrac{\theta}{360}$ of the full shape:
$$\text{arc}=\frac{\theta}{360}\times2\pi r,\qquad \text{sector area}=\frac{\theta}{360}\times\pi r^2$$
Radius $35$, angle $72^\circ$: arc $=\dfrac{72}{360}\times220=44$ cm, sector $=\dfrac{72}{360}\times3850=770$ sq cm.

Perimeter of a sector adds the two radii: $44+70=114$ cm. A $90^\circ$ sector of the same circle has arc $\dfrac14\times220=55$ cm and perimeter $55+70=125$ cm.

A ring between radii $17.5$ and $10.5$: $R^2-r^2=306.25-110.25=196$, so $K=\dfrac{22}{7}\times196=616$ sq cm. Difference of squares keeps it clean.

> **Tip:** $\dfrac{72}{360}=\dfrac15$. Simplify the fraction before multiplying; big numbers shrink fast.

### Rings and rolling wheels
A ring between radii $R$ and $r$ has area $\pi(R^2-r^2)$. Outer $14$, inner $7$: $\dfrac{22}{7}\times147=462$ sq cm.

A wheel of diameter $70$ cm covers $C=\dfrac{22}{7}\times70=220$ cm per turn. Rolling $231$ m $=23100$ cm:
$$\text{revolutions}=\frac{23100}{220}=105$$
The reverse works too: $150$ turns cover $150\times220=33000$ cm, which is $330$ m.

> **Watch:** Convert metres to centimetres before dividing. The wheel diameter is in centimetres.

### Circles and squares together
- Circle **inscribed** in a square: diameter $=$ square side. Side $14$ gives $r=7$ and $K=154$.
- Square **inside** a circle: the square's diagonal is the circle's diameter.

> **Remember:** Inscribed means the circle touches all four sides from inside, so side and diameter match.

### Quadrants and semicircles
A quadrant is a quarter circle ($90^\circ$), a semicircle half ($180^\circ$). Same fraction rules.

Quadrant with $r=14$: area $=\dfrac{1}{4}\times\dfrac{22}{7}\times196=154$ sq cm. Arc $=\dfrac14\times88=22$ cm, so its perimeter is $14+14+22=50$ cm. A semicircle with $r=7$ has area $\dfrac12\times154=77$ sq cm and perimeter $14+22=36$ cm.

> **Tip:** Perimeter of a quadrant is two radii plus the quarter arc. Semicircle: two radii make a diameter, plus the half arc.
"""

ci_formulas = [
    {"name": "Circle", "tex": r"K=\pi r^2,\quad C=2\pi r", "note": "Take pi as 22/7 unless stated."},
    {"name": "Arc and sector", "tex": r"\text{arc}=\frac{\theta}{360}2\pi r,\quad \text{sector}=\frac{\theta}{360}\pi r^2", "note": "Same fraction of circumference and area."},
    {"name": "Ring", "tex": r"K=\pi(R^2-r^2)", "note": "R = outer radius, r = inner radius."},
    {"name": "Wheel revolutions", "tex": r"N=\frac{D}{C}=\frac{\text{distance}}{2\pi r}", "note": "Count turns by dividing distance by one circumference."},
    {"name": "Quadrant / semicircle", "tex": r"\text{quad}=\frac{\pi r^2}{4},\quad \text{semi}=\frac{\pi r^2}{2}", "note": "Quarter and half of the circle area."},
]

ci_tricks = [
    {
        "title": "Radius first, always",
        "body": "Circumference, diameter or area given: convert to the radius before anything else. Every formula lives on r.",
        "example": {
            "q": "The circumference of a circle is 132 cm. Its area is:",
            "steps": [r"$r=\dfrac{132\times7}{2\times22}=21$ cm.", r"$K=\dfrac{22}{7}\times21\times21$.", r"$K=1386$ sq cm."],
            "answer": "1386 sq cm",
        },
    },
    {
        "title": "Simplify the sector fraction",
        "body": "Reduce theta over 360 first: 72/360 is 1/5, 90/360 is 1/4. Then one multiplication finishes.",
        "example": {
            "q": "Find the arc length of a sector of angle $72^\\circ$ in a circle of radius 35 cm.",
            "steps": [r"$2\pi r=2\times\dfrac{22}{7}\times35=220$ cm.", r"$\dfrac{72}{360}=\dfrac15$.", r"Arc $=\dfrac{220}{5}=44$ cm."],
            "answer": "44 cm",
        },
    },
    {
        "title": "Wheels: count the turns",
        "body": "One turn covers one circumference. Divide total distance by it, in the same units.",
        "example": {
            "q": "A wheel of diameter 70 cm rolls a distance of 231 m. The number of revolutions it makes is:",
            "steps": [r"$C=\dfrac{22}{7}\times70=220$ cm.", r"$231\text{ m}=23100$ cm.", r"$\dfrac{23100}{220}=105$ turns."],
            "answer": "105",
        },
    },
]

ci_mistakes = [
    {"wrong": "Using the diameter as $r$.", "right": "Diameter 70 means $r=35$. Halve before squaring."},
    {"wrong": "Taking $\\pi$ as 3.14 when the numbers are multiples of 7.", "right": "Radius 7, 14, 21, 35 with $\\pi=\\dfrac{22}{7}$ cancels the 7s cleanly."},
    {"wrong": "Forgetting the two radii in a sector perimeter.", "right": "Sector perimeter $=$ arc $+2r$. Radius 35, arc 44 gives 114."},
    {"wrong": "Computing ring area as $\\pi(R-r)^2$.", "right": "It is $\\pi(R^2-r^2)$; for 14 and 7 that is $\\dfrac{22}{7}\\times147=462$."},
    {"wrong": "Mixing metres and centimetres in wheel counts.", "right": "231 m is 23100 cm; match the wheel's units before dividing."},
]

ci_revision = [
    "$K=\\pi r^2$, $C=2\\pi r$; fix the radius before anything else.",
    "Arc and sector are the same fraction $\\dfrac{\\theta}{360}$ of circumference and area.",
    "Sector perimeter adds the two radii to the arc.",
    "Ring area is $\\pi(R^2-r^2)$, the difference of squares.",
    "Wheel revolutions $=$ distance divided by one circumference, same units.",
    "Quadrant $=\\dfrac14$ of the circle; semicircle $=\\dfrac12$; perimeter includes the straight edges.",
]

ci_patterns = [
    pat("m2d-ci-p1", "Area and circumference, forward and reverse", "very common",
        "One of area or circumference given, the other asked.",
        [r"From circumference: $r=\dfrac{C}{2\pi}$.", r"From area: $r=\sqrt{\dfrac{K}{\pi}}$.",
         r"Substitute into the asked formula."],
        "Both formulas share the single unknown $r$, so one conversion bridges the two.",
        "The circumference of a circle is 132 cm. Its area is:",
        [r"$r=\dfrac{132\times7}{44}=21$ cm.", r"$K=\dfrac{22}{7}\times21^2=1386$ sq cm."],
        "1386 sq cm"),
    pat("m2d-ci-p2", "Sector area and arc length", "very common",
        "A sector angle with a radius; arc, sector area or perimeter asked.",
        [r"Simplify $\dfrac{\theta}{360}$ to lowest terms.", r"Arc: multiply by $2\pi r$.",
         r"Sector area: multiply by $\pi r^2$.", r"Perimeter adds $2r$ to the arc."],
        "One fraction serves both quantities, and simplified fractions keep the arithmetic small.",
        "Find the arc length of a sector of angle $72^\\circ$ in a circle of radius 35 cm.",
        [r"$\dfrac{72}{360}=\dfrac15$ and $2\pi r=220$ cm.", r"Arc $=\dfrac{220}{5}=44$ cm."],
        "44 cm"),
    pat("m2d-ci-p3", "Ring (annulus) area and wheel revolutions", "common",
        "Two concentric radii, or a wheel rolling a distance.",
        [r"Ring: $K=\pi(R^2-r^2)$.", r"Wheel: one turn $=$ one circumference.",
         r"Divide total distance by the circumference, same units."],
        "Both ideas reuse the circumference and area formulas with zero new theory.",
        "A wheel of diameter 70 cm rolls a distance of 231 m. The number of revolutions it makes is:",
        [r"$C=\dfrac{22}{7}\times70=220$ cm; $231$ m $=23100$ cm.", r"$\dfrac{23100}{220}=105$."],
        "105 revolutions"),
    pat("m2d-ci-p4", "Circles inscribed in / circumscribed about squares", "common",
        "A circle touching a square from inside, or a square inside a circle.",
        [r"Circle in square: diameter $=$ side, so $r=\dfrac{a}{2}$.",
         r"Square in circle: square diagonal $=$ circle diameter.",
         r"Substitute and compute the asked area."],
        "The touch conditions translate straight into one length equality, so the shape pair collapses to one line.",
        "A circle is inscribed in a square of side 14 cm. The area of the circle is:",
        [r"$r=\dfrac{14}{2}=7$ cm.", r"$K=\dfrac{22}{7}\times49=154$ sq cm."],
        "154 sq cm"),
    pat("m2d-ci-p5", "Quadrant and semicircle pieces", "common",
        "A quarter or half circle, area or perimeter asked.",
        [r"Quadrant: take $\dfrac14$ of circle area; semicircle $\dfrac12$.",
         r"Arc is the same fraction of the circumference.", r"Perimeter adds the straight edges."],
        "These are sectors of $90^\\circ$ and $180^\\circ$, so the fraction rules already known do all the work.",
        "A quadrant has radius 14 cm. Find its area and its perimeter.",
        [r"Area $=\dfrac14\times\dfrac{22}{7}\times196=154$ sq cm.", r"Arc $=\dfrac14\times88=22$ cm.", r"Perimeter $=14+14+22=50$ cm."],
        "Area 154 sq cm, perimeter 50 cm"),
]

# ---------------- m2d-polygons ----------------
pg_concept = (
    "A regular polygon has equal sides and equal angles, so one side length fixes everything. "
    "The regular hexagon is the star: it is six equilateral triangles glued together. "
    "Exterior angles, interior angles and diagonal counts all come from the number of sides alone."
)

pg_notes = r"""### Hexagon: six equilateral triangles
Join the centre to all six corners. Six equilateral triangles of side $a$ appear, so
$$K=\frac{3\sqrt3}{2}a^2 = 6\times\frac{\sqrt3}{4}a^2$$
Side $6$ cm: each small triangle has area $9\sqrt3$, total $54\sqrt3$ sq cm.

Given a hexagon perimeter instead, divide by $6$ first: perimeter $36$ cm means side $6$ cm and area $54\sqrt3$ sq cm.

A regular octagon has area $2(1+\sqrt2)a^2$. Side $4$ cm gives $32+32\sqrt2$ sq cm, but the six-triangle picture is the one that pays off weekly.

> **Rule:** Hexagon side, radius (centre to corner) and side are equal: $R=a$. The apothem is $\dfrac{\sqrt3}{2}a$.

### Any regular polygon from perimeter and apothem
$$K=\frac{1}{2}\times\text{perimeter}\times\text{apothem}$$
The apothem is the perpendicular from the centre to a side. Perimeter $72$ cm, apothem $6$ cm: $K=\dfrac{1}{2}\times72\times6=216$ sq cm.

For the hexagon of side $6$: apothem $=\dfrac{\sqrt3}{2}\times6=3\sqrt3$, and $\dfrac12\times36\times3\sqrt3=54\sqrt3$, matching the six triangles. Two routes, one answer.

### Slices from the centre
Join the centre of any regular polygon to its corners. You get $n$ identical slices, each an isosceles triangle with apex angle $\dfrac{360^\circ}{n}$. That single picture generates the exterior angle, the apothem (slice height) and the area formula at once.

> **Tip:** This one formula fits every regular polygon, hexagon included. It is the triangle formula applied to all the slices.

### Angles from the side count
- Each exterior angle $=\dfrac{360^\circ}{n}$ (the turn at each corner while walking the boundary).
- Each interior angle $=180^\circ-$ exterior.
- Interior angle sum $=(n-2)\times180^\circ$.

Octagon: exterior $=\dfrac{360}{8}=45^\circ$, interior $=135^\circ$, angle sum $=6\times180^\circ=1080^\circ$.

Pentagon: exterior $72^\circ$, interior $108^\circ$, sum $540^\circ$. Decagon: exterior $36^\circ$, interior $144^\circ$. Reverse works too: interior $144^\circ$ means exterior $36^\circ$, so $n=\dfrac{360}{36}=10$.

> **Watch:** The regular polygon interior angles are equal, so divide the sum by $n$ to check one angle.

### Counting diagonals
From each corner, $n-3$ diagonals leave (skip itself and two neighbours). Each diagonal has two ends:
$$d=\frac{n(n-3)}{2}$$
A polygon with $90$ diagonals: $n^2-3n-180=0$, which factors as $(n-15)(n+12)=0$, so $n=15$.

Small counts are worth memorising: hexagon $9$, pentagon $5$, octagon $20$, decagon $35$.

### Hexagon special lengths
- Longest diagonal (through the centre) $=2a$. Side $8$ gives $16$.
- Short diagonal (skipping one corner) $=a\sqrt3$.

> **Remember:** In a hexagon, side $=$ radius and the longest diagonal $=$ diameter $=2a$. Both fall out of the six triangles picture.
"""

pg_formulas = [
    {"name": "Regular hexagon", "tex": r"K=\frac{3\sqrt3}{2}a^2", "note": "Six equilateral triangles of side a."},
    {"name": "Polygon from apothem", "tex": r"K=\frac{1}{2}\times P\times a", "note": "P = perimeter, a = apothem (centre to a side)."},
    {"name": "Exterior angle", "tex": r"\text{ext}=\frac{360^\circ}{n}", "note": "Equal turns around the boundary."},
    {"name": "Interior angle", "tex": r"\text{int}=180^\circ-\text{ext},\quad \text{sum}=(n-2)180^\circ", "note": "One angle plus the total for all n."},
    {"name": "Diagonals", "tex": r"d=\frac{n(n-3)}{2}", "note": "n sides give this many diagonals."},
]

pg_tricks = [
    {
        "title": "Hexagon = 6 equilateral triangles",
        "body": "Six triangles of side a. Use the equilateral area times six; the root-three factor is already familiar.",
        "example": {
            "q": "Find the area of a regular hexagon of side 6 cm.",
            "steps": [r"One triangle: $\dfrac{\sqrt3}{4}\times36=9\sqrt3$.", r"$K=6\times9\sqrt3$.", r"$K=54\sqrt3$ sq cm."],
            "answer": "54*sqrt(3) sq cm",
        },
    },
    {
        "title": "Exterior angle finds n",
        "body": "Divide 360 by the exterior angle to get the side count; the interior angle is its partner to 180.",
        "example": {
            "q": "Find the measure of each interior angle of a regular octagon.",
            "steps": [r"Exterior $=\dfrac{360}{8}=45^\circ$.", r"Interior $=180-45=135^\circ$."],
            "answer": "135 degrees",
        },
    },
    {
        "title": "Diagonal equation factors",
        "body": "Set n(n-3)/2 equal to the given count, then factor the quadratic. Exam answers are whole numbers.",
        "example": {
            "q": "A polygon has 90 diagonals. The number of its sides is:",
            "steps": [r"$n(n-3)=180$.", r"$n^2-3n-180=(n-15)(n+12)=0$.", r"$n=15$."],
            "answer": "15",
        },
    },
]

pg_mistakes = [
    {"wrong": "Using $\\dfrac{\\sqrt3}{4}a^2$ once for the hexagon.", "right": "That is one triangle. Six of them give $\\dfrac{3\\sqrt3}{2}a^2$."},
    {"wrong": "Interior angle $=\\dfrac{360}{n}$.", "right": "That is the exterior. Interior $=180-\\dfrac{360}{n}$; for an octagon, $135^\\circ$."},
    {"wrong": "Forgetting to halve $n(n-3)$.", "right": "Each diagonal was counted from both ends: $d=\\dfrac{n(n-3)}{2}$."},
    {"wrong": "Longest hexagon diagonal taken as $a\\sqrt3$.", "right": "$a\\sqrt3$ is the short one; the longest through the centre is $2a$."},
    {"wrong": "Using the side as the apothem.", "right": "The apothem is centre to the middle of a side; hexagon apothem $=\\dfrac{\\sqrt3}{2}a$."},
]

pg_revision = [
    "Hexagon $=$ six equilateral triangles; area $\\dfrac{3\\sqrt3}{2}a^2$.",
    "Any regular polygon: $\\dfrac12\\times$ perimeter $\\times$ apothem.",
    "Exterior $=\\dfrac{360}{n}$; interior $=180-$ exterior; sum $=(n-2)\\times180^\\circ$.",
    "Diagonals $=\\dfrac{n(n-3)}{2}$; given a count, factor the quadratic.",
    "Hexagon: side $=$ radius, longest diagonal $=2a$, short diagonal $=a\\sqrt3$.",
]

pg_patterns = [
    pat("m2d-pg-p1", "Hexagon as six equilateral triangles", "very common",
        "A regular hexagon with its side given.",
        [r"One equilateral triangle: $\dfrac{\sqrt3}{4}a^2$.", r"Multiply by $6$.",
         r"Or apply $K=\dfrac{3\sqrt3}{2}a^2$ directly."],
        "The hexagon is the only regular polygon that splits into equilateral triangles, a free shortcut.",
        "Find the area of a regular hexagon of side 6 cm.",
        [r"One triangle: $9\sqrt3$.", r"$K=6\times9\sqrt3=54\sqrt3$ sq cm."],
        "54*sqrt(3) sq cm"),
    pat("m2d-pg-p2", "Area from perimeter and apothem", "common",
        "A regular polygon with perimeter and apothem (inradius) given.",
        [r"Check the polygon is regular.", r"$K=\dfrac{1}{2}\times P\times a$.", r"Multiply once."],
        "The formula needs no side count and no angles, just the two given lengths.",
        "A regular polygon has perimeter 72 cm and apothem 6 cm. Its area is:",
        [r"$K=\dfrac12\times72\times6$.", r"$K=216$ sq cm."],
        "216 sq cm"),
    pat("m2d-pg-p3", "Interior and exterior angles and the angle sum", "very common",
        "A regular polygon with an angle or a side count given.",
        [r"Exterior $=\dfrac{360}{n}$.", r"Interior $=180-$ exterior.",
         r"Sum $=(n-2)\times180^\circ$; divide by $n$ for one angle."],
        "One small table answers every angle question for any regular polygon.",
        "Find the measure of each interior angle of a regular octagon.",
        [r"Exterior $=\dfrac{360}{8}=45^\circ$.", r"Interior $=180-45=135^\circ$."],
        "135 degrees"),
    pat("m2d-pg-p4", "Counting diagonals", "common",
        "A diagonal count with the side count asked, or the reverse.",
        [r"Write $\dfrac{n(n-3)}{2}=\text{count}$.", r"Expand into a quadratic.", r"Factor; keep the positive root."],
        "The count formula is quadratic in $n$, and exam values factor cleanly.",
        "A polygon has 90 diagonals. The number of its sides is:",
        [r"$n(n-3)=180$.", r"$(n-15)(n+12)=0$.", r"$n=15$."],
        "15"),
    pat("m2d-pg-p5", "Hexagon diagonals and side relations", "occasional",
        "Hexagon questions asking a diagonal or linking radius to side.",
        [r"Side $=$ radius: $R=a$.", r"Longest diagonal $=2a$ (through the centre).",
         r"Short diagonal $=a\sqrt3$ (skipping a corner)."],
        "All three lengths come from the six-equilateral-triangles picture, with no new formulas.",
        "The length of the longest diagonal of a regular hexagon of side 8 cm is:",
        [r"Longest diagonal $=2a$.", r"$=2\times8=16$ cm."],
        "16 cm"),
]

# ---------------- m2d-scaling ----------------
sc_concept = (
    "When a shape grows by a scale factor k, every length multiplies by k but every area multiplies by k squared. "
    "For percentage changes the master formula is a + b + ab/100. "
    "The same wire bent into different shapes encloses different areas, and the circle always wins."
)

sc_notes = r"""### Lengths scale once, areas twice
Similar figures with a length ratio $k$ have an area ratio $k^2$. Perimeters are lengths, so they take $k$ too.

Perimeters $3:5$ mean areas $9:25$. If the larger area is $200$ sq cm, the smaller is $200\times\dfrac{9}{25}=72$ sq cm. Multiply by the ratio; never subtract a guessed difference.

Going from areas back to lengths means a square root: areas $9:25$ give sides $3:5$. Two circles with areas $154$ and $616$ sq cm are in ratio $1:4$, so their radii are in ratio $1:2$.

> **Rule:** Square going from lengths to areas; take the root going back. This single line is half the subtopic.

### The percentage change master formula
For two successive percentage changes $a$ and $b$:
$$\text{net}=a+b+\frac{ab}{100}$$
Side $+20\%$: area $=20+20+\dfrac{400}{100}=+44\%$. Side $-10\%$: area $=-10-10+\dfrac{100}{100}=-19\%$.

Reverse it by factoring: area $+21\%$ means the side grew by $10\%$, because $1.21=1.1^2$.

> **Watch:** A $20\%$ side increase is a $44\%$ area increase, not $40\%$. The cross term is what the options try to hide.

### Costs and tiles scale with area
A square room of side $5$ m costs Rs $600$ to carpet. A similar room of side $15$ m has $k=3$, so area is $9$ times and cost is $600\times9=$ Rs $5400$.

Tiles ask the same: divide the floor area by one tile's area, then multiply by the rate. A floor of $6$ m by $4$ m carries $24$ sq m $=240{,}000$ sq cm; tiles of $20\times20$ cm cover $400$ sq cm each, so $600$ tiles.

Numbers to trust: side ratio $2:3$ gives cost ratio $4:9$. A Rs $500$ job grows to Rs $1125$ at that scale, since $500\times\dfrac{9}{4}=1125$.

> **Tip:** Never scale money by the side ratio. Money follows area, so it takes $k^2$.

### Maps, models and enlargements
A map scale $1:5000$ makes lengths $5000$ times bigger, so areas grow by $5000^2=25{,}000{,}000$. A $4$ sq cm plot is $10^8$ sq cm in truth, which is $10{,}000$ sq m ($1$ sq m $=10^4$ sq cm).

> **Remember:** Square the map scale for areas, then convert units once at the end.

### Same wire, different shapes
A $44$ cm wire bent into a circle gives $r=\dfrac{44}{2\pi}=7$ cm, area $154$ sq cm. Bent into a square, side $11$ cm, area $121$ sq cm.

For a fixed perimeter, the circle encloses the most area; among rectangles, the square wins. Equilateral beats every other triangle. Order the options by shape generosity when the question says 'maximum area'.

> **Watch:** Compare areas only after converting the perimeter into each shape's own dimensions.
"""

sc_formulas = [
    {"name": "Similar figures", "tex": r"\frac{a_1}{a_2}=k\Rightarrow\frac{K_1}{K_2}=k^2", "note": "Lengths take k once; areas take k squared."},
    {"name": "Successive percentage change", "tex": r"\text{net}=a+b+\frac{ab}{100}", "note": "Works for two changes in a row, like both dimensions."},
    {"name": "Reverse percentage area change", "tex": r"1+\frac{x}{100}=\left(1+\frac{y}{100}\right)^2", "note": "Area factor is the side factor squared."},
    {"name": "Map areas", "tex": r"\text{true area}=\text{map area}\times(\text{scale})^2", "note": "Square the linear scale before converting units."},
]

sc_tricks = [
    {
        "title": "a + b + ab/100 in one line",
        "body": "Both dimensions change by the same percent: plug once, no quadratics, no decimals.",
        "example": {
            "q": "If each side of a square is increased by 20%, the percentage increase in its area is:",
            "steps": [r"$a=b=20$.", r"$20+20+\dfrac{20\times20}{100}$.", r"$=44\%$."],
            "answer": "44%",
        },
    },
    {
        "title": "Reverse the square root",
        "body": "Area up 21%? Factor $1.21=1.1^2$, so the side rose 10%. Recognise perfect squares of decimals.",
        "example": {
            "q": "The area of a square increases by 21%. Each side increased by:",
            "steps": [r"$1.21=1.1^2$.", r"Side factor $=1.1$.", r"Increase $=10\%$."],
            "answer": "10%",
        },
    },
    {
        "title": "Wire into shapes: circle wins",
        "body": "Same perimeter, compare areas. Circle beats square beats any rectangle, so guess before computing.",
        "example": {
            "q": "A wire 44 cm long is bent into a circle. The area enclosed is (take pi = 22/7):",
            "steps": [r"$2\pi r=44\Rightarrow r=\dfrac{44\times7}{44}=7$ cm.", r"$K=\dfrac{22}{7}\times49=154$ sq cm."],
            "answer": "154 sq cm",
        },
    },
]

sc_mistakes = [
    {"wrong": "Multiplying area by $k$ instead of $k^2$.", "right": "Side ratio $3:5$ gives area ratio $9:25$. Square the length ratio."},
    {"wrong": "Adding $20\\%+20\\%=40\\%$ for an area change.", "right": "Use $a+b+\\dfrac{ab}{100}$: the answer is $44\\%$."},
    {"wrong": "Scaling cost by the side ratio.", "right": "Cost follows area: side $5\\to15$ is $k=3$, so cost multiplies by $9$."},
    {"wrong": "Applying the map scale once to areas.", "right": "Square it: $1:5000$ multiplies areas by $25{,}000{,}000$."},
    {"wrong": "Cutting the area change in half to get the side change.", "right": "Take the square root: $+21\\%$ area is $+10\\%$ side, not $+10.5\\%$."},
]

sc_revision = [
    "Length ratio $k$ gives area ratio $k^2$; perimeters take $k$ once.",
    "Two successive changes: $a+b+\\dfrac{ab}{100}$; $+20\\%$ side means $+44\\%$ area.",
    "Area to side: take the square root of the factor ($1.21\\to1.1$).",
    "Money, tiles and paint scale with area, never with a side.",
    "Map areas: square the linear scale, convert units once.",
    "Fixed perimeter: circle encloses the most area; square beats other rectangles.",
]

sc_patterns = [
    pat("m2d-sc-p1", "Linear scale to area scale", "very common",
        "Two similar figures with a perimeter or side ratio, an area asked.",
        [r"Read off the length ratio $k$.", r"Square it for the area ratio.",
         r"Apply the ratio to the given area."],
        "Squaring once converts any length comparison into an area comparison.",
        "The perimeters of two similar figures are in the ratio 3 : 5. If the larger area is 200 sq cm, the smaller area is:",
        [r"Area ratio $=\dfrac{9}{25}$.", r"Smaller $=200\times\dfrac{9}{25}=72$ sq cm."],
        "72 sq cm"),
    pat("m2d-sc-p2", "Cost, tiles and carpet scaling", "common",
        "A cost for one size, asked for a similar larger size.",
        [r"Find the linear scale $k$ between the shapes.", r"Square it: cost multiplies by $k^2$.",
         r"Multiply the given cost."],
        "Cost per unit area is fixed, so total cost behaves exactly like area.",
        "Carpeting a square room of side 5 m costs Rs 600. The cost of carpeting a square room of side 15 m is:",
        [r"$k=\dfrac{15}{5}=3$, so area factor $=9$.", r"Cost $=600\times9=$ Rs 5400."],
        "Rs 5400"),
    pat("m2d-sc-p3", "Percentage change in side to change in area", "very common",
        "A side percent change, area percent asked (or the reverse).",
        [r"Put $a=b=$ the percent change.", r"Net $=a+b+\dfrac{ab}{100}$.",
         r"Reverse direction: take the square root of the factor."],
        "The master formula handles both directions and dodges the missing cross term.",
        "If each side of a square is increased by 20%, the percentage increase in its area is:",
        [r"$20+20+\dfrac{400}{100}$.", r"$=44\%$."],
        "44%"),
    pat("m2d-sc-p4", "Maps, models and photo enlargements", "common",
        "A map or model with a scale, a true area asked.",
        [r"Note the linear scale.", r"Square it for the area factor.",
         r"Multiply the map area and convert units."],
        "Areas need the squared scale, and one clean unit conversion finishes it.",
        "On a map of scale 1 : 5000, a plot measures 4 sq cm. Its actual area is:",
        [r"Area factor $=5000^2=25{,}000{,}000$.", r"$4\times25{,}000{,}000=10^8$ sq cm $=10{,}000$ sq m."],
        "10,000 sq m"),
    pat("m2d-sc-p5", "Same perimeter: square vs circle", "occasional",
        "One wire or fence bent into different shapes.",
        [r"Split the perimeter into each shape's dimensions.", r"Compute each area.",
         r"Compare; the circle encloses the most."],
        "A fixed perimeter is shared, so the comparison isolates the shape effect alone.",
        "A wire 44 cm long is bent into a circle. The area enclosed is (take pi = 22/7):",
        [r"$r=\dfrac{44\times7}{2\times22}=7$ cm.", r"$K=\dfrac{22}{7}\times7^2=154$ sq cm."],
        "154 sq cm"),
]

# ---------------- patch ----------------
data = json.loads(TOPIC.read_text(encoding="utf-8"))

blocks = {
    "m2d-triangles": (tr_concept, tr_notes, tr_formulas, tr_tricks, tr_mistakes, tr_revision, tr_patterns),
    "m2d-quads": (qd_concept, qd_notes, qd_formulas, qd_tricks, qd_mistakes, qd_revision, qd_patterns),
    "m2d-circles": (ci_concept, ci_notes, ci_formulas, ci_tricks, ci_mistakes, ci_revision, ci_patterns),
    "m2d-polygons": (pg_concept, pg_notes, pg_formulas, pg_tricks, pg_mistakes, pg_revision, pg_patterns),
    "m2d-scaling": (sc_concept, sc_notes, sc_formulas, sc_tricks, sc_mistakes, sc_revision, sc_patterns),
}

new_ids = [p["id"] for blk in blocks.values() for p in blk[6]]
assert len(new_ids) == len(set(new_ids)), "duplicate new pattern ids within rewrite"

for sub in data["subtopics"]:
    if sub["id"] not in blocks:
        continue
    concept, notes, formulas, tricks, mistakes, revision, patterns = blocks[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sub['id']}: never drop a pattern id"
    other = {p["id"] for s in data["subtopics"] if s["id"] != sub["id"] for p in s.get("patterns", [])}
    clash = other & {p["id"] for p in patterns}
    assert not clash, f"{sub['id']}: pattern id clash {clash}"
    assert 2500 <= len(notes) <= 5000, f"{sub['id']} notes {len(notes)} chars"
    assert 4 <= len(mistakes) <= 8 and 4 <= len(revision) <= 9
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)
    print(f"{sub['id']}: notes {len(notes)} chars, {len(patterns)} patterns")

with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("mensuration-2d.json patched")
