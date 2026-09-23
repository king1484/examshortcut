import sympy as sp
from qa_common import Q, F, T, S, P, U, write_topic

PI = sp.Rational(22, 7)

# ---------------------------------------------------------------- sanity checks
assert 2 * (24 + 18) == 84
assert sp.sqrt(484) == 22 and 4 * 22 == 88
assert 2 * PI * 21 == 132
assert sp.sqrt(3) / 4 * 12**2 == 36 * sp.sqrt(3)
assert sp.Rational(1, 2) * (14 + 10) * 8 == 96
assert sp.Rational(120, 100) * sp.Rational(90, 100) == sp.Rational(108, 100)
assert sp.Rational(45, 360) * PI * 14**2 == 77
assert sp.Rational(1, 2) * 12 * 16 == 96
assert PI * (21**2 - 14**2) == 770
assert sp.Rational(14, 2) ** 2 * 2 == 98  # largest square in circle r=7
assert 300 * sp.Rational(22, 7) * sp.Rational(70, 100) == 660  # wheel metres
assert sp.sqrt(3) * 3 / 2 * 6**2 == 54 * sp.sqrt(3)
assert PI * 14**2 == 616 and 22**2 == 484 and sp.Rational(616, 484) == sp.Rational(14, 11)
r_ = sp.Rational(88, 2) / PI
assert r_ == 14 and PI * 14**2 == 616
assert (66 * 46) - (60 * 40) == 636 and 636 * 5 == 3180

FIG_TRAPEZIUM = (
    '<svg viewBox="0 0 260 160" width="260" stroke="currentColor" fill="none">'
    '<polygon points="40,130 220,130 170,40 90,40" stroke-width="1.5"/>'
    '<line x1="130" y1="40" x2="130" y2="130" stroke-dasharray="4 3"/>'
    '<text x="30" y="150" fill="currentColor" stroke="none" font-size="14" font-family="sans-serif">a</text>'
    '<text x="214" y="150" fill="currentColor" stroke="none" font-size="14" font-family="sans-serif">b</text>'
    '<text x="136" y="90" fill="currentColor" stroke="none" font-size="14" font-family="sans-serif">h</text>'
    '</svg>')

