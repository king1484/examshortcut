import sympy as sp
from qa_common import Q, F, T, S, P, U, write_topic

PI = sp.Rational(22, 7)

# ---------------------------------------------------------------- sanity checks
assert 6**3 == 216
assert 2 * (8 * 6 + 6 * 4 + 8 * 4) == 208
assert PI * 7**2 * 10 == 1540
assert 4 * PI * 7**2 == 616
assert 3 * PI * 7**2 == 462
assert sp.sqrt(3**2 + 4**2 + 12**2) == 13
assert sp.sqrt(7**2 + 24**2) == 25 and PI * 7 * 25 == 550
assert sp.Rational(4, 3) * PI * 6**3 == PI * 2**2 * 72  # sphere to wire of r=2
assert PI * (5**2 - 3**2) * 14 == 704
assert sp.Rational(8, 1) ** 3 == 512
assert sp.Rational(11, 10) ** 3 == sp.Rational(1331, 1000)
assert sp.Rational(1, 3) * 10**2 * 12 == 400
assert sp.Rational(1, 3) * PI * 6**2 * 3 == sp.Rational(4, 3) * PI * 3**3  # cone to sphere
assert sp.Rational(2, 3) * PI * 9**3 == PI * 3**2 * 54  # bowl to bottle
assert 12 * (7 - 2) == 60 and 6 * (7 - 2) ** 2 == 150 and (7 - 2) ** 3 == 125
assert 2 * (8 + 6) * 4 == 112
assert PI * 2**2 * 7 == 88
assert sp.Rational(1, 3) * PI * 7**2 * 24 == 1232
assert sp.sqrt(12**2 + 9**2 + 8**2) == 17
assert 500 * (2 * PI * sp.Rational(42, 100) * sp.Rational(120, 100)) == 1584  # road roller

