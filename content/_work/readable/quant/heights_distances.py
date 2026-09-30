r"""Readable rewrite of Heights & Distances (heights-distances) — all five subtopics.

Plain English, one idea per section, the reliable method first.
Every number in every example is rechecked below with exact surd arithmetic.
Run with Python 3.12 from the repo root.
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "heights-distances.json"


class S:
    """Exact value a + b*sqrt(3) with rational a, b — covers every angle used here."""

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        o = o if isinstance(o, S) else S(o)
        return S(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return S(-self.a, -self.b)

    def __sub__(self, o):
        o = o if isinstance(o, S) else S(o)
        return S(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return (o if isinstance(o, S) else S(o)) - self

    def __mul__(self, o):
        o = o if isinstance(o, S) else S(o)
        return S(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, S) else S(o)
        den = o.a * o.a - 3 * o.b * o.b
        num = self * S(o.a, -o.b)
        return S(num.a / den, num.b / den)

    def __rtruediv__(self, o):
        return (o if isinstance(o, S) else S(o)) / self

    def __eq__(self, o):
        o = o if isinstance(o, S) else S(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"S({self.a}, {self.b})"


TAN30, TAN45, TAN60 = S(0, F(1, 3)), S(1), S(0, 1)
COT30, COT45, COT60 = S(0, 1), S(1), S(0, F(1, 3))
SIN30, COS30, SIN60, COS60 = S(F(1, 2)), S(0, F(1, 2)), S(0, F(1, 2)), S(F(1, 2))
TAN15, TAN75 = S(2, -1), S(2, 1)

# ---------- answer checks: hd-basics ----------
assert TAN45 == 1 and COT45 == 1
assert 30 * TAN30 == S(0, 10)                                    # p1: 30 m away, 30 deg -> 10*sqrt3
assert 60 * COT45 == S(60)                                       # p2: depression 45 from 60 m tower -> 60 m
assert 100 * SIN30 == S(50) and 100 * COS30 == S(0, 50)          # p3: thread 100 m at 30 deg
assert 75 * F(3, 5) == 45                                        # p4: stick 1.5/2.5, shadow 75 -> 45 m
assert TAN60 / TAN30 == S(3) and 3 * (40 - 20) == 40 + 20        # p5: cloud 30/60, eye 20 m -> 40 m
# notes numbers
assert 20 * COT45 == S(20) and 40 * TAN30 == S(0, F(40, 3))
assert 30 * COT60 == S(0, 10)                                    # trick: tower 30 m at 60 deg -> 10*sqrt3
# ---------- answer checks: hd-standard-angles ----------
assert S(0, 30) * COT30 == S(90)                                 # p1: 30*sqrt3 tower at 30 deg -> 90 m
assert 20 * TAN45 == S(20) and 20 * COT45 == S(20)               # p2: shadow = height -> 45 deg
assert 20 * SIN30 == S(10) and 20 * COS30 == S(0, 10)            # p3: ladder 20 m at 30 deg
assert TAN15 * TAN75 == S(1) and 10 / TAN15 == S(20, 10)         # p4: 10/(2-sqrt3) = 20+10*sqrt3
assert 10 / (COT30 - COT60) == S(0, 5)                           # p5: shadow shortens 10 m -> 5*sqrt3
# ---------- answer checks: hd-two-angles ----------
assert 40 / (COT30 - COT60) == S(0, 20) and S(0, 20) * (COT30 - COT60) == S(40)
assert 80 / (COT30 + COT60) == S(0, 20)                          # p2: opposite sides, 80 m apart
assert 60 * (COT30 - COT60) == S(0, 40)                          # p3: ships gap 40*sqrt3
assert 30 * TAN60 == S(0, 30) and 30 * TAN30 == S(0, 10)         # p4: towers from midpoint
assert S(0, 30) - S(0, 10) == S(0, 20)
assert 10 / (TAN60 - TAN30) == S(0, 5) and S(0, 5) * TAN60 == S(15)   # p5: foot 60, roof 30
# ---------- answer checks: hd-motion ----------
assert 6 * 6 == 36 and 36 / (COT30 - COT60) == S(0, 18)          # p1: 6 m/s for 6 s, 30->60
assert 4 * 5 == 20 and 20 / (COT30 - COT60) == S(0, 10)          # p2: 4 m/s for 5 s
assert S(0, 18) * COT30 == S(54) and 54 // 6 == 9                # p3: time to reach the foot
assert S(0, 30) * COT60 == S(30) and S(0, 30) * COT30 == S(90)   # p4: two drivers, 6 m/s each
assert 90 // 6 - 30 // 6 == 10
assert 30 * TAN30 == S(0, 10) and 30 * TAN60 == S(0, 30)         # p5: balloon rises 30 m away
assert S(0, 30) - S(0, 10) == S(0, 20)
# ---------- answer checks: hd-compound ----------
assert 30 * COT45 == S(30) and S(30) * (TAN60 - TAN45) == S(-30, 30)   # p1: statue 30(sqrt3-1)
assert 20 * COT30 == S(0, 20) and S(0, 20) * TAN30 == S(20)      # p2: building 20 m at 30 deg
assert S(0, 20) * (TAN60 - TAN30) == S(40)                       # p2: tower on building = 40 m
assert 10 * COT30 == S(0, 10) and 10 + S(0, 10) * TAN60 == S(40)  # p3: roof, depression 30 + elevation 60
assert 15 * TAN30 == S(0, 5) and 15 / COS30 == S(0, 10)          # p4: broken tree
assert S(0, 5) + S(0, 10) == S(0, 15)
assert 10 * COS30 - 10 * COS60 == S(-5, 5)                       # p5: ladder foot slides 5(sqrt3-1)
# ---------- answer checks: tricks and inline notes numbers ----------
assert 28 * F(1, 2) == 14                                        # basics trick: shadow ratio
assert 10 / TAN75 == S(20, -10)                                  # standard trick: 10(2-sqrt3)
assert 90 * TAN60 == S(0, 90)                                    # standard notes: 90 m away -> 90*sqrt3
assert 10 * S(0, 1) == S(0, 10)                                  # two-angles trick: 20*sqrt3/2
assert 80 / (COT45 + COT60) == S(120, -40)                       # two-angles trick: 120-40*sqrt3
assert 8 * 3 == 24 and 12 * S(0, 1) == S(0, 12)                  # motion trick: 24 m -> 12*sqrt3
assert F(36 * 5, 18) == 10 and 50 * S(0, 1) == S(0, 50)          # motion trick: 36 km/h -> 50*sqrt3
assert 20 * (TAN60 - TAN45) == S(-20, 20)                        # compound trick: 20(sqrt3-1)
assert 1 / COS30 == S(0, F(2, 3)) and 9 * (TAN30 + 1 / COS30) == S(0, 9)   # compound trick: 9*sqrt3
print("all answer checks passed")


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ============================================================ hd-basics
BASICS = dict(
    concept=(
        "Elevation means looking **up** at an angle. Depression means looking **down**. "
        "Both angles sit between the **horizontal line** through the observer's eye and the line of sight.\n\n"
        "Each question hides one right triangle. The tower is the side opposite the angle. "
        "The ground distance is the side next to it. So one ratio, $\\tan\\theta$, solves most of them.\n\n"
        "First turn every depression into an elevation. Then solve the triangle."
    ),
    notes=r"""### Looking up: the angle of elevation
Stand on flat ground and look straight ahead. Now raise your eyes to the top of a tower.

The angle your line of sight turns **up** from the horizontal is the **angle of elevation**.

The horizontal ray and the tower make a right angle. So the figure is a right triangle:

- Tower = the side **opposite** the angle.
- Ground distance = the side **next to** the angle.
- Eye level = the height of the observer's eye above the ground.

> **Rule:** $\tan\theta = \dfrac{\text{height above eye level}}{\text{horizontal distance}}$

A tower top is seen at $45^\circ$ from a point on the ground. $\tan 45^\circ = 1$, so the tower is as tall as the point is far: tower 20 m, distance 20 m.

### Looking down: the angle of depression
Now stand on the tower and look at a car on the road.

The angle your line of sight turns **down** from your horizontal line is the **angle of depression**.

> **Rule:** Depression from the top equals elevation from the bottom. The two horizontal lines are parallel, so the two angles are equal (alternate angles).

This one line converts every depression question into the elevation question you already know.

> **Example:** From the top of a 60 m tower, the angle of depression of a car is $45^\circ$. Then the car sees the tower top at $45^\circ$, so the car is $60 \times \cot 45^\circ = 60$ m from the foot.

### Solve the triangle with tan
Write the ratio before touching any number.

$$h = d \times \tan\theta \qquad d = h \times \cot\theta$$

