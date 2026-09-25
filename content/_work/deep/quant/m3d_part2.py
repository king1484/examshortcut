"""Phase-2 deep content for quant/mensuration-3d — sphere, prism-pyramid."""
from fractions import Fraction as F

from _lib import Sub

PI = F(22, 7)


# ---------------- m3d-sphere ----------------

def build_sphere():
    S = Sub("m3d-sphere")

    S.notes = r"""### The sphere family
For a sphere of radius $r$:
$$V = \frac{4}{3}\pi r^3,\qquad \text{SA} = 4\pi r^2$$
For a hemisphere of the same radius: curved surface $= 2\pi r^2$ (half the sphere's), flat face $= \pi r^2$, and total $= 3\pi r^2$ — the famous "3" that examiners love. Volume of a hemisphere $= \frac{2}{3}\pi r^3$.
The radius is the only input: every question is "get $r$, then apply one formula". Given a diameter? Halve it first. Given the surface area? $r = \sqrt{\text{SA}/4\pi}$. Given the volume? $r = \sqrt[3]{\frac{3V}{4\pi}}$.

### Melting, scaling and submersion
- **Melting** preserves volume: a big sphere recast into $n$ small equal spheres gives $r_{\text{small}} = \frac{r}{\sqrt[3]{n}}$ — for $n = 8$ the radius halves, for $n = 27$ it divides by 3.
- **Scaling**: radius $\times k$ → surface $\times k^2$, volume $\times k^3$. "Radius doubled" means SA $\times 4$ and $V \times 8$; "radius halved" gives $\frac14$ and $\frac18$.
- **Submersion**: a solid dropped into a (partly filled) cylinder of base radius $R$ raises the water level by $h = \frac{V_{\text{solid}}}{\pi R^2}$ — the displaced volume spreads over the base.

### Same-base relations
Sphere vs cylinder of radius $r$, height $2r$ (the sphere fits exactly inside): both have volume $\frac{4}{3}\pi r^3$. Sphere vs hemisphere: hemisphere is half the volume, $\frac34$ of the total surface ($3\pi r^2$ vs $4\pi r^2$).

### The 22/7 number family
- $r = 7$: SA $= 616$, $V = \frac{4}{3} \times \frac{22}{7} \times 343 = 4312/3$ — exams avoid it; they use $r = 21$: $r^3 = 9261$, $V = 4 \times 22 \times 441 = 38808$, SA $= 4 \times \frac{22}{7} \times 441 = 5544$.
- Hemisphere at $r = 7$: CSA $308$, TSA $462$; at $r = 21$: CSA $2772$, TSA $4158$.
- The displacement pair worth memorising: a sphere of radius 3 displaces $36\pi$; a cylinder of radius 4 therefore rises $\frac{36}{16} = 2.25$ cm.

### Scaling in percent form
Radius $+10\%$: SA $+21\%$, $V$ $+33.1\%$ (from $1.1^2$ and $1.1^3$). Radius $-50\%$: SA $\frac14$, $V$ $\frac18$ — volume swings harder than area in both directions. Percent-change questions in this subtopic are always these two exponent rules; if you find yourself expanding $\frac{4}{3}\pi$, stop and write $k^2$ or $k^3$ instead.

### Quick revision
- $V = \frac43\pi r^3$; SA $= 4\pi r^2$; hemisphere: CSA $2\pi r^2$, TSA $3\pi r^2$, $V = \frac23\pi r^3$.
- Radius $\times k$: SA $\times k^2$, $V \times k^3$.
- Melt into $n$ equal spheres: radius $\div \sqrt[3]{n}$.
- Water rise: $h = \frac{V_{\text{solid}}}{\pi R^2}$ of the container.
"""

    S.pattern("m3d-sp-p1", "Surface area / volume of a sphere", "very common",
      "Radius (or diameter) given; SA or volume asked — or one of them given and $r$ asked.",
      r"SA = 4\pi r^2,\qquad V = \frac{4}{3}\pi r^3",
      r"""1. Halve diameters first; then $r$ drives both formulas.
2. With $\pi = 22/7$, the 7-cube of $r = 21$ gives the classic $V = 38808$.
3. Reverse: $r = \sqrt{\text{SA}/4\pi}$ or $r = \sqrt[3]{3V/4\pi}$.

Why: the sphere has a single parameter, so forward and reverse questions differ only by which side you solve for.""",
      "Find the surface area of a sphere of radius 7 cm (take pi = 22/7).",
      r"SA $= 4 \times \frac{22}{7} \times 49 = 616$ sq cm.")
    S.pattern("m3d-sp-p2", "Hemisphere: curved vs total vs volume", "very common",
      "A hemisphere (dome, bowl) — the curved surface, total surface, or volume asked; the TSA = 3*pi*r^2 fact is the trap-setter.",
      r"\text{CSA} = 2\pi r^2,\quad \text{TSA} = 3\pi r^2,\quad V = \frac{2}{3}\pi r^3",
      r"""1. Dome/tent/scoop of a sphere → hemisphere.
2. Painted outside only → CSA $2\pi r^2$; a solid hemisphere's whole surface → TSA $3\pi r^2$; capacity → $\frac23\pi r^3$.
3. Keep the three straight; the difference is exactly one $\pi r^2$.

Why: half a sphere's skin plus one circular lid — the arithmetic is deliberately easy once the pieces are named.""",
      "Find the total surface area of a solid hemisphere of radius 7 cm (take pi = 22/7).",
      r"TSA $= 3 \times \frac{22}{7} \times 49 = 462$ sq cm.")
    S.pattern("m3d-sp-p3", "Recasting and water displacement", "common",
      "A sphere melted into smaller spheres — or dropped into a cylindrical vessel, where the water rise is asked.",
      r"V_{\text{total}} = n\,V_{\text{small}};\quad h_{\text{rise}} = \frac{V_{\text{sphere}}}{\pi R^2}",
      r"""1. Melting: equate volumes; for $n$ equal spheres divide the radius by $\sqrt[3]{n}$.
2. Displacement: the rise times the container's base area equals the sphere's volume.
3. Watch which radius is which — the sphere's $r$ vs the vessel's $R$.

Why: displaced water is just the volume wearing a different shape; recasting is the same statement in metal.""",
      "A solid metal sphere of radius 6 cm is melted into 8 equal smaller spheres. The radius of each small sphere is:",
      r"$\frac{4}{3}\pi 6^3 = 8 \cdot \frac43 \pi r^3 \Rightarrow r^3 = 27 \Rightarrow r = 3$ cm.")
    S.pattern("m3d-sp-p4", "Radius-scaling multipliers", "common",
      "'Radius doubled/halved/increased 50%' — how do surface area and volume change?",
      r"\text{SA} \times k^2,\qquad V \times k^3",
      r"""1. Write the multiplier: $r \to kr$.
2. SA scales $k^2$; volume scales $k^3$ — never the same number.
3. Percent form: radius $+50\%$ → $k = 1.5$ → SA $\times 2.25$, $V \times 3.375$.

Why: area is a product of two lengths, volume of three — the exponents do all the work.""",
      "If the radius of a sphere is doubled, its volume becomes:",
      r"$k^3 = 8$ times the original volume.")

    # ---- practice ----
    assert 4 * F(22, 7) * 49 == 616
    S.q("m3d-sp-p1", "easy", "The surface area of a sphere of radius $7$ cm is (take $\\pi = 22/7$):",
        ["$616$ sq cm", "$308$ sq cm", "$462$ sq cm", "$154$ sq cm"], "$616$ sq cm",
        r"""SA $= 4\pi r^2 = 4 \times \frac{22}{7} \times 49 = 616$ sq cm.""",
        r"$4 \times 22 \times 7 = 616$. Trap: $308$ (half — the hemisphere CSA) or $462$ (hemisphere TSA).", 25)
    assert F(4, 3) * 9261 * F(22, 7) == 38808
    S.q("m3d-sp-p1", "medium", "The volume of a sphere of radius $21$ cm is (take $\\pi = 22/7$):",
        ["$38,808$ cu cm", "$19,404$ cu cm", "$29,106$ cu cm", "$12,936$ cu cm"], "$38,808$ cu cm",
        r"""$V = \frac43 \pi r^3 = \frac43 \times \frac{22}{7} \times 9261 = 4 \times 22 \times 441 = 38{,}808$ cu cm.""",
        r"$\frac43 \times 9261 = 12348$; $\frac{12348}{7} \times 22 = 38{,}808$. Trap: $19{,}404$ (the hemisphere).", 45)
    assert 2 * F(22, 7) * 49 == 308
    S.q("m3d-sp-p2", "medium", "The curved surface area of a hemisphere of radius $7$ cm is (take $\\pi = 22/7$):",
        ["$308$ sq cm", "$462$ sq cm", "$616$ sq cm", "$154$ sq cm"], "$308$ sq cm",
        r"""CSA $= 2\pi r^2 = 2 \times \frac{22}{7} \times 49 = 308$ sq cm.""",
        r"Half the sphere: $308$. Trap: $462$ — that adds the flat circular face.", 35)
    assert 3 * F(22, 7) * 49 == 462
    S.q("m3d-sp-p2", "medium", "The total surface area of a solid hemisphere of radius $7$ cm is (take $\\pi = 22/7$):",
        ["$462$ sq cm", "$308$ sq cm", "$616$ sq cm", "$770$ sq cm"], "$462$ sq cm",
        r"""TSA $= 3\pi r^2 = 3 \times \frac{22}{7} \times 49 = 462$ sq cm.""",
        r"Curved $308$ + flat face $154$ = $462$. Trap: $308$ (forgetting the lid) or $770$ (wrong $4\pi r^2 + \pi r^2$).", 35)
    assert F(4, 3) * 216 == 288 and 8 * F(4, 3) * 27 == 288
    S.q("m3d-sp-p3", "medium", "A solid metal sphere of radius $6$ cm is melted and drawn into $8$ equal small spheres. The radius of each small sphere is:",
        ["$3$ cm", "$2$ cm", "$1.5$ cm", "$4$ cm"], "$3$ cm",
        r"""$8 = 2^3$ equal spheres → each length divides by $\sqrt[3]{8} = 2$.

Radius $= \frac{6}{2} = 3$ cm.""",
        r"$r = 6/\sqrt[3]{8} = 3$ cm. Trap: $2$ cm (dividing the radius by 3, the wrong root).", 40)
    assert F(4, 3) * 27 == 36 and 36 / 16 == F(9, 4)
    S.q("m3d-sp-p3", "hard", "A solid sphere of radius $3$ cm is dropped into a cylindrical vessel of base radius $4$ cm containing water. The height by which the water rises is (take $\\pi = 22/7$):",
        ["$2.25$ cm", "$1.5$ cm", "$3$ cm", "$0.75$ cm"], "$2.25$ cm",
        r"""Displaced volume $= \frac43 \pi (27) = 36\pi$.

Rise $= \frac{36\pi}{\pi (4)^2} = \frac{36}{16} = 2.25$ cm.""",
        r"$h = \frac{V}{\pi R^2} = \frac{36}{16} = 2.25$ cm. Trap: $3$ cm (confusing the sphere's radius with the rise).", 50)
    assert 4 * 4 == 16
    S.q("m3d-sp-p4", "easy", "If the radius of a sphere is doubled, its surface area becomes:",
        ["$4$ times", "$2$ times", "$8$ times", "$16$ times"], "$4$ times",
        r"""SA $\propto r^2$: $k = 2$ → $k^2 = 4$ times.""",
        r"$k^2 = 4$. Trap: $8$ times — that is the VOLUME's multiplier ($k^3$).", 25)
    assert F(27, 1) and 3 ** 3 == 27 and 4 ** 3 == 64
    S.q("m3d-sp-p4", "medium", "The radii of two spheres are in the ratio $3:4$. The ratio of their volumes is:",
        ["$27:64$", "$9:16$", "$3:4$", "$64:27$"], "$27:64$",
        r"""Volumes scale as the cube of the radius ratio: $3^3 : 4^3 = 27 : 64$.""",
        r"$27:64$ (cube the ratio). Trap: $9:16$ — that is the surface-area ratio.", 35)
    return S


