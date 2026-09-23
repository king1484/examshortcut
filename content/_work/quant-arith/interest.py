from _lib import *
from fractions import Fraction as Fr

# ------------------------------------------------------------------ checks
assert 5000 * 8 * 3 // 100 == 1200
assert 100 * 100 / (100 * 10) == 10  # doubling at SI in 10 yrs -> 10%
assert 10000 * F(121, 100) - 10000 == 2100
assert 100 * 900 / (5 * 3) == 6000
assert 100 * 360 / (1200 * 3) == 10
assert 8000 * F(15, 2) * 4 // 100 == 2400
assert 12500 * F(12544, 10000) - 12500 == 3180 and F(112, 100)**2 == F(12544, 10000)
assert 16000 * F(105, 100)**3 == 18522 and 18522 - 16000 == 2522
assert 100 * (3 - 1) / 8 == 25  # 3x in 8 yrs at SI -> 25%
assert 100 * 4840 / 121 == 4000
assert F(121, 100) == F(11, 10)**2
# CI-SI 2yr diff
assert F(50, 1) * 10000 == 5000 * 100  # 0.01 * P = 50 -> P = 5000
assert 5000 * F(1, 100)**2 * 100 == 50
assert 1331 * 1000 // 1331 == 1000 and F(1331, 1000) == F(11, 10)**3
# half-yearly 8000 20% 1.5y
assert 8000 * F(11, 10)**3 == 10648 and 10648 - 8000 == 2648
# 1.44x in 2 yrs CI -> 20%
import sympy as sp
r = sp.symbols("r", positive=True)
sol = sp.solve(sp.Eq((100 + r)**2, 14400), r)
assert sol == [20]
# SI = 2/5 of P at 4% -> T
assert F(100 * 2, 5 * 4) == 10
# different yearly rates
assert 5000 * Fr(108, 100) * Fr(110, 100) == 5940 and 5940 - 5000 == 940
# CI & SI given -> rate 8%, P 5000
Pr = sp.symbols("P r", positive=True)
sol = sp.solve([sp.Eq(Pr[0] * Pr[1] * 2 / 100, 800), sp.Eq(Pr[0] * (Pr[1] / 100)**2, 32)], [Pr[0], Pr[1]], dict=True)
assert any(s[Pr[1]] == 8 and s[Pr[0]] == 5000 for s in sol)
# doubling at CI in 8 yrs -> 8x in 24 yrs
# instalment CI: 1050 at 10%, two equal annual payments of 605
d1 = 1050 * Fr(11, 10) - 605
d2 = d1 * Fr(11, 10) - 605
assert d1 == 550 and d2 == 0
assert Fr(21, 10) * 605 / Fr(121, 100) == 1050 or 1050 == (605 * Fr(11, 10) + 605) / Fr(121, 100)
# 3-year instalment: 3310 at 10% -> 1331
d1 = 3310 * Fr(11, 10) - 1331
d2 = d1 * Fr(11, 10) - 1331
d3 = d2 * Fr(11, 10) - 1331
assert d1 == 2310 and d2 == 1210 and d3 == 0

