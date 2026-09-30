"""Readable rewrite of Mensuration 3-D (all 5 subtopics).

Plain English, one idea per section, every number recomputed below.
Run: python mensuration_3d.py  (patches content/core/topics/quant/mensuration-3d.json)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "mensuration-3d.json"

# ---------- answer checks (every number printed on the page) ----------
# cube & cuboid
assert 2 * (12 * 10 + 10 * 8 + 12 * 8) == 592 and 12 * 10 * 8 == 960   # TSA, V of 12x10x8
assert 2 * 8 * (12 + 10) == 352                                         # LSA of 12x10x8
assert 6 * 6 * 6 == 216 and 4 * 36 == 144 and 3 * 36 == 108             # cube a=6
assert 108 ** 0 == 1 and 36 * 3 == 108                                  # diagonal 6*sqrt3
assert 15 * 10 * 8 // 10 == 120 and 1200 == 1200                        # tank 1.5x1x0.8 -> L
assert 343 == 7 ** 3 and 6 * 49 == 294                                  # V 343 -> a 7 -> TSA 294
assert 5 ** 2 * 6 == 150 and 10 ** 2 * 6 == 600 and 4 * 150 == 600      # side doubled: TSA x4
assert 10 ** 3 == 1000 == 8 * 125                                       # volume x8
assert 12 * (4 - 2) == 24 and 6 * (4 - 2) ** 2 == 24 and (4 - 2) ** 3 == 8  # painted 4-cube
assert 8 + 24 + 24 + 8 == 64 == 4 ** 3                                  # counts add to total
# cylinder
assert 22 * 7 * 10 == 1540 and 2 * 22 * 10 == 440 and 440 + 308 == 748  # r 7, h 10
assert 2 * 22 * 49 // 7 == 308                                          # two ends = 2*pi*r^2
assert 154 * 10 == 1540                                                  # reverse: h = V/(pi r^2)
assert 22 * 196 == 4312 and 22 * 14 * 5 == 1540                          # area and CSA parts
assert 22 * 196 * 5 == 21560 and 21560 // 700 == 30 and 30800 == 308 * 100  # well 1.4 m, 5 m -> 30.8 m3
assert 4 * 2 == 8 and 8 // 2 == 4                                       # r doubled, h halved -> V x2
assert 22 * 49 * 12 // (7 * 3) == 616 // 1                              # cone 7,12 volume 616
assert 616 == 154 * 4                                                     # cylinder h = 4
# cone
assert 7 ** 2 + 24 ** 2 == 625 == 25 ** 2                               # 7-24-25
assert 22 * 25 == 550                                                   # CSA r7 l25
assert 132 * 3 * 7 == 2772 and 2772 // 198 == 14                        # V 132, r 3 -> h 14
assert 6 * 6 * 24 == 864 and 864 // 3 == 288                            # cone 6,24 -> 288*pi
assert 216 == 6 ** 3                                                    # sphere R from cone
assert 120 // 3 == 40                                                   # cone = 1/3 cylinder
assert 550 == 22 * 7 * 25 // 7                                          # tent canvas
# sphere
assert 4 * 154 == 616                                                   # sphere r 7 surface
assert 22 * 49 * 4 == 4312 and 4312 % 3 == 1                            # V = 4312/3
assert 3 * 154 == 462                                                   # hemisphere TSA r 7
assert 22 * 49 * 2 == 2156 and 2156 % 3 == 2                            # hemisphere V = 2156/3
assert 6 ** 3 == 216 and 216 // 8 == 27 == 3 ** 3                       # 8 small spheres r 3
assert 2 ** 3 == 8                                                      # radius doubled -> V x8
assert 3 ** 3 == 27 and 4 ** 3 == 64 and 9 == 3 ** 2 and 16 == 4 ** 2   # ratios 27:64, 9:16
# prism & pyramid
assert 20 * 12 == 240                                                   # prism
assert 10 * 10 * 12 // 3 == 400                                         # pyramid
assert 25 + 9 + 15 == 49 and 22 * 6 * 49 // 21 == 308                   # frustum
assert 27 + 64 + 125 == 216 == 6 ** 3                                   # melt 3,4,5 cubes
assert 40 * 13 // 2 == 260                                              # pyramid LSA

# ---------------- m3d-cube-cuboid ----------------
cb_concept = (
    "A cuboid has three dimensions l, b, h; a cube makes them equal. "
    "Volume is the product of the three; surface area adds the six faces. "
    "Capacity questions are volume questions with a litres conversion at the end."
)

cb_notes = r"""### The master table
| Quantity | Cuboid $l\times b\times h$ | Cube, edge $a$ |
|---|---|---|
| Volume | $lbh$ | $a^3$ |
| Lateral surface (4 walls) | $2h(l+b)$ | $4a^2$ |
| Total surface (6 faces) | $2(lb+bh+hl)$ | $6a^2$ |
| Diagonal | $\sqrt{l^2+b^2+h^2}$ | $a\sqrt3$ |

Cuboid $12\times10\times8$: volume $960$, walls $2\times8\times22=352$, total surface $2\times(120+80+96)=592$.

Reverse works too: volume $960$ with two dimensions $12$ and $10$ leaves the third as $\dfrac{960}{120}=8$. Attach square units to areas and cubic units to volumes, always.

> **Rule:** Total surface is the walls plus top and bottom. Lateral surface alone skips the two $l\times b$ faces.

### Cube shortcuts
Edge $6$: volume $216$, lateral $144$, total $216$, diagonal $6\sqrt3$. The diagonal formula comes from using the cuboid diagonal with all three sides equal. A cube of volume $216$ has edge $6$; volume $125$ gives edge $5$.

Doubling every edge multiplies area by $4$ and volume by $8$. Edge $5\to10$: total surface $150\to600$, volume $125\to1000$.

> **Tip:** Lengths take $k$, areas $k^2$, volumes $k^3$. Count what kind of quantity is asked before multiplying anything.

### Capacity and cost
One cubic metre holds $1000$ litres, one litre is $1000$ cubic centimetres. A tank $1.5\times1\times0.8$ m has volume $1.2$ m$^3$, which is $1200$ litres.

Cost questions multiply volume by a rate: digging at Rs $20$ per m$^3$ costs $20\times1.2=$ Rs $24$ for that tank. Match the rate's units to the volume's units before multiplying.

> **Watch:** Convert units exactly once, at the end. Mixing cm and m midway is where capacity questions die.

### Reverse questions
Given the volume or surface, peel back to the edge, then forward to the asked quantity.

Volume $343$ cu cm means edge $7$ (since $7^3=343$); total surface is then $6\times49=294$ sq cm. Two steps, no algebra.

> **Remember:** Learn the cubes up to $12$: $1,8,27,64,125,216,343,512,729,1000,1331,1728$. Reverse questions then need no cube roots.

