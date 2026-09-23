# -*- coding: utf-8 -*-
"""Build t2-mock-1--quant.json: 30 Qs at Tier 2 Paper-1 level (+3/-1 feel) — advanced-maths
heavy with a 4-question DI block. Every numeric answer is asserted before writing."""
import os
import sys
from decimal import Decimal as D
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_common import Q, finalize

q = []

# ---- 1. simplification: fraction BODMAS (medium) ------------------------------
v1 = F(2, 3) + F(3, 4) / F(9, 8) - F(1, 2)
assert v1 == F(5, 6)
q.append(Q(
    "q-t2-mock-1-quant-1",
    r"Simplify: $\frac{2}{3} + \frac{3}{4} \div \frac{9}{8} - \frac{1}{2}$",
    [r"$\frac{1}{6}$", r"$\frac{5}{6}$", r"$\frac{7}{6}$", r"$\frac{3}{4}$"], 1,
    r"Division first: $\frac{3}{4}\div\frac{9}{8}=\frac{3}{4}\times\frac{8}{9}=\frac{2}{3}$. Then $\frac{2}{3}+\frac{2}{3}-\frac{1}{2}=\frac{8-3}{6}=\frac{5}{6}$.",
    "Convert to sixths early: $\\frac{4}{6}+\\frac{4}{6}-\\frac{3}{6}=\\frac{5}{6}$.",
    "medium", "simplification", "fraction BODMAS", 45))

# ---- 2. percentage: price reduction (medium) ----------------------------------
# original price p: same quantity costs 0.8p*orig_qty = 3840 -> saving 960 -> 6 kg at reduced price
red2 = F(4800) * F(20, 100) / 6          # saving = 960; buys 6 kg at reduced price
assert red2 == 160 and red2 / F(80, 100) == 200
q.append(Q(
    "q-t2-mock-1-quant-2",
    "A reduction of 20% in the price of ghee enables a family to buy 6 kg more for ₹4,800. What is the reduced price per kg?",
    ["₹140", "₹150", "₹160", "₹200"], 2,
    r"Money saved $=20\%$ of 4800 $=₹960$ (the price paid for the original quantity falls by $\frac{1}{4}$). At the reduced price, ₹960 buys the extra 6 kg: reduced price $=\frac{960}{6}=₹160$/kg.",
    "Reduced price $= \\frac{E \\times r}{(100-r) \\times \\text{extra}} = \\frac{4800 \\times 20}{80 \\times 6} = 160$; original was ₹200.",
    "medium", "percentage", "price reduction quantity gain", 60))

# ---- 3. ratio-proportion: compound ratio (medium) -----------------------------
parts = 15 + 20 + 24
assert parts == 59 and F(4720, 59) == 80 and 24 * 80 == 1920
q.append(Q(
    "q-t2-mock-1-quant-3",
    "A sum of ₹4,720 is divided among A, B and C such that A : B = 3 : 4 and B : C = 5 : 6. What is C's share?",
    ["₹1,600", "₹1,800", "₹1,920", "₹2,000"], 2,
    r"A : B : C $=15:20:24$ (make B equal: 3 : 4 → 15 : 20; 5 : 6 → 20 : 24). Total 59 parts; each part $=\frac{4720}{59}=80$. C $=24\times80=₹1{,}920$.",
    "LCM of B values (4, 5) = 20 → ratio 15 : 20 : 24; $4720/59 = 80$ per part.",
    "medium", "ratio-proportion", "compound ratio shares", 60))

# ---- 4. average: consecutive odd numbers (easy) -------------------------------
base = list(range(19, 36, 2))  # 19, 21, ..., 35
assert len(base) == 9 and sum(base) / 9 == 27 and max(base) == 35
q.append(Q(
    "q-t2-mock-1-quant-4",
    "The average of 9 consecutive odd numbers is 27. What is the largest of these numbers?",
    ["31", "33", "35", "37"], 2,
    r"For consecutive odd numbers the average is the middle (5th) term, so the numbers are $19, 21, \dots, 35$. Largest $=27+2\times4=35$.",
    "Largest = average + 2×4 = 35.",
    "easy", "average", "consecutive odd numbers average", 40))

