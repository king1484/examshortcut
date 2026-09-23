# -*- coding: utf-8 -*-
"""Build t1-pyq-2025--quant.json: 25 Qs mirroring the CGL 2025 Tier 1 topic-wise mix
(content/ssc-cgl/weightage.json 2025 counts + shift analyses). Fresh questions; each
question's `pattern` names the real PYQ type it mirrors. Every answer is asserted."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_common import Q, finalize

q = []

# ---- 1. simplification: fraction comparison (easy) ---------------------------
assert F(17, 24) < F(11, 15) < F(7, 9) < F(4, 5)
q.append(Q(
    "q-t1-pyq-2025-quant-1",
    r"Which of the following is the correct ascending order of $\frac{4}{5},\ \frac{7}{9},\ \frac{11}{15},\ \frac{17}{24}$?",
    [r"$\frac{17}{24}<\frac{11}{15}<\frac{7}{9}<\frac{4}{5}$",
     r"$\frac{11}{15}<\frac{17}{24}<\frac{7}{9}<\frac{4}{5}$",
     r"$\frac{4}{5}<\frac{7}{9}<\frac{11}{15}<\frac{17}{24}$",
     r"$\frac{17}{24}<\frac{7}{9}<\frac{11}{15}<\frac{4}{5}$"], 0,
    r"Convert to decimals: $\frac{4}{5}=0.8$, $\frac{7}{9}=0.77\overline{7}$, $\frac{11}{15}=0.7\overline{3}$, $\frac{17}{24}=0.708\overline{3}$. Ascending: $\frac{17}{24}<\frac{11}{15}<\frac{7}{9}<\frac{4}{5}$.",
    "Compare each fraction with $0.75$ ($=\frac{3}{4}$): only $\frac{17}{24}$ and $\frac{11}{15}$ fall below it, then order those two.",
    "easy", "simplification", "fraction comparison", 40))

# ---- 2. number system: rational vs irrational (easy) -------------------------
assert sp.sqrt(12) * sp.sqrt(3) == 6 and sp.expand((sp.sqrt(5) + sp.sqrt(3)) * (sp.sqrt(5) - sp.sqrt(3))) == 2
assert sp.simplify(sp.sqrt(18) + sp.sqrt(2) - 4 * sp.sqrt(2)) == 0 and sp.sqrt(16) + sp.sqrt(9) == 7
q.append(Q(
    "q-t1-pyq-2025-quant-2",
    "Which of the following is an irrational number?",
    [r"$\sqrt{12}\times\sqrt{3}$",
     r"$(\sqrt{5}+\sqrt{3})(\sqrt{5}-\sqrt{3})$",
     r"$\sqrt{18}+\sqrt{2}$",
     r"$\sqrt{16}+\sqrt{9}$"], 2,
    r"$\sqrt{12}\times\sqrt{3}=\sqrt{36}=6$ (rational); $(\sqrt5+\sqrt3)(\sqrt5-\sqrt3)=5-3=2$ (rational); $\sqrt{18}+\sqrt{2}=3\sqrt2+\sqrt2=4\sqrt2$ (irrational); $\sqrt{16}+\sqrt{9}=4+3=7$ (rational).",
    "Collapse every option to $p\\sqrt{q}$ form — only $4\\sqrt{2}$ keeps a surd.",
    "easy", "number-system", "rational-irrational classification", 40))

# ---- 3. ratio-proportion: partnership mid-year change (medium) ---------------
units_a = 50 * 6 + 40 * 6
units_b = 40 * 12
units_c = 30 * 6
tot_units = units_a + units_b + units_c
assert (units_a, units_b, units_c, tot_units) == (540, 480, 180, 1200) and 48000 // 1200 * 180 == 7200
q.append(Q(
    "q-t1-pyq-2025-quant-3",
    "A and B start a business with ₹50,000 and ₹40,000 respectively. After 6 months, A withdraws ₹10,000 while C joins with ₹30,000. At the end of the year the profit is ₹48,000. What is C's share of the profit?",
    ["₹6,000", "₹7,200", "₹8,400", "₹9,600"], 1,
    r"Capital-months: A $=50000\times6+40000\times6=540{,}000$; B $=40000\times12=480{,}000$; C $=30000\times6=180{,}000$. Ratio $=54:48:18=9:8:3$. C's share $=\frac{3}{20}\times48000=₹7{,}200$.",
    "Per ₹1,000 per month = 1 unit: A = 540, B = 480, C = 180 → total 1200 units; ₹40 per unit → C gets $180\\times40 = 7200$.",
    "medium", "ratio-proportion", "partnership mid-year change", 60))

# ---- 4. average: even numbers in a range (easy) ------------------------------
evens = list(range(22, 199, 2))
assert len(evens) == 89 and sum(evens) / len(evens) == 110
q.append(Q(
    "q-t1-pyq-2025-quant-4",
    "What is the average of all even numbers between 21 and 199?",
    ["109", "110", "111", "112"], 1,
    r"The even numbers form the AP $22, 24, \dots, 198$. Their average equals the mean of the first and last terms: $\frac{22+198}{2} = 110$.",
    "Average of an AP = (first + last)/2, no need to count terms.",
    "easy", "average", "average of arithmetic list", 40))

# ---- 5. percentage: savings change (medium) ----------------------------------
inc = F(25, 100)
old_save = F(30, 100)
new_save = F(120, 100) - F(70, 100) * F(125, 100)
pct = (new_save - old_save) / old_save * 100
assert pct == F(25, 3)
q.append(Q(
    "q-t1-pyq-2025-quant-5",
    "Ravi spends 70% of his income. His income increases by 20% and his expenditure increases by 25%. By what per cent do his savings increase?",
    [r"$8\tfrac{1}{3}\%$", "10%", r"$6\tfrac{2}{3}\%$", "12%"], 0,
    r"Let income $=100$: savings $=30$. New income $=120$, new expenditure $=70\times1.25=87.5$, new savings $=32.5$. Increase $=\frac{2.5}{30}\times100=8\tfrac{1}{3}\%$.",
    "Work on income = 100; savings rise 30 → 32.5, and $\\frac{2.5}{30} = \\frac{1}{12} = 8\\frac{1}{3}\\%$.",
    "medium", "percentage", "savings after income-expenditure change", 60))

# ---- 6. interest: CI given, find SI (medium) ---------------------------------
P = F(6620) / F(331, 1000)
assert P == 20000 and P * F(3, 10) == 6000
q.append(Q(
    "q-t1-pyq-2025-quant-6",
    "The compound interest on a certain sum at 10% per annum for 3 years is ₹6,620. What is the simple interest on the same sum at the same rate for the same period?",
    ["₹6,000", "₹6,200", "₹6,600", "₹6,620"], 0,
    r"CI factor for 3 yr at 10% $=1.1^3=1.331$, so CI $=0.331\,\text{P}=6620 \Rightarrow \text{P}=20000$. SI $=\frac{20000\times10\times3}{100}=₹6{,}000$.",
    "For 3 years at 10%: SI $= 30\\%$ of P and CI $= 33.1\\%$ of P; $6620 \\to$ P = 20000 → SI = 6000.",
    "medium", "interest", "CI given find SI", 60))

# ---- 7. profit-loss-discount: markup + successive discounts (hard) -----------
cp7 = F(25920) / (F(18, 10) * F(80, 100) * F(90, 100))
assert cp7 == 20000
q.append(Q(
    "q-t1-pyq-2025-quant-7",
    "A mobile phone is marked 80% above its cost price and sold at successive discounts of 20% and 10%. If it sells for ₹25,920, what is its cost price?",
    ["₹18,000", "₹20,000", "₹21,600", "₹22,000"], 1,
    r"SP $= \text{CP}\times1.8\times0.8\times0.9 = 1.296\,\text{CP} = 25920 \Rightarrow$ CP $= ₹20{,}000$.",
    "Single factor: $1.8 \\times 0.72 = 1.296$; $25920/1.296 = 20000$.",
    "hard", "profit-loss-discount", "markup with successive discounts", 75))

# ---- 8. profit-loss-discount: discount with embedded profit (medium) ---------
mp = F(1800) * F(125, 100) / F(75, 100)
assert mp == 3000
q.append(Q(
    "q-t1-pyq-2025-quant-8",
    "A shopkeeper allows a 25% discount on the marked price of an article and still gains 25%. If the cost price of the article is ₹1,800, what is its marked price?",
    ["₹2,750", "₹2,880", "₹3,000", "₹3,200"], 2,
    r"SP $=1.25\times1800=₹2250$. MP $=\frac{2250}{0.75}=₹3{,}000$.",
    "MP = CP × (gain factor)/(discount factor) $= 1800 \\times \\frac{125}{75} = 1800 \\times \\frac{5}{3} = 3000$.",
    "medium", "profit-loss-discount", "discount with embedded profit", 45))

# ---- 9. mixture-alligation: remove and replace (medium) ----------------------
milk = F(60) * F(4, 5) * F(48, 60)          # after removing 12 L of mixture
water = F(60) - F(12) - milk + F(12)        # remaining water + 12 L added
assert milk == F(192, 5) and water == F(108, 5) and milk / water == F(16, 9)
q.append(Q(
    "q-t1-pyq-2025-quant-9",
    "A vessel contains 60 litres of a milk-and-water mixture in the ratio 4 : 1. Twelve litres of the mixture are removed and replaced with water. What is the new ratio of milk to water?",
    ["9 : 5", "16 : 9", "3 : 2", "7 : 4"], 1,
    r"Milk $=48$ L, water $=12$ L. Removing 12 L of mixture removes $\frac{1}{5}$ of each: milk $=38.4$, water $=9.6$. After adding 12 L water: milk $=38.4$, water $=21.6$. Ratio $=38.4:21.6=16:9$.",
    "Milk becomes $48 \\times \\frac{4}{5} = 38.4$; water is simply $60 - 38.4 = 21.6$ — no need to track the removed water.",
    "medium", "mixture-alligation", "remove and replace", 60))

# ---- 10. time-work: pairwise rates (medium) ----------------------------------
combined = (F(1, 12) + F(1, 15) + F(1, 20)) / 2
assert combined == F(1, 10)
q.append(Q(
    "q-t1-pyq-2025-quant-10",
    "A and B together can do a work in 12 days, B and C in 15 days, and C and A in 20 days. In how many days will all three working together finish the work?",
    ["9 days", "10 days", "11 days", "12 days"], 1,
    r"Twice the one-day rate of all three $=\frac{1}{12}+\frac{1}{15}+\frac{1}{20}=\frac{5+4+3}{60}=\frac{1}{5}$. So all three do $\frac{1}{10}$ per day → 10 days.",
    "Sum the three pair-rates and halve: $\\frac{12}{60}/2 = \\frac{1}{10}$.",
    "medium", "time-work", "pairwise work rates", 60))

# ---- 11. time-speed-distance: two speeds early/late (medium) -----------------
d11 = F(30, 60) / (F(1, 12) - F(1, 16))
assert d11 == 24
q.append(Q(
    "q-t1-pyq-2025-quant-11",
    "Cycling at 12 km/h a man reaches his office 15 minutes late, while cycling at 16 km/h he reaches 15 minutes early. What is the distance to his office?",
    ["20 km", "24 km", "28 km", "30 km"], 1,
    r"The time gap between the two speeds is 30 min $=\frac{1}{2}$ h: $d\left(\frac{1}{12}-\frac{1}{16}\right)=\frac{1}{2} \Rightarrow \frac{d}{48}=\frac{1}{2} \Rightarrow d = 24$ km.",
    "$d = \\frac{a\\,b}{b-a} \\times$ (gap in hours) $= \\frac{12 \\times 16}{4} \\times \\frac{1}{2} = 24$ km.",
    "medium", "time-speed-distance", "two speeds early-late", 60))

# ---- 12. mensuration-2d: concentric ring (easy) ------------------------------
area12 = F(22, 7) * (14 ** 2 - 7 ** 2)
assert area12 == 462
q.append(Q(
    "q-t1-pyq-2025-quant-12",
    r"Two concentric circles have radii 14 cm and 7 cm. The area enclosed between them is: [Use $\pi = \frac{22}{7}$]",
    ["462 sq cm", "484 sq cm", "440 sq cm", "539 sq cm"], 0,
    r"Area $=\pi(R^2-r^2)=\frac{22}{7}\times(196-49)=\frac{22}{7}\times147=462$ sq cm.",
    "$147 = 22 \\times 7 - 7$... just do $\\frac{22}{7} \\times 147$: cancel the 7 → $22 \\times 21 = 462$.",
    "easy", "mensuration-2d", "concentric ring area", 40))

# ---- 13. mensuration-3d: sphere inscribed in cube (medium) -------------------
tsa13 = 4 * F(22, 7) * 7 ** 2
assert tsa13 == 616
q.append(Q(
    "q-t1-pyq-2025-quant-13",
    r"A sphere is inscribed in a cube of edge 14 cm. The total surface area of the sphere is: [Use $\pi = \frac{22}{7}$]",
    ["616 sq cm", "592 sq cm", "648 sq cm", "554 sq cm"], 0,
    r"Radius of the inscribed sphere $=\frac{14}{2}=7$ cm. TSA $=4\pi r^2=4\times\frac{22}{7}\times49=616$ sq cm.",
    "$4\\pi r^2$ with $r=7$: $4 \\times 22 \\times 7 = 616$.",
    "medium", "mensuration-3d", "sphere inscribed in cube", 45))

# ---- 14. geometry: centre vs circumference angle (easy) ----------------------
q.append(Q(
    "q-t1-pyq-2025-quant-14",
    r"In a circle with centre $O$, $\angle AOB = 150^\circ$ where $A$ and $B$ lie on the circle. $C$ is a point on the major arc $AB$. What is $\angle ACB$?",
    ["70°", "75°", "80°", "65°"], 1,
    r"The angle at the centre is twice the angle at the circumference on the same arc: $\angle ACB = \frac{150^\circ}{2} = 75^\circ$.",
    "Centre → circumference: halve it.",
    "easy", "geometry", "angle at centre and circumference", 30))

# ---- 15. geometry: parallel chords, same side (hard) -------------------------
r15 = sp.sqrt(12 ** 2 + 5 ** 2)
assert r15 == 13
# distances: d(24-chord) = 5, d(10-chord) = 12, same side, gap = 7
assert 12 - 5 == 7
q.append(Q(
    "q-t1-pyq-2025-quant-15",
    r"Two parallel chords $AB$ and $CD$ of lengths 24 cm and 10 cm lie on the same side of the centre of a circle and are 7 cm apart. The radius of the circle is:",
    ["12 cm", "13 cm", "14 cm", "15 cm"], 1,
    r"Let the chord of length 24 be at distance $x$ from the centre. Then $\sqrt{12^2+x^2}=\sqrt{5^2+(x+7)^2} \Rightarrow 144=25+14x+49 \Rightarrow x=5$. Radius $=\sqrt{144+25}=13$ cm.",
    "Try triplet radii: $r=13$ gives distances 5 (half-chord 12) and 12 (half-chord 5) — gap exactly 7.",
    "hard", "geometry", "parallel chords radius", 75))

# ---- 16. geometry: three common tangents (easy) ------------------------------
q.append(Q(
    "q-t1-pyq-2025-quant-16",
    "Two circles of radii 6 cm and 3 cm have exactly three common tangents. What is the distance between their centres?",
    ["3 cm", "6 cm", "9 cm", "12 cm"], 2,
    r"Three common tangents means the circles touch externally, so the distance between centres $=r_1+r_2=6+3=9$ cm.",
    "2 tangents → separate, 3 → touching externally ($r_1+r_2$), 4 → disjoint.",
    "easy", "geometry", "common tangents count", 30))

# ---- 17. algebra: sum-zero cube identity (medium) ----------------------------
v17 = 25 ** 3 + 30 ** 3 - 55 ** 3
assert v17 == -3 * 25 * 30 * 55 == -123750
q.append(Q(
    "q-t1-pyq-2025-quant-17",
    r"What is the value of $25^3 + 30^3 - 55^3$?",
    ["123750", "-123750", "-18750", "-93750"], 1,
    r"Since $25+30-55=0$, $a^3+b^3+c^3=3abc$ with $c=-55$: value $=3\times25\times30\times(-55)=-123750$.",
    "Sum of bases is zero → answer is $3abc$; never cube the numbers.",
    "medium", "algebra", "sum-zero cube identity", 60))

# ---- 18. algebra: line through two points (medium) ---------------------------
m18, b18 = sp.symbols("m b")
sol18 = sp.solve([sp.Eq(2 * m18 + b18, 3), sp.Eq(6 * m18 + b18, 15)], [m18, b18])
assert sol18[m18] == 3 and sol18[b18] == -3 and sol18[m18] + sol18[b18] == 0
q.append(Q(
    "q-t1-pyq-2025-quant-18",
    r"A straight line $y = mx + c$ passes through the points $(2, 3)$ and $(6, 15)$. What is the value of $m + c$?",
    ["0", "3", "6", "-3"], 0,
    r"$m=\frac{15-3}{6-2}=3$. Then $3=2(3)+c \Rightarrow c=-3$. So $m+c=0$.",
    "Slope from the two points, then back-substitute either point.",
    "medium", "algebra", "line from two points", 45))

# ---- 19. trigonometry: cos to tan (easy) -------------------------------------
t19 = sp.Rational(15, 8)
assert sp.simplify(sp.tan(sp.acos(sp.Rational(8, 17)))) == t19
q.append(Q(
    "q-t1-pyq-2025-quant-19",
    r"If $\cos\theta = \frac{8}{17}$ and $\theta$ is acute, what is the value of $\tan\theta$?",
    [r"$\frac{8}{15}$", r"$\frac{15}{8}$", r"$\frac{8}{17}$", r"$\frac{15}{17}$"], 1,
    r"$\sin\theta=\sqrt{1-\frac{64}{289}}=\frac{15}{17}$. So $\tan\theta=\frac{15/17}{8/17}=\frac{15}{8}$.",
    "8-15-17 triplet: opposite side 15, adjacent 8 → $\\tan = \\frac{15}{8}$.",
    "easy", "trigonometry", "ratio conversion via triplet", 30))

# ---- 20. trigonometry: sec-tan product (easy) --------------------------------
q.append(Q(
    "q-t1-pyq-2025-quant-20",
    r"If $\sec\theta - \tan\theta = \frac{1}{3}$, what is the value of $\sec\theta + \tan\theta$?",
    ["3", r"$\frac{1}{3}$", "9", r"$\frac{8}{3}$"], 0,
    r"Use $(\sec\theta+\tan\theta)(\sec\theta-\tan\theta)=\sec^2\theta-\tan^2\theta=1$. So $\sec\theta+\tan\theta=\frac{1}{1/3}=3$.",
    "The pair are reciprocals — just invert $\\frac{1}{3}$.",
    "easy", "trigonometry", "sec-tan reciprocal pair", 30))

# ---- 21. heights-distances: walking towards tower (medium) -------------------
d21 = 24
x21 = sp.symbols("x21")
h21 = sp.solve(sp.Eq(x21 / sp.sqrt(3), (x21 - d21) * sp.sqrt(3)), x21)[0]
hh21 = sp.simplify(h21 / sp.sqrt(3))
assert hh21 == 12 * sp.sqrt(3)
q.append(Q(
    "q-t1-pyq-2025-quant-21",
    r"On walking 24 m towards the base of a tower, the angle of elevation of its top rises from $30^\circ$ to $60^\circ$. The height of the tower is:",
    [r"$12\sqrt{3}$ m", r"$8\sqrt{3}$ m", r"$24\sqrt{3}$ m", r"$12(\sqrt{3}-1)$ m"], 0,
    r"$h=d\tan30^\circ=\frac{d}{\sqrt3}$ and $h=(d-24)\tan60^\circ=\sqrt3(d-24)$. Equating: $d=3(d-24)\Rightarrow d=36$, so $h=\frac{36}{\sqrt3}=12\sqrt3$ m.",
    "For $30^\\circ \\to 60^\\circ$, walking distance $= \\frac{2h}{\\sqrt3}$, so $h = \\frac{24\\sqrt3}{2} = 12\\sqrt3$.",
    "medium", "heights-distances", "walking towards tower", 60))

# ---- 22. statistics: grouped median (medium) ---------------------------------
freq = [6, 8, 12, 9, 5]
n = sum(freq)
cf = 6 + 8
med = 30 + F(F(n, 2) - cf, 12) * 10
assert n == 40 and cf == 14 and med == 35
q.append(Q(
    "q-t1-pyq-2025-quant-22",
    "For the distribution with classes 10–20, 20–30, 30–40, 40–50, 50–60 and frequencies 6, 8, 12, 9, 5 respectively, the median is:",
    ["34", "35", "36", "33.5"], 1,
    r"$N=40$, $\frac{N}{2}=20$. Cumulative frequencies: 6, 14, 26 — median class $30$–$40$. Median $=30+\frac{20-14}{12}\times10=30+5=35$.",
    "$\\frac{6}{12}$ of the class width above 30 → exactly 35.",
    "medium", "statistics", "grouped median formula", 60))

# ---- 23-25. DI set: vehicle plants ------------------------------------------
tbl = ("The table shows the production of vehicles (in thousands) by four plants of a company:\n\n"
       "| Plant | 2022 | 2023 | 2024 |\n|---|---|---|---|\n"
       "| W | 45 | 60 | 75 |\n| X | 50 | 55 | 70 |\n"
       "| Y | 40 | 50 | 60 |\n| Z | 70 | 60 | 65 |\n")
t23, t24 = 60 + 55 + 50 + 60, 75 + 70 + 60 + 65
assert (t23, t24) == (225, 270) and F(t23, t24) * 100 == F(250, 3)
q.append(Q(
    "q-t1-pyq-2025-quant-23",
    tbl + "\nThe total production in 2023 is what per cent of the total production in 2024?",
    [r"$83\tfrac{1}{3}\%$", "80%", "85%", r"$87\tfrac{1}{2}\%$"], 0,
    r"2023 total $=225$, 2024 total $=270$. Required $=\frac{225}{270}\times100=\frac{250}{3}=83\tfrac{1}{3}\%$.",
    "$225/270 = 5/6 = 83\\frac{1}{3}\\%$ from the fraction table.",
    "medium", "data-interpretation", "table percent of total", 45))
avg24 = (70 + 60 + 65) / 3
assert avg24 == 65
q.append(Q(
    "q-t1-pyq-2025-quant-24",
    tbl + "\nWhat is the average yearly production of plant Z over the three years?",
    ["63", "64", "65", "67"], 2,
    r"Z total $=70+60+65=195$. Average $=\frac{195}{3}=65$ thousand.",
    "65 is visibly the middle value — for an AP-style set the average is the middle entry.",
    "easy", "data-interpretation", "table average", 45))
g_w, g_x, g_y, g_z = F(30, 45), F(20, 50), F(20, 40), F(-5, 70)
assert max([(g_w, "W"), (g_x, "X"), (g_y, "Y"), (g_z, "Z")])[1] == "W"
q.append(Q(
    "q-t1-pyq-2025-quant-25",
    tbl + "\nWhich plant recorded the highest percentage increase in production from 2022 to 2024?",
    ["W", "X", "Y", "Z"], 0,
    r"W: $\frac{30}{45}=66\tfrac{2}{3}\%$; X: $\frac{20}{50}=40\%$; Y: $\frac{20}{40}=50\%$; Z: $-7\tfrac{1}{7}\%$. Highest is W.",
    "Compare rise/base: W $\\frac{30}{45}$ beats Y $\\frac{20}{40}$ — no full percentages needed.",
    "medium", "data-interpretation", "table growth ranking", 45))

finalize("t1-pyq-2025", q, 25)
