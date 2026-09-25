"""Phase-2 deep content for quant/heights-distances — basics, standard angles."""
import math

from fractions import Fraction as F

from _lib import Sub


# ---------------- hd-basics ----------------

def build_basics():
    S = Sub("hd-basics")

    S.notes = r"""### The picture is half the answer
Every heights-and-distances question is one right triangle wearing a story. The observer's **eye** is the starting point; through it runs a dashed **horizontal line**.
- Object **above** eye level: the angle from the horizontal **up** to the line of sight is the **angle of elevation**.
- Object **below** eye level: the angle **down** from the horizontal is the **angle of depression**.

The right angle sits between the horizontal and the vertical, so the trigonometry is always $\tan\theta = \frac{\text{height above or below eye level}}{\text{horizontal distance}}$.

### Eye level, not ground level
When the observer stands on a cliff, tower or building, the height asked is measured from the **eye**, and the ground distance runs from the **base of the object**. A 1.6 m tall person watching a kite: the kite's height above ground is $1.6 + d\tan\theta$. Exams keep the observer's height either zero or clearly stated — but the *eye* is always where the horizontal starts.

### Depression mirrors elevation
The angle of depression from the observer equals the angle of elevation from the object — alternate interior angles between two parallels (the two horizontals). So "from a lighthouse the depression of a boat is $30^\circ$" converts instantly to "from the boat the elevation of the lighthouse top is $30^\circ$", and the standard-angle rules apply unchanged. This one flip solves every lighthouse, cliff and aeroplane question.

### Reading the question into the figure
Four phrases carry all the information:
- "subtends an angle $\theta$ at a point" → the elevation at that point is $\theta$;
- "the angle changes from $\alpha$ to $\beta$ as he walks $d$ **towards**" → two positions on the same side, distance $d$ apart, $\beta > \alpha$;
- "observed from the top ... the angles of depression of two ships are ..." → same-side two-angle case, gap $= h(\cot\alpha - \cot\beta)$;
- "shadow is $k$ times the height" → $\tan(\text{sun elevation}) = \frac{1}{k}$.

### Distances that are NOT on the same line
Two points not collinear with the base (e.g. two corners of a street seen from a window): each gets its own right triangle, and the two base distances may themselves form a right angle — Pythagoras joins the party. "The bearings of the two cars differ by $90^\circ$" means their base distances are perpendicular legs and the distance between the cars is the hypotenuse. Sketch the plan view separately from the side view; exam questions love mixing the two.

### Quick revision
- Eye = origin; horizontal = baseline; elevation up, depression down.
- $\tan\theta = \frac{\text{height above/below eye level}}{\text{horizontal distance}}$.
- Depression at the top = elevation at the bottom (alternate angles).
- Observer on a platform: add the platform height at the end.
- "Subtends an angle at P" = elevation measured at P.
"""

    S.pattern("hd-ba-p1", "Single angle, eye-level work", "very common",
      "One angle and one of {height, distance} given; the other asked — including platform/cliff eye heights.",
      r"$\tan\theta = \frac{h}{d}$ w.r.t. the EYE level; add the observer's platform height if the question wants ground height.",
      r"""1. Draw the horizontal through the eye; mark the angle.
2. Write one tangent equation in the unknown.
3. Add the eye height (if any) before answering ground heights.

Why: everything else in the figure is decoration — one right triangle decides.""",
      "A kite is flying with $30^\\circ$ elevation from a point on level ground. If the kite's thread (assumed straight) is $100$ m long, the kite's height above the ground is:",
      r"$h = 100\sin30^\circ = 50$ m (the thread is the hypotenuse).")

    S.pattern("hd-ba-p2", "Angle of depression conversions", "very common",
      "Lighthouse/cliff/aeroplane looking down at boats, cars or road junctions; depression angle stated.",
      r"Depression at the eye = elevation at the object; then $d = \frac{h}{\tan\theta}$. Two objects on one side → subtract the two horizontal distances.",
      r"""1. Flip the depression into an elevation at the object.
2. Apply the standard-angle rule or a single tangent.
3. For two objects, compute both distances from the base and subtract.

Why: the flip turns a "looking down" story into the ordinary up-the-tower triangle.""",
      "From a $20$ m high tower the angle of depression of a car is $45^\\circ$. The car's distance from the tower base is:",
      r"$\tan45^\circ = \frac{20}{d} \Rightarrow d = 20$ m.")

    S.pattern("hd-ba-p3", "Hypotenuse (thread/ladder/line-of-sight) given", "common",
      "The slant distance — thread, ladder, wire, 'direct distance' — is given instead of the horizontal.",
      r"$h = L\sin\theta$, $d = L\cos\theta$: the slant line is the hypotenuse, so sine and cosine (not tangent).",
      r"""1. Name the hypotenuse explicitly.
2. Height = L·sin(angle), ground distance = L·cos(angle).
3. Standard-angle values keep answers exact.

Why: tangent mixes the two legs; with the hypotenuse given, tan is the wrong tool.""",
      "A cable of length $60$ m runs from the top of a pole to the ground making $60^\\circ$ with the ground. The pole's height is:",
      r"$h = 60\sin60^\circ = 60 \times \frac{\sqrt3}{2} = 30\sqrt3$ m.")

    S.pattern("hd-ba-p4", "Shadow geometry", "common",
      "A pole/building casts a shadow; the sun's elevation, the shadow length or the height is the unknown.",
      r"Shadow = horizontal distance: $\tan(\text{elevation}) = \frac{\text{height}}{\text{shadow}}$. Equal shadows at the same moment ⇒ equal heights; shadow $= \sqrt3 h$ means $30^\circ$, shadow $= h$ means $45^\circ$.",
      r"""1. Sun rays make the elevation angle with the ground; the triangle is pole–shadow–ray.
2. Match the shadow:height ratio to a standard angle.
3. Two poles at the same moment share the same sun angle — set up ratios, not two triangles.

Why: the sun's angle is the same for every object at one moment, which is the entire content of "at the same time".""",
      "A vertical stick $1.5$ m long casts a shadow $2.5$ m long on level ground. At the same time a tower casts a shadow $75$ m long. The tower's height is:",
      r"Same sun angle: $\frac{h}{75} = \frac{1.5}{2.5} \Rightarrow h = 45$ m.")

    # ---- practice ----
    assert math.isclose(100 * math.sin(math.radians(30)), 50)
    S.q("hd-ba-p1", "easy", "A kite is flying with $30^\\circ$ elevation from a point on level ground. If the kite's thread (assumed straight) is $100$ m long, the kite's height above the ground is:",
        ["$50$ m", "$100$ m", "$50\\sqrt{3}$ m", "$\\frac{100}{\\sqrt{3}}$ m"], "$50$ m",
        r"$h = 100\sin30^\circ = 50$ m.",
        r"Hypotenuse × sin. Trap: $50\sqrt3$ — that uses cos.", 30)
    assert 20 * 1 == 20
    S.q("hd-ba-p2", "easy", "From a $20$ m high tower, the angle of depression of a car on level ground is $45^\\circ$. The car's distance from the base of the tower is:",
        ["$20$ m", "$20\\sqrt{3}$ m", "$\\frac{20}{\\sqrt{3}}$ m", "$40$ m"], "$20$ m",
        r"Depression $45^\circ$ = elevation $45^\circ$: $\tan45^\circ = \frac{20}{d} \Rightarrow d = 20$ m.",
        r"45° → distance = height. Trap: $20\sqrt3$ — that is the 30° rule.", 30)
    assert math.isclose(60 * math.sqrt(3) / 2, 30 * math.sqrt(3))
    S.q("hd-ba-p3", "medium", "A cable of length $60$ m runs from the top of a pole to the ground, making $60^\\circ$ with the ground. The height of the pole is:",
        ["$30\\sqrt{3}$ m", "$60\\sqrt{3}$ m", "$30$ m", "$20\\sqrt{3}$ m"], "$30\\sqrt{3}$ m",
        r"$h = 60\sin60^\circ = 60 \times \frac{\sqrt3}{2} = 30\sqrt3$ m.",
        r"Hypotenuse × sin60. Trap: $60\sqrt3$ — forgetting to halve.", 35)
    assert F(3, 2) * F(30, 1) == F(45, 1)
    S.q("hd-ba-p4", "medium", "A vertical stick $1.5$ m long casts a shadow $2.5$ m long. At the same time, a nearby tower casts a shadow $75$ m long. The height of the tower is:",
        ["$45$ m", "$50$ m", "$40$ m", "$75$ m"], "$45$ m",
        r"Same sun angle: $\frac{h}{75} = \frac{1.5}{2.5} \Rightarrow h = 75 \times \frac{3}{5} = 45$ m.",
        r"Ratio trick: height = shadow × (stick/shadow-stick) = $75 × 0.6$.", 40)
    assert math.isclose(30 * math.cos(math.radians(60)), 15)
    S.q("hd-ba-p3", "easy", "A ladder of length $30$ m leans against a wall at $60^\\circ$ to the ground. The foot of the ladder is at what distance from the wall?",
        ["$15$ m", "$15\\sqrt{3}$ m", "$30\\sqrt{3}$ m", "$10$ m"], "$15$ m",
        r"$d = 30\cos60^\circ = 30 \times \frac12 = 15$ m.",
        r"Cos for the ground leg. Trap: $15\sqrt3$ — that is the wall height side.", 30)
    assert F(20, 1) * F(1, 1) == 20
    S.q("hd-ba-p2", "easy", "From the top of a cliff $80$ m high, the angle of depression of a ship is $45^\\circ$. The distance of the ship from the foot of the cliff is:",
        ["$80$ m", "$80\\sqrt{3}$ m", "$40$ m", "$\\frac{80}{\\sqrt{3}}$ m"], "$80$ m",
        r"Depression $45^\circ$ = elevation $45^\circ$: $d = \frac{80}{\tan45^\circ} = 80$ m.",
        r"45° flip → distance = height.", 30)
    assert math.isclose(50 * math.sin(math.radians(45)) * math.sqrt(2), 50)
    S.q("hd-ba-p3", "medium", "A straight wire from the top of a $50$ m tower reaches the ground $50$ m from the base. The angle the wire makes with the ground is:",
        ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$75^\\circ$"], "$45^\\circ$",
        r"$\tan\theta = \frac{50}{50} = 1 \Rightarrow \theta = 45^\circ$ (the wire length $50\sqrt2$ m is a distractor).",
        r"Height = ground distance → 45°. Trap: using the wire as if tangent asked for it.", 35)
    assert F(9, 1) * 2 == 18
    S.q("hd-ba-p4", "easy", "The shadow of a tower is $18$ m long when the sun's elevation is $45^\\circ$. The height of the tower is:",
        ["$18$ m", "$18\\sqrt{3}$ m", "$9$ m", "$36$ m"], "$18$ m",
        r"$\tan45^\circ = \frac{h}{18} \Rightarrow h = 18$ m.",
        r"45° → shadow = height.", 25)
    assert math.isclose(100 * math.cos(math.radians(30)), 100 * math.sqrt(3) / 2)
    S.q("hd-ba-p1", "medium", "From a point on the ground, the elevation of an aeroplane is $60^\\circ$. If the plane is $1000$ m away along the line of sight, its height above the ground is:",
        ["$500\\sqrt{3}$ m", "$1000$ m", "$500$ m", "$1000\\sqrt{3}$ m"], "$500\\sqrt{3}$ m",
        r"$h = 1000\sin60^\circ = 500\sqrt3$ m.",
        r"Line of sight = hypotenuse: sin60. Trap: $1000\sqrt3$ (used tan60 on the hypotenuse).", 35)
    assert F(2, 5) * F(25, 1) == 10
    S.q("hd-ba-p4", "medium", "A pole $10$ m high casts a shadow $25$ m long. At the same moment, the shadow of a building is $90$ m. The building's height is:",
        ["$36$ m", "$40$ m", "$45$ m", "$30$ m"], "$36$ m",
        r"Same sun angle: $\frac{H}{90} = \frac{10}{25} \Rightarrow H = 36$ m.",
        r"$90 × \frac{10}{25} = 36$. Trap: $40$ — dividing 90 by the pole height ratio inverted.", 35)
    assert math.isclose(80 / math.sqrt(3) * (math.sqrt(3) - 1 / math.sqrt(3)), 160 / 3)
    S.q("hd-ba-p2", "hard", r"From a $\frac{80}{\sqrt{3}}$ m high tower, the angles of depression of two cars due north of it are $60^\circ$ and $30^\circ$. The distance between the cars is:",
        ["$\\frac{80}{\\sqrt{3}}$ m", "$\\frac{160}{3}$ m", "$80\\sqrt{3}$ m", "$\\frac{160\\sqrt{3}}{3}$ m"], "$\\frac{160}{3}$ m",
        r"Distances: $\frac{80}{\sqrt3}\cot60^\circ = \frac{80}{3}$ and $\frac{80}{\sqrt3}\cot30^\circ = 80$. Gap $= 80 - \frac{80}{3} = \frac{160}{3}$ m.",
        r"Far minus near, both scaled by $h$. Trap: $\frac{160\sqrt3}{3}$ — a slipped surd.", 60)
    return S


