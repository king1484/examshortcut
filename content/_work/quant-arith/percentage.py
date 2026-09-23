from _lib import *

# ------------------------------------------------------------------ checks
assert 35 * 480 / 100 == 168
assert 256 * 100 / 40 == 640
assert F(3, 8) * 100 == F(75, 2) == F(375, 10)
assert F(200 - 250, 250) * 100 == -20
assert 60 * F(35, 100) == 21
assert 0.8 * 7500 == 6000 and 6000 * F(60, 100) - 6000 * F(40, 100) == 1200
assert 40000 * F(110, 100) == 44000 and 44000 * F(95, 100) == 41800
assert 500 * F(45, 100) - 500 * F(33, 100) == 60 and 500 * F(33, 100) + 45 == 210
assert F(100 * 20, 120) == F(50, 3) == F(100, 6)
assert F(108, 100) / F(120, 100) == F(9, 10)
assert F(120, 100) / F(90, 100) == F(4, 3)
i, e = 100 * F(115, 100), 80 * F(110, 100)
assert i - e == 27 and F(27 - 20, 20) * 100 == 35
assert F(40, 100) * F(25, 100) == F(10, 100)
x = 40000
for r in (20, 25, 10):
    x = x * (100 + r) / 100
assert x == 66000
assert 8100 / F(81, 100) == 10000
assert 400 * F(20, 100) / 5 == 16 and 16 / F(80, 100) == 20
assert 100 * 120 * 90 / (100 * 100) == 108
assert 200 * F(30, 100) == 60 and F(12, 60) * 100 == 20