subtopics = [
 sub("int-si", "Simple Interest",
  md(r"In simple interest the interest every year is a fixed slice of the original principal only.",
     "",
     r"$$SI = \frac{P \times R \times T}{100}, \qquad A = P + SI$$",
     "",
     "Any one of P, R, T, SI can be recovered from the other three. Amount-based questions: first get SI = A − P.",
     "",
     r"**Growth is linear** at SI: the amount grows by the same rupee amount every year. If a sum becomes n times in T years, the rate is $\frac{100(n-1)}{T}$.",
     "",
     "**Instalment intuition at SI:** the borrower pays interest only for the period each part of the money actually stayed with the lender."),
  [formula("Simple interest", r"SI = \frac{PRT}{100}"),
   formula("Amount", r"A = P + SI = P\left(1 + \frac{RT}{100}\right)"),
   formula("Recovering inputs", r"P = \frac{100\,SI}{RT},\quad R = \frac{100\,SI}{PT},\quad T = \frac{100\,SI}{PR}"),
   formula("n-times in T years", r"R = \frac{100(n-1)}{T}"),
   formula("Equal yearly interest", r"SI_{\text{per year}} = \frac{SI_{\text{total}}}{T}")],
  [trick("Flip the formula, don't solve equations",
         "Write SI = PRT/100 and cover the unknown — that IS the equation.",
         "Find the simple interest on ₹5,000 at 8% p.a. for 3 years.",
         "SI = 5000 × 8 × 3/100 = **₹1,200**."),
   trick("n-times ⇄ rate at SI",
         "'Becomes n times in T years' means interest earned = (n−1)P.",
         "At what rate per cent per annum will a sum of money double itself in 10 years at simple interest?",
         r"$R = \frac{100(2-1)}{10} = 10\%$ p.a."),
   trick("SI per year is constant",
         "Divide the total interest by the number of years; everything else follows.",
         r"The simple interest on a sum at 4% p.a. is $\frac{2}{5}$ of the principal. Find the time.",
         r"$\frac{PRT}{100} = \frac{2P}{5}$ ⇒ $T = \frac{100 \times 2}{5 \times 4} = 10$ years.")],
  ["Using the amount A as principal in the SI formula (SI is always on the original P).",
   r"For 'becomes n times', using n instead of n − 1 in the interest.",
   "Forgetting to convert months to years ($T = 9/12$) or paise-paise rate mix-ups.",
   "Adding SI of different sums without weighting by their time periods."]),

 sub("int-ci", "Compound Interest",
  md(r"Compound interest adds each year's interest to the principal — the amount grows **geometrically**.",
     "",
     r"$$A = P\left(1 + \frac{R}{100}\right)^T, \qquad CI = A - P$$",
     "",
     r"**Effective multipliers:** 10% → ×11/10, 20% → ×6/5, 4% → ×26/25. Chain the multipliers instead of using the formula blindly.",
     "",
     r"**Different rate each year** (or gain then loss): multiply the year-wise factors: $A = P\left(1+\frac{r_1}{100}\right)\left(1+\frac{r_2}{100}\right)\cdots$",
     "",
     r"**Fraction rates** become easy through approximations: $6\tfrac{2}{3}\% = \frac{1}{15}$, so 2 years at CI multiplies the money by $\frac{16}{15} \times \frac{16}{15}$."),
  [formula("Compound amount", r"A = P\left(1 + \frac{R}{100}\right)^T"),
   formula("Compound interest", r"CI = P\left[\left(1 + \frac{R}{100}\right)^T - 1\right]"),
   formula("Year-wise multipliers", r"A = P \times \frac{100 + r_1}{100} \times \frac{100 + r_2}{100} \times \cdots"),
   formula("Half-yearly compounding", r"A = P\left(1 + \frac{R}{200}\right)^{2T}", "rate halves, periods double"),
   formula("Quarterly compounding", r"A = P\left(1 + \frac{R}{400}\right)^{4T}")],
  [trick("Multiplier chips",
         "One chip per year; multiply. For fraction rates pick chips that cancel.",
         r"Find the amount on ₹10,000 at 10% p.a. compound interest for 2 years.",
         r"$10000 \times \frac{11}{10} \times \frac{11}{10} = 12100$, so CI = ₹2,100."),
   trick("Recover P by dividing the chip",
         "If the amount after T years is known, divide by the chip chain to get the principal.",
         "A sum amounts to ₹4,840 in 2 years at 10% p.a. CI. Find the sum.",
         r"$P = 4840 \times \frac{10}{11} \times \frac{10}{11} = 4000$, i.e. ₹4,000."),
   trick("Half-yearly: halve the rate, double the count",
         "Convert the problem, then run the chips.",
         r"Find the CI on ₹8,000 at 20% p.a. for 1$\frac{1}{2}$ years, compounded half-yearly.",
         r"3 half-years at 10%: $8000 \times (1.1)^3 = 10648$ ⇒ CI = ₹2,648.")],
  [r"Compounding $\left(1 + \frac{R}{100}\right)^T$ when the rates differ year to year — multiply factors instead.",
   "For half-yearly compounding, halving the time instead of the rate.",
   "Reporting the amount A when the question asks for CI (or the reverse).",
   r"Using $\frac{R}{200}$ but forgetting the exponent $2T$ (or vice versa)."]),

 sub("int-ci-si-diff", "CI vs SI: differences & doubling",
  md(r"The extra money CI earns over SI comes from **interest on interest**:",
     "",
     r"- 2 years: $CI - SI = P\left(\dfrac{R}{100}\right)^2$ — the first year's interest, again at rate R, for one year.",
     r"- 3 years: $CI - SI = P\left(\dfrac{R}{100}\right)^2\left(3 + \dfrac{R}{100}\right)$.",
     "",
     r"**Doubling time at CI:** rate ≈ $\frac{72}{T}$ (rule of 72); exactly, $T = \log 2 \,/\, \log(1 + r/100)$.",
     "",
     r"**Doubling/tripling chains:** if a sum doubles in T years at CI it becomes $2^k$ times in $kT$ years (4× in 2T, 8× in 3T). Same logic at SI: extra multiples need the same *linear* pace — n times in T ⇒ (n′ − 1) = (n − 1)·T′/T."),
  [formula("2-year difference", r"CI - SI = P\left(\frac{R}{100}\right)^2"),
   formula("3-year difference", r"CI - SI = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)"),
   formula("CI doubling chain", r"2\times \text{ in } T \Rightarrow 2^k\times \text{ in } kT"),
   formula("SI multiple pace", r"n\times \text{ in } T \Rightarrow n'\times \text{ in } T',\ (n'-1) = (n-1)\frac{T'}{T}"),
   formula("SI and CI both given", r"P\left(\frac{R}{100}\right)^2 = CI_2 - SI_2")],
  [trick("The P r²/10000 gap",
         "For 2 years, the SI–CI difference alone fixes the product structure: two equations, two unknowns.",
         "The simple interest on a sum for 2 years is ₹800 and the compound interest is ₹832. Find the rate.",
         r"Gap $= 32 = P\left(\frac{R}{100}\right)^2$; also $SI = \frac{PR \times 2}{100} = 800$ ⇒ $PR = 40000$. Then $\frac{R \times 40000}{10000} = 32$ ⇒ $R = 8\%$, $P = 5000$."),
   trick("Doubling chain at CI",
         "Every T years the money multiplies by the same factor — count the doublings.",
         "A sum doubles in 8 years at CI. In how many years will it become 8 times?",
         r"$8 = 2^3$ ⇒ $3 \times 8 = 24$ years."),
   trick("Difference as first-year interest re-lent",
         r"For 2 years, think: $CI - SI$ = (1st year interest) × (R/100).",
         "The CI–SI difference on a sum for 2 years at 10% is ₹50. Find the sum.",
         r"$P \times 0.1^2 = 50$ ⇒ $P = 5000$, i.e. ₹5,000.")],
  [r"Using $P\left(\frac{R}{100}\right)^2$ for 3 years without the $\left(3 + \frac{R}{100}\right)$ factor.",
   "Applying the CI doubling chain to SI problems (SI doubles in T ⇒ 4× in 2T is FALSE at SI; it is 3×).",
   "Forgetting to compute SI from the given amounts before using the difference.",
   "Mixing up which of CI/SI is larger — CI is always ≥ SI for T ≥ 1."]),

 sub("int-instalments", "Equal annual instalments",
  md("A loan at interest is cleared by equal instalments at the end of each year. Two clean methods:",
     "",
     "**Tabular (works for both SI and CI):** grow the outstanding debt by one year's interest, subtract the instalment, repeat. The last row must reach zero.",
     "",
     r"**Present value (CI):** with instalment x and rate r, $P = \dfrac{x}{1+\frac{r}{100}} + \dfrac{x}{(1+\frac{r}{100})^2} + \cdots + \dfrac{x}{(1+\frac{r}{100})^n}$.",
     "",
     r"**Simple-interest shortcut:** $P = nx - \frac{x\,r}{100}\cdot\frac{n(n-1)}{2}$ (each instalment saved earns interest for the years it was NOT outstanding).",
     "",
     "CGL numbers are chosen so the tabular method runs on small fractions — do it year by year."),
  [formula("Present value (CI)", r"P = \sum_{k=1}^{n} \frac{x}{\left(1 + \frac{r}{100}\right)^k}"),
   formula("Simple interest instalment", r"P = nx - \frac{x\,r}{100} \cdot \frac{n(n-1)}{2}"),
   formula("Tabular step", r"\text{debt}_{k+1} = \text{debt}_k\left(1 + \frac{r}{100}\right) - x")],
  [trick("Tabular year-by-year",
         "Grow, subtract, repeat. Two or three rows finish the question.",
         "A man borrows ₹1,050 at 10% p.a. compound interest and repays it in two equal annual instalments. Find each instalment.",
         "Year 1: 1050 → 1155; pay x → 1155 − x. Year 2: (1155 − x) × 1.1 = x ⇒ 1270.5 = 2.1x ⇒ x = **605**."),
   trick("Present-value fraction add",
         r"Discount each instalment by $\left(1+\frac{r}{100}\right)^{-k}$ and add.",
         r"$P = \frac{x}{1.1} + \frac{x}{1.21}$ ⇒ x in one line for 2-year cases.",
         r"For P = 1050, r = 10%: $\frac{1.1x + x}{1.21} = 1050$ ⇒ $x = 605$."),
   trick("SI instalment formula",
         r"Use $P = nx - \frac{xr}{100} \cdot \frac{n(n-1)}{2}$ directly for simple-interest loans.",
         "₹1,950 is repaid in two equal annual instalments at 5% per annum simple interest. Find each instalment.",
         r"$1950 = 2x - \frac{x \times 5}{100} \times 1 = 1.95x$ ⇒ $x = 1000$, i.e. ₹1,000.")],
  [r"Adding a full year's interest on money already repaid (use the outstanding balance, not the original P).",
   "Counting n instalments but compounding only n − 1 times (or the reverse).",
   r"In the SI formula, taking $\frac{n(n+1)}{2}$ instead of $\frac{n(n-1)}{2}$.",
   "Forgetting the final row must hit exactly zero — always verify the tabular closure."]),

 sub("int-rate-time-cases", "Finding P, R, T from amount data",
  md("The reverse-direction questions give you amounts and ask for the input:",
     "",
     r"- Amount at CI after T years ⇒ $P = \dfrac{A}{\left(1+\frac{r}{100}\right)^T}$ — divide by the chip chain.",
     r"- Amounts after consecutive years at CI give the yearly factor: $\frac{A_{t+1}}{A_t} = 1 + \frac{r}{100}$.",
     r"- At SI, consecutive-year amounts differ by the SAME rupee interest — the difference of two consecutive amounts IS the yearly SI, and $\frac{\text{yearly SI}}{P} \times 100$ = rate.",
     "- Two equations (2-year and 3-year amounts) solve for P and R simultaneously."),
  [formula("Principal from amount", r"P = \frac{A}{\left(1 + \frac{r}{100}\right)^T}"),
   formula("Rate from consecutive amounts", r"1 + \frac{r}{100} = \frac{A_{t+1}}{A_t} \quad (\text{CI})"),
   formula("Yearly SI from amounts", r"SI_{\text{year}} = A_{t+1} - A_t \quad (\text{SI})"),
   formula("Two-amount system", r"\frac{A_2}{A_1} = 1 + \frac{r}{100} \Rightarrow P = \frac{A_1}{1 + r/100}")],
  [trick("Consecutive amounts → rate → principal",
         "The ratio of consecutive CI amounts exposes the rate chip; divide once more for P.",
         "A sum amounts to ₹1,331 in 3 years at 10% p.a. CI. Find the sum.",
         r"$P = 1331 \times \frac{10}{11} \times \frac{10}{11} \times \frac{10}{11} = 1000$, i.e. ₹1,000."),
   trick("SI: equal yearly steps",
         "Check the amounts differ by a constant — that constant is the yearly interest.",
         "A sum amounts to ₹6,000 in 2 years and ₹6,750 in 3 years at SI. Find the rate if P = ₹4,500.",
         "Yearly SI = 6750 − 6000 = 750 ⇒ 2 years' SI = 1500 ⇒ P = 4500, R = 100×750/4500 = 16⅔% p.a."),
   trick("Two amounts, two unknowns",
         "Divide the equations: the ratio kills P and gives the chip.",
         "A sum amounts to ₹4,840 in 2 years and ₹5,324 in 3 years at CI. Find the rate.",
         r"$\frac{5324}{4840} = 1.1$ ⇒ $r = 10\%$.")],
  ["Using T years of SI data in a CI formula (check: SI amounts grow additively).",
   "For consecutive amounts, subtracting when you must divide (CI) or dividing when you must subtract (SI).",
   "Answering the rate as the chip (1.1) instead of 10%.",
   "In two-amount problems, forgetting to verify P comes out positive and sensible."]),
]