# ---------------------------------------------------------------- subtopics
subtopics = [
S("m3d-cube-cuboid", "Cube and cuboid",
r"""
For a cube of edge $a$ and a cuboid $l\times b\times h$:

| Quantity | Cuboid | Cube |
|---|---|---|
| Volume | $lbh$ | $a^3$ |
| Lateral (4 walls) | $2(l+b)h$ | $4a^2$ |
| Total surface | $2(lb+bh+lh)$ | $6a^2$ |
| Space diagonal | $\sqrt{l^2+b^2+h^2}$ | $a\sqrt3$ |

The space diagonal is the **longest rod that fits in the room**. Wall questions use the lateral area only.
""",
[
F("Volume", r"V=lbh,\qquad V_{\text{cube}}=a^3"),
F("Lateral surface", r"LSA=2(l+b)h,\qquad LSA_{\text{cube}}=4a^2"),
F("Total surface", r"TSA=2(lb+bh+lh),\qquad TSA_{\text{cube}}=6a^2"),
F("Space diagonal", r"d=\sqrt{l^2+b^2+h^2},\qquad d_{\text{cube}}=a\sqrt3"),
],
[
T("Longest rod = space diagonal",
r"""A rod can poke corner-to-corner through the room: $\sqrt{l^2+b^2+h^2}$. Triplets like (3,4,12,13) exist:
$3^2+4^2+12^2=169=13^2$.""",
r"Find the length of the longest rod that can be placed in a room of dimensions $12\text{ m}\times9\text{ m}\times8\text{ m}$.",
r"$\sqrt{12^2+9^2+8^2}=\sqrt{144+81+64}=\sqrt{289}=17$ m."),
T("Painting/flooring picks the right area",
r"""Four walls → $2(l+b)h$ (ignore floor and roof). Full painting including roof and floor → TSA. Cost = area × rate.""",
r"A room is 8 m long, 6 m wide and 4 m high. Find the cost of painting its four walls at ₹10 per sq m.",
r"Four walls $=2(8+6)\times4=112$ sq m; cost $=112\times10=$ ₹1,120."),
],
[
"Using TSA where the question asks only for the four walls (or the reverse).",
"Cube diagonal $a\\sqrt3$ confused with the face diagonal $a\\sqrt2$.",
"Height left out of the wall formula: walls need $h$; floor area does not.",
]),
S("m3d-cylinder", "Cylinder",
r"""
For a cylinder of radius $r$ and height $h$:
- Volume $=\pi r^2h$ (capacity in litres: multiply $\text{m}^3$ by 1000)
- Curved surface $=2\pi rh$
- Total surface $=2\pi r(r+h)$
- A **hollow pipe/well** of inner radius $r$, outer radius $R$: volume of material $=\pi(R^2-r^2)h$
- A **wire/rod** is a very long thin cylinder: its volume is $\pi r^2\times\text{length}$.
""",
[
F("Volume", r"V=\pi r^2h"),
F("Curved surface", r"CSA=2\pi rh"),
F("Total surface", r"TSA=2\pi r(r+h)"),
F("Hollow cylinder", r"V=\pi(R^2-r^2)h"),
F("Capacity", r"1\ \text{m}^3=1000\ \ell"),
],
[
T("1 m³ = 1000 litres",
r"""Tank answers in litres: compute $\pi r^2h$ in metres, then ×1000. Keep radii in the units the answer needs.""",
r"A cylindrical water tank has a radius of 2 m and a depth of 7 m. Find its capacity in litres. [Use $\pi=\frac{22}{7}$]",
r"$V=\frac{22}{7}\times4\times7=88$ m$^3$ $=88{,}000$ litres."),
T("Hollow cylinder: difference of squared radii",
r"""Material volume $=\pi(R^2-r^2)h$ — the cross-section is a ring.""",
r"A metallic pipe has inner radius 3 cm, outer radius 5 cm and length 14 cm. Find the volume of metal. [Use $\pi=\frac{22}{7}$]",
r"$\frac{22}{7}\times(25-9)\times14=\frac{22}{7}\times224=704$ cu cm."),
],
[
"Using the outer radius alone for a hollow pipe.",
"Forgetting the 1000 factor when the answer is asked in litres.",
"CSA ($2\\pi rh$) and TSA ($2\\pi r(r+h)$) mixed up when the question mentions a closed drum or an open tank.",
]),
S("m3d-cone", "Cone",
r"""
For a cone of radius $r$, height $h$ and slant height $\ell=\sqrt{r^2+h^2}$:
- Volume $=\frac13\pi r^2h$ (exactly one-third of the cylinder on the same base)
- Curved surface $=\pi r\ell$
- Total surface $=\pi r(\ell+r)$
- If a cone is rolled from a sector of a circle: the sector's radius is $\ell$, and arc length $=2\pi r$.

The $r$-$h$-$\ell$ triangle is right-angled, so Pythagorean triplets (3,4,5), (7,24,25), (5,12,13) appear constantly.
""",
[
F("Slant height", r"\ell=\sqrt{r^2+h^2}"),
F("Volume", r"V=\frac13\pi r^2h"),
F("Curved surface", r"CSA=\pi r\ell"),
F("Total surface", r"TSA=\pi r(\ell+r)"),
],
[
T("Triplet for the slant height",
r"""Check for (3,4,5) or (7,24,25) among $r,h,\ell$ before computing a square root.""",
r"The radius of a cone is 7 cm and its height 24 cm. Find its curved surface area. [Use $\pi=\frac{22}{7}$]",
r"$\ell=\sqrt{7^2+24^2}=25$; CSA $=\frac{22}{7}\times7\times25=550$ sq cm."),
T("One-third of the cylinder",
r"""Equal base and height: $V_{\text{cone}}=\frac13V_{\text{cylinder}}$ — useful directly in ratio questions and for
conical heaps of sand/grain.""",
r"A conical tent has base radius 7 m and height 24 m. Find its volume. [Use $\pi=\frac{22}{7}$]",
r"$V=\frac13\times\frac{22}{7}\times49\times24=1232$ cu m."),
],
[
"Using $\\pi r^2h$ (cylinder volume) for a cone — the one-third is forgotten most often.",
"CSA computed with $h$ instead of $\\ell$.",
"Rounding $\\ell$ from a non-triplet when exact fractions were expected.",
]),
S("m3d-sphere", "Sphere and hemisphere",
r"""
- Sphere (radius $r$): volume $=\frac43\pi r^3$, surface $=4\pi r^2$.
- Hemisphere: volume $=\frac23\pi r^3$; curved surface $=2\pi r^2$; **total** surface $=3\pi r^2$ (adds the flat circular face).
- Melting and recasting conserves **volume** (surface area almost never matches — that option is a trap).
""",
[
F("Sphere", r"V=\frac43\pi r^3,\quad S=4\pi r^2"),
F("Hemisphere", r"V=\frac23\pi r^3,\quad S_{\text{curved}}=2\pi r^2,\quad S_{\text{total}}=3\pi r^2"),
F("Melting rule", r"V_{\text{before}}=V_{\text{after}}"),
F("Count of small spheres", r"\text{count}=\left(\frac{R}{r}\right)^3"),
],
[
T("Count small balls by the cube of the radius ratio",
r"""Number of small spheres $=\left(\frac{R}{r}\right)^3$. Radii in ratio 8:1 → 512 pieces, no π needed.""",
r"A solid metallic sphere of radius 8 cm is melted and drawn into small spheres of radius 1 cm. How many are formed?",
r"$\left(\frac81\right)^3=512$."),
T("Hemisphere TSA is three circles",
r"""$3\pi r^2$: two for the curved half (recall the sphere is $4\pi r^2$) plus one for the base.""",
r"Find the total surface area of a solid hemisphere of radius 7 cm. [Use $\pi=\frac{22}{7}$]",
r"$3\times\frac{22}{7}\times49=462$ sq cm."),
],
[
"Hemisphere TSA taken as $2\\pi r^2$ (that is the curved part only).",
"Melting questions answered with equality of surface areas.",
"$\\frac43\\pi r^3$ misremembered as $\\frac{4\\pi r^3}{3\\text{ or }2}$ variants — write the fraction before substituting.",
]),
S("m3d-prism-pyramid", "Prisms, pyramids and painted cubes",
r"""
- **Prism:** two parallel congruent bases; volume $=$ base area $\times$ height.
- **Pyramid:** volume $=\frac13\times$ base area $\times$ height.
- **Painted cube cut into $n^3$ unit cubes** (side $n$): cubes with 3 painted faces $=8$ (corners);
  2 faces $=12(n-2)$ (edges); 1 face $=6(n-2)^2$; unpainted $=(n-2)^3$.
""",
[
F("Prism volume", r"V=A_{\text{base}}\times h"),
F("Pyramid volume", r"V=\frac13A_{\text{base}}h"),
F("Painted-cube counts", r"3\text{f}=8,\ 2\text{f}=12(n-2),\ 1\text{f}=6(n-2)^2,\ 0\text{f}=(n-2)^3"),
],
[
T("Painted-cube formula table",
r"""Identify $n$ = number of small cubes along one edge. Corners are fixed at 8; the rest depend on $n-2$.""",
r"A cube of side 7 cm is painted on all faces and cut into 1 cm cubes. How many small cubes have exactly two faces painted?",
r"$12(n-2)=12\times5=60$. (One face: $6\times25=150$; none: $125$.)"),
T("Pyramid by one-third",
r"""Same base and height as a prism: the pyramid holds exactly one-third.""",
r"A pyramid stands on a square base of side 10 cm and is 12 cm high. Find its volume.",
r"$V=\frac13\times100\times12=400$ cu cm."),
],
[
"Forgetting the $\\frac13$ in pyramid (and cone) volumes.",
"Painted-cube formulas applied with $n$ = side length in cm instead of cubes per edge.",
"Counting corner cubes as 6 or edge cubes as $12(n-1)$.",
]),
]