### Painted cubes
An $n\times n\times n$ cube painted outside, cut into unit cubes:
- $3$ faces painted: the $8$ corners
- $2$ faces: the edges, $12(n-2)$
- $1$ face: face centres, $6(n-2)^2$
- $0$ faces: inside, $(n-2)^3$

A $4$ cm cube cut into $1$ cm cubes: $8$, $24$, $24$, $8$. The four counts always add to $n^3=64$. A $3$ cm cube gives $8$, $12$, $6$, $1$.

> **Tip:** Only corner cubes get three faces, always exactly $8$. Start there, then fill the edge and face counts. Slice counts never change when the whole cube is dipped instead of brushed.
"""

cb_formulas = [
    {"name": "Cuboid", "tex": r"V=lbh,\quad \text{LSA}=2h(l+b),\quad \text{TSA}=2(lb+bh+hl)", "note": "l, b, h are the three dimensions."},
    {"name": "Cube", "tex": r"V=a^3,\quad \text{LSA}=4a^2,\quad \text{TSA}=6a^2", "note": "a = edge."},
    {"name": "Diagonals", "tex": r"d=\sqrt{l^2+b^2+h^2},\quad d_{\text{cube}}=a\sqrt3", "note": "Corner to opposite corner."},
    {"name": "Capacity", "tex": r"1\text{ m}^3=1000\text{ L},\quad 1\text{ L}=1000\text{ cm}^3", "note": "Convert once, at the end."},
    {"name": "Painted cube counts", "tex": r"8,\ 12(n-2),\ 6(n-2)^2,\ (n-2)^3", "note": "3, 2, 1, 0 painted faces for n by n by n."},
]

cb_tricks = [
    {
        "title": "Cubes table, not cube roots",
        "body": "Know the cubes to 12 by heart. Reverse questions become look-ups: 343 is 7 cubed.",
        "example": {
            "q": "The volume of a cube is 343 cu cm. Its total surface area is:",
            "steps": [r"$343=7^3$, so the edge is $7$ cm.", r"TSA $=6\times7^2$.", r"$=294$ sq cm."],
            "answer": "294 sq cm",
        },
    },
    {
        "title": "Capacity: metres to litres",
        "body": "Compute the volume in cubic metres, then multiply by 1000 for litres. Never by 100.",
        "example": {
            "q": "A tank is 1.5 m long, 1 m wide and 0.8 m deep. Its capacity in litres is:",
            "steps": [r"$V=1.5\times1\times0.8=1.2$ m$^3$.", r"$1.2\times1000$.", r"$=1200$ litres."],
            "answer": "1200 litres",
        },
    },
    {
        "title": "Edge scaling in powers",
        "body": "Edge times k: surface times k squared, volume times k cubed. Doubling is 4 and 8.",
        "example": {
            "q": "Each edge of a cube of edge 5 cm is doubled. The total surface area becomes:",
            "steps": [r"Old TSA $=6\times25=150$.", r"Area scales by $2^2=4$.", r"$150\times4=600$ sq cm."],
            "answer": "600 sq cm",
        },
    },
]

cb_mistakes = [
    {"wrong": "Using $6lb$ as the cuboid total surface.", "right": "It is $2(lb+bh+hl)$. For $12\\times10\\times8$ that is 592, not 720."},
    {"wrong": "Forgetting the two $lb$ faces in total surface.", "right": "Total = lateral + top + bottom. Lateral $352$ plus $2\\times120=240$ gives 592."},
    {"wrong": "Multiplying cubic metres by 100 for litres.", "right": "One cubic metre is $1000$ litres: $1.2$ m$^3$ is 1200 L."},
    {"wrong": "Doubling the edge and doubling the volume.", "right": "Volume takes the cube of the scale: $2^3=8$ times, so $125\\to1000$."},
    {"wrong": "Painted-cube corner counts other than 8.", "right": "Only the 8 corners carry three painted faces, whatever $n$ is."},
]

cb_revision = [
    "Cuboid: $V=lbh$, walls $2h(l+b)$, total $2(lb+bh+hl)$.",
    "Cube: $V=a^3$, walls $4a^2$, total $6a^2$, diagonal $a\\sqrt3$.",
    "$1$ m$^3=1000$ L and $1$ L $=1000$ cm$^3$; convert once at the end.",
    "Reverse questions: recall the cube from the table ($343\\to7$), then move forward.",
    "Scale $k$: areas $\\times k^2$, volumes $\\times k^3$.",
    "Painted $n$-cube: $8$ corners, $12(n-2)$ edges, $6(n-2)^2$ faces, $(n-2)^3$ inside.",
]

def pat(pid, name, freq, spot, steps, why, q, esteps, ans):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot,
            "steps": steps, "why": why, "example": {"q": q, "steps": esteps, "answer": ans}}

cb_patterns = [
    pat("m3d-cb-p1", "Volume and surface area of cuboid/cube", "very common",
        "Three dimensions given, volume or a surface asked.",
        [r"Volume: multiply all three.", r"Lateral: $2h(l+b)$.",
         r"Total: $2(lb+bh+hl)$, or $6a^2$ for a cube.", r"Attach square or cubic units."],
        "Both formulas are one substitution each once the dimensions are named.",
        "Find the total surface area of a cuboid 12 cm x 10 cm x 8 cm.",
        [r"$2\times(12\times10+10\times8+12\times8)$.", r"$=2\times296=592$ sq cm."],
        "592 sq cm"),
    pat("m3d-cb-p2", "Cube specifics: diagonal, lateral area, edges", "common",
        "A cube with one length given; a diagonal or surface asked.",
        [r"Write the cube formulas in terms of the edge $a$.", r"Diagonal $=a\sqrt3$.",
         r"Lateral $=4a^2$, total $=6a^2$."],
        "One variable drives every cube quantity, so a single given length answers everything.",
        "The length of the diagonal of a cube of side 6 cm is:",
        [r"$d=a\sqrt3$.", r"$=6\sqrt3$ cm."],
        "6*sqrt(3) cm"),
    pat("m3d-cb-p3", "Tank capacity in litres / volume cost", "very common",
        "A tank, pit or room with dimensions; litres or rupees asked.",
        [r"Compute the volume in cubic metres.", r"Capacity: multiply by $1000$.",
         r"Cost: multiply by the rate per cubic metre."],
        "Capacity and cost are both volume times a constant, so the geometry happens once.",
        "A tank is 1.5 m long, 1 m wide and 0.8 m deep. Its capacity in litres is:",
        [r"$V=1.2$ m$^3$.", r"$1.2\times1000=1200$ litres."],
        "1200 litres"),
    pat("m3d-cb-p4", "Reverse: from volume or area back to a side", "common",
        "A volume or surface area given, an edge or another quantity asked.",
        [r"Match the volume to a known cube ($7^3=343$).", r"Recover the edge.",
         r"Substitute into the asked formula."],
        "Reverse questions are look-ups when the cube table is memorised, algebra when it is not.",
        "The volume of a cube is 343 cu cm. Its total surface area is:",
        [r"$343=7^3$, edge $=7$ cm.", r"TSA $=6\times49=294$ sq cm."],
        "294 sq cm"),
    pat("m3d-cb-p5", "Painted cube cut into unit cubes", "common",
        "A big painted cube sliced into equal small cubes; a count asked.",
        [r"Find $n$: big edge over small edge.", r"Three painted faces: $8$ corners.",
         r"Two: $12(n-2)$; one: $6(n-2)^2$; none: $(n-2)^3$."],
        "Position, not luck, decides how many painted faces a small cube carries; the counts are pure formulas.",
        "A cube of 4 cm edge is painted on all faces and cut into 1 cm cubes. How many small cubes have exactly two painted faces?",
        [r"$n=\dfrac{4}{1}=4$.", r"Two faces: $12(n-2)=12\times2=24$."],
        "24"),
]

# ---------------- m3d-cylinder ----------------
cy_concept = (
    "A cylinder of radius r and height h has volume pi r squared h and curved surface two pi r h. "
    "The total surface adds the two circular ends. "
    "Most questions either substitute directly or reverse one dimension from the volume."
)

cy_notes = r"""### The three formulas
$$V=\pi r^2h,\qquad \text{CSA}=2\pi rh,\qquad \text{TSA}=2\pi r(h+r)$$
TSA is the curved surface plus both circles: $2\pi rh+2\pi r^2$.

