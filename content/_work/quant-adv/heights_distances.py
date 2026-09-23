import sympy as sp
from qa_common import Q, F, T, S, P, U, write_topic

r3 = sp.sqrt(3)

# ---------------------------------------------------------------- sanity checks
# standard-angle relations: 45 -> d=h ; 30 -> d = h*sqrt(3) ; 60 -> d = h/sqrt(3)
assert sp.tan(sp.pi / 4) == 1 and sp.tan(sp.pi / 6) == 1 / r3 and sp.tan(sp.pi / 3) == r3
# walking: h*(cot30 - cot60) = 40  ->  h = 20*sqrt(3)
assert sp.simplify(20 * r3 * (r3 - 1 / r3)) == 40
# opposite sides: h = d / (cot30 + cot60)
assert sp.simplify(20 * r3 * (r3 + 1 / r3)) == 80
# same-side two ships: gap = h*(cot30 - cot60), h=60 -> 40*sqrt(3)
assert sp.simplify(60 * (r3 - 1 / r3)) == 40 * r3
# building 20, point 20*sqrt(3): building top angle 30, tower top 60 -> tower = 40
assert sp.simplify(r3 * 20 * r3 - 20) == 40
# broken tree: L = 15/cos30, standing = L*sin30, total = L*(1+sin30) = 15*sqrt(3)
L = 15 / sp.cos(sp.pi / 6)
assert sp.simplify(L * (1 + sp.sin(sp.pi / 6))) == 15 * r3
# two towers from midpoint, angles 30 and 60, distance 60 (each 30 from midpoint)
h1, h2 = 30 * sp.tan(sp.pi / 6), 30 * sp.tan(sp.pi / 3)
assert sp.simplify(h2 - h1) == 20 * r3
# car: 6 m/s * 6 s = 36 m = h*(cot30-cot60) -> h = 18*sqrt(3)
assert sp.simplify(18 * r3 * (r3 - 1 / r3)) == 36
# two points 40 m apart, angles 45 and 30 (same side): h*(cot30-cot45) = 40 -> h = 20(1+sqrt(3))
h = 20 * (1 + r3)
assert sp.simplify(h * (r3 - 1)) == 40
# building 7, depression of base 45 -> d = 7; elevation of top 60 adds 7*sqrt(3)
assert sp.simplify(7 / sp.tan(sp.pi / 4)) == 7 and sp.simplify(7 * sp.tan(sp.pi / 3)) == 7 * r3
# statue: pedestal 30, angles 45 (bottom) and 60 (top) -> statue = 30*(sqrt(3)-1)
st = 30 * (r3 - 1)
assert sp.simplify(30 / sp.tan(sp.pi / 4)) == 30                       # d = 30 from the 45 deg sight
assert sp.simplify(30 * sp.tan(sp.pi / 3) - 30) == st                   # statue = 30*sqrt(3) - 30
# ladder 10*sqrt(2) at 45 -> height 10
assert sp.simplify(10 * sp.sqrt(2) * sp.sin(sp.pi / 4)) == 10
# shadow sqrt(3) * height -> angle 30: tan30 = 1/sqrt(3)
assert sp.simplify(12 / (12 * r3)) == 1 / r3

