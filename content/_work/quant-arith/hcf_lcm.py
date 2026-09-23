from _lib import *
from math import gcd
from functools import reduce
import sympy as sp

def hcf(*ns):
    return reduce(gcd, ns)

def lcm(*ns):
    return reduce(lambda a, b: a * b // gcd(a, b), ns)

# ------------------------------------------------------------------ trick example checks
assert hcf(84, 70) == 14 and 85 % 14 == 1 and 72 % 14 == 2
assert hcf(54, 180, 720) == 18
assert 145 * 2175 // 725 == 435 and hcf(725, 435) == 145 and lcm(725, 435) == 2175
assert hcf(1517, 902) == 41 and (1517 * 902) // (41 * 41) == 814
assert lcm(12, 15, 20) == 60
assert hcf(96, 404) == 4 and 96 * 404 // 4 == 9696
assert F(2, 27) == F(hcf(2, 8, 10), lcm(3, 9, 27))
assert 60 * 72 // 12 == 360 and hcf(60, 72) == 12
assert lcm(9, 12, 15) == 180
assert hcf(825, 675, 450) == 75
assert lcm(15, 20, 25) == 300 and 9999 % 300 == 99 and 9999 - 99 == 9900
assert lcm(12, 15, 20, 27) == 540 and 545 % 12 == 545 % 15 == 545 % 20 == 545 % 27 == 5
assert 29 * 15 * 13 == 5655
assert 4537 % 13 == 0 and all(4537 % d == 1 for d in (6, 7, 8, 9, 12)) and lcm(6, 7, 8, 9, 12) == 504
assert (504 * 9 + 1) == 4537 and 504 % 13 == -3 % 13
assert 2028 // 13 // 13 == 12
pair_list = [(a, 12 // a) for a in sp.divisors(12) if a <= 12 // a]
assert pair_list == [(1, 12), (2, 6), (3, 4)]
coprime_pairs = [(a, b) for a, b in pair_list if gcd(a, b) == 1]
assert coprime_pairs == [(1, 12), (3, 4)]
assert 5 * 9 * 11 == 495 and 45 + 55 == 100 and abs(45 - 55) == 10 and hcf(45, 55) == 5
assert 60 - 1 == 59 and all(59 % d == r for d, r in ((3, 2), (4, 3), (5, 4)))
assert 10080 % 32 == 10080 % 36 == 10080 % 40 == 10080 % 45 == 10080 % 48 == 0
assert lcm(32, 36, 40, 45, 48) == 1440 and 10000 // 1440 * 1440 + 1440 == 10080
assert 16 + 24 == 40 and lcm(16, 24) == 48
assert 5 * 320 == 1600
assert 4 * 320 != 1600 and 2 * 320 != 1600

subtopics = [
 sub("hl-basics", "HCF & LCM: definitions and core relations",
  md(r"**HCF (GCD)** of some numbers is the largest number that divides all of them. **LCM** is the smallest number divisible by all of them.",
     "",
     "- HCF ≤ every number ≤ LCM (for numbers ≥ 1).",
     "- LCM is always a **multiple** of the HCF.",
     "- For co-prime numbers: HCF = 1 and LCM = product.",
     r"- For two numbers: $\text{HCF} \times \text{LCM} =$ product of the numbers. (Does **not** hold for three numbers.)",
     r"- If one number and the HCF are given, the other number $= \frac{\text{HCF} \times \text{LCM}}{\text{given number}}$.",
     "",
     "HCF of numbers close together is small (it must divide their difference); HCF of numbers in a fixed ratio is the scale factor."),
  [formula("Product relation (two numbers)", r"\text{HCF} \times \text{LCM} = a \times b"),
   formula("Other number", r"b = \frac{\text{HCF} \times \text{LCM}}{a}"),
   formula("Co-prime case", r"\gcd(a,b) = 1 \Rightarrow \text{LCM}(a,b) = ab"),
   formula("HCF divides every difference", r"\gcd(a,b) \mid (a-b)"),
   formula("LCM multiple of HCF", r"\gcd(a,b) \mid \text{LCM}(a,b)")],
  [trick("Ratio split",
         r"Numbers in ratio $a : b$ (a, b co-prime) with HCF $h$ are $ha$ and $hb$; LCM $= hab$; sum $= h(a+b)$; difference $= h(b-a)$.",
         "Two numbers are in ratio 5 : 6 and their HCF is 12. Find the LCM.",
         r"Numbers are 60 and 72. LCM $= 12 \times 5 \times 6 = 360$."),
   trick("Product ÷ HCF = LCM in one step",
         "Any question giving two of {product, HCF, LCM, one number} resolves by the product relation.",
         "The product of two numbers is 1600 and their HCF is 5. Find the LCM.",
         r"$\text{LCM} = \frac{1600}{5} = 320$."),
   trick("Divisor pairs of (product ÷ HCF)",
         "For 'how many pairs of numbers' questions, split product/HCF into co-prime factor pairs.",
         "The product of two numbers is 2028 and HCF is 13. How many such pairs exist?",
         r"$\frac{2028}{13} = 156 = 13a \times 13b / 13^2$... i.e. $a \times b = 156$ with $\gcd(a,b)=1$: pairs (1,156), (3,52), (4,39), (12,13) ⇒ **4 pairs**.")],
  [r"Using $\text{HCF} \times \text{LCM} = abc$ for three numbers — false for three.",
   "Forgetting that the co-prime pair (1, product) counts as a valid pair.",
   "Confusing 'greatest number that divides' (HCF) with 'least number that is divisible by' (LCM).",
   "Assuming the HCF of a ratio pair is the ratio itself."]),

 sub("hl-methods", "Finding HCF & LCM (incl. fractions and decimals)",
  md("**Prime factorisation:** HCF = product of common primes with the **lowest** powers; LCM = product of all primes with the **highest** powers.",
     "",
     r"**Long division method** is faster for two numbers: divide, then divide the divisor by the remainder, repeat; the last non-zero remainder is the HCF. LCM $= \frac{ab}{\text{HCF}}$.",
     "",
     r"**Fractions:** $\text{HCF} = \frac{\text{HCF of numerators}}{\text{LCM of denominators}}$, $\quad\text{LCM} = \frac{\text{LCM of numerators}}{\text{HCF of denominators}}$.",
     "",
     "**Decimals:** equalise decimal places first (write 0.5 as 0.500), find HCF/LCM of the integers, put the decimal point back with the same number of places."),
  [formula("HCF by factors", r"\text{HCF} = p_1^{\min} \cdot p_2^{\min} \cdots \text{(common primes, lowest powers)}"),
   formula("LCM by factors", r"\text{LCM} = p_1^{\max} \cdot p_2^{\max} \cdots \text{(all primes, highest powers)}"),
   formula("HCF of fractions", r"\text{HCF}\!\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\gcd(a, c)}{\text{LCM}(b, d)}"),
   formula("LCM of fractions", r"\text{LCM}\!\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\text{LCM}(a, c)}{\gcd(b, d)}"),
   formula("Two-number division method", r"\text{LCM} = \frac{a \times b}{\gcd(a,b)}")],
  [trick("LCM row of prime powers",
         "Write each number as a row of prime powers; LCM = read column maxima, HCF = read common minima. Three numbers take under 30 seconds.",
         r"Find the LCM of 32, 36, 45.",
         r"$32 = 2^5$, $36 = 2^2 \cdot 3^2$, $45 = 3^2 \cdot 5$. LCM $= 2^5 \times 3^2 \times 5 = 1440$."),
   trick("Fractions: numerators ↔ denominators cross rule",
         "HCF of fractions = HCF of tops over LCM of bottoms; LCM is the mirror image.",
         r"Find the HCF of $\frac{2}{3}$, $\frac{8}{9}$ and $\frac{10}{27}$.",
         r"$\frac{\gcd(2, 8, 10)}{\text{LCM}(3, 9, 27)} = \frac{2}{27}$."),
   trick("Decimals: shift the point",
         "Multiply everything by the power of 10 needed to clear decimals, solve as integers, shift the point back.",
         "Find the HCF of 0.54, 1.8 and 7.2.",
         "As 54, 180, 720 the HCF is 18 ⇒ answer 0.18.")],
  [r"Taking the HCF of fractions as $\frac{\text{HCF of tops}}{\text{HCF of bottoms}}$.",
   "Forgetting to reduce to lowest terms before checking common primes.",
   "Mixing up min/max powers: highest power goes with LCM.",
   "Returning an integer answer for a decimals question (lost scale factor)."]),

 sub("hl-word-problems", "Standard word problems (tiles, bells, groups, divisible numbers)",
  md("Almost every CGL HCF/LCM question is a dressed-up version of one template:",
     "",
     "- **Largest tile / rod / measure / greatest number that divides** → HCF.",
     "- **Bells/traffic lights together, same starting time again** → LCM of intervals.",
     "- **Least number divisible by each of a set** → LCM; greatest such N-digit number = largest multiple of the LCM within range.",
     "- **Least number leaving the SAME remainder r** with each divisor → LCM + r.",
     "- **Largest number leaving the SAME remainder r** → HCF of (number − r); if remainders are not given, HCF of pairwise differences.",
     "- **Least number leaving DIFFERENT remainders**: try LCM − (divisor − remainder) when each remainder = divisor − constant.",
     "",
     "Groups/military columns/planting trees in rows → HCF of the counts/dimensions."),
  [formula("Same remainder r", r"N = \text{LCM}(d_1, d_2, \dots) \times k + r"),
   formula("Different remainders, N ≡ −c", r"N = \text{LCM} \times k - c \text{ when } r_i = d_i - c"),
   formula("Largest tile count", r"\text{tiles} = \frac{L \times W}{h^2},\ h = \gcd(L, W)"),
   formula("Greatest n-digit multiple", r"\text{answer} = \underbrace{99\ldots9}_{n} - \left(\underbrace{99\ldots9}_{n} \bmod \text{LCM}\right)")],
  [trick("Subtract remainders, then HCF",
         "'Same remainder' questions: HCF of (each given number minus its remainder). Remainder unknown: HCF of the pairwise differences.",
         "Find the greatest number which divides 85 and 72 leaving remainders 1 and 2 respectively.",
         r"$85 - 1 = 84$, $72 - 2 = 70$. $\gcd(84, 70) = 14$."),
   trick("LCM + r",
         "'Least number leaving remainder r with each divisor': add r to the LCM.",
         "Find the least number which when divided by 12, 15, 20 and 27 leaves remainder 5 in each case.",
         r"LCM $= 540$, answer $= 540 + 5 = 545$."),
   trick("Bells: add the LCM to the start time",
         "Convert all intervals to the same unit, take the LCM, add to the given time.",
         "Three bells toll at intervals of 9, 12 and 15 minutes. They toll together at 8 a.m. When do they next toll together?",
         r"LCM$(9, 12, 15) = 180$ min $= 3$ h ⇒ **11 a.m.**")],
  [r"Adding the remainder when the question asks for the **greatest** divisor (that needs HCF of differences, not LCM + r).",
   "Forgetting to convert metres to centimetres (or minutes to seconds) before taking HCF/LCM.",
   r"For 'leaves remainder 2, 3, 4 with 3, 4, 5' type questions, seeing $r_i = d_i - 1$ and answering LCM $-1$ only if asked for the least; other values are LCM·k − 1.",
   "Using HCF where 'divisible by all' demands LCM."]),

 sub("hl-remainder-cases", "Two-step LCM/HCF cases (extra condition, N-digit bounds)",
  md("The hardest CGL variants combine LCM/HCF with one extra condition:",
     "",
     r"- **LCM + remainder, further divisible by p:** write $N = \text{LCM}\cdot k + r$ and solve $N \equiv 0 \pmod p$ for the smallest k.",
     "- **Greatest/least n-digit number with properties:** bound the LCM multiples inside the digit range first, then apply the extra condition.",
     "- **Given HCF and LCM, reconstruct numbers:** numbers $= h\\,a$ and $h\\,b$ with $\\gcd(a,b) = 1$ and $ab = \\frac{\\text{LCM}}{h}$; use the sum/difference to pick the pair.",
     "- **Count of possible pairs:** count co-prime factor pairs of LCM/HCF."),
  [formula("Extra divisibility condition", r"N = Lk + r,\ N \equiv 0 \pmod p \ \Rightarrow\ Lk \equiv -r \pmod p"),
   formula("Reconstruction", r"ab = \frac{\text{LCM}}{h},\quad \gcd(a, b) = 1"),
   formula("Pair count", r"\#\{(a,b): ab = M,\ \gcd(a,b)=1,\ a \le b\}")],
  [trick("Solve the little congruence for k",
         "Once N = LCM·k + r, only k's remainder mod p matters — test k = 1, 2, 3, … until it clicks.",
         "Find the least number which when divided by 6, 7, 8, 9 and 12 leaves remainder 1 in each case, and is also divisible by 13.",
         r"LCM = 504, so $N = 504k + 1$. $504 \equiv -3 \pmod{13}$ ⇒ $-3k + 1 \equiv 0$ ⇒ $3k \equiv 1$ ⇒ $k = 9$. $N = 4537$."),
   trick("N-digit multiple scan",
         "For least n-digit: divide the smallest n-digit number by the LCM, go to the next multiple. For greatest: reduce the largest n-digit number by its remainder.",
         "Find the least five-digit number exactly divisible by 32, 36, 40, 45 and 48.",
         r"LCM $= 1440$. $10000 \div 1440 = 6$ remainder $1360$ ⇒ answer $= 7 \times 1440 = 10080$."),
   trick("Sum or difference picks the pair",
         "With LCM/HCF and a sum (or difference) given, list co-prime pairs of LCM/HCF and match the sum.",
         r"Two numbers have HCF 5, LCM 495 and sum 100. Find their difference.",
         r"$a b = \frac{495}{5} = 99$, co-prime pairs (1, 99) and (9, 11). Sum $5(a+b) = 100$ ⇒ (9, 11) ⇒ numbers 45, 55 ⇒ difference **10**.")],
  [r"Answering LCM $+ r$ when the extra condition demands a larger multiple of the LCM.",
   "Listing factor pairs of LCM/HCF without checking co-primality.",
   "Forgetting the (1, M) pair when counting possibilities, or counting (a, b) and (b, a) twice.",
   "Missing that HCF must divide the sum/difference — a quick sanity filter for options."]),
]

pyq = [
 pat("Greatest number dividing with same/known remainders (HCF of differences)", "very common",
     "'Find the greatest number which divides x, y, z leaving remainders a, b, c' (remainders may be equal or different).",
     "Subtract each remainder from its number and take the HCF of the results. If remainders are unknown, take the HCF of pairwise differences of the numbers."),
 pat("Least number leaving the same remainder (LCM + r)", "very common",
     "'Find the least number which when divided by a, b, c leaves remainder r in each case.'",
     "LCM of the divisors + r. If a further condition appears (divisible by p, or n-digit), write N = LCM·k + r and fit the condition."),
 pat("Ratio + HCF/LCM → find the numbers", "very common",
     "'Two numbers are in ratio m : n and their HCF (or LCM) is …'",
     "Numbers = h·m and h·n (m, n co-prime). From LCM = h·m·n work backwards. Then answer whatever is asked (sum, difference, LCM)."),
 pat("Bells / lights / runners together again", "common",
     "Events repeating at different intervals, together at a start time, asked when next together or how many times in a window.",
     "LCM of intervals; add to start time; for 'how many times in t minutes' divide (t − first interval) by LCM and add 1 carefully."),
 pat("Product / HCF / LCM / one-number relation", "common",
     "Two of {product, HCF, LCM, one number} given; find a third, or 'how many pairs possible'.",
     "Use HCF × LCM = product. For pair counts, split product ÷ HCF into co-prime factor pairs (including 1 × M)."),
 pat("Largest tile / rod / measure / group size (HCF)", "common",
     "Paving a floor with the largest square tiles, longest rod measuring all dimensions, biggest group of men/women.",
     "Convert all dimensions to the same unit and take the HCF; tiles needed = area ÷ tile area."),
 pat("Greatest / least n-digit number divisible by a set", "common",
     "'Find the greatest four-digit number divisible by 15, 20, 25' / 'least five-digit number divisible by …'.",
     "LCM first, then fit inside the digit range: subtract the remainder from the top bound, or step up from the bottom bound."),
 pat("HCF / LCM of fractions or decimals", "occasional",
     "Bar of fractions like 2/3, 8/9, 10/27, or decimals like 0.54, 1.8.",
     "Cross rule for fractions; clear decimals and restore the scale for decimal values."),
]

solved = []

assert hcf(725, 435) == 145 and lcm(725, 435) == 2175
solved.append(Q("hl-s01", "The HCF of two numbers is 145 and their LCM is 2175. If one number is 725, find the other number.",
  ["335", "435", "625", "725"], 1, 435,
  md(r"$\text{HCF} \times \text{LCM} = a \times b$",
     r"$b = \frac{145 \times 2175}{725} = \frac{145 \times 3}{1} = 435$",
     r"Check: $\gcd(725, 435) = 145$ ✓ and $\text{LCM}(725, 435) = 2175$ ✓."),
  r"725 = 145 × 5, so the other must be 145 × 3 = 435 because LCM ÷ HCF = 2175/145 = 15 = 5 × 3 with (5, 3) co-prime.",
  "easy", "hl-basics", "product relation", 35))

assert hcf(85, 72) < 14
solved.append(Q("hl-s02", "Find the greatest number which when dividing 85 and 72 leaves remainders 1 and 2 respectively.",
  ["8", "14", "17", "83"], 1, hcf(84, 70),
  md("The required number divides 85 − 1 = 84 and 72 − 2 = 70 exactly.",
     r"$84 = 2^2 \times 3 \times 7$, $70 = 2 \times 5 \times 7$ ⇒ HCF $= 14$.",
     r"Check: $85 = 6 \times 14 + 1$ ✓, $72 = 5 \times 14 + 2$ ✓."),
  "Subtract the remainders, take the HCF: gcd(84, 70) = 14. (Option 83/17 ignore one condition; 8 divides both but is not the greatest.)",
  "easy", "hl-word-problems", "HCF with remainders", 40))

v = F(hcf(2, 8, 10), lcm(3, 9, 27))
assert v == F(2, 27)
solved.append(Q("hl-s03", r"The HCF of $\frac{2}{3}$, $\frac{8}{9}$ and $\frac{10}{27}$ is:",
  [r"$\frac{2}{27}$", r"$\frac{10}{3}$", r"$\frac{2}{3}$", r"$\frac{10}{27}$"], 0, v,
  md(r"HCF of numerators: $\gcd(2, 8, 10) = 2$.",
     r"LCM of denominators: $\text{LCM}(3, 9, 27) = 27$.",
     r"Answer: $\frac{2}{27}$."),
  "Cross rule: HCF of tops / LCM of bottoms = 2/27.",
  "easy", "hl-methods", "HCF of fractions", 35))

N = 145 * 2175 // 725
solved.append(Q("hl-s04", "Find the least number of square tiles required to pave a hall 15 m 17 cm long and 9 m 2 cm broad.",
  ["414", "686", "814", "902"], 2, 814,
  md(r"Convert: 15 m 17 cm = 1517 cm, 9 m 2 cm = 902 cm.",
     r"$\gcd(1517, 902) = 41$ (since $1517 = 37 \times 41$ and $902 = 22 \times 41$).",
     r"Tile size 41 cm × 41 cm; number of tiles $= \frac{1517 \times 902}{41 \times 41} = 37 \times 22 = 814$."),
  "Factor both: 1517 = 37 × 41, 902 = 22 × 41 ⇒ side 41, tiles = 37 × 22 = 814. (902 is the breadth — a trap.)",
  "hard", "hl-word-problems", "largest square tile", 75))

a, b = 45, 55
assert hcf(a, b) == 5 and lcm(a, b) == 495 and a + b == 100
solved.append(Q("hl-s05", "The HCF and LCM of two numbers are 5 and 495 respectively. If their sum is 100, find their difference.",
  ["5", "10", "15", "20"], 1, abs(a - b),
  md(r"Let the numbers be $5a$ and $5b$ with $\gcd(a, b) = 1$.",
     r"$5a \times 5b = 5 \times 495$ ⇒ $ab = 99$.",
     r"Co-prime pairs of 99 = 9 × 11: (1, 99) and (9, 11).",
     r"Sum: $5(a + b) = 100$ ⇒ $a + b = 20$ ⇒ $(a, b) = (9, 11)$.",
     r"Numbers: 45 and 55 ⇒ difference **10**."),
  "LCM/HCF = 99 = 9 × 11 (the only co-prime pair with a workable sum). Numbers 45 & 55 → difference 10.",
  "medium", "hl-remainder-cases", "reconstruct numbers from HCF and LCM", 60))

# ------------------------------------------------------------------ practice
P = []

assert hcf(96, 404) == 4
P.append(Q("hl-q01", "What is the HCF of 96 and 404?",
  ["4", "6", "8", "12"], 0, 4,
  md(r"$96 = 2^5 \times 3$, $404 = 2^2 \times 101$.",
     r"Common prime with lowest power: $2^2 = 4$."),
  "404 = 4 × 101 and 101 is prime, so the HCF is gcd(96, 4) = 4.",
  "easy", "hl-basics", "HCF by prime factorisation", 30))

assert lcm(12, 15, 20) == 60
P.append(Q("hl-q02", "The LCM of 12, 15 and 20 is:",
  ["30", "45", "60", "120"], 2, 60,
  md(r"$12 = 2^2 \times 3$, $15 = 3 \times 5$, $20 = 2^2 \times 5$.",
     r"LCM $= 2^2 \times 3 \times 5 = 60$."),
  "60 is the only option divisible by all three (120 works but is not the least).",
  "easy", "hl-basics", "LCM by prime factorisation", 30))

assert 1600 // 5 == 320
P.append(Q("hl-q03", "The product of two numbers is 1600 and their HCF is 5. The LCM of the numbers is:",
  ["320", "640", "800", "1600"], 0, 320,
  md(r"$\text{HCF} \times \text{LCM} = $ product ⇒ $\text{LCM} = \frac{1600}{5} = 320$."),
  "1600 ÷ 5 = 320. Quick check: LCM must be a multiple of HCF 5 ✓.",
  "easy", "hl-basics", "product relation", 25))

assert 2 * 8 == 16 and 16 + 24 == 40
P.append(Q("hl-q04", "Two numbers are in the ratio 2 : 3 and their LCM is 48. The sum of the numbers is:",
  ["28", "32", "36", "40"], 3, 40,
  md(r"Let the numbers be $2k$ and $3k$ (co-prime parts).",
     r"LCM $= 6k = 48$ ⇒ $k = 8$.",
     r"Numbers: 16 and 24 ⇒ sum $= 40$."),
  "LCM of a 2:3 pair is 6k = 48 ⇒ k = 8 ⇒ 16 + 24 = 40.",
  "easy", "hl-basics", "ratio + LCM", 30))

assert hcf(65, 117) == 13
P.append(Q("hl-q05", "Find the greatest number which divides 70 and 125 leaving remainders 5 and 8 respectively.",
  ["13", "65", "9", "117"], 0, 13,
  md("Required number divides 70 − 5 = 65 and 125 − 8 = 117.",
     r"$65 = 5 \times 13$, $117 = 9 \times 13$ ⇒ HCF $= 13$."),
  "gcd(65, 117) = 13. (Options 65 and 117 are the numbers themselves after subtraction — a classic trap.)",
  "medium", "hl-word-problems", "greatest divisor with remainders", 40))

assert lcm(9, 12, 15) == 180
P.append(Q("hl-q06", "Three bells toll at intervals of 9, 12 and 15 minutes respectively. If they toll together at 8 a.m., at what time will they toll together next?",
  ["9:30 a.m.", "10 a.m.", "11 a.m.", "12 noon"], 2, "11 a.m.",
  md(r"LCM$(9, 12, 15) = 180$ minutes $= 3$ hours.",
     "8 a.m. + 3 h = **11 a.m.**"),
  "LCM of 9, 12, 15 is 180 min = 3 h ⇒ 11 a.m.",
  "medium", "hl-word-problems", "bells together", 40))

assert 29 * 15 * 13 == 5655 and hcf(15, 13) == 1
P.append(Q("hl-q07", "The HCF of two numbers is 29, and the other two factors of their LCM are 15 and 13. The larger of the two numbers is:",
  ["377", "435", "1885", "5655"], 1, 435,
  md(r"The numbers are $29 \times 15 = 435$ and $29 \times 13 = 377$ (15 and 13 are co-prime).",
     r"Their LCM is $29 \times 15 \times 13 = 5655$ ✓.",
     "The larger number is **435**."),
  "Multiply the HCF by the bigger 'other factor': 29 × 15 = 435. (5655 is the LCM, not a number.)",
  "medium", "hl-basics", "HCF with LCM factors", 40))

assert hcf(825, 675, 450) == 75
P.append(Q("hl-q08", "Three pieces of timber 825 cm, 675 cm and 450 cm long have to be cut into planks of equal length. What is the greatest length of a plank that can measure all three exactly, and how many planks result in total?",
  ["75 cm, 26 planks", "45 cm, 43 planks", "75 cm, 24 planks", "25 cm, 78 planks"], 0, "75 cm, 26 planks",
  md(r"Greatest length $= \gcd(825, 675, 450) = 75$ cm.",
     r"Number of planks $= \frac{825 + 675 + 450}{75} = \frac{1950}{75} = 26$."),
  "HCF is 75 (both 675 and 450 end in 75-multiples). Planks = total length ÷ 75 = 26.",
  "medium", "hl-word-problems", "greatest measuring length", 55))

assert lcm(15, 20, 25) == 300 and 9999 % 300 == 99
P.append(Q("hl-q09", "Find the greatest number of four digits which is exactly divisible by 15, 20 and 25.",
  ["9600", "9800", "9900", "9950"], 2, 9900,
  md(r"LCM$(15, 20, 25) = 300$.",
     r"Greatest four-digit number = 9999; $9999 \div 300$ leaves remainder 99.",
     r"Answer $= 9999 - 99 = 9900$."),
  "LCM 300; 9999 − (9999 mod 300) = 9900.",
  "medium", "hl-remainder-cases", "greatest n-digit multiple", 45))

pairs = 2
P.append(Q("hl-q10", "The product of two numbers is 2028 and their HCF is 13. How many pairs of such numbers are possible?",
  ["2", "3", "4", "6"], 0, pairs,
  md(r"Let the numbers be $13a$ and $13b$ with $\gcd(a, b) = 1$.",
     r"$13a \times 13b = 2028$ ⇒ $169ab = 2028$ ⇒ $ab = 12$.",
     r"Co-prime factor pairs of 12: $(1, 12)$ and $(3, 4)$.",
     "Pairs of numbers: (13, 156) and (39, 52) ⇒ **2 pairs**."),
  "product ÷ HCF² = 12 = 1×12 = 3×4 (co-prime only) ⇒ 2 pairs. (Answer 3 forgets the co-prime check: 2×6 shares a factor.)",
  "hard", "hl-remainder-cases", "count pairs from product and HCF", 75))

assert (1, 12) in [(1, 12), (3, 4)] and gcd(39, 52) == 13 and hcf(13, 156) == 13 and lcm(13, 156) == 156 and 13*156 == 2028

assert lcm(32, 36, 40, 45, 48) == 1440
P.append(Q("hl-q11", "Find the least number of five digits which is exactly divisible by 32, 36, 40, 45 and 48.",
  ["10080", "10240", "10800", "11520"], 0, 10080,
  md(r"LCM $= 2^5 \times 3^2 \times 5 = 1440$.",
     r"$10000 \div 1440$ gives remainder 1360, so $1440 - 1360 = 80$ more is needed.",
     r"Answer $= 10000 + 80 = 10080$."),
  "LCM 1440; step 10000 up to the next multiple: 7 × 1440 = 10080.",
  "medium", "hl-remainder-cases", "least n-digit multiple", 50))

assert 59 % 3 == 2 and 59 % 4 == 3 and 59 % 5 == 4
P.append(Q("hl-q12", "Find the least number which when divided by 3, 4 and 5 leaves remainders 2, 3 and 4 respectively.",
  ["29", "47", "59", "119"], 2, 59,
  md("In each case the remainder is 1 less than the divisor: N + 1 is divisible by 3, 4 and 5.",
     r"LCM$(3, 4, 5) = 60$ ⇒ N + 1 is a multiple of 60.",
     r"Least value: $N = 60 - 1 = 59$."),
  "Remainder = divisor − 1 ⇒ N = LCM − 1 = 59.",
  "medium", "hl-word-problems", "different remainders pattern", 45))

N = 504 * 9 + 1
assert N == 4537 and N % 13 == 0 and all(N % d == 1 for d in (6, 7, 8, 9, 12))
assert all((504 * k + 1) % 13 != 0 for k in range(1, 9))
P.append(Q("hl-q13", "Find the least number which when divided by 6, 7, 8, 9 and 12 leaves a remainder of 1 in each case, and is exactly divisible by 13.",
  ["301", "1691", "2197", "4537"], 3, N,
  md(r"N = LCM$(6,7,8,9,12)k + 1 = 504k + 1$.",
     r"Need $504k + 1 \equiv 0 \pmod{13}$. Since $504 = 13 \times 38 + 10$, $10k \equiv -1 \equiv 12 \pmod{13}$.",
     r"$10k \equiv 12$ ⇒ multiply by 4: $40k \equiv 48$ ⇒ $k \equiv 9 \pmod{13}$ (since $40 \equiv 1$, $48 \equiv 9$).",
     r"Least $k = 9$: $N = 504 \times 9 + 1 = 4537$. Check: $4537 \div 13 = 349$ ✓."),
  "Test k = 1, 2, 3, … quickly: 505, 1009, 1513, 2017, 2521, 3025, 3529, 4033, 4537 — first divisible by 13 is 4537 (13 × 349).",
  "hard", "hl-remainder-cases", "LCM + remainder + extra divisor", 90))

assert F(2, 27) == F(hcf(2, 8, 10), lcm(3, 9, 27))
P.append(Q("hl-q14", r"The HCF of $\frac{2}{3}$, $\frac{8}{9}$ and $\frac{10}{27}$ is:",
  [r"$\frac{10}{3}$", r"$\frac{2}{3}$", r"$\frac{2}{27}$", r"$\frac{10}{27}$"], 2, F(2, 27),
  md(r"$\frac{\gcd(2, 8, 10)}{\text{LCM}(3, 9, 27)} = \frac{2}{27}$."),
  "HCF of tops = 2; LCM of bottoms = 27 ⇒ 2/27.",
  "easy", "hl-methods", "HCF of fractions", 30))

assert hcf(54, 180, 720) == 18
P.append(Q("hl-q15", "The HCF of 0.54, 1.8 and 7.2 is:",
  ["0.09", "0.18", "0.6", "1.8"], 1, F(18, 100),
  md("Write all with two decimal places: 0.54, 1.80, 7.20.",
     r"$\gcd(54, 180, 720) = 18$ ⇒ HCF $= 0.18$."),
  "Clear decimals (×100): gcd(54, 180, 720) = 18, shift the point back → 0.18.",
  "easy", "hl-methods", "HCF of decimals", 30))

topic = {
 "id": "hcf-lcm", "sectionId": "quant", "title": "HCF & LCM", "order": 3,
 "importance": "medium", "avgQuestions": {"tier1": 1, "tier2": 1},
 "summary": "Highest common factor and lowest common multiple — a small but near-guaranteed slot in CGL. Most questions are template word problems: greatest divisor with remainders (HCF of differences), least number with given remainders (LCM + r), bells, tiles and ratio pairs.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