Radius $7$, height $10$: volume $\dfrac{22}{7}\times49\times10=1540$; CSA $2\times\dfrac{22}{7}\times7\times10=440$; TSA $440+308=748$. Check TSA the second way: $2\pi r(h+r)=2\times\dfrac{22}{7}\times7\times17=748$.

> **Rule:** Fix the radius first and keep it factored. The $r$ cancels out of most reverse questions.

### Reverse: find the missing dimension
Volume $1540$ with radius $7$: $h=\dfrac{1540}{154}=10$, because $\pi r^2=\dfrac{22}{7}\times49=154$. One division, and the same trick answers every reverse question.

The same move finds the radius when the height is given: $r^2=\dfrac{V}{\pi h}$, then recall the square. And the CSA reverses the same way: $440=2\times\dfrac{22}{7}\times7\times h$ gives $h=10$.

> **Tip:** $\pi r^2$ for $r=7$ is $154$; for $r=14$ it is $616$; for $r=21$ it is $1386$. Halves appear too: $r=3.5$ gives $38.5$. These four end up everywhere.

### Pipes, wells and capacity
A hollow pipe or a well uses the same cylinder; a pipe's length plays the height's role. Well of radius $1.4$ m and depth $5$ m:
$$V=\frac{22}{7}\times1.96\times5=30.8\text{ m}^3=30{,}800\text{ litres}$$

Cost of digging multiplies the volume by the rate per cubic metre, exactly like tank questions. At Rs $25$ per m$^3$, that well costs $25\times30.8=$ Rs $770$.

A one-litre bottle holds $1000$ cu cm; the tank and bottle rules are one rule.

> **Watch:** Radius $1.4$ m is $140$ cm if the question mixes units. Pick one unit before the first line.

### Changing the dimensions
- Radius doubled, height same: volume $4$ times, curved surface $2$ times.
- Radius doubled, height halved: volume $2$ times.
- Height alone doubled: volume $2$ times, curved surface $2$ times.
- Radius and height both doubled: volume $8$ times.

The exponent tracks the factor: $r$ appears squared in the volume, once in the curved surface.

> **Remember:** Ask which symbols the change touches. Volume $V=\pi r^2h$: scale $r^2$ by $4$ and $h$ by $\dfrac12$, net $2$.

### Melting into a cylinder
Volume survives a melt. The shape changes; the amount of metal does not. A cone of radius $7$, height $12$ has volume $\dfrac13\times154\times12=616$; poured into a cylinder of radius $7$ it reaches height $\dfrac{616}{154}=4$ cm.