# ---------------- m3d-prism-pyramid ----------------

def build_prism():
    S = Sub("m3d-prism-pyramid")

    S.notes = r"""### Prisms and pyramids: the one-third rule
A prism has a constant cross-section: $V = (\text{area of base}) \times (\text{length/height})$. A pyramid with the same base and apex over the centre holds exactly one-third: $V = \frac13 \times \text{base area} \times h$. This is the cone/cylinder relation in flat-base form — the fraction $\frac13$ is the whole topic.
$$V_{\text{prism}} = A_{\text{base}} \times h, \qquad V_{\text{pyramid}} = \frac{1}{3} A_{\text{base}} \times h$$

### Frustums (cut pyramids/cones)
Slice a cone or pyramid parallel to its base and remove the top: what remains is a frustum.
$$V = \frac{\pi h}{3}\left(R^2 + r^2 + Rr\right) \text{ (conical)}, \qquad V = \frac{h}{3}\left(A_1 + A_2 + \sqrt{A_1 A_2}\right) \text{ (any)}$$
with $R, r$ the two radii (or $A_1, A_2$ the two face areas) and $h$ the perpendicular height between them. Bucket and tumbler questions are frustums.

### Lateral surfaces
- Prism lateral area $=$ (perimeter of cross-section) $\times$ (length) — the tube unrolls flat.
- Pyramid lateral area $= \frac12 \times$ (perimeter of base) $\times$ (slant height) — sum of triangles.
The total adds the two base/cross-section ends.

### Cube cutting and melting
A cube of side $a$ cut into unit cubes yields $a^3$ of them. Melting several cubes into one: sum the volumes and take the cube root — edges $3, 4, 5$ combine into a cube of edge $\sqrt[3]{27+64+125} = 6$. Both facts are volume bookkeeping; nothing else changes on melting.

### Worked frustum
Bucket with $R = 5$, $r = 3$, $h = 6$: the bracket $R^2 + r^2 + Rr = 25 + 9 + 15 = 49$, and $\frac{\pi h}{3} = \frac{22}{7} \times 2$, so $V = \frac{22}{7} \times 2 \times 49 = 308$ cu cm. Exam frustums are built so the bracket is a perfect square times $\frac{22}{7}$-friendly numbers — if your bracket is ugly, recheck the radii (diameters halved?) and the terms ($Rr$ included?). For the cut-off top piece instead, either subtract the small cone from the big one or use the similarity ratio: cutting at half the height leaves $\frac18$ of the volume below-cut... rather, the removed top cone has $\frac18$ of the whole cone's volume, so the frustum is $\frac78$ of it.

### Cube numbers worth carrying
$a^3$: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728 — the melting answers live here ($216 \to 6$, $729 \to 9$, $1728 \to 12$). Two cubes of edge $a$ melted give $\sqrt[3]{2a^3} = a\sqrt[3]{2}$ — NOT $2a$; only cube-number sums recast into clean cubes, which is why exams pick $3^3 + 4^3 + 5^3 = 6^3$ (the only consecutive-cube identity).

### Quick revision
- Prism: $V = A \times h$; pyramid: $\frac13 A h$; lateral prism $= P \times h$, pyramid $= \frac12 P l$.
- Frustum (cone form): $\frac{\pi h}{3}(R^2 + r^2 + Rr)$.
- Cut cube of side $a$ into unit cubes: $a^3$ pieces.
- Melted cubes: $\sqrt[3]{\sum a_i^3}$.
"""

    S.pattern("m3d-pp-p1", "Volume of a prism", "common",
      "A prism/tank/beam with a stated cross-section area (or easy base) and a length — volume or capacity asked.",
      r"V = A_{\text{base}} \times \text{length}",
      r"""1. Identify the constant cross-section (triangular, rectangular, any).
2. Compute its area, then multiply by the length/height.
3. Capacity questions: $\text{m}^3 \times 1000$ = litres.

Why: a prism is a base 'swept' along a line — the volume is literally area times distance swept.""",
      "A triangular prism has a cross-section area of 20 sq cm and length 12 cm. Its volume is:",
      r"$V = 20 \times 12 = 240$ cu cm.")
    S.pattern("m3d-pp-p2", "Volume of a pyramid", "common",
      "A pyramid (square/rectangular base) with base side(s) and height given — volume asked, or compared with a prism.",
      r"V = \frac{1}{3} \times A_{\text{base}} \times h",
      r"""1. Base area from the sides; multiply by height.
2. Then take one-third — the step exams test by omitting.
3. Pyramid vs prism of the same base and height: volumes $1 : 3$.

Why: three pyramids fill the matching prism; the one-third is the definition being tested.""",
      "A pyramid stands on a square base of side 10 cm and is 12 cm high. Its volume is:",
      r"$V = \frac13 \times 100 \times 12 = 400$ cu cm.")
    S.pattern("m3d-pp-p3", "Frustum of a cone (bucket)", "occasional",
      "A bucket/tumbler shape — two radii (or diameters) and the height given; capacity asked.",
      r"V = \frac{\pi h}{3}\left(R^2 + r^2 + Rr\right)",
      r"""1. Halve diameters to get $R, r$; keep $h$ perpendicular (not slant).
2. Compute $R^2 + r^2 + Rr$; multiply by $\frac{\pi h}{3}$.
3. Litres conversion if the bucket capacity is asked.

Why: a frustum is the big cone minus the small cut-off cone; the three-term formula is its closed form.""",
      "A bucket is in the shape of a frustum with radii 5 cm and 3 cm and height 6 cm. Its volume is (take pi = 22/7):",
      r"$V = \frac{22 \times 6}{21}(25 + 9 + 15) = \frac{22}{7} \times 2 \times 49 = 308$ cu cm.")
    S.pattern("m3d-pp-p4", "Cube cutting and melting", "very common",
      "A cube cut into smaller equal cubes — or several cubes melted into one big cube; the count or the new edge asked.",
      r"N = \left(\frac{a}{s}\right)^3;\quad A = \sqrt[3]{\sum a_i^3}",
      r"""1. Cutting: the count is the cube of the side ratio; a cube of side $a$ cm gives $a^3$ unit cubes.
2. Melting: add the volumes, take the cube root — triplet sums like $27+64+125=216$ are favourites.
3. Surface-area questions after cutting: $6N s^2$, larger than the original block.

Why: volume is conserved on cutting/melting; only the shape of that volume is redistributed.""",
      "Three metal cubes of edges 3 cm, 4 cm and 5 cm are melted into a single cube. Its edge is:",
      r"$\sqrt[3]{27 + 64 + 125} = \sqrt[3]{216} = 6$ cm.")
    S.pattern("m3d-pp-p5", "Lateral surface of prism / pyramid", "occasional",
      "Perimeter of the cross-section (or base) plus a length/slant height — the lateral (side) area asked.",
      r"\text{prism}: P \times h;\qquad \text{pyramid}: \frac{1}{2} P l",
      r"""1. Prism: the side walls unroll into a rectangle $P \times h$.
2. Pyramid: the sides are triangles — half the base perimeter times the slant height.
3. Add the base area only if TOTAL surface is asked.

Why: both formulas are 'unroll the walls and measure the resulting flat shape'.""",
      "A square pyramid has a base of side 10 cm and slant height 13 cm. Its lateral surface area is:",
      r"LSA $= \frac12 \times 40 \times 13 = 260$ sq cm.")

    # ---- practice ----
    assert 20 * 12 == 240
    S.q("m3d-pp-p1", "medium", "A triangular prism has a cross-sectional area of $20$ sq cm and a length of $12$ cm. Its volume is:",
        ["$240$ cu cm", "$120$ cu cm", "$480$ cu cm", "$32$ cu cm"], "$240$ cu cm",
        r"""$V = A_{\text{base}} \times \text{length} = 20 \times 12 = 240$ cu cm.""",
        r"Area x length. Trap: $120$ (a stray half — prisms carry no $\frac13$ or $\frac12$ factor).", 30)
    assert 5 * 4 * 3 == 60 and 60 * 1000 == 60000
    S.q("m3d-pp-p1", "easy", "A rectangular tank measures $5$ m $\\times$ $4$ m $\\times$ $3$ m. Its capacity in litres is:",
        ["$60,000$ litres", "$6,000$ litres", "$600$ litres", "$60$ litres"], "$60,000$ litres",
        r"""$V = 5 \times 4 \times 3 = 60\ \text{m}^3 = 60 \times 1000 = 60{,}000$ litres.""",
        r"$60\ \text{m}^3 \times 1000$ = $60{,}000$ L. Trap: $6{,}000$ (a slipped zero).", 30)
    assert F(1, 3) * 100 * 12 == 400
    S.q("m3d-pp-p2", "medium", "A pyramid stands on a square base of side $10$ cm and has a height of $12$ cm. Its volume is:",
        ["$400$ cu cm", "$1200$ cu cm", "$300$ cu cm", "$240$ cu cm"], "$400$ cu cm",
        r"""$V = \frac13 \times (10)^2 \times 12 = \frac13 \times 1200 = 400$ cu cm.""",
        r"One-third of $1200 = 400$. Trap: $1200$ — the containing prism's volume.", 35)
    assert F(1, 3) * 108 * 10 == 360
    S.q("m3d-pp-p2", "medium", "A pyramid has a rectangular base $12$ cm $\\times$ $9$ cm and a height of $10$ cm. Its volume is:",
        ["$360$ cu cm", "$1080$ cu cm", "$330$ cu cm", "$120$ cu cm"], "$360$ cu cm",
        r"""Base $= 12 \times 9 = 108$; $V = \frac13 \times 108 \times 10 = 360$ cu cm.""",
        r"$\frac13 \times 1080 = 360$. Trap: $1080$ (no third) — one step, one mark.", 35)
    assert F(22, 7) * 2 * 49 == 308
    S.q("m3d-pp-p3", "hard", "A bucket is shaped like a frustum of a cone with end radii $5$ cm and $3$ cm and depth $6$ cm. Its capacity is (take $\\pi = 22/7$):",
        ["$308$ cu cm", "$616$ cu cm", "$264$ cu cm", "$330$ cu cm"], "$308$ cu cm",
        r"""$R^2 + r^2 + Rr = 25 + 9 + 15 = 49$.

$V = \frac{\pi h}{3} \times 49 = \frac{22}{7} \times 2 \times 49 = 308$ cu cm.""",
        r"$\frac{6}{3} = 2$; $2 \times \frac{22}{7} \times 49 = 308$. Trap: $264$ — the missing $Rr = 15$ term.", 55)
    assert F(1, 3) * 21 * F(22, 7) * 28 == 616
    S.q("m3d-pp-p3", "medium", "A tumbler is a frustum of a cone with radii $4$ cm and $2$ cm and height $21$ cm. Its volume is (take $\\pi = 22/7$):",
        ["$616$ cu cm", "$308$ cu cm", "$462$ cu cm", "$770$ cu cm"], "$616$ cu cm",
        r"""$16 + 4 + 8 = 28$; $V = \frac13 \times 21 \times \frac{22}{7} \times 28 = 7 \times \frac{22}{7} \times 28 = 616$ cu cm.""",
        r"$\frac{21}{3} = 7$; $22 \times 28 = 616$. Trap: $440$ (dropping the $Rr = 8$ term).", 50)
    assert 4 ** 3 == 64
    S.q("m3d-pp-p4", "easy", "A wooden cube of side $4$ cm is cut into unit cubes (edge $1$ cm). How many small cubes are formed?",
        ["$64$", "$16$", "$48$", "$32$"], "$64$",
        r"""$\left(\frac{4}{1}\right)^3 = 64$ unit cubes.""",
        r"$4^3 = 64$. Trap: $16$ — that is one FACE of small cubes ($4^2$).", 25)
    assert 27 + 64 + 125 == 216 and 6 ** 3 == 216
    S.q("m3d-pp-p4", "medium", "Three metallic cubes of edges $3$ cm, $4$ cm and $5$ cm are melted and recast into a single cube. The edge of the new cube is:",
        ["$6$ cm", "$12$ cm", "$4$ cm", "$8$ cm"], "$6$ cm",
        r"""Total volume $= 27 + 64 + 125 = 216 = 6^3$; edge $= 6$ cm.""",
        r"$\sqrt[3]{216} = 6$ cm. Trap: $12$ cm (the SUM of edges instead of the cube root of the volume sum).", 40)
    assert 12 * 10 == 120
    S.q("m3d-pp-p5", "easy", "A triangular prism has a perimeter of $12$ cm for its cross-section and a length of $10$ cm. Its lateral surface area is:",
        ["$120$ sq cm", "$60$ sq cm", "$240$ sq cm", "$100$ sq cm"], "$120$ sq cm",
        r"""LSA $= P \times h = 12 \times 10 = 120$ sq cm.""",
        r"The tube unrolls to $12 \times 10$. Trap: $60$ (a spurious half).", 25)
    assert F(1, 2) * 40 * 13 == 260
    S.q("m3d-pp-p5", "medium", "A square pyramid has a base edge of $10$ cm and a slant height of $13$ cm. Its lateral surface area is:",
        ["$260$ sq cm", "$520$ sq cm", "$100$ sq cm", "$250$ sq cm"], "$260$ sq cm",
        r"""Perimeter $= 40$; LSA $= \frac12 P l = \frac12 \times 40 \times 13 = 260$ sq cm.""",
        r"$\frac12 \times 40 \times 13 = 260$. Trap: $520$ (forgot the half) — four triangles, halved each.", 35)
    return S