pyq = [
 pat("SI: find P / R / T / interest", "very common",
     "Direct SI = PRT/100 recall with one quantity missing, often disguised as 'amounts to ₹…'.",
     "Convert amount to SI (SI = A − P), then flip the formula. n-times-in-T-years ⇒ R = 100(n−1)/T."),
 pat("Amount at CI (P, A, R or T unknown)", "very common",
     "A = P(1 + r/100)^T with one blank; clean chips like 11/10 or 6/5 are the norm.",
     "Run or reverse the multiplier chips. Consecutive-year amounts: their ratio IS the chip."),
 pat("CI − SI difference for 2 or 3 years", "very common",
     "'The difference between CI and SI for 2 years at 10% is ₹50' — find P, R, or the difference itself.",
     r"2 years: $P(R/100)^2$. 3 years: $P(R/100)^2(3 + R/100)$. With CI and SI both given, the gap and the SI together pin down P and R."),
 pat("Half-yearly / quarterly compounding", "common",
     "'Compounded half-yearly/quarterly' appears in the question — the trap is mechanical.",
     "Halve (or quarter) the rate and double (quadruple) the number of periods, then run chips."),
 pat("Doubling / tripling time", "common",
     "'A sum doubles in 8 years; when 8 times?' (CI) or the SI version.",
     "CI: powers of 2 chain (kT years for 2^k). SI: linear — 8× needs 7 units of the doubling interest."),
 pat("Equal annual instalments", "common",
     "Loan cleared in equal yearly payments at SI or CI; find the instalment or the loan.",
     "Tabular grow-and-subtract for small cases; present-value sum for CI; the n·x − x·r·n(n−1)/200 formula for SI."),
 pat("Different rates in different years", "occasional",
     "'8% in the first year, 10% in the second…' — one sum, year-wise rates.",
     "Multiply the year chips: (1.08)(1.10). Never average the rates."),
 pat("CI and SI both given, find sum and rate", "common",
     "'SI for 2 years is ₹800, CI for 2 years is ₹832' — find P and R.",
     "Gap = P(R/100)² and SI = PR·2/100: divide the equations to get R first, then P."),
]