> **Tip:** Melted questions never need the second solid's shape knowledge beyond its volume formula. Equate volumes, solve for one length.
"""

cy_formulas = [
    {"name": "Cylinder", "tex": r"V=\pi r^2h,\quad \text{CSA}=2\pi rh,\quad \text{TSA}=2\pi r(h+r)", "note": "r = radius, h = height."},
    {"name": "Missing height", "tex": r"h=\frac{V}{\pi r^2}", "note": "Reverse of the volume formula."},
    {"name": "Capacity", "tex": r"\text{litres}=\text{m}^3\times1000", "note": "Same conversion as tanks."},
    {"name": "Dimension change", "tex": r"V\propto r^2h,\quad \text{CSA}\propto rh", "note": "Scale each symbol by its own factor."},
]

cy_tricks = [
    {
        "title": "154 and friends",
        "body": "pi r squared for r = 7, 14, 21 is 154, 616, 1386. Reverse questions then divide by a friendly number.",
        "example": {
            "q": "The volume of a cylinder is 1540 cu cm and its radius is 7 cm. Its height is:",
            "steps": [r"$\pi r^2=\dfrac{22}{7}\times49=154$.", r"$h=\dfrac{1540}{154}$.", r"$h=10$ cm."],
            "answer": "10 cm",
        },
    },
    {
        "title": "Scale the symbols, not the shape",
        "body": "Radius doubled, height halved: volume factor is 4 times 1/2 = 2. Track r squared and h separately.",
        "example": {
            "q": "The radius of a cylinder is doubled and its height is halved. Its volume becomes:",
            "steps": [r"$r^2$ factor: $2^2=4$.", r"$h$ factor: $\dfrac12$.", r"Net: $4\times\dfrac12=2$ times."],
            "answer": "2 times",
        },
    },
    {
        "title": "Melt: equate volumes",
        "body": "Melting conserves volume. Write both volume formulas equal, cancel, solve for the new length.",
        "example": {
            "q": "A cone of radius 7 cm and height 12 cm is melted into a cylinder of radius 7 cm. The cylinder's height is:",
            "steps": [r"Cone: $\dfrac13\times\dfrac{22}{7}\times49\times12=616$ cu cm.", r"$616=\dfrac{22}{7}\times49\times h=154h$.", r"$h=4$ cm."],
            "answer": "4 cm",
        },
    },
]

cy_mistakes = [
    {"wrong": "Using the diameter in $\\pi r^2h$.", "right": "Radius only. Diameter $14$ means $r=7$."},
    {"wrong": "Calling the CSA the total surface.", "right": "TSA $=$ CSA $+$ two ends: $440+308=748$, not 440."},
    {"wrong": "Multiplying cubic metres by 100 for litres.", "right": "The factor is $1000$: $30.8$ m$^3$ is 30,800 L."},
    {"wrong": "Scaling volume by $2$ when only the radius doubles.", "right": "$r$ is squared: volume $\\times4$. Height halving then brings it to $\\times2$."},
    {"wrong": "Re-deriving $\\pi r^2$ every line.", "right": "Factor it once ($154$ for $r=7$) and reuse; errors drop sharply."},
]

cy_revision = [
    "$V=\\pi r^2h$, CSA $=2\\pi rh$, TSA $=2\\pi r(h+r)$.",
    "Reverse: $h=\\dfrac{V}{\\pi r^2}$; know $154$, $616$, $1386$ for $r=7,14,21$.",
    "Wells and pipes are cylinders; litres $=$ m$^3\\times1000$.",
    "Radius doubles: volume $\\times4$, CSA $\\times2$; both double: volume $\\times8$.",
    "Melting keeps volume: equate the two formulas, cancel, solve.",
]

cy_patterns = [
    pat("m3d-cy-p1", "Volume, CSA and TSA of a cylinder", "very common",
        "Radius and height given, a quantity asked.",
        [r"Volume: $\pi r^2h$.", r"CSA: $2\pi rh$.",
         r"TSA: add $2\pi r^2$ for the ends."],
        "Three direct substitutions cover the whole pattern; only the arithmetic changes.",
        "Find the volume of a cylinder of radius 7 cm and height 10 cm.",
        [r"$V=\dfrac{22}{7}\times49\times10$.", r"$V=1540$ cu cm."],
        "1540 cu cm"),
    pat("m3d-cy-p2", "Reverse: solve for the missing dimension", "common",
        "Volume plus one dimension, the other asked.",
        [r"Write $V=\pi r^2h$ with the knowns in.", r"Compute $\pi r^2$ (or $\pi h$) as one number.",
         r"Divide to isolate the unknown."],
        "One equation with one hidden quantity; the pi terms cancel to a clean division.",
        "The volume of a cylinder is 1540 cu cm and its radius is 7 cm. Its height is:",
        [r"$\pi r^2=154$.", r"$h=\dfrac{1540}{154}=10$ cm."],
        "10 cm"),
    pat("m3d-cy-p3", "Hollow pipe and well capacity", "common",
        "A pipe or well with radius and length; litres or cost asked.",
        [r"Treat it as a cylinder: $V=\pi r^2h$.", r"Convert cubic metres to litres by $1000$.",
         r"For cost, multiply by the rate."],
        "Wells and pipes add only a units conversion on top of the standard volume.",
        "A cylindrical well has radius 1.4 m and depth 5 m. Its capacity in litres is:",
        [r"$V=\dfrac{22}{7}\times1.96\times5=30.8$ m$^3$.", r"$30.8\times1000=30{,}800$ litres."],
        "30,800 litres"),
    pat("m3d-cy-p4", "Dimension-change multipliers", "common",
        "A radius or height scaled; the new volume or surface asked.",
        [r"Note the factor on each symbol.", r"Raise it to the symbol's power ($r^2$ in volume).",
         r"Multiply the factors."],
        "No recomputation needed: the formula's exponents convert scale factors directly.",
        "The radius of a cylinder is doubled and its height is halved. Its volume becomes:",
        [r"$r^2$ gives $4$, $h$ gives $\dfrac12$.", r"$4\times\dfrac12=2$ times."],
        "2 times"),
    pat("m3d-cy-p5", "Melting another solid into a cylinder", "common",
        "A cone, sphere or cubes melted and recast as a cylinder.",
        [r"Compute the source volume.", r"Set it equal to $\pi r^2h$ of the cylinder.",
         r"Solve for the asked length."],
        "Melting conserves volume, so the cylinder formula becomes a one-unknown equation.",
        "A cone of radius 7 cm and height 12 cm is melted into a cylinder of radius 7 cm. The cylinder's height is:",
        [r"$V_{\text{cone}}=\dfrac13\times154\times12=616$ cu cm.", r"$154h=616$.", r"$h=4$ cm."],
        "4 cm"),
]

# ---------------- m3d-cone ----------------
co_concept = (
    "A cone of radius r and height h has slant height root of r squared plus h squared. "
    "Its volume is one third of a cylinder on the same base; its curved surface is pi r l. "
    "Radius-height-slant triples are Pythagorean triplets, most often 3-4-5 and 7-24-25."
)

co_notes = r"""### The three lengths first
$$\ell=\sqrt{r^2+h^2}$$
Radius $7$ and height $24$ give slant $25$: the $7$-$24$-$25$ triplet. Check for a triplet before squaring anything. Radius $21$ with height $28$ gives slant $35$, and $\dfrac{22}{7}\times21\times35=2310$ sq cm of curved surface.

The three lengths make a right triangle inside the cone: radius and height at right angles, slant along the surface. Families to know: $3$-$4$-$5$ and its multiples, $7$-$24$-$25$, $8$-$15$-$17$, $12$-$35$-$37$.

A classic ratio: cylinder, hemisphere and cone on the same base with cylinder height $=$ radius hold volumes $3:2:1$.

> **Rule:** Find $\ell$ first. Both surface formulas need it, and triplet spotting avoids the root.

### Volume and the one-third
$$V=\frac{1}{3}\pi r^2h$$
Exactly one-third of the cylinder with the same base and height. A cylinder of volume $120$ pairs with a cone of $40$. Radius $7$ with height $9$ gives $V=\dfrac13\times154\times9=462$ cu cm.

The factor $\dfrac13$ also runs in reverse: cone volume $132$ with radius $3$ gives height $\dfrac{132\times3}{\dfrac{22}{7}\times9}=14$ cm.

> **Tip:** Multiply by $3$ before dividing by $\pi r^2$. Keeping the fraction until the end invites slips.

### Surfaces
- Curved surface: $\pi r\ell$. Radius $7$, slant $25$: $\dfrac{22}{7}\times7\times25=550$ sq cm.
- Total surface: $\pi r\ell+\pi r^2$, the skirt plus the circular base. Same cone: $550+154=704$ sq cm.

A conical tent uses the curved surface only: no floor. Canvas for radius $7$ m and slant $25$ m is $550$ sq m. A heap whose base circumference is $44$ m has radius $\dfrac{44\times7}{44}=7$ m, so slant $25$ m again means $550$ sq m of sheet.

> **Watch:** Tents and caps are curved surface; ice-cream cones and solid cones are total surface. Read what is covered.

### Melting a cone
Volume survives. A cone of radius $6$, height $24$ has volume $288\pi$; as a sphere:
$$\frac{4}{3}\pi R^3=288\pi \Rightarrow R^3=216 \Rightarrow R=6$$
The sphere comes out with the same $6$ cm radius, a clean coincidence worth noticing. And $216=6^3$ came straight from the cubes table, not a calculator.

