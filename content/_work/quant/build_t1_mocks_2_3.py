# -*- coding: utf-8 -*-
"""Build t1-mock-2--quant.json and t1-mock-3--quant.json (25 Qs each).

Every numeric answer is re-derived in Python and asserted against the option string
before the file is written. Also checks: 4 unique options, balanced answer letters,
difficulty mix, topic distribution, no control characters (\\t etc. from bad escapes),
and no duplicate question text vs topics/*.json, other mock parts, and each other.
"""
import glob
import json
import math
import os
import random
import re
import sys
from collections import Counter
from fractions import Fraction as F

import sympy as sp

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl"
PARTS = os.path.join(ROOT, "mocks", "parts")
TOPICS = {
    "number-system", "simplification", "hcf-lcm", "percentage", "ratio-proportion",
    "average", "interest", "profit-loss-discount", "mixture-alligation", "time-work",
    "time-speed-distance", "algebra", "geometry", "mensuration-2d", "mensuration-3d",
    "trigonometry", "heights-distances", "statistics", "data-interpretation",
}


def Q(q, correct, wrongs, solution, shortcut, difficulty, subtopic, pattern, timeSec):
    """Question with the correct option first; final placement is done in finalize()."""
    opts = [correct] + list(wrongs)
    assert len(opts) == 4, q
    assert len(set(opts)) == 4, "duplicate options: %r" % opts
    assert difficulty in ("easy", "medium", "hard")
    assert subtopic in TOPICS, subtopic
    assert 5 <= timeSec <= 300
    return {"q": q, "figure": None, "options": opts, "answer": 0, "solution": solution,
            "shortcut": shortcut, "difficulty": difficulty, "subtopic": subtopic,
            "pattern": pattern, "timeSec": timeSec}


def rupee(n):
    return "₹{:,}".format(n)


def near(a, b, eps=1e-9):
    return abs(float(a) - float(b)) < eps


# =============================================================================
#  MOCK 2  (CGL 2025 Tier 1 level)
# =============================================================================
m2 = []

# 1. simplification - 'of' precedence (easy)
v = F(96, 4 * 6) + F(5 * 8, 10) - 3
wrong_ltr = F(96, 4) * 6 + F(5 * 8, 10) - 3
assert v == 5 and wrong_ltr == 145
m2.append(Q(
    r"Simplify: $96 \div 4 \text{ of } 6 + 5 \times 8 \div 10 - 3$",
    "5", ["145", "8", "3"],
    r"'of' is solved before $\div$: $4 \text{ of } 6 = 24$, so $96 \div 24 = 4$. Next $5 \times 8 \div 10 = 4$. Value $= 4 + 4 - 3 = 5$.",
    r"Read 'of' as a bracketed multiplication: $96 \div (4 \times 6)$. Treating it as a plain $\times$ after $\div$ gives the trap 145.",
    "easy", "simplification", "BODMAS with 'of'", 35))

# 2. simplification - exponents (medium)
n = sp.symbols("n")
expr = (5**(n + 2) - 6 * 5**(n + 1)) / (13 * 5**n - 2 * 5**(n + 1))
assert sp.simplify(expr - sp.Rational(-5, 3)) == 0
m2.append(Q(
    r"What is the value of $\dfrac{5^{n+2} - 6 \cdot 5^{n+1}}{13 \cdot 5^{n} - 2 \cdot 5^{n+1}}$?",
    r"$-\frac{5}{3}$", [r"$\frac{5}{3}$", r"$-\frac{5}{23}$", r"$-\frac{5}{13}$"],
    r"Take $5^n$ common from both: numerator $= 5^n(25 - 30) = -5 \cdot 5^n$, denominator $= 5^n(13 - 10) = 3 \cdot 5^n$. Value $= -\frac{5}{3}$.",
    r"Put $n = 0$: $\frac{25 - 30}{13 - 10} = -\frac{5}{3}$. Watch the signs — $13 + 10$ in the denominator gives the trap $-\frac{5}{23}$.",
    "medium", "simplification", "common power factor out", 40))

# 3. percentage - failed in two subjects (medium)
fail_any = 35 + 25 - 10
total = F(300 * 100, 100 - fail_any)
assert total == 600 and F(30000, 100 - 35 - 25) == 750 and F(30000, 60) == 500
m2.append(Q(
    "In an examination, 35% of the candidates failed in Hindi, 25% failed in English and 10% failed in both subjects. If 300 candidates passed in both subjects, how many candidates appeared in the examination?",
    "600", ["750", "500", "1000"],
    r"Failed in at least one subject $= 35 + 25 - 10 = 50\%$. Passed in both $= 100 - 50 = 50\%$. So $50\%$ of total $= 300 \Rightarrow$ total $= 600$.",
    r"Venn rule: $n(A \cup B) = A + B - \text{both}$. Forgetting to add back the 10% gives $40\%$ passing and the trap 750.",
    "medium", "percentage", "pass-fail Venn percentage", 45))

# 4. percentage - more than a third number (easy)
v = F(130, 150) * 100
assert v == F(260, 3) and F(150, 130) * 100 == F(1500, 13)
m2.append(Q(
    "Two numbers are respectively 30% and 50% more than a third number. The first number is what per cent of the second number?",
    r"$86\frac{2}{3}\%$", ["80%", r"$115\frac{5}{13}\%$", "60%"],
    r"Let the third number $= 100$. Then the first $= 130$ and the second $= 150$. Required $= \frac{130}{150} \times 100 = 86\frac{2}{3}\%$.",
    r"$\frac{130}{150} = \frac{13}{15}$; $\frac{1}{15} = 6\frac{2}{3}\%$, so $13 \times 6\frac{2}{3} = 86\frac{2}{3}\%$. Do not just subtract $50 - 30$.",
    "easy", "percentage", "percent of a common base", 35))

# 5. ratio - incomes and expenditures (medium)
x, y = sp.symbols("x y")
sol = sp.solve([5 * x - 3 * y - 8000, 4 * x - 2 * y - 8000], [x, y])
assert sol[x] == 4000 and sol[y] == 4000
A_inc = 5 * sol[x]
assert A_inc == 20000
m2.append(Q(
    "The incomes of A and B are in the ratio 5 : 4 and their expenditures are in the ratio 3 : 2. If each of them saves ₹8,000, what is A's income?",
    rupee(20000), [rupee(16000), rupee(12000), rupee(24000)],
    r"Let incomes be $5x, 4x$ and expenditures $3y, 2y$. Then $5x - 3y = 8000$ and $4x - 2y = 8000$. From the second, $y = 2x - 4000$; substituting, $5x - 6x + 12000 = 8000 \Rightarrow x = 4000$. A's income $= 5x = ₹20{,}000$.",
    r"Equal savings: multiply to kill $y$ — $2(5x - 3y) - 3(4x - 2y) = 2(8000) - 3(8000) \Rightarrow -2x = -8000$, $x = 4000$. Check B: $16000 - 8000 = 8000$ saved.",
    "medium", "ratio-proportion", "income-expenditure equal savings", 60))

# 6. average - family before birth of youngest (medium)
tot_now = 6 * 25
v = F(tot_now - 7 - 5 * 7, 5)
assert v == F(108, 5)
assert F(tot_now - 7, 5) == F(143, 5) and F(tot_now - 42, 6) == 18 and F(tot_now - 35, 5) == 23
m2.append(Q(
    "The average age of a family of 6 members is 25 years. If the youngest member is 7 years old, what was the average age of the family just before the birth of the youngest member?",
    "21.6 years", ["28.6 years", "18 years", "23 years"],
    r"Present total $= 6 \times 25 = 150$. Remove the youngest: $150 - 7 = 143$ for the other 5. Seven years ago each of these 5 was 7 years younger: $143 - 5 \times 7 = 108$. Average $= \frac{108}{5} = 21.6$ years.",
    r"Take away the child's age AND 7 years from each of the other 5: $\frac{150 - 7 - 35}{5} = 21.6$. Forgetting the 35 gives 28.6; dividing by 6 gives 18.",
    "medium", "average", "average before a birth", 50))