# ---------------------------------------------------------------- subtopics
subtopics = [
S("hd-basics", "Angles of elevation and depression",
r"""
The observer's eye is the origin; the **horizontal line** through the eye is the reference.

- **Elevation**: object is *above* eye level — the angle from the horizontal *up* to the line of sight.
- **Depression**: object is *below* eye level — the angle from the horizontal *down* to the line of sight.

Height raised on a platform: always work with the **eye level**, not the ground. The ground distance $d$ and the
height *above eye level* $h$ satisfy $\tan\theta=\dfrac{h}{d}$.
""",
[
F("Master relation", r"\tan\theta=\frac{\text{height above eye level}}{\text{horizontal distance}}"),
F("Slant line", r"\sin\theta=\frac{h}{L},\quad \cos\theta=\frac{d}{L}\quad (L=\text{line-of-sight or ladder length})"),
F("Depression = elevation", r"\text{angle of depression at observer}=\text{angle of elevation at object}"),
],
[
T("Draw the horizontal through the eye",
r"""One sketch kills most errors: horizontal dashed line from the eye, the line of sight, and the right angle
between them. Drop heights *below the eye* when the observer is elevated.""",
r"From a cliff top, a boat is seen at an angle of depression of $30^\circ$. What angle does the line of sight make with the cliff face (vertical)?",
r"Depression is from the horizontal, so the line of sight is $30^\circ$ below horizontal; the vertical cliff makes $90^\circ-30^\circ=60^\circ$ with the line of sight."),
T("Depression at the top equals elevation at the bottom",
r"""Alternate interior angles: the depression from the observer equals the elevation measured at the object from
ground level directly below — use whichever is stated.""",
r"The angle of elevation of the top of a tower from a point on the ground is $45^\circ$. What is the angle of depression of the point from the tower top?",
r"Equal alternate angles: $45^\circ$."),
],
[
"Measuring height from the ground instead of eye level when the observer is on a cliff, tower or building.",
"Using $\\sin\\theta$ or $\\cos\\theta$ where the horizontal distance makes $\\tan\\theta$ the right ratio.",
"Swapping elevation and depression (drawing the angle from the object instead of the horizontal at the eye).",
]),
S("hd-standard-angles", "Standard angles: 30°, 45°, 60°",
r"""
Almost every CGL question uses only these three angles. Convert tan to a **height–distance rule** and the
answer is a one-liner:

| $\theta$ | $\tan\theta$ | rule ($h$ = height, $d$ = distance) |
|---|---|---|
| $45^\circ$ | $1$ | $d=h$ |
| $30^\circ$ | $\frac{1}{\sqrt3}$ | $d=\sqrt3\,h$ |
| $60^\circ$ | $\sqrt3$ | $d=\frac{h}{\sqrt3}$ |

So height from distance: $45^\circ\to h=d$; $30^\circ\to h=\frac{d}{\sqrt3}$; $60^\circ\to h=\sqrt3\,d$.
Take $\sqrt3\approx1.732$, $\sqrt2\approx1.414$ only if options are decimal.
""",
[
F("45 degrees", r"\theta=45^\circ\Rightarrow d=h"),
F("30 degrees", r"\theta=30^\circ\Rightarrow d=\sqrt3\,h\ \Leftrightarrow\ h=\frac{d}{\sqrt3}"),
F("60 degrees", r"\theta=60^\circ\Rightarrow d=\frac{h}{\sqrt3}\ \Leftrightarrow\ h=\sqrt3\,d"),
F("Ladder (hypotenuse given)", r"h=L\sin\theta,\quad d=L\cos\theta"),
],
[
T("Match the angle to the multiplier",
r"""45° → same; 30° → distance is $\sqrt3$ times the height; 60° → height is $\sqrt3$ times the distance.
Write the multiplier before touching numbers.""",
r"A tower subtends $60^\circ$ at a point 20 m from its base. Find its height.",
r"$h=\sqrt3\times20=20\sqrt3$ m."),
T("Ladder questions are sine/cosine, not tangent",
r"""The ladder itself is the hypotenuse: height $=L\sin\theta$, foot distance $=L\cos\theta$. A $45^\circ$ ladder
of length $L\sqrt2$ climbs exactly $L$.""",
r"A ladder of length $10\sqrt2$ m leans at $45^\circ$. How high up the wall does it reach?",
r"$10\sqrt2\times\frac{1}{\sqrt2}=10$ m."),
],
[
"Using the $60^\\circ$ rule for $30^\\circ$ (they are reciprocals: $d=\\sqrt3h$ vs $d=h/\\sqrt3$).",
"Approximating $\\sqrt3$ too early and landing between two options — keep the radical until the end.",
"Ladder: applying $\\tan\\theta=h/d$ with the ladder length mistaken for $d$.",
]),
S("hd-two-angles", "Two observation points (two angles)",
r"""
The highest-yield pattern: **two angles** from two points on the same line.

- **Same side** (walk toward the object, angle grows from $\alpha$ to $\beta$, $\beta>\alpha$):
  the distance walked equals $h(\cot\alpha-\cot\beta)$, so
  $$h=\frac{d}{\cot\alpha-\cot\beta}$$
- **Opposite sides** of the object, points $d$ apart:
  $$h=\frac{d}{\cot\alpha+\cot\beta}$$
- **From a height** (two ships seen from a lighthouse): the gap between them is
  $h(\cot\alpha-\cot\beta)$ for angles $\alpha<\beta$ measured to the nearer ship... i.e. gap $=d_{\text{far}}-d_{\text{near}}$.

With 30°/60° pairs remember $\cot30^\circ=\sqrt3$, $\cot60^\circ=\frac{1}{\sqrt3}$, so $\cot30-\cot60=\frac{2}{\sqrt3}$
and $h=\frac{d\sqrt3}{2}$ — the answer is $\frac{\sqrt3}{2}$ of the walked distance.
""",
[
F("Same side", r"h=\frac{d}{\cot\alpha-\cot\beta}"),
F("Opposite sides", r"h=\frac{d}{\cot\alpha+\cot\beta}"),
F("30-60 pair", r"\cot30^\circ-\cot60^\circ=\frac{2}{\sqrt3}\Rightarrow h=\frac{d\sqrt3}{2}"),
F("Gap from a height", r"\text{gap}=h(\cot\alpha-\cot\beta)"),
],
[
T("Subtract the cotangents, don't solve two triangles",
r"""Write $d_1=h\cot\alpha$, $d_2=h\cot\beta$ from each position; the difference of the distances is what is
given. One linear equation in $h$.""",
r"Walking 40 m toward a tower changes the elevation angle from $30^\circ$ to $60^\circ$. Find the tower's height.",
r"$h\cot30^\circ-h\cot60^\circ=40\Rightarrow h(\sqrt3-\frac1{\sqrt3})=40\Rightarrow h\cdot\frac2{\sqrt3}=40\Rightarrow h=20\sqrt3$ m."),
T("Opposite sides means add",
r"""When the two observers are on opposite sides, the base distances *add up* to $d$: denominators add, not
subtract.""",
r"Two men on opposite sides of a tower 80 m apart observe its top at $30^\circ$ and $60^\circ$. Find the height.",
r"$h=\frac{80}{\sqrt3+\frac1{\sqrt3}}=\frac{80}{\frac{4}{\sqrt3}}=20\sqrt3$ m."),
],
[
"Subtracting base distances for opposite-side observers (they add).",
"Using tan instead of cot in the difference formula: $d=h(\\cot\\alpha-\\cot\\beta)$, not $h(\\tan\\beta-\\tan\\alpha)$... note $\\cot\\alpha-\\cot\\beta$ with $\\alpha<\\beta$ is positive.",
"Forgetting the nearer point has the LARGER angle when assigning which distance is which.",
]),
S("hd-motion", "Moving observers: speed and time",
r"""
When a car/boat/man moves between the two observation points, the distance walked is **speed × time**. Chain:

$$\text{speed}\times\text{time}=h(\cot\theta_1-\cot\theta_2)$$

then solve for $h$ (or for the speed if $h$ is given). Keep angles straight: moving **toward** the object the
angle *increases*; moving **away** it *decreases*.
""",
[
F("Distance walked", r"\text{distance}=\text{speed}\times\text{time}"),
F("Chain to height", r"v\,t=h(\cot\theta_1-\cot\theta_2)"),
],
[
T("Convert speed and time first",
r"""Reduce to a plain distance (e.g. $6\times6=36$ m) and the problem becomes the standard two-angle pattern.""",
r"From a tower top, a car's angle of depression changes from $30^\circ$ to $60^\circ$ as the car approaches at a uniform 6 m/s for 6 s. Find the tower's height.",
r"$36=h(\cot30^\circ-\cot60^\circ)=h\cdot\frac2{\sqrt3}\Rightarrow h=18\sqrt3$ m."),
T("Read it backwards when height is given",
r"""If $h$ is known and the speed is asked, compute the gap $h(\cot\theta_1-\cot\theta_2)$ first, then divide by
time.""",
r"A car approaching a tower at a steady 4 m/s takes 5 s for the angle of elevation of the tower top to change from $30^\circ$ to $60^\circ$. Find the tower's height.",
r"Gap $=4\times5=20=h\cdot\frac2{\sqrt3}\Rightarrow h=10\sqrt3$ m."),
],
[
"Mixing units (km/h with seconds) — convert before chaining.",
"Assigning the larger angle to the farther position.",
]),
S("hd-compound", "Compound figures: buildings, pedestals, broken objects",
r"""
Split the figure at the **eye-level horizontal** and handle each piece with its own angle:

- **Statue on a pedestal**: pedestal gives the distance ($d=\text{pedestal}\cdot\cot45^\circ$ etc.); the statue is
  $d(\tan\beta-\tan\alpha)$ for bottom/top angles $\alpha,\beta$.
- **Tower on a building**: tower $=d\tan(\text{top})-$ building height.
- **Broken tree**: the fallen part is the hypotenuse. If the top touches ground at distance $b$ making angle
  $\theta$, broken part $=\frac{b}{\cos\theta}$, standing part $=b\tan\theta$, and the whole tree is their sum.
""",
[
F("Statue on pedestal", r"\text{statue}=d(\tan\beta-\tan\alpha)"),
F("Tower on building", r"\text{tower}=d\tan\theta_{\text{top}}-\text{building}"),
F("Broken tree", r"\text{tree}=\frac{b}{\cos\theta}+b\tan\theta"),
F("Building + tower from one height", r"\text{tower}=\text{building}+d(\tan\beta-\tan\alpha)"),
],
[
T("Angles differ by 15°? Expect a surd answer",
r"""45° paired with 60° or 30° gives clean radicals; keep $(\sqrt3-1)$ or $(1+\sqrt3)$ factored — that exact
form is what the options show.""",
r"A statue stands on a 30 m pedestal. From a point on the ground the elevation of the pedestal top is $45^\circ$ and of the statue top $60^\circ$. Find the statue's height.",
r"$d=30$ (from $45^\circ$); statue $=30\tan60^\circ-30=30(\sqrt3-1)$ m."),
T("Broken tree = broken + standing",
r"""Work the right triangle of the fallen part: horizontal $b$, angle $\theta$ at the tip. Standing part
$=b\tan\theta$, fallen part $=\frac{b}{\cos\theta}$; add them.""",
r"A tree breaks and the top touches the ground 15 m from the base, making $30^\circ$ with the ground. Find the original height.",
r"Fallen $=\frac{15}{\cos30^\circ}=10\sqrt3$; standing $=15\tan30^\circ=5\sqrt3$; total $=15\sqrt3$ m."),
],
[
"Forgetting the standing/building part and reporting only the extra piece.",
"Adding the fallen length and the standing height with the angle applied to the wrong side.",
"Rationalising $30(\\sqrt3-1)$ into a decimal when the options are in factored surd form.",
]),
]