Here $h$ is the height **above the observer's eye** and $d$ is the horizontal distance.

From a point 30 m from the foot of a pole, its top is at $30^\circ$. Height $= 30 \times \tan 30^\circ = 30 \times \dfrac{1}{\sqrt{3}} = 10\sqrt{3}$ m.

> **Tip:** Keep $\sqrt{3}$ as $\sqrt{3}$ until the last step. Only use $1.73$ when the question says "approximately".

### When the slanting length is given
A kite thread, a wire or a ladder runs **along the line of sight**. That slanting line is the hypotenuse.

- Height reached: $h = L\sin\theta$.
- Horizontal distance: $d = L\cos\theta$.

A kite flies on a 100 m thread at $30^\circ$. Height $= 100 \times \dfrac{1}{2} = 50$ m. Horizontal distance $= 100 \times \dfrac{\sqrt{3}}{2} = 50\sqrt{3}$ m.

> **Watch:** The thread is the slanting side, not the height. Options that treat the thread as the height are always present.

### Shadows: similar triangles
The sun makes the same angle with every vertical object at the same time. So the two triangles are similar, and you can compare without trigonometry:

$$\dfrac{\text{tower height}}{\text{tower shadow}} = \dfrac{\text{stick height}}{\text{stick shadow}}$$

A 1.5 m stick casts a 2.5 m shadow. A tower casts a 75 m shadow at the same moment. Tower $= 75 \times \dfrac{1.5}{2.5} = 45$ m.

### Eye level matters
Every angle starts at the observer's **eye**, not the ground.

An observer 1.5 m tall sees a tower top at $45^\circ$ from 20 m away. Height above eye level $= 20$ m. Tower $= 20 + 1.5 = 21.5$ m.

> **Watch:** When the question gives a man's height, add it at the end. When it says "from a point on the ground", the eye is at ground level and nothing is added.
""",
    formulas=[
        {"name": "Tangent rule", "tex": r"\tan\theta = \frac{\text{height above eye}}{\text{horizontal distance}}",
         "note": "The angle sits at the observer. Height is opposite, distance is next to the angle."},
        {"name": "Height and distance", "tex": r"h = d\tan\theta,\qquad d = h\cot\theta"},
        {"name": "Slanting length (thread, wire, ladder)", "tex": r"h = L\sin\theta,\qquad d = L\cos\theta",
         "note": "L is the slanting line of sight, the hypotenuse of the triangle."},
        {"name": "Depression to elevation", "tex": r"\text{depression from top} = \text{elevation from bottom}",
         "note": "The two horizontal lines are parallel, so the angles are equal."},
    ],
    tricks=[
        {"title": "Swap depression for elevation first",
         "body": "Never work with a downward angle directly. Redraw it at the bottom of the tower and solve an ordinary elevation question.",
         "example": {"q": "From the top of a 30 m tower, the angle of depression of a car is $60^\\circ$. How far is the car from the foot of the tower?",
                     "steps": ["Depression $60^\\circ$ means the car sees the top at $60^\\circ$.",
                               r"Distance $= 30 \times \cot 60^\circ = 30 \times \dfrac{1}{\sqrt{3}}$.",
                               r"$= \dfrac{30}{\sqrt{3}} = 10\sqrt{3}$ m."],
                     "answer": "$10\\sqrt{3}$ m"}},
        {"title": "Shadows without trigonometry",
         "body": "Same sun, same time, similar triangles. Set up the stick ratio and multiply; no tangent needed.",
         "example": {"q": "A 2 m pole casts a 4 m shadow. How tall is a tower whose shadow is 28 m at the same time?",
                     "steps": [r"Ratio $= \dfrac{2}{4} = \dfrac{1}{2}$.",
                               r"Tower $= 28 \times \dfrac{1}{2} = 14$ m."],
                     "answer": "14 m"}},
        {"title": "Forty-five degrees means equal legs",
         "body": "Whenever the angle is $45^\\circ$, the height above the eye equals the horizontal distance. Write the equal pair without any tangent.",
         "example": {"q": "The top of a tower is seen at $45^\\circ$ from a point 28 m from its foot. What is the height of the tower (eye at ground level)?",
                     "steps": [r"$\tan 45^\circ = 1$, so height $=$ distance.", "Height $= 28$ m."],
                     "answer": "28 m"}},
    ],
    mistakes=[
        {"wrong": r"Using $\sin\theta$ with the ground angle when the tower is the opposite side.",
         "right": r"The angle is at the observer, the tower is opposite it, so use $\tan\theta$."},
        {"wrong": "Measuring the angle of depression from the vertical line downward.",
         "right": "Depression is measured from the horizontal line through the eye, going down."},
        {"wrong": "Treating the kite thread or ladder length as the height.",
         "right": r"The thread is the hypotenuse: height $= L\sin\theta$, distance $= L\cos\theta$."},
        {"wrong": "Ignoring the observer's eye height when the question gives a man's height.",
         "right": "Add the eye height to the height above the eye at the end."},
        {"wrong": "Turning a depression into an elevation and then changing its value.",
         "right": "The two angles are equal. Only the position of the angle moves."},
    ],
    revision=[
        r"Elevation: angle up from the horizontal at the observer's eye.",
        r"Depression: angle down. It equals the elevation from the object below.",
        r"$\tan\theta = \dfrac{\text{height above eye}}{\text{distance}}$.",
        r"Thread, wire, ladder $= L$: use $h = L\sin\theta$, $d = L\cos\theta$.",
        r"Shadows: $\dfrac{\text{height}}{\text{shadow}}$ is the same for all objects at one time.",
        r"Height above eye $+$ eye height $=$ full height.",
    ],
    patterns=[
        pat("hd-ba-p1", "One angle at eye level", "very common",
            "A single angle of elevation from a point on the ground; a height or a distance is asked.",
            r"h = d\tan\theta",
            ["Draw the right triangle: angle at the observer, tower opposite.",
             "Mark what is known: height, distance or angle.",
             r"Write $\tan\theta = h/d$ and solve for the missing side."],
            "One angle and one side fix a right triangle completely.",
            "From a point on the ground 30 m from the foot of a tower, the angle of elevation of the top is $30^\\circ$. The height of the tower is:",
            [r"$\tan 30^\circ = \dfrac{h}{30}$.",
             r"$h = 30 \times \dfrac{1}{\sqrt{3}} = \dfrac{30}{\sqrt{3}}$.",
             r"$h = 10\sqrt{3}$ m."],
            "$10\\sqrt{3}$ m"),
        pat("hd-ba-p2", "Angle of depression from a height", "very common",
            "Someone on a tower, cliff or lighthouse looks down at a boat, car or person.",
            r"d = h\cot\theta \quad (\theta = \text{angle of depression})",
            ["Convert the depression into an equal elevation at the object below.",
             "The height of the tower is the side opposite the new angle.",
             r"Distance $= h \times \cot\theta$."],
            "The downward angle and the bottom angle are equal, so the triangle is the usual one.",
            "From the top of a lighthouse 60 m above the sea, the angle of depression of a boat is $45^\\circ$. The horizontal distance of the boat from the foot of the lighthouse is:",
            ["Boat sees the top at $45^\\circ$.",
             r"$\tan 45^\circ = \dfrac{60}{d} = 1$.",
             r"$d = 60$ m."],
            "60 m"),
        pat("hd-ba-p3", "Slanting length given (thread, wire, ladder)", "common",
            "The length of a kite thread, wire or ladder is given with its angle, not the ground distance.",
            r"h = L\sin\theta,\qquad d = L\cos\theta",
            ["Spot that the given length runs along the line of sight: it is the hypotenuse.",
             r"Height $= L \times \sin\theta$.",
             r"Distance $= L \times \cos\theta$."],
            "In a right triangle the hypotenuse pairs with the sine (opposite) and cosine (adjacent).",
            "A kite is flying with 100 m of thread released, and the thread makes $30^\\circ$ with the ground. Taking the thread as a straight line, the height of the kite above the ground is:",
            [r"$h = 100 \times \sin 30^\circ$.",
             r"$h = 100 \times \dfrac{1}{2} = 50$ m."],
            "50 m"),
        pat("hd-ba-p4", "Shadow of a tower and a stick", "common",
            "A pole or stick and its shadow are given; the shadow of a tower at the same time is asked.",
            r"\frac{H}{\text{tower shadow}} = \frac{\text{stick}}{\text{stick shadow}}",
            ["Write the stick ratio: height over shadow.",
             "Multiply the tower's shadow by that ratio.",
             "No tangent is needed when the sun angle is not given."],
            "The sun makes equal angles with both objects, so the two right triangles are similar.",
            "A vertical stick 1.5 m long casts a shadow 2.5 m long. At the same time, a tower casts a shadow 75 m long. The height of the tower is:",
            [r"Ratio $= \dfrac{1.5}{2.5} = \dfrac{3}{5}$.",
             r"Tower $= 75 \times \dfrac{3}{5}$.",
             r"Tower $= 45$ m."],
            "45 m"),
        pat("hd-ba-p5", "A cloud and its reflection in a lake", "occasional",
            "An observer above water sees a cloud at one angle and its reflection at another angle.",
            r"H = h\,\frac{\tan\alpha + \tan\beta}{\tan\beta - \tan\alpha}",
            ["Let $H$ be the cloud height and $h$ the eye height above the water.",
             r"Elevation $\alpha$: $\tan\alpha = (H-h)/d$. Reflection $\beta$: $\tan\beta = (H+h)/d$.",
             "Divide the two equations and solve for $H$."],
            "The reflection behaves like an object as far below the water as the cloud is above it.",
            "A man's eye is 20 m above a lake. The angle of elevation of a cloud is $30^\\circ$ and the angle of depression of its reflection is $60^\\circ$. The height of the cloud above the lake is:",
            [r"$\dfrac{\tan 60^\circ}{\tan 30^\circ} = \dfrac{H+20}{H-20}$.",
             r"$3 = \dfrac{H+20}{H-20}$, so $3H - 60 = H + 20$.",
             r"$2H = 80$, giving $H = 40$ m."],
            "40 m"),
    ],
)

# ============================================================ hd-standard-angles
STANDARD = dict(
    concept=(
        "Almost every exam question uses only $30^\\circ$, $45^\\circ$ and $60^\\circ$. "
        "Learn their tangent values once and most questions become one multiplication.\n\n"
        "The cotangent column is the handiest: it turns a height into a distance. "
        "At $45^\\circ$ the distance equals the height; at $30^\\circ$ it is $\\sqrt{3}$ times the height; "
        "at $60^\\circ$ it is $\\sqrt{3}$ divided by the height's factor."
    ),
    notes=r"""### The three friendly angles