# 7. interest - CI minus SI for 2 years (medium)
P = F(48) * (F(100, 8)) ** 2
assert P == 7500
Pc = sp.Rational(7500)
assert Pc * (sp.Rational(108, 100) ** 2 - 1) - Pc * sp.Rational(16, 100) == 48
m2.append(Q(
    "The difference between the compound interest and the simple interest on a sum for 2 years at 8% per annum is ₹48. What is the sum?",
    rupee(7500), [rupee(6000), rupee(600), rupee(3750)],
    r"For 2 years, $\text{CI} - \text{SI} = P\left(\frac{R}{100}\right)^2$. So $48 = P \times \frac{64}{10000} \Rightarrow P = \frac{48 \times 10000}{64} = ₹7{,}500$.",
    r"$\left(\frac{100}{R}\right)^2 = 12.5^2 = 156.25$; $48 \times 156.25 = 7500$. Using $\frac{100}{R}$ only once gives the trap 600.",
    "medium", "interest", "CI-SI difference 2 years", 40))

# 8. profit - buy 15 sell 12 (easy)
cp1, sp1 = F(100, 15), F(100, 12)
v = (sp1 - cp1) / cp1 * 100
assert v == 25
m2.append(Q(
    "A shopkeeper buys pens at 15 for ₹100 and sells them at 12 for ₹100. What is his profit per cent?",
    "25%", ["20%", r"$16\frac{2}{3}\%$", "30%"],
    r"CP of 1 pen $= ₹\frac{100}{15}$, SP of 1 pen $= ₹\frac{100}{12}$. Profit $\% = \frac{\frac{100}{12} - \frac{100}{15}}{\frac{100}{15}} \times 100 = \frac{15 - 12}{12} \times 100 = 25\%$.",
    r"Same money, different counts: profit $\% = \frac{\text{bought} - \text{sold}}{\text{sold}} \times 100 = \frac{3}{12} = 25\%$. Dividing by 15 instead gives the trap 20%.",
    "easy", "profit-loss-discount", "buy n sell m for same price", 35))

# 9. discount - find second successive discount (medium)
after1 = F(2400) * F(85, 100)
xd = (1 - F(1632) / after1) * 100
assert after1 == 2040 and xd == 20
single = (1 - F(1632, 2400)) * 100
assert single == 32
m2.append(Q(
    "The marked price of a cooler is ₹2,400. After two successive discounts, the first of 15% and the second of $x\\%$, it is sold for ₹1,632. What is the value of $x$?",
    "20", ["17", "32", "25"],
    r"After the first discount: $2400 \times 0.85 = 2040$. Second discount $= \frac{2040 - 1632}{2040} \times 100 = \frac{408}{2040} \times 100 = 20\%$.",
    r"The single equivalent discount is $\frac{768}{2400} = 32\%$, but successive discounts do not subtract: $32 - 15 = 17$ is the trap. Work on the reduced price 2040.",
    "medium", "profit-loss-discount", "find second successive discount", 45))

# 10. time-work - efficiency percent (medium)
a_eff, b_eff = 8, 5  # A 60% more efficient
work = (a_eff + b_eff) * 20
assert F(160, 100) == F(a_eff, b_eff)
assert F(work, b_eff) == 52 and F(work, a_eff) == F(65, 2)
m2.append(Q(
    "A is 60% more efficient than B. Working together, they can finish a piece of work in 20 days. In how many days can B alone finish the work?",
    "52 days", ["32.5 days", "32 days", "40 days"],
    r"Efficiency A : B $= 160 : 100 = 8 : 5$. Total work $= (8 + 5) \times 20 = 260$ units. B alone $= \frac{260}{5} = 52$ days.",
    r"Time $\propto \frac{1}{\text{efficiency}}$: B alone $= 20 \times \frac{8 + 5}{5} = 52$ days. $\frac{260}{8} = 32.5$ is A's time — a common mix-up.",
    "medium", "time-work", "efficiency percentage", 45))

# 11. TSD - trains after crossing (hard)
sx = 64
sy = F(sx) * F(3, 4)  # sx/sy = sqrt(16/9) = 4/3
assert sy == 48
t_meet = F(9) * sx / sy
assert t_meet == 16 * sy / F(sx)  # consistency of the meeting time
assert F(64 * 9, 16) == 36 and F(64 * 4, 3) == F(256, 3) and F(64 * 16, 9) == F(1024, 9)
m2.append(Q(
    "Two trains start at the same time from stations X and Y and move towards each other. After passing each other, the train from X takes 9 hours to reach Y and the train from Y takes 16 hours to reach X. If the speed of the train from X is 64 km/h, what is the speed of the train from Y?",
    "48 km/h", ["36 km/h", r"$85\frac{1}{3}$ km/h", r"$113\frac{7}{9}$ km/h"],
    r"Let them meet after $t$ hours. The part the X-train still has to cover ($64 \times 9$) was covered by the Y-train in $t$ hours, and vice versa: $S_Y t = 9 S_X$ and $S_X t = 16 S_Y$. Dividing, $\left(\frac{S_X}{S_Y}\right)^2 = \frac{16}{9}$, so $\frac{S_X}{S_Y} = \frac{4}{3}$ and $S_Y = \frac{3}{4} \times 64 = 48$ km/h.",
    r"$\frac{S_1}{S_2} = \sqrt{\frac{t_2}{t_1}}$ — the times go in reverse and under a square root: $\sqrt{\frac{16}{9}} = \frac{4}{3}$. Forgetting the root gives 36.",
    "hard", "time-speed-distance", "speed ratio after meeting", 60))

# 12. algebra - quadratic to x+1/x (easy)
xs = sp.symbols("xs")
for r in sp.solve(xs**2 - 7 * xs + 1, xs):
    assert sp.simplify(r**2 + 1 / r**2 - 47) == 0
m2.append(Q(
    r"If $x^2 - 7x + 1 = 0$, what is the value of $x^2 + \frac{1}{x^2}$?",
    "47", ["51", "49", "45"],
    r"Divide the equation by $x$: $x - 7 + \frac{1}{x} = 0 \Rightarrow x + \frac{1}{x} = 7$. Then $x^2 + \frac{1}{x^2} = 7^2 - 2 = 47$.",
    r"$x^2 - kx + 1 = 0$ means $x + \frac1x = k$; square and subtract 2. Adding 2 instead gives the trap 51.",
    "easy", "algebra", "quadratic to x+1/x", 30))

# 13. algebra - sixth power ladder (hard)
for r in sp.solve(xs**2 - 3 * xs + 1, xs):
    assert sp.simplify(r**6 + 1 / r**6 - 322) == 0
assert 7**3 - 3 * 7 == 322 and 18**2 - 2 == 322
m2.append(Q(
    r"If $a + \frac{1}{a} = 3$, what is the value of $a^6 + \frac{1}{a^6}$?",
    "322", ["343", "324", "729"],
    r"$a^2 + \frac{1}{a^2} = 3^2 - 2 = 7$. Then $a^6 + \frac{1}{a^6} = \left(a^2 + \frac{1}{a^2}\right)^3 - 3\left(a^2 + \frac{1}{a^2}\right) = 343 - 21 = 322$.",
    r"Two routes, same answer: $a^3 + \frac{1}{a^3} = 27 - 9 = 18$, then square and subtract 2: $324 - 2 = 322$. Stopping at $7^3$ or $18^2$ gives the traps 343 and 324.",
    "hard", "algebra", "x+1/x sixth power", 60))

# 14. geometry - incentre angle reverse (medium)
A = 2 * (118 - 90)
assert A == 56 and 90 + F(A, 2) == 118
m2.append(Q(
    r"In $\triangle ABC$, the internal bisectors of $\angle B$ and $\angle C$ meet at $I$. If $\angle BIC = 118^\circ$, what is the measure of $\angle A$?",
    r"$56^\circ$", [r"$62^\circ$", r"$28^\circ$", r"$59^\circ$"],
    r"For the incentre, $\angle BIC = 90^\circ + \frac{\angle A}{2}$. So $118 = 90 + \frac{A}{2} \Rightarrow \frac{A}{2} = 28^\circ \Rightarrow \angle A = 56^\circ$.",
    r"$\angle A = 2(\angle BIC - 90^\circ) = 2 \times 28 = 56^\circ$. Stopping at $28^\circ$ (forgetting to double) is the classic slip.",
    "medium", "geometry", "incentre angle BIC", 35))