patterns = [
P("Four walls / cost of painting a room", "very common",
  r"Room dimensions and a rate per sq m for painting walls or plastering.",
  r"LSA $=2(l+b)h$; multiply by rate. Roof/floor included only if stated."),
P("Melting and recasting", "very common",
  r"A sphere/cone/cylinder melted and recast into another shape; find a dimension or the count of pieces.",
  r"Equate volumes; for counts use the cube of the radius (or side) ratio. Ignore surface area completely."),
P("Tank capacity in litres", "common",
  r"Cylindrical or cuboidal tank; capacity asked in litres.",
  r"$\pi r^2h$ (or $lbh$) in m³, then ×1000; watch cm-to-m conversions."),
P("Cone with a Pythagorean triplet", "common",
  r"Radius and height given as (3,4), (6,8), (7,24); asked for CSA/TSA or volume.",
  r"$\ell$ from the triplet, then $\pi r\ell$; volume keeps $\frac13$."),
P("Longest rod / diagonal in 3D", "common",
  r"Longest pole/rod inside a room or cube.",
  r"Space diagonal $\sqrt{l^2+b^2+h^2}$; for a cube $a\sqrt3$."),
P("Painted cube cut into small cubes", "occasional",
  r"A painted cube is cut into equal small cubes; count cubes with 0/1/2/3 painted faces.",
  r"$8,\ 12(n-2),\ 6(n-2)^2,\ (n-2)^3$ with $n$ = cubes per edge."),
P("Percentage change in volume", "occasional",
  r"Sides of a cube change by x%; find the change in volume (or surface).",
  r"Volume factor $(1+x/100)^3$, surface factor $(1+x/100)^2$. +10% → +33.1% volume, +21% surface."),
]