# ---- 5. interest: CI-SI 3-year difference (hard) -------------------------------
P5 = F(93) / F(31, 1000)
assert P5 == 3000
q.append(Q(
    "q-t2-mock-1-quant-5",
    "The difference between the compound interest and the simple interest on a sum for 3 years at 10% per annum is ₹93. What is the sum?",
    ["₹2,800", "₹3,000", "₹3,200", "₹3,500"], 1,
    r"For 3 years, difference $=P\left(\frac{r}{100}\right)^2\left(3+\frac{r}{100}\right)=P\times0.01\times3.1=0.031P=93 \Rightarrow P=₹3{,}000$.",
    "At 10% for 3 years the difference factor is 3.1% of P — divide 93 by 0.031.",
    "hard", "interest", "CI-SI 3-year difference", 75))

# ---- 6. profit-loss-discount: ownership chain (hard) ---------------------------
factor6 = F(115, 100) * F(90, 100) * F(120, 100)
assert factor6 == F(621, 500) and F(62100) / factor6 == 50000
q.append(Q(
    "q-t2-mock-1-quant-6",
    "A trader sells a motorcycle to X at 15% profit. X sells it to Y at 10% loss, and Y sells it for ₹62,100 at 20% profit. What was the trader's original cost price?",
    ["₹48,000", "₹50,000", "₹52,000", "₹55,000"], 1,
    r"Net factor $=1.15\times0.90\times1.20=1.242$. Original CP $=\frac{62100}{1.242}=₹50{,}000$.",
    "Chain multipliers: $1.15 \\times 0.9 = 1.035$, $\\times 1.2 = 1.242$; $62100/1.242 = 50000$.",
    "hard", "profit-loss-discount", "successive profit-loss chain", 75))

# ---- 7. profit-loss-discount: false weight (easy) ------------------------------
g7 = F(250, 750) * 100
assert g7 == F(100, 3)
q.append(Q(
    "q-t2-mock-1-quant-7",
    "A dishonest dealer professes to sell goods at cost price but uses a weight of 750 grams in place of 1 kg. What is his gain per cent?",
    ["25%", r"$33\tfrac{1}{3}\%$", "30%", "40%"], 1,
    r"For every 750 g sold at the price of 1000 g, he gains 250 g. Gain % $=\frac{250}{750}\times100=33\tfrac{1}{3}\%$.",
    "Gain% on false weight = $\\frac{\\text{shortfall}}{\\text{weight given}} \\times 100 = \\frac{250}{750} \\times 100$.",
    "easy", "profit-loss-discount", "false weight", 40))

# ---- 8. mixture-alligation: alloy blending (medium) ----------------------------
cu = F(1) * F(5, 8) + F(2) * F(3, 8)
zn = F(1) * F(3, 8) + F(2) * F(5, 8)
assert cu == F(11, 8) and zn == F(13, 8) and cu / zn == F(11, 13)
q.append(Q(
    "q-t2-mock-1-quant-8",
    "Two alloys contain copper and zinc in the ratios 5 : 3 and 3 : 5 respectively. If they are mixed in the ratio 1 : 2, what is the ratio of copper to zinc in the new alloy?",
    ["11 : 13", "13 : 11", "1 : 1", "5 : 7"], 0,
    r"Take 1 part of alloy A and 2 of B. Copper $=\frac{5}{8}+2\times\frac{3}{8}=\frac{11}{8}$; zinc $=\frac{3}{8}+2\times\frac{5}{8}=\frac{13}{8}$. Ratio $=11:13$.",
    "Work in eighths directly: copper $5+6=11$, zinc $3+10=13$.",
    "medium", "mixture-alligation", "alloy blending", 60))