# ---------------- hd-standard-angles ----------------

def build_standard():
    S = Sub("hd-standard-angles")

    S.notes = r"""### The three multipliers
Almost every exam question uses only $30^\circ$, $45^\circ$ or $60^\circ$. Convert each to a **height–distance rule** and the tangent table becomes a cheat sheet:

| $\theta$ | $\tan\theta$ | rule ($h$ up, $d$ across) |
|---|---|---|
| $30^\circ$ | $\frac{1}{\sqrt3}$ | $d = \sqrt3\,h$ |
| $45^\circ$ | $1$ | $d = h$ |
| $60^\circ$ | $\sqrt3$ | $d = \frac{h}{\sqrt3}$ |

Read the pair as a swap: at $30^\circ$ the distance is $\sqrt3$ times the height; at $60^\circ$ the height is $\sqrt3$ times the distance. Ratios like $\frac{h}{d}$ identify the angle from either side.

### Keeping surds exact
$\sqrt3 \approx 1.732$ and $\sqrt2 \approx 1.414$ — but only reach for decimals if the options are decimal. An answer of $\frac{40}{\sqrt3}$ rationalises to $\frac{40\sqrt3}{3}$; the options may present either form, so carry the radical and match at the end. Every "odd" distractor is a surd in the wrong slot ($h\sqrt3$ vs $\frac{h}{\sqrt3}$ is the single most common trap).

### Angles that are not 30-45-60
Elevations like $15^\circ$, $75^\circ$ or $22.5^\circ$ do appear — as *differences* of standard angles. $15^\circ = 45^\circ - 30^\circ$, $75^\circ = 45^\circ + 30^\circ$; the compound expressions $\tan(45^\circ \pm \theta) = \frac{1 \pm \tan\theta}{1 \mp \tan\theta}$ finish them in one line. A question using $75^\circ$ is almost always a $45+30$ identity question in disguise.

### The ladder and the hypotenuse rule
When the slant length (ladder, thread, wire) is the given, switch to sine and cosine: $h = L\sin\theta$, $d = L\cos\theta$. The classic check: a $45^\circ$ ladder of length $L\sqrt2$ climbs exactly $L$ — the $45^\circ$ isosceles right triangle always has hypotenuse $\sqrt2$ times a leg.

### Combination moves with the same angle twice
Two objects at the same standard angle from two positions of known separation (e.g. two towers seen from a point between them at $30^°$ each, separation $D$): the heights are $\frac{D}{2\sqrt3}$ each — equal heights, equal angles. When the angles differ, each height uses its own tangent against the half-separation. A chain of two standard-angle steps (walk 10 m at 30°, then 10 m more at 45°) is just two single-angle equations written in sequence and subtracted; nothing new is needed beyond bookkeeping.

### Quick revision
- $30^\circ$: $d = \sqrt3 h$; $45^\circ$: $d = h$; $60^\circ$: $h = \sqrt3 d$.
- $\frac{h}{d} = \frac{1}{\sqrt3}$ → 30°, $= 1$ → 45°, $= \sqrt3$ → 60°.
- Shadow $= \sqrt3 h$ at 30°; shadow $= h$ at 45°; shadow $= \frac{h}{\sqrt3}$ at 60°.
- Hypotenuse given: $L\sin\theta$ up, $L\cos\theta$ across.
- $15^\circ$ and $75^\circ$ are $45 \mp 30$ identities in disguise.
"""

    S.pattern("hd-sa-p1", "Height from distance (or reverse) at a standard angle", "very common",
      "One standard angle, height or distance given, the other asked — often dressed as a tower, statue, pole or hill.",
      r"$30^\circ \to d = \sqrt3 h$; $45^\circ \to d = h$; $60^\circ \to d = \frac{h}{\sqrt3}$. Keep surds exact and match the option form at the end.",
      r"""1. Write the rule for the stated angle before touching numbers.
2. Substitute; rationalise only if the options demand it.
3. Check the size: 60° puts the point CLOSER than the height; 30° puts it FARTHER.

Why: the whole question is one table lookup — the difficulty is only in the surd bookkeeping.""",
      "The elevation of the top of a tower from a point $30\\sqrt3$ m from its base is $30^\\circ$. The tower's height is:",
      r"$h = \frac{30\sqrt3}{\sqrt3} = 30$ m.")

    S.pattern("hd-sa-p2", "Reading the angle from a ratio", "common",
      "'The shadow is √3 times the height' or 'height equals distance' — the angle itself is the answer.",
      r"$\tan\theta = \frac{h}{d}$: shadow $\sqrt3 h$ → $30^\circ$; equal → $45^\circ$; shadow $= \frac{h}{\sqrt3}$ → $60^\circ$.",
      r"""1. Write tan as height over distance (shadow IS the distance).
2. Reduce the ratio to a table value.
3. Quote the angle — no further computation exists.

Why: the inverse direction of the standard rules; the same three numbers appear in reverse.""",
      "When the sun's elevation is such that a pole's shadow equals the pole's height, the elevation is:",
      r"$\tan\theta = \frac{h}{h} = 1 \Rightarrow \theta = 45^\circ$.")

    S.pattern("hd-sa-p3", "Ladder / wire sliding geometry", "occasional",
      "A ladder leaning at a standard angle; the height reached or the foot distance (or the length itself) asked.",
      r"$h = L\sin\theta$, $d = L\cos\theta$. $45^\circ$ → $h = d = \frac{L}{\sqrt2}$; $30^\circ$ → $h = \frac{L}{2}$; $60^\circ$ → $h = \frac{L\sqrt3}{2}$.",
      r"""1. The ladder is the hypotenuse — sin and cos only.
2. At 30° the vertical is exactly half the ladder (sin30 = ½).
3. Sanity-check with the isosceles case: 45° puts the foot at $L/\sqrt2$.

Why: 30-60-90 triangles have sides $1 : \sqrt3 : 2$ — half the ladder is the shortest side.""",
      "A ladder $20$ m long rests at $30^\\circ$ against a wall. How high up the wall does it reach?",
      r"$h = 20\sin30^\circ = 10$ m.")

    S.pattern("hd-sa-p4", "45+30 identity angles (15°, 75°)", "occasional",
      "Elevation stated as 15° or 75°, or a tan(45°±θ) expression appears inside the question.",
      r"$\tan(45^\circ \pm \theta) = \frac{1 \pm \tan\theta}{1 \mp \tan\theta}$; with $\theta = 30^\circ$: $\tan75^\circ = 2+\sqrt3$, $\tan15^\circ = 2-\sqrt3$.",
      r"""1. Split the odd angle as 45 ± 30.
2. Apply the compound formula; memorise the two finished values.
3. Expect a factored surd answer $(2 \pm \sqrt3)$ — do not decimalise.

Why: 15°/75° triangles are the standard "hard" elevations; the formula turns them into one substitution.""",
      "The value of $\\tan 15^\\circ \\tan 75^\\circ$ is:",
      r"$(2-\sqrt3)(2+\sqrt3) = 4 - 3 = 1$ (they are complementary).")

    # ---- practice ----
    assert F(30 * 3, 1) == 90
    S.q("hd-sa-p1", "easy", "The angle of elevation of the top of a tower from a point $30\\sqrt{3}$ m from its base is $30^\\circ$. The height of the tower is:",
        ["$30$ m", "$30\\sqrt{3}$ m", "$10\\sqrt{3}$ m", "$60$ m"], "$30$ m",
        r"$d = \sqrt3 h \Rightarrow h = \frac{30\sqrt3}{\sqrt3} = 30$ m.",
        r"30° → distance is √3 × height; divide back.", 30)
    assert F(20, 1) * 3 == 60
    S.q("hd-sa-p1", "easy", "A tree casts a shadow $60$ m long when the sun's elevation is $30^\\circ$. The height of the tree is:",
        ["$20\\sqrt{3}$ m", "$60$ m", "$20$ m", "$30\\sqrt{3}$ m"], "$20\\sqrt{3}$ m",
        r"$h = \frac{60}{\sqrt3} = 20\sqrt3$ m.",
        r"30°: height = shadow/√3 = $60/\sqrt3 = 20\sqrt3$. Trap: 20 — dividing twice.", 30)
    assert F(1, 1) == 1
    S.q("hd-sa-p2", "easy", "A pole casts a shadow equal to its own height. The sun's angle of elevation is:",
        ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$90^\\circ$"], "$45^\\circ$",
        r"$\tan\theta = \frac{h}{h} = 1 \Rightarrow \theta = 45^\circ$.",
        r"Equal shadow and height is the 45° signature.", 25)
    assert math.isclose(math.tan(math.radians(60)), math.sqrt(3))
    S.q("hd-sa-p1", "medium", "From a point $15$ m from the base of a flagstaff, the elevation of its top is $60^\\circ$. The height of the flagstaff is:",
        ["$15\\sqrt{3}$ m", "$5\\sqrt{3}$ m", "$15\\sqrt{2}$ m", "$30$ m"], "$15\\sqrt{3}$ m",
        r"$h = 15\tan60^\circ = 15\sqrt3$ m.",
        r"60° → height = √3 × distance. Trap: $5\sqrt3$ — that is the distance rule inverted.", 30)
    assert F(20, 2) == 10
    S.q("hd-sa-p3", "medium", "A ladder $20$ m long rests against a wall at $30^\\circ$ to the ground. The height it reaches on the wall is:",
        ["$10$ m", "$10\\sqrt{3}$ m", "$20\\sqrt{3}$ m", "$15$ m"], "$10$ m",
        r"$h = 20\sin30^\circ = 10$ m.",
        r"sin30 = ½ → half the ladder. Trap: $10\sqrt3$ — that is the foot distance ($20\cos30$).", 35)
    assert F(45, 1) * F(2, 1) == 90
    S.q("hd-sa-p1", "easy", "The elevation of a hilltop from a point $45$ m away (horizontal) is $60^\\circ$. The hill's height is:",
        ["$45\\sqrt{3}$ m", "$15\\sqrt{3}$ m", "$45\\sqrt{2}$ m", "$90$ m"], "$45\\sqrt{3}$ m",
        r"$h = 45\tan60^\circ = 45\sqrt3$ m.",
        r"60° multiplies the distance by √3.", 30)
    assert (2 + 3 ** 0.5) ** 2 + (2 - 3 ** 0.5) ** 2 - 14 < 1e-9  # tan²75 + tan²15 = 14
    S.q("hd-sa-p4", "hard", "The value of $\\tan^2 75^\\circ + \\tan^2 15^\\circ$ is:",
        ["$14$", "$10$", "$16$", "$4$"], "$14$",
        r"$\tan75^\circ = 2+\sqrt3$, $\tan15^\circ = 2-\sqrt3$. Sum of squares $= (2+\sqrt3)^2 + (2-\sqrt3)^2 = (7+4\sqrt3) + (7-4\sqrt3) = 14$.",
        r"$(a+b)^2 + (a-b)^2 = 2(a^2+b^2) = 2(4+3) = 14$. Trap: 10 — using $a^2 - b^2$.", 55)
    assert F(1, 2) == 0.5
    S.q("hd-sa-p3", "easy", "A $12$ m ladder leans at $45^\\circ$ against a vertical wall. The height it reaches is:",
        ["$6\\sqrt{2}$ m", "$6$ m", "$12\\sqrt{2}$ m", "$12$ m"], "$6\\sqrt{2}$ m",
        r"$h = 12\sin45^\circ = 12 \times \frac{1}{\sqrt2} = 6\sqrt2$ m.",
        r"45°: height = $\frac{L}{\sqrt2} = 6\sqrt2$. Trap: 6 — that would be sin30.", 30)
    assert 2 + F(3, 1) ** 0 - 1 == 2
    S.q("hd-sa-p4", "hard", "A tower subtends $75^\\circ$ at a point $10$ m from its base (horizontal). Its height is:",
        ["$10(2+\\sqrt{3})$ m", "$10\\sqrt{3}$ m", "$10(2-\\sqrt{3})$ m", "$20$ m"], "$10(2+\\sqrt{3})$ m",
        r"$h = 10\tan75^\circ = 10(2+\sqrt3)$ m.",
        r"$\tan75^\circ = 2+\sqrt3$ from the 45+30 identity. Keep it factored.", 50)
    assert F(1, 3) * 3 == 1
    S.q("hd-sa-p2", "medium", r"The shadow of a tower is $\frac{1}{\sqrt{3}}$ times its height. The sun's elevation is:",
        ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$75^\\circ$"], "$60^\\circ$",
        r"$\tan\theta = \frac{h}{h/\sqrt3} = \sqrt3 \Rightarrow \theta = 60^\circ$.",
        r"Short shadow means a HIGH sun: 60°. Trap: 30° — the reciprocal ratio.", 35)
    return S