solved = []

assert 8000 * F(15, 2) * 4 // 100 == 2400
solved.append(Q("int-s01", "Find the simple interest on ₹8,000 at 7.5% per annum for 4 years.",
  ["₹2,200", "₹2,400", "₹2,600", "₹2,800"], 1, 2400,
  md(r"$SI = \frac{8000 \times 7.5 \times 4}{100} = 80 \times 30 = 2400$, i.e. ₹2,400."),
  "7.5% for 4 years = 30% of the principal = 0.3 × 8000 = ₹2,400.",
  "easy", "int-si", "direct SI", 25))

assert 12500 * F(12544, 10000) - 12500 == 3180
solved.append(Q("int-s02", "Find the compound interest on ₹12,500 at 12% per annum for 2 years.",
  ["₹3,000", "₹3,120", "₹3,180", "₹3,240"], 2, 3180,
  md(r"$A = 12500\left(1 + \frac{12}{100}\right)^2 = 12500 \times \frac{28}{25} \times \frac{28}{25} = 12500 \times 1.2544$",
     "= ₹15,680 ⇒ CI = ₹3,180."),
  "20% would give exactly 2 × 2500 = 5000... for 12% use chips: 12500 × 28/25 = 14000, × 28/25 = 15,680 ⇒ CI 3,180.",
  "medium", "int-ci", "direct CI", 40))

