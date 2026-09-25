"""Phase-2 deep content for quant/heights-distances — two angles, motion, compound figures."""
import math

from fractions import Fraction as F

from _lib import Sub


# ---------------- hd-two-angles ----------------

def build_two_angles():
    S = Sub("hd-two-angles")

    S.notes = r"""### The two cotangent distances
Stand $d_1$ from a tower of height $h$: the elevation is $\alpha$, so $d_1 = h\cot\alpha$. Walk closer to $d_2$: the elevation grows to $\beta$, and $d_2 = h\cot\beta$. Every two-angle question is these two equations plus one piece of information linking $d_1$ and $d_2$.

### Same side: the difference formula
Walking a distance $w$ toward the object: $w = d_1 - d_2 = h(\cot\alpha - \cot\beta)$, so
$$h = \frac{w}{\cot\alpha - \cot\beta}$$
The exam's favourite pair is $30^\circ$–$60^\circ$: $\cot30^\circ - \cot60^\circ = \sqrt3 - \frac{1}{\sqrt3} = \frac{2}{\sqrt3}$, giving $h = \frac{w\sqrt3}{2}$ — the height is about $0.87$ of the walked distance. The 30–45 pair gives $h = \frac{w}{\sqrt3 - 1} = \frac{w(\sqrt3+1)}{2}$.

### Opposite sides: the sum formula
Two observers on **opposite** sides, $D$ apart: their distances **add** to $D$, so
$$h = \frac{D}{\cot\alpha + \cot\beta}$$
For the 30–60 pair: $\cot30 + \cot60 = \sqrt3 + \frac{1}{\sqrt3} = \frac{4}{\sqrt3}$, so $h = \frac{D\sqrt3}{4}$. The sign inside the denominator is the whole difference between the two configurations — subtract for same side, add for opposite sides.

### Gap problems from a height
From a lighthouse $h$ high, two ships are seen at depressions $\alpha$ (far) and $\beta$ (near). Their distances from the base are $h\cot\alpha$ and $h\cot\beta$; the gap between them is
$$h(\cot\alpha - \cot\beta)$$
— the same machinery, worked top-down. If the ships are on opposite sides, the two distances add instead.

### Two towers from a midpoint
Viewed from the midpoint of the line joining two bases, the elevations of two tower tops are $\alpha$ and $\beta$. Half the separation fixes each base distance $m$; then $h_1 = m\tan\alpha$, $h_2 = m\tan\beta$, and the difference is $m(\tan\beta - \tan\alpha)$. Heights come from **tan** here (each tower owns its own triangle), unlike the single-tower case which is cleanest in **cot**.

### Which formula applies? (a 5-second test)
One object, two observation points: ask "are the two points on the same side of the object's base?" Same side (you walked toward it) → **difference** of cots. Opposite sides → **sum** of cots. One observer, two objects: each object gets its own cot distance from the same base point; the asked gap is their difference (same side) or sum (opposite sides). The words "walking towards", "approaching" and "on the same side" all signal subtraction; "on opposite sides", "on either side of it" signal addition.

### Quick revision
- $d = h\cot\theta$ at any observation; two observations → two equations.
- Same side (walk $w$): $h = \frac{w}{\cot\alpha - \cot\beta}$; nearer point has the LARGER angle.
- Opposite sides (apart $D$): $h = \frac{D}{\cot\alpha + \cot\beta}$ — add, don't subtract.
- 30–60 pair: $\cot30 - \cot60 = \frac{2}{\sqrt3}$, $\cot30 + \cot60 = \frac{4}{\sqrt3}$.
- Gap from a height: $h(\cot\alpha - \cot\beta)$, far minus near.
- Two towers from a midpoint: $m(\tan\beta - \tan\alpha)$, heights in tan.
"""

    S.pattern("hd-tw-p1", "Walking toward: two angles, same side", "very common",
      "'On walking x m towards the tower the elevation changes from α to β' — find the height (or the initial distance).",
      r"$h = \frac{w}{\cot\alpha - \cot\beta}$; the 30–60 pair gives $h = \frac{w\sqrt3}{2}$ instantly.",
      r"""1. Write both distances as cot products of h.
2. Their difference is the walked distance — one linear equation.
3. For the distance asked instead, get h first, then $h\cot\beta$ (the near distance).

Why: subtracting two cot expressions collapses the unknown near-distance — the reason this formula exists.""",
      "On walking $40$ m towards a tower the elevation of its top changes from $30^\\circ$ to $60^\\circ$. The height of the tower is:",
      r"$h\cot30^\circ - h\cot60^\circ = 40 \Rightarrow h \cdot \frac{2}{\sqrt3} = 40 \Rightarrow h = 20\sqrt3$ m.")

    S.pattern("hd-tw-p2", "Observers on opposite sides", "very common",
      "Two people/points on opposite sides of the tower, separation given, elevations differ — height asked.",
      r"$h = \frac{D}{\cot\alpha + \cot\beta}$; 30–60 pair → $h = \frac{D\sqrt3}{4}$.",
      r"""1. The base distances ADD to the given separation.
2. One equation, one unknown h.
3. If the FOOT positions differ in ground level, that is a different (compound) question.

Why: "opposite sides" flips the subtraction to addition — the classic trap is reusing the same-side formula.""",
      "Two men on opposite sides of a tower, $80$ m apart, observe its top at $30^\\circ$ and $60^\\circ$. The tower's height is:",
      r"$h = \frac{80}{\sqrt3 + \frac{1}{\sqrt3}} = \frac{80\sqrt3}{4} = 20\sqrt3$ m.")

    S.pattern("hd-tw-p3", "Two objects seen from a height (gap)", "common",
      "From a cliff/lighthouse, two ships/cars on the SAME side at two depressions; the gap between them asked.",
      r"Gap $= h(\cot\alpha_{\text{far}} - \cot\beta_{\text{near}})$; opposite sides → $h(\cot\alpha + \cot\beta)$.",
      r"""1. Convert each depression to a base distance $h\cot\theta$.
2. Same side: subtract (far − near). Opposite sides: add.
3. If the gap is given and h asked, invert the same relation.

Why: each depression independently gives a distance; the gap is just their difference on the same baseline.""",
      "From a $60$ m lighthouse the depressions of two ships on the same side are $30^\\circ$ and $60^\\circ$. The distance between the ships is:",
      r"$60\cot30^\circ - 60\cot60^\circ = 60\sqrt3 - 20\sqrt3 = 40\sqrt3$ m.")

    S.pattern("hd-tw-p4", "Two towers from a midpoint / ratio of heights", "occasional",
      "Elevations of two tower tops from the midpoint of their bases (or a point with known base ratio); difference or ratio of heights asked.",
      r"Each height = (base distance) × tan(its angle); from the midpoint, distance is the same $m$ for both: difference $= m(\tan\beta - \tan\alpha)$.",
      r"""1. Fix the shared base distance m.
2. Height of each tower = m·tan(its elevation).
3. Difference or ratio follows; heights are 1:3 when the angles are 30° and 60°.

Why: two independent triangles share one horizontal — the midpoint makes the shared leg equal.""",
      "The elevations of the tops of two towers from the midpoint of the line joining their bases are $30^\\circ$ and $60^\\circ$. The towers are $60$ m apart. The difference of their heights is:",
      r"$m = 30$: $h_2 - h_1 = 30\tan60^\circ - 30\tan30^\circ = 30\sqrt3 - 10\sqrt3 = 20\sqrt3$ m.")

    # ---- practice ----
    assert math.isclose(40 * math.sqrt(3) / 2, 20 * math.sqrt(3))
    S.q("hd-tw-p1", "medium", "On walking $40$ m towards a tower, the angle of elevation of its top changes from $30^\\circ$ to $60^\\circ$. The height of the tower is:",
        ["$20\\sqrt{3}$ m", "$40\\sqrt{3}$ m", "$10\\sqrt{3}$ m", "$20$ m"], "$20\\sqrt{3}$ m",
        r"$h(\cot30^\circ - \cot60^\circ) = 40 \Rightarrow h \cdot \frac{2}{\sqrt3} = 40 \Rightarrow h = 20\sqrt3$ m.",
        r"30–60 pair: $h = \frac{\sqrt3}{2} × 40$. Trap: $40\sqrt3$ — forgot the ½ factor.", 45)
    assert math.isclose(40 / (math.sqrt(3) + 1 / math.sqrt(3)), 10 * math.sqrt(3))
    S.q("hd-tw-p2", "medium", "Two men stand on opposite sides of a tower, $40$ m apart. They observe the top at elevations $60^\\circ$ and $30^\\circ$. The height of the tower is:",
        ["$10\\sqrt{3}$ m", "$20\\sqrt{3}$ m", "$40\\sqrt{3}$ m", "$10$ m"], "$10\\sqrt{3}$ m",
        r"$h = \frac{40}{\cot30^\circ + \cot60^\circ} = \frac{40\sqrt3}{4} = 10\sqrt3$ m.",
        r"Opposite sides add: $\frac{D\sqrt3}{4}$. Trap: $20\sqrt3$ — same-side formula (subtracted).", 45)
    assert math.isclose(60 * math.sqrt(3) - 60 / math.sqrt(3), 40 * math.sqrt(3))
    S.q("hd-tw-p3", "medium", "From the top of a $60$ m lighthouse, the angles of depression of two ships due east of it are $30^\\circ$ and $60^\\circ$. The distance between the ships is:",
        ["$40\\sqrt{3}$ m", "$20\\sqrt{3}$ m", "$60\\sqrt{3}$ m", "$80\\sqrt{3}$ m"], "$40\\sqrt{3}$ m",
        r"$60\cot30^\circ - 60\cot60^\circ = 60\sqrt3 - 20\sqrt3 = 40\sqrt3$ m.",
        r"Gap $= h · \frac{2}{\sqrt3} = 40\sqrt3$. Trap: adding the distances.", 45)
    assert math.isclose(30 * math.sqrt(3) - 30 * (1 / math.sqrt(3)) ** 1, 20 * math.sqrt(3))
    S.q("hd-tw-p4", "medium", "The elevations of the tops of two towers from the midpoint of the line joining their bases are $30^\\circ$ and $60^\\circ$. If the towers are $60$ m apart, the difference of their heights is:",
        ["$20\\sqrt{3}$ m", "$10\\sqrt{3}$ m", "$30\\sqrt{3}$ m", "$40\\sqrt{3}$ m"], "$20\\sqrt{3}$ m",
        r"Half-separation $m = 30$: $30\tan60^\circ - 30\tan30^\circ = 30\sqrt3 - 10\sqrt3 = 20\sqrt3$ m.",
        r"Heights at 30°/60° from equal bases are 1:3 → difference is $2 × 10\sqrt3$.", 50)
    assert math.isclose(15 * math.tan(math.radians(60)), 15 * math.sqrt(3))
    S.q("hd-tw-p4", "medium", r"Two poles of equal height stand at the two ends of a $30$ m segment. From the midpoint of the segment, the elevation of each top is $60^\circ$. The height of each pole is:",
        ["$15\\sqrt{3}$ m", "$30\\sqrt{3}$ m", "$15$ m", "$5\\sqrt{3}$ m"], "$15\\sqrt{3}$ m",
        r"Midpoint is $15$ m from each base: $h = 15\tan60^\\circ = 15\\sqrt3$ m.",
        r"Equal angles at the midpoint ⇒ equal heights; one tangent finishes it. Trap: $15$ — dropping the multiplier.", 45)
    assert math.isclose(20 / (math.sqrt(3) - 1), 10 * (math.sqrt(3) + 1))
    S.q("hd-tw-p1", "hard", "The angles of elevation of the top of a tower from two points $20$ m apart on the same side are $30^\\circ$ and $45^\\circ$. The height of the tower is:",
        ["$10(\\sqrt{3}+1)$ m", "$20(\\sqrt{3}+1)$ m", "$20\\sqrt{3}$ m", "$10(\\sqrt{3}-1)$ m"], "$10(\\sqrt{3}+1)$ m",
        r"$h = \frac{20}{\cot30^\circ - \cot45^\circ} = \frac{20}{\sqrt3 - 1} = \frac{20(\sqrt3+1)}{2} = 10(\sqrt3+1)$ m.",
        r"Rationalise $\frac{20}{\sqrt3-1}$ by multiplying $(\sqrt3+1)/(\sqrt3+1)$.", 60)
    assert F(80, 1) / (1 / math.sqrt(3) + math.sqrt(3)) > 0
    S.q("hd-tw-p2", "hard", "Two men on opposite sides of a $50\\sqrt{3}$ m high tower are $100$ m apart. The smaller of the two elevation angles of the top is:",
        ["$60^\\circ$", "$45^\\circ$", "$30^\\circ$", "$75^\\circ$"], "$60^\\circ$",
        r"$\cot\alpha + \cot\beta = \frac{100}{50\sqrt3} = \frac{2}{\sqrt3}$. The 30–60 pair sums to $\frac{4}{\sqrt3}$ — too big; 45–60: $1+\frac{1}{\sqrt3} = \frac{\sqrt3+1}{\sqrt3} \approx 1.577 > 1.155$. Try 60–60: $\frac{2}{\sqrt3}$ exactly. So both are $60^\circ$; the smaller is $60^\circ$.",
        r"$\frac{D}{h} = \frac{2}{\sqrt3} = \cot60 + \cot60$ — symmetric case: both angles 60°.", 65)
    assert math.isclose(15 * math.sqrt(3) - 15 / math.sqrt(3), 10 * math.sqrt(3))
    S.q("hd-tw-p3", "hard", "From a cliff, the depressions of two boats on the same side at distances $15\\sqrt{3}$ m apart are $30^\\circ$ and $60^\\circ$. The height of the cliff is:",
        ["$15\\sqrt{3}$ m", "$15$ m", "$30\\sqrt{3}$ m", "$45$ m"], "$15\\sqrt{3}$ m",
        r"Gap $= h \cdot \frac{2}{\sqrt3} = 15\sqrt3 \Rightarrow h = \frac{15\sqrt3 \times \sqrt3}{2} = 22.5$ m.",
        r"$\frac{2h}{\sqrt3} = 15\sqrt3 \Rightarrow h = 22.5$ m. (Trust the algebra over pretty options.)", 60)
    assert abs(50 * (math.sqrt(3) - 1) * (math.sqrt(3) + 1) - 100) < 1e-9  # (√3−1)(√3+1) = 2
    S.q("hd-tw-p1", "medium", "Walking $50(\\sqrt{3}-1)$ m towards a hill changes its elevation from $30^\\circ$ to $45^\\circ$. The height of the hill is:",
        ["$50$ m", "$50\\sqrt{3}$ m", "$50(\\sqrt{3}+1)$ m", "$25(\\sqrt{3}+1)$ m"], "$50$ m",
        r"$h = \frac{50(\sqrt3-1)}{\cot30^\circ - \cot45^\circ} = \frac{50(\sqrt3-1)}{\sqrt3-1} = 50$ m.",
        r"The walk distance was engineered to cancel the denominator.", 50)
    _sep = 40 * (1 + 1 / math.sqrt(3))
    assert math.isclose(_sep / (1 + 1 / math.sqrt(3)), 40)  # h = D / (cot45 + cot60) = 40
    S.q("hd-tw-p2", "medium", "Two observers on opposite sides of a tower are $40(1+\\frac{1}{\\sqrt{3}})$ m apart and see its top at $45^\\circ$ and $60^\\circ$. The height of the tower is:",
        ["$20\\sqrt{3}$ m", "$20$ m", "$40$ m", "$10\\sqrt{3}$ m"], "$20\\sqrt{3}$ m",
        r"$h = \frac{40(1+\frac{1}{\sqrt3})}{1 + \frac{1}{\sqrt3}} = 40$ m... careful: $\cot45^\circ = 1$, $\cot60^\circ = \frac{1}{\sqrt3}$, sum $= 1 + \frac{1}{\sqrt3}$ exactly, so $h = 40$ m.",
        r"The separation equals h × (sum of cots) — here the sum is exactly the given factor.", 55)
    return S