patterns = [
P("Single angle, one unknown", "very common",
  r"One angle ($30^\circ$, $45^\circ$ or $60^\circ$) with either height or distance given.",
  r"Standard-angle rule: $d=h$ at 45°, $d=\sqrt3h$ at 30°, $d=h/\sqrt3$ at 60°; answer keeps the radical."),
P("Two angles from two points", "very common",
  r"Two elevation angles from two positions on the same line (walking, or observers on opposite sides).",
  r"$h=\frac{d}{\cot\alpha-\cot\beta}$ (same side) or $\frac{d}{\cot\alpha+\cot\beta}$ (opposite sides)."),
P("Angle of depression from a height", "very common",
  r"Lighthouse/cliff/aeroplane looking down at ships, cars or corners.",
  r"Depression at the eye = elevation at the object; then $d=\frac{h}{\tan\theta}$. Two objects → subtract the two distances."),
P("Speed-time two-angle problem", "common",
  r"Car/boat moves at uniform speed; depression or elevation angle changes after a stated time.",
  r"Distance = speed × time = $h(\cot\theta_1-\cot\theta_2)$; solve for $h$."),
P("Compound structure", "common",
  r"Statue on pedestal, tower on building, broken tree, flagstaff on tower.",
  r"Split at eye level; the lower element usually fixes the distance $d$; the asked part is the difference of two tan products."),
P("Shadow problems", "occasional",
  r"Shadow length related to height (equal, $\sqrt3$ times, or a ratio given).",
  r"Shadow = horizontal distance: $\tan(\text{sun elevation})=\frac{h}{\text{shadow}}$. Equal shadows at the same moment ⇒ equal heights."),
]