assert 16000 * F(105, 100)**3 == 18522
solved.append(Q("int-s03", r"Find the compound interest on ₹16,000 at 10% per annum for 1$\frac{1}{2}$ years, interest compounded half-yearly.",
  ["₹2,400", "₹2,448", "₹2,522", "₹2,560"], 2, 2522,
  md(r"Half-yearly: rate 5% per half-year, periods = 3.",
     r"$A = 16000 \times (1.05)^3 = 16000 \times \frac{9261}{8000} = 18522$.",
     "CI = 18,522 − 16,000 = **₹2,522**."),
  "3 chips of 21/20: 16000 × 21/20 = 16,800; × 21/20 = 17,640; × 21/20 = 18,522.",
  "medium", "int-ci", "half-yearly compounding", 50))

assert 100 * 2 / 8 == 25
solved.append(Q("int-s04", "A sum of money becomes three times itself in 8 years at simple interest. The rate of interest per annum is:",
  ["20%", "25%", "30%", "33.33%"], 1, 25,
  md(r"Becoming 3 times means interest earned = 2P.",
     r"$\frac{P \times R \times 8}{100} = 2P$ ⇒ $R = \frac{200}{8} = 25\%$ p.a."),
  r"At SI: R = 100(n − 1)/T = 100 × 2/8 = 25%.",
  "easy", "int-si", "n-times rate", 25))