# ---------------------------------------------------------------- solved examples
solved = []

solved.append(Q("m3d-s01",
r"A room is 12 m long, 9 m wide and 8 m high. Find the length of the longest pole that can be placed inside the room.",
[("17 m", 17), ("15 m", 15), ("19 m", 19), ("16 m", 16)], 17,
r"""
The longest pole fits along the space diagonal:

$\sqrt{12^2+9^2+8^2}=\sqrt{144+81+64}=\sqrt{289}=17$ m.
""",
r"12-9-8 → 17 is a stock diagonal: $144+81+64=289=17^2$. Trap: 15 m is the floor diagonal $\sqrt{12^2+9^2}$.",
"easy", "m3d-cube-cuboid", "space diagonal (longest rod)", 40))

solved.append(Q("m3d-s02",
r"A cylindrical tank of radius 2 m and depth 7 m is full of water. The capacity of the tank is: [Use $\pi=\frac{22}{7}$]",
[("88,000 litres", 88000), ("8,800 litres", 8800), ("880 litres", 880), ("44,000 litres", 44000)], 88000,
r"""
$V=\pi r^2h=\frac{22}{7}\times4\times7=88$ m$^3$.

$1$ m$^3=1000$ litres, so capacity $=88{,}000$ litres.
""",
r"$88$ m³ ×1000 → 88,000 L. Trap: 880 (×10) or answering in m³.",
"medium", "m3d-cylinder", "tank capacity in litres", 40))

solved.append(Q("m3d-s03",
r"A solid metallic cone of radius 6 cm and height 3 cm is melted and recast into a sphere. The radius of the sphere is:",
[("3 cm", 3), ("6 cm", 6), ("2 cm", 2), ("4 cm", 4)], 3,
r"""
$\frac13\pi r_c^2h=\frac43\pi R^3$

$\frac13\times36\times3=36=\frac43R^3\Rightarrow R^3=27\Rightarrow R=3$ cm.
""",
r"$V_{\text{cone}}=36\pi$; set $\frac43\pi R^3=36\pi$ → $R^3=27$ → 3 cm. Trap: 6 cm (radius unchanged) and 2 cm (took $R^3=36/4$ with a slip).",
"hard", "m3d-sphere", "melted cone to sphere", 60))

solved.append(Q("m3d-s04",
r"If each edge of a cube increases by 10%, the percentage increase in its volume is:",
[("33.1%", sp.Rational(331, 10)), ("30%", 30), ("21%", 21), ("33%", 33)], sp.Rational(331, 10),
r"""
Volume scales as the cube of the linear factor: $(1.1)^3=1.331$.

Increase $=33.1\%$. (Surface would rise by $(1.1)^2=1.21$, i.e. 21%.)
""",
r"$1.1^3=1.331$ → 33.1%. Traps: 30% (linear ×3), 21% (that is the **surface** increase).",
"medium", "m3d-cube-cuboid", "percentage change in volume", 35))

# ---------------------------------------------------------------- practice
pr = []

pr.append(Q("m3d-q01",
r"The volume of a cube of edge 6 cm is:",
[("216 cu cm", 216), ("36 cu cm", 36), ("1296 cu cm", 1296), ("18 cu cm", 18)], 216,
r"$V=a^3=6^3=216$ cu cm.",
r"$6^3=216$. Trap: 36 is the face area.",
"easy", "m3d-cube-cuboid", "cube volume", 20))

pr.append(Q("m3d-q02",
r"The total surface area of a cuboid of dimensions $8\text{ cm}\times6\text{ cm}\times4\text{ cm}$ is:",
[("208 sq cm", 208), ("104 sq cm", 104), ("192 sq cm", 192), ("216 sq cm", 216)], 208,
r"$TSA=2(lb+bh+lh)=2(48+24+32)=208$ sq cm.",
r"Half of 208 is 104 — the bracket sum; double it. Trap: 104 (no doubling).",
"easy", "m3d-cube-cuboid", "cuboid total surface", 30))