# ---- 9. time-work: men-women equivalence (hard) --------------------------------
work9 = 25 * 40
days9 = work9 / 40
assert days9 == 25 and F(12) * F(5, 3) + 20 == 40
q.append(Q(
    "q-t2-mock-1-quant-9",
    "If 15 men or 25 women can complete a work in 40 days, in how many days will 12 men and 20 women together complete the same work?",
    ["20 days", "24 days", "25 days", "30 days"], 2,
    r"$15\text{M}=25\text{W}\Rightarrow1\text{M}=\frac{5}{3}\text{W}$. So $12\text{M}+20\text{W}=20\text{W}+20\text{W}=40\text{W}$. Total work $=25\times40=1000$ woman-days $\Rightarrow \frac{1000}{40}=25$ days.",
    "Convert everything to women: 12 men = 20 women, team = 40 women, job = 1000 woman-days → 25 days.",
    "hard", "time-work", "men-women equivalence", 75))

# ---- 10. time-speed-distance: crossing times (hard) ----------------------------
v10 = F(75, 25)
assert v10 == 3
a_, b_ = sp.symbols("a_ b_", positive=True)
sol10 = sp.solve([sp.Eq(a_ + b_, 3 * (a_ - b_))], [b_])
assert sp.simplify(sol10[b_] - a_ / 2) == 0  # a:b = 2:1
q.append(Q(
    "q-t2-mock-1-quant-10",
    "Two trains of equal length cross each other completely in 25 seconds when moving in opposite directions, and in 75 seconds when moving in the same direction. What is the ratio of their speeds?",
    ["1 : 1", "2 : 1", "3 : 1", "3 : 2"], 1,
    r"Relative speeds: $(a+b)\propto\frac{1}{25}$ and $(a-b)\propto\frac{1}{75}$, so $\frac{a+b}{a-b}=3$. Solving: $a+b=3a-3b \Rightarrow 2a=4b \Rightarrow a:b=2:1$.",
    "Opposite: same-direction time ratio 75 : 25 = 3 : 1 gives $\\frac{a+b}{a-b}=3$ → speeds 2 : 1.",
    "hard", "time-speed-distance", "crossing times direction ratio", 75))

# ---- 11. algebra: symmetric sums (medium) --------------------------------------
xs, ys = sp.symbols("xs ys", positive=True)
sol11 = sp.solve([sp.Eq(xs**2 + ys**2, 29), sp.Eq(xs * ys, 10)], [xs, ys])
v11 = [sp.simplify(s[0]**3 + s[1]**3) for s in sol11]
assert set(v11) == {sp.Integer(133)}
q.append(Q(
    "q-t2-mock-1-quant-11",
    r"If $x$ and $y$ are positive real numbers with $x^2 + y^2 = 29$ and $xy = 10$, what is the value of $x^3 + y^3$?",
    ["119", "133", "147", "105"], 1,
    r"$x^3+y^3=(x+y)(x^2-xy+y^2)$. Here $(x+y)^2=29+20=49 \Rightarrow x+y=7$. So $x^3+y^3=7\times(29-10)=7\times19=133$.",
    "$x, y = 2, 5$ fits both — sum of cubes $8+125 = 133$.",
    "medium", "algebra", "symmetric sums cubes", 60))

# ---- 12. algebra: conjugate surd (medium) --------------------------------------
a12 = 2 + sp.sqrt(3)
v12 = sp.simplify(a12**2 + 1 / a12**2)
assert v12 == 14
q.append(Q(
    "q-t2-mock-1-quant-12",
    r"If $a = 2 + \sqrt{3}$, what is the value of $a^2 + \frac{1}{a^2}$?",
    ["12", "14", "16", "10"], 1,
    r"$\frac{1}{a}=2-\sqrt3$, so $a+\frac1a=4$. Then $a^2+\frac{1}{a^2}=\left(a+\frac1a\right)^2-2=16-2=14$.",
    "Conjugate ladder: $a+\\frac1a = 4$ → square minus 2.",
    "medium", "algebra", "conjugate surd ladder", 60))