subtopics = [
 sub("pct-basics", "Percentage meaning & conversions",
  md(r"Per cent means per hundred: $x\% = \frac{x}{100}$. The single most profitable memorisation in Quant is the fraction table — every CGL percentage, profit-loss, interest and DI question gets faster.",
     "",
     "| Fraction | % | Fraction | % |",
     "|---|---|---|---|",
     r"| $\frac{1}{2}$ | 50% | $\frac{1}{8}$ | 12.5% |",
     r"| $\frac{1}{3}$ | $33\frac{1}{3}\%$ | $\frac{3}{8}$ | 37.5% |",
     r"| $\frac{2}{3}$ | $66\frac{2}{3}\%$ | $\frac{5}{8}$ | 62.5% |",
     r"| $\frac{1}{4}$ | 25% | $\frac{1}{6}$ | $16\frac{2}{3}\%$ |",
     r"| $\frac{3}{4}$ | 75% | $\frac{5}{6}$ | $83\frac{1}{3}\%$ |",
     r"| $\frac{1}{5}$ | 20% | $\frac{1}{7}$ | $14\frac{2}{7}\%$ |",
     r"| $\frac{2}{5}$ | 40% | $\frac{1}{9}$ | $11\frac{1}{9}\%$ |",
     r"| $\frac{1}{12}$ | $8\frac{1}{3}\%$ | $\frac{1}{16}$ | 6.25% |",
     "",
     r"**Handy symmetry:** $x\%$ of $y = y\%$ of $x$ (16% of 25 = 25% of 16).",
     "",
     r"$p\%$ of a quantity $N = \frac{pN}{100}$; to find the whole when a part is known, divide: $N = \frac{\text{part} \times 100}{p}$."),
  [formula("Per cent of a number", r"x\% \text{ of } N = \frac{xN}{100}"),
   formula("Fraction to per cent", r"\frac{p}{q} \times 100\%"),
   formula("Per cent to fraction", r"x\% = \frac{x}{100}"),
   formula("Commutativity", r"x\% \text{ of } y = y\% \text{ of } x"),
   formula("Recovering the base", r"N = \frac{\text{part} \times 100}{\text{percentage}}")],
  [trick("The fraction table IS the shortcut",
         "Convert percentages to fractions before multiplying: 12.5% of 640 = 1/8 × 640 = 80. One line, no calculator.",
         "Find $16\\frac{2}{3}\\%$ of 720.",
         r"$16\frac{2}{3}\% = \frac{1}{6}$ ⇒ $\frac{720}{6} = 120$."),
   trick("Swap the percentages",
         r"Use $x\%$ of $y = y\%$ of $x$ when the swapped pair is friendlier.",
         "Find 4% of 25.",
         r"$= 25\%$ of $4 = 1$."),
   trick("Part-to-whole in one division",
         "'p% of a number is k' ⇒ number = 100k/p. Look at options: only one will make the product land on k.",
         "If 40% of a number is 256, find the number.",
         r"$\frac{256 \times 100}{40} = 640$.")],
  [r"Treating $x\%$ of $y$ as $xy$ (missing the ÷100).",
   "Converting 1/8 as 18% instead of 12.5%.",
   "Dividing by the wrong base: % change must always use the ORIGINAL value as denominator.",
   r"Reading 'B's income is x% of A's' as 'x% more than A's'."]),

 sub("pct-change", "Percentage increase / decrease & successive change",
  md(r"Percentage change $= \frac{\text{final} - \text{initial}}{\text{initial}} \times 100$ (initial = the base being changed).",
     "",
     r"**Two successive changes** of $a\%$ and $b\%$ combine to $a + b + \frac{ab}{100}$ (keep minus signs for decreases).",
     "",
     r"+10% then −10% is **not** zero: net $= -\frac{10^2}{100} = -1\%$ (a fall of a²/100 %).",
     "",
     r"To restore an original value after a multiplier, divide back: if $F = I \times \frac{120}{100}$ then $I = F \times \frac{100}{120}$.",
     "",
     "Model every change as a fraction multiplier: +20% → ×6/5, −25% → ×3/4. Chain the multipliers."),
  [formula("Percentage change", r"\%\ \text{change} = \frac{\text{final} - \text{initial}}{\text{initial}} \times 100"),
   formula("Successive change", r"a + b + \frac{ab}{100}", "use signs: + for increase, − for decrease"),
   formula("Same % up and down", r"+x\% \text{ then } -x\% \Rightarrow \text{net} = -\frac{x^2}{100}\%"),
   formula("Multiplier form", r"\text{final} = \text{initial} \times \frac{100 + a}{100} \times \frac{100 - b}{100}"),
   formula("Original value back", r"\text{initial} = \text{final} \times \frac{100}{100 + a}")],
  [trick("Multiplier chaining",
         "Replace every % by its fraction multiplier and multiply across all steps.",
         "A number is increased by 20% and the result is decreased by 10%. Net change?",
         r"$\frac{6}{5} \times \frac{9}{10} = \frac{54}{50} = \frac{27}{25}$ ⇒ net $+\frac{2}{25} = +8\%$."),
   trick("a + b + ab/100 in one line",
         "Add, then adjust by the product term. Fastest when one change is small.",
         "Successive changes: +30% and −20%.",
         r"$30 - 20 - \frac{600}{100} = 10 - 6 = 4\%$ increase."),
   trick("Reverse to the original",
         "To undo +25%, divide by 5/4 (not multiply by 75/100).",
         "After a 25% increase a salary is ₹50,000. What was it before?",
         "Salary after increase = ₹50,000. Before = ₹$50000 \\times \\frac{100}{125}$, i.e. ₹40,000.")],
  [r"Adding successive percentages without the $\frac{ab}{100}$ term.",
   r"Assuming +x% followed by −x% is a net zero.",
   "Using the new (increased) value as the base when computing a percentage decrease.",
   "Undoing +25% by applying −25% (the right move is ÷1.25)."]),

 sub("pct-more-less", "'x% more than' ↔ 'x% less than' & chains",
  md(r"The 'more than / less than' pair has **different bases** — this asymmetry is tested constantly.",
     "",
     r"- If A is $x\%$ **more** than B: $A = B\left(1 + \frac{x}{100}\right)$, and B is $\frac{100x}{100 + x}\%$ **less** than A.",
     r"- If A is $x\%$ **less** than B: $A = B\left(1 - \frac{x}{100}\right)$, and B is $\frac{100x}{100 - x}\%$ **more** than A.",
     "",
     r"**Chains:** if A = a% of B and B = b% of C, then A $= \frac{ab}{100}\%$ of C.",
     "",
     "The 'less than' percentage is always LARGER than the 'more than' percentage — use that to sanity-check options."),
  [formula("More → less", r"A = B\left(1 + \frac{x}{100}\right) \Rightarrow B = A\left(\frac{100}{100+x}\right),\ \text{less by } \frac{100x}{100+x}\%"),
   formula("Less → more", r"A = B\left(1 - \frac{x}{100}\right) \Rightarrow \text{B is } \frac{100x}{100-x}\% \text{ more than A}"),
   formula("Chain of percentages", r"A = \frac{a}{100}B,\ B = \frac{b}{100}C \Rightarrow A = \frac{ab}{100}\% \text{ of } C")],
  [trick("Flip with 100x/(100±x)",
         "More→less uses 100+x in the denominator; less→more uses 100−x. The answer must be bigger than x for the less→more direction.",
         "A's salary is 25% more than B's. B's salary is what per cent less than A's?",
         r"$\frac{100 \times 25}{125} = 20\%$."),
   trick("Assume the base = 100",
         "Set the unmentioned quantity to 100 and read off both values.",
         "A's salary is 20% more than B's. By what per cent is B's salary less than A's?",
         "B = 100, A = 120. Gap 20, base A = 120 ⇒ 20/120 = 16⅔%."),
   trick("Chain percentages by multiplying fractions",
         "Convert each link to a fraction of the next and multiply.",
         "A's income is 40% of B's, and B's is 25% of C's. A's income is what % of C's?",
         r"$\frac{40}{100} \times \frac{25}{100} = \frac{10}{100}$ ⇒ 10%.")],
  [r"Answering 'x% less' with the same x (the correct value $\frac{100x}{100+x}$ is always smaller than x).",
   "Using 100 − x in the denominator for the more→less direction.",
   "Chaining by adding percentages instead of multiplying fractions.",
   "Ignoring which quantity the question calls the base."]),

 sub("pct-population-election", "Population growth, depreciation & elections",
  md(r"**Population / value growth-decay:** value after n years $= P\left(1 \pm \frac{r}{100}\right)^n$ (+ for growth, − for depreciation). Work backwards by dividing.",
     "",
     "**Two different rates** in two years: apply the multipliers one after another (e.g. ×11/10 then ×19/20).",
     "",
     "**Election problems:** total votes polled = valid + invalid. Both candidates' shares must be read off the VALID votes. Margin = difference of shares × valid votes.",
     "",
     r"Depreciation is the same formula with a negative rate: present $= P\left(\frac{100-r}{100}\right)^n$."),
  [formula("Growth / decay", r"P_n = P\left(1 \pm \frac{r}{100}\right)^n"),
   formula("Two different rates", r"P_2 = P\left(1 + \frac{r_1}{100}\right)\left(1 + \frac{r_2}{100}\right)"),
   formula("Depreciated value back", r"P = \text{present} \times \left(\frac{100}{100-r}\right)^n"),
   formula("Election margin", r"\text{margin} = (\text{winner share} - \text{loser share}) \times \text{valid votes}")],
  [trick("Multiplier chips for n years",
         "Chips: +10% → 11/10, −5% → 19/20. Multiply chips across years; the final fraction tells everything.",
         "A town's population of 40,000 grows 10% in year 1 and falls 5% in year 2. Find the present population.",
         r"$40000 \times \frac{11}{10} \times \frac{19}{20} = 22000 \times \frac{19}{10}... = 41800$? Compute: $40000 \times 1.1 = 44000$, $44000 \times 0.95 = 41800$."),
   trick("Work backwards with division",
         "For 'value n years ago', divide by the chips instead of guessing.",
         "A machine worth ₹8,100 depreciates at 10% p.a. What was its value 2 years ago?",
         "Divide by the chip twice: ₹$8100 \\times \\frac{10}{9} = 9000$, then $9000 \\times \\frac{10}{9} = 10000$."),
   trick("Elections: everything on valid votes",
         "Convert both candidates' data to fractions of valid votes; the total polled number then follows from the margin.",
         "In an election, 20% of votes polled were invalid. The winner got 60% of valid votes and won by 1200 votes. Total votes polled?",
         r"Margin = 20% of valid = $\frac{1}{5}V = 1200$ ⇒ V = 6000 = 80% of total ⇒ total = 7500.")],
  [r"Applying $\left(1 + \frac{r}{100}\right)^n$ when the two years have different rates.",
   "Counting invalid votes as a candidate's votes.",
   r"Depreciating 2 years as $P - 2r\%$ instead of $\left(\frac{90}{100}\right)^2$.",
   "In 'population 2 years ago' questions, dividing by (1 + net%) with the averaged rate."]),

 sub("pct-marks-income", "Marks, income–expenditure–savings & price–consumption",
  md(r"**Pass-marks template:** candidate 1 scores $p\%$ and fails by $f$ marks ⇒ pass mark $= \frac{pM}{100} + f$; candidate 2 scores $q\%$ and exceeds by $e$ ⇒ pass mark $= \frac{qM}{100} - e$. Equate and solve for maximum marks $M$.",
     "",
     r"**Income–expenditure:** savings = income − expenditure. If income is I and savings s%, expenditure = (100 − s)% of I.",
     "",
     r"**Price rises, keep expenditure fixed:** consumption must fall by $\frac{100r}{100 + r}\%$.",
     r"**Price falls, same quantity-money:** extra quantity bought $= \frac{\text{money} \times r}{100 \times \text{reduced price}}$; reduced price $= \frac{r\% \text{ of outlay}}{\text{extra quantity}}$."),
  [formula("Pass marks equation", r"\frac{pM}{100} + f = \frac{qM}{100} - e"),
   formula("Savings identity", r"\text{savings} = \text{income} - \text{expenditure}"),
   formula("Price up r%, expenditure fixed", r"\text{reduce consumption by } \frac{100r}{100+r}\%"),
   formula("Price cut & extra quantity", r"\text{reduced price} = \frac{r\% \text{ of outlay}}{\text{extra quantity}},\quad \text{old price} = \frac{\text{reduced price}}{1 - r/100}")],
  [trick("Marks gap = percentage gap",
         "In two-candidate mark problems the difference of the two percentages times M equals the total mark gap (fail-by + exceed-by).",
         "A candidate scoring 33% fails by 45 marks; another scoring 45% gets 15 marks more than the pass mark. Find the maximum marks.",
         r"$(45 - 33)\%$ of M = 45 + 15 = 60 ⇒ $M = 500$."),
   trick("Income = 100 bookkeeping",
         "Set income to 100, express savings and expenditure, then apply every change and read the answer off.",
         "A man saves 20% of his income. His income rises 15% and expenditure rises 10%. % increase in savings?",
         "Income 100 → save 20, spend 80. New: income 115, spend 88 ⇒ save 27. Increase = 7/20 = 35%."),
   trick("Price cut: r% of money buys the extra",
         "A r% price cut saves r% of the outlay, and that saved money buys the extra quantity at the REDUCED price.",
         "A 20% cut in sugar price lets a buyer get 5 kg more for ₹400. Find the original price.",
         "Saved money = 20% of 400 = ₹80 = price of extra 5 kg ⇒ reduced price ₹16/kg ⇒ original price = ₹$16 \\times \\frac{100}{80}$ = ₹20 per kg.")],
  [r"Using the fail-by and exceed-by marks with the same sign (they act in opposite directions: +f and −e on the two sides).",
   "In savings problems, raising expenditure by 10% as 'reduce savings by 10%'.",
   "For the price-cut question, dividing the full outlay (not r% of it) by the extra quantity.",
   r"Consumption reduction for a 25% price rise answered as 25% instead of 20%."]),
]

