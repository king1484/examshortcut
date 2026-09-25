"""Phase-2 deep content build for quant/geometry. Run: py -3 geometry.py"""
from _lib import apply_topic
import geo_part1
import geo_part2


def P(pattern, frequency, howToSpot, approach, subtopic, ex_q, ex_sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot,
            "approach": approach, "subtopic": subtopic,
            "example": {"q": ex_q, "solution": ex_sol}}


PYQ = [
    P("Angles between parallel lines (expressions in x)", "very common",
      "Two angles formed by a transversal cutting parallel lines are given as (ax ± b) degrees; x or one of the angles is asked.",
      r"Classify the pair first: corresponding/alternate → equal; co-interior → sum $180^\circ$. That gives one linear equation in $x$. Solve, substitute back, and answer the angle actually asked (not $x$).",
      "geo-lines-angles",
      r"Two co-interior angles between parallel lines are $(5x-40)^\circ$ and $(3x+20)^\circ$. The smaller angle is:",
      r"$5x-40+3x+20=180 \Rightarrow 8x=200 \Rightarrow x=25$; the angles are $85^\circ$ and $95^\circ$, so the smaller is $85^\circ$."),
    P("Complement and supplement of an angle", "very common",
      "'The supplement is k times the complement', 'find the complement of x degrees', or the angle stated through its relation to its complement/supplement.",
      r"Write complement $= 90^\circ - x$ and supplement $= 180^\circ - x$, translate the sentence into one linear equation, solve for $x$. Instant check: supplement minus complement is always $90^\circ$.",
      "geo-lines-angles",
      r"The supplement of an angle is three times its complement. Find the angle.",
      r"$180-x = 3(90-x) \Rightarrow 180-x = 270-3x \Rightarrow 2x = 90 \Rightarrow x = 45^\circ$."),
    P("Angle at incentre / circumcentre / orthocentre", "very common",
      "The centre is named or defined (angle bisectors, perpendicular bisectors, altitudes) and ∠A is given — or the angle at the centre is given and ∠A asked.",
      r"Identify the centre, then apply: incentre $\angle BIC = 90^\circ + \frac{A}{2}$; circumcentre $\angle BOC = 2A$; orthocentre $\angle BHC = 180^\circ - A$. Invert the same formulas when the centre angle is given.",
      "geo-triangles",
      r"In $\triangle ABC$, $\angle A = 50^\circ$. If $O$ is the circumcentre, find $\angle BOC$.",
      r"$\angle BOC = 2\angle A = 2 \times 50^\circ = 100^\circ$."),
    P("Centroid divides the median 2 : 1", "common",
      "A median and the centroid G appear; AG, GD or AD is asked, sometimes through a sum or difference condition.",
      r"On median $AD$: $AG = \frac{2}{3}AD$, $GD = \frac{1}{3}AD$, and $AG - GD = \frac{1}{3}AD$. Set the smaller piece as $k$ when a condition is given.",
      "geo-triangles",
      r"The median $AD$ of a triangle is $15$ cm and $G$ is the centroid. Find $AG$.",
      r"$AG = \frac{2}{3} \times 15 = 10$ cm (and $GD = 5$ cm)."),
    P("Similar triangles: perimeter ratio vs area ratio", "very common",
      "Perimeters (or a pair of corresponding sides/altitudes) of two similar triangles are given and an area is asked — or areas are given and a perimeter asked.",
      r"Perimeter/side ratio is linear ($k$); areas scale as $k^2$. Going from areas back to lengths needs the square root. Then scale the known quantity.",
      "geo-similarity",
      r"The areas of two similar triangles are $25$ and $81$ sq cm; the smaller perimeter is $40$ cm. Find the larger perimeter.",
      r"Side ratio $= \sqrt{\frac{81}{25}} = \frac{9}{5}$; larger perimeter $= 40 \times \frac{9}{5} = 72$ cm."),
    P("Parallel line inside a triangle (BPT / midpoint theorem)", "common",
      "DE parallel to BC is stated inside a triangle — or D, E are described as midpoints — and a segment length is asked.",
      r"BPT: $\frac{AD}{DB} = \frac{AE}{EC}$. Midpoint theorem: $DE = \frac{BC}{2}$ (the midpoint triangle has half the perimeter and quarter of the area). Substitute the three known segments and solve.",
      "geo-similarity",
      r"In $\triangle ABC$, $DE \parallel BC$ with $AD = 3$, $DB = 5$, $AE = 6$. Find $EC$.",
      r"$\frac{AD}{DB} = \frac{AE}{EC} \Rightarrow \frac{3}{5} = \frac{6}{EC} \Rightarrow EC = 10$ cm."),
    P("Pythagoras in a story (ladder, poles, displacement, diagonal)", "very common",
      "A ladder against a wall, two poles with a rope between tops, a north-then-east walk, or a rectangle diagonal — a right triangle hiding in a sentence.",
      r"Draw the right triangle; the ladder/wire/diagonal/displacement is the hypotenuse. Then $a^2+b^2=c^2$, ideally via a triplet family (3-4-5, 5-12-13, 8-15-17, 7-24-25).",
      "geo-pythagoras",
      r"Two poles $6$ m and $11$ m high stand $12$ m apart on level ground. Find the distance between their tops.",
      r"Legs: gap $12$ m, height difference $5$ m → $\sqrt{144+25} = 13$ m."),
    P("Regular polygon: angle vs number of sides", "common",
      "An interior/exterior angle, the angle sum, or the diagonal count of a regular polygon is given; n or another of these quantities is asked.",
      r"Convert to the exterior angle: ext $= 180^\circ - $ int, then $n = \frac{360^\circ}{\text{ext}}$. From the sum: $n = \frac{\text{sum}}{180^\circ} + 2$. From diagonals: solve $\frac{n(n-3)}{2} = d$.",
      "geo-quad-poly",
      r"Each interior angle of a regular polygon is $150^\circ$. Find the number of sides.",
      r"ext $= 180^\circ - 150^\circ = 30^\circ$; $n = \frac{360}{30} = 12$."),
    P("Rhombus from diagonals / cyclic quad opposite angles", "very common",
      "Either the diagonals of a rhombus (or its area plus one diagonal) with side/perimeter asked — or a cyclic quadrilateral with one angle (or a ratio) given.",
      r"Rhombus: half-diagonals and side form a right triangle (a triplet in halves); area $= \frac{1}{2}d_1 d_2$. Cyclic quad: opposite angles sum to $180^\circ$; in ratio questions each opposite pair's parts must total the same count.",
      "geo-quad-poly",
      r"The diagonals of a rhombus are $10$ cm and $24$ cm. Find its perimeter.",
      r"Halves $5, 12$ → side $13$ (5-12-13) → perimeter $4 \times 13 = 52$ cm."),
    P("Circle theorems: chord-distance, power of a point, tangent count, centre angle", "very common",
      "A chord with its distance from the centre, a tangent-secant configuration, two circles and their common tangents, or centre-vs-circumference angles on the same arc.",
      r"Chord: $\left(\frac{c}{2}\right)^2 + d^2 = r^2$. Power of a point: tangent$^2$ = external × whole secant; crossing chords $ab = cd$. Common tangents: 4/3/2/1/0 by configuration. Centre angle $= 2 \times$ circumference angle; angle in a semicircle is $90^\circ$.",
      "geo-circles",
      r"A chord $16$ cm long lies in a circle of radius $10$ cm. Find its distance from the centre.",
      r"Half-chord $8$: $d = \sqrt{100-64} = 6$ cm."),
]

if __name__ == "__main__":
    subs = [
        geo_part1.build_lines(),
        geo_part1.build_triangles(),
        geo_part1.build_similarity(),
        geo_part2.build_pyth(),
        geo_part2.build_quadpoly(),
        geo_part2.build_circles(),
    ]
    apply_topic("geometry", subs, PYQ)