Exam papers love $30^\circ$, $45^\circ$ and $60^\circ$ because their ratios are clean.

| Angle | $\tan$ | $\cot$ (distance per unit height) |
|---|---|---|
| $30^\circ$ | $\dfrac{1}{\sqrt{3}}$ | $\sqrt{3}$ |
| $45^\circ$ | $1$ | $1$ |
| $60^\circ$ | $\sqrt{3}$ | $\dfrac{1}{\sqrt{3}}$ |

> **Tip:** Memorise the $\cot$ column as "how far you stand from a 1 m object". At $30^\circ$ you stand $\sqrt{3}$ m; at $60^\circ$ only $\dfrac{1}{\sqrt{3}}$ m.

Worked number: a tower is $30\sqrt{3}$ m tall and its top is seen at $30^\circ$. Distance $= 30\sqrt{3} \times \sqrt{3} = 90$ m.

### Swapping between height and distance
One multiplication is enough, once the angle is standard.

$$d = h \times \cot\theta \qquad h = d \times \tan\theta$$

A point is 90 m from the foot of a tower, and the top is at $60^\circ$. Height $= 90 \times \sqrt{3} = 90\sqrt{3}$ m. Check the size: a near angle ($60^\circ$) with a long distance must give a tall tower.

> **Rule:** Bigger angle, closer point. At $60^\circ$ the tower is about 1.7 times the distance; at $30^\circ$ it is about 0.6 times.

### Spotting the angle from the sides
Sometimes the sides are given and the angle is asked.

A tower 20 m tall casts a shadow 20 m long. Height equals distance, and only one angle makes the legs equal: $45^\circ$.

> **Example:** A tower is $\sqrt{3}$ times as far from you as it is tall, so $\cot\theta = \sqrt{3}$, so $\theta = 30^\circ$.

### Ladders and slanting wires
When the slanting length $L$ is given, use sine and cosine.

A 20 m ladder leans on a wall at $30^\circ$ with the ground:

- Height on the wall $= 20 \times \dfrac{1}{2} = 10$ m.
- Foot from the wall $= 20 \times \dfrac{\sqrt{3}}{2} = 10\sqrt{3}$ m.

> **Watch:** The $30^\circ$ angle is between the ladder and the **ground**. If it is given at the wall, swap sine and cosine.

### The fifteen and seventy-five pair
Two more exact values appear in harder papers:

$$\tan 75^\circ = 2 + \sqrt{3}, \qquad \tan 15^\circ = 2 - \sqrt{3}$$

They multiply to 1, because $15^\circ + 75^\circ = 90^\circ$.

A tower 10 m tall is seen at $15^\circ$. Distance $= \dfrac{10}{2-\sqrt{3}} = 10(2+\sqrt{3}) = 20 + 10\sqrt{3}$ m. Rationalise by multiplying top and bottom by $2+\sqrt{3}$.

### When the sun moves
As the sun climbs, the shadow shrinks. Two positions of the same shadow give one equation.

A tower's shadow shortens by 10 m as the sun moves from $30^\circ$ to $60^\circ$:

$$h(\cot 30^\circ - \cot 60^\circ) = 10 \Rightarrow h \times \frac{2}{\sqrt{3}} = 10 \Rightarrow h = 5\sqrt{3} \text{ m}$$