The reverse melt works the same way: a sphere of radius $6$ recast as a cone of radius $6$ needs $\dfrac13\times36\times h=288$, so $h=24$ cm.

### Heaps and tents
A heap of rice is a cone: base circumference gives the radius, slant gives the canvas or sheet. Cloth width questions divide the curved area by the width.

> **Remember:** Cone problems are two-part: the inner right triangle for lengths, then one formula for the asked quantity.
"""

co_formulas = [
    {"name": "Slant height", "tex": r"\ell=\sqrt{r^2+h^2}", "note": "Radius, height, slant: a right triangle."},
    {"name": "Cone volume", "tex": r"V=\frac{1}{3}\pi r^2h", "note": "One-third of the same-base cylinder."},
    {"name": "Cone surfaces", "tex": r"\text{CSA}=\pi r\ell,\quad \text{TSA}=\pi r(\ell+r)", "note": "Skirt alone, or skirt plus base."},
    {"name": "Same base ratios", "tex": r"V_{\text{cone}}=\frac{V_{\text{cyl}}}{3}", "note": "Equal base and height."},
]

co_tricks = [
    {
        "title": "Hunt the triplet",
        "body": "7-24-25, 3-4-5 and their multiples cover nearly every cone. Two lengths known, read the third.",
        "example": {
            "q": "The radius of a cone is 7 cm and its height is 24 cm. Its curved surface area is:",
            "steps": [r"$\ell=\sqrt{49+576}=25$ cm (triplet).", r"CSA $=\dfrac{22}{7}\times7\times25$.", r"$=550$ sq cm."],
            "answer": "550 sq cm",
        },
    },
    {
        "title": "One-third both ways",
        "body": "Cone to cylinder: divide by 3. Cone volume given: multiply by 3 before dividing by the base area.",
        "example": {
            "q": "The volume of a cone is 132 cu cm and its base radius is 3 cm. Its height is:",
            "steps": [r"$132\times3=396$.", r"$\pi r^2=\dfrac{22}{7}\times9=\dfrac{198}{7}$.", r"$h=396\div\dfrac{198}{7}=14$ cm."],
            "answer": "14 cm",
        },
    },
    {
        "title": "Tent = curved surface",
        "body": "Canvas touches only the slanted side, so use pi r l. Add the base circle only for a solid cone.",
        "example": {
            "q": "A conical tent has base radius 7 m and slant height 25 m. The canvas required to make it (sq m) is:",
            "steps": [r"CSA $=\dfrac{22}{7}\times7\times25$.", r"$=550$ sq m."],
            "answer": "550 sq m",
        },
    },
]

co_mistakes = [
    {"wrong": "Using $\\pi rh$ for the curved surface.", "right": "It is $\\pi r\\ell$ with the slant. For 7 and 24 that means 550, not $\\pi\\times7\\times24$."},
    {"wrong": "Treating the slant as the height.", "right": "Height is the drop down the middle; slant runs along the surface. $\\ell=\\sqrt{r^2+h^2}$."},
    {"wrong": "Forgetting the $\\dfrac13$ in the cone volume.", "right": "A cone is one-third of its cylinder: $120$ cylinder means $40$ cone."},
    {"wrong": "Adding the base to a tent's canvas.", "right": "Tents need the curved surface $\\pi r\\ell$ only."},
    {"wrong": "Cancelling $\\pi$ but not the $\\dfrac13$ when melting.", "right": "Carry the one-third: $288\\pi$ as a sphere gives $R^3=216$, $R=6$."},
]

co_revision = [
    "Slant $\\ell=\\sqrt{r^2+h^2}$; hunt for triplets first.",
    "$V=\\dfrac13\\pi r^2h$: one-third of the same-base cylinder.",
    "CSA $=\\pi r\\ell$; TSA adds the base circle.",
    "Tents and caps: curved surface only.",
    "Melting keeps volume: equate $\\dfrac13\\pi r^2h$ with the new solid's formula.",
]

co_patterns = [
    pat("m3d-co-p1", "Slant height and CSA/TSA with a triplet", "very common",
        "Radius and height given, slant or a surface asked.",
        [r"Look for a triplet among $r$, $h$, $\ell$.", r"Compute $\ell$ if missing.",
         r"CSA $=\pi r\ell$; TSA adds $\pi r^2$."],
        "The inner right triangle settles the lengths, then one multiplication finishes.",
        "The radius of a cone is 7 cm and its height is 24 cm. Its curved surface area is:",
        [r"$\ell=\sqrt{49+576}=25$.", r"CSA $=\dfrac{22}{7}\times7\times25=550$ sq cm."],
        "550 sq cm"),
    pat("m3d-co-p2", "Volume of a cone (and reverse)", "very common",
        "Volume asked from dimensions, or a dimension from the volume.",
        [r"$V=\dfrac{1}{3}\pi r^2h$.", r"Reverse: multiply the volume by $3$.",
         r"Divide by the known factors to isolate the unknown."],
        "The one-third factor runs both directions with one multiplication.",
        "The volume of a cone is 132 cu cm and its base radius is 3 cm. Its height is:",
        [r"$3V=396$.", r"$\pi r^2=\dfrac{198}{7}$.", r"$h=396\times\dfrac{7}{198}=14$ cm."],
        "14 cm"),
    pat("m3d-co-p3", "Recasting: cone into sphere or spheres", "common",
        "A cone melted and recast; a radius of the new solid asked.",
        [r"Write the cone volume.", r"Set it equal to the target solid's volume.",
         r"Cancel $\pi$, solve the remaining equation."],
        "Melting conserves volume, and the pi cancels, leaving integer arithmetic.",
        "A solid metallic cone of radius 6 cm and height 24 cm is melted into a sphere. The radius of the sphere is:",
        [r"$V=\dfrac13\pi\times36\times24=288\pi$.", r"$\dfrac43\pi R^3=288\pi\Rightarrow R^3=216$.", r"$R=6$ cm."],
        "6 cm"),
    pat("m3d-co-p4", "Cone vs cylinder and hemisphere ratios", "common",
        "Two solids on the same base; a volume ratio asked.",
        [r"Same base and height: cone $=$ one-third of cylinder.",
         r"Hemisphere on the same radius: volume $\dfrac23\pi r^3$.",
         r"Compare by dividing the formulas."],
        "With equal bases the pi and radius cancel, so ratios come from the constants alone.",
        "A cylinder and a cone have equal bases and equal heights. If the cylinder's volume is 120 cu cm, the cone's volume is:",
        [r"Cone $=\dfrac13$ of the cylinder.", r"$\dfrac{120}{3}=40$ cu cm."],
        "40 cu cm"),
    pat("m3d-co-p5", "Conical heap or tent word problems", "common",
        "A tent, heap or cap; canvas, cloth or sheet area asked.",
        [r"Extract $r$ (from circumference if needed) and $\ell$.", r"Tent: CSA $=\pi r\ell$.",
         r"Cloth width: divide the area by the width."],
        "Real-world wording hides the same two formulas; the curved surface is almost always the target.",
        "A conical tent has base radius 7 m and slant height 25 m. The canvas required to make it (sq m) is:",
        [r"CSA $=\dfrac{22}{7}\times7\times25$.", r"$=550$ sq m."],
        "550 sq m"),
]

# ---------------- m3d-sphere ----------------
sp_concept = (
    "A sphere of radius r has volume four-thirds pi r cubed and surface four pi r squared. "
    "A hemisphere is half a sphere for volume, but its total surface is three pi r squared because it adds the flat circle. "
    "Radius scaling cubes for volume and squares for surface."
)

sp_notes = r"""### The sphere pair
$$V=\frac{4}{3}\pi r^3,\qquad S=4\pi r^2$$
Radius $7$: surface $4\times154=616$ sq cm; volume $\dfrac43\times\dfrac{22}{7}\times343=\dfrac{4312}{3}\approx1437.3$ cu cm.