d1 = 3310 * Fr(11, 10) - 1331
assert d1 == 2310 and d1 * Fr(11, 10) - 1331 == 1210 and 1210 * Fr(11, 10) - 1331 == 0
solved.append(Q("int-s05", "A man borrows ₹3,310 at 10% per annum compound interest and repays the loan in three equal annual instalments at the end of each year. Find the value of each instalment.",
  ["₹1,210", "₹1,331", "₹1,364", "₹1,464"], 1, 1331,
  md(r"Tabular method: debt grows 10% each year, then x is paid.",
     "Year 1: 3310 × 1.1 = 3641 → pay x → 3641 − x.",
     "Year 2: (3641 − x) × 1.1 = 4005.1 − 1.1x → pay x → 4005.1 − 2.1x.",
     "Year 3: (4005.1 − 2.1x) × 1.1 = 4405.61 − 2.31x = x ⇒ 3.31x = 4405.61 ⇒ x = 1,331.",
     "Check: 3310 → 3641 − 1331 = 2310 → 2541 − 1331 = 1210 → 1331 − 1331 = 0 ✓."),
  "Present values: P = x(1/1.1 + 1/1.21 + 1/1.331) = 3.31x/1.331 = 3310 ⇒ x = 1331. (The chip 11/10³ = 1331/1000 signals the design.)",
  "hard", "int-instalments", "three-year CI instalment", 80))

# ------------------------------------------------------------------ practice
P = []

assert 5000 * 8 * 3 // 100 == 1200
P.append(Q("int-q01", "What is the simple interest on ₹5,000 at 8% per annum for 3 years?",
  ["₹1,000", "₹1,200", "₹1,400", "₹1,500"], 1, 1200,
  md(r"$SI = \frac{5000 \times 8 \times 3}{100} = 1200$, i.e. ₹1,200."),
  "8% × 3 = 24% of 5,000 = ₹1,200.",
  "easy", "int-si", "direct SI", 20))

assert 100 * 900 / 15 == 6000
P.append(Q("int-q02", "The simple interest on a certain sum at 5% per annum for 3 years is ₹900. The sum is:",
  ["₹5,400", "₹6,000", "₹6,500", "₹7,200"], 1, 6000,
  md(r"$P = \frac{100 \times SI}{R \times T} = \frac{100 \times 900}{15} = 6000$, i.e. ₹6,000."),
  "Total interest % = 15 ⇒ P = 900/0.15 = ₹6,000.",
  "easy", "int-si", "find principal SI", 25))

assert 100 * 360 / 3600 == 10
P.append(Q("int-q03", "At what rate of simple interest per annum will ₹1,200 amount to ₹1,560 in 3 years?",
  ["8%", "9%", "10%", "12%"], 2, 10,
  md(r"SI $= 1560 - 1200 = 360$.",
     r"$R = \frac{100 \times 360}{1200 \times 3} = 10\%$."),
  "Interest = ₹360 over 3 years = ₹120/yr = 10% of 1,200.",
  "easy", "int-si", "find rate SI", 25))

