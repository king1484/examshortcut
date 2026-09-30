"""Readable rewrite of Geometry (all 6 subtopics).

Plain English, one idea per section, every number recomputed below.
Run: python geometry.py  (patches content/core/topics/quant/geometry.json in place)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "geometry.json"

# ---------- answer checks (every number printed on the page) ----------
# lines & angles
assert 130 - 40 == 90 and 180 - 50 == 130 and 90 - 50 == 40            # supplement - complement
assert (180 - 30) // 2 == 75 and (180 - 75) - 75 == 30                  # supplement exceeds by d
assert 2 * 45 + 30 == 120 and 45 + 15 == 60 and 120 + 60 == 180         # co-interior x = 45
assert 75 + 105 == 180 and 75 + 75 + 105 + 105 == 360                   # crossing lines
assert 2 * 36 == 72 and 3 * 36 == 108 and 72 + 108 == 180               # ratio 2:3
assert 3 * 25 - 10 == 65 and 2 * 25 + 15 == 65                          # equal pair x = 25
assert 3 * 30 + 20 == 110 and 2 * 30 + 10 == 70 and 110 + 70 == 180       # trick: x = 30
assert 180 - 60 == 120 and 4 * (90 - 60) == 120                         # supplement 4x complement
assert (110 - 70) == 40 and (55 - 35) == 20 and 55 + 35 == 90           # bisector halves
# triangles
assert 40 + 60 + 80 == 180 and 2 * 20 == 40 and 4 * 20 == 80            # ratio 2:3:4
assert 90 + 60 // 2 == 120                                              # BIC, A = 60
assert 120 - 50 == 70                                                   # exterior remote pair
assert 18 // 3 == 6 and 2 * 6 == 12 and 6 + 12 == 18                    # centroid median 18
assert 90 + 70 // 2 == 125 and 2 * 70 == 140 and 180 - 70 == 110        # centres, A = 70
assert (15 // 3) * 2 == 10 and 10 + 5 == 15                             # median 15 -> 10, 5
assert 13 ** 2 - 5 ** 2 == 144 and 144 ** 0 == 1                        # isosceles 13,13,10 -> h 12
assert 21 * 8 * 7 * 6 == 7056 == 84 ** 2                                # Heron 13-14-15
assert 18 * 9 * 6 * 3 == 2916 == 54 ** 2                                # Heron 9-12-15
assert (180 - 40) // 2 == 70                                            # isosceles base angles
# similarity
assert 6 * 16 == 96 and 4 * 4 == 16                                     # 3-4-5 scaled k=4
assert 5 * 9 == 45 and 25 + 81 == 106                                   # area ratio 25:81 -> 5:9
assert 54 * 4 == 216 and 216 // 9 == 24                                 # perimeters 24:36
assert 6 * 5 // 3 == 10                                                 # BPT EC
assert 14 // 2 == 7                                                     # midpoint XY
assert 15 * 3 == 45 and 45 // 5 == 9                                    # bisector DC
assert 20 // 5 == 4 and 3 * 4 + 4 * 4 + 5 * 4 == 48                     # 3-4-5 -> hyp 20, P 48
assert 30 * 5 == 50 * 3 and 18 * 25 // 9 == 50                          # trick: 30/50 perimeters
# pythagoras
assert 17 ** 2 - 8 ** 2 == 225 == 15 ** 2                               # ladder 17, 8 -> 15
assert 9 ** 2 + 12 ** 2 == 225 == 15 ** 2                               # 9-12-15 right
assert 6 ** 2 + 8 ** 2 == 100 < 121 and 81 < 100                        # obtuse vs acute
assert 2 * 6.5 == 13                                                    # median -> hypotenuse
assert 65 ** 2 - 25 ** 2 == 3600 == 60 ** 2                             # field 65, 25 -> 60
assert 7 ** 2 + 24 ** 2 == 625 == 25 ** 2                               # ladder 25, foot 7 -> 24
assert 25 ** 2 - 7 ** 2 == 576 == 24 ** 2
assert 13 / 2 == 6.5                                                    # median to hyp 13
assert 5 * 12 == 60 and 8 * 15 == 120                                   # family multiples
assert 12 + 16 + 20 == 48 and 3 * 4 == 12 and 4 * 4 == 16               # 3:4 legs, hyp 20
# quads & polygons
assert 180 - 150 == 30 and 360 // 30 == 12                              # interior 150 -> n 12
assert 180 - 156 == 24 and 360 // 24 == 15                              # interior 156 -> n 15
assert 5 ** 2 + 12 ** 2 == 169 == 13 ** 2 and 4 * 13 == 52              # rhombus 10,24 -> P 52
assert 10 * 24 // 2 == 120                                              # rhombus area
assert 30 * 24 // 2 == 360 and 8 * 6 == 48                              # rhombus 16,12 -> side 10, area 96
assert 16 * 12 // 2 == 96 and 4 * 10 == 40
assert 3 * 180 // 4 == 135 and 180 - 135 == 45                          # parallelogram 1:3
assert 180 - 70 == 110                                                  # cyclic opposite
assert 2 * 105 == 210 and 210 // 30 == 7                                # trapezium height
assert (13 + 17) // 2 == 15 and (13 + 17) * 7 // 2 == 105               # midsegment, area
assert 10 * 7 // 2 == 35                                                # decagon diagonals
assert (6 - 2) * 180 == 720 and 360 // 6 == 60 and 180 - 60 == 120      # hexagon angles
assert 2 * 30 == 60 and 3 * 30 == 90 and 4 * 30 == 120                  # cyclic 2:3:4:3
assert 60 + 120 == 180 and 90 + 90 == 180                               # opposite pairs
# circles
assert 15 ** 2 - 9 ** 2 == 144 == 12 ** 2 and 2 * 12 == 24              # chord 9 from centre, r 15
assert 13 ** 2 - 5 ** 2 == 144 == 12 ** 2 and 2 * 12 == 24              # chord 5 from centre, r 13
assert 10 ** 2 == 5 * 20 and 20 - 5 == 15                               # tangent-secant
assert 4 == 6 - 2                                                       # internal tangency
assert 6 + 2 == 8 < 13 and 13 == 4 + 9                                  # external tangency
assert 120 // 2 == 60                                                   # centre vs circumference
assert 13 ** 2 - 5 ** 2 == 144 == 12 ** 2                               # tangent from P, d 13, r 5
assert 625 - 49 == 576 == 24 ** 2 and 2 * 24 == 48                      # concentric 25, 7
assert 40 == 40                                                         # alternate segment

# ================= geo-lines-angles =================
la_concept = (
    "Angles on one straight line add to $180^\\circ$. Angles around one point add to $360^\\circ$. "
    "When two lines cross, the angles facing each other are equal. "
    "When a line cuts two parallel lines, matching angles are equal and one inside pair adds to $180^\\circ$. "
    "Almost every question becomes one small equation in $x$."
)

la_notes = r"""### The two angle pairs
An angle measures the turn between two lines.

- Two angles are **complementary** if they add to $90^\circ$.
- Two angles are **supplementary** if they add to $180^\circ$.

For any angle $x$: its complement is $90^\circ-x$ and its supplement is $180^\circ-x$.

> **Rule:** Supplement $-$ complement $=90^\circ$, always. For $x=50^\circ$: $130^\circ-40^\circ=90^\circ$.

If a supplement exceeds its angle by $d$, the angle is $\dfrac{180^\circ-d}{2}$.
With $d=30^\circ$: angle $=75^\circ$, supplement $=105^\circ$, gap $=30^\circ$. It works.

### One line, one point, two crossing lines
Angles on one straight line add to $180^\circ$. Angles filling one full turn around a point add to $360^\circ$.

Two straight lines cross and make four angles:
- **Vertically opposite** angles (facing each other) are equal.
- Any two neighbouring angles add to $180^\circ$.

So one angle of $75^\circ$ fixes all four: $75^\circ, 105^\circ, 75^\circ, 105^\circ$.

> **Tip:** Given three angles around a point, the fourth is $360^\circ$ minus their sum. That is the whole sum.

### Parallel lines cut by a transversal
A **transversal** is a line that crosses two parallel lines. It makes eight angles, but only two different sizes.

| Pair | Shape | Rule |
|---|---|---|
| Corresponding | F | equal |
| Alternate | Z | equal |
| Co-interior (allied) | C, same side inside | add to $180^\circ$ |

> **Watch:** Co-interior angles add to $180^\circ$ only because the lines are parallel. No parallel lines, no rule.

### Turn the picture into one equation
Write the relation the picture shows. Then solve for $x$.

Two co-interior angles are $(2x+30)^\circ$ and $(x+15)^\circ$:
$$(2x+30)+(x+15)=180 \Rightarrow 3x=135 \Rightarrow x=45$$
So the angles are $120^\circ$ and $60^\circ$. Check by adding: $120^\circ+60^\circ=180^\circ$.

A ratio works the same way. Co-interior angles in the ratio $2:3$ are $2k$ and $3k$, so $5k=180^\circ$. The angles are $72^\circ$ and $108^\circ$.

> **Watch:** After finding $x$, re-read the question. It often asks the larger angle, the smaller one, or a partner angle, not $x$ itself.

### Bisectors
A **bisector** cuts an angle into two equal halves. Halving keeps every relation, only smaller.

Supplementary angles $110^\circ$ and $70^\circ$ have halves $55^\circ$ and $35^\circ$. The gap halves too: from $40^\circ$ to $20^\circ$.