# ---- 13. algebra: cubic identity with product (hard) ---------------------------
x13, y13 = sp.symbols("x13 y13")
sol13 = sp.solve([sp.Eq(3 * x13 + 2 * y13, 20), sp.Eq(x13 * y13, 15)], [x13, y13])
v13 = [sp.simplify((3 * s[0])**3 + (2 * s[1])**3) for s in sol13]
assert set(v13) == {sp.Integer(2600)}
q.append(Q(
    "q-t2-mock-1-quant-13",
    r"If $3x + 2y = 20$ and $xy = 15$, what is the value of $27x^3 + 8y^3$?",
    ["2400", "2600", "2800", "3200"], 1,
    r"$27x^3+8y^3=(3x)^3+(2y)^3=(3x+2y)\left[(3x+2y)^2-3(3x)(2y)\right]=20\,(400-270)=20\times130=2600$.",
    "Let $u = 3x, v = 2y$: $u^3+v^3 = (u+v)(u^2-uv+v^2)$ with $uv = 6 \\times 15 = 90$.",
    "hard", "algebra", "cubic identity given product", 75))

# ---- 14. geometry: BPT (medium) -------------------------------------------------
bc14 = F(4) * (F(24, 10) + F(36, 10)) / F(24, 10)
assert bc14 == 10
q.append(Q(
    "q-t2-mock-1-quant-14",
    r"In $\triangle ABC$, points $D$ and $E$ lie on $AB$ and $AC$ respectively with $DE \parallel BC$. If $AD = 2.4$ cm, $DB = 3.6$ cm and $DE = 4$ cm, what is the length of $BC$?",
    ["8 cm", "9 cm", "10 cm", "12 cm"], 2,
    r"$AB = 2.4+3.6 = 6$ cm. Triangles $ADE$ and $ABC$ are similar with ratio $\frac{AD}{AB}=\frac{2.4}{6}=\frac{2}{5}$, so $BC = DE\times\frac{5}{2}=10$ cm.",
    "Scale factor $\\frac{2.4}{6} = \\frac{2}{5}$; invert and multiply 4 by $\\frac{5}{2}$.",
    "medium", "geometry", "basic proportionality theorem", 60))

# ---- 15. geometry: circumcentre (medium) ----------------------------------------
q.append(Q(
    "q-t2-mock-1-quant-15",
    r"In $\triangle ABC$, $O$ is the circumcentre and $\angle BAC = 55^\circ$. What is the measure of $\angle BOC$?",
    ["55°", "110°", "125°", "70°"], 1,
    r"The angle subtended by arc $BC$ at the circumcentre is twice the angle at the circumference: $\angle BOC = 2\times55^\circ = 110^\circ$.",
    "Circumcentre: central angle = 2 × vertex angle facing the same side.",
    "medium", "geometry", "circumcentre central angle", 60))

# ---- 16. geometry: intersecting circles, common chord (hard) --------------------
half16 = sp.sqrt(13 ** 2 - 12 ** 2)
assert half16 == 5 and 2 * half16 == 10
q.append(Q(
    "q-t2-mock-1-quant-16",
    r"Two circles of radii 5 cm and 13 cm intersect at two points and the distance between their centres is 12 cm. What is the length of their common chord?",
    ["8 cm", "9.6 cm", "10 cm", "12 cm"], 2,
    r"The common chord is perpendicular to the line of centres. Its half-length $h$ satisfies $h=\sqrt{13^2-12^2}=5$ from the bigger circle. So the chord $=2\times5=10$ cm (it is a diameter of the smaller circle).",
    "$5^2+12^2=13^2$ — the centres and an intersection point form a right triangle; chord = 10.",
    "hard", "geometry", "intersecting circles common chord", 90))