# ---------------------------------------------------------------- solved examples
solved = []

solved.append(Q("hd-s01",
r"The angle of elevation of the top of a 50 m high tower from a point on the ground is $45^\circ$. Find the distance of the point from the base of the tower.",
U(" m", 50, 25, 50 * r3, 50 / r3), 50,
r"""
$\tan45^\circ=\frac{50}{d}\Rightarrow1=\frac{50}{d}\Rightarrow d=50$ m.
""",
r"At $45^\circ$, distance = height — no calculation at all. (Diagram: eye at the point, horizontal to the tower, angle up to the top.)",
"easy", "hd-basics", "single angle 45", 30,
figure=r"""<svg viewBox="0 0 240 130" width="240" height="130" stroke="currentColor" fill="none">
  <line x1="30" y1="110" x2="210" y2="110"/>
  <line x1="170" y1="110" x2="170" y2="20"/>
  <line x1="30" y1="110" x2="170" y2="20"/>
  <line x1="30" y1="80" x2="150" y2="80" stroke-dasharray="4 3"/>
  <text x="8" y="114" font-size="13" fill="currentColor" stroke="none">P</text>
  <text x="176" y="18" font-size="13" fill="currentColor" stroke="none">A</text>
  <text x="176" y="114" font-size="13" fill="currentColor" stroke="none">B</text>
  <text x="52" y="76" font-size="12" fill="currentColor" stroke="none">45&#176;</text>
  <text x="120" y="126" font-size="12" fill="currentColor" stroke="none">d</text>
  <text x="196" y="70" font-size="12" fill="currentColor" stroke="none">h</text>
</svg>"""))

