"""Phase-2 deep content build for quant/heights-distances. Run: py -3 heights-distances.py"""
from _lib import apply_topic
import hd_part1
import hd_part2


def P(pattern, frequency, howToSpot, approach, subtopic, ex_q, ex_sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot,
            "approach": approach, "subtopic": subtopic,
            "example": {"q": ex_q, "solution": ex_sol}}


PYQ = [
    P("Single angle, one unknown", "very common",
      "One angle (30°, 45° or 60°) with either the height or the distance given.",
      r"Standard-angle rule: $d = h$ at 45°, $d = \sqrt3 h$ at 30°, $d = \frac{h}{\sqrt3}$ at 60°; keep the radical until the option match.",
      "hd-basics",
      r"The angle of elevation of the top of a 50 m tower from a point on the ground is $60^\circ$. The distance of the point from the base is:",
      r"$d = \frac{50}{\sqrt3} = \frac{50\sqrt3}{3}$ m."),
    P("Angle of depression from a height", "very common",
      "Lighthouse/cliff/aeroplane looking down at ships, cars or buildings.",
      r"Depression at the eye = elevation at the object; then $d = h\cot\theta$. Two objects → subtract (same side) or add (opposite sides) the two distances.",
      "hd-basics",
      r"From a 100 m cliff the depression of a boat is $30^\circ$. Its distance from the cliff base is:",
      r"$d = 100\tan60^\circ = 100\sqrt3$ m."),
    P("Two angles from two points (walking or opposite sides)", "very common",
      "Elevation changes from α to β after walking $w$ m, or two observers $D$ apart on opposite sides.",
      r"$h = \frac{w}{\cot\alpha - \cot\beta}$ (same side) or $\frac{D}{\cot\alpha + \cot\beta}$ (opposite); 30–60 pairs give $\frac{w\sqrt3}{2}$ and $\frac{D\sqrt3}{4}$.",
      "hd-two-angles",
      r"Walking 40 m towards a tower changes the elevation from $30^\circ$ to $60^\circ$. The height is:",
      r"$h = \frac{40\sqrt3}{2} = 20\sqrt3$ m."),
    P("Speed-time two-angle problem", "common",
      "A car/boat moves at uniform speed; the depression or elevation changes after a stated time.",
      r"Distance = speed × time $= h(\cot\theta_{\text{far}} - \cot\theta_{\text{near}})$; solve for $h$, $v$ or $t$. Remaining distance to the base is $h\cot\theta_{\text{near}}$.",
      "hd-motion",
      r"At 6 m/s a car's depression changes from $30^\circ$ to $60^\circ$ in 6 s. The tower's height is:",
      r"$36 = \frac{2h}{\sqrt3} \Rightarrow h = 18\sqrt3$ m."),
    P("Compound structure (statue/pedestal, tower/building)", "common",
      "A statue on a pedestal, tower on a building, or flagstaff on a tower; two elevations from one point.",
      r"Split at the change point: upper piece $= d(\tan\beta - \tan\alpha)$; a 45° lower angle fixes $d$ = lower height. Roof observations: add the building back.",
      "hd-compound",
      r"A statue on a 30 m pedestal is seen at $45^\circ$ (pedestal top) and $60^\circ$ (statue top). The statue's height is:",
      r"$30\tan60^\circ - 30 = 30(\sqrt3-1)$ m."),
    P("Shadow problems", "common",
      "Shadow length related to height (equal, √3 times, or a ratio), possibly two objects at once.",
      r"Shadow = horizontal distance: $\tan(\text{elevation}) = \frac{h}{\text{shadow}}$. Equal shadows ⇒ equal heights; two objects at one moment share the sun's angle — use ratios.",
      "hd-basics",
      r"A stick 1.5 m casts a 2.5 m shadow while a tower casts 75 m. The tower's height is:",
      r"$75 \times \frac{1.5}{2.5} = 45$ m."),
    P("Broken tree / pole", "occasional",
      "A tree breaks and the top touches the ground at a stated distance and ground angle.",
      r"Standing $= b\tan\theta$; broken (hypotenuse) $= \frac{b}{\cos\theta}$; original height $= b\tan\theta + \frac{b}{\cos\theta}$.",
      "hd-compound",
      r"A tree breaks; the top touches ground 15 m away at $30^\circ$. The original height is:",
      r"$5\sqrt3 + 10\sqrt3 = 15\sqrt3$ m."),
    P("Hypotenuse given (ladder, thread, wire)", "occasional",
      "The slant distance is given with the angle; a height or ground distance asked.",
      r"$h = L\sin\theta$, $d = L\cos\theta$ — sine/cosine, never tangent, when the hypotenuse is the given.",
      "hd-basics",
      r"A 60 m cable makes $60^\circ$ with the ground. The pole height is:",
      r"$60\sin60^\circ = 30\sqrt3$ m."),
]

if __name__ == "__main__":
    subs = [
        hd_part1.build_basics(),
        hd_part1.build_standard(),
        hd_part2.build_two_angles(),
        hd_part2.build_motion(),
        hd_part2.build_compound(),
    ]
    apply_topic("heights-distances", subs, PYQ)
