import sympy as sp
from sympy.geometry import Point, Triangle, Circle
from qa_common import Q, F, T, S, P, U, write_topic

A_ = sp.symbols("A")

# ---------------------------------------------------------------- sanity checks
assert 90 + sp.Rational(80, 2) == 130
assert 180 - 80 == 100
assert sp.Rational(3, 2) * 20 + 90 == 120
assert 2 * sp.sqrt(13**2 - 5**2) == 24
assert sp.sqrt(25**2 - sp.Rational(14, 2) ** 2) == 24  # median to base of isosceles 25,25,14
assert sp.Rational(1, 2) * 14 * 24 == 168
# centroid of a real triangle
tri = Triangle(Point(0, 0), Point(6, 0), Point(0, 8))
cen = tri.centroid
assert cen == Point(2, sp.Rational(8, 3))
# tangent length from point at distance 13 from centre, radius 5
assert sp.sqrt(13**2 - 5**2) == 12
# secant-tangent: 6^2 = 4 * PB
assert sp.Rational(36, 4) == 9
# transverse common tangent sqrt(d^2-(r1+r2)^2)
assert sp.sqrt(13**2 - (3 + 8) ** 2) == 4 * sp.sqrt(3)
# concentric circles: chord of outer tangent to inner
assert 2 * sp.sqrt(25**2 - 7**2) == 48
# rhombus side from half-diagonals 8, 6
assert sp.sqrt(8**2 + 6**2) == 10
# cyclic quad 1:2:3:2  (opposite sums equal is the cyclic condition)
ks = sp.symbols("k")
sol = sp.solve(sp.Eq(ks * (1 + 3), 180), ks)
assert [int(k * v) for k in sol for v in (1, 2, 3, 2)] == [45, 90, 135, 90]
assert 2 * 45 + 2 * 45 == 180  # B+D also supplementary
# similar triangles: perimeters 3:5, areas sum 68
k2 = sp.Rational(9, 25)
small = sp.Rational(68 * 9, 34)
assert small == 18 and sp.Rational(68 * 25, 34) == 50

# ---------------------------------------------------------------- SVG helpers
def pt_text(x, y, s, dx=0, dy=-6):
    return f'<text x="{x}" y="{y}" dx="{dx}" dy="{dy}" fill="currentColor" stroke="none" font-size="14" font-family="sans-serif">{s}</text>'

FIG_CENTROID = (
    '<svg viewBox="0 0 260 200" width="260" stroke="currentColor" fill="none">'
    '<polygon points="130,30 30,170 230,170" stroke-width="1.5"/>'
    '<line x1="130" y1="30" x2="130" y2="170" stroke-dasharray="4 3"/>'
    '<line x1="30" y1="170" x2="180" y2="100" stroke-dasharray="4 3"/>'
    '<line x1="230" y1="170" x2="80" y2="100" stroke-dasharray="4 3"/>'
    + pt_text(130, 30, "A", -5) + pt_text(30, 170, "B", -12) + pt_text(230, 170, "C", 2)
    + pt_text(130, 170, "D", -4, 16) + pt_text(80, 100, "E", -16, 0) + pt_text(180, 100, "F", 6, 0)
    + pt_text(130, 123, "G", 8, 4) + '</svg>')

FIG_INCENTRE = (
    '<svg viewBox="0 0 250 190" width="250" stroke="currentColor" fill="none">'
    '<polygon points="115,30 35,165 215,140" stroke-width="1.5"/>'
    '<line x1="115" y1="30" x2="122" y2="112" stroke-dasharray="4 3"/>'
    '<line x1="35" y1="165" x2="122" y2="112" stroke-dasharray="4 3"/>'
    '<line x1="215" y1="140" x2="122" y2="112" stroke-dasharray="4 3"/>'
    + pt_text(115, 30, "A", -5) + pt_text(35, 165, "B", -12) + pt_text(215, 140, "C", 2)
    + pt_text(122, 112, "I", 6, 8) + '</svg>')

FIG_CYCLIC = (
    '<svg viewBox="0 0 260 205" width="260" stroke="currentColor" fill="none">'
    '<circle cx="130" cy="105" r="75"/>'
    '<polygon points="59.5,79.4 104.35,175.5 200.5,130.65 155.65,34.5" stroke-width="1.5"/>'
    + pt_text(59.5, 79.4, "A", -16, 0) + pt_text(104.35, 175.5, "B", -6, 16)
    + pt_text(200.5, 130.65, "C", 6, 4) + pt_text(155.65, 34.5, "D", 0, -6) + '</svg>')

FIG_TANGENT = (
    '<svg viewBox="0 0 250 175" width="250" stroke="currentColor" fill="none">'
    '<circle cx="65" cy="105" r="50"/>'
    '<line x1="65" y1="105" x2="185" y2="105" stroke-dasharray="4 3"/>'
    '<line x1="185" y1="105" x2="85.8" y2="59.5"/>'
    '<line x1="65" y1="105" x2="85.8" y2="59.5"/>'
    + pt_text(65, 105, "O", -14, 6) + pt_text(185, 105, "P", 2, 16)
    + pt_text(85.8, 59.5, "T", -4, -6) + '</svg>')