assert 10000 * F(121, 100) - 10000 == 2100
P.append(Q("int-q04", "The compound interest on ₹10,000 at 10% per annum for 2 years is:",
  ["₹2,000", "₹2,100", "₹2,200", "₹2,310"], 1, 2100,
  md(r"$A = 10000 \times 1.1 \times 1.1 = 12100$, so CI $= 2100$, i.e. ₹2,100."),
  "Chips 11/10 × 11/10; or SI 2000 + interest-on-interest 10% of 2000 = 2100.",
  "easy", "int-ci", "direct CI", 30))

assert 100 * 100 / 1000 == 10
P.append(Q("int-q05", "A sum of money doubles itself in 10 years at simple interest. The rate of interest per annum is:",
  ["8%", "10%", "12%", "12.5%"], 1, 10,
  md(r"Doubling ⇒ interest = P. $\frac{P \times R \times 10}{100} = P$ ⇒ $R = 10\%$."),
  "R = 100(n−1)/T = 100/10 = 10%.",
  "easy", "int-si", "doubling at SI", 20))

assert F(50, 10000) * 10000 == 50
P.append(Q("int-q06", "The difference between the compound interest and the simple interest on a sum for 2 years at 10% per annum is ₹50. The sum is:",
  ["₹4,000", "₹5,000", "₹6,000", "₹8,000"], 1, 5000,
  md(r"$CI - SI = P\left(\frac{10}{100}\right)^2 = \frac{P}{100} = 50$ ⇒ $P = 5000$, i.e. ₹5,000."),
  "Gap = P × r²/10000 ⇒ P = 50 × 10000/100 = ₹5,000.",
  "medium", "int-ci-si-diff", "CI-SI difference 2 years", 30))

assert 100 * 4840 / 121 == 4000
P.append(Q("int-q07", "A sum amounts to ₹4,840 in 2 years at 10% per annum compound interest. The sum is:",
  ["₹4,000", "₹4,200", "₹4,400", "₹4,600"], 0, 4000,
  md(r"$P = \frac{4840}{(1.1)^2} = \frac{4840}{1.21} = 4000$, i.e. ₹4,000."),
  "Divide by the chip chain: 4840 × 10/11 = 4,400; × 10/11 = 4,000.",
  "medium", "int-rate-time-cases", "principal from CI amount", 30))

assert 8000 * F(11, 10)**3 == 10648
P.append(Q("int-q08", r"Find the compound interest on ₹8,000 at 20% per annum for 1$\frac{1}{2}$ years, compounded half-yearly.",
  ["₹2,448", "₹2,520", "₹2,648", "₹2,800"], 2, 2648,
  md(r"Rate per half-year = 10%; periods = 3.",
     r"$A = 8000 \times (1.1)^3 = 10648$, so CI = ₹2,648."),
  "Three chips of 11/10: 8000 → 8800 → 9680 → 10,648.",
  "medium", "int-ci", "half-yearly compounding", 40))

sol = sp.solve(sp.Eq((100 + r)**2, 14400), r)
assert sol == [20]
P.append(Q("int-q09", "A sum of money becomes 1.44 times itself in 2 years when invested at compound interest. The annual rate of interest is:",
  ["12%", "14.4%", "20%", "22%"], 2, 20,
  md(r"$\left(1 + \frac{R}{100}\right)^2 = 1.44$ ⇒ $1 + \frac{R}{100} = 1.2$ ⇒ $R = 20\%$."),
  "√1.44 = 1.2 ⇒ rate 20%. (14.4% is the trap for linear thinking.)",
  "medium", "int-ci-si-diff", "rate from multiplier", 30))

assert F(100 * 2, 5 * 4) == 10
P.append(Q("int-q10", r"The simple interest on a sum at 4% per annum is $\frac{2}{5}$ of the sum. The number of years for which the sum is invested is:",
  ["8", "10", "12", "15"], 1, 10,
  md(r"$\frac{P \times 4 \times T}{100} = \frac{2P}{5}$ ⇒ $T = \frac{100 \times 2}{4 \times 5} = 10$ years."),
  "4% per year ⇒ 2/5 = 40% needs 40/4 = 10 years.",
  "medium", "int-si", "fraction of principal", 30))