# ---------------------------------------------------------------- subtopics
subtopics = [
S("m2d-triangles", "Areas of triangles",
r"""
Area of a triangle $=\frac12\times\text{base}\times\text{height}$. Special cases carry most CGL questions:
- **Equilateral** (side $a$): area $\frac{\sqrt3}{4}a^2$, height $\frac{\sqrt3}{2}a$.
- **Heron** for three sides $a,b,c$: semi-perimeter $s=\frac{a+b+c}{2}$, area $=\sqrt{s(s-a)(s-b)(s-c)}$.
- **Right triangle:** the two legs are base and height, area $=\frac12\,p\,b$.

For an equilateral triangle the inradius is $\frac{a}{2\sqrt3}$ and the circumradius is $\frac{a}{\sqrt3}$.
""",
[
F("General triangle", r"K=\frac12 b h"),
F("Equilateral triangle", r"K=\frac{\sqrt3}{4}a^2,\quad h=\frac{\sqrt3}{2}a"),
F("Heron's formula", r"s=\frac{a+b+c}{2},\quad K=\sqrt{s(s-a)(s-b)(s-c)}"),
F("Radii of an equilateral triangle", r"r_{\text{in}}=\frac{a}{2\sqrt3},\quad R=\frac{a}{\sqrt3}"),
],
[
T("Equilateral area from the side table",
r"""$\frac{\sqrt3}{4}=0.433$. Memorise: side 4 → $4\sqrt3$, side 6 → $9\sqrt3$, side 8 → $16\sqrt3$, side 12 → $36\sqrt3$,
side 10 → $25\sqrt3$. The coefficient is just $\left(\frac{\text{side}}{4}\right)^2$.""",
r"Find the area of an equilateral triangle of side 12 cm.",
r"$\frac{\sqrt3}{4}\times12^2=36\sqrt3$ sq cm."),
T("Heron with a triplet shortcut",
r"""If the sides form a Pythagorean triple the triangle is right-angled: use $\frac12\times$ legs directly.
13-14-15 is the classic non-right Heron case, area 84.""",
r"Find the area of the triangle with sides 13 cm, 14 cm, 15 cm.",
r"$s=21$, $K=\sqrt{21\times8\times7\times6}=84$ sq cm."),
],
[
r"Using $\frac{\sqrt3}{2}a^2$ (the height formula's coefficient) for the equilateral area.",
r"Heron: forgetting the square root at the end.",
r"Taking the longest side as the height in a right triangle — the legs are base and height.",
]),
S("m2d-quads", "Areas of quadrilaterals",
r"""
| Figure | Area | Perimeter / diagonal |
|---|---|---|
| Rectangle $l\times b$ | $lb$ | $2(l+b)$; diagonal $\sqrt{l^2+b^2}$ |
| Square (side $a$) | $a^2$ | $4a$; diagonal $a\sqrt2$ |
| Square (diagonal $d$) | $\frac{d^2}{2}$ | $2\sqrt2\,d$ |
| Parallelogram | $b\times h$ | — |
| Rhombus | $\frac12 d_1d_2$ | side $\sqrt{(d_1/2)^2+(d_2/2)^2}$ |
| Trapezium | $\frac12(a+b)h$ | — |
| Cyclic quadrilateral | $\sqrt{(s-a)(s-b)(s-c)(s-d)}$ | opposite angles sum to $180^\circ$ |

A square gives the **maximum area for a given perimeter** among quadrilaterals.
""",
[
F("Rectangle", r"K=lb,\quad P=2(l+b),\quad d=\sqrt{l^2+b^2}"),
F("Square", r"K=a^2=\frac{d^2}{2},\quad d=a\sqrt2"),
F("Rhombus", r"K=\frac{d_1d_2}{2}"),
F("Trapezium", r"K=\frac{(a+b)}{2}h"),
F("Cyclic quadrilateral (Brahmagupta)", r"K=\sqrt{(s-a)(s-b)(s-c)(s-d)}"),
],
[
T("Square from its diagonal",
r"""Area $=\frac{d^2}{2}$, side $=\frac{d}{\sqrt2}$. Halve any square-area question that gives a diagonal.""",
r"Find the area of the largest square that can be inscribed in a circle of radius 7 cm.",
r"Diagonal of the square $=$ diameter $=14$. Area $=\frac{14^2}{2}=98$ sq cm."),
T("Rhombus: the half-diagonals are a right triangle",
r"""Perimeter → side → half the other diagonal by Pythagoras → area by $\frac12d_1d_2$.
Triplets (6,8,10) and (5,12,13) appear constantly.""",
r"The perimeter of a rhombus is 40 cm and one diagonal is 12 cm. Find its area.",
r"Side $=10$, half-diagonal $=6$, other half-diagonal $=8$ → diagonals 12 and 16 → area $\frac12\times12\times16=96$ sq cm."),
],
[
r"Rhombus area computed as $d_1d_2$ (missing the half).",
r"Square from diagonal: using $d^2$ instead of $d^2/2$.",
r"Trapezium: adding the parallel sides but forgetting the half.",
]),
S("m2d-circles", "Circles, sectors and rings",
r"""
For a circle of radius $r$: area $\pi r^2$, circumference $2\pi r$ (use $\pi=\frac{22}{7}$ unless told otherwise).

- **Arc length:** $\frac{\theta}{360}\times2\pi r$; **sector area:** $\frac{\theta}{360}\times\pi r^2$ — the sector
  is just that fraction of the full circle.
- **Segment:** sector area minus the triangle formed by the two radii and the chord.
- **Ring (annulus):** $\pi(R^2-r^2)$ — a path of width $w$ around a circle has outer radius $r+w$.
- **Rolling wheel:** distance $=$ number of revolutions $\times$ circumference $=n\pi d$.
""",
[
F("Circle", r"K=\pi r^2,\quad C=2\pi r=\pi d"),
F("Sector", r"K=\frac{\theta}{360}\pi r^2,\quad \ell=\frac{\theta}{360}\,2\pi r"),
F("Segment", r"K=\frac{\theta}{360}\pi r^2-\frac12 r^2\sin\theta"),
F("Ring / path", r"K=\pi(R^2-r^2)=\pi(R+r)(R-r)"),
F("Rolling wheel", r"\text{distance}=n\pi d"),
],
[
T("Sector as a fraction of the circle",
r"""$\theta=60^\circ\to\frac16$, $90^\circ\to\frac14$, $45^\circ\to\frac18$, $120^\circ\to\frac13$ of the circle.
No separate formula needed.""",
r"Find the area of a sector of angle $45^\circ$ in a circle of radius 14 cm.",
r"$\frac18\times\frac{22}{7}\times14^2=\frac18\times616=77$ sq cm."),
T("Ring: difference of squares",
r"""$R^2-r^2=(R+r)(R-r)$: with a path of width $w$, $R-r=w$ and $R+r=2r+w$ — often a one-line answer.""",
r"A path 7 m wide runs around a circular park of radius 14 m. Find the area of the path.",
r"$\frac{22}{7}\times(21^2-14^2)=\frac{22}{7}\times245=770$ sq m."),
T("Wheel revolutions = distance / circumference",
r"""Convert the diameter to metres first: $d=70$ cm $=0.7$ m gives a 2.2 m circumference with $\pi=\frac{22}{7}$.""",
r"A wheel of diameter 70 cm makes 300 revolutions. How far does it travel?",
r"$300\times\frac{22}{7}\times0.7=300\times2.2=660$ m."),
],
[
r"Forgetting to add the path width when a path runs **around** a circle ($R=r+w$).",
r"Sector area taken as a fraction of the circumference, or arc length as a fraction of the area.",
r"Mixing units: radius in cm vs answer demanded in m.",
]),
S("m2d-polygons", "Regular polygons and inscribed figures",
r"""
- **Regular hexagon** (side $a$): area $\frac{3\sqrt3}{2}a^2$ — six equilateral triangles of side $a$.
- **Regular octagon:** area $2(1+\sqrt2)\,a^2$.
- Any regular $n$-gon: area $=\frac12\times\text{perimeter}\times\text{apothem}$.

**Standard inscriptions (most-tested):**
- Largest **square in a circle**: diagonal $=$ diameter.
- Largest **circle in a square**: diameter $=$ side of square.
- Largest **circle in an equilateral triangle**: $r=\frac{a}{2\sqrt3}$.
- Largest **triangle in a semicircle** is right-angled.
""",
[
F("Regular hexagon", r"K=\frac{3\sqrt3}{2}a^2=6\times\frac{\sqrt3}{4}a^2"),
F("Regular octagon", r"K=2(1+\sqrt2)a^2"),
F("Square in a circle", r"\text{diagonal}=\text{diameter}=2R"),
F("Circle in a square", r"d_{\text{circle}}=a"),
F("Circle in an equilateral triangle", r"r=\frac{a}{2\sqrt3}"),
],
[
T("Hexagon = six equilateral triangles",
r"""Multiply the equilateral area by 6: $\frac{3\sqrt3}{2}a^2$. Given the perimeter, divide by 6 first.""",
r"Find the area of a regular hexagon of perimeter 36 cm.",
r"Side $=6$: area $=\frac{3\sqrt3}{2}\times36=54\sqrt3$ sq cm."),
T("Inscribed square → the diameter is the diagonal",
r"""All four corners touch the circle, so the square's diagonal passes through the centre and equals the diameter.""",
r"A square is inscribed in a circle of radius $7\sqrt2$ cm. Find the side of the square.",
r"Diagonal $=14\sqrt2\Rightarrow$ side $=\frac{14\sqrt2}{\sqrt2}=14$ cm."),
],
[
r"Hexagon area computed with $\frac{\sqrt3}{4}a^2$ (one triangle) instead of six triangles.",
r"Inscribed vs circumscribed confusion: circle inside the triangle vs triangle inside the circle.",
r"Using the side where the diagonal (or vice versa) is required.",
]),
S("m2d-scaling", "Percentage change, similarity and re-bent shapes",
r"""
Three ideas cover the rest of 2-D mensuration:

1. **Linear scale $k$:** all lengths ×$k$ → areas ×$k^2$ (perimeters only ×$k$).
2. **Percentage change in area:** if length changes $a\%$ and breadth $b\%$, the area changes by
   $a+b+\frac{ab}{100}\%$ (negative signs for decreases).
3. **Re-bent wires / fences:** the perimeter (or circumference) is conserved — equate the perimeters of the two shapes.
""",
[
F("Scaling", r"\ell\to k\ell\ \Rightarrow\ K\to k^2K,\quad P\to kP"),
F("Successive change in area", r"\Delta\%=a+b+\frac{ab}{100}"),
F("Equal perimeter", r"P_1=P_2\ \text{(re-bent wire)}"),
F("Side change from area change", r"\Delta a\%=\left(\sqrt{1+\frac{\Delta K}{100}}-1\right)\times100"),
],
[
T("Two-dimensional percentage change",
r"""Apply $a+b+\frac{ab}{100}$ with signs. $+20\%$ and $-10\%$: $20-10-\frac{200}{100}=+8\%$.""",
r"The length of a rectangle increases by 20% and the breadth decreases by 10%. Find the percentage change in area.",
r"$20-10-\frac{20\times10}{100}=+8\%$ increase."),
T("Area change → side change via square root",
r"""The side multiplies by $\sqrt{\text{area factor}}$. An increase of 21% → factor 1.21 → side ×1.1 → +10%.""",
r"If the area of a square increases by 96%, by what percentage does its side increase?",
r"Factor $=1.96$, $\sqrt{1.96}=1.4$ → the side increases 40%."),
T("Re-bent wire: conserve the perimeter",
r"""Circumference $=$ perimeter of the new shape. Compare the two areas computed from the common length $L$.""",
r"A wire bent as a circle of circumference 88 cm is re-bent into a square. Find the ratio of the areas of the circle and the square.",
r"Circle: $r=\frac{88}{2\pi}=14$, area 616. Square: side $=\frac{88}{4}=22$, area 484. Ratio $616:484=14:11$."),
],
[
r"Applying $k^2$ to perimeters or $k$ to areas.",
r"Percentage formula with the wrong sign for a decrease.",
r"Re-bent shapes: equating areas instead of perimeters.",
]),
]