# 15. geometry - polygon angle sum (easy)
nsides = 1980 // 180 + 2
assert (nsides - 2) * 180 == 1980 and nsides == 13
m2.append(Q(
    r"The sum of the interior angles of a polygon is $1980^\circ$. How many sides does the polygon have?",
    "13", ["11", "12", "15"],
    r"Sum of interior angles $= (n - 2) \times 180^\circ$. So $(n - 2) \times 180 = 1980 \Rightarrow n - 2 = 11 \Rightarrow n = 13$.",
    r"$1980 \div 180 = 11$, then add 2. Stopping at 11 is the trap.",
    "easy", "geometry", "polygon interior angle sum", 25))

# 16. geometry - Apollonius median (hard)
AB, AC, BC = 10, 14, 16
AD2 = F(AB**2 + AC**2, 2) - F(BC, 2) ** 2
assert AD2 == 84
# coordinate check: B(0,0), C(16,0), A(p,q)
p = F(AB**2 - AC**2 + BC**2, 2 * BC)
q2 = AB**2 - p**2
Dx = F(BC, 2)
assert (p - Dx) ** 2 + q2 == 84
m2.append(Q(
    r"In $\triangle ABC$, $AB = 10$ cm, $AC = 14$ cm and $BC = 16$ cm. If $AD$ is the median to $BC$, what is the length of $AD$?",
    r"$2\sqrt{21}$ cm", ["12 cm", r"$2\sqrt{35}$ cm", r"$2\sqrt{58}$ cm"],
    r"Apollonius' theorem: $AB^2 + AC^2 = 2(AD^2 + BD^2)$ with $BD = 8$. So $100 + 196 = 2(AD^2 + 64) \Rightarrow AD^2 = 148 - 64 = 84 \Rightarrow AD = 2\sqrt{21}$ cm.",
    r"$AD^2 = \frac{AB^2 + AC^2}{2} - \left(\frac{BC}{2}\right)^2 = 148 - 64 = 84$. Forgetting to halve $296$ gives $2\sqrt{58}$; 12 is just the average of the two sides.",
    "hard", "geometry", "median length Apollonius", 60))

# 17. heights - building and tower (medium)
d = 45  # depression 45 deg to foot => horizontal distance = 45
tower = d + d * sp.tan(sp.pi / 6)
assert sp.simplify(tower - 15 * (3 + sp.sqrt(3))) == 0
assert sp.simplify(d + d * sp.tan(sp.pi / 3) - 45 * (1 + sp.sqrt(3))) == 0
m2.append(Q(
    r"From the top of a 45 m high building, the angle of elevation of the top of a tower is $30^\circ$ and the angle of depression of the foot of the tower is $45^\circ$. What is the height of the tower?",
    r"$15(3 + \sqrt{3})$ m", [r"$45(1 + \sqrt{3})$ m", r"$15\sqrt{3}$ m", r"$15(3 - \sqrt{3})$ m"],
    r"Depression $45^\circ$ to the foot: horizontal distance $= 45$ m. Height of the tower above the building's roof $= 45 \tan 30^\circ = \frac{45}{\sqrt{3}} = 15\sqrt{3}$ m. Tower $= 45 + 15\sqrt{3} = 15(3 + \sqrt{3})$ m.",
    r"Tower $=$ building $+$ distance $\times \tan(\text{elevation})$ $= 45 + 45 \times \frac{1}{\sqrt{3}}$. Using $\tan 60^\circ$ by mistake gives $45(1 + \sqrt{3})$.",
    "medium", "heights-distances", "elevation and depression from a building", 50))

# 18. mensuration-2d - Heron (medium)
a_, b_, c_ = 13, 14, 15
s = F(a_ + b_ + c_, 2)
area2 = s * (s - a_) * (s - b_) * (s - c_)
assert area2 == 84**2
m2.append(Q(
    "What is the area of a triangle whose sides are 13 cm, 14 cm and 15 cm?",
    "84 cm²", ["91 cm²", "168 cm²", "105 cm²"],
    r"$s = \frac{13 + 14 + 15}{2} = 21$. Area $= \sqrt{21 \times 8 \times 7 \times 6} = \sqrt{7056} = 84$ cm².",
    r"13-14-15 splits into two right triangles (5-12-13 and 9-12-15) on base 14 with height 12: $\frac{1}{2} \times 14 \times 12 = 84$. Treating it as right-angled ($\frac12 \times 13 \times 14 = 91$) is the trap.",
    "medium", "mensuration-2d", "Heron's formula triangle", 45))

# 19. mensuration-3d - cone from CSA (medium)
pi = F(22, 7)
r_ = 21
l_ = F(1914) / (pi * r_)
assert l_ == 29
h_ = math.isqrt(29**2 - 21**2)
assert h_ == 20 and h_**2 == 29**2 - 21**2
V = F(1, 3) * pi * r_**2 * h_
assert V == 9240 and F(1, 3) * pi * r_**2 * 29 == 13398 and pi * r_**2 * h_ == 27720
m2.append(Q(
    r"The base radius of a right circular cone is 21 cm and its curved surface area is 1914 cm². What is the volume of the cone? [Use $\pi = \frac{22}{7}$]",
    "9240 cm³", ["13398 cm³", "27720 cm³", "4620 cm³"],
    r"CSA $= \pi r l \Rightarrow 1914 = \frac{22}{7} \times 21 \times l = 66l \Rightarrow l = 29$ cm. Height $= \sqrt{29^2 - 21^2} = \sqrt{400} = 20$ cm. Volume $= \frac{1}{3} \times \frac{22}{7} \times 21^2 \times 20 = 9240$ cm³.",
    r"20-21-29 is a Pythagorean triplet — spot it and skip the square root. Using the slant height 29 as the height gives the trap 13398; dropping $\frac{1}{3}$ gives 27720.",
    "medium", "mensuration-3d", "cone volume from CSA", 60))

# 20. trigonometry - standard values (easy)
val = sp.sin(sp.pi / 6) ** 2 + sp.cos(sp.pi / 4) ** 2 + sp.tan(sp.pi / 3) ** 2
assert sp.simplify(val - sp.Rational(15, 4)) == 0
m2.append(Q(
    r"What is the value of $\sin^2 30^\circ + \cos^2 45^\circ + \tan^2 60^\circ$?",
    r"$\frac{15}{4}$", ["4", r"$\frac{3}{4} + \sqrt{3}$", r"$\frac{13}{4}$"],
    r"$\sin^2 30^\circ = \frac{1}{4}$, $\cos^2 45^\circ = \frac{1}{2}$, $\tan^2 60^\circ = 3$. Sum $= \frac{1}{4} + \frac{1}{2} + 3 = \frac{15}{4}$.",
    r"Square every value before adding. Using $\sin 30^\circ = \frac12$ unsquared gives 4; leaving $\tan 60^\circ = \sqrt3$ unsquared gives $\frac34 + \sqrt3$.",
    "easy", "trigonometry", "standard angle values", 30))

# 21. trigonometry - sec+tan to cos (hard)
th = sp.symbols("th")
sec_v = (4 + sp.Rational(1, 4)) / 2
assert sec_v == sp.Rational(17, 8)
tan_v = 4 - sec_v
assert sec_v**2 - tan_v**2 == 1
m2.append(Q(
    r"If $\sec\theta + \tan\theta = 4$ and $\theta$ is acute, what is the value of $\cos\theta$?",
    r"$\frac{8}{17}$", [r"$\frac{15}{17}$", r"$\frac{17}{8}$", r"$\frac{8}{15}$"],
    r"Since $\sec^2\theta - \tan^2\theta = 1$, $(\sec\theta - \tan\theta) = \frac{1}{4}$. Adding the two equations: $2\sec\theta = 4 + \frac{1}{4} = \frac{17}{4} \Rightarrow \sec\theta = \frac{17}{8}$. So $\cos\theta = \frac{8}{17}$.",
    r"$\sec\theta = \frac{1}{2}\left(k + \frac{1}{k}\right)$ for $\sec\theta + \tan\theta = k$: $\frac{1}{2}\left(4 + \frac14\right) = \frac{17}{8}$, so $\cos\theta = \frac{8}{17}$. $\frac{15}{17}$ is $\sin\theta$ — read the question.",
    "hard", "trigonometry", "sec+tan reciprocal pair", 60))