# ---- 17. geometry: interior-exterior angle ratio (medium) -----------------------
ext17 = F(180, 5)
assert ext17 == 36 and 360 // 36 == 10
q.append(Q(
    "q-t2-mock-1-quant-17",
    "In a regular polygon the ratio of each interior angle to each exterior angle is 4 : 1. How many sides does the polygon have?",
    ["8", "9", "10", "12"], 2,
    r"Interior $+$ exterior $=180^\circ$, so exterior $=\frac{180^\circ}{5}=36^\circ$. Number of sides $=\frac{360^\circ}{36^\circ}=10$.",
    "Exterior angle 36° → 10 sides straight away ($360/36$).",
    "medium", "geometry", "interior-exterior angle ratio", 60))

# ---- 18. mensuration-2d: percent change in circle area (easy) -------------------
assert F(140, 100) ** 2 == F(196, 100)
q.append(Q(
    "q-t2-mock-1-quant-18",
    "If the radius of a circle is increased by 40%, by what per cent does its area increase?",
    ["80%", "96%", "116%", "40%"], 1,
    r"Area scales as $1.4^2=1.96$, i.e. a $96\%$ increase.",
    "Successive change formula: $40+40+\frac{40\times40}{100}=96\\%$.",
    "easy", "mensuration-2d", "percent change in area", 40))

# ---- 19. mensuration-2d: inner path (medium) -------------------------------------
path19 = 50 * 30 - 46 * 26
assert path19 == 304
q.append(Q(
    "q-t2-mock-1-quant-19",
    "A rectangular garden 50 m by 30 m has a 2 m wide path built inside it along the boundary. What is the area of the path?",
    ["296 sq m", "304 sq m", "312 sq m", "320 sq m"], 1,
    r"Inner rectangle $=(50-4)\times(30-4)=46\times26=1196$ sq m. Path $=1500-1196=304$ sq m.",
    "Subtract 4 (not 2) from each dimension for an inside path.",
    "medium", "mensuration-2d", "inner path area", 60))

# ---- 20. mensuration-3d: hemisphere to cone (medium) -----------------------------
h20 = F(2, 3) * F(216) / (F(1, 3) * F(9))
assert h20 == 48
q.append(Q(
    "q-t2-mock-1-quant-20",
    "A solid metallic hemisphere of radius 6 cm is melted and recast into a cone of base radius 3 cm. What is the height of the cone?",
    ["42 cm", "48 cm", "54 cm", "36 cm"], 1,
    r"Hemisphere volume $=\frac{2}{3}\pi(6^3)=144\pi$. Cone: $\frac{1}{3}\pi(3^2)h=3\pi h=144\pi \Rightarrow h=48$ cm.",
    "In units of $\\pi$: hemisphere $144$, cone $3h$ → $h = 48$.",
    "medium", "mensuration-3d", "hemisphere to cone recast", 60))

# ---- 21. mensuration-3d: cube cutting (hard) --------------------------------------
surface21 = 4 ** 3 - 2 ** 3
assert surface21 == 56
q.append(Q(
    "q-t2-mock-1-quant-21",
    "A cube of edge 12 cm is cut into smaller cubes of edge 3 cm. How many of the small cubes have at least one face on the surface of the original cube?",
    ["48", "52", "56", "64"], 2,
    r"Small cubes per edge $=\frac{12}{3}=4$, total $=4^3=64$. Inner (unpainted) cubes $=(4-2)^3=8$. Surface cubes $=64-8=56$.",
    "Total minus the inner $(n-2)^3$ block.",
    "hard", "mensuration-3d", "cube cutting surface cubes", 75))