> **Tip:** For the $30^\circ$ and $60^\circ$ pair, $\cot 30^\circ - \cot 60^\circ = \dfrac{2}{\sqrt{3}}$. The same difference appears in many questions.
""",
    formulas=[
        {"name": "Tangent values", "tex": r"\tan 30^\circ = \frac{1}{\sqrt{3}},\quad \tan 45^\circ = 1,\quad \tan 60^\circ = \sqrt{3}"},
        {"name": "Distance from height", "tex": r"d = h\cot\theta",
         "note": "cot 30 = sqrt3, cot 45 = 1, cot 60 = 1/sqrt3."},
        {"name": "Ladder on a wall", "tex": r"h = L\sin\theta,\quad d = L\cos\theta",
         "note": "Theta is the ladder's angle with the ground."},
        {"name": "Fifteen and seventy-five", "tex": r"\tan 15^\circ = 2-\sqrt{3},\qquad \tan 75^\circ = 2+\sqrt{3}"},
    ],
    tricks=[
        {"title": "Read distance straight off the cot column",
         "body": "With a standard angle, distance = height $\\times$ the cot value. No division, no fraction juggling.",
         "example": {"q": "A tower 30 m tall has its top seen at $60^\\circ$ from a point on the ground. How far is the point from the foot?",
                     "steps": [r"$\cot 60^\circ = \dfrac{1}{\sqrt{3}}$.",
                               r"Distance $= 30 \times \dfrac{1}{\sqrt{3}} = \dfrac{30}{\sqrt{3}} = 10\sqrt{3}$ m."],
                     "answer": "$10\\sqrt{3}$ m"}},
        {"title": "Fifteen and seventy-five multiply to one",
         "body": "Angles that add to $90^\\circ$ have tangents that multiply to 1. Use this to check answers or flip a division into a multiplication.",
         "example": {"q": "A tower is seen at $75^\\circ$ from 10 m away. Using $\\tan 15^\\circ = 2-\\sqrt{3}$, its height is:",
                     "steps": [r"$h = 10 \times \tan 75^\circ = 10 \times \dfrac{1}{2-\sqrt{3}}$.",
                               r"$= 10(2+\sqrt{3}) = 20 + 10\sqrt{3}$ m."],
                     "answer": "$20+10\\sqrt{3}$ m"}},
    ],
    mistakes=[
        {"wrong": r"Swapping the values: writing $\tan 30^\circ = \sqrt{3}$.",
         "right": r"$\tan 30^\circ = \dfrac{1}{\sqrt{3}}$; the big value belongs to $60^\circ$."},
        {"wrong": "Computing distance as height $\\times\\tan\\theta$.",
         "right": r"Distance $= h \times \cot\theta$; the tangent gives height from distance."},
        {"wrong": "Using the ladder's length as the height it reaches.",
         "right": r"Height on the wall $= L\sin\theta$; the ladder itself is the slanting side."},
        {"wrong": "Placing the $30^\\circ$ ladder angle at the top of the wall.",
         "right": "The ladder's angle is normally with the ground. At the wall, the angle is $60^\\circ$."},
        {"wrong": "Replacing $\\sqrt{3}$ by 1.7 in an exact-answer question.",
         "right": r"Keep $\sqrt{3}$ symbolic unless the question says approximately or gives $1.73$."},
    ],
    revision=[
        r"$\tan 30^\circ = \dfrac{1}{\sqrt{3}}$, $\tan 45^\circ = 1$, $\tan 60^\circ = \sqrt{3}$.",
        r"$\cot$ column: $\sqrt{3}$, $1$, $\dfrac{1}{\sqrt{3}}$ for $30^\circ$, $45^\circ$, $60^\circ$.",
        r"$d = h\cot\theta$ and $h = d\tan\theta$.",
        r"Ladder: height $= L\sin\theta$, foot distance $= L\cos\theta$.",
        r"$\tan 75^\circ = 2+\sqrt{3}$, $\tan 15^\circ = 2-\sqrt{3}$, product $1$.",
        r"Shadow change: $h(\cot\alpha - \cot\beta)$ = change in length.",
    ],
    patterns=[
        pat("hd-sa-p1", "Height or distance at a standard angle", "very common",
            "One standard angle with one side; the other side is asked.",
            r"d = h\cot\theta",
            ["Pick the standard angle's cot value.",
             "Multiply the height by it for the distance, or divide for the height.",
             r"Keep $\sqrt{3}$ exact."],
            "A standard angle fixes the ratio of the two legs, so one multiplication finishes it.",
            "The angle of elevation of the top of a tower $30\\sqrt{3}$ m high, from a point on the ground, is $30^\\circ$. The distance of the point from the foot of the tower is:",
            [r"$d = 30\sqrt{3} \times \cot 30^\circ$.",
             r"$d = 30\sqrt{3} \times \sqrt{3}$.",
             r"$d = 90$ m."],
            "90 m"),
        pat("hd-sa-p2", "Find the angle from the sides", "common",
            "Both legs are given (or their ratio) and the sun's or tower's angle is asked.",
            r"\tan\theta = \frac{h}{d}",
            ["Form the ratio height over distance.",
             "Reduce it to a surd form.",
             "Match against the standard tangent table."],
            "The legs decide the angle, so the ratio reads the angle straight off the table.",
            "A vertical tower 20 m tall casts a shadow 20 m long on the ground. The sun's elevation is:",
            [r"$\tan\theta = \dfrac{20}{20} = 1$.",
             r"$\tan 45^\circ = 1$.",
             r"$\theta = 45^\circ$."],
            "$45^\\circ$"),
        pat("hd-sa-p3", "Ladder against a wall", "common",
            "A ladder's length and its angle with the ground are given.",
            r"h = L\sin\theta,\qquad d = L\cos\theta",
            ["Confirm the angle is with the ground, not the wall.",
             r"Height reached $= L\sin\theta$.",
             r"Foot distance $= L\cos\theta$."],
            "The ladder is the hypotenuse, so sine gives the wall side and cosine the ground side.",
            "A 20 m ladder leans against a vertical wall, making $30^\\circ$ with the ground. The height reached on the wall and the distance of the foot from the wall are:",
            [r"Height $= 20\sin 30^\circ = 20 \times \dfrac{1}{2} = 10$ m.",
             r"Distance $= 20\cos 30^\circ = 20 \times \dfrac{\sqrt{3}}{2}$.",
             r"Distance $= 10\sqrt{3}$ m."],
            "10 m and $10\\sqrt{3}$ m"),
        pat("hd-sa-p4", "Fifteen or seventy-five degrees", "occasional",
            "An uncommon angle that is 15 or 75 degrees; options contain surds.",
            r"\tan 75^\circ = 2+\sqrt{3},\qquad \tan 15^\circ = 2-\sqrt{3}",
            ["Replace the tangent with its surd value.",
             "Rationalise the denominator with the partner surd.",
             "The two surds multiply to 1."],
            "These two angles have exact surd tangents, so the arithmetic stays exact.",
            "From a point on the ground, the angle of elevation of the top of a 10 m tower is $15^\\circ$. The distance of the point from the foot of the tower is:",
            [r"$d = 10 \times \cot 15^\circ = \dfrac{10}{2-\sqrt{3}}$.",
             r"Multiply top and bottom by $2+\sqrt{3}$: $d = 10(2+\sqrt{3})$.",
             r"$d = 20 + 10\sqrt{3}$ m."],
            "$20+10\\sqrt{3}$ m"),
        pat("hd-sa-p5", "Shadow changing as the sun moves", "occasional",
            "The same object's shadow is described at two sun positions; the change in shadow is given.",
            r"h(\cot\alpha - \cot\beta) = \text{change in shadow}",
            [r"Write both shadow lengths: $h\cot\alpha$ and $h\cot\beta$.",
             "Subtract and equate to the given change.",
             "Solve for $h$."],
            "Each sun position makes its own triangle with the same height, so one equation links them.",
            "As the sun rises from $30^\\circ$ to $60^\\circ$, the shadow of a tower shortens by 10 m. The height of the tower is:",
            [r"Shadow at $30^\circ$: $h\sqrt{3}$. Shadow at $60^\circ$: $\dfrac{h}{\sqrt{3}}$.",
             r"$h\sqrt{3} - \dfrac{h}{\sqrt{3}} = \dfrac{2h}{\sqrt{3}} = 10$.",
             r"$h = 5\sqrt{3}$ m."],
            "$5\\sqrt{3}$ m"),
    ],
)

# ============================================================ hd-two-angles
TWO = dict(
    concept=(
        "One angle gives only a ratio: two sides, one equation. Two angles from two places give the height itself.\n\n"
        "The trick is simple. Write $h\\cot\\alpha$ for one distance and $h\\cot\\beta$ for the other. "
        "The walked gap between the two viewpoints is the difference (same side) or the sum (opposite sides) of these.\n\n"
        "So every two-angle question is one equation with one unknown: $h$."
    ),
    notes=r"""### Why two angles are enough
A single angle only tells you a ratio. Add a second viewpoint and the ground between them, and the height falls out.

Set the tower's height as $h$. From point P the angle is $\alpha$, from point Q it is $\beta$. Then:

- Distance of P from the foot $= h\cot\alpha$.
- Distance of Q from the foot $= h\cot\beta$.

Everything else is adding or subtracting these two lengths.

> **Rule:** Same side of the tower: the gap is a **difference**. Opposite sides: the gap is a **sum**.

### Walking towards the tower
The most common pattern. A man sees the top at $30^\circ$, walks some distance towards it, and sees $60^\circ$.

$$h(\cot\alpha - \cot\beta) = d \qquad\Rightarrow\qquad h = \frac{d}{\cot\alpha - \cot\beta}$$

The walked distance is 40 m: $h\left(\sqrt{3} - \dfrac{1}{\sqrt{3}}\right) = h \times \dfrac{2}{\sqrt{3}} = 40$, so $h = 20\sqrt{3}$ m.

> **Tip:** For the $30^\circ$ and $60^\circ$ pair, $\cot 30^\circ - \cot 60^\circ = \dfrac{2}{\sqrt{3}}$. So $h = d \times \dfrac{\sqrt{3}}{2}$: with $d = 40$, $h = 20\sqrt{3}$ m in one step.

### Watching from opposite sides
Two men stand on opposite banks of a river, or the two angles at the tower top are measured from two sides.

$$h = \frac{d}{\cot\alpha + \cot\beta}$$

Two points are 80 m apart on opposite sides of a tower, with angles $30^\circ$ and $60^\circ$: $h\left(\sqrt{3} + \dfrac{1}{\sqrt{3}}\right) = h \times \dfrac{4}{\sqrt{3}} = 80$, so $h = 20\sqrt{3}$ m.

> **Watch:** If a question says "the angles of elevation of the top of an unfinished tower", the taller part still counts: draw the full height in both triangles.

### Two objects seen from a height
From the top of a lighthouse $h$ metres high, two boats lie in the same line, at depressions $\alpha$ and $\beta$.

Each boat's distance from the foot is $h\cot\alpha$ and $h\cot\beta$. The distance **between the boats** is:

$$\text{gap} = h(\cot\alpha - \cot\beta)$$

From a 60 m lighthouse the depressions are $30^\circ$ and $60^\circ$: gap $= 60 \times \dfrac{2}{\sqrt{3}} = 40\sqrt{3}$ m.

### Two towers from one point
Two towers stand on opposite sides of a road. From a point on the road, their tops are at $\alpha$ and $\beta$.

Each tower makes its own triangle sharing the same ground distance $d$: heights are $d\tan\alpha$ and $d\tan\beta$.

From the midpoint of a 60 m road, the angles are $60^\circ$ and $30^\circ$. Each tower is 30 m away: heights $= 30\sqrt{3}$ m and $10\sqrt{3}$ m. Difference $= 20\sqrt{3}$ m.

### Watching from two floors
A tower is seen from the foot of a building and again from its roof, $b$ metres higher.

From the foot the angle is $\beta$ (larger). From the roof it is $\alpha$ (smaller), because the roof already covers part of the height. The two equations are $H = d\tan\beta$ and $H - b = d\tan\alpha$. Subtract:

$$d = \frac{b}{\tan\beta - \tan\alpha}, \qquad H = d\tan\beta$$

Building 10 m, roof $30^\circ$, foot $60^\circ$: $d = \dfrac{10}{\sqrt{3} - 1/\sqrt{3}} = 5\sqrt{3}$ m and $H = 5\sqrt{3} \times \sqrt{3} = 15$ m.

> **Watch:** From the higher point the angle is smaller, because the tower top is closer to eye level.
""",
    formulas=[
        {"name": "Same side (walk towards)", "tex": r"h = \frac{d}{\cot\alpha - \cot\beta}",
         "note": "d is the distance walked; beta is the nearer, bigger angle."},
        {"name": "Opposite sides", "tex": r"h = \frac{d}{\cot\alpha + \cot\beta}",
         "note": "d is the full distance between the two observers."},
        {"name": "Gap between two objects from a height", "tex": r"\text{gap} = h(\cot\alpha - \cot\beta)"},
        {"name": "Tower seen from foot and roof of a building", "tex": r"d = \frac{b}{\tan\beta - \tan\alpha},\quad H = d\tan\beta",
         "note": "b = building height; beta from the foot, alpha from the roof."},
    ],
    tricks=[
        {"title": "Thirty-sixty fast numbers",
         "body": "For the 30 and 60 pair: same side $h = d\\times\\dfrac{\\sqrt{3}}{2}$; opposite sides $h = d\\times\\dfrac{\\sqrt{3}}{4}$. Both come from $\\cot 30^\\circ - \\cot 60^\\circ = \\dfrac{2}{\\sqrt{3}}$.",
         "example": {"q": "Walking 20 m towards a tower raises the angle from $30^\\circ$ to $60^\\circ$. Find the height.",
                     "steps": [r"$h = 20 \times \dfrac{\sqrt{3}}{2}$.",
                               r"$h = 10\sqrt{3}$ m."],
                     "answer": "$10\\sqrt{3}$ m"}},
        {"title": "Write the cot pair before the numbers",
         "body": "Always simplify $\\cot\\alpha - \\cot\\beta$ (or the sum) first. Substituting numbers into unsimplified surds is where errors creep in.",
         "example": {"q": "Two observers 80 m apart on opposite sides see a tower top at $45^\\circ$ and $60^\\circ$. Find the height.",
                     "steps": [r"$\cot 45^\circ + \cot 60^\circ = 1 + \dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}+1}{\sqrt{3}}$.",
                               r"$h = \dfrac{80\sqrt{3}}{\sqrt{3}+1} = \dfrac{80\sqrt{3}(\sqrt{3}-1)}{2}$.",
                               r"$h = 40\sqrt{3}(\sqrt{3}-1) = 120 - 40\sqrt{3}$ m."],
                     "answer": "$(120-40\\sqrt{3})$ m"}},
    ],
    mistakes=[
        {"wrong": "Using a difference of cotangents for observers on opposite sides.",
         "right": "Opposite sides add the distances, so use $\\cot\\alpha+\\cot\\beta$."},
        {"wrong": "Subtracting the angles first and then taking one cotangent.",
         "right": "The cotangents subtract, never the angles."},
        {"wrong": "Treating the midpoint between two towers as the full distance to each.",
         "right": "From the midpoint each tower is half the road away."},
        {"wrong": "Using the far angle as the near one.",
         "right": "Walking towards the tower raises the angle; the bigger angle is the closer point."},
        {"wrong": "Forgetting both triangles share the same tower height.",
         "right": "Write $h$ once and use it in both cotangent expressions."},
    ],
    revision=[
        r"Same side: $h = \dfrac{d}{\cot\alpha - \cot\beta}$.",
        r"Opposite sides: $h = \dfrac{d}{\cot\alpha + \cot\beta}$.",
        r"$30^\circ$ and $60^\circ$ pair: difference $= \dfrac{2}{\sqrt{3}}$, sum $= \dfrac{4}{\sqrt{3}}$.",
        r"Two boats from a lighthouse: gap $= h(\cot\alpha - \cot\beta)$.",
        r"Two towers from a midpoint: each is half the road away; heights $= \dfrac{d}{2}\tan\alpha$ and $\dfrac{d}{2}\tan\beta$.",
        r"Foot and roof of a building: $d = \dfrac{b}{\tan\beta - \tan\alpha}$, $H = d\tan\beta$.",
    ],
    patterns=[
        pat("hd-tw-p1", "Walking towards the tower", "very common",
            "The angle of elevation increases as the observer walks a given distance towards the tower.",
            r"h = \frac{d}{\cot\alpha - \cot\beta}",
            ["Name the two angles: far first, near second.",
             "Write both distances from the foot: $h\\cot\\alpha$ and $h\\cot\\beta$.",
             "Their difference equals the distance walked.",
             "Solve for $h$."],
            "The same height sits inside two triangles, so the walked ground equals the difference of the two cotangent distances.",
            "The angle of elevation of the top of a tower from a point is $30^\\circ$. On walking 40 m towards the tower, the angle becomes $60^\\circ$. The height of the tower is:",
            [r"Far distance $= h\cot 30^\circ = h\sqrt{3}$.",
             r"Near distance $= h\cot 60^\circ = \dfrac{h}{\sqrt{3}}$.",
             r"Difference: $\dfrac{2h}{\sqrt{3}} = 40$, so $h = 20\sqrt{3}$ m."],
            "$20\\sqrt{3}$ m"),
        pat("hd-tw-p2", "Observers on opposite sides", "common",
            "Two people (or banks of a river) on opposite sides of the tower with different angles.",
            r"h = \frac{d}{\cot\alpha + \cot\beta}",
            ["Write the two distances from the foot as $h\\cot\\alpha$ and $h\\cot\\beta$.",
             "Their sum is the full separation $d$.",
             "Solve for $h$."],
            "On opposite sides the two distances add up to the ground between the observers.",
            "Two men on opposite sides of a tower, 80 m apart, see its top at $30^\\circ$ and $60^\\circ$. The height of the tower is:",
            [r"$h\cot 30^\circ + h\cot 60^\circ = 80$.",
             r"$h\left(\sqrt{3} + \dfrac{1}{\sqrt{3}}\right) = h \times \dfrac{4}{\sqrt{3}} = 80$.",
             r"$h = 20\sqrt{3}$ m."],
            "$20\\sqrt{3}$ m"),
        pat("hd-tw-p3", "Distance between two objects seen from a height", "common",
            "From the top of a lighthouse or cliff, two boats or cars are seen at two angles of depression.",
            r"\text{gap} = h(\cot\alpha - \cot\beta)",
            ["Convert each depression into an elevation at the object.",
             "Distance of the farther object $= h\\cot\\alpha$ (smaller angle).",
             "Subtract the nearer distance $h\\cot\\beta$ to get the gap."],
            "Each object sits at its own cotangent distance from the foot, so the gap is their difference.",
            "From the top of a lighthouse 60 m above the sea, the angles of depression of two boats in the same line are $30^\\circ$ and $60^\\circ$. The distance between the boats is:",
            [r"Far boat: $60 \times \cot 30^\circ = 60\sqrt{3}$ m.",
             r"Near boat: $60 \times \cot 60^\circ = \dfrac{60}{\sqrt{3}} = 20\sqrt{3}$ m.",
             r"Gap $= 60\sqrt{3} - 20\sqrt{3} = 40\sqrt{3}$ m."],
            "$40\\sqrt{3}$ m"),
        pat("hd-tw-p4", "Two towers seen from one point", "common",
            "Two towers on opposite sides of a road; from a point between them both tops are seen.",
            r"H_1 = d\tan\alpha,\qquad H_2 = d\tan\beta",
            ["Split the ground distance as the question directs (midpoint means half each).",
             "Each tower forms its own right triangle.",
             "Compute each height; subtract if a difference is asked."],
            "The triangles are independent, joined only by the shared ground distance.",
            "Two towers stand on opposite sides of a road 60 m wide. From the midpoint of the road, their tops are seen at $60^\\circ$ and $30^\\circ$. The difference of their heights is:",
            [r"Each tower is 30 m from the midpoint.",
             r"Taller tower $= 30\tan 60^\circ = 30\sqrt{3}$ m; other $= 30\tan 30^\circ = 10\sqrt{3}$ m.",
             r"Difference $= 20\sqrt{3}$ m."],
            "$20\\sqrt{3}$ m"),
        pat("hd-tw-p5", "Tower seen from the foot and the roof of a building", "occasional",
            "The same tower's top is observed from ground level and from a window or roof above.",
            r"d = \frac{b}{\tan\beta - \tan\alpha}",
            ["Let the building be $b$ and the tower $H$, with ground distance $d$.",
             "From the foot: $\\tan\\beta = H/d$. From the roof: $\\tan\\alpha = (H-b)/d$.",
             "Subtract to eliminate $H$ and find $d$, then $H = d\\tan\\beta$."],
            "Raising the observer cuts the tower's apparent height by exactly the building's height.",
            "A tower is seen from the foot of a 10 m building at $60^\\circ$, and from its roof at $30^\\circ$. The height of the tower is:",
            [r"$H - 10 = d\tan 30^\circ = \dfrac{d}{\sqrt{3}}$ and $H = d\tan 60^\circ = d\sqrt{3}$.",
             r"$d\sqrt{3} - \dfrac{d}{\sqrt{3}} = 10 \Rightarrow \dfrac{2d}{\sqrt{3}} = 10$.",
             r"$d = 5\sqrt{3}$ m, so $H = 5\sqrt{3} \times \sqrt{3} = 15$ m."],
            "15 m"),
    ],
)

# ============================================================ hd-motion
MOTION = dict(
    concept=(
        "A car, a man or a plane moves while someone watches. Motion adds only one new fact: "
        "**distance = speed $\\times$ time**.\n\n"
        "That product replaces the 'walked distance' of the two-angle questions. "
        "So the master equation becomes speed $\\times$ time $= h(\\cot\\alpha - \\cot\\beta)$.\n\n"
        "Convert every speed to metres per second first. Then the question is an old friend."
    ),
    notes=r"""### Motion only supplies the ground distance
