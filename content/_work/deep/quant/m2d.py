"""Phase-2 deep content build for quant/mensuration-2d. Run: py -3 m2d.py"""
from _lib import apply_topic
import m2d_part1
import m2d_part2


def P(pattern, frequency, howToSpot, approach, subtopic, ex_q, ex_sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot,
            "approach": approach, "subtopic": subtopic,
            "example": {"q": ex_q, "solution": ex_sol}}


PYQ = [
    P("Triangle area: base-height, equilateral, right-triangle", "very common",
      "A triangle with base and height given, or 'equilateral triangle of side a', or three sides that form a Pythagorean family.",
      r"General: $K = \frac{1}{2}bh$. Equilateral: $\frac{\sqrt{3}}{4}a^2$, height $\frac{\sqrt{3}}{2}a$. Triplet sides → right triangle → $\frac{1}{2} \times$ legs, skipping Heron.",
      "m2d-triangles",
      r"Find the area of an equilateral triangle of side $12$ cm.",
      r"$K = \frac{\sqrt{3}}{4} \times 144 = 36\sqrt{3}$ sq cm."),
    P("Heron's formula for three sides", "very common",
      "Three side lengths given with no height mentioned; the numbers are not an obvious triplet.",
      r"Compute $s = \frac{a+b+c}{2}$, then $K = \sqrt{s(s-a)(s-b)(s-c)}$. Check (13,14,15) → 84 and triplet families first.",
      "m2d-triangles",
      r"Find the area of the triangle with sides $13$, $14$, $15$ cm.",
      r"$s = 21$; $K = \sqrt{21 \times 8 \times 7 \times 6} = 84$ sq cm."),
    P("Isosceles triangle area via half-base", "common",
      "Equal sides and base given; the height is not stated but implied by the symmetry.",
      r"$h = \sqrt{a^2 - (b/2)^2}$, then $K = \frac{1}{2}bh$. The half-base triplets (5,12,13), (8,15,17) appear constantly.",
      "m2d-triangles",
      r"An isosceles triangle has equal sides $17$ cm and base $16$ cm. Find its area.",
      r"$h = \sqrt{17^2 - 8^2} = 15$; $K = \frac{1}{2} \times 16 \times 15 = 120$ sq cm."),
    P("Rectangle from two of {perimeter, diagonal, area}", "very common",
      "The perimeter and diagonal of a rectangle given (or area and diagonal) — the missing quantity asked.",
      r"$l + b = \frac{P}{2}$; match with the diagonal to a triplet (5-12-13 etc.). General: $K = \left(\frac{l+b}{2}\right)^2 - \left(\frac{d}{2}\right)^2$.",
      "m2d-quads",
      r"A rectangle has perimeter $34$ cm and diagonal $13$ cm. Find its area.",
      r"$l+b = 17$; 5-12-13 → area $60$ sq cm."),
    P("Rhombus: diagonals, area, perimeter chain", "very common",
      "Diagonals given (or area + one diagonal, or diagonals in a ratio) — side, perimeter or the other diagonal asked.",
      r"$K = \frac{1}{2}d_1d_2$; half-diagonals form a right triangle with the side — use half-size triplets. Ratio form: $d_1 = mk, d_2 = nk$ into the area.",
      "m2d-quads",
      r"The diagonals of a rhombus are $10$ cm and $24$ cm. Find its perimeter.",
      r"Halves $5, 12$ → side $13$ → perimeter $52$ cm."),
    P("Circle: area ↔ circumference forward and reverse", "very common",
      "Radius/diameter given for one of area/circumference — or circumference/area given and the other asked.",
      r"$C = 2\pi r$, $K = \pi r^2$ with $\pi = 22/7$. Reverse: $r = \frac{C}{2\pi}$ or $r = \sqrt{K/\pi}$. Halve diameters before anything else.",
      "m2d-circles",
      r"The circumference of a circle is $132$ cm. Find its area.",
      r"$r = \frac{132 \times 7}{44} = 21$; $K = \frac{22}{7} \times 441 = 1386$ sq cm."),
    P("Sector area and arc length", "very common",
      "A central angle and radius given; the sector's area or the arc's length asked (sometimes reversed).",
      r"Multiply the full circle's area (or circumference) by $\frac{\theta}{360}$; reduce the fraction first ($72^\circ \to \frac15$).",
      "m2d-circles",
      r"Find the area of a sector of angle $90^\circ$ in a circle of radius $14$ cm.",
      r"$\frac14 \times \frac{22}{7} \times 196 = 154$ sq cm."),
    P("Ring area and wheel revolutions", "common",
      "Two concentric circles forming a path/border — or a wheel of given diameter rolling a stated distance.",
      r"Ring: $\pi(R^2 - r^2) = \pi(R+r)(R-r)$. Wheel: one revolution = $\pi D$; revolutions $= \frac{\text{distance}}{\pi D}$ with units matched first.",
      "m2d-circles",
      r"A wheel of diameter $70$ cm rolls $231$ m. How many revolutions does it make?",
      r"$C = 2.2$ m; $\frac{231}{2.2} = 105$ revolutions."),
    P("Regular polygon: angles, diagonals, hexagon area", "very common",
      "An interior/exterior angle, angle sum or diagonal count given — or a regular hexagon with its side/diagonal.",
      r"Route through the exterior angle $\frac{360^\circ}{n}$. Diagonals $\frac{n(n-3)}{2}$ — reverse by factor pairs. Hexagon $= 6$ equilateral triangles: $K = \frac{3\sqrt3}{2}a^2$, long diagonal $2a$, short $a\sqrt3$.",
      "m2d-polygons",
      r"Each interior angle of a regular polygon is $150^\circ$. Find the number of sides.",
      r"ext $= 30^\circ$; $n = \frac{360}{30} = 12$."),
    P("Area scaling: side change, cost, map scale", "very common",
      "'Side increased by x%', painting/carpeting costs for a resized figure, map scale 1 : n with a map area given.",
      r"Areas scale as $k^2$; lengths as $k$. Side $+x\%$ → area $+\left(2x + \frac{x^2}{100}\right)\%$. Map $1:n$ → actual area $=$ map area $\times n^2$ (convert units).",
      "m2d-scaling",
      r"If each side of a square is increased by $20\%$, by what percent does the area increase?",
      r"$1.2^2 = 1.44$ → $44\%$."),
]

if __name__ == "__main__":
    subs = [
        m2d_part1.build_triangles(),
        m2d_part1.build_quads(),
        m2d_part1.build_circles(),
        m2d_part2.build_polygons(),
        m2d_part2.build_scaling(),
    ]
    apply_topic("mensuration-2d", subs, PYQ)