patterns = [
P("Rectangle/square perimeter-area combo", "very common",
  r"Perimeter and one relation between length and breadth given; find the area, or vice versa.",
  r"Set $l+b=\frac{P}{2}$ together with the relation; sum and difference give both sides without a quadratic."),
P("Sector and arc as fractions", "very common",
  r"A sector with angle like $45^\circ$, $60^\circ$, $120^\circ$; find its area or perimeter.",
  r"Straight fraction of the full circle; sector perimeter $=$ arc $+2r$."),
P("Path / ring around a shape", "common",
  r"A path of given width around a garden (circular or rectangular); find its area or the cost of paving.",
  r"Outer minus inner area; for circles use $(R+r)(R-r)$; rectangular: $(l+2w)(b+2w)-lb$."),
P("Percentage change of area", "very common",
  r"Sides change by percentages; find the change in area, or the area change gives the side change.",
  r"$a+b+\frac{ab}{100}$ with signs; invert with a square root when the area change is given."),
P("Largest figure inscribed in another", "common",
  r"Largest circle/square/triangle inside another standard shape.",
  r"Diagonal = diameter (square in circle), diameter = side (circle in square), $r=\frac{a}{2\sqrt3}$ (circle in equilateral triangle)."),
P("Wire re-bent between shapes", "occasional",
  r"Same wire forms a circle, then a square/rectangle; compare areas.",
  r"Perimeter conserved: find $r$ or the side from the same $L$; expect a clean ratio like 14:11."),
P("Wheel/track revolution distance", "common",
  r"Wheels of given diameter covering a distance in $n$ revolutions.",
  r"$n=\frac{\text{distance}}{\pi d}$; keep units identical (cm vs m)."),
]