pyq = [
 pat("x% of a number / fraction conversion", "very common",
     "'What is 35% of 480', '1/8 as a percentage', 'if p% of N is k find N'.",
     "Fraction table + one multiplication or division. Under 30 seconds; never long-multiply."),
 pat("Successive percentage change", "very common",
     "Two or three changes applied one after another (price/population/marks), asking net change or final value.",
     "Multiplier chips (×6/5, ×3/4 …) or a + b + ab/100. For up-then-down by the same rate, remember the −x²/100 rule."),
 pat("'More than / less than' flip", "very common",
     "'A's income is 25% more than B's; B's income is what % less than A's?'",
     r"$\frac{100x}{100+x}$ (more→less) or $\frac{100x}{100-x}$ (less→more). Assume the base = 100 to verify."),
 pat("Population / depreciation over years", "common",
     "Population grows/falls at stated yearly rates (same or different); find present, past, or future value.",
     "Chain the multipliers forward; divide by them to go back. Two different rates: never average them, multiply chips."),
 pat("Election / voting percentages", "common",
     "Two candidates, invalid votes given, winner's share of valid votes and margin given; find total votes or votes got.",
     "Work everything in fractions of VALID votes; margin% × valid votes = margin; then unmask the total."),
 pat("Pass marks with two candidates", "common",
     "One candidate fails by f marks at p%, another exceeds pass by e at q%; find maximum marks or pass mark.",
     "% gap × M = f + e. Solve M, then pass mark from either candidate."),
 pat("Price rise vs consumption / expenditure", "common",
     "'Price rises 20%, by what % reduce consumption to keep expenditure same' or the reverse (5 kg more for a fixed outlay).",
     r"Consumption factor = new expenditure factor ÷ price factor. For the outlay version, r% of money = extra quantity × reduced price."),
 pat("Income–expenditure–savings change", "occasional",
     "Savings % given; income and expenditure change by given %; find % change in savings.",
     "Set income = 100, track all three quantities with chips, compute the new savings directly."),
]