The bisectors of a co-interior pair meet at $90^\circ$. The halves add to half of $180^\circ$, so the remaining angle in their triangle is exactly $90^\circ$.
"""

la_formulas = [
    {"name": "Angles on a line / around a point", "tex": r"180^\circ,\ 360^\circ", "note": "A straight line totals 180 degrees; one full turn totals 360."},
    {"name": "Co-interior angles", "tex": r"a+b=180^\circ", "note": "The two inside angles on one side of a transversal, between parallel lines."},
    {"name": "Complement / supplement", "tex": r"\text{supplement}-\text{complement}=90^\circ", "note": "Complement = 90 − x, supplement = 180 − x."},
    {"name": "Equal pairs at parallels", "tex": r"\text{corresponding}=\text{alternate}=\text{vertically opposite}", "note": "Each of these pairs is equal."},
]

la_tricks = [
    {
        "title": "Say the shape, then the rule",
        "body": "Trace the two angles with your finger. An F or Z shape means they are equal. A C shape means they add to $180^\\circ$.",
        "example": {
            "q": "Two co-interior angles between parallel lines are $(3x+20)^\\circ$ and $(2x+10)^\\circ$. Find the larger angle.",
            "steps": [r"C shape, so the sum is $180^\circ$: $5x+30=180$.", r"$x=30$.", r"Angles: $3(30)+20=110^\circ$ and $2(30)+10=70^\circ$."],
            "answer": "110°",
        },
    },
    {
        "title": "Supplement minus complement is always 90",
        "body": "Whatever the angle, its supplement and its complement differ by exactly $90^\\circ$. Use it as a free check, or to build the equation.",
        "example": {
            "q": "The supplement of an angle is four times its complement. Find the angle.",
            "steps": [r"Let the angle be $x$. Then $180-x=4(90-x)$.", r"$180-x=360-4x$, so $3x=180$.", r"$x=60^\circ$. Check: supplement $120^\circ$, complement $30^\circ$, ratio $4$."],
            "answer": "60°",
        },
    },
]

la_mistakes = [
    {"wrong": "Adding co-interior angles to $180^\\circ$ when the lines are not parallel.", "right": "Check the question says parallel first. Only then use the $180^\\circ$ rule."},
    {"wrong": "Mixing up the Z pair and the C pair in the transversal figure.", "right": "Z (alternate) pairs are equal; C (co-interior) pairs add to $180^\\circ$. Trace the shape."},
    {"wrong": "Solving for $x$ and marking $x$ as the answer.", "right": "Re-read the last line, then put $x$ into the angle actually asked."},
    {"wrong": "Writing the complement as $180^\\circ-x$.", "right": "Complement is $90^\\circ-x$. Supplement is $180^\\circ-x$."},
    {"wrong": "Halving one angle but not the other in bisector questions.", "right": "A bisector halves both angles, so every difference also halves."},
]

la_revision = [
    "On a line: $180^\\circ$. Around a point: $360^\\circ$. Vertically opposite angles are equal.",
    "Parallel lines: F-shape and Z-shape pairs equal, C-shape pairs add to $180^\\circ$.",
    r"Complement $=90^\circ-x$, supplement $=180^\circ-x$; they always differ by $90^\circ$.",
    r"Supplement exceeds the angle by $d$: angle $=\dfrac{180^\circ-d}{2}$.",
    "Solve the equation for $x$, then answer the angle asked.",
    "Bisectors halve angles, and halve the gaps between them.",
]

la_patterns = [
    {"id": "geo-la-p1", "name": "Co-interior angles with x in them", "frequency": "very common",
     "howToSpot": "Parallel lines with a transversal; the two inside angles on one side are given as $(ax+b)^\\circ$ and $(cx+d)^\\circ$.",
     "formula": r"(ax+b)+(cx+d)=180^\circ",
     "steps": ["Add the two expressions and set the total to $180^\\circ$.", "Solve the linear equation for $x$.", "Put $x$ back into the angle asked.", "Check the two angles add to $180^\\circ$."],
     "why": "Co-interior angles between parallel lines are supplementary, so the expressions must total $180^\\circ$.",
     "example": {"q": "Two co-interior angles between parallel lines are $(2x+30)^\\circ$ and $(x+15)^\\circ$. Find the larger angle.",
                 "steps": [r"Sum: $(2x+30)+(x+15)=180$.", r"$3x+45=180$, so $x=45$.", r"Angles: $2(45)+30=120^\circ$ and $45+15=60^\circ$."],
                 "answer": "120°"}},
    {"id": "geo-la-p2", "name": "Corresponding or alternate angles are equal", "frequency": "very common",
     "howToSpot": "Two angles in an F-shape (corresponding) or Z-shape (alternate) position, both with $x$ in them, or one given and its partner asked.",
     "formula": r"ax+b=cx+d",
     "steps": ["Spot the pair shape: F means corresponding, Z means alternate. Both are equal.", "Equate the two expressions.", "Solve for $x$ and substitute back.", "Any neighbouring angle is $180^\\circ$ minus this one."],
     "why": "A transversal across parallels makes only two angle sizes, and an equal pair uses the same size twice.",
     "example": {"q": "Two corresponding angles between parallel lines are $(3x-10)^\\circ$ and $(2x+15)^\\circ$. Find the angle.",
                 "steps": [r"Equal pair: $3x-10=2x+15$.", r"$x=25$.", r"Angle: $3(25)-10=65^\circ$."],
                 "answer": "65°"}},
    {"id": "geo-la-p3", "name": "Complement and supplement of an angle", "frequency": "very common",
     "howToSpot": "'The supplement of an angle is n times its complement', or a difference between supplement and complement is mentioned.",
     "formula": r"180^\circ-x=n(90^\circ-x)",
     "steps": ["Write complement $=90^\\circ-x$ and supplement $=180^\\circ-x$.", "Turn the sentence into one equation.", "Solve for $x$.", "Check with supplement $-$ complement $=90^\\circ$."],
     "why": "Both come from the same $x$, so any 'n times' sentence is one linear equation.",
     "example": {"q": "The supplement of an angle is three times its complement. Find the angle.",
                 "steps": [r"$180-x=3(90-x)$.", r"$180-x=270-3x$, so $2x=90$.", r"$x=45^\circ$. Check: supplement $135^\circ$, complement $45^\circ$."],
                 "answer": "45°"}},
    {"id": "geo-la-p4", "name": "Angles on a line, around a point, crossing lines", "frequency": "common",
     "howToSpot": "Several angles at a point or on a line are given and one is missing, or two crossing lines give one angle and ask the rest.",
     "formula": r"\text{line}=180^\circ,\quad \text{point}=360^\circ",
     "steps": ["Pick the total: $180^\\circ$ on a line, $360^\\circ$ around a point.", "Add the known angles.", "Subtract from the total to get the missing angle.", "For crossing lines, mark the equal vertically opposite pairs."],
     "why": "The totals are fixed, so the missing angle is always a remainder.",
     "example": {"q": "Two straight lines intersect. One of the four angles formed is $75^\\circ$. Find the obtuse angle among the other three.",
                 "steps": [r"Neighbours are supplementary: $180-75=105^\circ$.", r"The vertically opposite angle is also $105^\circ$.", r"Both remaining angles are obtuse: $105^\circ$."],
                 "answer": "105°"}},
    {"id": "geo-la-p5", "name": "Angle bisectors in line figures", "frequency": "occasional",
     "howToSpot": "An angle is bisected and the halves, or the angle between two bisectors, are asked.",
     "formula": r"\text{half}=\dfrac{\theta}{2}",
     "steps": ["Halve every angle the bisector touches.", "Halve every difference too: bisecting keeps relations but halves gaps.", "Remember: bisectors of a co-interior pair meet at $90^\\circ$."],
     "why": "Cutting two angles in half cuts every gap between them in half as well.",
     "example": {"q": "Two supplementary angles differ by $40^\\circ$. After both are bisected, what is the difference between the halves?",
                 "steps": [r"The angles are $110^\circ$ and $70^\circ$.", r"Halves: $55^\circ$ and $35^\circ$.", r"Difference of halves: $55-35=20^\circ$."],
                 "answer": "20°"}},
]

# ================= geo-triangles =================
tr_concept = (
    "The three inside angles of a triangle add to $180^\\circ$. An outside angle equals the sum of the two far inside angles. "
    "Each triangle has four special centres: centroid (medians), incentre (angle bisectors), circumcentre (perpendicular bisectors) "
    "and orthocentre (altitudes). Exams ask one fixed fact about each."
)

tr_notes = r"""### The angle rules
Inside angles always add to $180^\circ$. An **exterior angle** is made by extending one side. It equals the sum of the two **remote** interior angles, the two far away from it. So the exterior angle at $A$ equals $B+C$.

Angles given as a ratio $2:3:4$: write them $2k$, $3k$, $4k$. Then $9k=180^\circ$, so $k=20^\circ$. The angles are $40^\circ$, $60^\circ$, $80^\circ$.

An **isosceles** triangle has two equal sides and two equal base angles. The median to the base is also the height and the bisector: one line, three jobs. Two angles of $40^\circ$ force the third to be $100^\circ$, because equal angles sit opposite equal sides.

### The four centres
| Centre | Made by | Fact to use |
|---|---|---|
| Centroid $G$ | medians | cuts each median $2:1$ from the vertex |
| Incentre $I$ | angle bisectors | $\angle BIC=90^\circ+\dfrac{A}{2}$ |
| Circumcentre $O$ | perpendicular bisectors | $\angle BOC=2A$ |
| Orthocentre $H$ | altitudes | $\angle BHC=180^\circ-A$ |

> **Rule:** Name the centre from what builds it. Then apply its one formula with the given $\angle A$.

### Using the centre facts
Take $\angle A=70^\circ$:
- Incentre: $\angle BIC=90^\circ+35^\circ=125^\circ$
- Circumcentre: $\angle BOC=2\times70^\circ=140^\circ$
- Orthocentre: $\angle BHC=180^\circ-70^\circ=110^\circ$

The centroid works on lengths, not angles. It cuts every median $2:1$ from the vertex. A median of $15$ cm splits into $10$ cm (vertex side) and $5$ cm (base side). A median of $18$ cm splits into $12$ cm and $6$ cm the same way.

> **Tip:** In a right triangle the orthocentre sits at the right-angle vertex and the circumcentre is the midpoint of the hypotenuse. In an equilateral triangle all four centres are one point.

### Median lengths
Three facts cover the median questions:
- Median to the hypotenuse of a right triangle $=$ half the hypotenuse.
- Isosceles with equal sides $13$ and base $10$: median to base $=\sqrt{13^2-5^2}=\sqrt{169-25}=12$.
- Any triangle: Apollonius, $m_a^2=\dfrac{2b^2+2c^2-a^2}{4}$, where $m_a$ is the median to side $a$.

### Area from three sides
Heron's rule: $s=\dfrac{a+b+c}{2}$ (half the perimeter), then area $=\sqrt{s(s-a)(s-b)(s-c)}$.
Sides $13$, $14$, $15$: $s=21$, area $=\sqrt{21\times8\times7\times6}=\sqrt{7056}=84$. Sides $9$, $12$, $15$ give $s=18$ and area $\sqrt{18\times9\times6\times3}=54$ by either route.