solved.append(Q("hd-s02",
r"The shadow of a tower is $40\sqrt{3}$ m long when the sun's elevation is $30^\circ$. Find the height of the tower.",
U(" m", 40, 40 * r3, 80, 40 / r3), 40,
r"""
$\tan30^\circ=\frac{h}{40\sqrt3}\Rightarrow\frac{1}{\sqrt3}=\frac{h}{40\sqrt3}\Rightarrow h=40$ m.
""",
r"30° → height = $\frac{\text{shadow}}{\sqrt3}=\frac{40\sqrt3}{\sqrt3}=40$ m. The $\sqrt3$ cancels by design.",
"easy", "hd-standard-angles", "shadow with 30 degree sun", 35))

solved.append(Q("hd-s03",
r"From the top of a 100 m high cliff, the angle of depression of a ship is $30^\circ$. Find the distance of the ship from the base of the cliff.",
U(" m", 100 * r3, 100 / r3, 100, 50 * r3), 100 * r3,
r"""
Depression $30^\circ$ = elevation $30^\circ$ at the ship. $\tan30^\circ=\frac{100}{d}$

$\frac{1}{\sqrt3}=\frac{100}{d}\Rightarrow d=100\sqrt3$ m.
""",
r"Flip depression to elevation, then the 30° rule: $d=\sqrt3\times100=100\sqrt3$ m. Trap: $\frac{100}{\sqrt3}$ (that is the 60° answer).",
"easy", "hd-basics", "depression single angle", 35))

solved.append(Q("hd-s04",
r"Walking 40 m towards a tower, the angle of elevation of its top changes from $30^\circ$ to $60^\circ$. Find the height of the tower.",
U(" m", 20 * r3, 40 * r3, 10 * r3, 20 * (1 + r3)), 20 * r3,
r"""
Let $h$ be the height and $x$ the nearer distance. Then $x\tan60^\circ=h$ and $(x+40)\tan30^\circ=h$:

$h\cot60^\circ+40=h\cot30^\circ\Rightarrow40=h(\sqrt3-\frac{1}{\sqrt3})=\frac{2h}{\sqrt3}\Rightarrow h=20\sqrt3$ m.
""",
r"Direct formula: $h=\frac{d}{\cot30-\cot60}=\frac{40\sqrt3}{2}=20\sqrt3$ m. For a 30–60 pair the height is always $\frac{\sqrt3}{2}$ of the walked distance.",
"medium", "hd-two-angles", "walking two-angle", 50))