# 22. statistics - weighted mean (medium)
xsv = [4, 6, 8, 10, 12]
fsv = [3, 5, 9, 2, 1]
mean = F(sum(a * b for a, b in zip(xsv, fsv)), sum(fsv))
assert mean == F(73, 10)
assert F(sum(xsv), 5) == 8 and F(146, 5) == F(292, 10)
m2.append(Q(
    "Find the mean of the following frequency distribution:\n\n| $x$ | 4 | 6 | 8 | 10 | 12 |\n|---|---|---|---|---|---|\n| $f$ | 3 | 5 | 9 | 2 | 1 |",
    "7.3", ["8", "29.2", "7.5"],
    r"$\sum f = 3 + 5 + 9 + 2 + 1 = 20$. $\sum fx = 12 + 30 + 72 + 20 + 12 = 146$. Mean $= \frac{146}{20} = 7.3$.",
    r"Mean $= \frac{\sum fx}{\sum f}$ — divide by the total frequency 20, not by the 5 values (which gives 29.2). The plain average of $x$ (8) ignores the weights.",
    "medium", "statistics", "mean of frequency table", 45))

# 23-25. DI laptops table
DI2 = {"A": (45, 54, 63), "B": (60, 48, 72), "C": (36, 45, 54), "D": (50, 65, 55), "E": (40, 52, 48)}
table2 = ("The table shows the number of laptops (in thousands) sold by five companies A, B, C, D and E in three years:\n\n"
          "| Company | 2022 | 2023 | 2024 |\n|---|---|---|---|\n"
          + "".join("| %s | %d | %d | %d |\n" % (k, *v_) for k, v_ in DI2.items()))

inc = F(DI2["B"][2] - DI2["B"][1], DI2["B"][1]) * 100
assert inc == 50 and F(24, 72) * 100 == F(100, 3)
m2.append(Q(
    table2 + "\nBy what per cent did the sales of company B increase from 2023 to 2024?",
    "50%", [r"$33\frac{1}{3}\%$", "20%", "24%"],
    r"B: 2023 $= 48$, 2024 $= 72$. Increase $= 24$. Per cent increase $= \frac{24}{48} \times 100 = 50\%$.",
    r"Divide the change by the OLD value (48). Dividing by the new value 72 gives the trap $33\frac13\%$; 20% compares 2024 with 2022.",
    "easy", "data-interpretation", "table percent increase", 35))

t22 = sum(v_[0] for v_ in DI2.values())
t23 = sum(v_[1] for v_ in DI2.values())
more = F(t23 - t22, t22) * 100
assert (t22, t23) == (231, 264) and more == F(100, 7)
assert F(33, 264) * 100 == F(25, 2)
m2.append(Q(
    table2 + "\nThe total sales of all five companies in 2023 is what per cent more than their total sales in 2022?",
    r"$14\frac{2}{7}\%$", [r"$12\frac{1}{2}\%$", "33%", "15%"],
    r"Total 2022 $= 45 + 60 + 36 + 50 + 40 = 231$. Total 2023 $= 54 + 48 + 45 + 65 + 52 = 264$. Required $= \frac{264 - 231}{231} \times 100 = \frac{33}{231} \times 100 = \frac{100}{7} = 14\frac{2}{7}\%$.",
    r"$\frac{33}{231} = \frac{1}{7} = 14\frac{2}{7}\%$ from the fraction table. Base is 2022 (the 'than' year); using 264 as the base gives $12\frac12\%$.",
    "medium", "data-interpretation", "table total percent more", 60))

avg_abc = F(DI2["A"][2] + DI2["B"][2] + DI2["C"][2], 3)
avg_de = F(DI2["D"][0] + DI2["E"][0], 2)
pm = (avg_abc - avg_de) / avg_de * 100
assert avg_abc == 63 and avg_de == 45 and pm == 40
assert (avg_abc - avg_de) / avg_abc * 100 == F(200, 7)
m2.append(Q(
    table2 + "\nThe average sales of companies A, B and C in 2024 is what per cent more than the average sales of companies D and E in 2022?",
    "40%", [r"$28\frac{4}{7}\%$", "18%", "25%"],
    r"Average of A, B, C in 2024 $= \frac{63 + 72 + 54}{3} = \frac{189}{3} = 63$. Average of D, E in 2022 $= \frac{50 + 40}{2} = 45$. Required $= \frac{63 - 45}{45} \times 100 = 40\%$.",
    r"$\frac{63}{45} = \frac{7}{5} = 1.4 \Rightarrow 40\%$ more. Dividing 18 by 63 gives $28\frac47\%$ (wrong base); 18 is the raw difference, not a per cent.",
    "hard", "data-interpretation", "table averages compared", 70))


# =============================================================================
#  MOCK 3  (final-week, slightly tougher)
# =============================================================================
m3 = []

# 1. simplification - telescoping (medium)
v = sum(F(1, k * (k + 1)) for k in range(1, 25))
assert v == F(24, 25)
m3.append(Q(
    r"What is the value of $\frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4} + \cdots + \frac{1}{24 \times 25}$?",
    r"$\frac{24}{25}$", [r"$\frac{25}{26}$", r"$\frac{23}{24}$", r"$\frac{1}{25}$"],
    r"Each term splits: $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$. The sum telescopes to $1 - \frac{1}{25} = \frac{24}{25}$.",
    r"For $\frac{1}{1\cdot2} + \cdots + \frac{1}{n(n+1)}$ the answer is $\frac{n}{n+1}$ with $n = 24$ (the smaller factor of the last term), not 25.",
    "medium", "simplification", "telescoping fraction series", 40))

# 2. number-system - remainder by cyclicity (hard)
assert pow(3, 2026, 7) == 4 and pow(3, 6, 7) == 1 and 2026 % 6 == 4
m3.append(Q(
    r"What is the remainder when $3^{2026}$ is divided by 7?",
    "4", ["2", "1", "5"],
    r"Powers of 3 mod 7: $3, 2, 6, 4, 5, 1$ — the cycle length is 6 ($3^6 \equiv 1$). $2026 = 6 \times 337 + 4$, so $3^{2026} \equiv 3^4 = 81 \equiv 4 \pmod 7$.",
    r"Fermat: $3^6 \equiv 1 \pmod 7$. Reduce the exponent mod 6: $2026 \to 4$, and $81 = 77 + 4$. Using cycle 4 (the unit-digit cycle) wrongly gives $3^2 = 9 \to 2$.",
    "hard", "number-system", "remainder of large power", 60))

# 3. percentage - population male/female (medium)
male_frac = F(60, 100) * F(55, 100) + F(40, 100) * F(75, 100)
Ppop = F(12600) / male_frac
assert male_frac == F(63, 100) and Ppop == 20000
assert F(12600) / (F(60, 100) * F(55, 100) + F(40, 100) * F(75, 100)) == 20000
assert F(12600, 1) / F(60, 100) == 21000 and F(12600) / F(45, 100) == 28000
m3.append(Q(
    "In a town, 60% of the population are adults and the rest are children. 45% of the adults and 25% of the children are females. If the total number of males in the town is 12,600, what is the population of the town?",
    "20,000", ["21,000", "18,000", "28,000"],
    r"Adult males $= 60\% \times 55\% = 33\%$ of the population. Male children $= 40\% \times 75\% = 30\%$. Total males $= 63\%$. So $0.63P = 12600 \Rightarrow P = 20{,}000$.",
    r"Weight each group's male share by its size: $0.6 \times 0.55 + 0.4 \times 0.75 = 0.63$; $12600 \div 0.63 = 20000$. Using only the adults' 60% gives the trap 21,000.",
    "medium", "percentage", "population sub-group percentages", 60))