# ---------------------------------------------------------------- solved examples
solved = []

solved.append(Q("m2d-s01",
r"The perimeter of a rectangle is 50 cm and its length is 5 cm more than its breadth. Find its area.",
[("150 sq cm", 150), ("160 sq cm", 160), ("144 sq cm", 144), ("169 sq cm", 169)], 150,
r"""
$l+b=\frac{50}{2}=25$ and $l-b=5$.

So $l=15$, $b=10$; area $=150$ sq cm.
""",
r"Sum 25, difference 5 → 15 and 10 directly. Area 150. Trap: 169 = $13^2$ if you misread the relation.",
"easy", "m2d-quads", "rectangle perimeter and area", 35))

solved.append(Q("m2d-s02",
r"Find the perimeter (in cm) of a sector of a circle of radius 7 cm with central angle $90^\circ$. [Use $\pi=\frac{22}{7}$]",
[25, 11, 39, 29], 25,
r"""
Arc $=\frac{90}{360}\times2\times\frac{22}{7}\times7=11$ cm.

Perimeter of sector $=$ arc $+2r=11+14=25$ cm.
""",
r"Quarter circle: arc 11, add two radii 14 → 25. Trap: 11 (arc only).",
"medium", "m2d-circles", "sector perimeter", 40))

solved.append(Q("m2d-s03",
r"A rectangular park is 60 m long and 40 m wide. A path 3 m wide is built all around it on the outside. Find the area of the path.",
[("636 sq m", 636), ("600 sq m", 600), ("672 sq m", 672), ("2,400 sq m", 2400)], 636,
r"""
Outer rectangle: $(60+6)\times(40+6)=66\times46=3036$ sq m.

Path area $=3036-2400=636$ sq m.
""",
r"Add the width **twice** on each dimension: $66\times46-60\times40=636$. The width joins both sides of each dimension.",
"medium", "m2d-quads", "path around a rectangle", 50))