> **Tip:** If the sides form a Pythagorean triplet such as 9-12-15, skip Heron. The triangle is right-angled, so the area is half the product of the two legs.
"""

tr_formulas = [
    {"name": "Angle sum and exterior angle", "tex": r"A+B+C=180^\circ,\quad \text{ext at }A=B+C", "note": "Exterior angle = sum of the two remote (far) interior angles."},
    {"name": "Centroid division", "tex": r"AG:GD=2:1", "note": "G is the centroid on median AD; the vertex piece is twice the base piece."},
    {"name": "Incentre angle", "tex": r"\angle BIC=90^\circ+\dfrac{A}{2}", "note": "I = incentre, where the angle bisectors meet."},
    {"name": "Circumcentre angle", "tex": r"\angle BOC=2A", "note": "O = circumcentre; the angle at O stands on the same arc BC as angle A."},
    {"name": "Orthocentre angle", "tex": r"\angle BHC=180^\circ-A", "note": "H = orthocentre, where the altitudes meet."},
    {"name": "Apollonius (median length)", "tex": r"m_a^2=\dfrac{2b^2+2c^2-a^2}{4}", "note": "Median to side a of a triangle with sides a, b, c."},
    {"name": "Isosceles median to base", "tex": r"m=\sqrt{a^2-\left(\dfrac{b}{2}\right)^2}", "note": "a = equal side, b = base."},
    {"name": "Heron's area", "tex": r"K=\sqrt{s(s-a)(s-b)(s-c)},\ s=\dfrac{a+b+c}{2}", "note": "s = semi-perimeter (half the perimeter)."},
]

tr_tricks = [
    {
        "title": "Centre angles from one input",
        "body": "Only $\\angle A$ is needed. Read which centre the question names, then use its formula.",
        "example": {
            "q": "In $\\triangle ABC$, $\\angle A=70^\\circ$ and $H$ is the orthocentre. Find $\\angle BHC$.",
            "steps": [r"Orthocentre: $\angle BHC=180^\circ-A$.", r"$180^\circ-70^\circ=110^\circ$.", r"(Incentre would give $125^\circ$, circumcentre $140^\circ$.)"],
            "answer": "110°",
        },
    },
    {
        "title": "Centroid cut in the ratio 2 : 1",
        "body": "Call the median $3$ parts. The centroid gives $2$ parts on the vertex side and $1$ part on the base side.",
        "example": {
            "q": "The median $AD$ of $\\triangle ABC$ is 15 cm and $G$ is the centroid. Find $AG$.",
            "steps": [r"$AG=\dfrac{2}{3}\times15$.", r"$AG=10$ cm (and $GD=5$ cm)."],
            "answer": "10 cm",
        },
    },
    {
        "title": "Median in an isosceles triangle",
        "body": "Skip Apollonius when two sides are equal. The median to the base is $\\sqrt{a^2-(b/2)^2}$ with $a$ the equal side and $b$ the base.",
        "example": {
            "q": "Find the median to the base of an isosceles triangle with equal sides 25 cm and base 14 cm.",
            "steps": [r"Half the base $=7$ cm.", r"$\sqrt{25^2-7^2}=\sqrt{625-49}$.", r"$\sqrt{576}=24$ cm."],
            "answer": "24 cm",
        },
    },
    {
        "title": "Heron families worth memorising",
        "body": "(3,4,5) gives 6, (5,12,13) gives 30, (13,14,15) gives 84, (7,24,25) gives 84, (9,12,15) gives 54, (10,24,26) gives 120.",
        "example": {
            "q": "Find the area of a triangle with sides 13 cm, 14 cm, 15 cm.",
            "steps": [r"$s=\dfrac{13+14+15}{2}=21$.", r"$\sqrt{21\times8\times7\times6}$.", r"$\sqrt{7056}=84$ sq cm."],
            "answer": "84 sq cm",
        },
    },
]

tr_mistakes = [
    {"wrong": "Swapping the centre formulas under time pressure.", "right": "Incentre $90^\\circ+\\dfrac{A}{2}$, circumcentre $2A$, orthocentre $180^\\circ-A$. Recite before substituting."},
    {"wrong": "Taking $GD=\\dfrac{2}{3}AD$ at the centroid.", "right": "The vertex piece $AG$ is $\\dfrac{2}{3}$. The base piece $GD$ is $\\dfrac{1}{3}$."},
    {"wrong": "Adding the two near angles for the exterior angle.", "right": "The exterior angle equals the two remote interior angles, the ones away from that corner."},
    {"wrong": "Using the full perimeter inside Heron's formula.", "right": "Halve the perimeter first: $s=\\dfrac{a+b+c}{2}$, then use $s-a$, $s-b$, $s-c$."},
    {"wrong": "Forgetting the median to the hypotenuse is half of it.", "right": "In a right triangle that median is always $\\dfrac{\\text{hypotenuse}}{2}$."},
]

tr_revision = [
    "Inside angles total $180^\\circ$; exterior angle $=$ sum of the two remote interior angles.",
    "$\\angle BIC=90^\\circ+\\dfrac{A}{2}$, $\\angle BOC=2A$, $\\angle BHC=180^\\circ-A$.",
    "Centroid cuts each median $2:1$ from the vertex: $AG=\\dfrac{2}{3}AD$.",
    "Median to the hypotenuse $=$ half the hypotenuse.",
    r"Isosceles median $=\sqrt{a^2-(b/2)^2}$; general median by Apollonius.",
    r"Heron: $s$ first, then $\sqrt{s(s-a)(s-b)(s-c)}$; triplet sides mean a right triangle.",
]

tr_patterns = [
    {"id": "geo-tr-p1", "name": "Angle at a triangle centre", "frequency": "very common",
     "howToSpot": "The question names I, O or H as incentre, circumcentre or orthocentre (or defines them by bisectors, perpendicular bisectors, altitudes).",
     "formula": r"\angle BIC=90^\circ+\dfrac{A}{2},\quad \angle BOC=2A,\quad \angle BHC=180^\circ-A",
     "steps": ["Name the centre from its definition.", "Pick its formula and substitute the given $\\angle A$.", "Going backwards: from $\\angle BIC$ get $A=2(\\angle BIC-90^\\circ)$."],
     "why": "Each centre fixes a triangle inside the original, and its angles depend only on $\\angle A$.",
     "example": {"q": "In $\\triangle ABC$, $\\angle A=60^\\circ$ and $I$ is the incentre. Find $\\angle BIC$.",
                 "steps": [r"$\angle BIC=90^\circ+\dfrac{A}{2}$.", r"$=90^\circ+30^\circ$.", r"$=120^\circ$."],
                 "answer": "120°"}},
    {"id": "geo-tr-p2", "name": "Exterior angle of a triangle", "frequency": "very common",
     "howToSpot": "One side of the triangle is extended; the exterior angle is asked, or a remote interior angle is missing.",
     "formula": r"\text{ext at }A=B+C",
     "steps": ["Find the two remote interior angles, away from the extended corner.", "Add them for the exterior angle.", "Subtract instead when one remote angle is missing."],
     "why": "The exterior angle and the corner angle add to $180^\\circ$, and the three interior angles also add to $180^\\circ$.",
     "example": {"q": "An exterior angle of a triangle is $120^\\circ$ and one remote interior angle is $50^\\circ$. Find the other remote interior angle.",
                 "steps": [r"Exterior $=$ sum of remotes.", r"$120-50=70^\circ$.", r"Check: $50+70=120$."],
                 "answer": "70°"}},
    {"id": "geo-tr-p3", "name": "Centroid cuts the median 2 : 1", "frequency": "very common",
     "howToSpot": "A median and the centroid G appear; AG, GD, their sum or difference is asked.",
     "formula": r"AG=\dfrac{2}{3}AD,\quad GD=\dfrac{1}{3}AD",
     "steps": ["Mark the median and the centroid on it.", "Split it $2:1$: vertex side twice the base side.", "Turn word conditions into parts of the median, e.g. $AG-GD=c$ means $\\dfrac{1}{3}AD=c$."],
     "why": "The centroid is the balance point, and it sits twice as far from the vertex as from the side.",
     "example": {"q": "In $\\triangle ABC$, median $AD=18$ cm and $G$ is the centroid. Find $GD$.",
                 "steps": [r"$GD=\dfrac{1}{3}\times18$.", r"$GD=6$ cm.", r"(And $AG=12$ cm.)"],
                 "answer": "6 cm"}},
    {"id": "geo-tr-p4", "name": "Area of a triangle: Heron or triplet", "frequency": "common",
     "howToSpot": "Three sides given and the area asked, often a triplet family in disguise.",
     "formula": r"K=\sqrt{s(s-a)(s-b)(s-c)},\quad s=\dfrac{a+b+c}{2}",
     "steps": ["Check for a triplet: right triangle, so area $=\\dfrac{1}{2}\\times$ the two legs.", "Otherwise compute $s$, the semi-perimeter.", "Multiply $s(s-a)(s-b)(s-c)$ and take the square root."],
     "why": "Heron works for any triangle; triplets just let you skip it.",
     "example": {"q": "Find the area of a triangle with sides 9 cm, 12 cm and 15 cm.",
                 "steps": [r"9-12-15 is 3-4-5 times 3, so it is right-angled.", r"Area $=\dfrac{1}{2}\times9\times12$.", r"$=54$ sq cm."],
                 "answer": "54 sq cm"}},
    {"id": "geo-tr-p5", "name": "Angles given as a ratio", "frequency": "very common",
     "howToSpot": "The three angles of a triangle are in a ratio like 2 : 3 : 4; one angle, or the largest, is asked.",
     "formula": r"(a+b+c)k=180^\circ",
     "steps": ["Write the angles as $ak$, $bk$, $ck$.", "Add the ratio parts and divide $180^\\circ$ by the total.", "Multiply each part by $k$; read off the angle asked."],
     "why": "The ratio fixes the shares; the $180^\\circ$ total fixes their size.",
     "example": {"q": "The angles of a triangle are in the ratio $2:3:4$. Find the largest angle.",
                 "steps": [r"$2k+3k+4k=180^\circ$.", r"$9k=180^\circ$, so $k=20^\circ$.", r"Largest $=4\times20^\circ=80^\circ$."],
                 "answer": "80°"}},
    {"id": "geo-tr-p6", "name": "Isosceles triangle angles", "frequency": "common",
     "howToSpot": "Two equal sides are stated or drawn; one angle is given and another is asked.",
     "formula": r"\text{base}+\text{base}+\text{vertex}=180^\circ",
     "steps": ["Mark the two equal base angles.", "Use the $180^\\circ$ total with the given angle.", "Equal sides sit opposite equal angles."],
     "why": "Equal sides always face equal angles, so two of the three angles match.",
     "example": {"q": "The vertex angle of an isosceles triangle is $40^\\circ$. Find each base angle.",
                 "steps": [r"Base angles are equal: $2b+40^\circ=180^\circ$.", r"$2b=140^\circ$.", r"$b=70^\circ$."],
                 "answer": "70°"}},
]

# ================= geo-similarity =================
si_concept = (
    "**Congruent** triangles are identical in size and shape. **Similar** triangles have the same shape but a different size. "
    "If the scale factor is $k$, every length scales by $k$ and every area by $k^2$. "
    "A line parallel to one side cuts the other two sides in the same ratio (BPT). "
    "The segment joining two midpoints is half the third side."
)

si_notes = r"""### Same shape, different size
Similar figures keep the same shape. One is a scaled copy of the other.

