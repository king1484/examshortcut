# -*- coding: utf-8 -*-
"""Build t1-mock-1--quant.json (25 Qs, typical Tier 1 mix per content/ssc-cgl/weightage.json).
Every numeric answer is re-derived and asserted before the file is written."""
import os
import sys
from decimal import Decimal as D
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_common import Q, finalize

q = []

# ---- 1. simplification (easy) ------------------------------------------------
c = D("12.6") / D("0.3") * D("0.5")
assert c == D("21")
q.append(Q(
    "q-t1-mock-1-quant-1",
    r"Simplify: $12.6 \div 0.3 \times 0.5$",
    ["21", "84", "8.4", "42"], 0,
    r"$\div$ and $\times$ have equal precedence, so work left to right: $12.6 \div 0.3 = 42$, then $42 \times 0.5 = 21$.",
    "Never do $0.3 \\times 0.5$ first — that gives the trap option 84. Left-to-right on equal precedence.",
    "easy", "simplification", "decimal BODMAS order", 30))

# ---- 2. simplification (easy) ------------------------------------------------
tot = 7 + 77 + 777 + 7777 + 77777
assert tot == 7 * 12345 == 86415
q.append(Q(
    "q-t1-mock-1-quant-2",
    "What is the value of $7 + 77 + 777 + 7777 + 77777$?",
    ["85415", "86415", "86450", "87415"], 1,
    r"Take 7 common: $7(1 + 11 + 111 + 1111 + 11111) = 7 \times 12345 = 86415$.",
    "Sum of repunits $1+11+111+1111+11111 = 12345$ — memorise; answer $= 7 \\times 12345 = 86415$.",
    "easy", "simplification", "repdigit series sum", 40))

# ---- 3. percentage, election (medium) ---------------------------------------
polled = 40000 * 85 // 100
valid = polled * 95 // 100
win = valid * 60 // 100
assert (polled, valid, win) == (34000, 32300, 19380)
q.append(Q(
    "q-t1-mock-1-quant-3",
    "In an election between two candidates, 85% of the 40,000 registered voters cast their votes and 5% of the votes polled were declared invalid. The winning candidate received 60% of the valid votes. How many valid votes did the winning candidate receive?",
    ["18900", "19380", "19540", "20100"], 1,
    r"Polled $= 85\%$ of $40000 = 34000$. Valid $= 95\%$ of $34000 = 32300$. Winner $= 60\%$ of $32300 = 19380$.",
    "Chain the percentages on one line: $40000 \\to \\times 0.85 \\to \\times 0.95 \\to \\times 0.6 = 19380$.",
    "medium", "percentage", "election voting with invalid votes", 45))

# ---- 4. percentage comparison (easy) ----------------------------------------
assert F(1, 125) * 100 == F(4, 5) == F(80, 100)
q.append(Q(
    "q-t1-mock-1-quant-4",
    "The population of City A is 25% more than the population of City B. City B's population is what per cent of City A's population?",
    ["80%", "75%", "85%", "70%"], 0,
    r"Let B $= 100$, so A $= 125$. Required $= \frac{100}{125} \times 100 = 80\%$.",
    r"A $=\frac{5}{4}$B $\Rightarrow$ B $= \frac{4}{5}$A $= 80\%$ of A (fraction table: $\frac{1}{5} = 20\%$).",
    "easy", "percentage", "percent more-less comparison", 30))