pr.append(Q("m3d-q03",
r"The volume of a cylinder of radius 7 cm and height 10 cm is: [Use $\pi=\frac{22}{7}$]",
[("1,540 cu cm", 1540), ("440 cu cm", 440), ("220 cu cm", 220), ("770 cu cm", 770)], 1540,
r"$V=\pi r^2h=\frac{22}{7}\times49\times10=1540$ cu cm.",
r"$49\times10\times22/7=1540$. Trap: 440 is the CSA ($2\pi rh$).",
"easy", "m3d-cylinder", "cylinder volume", 30))

pr.append(Q("m3d-q04",
r"The surface area of a sphere of radius 7 cm is: [Use $\pi=\frac{22}{7}$]",
[("616 sq cm", 616), ("462 sq cm", 462), ("308 sq cm", 308), ("154 sq cm", 154)], 616,
r"$S=4\pi r^2=4\times\frac{22}{7}\times49=616$ sq cm.",
r"$4\times154=616$. Trap: 462 is the hemisphere TSA ($3\pi r^2$); 308 is $2\pi r^2$.",
"easy", "m3d-sphere", "sphere surface area", 30))

pr.append(Q("m3d-q05",
r"The total surface area of a solid hemisphere of radius 7 cm is: [Use $\pi=\frac{22}{7}$]",
[("462 sq cm", 462), ("616 sq cm", 616), ("308 sq cm", 308), ("770 sq cm", 770)], 462,
r"$TSA=3\pi r^2=3\times\frac{22}{7}\times49=462$ sq cm.",
r"Three circles of $\pi r^2=154$ each → 462. Trap: 308 is only the curved half.",
"easy", "m3d-sphere", "hemisphere total surface", 30))

pr.append(Q("m3d-q06",
r"The diagonal of a cuboid of dimensions $3\text{ cm}\times4\text{ cm}\times12\text{ cm}$ is:",
[("13 cm", 13), ("12 cm", 12), ("19 cm", 19), (r"$\sqrt{24}$ cm", sp.sqrt(24))], 13,
r"$d=\sqrt{3^2+4^2+12^2}=\sqrt{169}=13$ cm.",
r"$9+16+144=169=13^2$. This cuboid is a stock triplet (3, 4, 12 → 13).",
"medium", "m3d-cube-cuboid", "cuboid diagonal", 35))

pr.append(Q("m3d-q07",
r"The radius of a cone is 7 cm and its height is 24 cm. Its curved surface area is: [Use $\pi=\frac{22}{7}$]",
[("550 sq cm", 550), ("528 sq cm", 528), ("1,100 sq cm", 1100), ("704 sq cm", 704)], 550,
r"$\ell=\sqrt{7^2+24^2}=25$ cm; CSA $=\pi r\ell=\frac{22}{7}\times7\times25=550$ sq cm.",
r"7-24-25 triplet: $\ell=25$, then $\pi\times7\times25=550$. Trap: 528 uses $h$ instead of $\ell$ ($2\pi rh$).",
"medium", "m3d-cone", "cone CSA with triplet", 40))

pr.append(Q("m3d-q08",
r"A solid metallic sphere of radius 6 cm is melted and drawn into a cylindrical wire of radius 2 mm. The length of the wire is:",
[("72 m", 72), ("7.2 m", sp.Rational(72, 10)), ("720 m", 720), ("36 m", 36)], 72,
r"""
Sphere: $V=\frac43\pi(6)^3=288\pi$ cu cm.

Wire radius: 2 mm $=0.2$ cm. $V_{\text{wire}}=\pi(0.2)^2L=0.04\pi L$.

$0.04\pi L=288\pi\Rightarrow L=7200$ cm $=72$ m.
""",
r"$288\pi/0.04\pi=7200$ cm. Units trap: 2 mm $=0.2$ cm; answer in metres divides by 100. 720 m forgot that step.",
"hard", "m3d-cylinder", "sphere melted into wire", 70))

pr.append(Q("m3d-q09",
r"A metallic pipe has inner radius 3 cm, outer radius 5 cm and length 14 cm. The volume of metal used is: [Use $\pi=\frac{22}{7}$]",
[("704 cu cm", 704), ("1,100 cu cm", 1100), ("396 cu cm", 396), ("308 cu cm", 308)], 704,
r"$V=\pi(R^2-r^2)h=\frac{22}{7}\times(25-9)\times14=\frac{22}{7}\times224=704$ cu cm.",
r"Ring area $22\times16=352$, ×14/2... directly: $\frac{22}{7}\times224=704$. Trap: 1100 uses only the outer cylinder.",
"medium", "m3d-cylinder", "hollow pipe volume", 45))