FIG_CONCENTRIC = (
    '<svg viewBox="0 0 300 195" width="300" stroke="currentColor" fill="none">'
    '<circle cx="150" cy="105" r="68"/>'
    '<circle cx="150" cy="105" r="19"/>'
    '<line x1="84.7" y1="86" x2="215.3" y2="86"/>'
    '<line x1="150" y1="105" x2="215.3" y2="86" stroke-dasharray="4 3"/>'
    + pt_text(150, 105, "O", 4, 6) + pt_text(84.7, 86, "A", -14, 0) + pt_text(215.3, 86, "B", 2, -4)
    + pt_text(150, 86, "M", -6, -6) + '</svg>')

FIG_COMMONTAN = (
    '<svg viewBox="0 0 280 200" width="280" stroke="currentColor" fill="none">'
    '<circle cx="55" cy="100" r="18"/>'
    '<circle cx="195" cy="100" r="48"/>'
    '<line x1="55" y1="100" x2="195" y2="100" stroke-dasharray="4 3"/>'
    '<line x1="55" y1="100" x2="55" y2="82"/>'
    '<line x1="195" y1="100" x2="195" y2="52"/>'
    + pt_text(55, 100, "O", -14, 8) + pt_text(195, 100, "P", 0, 18)
    + pt_text(55, 82, "r", -12, 2) + pt_text(195, 52, "R", 8, 2) + '</svg>')