solved.append(Q("hd-s05",
r"A statue stands on a 30 m high pedestal. From a point on the ground, the angle of elevation of the top of the pedestal is $45^\circ$ and that of the top of the statue is $60^\circ$. Find the height of the statue.",
[(r"$30(\sqrt{3}-1)$ m", 30 * (r3 - 1)), (r"$30(\sqrt{3}+1)$ m", 30 * (r3 + 1)), (r"$15(\sqrt{3}-1)$ m", 15 * (r3 - 1)), (r"$30\sqrt{3}$ m", 30 * r3)], 30 * (r3 - 1),
r"""
From the $45^\circ$ observation: $d=\frac{30}{\tan45^\circ}=30$ m.

From the $60^\circ$ observation: $30+\text{statue}=30\tan60^\circ=30\sqrt3$.

So statue $=30\sqrt3-30=30(\sqrt3-1)$ m.
""",
r"45° fixes $d$ = pedestal height; statue $=d(\tan60-\tan45)=30(\sqrt3-1)$. Keep the factored surd — that is how the options read.",
"hard", "hd-compound", "statue on pedestal", 55))

# ---------------------------------------------------------------- practice
pr = []

pr.append(Q("hd-q01",
r"A vertical pole 12 m high casts a shadow on level ground when the sun's elevation is $45^\circ$. The length of the shadow is:",
U(" m", 12, 12 * r3, 6, 12 / r3), 12,
r"$\tan45^\circ=\frac{12}{s}\Rightarrow s=12$ m.",
r"45° → shadow = height = 12 m.",
"easy", "hd-standard-angles", "shadow at 45", 25))

pr.append(Q("hd-q02",
r"The angle of elevation of the top of a 30 m high tower from a point on the ground is $60^\circ$. The distance of the point from the base of the tower is:",
U(" m", 10 * r3, 30 * r3, 10, 15 * r3), 10 * r3,
r"$\tan60^\circ=\frac{30}{d}\Rightarrow\sqrt3=\frac{30}{d}\Rightarrow d=\frac{30}{\sqrt3}=10\sqrt3$ m.",
r"60° → distance $=\frac{h}{\sqrt3}=10\sqrt3$ m. Trap: $30\sqrt3$ (that is the 30° rule).",
"easy", "hd-standard-angles", "single angle 60", 30))

pr.append(Q("hd-q03",
r"From the top of a 60 m high lighthouse, the angle of depression of a boat is $60^\circ$. The horizontal distance of the boat from the lighthouse is:",
U(" m", 20 * r3, 60 * r3, 20, 30 * r3), 20 * r3,
r"Depression $60^\circ$ = elevation $60^\circ$: $\sqrt3=\frac{60}{d}\Rightarrow d=\frac{60}{\sqrt3}=20\sqrt3$ m.",
r"60° → $d=\frac{h}{\sqrt3}=20\sqrt3$ m.",
"easy", "hd-basics", "depression 60", 30))

pr.append(Q("hd-q04",
r"If the sun's elevation is $30^\circ$ and a tower's shadow is $30\sqrt{3}$ m long, the height of the tower is:",
U(" m", 30, 30 * r3, 10, 60), 30,
r"$h=\frac{\text{shadow}}{\sqrt3}=\frac{30\sqrt3}{\sqrt3}=30$ m.",
r"30° → height = shadow ÷ $\sqrt3$ = 30 m.",
"easy", "hd-standard-angles", "shadow at 30", 25))

pr.append(Q("hd-q05",
r"A ladder 20 m long leans against a wall at $45^\circ$ to the ground. The height it reaches on the wall is:",
U(" m", 10 * sp.sqrt(2), 20, 10, 20 / r3), 10 * sp.sqrt(2),
r"Height $=L\sin45^\circ=20\times\frac{1}{\sqrt2}=10\sqrt2$ m.",
r"Ladder is the hypotenuse: $h=L\sin\theta$. At 45°: $h=\frac{L}{\sqrt2}$. Trap: 10 is the $\frac{L}{2}$ guess.",
"easy", "hd-standard-angles", "ladder 45", 30))