Radius $14$: surface $4\times616=2464$ sq cm; volume $\dfrac43\times\dfrac{22}{7}\times2744=\dfrac{34496}{3}$ cu cm, exactly $8$ times the radius-$7$ volume. Radius $3.5$: surface $154$ sq cm, volume $\dfrac{539}{3}\approx179.7$ cu cm.

The surface formula is exactly four circles of the same radius. Half of it, $2\pi r^2$, is the hemisphere's curved part. A sphere also fills exactly two-thirds of the cylinder that tightly contains it.

> **Rule:** Surface grows with $r^2$, volume with $r^3$. Doubling the radius gives $4$ times the surface and $8$ times the volume, as the $7\to14$ line above shows.

### Hemisphere: three halves and three pi
- Volume: $\dfrac{2}{3}\pi r^3$ (half the sphere).
- Curved surface: $2\pi r^2$ (half the shell).
- **Total surface: $3\pi r^2$** because the flat circular face $\pi r^2$ joins the shell.

Radius $7$: curved $308$, total $3\times154=462$, volume $\dfrac{2156}{3}$ cu cm. Radius $21$: curved $2772$, total $4158$, all from the $1386$ base circle.

> **Watch:** 'Total surface of a hemisphere' is $3\pi r^2$, never $2\pi r^2$. The flat face counts once it is solid.

### Melting and dividing
A sphere of radius $6$ melted into $8$ equal small spheres: each carries $\dfrac{216}{8}=27$ of the cubed length, so each radius is $3$.

Count multiplies the volume, so the radius shrinks by the cube root of the count. Eight pieces mean half the radius; $27$ pieces mean one-third; counts $1,8,27$ pair with radius factors $1,\dfrac12,\dfrac13$.

> **Tip**: When a big solid becomes $n$ equal small ones, divide the cubed length by $n$, then take the cube root.

### Displacing water
A solid dropped in a full tub pushes out its own volume. Sphere of radius $3$ in a full tank: overflow $=\dfrac43\pi\times27=36\pi$ cu cm.

In a partly filled cylinder the level rises instead: sphere of radius $7$ into a cylinder of radius $14$ raises the water by $\dfrac{4312/3}{616}=\dfrac73$ cm. Read the story: 'water level rose' means the rise's cylinder volume equals the sphere's volume.

### Radius ratios
Radii $3:4$ give volumes $27:64$ and surfaces $9:16$. Cube the ratio for volumes, square it for surfaces, and say which one the question wants. Equal surfaces force equal radii; equal volumes likewise.