assert 5000 * Fr(108, 100) * Fr(110, 100) == 5940
P.append(Q("int-q11", "A man invests ₹5,000 for two years. The rate of interest is 8% for the first year and 10% for the second year, compounded annually. The amount at the end of two years is:",
  ["₹5,900", "₹5,940", "₹5,980", "₹6,000"], 1, 5940,
  md(r"$A = 5000 \times 1.08 \times 1.10 = 5940$."),
  "Chips: 5000 × 27/25 = 5,400; × 11/10 = ₹5,940. (Never average 8% and 10%.)",
  "medium", "int-ci", "different yearly rates", 35))

d1 = 1050 * Fr(11, 10) - 605
assert d1 == 550 and d1 * Fr(11, 10) - 605 == 0
P.append(Q("int-q12", "A man borrows ₹1,050 at 10% per annum compound interest and agrees to repay it in two equal annual instalments. Each instalment is:",
  ["₹550", "₹578", "₹605", "₹630"], 2, 605,
  md(r"Year 1: $1050 \times 1.1 = 1155$; pay x → $1155 - x$.",
     r"Year 2: $1.1(1155 - x) = x$ ⇒ $1270.5 = 2.1x$ ⇒ $x = 605$."),
  "Present values: 1050 = x/1.1 + x/1.21 = 2.1x/1.21 ⇒ x = 605.",
  "hard", "int-instalments", "two-year CI instalment", 60))

assert F(32 * 10000, 40000) == 8
P.append(Q("int-q13", "The simple interest on a certain sum for 2 years is ₹800 and the compound interest for the same period is ₹832. The rate of interest per annum is:",
  ["6%", "7%", "8%", "10%"], 2, 8,
  md(r"Gap $= 32 = P\left(\frac{R}{100}\right)^2$ and $\frac{PR \times 2}{100} = 800$ ⇒ $PR = 40000$.",
     r"$\frac{R \times 40000}{10000} = 32$ ⇒ $R = 8\%$ (and P = ₹5,000)."),
  "Ratio trick: gap/SI = R/200 ⇒ 32/800 = R/200 ⇒ R = 8%.",
  "hard", "int-ci-si-diff", "CI and SI both given", 55))

assert 8 * 3 == 24
P.append(Q("int-q14", "A sum of money invested at compound interest doubles itself in 8 years. In how many years will it become 8 times itself?",
  ["16 years", "20 years", "24 years", "27 years"], 2, 24,
  md(r"$8 = 2^3$: three doublings ⇒ $3 \times 8 = 24$ years."),
  "Doubling chain at CI: 2× in 8 yrs ⇒ 4× in 16 ⇒ 8× in 24.",
  "medium", "int-ci-si-diff", "doubling chain CI", 30))

assert F(100 * 750, 4500) == F(50, 3)
P.append(Q("int-q15", "A sum amounts to ₹6,000 in 2 years and ₹6,750 in 3 years at simple interest. The rate of interest per annum is:",
  ["12%", "15%", "$16\\frac{2}{3}$%", "18%"], 2, F(50, 3),
  md("Yearly SI = 6750 − 6000 = ₹750 (same every year).",
     r"Two years' SI $= 1500$ ⇒ principal $= 6000 - 1500 = 4500$.",
     r"$R = \frac{100 \times 750}{4500} = 16\frac{2}{3}\%$ p.a."),
  "SI amounts step up by the same ₹750 yearly; P = 4,500, R = 750/4500 = 16⅔%.",
  "hard", "int-rate-time-cases", "consecutive SI amounts", 50))

topic = {
 "id": "interest", "sectionId": "quant", "title": "Interest (SI & CI)", "order": 7,
 "importance": "high", "avgQuestions": {"tier1": 1, "tier2": 2},
 "summary": "Simple and compound interest — a near-certain slot in every shift. Tier 1 favourites: direct SI, amount at CI with clean chips, CI–SI differences and doubling chains. Tier 2 adds instalments and multi-year rate cases. Everything runs on the multiplier-chip habit.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
