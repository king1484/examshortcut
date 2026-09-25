"""Phase-2 deep content for quant/geometry — lines-angles, triangles, similarity."""
from fractions import Fraction as F

from _lib import Sub


# ---------------- geo-lines-angles ----------------

def build_lines():
    S = Sub("geo-lines-angles")

    S.notes = r"""### The angle family you must see instantly
An angle measures the turn between two rays. The two facts every question uses:
- **Complementary angles** add to $90^\circ$; **supplementary angles** add to $180^\circ$.
- If the supplement of an angle exceeds the angle by $d$, the angle is $\frac{180^\circ - d}{2}$. If the angle is $n$ times its complement, write $x = n(90^\circ - x)$ and solve — the unknown always cancels to one linear equation.

A useful fixed result: supplement $-$ complement $= (180^\circ - x) - (90^\circ - x) = 90^\circ$, always, whatever $x$ is. Questions test this fact directly, so keep it ready.

### Angles on a line and around a point
Angles on one straight line add to $180^\circ$; angles filling one full turn around a point add to $360^\circ$. When two straight lines cross, four angles appear — the **vertically opposite** pairs are equal, and any two neighbouring angles are supplementary. So if one of the four angles is $a$, the set is $a,\ 180-a,\ a,\ 180-a$. Given three angles around a point, the fourth is just the remainder after subtracting from $360^\circ$ — the whole subtopic is subtraction once the picture is right.

### Parallel lines cut by a transversal
A transversal is a line crossing two (parallel) lines. It creates 8 angles, but only 2 distinct values. Three name-tags describe the same two facts:
| Pair | Picture | Rule |
|---|---|---|
| Corresponding | F-shape, same corner | equal |
| Alternate | Z-shape, opposite sides | equal |
| Co-interior (allied) | C-shape, same side inside | add to $180^\circ$ |

So the exam question is really: *pick the correct relation, get one linear equation in $x$, solve, substitute back*. Two checks catch almost every slip: a co-interior pair must sum to exactly $180^\circ$, and a corresponding/alternate pair must be exactly equal.

### Reading the question, not just solving it
The classic lost mark: the question asks for the **angle** and the options include $x$ itself. After solving for $x$, re-read which angle was asked — the larger of the pair, the smaller, or an angle in a different position (a corresponding partner of a co-interior mate, say). Another common twist: a ratio like $2:3$ for co-interior angles — let them be $2k$ and $3k$ so that $5k = 180^\circ$.

### Bisectors
An angle **bisector** splits an angle into two equal halves. Two results get asked:
- If two supplementary angles are bisected, the halves differ by half the original difference.
- The bisectors of a pair of co-interior angles meet at $90^\circ$ — the halves sum to half of $180^\circ$, so the third angle of the triangle they form is exactly $90^\circ$.

### Quick revision
- Complement $= 90^\circ - x$; supplement $= 180^\circ - x$; their difference is always $90^\circ$.
- On a line $180^\circ$; around a point $360^\circ$; vertically opposite angles are equal.
- Parallel + transversal: corresponding = alternate; co-interior sums to $180^\circ$.
- Expressions in $x$: choose the relation first, solve the linear equation, then answer the angle actually asked.
- Supplement exceeds angle by $d$ $\Rightarrow$ angle $= \frac{180^\circ - d}{2}$.
- Bisectors of co-interior angles meet at $90^\circ$; bisecting halves any difference.
"""

    S.pattern("geo-la-p1", "Co-interior angles given as expressions in x", "very common",
        "Parallel lines with a transversal; two angles on the same side inside are $(ax+b)^\\circ$ and $(cx+d)^\\circ$ — find $x$ or one of the angles.",
        r"(ax+b) + (cx+d) = 180",
        r"""1. Co-interior (allied) angles between parallels add to $180^\circ$ — set the sum.
2. Solve the linear equation for $x$.
3. Substitute back into the angle asked; check the pair really sums to $180^\circ$.

Why: only the allied pair is supplementary — corresponding and alternate pairs are equal, not added.""",
        "Two co-interior angles between parallel lines are $(2x+30)^\\circ$ and $(x+15)^\\circ$. Find the larger angle.",
        r"$3x + 45 = 180 \Rightarrow x = 45$. Angles: $120^\circ$ and $60^\circ$ — larger $= 120^\circ$. Check: $120+60=180$.")
    S.pattern("geo-la-p2", "Corresponding or alternate angles set equal", "very common",
        "Angles in F-shape (corresponding) or Z-shape (alternate) positions are both given as expressions in $x$ — or one is given and its partner asked.",
        r"ax+b = cx+d \ \text{(equal pairs)}",
        r"""1. Identify the pair shape: F (corresponding) or Z (alternate) — both are EQUAL.
2. Equate the two expressions; solve for $x$.
3. Answer the angle asked; the other angle values follow from $180^\circ - $ the found angle.

Why: a transversal across parallels makes only two distinct angle values — an acute one $a$ and its supplement $180^\circ-a$.""",
        "Two corresponding angles between parallel lines are $(3x-10)^\\circ$ and $(2x+15)^\\circ$. Find the angle.",
        r"$3x-10 = 2x+15 \Rightarrow x = 25$; angle $= 3(25)-10 = 65^\circ$. (Its supplement is $115^\circ$. )")
    S.pattern("geo-la-p3", "Complement and supplement of an angle", "very common",
        "'Find the angle whose supplement is k times its complement', 'the complement of x°', or a difference between supplement and complement.",
        r"180 - x = n(90 - x)",
        r"""1. Write complement $= 90^\circ - x$, supplement $= 180^\circ - x$.
2. Translate the sentence into one equation and solve for $x$.
3. Remember supplement $-$ complement is always $90^\circ$ — use it as an instant check.

Why: both are defined from the same $x$, so every 'k times' statement is a linear equation.""",
        "The supplement of an angle is three times its complement. Find the angle.",
        r"$180 - x = 3(90 - x) \Rightarrow 180 - x = 270 - 3x \Rightarrow 2x = 90 \Rightarrow x = 45^\circ$. Check: supplement $135 = 3 \times 45$.")
    S.pattern("geo-la-p4", "Angles on a line, around a point, vertically opposite", "common",
        "Several angles at a point or on a line are given (some as expressions); the missing one is asked — or two crossing lines give one angle and ask the rest.",
        r"\text{on a line}=180^\circ,\quad \text{round a point}=360^\circ",
        r"""1. Decide the total: straight line $180^\circ$, full turn $360^\circ$.
2. Add the known/expression angles, equate to the total, solve.
3. For crossing lines: vertically opposite pairs are equal and neighbours are supplementary.

Why: turn totals are fixed, so the missing angle is just the remainder.""",
        "Two straight lines intersect. One of the four angles formed is $75^\\circ$. The obtuse angle among the remaining three is:",
        r"Neighbour angles are supplementary: $180 - 75 = 105^\circ$; the vertically opposite mate repeats $75^\circ$. Obtuse answer $= 105^\circ$.")
    S.pattern("geo-la-p5", "Angle bisectors in line configurations", "occasional",
        "An angle is bisected and the halves (or the angle between two bisectors) are asked, often inside a parallel-lines or triangle figure.",
        r"\text{bisected half} = \frac{\theta}{2}",
        r"""1. A bisector splits the angle into two equal parts — write each as $\frac{\theta}{2}$.
2. Carry the halves into the triangle/pair the figure forms.
3. Known bonus: bisectors of a co-interior pair meet at $90^\circ$.

Why: halving both of two angles that sum to $180^\circ$ leaves exactly $90^\circ$ for the triangle the bisectors form.""",
        "Two supplementary angles differ by $40^\\circ$. After both are bisected, what is the difference between the two bisected halves?",
        r"Halving scales every difference by $\frac12$: $\frac{40}{2} = 20^\circ$. (Angles $110^\circ, 70^\circ$ → halves $55^\circ, 35^\circ$ → gap $20^\circ$.)")

    # ---- practice ----
    assert 2 * 45 + 30 == 120 and 45 + 15 == 60 and 120 + 60 == 180
    S.q("geo-la-p1", "easy", "Two co-interior angles between parallel lines are $(2x+30)^\\circ$ and $(x+15)^\\circ$. The larger of the two angles is:",
        ["$120^\\circ$", "$60^\\circ$", "$135^\\circ$", "$150^\\circ$"], "$120^\\circ$",
        r"""Co-interior angles add to $180^\circ$: $2x+30+x+15=180 \Rightarrow 3x=135 \Rightarrow x=45$.

The angles are $120^\circ$ and $60^\circ$; the larger is $120^\circ$.""",
        r"$3x = 135 \Rightarrow x=45$; angle $= 2(45)+30 = 120^\circ$. Trap: $60^\circ$ (the smaller) or $45^\circ$ ($x$ itself).", 35)
    S.questions[-1]["figure"] = ('<svg viewBox="0 0 280 190" width="280" stroke="currentColor" fill="none">'
        '<line x1="30" y1="60" x2="250" y2="60"/><line x1="30" y1="140" x2="250" y2="140"/>'
        '<line x1="90" y1="20" x2="190" y2="180"/>'
        '<text x="176" y="52" dx="6" dy="-4" fill="currentColor" stroke="none" font-size="13" font-family="sans-serif">(2x+30)&#176;</text>'
        '<text x="196" y="132" dx="6" dy="12" fill="currentColor" stroke="none" font-size="13" font-family="sans-serif">(x+15)&#176;</text>'
        '</svg>')
    assert 5 * 25 - 40 == 85 and 3 * 25 + 20 == 95 and 85 + 95 == 180
    S.q("geo-la-p1", "medium", "Two parallel lines are cut by a transversal. If two co-interior angles are $(5x-40)^\\circ$ and $(3x+20)^\\circ$, the smaller angle is:",
        ["$95^\\circ$", "$85^\\circ$", "$75^\\circ$", "$105^\\circ$"], "$85^\\circ$",
        r"""$5x-40+3x+20=180 \Rightarrow 8x=200 \Rightarrow x=25$.

Angles: $5(25)-40=85^\circ$ and $3(25)+20=95^\circ$; the smaller is $85^\circ$.""",
        r"$8x=200 \Rightarrow x=25$; smaller angle uses the minus sign: $85^\circ$. Check $85+95=180$.", 40)
    assert F(72, 108) == F(2, 3) and 72 + 108 == 180
    S.q("geo-la-p1", "medium", "Two co-interior angles between parallel lines are in the ratio $2:3$. The difference between the two angles is:",
        ["$36^\\circ$", "$30^\\circ$", "$40^\\circ$", "$24^\\circ$"], "$36^\\circ$",
        r"""Let the angles be $2k$ and $3k$: $2k+3k=180 \Rightarrow k=36^\circ$.

Angles $72^\circ$ and $108^\circ$; difference $=36^\circ$.""",
        r"$5k=180 \Rightarrow k=36$; difference $= (3-2)k = 36^\circ$. Trap: $72^\circ$ (the smaller angle).", 40)
    assert 3 * 25 - 10 == 65 and 2 * 25 + 15 == 65
    S.q("geo-la-p2", "easy", "Two corresponding angles between parallel lines are $(3x-10)^\\circ$ and $(2x+15)^\\circ$. The value of each angle is:",
        ["$55^\\circ$", "$75^\\circ$", "$65^\\circ$", "$35^\\circ$"], "$65^\\circ$",
        r"""Corresponding angles are equal: $3x-10=2x+15 \Rightarrow x=25$.

Angle $=3(25)-10=65^\circ$ (and $2(25)+15=65^\circ$ ✓ ).""",
        r"$x=25$ from the equality; angle $65^\circ$. Trap: $115^\circ$ is its supplement.", 35)
    assert 4 * 20 + 5 == 85 and 5 * 20 - 15 == 85
    S.q("geo-la-p2", "medium", "Two alternate angles between parallel lines are $(4x+5)^\\circ$ and $(5x-15)^\\circ$. Find the value of $x$.",
        ["$15$", "$25$", "$20$", "$10$"], "$20$",
        r"""Alternate angles are equal: $4x+5=5x-15 \Rightarrow x=20$.

Each angle is $85^\circ$.""",
        r"$4x+5=5x-15$ → $x=20$ directly. Trap: adding them to $180^\circ$ — that is the co-interior rule, not this pair.", 35)
    assert 180 - 45 == 3 * (90 - 45)
    S.q("geo-la-p3", "easy", "The supplement of an angle is three times its complement. The angle is:",
        ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$75^\\circ$"], "$45^\\circ$",
        r"""$180-x = 3(90-x) \Rightarrow 180-x=270-3x \Rightarrow 2x=90 \Rightarrow x=45^\circ$.

Check: supplement $135^\circ = 3 \times 45^\circ$ ✓.""",
        r"$180-x=3(90-x)$ → $x=45^\circ$. Trap: $60^\circ$ from $180-3\times90$ mis-signed.", 35)
    assert 37 + 53 == 90 and 90 - 37 == 53
    S.q("geo-la-p3", "easy", "The complement of an angle of $37^\\circ$ is:",
        ["$143^\\circ$", "$63^\\circ$", "$53^\\circ$", "$64^\\circ$"], "$53^\\circ$",
        r"""Complement $=90^\circ-37^\circ=53^\circ$.

(Its supplement would be $143^\circ$.)""",
        r"$90-37=53^\circ$. Trap: $143^\circ$ answered the supplement.", 25)
    assert 120 + 150 + 90 == 360
    S.q("geo-la-p4", "easy", "Three angles around a point measure $120^\\circ$, $150^\\circ$ and $x$. The value of $x$ is:",
        ["$100^\\circ$", "$80^\\circ$", "$90^\\circ$", "$60^\\circ$"], "$90^\\circ$",
        r"""Angles around a point add to $360^\circ$: $120+150+x=360 \Rightarrow x=90^\circ$.""",
        r"$360-270=90^\circ$. Trap: using $180^\circ$ (line total) instead of $360^\circ$.", 30)
    assert 180 - 75 == 105
    S.q("geo-la-p4", "medium", "Two straight lines intersect at a point. If one of the angles so formed is $75^\\circ$, the measure of the obtuse angle among the remaining three is:",
        ["$75^\\circ$", "$85^\\circ$", "$115^\\circ$", "$105^\\circ$"], "$105^\\circ$",
        r"""Crossing lines give angles $75^\circ, 105^\circ, 75^\circ, 105^\circ$ (vertical pairs equal, neighbours supplementary).

The obtuse one is $105^\circ$.""",
        r"$180-75=105^\circ$. Trap: another $75^\circ$ also appears (vertically opposite), but it is not obtuse.", 35)
    assert F(40, 2) == 20
    S.q("geo-la-p5", "medium", "Two supplementary angles are bisected. If the original angles differ by $40^\\circ$, the difference between the two bisected halves is:",
        ["$40^\\circ$", "$10^\\circ$", "$20^\\circ$", "$80^\\circ$"], "$20^\\circ$",
        r"""Bisecting halves both angles, so it also halves their difference: $\frac{40}{2}=20^\circ$.

(Angles $110^\circ,70^\circ$ → halves $55^\circ,35^\circ$; gap $20^\circ$.)""",
        r"Difference scales with the halving: $\frac12 \times 40 = 20^\circ$. Trap: $40^\circ$ (forgot to halve).", 40)
    assert 90 + 45 + 45 == 180
    S.q("geo-la-p5", "medium", "The bisectors of a pair of co-interior angles between parallel lines meet at an angle of:",
        ["$45^\\circ$", "$90^\\circ$", "$60^\\circ$", "$180^\\circ$"], "$90^\\circ$",
        r"""Co-interior angles sum to $180^\circ$; their bisectors carry half of each, i.e. $90^\circ$ in total.

In the triangle the two bisectors form with the transversal, the third angle is $180^\circ - 90^\circ = 90^\circ$.""",
        r"Halves of two angles totalling $180^\circ$ total $90^\circ$ — so the bisectors meet at $90^\circ$. No algebra needed.", 40)
    return S