solved = []

v = 20 - 10 + F(20 * -10, 100)
assert v == 8
solved.append(Q("pct-s01", "A number is first increased by 20% and then decreased by 10%. What is the net percentage change?",
  ["+8%", "+10%", "−8%", "+12%"], 0, v,
  md(r"Formula: $a + b + \frac{ab}{100}$ with $a = 20$, $b = -10$.",
     r"$= 20 - 10 - \frac{200}{100} = 10 - 2 = +8\%$."),
  r"Chips: $\frac{6}{5} \times \frac{9}{10} = \frac{27}{25}$ ⇒ +2/25 = +8%.",
  "easy", "pct-change", "successive change", 30))

v = F(50, 3) * F(720, 100) + F(100, 3) * F(450, 100)
assert v == 270 and F(720, 6) + F(450, 3) == 270
solved.append(Q("pct-s02", r"Find the value of $16\frac{2}{3}\%$ of 720 $+$ $33\frac{1}{3}\%$ of 450.",
  ["240", "250", "270", "290"], 2, v,
  md(r"$16\frac{2}{3}\% = \frac{1}{6}$ ⇒ $\frac{720}{6} = 120$.",
     r"$33\frac{1}{3}\% = \frac{1}{3}$ ⇒ $\frac{450}{3} = 150$.",
     "Sum = 120 + 150 = **270**."),
  "Fraction table: 1/6 of 720 = 120, 1/3 of 450 = 150 ⇒ 270.",
  "easy", "pct-basics", "fraction table evaluation", 35))