If the **scale factor** is $k$ (a side of the big one is $k$ times the matching side of the small one):
- lengths (sides, perimeters, medians, heights) scale by $k$
- **areas scale by $k^2$**

A 3-4-5 triangle scaled by $k=4$ becomes 12-16-20. Its area grows $6 \to 96$, which is $6\times16=6\times k^2$.

> **Rule:** Lengths take $k$ once, areas take $k$ twice. That one line is half the subtopic.

### From areas back to sides
Going from an area ratio to a length ratio needs a square root.

Areas $25$ and $81$ give a side ratio $5:9$, never $25:81$. In the other direction, perimeters $p:q$ give areas $p^2:q^2$. A $9:25$ area ratio means sides and perimeters in $3:5$. First match the vertices in order: $A$ pairs with $A'$, $B$ with $B'$, so side $AB$ pairs with $A'B'$. Only then form ratios.

> **Watch:** Options almost always include both the squared and the unsquared ratio. Decide which way you are going before looking.

### A line parallel to a side (BPT)
Draw $DE$ parallel to $BC$ inside $\triangle ABC$. Then
$$\frac{AD}{DB}=\frac{AE}{EC}$$
So the parallel line cuts both sides in the same ratio.

If $AD:DB=3:5$ and $AE=6$ cm, then $EC=\dfrac{6\times5}{3}=10$ cm. Cross-multiply and the answer falls out in one line.

> **Watch:** Use part with part ($AD$ with $DB$) or full with full ($AD$ with $AB$). Mixing a part with a full side is the classic slip.

### The midpoint theorem
$D$ and $E$ are the midpoints of two sides. Then $DE$ is parallel to the third side and
$$DE=\frac{BC}{2}$$
Join all three midpoints and you get four small triangles. Each small side is half a big side, so each small triangle has half the perimeter and one quarter of the area. A 3-4-5 triangle of area $6$ splits into four small triangles of area $1.5$ each. Heights, medians and diagonals are lengths too, so they scale by $k$ just like the sides.

Converse: through the midpoint of one side, a line parallel to a second side bisects the third.

### The angle bisector theorem
The bisector of $\angle A$ meets $BC$ at $D$. Then
$$\frac{BD}{DC}=\frac{AB}{AC}$$
The opposite side is split in the ratio of its two neighbouring sides.

With $AB=8$, $AC=12$, $BC=15$: the ratio is $8:12=2:3$, so $DC=\dfrac{3}{5}\times15=9$ cm and $BD=15-9=6$ cm. The two pieces always add back to the whole side, which is a fast check.

> **Tip:** No parallel line is needed here. BPT needs parallels; the bisector theorem needs an angle bisector.
"""

si_formulas = [
    {"name": "Similarity ratios", "tex": r"\frac{a_1}{a_2}=k,\quad \frac{P_1}{P_2}=k,\quad \frac{K_1}{K_2}=k^2", "note": "a = side, P = perimeter, K = area; k = scale factor."},
    {"name": "Areas from perimeters", "tex": r"\frac{K_1}{K_2}=\left(\frac{P_1}{P_2}\right)^2", "note": "Square a length ratio to get the area ratio; take a root to go back."},
    {"name": "BPT (Thales)", "tex": r"DE\parallel BC\Rightarrow\frac{AD}{DB}=\frac{AE}{EC}", "note": "A line parallel to one side cuts the other two sides in the same ratio."},
    {"name": "Midpoint theorem", "tex": r"D,E\ \text{midpoints}\Rightarrow DE=\frac{BC}{2}", "note": "The join of two midpoints is half the third side and parallel to it."},
    {"name": "Angle bisector theorem", "tex": r"\frac{BD}{DC}=\frac{AB}{AC}", "note": "The bisector of angle A splits BC in the ratio of the sides AB and AC."},
]

si_tricks = [
    {
        "title": "Square the perimeter ratio for areas",
        "body": "Perimeters in ratio $p:q$ mean areas in ratio $p^2:q^2$. Going back, take the square root.",
        "example": {
            "q": "Two similar triangles have perimeters 30 cm and 50 cm. The smaller has area 18 sq cm. Find the larger area.",
            "steps": [r"Side ratio $=\dfrac{30}{50}=\dfrac{3}{5}$.", r"Area ratio $=\dfrac{9}{25}$.", r"Larger $=18\times\dfrac{25}{9}=50$ sq cm."],
            "answer": "50 sq cm",
        },
    },
    {
        "title": "Spot the word midpoints",
        "body": "'Midpoints of two sides' means the joining segment is half the third side, and parallel to it.",
        "example": {
            "q": "In $\\triangle ABC$, $D$ and $E$ are midpoints of $AB$ and $AC$. If $DE=4.5$ cm, find $BC$.",
            "steps": [r"$BC=2\times DE$.", r"$=2\times4.5$.", r"$=9$ cm."],
            "answer": "9 cm",
        },
    },
    {
        "title": "BPT: write the ratio directly",
        "body": "A line parallel to a side cuts equal ratios on both other sides. Write the proportion, substitute, solve.",
        "example": {
            "q": "In $\\triangle ABC$, $DE\\parallel BC$ with $AD=4$ cm, $DB=6$ cm and $AE=5$ cm. Find $EC$.",
            "steps": [r"$\dfrac{AE}{EC}=\dfrac{AD}{DB}=\dfrac{4}{6}$.", r"$EC=\dfrac{5\times6}{4}$.", r"$EC=7.5$ cm."],
            "answer": "7.5 cm",
        },
    },
]

si_mistakes = [
    {"wrong": "Using the side ratio for areas without squaring.", "right": "Areas take $k^2$. A $3:5$ side ratio means a $9:25$ area ratio."},
    {"wrong": "Squaring when going from areas back to lengths.", "right": "That direction needs the square root: areas $25:81$ give sides $5:9$."},
    {"wrong": "Using $DE=\\dfrac{BC}{2}$ for any parallel line.", "right": "The half rule needs midpoints. A general parallel uses BPT ratios."},
    {"wrong": "Mixing part and full ratios in BPT.", "right": "Pair $AD$ with $DB$, or $AD$ with $AB$. Never one of each."},
    {"wrong": "Applying BPT to an angle bisector figure.", "right": "No parallel line, no BPT. The bisector splits the side as $AB:AC$."},
]

si_revision = [
    "Similar figures: lengths scale by $k$, areas by $k^2$.",
    "Area ratio to length ratio: take the square root.",
    "$DE\\parallel BC$ gives $\\dfrac{AD}{DB}=\\dfrac{AE}{EC}$.",
    "Midpoints: $DE=\\dfrac{BC}{2}$; midpoint triangle has half perimeter, quarter area.",
    "Bisector of $\\angle A$: $\\dfrac{BD}{DC}=\\dfrac{AB}{AC}$.",
    "Match small with small and large with large before scaling.",
]

si_patterns = [
    {"id": "geo-si-p1", "name": "Perimeter ratio and area ratio", "frequency": "very common",
     "howToSpot": "Two similar triangles with perimeters (or a pair of matching sides) in a ratio; one area is asked, or areas are given and a perimeter asked.",
     "formula": r"\frac{K_1}{K_2}=\left(\frac{P_1}{P_2}\right)^2",
     "steps": ["Find the length ratio from the perimeters or matching sides.", "Square it for the area ratio, or take a root to go from areas to lengths.", "Scale the known quantity by that ratio."],
     "why": "Area multiplies two lengths, so the scale factor enters twice.",
     "example": {"q": "Two similar triangles have perimeters 24 cm and 36 cm. The larger has area 54 sq cm. Find the smaller area.",
                 "steps": [r"Side ratio $=\dfrac{24}{36}=\dfrac{2}{3}$.", r"Area ratio $=\dfrac{4}{9}$.", r"Smaller $=54\times\dfrac{4}{9}=24$ sq cm."],
                 "answer": "24 sq cm"}},
    {"id": "geo-si-p2", "name": "BPT: a parallel line inside the triangle", "frequency": "very common",
     "howToSpot": "$DE\\parallel BC$ with three of the four pieces $AD$, $DB$, $AE$, $EC$ known; the fourth is asked.",
     "formula": r"\frac{AD}{DB}=\frac{AE}{EC}",
     "steps": ["Write the part ratio on one side equal to the part ratio on the other.", "Substitute the three known pieces.", "Solve the proportion for the fourth."],
     "why": "The parallel line makes two similar triangles, so both sides carry the same cut ratio.",
     "example": {"q": "In $\\triangle ABC$, $DE\\parallel BC$ with $AD=3$ cm, $DB=5$ cm and $AE=6$ cm. Find $EC$.",
                 "steps": [r"$\dfrac{3}{5}=\dfrac{6}{EC}$.", r"$EC=\dfrac{6\times5}{3}$.", r"$EC=10$ cm."],
                 "answer": "10 cm"}},
    {"id": "geo-si-p3", "name": "Midpoint theorem", "frequency": "common",
     "howToSpot": "'D and E are the midpoints of AB and AC'; find DE from BC or BC from DE, or use the midpoint triangle.",
     "formula": r"DE=\frac{BC}{2}",
     "steps": ["Confirm both points are midpoints.", "Double or halve as asked.", "For the triangle of midpoints: perimeter half, area one quarter."],
     "why": "The midpoint segment is the BPT case where the cut ratio is $1:1$.",
     "example": {"q": "In $\\triangle PQR$, $X$ and $Y$ are the midpoints of $PQ$ and $PR$. If $QR=14$ cm, find $XY$.",
                 "steps": [r"$XY=\dfrac{QR}{2}$.", r"$=\dfrac{14}{2}$.", r"$=7$ cm."],
                 "answer": "7 cm"}},
    {"id": "geo-si-p4", "name": "Angle bisector theorem", "frequency": "common",
     "howToSpot": "A bisector meets the opposite side; the two pieces of that side, or a side length, are asked.",
     "formula": r"\frac{BD}{DC}=\frac{AB}{AC}",
     "steps": ["Write the ratio of the two sides around the bisected angle.", "Split the opposite side in that ratio.", "With one piece known, scale it by the ratio."],
     "why": "The bisector divides the opposite side exactly as the adjacent sides are divided.",
     "example": {"q": "In $\\triangle ABC$, the bisector of $\\angle A$ meets $BC$ at $D$. If $AB=8$ cm, $AC=12$ cm and $BC=15$ cm, find $DC$.",
                 "steps": [r"$BD:DC=8:12=2:3$.", r"$DC=\dfrac{3}{5}$ of $BC$.", r"$DC=\dfrac{3}{5}\times15=9$ cm."],
                 "answer": "9 cm"}},
    {"id": "geo-si-p5", "name": "Scale a whole triangle", "frequency": "common",
     "howToSpot": "All three sides of one triangle given; the similar triangle has one side given and the rest asked.",
     "formula": r"k=\frac{\text{known side of second}}{\text{matching side of first}}",
     "steps": ["Match corresponding sides: smallest with smallest, largest with largest.", "Find the scale factor $k$ once.", "Multiply every side or the perimeter by $k$."],
     "why": "Similarity stretches all lengths by the same factor.",
     "example": {"q": "A triangle with sides 3 cm, 4 cm and 5 cm is similar to a bigger triangle whose hypotenuse is 20 cm. Find the bigger perimeter.",
                 "steps": [r"$k=\dfrac{20}{5}=4$.", r"Sides become $12$, $16$, $20$.", r"Perimeter $=12+16+20=48$ cm."],
                 "answer": "48 cm"}},
]

# ================= geo-pythagoras =================
py_concept = (
    "In a right triangle, the square of the longest side (the **hypotenuse**) equals the sum of squares of the other two sides: $h^2=p^2+b^2$. "
    "Learn the triplet families: $(3,4,5)$, $(5,12,13)$, $(7,24,25)$, $(8,15,17)$, $(9,40,41)$ and their multiples. "
    "The test also works backwards: if $a^2+b^2=c^2$ holds, the triangle is right-angled. "
    "The median to the hypotenuse equals half of it."
)

py_notes = r"""### The rule and where it hides
In a right triangle with right angle at $C$:
$$a^2+b^2=c^2$$
$c$ is the **hypotenuse**: the side opposite the right angle, always the longest.