# ---------------------------------------------------------------- subtopics
subtopics = [
S("geo-lines-angles", "Lines and angles",
r"""
At a point on a straight line the total angle is $180^\circ$; around a point it is $360^\circ$.
When two straight lines cross, the **vertically opposite** angles are equal.

For **parallel lines** cut by a transversal (the standard CGL figure):
- **Corresponding angles** are equal (both "top-right", etc.).
- **Alternate angles** are equal (Z-shape).
- **Co-interior (allied) angles** add to $180^\circ$ — this gives a small equation in $x$.

An **angle bisector** splits an angle into two equal parts; two bisectors of a triangle meet at the incentre.
""",
[
F("Angles on a line / around a point", r"\text{on a line}=180^\circ,\quad \text{round a point}=360^\circ"),
F("Co-interior angles", r"(a+b)^\circ=180^\circ\ \text{for allied angles between parallels}"),
F("Complement / supplement", r"x+(90^\circ-x)=180^\circ\cdot\tfrac12,\quad \text{supplement}-\text{complement}=180^\circ-2\cdot\text{angle}"),
F("Parallel line pairs", r"\text{corresponding}=\text{alternate}=\text{vertically opposite (each pair equal)}"),
],
[
T("Co-interior gives the equation",
r"""If two allied angles are given as expressions in $x$, set their sum to $180^\circ$, solve for $x$, then substitute
back into the angle asked.""",
r"Two co-interior angles between parallel lines are $(3x+20)^\circ$ and $(2x+10)^\circ$. Find the larger angle.",
r"$3x+20+2x+10=180\Rightarrow x=30$. Angles: $110^\circ$ and $70^\circ$; larger $=110^\circ$."),
T("Supplement − complement one-liner",
r"""For an angle $x$: supplement $=180-x$, complement $=90-x$, so the difference is always $90^\circ$, and the angle
itself is $\frac{180-d}{2}$ if the difference $d$ is given.""",
r"The supplement of an angle is four times its complement. Find the angle.",
r"$180-x=4(90-x)\Rightarrow 180-x=360-4x\Rightarrow 3x=180\Rightarrow x=60^\circ$."),
],
[
"Forgetting that co-interior angles are supplementary only between **parallel** lines.",
"Reading the wrong pair: alternate vs corresponding in the transversal figure.",
"Solving for $x$ and answering $x$ instead of the angle asked.",
]),
S("geo-triangles", "Triangles and their centres",
r"""
Angle facts: the interior angles add to $180^\circ$; an **exterior angle equals the sum of the two remote interior
angles**. In an isosceles triangle the median to the base is also the altitude and the bisector.

**The four centres (memorise the angle results):**

| Centre | Defined by | Key result |
|---|---|---|
| Centroid G | medians | divides each median $2:1$ from the vertex |
| Incentre I | angle bisectors | $\angle BIC=90^\circ+\frac{A}{2}$ |
| Circumcentre O | perpendicular bisectors | $\angle BOC=2\angle A$ |
| Orthocentre H | altitudes | $\angle BHC=180^\circ-\angle A$ |

For a right triangle the orthocentre is the right-angle vertex and the circumcentre is the midpoint of the
hypotenuse; in an equilateral triangle all four centres coincide.
""",
[
F("Angle sum & exterior angle", r"A+B+C=180^\circ,\quad \text{ext}=B+C"),
F("Centroid division", r"AG:GD=2:1\ \text{on median }AD"),
F("Incentre angle", r"\angle BIC=90^\circ+\frac{A}{2}"),
F("Circumcentre angle", r"\angle BOC=2A\ \text{(minor arc BC)}"),
F("Orthocentre angle", r"\angle BHC=180^\circ-A"),
F("Apollonius (median length)", r"m_a^2=\frac{2b^2+2c^2-a^2}{4}"),
F("Isosceles median", r"m_{\text{base}}=\sqrt{a^2-\left(\frac{\text{base}}{2}\right)^2}"),
F("Heron's area", r"K=\sqrt{s(s-a)(s-b)(s-c)},\ s=\frac{a+b+c}{2}"),
],
[
T("Centre angles from one input",
r"""The asked angle involves $\angle A$ only. Read off which centre is drawn: bisectors → $90+\frac A2$,
perpendicular bisectors → $2A$, altitudes → $180-A$.""",
r"In $\triangle ABC$, $\angle A=70^\circ$. Find $\angle BHC$ where $H$ is the orthocentre.",
r"$\angle BHC=180^\circ-70^\circ=110^\circ$. (For the incentre it would be $90+35=125^\circ$; for the circumcentre $140^\circ$.)"),
T("Centroid ratios without coordinates",
r"""The centroid cuts each median in $2:1$ from the vertex. If the median is $3m$ long, the pieces are $2m$ and $m$.""",
r"The median $AD$ of $\triangle ABC$ is 15 cm. Find $AG$ where $G$ is the centroid.",
r"$AG=\frac23\times15=10$ cm, $GD=5$ cm."),
T("Median by Apollonius or symmetry",
r"""For an isosceles triangle skip the formula: the median to the base is $\sqrt{a^2-(b/2)^2}$.
Otherwise use $m_a^2=\frac{2b^2+2c^2-a^2}{4}$.""",
r"Find the median to the base of an isosceles triangle with equal sides 25 cm and base 14 cm.",
r"$\sqrt{25^2-7^2}=\sqrt{625-49}=24$ cm."),
T("Heron with a standard semi-perimeter",
r"""For 13-14-15, $s=21$, area $=\sqrt{21\cdot8\cdot7\cdot6}=84$. Memorise the common Heron families:
(13,14,15)→84, (3,4,5)→6, (5,12,13)→30, (6,8,10)→24, (7,24,25)→84, (9,12,15)→54, (10,24,26)→120.""",
r"Find the area of a triangle with sides 13, 14, 15 cm.",
r"$s=21$: $K=\sqrt{21\times8\times7\times6}=\sqrt{7056}=84$ sq cm."),
],
[
"$\\angle BIC=90^\\circ+\\frac A2$ vs $\\angle BOC=2A$ vs $\\angle BHC=180^\\circ-A$ get swapped under exam pressure.",
"Centroid ratio read the wrong way: $GD=\\frac13 AD$, not $\\frac23$.",
"Exterior angle taken at the wrong vertex — it equals the sum of the two **remote** interior angles.",
"Heron: forgetting to halve the perimeter before subtracting.",
]),
S("geo-similarity", "Congruence, similarity and BPT",
r"""
**Congruence** (same size and shape): SSS, SAS, ASA/AAS, RHS.

**Similarity** (same shape): corresponding angles equal and sides in the same ratio. For similar triangles with
scale factor $k$:
- corresponding sides, perimeters, medians, altitudes → ratio $k$,
- areas → ratio $k^2$.

**Basic Proportionality Theorem (Thales):** a line parallel to one side of a triangle divides the other two sides
in the same ratio: $DE\parallel BC\Rightarrow\frac{AD}{DB}=\frac{AE}{EC}$.

**Midpoint theorem:** the segment joining midpoints of two sides is parallel to the third side and half its length.
""",
[
F("Similarity ratios", r"\frac{a_1}{a_2}=k,\quad \frac{P_1}{P_2}=k,\quad \frac{K_1}{K_2}=k^2"),
F("Areas from perimeters", r"\frac{K_1}{K_2}=\left(\frac{P_1}{P_2}\right)^2"),
F("BPT", r"DE\parallel BC\Rightarrow\frac{AD}{DB}=\frac{AE}{EC}"),
F("Midpoint theorem", r"D,E\ \text{midpoints}\Rightarrow DE=\frac{BC}{2}"),
F("Angle bisector theorem", r"\frac{BD}{DC}=\frac{AB}{AC}\ \text{(internal bisector of }A\text{)}"),
],
[
T("Square the perimeter ratio for areas",
r"""Perimeters in ratio $p:q$ → areas in ratio $p^2:q^2$ (and back: side ratio $=\sqrt{\text{area ratio}}$).""",
r"Two similar triangles have perimeters 30 cm and 50 cm. If the area of the smaller is 18 sq cm, find the area of the larger.",
r"Side ratio $=\frac35$, so area ratio $=\frac{9}{25}$: larger area $=18\times\frac{25}{9}=50$ sq cm."),
T("Midpoint theorem shortcut",
r"""Spot the words "midpoints of two sides" → the joining segment is half the third side, parallel to it.
Conversely, through the midpoint of one side, parallel to another → it bisects the third side.""",
r"In $\triangle ABC$, $D$ and $E$ are midpoints of $AB$ and $AC$. If $DE=4.5$ cm, find $BC$.",
r"$BC=2\times DE=9$ cm."),
T("BPT with a parallel drawn inside",
r"""When a line parallel to a side cuts the other two sides, write the ratio directly. If the segments on one side
are $AD:DB=2:3$, the same ratio holds on the other side.""",
r"In $\triangle ABC$, $DE\parallel BC$ with $AD=4$ cm, $DB=6$ cm, $AE=5$ cm. Find $EC$.",
r"$\frac{AE}{EC}=\frac{AD}{DB}=\frac46\Rightarrow EC=\frac{5\times6}{4}=7.5$ cm."),
],
[
"Using the side ratio (not its square) for areas — or squaring when you should not.",
"Taking $DE=\\frac{BC}{2}$ as true for any parallel line; it needs **midpoints**.",
"BPT ratio written as $AD/AB=AE/AC$ carelessly — it is correct, but mixing $AD/DB$ with $AE/AC$ on opposite sides is the classic slip.",
]),
S("geo-pythagoras", "Pythagoras theorem and triplets",
r"""
In a right triangle with hypotenuse $h$: $h^2=p^2+b^2$. The converse also holds — it is how CGL tests
"which triangle is right-angled". Memorise the standard **triplets** (and their multiples):
$$(3,4,5)\ (5,12,13)\ (7,24,25)\ (8,15,17)\ (9,40,41)\ (11,60,61)\ (12,35,37)\ (20,21,29)$$
Useful extras: median to the hypotenuse $=\frac{h}{2}$; the diagonal of a rectangle is $\sqrt{l^2+b^2}$; in an
obtuse triangle $a^2>b^2+c^2$ (acute if $a^2<b^2+c^2$) where $a$ is the longest side.
""",
[
F("Pythagoras", r"h^2=p^2+b^2"),
F("Median to hypotenuse", r"m_{\text{hyp}}=\frac{h}{2}"),
F("Rectangle diagonal", r"d=\sqrt{l^2+b^2}"),
F("Triangle type test", r"a\ \text{longest}:\ a^2\gtrless b^2+c^2\Rightarrow \text{obtuse}/\text{acute}"),
],
[
T("Triplet recognition",
r"""See two numbers, recall the third: 12 and 13 → 5; 24 and 25 → 7; 15 and 17 → 8. Multiples scale: 6-8-10,
9-12-15, 10-24-26 are all 3-4-5 families.""",
r"A ladder 25 m long stands with its foot 7 m from a wall. How high does it reach?",
r"7-24-25 triplet → height $=24$ m."),
T("Median to the hypotenuse is half of it",
r"""In any right triangle the median from the right angle equals half the hypotenuse (three equal pieces:
the two half-hypotenuses and the median).""",
r"In a right triangle with hypotenuse 13 cm, find the median to the hypotenuse.",
r"$\frac{13}{2}=6.5$ cm."),
T("Converse: check $a^2$ vs $b^2+c^2$",
r"""To identify the right/obtuse/acute triangle, square only the longest side and compare.""",
r"Which of the triangles with sides (i) 6, 8, 11 (ii) 6, 8, 10 (iii) 6, 8, 9 is right-angled?",
r"(ii) $10^2=6^2+8^2$. (i) is obtuse ($121>100$), (iii) is acute ($81<100$)."),
],
[
"Adding instead of subtracting: the unknown leg is $\\sqrt{h^2-b^2}$, not $\\sqrt{h^2+b^2}$.",
"Calling any big triangle right-angled without checking a triplet or the squares.",
"Half-hypotenuse median confused with the median to a leg.",
]),
S("geo-quad-poly", "Quadrilaterals and polygons",
r"""
**Quadrilateral:** angles add to $360^\circ$. Key areas: parallelogram $=b\times h$; rhombus $=\frac12 d_1d_2$
(with side $=\sqrt{(d_1/2)^2+(d_2/2)^2}$); trapezium $=\frac12(a+b)h$. Diagonals of a rectangle are equal and
bisect each other; of a rhombus they bisect at right angles.

**Cyclic quadrilateral:** all four vertices on a circle; **opposite angles are supplementary**. Its area
(Brahmagupta) is $\sqrt{(s-a)(s-b)(s-c)(s-d)}$.

**Regular polygon** with $n$ sides: interior angle $=\frac{(n-2)180^\circ}{n}$, each exterior $=\frac{360^\circ}{n}$,
diagonals $=\frac{n(n-3)}{2}$.
""",
[
F("Quadrilateral angle sum", r"A+B+C+D=360^\circ"),
F("Cyclic quadrilateral", r"A+C=180^\circ,\quad B+D=180^\circ"),
F("Rhombus", r"K=\frac12 d_1d_2,\quad a=\sqrt{\left(\frac{d_1}{2}\right)^2+\left(\frac{d_2}{2}\right)^2}"),
F("Trapezium", r"K=\frac12(a+b)h"),
F("Parallelogram", r"K=bh"),
F("Regular polygon", r"\text{int}=\frac{(n-2)180^\circ}{n},\quad \text{ext}=\frac{360^\circ}{n},\quad \text{diagonals}=\frac{n(n-3)}{2}"),
F("Brahmagupta", r"K=\sqrt{(s-a)(s-b)(s-c)(s-d)}"),
],
[
T("Exterior angle → number of sides",
r"""For regular polygons the exterior angle is the fastest route: $n=\frac{360^\circ}{\text{ext}}$, and
$\text{ext}=180^\circ-\text{int}$.""",
r"The interior angle of a regular polygon is $156^\circ$. How many sides has it?",
r"ext $=24^\circ$, so $n=360/24=15$."),
T("Rhombus side from diagonals",
r"""Half-diagonals form a right triangle with the side: side $=\sqrt{(d_1/2)^2+(d_2/2)^2}$. If the halves are 8 and 6,
the side is a 6-8-10 triplet.""",
r"The diagonals of a rhombus are 16 cm and 12 cm. Find its side.",
r"Halves 8 and 6 → side $=10$ cm (area $=96$ sq cm)."),
T("Diagonal count one-liner",
r"""$n$ vertices, each joins $n-3$ others (not itself, not two neighbours), each diagonal counted twice:
$\frac{n(n-3)}{2}$.""",
r"How many diagonals does a decagon have?",
r"$\frac{10\times7}{2}=35$."),
],
[
"Rhombus area $\\frac12 d_1d_2$ applied to a rectangle or parallelogram.",
"Cyclic quadrilateral: adding non-opposite angles to $180^\\circ$.",
"Interior/exterior angle confused; also $(n-2)\\times180^\\circ$ misapplied as $n\\times180^\\circ$.",
]),
S("geo-circles", "Circles: chords, tangents, secants and cyclic angles",
r"""
**Chords:** a perpendicular from the centre bisects a chord; chord $=2\sqrt{r^2-d^2}$. Equal chords are
equidistant from the centre (and subtend equal angles at the centre).

**Angles:** angle at the centre $=$ twice the angle at the circumference on the same arc; angles in the same
segment are equal; the angle in a semicircle is $90^\circ$.

**Tangents:** tangent $\perp$ radius; the two tangents from an external point are equal; tangent–secant
$PT^2=PA\cdot PB$; two chords crossing inside give $p_1p_2=q_1q_2$.

**Cyclic quadrilateral:** opposite angles supplementary; the exterior angle equals the interior opposite angle.

**Common tangents of two circles** ($d$ = centre distance): separate ($d>r_1+r_2$) → 4; externally tangent → 3;
intersecting → 2; internally tangent → 1; one inside the other → 0. Direct tangent length
$=\sqrt{d^2-(r_1-r_2)^2}$, transverse $=\sqrt{d^2-(r_1+r_2)^2}$.
""",
[
F("Chord from distance", r"\ell=2\sqrt{r^2-d^2}"),
F("Equal chords", r"\ell_1=\ell_2\Rightarrow d_1=d_2"),
F("Tangent–secant", r"PT^2=PA\cdot PB"),
F("Intersecting chords", r"PA\cdot PB=PC\cdot PD"),
F("Cyclic quadrilateral", r"A+C=180^\circ,\ \text{ext}=\text{interior opposite}"),
F("Alternate segment", r"\angle\text{tangent-chord}=\angle\text{in alternate segment}"),
F("Common tangents (transverse)", r"L_T=\sqrt{d^2-(r_1+r_2)^2}"),
F("Common tangents (direct)", r"L_D=\sqrt{d^2-(r_1-r_2)^2}"),
],
[
T("Triplet inside a circle",
r"""$r$-$d$-$\frac{\ell}{2}$ is a right triangle: radius 13 and distance 5 → half-chord 12 → chord 24. Circles reuse
the same triplets as Pythagoras questions.""",
r"A chord is at distance 5 cm from the centre of a circle of radius 13 cm. Find its length.",
r"Half-chord $=\sqrt{169-25}=12$; chord $=24$ cm."),
T("Tangent–secant: multiply the pieces",
r"""Tangent squared = external secant × whole secant. Read the "whole" as external + internal part.""",
r"From P, a tangent of length 6 cm and a secant whose external part is 4 cm are drawn. Find the internal (chord) part.",
r"$6^2=4\times\text{whole}\Rightarrow$ whole $=9$, so the chord inside is $9-4=5$ cm."),
T("Count common tangents from $d$ vs $r_1, r_2$",
r"""Compare $d$ with $r_1+r_2$ and $|r_1-r_2|$: outside → 4, touching outside → 3, overlapping → 2, touching
inside → 1, contained → 0.""",
r"Two circles of radii 4 cm and 9 cm have centres 13 cm apart. How many common tangents do they have?",
r"$d=13=r_1+r_2$ → externally tangent → **3** common tangents."),
T("Concentric chord trick",
r"""A chord of the outer circle tangent to the inner circle has length $2\sqrt{R^2-r^2}$ — the inner radius is the
distance from the centre to the chord.""",
r"Two concentric circles have radii 25 cm and 7 cm. Find the chord of the larger that touches the smaller.",
r"$2\sqrt{625-49}=2\times24=48$ cm."),
],
[
"Forgetting to **double** the half-chord: $\\sqrt{r^2-d^2}$ is only half the chord.",
"Tangent–secant: using the internal part instead of the whole secant length.",
"$d=r_1+r_2$ vs $d=|r_1-r_2|$ confusion changes the tangent count completely.",
"Angle in the same segment vs angle in the alternate segment mixed up.",
]),
]