v = 10 - 10 + F(10 * -10, 100)
assert v == -1
solved.append(Q("pct-s03", "The price of an article is first increased by 10% and then decreased by 10%. What is the net change in price?",
  ["No change", "1% increase", "1% decrease", "2% decrease"], 2, v,
  md(r"Net $= 10 - 10 - \frac{10 \times 10}{100} = -1\%$.",
     "A rise of 10% followed by a fall of 10% always leaves a **1% decrease**."),
  r"Rule: +x% then −x% ⇒ net −$\frac{x^2}{100}\%$ = −1%.",
  "easy", "pct-change", "same % up and down", 25,
  vals=[0, 1, -1, -2]))

v = F(100 * 25, 125)
assert v == 20
solved.append(Q("pct-s04", "A's salary is 25% more than B's salary. B's salary is what per cent less than A's salary?",
  ["25%", "20%", "$18\\frac{3}{4}$%", "15%"], 1, v,
  md(r"Let B = 100 ⇒ A = 125.",
     r"Gap = 25 on base A = 125 ⇒ $\frac{25}{125} \times 100 = 20\%$."),
  r"Flip formula: $\frac{100 \times 25}{100 + 25} = 20\%$. (Answer is never 25%.)",
  "easy", "pct-more-less", "more-less flip", 30))