Every ladder, pole-and-wire or walk-north-then-east question is this equation with a story wrapped around it. Draw the right triangle first. Label the hypotenuse before anything else. A 17 m ladder with its foot 8 m from a wall reaches $\sqrt{17^2-8^2}=\sqrt{225}=15$ m up. Same rule, story skin only.

> **Rule:** The hypotenuse is opposite the right angle. Ladder, wire and shortest-path lengths are hypotenuses.

### Learn the triplet families
| Family | Multiples you will meet |
|---|---|
| 3-4-5 | 6-8-10, 9-12-15, 12-16-20, 15-20-25 |
| 5-12-13 | 10-24-26, 15-36-39, 25-60-65 |
| 7-24-25 | 14-48-50 |
| 8-15-17 | 16-30-34 |
| 9-40-41, 12-35-37, 20-21-29 | as they are |

See two sides, recall the third. Hypotenuse 26 with one side 10 is 10-24-26 ($5$-$12$-$13$ times 2). Diagonal 65 with one side 25 gives 60 instantly. Two sides 20 and 21? That is 20-21-29, straight from the table.

> **Tip:** Check the leg ratios $3:4$, $5:12$, $8:15$, $7:24$ first. Exam numbers come from these families.

### Missing side: add or subtract?
- Missing **leg**: subtract. $\text{leg}=\sqrt{h^2-a^2}$.
- Missing **hypotenuse**: add. $h=\sqrt{a^2+b^2}$.

Legs $9$ and $12$: $h=\sqrt{81+144}=\sqrt{225}=15$, the 3-4-5 family times 3. Hypotenuse $25$ with leg $7$: other leg $=\sqrt{625-49}=24$.

> **Watch:** Writing $\sqrt{h^2+a^2}$ for a missing leg is the most common rush error. Subtract for legs, add for the hypotenuse.

### Is the triangle right-angled?
The rule works both ways. Square the two shorter sides, add, and compare with the square of the longest:
- equal: right-angled
- sum smaller ($6,8,11$: $100<121$): obtuse
- sum larger ($6,8,9$: $100>81$): acute

One comparison answers the whole question. For $6,8,11$: $36+64=100$ against $121$, so obtuse. For $6,8,9$: $100>81$, so acute.

### Two free results
- **Median to the hypotenuse** $=\dfrac{c}{2}$. Hypotenuse $13$ gives median $6.5$.
- **Diagonals**: rectangle $l\times b$ has diagonal $\sqrt{l^2+b^2}$; a square of side $a$ has diagonal $a\sqrt2$. A square of side $5$ has diagonal $5\sqrt2$. A rope from the top of a 12 m pole to a point 5 m out is the 5-12-13 hypotenuse, 13 m.

Special right triangles: 45-45-90 has sides $x$, $x$, $x\sqrt2$; 30-60-90 has $x$, $x\sqrt3$, $2x$.