solved.append(Q("m2d-s04",
r"If each side of an equilateral triangle is increased by 10%, then the percentage increase in its area is:",
[("21%", 21), ("20%", 20), ("11%", 11), ("10%", 10)], 21,
r"""
Area scales as the square of the side: $1.1^2=1.21$, i.e. a 21% increase.

Equivalently, $10+10+\frac{10\times10}{100}=21\%$.
""",
r"Square the factor: $(1.1)^2=1.21\Rightarrow+21\%$. Trap: 20% (ignoring the $ab/100$ term).",
"easy", "m2d-scaling", "percentage change of area", 30))

# ---------------------------------------------------------------- practice
pr = []

pr.append(Q("m2d-q01",
r"The length and breadth of a rectangle are 24 cm and 18 cm. Its perimeter is:",
[("84 cm", 84), ("42 cm", 42), ("432 cm", 432), ("72 cm", 72)], 84,
r"$P=2(l+b)=2\times42=84$ cm.",
r"$2\times(24+18)=84$. Trap: 432 is the area; 42 forgot to double.",
"easy", "m2d-quads", "rectangle perimeter", 20))

pr.append(Q("m2d-q02",
r"The area of a square is 484 sq cm. Its perimeter is:",
[("88 cm", 88), ("44 cm", 44), ("121 cm", 121), ("176 cm", 176)], 88,
r"Side $=\sqrt{484}=22$ cm; perimeter $=4\times22=88$ cm.",
r"$\sqrt{484}=22$, then ×4 = 88. Trap: 44 is $2\times$side.",
"easy", "m2d-quads", "square area to perimeter", 25))

pr.append(Q("m2d-q03",
r"The radius of a circular field is 21 m. The cost of fencing it at ₹10 per metre is: [Use $\pi=\frac{22}{7}$]",
[("₹1,320", 1320), ("₹1,380", 1380), ("₹13,860", 13860), ("₹1,100", 1100)], 1320,
r"Circumference $=2\times\frac{22}{7}\times21=132$ m. Cost $=132\times10=$ ₹1,320.",
r"$132$ m → ₹1320. Trap: ₹13,860 uses area ($\pi r^2$) instead of circumference.",
"easy", "m2d-circles", "fencing cost of a circle", 30))