In a moving-observer question, the triangle does not change. Only the ground between the two viewpoints is now covered at a speed.

$$v \times t = h(\cot\alpha - \cot\beta)$$

Here $v$ is the speed, $t$ the time between the two angle readings, $h$ the tower height, $\alpha$ the first (farther) angle and $\beta$ the second (nearer) angle.

> **Example:** A car running at 6 m/s takes 6 s to change the elevation of a tower top from $30^\circ$ to $60^\circ$. Ground covered $= 36$ m. Then $36 = h \times \dfrac{2}{\sqrt{3}}$, so $h = 18\sqrt{3}$ m.

### Finding the height
Given speed, time and both angles, the height comes out in two lines.

1. Ground distance $= v \times t$.
2. Divide by $\cot\alpha - \cot\beta$.

At $4$ m/s for $5$ s the car covers 20 m, so $h = 20 \times \dfrac{\sqrt{3}}{2} = 10\sqrt{3}$ m.

> **Tip:** For $30^\circ \to 60^\circ$, $h = (v t)\times\dfrac{\sqrt{3}}{2}$. One multiplication, no surd subtraction.

### Finding the speed or the time
The same equation reads in any direction. Solve for what is missing.

A car changes the elevation from $30^\circ$ to $60^\circ$ in 5 s, and the tower is known to be $10\sqrt{3}$ m. Ground covered $= h \times \dfrac{2}{\sqrt{3}} = 20$ m. Speed $= 20 \div 5 = 4$ m/s.

> **Watch:** Speeds in km/h must be converted: multiply by $\dfrac{5}{18}$ to get m/s. 36 km/h is 10 m/s.

### Time to reach the foot
Sometimes the question asks how much longer the car needs to reach the tower.

After the second reading, the car is still $h\cot\beta$ away (using the **nearer** angle). Divide that distance by the speed.

A tower is $18\sqrt{3}$ m tall and a car sees its top at $30^\circ$. Distance $= 18\sqrt{3} \times \sqrt{3} = 54$ m. At 6 m/s the car needs $54 \div 6 = 9$ s more.

### Moving on both sides
Two friends drive towards the same tower from opposite sides at the same speed.

Each starts at $h\cot\alpha$ or $h\cot\beta$ away. Their arrival times differ by:

$$\Delta t = \frac{h(\cot\alpha - \cot\beta)}{v}$$

Tower $30\sqrt{3}$ m, angles $60^\circ$ and $30^\circ$, both at 6 m/s: distances $30$ m and $90$ m, times $5$ s and $15$ s. The nearer starter wins by 10 s.

### Rising straight up
A balloon rises vertically while someone watches a point on the ground. The horizontal distance stays fixed; the height changes.

At horizontal distance $d$: heights are $d\tan 30^\circ = \dfrac{d}{\sqrt{3}}$ and $d\tan 60^\circ = d\sqrt{3}$. The rise $= d \times \dfrac{2}{\sqrt{3}}$. With $d = 30$ m, the balloon climbed $20\sqrt{3}$ m.