assert 8100 * 100 // 81 == 10000
solved.append(Q("pct-s05", "The value of a machine depreciates at the rate of 10% per annum. If its present value is ₹8,100, what was its value 2 years ago?",
  ["₹9,000", "₹9,800", "₹10,000", "₹10,800"], 2, 10000,
  md(r"Let the value 2 years ago be P.",
     r"$P\left(\frac{90}{100}\right)^2 = 8100$",
     r"$P \times \frac{81}{100} = 8100$, so P = ₹10,000."),
  r"Divide by the chip twice: $8100 \times \frac{10}{9} = 9000$, $9000 \times \frac{10}{9} = 10000$.",
  "medium", "pct-population-election", "depreciation backwards", 45))

# ------------------------------------------------------------------ practice
P = []

assert 35 * 480 / 100 == 168
P.append(Q("pct-q01", "What is 35% of 480?",
  ["158", "164", "168", "172"], 2, 168,
  md(r"$\frac{35 \times 480}{100} = 35 \times 4.8 = 168$."),
  "10% of 480 = 48; 35% = 48 × 3.5 = 168.",
  "easy", "pct-basics", "percent of number", 25))

assert 256 * 100 / 40 == 640
P.append(Q("pct-q02", "If 40% of a number is 256, then 55% of that number is:",
  ["316", "340", "352", "364"], 2, 352,
  md(r"Number $= \frac{256 \times 100}{40} = 640$.",
     r"$55\%$ of 640 $= 352$."),
  "1% of the number = 256/40 = 6.4 ⇒ 55% = 6.4 × 55 = 352.",
  "easy", "pct-basics", "recover base then percent", 30))

assert F(3, 8) * 100 == F(75, 2)
P.append(Q("pct-q03", r"Expressed as a percentage, $\frac{3}{8}$ is equal to:",
  ["3.75%", "37.5%", "375%", "0.375%"], 1, F(75, 2),
  md(r"$\frac{3}{8} \times 100 = \frac{300}{8} = 37.5\%$."),
  "1/8 = 12.5% ⇒ 3/8 = 3 × 12.5 = 37.5%.",
  "easy", "pct-basics", "fraction to percent", 20))

assert F(50, 250) * 100 == 20
P.append(Q("pct-q04", "The price of an article falls from ₹250 to ₹200. The percentage decrease in price is:",
  ["16$\\frac{2}{3}$%", "20%", "25%", "50%"], 1, 20,
  md(r"Decrease $= 50$ on the original ₹250.",
     r"$\frac{50}{250} \times 100 = 20\%$."),
  "Base is the ORIGINAL 250, not 200. 50/250 = 1/5 = 20%.",
  "easy", "pct-change", "percentage decrease", 25))