# ---------------- geo-triangles ----------------

def build_triangles():
    S = Sub("geo-triangles")

    S.notes = r"""### The angle machinery of a triangle
Interior angles always add to $180^\circ$. An **exterior angle** (one side produced) equals the sum of the two **remote** interior angles — the two not touching that vertex. So exterior at $A = B + C$. Ratio questions: let the angles be $ak, bk, ck$ with $k(a+b+c)=180^\circ$.

An **isosceles** triangle (two equal sides) has two equal base angles, and the median to the base is also the altitude and the angle bisector — one line does three jobs. **Equilateral**: all $60^\circ$; every median is an altitude.

### The four centres — memorise three angle results
| Centre | Defined by | The result asked in exams |
|---|---|---|
| Incentre $I$ | angle bisectors | $\angle BIC = 90^\circ + \frac{A}{2}$ |
| Circumcentre $O$ | perpendicular bisectors | $\angle BOC = 2A$ (same arc $BC$) |
| Orthocentre $H$ | altitudes | $\angle BHC = 180^\circ - A$ |

Each gives the asked angle from $\angle A$ alone — identify the centre from its definition, then read the formula. The **centroid** $G$ (medians) is about lengths, not angles: it divides every median $2:1$ from the vertex, so $AG = \frac{2}{3}AD$ and $GD = \frac{1}{3}AD$. Conditions like "$AG$ exceeds $GD$ by 3" translate to $\frac{1}{3}AD = 3$.

Special positions worth remembering: in a right triangle the orthocentre is the right-angle vertex and the circumcentre is the midpoint of the hypotenuse (so the median to the hypotenuse equals half of it). In an equilateral triangle all four centres coincide.

### Median lengths
- **Apollonius:** median to side $a$: $m_a^2 = \frac{2b^2+2c^2-a^2}{4}$.
- **Isosceles shortcut:** median to the base $= \sqrt{a^2 - \left(\frac{\text{base}}{2}\right)^2}$ — the altitude-right-triangle relation, usually a Pythagorean triplet (13, 13, 10 → height 12).
- Median to the hypotenuse $= \frac{h}{2}$.

### Area of a triangle (three sides)
**Heron:** semi-perimeter $s = \frac{a+b+c}{2}$, area $= \sqrt{s(s-a)(s-b)(s-c)}$. Memorise the standard families: (13,14,15)→84, (5,12,13)→30, (9,12,15)→54, (10,24,26)→120, (7,24,25)→84. If the sides are a Pythagorean family, skip Heron — the triangle is right-angled and area $= \frac{1}{2}\times$ legs.

### Quick revision
- $A+B+C=180^\circ$; exterior $=$ sum of remote interiors.
- $\angle BIC = 90^\circ+\frac{A}{2}$, $\angle BOC = 2A$, $\angle BHC = 180^\circ-A$.
- Centroid: $AG:GD = 2:1$ on every median; $AG-GD = \frac{1}{3}AD$.
- Median: Apollonius, or isosceles $\sqrt{a^2-(b/2)^2}$; median to hypotenuse $=\frac{h}{2}$.
- Heron: $s$, then $\sqrt{s(s-a)(s-b)(s-c)}$; triplet sides → $\frac12 \times$ legs.
"""

    S.pattern("geo-tr-p1", "Angle at a triangle centre (I, O or H)", "very common",
        "$I$/$O$/$H$ is named as incentre/circumcentre/orthocentre (or defined by bisectors/perpendicular bisectors/altitudes); $\\angle A$ is given or asked.",
        r"\angle BIC = 90^\circ+\frac{A}{2},\quad \angle BOC = 2A,\quad \angle BHC = 180^\circ-A",
        r"""1. Identify the centre from its definition (bisectors → I, perpendicular bisectors → O, altitudes → H).
2. Apply the matching formula with the given $\angle A$.
3. Reverse direction: from $\angle BIC$ get $A = 2(\angle BIC - 90^\circ)$; from $\angle BHC$ get $A = 180^\circ - \angle BHC$.

Why: each centre fixes a triangle whose angles are forced by $A$ alone.""",
        "In $\\triangle ABC$, $\\angle A = 60^\\circ$ and $I$ is the incentre. Find $\\angle BIC$.",
        r"$\angle BIC = 90^\circ + \frac{60^\circ}{2} = 120^\circ$. (Check the centre type first — $O$ would also give $2 \times 60^\circ$ here.)")
    S.pattern("geo-tr-p2", "Exterior angle of a triangle", "very common",
        "One side of the triangle is produced; the exterior angle is asked from the two remote interiors, or one interior is missing from the exterior angle.",
        r"\text{ext at } A = B + C",
        r"""1. Spot which two interior angles are REMOTE from the produced side.
2. Add them for the exterior angle; subtract to recover a missing remote interior.
3. The interior angle at the same vertex is $180^\circ - $ exterior — read carefully which is asked.

Why: the exterior and the adjacent interior are supplementary, and the three interiors total $180^\circ$ — the same fact written twice.""",
        "An exterior angle of a triangle is $120^\\circ$ and one of the remote interior angles is $50^\\circ$. The other remote interior angle is:",
        r"$120 - 50 = 70^\circ$. Check: $50+70=120$ ✓ (the interior at the produced vertex is $60^\circ$ — not asked).")
    S.pattern("geo-tr-p3", "Centroid cuts the median 2 : 1", "very common",
        "A median and the centroid $G$ appear; $AG$, $GD$, their sum/difference, or the median length is asked.",
        r"AG = \frac{2}{3}AD,\quad GD = \frac{1}{3}AD",
        r"""1. Name the median $AD$ with $G$ on it; the vertex-side piece is twice the base-side piece.
2. From $AD$: $AG = \frac{2}{3}AD$, $GD = \frac{1}{3}AD$.
3. Conditions like $AG - GD = c$ mean $\frac{1}{3}AD = c$; solve for the asked piece.

Why: the three medians balance at $G$, and on each median the balance point sits twice as far from the vertex as from the opposite side's midpoint.""",
        "In $\\triangle ABC$, the median $AD = 18$ cm and $G$ is the centroid. Find $GD$.",
        r"$GD = \frac{1}{3} \times 18 = 6$ cm (and $AG = 12$ cm — the $2:1$ split).")
    S.pattern("geo-tr-p4", "Area of a triangle: Heron and isosceles height", "common",
        "Three sides given (a triplet family) — area asked; or an isosceles triangle with equal sides and base — area asked.",
        r"K = \sqrt{s(s-a)(s-b)(s-c)},\quad s=\frac{a+b+c}{2}",
        r"""1. Triplet sides? Use right-triangle area $= \frac12 \times$ legs directly.
2. Otherwise Heron: halve the perimeter, multiply the four factors, take the root.
3. Isosceles: height $= \sqrt{a^2 - (b/2)^2}$, then area $= \frac12 b\,h$.

Why: Heron is the general version of the right-triangle shortcut; both run on memorised families.""",
        "Find the area of a triangle with sides 9 cm, 12 cm and 15 cm.",
        r"$9\text{-}12\text{-}15$ is $3\text{-}4\text{-}5 \times 3$ → right-angled: area $= \frac12 \times 9 \times 12 = 54$ sq cm. (Heron agrees: $s=18$, $\sqrt{18 \cdot 9 \cdot 6 \cdot 3} = 54$.)")

    # ---- practice ----
    assert 90 + 30 == 120
    S.q("geo-tr-p1", "easy", "In $\\triangle ABC$, $\\angle A = 60^\\circ$. If $I$ is the incentre of the triangle, then $\\angle BIC$ equals:",
        ["$120^\\circ$", "$90^\\circ$", "$150^\\circ$", "$100^\\circ$"], "$120^\\circ$",
        r"""$\angle BIC = 90^\circ + \frac{A}{2} = 90^\circ + 30^\circ = 120^\circ$.""",
        r"$90 + \frac{60}{2} = 120^\circ$. Trap: $2A = 120^\circ$ happens to match here too, but the incentre formula is the safe route.", 35)
    assert 2 * (110 - 90) == 40
    S.q("geo-tr-p1", "medium", "In $\\triangle ABC$, $\\angle BIC = 110^\\circ$ where $I$ is the incentre. The angle $\\angle A$ equals:",
        ["$50^\\circ$", "$55^\\circ$", "$40^\\circ$", "$70^\\circ$"], "$40^\\circ$",
        r"""$\angle BIC = 90^\circ + \frac{A}{2} \Rightarrow \frac{A}{2} = 110^\circ - 90^\circ = 20^\circ \Rightarrow A = 40^\circ$.""",
        r"$A = 2(\angle BIC - 90^\circ) = 2 \times 20 = 40^\circ$. Trap: $70^\circ$ (using $180 - 110$, the orthocentre relation in reverse).", 40)
    assert 40 + 60 == 100 and 2 + 3 + 4 == 9 and 180 // 9 == 20
    S.q("geo-tr-p2", "easy", "The angles of a triangle are in the ratio $2:3:4$. The exterior angle at the largest angle is:",
        ["$100^\\circ$", "$80^\\circ$", "$120^\\circ$", "$140^\\circ$"], "$100^\\circ$",
        r"""Angles are $40^\circ, 60^\circ, 80^\circ$ ($9k = 180$). The exterior at the $80^\circ$ vertex equals the two remote interiors:

$40^\circ + 60^\circ = 100^\circ$.""",
        r"Exterior $= 180 - 80 = 100^\circ$. Trap: $80^\circ$ (the interior) or $140^\circ$ (wrong vertex).", 40)
    assert 120 - 50 == 70
    S.q("geo-tr-p2", "medium", "A side of a triangle is produced and the exterior angle formed is $120^\\circ$. If one of the two remote interior angles is $50^\\circ$, the other remote interior angle is:",
        ["$60^\\circ$", "$70^\\circ$", "$80^\\circ$", "$30^\\circ$"], "$70^\\circ$",
        r"""Exterior $=$ sum of the remote interiors: $50 + x = 120 \Rightarrow x = 70^\circ$.""",
        r"$120-50=70^\circ$. Trap: $60^\circ$ — that is the interior angle at the produced vertex ($180-120$).", 40)
    assert F(1, 3) * 18 == 6
    S.q("geo-tr-p3", "easy", "The median $AD$ of $\\triangle ABC$ is $18$ cm and $G$ is the centroid. The length of $GD$ is:",
        ["$12$ cm", "$9$ cm", "$6$ cm", "$4.5$ cm"], "$6$ cm",
        r"""$G$ divides the median $2:1$ from the vertex: $GD = \frac{1}{3} \times 18 = 6$ cm ($AG = 12$ cm).""",
        r"$\frac{18}{3} = 6$ cm. Trap: $12$ cm is $AG$, not $GD$.", 30)
    assert F(1, 3) * 9 == 3 and 2 * 3 + 3 == 9
    S.q("geo-tr-p3", "hard", "In $\\triangle ABC$, $G$ is the centroid and $AD$ is a median. If $AG - GD = 3$ cm, the length of $AD$ is:",
        ["$12$ cm", "$6$ cm", "$15$ cm", "$9$ cm"], "$9$ cm",
        r"""Let $GD = k$; then $AG = 2k$, so $AG - GD = k = 3$.

$AD = AG + GD = 3k = 9$ cm.""",
        r"$AG-GD = \frac{1}{3}AD$ → $AD = 3 \times 3 = 9$ cm. Trap: $6$ cm ($2k$ is $AG$, not $AD$).", 50)
    assert F(1, 2) * 9 * 12 == 54
    S.q("geo-tr-p4", "medium", "The sides of a triangle are $9$ cm, $12$ cm and $15$ cm. Its area is:",
        ["$54$ sq cm", "$108$ sq cm", "$45$ sq cm", "$60$ sq cm"], "$54$ sq cm",
        r"""$9\text{-}12\text{-}15$ is a $3\text{-}4\text{-}5$ multiple, so the triangle is right-angled:

area $= \frac12 \times 9 \times 12 = 54$ sq cm.""",
        r"Skip Heron — spot the triplet: $\frac12 \times 108 = 54$. Trap: $108$ (forgot the half).", 45)
    assert F(1, 2) * 10 * 12 == 60 and 13 ** 2 - 5 ** 2 == 144
    S.q("geo-tr-p4", "hard", "An isosceles triangle has equal sides of $13$ cm each and base $10$ cm. Its area is:",
        ["$65$ sq cm", "$60$ sq cm", "$120$ sq cm", "$50$ sq cm"], "$60$ sq cm",
        r"""Height to the base $= \sqrt{13^2 - 5^2} = \sqrt{144} = 12$ cm.

Area $= \frac12 \times 10 \times 12 = 60$ sq cm.""",
        r"5-12-13 triplet: height 12 → $\frac12 \times 10 \times 12 = 60$. Trap: $65$ ($\frac12 \times 13 \times 10$ uses a leg as height).", 50)
    return S