> **Rule:** Horizontal motion changes the distance; vertical motion changes the height. Check which one is fixed before writing tan or cot.
""",
    formulas=[
        {"name": "Moving observer chain", "tex": r"v\,t = h(\cot\alpha - \cot\beta)",
         "note": "alpha = first (farther) angle, beta = second (nearer) angle."},
        {"name": "Time to reach the foot", "tex": r"t = \frac{h\cot\beta}{v}",
         "note": "Use the angle at the car's current position."},
        {"name": "Vertical rise", "tex": r"\text{rise} = d(\tan\beta - \tan\alpha)",
         "note": "d = fixed horizontal distance; angles of depression shrink as the balloon rises."},
        {"name": "Speed conversion", "tex": r"1\ \text{km/h} = \frac{5}{18}\ \text{m/s}"},
    ],
    tricks=[
        {"title": "One chain, any unknown",
         "body": "$v t = h(\\cot\\alpha - \\cot\\beta)$ contains every moving-observer question. Cover the unknown and solve.",
         "example": {"q": "A jeep takes 3 s at 8 m/s to change a tower's elevation from $30^\\circ$ to $60^\\circ$. Find the height.",
                     "steps": [r"Ground $= 8 \times 3 = 24$ m.",
                               r"$h = 24 \times \dfrac{\sqrt{3}}{2} = 12\sqrt{3}$ m."],
                     "answer": "$12\\sqrt{3}$ m"}},
        {"title": "Check the units before the triangle",
         "body": "Convert km/h to m/s with $5/18$ before anything else. A speed in the wrong unit spoils an otherwise perfect triangle.",
         "example": {"q": "A car at 36 km/h takes 10 s to change the elevation from $30^\\circ$ to $60^\\circ$. Find the height.",
                     "steps": [r"$36$ km/h $= 36 \times \dfrac{5}{18} = 10$ m/s.",
                               r"Ground $= 10 \times 10 = 100$ m.",
                               r"$h = 100 \times \dfrac{\sqrt{3}}{2} = 50\sqrt{3}$ m."],
                     "answer": "$50\\sqrt{3}$ m"}},
    ],
    mistakes=[
        {"wrong": "Using $v\\times t$ as the height instead of the ground distance.",
         "right": "Speed times time is ground covered; it equals the cotangent difference."},
        {"wrong": "Working in km/h with metres in the same equation.",
         "right": r"Convert with $\times\dfrac{5}{18}$ first."},
        {"wrong": "Giving the total time when the remaining time to the foot is asked.",
         "right": "After the second angle, the car still has $h\\cot\\beta$ to cover; divide that by the speed."},
        {"wrong": "Adding angles of two observers who move on opposite sides.",
         "right": "Opposite sides still add the two cotangent distances; only the ground differs."},
        {"wrong": "Using cot when the observer rises vertically.",
         "right": "With a fixed horizontal distance, both readings use tan with the same $d$."},
    ],
    revision=[
        r"$v\,t = h(\cot\alpha - \cot\beta)$: the master chain.",
        r"$30^\circ \to 60^\circ$: $h = (v t)\times\dfrac{\sqrt{3}}{2}$.",
        r"Remaining time to the foot: $h\cot\beta \div v$.",
        r"km/h to m/s: multiply by $\dfrac{5}{18}$.",
        r"Opposite-side movers: distances $h\cot\alpha$ and $h\cot\beta$, times differ by their difference over $v$.",
        r"Balloon rising: rise $= d(\tan\beta - \tan\alpha)$ with $d$ fixed.",
    ],
    patterns=[
        pat("hd-mo-p1", "Find the height from speed and time", "very common",
            "A vehicle moves at a given speed for a given time while the elevation angle changes.",
            r"h = \frac{v\,t}{\cot\alpha - \cot\beta}",
            ["Compute the ground covered: $v \\times t$.",
             "Write $\\cot\\alpha - \\cot\\beta$ for the two angles.",
             "Divide to get $h$."],
            "The covered ground equals the difference of the two cotangent distances of the same height.",
            "A car moving at 6 m/s takes 6 seconds to change the angle of elevation of a tower's top from $30^\\circ$ to $60^\\circ$. The height of the tower is:",
            [r"Ground $= 6 \times 6 = 36$ m.",
             r"$\cot 30^\circ - \cot 60^\circ = \dfrac{2}{\sqrt{3}}$.",
             r"$h = 36 \times \dfrac{\sqrt{3}}{2} = 18\sqrt{3}$ m."],
            "$18\\sqrt{3}$ m"),
        pat("hd-mo-p2", "Find the speed or the time", "common",
            "The height and both angles are known; a speed or a time is asked.",
            r"v = \frac{h(\cot\alpha - \cot\beta)}{t}",
            ["Compute the ground: $h(\\cot\\alpha - \\cot\\beta)$.",
             "Divide by the time for the speed, or by the speed for the time.",
             "Convert units if the options are in km/h."],
            "With the height known, the chain gives the ground and speed is ground over time.",
            "The angle of elevation of the top of a $10\\sqrt{3}$ m tower changes from $30^\\circ$ to $60^\\circ$ as a car approaches in 5 seconds. The speed of the car is:",
            [r"Ground $= 10\sqrt{3} \times \dfrac{2}{\sqrt{3}} = 20$ m.",
             r"Speed $= 20 \div 5 = 4$ m/s.",
             r"In km/h: $4 \times \dfrac{18}{5} = 14.4$ km/h."],
            "4 m/s (14.4 km/h)"),
        pat("hd-mo-p3", "Time to reach the foot of the tower", "common",
            "After the angle change the question asks how much longer the mover needs to reach the tower.",
            r"t = \frac{h\cot\beta}{v}",
            ["Use the angle at the mover's current position.",
             "Remaining distance $= h\\cot\\beta$.",
             "Divide by the speed."],
            "One triangle is enough: the current angle fixes the remaining ground.",
            "A tower is $18\\sqrt{3}$ m tall. A car approaching it at 6 m/s currently sees the top at $30^\\circ$. The time the car needs to reach the foot of the tower is:",
            [r"Distance $= 18\sqrt{3} \times \cot 30^\circ = 18\sqrt{3} \times \sqrt{3} = 54$ m.",
             r"Time $= 54 \div 6$.",
             r"$= 9$ seconds."],
            "9 seconds"),
        pat("hd-mo-p4", "Two movers on opposite sides", "occasional",
            "Two people drive towards the same tower from opposite sides; who arrives first and by how much.",
            r"\Delta t = \frac{h(\cot\alpha - \cot\beta)}{v}",
            ["Find each starting distance: $h\\cot\\alpha$ and $h\\cot\\beta$.",
             "Divide each by its speed to get two times.",
             "Subtract for the gap."],
            "Each mover runs an independent race against their own cotangent distance.",
            "A tower $30\\sqrt{3}$ m tall stands between two friends who see its top at $60^\\circ$ and $30^\\circ$. Both drive towards the tower at 6 m/s, starting together. By how many seconds does the first one reach the tower before the second?",
            [r"Friend with $60^\circ$: distance $= 30\sqrt{3} \times \dfrac{1}{\sqrt{3}} = 30$ m, time $= 5$ s.",
             r"Friend with $30^\circ$: distance $= 30\sqrt{3} \times \sqrt{3} = 90$ m, time $= 15$ s.",
             r"Gap $= 15 - 5 = 10$ s."],
            "10 seconds"),
        pat("hd-mo-p5", "Observer rising vertically", "occasional",
            "A balloon or lift rises; the angle of depression of a fixed point changes.",
            r"\text{rise} = d(\tan\beta - \tan\alpha)",
            ["Fix the horizontal distance $d$ to the point.",
             "Two heights: $d\\tan\\alpha$ (start) and $d\\tan\\beta$ (later).",
             "Subtract for the rise."],
            "Only the height changes, so the rise is the difference of two tangents over the same base.",
            "A balloon rises straight up. The angle of depression of a stone 30 m away (horizontally) changes from $30^\\circ$ to $60^\\circ$. The height the balloon gained is:",
            [r"Start: $30\tan 30^\circ = \dfrac{30}{\sqrt{3}} = 10\sqrt{3}$ m.",
             r"Later: $30\tan 60^\circ = 30\sqrt{3}$ m.",
             r"Rise $= 30\sqrt{3} - 10\sqrt{3} = 20\sqrt{3}$ m."],
            "$20\\sqrt{3}$ m"),
    ],
)

# ============================================================ hd-compound
COMPOUND = dict(
    concept=(
        "Compound figures stack two heights or bend one object: a statue on a pedestal, a tower on a building, a broken tree.\n\n"
        "The method never changes. Draw the two triangles separately. "
        "The lower triangle gives the ground distance. The upper triangle gives the extra height.\n\n"
        "Most answers reduce to one line: extra height $= d(\\tan\\beta - \\tan\\alpha)$."
    ),
    notes=r"""### Two heights stacked
A statue stands on a pedestal. From one point you see the pedestal's top at $\alpha$ and the statue's head at $\beta$.

The lower triangle fixes the ground: $d = p\cot\alpha$, where $p$ is the pedestal's height. The statue's height is then:

$$s = d(\tan\beta - \tan\alpha)$$

Pedestal 30 m, angles $45^\circ$ and $60^\circ$: $d = 30$, and $s = 30(\sqrt{3} - 1) = 30\sqrt{3} - 30$ m.

> **Rule:** The difference of tangents times the ground distance gives the stacked part. Never multiply the whole height twice.

### A tower standing on a building
Same picture, other way round. You know the building, or you know the tower; the two angles come from the same point.

Building 20 m seen at $30^\circ$, tower top at $60^\circ$, both from one point:

- Ground: $d = 20\cot 30^\circ = 20\sqrt{3}$ m.
- Tower: $d(\tan 60^\circ - \tan 30^\circ) = 20\sqrt{3} \times \dfrac{2}{\sqrt{3}} = 40$ m.

> **Tip:** The building's triangle is $20 = d\tan 30^\circ$; the tower's is $20 + t = d\tan 60^\circ$. Two equations, two unknowns.

### Watching from a roof
From a building's roof you look **down** at a tower's foot and **up** at its top. Two angles, one roof.

- Depression $\alpha$ of the foot: $d = b\cot\alpha$ where $b$ is the building's height.
- Elevation $\beta$ of the top: tower $= b + d\tan\beta$.

Building 10 m, depression $30^\circ$, elevation $60^\circ$: $d = 10\sqrt{3}$ m and tower $= 10 + 10\sqrt{3}\times\sqrt{3} = 40$ m.

> **Watch:** The building's height is inside the second triangle too. Forgetting the extra $b$ is the most common slip here.

### The broken tree
A tree breaks and the top touches the ground some distance away, making angle $\theta$ with the ground.

Let $x$ be the distance from the foot to the touching point:

- Standing stump $= x\tan\theta$.
- Broken piece (the slanting hypotenuse) $= x\sec\theta = \dfrac{x}{\cos\theta}$.
- Original height $=$ stump $+$ broken piece.

At $x = 15$ m and $\theta = 30^\circ$: stump $= 5\sqrt{3}$ m, broken piece $= \dfrac{15}{\sqrt{3}/2} = 10\sqrt{3}$ m, total $= 15\sqrt{3}$ m.

> **Example:** A quick check: the broken piece must be longer than the stump, because it is the slanting side.

### A slipping ladder
A ladder of fixed length $L$ rests at angle $\theta_1$, then slips to $\theta_2$. Both positions share $L$:

- Foot slides by $L\cos\theta_2 - L\cos\theta_1$ (the new angle is smaller, so its cosine is bigger).
- Top drops by $L\sin\theta_1 - L\sin\theta_2$.

Ladder 10 m from $60^\circ$ to $30^\circ$: the foot moves $10\times\dfrac{\sqrt{3}}{2} - 10\times\dfrac{1}{2} = 5\sqrt{3} - 5 = 5(\sqrt{3}-1)$ m.