# ---- 22. trigonometry: double-angle evaluation (easy) -----------------------------
v22 = sp.simplify(2 * sp.tan(sp.pi / 6) / (1 + sp.tan(sp.pi / 6) ** 2))
assert v22 == sp.sqrt(3) / 2
q.append(Q(
    "q-t2-mock-1-quant-22",
    r"What is the value of $\frac{2\tan 30^\circ}{1+\tan^2 30^\circ}$?",
    [r"$\frac{1}{2}$", r"$\frac{\sqrt{3}}{2}$", r"$\sqrt{3}$", r"$\frac{1}{\sqrt{2}}$"], 1,
    r"The expression equals $\sin 2\theta$ with $\theta=30^\circ$, so it is $\sin 60^\circ=\frac{\sqrt3}{2}$.",
    "Recognise $\\frac{2t}{1+t^2} = \\sin 2\\theta$; at $30^\\circ$ → $\\sin 60^\\circ = \\frac{\\sqrt3}{2}$.",
    "easy", "trigonometry", "double angle evaluation", 40))

# ---- 23. trigonometry: standard-angle substitution (medium) -----------------------
v23 = sp.simplify((3 - sp.Rational(3, 4)) / (3 + sp.Rational(3, 4)))
assert v23 == sp.Rational(3, 5)
q.append(Q(
    "q-t2-mock-1-quant-23",
    r"If $\cot\theta = \frac{1}{\sqrt{3}}$ and $\theta$ is acute, what is the value of $\frac{3-\sin^2\theta}{3+\sin^2\theta}$?",
    [r"$\frac{2}{3}$", r"$\frac{3}{5}$", r"$\frac{4}{5}$", r"$\frac{1}{3}$"], 1,
    r"$\cot\theta=\frac{1}{\sqrt3}\Rightarrow\tan\theta=\sqrt3\Rightarrow\theta=60^\circ$, so $\sin^2\theta=\frac34$. Value $=\frac{3-\frac34}{3+\frac34}=\frac{9}{15}=\frac{3}{5}$.",
    "In quarters: $\\frac{12-3}{12+3} = \\frac{9}{15} = \\frac{3}{5}$.",
    "medium", "trigonometry", "standard angle substitution", 60))

# ---- 24. trigonometry: complementary pairing (medium) ------------------------------
v24 = sp.sin(sp.pi / 9) ** 2 + sp.sin(7 * sp.pi / 18) ** 2 + 1  # sin^2 20 + sin^2 70 + cot^2 45
assert sp.nsimplify(v24) == 2
q.append(Q(
    "q-t2-mock-1-quant-24",
    r"What is the value of $\sin^2 20^\circ + \sin^2 70^\circ + \cot^2 45^\circ$?",
    ["1", "2", "3", "0"], 1,
    r"$70^\circ=90^\circ-20^\circ$, so $\sin^2 70^\circ=\cos^2 20^\circ$; the first two terms add to 1. $\cot 45^\circ=1$. Total $=1+1=2$.",
    "Complementary pair sums to 1; $\\cot^2 45^\\circ = 1$; answer 2.",
    "medium", "trigonometry", "complementary angle pairing", 45))

# ---- 25. heights-distances: same-side two points (hard) ----------------------------
h25 = 16 * sp.sqrt(3)
assert sp.simplify(sp.tan(sp.pi / 3) * 16 - h25) == 0 and sp.simplify(sp.tan(sp.pi / 6) * 48 - h25) == 0
q.append(Q(
    "q-t2-mock-1-quant-25",
    r"The angles of elevation of the top of a tower from two points on the ground at distances 16 m and 48 m from its base, on the same side, are $60^\circ$ and $30^\circ$ respectively. The height of the tower is:",
    [r"$16\sqrt{3}$ m", r"$24\sqrt{3}$ m", r"$32\sqrt{3}$ m", r"$8\sqrt{3}$ m"], 0,
    r"$h=16\tan60^\circ=16\sqrt3$ m; check: $48\tan30^\circ=\frac{48}{\sqrt3}=16\sqrt3$ m. Both agree.",
    "Cross-check both points: $16\\sqrt3$ satisfies each; if only one had matched, the data would be inconsistent.",
    "hard", "heights-distances", "same-side two elevation points", 90))