patterns = [
P("Parallel lines with expressions in x", "very common",
  r"A transversal across parallel lines with angles $(ax+b)^\circ$; find $x$ or the angle.",
  r"Co-interior sum to $180^\circ$, corresponding/alternate are equal; solve the small equation and substitute back."),
P("Angle result at a triangle centre", "very common",
  r"$I$/$O$/$H$ defined as incentre/circumcentre/orthocentre; $\angle A$ given, find $\angle BIC$, $\angle BOC$ or $\angle BHC$.",
  r"$90^\circ+\frac A2$, $2A$, $180^\circ-A$ respectively. For bisectors of $B$ and $C$ directly: $90^\circ+\frac A2$."),
P("Ratio of areas of similar triangles", "very common",
  r"Perimeters (or sides/altitudes) of two similar triangles in ratio; find areas, or reverse.",
  r"Perimeter ratio $k$ → area ratio $k^2$; invert with a square root when going from areas to sides."),
P("Midpoint theorem / BPT", "common",
  r"Midpoints of sides, or a line parallel to one side cutting the other two.",
  r"$DE=\frac{BC}{2}$ for midpoints; $\frac{AD}{DB}=\frac{AE}{EC}$ for parallels."),
P("Pythagoras with a triplet", "very common",
  r"Ladder, pole, diagonal, or circle radius–chord–distance; numbers like 13-12, 25-24, 17-15.",
  r"Recognise the triplet and answer without computing squares; multiples of (3,4,5) are everywhere."),
P("Regular polygon angle or diagonal count", "common",
  r"Interior angle given → find $n$; or diagonals of an $n$-gon.",
  r"$\text{ext}=180^\circ-\text{int}$, $n=\frac{360^\circ}{\text{ext}}$, diagonals $=\frac{n(n-3)}{2}$."),
P("Circle: tangent, secant or chord products", "very common",
  r"Tangent from an external point, secant pieces, intersecting chords, concentric-circle chord.",
  r"$PT^2=PA\cdot PB$, $p_1p_2=q_1q_2$, chord $=2\sqrt{r^2-d^2}$; triplets 3-4-5, 5-12-13, 7-24-25, 8-15-17."),
P("Cyclic quadrilateral angles", "common",
  r"Angles of a cyclic quadrilateral given as a ratio or one angle given.",
  r"Opposite pairs sum to $180^\circ$: set up $k(a+c)=180^\circ$ or subtract the given angle from $180^\circ$."),
]