# 4. mixture - third variety price (medium)
x3 = F(4 * 160 - 132 - 140, 2)
assert x3 == 184 and (132 + 140 + 2 * x3) / 4 == 160
assert 3 * 160 - 132 - 140 == 208
m3.append(Q(
    "Two varieties of tea costing ₹132 per kg and ₹140 per kg are mixed with a third variety in the ratio 1 : 1 : 2. If the mixture is worth ₹160 per kg, what is the price of the third variety per kg?",
    "₹184", ["₹208", "₹176", "₹194"],
    r"Let the third variety cost $₹x$. Then $\frac{132 \times 1 + 140 \times 1 + x \times 2}{4} = 160 \Rightarrow 272 + 2x = 640 \Rightarrow x = 184$.",
    r"The first two average to 136 (weight 2) and the third has weight 2, so the mixture price 160 is the midpoint: $x = 2 \times 160 - 136 = 184$. Ignoring the weight 2 gives the trap 208.",
    "medium", "mixture-alligation", "three-variety weighted mixture", 50))

# 5. ratio - 4A = 5B = 7C (medium)
ra = [F(1, 4), F(1, 5), F(1, 7)]
l = 140
parts = [int(z * l) for z in ra]
assert parts == [35, 28, 20] and sum(parts) == 83
per = F(6640, 83)
assert per == 80 and parts[2] * per == 1600 and parts[0] * per == 2800 and parts[1] * per == 2240
assert F(7, 16) * 6640 == 2905
m3.append(Q(
    "A sum of ₹6,640 is divided among A, B and C such that 4 times A's share, 5 times B's share and 7 times C's share are all equal. What is C's share?",
    rupee(1600), [rupee(2905), rupee(2800), rupee(2240)],
    r"$4A = 5B = 7C = k \Rightarrow A : B : C = \frac{1}{4} : \frac{1}{5} : \frac{1}{7} = 35 : 28 : 20$ (multiply by LCM 140). Total 83 parts $= 6640 \Rightarrow$ 1 part $= 80$. C $= 20 \times 80 = ₹1{,}600$.",
    r"Equal products means shares in the INVERSE ratio. Taking $4 : 5 : 7$ directly gives C $= \frac{7}{16} \times 6640 = 2905$ — the trap.",
    "medium", "ratio-proportion", "inverse ratio division", 50))

# 6. average - batsman innings count (medium)
ninn = sp.symbols("ninn")
nn = sp.solve(42 * ninn + 90 - 46 * (ninn + 1), ninn)[0]
assert nn == 11 and F(90 - 42, 4) == 12
m3.append(Q(
    "A batsman has an average of 42 runs per innings. In his next innings he scores 90 runs, which raises his average by 4 runs. How many innings had he played before this innings?",
    "11", ["12", "10", "13"],
    r"Let him have played $n$ innings. $42n + 90 = 46(n + 1) \Rightarrow 42n + 90 = 46n + 46 \Rightarrow 4n = 44 \Rightarrow n = 11$.",
    r"The new score covers the old average, pays the +4 rise to all $n + 1$ innings: $90 = 42 + 4(n + 1) \Rightarrow n + 1 = 12 \Rightarrow n = 11$. $\frac{90 - 42}{4} = 12$ counts the new innings too.",
    "medium", "average", "new innings raises average", 45))

# 7. interest - equal instalments (medium)
inst = 2420
Psum = F(inst) / F(11, 10) + F(inst) / F(11, 10) ** 2
assert Psum == 4200
# loan check: 4200 -> 4620 - 2420 = 2200 -> 2420 - 2420 = 0
bal = F(4200) * F(11, 10) - inst
bal = bal * F(11, 10) - inst
assert bal == 0
assert F(2 * inst) / F(11, 10) == 4400
m3.append(Q(
    "A loan is to be repaid in two equal annual instalments of ₹2,420 each at 10% per annum compound interest, compounded annually. What is the amount of the loan?",
    rupee(4200), [rupee(4840), rupee(4400), rupee(4000)],
    r"Loan $=$ present value of the instalments $= \frac{2420}{1.1} + \frac{2420}{1.1^2} = 2200 + 2000 = ₹4{,}200$. Check: $4200 \to 4620$; pay 2420 leaves 2200 $\to 2420$; pay 2420 leaves 0.",
    r"Discount each instalment back to today: $\frac{2420}{1.1} = 2200$, $\frac{2420}{1.21} = 2000$. Adding the instalments (4840) or discounting both by one year only (4400) are the traps.",
    "medium", "interest", "CI equal instalments", 55))

# 8. profit - mixed purchase (easy)
cp = 40 * 32 + 60 * 37
spv = 100 * 42
assert cp == 3500 and F(spv - cp, cp) * 100 == 20
wrong_avg = (F(42) / F(32 + 37, 2) - 1) * 100
assert wrong_avg == F(500, 23)  # 21 17/23 %
m3.append(Q(
    "A grocer buys 40 kg of rice at ₹32 per kg and 60 kg at ₹37 per kg. He mixes them and sells the whole mixture at ₹42 per kg. What is his profit per cent?",
    "20%", [r"$16\frac{2}{3}\%$", r"$21\frac{17}{23}\%$", "25%"],
    r"CP $= 40 \times 32 + 60 \times 37 = 1280 + 2220 = ₹3500$. SP $= 100 \times 42 = ₹4200$. Profit $= 700$, i.e. $\frac{700}{3500} \times 100 = 20\%$.",
    r"Weighted CP per kg $= 35$ (not the simple average 34.5, which gives $21\frac{17}{23}\%$); $\frac{42 - 35}{35} = \frac{1}{5} = 20\%$.",
    "easy", "profit-loss-discount", "mixed purchase profit", 40))

# 9. discount - SP of 16 = CP of 20 (hard)
sp_cp = F(20, 16)
mp_cp = sp_cp / F(80, 100)
assert (mp_cp - 1) * 100 == F(225, 4)
m3.append(Q(
    "A shopkeeper allows a discount of 20% on the marked price of an article. The selling price of 16 such articles equals the cost price of 20 articles. By what per cent is the marked price above the cost price?",
    "56.25%", ["45%", "25%", "50%"],
    r"$16 \times \text{SP} = 20 \times \text{CP} \Rightarrow \text{SP} = 1.25\,\text{CP}$. Also $\text{SP} = 0.8\,\text{MP}$, so $\text{MP} = \frac{1.25}{0.8}\,\text{CP} = 1.5625\,\text{CP}$. MP is $56.25\%$ above CP.",
    r"$\frac{\text{MP}}{\text{CP}} = \frac{20}{16} \times \frac{100}{80} = \frac{5}{4} \times \frac{5}{4} = \frac{25}{16}$. Adding the 25% profit and 20% discount (45%) is the trap.",
    "hard", "profit-loss-discount", "article-count equation with discount", 60))

# 10. time-work - A leaves before completion (medium)
W = 120  # LCM of 30, 40
ra_, rb_ = W // 30, W // 40
total_days = 28
a_days = F(W - rb_ * total_days, ra_)
assert a_days == 9 and total_days - a_days == 19
m3.append(Q(
    "A and B can complete a piece of work in 30 days and 40 days respectively. They start working together, but A leaves some days before the work is completed. If the whole work is finished in 28 days, how many days before completion did A leave?",
    "19 days", ["9 days", "17 days", "21 days"],
    r"Let the work $= 120$ units (LCM of 30, 40): A does 4 units/day, B 3 units/day. B works all 28 days: $28 \times 3 = 84$ units. A did the remaining $36$ units in $\frac{36}{4} = 9$ days. So A left $28 - 9 = 19$ days before completion.",
    r"Fill the full span with the worker who stayed (B: 84 of 120), the gap (36) is the leaver's share. 9 is how long A worked — the question asks for $28 - 9$.",
    "medium", "time-work", "one leaves before completion", 55))