> **Example:** Diagonal 65, one side 25: other side $=\sqrt{4225-625}=\sqrt{3600}=60$. The 5-12-13 family, times 5.
"""

py_formulas = [
    {"name": "Pythagoras", "tex": r"h^2=p^2+b^2", "note": "h = hypotenuse (longest side, opposite the right angle)."},
    {"name": "Missing leg", "tex": r"p=\sqrt{h^2-b^2}", "note": "Subtract when a leg is missing."},
    {"name": "Median to hypotenuse", "tex": r"m=\dfrac{h}{2}", "note": "The median drawn from the right-angle corner."},
    {"name": "Rectangle diagonal", "tex": r"d=\sqrt{l^2+b^2}", "note": "The corner angles of a rectangle are right angles."},
    {"name": "Triangle type test", "tex": r"a^2\lessgtr b^2+c^2", "note": "a = longest side; equal means right, greater means obtuse, smaller means acute."},
]

py_tricks = [
    {
        "title": "See two numbers, recall the third",
        "body": "12 with 13 gives 5. 24 with 25 gives 7. 15 with 17 gives 8. Multiples scale: 10-24-26 is 5-12-13 times 2.",
        "example": {
            "q": "A 25 m ladder stands with its foot 7 m from a wall. How high up the wall does it reach?",
            "steps": [r"7-24-25 triplet.", r"Ladder 25 and foot 7 are given.", r"Height $=24$ m."],
            "answer": "24 m",
        },
    },
    {
        "title": "Median to the hypotenuse is half of it",
        "body": "In any right triangle, the median from the right angle equals half the hypotenuse.",
        "example": {
            "q": "In a right triangle with hypotenuse 13 cm, find the median to the hypotenuse.",
            "steps": [r"$m=\dfrac{13}{2}$.", r"$m=6.5$ cm."],
            "answer": "6.5 cm",
        },
    },
    {
        "title": "Classify: square the longest side only",
        "body": "To name the triangle type, compare the longest side's square with the sum of the other two squares.",
        "example": {
            "q": "Which of these is right-angled: (i) 6, 8, 11 (ii) 6, 8, 10 (iii) 6, 8, 9?",
            "steps": [r"$6^2+8^2=100$ for all three.", r"(ii) $10^2=100$: right-angled.", r"(i) $121>100$ obtuse; (iii) $81<100$ acute."],
            "answer": "(ii) 6, 8, 10",
        },
    },
]

py_mistakes = [
    {"wrong": "Adding squares when a leg is missing.", "right": "A missing leg subtracts: $\\sqrt{h^2-a^2}$. Only the hypotenuse adds."},
    {"wrong": "Treating a leg as the hypotenuse because it looks longest.", "right": "The hypotenuse is opposite the right angle. Check the angle, not the drawing."},
    {"wrong": "Calling any near-triplet right-angled without checking.", "right": "Test $a^2+b^2=c^2$ on the squares. 6, 8, 11 fails ($100\\ne121$)."},
    {"wrong": "Confusing the median to the hypotenuse with half a leg.", "right": "Half the hypotenuse, always. The right-angle corner is what matters."},
    {"wrong": "Using $a\\sqrt2$ for a rectangle diagonal.", "right": "$a\\sqrt2$ is only for squares. Rectangles need $\\sqrt{l^2+b^2}$."},
]

py_revision = [
    "$h^2=p^2+b^2$; the hypotenuse is opposite the right angle.",
    "Triplets: 3-4-5, 5-12-13, 7-24-25, 8-15-17, 9-40-41 and multiples. Spot, don't compute.",
    "Missing leg: subtract squares. Missing hypotenuse: add squares.",
    "Converse: equal squares means right; longer longest side means obtuse; shorter means acute.",
    "Median to the hypotenuse $=$ half the hypotenuse.",
    "Rectangle diagonal $\\sqrt{l^2+b^2}$; square diagonal $a\\sqrt2$.",
]

py_patterns = [
    {"id": "geo-py-p1", "name": "Ladder and two-leg stories", "frequency": "very common",
     "howToSpot": "A ladder against a wall, a wire on a pole, walking north then east: a right-triangle story with one side missing.",
     "formula": r"a^2+b^2=c^2",
     "steps": ["Draw the right triangle. The ladder, wire or return path is the hypotenuse.", "Mark the two known sides.", "Subtract for a missing leg, add for a missing hypotenuse.", "Check the answer against a triplet family."],
     "why": "Every story is the same equation; only the names of the sides change.",
     "example": {"q": "A 17 m ladder leans against a wall with its foot 8 m from the base. How high up the wall does it reach?",
                 "steps": [r"Height $=\sqrt{17^2-8^2}$.", r"$=\sqrt{289-64}=\sqrt{225}$.", r"$=15$ m (the 8-15-17 family)."],
                 "answer": "15 m"}},
    {"id": "geo-py-p2", "name": "Classify the triangle", "frequency": "common",
     "howToSpot": "Three sides given; the triangle must be named right-angled, obtuse or acute.",
     "formula": r"a^2+b^2\lessgtr c^2",
     "steps": ["Square the two shorter sides and add.", "Compare with the square of the longest side.", "Equal means right, smaller sum means obtuse, larger means acute."],
     "why": "The rule works both ways, so the comparison classifies the biggest angle.",
     "example": {"q": "What type of triangle has sides 9 cm, 12 cm and 15 cm?",
                 "steps": [r"$9^2+12^2=81+144=225$.", r"$15^2=225$.", r"Equal, so it is right-angled (3-4-5 times 3)."],
                 "answer": "Right-angled"}},
    {"id": "geo-py-p3", "name": "Median to the hypotenuse", "frequency": "common",
     "howToSpot": "A median from the right angle (or to the hypotenuse) appears; its length or the hypotenuse is asked.",
     "formula": r"m=\dfrac{c}{2}",
     "steps": ["Confirm it is a right triangle and the median ends on the hypotenuse.", "Median $=$ half the hypotenuse.", "Double the median if the hypotenuse is asked."],
     "why": "The right-angle corner sits on the circle whose diameter is the hypotenuse, so the midpoint is equidistant from all three corners.",
     "example": {"q": "In a right triangle, the median to the hypotenuse is 6.5 cm. Find the hypotenuse.",
                 "steps": [r"$c=2\times6.5$.", r"$c=13$ cm."],
                 "answer": "13 cm"}},
    {"id": "geo-py-p4", "name": "Rectangle and square diagonals", "frequency": "very common",
     "howToSpot": "A diagonal of a rectangle, field or room with one dimension missing, or a square's side from its diagonal.",
     "formula": r"d=\sqrt{l^2+b^2},\quad a=\dfrac{d}{\sqrt2}",
     "steps": ["The diagonal splits the rectangle into two right triangles.", "Missing side $=\\sqrt{d^2-\\text{known}^2}$.", "For a square, side $=\\dfrac{d}{\\sqrt2}$."],
     "why": "Every corner of a rectangle is a right angle, so the diagonal is a hypotenuse.",
     "example": {"q": "The diagonal of a rectangular field is 65 m and one side is 25 m. Find the other side.",
                 "steps": [r"$\sqrt{65^2-25^2}$.", r"$=\sqrt{4225-625}=\sqrt{3600}$.", r"$=60$ m (25-60-65 is 5-12-13 times 5)."],
                 "answer": "60 m"}},
    {"id": "geo-py-p5", "name": "Triplet families in disguise", "frequency": "common",
     "howToSpot": "Legs in a ratio like $3:4$ or $5:12$ with the hypotenuse given, or hypotenuse plus one leg with perimeter or area asked.",
     "formula": r"(3k,\ 4k,\ 5k)",
     "steps": ["Spot the family in the ratio or the given pair.", "Find the multiplier $k$.", "Write all three sides.", "Answer what is asked: perimeter, area or the missing side."],
     "why": "Exam numbers come from these families, so recognition replaces calculation.",
     "example": {"q": "The legs of a right triangle are in the ratio $3:4$ and the hypotenuse is 20 cm. Find its perimeter.",
                 "steps": [r"Legs $3k$, $4k$, so hypotenuse $5k$.", r"$5k=20$, so $k=4$.", r"Sides $12$, $16$, $20$: perimeter $=48$ cm."],
                 "answer": "48 cm"}},
]

# ================= geo-quad-poly =================
qp_concept = (
    "The four angles of any quadrilateral add to $360^\\circ$. Key areas: parallelogram $=b\\times h$, rhombus $=\\dfrac{1}{2}d_1d_2$, trapezium $=\\dfrac{1}{2}(a+b)h$. "
    "In a **cyclic** quadrilateral (all four corners on one circle) opposite angles add to $180^\\circ$. "
    "A regular polygon with $n$ sides has exterior angle $\\dfrac{360^\\circ}{n}$, interior angle $180^\\circ$ minus that, and $\\dfrac{n(n-3)}{2}$ diagonals."
)

qp_notes = r"""### The parallelogram family
- **Parallelogram**: opposite sides parallel and equal; opposite angles equal; **adjacent angles add to $180^\circ$**.
- **Rectangle**: parallelogram with all angles $90^\circ$; equal diagonals that bisect each other.
- **Rhombus**: parallelogram with all sides equal; diagonals cross at $90^\circ$ and bisect each other.
- **Square**: rectangle and rhombus together; diagonal $=a\sqrt2$.
- **Trapezium**: exactly one pair of parallel sides, $a$ and $b$; an isosceles trapezium also has equal slanted sides and equal base angles.

A rectangle $8\times6$ has diagonal $10$ and area $48$. Every claim above turns into a one-line sum like that.

> **Rule:** In a parallelogram, ratio questions on adjacent angles are just co-interior angles: the parts add to $180^\circ$.

### Rhombus: work with half-diagonals
The diagonals of a rhombus cut each other in half at right angles. So the halves and one side form a right triangle:
$$\text{side}=\sqrt{\left(\frac{d_1}{2}\right)^2+\left(\frac{d_2}{2}\right)^2}$$

Diagonals 10 and 24: halves 5 and 12, side 13, perimeter 52. Area $=\dfrac{1}{2}d_1d_2=\dfrac{1}{2}\times10\times24=120$.

> **Tip:** Halves of diagonals are almost always a triplet: (5,12,13), (8,6,10), (12,35,37).

### Angles: parallelogram and cyclic quadrilateral
Adjacent angles of a parallelogram add to $180^\circ$. Ratio $1:3$ gives $\dfrac{1}{4}\times180^\circ=45^\circ$ and $135^\circ$.

A **cyclic quadrilateral** has all four corners on one circle. Its opposite angles add to $180^\circ$.
Angles in ratio $2:3:4:3$: opposite parts must match, $2+4=3+3=6$. So $k=30^\circ$ and the angles are $60^\circ, 90^\circ, 120^\circ, 90^\circ$.

The exterior angle of a cyclic quadrilateral equals the interior angle at the opposite corner.

### Regular polygons: everything from n
For $n$ equal sides:
- each exterior angle $=\dfrac{360^\circ}{n}$
- each interior angle $=180^\circ-$ exterior
- interior angle sum $=(n-2)\times180^\circ$
- diagonals $=\dfrac{n(n-3)}{2}$

Interior angle $150^\circ$ means exterior $30^\circ$, so $n=\dfrac{360}{30}=12$. A decagon has $\dfrac{10\times7}{2}=35$ diagonals. A pentagon: exterior $72^\circ$, interior $108^\circ$, diagonals $\dfrac{5\times2}{2}=5$.

> **Tip:** Travel through the exterior angle. It is the fastest bridge: interior $\to$ exterior $\to$ $n$.

### Trapezium
$$K=\frac{1}{2}(a+b)h$$
Parallel sides 13 and 17 with area 105: $h=\dfrac{2\times105}{30}=7$.