> **Remember:** Ratio questions never need pi. Cancel it first, then compare powers of the ratio.
"""

sp_formulas = [
    {"name": "Sphere", "tex": r"V=\frac{4}{3}\pi r^3,\quad S=4\pi r^2", "note": "One radius drives both."},
    {"name": "Hemisphere", "tex": r"V=\frac{2}{3}\pi r^3,\quad \text{curved}=2\pi r^2,\quad \text{total}=3\pi r^2", "note": "Total adds the flat circle."},
    {"name": "Melting into n parts", "tex": r"r_{\text{small}}^3=\frac{R^3}{n}", "note": "Divide the cubed length, then cube-root."},
    {"name": "Radius scaling", "tex": r"V\to k^3V,\quad S\to k^2S", "note": "k = radius scale factor."},
]

sp_tricks = [
    {
        "title": "Total hemisphere = 3 circles",
        "body": "Curved shell 2 pi r squared plus flat face pi r squared equals 3 pi r squared. Never 2.",
        "example": {
            "q": "Find the total surface area of a solid hemisphere of radius 7 cm (take pi = 22/7).",
            "steps": [r"Total $=3\pi r^2$.", r"$=3\times\dfrac{22}{7}\times49$.", r"$=462$ sq cm."],
            "answer": "462 sq cm",
        },
    },
    {
        "title": "Cube-root the split",
        "body": "One sphere into 8 equal spheres: each cubed radius is one-eighth, so each radius is half.",
        "example": {
            "q": "A solid metal sphere of radius 6 cm is melted into 8 equal smaller spheres. The radius of each small sphere is:",
            "steps": [r"$r^3=\dfrac{6^3}{8}=\dfrac{216}{8}=27$.", r"$r=\sqrt[3]{27}$.", r"$r=3$ cm."],
            "answer": "3 cm",
        },
    },
    {
        "title": "Ratio: cube it or square it",
        "body": "Radii 3:4 mean volumes 27:64 and surfaces 9:16. Cancel pi, apply the right power.",
        "example": {
            "q": "The radii of two spheres are in the ratio 3 : 4. The ratio of their volumes is:",
            "steps": [r"Cube the ratio: $3^3:4^3$.", r"$27:64$."],
            "answer": "27 : 64",
        },
    },
]

sp_mistakes = [
    {"wrong": "Total hemisphere surface taken as $2\\pi r^2$.", "right": "That is the curved part only. Solid hemisphere total is $3\\pi r^2=462$ for $r=7$."},
    {"wrong": "Squaring instead of cubing for volume ratios.", "right": "Volume goes with $r^3$: radii $3:4$ give $27:64$."},
    {"wrong": "Forgetting $\\dfrac43$ when melting.", "right": "Sphere volume is $\\dfrac43\\pi r^3$; drop it and the sphere comes out too big."},
    {"wrong": "Dividing the radius by $n$ for $n$ small spheres.", "right": "Divide the cubed radius: $n=8$ halves the radius, not eighth-ing it."},
    {"wrong": "Doubling radius thought to double volume.", "right": "Volume scales by $2^3=8$; surface by $2^2=4$."},
]

sp_revision = [
    "Sphere: $V=\\dfrac43\\pi r^3$, $S=4\\pi r^2$.",
    "Hemisphere: volume $\\dfrac23\\pi r^3$, curved $2\\pi r^2$, total $3\\pi r^2$.",
    "$n$ equal pieces: divide $r^3$ by $n$, then cube-root.",
    "Overflow $=$ submerged volume; no new formula.",
    "Ratios: volumes cube, surfaces square; cancel $\\pi$ first.",
]

sp_patterns = [
    pat("m3d-sp-p1", "Surface area and volume of a sphere", "very common",
        "One radius given, surface or volume asked.",
        [r"Surface: $4\pi r^2$.", r"Volume: $\dfrac{4}{3}\pi r^3$.",
         r"Keep pi as $\dfrac{22}{7}$ for radius multiples of $7$."],
        "Two direct formulas; radius $7$ alone answers many papers since $4\times154=616$.",
        "Find the surface area of a sphere of radius 7 cm (take pi = 22/7).",
        [r"$S=4\times\dfrac{22}{7}\times49$.", r"$S=616$ sq cm."],
        "616 sq cm"),
    pat("m3d-sp-p2", "Hemisphere: curved vs total vs volume", "very common",
        "A solid or hollow hemisphere; a surface or volume asked.",
        [r"Curved surface: $2\pi r^2$.", r"Solid total: $3\pi r^2$.",
         r"Volume: $\dfrac23\pi r^3$."],
        "The only trap is which surface: curved for hollow, total (plus flat face) for solid.",
        "Find the total surface area of a solid hemisphere of radius 7 cm (take pi = 22/7).",
        [r"Total $=3\pi r^2$.", r"$=3\times154=462$ sq cm."],
        "462 sq cm"),
    pat("m3d-sp-p3", "Recasting and water displacement", "common",
        "A sphere melted into smaller ones, or dropped into water.",
        [r"Write the big sphere's volume.", r"Divide by the count for equal pieces.",
         r"Overflow equals the submerged volume."],
        "Both stories reduce to comparing volumes; the pi cancels on the way.",
        "A solid metal sphere of radius 6 cm is melted into 8 equal smaller spheres. The radius of each small sphere is:",
        [r"$r^3=\dfrac{216}{8}=27$.", r"$r=3$ cm."],
        "3 cm"),
    pat("m3d-sp-p4", "Radius-scaling multipliers", "common",
        "The radius scaled; new volume or surface asked.",
        [r"Read the scale factor $k$.", r"Volume: multiply by $k^3$.",
         r"Surface: multiply by $k^2$."],
        "The formulas' exponents convert any scale factor directly, no recomputation.",
        "If the radius of a sphere is doubled, its volume becomes:",
        [r"$k=2$.", r"Volume $\times 2^3=8$ times."],
        "8 times"),
    pat("m3d-sp-p5", "Two spheres: ratio questions", "common",
        "Radii in a ratio; volume or surface ratio asked.",
        [r"Cancel $\pi$ and constants.", r"Volumes: cube the radius ratio.",
         r"Surfaces: square it."],
        "With pi cancelled, a ratio question is a pure power of the given ratio.",
        "The radii of two spheres are in the ratio 3 : 4. The ratio of their surface areas is:",
        [r"Square the ratio: $3^2:4^2$.", r"$9:16$."],
        "9 : 16"),
]

# ---------------- m3d-prism-pyramid ----------------
pp_concept = (
    "A prism's volume is base area times height; a pyramid's is one third of that. "
    "Frustums interpolate between two circular ends. "
    "Cutting and melting questions conserve volume, and painted or cut cubes follow counting formulas."
)

pp_notes = r"""### Prism: base times length
$$V=\text{base area}\times\text{length}$$
A triangular prism with cross-section $20$ sq cm and length $12$ cm holds $240$ cu cm. A rectangular base $7\times5$ with length $10$ holds $350$ cu cm.

The base can be a triangle, square, hexagon, anything regular. Find its area first, multiply by the length second. A cuboid is just a prism with a rectangle base, so the tank formula lives here too.

> **Rule:** The prism formula needs exactly two things: the base area and the prism length. Everything else is decoration.

### Pyramid: a third of the prism
$$V=\frac{1}{3}\times\text{base area}\times\text{height}$$
Square base $10$, height $12$: $V=\dfrac13\times100\times12=400$ cu cm. Rectangular base $9\times4$ with height $7$: $V=\dfrac13\times36\times7=84$ cu cm.

Same base, same height: the pyramid always holds one-third of the prism's volume. The cone's one-third is the same idea on a circular base.

When a face slant of $13$ sits on a base of side $10$, the half-base is $5$, so the true height is $\sqrt{169-25}=12$. Slant first, height second.

> **Tip:** The pyramid height is the perpendicular drop to the base centre, never the slant edge.

### Frustum: the bucket shape
A cone with its top sliced off. With radii $R$ (bottom) and $r$ (top), height $h$:
$$V=\frac{\pi h}{3}\left(R^2+r^2+Rr\right)$$
Radii $5$ and $3$, height $6$: $\dfrac{22}{7}\times\dfrac{6}{3}\times(25+9+15)=\dfrac{44}{7}\times49=308$ cu cm.

A frustum is a big cone minus the small cone sliced off, and similar triangles link the two radii. Slant height $\sqrt{h^2+(R-r)^2}$: with radii $8$ and $3$ and height $12$ it is $\sqrt{144+25}=13$, the $5$-$12$-$13$ triplet again.

> **Watch:** The cross term $Rr$ is the one students drop. Three terms, always: $R^2$, $r^2$, $Rr$.

### Melting cubes
Three cubes of edges $3$, $4$, $5$ melt into one cube. Volume adds: $27+64+125=216=6^3$, so the new edge is $6$ cm.

Melting adds volumes, then one cube root. The cube table turns this into arithmetic. Splitting runs the other way: one cube of edge $12$ gives $8$ cubes of edge $6$, since $\dfrac{1728}{8}=216=6^3$.

### Lateral surfaces
- Prism: perimeter of base $\times$ length.
- Pyramid: $\dfrac12\times$ perimeter of base $\times$ slant height.

Square pyramid, base $10$, slant $13$: $\dfrac12\times40\times13=260$ sq cm. The slant height belongs to each triangular face.

Triangular prism with base sides $6$, $8$, $10$ and length $12$: perimeter $24$, so lateral $=24\times12=288$ sq cm. The base is a right triangle by the $6$-$8$-$10$ test.

