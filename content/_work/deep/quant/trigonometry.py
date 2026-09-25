"""Phase-2 deep content build for quant/trigonometry. Run: py -3 trigonometry.py"""
from _lib import apply_topic
import trig_part1
import trig_part2


def P(pattern, frequency, howToSpot, approach, subtopic, ex_q, ex_sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot,
            "approach": approach, "subtopic": subtopic,
            "example": {"q": ex_q, "solution": ex_sol}}


PYQ = [
    P("Standard values at special angles", "very common",
      "A sum/difference/product of sin/cos/tan (often sec/cosec/cot too) at 0°, 30°, 45°, 60°, 90° asked as one value.",
      r"Convert every function to its table value via the $\frac{\sqrt{k}}{2}$ construction (reciprocals for sec/cosec/cot), then compute with exact fractions. Keep surds as surds; rationalise only the final answer.",
      "trig-ratios",
      r"The value of $\tan 45^\circ + \cot 45^\circ$ is:",
      r"$\tan 45^\circ = 1$ and $\cot 45^\circ = 1$: sum $= 2$."),
    P("One ratio given → the rest of the triangle", "very common",
      "'If sinθ = 3/5 find tanθ' style — one ratio (sometimes surd form), other ratios asked.",
      r"Draw the right triangle from the given ratio, complete the third side by Pythagoras (expect a triplet), and read the asked ratio off the same triangle w.r.t. the named angle.",
      "trig-ratios",
      r"If $\cosec\theta = \frac{13}{5}$ ($\theta$ acute), the value of $\tan\theta$ is:",
      r"$\sin\theta = \frac{5}{13}$ → triangle 5-12-13: $\tan\theta = \frac{5}{12}$."),
    P("Conjugate pairs: sec±tan, cosec±cot", "very common",
      "'If secθ + tanθ = m, find secθ − tanθ' — or the pair subtracted/added to extract an individual ratio.",
      r"$(\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = 1$, so the conjugate is its reciprocal $\frac{1}{m}$. Adding/subtracting the pair gives $2\sec\theta$ and $2\tan\theta$ individually; a triangle then returns sin/cos.",
      "trig-identities",
      r"If $\cosec\theta + \cot\theta = 3$ ($\theta$ acute), the value of $\cosec\theta - \cot\theta$ is:",
      r"$\cosec\theta - \cot\theta = \frac{1}{\cosec\theta + \cot\theta} = \frac13$."),
    P("sinθ + cosθ = m family", "very common",
      "A sum (or difference) of sin and cos given as m; the product sinθcosθ, the opposite difference, or a cubic combination asked.",
      r"Square the given: $\sin\theta\cos\theta = \frac{m^2-1}{2}$; $(\sin\theta - \cos\theta)^2 = 2 - m^2$; cubes via $x^3+y^3=(x+y)(x^2-xy+y^2)$. Sub-specials: $m = \sqrt2$ → product $\frac12$; $m = 1$ → product $0$.",
      "trig-valueput",
      r"If $\sin\theta + \cos\theta = \frac{6}{5}$, the value of $\sin\theta\cos\theta$ is:",
      r"$\frac{m^2-1}{2} = \frac{\frac{36}{25}-1}{2} = \frac{11}{50}$."),
    P("tanθ given → linear fraction in sin and cos", "very common",
      "tanθ = p/q (or 5tanθ = 4 style); a fraction like (a·sinθ + b·cosθ)/(c·cosθ + d·sinθ) asked.",
      r"Divide numerator and denominator by $\cos\theta$: the fraction becomes $\frac{a\tan\theta + b}{c + d\tan\theta}$. Substitute $t = \frac{p}{q}$ exactly (fractions, not decimals) and simplify once.",
      "trig-valueput",
      r"If $\tan\theta = \frac{4}{3}$, the value of $\frac{3\sin\theta + 2\cos\theta}{3\cos\theta - 2\sin\theta}$ is:",
      r"Divide by $\cos\theta$: $\frac{3\cdot\frac43 + 2}{3 - 2\cdot\frac43} = \frac{6}{\frac13} = 18$."),
    P("Complementary pairs collapse a sum/product", "very common",
      "Angles pair to 90° (35 & 55, 20 & 70...) across different functions — or a long tangent chain with 45° in the middle.",
      r"Flip one function of each pair: $\sec 55^\circ = \frac{1}{\sin 35^\circ}$ etc.; products like $\tan\theta\tan(90^\circ-\theta) = 1$. Chains $\tan 1^\circ \cdots \tan 89^\circ$ collapse to 1. Difference-of-twins questions ($\cos 50^\circ - \sin 40^\circ$) are instantly 0.",
      "trig-complementary",
      r"The value of $\tan 10^\circ \tan 20^\circ \tan 70^\circ \tan 80^\circ$ is:",
      r"Pairs: $10+80 = 90$ and $20+70 = 90$; each pair multiplies to 1, so the product is 1."),
    P("Angle from a complementary-function equality", "very common",
      "'If sin 3A = cos(A − 10°), find A' — different functions at related angles, one unknown.",
      r"Force the same function ($\cos x = \sin(90^\circ - x)$) or use the shortcut: complementary-function arguments sum to $90^\circ$. Solve the resulting linear equation; sanity-check the angle keeps all arguments in range.",
      "trig-complementary",
      r"If $\tan 2\theta = \cot(\theta - 12^\circ)$, the value of $\theta$ is:",
      r"$2\theta + \theta - 12^\circ = 90^\circ \Rightarrow 3\theta = 102^\circ \Rightarrow \theta = 34^\circ$."),
    P("Max/min of a·sinθ ± b·cosθ", "very common",
      "'Find the maximum of 4sinθ + 3cosθ' — Pythagorean coefficients; minimum may be asked instead.",
      r"Max $= +\sqrt{a^2+b^2}$, min $= -\sqrt{a^2+b^2}$ (unrestricted θ); with $0^\circ \le \theta \le 90^\circ$ check endpoints too. Expect triplets: (3,4,5), (5,12,13), (8,15,17).",
      "trig-maxmin",
      r"The maximum value of $8\sin\theta - 15\cos\theta$ is:",
      r"$\sqrt{8^2 + 15^2} = 17$ (minimum $-17$)."),
    P("AM-GM bounds and sinθcosθ ≤ ½", "common",
      "Minimum of tan²+cot², sec²+cosec², tan+cot — or the max of sinθcosθ / 2sinθcosθ.",
      r"$x + \frac1x \ge 2$ (equality $x=1$, i.e. 45°); $\sec^2\theta + \cosec^2\theta = \frac{1}{\sin^2\theta\cos^2\theta} \ge 4$; $\sin\theta\cos\theta \le \frac12$ peaking at 45°.",
      "trig-maxmin",
      r"The minimum value of $\tan\theta + \cot\theta$ ($\theta$ acute) is:",
      r"$\tan\theta + \frac{1}{\tan\theta} \ge 2$, equality at $\theta = 45^\circ$."),
    P("Two sides of the right triangle → a named ratio", "common",
      "Two sides given (or hyp + one leg); sin/cos/tan of one acute angle asked — the angle described in words ('opposite the longer leg').",
      r"Third side by Pythagoras, then attach opposite/adjacent to the NAMED angle — 'opposite the shorter leg' is the smaller angle. Triplet multiples supply the exam numbers.",
      "trig-ratios",
      r"In a right triangle, the legs adjacent to and opposite an acute angle are $15$ cm and $8$ cm. The hypotenuse is:",
      r"$\sqrt{15^2 + 8^2} = \sqrt{289} = 17$ cm (8-15-17)."),
]

if __name__ == "__main__":
    subs = [
        trig_part1.build_ratios(),
        trig_part1.build_identities(),
        trig_part2.build_complementary(),
        trig_part2.build_valueput(),
        trig_part2.build_maxmin(),
    ]
    apply_topic("trigonometry", subs, PYQ)