The segment joining the midpoints of the two slanted sides (the midsegment) $=\dfrac{a+b}{2}=\dfrac{13+17}{2}=15$. No height needed.
"""

qp_formulas = [
    {"name": "Quadrilateral angle sum", "tex": r"A+B+C+D=360^\circ", "note": "Any four-sided figure."},
    {"name": "Parallelogram angles", "tex": r"A+B=180^\circ,\quad A=C", "note": "Adjacent angles supplement; opposite angles equal."},
    {"name": "Cyclic quadrilateral", "tex": r"A+C=180^\circ,\quad B+D=180^\circ", "note": "Opposite corners on one circle."},
    {"name": "Rhombus", "tex": r"K=\frac{1}{2}d_1d_2,\quad a=\sqrt{\left(\frac{d_1}{2}\right)^2+\left(\frac{d_2}{2}\right)^2}", "note": "d1, d2 = diagonals; they cross at right angles."},
    {"name": "Trapezium", "tex": r"K=\frac{1}{2}(a+b)h", "note": "a and b are the two parallel sides; h is the gap between them."},
    {"name": "Parallelogram", "tex": r"K=bh", "note": "Height is measured perpendicular to the base."},
    {"name": "Regular polygon", "tex": r"\text{ext}=\frac{360^\circ}{n},\quad \text{int}=180^\circ-\text{ext},\quad \text{diagonals}=\frac{n(n-3)}{2}", "note": "n = number of sides."},
]

qp_tricks = [
    {
        "title": "Exterior angle to number of sides",
        "body": "Exterior angle $=180^\\circ-$ interior, and $n=\\dfrac{360^\\circ}{\\text{exterior}}$.",
        "example": {
            "q": "The interior angle of a regular polygon is $156^\\circ$. How many sides does it have?",
            "steps": [r"Exterior $=180-156=24^\circ$.", r"$n=\dfrac{360}{24}$.", r"$n=15$."],
            "answer": "15 sides",
        },
    },
    {
        "title": "Rhombus side from half-diagonals",
        "body": "Halve both diagonals. They are the legs of a right triangle whose hypotenuse is the side.",
        "example": {
            "q": "The diagonals of a rhombus are 16 cm and 12 cm. Find its side and area.",
            "steps": [r"Halves: $8$ and $6$.", r"Side $=\sqrt{64+36}=10$ cm.", r"Area $=\dfrac{1}{2}\times16\times12=96$ sq cm."],
            "answer": "Side 10 cm, area 96 sq cm",
        },
    },
    {
        "title": "Count diagonals in one line",
        "body": "Each of the $n$ corners joins $n-3$ others, and every diagonal is counted twice, giving $\\dfrac{n(n-3)}{2}$.",
        "example": {
            "q": "How many diagonals does a decagon have?",
            "steps": [r"$\dfrac{10\times(10-3)}{2}$.", r"$=\dfrac{70}{2}$.", r"$=35$."],
            "answer": "35",
        },
    },
]

qp_mistakes = [
    {"wrong": "Using $\\dfrac{1}{2}d_1d_2$ for a rectangle or parallelogram.", "right": "That area formula is for a rhombus (or a kite with perpendicular diagonals)."},
    {"wrong": "Adding two neighbouring angles of a cyclic quadrilateral to $180^\\circ$.", "right": "Opposite corners add to $180^\\circ$. Neighbours add to whatever is left of $360^\\circ$."},
    {"wrong": "Using $(n-2)\\times180^\\circ$ as one interior angle.", "right": "That is the whole sum. Divide by $n$ for one angle of a regular polygon."},
    {"wrong": "Forgetting the half in $\\dfrac{1}{2}(a+b)h$ for a trapezium.", "right": "Average the parallel sides first, then multiply by the height."},
    {"wrong": "Using full diagonals as legs of the rhombus right triangle.", "right": "Halve both diagonals first. The side is the hypotenuse of the halves."},
]

qp_revision = [
    "Quadrilateral angles total $360^\\circ$; parallelogram adjacent angles total $180^\\circ$.",
    "Cyclic quadrilateral: opposite angles total $180^\\circ$.",
    "Rhombus: side $=\\sqrt{(d_1/2)^2+(d_2/2)^2}$, area $=\\dfrac{1}{2}d_1d_2$.",
    "Trapezium: area $\\dfrac{1}{2}(a+b)h$; midsegment $\\dfrac{a+b}{2}$.",
    "Regular polygon: ext $=\\dfrac{360^\\circ}{n}$, int $=180^\\circ-$ ext, sum $(n-2)\\times180^\\circ$.",
    "Diagonals $=\\dfrac{n(n-3)}{2}$.",
]

qp_patterns = [
    {"id": "geo-qp-p1", "name": "Regular polygon: angle to number of sides", "frequency": "very common",
     "howToSpot": "An interior or exterior angle, an angle sum, or a diagonal count is given; find $n$ or another angle.",
     "formula": r"\text{ext}=\frac{360^\circ}{n},\quad \text{int}=180^\circ-\text{ext},\quad d=\frac{n(n-3)}{2}",
     "steps": ["Turn the interior angle into the exterior one: $180^\\circ-$ interior.", "Divide $360^\\circ$ by the exterior angle to get $n$.", "From a sum: $n=\\dfrac{\\text{sum}}{180^\\circ}+2$. From diagonals: solve $n(n-3)=2d$."],
     "why": "All these quantities are fixed by $n$, and the exterior angle is the quickest link between them.",
     "example": {"q": "Each interior angle of a regular polygon is $150^\\circ$. How many sides does it have?",
                 "steps": [r"Exterior $=180-150=30^\circ$.", r"$n=\dfrac{360}{30}$.", r"$n=12$."],
                 "answer": "12"}},
    {"id": "geo-qp-p2", "name": "Rhombus from its diagonals", "frequency": "very common",
     "howToSpot": "Diagonals of a rhombus given (or area with one diagonal); side, perimeter or the other diagonal asked.",
     "formula": r"a=\sqrt{\left(\frac{d_1}{2}\right)^2+\left(\frac{d_2}{2}\right)^2},\quad K=\frac{d_1d_2}{2}",
     "steps": ["Halve both diagonals.", "Side $=$ hypotenuse of the halves (spot the triplet).", "Perimeter $=4\\times$ side; area $=\\dfrac{1}{2}d_1d_2$.", "Given area and one diagonal: $d_2=\\dfrac{2K}{d_1}$ first."],
     "why": "Rhombus diagonals cross at right angles and bisect each other, so the halves make a right triangle.",
     "example": {"q": "The diagonals of a rhombus are 10 cm and 24 cm. Find its perimeter.",
                 "steps": [r"Halves: $5$ and $12$.", r"Side $=\sqrt{25+144}=13$.", r"Perimeter $=4\times13=52$ cm."],
                 "answer": "52 cm"}},
    {"id": "geo-qp-p3", "name": "Parallelogram angles", "frequency": "very common",
     "howToSpot": "Adjacent angles of a parallelogram given as a ratio or as $\\angle A=k\\angle B$; one angle asked.",
     "formula": r"\angle A+\angle B=180^\circ",
     "steps": ["Add the ratio parts to $180^\\circ$.", "Scale each part to get the two angles.", "Opposite angles repeat; check which letter is asked."],
     "why": "The parallel sides make each adjacent pair co-interior, so they supplement.",
     "example": {"q": "Two adjacent angles of a parallelogram are in the ratio $1:3$. Find the larger angle.",
                 "steps": [r"Parts $1+3=4$ share $180^\circ$.", r"Larger $=\dfrac{3}{4}\times180^\circ$.", r"$=135^\circ$."],
                 "answer": "135°"}},
    {"id": "geo-qp-p4", "name": "Cyclic quadrilateral opposite angles", "frequency": "common",
     "howToSpot": "Four corners on a circle; one angle or an angle ratio given, a missing angle asked.",
     "formula": r"\angle A+\angle C=180^\circ",
     "steps": ["Find the corner opposite the given one.", "Subtract the given angle from $180^\\circ$.", "In ratio questions, check which parts sit opposite each other; each pair totals $180^\\circ$."],
     "why": "Opposite corners of a cyclic quadrilateral split the circle's arc between them, so their angles supplement.",
     "example": {"q": "In a cyclic quadrilateral $ABCD$, $\\angle A=70^\\circ$. Find $\\angle C$.",
                 "steps": [r"$A$ and $C$ are opposite.", r"$\angle C=180^\circ-70^\circ$.", r"$=110^\circ$."],
                 "answer": "110°"}},
    {"id": "geo-qp-p5", "name": "Trapezium area and midsegment", "frequency": "common",
     "howToSpot": "Parallel sides with height or area given; area, height or midsegment asked.",
     "formula": r"K=\frac{1}{2}(a+b)h,\quad m=\frac{a+b}{2}",
     "steps": ["Average the two parallel sides.", "Multiply by the height for the area.", "Height from area: $h=\\dfrac{2K}{a+b}$.", "Midsegment $=$ the average, no height needed."],
     "why": "A trapezium is its average width times its height.",
     "example": {"q": "A trapezium has parallel sides 13 cm and 17 cm and area 105 sq cm. Find its height.",
                 "steps": [r"$h=\dfrac{2\times105}{13+17}$.", r"$=\dfrac{210}{30}$.", r"$=7$ cm."],
                 "answer": "7 cm"}},
]

# ================= geo-circles =================
ci_concept = (
    "A line from the centre perpendicular to a chord cuts the chord in half. So half-chord, distance from centre and radius form a right triangle. "
    "The angle a chord makes at the centre is twice the angle it makes at the circle. "
    "A tangent meets the radius at $90^\\circ$, and the two tangents from one outside point are equal. "
  "Two circles can share 4, 3, 2, 1 or 0 common tangents, decided by how they sit."
)

ci_notes = r"""### Chord, distance, radius
Drop a perpendicular from the centre to a chord. It lands at the chord's midpoint. So:
$$\left(\frac{c}{2}\right)^2+d^2=r^2$$
$c$ = chord, $d$ = its distance from the centre, $r$ = radius.

Radius 15, chord 9 from the centre: half-chord $=\sqrt{225-81}=\sqrt{144}=12$, chord $=24$.

> **Rule:** Two of the three $(c/2,\ d,\ r)$ always give the third. Circle questions reuse the same Pythagorean triplets.

Equal chords sit at equal distances from the centre. Longer chords sit closer to the centre. Diameter 10 with chord 8: half-chord $4$, distance $\sqrt{25-16}=3$. The triplet 3-4-5 again.

### Angles in a circle
- Angle at the centre $=$ twice the angle at the circle on the same arc: $\angle BOC=2\angle BAC$.
- Angles in the **same segment** (standing on the same arc) are equal.
- An angle in a **semicircle** (diameter as one side) is $90^\circ$.

$\angle BOC=120^\circ$ gives $\angle BAC=60^\circ$ instantly.

> **Tip:** When a chord and a circle-angle appear together, double the circle-angle first. The centre angle tells you where the chord sits.

### Tangents from an outside point
- The tangent meets the radius at $90^\circ$ at the touch point.
- The two tangents from one outside point are equal in length.
- Tangent length from distance $d$ of the point and radius $r$: $\sqrt{d^2-r^2}$.

Point 13 cm from the centre, radius 5: tangent $=\sqrt{169-25}=12$ cm. The line joining the point to the centre also bisects the angle between the two tangents.

### Power of a point
Two one-line rules for secants and chords:
- **Tangent + secant** from one outside point: $(\text{tangent})^2=\text{outside part}\times\text{whole secant}$.
- **Two chords crossing inside**: the products of their pieces are equal, $a\times b=c\times d$. Pieces 4 and 6 crossing pieces 2 and 12: $4\times6=2\times12=24$.

Tangent 10 with a 5 cm outside secant part: whole secant $=\dfrac{100}{5}=20$, so the inside part is 15.

> **Watch:** 'Whole secant' means outside part plus inside part. Using only the inside part is the classic error.

### How many common tangents?
Two circles, radii $r_1>r_2$, centres $d$ apart:

| Position | Tangents |
|---|---|
| Apart ($d>r_1+r_2$) | 4 |
| Touching outside ($d=r_1+r_2$) | 3 |
| Overlapping | 2 |
| Touching inside ($d=r_1-r_2$) | 1 |
| One inside the other | 0 |

Radii 6 and 2, centres 4 apart: $4=6-2$, touching inside, exactly **1** tangent.