> **Remember:** Prism lateral uses the length; pyramid lateral uses the slant height. Check which one the question gives.
"""

pp_formulas = [
    {"name": "Prism", "tex": r"V=\text{base area}\times\text{length}", "note": "Base can be any polygon."},
    {"name": "Pyramid", "tex": r"V=\frac{1}{3}\times\text{base area}\times h", "note": "h = perpendicular height."},
    {"name": "Frustum", "tex": r"V=\frac{\pi h}{3}(R^2+r^2+Rr)", "note": "R, r = the two end radii."},
    {"name": "Lateral surfaces", "tex": r"\text{prism}=P\times L,\quad \text{pyramid}=\frac12 P\times\ell", "note": "P = base perimeter; L = length; slant for pyramid."},
]

pp_tricks = [
    {
        "title": "One-third rule of thumb",
        "body": "Same base and height: pyramid = one third of the prism. Use it to sanity-check any answer.",
        "example": {
            "q": "A pyramid stands on a square base of side 10 cm and is 12 cm high. Its volume is:",
            "steps": [r"Prism would be $100\times12=1200$.", r"Pyramid $=\dfrac{1200}{3}$.", r"$=400$ cu cm."],
            "answer": "400 cu cm",
        },
    },
    {
        "title": "Add volumes, then root",
        "body": "Melting several solids: add the volumes, then take the cube root for a cube's edge.",
        "example": {
            "q": "Three metal cubes of edges 3 cm, 4 cm and 5 cm are melted into a single cube. Its edge is:",
            "steps": [r"$27+64+125=216$.", r"$216=6^3$.", r"Edge $=6$ cm."],
            "answer": "6 cm",
        },
    },
    {
        "title": "Frustum: three terms",
        "body": "R squared, r squared, Rr. Radii 5 and 3 give 25 + 9 + 15 = 49, and the numbers turn friendly.",
        "example": {
            "q": "A bucket is in the shape of a frustum with radii 5 cm and 3 cm and height 6 cm. Its volume is (take pi = 22/7):",
            "steps": [r"$R^2+r^2+Rr=25+9+15=49$.", r"$V=\dfrac{22}{7}\times\dfrac{6}{3}\times49$.", r"$V=308$ cu cm."],
            "answer": "308 cu cm",
        },
    },
]

pp_mistakes = [
    {"wrong": "Using the full prism volume for a pyramid.", "right": "The pyramid takes one-third: $\\dfrac13\\times100\\times12=400$, not 1200."},
    {"wrong": "Dropping the $Rr$ term in a frustum.", "right": "Radii $5$ and $3$ need $25+9+15=49$; without $Rr$ it is only 34."},
    {"wrong": "Using the slant edge as the pyramid height.", "right": "Volume needs the perpendicular height; slant heights serve the lateral surface."},
    {"wrong": "Adding the cube edges when melting.", "right": "Add volumes: $27+64+125=216$, edge $6$. Not $3+4+5=12$."},
    {"wrong": "Prism lateral with the slant height.", "right": "Prisms have no slant; lateral $=$ perimeter $\\times$ length."},
]

pp_revision = [
    "Prism: base area $\\times$ length.",
    "Pyramid: one-third of the same-base prism volume.",
    "Frustum: $\\dfrac{\\pi h}{3}(R^2+r^2+Rr)$; keep all three terms.",
    "Melting: add volumes, then take the cube root for an edge.",
    "Lateral: prism $P\\times L$; pyramid $\\dfrac12 P\\ell$ with the slant.",
]

pp_patterns = [
    pat("m3d-pp-p1", "Volume of a prism", "common",
        "A prism with its cross-section described.",
        [r"Identify the base shape.", r"Compute the base area.",
         r"Multiply by the prism length."],
        "One product of two quantities, whatever polygon the base is.",
        "A triangular prism has a cross-section area of 20 sq cm and length 12 cm. Its volume is:",
        [r"$V=20\times12$.", r"$V=240$ cu cm."],
        "240 cu cm"),
    pat("m3d-pp-p2", "Volume of a pyramid", "common",
        "A pyramid with a known base and height.",
        [r"Find the base area.", r"Multiply by the height.",
         r"Take one-third."],
        "The one-third factor is the only step beyond a prism volume.",
        "A pyramid stands on a square base of side 10 cm and is 12 cm high. Its volume is:",
        [r"$\dfrac13\times100\times12$.", r"$V=400$ cu cm."],
        "400 cu cm"),
    pat("m3d-pp-p3", "Frustum of a cone (bucket)", "occasional",
        "A bucket or lampshade with two radii and a height.",
        [r"Label the radii $R$ and $r$.", r"Compute $R^2+r^2+Rr$.",
         r"$V=\dfrac{\pi h}{3}$ times that sum."],
        "The three-term bracket is the entire formula; heights and radii are given directly.",
        "A bucket is in the shape of a frustum with radii 5 cm and 3 cm and height 6 cm. Its volume is (take pi = 22/7):",
        [r"$25+9+15=49$.", r"$V=\dfrac{22}{7}\times2\times49=308$ cu cm."],
        "308 cu cm"),
    pat("m3d-pp-p4", "Cube cutting and melting", "very common",
        "Several solids melted into one, or one cube cut into many.",
        [r"Add all volumes (or divide for pieces).", r"Equate to the target solid's volume formula.",
         r"Solve for the length asked."],
        "Volume conservation turns multi-solid stories into one equation.",
        "Three metal cubes of edges 3 cm, 4 cm and 5 cm are melted into a single cube. Its edge is:",
        [r"$27+64+125=216$.", r"$216=6^3$.", r"Edge $=6$ cm."],
        "6 cm"),
    pat("m3d-pp-p5", "Lateral surface of prism or pyramid", "occasional",
        "A side surface asked, with perimeter and slant data.",
        [r"Prism: perimeter $\times$ length.", r"Pyramid: $\dfrac12\times$ perimeter $\times$ slant.",
         r"Add base areas only if total surface is asked."],
        "Lateral formulas avoid computing each face separately.",
        "A square pyramid has a base of side 10 cm and slant height 13 cm. Its lateral surface area is:",
        [r"$P=4\times10=40$.", r"$\dfrac12\times40\times13=260$ sq cm."],
        "260 sq cm"),
]

# ---------------- patch ----------------
data = json.loads(TOPIC.read_text(encoding="utf-8"))

blocks = {
    "m3d-cube-cuboid": (cb_concept, cb_notes, cb_formulas, cb_tricks, cb_mistakes, cb_revision, cb_patterns),
    "m3d-cylinder": (cy_concept, cy_notes, cy_formulas, cy_tricks, cy_mistakes, cy_revision, cy_patterns),
    "m3d-cone": (co_concept, co_notes, co_formulas, co_tricks, co_mistakes, co_revision, co_patterns),
    "m3d-sphere": (sp_concept, sp_notes, sp_formulas, sp_tricks, sp_mistakes, sp_revision, sp_patterns),
    "m3d-prism-pyramid": (pp_concept, pp_notes, pp_formulas, pp_tricks, pp_mistakes, pp_revision, pp_patterns),
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
print("mensuration-3d.json patched")