# ---------------------------------------------------------------- solved examples
solved = []

solved.append(Q("geo-s01",
r"In $\triangle ABC$, $\angle A=50^\circ$. $BO$ and $CO$ are the internal bisectors of $\angle B$ and $\angle C$, meeting at $O$. Find $\angle BOC$.",
U("°", 115, 90, 105, 130), 115,
r"""
$B+C=180^\circ-50^\circ=130^\circ$. The bisectors take half of each:

$\angle OBC+\angle OCB=\frac{B}{2}+\frac{C}{2}=\frac{130^\circ}{2}=65^\circ$.

So $\angle BOC=180^\circ-65^\circ=115^\circ$.
""",
r"Memorise $\angle BIC=90^\circ+\frac{A}{2}=90^\circ+25^\circ=115^\circ$ — valid for the incentre, which is exactly where the two bisectors meet.",
"easy", "geo-triangles", "incentre angle", 35, FIG_INCENTRE))

solved.append(Q("geo-s02",
r"Two similar triangles have areas of $16\ \text{cm}^2$ and $25\ \text{cm}^2$. If the perimeter of the smaller triangle is $32$ cm, find the perimeter of the larger triangle.",
[("40 cm", 40), ("45 cm", 45), ("50 cm", 50), ("36 cm", 36)], 40,
r"""
Area ratio $=16:25$, so the side (and perimeter) ratio is $\sqrt{16}:\sqrt{25}=4:5$.

Larger perimeter $=32\times\frac54=40$ cm.
""",
r"Areas → perimeters needs a square **root**: $\sqrt{16/25}=\frac45$. Traps: $32\times\frac{25}{16}=50$ (forgot the root), $32\times\frac45=25.6$ (inverted).",
"medium", "geo-similarity", "similar triangles: areas vs perimeters", 45))