# 11. TSD - boat upstream extra time (medium)
b = sp.symbols("b", positive=True)
bs = sp.solve(sp.Eq(36 / (b - 3) - 36 / (b + 3), 3), b)
assert bs == [9]
m3.append(Q(
    "A boat takes 3 hours more to cover 36 km upstream than to cover the same distance downstream. If the speed of the stream is 3 km/h, what is the speed of the boat in still water?",
    "9 km/h", ["12 km/h", "6 km/h", "15 km/h"],
    r"$\frac{36}{b - 3} - \frac{36}{b + 3} = 3 \Rightarrow 36 \times 6 = 3(b^2 - 9) \Rightarrow b^2 = 81 \Rightarrow b = 9$ km/h. Check: upstream 6 km/h takes 6 h, downstream 12 km/h takes 3 h — difference 3 h.",
    r"Use the options: $b = 9$ gives speeds 6 and 12, times $6$ h and $3$ h, gap 3 h. Done in 10 seconds. 12 km/h is the downstream speed, not the boat's.",
    "medium", "time-speed-distance", "boat time difference", 50))

# 12. algebra - scaled reciprocal (medium)
for r in sp.solve(2 * xs + 1 / (3 * xs) - 4, xs):
    assert sp.simplify(9 * r**2 + 1 / (4 * r**2) - 33) == 0
m3.append(Q(
    r"If $2x + \frac{1}{3x} = 4$, what is the value of $9x^2 + \frac{1}{4x^2}$?",
    "33", ["36", "39", "30"],
    r"Multiply the given equation by $\frac{3}{2}$: $3x + \frac{1}{2x} = 6$. Squaring, $9x^2 + \frac{1}{4x^2} + 2 \cdot 3x \cdot \frac{1}{2x} = 36 \Rightarrow 9x^2 + \frac{1}{4x^2} = 36 - 3 = 33$.",
    r"Scale first so the square matches: the cross term of $\left(3x + \frac{1}{2x}\right)^2$ is $2 \times 3x \times \frac{1}{2x} = 3$. Forgetting to remove it gives 36; adding it instead gives 39.",
    "medium", "algebra", "scaled x+1/x square", 50))

# 13. algebra - fourth power back to cube (hard)
checked = 0
for r in sp.solve(xs**4 + 1 / xs**4 - 119, xs):
    rv = complex(sp.N(r, 30))
    if abs(rv.imag) < 1e-12 and rv.real > 1:
        assert abs(rv.real**3 - 1 / rv.real**3 - 36) < 1e-9
        checked += 1
assert checked == 1  # exactly one real root > 1: (3 + sqrt 13)/2
assert math.isqrt(119 + 2) == 11 and 11 - 2 == 9 and 27 + 3 * 3 == 36
m3.append(Q(
    r"If $x^4 + \frac{1}{x^4} = 119$ and $x > 1$, what is the value of $x^3 - \frac{1}{x^3}$?",
    "36", ["18", r"$10\sqrt{13}$", "33"],
    r"$x^2 + \frac{1}{x^2} = \sqrt{119 + 2} = 11$. Then $\left(x - \frac{1}{x}\right)^2 = 11 - 2 = 9 \Rightarrow x - \frac{1}{x} = 3$ (positive since $x > 1$). $x^3 - \frac{1}{x^3} = 3^3 + 3 \times 3 = 36$.",
    r"Climb down the ladder: $119 \to 11 \to 3$, then $k^3 + 3k$ for the minus version. Using $k^3 - 3k$ (18) mixes up the plus and minus ladders; $10\sqrt{13}$ is $x^3 + \frac{1}{x^3}$.",
    "hard", "algebra", "x-1/x ladder from fourth power", 70))

# 14. geometry - tangents from external point (easy)
AOB = 180 - 64
OAB = F(180 - AOB, 2)
assert OAB == 32 and F(180 - 64, 2) == 58
m3.append(Q(
    r"$PA$ and $PB$ are tangents drawn from an external point $P$ to a circle with centre $O$. If $\angle APB = 64^\circ$, what is the measure of $\angle OAB$?",
    r"$32^\circ$", [r"$58^\circ$", r"$26^\circ$", r"$64^\circ$"],
    r"$\angle OAP = \angle OBP = 90^\circ$, so $\angle AOB = 180^\circ - 64^\circ = 116^\circ$. In isosceles $\triangle OAB$ ($OA = OB$), $\angle OAB = \frac{180^\circ - 116^\circ}{2} = 32^\circ$.",
    r"$\angle OAB = \frac{1}{2}\angle APB = 32^\circ$ always. $58^\circ$ is $\angle PAB$ — a different angle.",
    "medium", "geometry", "tangents from external point angle", 40))

# 15. geometry - DE parallel BC trapezium area (medium)
k = F(2, 5)
ABC = F(84) / (1 - k**2)
assert ABC == 100 and F(84 * 5, 3) == 140 and F(84 * 5, 4) == 105 and F(84 * 3, 2) == 126
m3.append(Q(
    r"In $\triangle ABC$, $D$ and $E$ are points on $AB$ and $AC$ respectively such that $DE \parallel BC$ and $AD : DB = 2 : 3$. If the area of the trapezium $DECB$ is 84 cm², what is the area of $\triangle ABC$?",
    "100 cm²", ["140 cm²", "105 cm²", "126 cm²"],
    r"$\triangle ADE \sim \triangle ABC$ with $\frac{AD}{AB} = \frac{2}{5}$. Area ratio $= \frac{4}{25}$, so the trapezium is $\frac{21}{25}$ of $\triangle ABC$. $\frac{21}{25} \times \text{ar}(ABC) = 84 \Rightarrow \text{ar}(ABC) = 100$ cm².",
    r"Areas go as squares: $2^2 : 5^2 = 4 : 25$, trapezium $= 21$ parts $= 84 \Rightarrow$ 1 part $= 4$, whole $= 100$. Using the linear ratio $2 : 5$ gives the trap 140.",
    "medium", "geometry", "BPT similar triangle area", 50))

# 16. geometry - perpendicular medians (hard)
# coordinates: G at origin, AD along y-axis, BE along x-axis
AG, GD = F(2, 3) * 9, F(1, 3) * 9
BG, GE = F(2, 3) * 12, F(1, 3) * 12
Apt = (F(0), AG)
Bpt = (-BG, F(0))
Dpt = (F(0), -GD)
Cpt = (2 * Dpt[0] - Bpt[0], 2 * Dpt[1] - Bpt[1])
Ept = ((Apt[0] + Cpt[0]) / 2, (Apt[1] + Cpt[1]) / 2)
assert Ept == (GE, F(0))  # E lies on the BE line at distance 4 from G
area = abs(Apt[0] * (Bpt[1] - Cpt[1]) + Bpt[0] * (Cpt[1] - Apt[1]) + Cpt[0] * (Apt[1] - Bpt[1])) / 2
assert area == 72
m3.append(Q(
    r"In $\triangle ABC$, the medians $AD$ and $BE$ intersect at right angles. If $AD = 9$ cm and $BE = 12$ cm, what is the area of $\triangle ABC$?",
    "72 cm²", ["54 cm²", "24 cm²", "108 cm²"],
    r"The centroid $G$ divides each median $2 : 1$: $AG = 6$, $BG = 8$. $\triangle ABG$ is right-angled at $G$, so its area $= \frac{1}{2} \times 6 \times 8 = 24$. The three medians split $\triangle ABC$ into three equal-area triangles $GAB, GBC, GCA$, so area $= 3 \times 24 = 72$ cm².",
    r"Perpendicular medians: area $= \frac{2}{3} \times AD \times BE = \frac{2}{3} \times 9 \times 12 = 72$. Treating the medians like rhombus diagonals ($\frac12 \times 9 \times 12 = 54$) is the trap.",
    "hard", "geometry", "perpendicular medians area", 70))