assert 60 - 21 == 39 and 60 * F(65, 100) == 39
P.append(Q("pct-q05", "In a class of 60 students, 65% are boys. The number of girls in the class is:",
  ["18", "21", "24", "39"], 1, 21,
  md(r"Girls $= (100 - 65)\%$ of 60 $= 35\%$ of 60 $= 21$."),
  "35% of 60 = 21. (39 is the number of boys — the trap.)",
  "easy", "pct-marks-income", "complement percent", 25))

assert 7500 * 0.8 * 0.2 == 1200
P.append(Q("pct-q06", "In an election between two candidates, 20% of the votes polled were invalid. The winner secured 60% of the valid votes and won by a margin of 1,200 votes. How many votes were polled in total?",
  ["6,000", "7,000", "7,500", "8,000"], 2, 7500,
  md("Let total polled = T; valid = 0.8T.",
     "Winner gets 60% of valid, loser 40%; margin = 20% of valid.",
     r"$0.2 \times 0.8T = 1200$ ⇒ $0.16T = 1200$ ⇒ T = 7500."),
  "Margin is 1/5 of valid votes ⇒ valid = 6000 = 80% of total ⇒ total 7500.",
  "medium", "pct-population-election", "election with invalid votes", 55))

assert 41800 == 40000 * 1.1 * 0.95
P.append(Q("pct-q07", "The population of a town two years ago was 40,000. It increased by 10% in the first year and decreased by 5% in the second year. The present population is:",
  ["41,600", "41,800", "42,000", "42,500"], 1, 41800,
  md(r"$40000 \times \frac{110}{100} = 44000$ after year 1.",
     r"$44000 \times \frac{95}{100} = 41800$ after year 2."),
  "Chips 11/10 × 19/20. Never average the rates (net is +4.5%, not +5%).",
  "medium", "pct-population-election", "population two rates", 45))

assert 500 * 0.45 == 210 + 15 and 500 * 0.33 == 165 and 165 + 45 == 210
P.append(Q("pct-q08", "In an examination, a candidate scoring 33% marks fails by 45 marks, while another candidate scoring 45% marks gets 15 marks more than the pass marks. What are the maximum marks?",
  ["400", "450", "500", "600"], 2, 500,
  md(r"Pass mark from candidate 1: $0.33M + 45$; from candidate 2: $0.45M - 15$.",
     r"$0.33M + 45 = 0.45M - 15$ ⇒ $0.12M = 60$ ⇒ $M = 500$.",
     r"Pass mark $= 165 + 45 = 210$."),
  "(45 − 33)% of M = 45 + 15 = 60 ⇒ M = 500.",
  "medium", "pct-marks-income", "pass marks two candidates", 55))

v = F(100 * 20, 120)
assert v == F(50, 3)
P.append(Q("pct-q09", "A's income is 20% more than B's income. B's income is less than A's income by:",
  ["20%", "$16\\frac{2}{3}$%", "$18\\frac{1}{4}$%", "15%"], 1, v,
  md("Let B = 100, then A = 120.",
     r"B is short of A by 20 on base 120 ⇒ $\frac{20}{120} \times 100 = 16\frac{2}{3}\%$."),
  r"Flip: $\frac{100 \times 20}{120} = 16\frac{2}{3}\%$.",
  "medium", "pct-more-less", "more-less flip", 30))

assert F(108, 120) == F(9, 10)
P.append(Q("pct-q10", "The price of rice increases by 20%. By what per cent must a family reduce its consumption so that the expenditure on rice increases by only 8%?",
  ["8%", "10%", "12%", "15%"], 1, 10,
  md(r"Consumption factor $= \frac{\text{expenditure factor}}{\text{price factor}} = \frac{108}{120} = \frac{9}{10}$.",
     "So consumption must be cut by **10%**."),
  "1.08 ÷ 1.20 = 0.90 ⇒ reduce 10%. (20% is the trap from the standard 'same expenditure' rule.)",
  "medium", "pct-marks-income", "price vs consumption", 40))