# ---------------- geo-similarity ----------------

def build_similarity():
    S = Sub("geo-similarity")

    S.notes = r"""### Congruent vs similar
**Congruent** triangles are identical in size and shape (SSS, SAS, ASA, RHS). **Similar** triangles have the same shape: equal corresponding angles and proportional sides. Every question here lives in the proportions, so fix the scale factor $k = \frac{\text{side of first}}{\text{corresponding side of second}}$ and remember what it does:
- lengths (sides, perimeters, medians, altitudes) → ratio $k$;
- **areas → ratio $k^2$**.

Going from areas back to lengths needs the square **root** — the single most-tested switch in this subtopic. Perimeter ratio $p:q$ → area ratio $p^2:q^2$; area ratio $a:b$ → perimeter ratio $\sqrt{a}:\sqrt{b}$. Areas $25$ and $81$ give a side ratio of $5:9$, never $25:81$.

### Basic Proportionality Theorem (Thales)
Draw a line parallel to one side of a triangle; it cuts the other two sides in the same ratio:
$$DE \parallel BC \Rightarrow \frac{AD}{DB} = \frac{AE}{EC}$$
The full-side form also holds: $\frac{AD}{AB} = \frac{AE}{AC}$. Keep one form and stay consistent — mixing a part-ratio with a full-ratio is the classic slip. If $AD:DB = 3:4$, then $E$ also cuts $AC$ as $3:4$, so $AE = \frac{3}{7}AC$.

### Midpoint theorem
If $D, E$ are the **midpoints** of two sides, $DE$ is parallel to the third side and $DE = \frac{BC}{2}$. The triangle formed by joining all three midpoints has sides exactly half of the original — its perimeter is half and its area is one-quarter of the original. Converse: through the midpoint of one side, a line parallel to a second side bisects the third.

### Angle bisector theorem
The internal bisector of $\angle A$ meets $BC$ at $D$ with
$$\frac{BD}{DC} = \frac{AB}{AC}$$
This divides the opposite side in the ratio of the adjacent sides — a different mechanism from BPT (no parallel line involved), though the number work looks identical. With $BC$ known, split it in the ratio; with one part known, scale the other.

### Reading similar-triangle data
When one full set of sides is known and one side of the twin: match the **corresponding** sides (largest with largest, smallest with smallest), get $k$ once, then scale everything by $k$. When perimeters and areas are mixed, convert perimeters to a side ratio, square it for areas, or take the root to go back.

### Quick revision
- Similar: lengths $\times k$; areas $\times k^2$. Areas → lengths: take $\sqrt{\ }$.
- $DE \parallel BC \Rightarrow \frac{AD}{DB} = \frac{AE}{EC}$.
- Midpoints: $DE = \frac{BC}{2}$; midpoint triangle: perimeter $\frac12$, area $\frac14$.
- Bisector of $A$: $\frac{BD}{DC} = \frac{AB}{AC}$.
- Match corresponding sides (small ↔ small, large ↔ large) before scaling.
"""

    S.pattern("geo-si-p1", "Perimeter ratio ↔ area ratio", "very common",
        "Two similar triangles have perimeters (or a pair of corresponding sides/altitudes) in a given ratio and one area is asked — or areas are given and a perimeter asked.",
        r"\frac{K_1}{K_2} = \left(\frac{P_1}{P_2}\right)^2",
        r"""1. Perimeters (sides, altitudes) give the linear ratio $k$.
2. Areas need $k^2$; recovering lengths from areas needs $\sqrt{k_{\text{area}}}$.
3. Scale the known area/perimeter by the right ratio.

Why: area is two lengths multiplied, so the scale factor enters twice.""",
        "Two similar triangles have perimeters 24 cm and 36 cm. If the area of the larger triangle is 54 sq cm, find the area of the smaller.",
        r"Side ratio $= \frac{24}{36} = \frac{2}{3}$, so area ratio $= \frac{4}{9}$: smaller area $= 54 \times \frac{4}{9} = 24$ sq cm.")
    S.pattern("geo-si-p2", "BPT: a parallel line inside the triangle", "very common",
        "$DE \\parallel BC$ is stated (or drawn) with three of the four segments $AD, DB, AE, EC$ given; the fourth is asked.",
        r"DE \parallel BC \Rightarrow \frac{AD}{DB} = \frac{AE}{EC}",
        r"""1. Write the part-ratio on one side equals the part-ratio on the other.
2. Substitute the three known segments; solve the proportion.
3. If a full side is given instead, switch to $\frac{AD}{AB} = \frac{AE}{AC}$ — but never mix part with full.

Why: the parallel line makes two similar triangles, so the cut points keep one ratio on both sides.""",
        "In $\\triangle ABC$, $DE \\parallel BC$ with $AD = 3$ cm, $DB = 5$ cm and $AE = 6$ cm. Find $EC$.",
        r"$\frac{AD}{DB} = \frac{AE}{EC} \Rightarrow \frac{3}{5} = \frac{6}{EC} \Rightarrow EC = 10$ cm.")
    S.pattern("geo-si-p3", "Midpoint theorem", "common",
        "'D and E are the midpoints of AB and AC' — find $DE$ from $BC$ or $BC$ from $DE$, or use the midpoint-triangle perimeter/area.",
        r"DE = \frac{BC}{2}",
        r"""1. Midpoints on two sides → the joining segment is half the third side and parallel to it.
2. Double/halve as asked.
3. All three midpoints joined: each small side is half a big side → perimeter $\frac12$, area $\frac14$.

Why: the midpoint segment is the special BPT case with ratio $1:1$.""",
        "In $\\triangle PQR$, $X$ and $Y$ are the midpoints of $PQ$ and $PR$. If $QR = 14$ cm, find $XY$.",
        r"$XY = \frac{QR}{2} = 7$ cm by the midpoint theorem.")
    S.pattern("geo-si-p4", "Angle bisector theorem", "common",
        "The bisector of an angle of a triangle meets the opposite side; the two parts of that side (or a side length) are asked.",
        r"\frac{BD}{DC} = \frac{AB}{AC}",
        r"""1. The bisected angle's two sides give the ratio $AB : AC$.
2. The opposite side is split in that same ratio.
3. With $BC$ known, divide it in the ratio; with one part known, scale.

Why: the bisector creates two triangles that mirror the ratio via the sine rule — the exam-ready statement is the ratio formula.""",
        "In $\\triangle ABC$, the bisector of $\\angle A$ meets $BC$ at $D$. If $AB = 8$ cm, $AC = 12$ cm and $BC = 15$ cm, find $DC$.",
        r"$BD:DC = 8:12 = 2:3$; $DC = \frac{3}{5} \times 15 = 9$ cm.")
    S.pattern("geo-si-p5", "Scaling a full triangle (find the missing sides)", "common",
        "One triangle's three sides are given; a similar triangle has one side known — the remaining sides or its perimeter is asked.",
        r"k = \frac{\text{known side of 2nd}}{\text{corresponding side of 1st}}",
        r"""1. Match corresponding sides: smallest ↔ smallest, largest ↔ largest.
2. Compute the scale $k$ once.
3. Multiply every side (or the whole perimeter) by $k$.

Why: similarity scales all lengths by the same $k$ — one multiplication per side, no per-side algebra.""",
        "A triangle with sides 3, 4 and 5 cm is similar to a larger triangle whose hypotenuse is 20 cm. The perimeter of the larger triangle is:",
        r"$k = \frac{20}{5} = 4$; sides $12, 16, 20$ → perimeter $= 4 \times 12 = 48$ cm.")

    # ---- practice ----
    assert F(4, 9) * 54 == 24
    S.q("geo-si-p1", "easy", "Two similar triangles have perimeters $24$ cm and $36$ cm. If the area of the larger triangle is $54$ sq cm, the area of the smaller triangle is:",
        ["$36$ sq cm", "$24$ sq cm", "$32$ sq cm", "$27$ sq cm"], "$24$ sq cm",
        r"""Side ratio $= \frac{24}{36} = \frac{2}{3}$, so the area ratio is $\frac{4}{9}$.

Smaller area $= 54 \times \frac{4}{9} = 24$ sq cm.""",
        r"$\left(\frac{2}{3}\right)^2 = \frac49$; $54 \times \frac49 = 24$. Trap: $36$ (used the linear ratio $\frac23$).", 40)
    assert F(9, 5) * 40 == 72
    S.q("geo-si-p1", "medium", "The areas of two similar triangles are $25$ sq cm and $81$ sq cm. If the perimeter of the smaller triangle is $40$ cm, the perimeter of the larger triangle is:",
        ["$64.8$ cm", "$72$ cm", "$90$ cm", "$56$ cm"], "$72$ cm",
        r"""Area ratio $25:81$ → side ratio $5:9$ (square root!).

Larger perimeter $= 40 \times \frac{9}{5} = 72$ cm.""",
        r"$\sqrt{\frac{81}{25}} = \frac95$; $40 \times \frac95 = 72$. Trap: $64.8$ (multiplied by $\frac{81}{25}$).", 45)
    assert 3 * 10 == 6 * 5
    S.q("geo-si-p2", "easy", "In $\\triangle ABC$, $DE \\parallel BC$ with $AD = 3$ cm, $DB = 5$ cm and $AE = 6$ cm. The length of $EC$ is:",
        ["$10$ cm", "$9$ cm", "$7.5$ cm", "$8$ cm"], "$10$ cm",
        r"""$\frac{AE}{EC} = \frac{AD}{DB} \Rightarrow \frac{6}{EC} = \frac{3}{5} \Rightarrow EC = 10$ cm.""",
        r"$EC = 6 \times \frac{5}{3} = 10$ cm. Trap: $7.5$ from $\frac{AD}{AB}$ mixed with $\frac{AE}{EC}$.", 35)
    assert F(3, 7) * 28 == 12
    S.q("geo-si-p2", "medium", "In $\\triangle ABC$, $DE \\parallel BC$ where $D$ lies on $AB$ with $AD : DB = 3 : 4$. If $AC = 28$ cm, the length of $AE$ is:",
        ["$16$ cm", "$12$ cm", "$15$ cm", "$21$ cm"], "$12$ cm",
        r"""$\frac{AE}{EC} = \frac{AD}{DB} = \frac{3}{4}$, so $AE = \frac{3}{7} \times AC = \frac{3}{7} \times 28 = 12$ cm.""",
        r"$E$ cuts $AC$ in ratio $3:4$ → $AE = \frac{3}{7} \times 28 = 12$ cm. Trap: $16$ is $EC$.", 45)
    assert F(14, 2) == 7
    S.q("geo-si-p3", "easy", "In $\\triangle PQR$, $X$ and $Y$ are the midpoints of $PQ$ and $PR$ respectively. If $QR = 14$ cm, then $XY$ equals:",
        ["$7$ cm", "$14$ cm", "$28$ cm", "$3.5$ cm"], "$7$ cm",
        r"""Midpoint theorem: $XY = \frac{QR}{2} = 7$ cm.""",
        r"Half of the third side: $7$ cm. Trap: $28$ (doubled instead of halved).", 30)
    assert F(36, 2) == 18 and F(36, 4) == 9
    S.q("geo-si-p3", "medium", "The midpoints of the three sides of a triangle of perimeter $36$ cm are joined to form a smaller triangle. The perimeter of this smaller triangle is:",
        ["$18$ cm", "$12$ cm", "$24$ cm", "$9$ cm"], "$18$ cm",
        r"""Each side of the midpoint triangle is half the corresponding original side.

Perimeter $= \frac{36}{2} = 18$ cm (its area would be $\frac14$ of the original).""",
        r"Half the perimeter: $18$ cm. Trap: $9$ cm — that logic belongs to the AREA ratio $\frac14$, not perimeter.", 40)
    assert F(3, 5) * 15 == 9 and F(2, 3) * 15 == 10
    S.q("geo-si-p4", "medium", "In $\\triangle ABC$, the internal bisector of $\\angle A$ meets $BC$ at $D$. If $AB = 8$ cm, $AC = 12$ cm and $BC = 15$ cm, then $DC$ equals:",
        ["$6$ cm", "$9$ cm", "$10$ cm", "$7.5$ cm"], "$9$ cm",
        r"""$\frac{BD}{DC} = \frac{AB}{AC} = \frac{8}{12} = \frac{2}{3}$, so $BC = 15$ splits into $6$ cm and $9$ cm.

$DC = 9$ cm.""",
        r"$15 \times \frac{3}{5} = 9$ cm (the $AC$ share). Trap: $6$ cm is $BD$.", 45)
    assert 10 * 7 == 14 * 5 and 5 + 7 == 12
    S.q("geo-si-p4", "hard", "In $\\triangle ABC$, the bisector of $\\angle A$ meets $BC$ at $D$ with $BD = 5$ cm. If $AB = 10$ cm and $AC = 14$ cm, the length of $BC$ is:",
        ["$17$ cm", "$10$ cm", "$14$ cm", "$12$ cm"], "$12$ cm",
        r"""$\frac{BD}{DC} = \frac{AB}{AC} \Rightarrow \frac{5}{DC} = \frac{10}{14} \Rightarrow DC = 7$ cm.

$BC = 5 + 7 = 12$ cm.""",
        r"$DC = 5 \times \frac{14}{10} = 7$; add the parts: $12$ cm. Trap: stopping at $7$.", 55)
    assert 3 * 4 + 4 * 4 + 5 * 4 == 48
    S.q("geo-si-p5", "easy", "A triangle with sides $3$ cm, $4$ cm and $5$ cm is similar to a larger triangle whose longest side is $20$ cm. The perimeter of the larger triangle is:",
        ["$40$ cm", "$48$ cm", "$60$ cm", "$36$ cm"], "$48$ cm",
        r"""$k = \frac{20}{5} = 4$; sides become $12, 16, 20$.

Perimeter $= 4 \times 12 = 48$ cm.""",
        r"Perimeter scales by $k = 4$: $12 \times 4 = 48$ cm. Trap: $60$ ($5 \times 12$, mixing sides).", 35)
    assert F(20, 4) == 5 and 6 * F(10, 8) == F(15, 2)
    S.q("geo-si-p5", "medium", "Two similar triangles have sides $8$ cm, $6$ cm, $4$ cm and $10$ cm, $7.5$ cm, $x$ cm (in corresponding order). The value of $x$ is:",
        ["$5$ cm", "$5.5$ cm", "$6$ cm", "$4.5$ cm"], "$5$ cm",
        r"""Corresponding pairs: $\frac{10}{8} = \frac{7.5}{6} = \frac{x}{4} = 1.25$.

$x = 4 \times 1.25 = 5$ cm.""",
        r"One scale for all sides: $k = 1.25$ → $x = 5$ cm. Check the middle pair: $6 \times 1.25 = 7.5$ ✓.", 40)
    return S