pr.append(Q("hd-q06",
r"Two men stand on opposite sides of a tower, 80 m apart, and observe its top at elevations of $30^\circ$ and $60^\circ$. The height of the tower is:",
U(" m", 20 * r3, 40 * r3, 40, 10 * r3), 20 * r3,
r"""
$h=\frac{d}{\cot30^\circ+\cot60^\circ}=\frac{80}{\sqrt3+\frac{1}{\sqrt3}}=\frac{80}{\frac{4}{\sqrt3}}=20\sqrt3$ m.
""",
r"Opposite sides → add the cotangents: $\frac{80}{\frac{4}{\sqrt3}}=20\sqrt3$ m. Trap: subtracting gives $\frac{80\sqrt3}{2}=40\sqrt3$ (wrong side of the figure).",
"medium", "hd-two-angles", "opposite sides 30-60", 45))

pr.append(Q("hd-q07",
r"On walking 20 m towards a tower the angle of elevation of its top rises from $30^\circ$ to $60^\circ$. The height of the tower is:",
U(" m", 10 * r3, 20 * r3, 5 * r3, 20), 10 * r3,
r"$h=\frac{d}{\cot30^\circ-\cot60^\circ}=\frac{20}{\frac{2}{\sqrt3}}=10\sqrt3$ m.",
r"30–60 pair: $h=\frac{\sqrt3}{2}\times d=\frac{\sqrt3}{2}\times20=10\sqrt3$ m.",
"medium", "hd-two-angles", "walking two-angle", 45))

pr.append(Q("hd-q08",
r"The shadow of a pole is $\sqrt{3}$ times the height of the pole. The angle of elevation of the sun is:",
U("°", 30, 45, 60, 90), 30,
r"$\tan\theta=\frac{h}{\sqrt3\,h}=\frac{1}{\sqrt3}\Rightarrow\theta=30^\circ$.",
r"Shadow $\sqrt3\times$ height is the signature of 30° ($d=\sqrt3h$). Trap: 60° inverts the ratio.",
"medium", "hd-standard-angles", "shadow ratio to angle", 30))

pr.append(Q("hd-q09",
r"From the top of a 60 m high lighthouse, the angles of depression of two ships on the same side are $30^\circ$ and $60^\circ$. The distance between the ships is:",
U(" m", 40 * r3, 20 * r3, 80 * r3, 40), 40 * r3,
r"""
Distances from the base: far $=60\cot30^\circ=60\sqrt3$, near $=60\cot60^\circ=\frac{60}{\sqrt3}=20\sqrt3$.

Gap $=60\sqrt3-20\sqrt3=40\sqrt3$ m.
""",
r"Gap $=h(\cot30-\cot60)=60\cdot\frac2{\sqrt3}=40\sqrt3$ m — same $\frac{\sqrt3}{2}\times$ nothing; here $\frac{2h}{\sqrt3}$. Watch: far minus near, never add.",
"medium", "hd-two-angles", "two ships from lighthouse", 45))

pr.append(Q("hd-q10",
r"From a point 20$\sqrt{3}$ m from the base of a building, the elevation of the top of the building is $30^\circ$ and of the top of the tower standing on it is $60^\circ$. The height of the tower is:",
U(" m", 40, 20 * r3, 60, 20), 40,
r"""
Building: $h_b=20\sqrt3\tan30^\circ=20$ m.

Building + tower: $20\sqrt3\tan60^\circ=60$ m. Tower $=60-20=40$ m.
""",
r"$\text{tower}=d(\tan60-\tan30)=20\sqrt3(\sqrt3-\frac1{\sqrt3})=20\sqrt3\cdot\frac{2}{\sqrt3}=40$ m.",
"medium", "hd-compound", "tower on building", 50))

pr.append(Q("hd-q11",
r"A tree breaks due to a storm and the broken part touches the ground 15 m from the base, making an angle of $30^\circ$ with the ground. The height of the tree before breaking was:",
U(" m", 15 * r3, 15, 10 * r3, 30 * r3), 15 * r3,
r"""
Fallen part $=\frac{15}{\cos30^\circ}=\frac{30}{\sqrt3}=10\sqrt3$ m; standing part $=15\tan30^\circ=5\sqrt3$ m.

Total $=15\sqrt3$ m.
""",
r"Tree $=\frac{b}{\cos\theta}+b\tan\theta=10\sqrt3+5\sqrt3=15\sqrt3$. Trap: $10\sqrt3$ (forgotten standing part).",
"medium", "hd-compound", "broken tree", 55))