assert F(4, 3) - 1 == F(1, 3)
P.append(Q("pct-q11", "If the numerator of a fraction is increased by 20% and the denominator is decreased by 10%, the fraction becomes:",
  ["increased by 10%", "increased by 30%", "increased by $33\\frac{1}{3}$%", "decreased by 8%"], 2, F(100, 3),
  md(r"New fraction factor $= \frac{120}{100} \div \frac{90}{100} = \frac{4}{3}$.",
     r"Increase $= \frac{1}{3} = 33\frac{1}{3}\%$."),
  "Numerator chip 6/5, denominator chip 9/10 ⇒ net 4/3 ⇒ +33⅓%.",
  "medium", "pct-change", "fraction numerator-denominator change", 40,
  vals=[10, 30, F(100, 3), -8]))

i, e = 115, 88
assert i - e == 27 and F(7, 20) * 100 == 35
P.append(Q("pct-q12", "A man spends 80% of his income. His income increases by 15% and his expenditure increases by 10%. The percentage increase in his savings is:",
  ["25%", "30%", "35%", "40%"], 2, 35,
  md("Take income = 100 ⇒ expenditure = 80, savings = 20.",
     "New income = 115, new expenditure = 88 ⇒ new savings = 27.",
     r"Increase $= \frac{7}{20} \times 100 = 35\%$."),
  "Track the three quantities on income = 100. Savings go 20 → 27 = +35%.",
  "medium", "pct-marks-income", "savings change", 50))

assert F(40, 100) * F(25, 100) == F(10, 100)
P.append(Q("pct-q13", "A's salary is 40% of B's salary and B's salary is 25% of C's salary. A's salary is what per cent of C's salary?",
  ["10%", "15%", "20%", "25%"], 0, 10,
  md(r"$A = \frac{40}{100} \times \frac{25}{100} \times C = \frac{10}{100}C$ ⇒ 10%."),
  "Chain fractions: 2/5 × 1/4 = 1/10 = 10%.",
  "medium", "pct-more-less", "percentage chain", 35))

x = 40000
for r in (120, 125, 110):
    x = x * r / 100
assert x == 66000
P.append(Q("pct-q14", "The population of a village increased by 20% in the first year, by 25% in the second year and by 10% in the third year. If the present population is 66,000, what was it 3 years ago?",
  ["36,000", "40,000", "44,000", "45,000"], 1, 40000,
  md(r"$P \times \frac{120}{100} \times \frac{125}{100} \times \frac{110}{100} = 66000$",
     r"$P \times \frac{33}{20} = 66000$ ⇒ $P = 40000$."),
  r"Chips: $\frac{6}{5} \times \frac{5}{4} = \frac{3}{2}$, then $\times \frac{11}{10} = \frac{33}{20}$. $66000 \times \frac{20}{33} = 40000$.",
  "hard", "pct-population-election", "population reverse three rates", 60))

assert 400 * F(20, 100) == 80 and 80 / 5 == 16 and 16 * 100 / 80 == 20
P.append(Q("pct-q15", "A reduction of 20% in the price of sugar enables a person to buy 5 kg more sugar for ₹400. The original price of sugar per kg is:",
  ["₹16", "₹18", "₹20", "₹25"], 2, 20,
  md("Money saved due to the cut = 20% of ₹400 = ₹80.",
     "This ₹80 buys the extra 5 kg at the reduced price ⇒ reduced price = ₹16/kg.",
     "Original price = ₹$16 \\times \\frac{100}{80}$ = ₹20 per kg."),
  "r% of outlay ÷ extra kg = reduced price (80/5 = 16); original = reduced ÷ 0.8 = 20.",
  "hard", "pct-marks-income", "price cut extra quantity", 60))

topic = {
 "id": "percentage", "sectionId": "quant", "title": "Percentage", "order": 4,
 "importance": "high", "avgQuestions": {"tier1": 2, "tier2": 3},
 "summary": "The language of the whole arithmetic section — profit-loss, interest, discount and DI are all percentage questions in disguise. Tier 1 asks 1–2 direct questions per shift (successive change, more/less flips, election and population problems) and Tier 2 leans on it heavily.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