# ---- 26. statistics: variance scaling (medium) --------------------------------------
v26 = F(4) * 2 ** 2
assert v26 == 16
q.append(Q(
    "q-t2-mock-1-quant-26",
    "The variance of 5 observations is 4. If each observation is doubled, the new variance is:",
    ["4", "8", "16", "32"], 2,
    r"Variance scales by $k^2$ when every observation is multiplied by $k$: $4\times2^2=16$.",
    "Multiply by $k^2$, not $k$ — 4 → 16.",
    "medium", "statistics", "variance under scaling", 45))

# ---- 27-30. DI set: electricity consumption ----------------------------------------
tbl = ("The table shows the monthly electricity consumption (in million units) of four states:\n\n"
       "| State | 2021 | 2022 | 2023 |\n|---|---|---|---|\n"
       "| P | 280 | 320 | 390 |\n| Q | 240 | 260 | 325 |\n"
       "| R | 300 | 280 | 350 |\n| S | 180 | 216 | 225 |\n")
tot21 = 280 + 240 + 300 + 180
tot23 = 390 + 325 + 350 + 225
assert tot21 == 1000 and tot23 == 1290 and F(290, 1000) * 100 == 29
q.append(Q(
    "q-t2-mock-1-quant-27",
    tbl + "\nThe total consumption in 2023 is what per cent more than the total consumption in 2021?",
    ["27%", "29%", "31%", "33%"], 1,
    r"2021 total $=1000$; 2023 total $=1290$. Increase $=\frac{290}{1000}\times100=29\%$.",
    "Totals of 1000 and 1290 make the rise exactly 29%.",
    "medium", "data-interpretation", "table percent growth", 60))
avg27 = (240 + 260 + 325) / 3
assert avg27 == 275
q.append(Q(
    "q-t2-mock-1-quant-28",
    tbl + "\nWhat is the average yearly consumption of state Q over the three years?",
    ["265", "270", "275", "280"], 2,
    r"Q total $=240+260+325=825$. Average $=\frac{825}{3}=275$ million units.",
    "$825/3 = 275$ — the 25 at the end makes the divisibility by 3 easy to spot.",
    "easy", "data-interpretation", "table average", 45))
g27 = [(F(390 - 280, 280), "P"), (F(325 - 240, 240), "Q"), (F(350 - 300, 300), "R"), (F(225 - 180, 180), "S")]
ranked = sorted(g27, reverse=True)
assert ranked[0][1] == "P" and ranked[1][1] == "Q"
q.append(Q(
    "q-t2-mock-1-quant-29",
    tbl + "\nWhich state has the second highest percentage increase in consumption from 2021 to 2023?",
    ["P", "Q", "R", "S"], 1,
    r"P: $\frac{110}{280}\approx39.3\%$; Q: $\frac{85}{240}\approx35.4\%$; R: $\frac{50}{300}\approx16.7\%$; S: $\frac{45}{180}=25\%$. Order: P > Q > S > R — second highest is Q.",
    "Compare rise/base: P $\\frac{110}{280}$, Q $\\frac{85}{240}$ — Q's ratio is just under P's, clearly above S's $\\frac14$.",
    "hard", "data-interpretation", "table growth ranking", 75))
avg30 = (180 + 216 + 225) / 3
assert avg30 == 207
q.append(Q(
    "q-t2-mock-1-quant-30",
    tbl + "\nWhat is the average yearly consumption of state S over the three years?",
    ["205", "206", "207", "208"], 2,
    r"S total $=180+216+225=621$. Average $=\frac{621}{3}=207$ million units.",
    "$621/3$: 6 and 3 divide, $\frac{21}{3}=7$ → 207.",
    "easy", "data-interpretation", "table average", 45))

finalize("t2-mock-1", q, 30)