solved.append(Q("geo-s03",
r"From an external point $P$, a tangent $PT$ of length $12$ cm and a secant $PAB$ are drawn to a circle. If $PA=8$ cm, find the length of the chord $AB$.",
[("10 cm", 10), ("16 cm", 16), ("18 cm", 18), ("9 cm", 9)], 10,
r"""
$PT^2=PA\cdot PB\Rightarrow 144=8\,PB\Rightarrow PB=18$ cm.

$AB=PB-PA=18-8=10$ cm.
""",
r"$144/8=18$ is the **whole** secant; subtract the external part: $18-8=10$. Trap: 18 itself.",
"medium", "geo-circles", "tangent-secant theorem", 40))

solved.append(Q("geo-s04",
r"The angles of a cyclic quadrilateral $ABCD$ are in the ratio $1:2:3:2$ in that order. Find the largest angle.",
U("°", 135, 120, 144, 150), 135,
r"""
Let the angles be $k, 2k, 3k, 2k$. Since $ABCD$ is cyclic, $A+C=180^\circ$:

$k+3k=180^\circ\Rightarrow k=45^\circ$.

Angles: $45^\circ, 90^\circ, 135^\circ, 90^\circ$. Largest $=135^\circ$.
""",
r"Only **opposite** pairs must sum to $180^\circ$: $(1+3)k=180$ gives $k=45$; check $B+D=(2+2)\times45=180$ ✓. The largest is $3k=135^\circ$.",
"medium", "geo-circles", "cyclic quadrilateral angle ratio", 50, FIG_CYCLIC))

# ---------------------------------------------------------------- practice
pr = []