# 17. heights - flagstaff on tower (hard)
hh = sp.symbols("hh", positive=True)
dist = hh  # tower top at 45 deg
hsol = sp.solve(sp.Eq(hh + 10, dist * sp.sqrt(3)), hh)[0]
assert sp.simplify(hsol - 5 * (sp.sqrt(3) + 1)) == 0
m3.append(Q(
    r"A flagstaff 10 m high stands on the top of a tower. From a point on the ground, the angle of elevation of the top of the flagstaff is $60^\circ$ and that of the top of the tower is $45^\circ$. What is the height of the tower?",
    r"$5(\sqrt{3} + 1)$ m", [r"$10(\sqrt{3} + 1)$ m", r"$5(\sqrt{3} - 1)$ m", r"$10\sqrt{3}$ m"],
    r"Let the tower be $h$ m. With $45^\circ$, the point is $h$ m from the base. With $60^\circ$: $h + 10 = h\sqrt{3} \Rightarrow h(\sqrt{3} - 1) = 10 \Rightarrow h = \frac{10}{\sqrt{3} - 1} = 5(\sqrt{3} + 1)$ m.",
    r"Rationalise: $\frac{10}{\sqrt3 - 1} \times \frac{\sqrt3 + 1}{\sqrt3 + 1} = \frac{10(\sqrt3 + 1)}{2}$. Forgetting to divide by the 2 from $(\sqrt3)^2 - 1$ gives the trap $10(\sqrt3+1)$.",
    "hard", "heights-distances", "flagstaff on tower", 60))

# 18. mensuration-2d - sector perimeter to area (medium)
arc = 50 - 2 * 14
areas = F(1, 2) * arc * 14
assert arc == 22 and areas == 154
theta = F(arc, 1) / (2 * F(22, 7) * 14) * 360
assert theta == 90
m3.append(Q(
    "The perimeter of a sector of a circle of radius 14 cm is 50 cm. What is the area of the sector?",
    "154 cm²", ["308 cm²", "350 cm²", "196 cm²"],
    r"Perimeter $= 2r + \text{arc} \Rightarrow \text{arc} = 50 - 28 = 22$ cm. Area of sector $= \frac{1}{2} \times \text{arc} \times r = \frac{1}{2} \times 22 \times 14 = 154$ cm².",
    r"Sector area $= \frac{1}{2} l r$ — no angle needed. Using the whole perimeter 50 as the arc gives 350; dropping the $\frac12$ gives 308.",
    "medium", "mensuration-2d", "sector area from perimeter", 45))

# 19. mensuration-3d - ice-cream cones (hard)
pi_s = sp.pi
cyl = pi_s * 9**2 * 16
cone_h = sp.Rational(1, 3) * pi_s * 3**2 * 10 + sp.Rational(2, 3) * pi_s * 3**3
nc = sp.simplify(cyl / cone_h)
assert nc == 27
assert sp.simplify(cyl / (pi_s * 3**2 * 10 + sp.Rational(2, 3) * pi_s * 27)) == 12
assert sp.simplify(cyl / (sp.Rational(1, 3) * pi_s * 9 * 10 + sp.Rational(4, 3) * pi_s * 27)) != 27
m3.append(Q(
    "A right circular cylinder of radius 9 cm and height 16 cm is full of ice-cream. The ice-cream is to be filled into cones of height 10 cm and diameter 6 cm, each having a hemispherical top. How many such cones can be filled?",
    "27", ["12", "36", "24"],
    r"Cylinder $= \pi \times 9^2 \times 16 = 1296\pi$. One cone with hemispherical top $= \frac{1}{3}\pi \times 3^2 \times 10 + \frac{2}{3}\pi \times 3^3 = 30\pi + 18\pi = 48\pi$. Number $= \frac{1296\pi}{48\pi} = 27$.",
    r"Cancel $\pi$ at once and work in 'units': $81 \times 16 = 1296$; $30 + 18 = 48$; $1296 \div 48 = 27$. Forgetting the $\frac13$ for the cone gives 12. Radius is 3, not the diameter 6.",
    "hard", "mensuration-3d", "recast into cones with hemispheres", 75))

# 20. trigonometry - complementary angles (easy)
e = sp.cos(sp.rad(37)) / sp.sin(sp.rad(53)) + sp.sec(sp.rad(28)) / sp.csc(sp.rad(62)) - 3 * sp.tan(sp.rad(15)) * sp.tan(sp.rad(75))
assert abs(sp.N(e, 30) + 1) < 1e-20
m3.append(Q(
    r"What is the value of $\dfrac{\cos 37^\circ}{\sin 53^\circ} + \dfrac{\sec 28^\circ}{\text{cosec}\, 62^\circ} - 3\tan 15^\circ \tan 75^\circ$?",
    "$-1$", ["5", "1", "2"],
    r"$\sin 53^\circ = \cos 37^\circ$, so the first term is 1. $\text{cosec}\,62^\circ = \sec 28^\circ$, so the second term is 1. $\tan 75^\circ = \cot 15^\circ$, so $\tan 15^\circ \tan 75^\circ = 1$. Value $= 1 + 1 - 3 = -1$.",
    r"Angles adding to $90^\circ$: co-function pairs cancel to 1. So it is $1 + 1 - 3(1) = -1$. A sign slip on the last term gives 5.",
    "easy", "trigonometry", "complementary angle ratios", 30))

# 21. trigonometry - sin-cos to sin+cos (hard)
s_, c_ = sp.Rational(12, 13), sp.Rational(5, 13)
assert s_**2 + c_**2 == 1 and s_ - c_ == sp.Rational(7, 13) and s_ + c_ == sp.Rational(17, 13)
assert 2 - sp.Rational(7, 13) ** 2 == sp.Rational(289, 169)
m3.append(Q(
    r"If $\sin\theta - \cos\theta = \frac{7}{13}$ and $0^\circ < \theta < 90^\circ$, what is the value of $\sin\theta + \cos\theta$?",
    r"$\frac{17}{13}$", [r"$\frac{12}{13}$", r"$\frac{7}{13}$", r"$\frac{13}{17}$"],
    r"$(\sin\theta + \cos\theta)^2 + (\sin\theta - \cos\theta)^2 = 2$. So $(\sin\theta + \cos\theta)^2 = 2 - \frac{49}{169} = \frac{289}{169}$, giving $\sin\theta + \cos\theta = \frac{17}{13}$ (positive for an acute angle).",
    r"Guess the triplet: $\frac{12}{13} - \frac{5}{13} = \frac{7}{13}$, so $\sin = \frac{12}{13}$, $\cos = \frac{5}{13}$, sum $\frac{17}{13}$. $\frac{12}{13}$ alone is only $\sin\theta$.",
    "hard", "trigonometry", "sum from difference of sin and cos", 60))

# 22. statistics - median after finding x (easy)
data = [12, 15, 17, None, 24, 28, 33]
xv = 7 * 21 - sum(z for z in data if z is not None)
data[3] = xv
assert xv == 18 and data == sorted(data)
assert sorted(data)[3] == 18 and F(17 + 24, 2) == F(41, 2)
m3.append(Q(
    r"The observations $12, 15, 17, x, 24, 28, 33$ are arranged in ascending order and their mean is 21. What is the median of the data?",
    "18", ["21", "24", "20.5"],
    r"Sum $= 7 \times 21 = 147$. Known values add to $12 + 15 + 17 + 24 + 28 + 33 = 129$, so $x = 18$. With 7 values, the median is the 4th value $= x = 18$.",
    r"Odd count: median is the middle (4th) term, which is $x$ itself — find $x$ from the total. 21 is the mean, not the median.",
    "easy", "statistics", "median with unknown term", 40))

# 23-25. DI exam centres
DI3 = {"P": (1200, 45), "Q": (1500, 36), "R": (900, 60), "S": (1600, 40), "T": (800, 55)}
table3 = ("The table shows the number of candidates who appeared in an examination from five centres and the percentage of them who qualified:\n\n"
          "| Centre | Appeared | Qualified (%) |\n|---|---|---|\n"
          + "".join("| %s | %d | %d%% |\n" % (k, a_, p_) for k, (a_, p_) in DI3.items()))