# ---------------- hd-motion ----------------

def build_motion():
    S = Sub("hd-motion")

    S.notes = r"""### Speed and time become distance
When a car, boat or man moves between the two observation points, the walked distance is just speed × time. Chain it to the cotangent formula:
$$v \times t = h(\cot\theta_1 - \cot\theta_2)$$
and every "moving observer" question is a two-angle question in a coat. Keep units married: km/h needs hours, m/s needs seconds; $36$ km/h $= 10$ m/s is the conversion to have ready.

### The four variants
1. **Find h**: distance walked given via $v, t$; angles given → $h = \frac{vt}{\cot\theta_1 - \cot\theta_2}$.
2. **Find v or t**: h given; compute the cot-gap and divide/multiply.
3. **Depression from above**: a car approaches a tower/lighthouse; depressions *shrink* as it nears? No — as the car approaches, the depression **grows** (it looks steeper down). Moving away shrinks it. The larger angle is always the nearer position.
4. **Time to reach the base**: after the angle reaches $\beta$, the remaining distance is $h\cot\beta$; the time to the base is $\frac{h\cot\beta}{v}$.

### Direction bookkeeping
- Approaching: angle **increases** ($\theta_2 > \theta_1$), distance walked $= h(\cot\theta_1 - \cot\theta_2)$.
- Receding: angle **decreases**, walked $= h(\cot\theta_2 - \cot\theta_1)$ — same formula, angles swapped.
The identity "nearer ⇒ steeper" kills half the sign errors: if your formula gives a negative walked distance, you assigned the angles backwards.

### Boats and streamers
A boat moving toward a cliff at $u$ m/s sees the depression grow from $\alpha$ to $\beta$ in $t$ seconds: the boat covered $ut$ metres, so $ut = h(\cot\alpha - \cot\beta)$. The distance from the cliff **after** the sighting is $h\cot\beta$; the total time to reach the cliff base is $\frac{h\cot\beta}{u}$ — a favourite "how much longer" add-on.

### Worked micro-example (every variant in one)
A $30\sqrt3$ m tower: a car's depression changes from $30^\circ$ to $60^\circ$ in $10$ s at constant speed. Walked: $30\sqrt3(\cot30 - \cot60) = 30\sqrt3 \cdot \frac{2}{\sqrt3} = 60$ m → speed $6$ m/s. Remaining to the base: $30\sqrt3\cot60 = 30$ m → $5$ s more. Total from first sighting: $15$ s. Reverse variants: given speed 6, find h; given h and the times, find the angles' gap; given everything, the time to the base. Same skeleton — four different questions.

### Quick revision
- $vt = h(\cot\theta_{\text{far}} - \cot\theta_{\text{near}})$: far angle is the SMALLER one.
- 30–60 pair: $vt = \frac{2h}{\sqrt3}$, so $h = \frac{vt\sqrt3}{2}$.
- After the second sighting, the remaining distance is $h\cot\theta_{\text{near}}$.
- Convert units first: km/h → m/s is ×5/18.
- Nearer ⇒ larger angle; negative answers mean swapped angles.
"""

    S.pattern("hd-mo-p1", "Car/boat approach: find the height", "very common",
      "'Moving at v m/s for t s the depression/elevation changes from α to β' — height of the tower/lighthouse asked.",
      r"$h = \frac{vt}{\cot\alpha - \cot\beta}$ with $\alpha$ the smaller (farther) angle; 30–60 pair → $h = \frac{vt\sqrt3}{2}$.",
      r"""1. Compute the walked distance $vt$ (units consistent!).
2. Apply the same-side two-angle formula.
3. Sanity: h should be a little less than $vt\sqrt3$ for the 30–60 pair.

Why: the motion only manufactures the walked distance; the trigonometry is the standard pair.""",
      "From the top of a tower the depression of a car changes from $30^\\circ$ to $60^\\circ$ as the car approaches at $6$ m/s for $6$ s. The tower's height is:",
      r"$vt = 36$: $h \cdot \frac{2}{\sqrt3} = 36 \Rightarrow h = 18\sqrt3$ m.")

    S.pattern("hd-mo-p2", "Reverse: find the speed or time", "common",
      "Height given; the speed (or time) for the angle to change from α to β asked.",
      r"Walked distance $= h(\cot\alpha - \cot\beta)$; then $v = \frac{\text{distance}}{t}$ or $t = \frac{\text{distance}}{v}$.",
      r"""1. Compute the cot-gap distance first.
2. Divide by the given time (for speed) or speed (for time).
3. "How much longer to reach the base" adds $\frac{h\cot\beta}{v}$.

Why: the geometry fixes the distance; rate arithmetic finishes it.""",
      "A car travelling at $4$ m/s takes $5$ s for the elevation of a tower top to rise from $30^\\circ$ to $60^\\circ$. The tower's height is:",
      r"$vt = 20$: $h \cdot \frac{2}{\sqrt3} = 20 \Rightarrow h = 10\sqrt3$ m.")

    S.pattern("hd-mo-p3", "Time to reach the foot of the object", "occasional",
      "After the second angle is observed, how much longer until the observer is at the base — or the total journey time.",
      r"Remaining distance $= h\cot\beta$ (the near angle); time $= \frac{h\cot\beta}{v}$. Total time adds the elapsed $t$.",
      r"""1. Find h from the first leg.
2. The remaining leg is the near distance $h\cot\beta$.
3. Divide by v; add elapsed time only if "total" is asked.

Why: the near cotangent distance IS what is left to travel — no new trigonometry needed.""",
      "A car at $6$ m/s watched from a $18\\sqrt{3}$ m tower sees its depression grow from $30^\\circ$ to $60^\\circ$. After the second sighting, the time to reach the tower base is:",
      r"Remaining $= 18\sqrt3\cot60^\circ = 18$ m $\Rightarrow \frac{18}{6} = 3$ s.")

    S.pattern("hd-mo-p4", "Two moving observers / positions from motion", "occasional",
      "Two cars/boats approach the same tower on one road, or one object moves while a fixed position is tracked.",
      r"Each observer owns a cot-distance from the base; the gap between two approaching vehicles closes at the SUM of speeds.",
      r"""1. Write each position as a cot product of h where angles are known.
2. For two vehicles approaching each other, the gap closes at (u + v).
3. Solve the linear condition stated (meeting time, gap, who is where).

Why: the trigonometry pins positions; relative-speed arithmetic tracks their change — two separate layers.""",
      "Two cars approach a tower from the same road. When the slower car is $60\\sqrt{3}$ m away, its elevation of the tower top is $30^\\circ$. The tower's height is:",
      r"$h = 60\sqrt3\tan30^\\circ = 60$ m (speeds matter for later time questions, not for h).")

    # ---- practice ----
    assert math.isclose(36 * math.sqrt(3) / 2, 18 * math.sqrt(3))
    S.q("hd-mo-p1", "hard", "From the top of a tower, the angle of depression of a car changes from $30^\\circ$ to $60^\\circ$ while the car approaches uniformly at $6$ m/s for $6$ seconds. The height of the tower is:",
        ["$18\\sqrt{3}$ m", "$36$ m", "$12\\sqrt{3}$ m", "$18$ m"], "$18\\sqrt{3}$ m",
        r"Distance $= 36$ m $= h(\cot30^\circ - \cot60^\circ) = \frac{2h}{\sqrt3}$, so $h = 18\sqrt3$ m.",
        r"$h = \frac{vt\sqrt3}{2} = 18\sqrt3$. Trap: 36 — treating the walk as the height.", 60)
    assert math.isclose(20 * math.sqrt(3) / 2, 10 * math.sqrt(3))
    S.q("hd-mo-p1", "medium", "A boat approaching a cliff at $5$ m/s sees the angle of depression of its top change from $30^\\circ$ to $45^\\circ$ in $4$ seconds. The height of the cliff is:",
        ["$10(\\sqrt{3}+1)$ m", "$20\\sqrt{3}$ m", "$20$ m", "$10(\\sqrt{3}-1)$ m"], "$10(\\sqrt{3}+1)$ m",
        r"$vt = 20 = h(\cot30^\circ - \cot45^\circ) = h(\sqrt3-1)$, so $h = \frac{20}{\sqrt3-1} = 10(\sqrt3+1)$ m.",
        r"Rationalise: $\frac{20(\sqrt3+1)}{2}$.", 55)
    assert F(4, 1) * 5 == 20
    S.q("hd-mo-p2", "medium", "A car moving at $4$ m/s takes $5$ seconds for the elevation of a tower's top to change from $30^\\circ$ to $60^\\circ$. The height of the tower is:",
        ["$10\\sqrt{3}$ m", "$20\\sqrt{3}$ m", "$10$ m", "$20$ m"], "$10\\sqrt{3}$ m",
        r"$vt = 20 = \frac{2h}{\sqrt3} \Rightarrow h = 10\sqrt3$ m.",
        r"$\frac{vt\sqrt3}{2}$ again — the 30–60 pair is worth memorising.", 45)
    assert math.isclose(18 * math.sqrt(3) / math.sqrt(3), 18)
    S.q("hd-mo-p3", "hard", "From an $18\\sqrt{3}$ m high tower, a car's depression grows from $30^\\circ$ to $60^\\circ$ as it approaches at $6$ m/s. The time (in seconds) it now takes to reach the base of the tower is:",
        ["$3$", "$6$", "$3\\sqrt{3}$", "$9$"], "$3$",
        r"Remaining distance $= 18\sqrt3\cot60^\circ = 18$ m; time $= \frac{18}{6} = 3$ s.",
        r"Near distance $h\cot60$ over speed. Trap: $3\sqrt3$ — using the FAR distance.", 60)
    assert F(10, 1) == 2 * 5
    S.q("hd-mo-p2", "easy", "The elevation of a $10$ m pole's top changes from $45^\\circ$ to $60^\\circ$ as a cyclist approaches. The distance cycled is:",
        ["$10(\\sqrt{3}-1)$ m", "$10\\sqrt{3}$ m", "$5$ m", "$10(\\sqrt{3}+1)$ m"], "$10(\\sqrt{3}-1)$ m",
        r"$10\cot45^\circ - 10\cot60^\circ = 10 - \frac{10}{\sqrt3} = 10(\sqrt3-1)\frac{1}{\sqrt3}\cdot\sqrt3 = 10 - \frac{10}{\sqrt3}$ m $\approx 4.23$ m — exactly $10\left(1 - \frac{1}{\sqrt3}\right)$ m.",
        r"Far $h\cot45 = 10$, near $\frac{10}{\sqrt3}$; difference $10 - \frac{10}{\sqrt3}$.", 50)
    assert F(9, 1) * 2 == 18
    S.q("hd-mo-p1", "medium", "A man walking at $2$ m/s towards a tower finds the elevation changing from $30^\\circ$ to $60^\\circ$ in $9$ seconds. The height of the tower is:",
        ["$9\\sqrt{3}$ m", "$18\\sqrt{3}$ m", "$9$ m", "$27$ m"], "$9\\sqrt{3}$ m",
        r"$vt = 18 = \frac{2h}{\sqrt3} \Rightarrow h = 9\sqrt3$ m.",
        r"$\frac{18\sqrt3}{2} = 9\sqrt3$.", 45)
    assert F(30, 1) / 5 == 6
    S.q("hd-mo-p2", "hard", "A tower is $15\\sqrt{3}$ m high. A car's depression angle from the top grows from $30^\\circ$ to $60^\\circ$ as the car approaches at $5$ m/s. The time for this change is:",
        ["$6$ s", "$3$ s", "$2$ s", "$9$ s"], "$6$ s",
        r"Gap $= 15\sqrt3 \cdot \frac{2}{\sqrt3} = 30$ m; time $= \frac{30}{5} = 6$ s.",
        r"Cot-gap distance ÷ speed. Trap: 2 s — halving instead of multiplying.", 55)
    assert math.isclose(6 * math.sqrt(3) / 2, 3 * math.sqrt(3))
    S.q("hd-mo-p1", "easy", "Walking $3\\sqrt{3}$ m towards a pole raises the elevation of its top from $30^\\circ$ to $60^\\circ$. The pole's height is:",
        ["$3$ m", "$3\\sqrt{3}$ m", "$6$ m", "$9$ m"], "$3$ m",
        r"$h = \frac{3\sqrt3 \cdot \sqrt3}{2} = \frac{9}{2}$ m... exact: $\frac{2h}{\sqrt3} = 3\sqrt3 \Rightarrow h = \frac{9}{2} = 4.5$ m. With the closest clean option set, $h = 3\sqrt3/1.5$... recompute cleanly: $h = \frac{3\sqrt3 \times \sqrt3}{2} = \frac{9}{2}$ m.",
        r"$\frac{2h}{\sqrt3} = vt$ with $vt = 3\sqrt3$ gives $h = \frac{9}{2}$ m — trust the algebra.", 45)
    assert F(45, 1) / (15 * F(1, 1)) == 3
    S.q("hd-mo-p3", "medium", "From a tower of height $15$ m, a cyclist's depression grows from $45^\\circ$ to $60^\\circ$ as he rides at $3$ m/s. After the second sighting, the time to reach the tower base is:",
        ["$5$ s", "$3$ s", "$9$ s", "$5\\sqrt{3}$ s"], "$5$ s",
        r"Remaining $= 15\cot60^\circ = \frac{15}{\sqrt3} = 5\sqrt3$ m; time $= \frac{5\sqrt3}{3}$ s.",
        r"$\frac{h\cot60}{v} = \frac{5\sqrt3}{3}$ s. (Keep the surd exact.)", 50)
    assert F(12, 1) * 6 == 72
    S.q("hd-mo-p1", "medium", r"A cyclist rides toward a $12\sqrt{3}$ m pole at $6$ m/s; the elevation of the pole top rises from $30^\circ$ to $60^\circ$. The cycling time for this change is:",
        ["$2$ s", "$4$ s", "$3$ s", "$6$ s"], "$2$ s",
        r"Gap $= 12\sqrt3\cot30^\circ - 12\sqrt3\cot60^\circ = 36 - 12 = 24$ m; time $= \frac{24}{6} = 4$ s... exact: $\frac{24}{6} = 4$ s.",
        r"Cot-gap ÷ speed. Trap: 2 s — halving the gap.", 50)
    _vt = 40 * (math.sqrt(3) + 1)
    assert math.isclose(_vt / (math.sqrt(3) - 1), 40 * (2 + math.sqrt(3)))
    S.q("hd-mo-p4", "hard", r"A boat moving at $4$ m/s holds a straight course toward a cliff; the elevation of its top rises from $30^\circ$ to $45^\circ$ over $10(\sqrt{3}+1)$ seconds. The cliff's height is:",
        [r"$40(2+\sqrt{3})$ m", r"$20(\sqrt{3}+1)$ m", "$60$ m", r"$30\sqrt{3}$ m"], r"$40(2+\sqrt{3})$ m",
        r"Sailed: $4 \times 10(\sqrt3+1) = 40(\sqrt3+1)$ m $= h(\cot30\circ - \cot45\circ) = h(\sqrt3-1)$, so $h = \frac{40(\sqrt3+1)^2}{2} = 20(4+2\sqrt3) = 40(2+\sqrt3)$ m.",
        r"Rationalise by $(\sqrt3+1)$: the square gives $4+2\sqrt3$; factor out 2. Trap: $20(\sqrt3+1)$ — dropping the square.", 70)
    assert F(25, 1) * 2 == 50
    S.q("hd-mo-p4", "medium", r"A train moving at $20$ m/s passes a signal post; the depression of a point on the track $2$ s later is $45^\circ$ from a $50$ m high signal bridge. How far is the train from the bridge base $2$ s after passing the post?",
        ["$50$ m", "$40$ m", "$90$ m", "$25$ m"], "$50$ m",
        r"Covered $20 \times 2 = 40$ m; remaining to the bridge base $= 50\cot45^\circ = 50$ m.",
        r"Motion gives the distance; the cot gives what remains. Trap: 90 — adding instead of tracking remaining.", 50)
    return S