pr.append(Q("m2d-q04",
r"The area of an equilateral triangle of side 12 cm is:",
[(r"$36\sqrt{3}$ sq cm", 36 * sp.sqrt(3)), (r"$24\sqrt{3}$ sq cm", 24 * sp.sqrt(3)), (r"$48\sqrt{3}$ sq cm", 48 * sp.sqrt(3)), (r"$72\sqrt{3}$ sq cm", 72 * sp.sqrt(3))], 36 * sp.sqrt(3),
r"$K=\frac{\sqrt3}{4}a^2=\frac{\sqrt3}{4}\times144=36\sqrt3$ sq cm.",
r"$\frac{144}{4}=36$ → $36\sqrt3$. Trap: $24\sqrt3$ comes from the height formula $\frac{\sqrt3}{2}a$.",
"easy", "m2d-triangles", "equilateral triangle area", 25))

pr.append(Q("m2d-q05",
r"The parallel sides of a trapezium are 14 cm and 10 cm, and the distance between them is 8 cm. Its area is:",
[("96 sq cm", 96), ("192 sq cm", 192), ("48 sq cm", 48), ("100 sq cm", 100)], 96,
r"$K=\frac12(a+b)h=\frac12\times24\times8=96$ sq cm.",
r"Sum 24, half is 12, ×8 = 96. Trap: 192 missed the half.",
"easy", "m2d-quads", "trapezium area", 25, FIG_TRAPEZIUM))

pr.append(Q("m2d-q06",
r"The length of a rectangle increases by 20% and the breadth decreases by 10%. The percentage change in its area is:",
[("8% increase", 8), ("10% increase", 10), ("8% decrease", -8), ("No change", 0)], 8,
r"$\Delta\%=20-10-\frac{20\times10}{100}=+8\%$ — an 8% increase.",
r"$20-10-2=+8$. Traps: 10% (ignores the cross term), 'no change' (assumes cancellation).",
"medium", "m2d-scaling", "successive change in area", 35))

pr.append(Q("m2d-q07",
r"A sector of a circle has radius 14 cm and central angle $45^\circ$. Its area is: [Use $\pi=\frac{22}{7}$]",
[("77 sq cm", 77), ("154 sq cm", 154), ("88 sq cm", 88), ("616 sq cm", 616)], 77,
r"$K=\frac{45}{360}\times\frac{22}{7}\times14^2=\frac18\times616=77$ sq cm.",
r"$45^\circ=\frac18$ of a circle: $616/8=77$. Trap: 616 is the whole circle.",
"medium", "m2d-circles", "sector area", 35))

pr.append(Q("m2d-q08",
r"The perimeter of a rhombus is 40 cm and one of its diagonals is 12 cm. The area of the rhombus is:",
[("96 sq cm", 96), ("120 sq cm", 120), ("192 sq cm", 192), ("60 sq cm", 60)], 96,
r"""Side $=10$ cm. Half of the given diagonal $=6$, so the other half-diagonal $=\sqrt{10^2-6^2}=8$, giving
diagonals 12 and 16. Area $=\frac12\times12\times16=96$ sq cm.""",
r"6-8-10 triplet with the half-diagonals: other diagonal 16, area $\frac12\times12\times16=96$.",
"medium", "m2d-quads", "rhombus from perimeter and diagonal", 45))

pr.append(Q("m2d-q09",
r"A path 7 m wide runs around a circular park of radius 14 m. The area of the path is: [Use $\pi=\frac{22}{7}$]",
[("770 sq m", 770), ("616 sq m", 616), ("308 sq m", 308), ("1,386 sq m", 1386)], 770,
r"""Outer radius $=14+7=21$ m.

Path area $=\frac{22}{7}(21^2-14^2)=\frac{22}{7}\times245=770$ sq m.""",
r"$\frac{22}{7}\times(441-196)=770$. Trap: 616 forgets the path width.",
"medium", "m2d-circles", "circular path area", 45))

pr.append(Q("m2d-q10",
r"The diagonal of a rectangle is 25 cm and one of its sides is 15 cm. The area of the rectangle is:",
[("300 sq cm", 300), ("375 sq cm", 375), ("325 sq cm", 325), ("240 sq cm", 240)], 300,
r"""Other side $=\sqrt{25^2-15^2}=\sqrt{625-225}=20$ cm.

Area $=15\times20=300$ sq cm.""",
r"15-20-25 triplet → other side 20, area 300.",
"medium", "m2d-quads", "rectangle from diagonal", 35))