pr.append(Q("geo-q01",
r"Two parallel lines are cut by a transversal. If two co-interior angles are $(3x+20)^\circ$ and $(2x+10)^\circ$, then the larger of the two angles is:",
U("°", 110, 70, 100, 120), 110,
r"Co-interior angles add to $180^\circ$: $3x+20+2x+10=180\Rightarrow 5x=150\Rightarrow x=30$. The angles are $110^\circ$ and $70^\circ$; the larger is $110^\circ$.",
r"$x=30$ at once ($150/5$); angle $=3(30)+20=110^\circ$. Answering $70^\circ$ or $x=30$ are the traps.",
"easy", "geo-lines-angles", "co-interior angles", 30))

pr.append(Q("geo-q02",
r"In $\triangle ABC$ the interior angles at $A$ and $B$ are $52^\circ$ and $63^\circ$. The exterior angle at $C$ is:",
U("°", 115, 65, 125, 117), 115,
r"The exterior angle at a vertex equals the sum of the two remote interior angles: $52^\circ+63^\circ=115^\circ$.",
r"Add the two remote angles: $115^\circ$. (Computing $180-115=65^\circ$ gives the *interior* angle at $C$ — a trap.)",
"easy", "geo-triangles", "exterior angle theorem", 25))

pr.append(Q("geo-q03",
r"A ladder 25 m long leans against a wall with its foot 7 m away from the base of the wall. How high up the wall does the ladder reach?",
[("24 m", 24), ("20 m", 20), ("26 m", 26), ("18 m", 18)], 24,
r"$h^2+7^2=25^2\Rightarrow h^2=625-49=576\Rightarrow h=24$ m.",
r"7-24-25 triplet → 24 m, no calculation needed.",
"easy", "geo-pythagoras", "ladder Pythagoras", 25))

pr.append(Q("geo-q04",
r"Each interior angle of a regular polygon is $156^\circ$. The number of sides of the polygon is:",
[15, 12, 18, 20], 15,
r"Exterior angle $=180^\circ-156^\circ=24^\circ$, and $n=\frac{360^\circ}{24}=15$.",
r"$n=360/24=15$. Trap: $1560/... $ i.e. using $(n-2)180=156n$ directly is slower; and 13 (from $n=\frac{180}{180-156}$... just memorise ext route).",
"easy", "geo-quad-poly", "regular polygon: interior angle to n", 30))

pr.append(Q("geo-q05",
r"A chord of a circle is at a distance of $5$ cm from the centre. If the radius of the circle is $13$ cm, the length of the chord is:",
[("24 cm", 24), ("12 cm", 12), ("26 cm", 26), ("18 cm", 18)], 24,
r"Half-chord $=\sqrt{13^2-5^2}=\sqrt{169-25}=12$ cm, so the chord is $24$ cm.",
r"5-12-13 triplet → half-chord 12 → chord 24 cm. Trap: 12 cm (forgot to double).",
"easy", "geo-circles", "chord from radius and distance", 30))

pr.append(Q("geo-q06",
r"In $\triangle ABC$, the median $AD$ from $A$ to $BC$ is $15$ cm long. If $G$ is the centroid of the triangle, then $AG$ is equal to:",
[("10 cm", 10), ("5 cm", 5), ("7.5 cm", sp.Rational(15, 2)), ("12 cm", 12)], 10,
r"The centroid divides each median in the ratio $2:1$ from the vertex: $AG=\frac{2}{3}\times15=10$ cm (and $GD=5$ cm).",
r"$\frac23\times15=10$ cm. Traps: 5 ($1:2$ read backwards gives $GD$), 7.5 (halving).",
"medium", "geo-triangles", "centroid divides median 2:1", 25, FIG_CENTROID))

pr.append(Q("geo-q07",
r"In $\triangle ABC$, $\angle B=55^\circ$ and $\angle C=45^\circ$. If $I$ is the incentre of the triangle, then $\angle BIC$ is equal to:",
U("°", 130, 100, 125, 140), 130,
r"""$\angle A=180^\circ-55^\circ-45^\circ=80^\circ$.

$\angle BIC=90^\circ+\frac{A}{2}=90^\circ+40^\circ=130^\circ$.""",
r"$A=80\Rightarrow 90+\frac{80}{2}=130^\circ$. Trap: $2A=160^\circ$ (circumcentre formula).",
"medium", "geo-triangles", "incentre angle BIC", 40))

pr.append(Q("geo-q08",
r"Two triangles are similar and their perimeters are $30$ cm and $50$ cm. If the area of the smaller triangle is $18\ \text{cm}^2$, the area of the larger triangle is:",
[("50", 50), ("40", 40), ("60", 60), ("32", 32)], 50,
r"""Side ratio $=\frac{30}{50}=\frac35$, so the area ratio is $\frac{9}{25}$.

Larger area $=18\times\frac{25}{9}=50\ \text{cm}^2$.""",
r"Area ratio $=(3/5)^2=9/25$; scale up: $18\times25/9=50$. Trap: $18\times5/3=30$ (used the linear ratio).",
"medium", "geo-similarity", "similar triangles: perimeter ratio to areas", 45))

