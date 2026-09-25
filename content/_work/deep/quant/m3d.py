"""Phase-2 deep content build for quant/mensuration-3d. Run: py -3 m3d.py"""
from _lib import apply_topic
import m3d_part1
import m3d_part2


def P(pattern, frequency, howToSpot, approach, subtopic, ex_q, ex_sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot,
            "approach": approach, "subtopic": subtopic,
            "example": {"q": ex_q, "solution": ex_sol}}


PYQ = [
    P("Cuboid/cube: volume, total/lateral surface area", "very common",
      "Dimensions of a box given; volume, total surface, or the four walls of a room asked.",
      r"$V = lbh = a^3$; TSA $= 2(lb+bh+lh) = 6a^2$; four walls $= 2h(l+b)$. Read which measure the wording prices.",
      "m3d-cube-cuboid",
      r"Find the total surface area of a cuboid of dimensions $12 \times 10 \times 8$ cm.",
      r"TSA $= 2(120 + 80 + 96) = 592$ sq cm."),
    P("Cube diagonal and edge-sum", "common",
      "A cube's body/face diagonal or the total edge length asked; or volume/area given and the diagonal asked.",
      r"Body diagonal $a\sqrt3$, face diagonal $a\sqrt2$, edges $12a$. Reverse from $V$ or TSA to $a$ first.",
      "m3d-cube-cuboid",
      r"The total surface area of a cube is $294$ sq cm. Find its body diagonal.",
      r"$a = 7$; diagonal $= 7\sqrt3$ cm."),
    P("Tank/pit capacity in litres, digging cost", "very common",
      "A tank/pit/room's capacity asked in litres, or a cost at Rs x per cu m / per sq m.",
      r"$1\ \text{m}^3 = 1000$ L; volume for capacity/digging, area for painting. Convert BEFORE applying rates.",
      "m3d-cube-cuboid",
      r"A tank $1.5$ m $\times$ $1$ m $\times$ $0.8$ m holds how many litres?",
      r"$1.2\ \text{m}^3 = 1200$ litres."),
    P("Cylinder: volume / CSA / TSA", "very common",
      "Radius and height given (diameter must be halved); volume, curved or total surface asked.",
      r"$V = \pi r^2 h$, CSA $= 2\pi rh$, TSA $= 2\pi r(h+r)$ with $\pi = 22/7$. Capacity → $V$, label → CSA, closed drum → TSA.",
      "m3d-cylinder",
      r"Find the volume of a cylinder of radius $7$ cm and height $10$ cm.",
      r"$V = \frac{22}{7} \times 49 \times 10 = 1540$ cu cm."),
    P("Cylinder: reverse dimension or multiplier change", "common",
      "Volume/CSA given with a dimension asked — or 'radius doubled, height halved' style volume changes.",
      r"$h = \frac{V}{\pi r^2}$, $r = \frac{\text{CSA}}{2\pi h}$; multipliers: $r \times k$ contributes $k^2$, $h \times m$ contributes $m$.",
      "m3d-cylinder",
      r"The radius of a cylinder is doubled and its height halved. Its volume becomes:",
      r"$4 \times \frac12 = 2$ times."),
    P("Hollow pipe, well capacity, water flow", "common",
      "A pipe with outer/inner radii (metal volume), a well (litres), or water flowing through a pipe.",
      r"Pipe metal $= \pi(R^2 - r^2)L$; flow per second $= \pi r^2 \times$ speed; well litres $= 1000 \times \text{m}^3$.",
      "m3d-cylinder",
      r"An iron pipe of length $14$ cm has outer radius $5$ cm and inner radius $3$ cm. Find the volume of iron.",
      r"$\frac{22}{7} \times 16 \times 14 = 704$ cu cm."),
    P("Cone: slant triplet with CSA/TSA/volume", "very common",
      "Radius and height given; curved/total surface or volume asked — the $(r, h, l)$ triplet makes $l$ instant.",
      r"$l = \sqrt{r^2+h^2}$ (7-24-25 family), CSA $= \pi r l$, TSA $= \pi r(l+r)$, $V = \frac13\pi r^2 h$.",
      "m3d-cone",
      r"A cone has $r = 7$ cm and $h = 24$ cm. Find its CSA and TSA.",
      r"$l = 25$: CSA $= 550$, TSA $= 550 + 154 = 704$ sq cm."),
    P("Recasting: cone/sphere/cylinder into each other", "very common",
      "'Melted and recast' — a solid's material reshaped; the target dimension asked.",
      r"Equate volumes. Cone→sphere: $R^3 = \frac{r^2 h}{4}$. Into $n$ similar solids: lengths divide by $\sqrt[3]{n}$.",
      "m3d-cone",
      r"A metallic cone of radius $6$ cm and height $24$ cm is melted into a sphere. Find the sphere's radius.",
      r"$R^3 = \frac{36 \times 24}{4} = 216 \Rightarrow R = 6$ cm."),
    P("Sphere/hemisphere: surface and volume", "very common",
      "A sphere or hemisphere (dome/bowl) with radius given or implied; SA, TSA, or volume asked.",
      r"$SA = 4\pi r^2$, $V = \frac43 \pi r^3$; hemisphere CSA $2\pi r^2$, TSA $3\pi r^2$, $V \frac23 \pi r^3$. Radius $\times k$: SA $k^2$, V $k^3$.",
      "m3d-sphere",
      r"Find the volume of a sphere of radius $21$ cm (take $\pi = 22/7$).",
      r"$\frac43 \times \frac{22}{7} \times 9261 = 38808$ cu cm."),
    P("Prism, pyramid, frustum volumes", "common",
      "A constant cross-section solid (prism), a pointed solid (pyramid), or a bucket-shaped frustum with volumes asked.",
      r"Prism $V = A \times h$; pyramid $\frac13 A h$; frustum $\frac{\pi h}{3}(R^2 + r^2 + Rr)$. Cube melts: $\sqrt[3]{\sum a_i^3}$.",
      "m3d-prism-pyramid",
      r"A bucket is a frustum with radii $5$ cm, $3$ cm and height $6$ cm. Find its capacity.",
      r"$\frac{22}{7} \times 2 \times (25+9+15) = 308$ cu cm."),
]

if __name__ == "__main__":
    subs = [
        m3d_part1.build_cube(),
        m3d_part1.build_cylinder(),
        m3d_part1.build_cone(),
        m3d_part2.build_sphere(),
        m3d_part2.build_prism(),
    ]
    apply_topic("mensuration-3d", subs, PYQ)