pr.append(Q("m3d-q10",
r"A solid sphere of radius 8 cm is melted and recast into small spheres of radius 1 cm each. The number of small spheres formed is:",
[512, 64, 8, 128], 512,
r"Volume ratio $=\left(\frac{8}{1}\right)^3=512$.",
r"Cube the radius ratio: $8^3=512$. Trap: 64 (squared the ratio — that is an area ratio).",
"medium", "m3d-sphere", "count of small spheres", 35))

pr.append(Q("m3d-q11",
r"If each edge of a cube increases by 10%, its volume increases by:",
[("33.1%", sp.Rational(331, 10)), ("30%", 30), ("21%", 21), ("10%", 10)], sp.Rational(331, 10),
r"$(1.1)^3=1.331$, so the increase is 33.1%.",
r"$1.1^3=1.331$. Trap: 21% is the surface increase; 30% treats volume as linear.",
"medium", "m3d-cube-cuboid", "percentage change in volume", 35))

pr.append(Q("m3d-q12",
r"A pyramid stands on a square base of side 10 cm and is 12 cm high. Its volume is:",
[("400 cu cm", 400), ("1200 cu cm", 1200), ("300 cu cm", 300), ("600 cu cm", 600)], 400,
r"$V=\frac13\times\text{base area}\times h=\frac13\times100\times12=400$ cu cm.",
r"$100\times12=1200$, then one-third → 400. Trap: 1200 forgot the $\frac13$.",
"medium", "m3d-prism-pyramid", "pyramid volume", 40))

pr.append(Q("m3d-q13",
r"A hemispherical bowl of internal radius 9 cm is full of water. The water is emptied into a cylindrical bottle of radius 3 cm. The height of water in the bottle is: [Use $\pi=\frac{22}{7}$]",
[("54 cm", 54), ("27 cm", 27), ("18 cm", 18), ("36 cm", 36)], 54,
r"""
Bowl: $V=\frac23\pi(9)^3=486\pi$.

Bottle: $\pi(3)^2h=486\pi\Rightarrow h=54$ cm.
""",
r"$486\pi/9\pi=54$. Keep π symbolic — it cancels. Trap: 18 cm uses the bowl volume as $\frac13\pi r^3$.",
"hard", "m3d-sphere", "hemispherical bowl into cylinder", 60))

pr.append(Q("m3d-q14",
r"A cube of side 7 cm is painted on all its faces and then cut into 1 cm cubes. How many of the small cubes have exactly two faces painted?",
[60, 54, 75, 90], 60,
r"$n=7$: cubes on edges (excluding corners) have exactly two painted faces: $12(n-2)=12\times5=60$.",
r"12 edges × 5 cubes each = 60. Trap: 54 ($6(n-2)^2$ mixing formulas), 75 (5³).",
"hard", "m3d-prism-pyramid", "painted cube: two-face count", 50))

pr.append(Q("m3d-q15",
r"A road roller of diameter 84 cm and length 120 cm rolls 500 times over a road. The area of the road levelled is: [Use $\pi=\frac{22}{7}$]",
[("1,584 sq m", 1584), ("3,168 sq m", 3168), ("792 sq m", 792), ("15,840 sq m", 15840)], 1584,
r"""
The roller levels with its curved surface: $CSA=2\pi rh=2\times\frac{22}{7}\times0.42\times1.2=3.168$ sq m.

Area $=500\times3.168=1584$ sq m.
""",
r"CSA in metres ($r=0.42$ m, $h=1.2$ m) is 3.168, then ×500 = 1584. Trap: 3168 doubles it; 792 halves it.",
"medium", "m3d-cylinder", "road roller area", 55))

topic = {
    "id": "mensuration-3d",
    "sectionId": "quant",
    "title": "Mensuration (3D)",
    "order": 15,
    "importance": "medium",
    "avgQuestions": {"tier1": 2, "tier2": 3},
    "summary": "Volumes and surface areas of cubes, cuboids, cylinders, cones, spheres, hemispheres, prisms and pyramids, plus melting-recasting, capacities and painted-cube counts. "
               "About 1-3 questions per shift; every question reduces to one formula plus a unit conversion, so memorising the formula sheet is nearly the whole job.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