pr.append(Q("geo-q09",
r"In $\triangle ABC$, $D$ and $E$ are the midpoints of $AB$ and $AC$ respectively. If $DE=4.5$ cm, then $BC$ is equal to:",
[("9 cm", 9), ("2.25 cm", sp.Rational(9, 4)), ("6.75 cm", sp.Rational(27, 4)), ("12 cm", 12)], 9,
r"By the midpoint theorem, $DE\parallel BC$ and $DE=\frac{BC}{2}$. So $BC=2\times4.5=9$ cm.",
r"Double it: 9 cm. Trap: 2.25 (halved instead of doubled).",
"medium", "geo-similarity", "midpoint theorem", 25))

pr.append(Q("geo-q10",
r"$ABCD$ is a cyclic quadrilateral in which $\angle A:\angle C=3:2$ and $\angle B=95^\circ$. The angle $\angle D$ is equal to:",
U("°", 85, 95, 75, 105), 85,
r"""$\angle B$ and $\angle D$ are opposite angles of a cyclic quadrilateral, so $\angle B+\angle D=180^\circ$:

$\angle D=180^\circ-95^\circ=85^\circ$.""",
r"The $3:2$ data is a distractor — only $\angle B$ and $\angle D$ are opposite, so $180-95=85^\circ$. (Ratios would matter only if $\angle A$ were asked: $108^\circ$.)",
"medium", "geo-circles", "cyclic quadrilateral opposite angles", 35))

pr.append(Q("geo-q11",
r"Point $P$ is at a distance of $13$ cm from the centre $O$ of a circle of radius $5$ cm. The length of the tangent drawn from $P$ to the circle is:",
[("12 cm", 12), ("13 cm", 13), ("8 cm", 8), (r"$\sqrt{194}$ cm", sp.sqrt(194))], 12,
r"The radius to the point of contact is perpendicular to the tangent: $PT^2=OP^2-OT^2=169-25=144$, so $PT=12$ cm.",
r"5-12-13 triplet → 12 cm.",
"medium", "geo-circles", "tangent length from external point", 30, FIG_TANGENT))

pr.append(Q("geo-q12",
r"The diagonals of a rhombus are $16$ cm and $12$ cm. The length of each side of the rhombus is:",
[("10 cm", 10), ("14 cm", 14), ("8 cm", 8), ("20 cm", 20)], 10,
r"""The diagonals of a rhombus bisect each other at right angles. Half-diagonals are $8$ and $6$:

side $=\sqrt{8^2+6^2}=10$ cm.""",
r"6-8-10 triplet → 10 cm. Trap: 14 (half the sum of half-diagonals... i.e. averaging), 20 (using full diagonals as legs).",
"medium", "geo-quad-poly", "rhombus side from diagonals", 35))

pr.append(Q("geo-q13",
r"Two concentric circles have radii $25$ cm and $7$ cm. A chord of the larger circle touches the smaller circle. The length of this chord is:",
[("48 cm", 48), ("24 cm", 24), ("40 cm", 40), ("50 cm", 50)], 48,
r"""
The radius of the smaller circle is the distance from the centre to the chord. Half-chord
$=\sqrt{25^2-7^2}=\sqrt{625-49}=24$, so the chord is $48$ cm.
""",
r"7-24-25 triplet: half-chord 24 → chord 48 cm. Trap: 24 cm (half only).",
"hard", "geo-circles", "concentric circles chord", 40, FIG_CONCENTRIC))

pr.append(Q("geo-q14",
r"In an isosceles triangle $ABC$, $AB=AC=25$ cm and $BC=14$ cm. The area of the triangle is:",
[("168", 168), ("175", 175), ("150", 150), ("336", 336)], 168,
r"""
The median/altitude to the base: $h=\sqrt{25^2-7^2}=24$ cm.

Area $=\frac12\times14\times24=168\ \text{cm}^2$.
""",
r"7-24-25 again: height 24, area $=\frac12\times14\times24=168$. Trap: 336 forgot the $\frac12$.",
"hard", "geo-triangles", "isosceles area via median-altitude", 45))

pr.append(Q("geo-q15",
r"Two circles of radii $3$ cm and $8$ cm have their centres $13$ cm apart. The length of a transverse (cross) common tangent is:",
[(r"$4\sqrt{3}$ cm", 4 * sp.sqrt(3)), (r"$\sqrt{105}$ cm", sp.sqrt(105)), (r"$\sqrt{69}$ cm", sp.sqrt(69)), ("12 cm", 12)], 4 * sp.sqrt(3),
r"""
Transverse tangent length $=\sqrt{d^2-(r_1+r_2)^2}=\sqrt{169-121}=\sqrt{48}=4\sqrt3$ cm.
""",
r"$d=13$, $r_1+r_2=11$: $\sqrt{13^2-11^2}=\sqrt{48}=4\sqrt3$. Trap: $\sqrt{105}$ is the **direct** tangent $\sqrt{169-8^2}$. Both tangent types exist since $13>11$.",
"hard", "geo-circles", "transverse common tangent", 50, FIG_COMMONTAN))

topic = {
    "id": "geometry",
    "sectionId": "quant",
    "title": "Geometry",
    "order": 13,
    "importance": "high",
    "avgQuestions": {"tier1": 4, "tier2": 5},
    "summary": "Lines and angles, triangles and their four centres, similarity and BPT, Pythagoras, quadrilaterals, polygons and circles. "
               "The single largest advanced-maths block in CGL (3–5 questions per shift), and nearly every question runs off a memorised angle result, a triplet, or a ratio rule.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