pr.append(Q("m2d-q11",
r"The area of the largest square that can be inscribed in a circle of radius 7 cm is: [Use $\pi=\frac{22}{7}$]",
[("98 sq cm", 98), ("196 sq cm", 196), ("154 sq cm", 154), ("49 sq cm", 49)], 98,
r"""Diagonal of the square $=$ diameter $=14$ cm.

Area $=\frac{d^2}{2}=\frac{196}{2}=98$ sq cm.""",
r"$d=14$: area $=\frac{196}{2}=98$. Trap: 154 is the circle's area, 49 is $r^2$.",
"medium", "m2d-polygons", "largest square in a circle", 40))

pr.append(Q("m2d-q12",
r"A wheel of diameter 70 cm makes 300 revolutions. The distance travelled by the wheel is: [Use $\pi=\frac{22}{7}$]",
[("660 m", 660), ("66 m", 66), ("6,600 m", 6600), ("220 m", 220)], 660,
r"""Circumference $=\frac{22}{7}\times0.7=2.2$ m.

Distance $=300\times2.2=660$ m.""",
r"$d=0.7$ m → 2.2 m per revolution → 660 m. Trap: 6,600 m (cm-m slip).",
"medium", "m2d-circles", "wheel revolutions", 40))

pr.append(Q("m2d-q13",
r"If the area of a square increases by 96%, then each of its sides increases by:",
[("40%", 40), ("48%", 48), ("96%", 96), ("24%", 24)], 40,
r"Side factor $=\sqrt{1.96}=1.4$, so the side increases by 40%.",
r"$\sqrt{1.96}=1.4$ → 40%. Trap: 48% (half of 96) has no basis.",
"hard", "m2d-scaling", "side change from area change", 40))

pr.append(Q("m2d-q14",
r"The area of a regular hexagon of perimeter 36 cm is:",
[(r"$54\sqrt{3}$ sq cm", 54 * sp.sqrt(3)), (r"$36\sqrt{3}$ sq cm", 36 * sp.sqrt(3)), (r"$108\sqrt{3}$ sq cm", 108 * sp.sqrt(3)), (r"$72\sqrt{3}$ sq cm", 72 * sp.sqrt(3))], 54 * sp.sqrt(3),
r"""Side $=\frac{36}{6}=6$ cm.

Area $=\frac{3\sqrt3}{2}\times6^2=54\sqrt3$ sq cm.""",
r"Six equilateral triangles: $6\times\frac{\sqrt3}{4}\times36=54\sqrt3$. Trap: $36\sqrt3$ is the equilateral area with side 6... ×6 rule forgotten halfway.",
"hard", "m2d-polygons", "hexagon from perimeter", 45))

pr.append(Q("m2d-q15",
r"A wire of length 88 cm is first bent in the form of a circle and then re-bent in the form of a square. The ratio of the area of the circle to the area of the square is: [Use $\pi=\frac{22}{7}$]",
[("14 : 11", sp.Rational(14, 11)), ("11 : 14", sp.Rational(11, 14)), ("1 : 1", 1), ("7 : 11", sp.Rational(7, 11))], sp.Rational(14, 11),
r"""
Circle: $2\pi r=88\Rightarrow r=14$, area $=\frac{22}{7}\times196=616$ sq cm.

Square: side $=22$, area $=484$ sq cm.

Ratio $=616:484=14:11$.
""",
r"$r=14$ (since $88=2\times\frac{22}{7}\times14$), circle area 616; square side 22, area 484; divide both by 44: 14:11.",
"hard", "m2d-scaling", "wire re-bent circle to square", 60))

topic = {
    "id": "mensuration-2d",
    "sectionId": "quant",
    "title": "Mensuration (2D)",
    "order": 14,
    "importance": "high",
    "avgQuestions": {"tier1": 2, "tier2": 3},
    "summary": "Areas and perimeters of triangles, quadrilaterals, circles, sectors and regular polygons, plus paths, wheels and percentage-change effects. "
               "A reliable 1-3 questions per shift; the formulas are few and heavily recycled, so this converts to marks faster than almost any other advanced topic.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