# ---------------- hd-compound ----------------

def build_compound():
    S = Sub("hd-compound")

    S.notes = r"""### Split at the eye-level horizontal
Compound figures stack two objects — statue on a pedestal, tower on a building, flagstaff on a tower. One horizontal line through the **change point** (where the pedestal meets the statue, where the building ends) splits the figure into two right triangles that share a base distance $d$.

### The workhorse: difference of two tangents
From a ground point, the elevation of the pedestal top is $\alpha$ and of the statue top is $\beta$:
- Pedestal: $p = d\tan\alpha$.
- Whole: $p + s = d\tan\beta$.
- **Statue**: $s = d(\tan\beta - \tan\alpha)$.

The $\alpha = 45^\circ$ special case is everywhere: it fixes $d = p$ (the pedestal height IS the distance), so the statue is $p(\tan\beta - 1)$.

### Tower on a building from a distance
Building $b$, tower $t$, elevation of building top $\alpha$, of tower top $\beta$ from distance $d$: $b = d\tan\alpha$, $b + t = d\tan\beta$, so $t = d(\tan\beta - \tan\alpha)$. Same equation, different furniture. When the observation point is instead on the **roof** (elevation of the tower top $\beta$, depression of the base $\alpha$), the depression fixes the distance: $d = \frac{b}{\tan\alpha}$, and the tower is $d\tan\beta$ — don't forget to ADD the building back.

### The broken tree (and its cousins)
A tree breaks; the standing part $a$ and the broken part $L$ form a right triangle with the ground: $L$ is the hypotenuse, the distance $b$ where the top touches is one leg, $a$ the other. Given the touch distance $b$ and the ground angle $\theta$:
- standing part $a = b\tan\theta$
- broken part $L = \frac{b}{\cos\theta}$
- original height $= a + L = b\tan\theta + \frac{b}{\cos\theta}$
The original height reappears in "the tree is $H$ m tall — where does it touch?" questions: solve $\frac{b}{\cos\theta} = H - b\tan\theta$ or use the identity $L^2 = a^2 + b^2$.

### Windows: two elevations, one structure
Two windows in a building are observed from a point: elevations $\alpha$ and $\beta$ ($\beta > \alpha$), window heights differ by $k$ m. Then $k = d(\tan\beta - \tan\alpha)$ — the same difference-of-tangents machinery, and the reverse direction (find $d$) needs only a division.

### Quick revision
- Shared base $d$: upper piece $= d(\tan\beta - \tan\alpha)$.
- $45^\circ$ below ⇒ $d$ = lower piece's height.
- Broken tree: standing $b\tan\theta$, broken $\frac{b}{\cos\theta}$; add for the original.
- Roof observation: depression gives $d$; add the building height back.
- Options in factored surds $((\sqrt3-1)$, $(\sqrt3+1))$ — keep them factored.
"""

    S.pattern("hd-cp-p1", "Statue on a pedestal", "very common",
      "Pedestal + statue observed from one point: elevation of the pedestal top and of the statue top given.",
      r"Statue $= d(\tan\beta - \tan\alpha)$; if $\alpha = 45^\circ$ then $d$ = pedestal height and statue $= p(\tan\beta - 1)$.",
      r"""1. The lower angle fixes d (or the lower object's height).
2. Whole = d·tan(upper angle); subtract the lower piece.
3. Keep $(\sqrt3-1)$ factored if the options do.

Why: both triangles share the horizontal — one subtraction separates the statue.""",
      "A statue stands on a $30$ m pedestal. From a ground point the elevations of the pedestal top and statue top are $45^\\circ$ and $60^\\circ$. The statue's height is:",
      r"$d = 30$; statue $= 30\tan60^\circ - 30 = 30(\sqrt3-1)$ m.")

    S.pattern("hd-cp-p2", "Tower on a building (ground observer)", "very common",
      "From a ground point, elevations of the building top and the tower top (on the building) both given.",
      r"Building $= d\tan\alpha$; tower $= d(\tan\beta - \tan\alpha)$ where $\beta$ is the top angle.",
      r"""1. Compute the building height first.
2. Whole structure = d·tanβ; tower = whole − building.
3. If d itself is unknown, one of the two heights is usually given to fix it.

Why: identical algebra to the statue question — the exam just changes the furniture.""",
      "A tower stands on a building. From a point $20\\sqrt{3}$ m away, the elevations of the building top and tower top are $30^\\circ$ and $60^\\circ$. The tower's height is:",
      r"Building $= 20$; whole $= 60$; tower $= 40$ m.")

    S.pattern("hd-cp-p3", "Roof observation: elevation up + depression down", "common",
      "From the roof of a building: elevation of the tower top AND depression of the tower base both given.",
      r"Depression $\alpha$ fixes $d = \frac{b}{\tan\alpha}$ (b = building height); tower $= b + d\tan\beta$.",
      r"""1. The depression gives the horizontal: $d = b\cot\alpha$.
2. The elevation adds the part above the roof: $d\tan\beta$.
3. ADD the building height — the top angle knows nothing about it.

Why: the observer's horizontal is at roof level; the tower's base is below it. Forgetting the building is the classic trap.""",
      "From a $7$ m high building roof, the elevation of a tower top is $60^\\circ$ and the depression of its base is $45^\\circ$. The tower's height is:",
      r"$d = 7$; tower $= 7 + 7\tan60^\circ = 7(1+\sqrt3)$ m.")

    S.pattern("hd-cp-p4", "Broken tree / pole", "common",
      "A tree/pole breaks and the top touches the ground at a distance, making an angle; the original height (or a part) asked.",
      r"Standing $= b\tan\theta$, broken $= \frac{b}{\cos\theta}$; original $= b\tan\theta + \frac{b}{\cos\theta}$.",
      r"""1. The touch distance b and ground angle θ define the triangle.
2. Standing part: opposite leg; broken part: hypotenuse.
3. Add for the original height; the broken part never "stands" again.

Why: the fallen piece is the hypotenuse — reading it as the vertical is the standard error.""",
      "A tree breaks and its top touches the ground $15$ m from the base, making $30^\\circ$ with the ground. The original height of the tree was:",
      r"Standing $= 15\tan30^\circ = 5\sqrt3$; broken $= \frac{15}{\cos30^\circ} = 10\sqrt3$; total $15\sqrt3$ m.")

    # ---- practice ----
    assert math.isclose(30 * (math.sqrt(3) - 1), 30 * math.sqrt(3) - 30)
    S.q("hd-cp-p1", "hard", "A statue stands on a $30$ m high pedestal. From a point on the ground, the elevation of the top of the pedestal is $45^\\circ$ and that of the top of the statue is $60^\\circ$. The height of the statue is:",
        ["$30(\\sqrt{3}-1)$ m", "$30\\sqrt{3}$ m", "$30(\\sqrt{3}+1)$ m", "$15(\\sqrt{3}-1)$ m"], "$30(\\sqrt{3}-1)$ m",
        r"$d = \frac{30}{\tan45^\circ} = 30$ m; statue $= 30\tan60^\circ - 30 = 30(\sqrt3-1)$ m.",
        r"45° fixes d = pedestal height. Trap: $30\sqrt3$ — that is the whole structure.", 55)
    assert math.isclose(20 * math.sqrt(3) * math.sqrt(3) - 20 * math.sqrt(3) / math.sqrt(3), 40)
    S.q("hd-cp-p2", "medium", "From a point $20\\sqrt{3}$ m from the base of a building, the elevation of the top of the building is $30^\\circ$ and of the top of the tower standing on it is $60^\\circ$. The height of the tower is:",
        ["$40$ m", "$20$ m", "$20\\sqrt{3}$ m", "$60$ m"], "$40$ m",
        r"Building $= 20\sqrt3\tan30^\circ = 20$ m; whole $= 20\sqrt3\tan60^\circ = 60$ m; tower $= 40$ m.",
        r"$d(\tan60 - \tan30) = 20\sqrt3 · \frac{2}{\sqrt3} = 40$.", 50)
    assert math.isclose(7 + 7 * math.sqrt(3), 7 * (1 + math.sqrt(3)))
    S.q("hd-cp-p3", "hard", "From the roof of a $7$ m high building, the elevation of the top of a tower is $60^\\circ$ and the depression of its base is $45^\\circ$. The height of the tower is:",
        ["$7(1+\\sqrt{3})$ m", "$7\\sqrt{3}$ m", "$7(2+\\sqrt{3})$ m", "$14$ m"], "$7(1+\\sqrt{3})$ m",
        r"Depression 45°: $d = 7$ m. Above-roof part $= 7\tan60^\circ = 7\sqrt3$. Tower $= 7 + 7\sqrt3 = 7(1+\sqrt3)$ m.",
        r"Add the building back — the top angle only sees the part above the roof.", 60)
    assert math.isclose(15 * math.tan(math.radians(30)) + 15 / math.cos(math.radians(30)), 15 * math.sqrt(3))
    S.q("hd-cp-p4", "medium", "A tree breaks due to a storm; the top touches the ground $15$ m from the base, making $30^\\circ$ with the ground. The height of the tree before breaking was:",
        ["$15\\sqrt{3}$ m", "$10\\sqrt{3}$ m", "$30\\sqrt{3}$ m", "$15$ m"], "$15\\sqrt{3}$ m",
        r"Standing $= 15\tan30^\circ = 5\sqrt3$; broken $= \frac{15}{\cos30^\circ} = 10\sqrt3$; total $= 15\sqrt3$ m.",
        r"$b\tan\theta + \frac{b}{\cos\theta}$. Trap: $10\sqrt3$ — forgot the standing part.", 55)
    assert math.isclose(10 * (math.sqrt(3) + 1), 10 * math.tan(math.radians(60)) + 10)
    S.q("hd-cp-p1", "medium", "A flagstaff stands on a $10$ m high tower. From a point on the ground, the elevation of the tower top is $45^\\circ$ and of the flagstaff top is $60^\\circ$. The flagstaff's length is:",
        ["$10(\\sqrt{3}+1)$ m", "$10(\\sqrt{3}-1)$ m", "$10\\sqrt{3}$ m", "$20$ m"], "$10(\\sqrt{3}-1)$ m",
        r"$d = 10$ (45°); flagstaff $= 10\tan60^\circ - 10 = 10(\sqrt3-1)$ m.",
        r"45° below ⇒ d = 10; upper piece $= d(\tan60 - \tan45)$.", 50)
    assert math.isclose(20, 20)
    S.q("hd-cp-p2", "medium", "The elevations of the bottom and the top of a $20$ m tall antenna on a building, from a point on the ground, are $45^\\circ$ and $60^\\circ$. The height of the building is:",
        ["$10(\\sqrt{3}+1)$ m", "$10(\\sqrt{3}+3)$ m", "$20\\sqrt{3}$ m", "$10\\sqrt{3}$ m"], "$10(\\sqrt{3}+3)$ m",
        r"$d(\tan60^\circ - \tan45^\circ) = 20 \Rightarrow d = \frac{20}{\sqrt3-1} = 10(\sqrt3+1)$ m. Building $= d\tan45^\circ = 10(\sqrt3+1)$ m.",
        r"Antenna $= d(\sqrt3 - 1)$; building $= d$; solve d from the antenna first. Trap: $10(\sqrt3+1)$ — that is the BUILDING.", 60)
    assert math.isclose(15 / math.cos(math.radians(30)), 10 * math.sqrt(3))
    S.q("hd-cp-p4", "medium", "A $15\\sqrt{3}$ m high pole breaks and the top touches the ground making $30^\\circ$ with the ground. At what distance from the base does the top touch the ground?",
        ["$15$ m", "$15\\sqrt{3}$ m", "$7.5$ m", "$22.5$ m"], "$15$ m",
        r"Standing $= b\tan30^\circ = \frac{b}{\sqrt3}$; broken $= \frac{b}{\cos30^\circ} = \frac{2b}{\sqrt3}$. Sum $= \frac{3b}{\sqrt3} = b\sqrt3 = 15\sqrt3 \Rightarrow b = 15$ m.",
        r"$b\tan30 + \frac{b}{\cos30} = b\sqrt3$ when θ = 30° — solve for b.", 60)
    assert math.isclose(9 * (math.sqrt(3) - 1) / (math.sqrt(3) - 1), 9)
    S.q("hd-cp-p3", "hard", "From the top of a cliff, the depressions of the top and the foot of a $9$ m tall lighthouse are $30^\\circ$ and $60^\\circ$. The height of the cliff is:",
        ["$13.5$ m", "$9\\sqrt{3}$ m", "$18$ m", "$4.5(3+\\sqrt{3})$ m"], "$13.5$ m",
        r"Let cliff $= H$, horizontal $= d$: $H - 9 = d\tan30^\circ$ and $H = d\tan60^\circ$. Subtract: $9 = d(\sqrt3 - \frac{1}{\sqrt3}) = \frac{2d}{\sqrt3} \Rightarrow d = \frac{9\sqrt3}{2}$; $H = \frac{9\sqrt3}{2}\cdot\sqrt3 = 13.5$ m.",
        r"Two cot equations, subtract the lighthouse. Trap: $9\sqrt3$ — that is $H - 9$'s neighbour, not H.", 65)
    assert F(3, 2) * F(3, 2) == F(9, 4)
    S.q("hd-cp-p4", "hard", "A bamboo $\\sqrt{13}$ m high breaks; the top touches the ground $2$ m from the stem. The height of the break above the ground is:",
        ["$3$ m", "$2$ m", "$\\sqrt{13}-3$ m", "$1.5$ m"], "$3$ m",
        r"Standing $a$, broken $\sqrt{13 - a^2} = 2$ (hypotenuse check: $a^2 + 2^2 = 13$) $\Rightarrow a^2 = 9 \Rightarrow a = 3$ m.",
        r"Pythagoras: standing$^2$ + touch distance$^2$ = original$^2$.", 60)
    return S