> **Tip:** Length stays constant. That single fact links the two triangles.
""",
    formulas=[
        {"name": "Stacked object (statue on pedestal)", "tex": r"s = d(\tan\beta - \tan\alpha)",
         "note": "d comes from the lower triangle: d = pedestal height x cot alpha."},
        {"name": "Tower on a building", "tex": r"t = d(\tan\beta - \tan\alpha),\quad d = b\cot\alpha"},
        {"name": "From a roof: depression and elevation", "tex": r"d = b\cot\alpha,\qquad H = b + d\tan\beta"},
        {"name": "Broken tree", "tex": r"\text{stump} = x\tan\theta,\quad \text{broken} = \frac{x}{\cos\theta}",
         "note": "x = distance from the foot to where the top touches."},
    ],
    tricks=[
        {"title": "Subtract the tans, multiply once",
         "body": "For any stacked object, extra height $= d(\\tan\\beta - \\tan\\alpha)$. Compute the tangent difference first, then one multiplication.",
         "example": {"q": "A flagstaff on a pillar is seen from 20 m away. The pillar's top and the flagstaff's top are at $45^\\circ$ and $60^\\circ$. Find the flagstaff's height.",
                     "steps": [r"$\tan 60^\circ - \tan 45^\circ = \sqrt{3} - 1$.",
                               r"Flagstaff $= 20(\sqrt{3}-1)$ m."],
                     "answer": "$20(\\sqrt{3}-1)$ m"}},
        {"title": "Broken tree: tan plus sec",
         "body": "Total height $= x(\\tan\\theta + \\sec\\theta)$ where $x$ is the ground distance to the touching point. At $30^\\circ$ that is $x\\left(\\dfrac{1}{\\sqrt{3}} + \\dfrac{2}{\\sqrt{3}}\\right) = x\\sqrt{3}$.",
         "example": {"q": "A bamboo breaks and its top touches the ground 9 m from the foot at $30^\\circ$ with the ground. The original height was:",
                     "steps": [r"Total $= 9\left(\tan 30^\circ + \sec 30^\circ\right) = 9 \times \sqrt{3}$.",
                               r"$= 9\sqrt{3}$ m."],
                     "answer": "$9\\sqrt{3}$ m"}},
    ],
    mistakes=[
        {"wrong": "Computing the statue's height as $d\\tan\\beta$ (the whole height) and stopping.",
         "right": "Subtract the lower tangent: statue $= d(\\tan\\beta-\\tan\\alpha)$."},
        {"wrong": "Forgetting the building's height when the tower stands on it.",
         "right": "Tower-on-building: total $= b + t$, so the tower alone needs the tangent difference."},
        {"wrong": "Treating the broken piece of a tree as vertical.",
         "right": "The broken piece is the slanting side: $x\\sec\\theta$."},
        {"wrong": "Adding the two angles' tangents instead of subtracting.",
         "right": "The lower triangle's height must come off; subtract."},
        {"wrong": "Using the ladder's old angle after it slips.",
         "right": "Each ladder position is its own triangle; only the length $L$ is shared."},
    ],
    revision=[
        r"Stacked object: extra height $= d(\tan\beta - \tan\alpha)$.",
        r"Ground first: $d$ = lower height $\\times$ cot of the lower angle.",
        r"Tower on building: two equations, $b = d\\tan\\alpha$ and $b+t = d\\tan\\beta$.",
        r"From a roof: $d = b\\cot\\alpha$ (depression), tower $= b + d\\tan\\beta$.",
        r"Broken tree: stump $= x\\tan\\theta$, broken $= x\\sec\\theta$, total is their sum.",
        r"Slipping ladder: foot slides $L(\\cos\\theta_2 - \\cos\\theta_1)$.",
    ],
    patterns=[
        pat("hd-cp-p1", "Statue on a pedestal", "very common",
            "A statue or flagstaff on a pillar; angles to the pillar's top and to the statue's top.",
            r"s = d(\tan\beta - \tan\alpha),\qquad d = p\cot\alpha",
            ["Use the lower angle with the pedestal height to find $d$.",
             "Compute $\\tan\\beta - \\tan\\alpha$.",
             "Multiply by $d$ for the statue's height."],
            "The two angles share one ground distance, so the height difference is one tangent subtraction.",
            "A statue stands on a pedestal 30 m tall. From a point on the ground, the angles of elevation of the top of the pedestal and the top of the statue are $45^\\circ$ and $60^\\circ$. The height of the statue is:",
            [r"$d = 30\cot 45^\circ = 30$ m.",
             r"$\tan 60^\circ - \tan 45^\circ = \sqrt{3} - 1$.",
             r"Statue $= 30(\sqrt{3}-1)$ m."],
            "$30(\\sqrt{3}-1)$ m"),
        pat("hd-cp-p2", "Tower standing on a building", "common",
            "The angles to the building's top and the tower's top come from the same point.",
            r"b = d\tan\alpha,\qquad b + t = d\tan\beta",
            ["Write the building's triangle and find $d$.",
             "Write the full-height triangle.",
             "Subtract for the tower alone."],
            "Two triangles share the ground distance, so the tower is the tangent difference times $d$.",
            "From a point on the ground, the top of a building 20 m high and the top of a tower on it are seen at $30^\\circ$ and $60^\\circ$. The height of the tower is:",
            [r"$d = 20\cot 30^\circ = 20\sqrt{3}$ m.",
             r"Total height $= 20\sqrt{3}\tan 60^\circ = 60$ m.",
             r"Tower $= 60 - 20 = 40$ m."],
            "40 m"),
        pat("hd-cp-p3", "Depression and elevation from a roof", "common",
            "From a roof: looking down at a tower's foot and up at its top.",
            r"d = b\cot\alpha,\qquad H = b + d\tan\beta",
            ["Turn the depression $\\alpha$ into an elevation at the tower's foot.",
             "Solve that triangle for $d$.",
             "Add the building's height to $d\\tan\\beta$ for the tower."],
            "The roof height feeds both triangles: once as the opposite side, once as the base offset.",
            "From the roof of a 10 m building, the angle of depression of the foot of a tower is $30^\\circ$ and the angle of elevation of its top is $60^\\circ$. The height of the tower is:",
            [r"$d = 10\cot 30^\circ = 10\sqrt{3}$ m.",
             r"Height above roof $= 10\sqrt{3}\tan 60^\circ = 30$ m.",
             r"Tower $= 10 + 30 = 40$ m."],
            "40 m"),
        pat("hd-cp-p4", "The broken tree", "common",
            "A tree or pole breaks and the top touches the ground at a distance and angle.",
            r"\text{total} = x\tan\theta + \frac{x}{\cos\theta}",
            ["Mark the distance $x$ from foot to touching point.",
             "Stump $= x\\tan\\theta$; broken piece $= x\\sec\\theta$.",
             "Add them for the original height."],
            "The standing part and the slanting broken part meet at the break height.",
            "A tree breaks and its top touches the ground 15 m from the foot, making $30^\\circ$ with the ground. The original height of the tree was:",
            [r"Stump $= 15\tan 30^\circ = 5\sqrt{3}$ m.",
             r"Broken piece $= \dfrac{15}{\cos 30^\circ} = \dfrac{15 \times 2}{\sqrt{3}} = 10\sqrt{3}$ m.",
             r"Total $= 15\sqrt{3}$ m."],
            "$15\\sqrt{3}$ m"),
        pat("hd-cp-p5", "A slipping ladder", "occasional",
            "A ladder's angle falls; how far the foot slides or the top drops is asked.",
            r"L\cos\theta_2 - L\cos\theta_1",
            ["Write both triangles with the same ladder length $L$.",
             "Foot distances: $L\\cos\\theta_1$ then $L\\cos\\theta_2$.",
             "Subtract for the slide (or use sines for the drop)."],
            "The length is constant, so the change in the ground angle converts straight into ground distance.",
            "A 10 m ladder leaning against a wall at $60^\\circ$ with the ground starts slipping until it makes $30^\\circ$. The foot of the ladder slides through a distance of:",
            [r"First foot distance $= 10\cos 60^\circ = 5$ m.",
             r"New foot distance $= 10\cos 30^\circ = 5\sqrt{3}$ m.",
             r"Slide $= 5\sqrt{3} - 5 = 5(\sqrt{3}-1)$ m."],
            "$5(\\sqrt{3}-1)$ m"),
    ],
)

# ============================================================ patch and save
PATCHES = {
    "hd-basics": BASICS,
    "hd-standard-angles": STANDARD,
    "hd-two-angles": TWO,
    "hd-motion": MOTION,
    "hd-compound": COMPOUND,
}

data = json.loads(TOPIC.read_text(encoding="utf-8"))
for sid, patch in PATCHES.items():
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = {p["id"] for p in patch["patterns"]}
    assert old_ids <= new_ids, f"{sid}: never drop a pattern id: {old_ids - new_ids}"
    others = {p["id"] for s in data["subtopics"] for p in s.get("patterns", []) if s["id"] != sid}
    assert not (others & new_ids), f"{sid}: pattern id clash: {others & new_ids}"
    notes = patch["notes"]
    assert 2500 <= len(notes) <= 5000, f"{sid}: notes length {len(notes)}"
    sub.update(concept=patch["concept"], notes=notes.strip() + "\n", formulas=patch["formulas"],
               tricks=patch["tricks"], mistakes=patch["mistakes"], revision=patch["revision"],
               patterns=patch["patterns"])
    print(f"{sid}: notes {len(notes)} chars, patterns {len(old_ids)} -> {len(new_ids)}")

with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("heights-distances.json updated")