qual = {k: F(a_ * p_, 100) for k, (a_, p_) in DI3.items()}
assert all(q_.denominator == 1 for q_ in qual.values())
app_tot = sum(a_ for a_, _ in DI3.values())
q_tot = sum(qual.values())
overall = q_tot / app_tot * 100
assert app_tot == 6000 and q_tot == 2700 and overall == 45
assert F(sum(p_ for _, p_ in DI3.values()), 5) == F(236, 5)
m3.append(Q(
    table3 + "\nWhat is the overall percentage of qualified candidates from all five centres taken together?",
    "45%", ["47.2%", "44%", "42.5%"],
    r"Qualified: P $= 540$, Q $= 540$, R $= 540$, S $= 640$, T $= 440$; total $= 2700$. Appeared total $= 6000$. Overall $= \frac{2700}{6000} \times 100 = 45\%$.",
    r"Never average the percentages ($\frac{236}{5} = 47.2\%$) when the bases differ — convert to counts first. Three centres give exactly 540 each, which speeds the addition.",
    "medium", "data-interpretation", "overall percentage from weighted table", 60))

fail = {k: DI3[k][0] - qual[k] for k in DI3}
assert fail["S"] == 960 and fail["R"] == 360
pmore = (fail["S"] - fail["R"]) / fail["R"] * 100
assert pmore == F(500, 3) and F(600, 960) * 100 == F(125, 2) and F(960, 360) * 100 == F(800, 3)
m3.append(Q(
    table3 + "\nThe number of candidates who did not qualify from centre S is what per cent more than the number who did not qualify from centre R?",
    r"$166\frac{2}{3}\%$", ["62.5%", r"$266\frac{2}{3}\%$", "150%"],
    r"Not qualified at S $= 1600 \times 60\% = 960$. Not qualified at R $= 900 \times 40\% = 360$. Required $= \frac{960 - 360}{360} \times 100 = \frac{600}{360} \times 100 = 166\frac{2}{3}\%$.",
    r"$\frac{960}{360} = \frac{8}{3} = 266\frac23\%$ is 'what per cent OF'; 'per cent MORE' subtracts 100: $166\frac23\%$. Dividing by 960 gives 62.5%.",
    "hard", "data-interpretation", "table percent more of failures", 70))

rq, rt = qual["Q"], qual["T"]
g = math.gcd(int(rq), int(rt))
assert (int(rq) // g, int(rt) // g) == (27, 22)
m3.append(Q(
    table3 + "\nWhat is the ratio of the number of qualified candidates from centre Q to that from centre T?",
    "27 : 22", ["15 : 8", "36 : 55", "22 : 27"],
    r"Qualified at Q $= 1500 \times 36\% = 540$. Qualified at T $= 800 \times 55\% = 440$. Ratio $= 540 : 440 = 27 : 22$.",
    r"Multiply appeared by per cent for each first; comparing only the appeared (15 : 8) or only the percentages (36 : 55) ignores half the data.",
    "easy", "data-interpretation", "table ratio of computed values", 40))


# =============================================================================
#  Finalise: placement, checks, duplicate scan, write
# =============================================================================
CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def norm(t):
    t = re.sub(r"[*_`]", "", t).lower()
    return re.sub(r"\s+", " ", t).strip()


def existing_questions(exclude):
    out = []
    for p in glob.glob(os.path.join(ROOT, "topics", "quant", "*.json")):
        d = json.load(open(p, encoding="utf-8"))
        for x in d.get("solvedExamples", []) + d.get("practice", []):
            out.append((os.path.basename(p), x))
    for p in glob.glob(os.path.join(PARTS, "*--quant.json")):
        if os.path.basename(p) in exclude:
            continue
        d = json.load(open(p, encoding="utf-8"))
        for x in d["questions"]:
            out.append((os.path.basename(p), x))
    return out


def numsig(t):
    return tuple(sorted(re.findall(r"\d+(?:\.\d+)?", t)))


EXPECT_DIST = {
    "t1-mock-2": {"simplification": 2, "percentage": 2, "ratio-proportion": 1, "average": 1, "interest": 1,
                  "profit-loss-discount": 2, "time-work": 1, "time-speed-distance": 1, "algebra": 2,
                  "geometry": 3, "heights-distances": 1, "mensuration-2d": 1, "mensuration-3d": 1,
                  "trigonometry": 2, "statistics": 1, "data-interpretation": 3},
    "t1-mock-3": {"simplification": 1, "number-system": 1, "percentage": 1, "mixture-alligation": 1,
                  "ratio-proportion": 1, "average": 1, "interest": 1, "profit-loss-discount": 2,
                  "time-work": 1, "time-speed-distance": 1, "algebra": 2, "geometry": 3,
                  "heights-distances": 1, "mensuration-2d": 1, "mensuration-3d": 1, "trigonometry": 2,
                  "statistics": 1, "data-interpretation": 3},
}
EXPECT_DIFF = {"t1-mock-2": {"easy": 7, "medium": 13, "hard": 5},
               "t1-mock-3": {"easy": 4, "medium": 13, "hard": 8}}


def finalize(mock_id, qs, seed, extra_letter):
    assert len(qs) == 25, (mock_id, len(qs))
    targets = [0] * 6 + [1] * 6 + [2] * 6 + [3] * 6 + [extra_letter]
    rnd = random.Random(seed)
    rnd.shuffle(targets)
    for i, (x, t) in enumerate(zip(qs, targets), start=1):
        correct = x["options"][0]
        wrongs = x["options"][1:]
        opts = wrongs[:t] + [correct] + wrongs[t:]
        x["options"] = opts
        x["answer"] = t
        assert x["options"][x["answer"]] == correct
        x_id = "q-%s-quant-%d" % (mock_id, i)
        # rebuild with id first for readable JSON
        qs[i - 1] = {"id": x_id, **x}
    for x in qs:
        for key in ("q", "solution", "shortcut", "pattern", *[]):
            assert not CTRL.search(x[key] or ""), (x["id"], key)
        for o in x["options"]:
            assert not CTRL.search(o), (x["id"], o)
    dist = Counter(x["subtopic"] for x in qs)
    assert dict(dist) == EXPECT_DIST[mock_id], dict(dist)
    diff = Counter(x["difficulty"] for x in qs)
    assert dict(diff) == EXPECT_DIFF[mock_id], dict(diff)
    return qs


m2 = finalize("t1-mock-2", m2, 20260924, 0)
m3 = finalize("t1-mock-3", m3, 20260925, 3)

OUTS = {"t1-mock-2--quant.json", "t1-mock-3--quant.json"}
ex = existing_questions(OUTS)
ex_norm = {norm(x["q"]): src for src, x in ex}
ex_sig = {}
for src, x in ex:
    ex_sig.setdefault(numsig(x["q"]), []).append(src)

seen = {}
warn = 0
for mock_id, qs in (("t1-mock-2", m2), ("t1-mock-3", m3)):
    for x in qs:
        n_ = norm(x["q"])
        assert n_ not in ex_norm, "DUPLICATE of %s: %s" % (ex_norm[n_], x["id"])
        assert n_ not in seen, "DUPLICATE between new files: %s / %s" % (seen[n_], x["id"])
        seen[n_] = x["id"]
        key = numsig(x["q"])
        if len(key) >= 2 and key in ex_sig:
            warn += 1
            print("WARN same numbers as existing:", x["id"], ex_sig[key])

for mock_id, qs in (("t1-mock-2", m2), ("t1-mock-3", m3)):
    doc = {"mockId": mock_id, "sectionId": "quant", "questions": qs}
    out = os.path.join(PARTS, "%s--quant.json" % mock_id)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    back = json.load(open(out, encoding="utf-8"))
    assert len(back["questions"]) == 25
    letters = Counter("ABCD"[x["answer"]] for x in qs)
    print("WROTE", out)
    print("  letters:", dict(sorted(letters.items())), " seq:", "".join("ABCD"[x["answer"]] for x in qs))
    print("  difficulty:", dict(Counter(x["difficulty"] for x in qs)))
    print("  topics:", dict(Counter(x["subtopic"] for x in qs)))
print("number-signature warnings:", warn)
print("ALL CHECKS PASSED")
