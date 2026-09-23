from _lib import *

# ------------------------------------------------------------------ checks
assert F(2, 5) * 1200 == 480 and F(3, 5) * 1200 == 720
# combine 2:3 and 4:5 -> 8:12:15
assert F(8, 3) == F(4, 3) * 2 and 8 + 15 == 23
# fourth proportional to 4, 9, 12 -> d = 9*12/4 = 27
assert 9 * 12 // 4 == 27
# third proportional to 12, 18 -> 18*18/12 = 27
assert 18 * 18 // 12 == 27
# mean proportional 25, 81 -> 45
import math
assert math.isqrt(25 * 81) == 45
# ages 3:5 sum 48 -> 18, 30
assert 48 // 8 == 6 and 3 * 6 == 18 and 5 * 6 == 30
# ratio 5:7 diff 12 -> sum 72
assert 12 // 2 == 6 and 12 * 6 == 72
# partnership: 12000*12 : 18000*8 = 1:1, profit 9600 -> 4800 each
assert 12000 * 12 == 18000 * 8 and 9600 // 2 == 4800
# coins 50p:25p:10p = 7:6:5, total Rs 550 -> k=100 -> 25p coins 600
vset = 7 * 50 + 6 * 25 + 5 * 10
assert vset == 550 and 55000 // 550 == 100 and 6 * 100 == 600
# father 3x, 8 yrs ago 5:1 -> son 16, father 48
import sympy as sp
s = sp.symbols("s")
sol = sp.solve(sp.Eq(3 * s - 8, 5 * (s - 8)), s)
assert sol == [16] and 3 * 16 == 48
# componendo: (x+y)/(x-y) = 5/3 -> x/y = 4
assert F(5 + 3, 5 - 3) == 4
# partnership 240:180:200 -> 12:9:10, profit 46500 -> C 15000
sh = [240, 180, 200]
g = math.gcd(math.gcd(240, 180), 200)
red = [x // g for x in sh]
assert red == [12, 9, 10] and sum(red) == 31 and F(10, 31) * 46500 == 15000
# ages 5:7 after 8 -> 3:4 -> x=8 -> present 40, 56, sum 96
x = sp.symbols("x")
sol = sp.solve(sp.Eq(4 * (5 * x + 8), 3 * (7 * x + 8)), x)
assert sol == [8] and 5 * 8 + 7 * 8 == 96 and F(48, 64) == F(3, 4)
# income-exp: 8x/5x vs 5y/3y, save 1200 -> x = 2400 -> income A = 19200
xx, y = sp.symbols("x y")
sol = sp.solve([sp.Eq(8 * xx - 5 * y, 1200), sp.Eq(5 * xx - 3 * y, 1200)], [xx, y])
assert sol[xx] == 2400 and 8 * 2400 == 19200
# working partner: 6000 & 4000, profit 9000, B gets 10% for management
p = 9000
rem = p - 900
a = F(6000, 10000) * rem
b = 900 + F(4000, 10000) * rem
assert a == 4860 and b == 4140 and a + b == p
# ages: 6 yrs ago 5:6, after 6 yrs 6:7 -> x=12 -> B present 78
x = sp.symbols("x")
sol = sp.solve(sp.Eq(7 * (5 * x + 12), 6 * (6 * x + 12)), x)
assert sol == [12] and 6 * 12 + 6 == 78 and F(66, 78) == F(11, 13)
# solved: 2500 in 2:3:5 -> largest 1250
assert F(5, 10) * 2500 == 1250
# solved: 3:4 and 2:3 -> 3:4:6
assert F(3, 4) == F(6, 8)
# solved: 30000x12 : 40000x6 -> 3:2, profit 28800 -> 17280 / 11520
assert 30000 * 12 == 360000 and 40000 * 6 == 240000 and F(360000, 240000) == F(3, 2)
assert F(3, 5) * 28800 == 17280 and F(2, 5) * 28800 == 11520
# solved: 4:5, after 16 -> 6:7 -> x=8, sum 72
sol = sp.solve(sp.Eq(7 * (4 * x + 16), 6 * (5 * x + 16)), x)
assert sol == [8] and 4 * 8 + 5 * 8 == 72

subtopics = [
 sub("rp-basics", "Ratio basics & dividing amounts",
  md(r"A ratio $a : b$ compares two quantities of the same kind. Multiplying/dividing both terms by the same number does not change it — $2:3 = 8:12$. Write every ratio as a fraction to compare or compute.",
     "",
     r"**Dividing an amount N in the ratio $a : b : c$:** the shares are $\frac{a}{a+b+c}N$, $\frac{b}{a+b+c}N$, $\frac{c}{a+b+c}N$.",
     "",
     "**Combining ratios:** given A : B and B : C, scale both so the B-parts match (use the LCM of the two B values).",
     "",
     "**Comparing two ratios** $a : b$ and $c : d$: compare the products $ad$ and $bc$ (cross-multiplication).",
     "",
     r"**Proportional parts language:** if a number is divided so that one share exceeds another by k, work with the multiplier: shares $= ax, bx$ with $(b-a)x = k$."),
  [formula("Share of the total", r"\text{share} = \frac{\text{ratio term}}{\text{sum of terms}} \times N"),
   formula("Combining ratios", r"A:B = m:n,\ B:C = p:q \Rightarrow A:B:C = mp : np : nq"),
   formula("Cross-multiplication test", r"a:b > c:d \iff ad > bc"),
   formula("Multiplier method", r"\text{shares } ax, bx,\ (b-a)x = \text{given difference}"),
   formula("Duplicate / sub-duplicate", r"a:b \Rightarrow a^2:b^2 \text{ (duplicate)},\ \sqrt{a}:\sqrt{b} \text{ (sub-duplicate)}")],
  [trick("Multiplier x solves everything",
         "Translate 'numbers are in ratio a : b' into ax and bx. Every extra fact (sum, difference, product) becomes a small linear equation in x.",
         "Two numbers are in the ratio 5 : 7 and their difference is 12. Find their sum.",
         "Numbers are 5x and 7x; 2x = 12 ⇒ x = 6. Sum = 12x = **72**."),
   trick("LCM bridging for three-term ratios",
         "Scale A:B so its B-term equals the B-term of B:C, then read off A:B:C.",
         "If A : B = 2 : 3 and B : C = 4 : 5, find A : B : C.",
         "Make B = 12 (LCM of 3, 4): A : B = 8 : 12 and B : C = 12 : 15 ⇒ **8 : 12 : 15**."),
   trick("One share or difference known",
         "Share = fraction × total. If one share is given, first recover the total, then any other share.",
         "₹1,200 is divided between A and B in the ratio 2 : 3. Find B's share.",
         r"B's share $= \frac{3}{5} \times 1200$ = ₹720.")],
  ["Adding ratios term-wise (A:B = 2:3, B:C = 4:5 is NOT 2:3:5).",
   r"Using the changed value as the base when a ratio changes ('ratio becomes a:b' — the total is usually redistributed).",
   "Forgetting that ratio terms must be of the same unit (₹ with ₹, kg with kg).",
   "Reducing 8 : 12 to 4 : 6 but then answering 4 : 6 where the reduced 2 : 3 is asked (read what the option set wants)."]),

 sub("rp-proportion", "Proportion & proportional division of terms",
  md(r"Four numbers $a, b, c, d$ are in proportion when $\frac{a}{b} = \frac{c}{d}$, written $a : b :: c : d$; then $ad = bc$ (product of extremes = product of means).",
     "",
     r"- **Fourth proportional** to $a, b, c$: $d = \frac{bc}{a}$.",
     r"- **Third proportional** to $a, b$ (a : b :: b : ?): $c = \frac{b^2}{a}$.",
     r"- **Mean proportional** between $a$ and $b$: $\sqrt{ab}$.",
     r"- **Continued proportion:** $a, b, c$ with $\frac{a}{b} = \frac{b}{c}$.",
     "",
     r"**Componendo and dividendo:** if $\frac{a}{b} = \frac{c}{d}$ then $\frac{a+b}{a-b} = \frac{c+d}{c-d}$ — the fastest route when x and y appear as a sum and difference."),
  [formula("Basic proportion", r"\frac{a}{b} = \frac{c}{d} \iff ad = bc"),
   formula("Fourth proportional", r"d = \frac{bc}{a}"),
   formula("Third proportional", r"c = \frac{b^2}{a}"),
   formula("Mean proportional", r"\text{mean} = \sqrt{ab}"),
   formula("Componendo & dividendo", r"\frac{a}{b} = \frac{c}{d} \Rightarrow \frac{a+b}{a-b} = \frac{c+d}{c-d}"),
   formula("Invertendo / alternando", r"\frac{b}{a} = \frac{d}{c},\quad \frac{a}{c} = \frac{b}{d}")],
  [trick("Extremes × means",
         "Set up the proportion, cross-multiply, done. For 'fourth proportional' keep the order exactly as written.",
         "Find the fourth proportional to 4, 9 and 12.",
         r"$\frac{4}{9} = \frac{12}{d}$ ⇒ $4d = 108$ ⇒ $d = 27$."),
   trick("Mean proportional = geometric mean",
         "Multiply the two numbers and take the square root. Perfect squares make it instant.",
         "Find the mean proportional between 25 and 81.",
         r"$\sqrt{25 \times 81} = 5 \times 9 = 45$."),
   trick("Componendo-dividendo for x : y",
         "When (x + y) and (x − y) both appear, write the ratio and jump straight to x/y.",
         r"If $\frac{x+y}{x-y} = \frac{5}{3}$, find $\frac{x}{y}$.",
         r"$\frac{x}{y} = \frac{5+3}{5-3} = 4$.")],
  ["Mixing up third and fourth proportional (third has a repeated middle term).",
   "Forgetting the middle term repeats when checking a continued proportion.",
   "Applying componendo-dividendo without the base proportion being true.",
   "Taking the arithmetic mean (a+b)/2 instead of √(ab) for the mean proportional."]),

 sub("rp-partnership", "Partnership",
  md(r"Profit is divided in the ratio of **capital × time** invested.",
     "",
     r"- Same period: share ratio = capital ratio $C_1 : C_2 : C_3$.",
     r"- Different periods (or a partner joins later / withdraws early): share ratio $= C_1 T_1 : C_2 T_2 : C_3 T_3$ (capital-months).",
     "- A working partner's fee/salary/commission is taken OUT of the profit first; the rest is divided by capital-time ratios.",
     "",
     "For a mid-year capital change, split the year into stretches and add capital × months over the stretches."),
  [formula("Simple partnership", r"P_1 : P_2 = C_1 : C_2 \quad (\text{same time})"),
   formula("Compound partnership", r"P_1 : P_2 : P_3 = C_1T_1 : C_2T_2 : C_3T_3"),
   formula("Working partner", r"\text{profit} = \text{manager's cut} + \text{residual split by } C_iT_i"),
   formula("Capital change mid-year", r"\text{effective capital} = C_a t_1 + C_b t_2 + \cdots")],
  [trick("Capital-months table",
         "One row per partner: capital × months. The profit ratio is the row ratio — no other step.",
         "A invests ₹12,000 for the full year; B joins after 4 months with ₹18,000. Divide a ₹9,600 profit.",
         "A: 12,000 × 12 = 144,000; B: 18,000 × 8 = 144,000 ⇒ 1 : 1 ⇒ ₹4,800 each."),
   trick("Deduct the working partner's cut first",
         "Salary/commission % applies to the whole profit; only the residue is shared by capital-time.",
         "A and B invest ₹6,000 and ₹4,000. B manages the business and gets 10% of the profit. On a ₹9,000 profit, find A's share.",
         r"Cut = ₹900; residue ₹8,100 split 3 : 2 ⇒ A = $\frac{3}{5} \times 8100$ = ₹4,860."),
   trick("Split the year for capital changes",
         "Add capital × months across the stretches of the year.",
         "A starts with ₹20,000 and adds ₹5,000 after 6 months. B invests ₹22,500 throughout. Profit ratio?",
         r"A: $20000 \times 6 + 25000 \times 6 = 270000$; B: $22500 \times 12 = 270000$ ⇒ **1 : 1**.")],
  ["Ignoring time when partners join at different dates.",
   "Applying the working partner's % after sharing instead of before.",
   "For months: counting the joiner's period from the start of the year instead of from the joining month.",
   "For mid-year capital changes, using only the final capital."]),

 sub("rp-ages", "Problems on ages",
  md(r"**Golden rule:** the *difference* of ages is constant over time; the *sum* grows by 2 per year; each person's age grows by 1 per year.",
     "",
     "Standard template: present ratio given (say a : b), and a ratio after (or before) n years given. Write present ages ax, bx and form the equation from the second ratio.",
     "",
     r"If one age is a multiple of the other ('father is 3 times the son'), write the larger as k × smaller and use the time-shifted condition. Two unknowns are never needed — one multiplier x or k suffices.",
     "",
     "Double-ratio questions (a ratio n years ago AND a ratio n years hence) give two equations in x; eliminate x."),
  [formula("Present = a x, b x", r"\frac{ax + n}{bx + n} = \frac{p}{q} \quad (\text{ratio after } n \text{ years})"),
   formula("Ratio n years ago", r"\frac{ax - n}{bx - n} = \frac{p}{q}"),
   formula("Constant difference", r"A - B \text{ is the same at every time}"),
   formula("Multiple of age", r"F = kS \Rightarrow \frac{F - n}{S - n} = \frac{p}{q}")],
  [trick("Multiplier + shift equation",
         "Ages = ax and bx now; add/subtract the shift; equate the new ratio; solve for x.",
         "The present ages of A and B are in ratio 5 : 7. After 8 years the ratio becomes 3 : 4. Find the sum of their present ages.",
         r"$\frac{5x+8}{7x+8} = \frac{3}{4}$ ⇒ $20x + 32 = 21x + 24$ ⇒ x = 8. Ages 40 and 56 ⇒ sum **96**."),
   trick("Use the constant difference",
         "The gap between two ages never changes — compute it once and reuse it at any time point.",
         "Father is 3 times as old as his son. Eight years ago he was 5 times as old. Find their present ages.",
         r"Gap = 3s − s = 2s. Eight years ago gap = 2s still: $\frac{3s-8}{s-8} = 5$ ⇒ s = 16, father 48 (gap 32, checks out)."),
   trick("Two ratios bracket the answer",
         "With 'n years ago' and 'n years hence' ratios, form both equations and eliminate x by subtraction.",
         "Six years ago A : B was 5 : 6, and six years hence it will be 6 : 7. Find B's present age.",
         r"$7(5x+12) = 6(6x+12)$ ⇒ x = 12 ⇒ B $= 6 \times 12 + 6 = 78$.")],
  ["Shifting the ratio by n (ratio 5:7 now does NOT become 5:7 + n).",
   "Adding n to the sum of ages once instead of twice.",
   "For 'n years ago', subtracting from the ratio terms but forgetting both persons.",
   "Assuming the ratio difference (b − a)x equals the age difference at a shifted time."]),

 sub("rp-money-applications", "Money ratios: income–expenditure, coins & mixed amounts",
  md("Two classic containers for ratios:",
     "",
     r"- **Income–expenditure:** incomes and expenditures are given as two ratios, and each person's savings (income − expenditure) is known. Set incomes $= ax, bx$ and expenditures $= py, qy$ and solve the two saving equations.",
     r"- **Coin bags:** numbers of coins of denominations are in a given ratio. Value per 'set' = Σ(count × denomination); total value = (value per set) × k.",
     "",
     "The two-variable (x, y) income-expenditure setup is the standard CGL hard question — keep the arithmetic in fractions and it stays small."),
  [formula("Savings equations", r"ax - py = s_1,\quad bx - qy = s_2"),
   formula("Coin value", r"\text{total value} = k \sum_i (n_i \times d_i)"),
   formula("Difference of shares", r"\text{given excess} = (b - a)x")],
  [trick("Solve for x, y in two lines",
         "Write both saving equations, subtract them to kill one variable.",
         "Incomes of A and B are in ratio 8 : 5 and expenditures in 5 : 3. If each saves ₹1,200, find A's income.",
         "8x − 5y = 1200 and 5x − 3y = 1200 ⇒ subtract: 3x − 2y = 0 ⇒ y = 1.5x ⇒ 0.5x = 1200 ⇒ x = 2400 ⇒ A's income = 8 × 2400 = ₹19,200."),
   trick("Value per set for coins",
         "Take one full set of coins in the given ratio, price it, and scale.",
         "A bag has 50-paise, 25-paise and 10-paise coins in the ratio 7 : 6 : 5 amounting to ₹550 in total. Find the number of 25-paise coins.",
         "Set value = 350 + 150 + 50 = 550 paise ⇒ 550 ÷ 5.50 = 100 sets ⇒ 25p coins = 6 × 100 = 600."),
   trick("Sum-difference shortcuts",
         "Sum of shares = (a + b)x, difference = (b − a)x — jump straight to x from whichever is given.",
         "Two numbers in ratio 5 : 7 have difference 12. Find the smaller.",
         "2x = 12 ⇒ x = 6 ⇒ smaller = 30.")],
  [r"Using the expenditure ratio with the income multiplier x (they are different variables x and y).",
   "Mixing paise and rupees in coin problems (1 rupee = 100 paise).",
   "In coin questions, giving the value of the coins instead of their count (or vice versa).",
   "Forgetting to check that savings come out positive for both persons."]),
]

pyq = [
 pat("Divide an amount in a given ratio", "very common",
     "A sum (inheritance, bonus, scholarship) split among 2-3 people in ratio m : n : p; find a share, or a share given the total/difference.",
     "Share = fraction × total. If one share or the difference is given, recover the multiplier x first."),
 pat("Combine two ratios into A : B : C", "very common",
     "'A : B = …, B : C = …, find A : B : C' or a quantity-based version ('twice of A = thrice of B').",
     "Make the shared term equal (LCM bridge). Convert 'twice of A = thrice of B' into A : B = 3 : 2 first."),
 pat("Mean / third / fourth proportional", "common",
     "Direct definition question: 'mean proportional between a and b', 'third proportional to a and b'.",
     "√(ab), b²/a, bc/a respectively. Pure formula recall — 20-second marks."),
 pat("Partnership profit division", "very common",
     "2-3 partners, capitals (sometimes changed mid-year or joined late), profit at year end; find a share or the total.",
     "Capital × months ratio, then fraction × profit. Working partner: take their cut out of the profit first."),
 pat("Ages: present and shifted ratios", "very common",
     "'Ratio of present ages is a : b; after/before n years it is p : q' or 'father is k times the son'.",
     "Ages ax, bx; shift both by n; equate to p : q. The constant age-difference is a good checker."),
 pat("Income–expenditure–savings ratios", "common",
     "Two ratios (income, expenditure) plus equal or unequal savings; find an income.",
     "Two linear equations in x and y; subtract to eliminate. Keep everything fractional."),
 pat("Coin denomination ratios", "occasional",
     "50p/25p/10p (or ₹1/50p) coins in a ratio with total value; find coin count or total.",
     "Price one set of coins, divide the total value by the set value to get the number of sets."),
 pat("Componendo–dividendo", "occasional",
     "(x + y)/(x − y) given as a ratio; find x : y or x : (x + y).",
     r"Jump formula: $\frac{x}{y} = \frac{p+q}{p-q}$. Verify the direction (sum over difference)."),
]

solved = []

assert F(2, 10) * 2500 == 500 and F(3, 10) * 2500 == 750
solved.append(Q("rp-s01", "A sum of ₹2,500 is divided among A, B and C in the ratio 2 : 3 : 5. What is the largest share?",
  ["₹500", "₹750", "₹1,000", "₹1,250"], 3, F(5, 10) * 2500,
  md("Total parts = 2 + 3 + 5 = 10.",
     r"Largest share (C) = $\frac{5}{10} \times 2500$ = ₹1,250."),
  "1 part = 2500/10 = 250 ⇒ C = 5 × 250 = ₹1,250.",
  "easy", "rp-basics", "divide amount in ratio", 25))

assert F(3, 4) == F(9, 12) and F(6, 12) == F(1, 2)
solved.append(Q("rp-s02", "If A : B = 3 : 4 and B : C = 2 : 3, then A : B : C is:",
  ["3 : 4 : 6", "3 : 4 : 8", "6 : 8 : 9", "2 : 3 : 4"], 0, (1, F(4, 3), 2),
  md("Make the B-parts equal: LCM of 4 and 2 = 4.",
     "A : B = 3 : 4 stays; B : C = 2 : 3 becomes 4 : 6.",
     "So A : B : C = **3 : 4 : 6**."),
  "B = 4: scale the second ratio by 2. Answer 3 : 4 : 6 (option 6 : 8 : 9 is the trap from wrong scaling).",
  "easy", "rp-basics", "combine ratios", 30))

assert 18 * 18 // 12 == 27
solved.append(Q("rp-s03", "Find the third proportional to 12 and 18.",
  ["24", "27", "30", "36"], 1, 27,
  md(r"$12 : 18 :: 18 : x$ ⇒ $12x = 18 \times 18$ ⇒ $x = 27$."),
  "Third proportional = b²/a = 18²/12 = 27.",
  "easy", "rp-proportion", "third proportional", 25))

assert F(3, 5) * 28800 == 17280
solved.append(Q("rp-s04", "A and B enter into a partnership. A invests ₹30,000 for 12 months and B invests ₹40,000 for 6 months. At the end of the year they earn a profit of ₹28,800. Find A's share.",
  ["₹11,520", "₹14,400", "₹17,280", "₹19,200"], 2, F(3, 5) * 28800,
  md(r"Capital-months: A $= 30000 \times 12 = 360000$; B $= 40000 \times 6 = 240000$.",
     "Ratio = 360 : 240 = 3 : 2.",
     r"A's share = $\frac{3}{5} \times 28800$ = ₹17,280."),
  "Profit ratio is capital × time = 3 : 2 ⇒ A gets 3/5 of ₹28,800 = ₹17,280.",
  "medium", "rp-partnership", "capital-months partnership", 50))

sol = sp_solve = None
import sympy as sp
x = sp.symbols("x")
sol = sp.solve(sp.Eq(7 * (4 * x + 16), 6 * (5 * x + 16)), x)
assert sol == [8] and 4 * 8 + 5 * 8 == 72
solved.append(Q("rp-s05", "The present ages of two persons are in the ratio 4 : 5. After 16 years, the ratio of their ages will be 6 : 7. What is the sum of their present ages?",
  ["54 years", "63 years", "72 years", "81 years"], 2, 72,
  md(r"Let present ages be $4x$ and $5x$.",
     r"$\frac{4x + 16}{5x + 16} = \frac{6}{7}$ ⇒ $28x + 112 = 30x + 96$ ⇒ $2x = 16$ ⇒ $x = 8$.",
     r"Present ages 32 and 40 ⇒ sum **72 years**."),
  "Cross-multiply once: 7(4x+16) = 6(5x+16) ⇒ x = 8 ⇒ sum = 9x = 72. (Constant difference 8 years never changes — good check.)",
  "medium", "rp-ages", "present and future ratio", 45))

# ------------------------------------------------------------------ practice
P = []

assert F(3, 5) * 1200 == 720
P.append(Q("rp-q01", "₹1,200 is divided between A and B in the ratio 2 : 3. What is B's share?",
  ["₹480", "₹600", "₹720", "₹800"], 2, 720,
  md(r"B's share = $\frac{3}{5} \times 1200$ = ₹720."),
  "5 parts = 1200 ⇒ 1 part = 240 ⇒ B = 3 × 240 = ₹720.",
  "easy", "rp-basics", "divide amount in ratio", 25))

assert 8 + 12 + 15 == 35
P.append(Q("rp-q02", "If A : B = 2 : 3 and B : C = 4 : 5, then A : C is:",
  ["8 : 15", "2 : 5", "3 : 5", "8 : 12"], 0, (1, F(15, 8)),
  md("A : B : C = 8 : 12 : 15 (bridge B = 12).",
     r"$A : C = 8 : 15$."),
  "A/B = 2/3, B/C = 4/5 ⇒ A/C = (2/3)(4/5) = 8/15.",
  "easy", "rp-basics", "combine ratios", 30))

assert 9 * 12 // 4 == 27
P.append(Q("rp-q03", "The fourth proportional to 4, 9 and 12 is:",
  ["16", "21", "27", "36"], 2, 27,
  md(r"$\frac{4}{9} = \frac{12}{d}$ ⇒ $4d = 108$ ⇒ $d = 27$."),
  "d = bc/a = (9 × 12)/4 = 27.",
  "easy", "rp-proportion", "fourth proportional", 25))

assert 48 // 8 * 3 == 18
P.append(Q("rp-q04", "The ages of A and B are in the ratio 3 : 5 and the sum of their ages is 48 years. A's age is:",
  ["15 years", "18 years", "21 years", "30 years"], 1, 18,
  md("8 parts = 48 ⇒ 1 part = 6.",
     "A = 3 × 6 = **18 years**."),
  "1 part = 48/8 = 6 ⇒ A = 18 (B = 30).",
  "easy", "rp-ages", "age ratio with sum", 25))

assert 12 * 6 == 72
P.append(Q("rp-q05", "Two numbers are in the ratio 5 : 7. If their difference is 12, their sum is:",
  ["60", "66", "72", "84"], 2, 72,
  md("Numbers 5x, 7x ⇒ 2x = 12 ⇒ x = 6.",
     "Sum = 12x = **72**."),
  "Difference 2 parts = 12 ⇒ 1 part = 6 ⇒ sum 12 parts = 72.",
  "easy", "rp-basics", "ratio sum-difference", 25))

assert math.isqrt(25 * 81) == 45
P.append(Q("rp-q06", "The mean proportional between 25 and 81 is:",
  ["45", "50", "53", "56.25"], 0, 45,
  md(r"Mean proportional $= \sqrt{25 \times 81} = 5 \times 9 = 45$."),
  "√2025 = 45. (53 is the arithmetic mean (25+81)/2 — the trap.)",
  "medium", "rp-proportion", "mean proportional", 25))

assert 12000 * 12 == 18000 * 8 and 9600 // 2 == 4800
P.append(Q("rp-q07", "A starts a business with ₹12,000. After 4 months, B joins with ₹18,000. At the end of the year, in what ratio should they divide a profit of ₹9,600?",
  ["1 : 1", "2 : 3", "3 : 4", "4 : 5"], 0, (1, 1),
  md(r"A: $12000 \times 12 = 144000$; B: $18000 \times 8 = 144000$.",
     "Ratio = 1 : 1 ⇒ ₹4,800 each."),
  "12k × 12 months vs 18k × 8 months — equal ⇒ 1 : 1.",
  "medium", "rp-partnership", "late joining partner", 40))

vset = 7 * 50 + 6 * 25 + 5 * 10
assert vset == 550 and 55000 // vset == 100 and 6 * 100 == 600
P.append(Q("rp-q08", "A bag contains 50-paise, 25-paise and 10-paise coins in the ratio 7 : 6 : 5, amounting to ₹550 in all. The number of 25-paise coins is:",
  ["500", "550", "600", "650"], 2, 600,
  md("Value of one set = 350 + 150 + 50 = 550 paise = ₹5.50.",
     "Number of sets = 550 ÷ 5.50 = 100.",
     "25-paise coins = 6 × 100 = **600**."),
  "One set is worth ₹5.50; ₹550/5.50 = 100 sets ⇒ 600 twenty-five-paise coins.",
  "medium", "rp-money-applications", "coin ratio value", 55))

sol = None
x = sp.symbols("s")
sol = sp.solve(sp.Eq(3 * x - 8, 5 * (x - 8)), x)
assert sol == [16]
P.append(Q("rp-q09", "A father is three times as old as his son. Eight years ago, he was five times as old as his son. The father's present age is:",
  ["42 years", "45 years", "48 years", "51 years"], 2, 48,
  md("Let the son be s; father = 3s.",
     r"$3s - 8 = 5(s - 8)$ ⇒ $3s - 8 = 5s - 40$ ⇒ $s = 16$.",
     "Father = 3 × 16 = **48 years**."),
  "Age gap = 2s is constant: now 32, so 8 years ago son 8 = 32/4? Quicker: 5:1 ratio with gap 32 needs son 8, father 40 — that's 8 years ago ⇒ now 16 and 48.",
  "medium", "rp-ages", "father-son multiple", 45))

assert F(5 + 3, 5 - 3) == 4
P.append(Q("rp-q10", r"If $\frac{x+y}{x-y} = \frac{5}{3}$, then $\frac{x}{y}$ equals:",
  [r"$\frac{5}{3}$", "2", "4", "8"], 2, 4,
  md(r"By componendo and dividendo: $\frac{x}{y} = \frac{5+3}{5-3} = \frac{8}{2} = 4$."),
  r"x : y = (p + q) : (p − q) = 8 : 2 = 4 : 1.",
  "medium", "rp-proportion", "componendo dividendo", 30))

sh = [20000 * 12, 15000 * 12, 25000 * 8]
g = math.gcd(math.gcd(*sh), 10 ** 9)
red = [s // 1000 for s in sh]
from fractions import Fraction as Fr
assert [Fr(s) / max(sh) for s in sh] == [Fr(12, 12), Fr(9, 12), Fr(10, 12)]
P.append(Q("rp-q11", "A, B and C invest ₹20,000, ₹15,000 and ₹25,000 respectively in a business. C joined the business 4 months after its start. If the total profit at the end of the year is ₹46,500, find C's share.",
  ["₹12,000", "₹13,500", "₹15,000", "₹16,500"], 2, 15000,
  md(r"A: $20000 \times 12 = 240000$; B: $15000 \times 12 = 180000$; C: $25000 \times 8 = 200000$.",
     "Ratio = 240 : 180 : 200 = 12 : 9 : 10 (31 parts).",
     r"C = $\frac{10}{31} \times 46500$ = ₹15,000."),
  "C worked only 8 months. Capital-months 12 : 9 : 10 ⇒ C gets 10/31 of ₹46,500 = ₹15,000.",
  "medium", "rp-partnership", "three partners different times", 55))

sol = None
x = sp.symbols("x")
sol = sp.solve(sp.Eq(4 * (5 * x + 8), 3 * (7 * x + 8)), x)
assert sol == [8] and 40 + 56 == 96
P.append(Q("rp-q12", "The ratio of the present ages of A and B is 5 : 7. Eight years from now, the ratio will become 3 : 4. The sum of their present ages is:",
  ["84 years", "90 years", "96 years", "108 years"], 2, 96,
  md(r"$\frac{5x + 8}{7x + 8} = \frac{3}{4}$ ⇒ $20x + 32 = 21x + 24$ ⇒ $x = 8$.",
     r"Ages 40 and 56 ⇒ sum = **96 years**."),
  "Cross-multiply: 4(5x+8) = 3(7x+8) ⇒ x = 8 ⇒ 12x = 96.",
  "medium", "rp-ages", "present and future ratio", 40))

xx, y = sp.symbols("x y")
sol = sp.solve([sp.Eq(8 * xx - 5 * y, 1200), sp.Eq(5 * xx - 3 * y, 1200)], [xx, y])
assert sol[xx] == 2400 and sol[xx] * 8 == 19200
P.append(Q("rp-q13", "The incomes of A and B are in the ratio 8 : 5 and their expenditures are in the ratio 5 : 3. If each saves ₹1,200, then A's income is:",
  ["₹14,400", "₹16,800", "₹19,200", "₹21,600"], 2, 19200,
  md("Incomes 8x, 5x; expenditures 5y, 3y.",
     "8x − 5y = 1200 and 5x − 3y = 1200.",
     "Subtracting: 3x − 2y = 0 ⇒ y = 1.5x. Then 5x − 4.5x = 1200 ⇒ x = 2400.",
     r"A's income = $8 \times 2400$ = ₹19,200."),
  "Two equations, subtract to kill one variable: y = 1.5x ⇒ 0.5x = 1200 ⇒ A = 8x = ₹19,200.",
  "hard", "rp-money-applications", "income-expenditure savings", 80))

p = 9000
rem = p - 900
assert F(6000, 10000) * rem == 4860 and 900 + F(4000, 10000) * rem == 4140
P.append(Q("rp-q14", "A and B invest ₹6,000 and ₹4,000 in a business. B manages the business and receives 10% of the profit as salary. If the annual profit is ₹9,000, what does A receive?",
  ["₹4,140", "₹4,500", "₹4,860", "₹5,400"], 2, 4860,
  md("B's management salary = 10% of 9,000 = ₹900. Residue = ₹8,100.",
     "Capital ratio = 6,000 : 4,000 = 3 : 2.",
     r"A gets $\frac{3}{5} \times 8100$ = ₹4,860 (B gets ₹3,240 + ₹900 = ₹4,140)."),
  "Cut 10% off the top, split 3 : 2: A = 3/5 × 8,100 = ₹4,860.",
  "hard", "rp-partnership", "working partner salary", 65))

sol = None
x = sp.symbols("x")
sol = sp.solve(sp.Eq(7 * (5 * x + 12), 6 * (6 * x + 12)), x)
assert sol == [12] and 6 * 12 + 6 == 78
P.append(Q("rp-q15", "Six years ago the ratio of the ages of A and B was 5 : 6. Six years hence this ratio will become 6 : 7. B's present age is:",
  ["66 years", "72 years", "78 years", "84 years"], 2, 78,
  md(r"Ages 6 years ago: 5x, 6x. Six years hence: $5x + 12$, $6x + 12$.",
     r"$\frac{5x + 12}{6x + 12} = \frac{6}{7}$ ⇒ $35x + 84 = 36x + 72$ ⇒ $x = 12$.",
     r"B now $= 6 \times 12 + 6 = 78$ years."),
  "The 12-year gap between the two time points adds 12 to each age. Solve 7(5x+12) = 6(6x+12) ⇒ x = 12 ⇒ B = 78.",
  "hard", "rp-ages", "two shifted ratios", 75))

topic = {
 "id": "ratio-proportion", "sectionId": "quant", "title": "Ratio, Proportion, Partnership & Ages", "order": 5,
 "importance": "high", "avgQuestions": {"tier1": 2, "tier2": 2},
 "summary": "Ratio technique with its three biggest exam containers: proportion (mean/third/fourth proportional), partnership (capital × time profit splits) and ages (present vs shifted ratios). Tier 1 reliably has 2 questions from this cluster; most are 30–45 second marks once the multiplier habit is built.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