# ---- 5. ratio-proportion, partnership (medium) -------------------------------
a, b = 36000 * 12, 48000 * 8
import math
g = math.gcd(a, b)
assert (a // g, b // g) == (9, 8) and 34000 * 9 // 17 == 18000
q.append(Q(
    "q-t1-mock-1-quant-5",
    "A starts a business with ₹36,000. After 4 months B joins with ₹48,000. At the end of the year the profit is ₹34,000. What is A's share of the profit?",
    ["₹16,000", "₹18,000", "₹19,000", "₹17,000"], 1,
    r"Profit ratio $=$ capital $\times$ months: A $= 36000 \times 12 = 432000$, B $= 48000 \times 8 = 384000$, i.e. $9 : 8$. A's share $= \frac{9}{17} \times 34000 = ₹18{,}000$.",
    "Reduce the capital-months to 9 : 8 immediately; A gets 9 parts of 17 — $34000/17 = 2000$ per part.",
    "medium", "ratio-proportion", "partnership staggered entry", 45))

# ---- 6. average, replacement (medium) ----------------------------------------
assert 65 + 8 * F(25, 10) == 85
q.append(Q(
    "q-t1-mock-1-quant-6",
    "The average weight of a group of 8 persons increases by 2.5 kg when a new person replaces one weighing 65 kg. The weight of the new person is:",
    ["80 kg", "82.5 kg", "85 kg", "87.5 kg"], 2,
    r"Total increase $= 8 \times 2.5 = 20$ kg. New person $= 65 + 20 = 85$ kg.",
    "Weight of replacement = outgoing weight $+$ (count $\\times$ rise in average) $= 65 + 20 = 85$ kg.",
    "medium", "average", "replacement changes average", 45))

# ---- 7. interest, n-times SI (medium) ----------------------------------------
# 3 times in 8 yr => SI gain 2P in 8 yr => 1P per 4 yr; 7 times needs gain 6P => 24 yr
assert F(8, 2) * 6 == 24
q.append(Q(
    "q-t1-mock-1-quant-7",
    "A sum of money becomes 3 times itself in 8 years at simple interest. In how many years will it become 7 times itself at the same rate?",
    ["21 years", "24 years", "28 years", "32 years"], 1,
    r"Becoming 3 times means SI gained $= 2P$ in 8 years, so $1P$ of interest takes 4 years. To become 7 times it must gain $6P$, i.e. $6 \times 4 = 24$ years.",
    "Only the gain counts: 2 units of interest in 8 yr → 1 unit per 4 yr → 6 units in 24 yr.",
    "medium", "interest", "n-times at simple interest", 40))

# ---- 8. profit-loss-discount, markup-discount (medium) -----------------------
sp_ = D("14400")
cp = sp_ / (D("1.6") * D("0.75"))
assert cp == D("12000")
q.append(Q(
    "q-t1-mock-1-quant-8",
    "A trader marks his article 60% above its cost price and allows a discount of 25%. If the article is sold for ₹14,400, what is its cost price?",
    ["₹11,500", "₹12,000", "₹12,500", "₹13,200"], 1,
    r"MP $= 1.6$ CP; SP $= 0.75 \times 1.6\,\text{CP} = 1.2\,\text{CP} = 14400 \Rightarrow$ CP $= ₹12{,}000$.",
    "Net factor $= 1.6 \times 0.75 = 1.2$, so SP is 120% of CP: CP $= 14400 \times \frac{100}{120} = 12000$.",
    "medium", "profit-loss-discount", "markup then discount find CP", 45))

# ---- 9. profit-loss-discount, two scenarios (hard) ---------------------------
cp9 = F(540) / F(15, 100)
assert cp9 == 3600
q.append(Q(
    "q-t1-mock-1-quant-9",
    "A man sells a watch at a loss of 10%. Had he sold it for ₹540 more, he would have gained 5%. The cost price of the watch is:",
    ["₹3,200", "₹3,600", "₹4,000", "₹3,800"], 1,
    r"The ₹540 bridges a 10% loss and a 5% gain, so it equals $15\%$ of CP. CP $= \frac{540 \times 100}{15} = ₹3{,}600$.",
    r"Difference of the two scenarios $=$ (5 $-$ ($-$10))% of CP: CP $= \frac{540}{15}\% = 3600$.",
    "medium", "profit-loss-discount", "two-scenario SP gap", 60))

# ---- 10. time-work (medium) ---------------------------------------------------
w = 6 * (F(1, 20) + F(1, 30))  # work done together in 6 days
rest_days = (1 - w) / F(1, 30)
assert w == F(1, 2) and 6 + rest_days == 21
q.append(Q(
    "q-t1-mock-1-quant-10",
    "A can finish a piece of work in 20 days and B can finish it in 30 days. They work together for 6 days and then A leaves. In how many days will B alone finish the remaining work?",
    ["20 days", "21 days", "23 days", "24 days"], 1,
    r"One-day rates: $\frac{1}{20} + \frac{1}{30} = \frac{1}{12}$. In 6 days they do $\frac{6}{12} = \frac{1}{2}$. Remaining $\frac{1}{2}$ at $\frac{1}{30}$ per day takes 15 days, so total $= 6 + 15 = 21$ days from the start.",
    "LCM 60 units: A 3 u/day, B 2 u/day, 5 u/day; 6 days = 30 u done, 30 left for B at 2 u/day = 15 days.",
    "medium", "time-work", "one leaves mid-work", 45))

# ---- 11. time-speed-distance, platform (easy) --------------------------------
v = F(240 + 360, 30)  # m/s
assert v == 20 and v * F(18, 5) == 72
q.append(Q(
    "q-t1-mock-1-quant-11",
    "A train 240 m long crosses a platform 360 m long in 30 seconds. The speed of the train is:",
    ["64 km/h", "68 km/h", "72 km/h", "76 km/h"], 2,
    r"Distance $= 240 + 360 = 600$ m. Speed $= \frac{600}{30} = 20$ m/s $= 20 \times \frac{18}{5} = 72$ km/h.",
    "Total length ÷ time, then $\\times \frac{18}{5}$: $\frac{600}{30} \\times \frac{18}{5} = 72$ km/h.",
    "easy", "time-speed-distance", "train crosses platform", 40))

# ---- 12. algebra, x+1/x cube (easy) ------------------------------------------
x = sp.symbols("x")
sol = sp.solve(sp.Eq(x + 1 / x, 6), x)
vals = [sp.simplify(s**3 + 1 / s**3) for s in sol]
assert set(vals) == {sp.Integer(198)}
q.append(Q(
    "q-t1-mock-1-quant-12",
    r"If $x + \frac{1}{x} = 6$, what is the value of $x^3 + \frac{1}{x^3}$?",
    ["190", "198", "204", "216"], 1,
    r"$x^3 + \frac{1}{x^3} = \left(x + \frac{1}{x}\right)^3 - 3\left(x + \frac{1}{x}\right) = 216 - 18 = 198$.",
    "Cube-ladder: for $x+\frac1x = k$, the next rung is $k^3 - 3k = 216 - 18 = 198$.",
    "easy", "algebra", "x+1/x cube ladder", 40))

# ---- 13. algebra, identity (hard) --------------------------------------------
# spot-check the identity on the real triple (a,b,c) = (1,3,5): s=9, ab+bc+ca=23
assert 1 + 3 + 5 == 9 and (1 * 3 + 3 * 5 + 5 * 1) == 23
assert 1 + 27 + 125 - 3 * 1 * 3 * 5 == 108  # a^3+b^3+c^3-3abc
assert 9 * (9**2 - 3 * 23) == 108           # identity formula route
q.append(Q(
    "q-t1-mock-1-quant-13",
    r"If $a + b + c = 9$ and $ab + bc + ca = 23$, what is the value of $a^3 + b^3 + c^3 - 3abc$?",
    ["96", "102", "108", "120"], 2,
    r"$a^3+b^3+c^3-3abc = (a+b+c)\left[(a+b+c)^2 - 3(ab+bc+ca)\right] = 9 \times (81 - 69) = 9 \times 12 = 108$.",
    "Direct identity: $(s)(s^2 - 3p)$ with $s=9, p=23$ gives $9 \\times 12 = 108$.",
    "hard", "algebra", "sum of cubes minus 3abc", 60))

# ---- 14. geometry, angle bisector (medium) ------------------------------------
bd = F(8, 8 + 12) * 15
assert bd == 6
q.append(Q(
    "q-t1-mock-1-quant-14",
    r"In $\triangle ABC$, $AD$ is the bisector of $\angle A$ meeting $BC$ at $D$. If $AB = 8$ cm, $AC = 12$ cm and $BC = 15$ cm, what is the length of $BD$?",
    ["5 cm", "6 cm", "7.5 cm", "9 cm"], 1,
    r"By the angle-bisector theorem $\frac{BD}{DC} = \frac{AB}{AC} = \frac{8}{12} = \frac{2}{3}$, so $BD = \frac{2}{5} \times 15 = 6$ cm.",
    "Split $BC$ in ratio $2:3$ — 5 parts of 15 give 6 per part.",
    "medium", "geometry", "angle bisector theorem", 45))

# ---- 15. geometry, chord-radius (easy) ----------------------------------------
assert sp.Integer(8) ** 2 + 15 ** 2 == 17 ** 2
q.append(Q(
    "q-t1-mock-1-quant-15",
    "A chord of length 30 cm is at a distance of 8 cm from the centre of a circle. The radius of the circle is:",
    ["15 cm", "16 cm", "17 cm", "19 cm"], 2,
    r"Half-chord $= 15$. Radius $= \sqrt{15^2 + 8^2} = \sqrt{289} = 17$ cm.",
    "8-15-17 triplet: radius is the hypotenuse of half-chord and distance.",
    "easy", "geometry", "chord distance radius", 30))

# ---- 16. geometry, tangent-secant (hard) --------------------------------------
pb = F(15) ** 2 / 9
assert pb == 25 and pb - 9 == 16
q.append(Q(
    "q-t1-mock-1-quant-16",
    r"From an external point $P$, a tangent $PT = 15$ cm and a secant $PAB$ are drawn to a circle. If $PA = 9$ cm ($A$ nearer to $P$), what is the length of the chord $AB$?",
    ["12 cm", "16 cm", "18 cm", "20 cm"], 1,
    r"$PT^2 = PA \cdot PB \Rightarrow PB = \frac{15^2}{9} = 25$ cm. $AB = PB - PA = 25 - 9 = 16$ cm.",
    "$\\frac{225}{9} = 25$ = full secant; subtract the external part 9.",
    "hard", "geometry", "tangent-secant relation", 60))

# ---- 17. heights-distances, two-point walk (hard) -----------------------------
# elevation 30 deg at distance d, 45 deg at d-30: h = d/sqrt3 = d-30
# d/sqrt3 = d-30 -> d = 30*sqrt3/(sqrt3-1) -> h = 15(sqrt3+1)
h = 15 * (sp.sqrt(3) + 1)
assert sp.simplify(h - 30 / (sp.sqrt(3) - 1)) == 0
assert abs(float(h) - 40.98) < 0.01
q.append(Q(
    "q-t1-mock-1-quant-17",
    r"The angle of elevation of the top of a tower from a point on the ground is $30^\circ$. On walking 30 m directly towards its base, the angle of elevation becomes $45^\circ$. The height of the tower is:",
    [r"$15(\sqrt{3}+1)$ m", r"$15\sqrt{3}$ m", r"$30(\sqrt{3}-1)$ m", r"$15(\sqrt{3}-1)$ m"], 0,
    r"Let the height be $h$ and the near point be $h$ m from the base ($45^\circ$). Then the far point is at $h\sqrt{3}$, so $h\sqrt{3} - h = 30 \Rightarrow h = \frac{30}{\sqrt{3}-1} = 15(\sqrt{3}+1)$ m.",
    r"With angles $30^\circ \to 45^\circ$: extra distance $= h(\sqrt{3}-1)$, so $h = \frac{30}{\sqrt{3}-1} = 15(\sqrt{3}+1)$.",
    "hard", "heights-distances", "two-point elevation walk", 60))

# ---- 18. mensuration-2d, rhombus (medium) -------------------------------------
side = sp.sqrt(12 ** 2 + 5 ** 2)
assert side == 13 and 4 * side == 52
q.append(Q(
    "q-t1-mock-1-quant-18",
    "The diagonals of a rhombus are 24 cm and 10 cm. The perimeter of the rhombus is:",
    ["48 cm", "52 cm", "56 cm", "44 cm"], 1,
    r"Diagonals bisect at right angles, so side $= \sqrt{12^2 + 5^2} = 13$ cm. Perimeter $= 4 \times 13 = 52$ cm.",
    "5-12-13 triplet — side 13, perimeter 52.",
    "medium", "mensuration-2d", "rhombus diagonals perimeter", 45))

# ---- 18. mensuration-3d, cylinder TSA (easy) ----------------------------------
tsa = 2 * F(22, 7) * 7 * (20 + 7)
assert tsa == 1188
q.append(Q(
    "q-t1-mock-1-quant-19",
    r"The total surface area of a solid cylinder of radius 7 cm and height 20 cm is: [Use $\pi = \frac{22}{7}$]",
    ["1100 cm²", "1188 cm²", "1232 cm²", "924 cm²"], 1,
    r"TSA $= 2\pi r(h + r) = 2 \times \frac{22}{7} \times 7 \times 27 = 44 \times 27 = 1188$ cm².",
    r"$2\pi r = 44$, times $(h+r) = 27$: $44 \times 27 = 1188$.",
    "easy", "mensuration-3d", "cylinder total surface area", 40))

# ---- 19. trigonometry, from tan (easy) -----------------------------------------
t = sp.Rational(4, 3)
s_, c_ = t / sp.sqrt(1 + t**2), 1 / sp.sqrt(1 + t**2)
v19 = sp.simplify((4 * s_ - 2 * c_) / (4 * s_ + 2 * c_))
assert v19 == sp.Rational(5, 11)
q.append(Q(
    "q-t1-mock-1-quant-20",
    r"If $3\tan\theta = 4$ and $\theta$ is acute, what is the value of $\frac{4\sin\theta - 2\cos\theta}{4\sin\theta + 2\cos\theta}$?",
    [r"$\frac{5}{11}$", r"$\frac{7}{11}$", r"$\frac{3}{11}$", r"$\frac{5}{9}$"], 0,
    r"$\tan\theta = \frac{4}{3}$, so $\sin\theta = \frac{4}{5}$, $\cos\theta = \frac{3}{5}$. Numerator $= \frac{16 - 6}{5}$, denominator $= \frac{16 + 6}{5}$: value $= \frac{10}{22} = \frac{5}{11}$.",
    "Divide the whole expression by $\\cos\\theta$ and put $\\tan = \\frac{4}{3}$: $\\frac{4\\tan - 2}{4\\tan + 2} = \\frac{16-6}{16+6} = \\frac{5}{11}$.",
    "easy", "trigonometry", "evaluate using tan ratio", 40))

# ---- 20. trigonometry, sum-with-reciprocal (hard) ------------------------------
# sin + 1/sin = 5 => sin^2 + 1/sin^2 = 25 - 2 = 23 (true for every root)
s20 = sp.symbols("s20")
r20 = sp.solve(sp.Eq(s20 + 1 / s20, 5), s20)
v20 = [sp.simplify(s**2 + 1 / s**2) for s in r20]
assert set(v20) == {sp.Integer(23)}
q.append(Q(
    "q-t1-mock-1-quant-21",
    r"If $\sin\theta + \text{cosec}\,\theta = 5$, what is the value of $\sin^2\theta + \text{cosec}^2\theta$?",
    ["21", "23", "25", "27"], 1,
    r"Square both sides: $\sin^2\theta + \text{cosec}^2\theta + 2 = 25$, so the value $= 25 - 2 = 23$.",
    "Sum-with-reciprocal: square and subtract 2.",
    "hard", "trigonometry", "sum-with-reciprocal ladder", 60))

# ---- 21. statistics, median of primes (easy) -----------------------------------
pr = [2, 3, 5, 7, 11, 13]
assert (pr[2] + pr[3]) / 2 == 6
q.append(Q(
    "q-t1-mock-1-quant-22",
    "What is the median of the first six prime numbers?",
    ["5", "6", "6.5", "7"], 1,
    r"The primes are $2, 3, 5, 7, 11, 13$. Median $= \frac{5 + 7}{2} = 6$.",
    "Even count → average the 3rd and 4th values: $(5+7)/2 = 6$.",
    "easy", "statistics", "median of even data set", 30))

# ---- 22-24. DI set: smartphone stores -----------------------------------------
tbl = ("The table shows the number of smartphones sold by four stores P, Q, R and S in three months:\n\n"
       "| Store | January | February | March |\n|---|---|---|---|\n"
       "| P | 320 | 280 | 400 |\n| Q | 240 | 360 | 300 |\n"
       "| R | 400 | 320 | 240 |\n| S | 280 | 240 | 360 |\n")
assert (320 + 280 + 400) == 1000 and (280 + 240 + 360) == 880
q.append(Q(
    "q-t1-mock-1-quant-23",
    tbl + "\nWhat is the ratio of the total sales of store P to the total sales of store S over the three months?",
    ["25 : 22", "24 : 21", "26 : 23", "23 : 20"], 0,
    r"P total $= 320+280+400 = 1000$; S total $= 280+240+360 = 880$. Ratio $= 1000:880 = 25:22$.",
    "Both totals end in 0 — divide by 40 first: $25:22$.",
    "easy", "data-interpretation", "table ratio", 45))
feb_total = 280 + 360 + 320 + 240
assert feb_total == 1200 and F(360, 1200) * 100 == 30
q.append(Q(
    "q-t1-mock-1-quant-24",
    tbl + "\nThe sales of store Q in February are what per cent of the total sales of all four stores in February?",
    ["28%", "30%", "32%", "36%"], 1,
    r"February total $= 280+360+320+240 = 1200$. Required $= \frac{360}{1200} \times 100 = 30\%$.",
    "$360/1200 = 3/10 = 30\\%$ straight from the fraction table.",
    "medium", "data-interpretation", "table percent share", 45))
r_avg = (400 + 320 + 240) / 3
assert r_avg == 320
q.append(Q(
    "q-t1-mock-1-quant-25",
    tbl + "\nWhat is the average monthly sale of store R over the three months?",
    ["300", "310", "320", "330"], 2,
    r"R total $= 400+320+240 = 960$. Average $= \frac{960}{3} = 320$.",
    "Units digit trick: $960/3 = 320$; totals of 9 are divisible by 3.",
    "medium", "data-interpretation", "table average", 45))

finalize("t1-mock-1", q, 25)