> **Tip:** Compare $d$ with $r_1+r_2$ and $r_1-r_2$. The countdown 4-3-2-1-0 follows the two checks.
"""

ci_formulas = [
    {"name": "Chord from distance", "tex": r"\ell=2\sqrt{r^2-d^2}", "note": "d = distance from centre to chord."},
    {"name": "Equal chords", "tex": r"\ell_1=\ell_2\Rightarrow d_1=d_2", "note": "Equal chords sit equally far from the centre."},
    {"name": "Centre vs circumference angle", "tex": r"\angle BOC=2\angle BAC", "note": "Both angles stand on chord BC."},
    {"name": "Tangent length", "tex": r"PT=\sqrt{d^2-r^2}", "note": "P is d from the centre of a circle of radius r."},
    {"name": "Tangent-secant", "tex": r"PT^2=PA\cdot PB", "note": "Tangent squared = outside part times whole secant."},
    {"name": "Intersecting chords", "tex": r"PA\cdot PB=PC\cdot PD", "note": "Two chords crossing inside the circle."},
    {"name": "Alternate segment", "tex": r"\angle(\text{tangent},\ \text{chord})=\angle\text{ in alternate segment}", "note": "The angle between a tangent and a chord equals the angle the chord makes on the far side."},
    {"name": "Common tangents (transverse / direct)", "tex": r"L_T=\sqrt{d^2-(r_1+r_2)^2},\quad L_D=\sqrt{d^2-(r_1-r_2)^2}", "note": "d = distance between centres."},
]

ci_tricks = [
    {
        "title": "The triplet inside the circle",
        "body": "Radius, distance and half-chord are the sides of a right triangle. Radius 13 and distance 5 give half-chord 12.",
        "example": {
            "q": "A chord is 5 cm from the centre of a circle of radius 13 cm. Find the chord.",
            "steps": [r"Half-chord $=\sqrt{13^2-5^2}$.", r"$=\sqrt{169-25}=\sqrt{144}=12$.", r"Chord $=2\times12=24$ cm."],
            "answer": "24 cm",
        },
    },
    {
        "title": "Tangent-secant: multiply the pieces",
        "body": "Tangent squared equals outside part times the whole secant. Whole = outside + inside.",
        "example": {
            "q": "From P, a tangent of 6 cm and a secant with a 4 cm outside part are drawn. Find the inside (chord) part.",
            "steps": [r"$6^2=4\times$ whole.", r"Whole $=\dfrac{36}{4}=9$.", r"Inside part $=9-4=5$ cm."],
            "answer": "5 cm",
        },
    },
    {
        "title": "Count common tangents from d",
        "body": "Compare the centre distance with $r_1+r_2$ and $r_1-r_2$ and read off 4, 3, 2, 1 or 0.",
        "example": {
            "q": "Two circles of radii 4 cm and 9 cm have centres 13 cm apart. How many common tangents?",
            "steps": [r"$r_1+r_2=13$.", r"$d=13=r_1+r_2$: touching outside.", r"3 common tangents."],
            "answer": "3",
        },
    },
    {
        "title": "Chord of the outer circle touching the inner one",
        "body": "Concentric circles: a chord of the big circle that just touches the small one is $2\\sqrt{R^2-r^2}$. The small radius is its distance from the centre.",
        "example": {
            "q": "Two concentric circles have radii 25 cm and 7 cm. Find the chord of the larger that touches the smaller.",
            "steps": [r"Half-chord $=\sqrt{25^2-7^2}$.", r"$=\sqrt{625-49}=\sqrt{576}=24$.", r"Chord $=48$ cm."],
            "answer": "48 cm",
        },
    },
]

ci_mistakes = [
    {"wrong": "Forgetting to double: $\\sqrt{r^2-d^2}$ is only half the chord.", "right": "Multiply by 2 for the full chord length."},
    {"wrong": "Using the inside part instead of the whole secant.", "right": "Whole secant $=$ outside part $+$ inside part. Then divide the tangent square by it."},
    {"wrong": "Mixing up $d=r_1+r_2$ and $d=r_1-r_2$ when counting tangents.", "right": "Sum means touching outside (3 tangents); difference means touching inside (1)."},
    {"wrong": "Doubling an angle at the circumference that already sits at the centre.", "right": "Centre angles are the big ones. Only the circumference angle doubles to give it."},
    {"wrong": "Treating the angle in the same segment as the alternate segment angle.", "right": "Same segment $=$ equal angles on one arc. Alternate segment pairs a tangent with the far arc."},
]

ci_revision = [
    "$\\left(\\dfrac{c}{2}\\right)^2+d^2=r^2$: the perpendicular from the centre halves the chord.",
    "$\\angle BOC=2\\angle BAC$; same-segment angles equal; semicircle angle $90^\\circ$.",
    "Tangent $\\perp$ radius; two tangents from one point are equal; length $\\sqrt{d^2-r^2}$.",
    "Tangent$^2$ $=$ outside $\\times$ whole secant; crossing chords: $ab=cd$.",
    "Common tangents: apart 4, touch outside 3, overlap 2, touch inside 1, inside 0.",
    "Alternate segment: tangent-chord angle equals the angle on the far arc.",
]

ci_patterns = [
    {"id": "geo-ci-p1", "name": "Chord, distance, radius triangle", "frequency": "very common",
     "howToSpot": "A chord's length, the radius, or its distance from the centre is missing.",
     "formula": r"\left(\frac{c}{2}\right)^2+d^2=r^2",
     "steps": ["Halve the chord: the centre line hits its midpoint.", "Write the right triangle: half-chord and distance as legs, radius as hypotenuse.", "Solve for the missing one.", "Check for a triplet in the halves."],
     "why": "The perpendicular from the centre bisects the chord, so Pythagoras finishes it.",
     "example": {"q": "A circle of radius 15 cm has a chord 9 cm from the centre. Find the chord's length.",
                 "steps": [r"Half-chord $=\sqrt{15^2-9^2}$.", r"$=\sqrt{225-81}=\sqrt{144}=12$.", r"Chord $=24$ cm (9-12-15)."],
                 "answer": "24 cm"}},
    {"id": "geo-ci-p2", "name": "Tangent-secant and crossing chords", "frequency": "common",
     "howToSpot": "A tangent and a secant from one outside point, or two chords crossing inside, with piece lengths to find.",
     "formula": r"t^2=a(a+b),\quad ab=cd",
     "steps": ["Square the tangent.", "Divide by the outside part to get the whole secant.", "Subtract the outside part for the inside piece.", "For crossing chords: set the two products equal."],
     "why": "Along any line through the point, the product of the two stretches to the circle is the same.",
     "example": {"q": "From an outside point P, a tangent of 10 cm and a secant with a 5 cm outside part are drawn. Find the whole secant.",
                 "steps": [r"$10^2=5\times$ whole.", r"Whole $=\dfrac{100}{5}$.", r"$=20$ cm (inside part 15 cm)."],
                 "answer": "20 cm"}},
    {"id": "geo-ci-p3", "name": "Counting common tangents", "frequency": "common",
     "howToSpot": "Two circles with given radii and centre distance; 'how many common tangents?'",
     "formula": r"d\gtrless r_1+r_2,\quad d\gtrless r_1-r_2",
     "steps": ["Compare $d$ with $r_1+r_2$.", "Compare $d$ with $r_1-r_2$.", "Read the count: apart 4, touch outside 3, overlap 2, touch inside 1, nested 0."],
     "why": "Each way the circles touch removes one tangent from the maximum of four.",
     "example": {"q": "Two circles of radii 6 cm and 2 cm have centres 4 cm apart. How many common tangents do they have?",
                 "steps": [r"$r_1-r_2=6-2=4$.", r"$d=4=r_1-r_2$: touching inside.", r"Exactly 1 common tangent."],
                 "answer": "1"}},
    {"id": "geo-ci-p4", "name": "Centre angle vs circle angle", "frequency": "very common",
     "howToSpot": "O is the centre; an angle at the centre or at the circle on the same arc is given; the other is asked.",
     "formula": r"\angle BOC=2\angle BAC",
     "steps": ["Check both angles stand on the same chord or arc.", "Halve the centre angle for the circle angle, or double the circle angle.", "Use $90^\\circ$ at once if one side is a diameter."],
     "why": "The centre angle takes the whole arc; a circle angle takes half of it.",
     "example": {"q": "In a circle with centre O, $\\angle BOC=120^\\circ$ on arc BC. Find $\\angle BAC$ at the circle.",
                 "steps": [r"$\angle BAC=\dfrac{\angle BOC}{2}$.", r"$=\dfrac{120^\circ}{2}$.", r"$=60^\circ$."],
                 "answer": "60°"}},
    {"id": "geo-ci-p5", "name": "Tangent length from an outside point", "frequency": "very common",
     "howToSpot": "A point outside the circle with its distance from the centre (or a tangent and a radius) given; the tangent length is asked.",
     "formula": r"PT=\sqrt{d^2-r^2}",
     "steps": ["Note the distance $d$ of the point from the centre and the radius $r$.", "The radius to the touch point is perpendicular to the tangent.", "Tangent $=\\sqrt{d^2-r^2}$; check for a triplet."],
     "why": "Radius, tangent and the line to the centre form a right triangle with $d$ as hypotenuse.",
     "example": {"q": "P is 13 cm from the centre of a circle of radius 5 cm. Find the length of the tangent from P.",
                 "steps": [r"$PT=\sqrt{13^2-5^2}$.", r"$=\sqrt{169-25}=\sqrt{144}$.", r"$=12$ cm."],
                 "answer": "12 cm"}},
    {"id": "geo-ci-p6", "name": "Alternate segment theorem", "frequency": "occasional",
     "howToSpot": "A tangent touches the circle at one end of a chord; the angle between them is linked to an angle on the far arc.",
     "formula": r"\angle(\text{tangent},\text{chord})=\angle\text{in alternate segment}",
     "steps": ["Mark the angle between the tangent and the chord.", "Find the angle standing on the same chord from the far side.", "The two are equal; no computation needed."],
     "why": "Both angles hold half of the same arc, one through the tangent, one through the chord.",
     "example": {"q": "AT is a tangent at A, and AB is a chord. If $\\angle TAB=40^\\circ$, find $\\angle ACB$ where C is on the circle on the far side of AB from T.",
                 "steps": [r"$\\angle TAB$ is a tangent-chord angle at chord AB.", r"Alternate segment: it equals any angle on the far arc AB.", r"$\\angle ACB=40^\\circ$."],
                 "answer": "40°"}},
]

# ---------- patch ----------
data = json.loads(TOPIC.read_text(encoding="utf-8"))

blocks = {
    "geo-lines-angles": (la_concept, la_notes, la_formulas, la_tricks, la_mistakes, la_revision, la_patterns),
    "geo-triangles": (tr_concept, tr_notes, tr_formulas, tr_tricks, tr_mistakes, tr_revision, tr_patterns),
    "geo-similarity": (si_concept, si_notes, si_formulas, si_tricks, si_mistakes, si_revision, si_patterns),
    "geo-pythagoras": (py_concept, py_notes, py_formulas, py_tricks, py_mistakes, py_revision, py_patterns),
    "geo-quad-poly": (qp_concept, qp_notes, qp_formulas, qp_tricks, qp_mistakes, qp_revision, qp_patterns),
    "geo-circles": (ci_concept, ci_notes, ci_formulas, ci_tricks, ci_mistakes, ci_revision, ci_patterns),
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
print("geometry.json patched")