pr.append(Q("hd-q12",
r"The angles of elevation of the tops of two towers from the midpoint of the line joining their bases are $30^\circ$ and $60^\circ$. If the towers are 60 m apart, the difference of their heights is:",
U(" m", 20 * r3, 10 * r3, 40 * r3, 30 * r3), 20 * r3,
r"""
Each base is 30 m from the midpoint.

$h_1=30\tan30^\circ=10\sqrt3$, $h_2=30\tan60^\circ=30\sqrt3$. Difference $=20\sqrt3$ m.
""",
r"Midpoint splits 60 into 30 + 30; heights are $30\times\frac{1}{\sqrt3}$ and $30\times\sqrt3$ → difference $20\sqrt3$ m. (Ratio check: heights are always 1 : 3 here.)",
"medium", "hd-two-angles", "two towers from midpoint", 60))

pr.append(Q("hd-q13",
r"From the top of a tower, the angle of depression of a car changes from $30^\circ$ to $60^\circ$ while the car approaches uniformly at 6 m/s for 6 seconds. The height of the tower is:",
U(" m", 18 * r3, 36, 12 * r3, 18), 18 * r3,
r"""
Distance covered $=6\times6=36$ m $=h(\cot30^\circ-\cot60^\circ)=\frac{2h}{\sqrt3}$.

$h=\frac{36\sqrt3}{2}=18\sqrt3$ m.
""",
r"Speed × time gives the walked distance; then the 30–60 pair: $h=\frac{\sqrt3}{2}\times36=18\sqrt3$ m.",
"hard", "hd-motion", "car speed two-angle", 60))

pr.append(Q("hd-q14",
r"The angles of elevation of the top of a tower from two points 40 m apart on the same side of it are $30^\circ$ and $45^\circ$. The height of the tower is:",
[(r"$20(\sqrt{3}+1)$ m", 20 * (1 + r3)), (r"$20(\sqrt{3}-1)$ m", 20 * (r3 - 1)), (r"$40(\sqrt{3}+1)$ m", 40 * (1 + r3)), (r"$40\sqrt{3}$ m", 40 * r3)], 20 * (1 + r3),
r"""
$h=\frac{d}{\cot30^\circ-\cot45^\circ}=\frac{40}{\sqrt3-1}$.

Rationalise: $\frac{40(\sqrt3+1)}{3-1}=20(\sqrt3+1)$ m.
""",
r"$\frac{40}{\sqrt3-1}$ → multiply by $\frac{\sqrt3+1}{\sqrt3+1}$ → $20(\sqrt3+1)$ m. The $30/45$ pair always ends in $(\sqrt3+1)\times\frac{d}{2}$.",
"hard", "hd-two-angles", "30-45 same side pair", 60))

pr.append(Q("hd-q15",
r"From the roof of a 7 m high building, the angle of elevation of the top of a tower is $60^\circ$ and the angle of depression of its base is $45^\circ$. The height of the tower is:",
[(r"$7(1+\sqrt{3})$ m", 7 * (1 + r3)), (r"$7\sqrt{3}$ m", 7 * r3), (r"$7(2+\sqrt{3})$ m", 7 * (2 + r3)), (r"$(7+14\sqrt{3})$ m", 7 + 14 * r3)], 7 * (1 + r3),
r"""
Depression $45^\circ$: horizontal distance $d=\frac{7}{\tan45^\circ}=7$ m.

Elevation $60^\circ$: top above roof $=7\tan60^\circ=7\sqrt3$.

Tower $=7+7\sqrt3=7(1+\sqrt3)$ m.
""",
r"45° depression gives $d$ = building height (7); tower $=7+7\sqrt3$. Add the building back — the top angle only measures the part above the roof.",
"hard", "hd-compound", "building and tower", 65))

topic = {
    "id": "heights-distances",
    "sectionId": "quant",
    "title": "Heights and Distances",
    "order": 17,
    "importance": "high",
    "avgQuestions": {"tier1": 2, "tier2": 3},
    "summary": "Applied trigonometry: angles of elevation and depression, the 30-45-60 rules, two-angle configurations, moving observers and compound figures. "
               "Every question reduces to one right triangle and one tangent — learn the three standard-angle multipliers and the cot-difference formula and this becomes near-guaranteed marks.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
