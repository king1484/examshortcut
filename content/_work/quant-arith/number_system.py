from _lib import *
from math import gcd, floor
import sympy as sp

# ------------------------------------------------------------------ helpers
def ndiv(n):
    return sp.divisor_count(n)

def zeros_fact(n):
    z, p = 0, 5
    while p <= n:
        z += n // p
        p *= 5
    return z

# ------------------------------------------------------------------ trick example checks
assert 400 // 13 - 99 // 13 == 23
assert 7000 - 7 == 6993
assert len(range(21, 80, 2)) == 30 and sum(range(21, 80, 2)) == 1500
assert [x for x in range(10) if int("37%d84" % x) % 12 == 0][0] == 2
assert pow(17, 15, 40) + pow(23, 15, 40) in (40, 0) and (17**15 + 23**15) % 40 == 0
assert 345345 == 345 * 1001 and 1001 == 7 * 11 * 13
assert pow(15, 47, 16) == 15
assert (98 * 97 * 96) % 99 == 93
assert 29 % 8 == 5
assert pow(1357, 2463, 10) == 3
assert (2**31 * 5**17 * 3**9) % 10 == 0
assert sum(math.factorial(k) for k in range(1, 51)) % 10 == 3
assert sp.factorint(360) == {2: 3, 3: 2, 5: 1} and 3 * 3 * 2 == 18
assert sum(1 for d in sp.divisors(360) if d % 2 == 0) == 18
assert zeros_fact(1000) == 249
assert sp.divisor_sigma(72) == 195
assert F(245 - 2, 990) == F(27, 110) and abs(float(F(27, 110)) - 0.24545454545454) < 1e-12
fr = [F(11, 12), F(13, 14), F(17, 18), F(19, 21)]
assert max(fr) == F(17, 18)
def terminates(f):
    d = f.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1
assert [terminates(x) for x in (F(7, 80), F(9, 42), F(11, 75), F(13, 120))] == [True, False, False, False]

subtopics = [
 sub("ns-types-counting", "Number types, place value & counting",
  md(r"**Number families you must know cold**",
     "",
     "| Type | Meaning | Watch-out |",
     "|---|---|---|",
     "| Natural | 1, 2, 3, … | 0 is **not** natural |",
     "| Whole | 0, 1, 2, … | smallest whole number is 0 |",
     "| Integers | …, −2, −1, 0, 1, 2, … | 0 is neither positive nor negative |",
     r"| Rational | $\frac{p}{q}$, $q \neq 0$ | every terminating/recurring decimal is rational |",
     r"| Irrational | non-terminating, non-recurring | $\sqrt{2}$, $\pi$; sum of two irrationals can be rational |",
     "| Prime | exactly two factors | 1 is neither prime nor composite; 2 is the only even prime; 25 primes up to 100 |",
     "| Co-prime | HCF = 1 | 8 and 15 are co-prime though neither is prime |",
     "",
     "**Place value vs face value:** in 3,47,218 the face value of 7 is 7, the place value is 7000.",
     "",
     "**Counting multiples** in a range and **sums of series** (natural numbers, squares, cubes, odd numbers, AP) appear as 1-mark sitters in Tier 1. Always read *between* (exclusive) vs *from … to* (inclusive)."),
  [formula("Multiples of k from 1 to n", r"\left\lfloor \frac{n}{k} \right\rfloor"),
   formula("Multiples of k from a to b", r"\left\lfloor \frac{b}{k} \right\rfloor - \left\lfloor \frac{a-1}{k} \right\rfloor"),
   formula("Inclusion–exclusion", r"n(A \cup B) = n(A) + n(B) - n(A \cap B)", "A ∩ B = multiples of LCM"),
   formula("Sum of first n natural numbers", r"\frac{n(n+1)}{2}"),
   formula("Sum of squares", r"1^2+2^2+\cdots+n^2 = \frac{n(n+1)(2n+1)}{6}"),
   formula("Sum of cubes", r"1^3+2^3+\cdots+n^3 = \left[\frac{n(n+1)}{2}\right]^2"),
   formula("First n odd / even numbers", r"1+3+\cdots+(2n-1) = n^2,\quad 2+4+\cdots+2n = n(n+1)"),
   formula("AP: terms and sum", r"n = \frac{l-a}{d}+1,\quad S = \frac{n}{2}(a+l)")],
  [trick("Floor-division counting",
         "Count multiples of $k$ up to $b$, subtract the multiples up to $a-1$. No listing needed.",
         "How many numbers from 100 to 400 are divisible by 13?",
         r"$\left\lfloor \frac{400}{13} \right\rfloor - \left\lfloor \frac{99}{13} \right\rfloor = 30 - 7 = 23$."),
   trick("Place value − face value",
         "Place value = digit × its position value. Difference = digit × (position value − 1).",
         "Find the difference between the place value and face value of 7 in 3,47,218.",
         r"Place value $= 7000$, face value $= 7$. Difference $= 7 \times 999 = 6993$."),
   trick("AP sum = terms × middle term",
         "For any AP, sum = number of terms × average of first and last term. Saves writing the formula.",
         "Find the sum of all odd numbers from 21 to 79.",
         r"Terms $= \frac{79-21}{2}+1 = 30$, average $= \frac{21+79}{2} = 50$. Sum $= 30 \times 50 = 1500$.")],
  ["Counting the end points when the question says *between* (exclusive).",
   "Treating 1 as a prime number, or forgetting that 2 is prime.",
   "In 'divisible by 3 or 5' questions, adding both counts without subtracting multiples of 15.",
   "Using $\\frac{n(n+1)}{2}$ for a series that does not start at 1."]),

 sub("ns-divisibility", "Divisibility rules",
  md("| Divisor | Rule |",
     "|---|---|",
     "| 2, 5, 10 | last digit |",
     "| 4 | last two digits divisible by 4 |",
     "| 8 | last three digits divisible by 8 |",
     "| 3, 9 | digit sum divisible by 3 / 9 |",
     "| 11 | (sum of digits at odd places) − (sum at even places) = 0 or a multiple of 11 |",
     "| 7, 11, 13 | alternating sum of 3-digit groups from the right divisible by 7/11/13 (since 1001 = 7 × 11 × 13) |",
     "| composite | break into **co-prime** factors: 12 = 3 × 4, 72 = 8 × 9, 88 = 8 × 11, 99 = 9 × 11 |",
     "",
     r"**Algebraic divisibility** (very popular): $a^n - b^n$ is always divisible by $a-b$; by $a+b$ too when $n$ is even. $a^n + b^n$ is divisible by $a+b$ when $n$ is odd.",
     "",
     "For missing-digit questions, apply the **most restrictive** rule first (usually 8 or 11), then the digit-sum rule."),
  [formula("Divisibility by 11", r"\left(\sum \text{odd-place digits}\right) - \left(\sum \text{even-place digits}\right) \in \{0, \pm 11, \pm 22, \dots\}"),
   formula("Composite divisor", r"pq \mid N \iff p \mid N \text{ and } q \mid N, \quad \gcd(p,q)=1"),
   formula("Difference of powers", r"(a-b) \mid (a^n - b^n) \text{ for all } n"),
   formula("Difference of even powers", r"(a+b) \mid (a^n - b^n) \text{ when } n \text{ is even}"),
   formula("Sum of odd powers", r"(a+b) \mid (a^n + b^n) \text{ when } n \text{ is odd}"),
   formula("abcabc form", r"\overline{abcabc} = \overline{abc} \times 1001 = \overline{abc} \times 7 \times 11 \times 13")],
  [trick("Split into co-prime factors",
         "Never split 12 as 2 × 6 or 72 as 4 × 18 — the factors must be co-prime. Test each factor's rule separately.",
         "If the five-digit number 37x84 is divisible by 12, find the smallest value of x.",
         md("12 = 3 × 4. **By 4:** last two digits 84 ✓ (any x).",
            r"**By 3:** $3+7+x+8+4 = 22+x$ must be a multiple of 3 ⇒ $x \in \{2, 5, 8\}$. Smallest $x = 2$.")),
   trick("The 1001 family",
         r"Any six-digit number of the form $abcabc$ equals $abc \times 1001$, so it is always divisible by 7, 11, 13 (and 77, 91, 143, 1001).",
         "Which of 7, 11 and 13 divide 345345?",
         r"$345345 = 345 \times 1001 = 345 \times 7 \times 11 \times 13$ — all three divide it."),
   trick("Sum of odd powers",
         r"$a^n + b^n$ with odd $n$ is divisible by $a+b$ — look at the options for $a+b$ first.",
         r"Is $17^{15} + 23^{15}$ divisible by 40?",
         r"Exponent 15 is odd, so $17 + 23 = 40$ divides $17^{15} + 23^{15}$. **Yes.**")],
  ["Splitting a composite divisor into non-co-prime factors (e.g. 18 is divisible by 2 and 6 but not by 12).",
   "Checking only the last two digits for 8 (need last three).",
   "For 11, forgetting that the difference can be 0 or a negative multiple of 11.",
   r"Applying the $(a+b)$ rule to $a^n + b^n$ when $n$ is even — it fails."]),

 sub("ns-remainders", "Remainders & remainder theorem",
  md(r"**Division algorithm:** $N = dq + r$ with $0 \le r < d$.",
     "",
     "**Remainder of sums/products** = remainder of the sum/product of individual remainders. Reduce every number first, then multiply small numbers.",
     "",
     r"**Negative remainders:** $98 \equiv -1 \pmod{99}$. Working with $-1, -2$ keeps numbers tiny; add the divisor at the end if the result is negative.",
     "",
     r"**Large powers:** find a small power that gives remainder $\pm 1$ (e.g. $2^3 = 8 \equiv 1 \pmod 7$, $2^4 = 16 \equiv -1 \pmod{17}$), then split the exponent. For a prime $p$ not dividing $a$: $a^{p-1} \equiv 1 \pmod p$ (Fermat).",
     "",
     r"**Divisor-multiple rule:** if $N$ leaves remainder $r$ with divisor $D$ and $d$ is a factor of $D$, the remainder with $d$ is simply $r \bmod d$."),
  [formula("Division algorithm", r"N = d \times q + r,\quad 0 \le r < d"),
   formula("Product rule", r"\text{Rem}\left(\frac{a \times b}{d}\right) = \text{Rem}\left(\frac{R_a \times R_b}{d}\right)"),
   formula("Fermat's little theorem", r"a^{p-1} \equiv 1 \pmod{p},\quad p \text{ prime},\ \gcd(a,p)=1"),
   formula("Divisor-multiple rule", r"N \equiv r \pmod{D},\ d \mid D \ \Rightarrow\ N \equiv r \pmod{d}"),
   formula("Base one more than divisor", r"(ad+1)^n \equiv 1 \pmod{d}"),
   formula("Base one less than divisor", r"(ad-1)^n \equiv (-1)^n \pmod{d}", "remainder 1 if n even, d − 1 if n odd")],
  [trick("Make the base ±1",
         r"Write the base as (multiple of divisor) ± 1. Then the power collapses to $\pm 1$.",
         r"Find the remainder when $15^{47}$ is divided by 16.",
         r"$15 \equiv -1 \pmod{16}$, so $15^{47} \equiv (-1)^{47} = -1 \equiv 16 - 1 = 15$."),
   trick("Negative remainders for products",
         "When the numbers are just below the divisor, use small negative remainders.",
         r"Find the remainder when $98 \times 97 \times 96$ is divided by 99.",
         r"$(-1)(-2)(-3) = -6 \equiv 99 - 6 = 93$."),
   trick("Divisor is a multiple — just reduce",
         "If the second divisor is a factor of the first, divide the old remainder by the new divisor. If it is NOT a factor, the answer cannot be found this way.",
         "A number leaves remainder 29 when divided by 56. What is the remainder when it is divided by 8?",
         r"$56 = 8 \times 7$, so remainder $= 29 \bmod 8 = 5$.")],
  ["Leaving a negative remainder as the final answer — add the divisor.",
   "Using the divisor-multiple rule in reverse: knowing N mod 8 does NOT give N mod 56.",
   "Applying Fermat when the divisor is not prime or divides the base.",
   "Multiplying the big numbers before reducing — wastes time and invites errors."]),

 sub("ns-unit-digit", "Unit digit & cyclicity",
  md("The unit digit of a power depends only on the unit digit of the base and the exponent's position in the **cycle**.",
     "",
     "| Unit digit of base | Cycle | Length |",
     "|---|---|---|",
     "| 0, 1, 5, 6 | same digit always | 1 |",
     "| 4 | 4, 6 | 2 (odd power → 4, even → 6) |",
     "| 9 | 9, 1 | 2 (odd power → 9, even → 1) |",
     "| 2 | 2, 4, 8, 6 | 4 |",
     "| 3 | 3, 9, 7, 1 | 4 |",
     "| 7 | 7, 9, 3, 1 | 4 |",
     "| 8 | 8, 4, 2, 6 | 4 |",
     "",
     "**Method:** divide the exponent by 4 (only its last two digits matter). Remainder r → use power r; remainder 0 → use power 4.",
     "",
     "For products, multiply only the unit digits. Any even number × any number ending in 5 ends in 0. Every n! with n ≥ 5 ends in 0."),
  [formula("Cyclicity rule", r"\text{u.d.}(a^n) = \text{u.d.}(a^{r}),\ r = n \bmod 4,\ (r = 0 \Rightarrow r = 4)"),
   formula("Cycles of 2, 3, 7, 8", r"2:\,2,4,8,6 \quad 3:\,3,9,7,1 \quad 7:\,7,9,3,1 \quad 8:\,8,4,2,6"),
   formula("Factorials", r"n! \equiv 0 \pmod{10} \text{ for } n \ge 5")],
  [trick("Last two digits of the exponent",
         "For mod 4, only the last two digits of the exponent matter (100 is a multiple of 4).",
         r"Find the unit digit of $1357^{2463}$.",
         r"Base ends in 7. $63 \bmod 4 = 3$ ⇒ $7^3 = 343$ ⇒ unit digit **3**."),
   trick("Even × 5 = 0",
         "If the product contains an even factor and a factor ending in 5, the unit digit is 0 — no cycle work needed.",
         r"Find the unit digit of $2^{31} \times 5^{17} \times 3^{9}$.",
         r"$2^{31}$ is even and $5^{17}$ ends in 5 ⇒ product ends in **0**."),
   trick("Factorial sums: only the first four terms",
         "From 5! onwards every factorial ends in 0, so the unit digit of 1! + 2! + … + n! (n ≥ 4) is always 3.",
         "Find the unit digit of 1! + 2! + 3! + … + 50!.",
         "1 + 2 + 6 + 24 = 33; all later terms end in 0 ⇒ unit digit **3**.")],
  ["Treating exponent remainder 0 as power 0 (unit digit 1) — use power 4 instead.",
   "Taking the exponent mod 4 using only its last digit (use the last two digits).",
   "For a difference like $7^{a} - 3^{b}$, forgetting to borrow 10 when the first unit digit is smaller."]),

 sub("ns-factors", "Factors, prime factorisation & trailing zeros",
  md(r"Write $N = p^a q^b r^c$ (prime factorisation). Everything about factors comes from the exponents.",
     "",
     r"- **Number of factors** $= (a+1)(b+1)(c+1)$",
     r"- **Odd factors:** ignore the power of 2. **Even factors** = total − odd (or give 2 an exponent from 1 to its max).",
     r"- **Perfect-square factors:** each exponent can only take even values 0, 2, 4, …",
     r"- **Sum of factors:** multiply $(1 + p + \dots + p^a)$ for each prime.",
     "",
     "**Trailing zeros** of a product = number of (2, 5) pairs = number of 5s (5s are scarcer). In n!, count 5s by successive division by 5."),
  [formula("Number of factors", r"d(N) = (a+1)(b+1)(c+1)"),
   formula("Sum of factors", r"\sigma(N) = \frac{p^{a+1}-1}{p-1} \cdot \frac{q^{b+1}-1}{q-1} \cdot \frac{r^{c+1}-1}{r-1}"),
   formula("Even factors", r"a \cdot (b+1)(c+1)", "when p = 2 with exponent a"),
   formula("Product of all factors", r"N^{d(N)/2}"),
   formula("Trailing zeros in n!", r"\left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \cdots"),
   formula("Highest power of prime p in n!", r"\sum_{k \ge 1} \left\lfloor \frac{n}{p^k} \right\rfloor")],
  [trick("Even factors: force one 2",
         r"If $N = 2^a \times (\text{odd part})$, even factors $= a \times$ (factors of odd part).",
         "How many even factors does 360 have?",
         r"$360 = 2^3 \times 3^2 \times 5$ ⇒ even factors $= 3 \times 3 \times 2 = 18$."),
   trick("Successive division by 5",
         "Keep dividing by 5 (dropping remainders) and add the quotients.",
         "How many zeros are at the end of 1000!?",
         r"$1000 \to 200 \to 40 \to 8 \to 1$. Sum $= 200+40+8+1 = 249$."),
   trick("Sum of factors as bracket product",
         "Write one bracket per prime: (1 + p + p² + …). Multiply.",
         "Find the sum of all factors of 72.",
         r"$72 = 2^3 \times 3^2$ ⇒ $(1+2+4+8)(1+3+9) = 15 \times 13 = 195$.")],
  ["Counting only n/5 for trailing zeros and missing the extra 5s from 25, 125, …",
   "Adding exponents instead of multiplying (a + 1)(b + 1)(c + 1).",
   "Forgetting that 1 and N are themselves factors.",
   "For trailing zeros of a SUM (e.g. 100! + 200!) adding the zeros — the sum has the smaller count."]),

 sub("ns-fractions-decimals", "Fractions, decimals & recurring decimals",
  md(r"**Terminating or not?** Reduce $\frac{p}{q}$ to lowest terms. It terminates only if $q$ has no prime factor other than 2 and 5.",
     "",
     "**Recurring decimal → fraction**",
     "",
     r"- Pure recurring: repeating digits over as many 9s. $0.\overline{36} = \frac{36}{99} = \frac{4}{11}$",
     r"- Mixed recurring: (all digits after the point − non-repeating part) over (one 9 per repeating digit followed by one 0 per non-repeating digit). $0.2\overline{45} = \frac{245-2}{990}$",
     r"- With a whole number: $2.4\overline{7} = 2 + \frac{47-4}{90}$",
     "",
     "**Comparing fractions:** cross-multiply two at a time, convert to decimals, or compare the gap from 1 (complement) when all fractions are close to 1."),
  [formula("Pure recurring", r"0.\overline{ab} = \frac{ab}{99},\quad 0.\overline{abc} = \frac{abc}{999}"),
   formula("Mixed recurring", r"0.a\overline{bc} = \frac{abc - a}{990}"),
   formula("Terminating test", r"\frac{p}{q} \text{ (lowest terms) terminates} \iff q = 2^m \, 5^n"),
   formula("Cross-multiplication", r"\frac{a}{b} > \frac{c}{d} \iff ad > bc \quad (b, d > 0)")],
  [trick("9s-and-0s rule",
         "Numerator: whole block after the point minus the non-repeating part. Denominator: one 9 per repeating digit, then one 0 per non-repeating digit.",
         r"Convert $0.2\overline{45}$ into a fraction.",
         r"$\frac{245 - 2}{990} = \frac{243}{990} = \frac{27}{110}$."),
   trick("Complement comparison",
         r"When fractions are close to 1, compare $1 - \text{fraction}$: the **smallest** gap gives the **largest** fraction.",
         r"Which is the largest: $\frac{11}{12}, \frac{13}{14}, \frac{17}{18}, \frac{19}{21}$?",
         r"Gaps: $\frac{1}{12}, \frac{1}{14}, \frac{1}{18}, \frac{2}{21}$. Smallest gap $\frac{1}{18}$ ⇒ $\frac{17}{18}$ is largest."),
   trick("Terminating check in one glance",
         "Cancel first, then look only at the denominator's primes.",
         r"Which of $\frac{7}{80}, \frac{9}{42}, \frac{11}{75}, \frac{13}{120}$ is a terminating decimal?",
         r"$80 = 2^4 \times 5$ ✓. $\frac{9}{42} = \frac{3}{14}$ (7) ✗, $75 = 3 \times 5^2$ ✗, $120 = 2^3 \times 3 \times 5$ ✗. Answer: $\frac{7}{80}$.")],
  [r"Writing $0.2\overline{45}$ as $\frac{245}{999}$ — ignoring the non-repeating digit.",
   "Testing the denominator for 2s and 5s before reducing the fraction.",
   "Assuming the fraction with the larger numerator is larger."]),
]

pyq = [
 pat("Missing digit for divisibility (by 11, 72, 88, 99)", "very common",
     "A number with one or two blanks (x, y) and 'is divisible by …'; options are digits or x + y.",
     "Split the divisor into co-prime factors. Apply the rule with fewest possibilities first (8 → last three digits, 11 → alternating sum), then the digit-sum rule. With two blanks, list the few cases and check which quantity (x + y, x − y) is fixed."),
 pat("Remainder with a factor of the old divisor", "very common",
     "'A number divided by 342 leaves remainder 47; find the remainder when divided by 18.'",
     "Check that the new divisor divides the old one (342 = 18 × 19). Answer = old remainder mod new divisor. One-line question — do not overthink."),
 pat("Unit digit of a power product", "very common",
     r"'Find the unit digit of $7^{95} \times 3^{58}$' or of a sum/difference of powers.",
     "Exponent mod 4 using last two digits; remainder 0 → power 4. Look for even × 5 shortcuts. Multiply only unit digits."),
 pat("Remainder of a large power", "common",
     r"'Find the remainder when $2^{99}$ is divided by 17' or $(x^n + a^n)$ divisibility.",
     r"Find the smallest power that gives ±1 mod the divisor; split the exponent. Use $a^n \pm b^n$ rules when two powers with equal exponents appear."),
 pat("Number / sum / even / odd / square factors", "common",
     "'How many factors does 540 have', 'sum of factors of 72', 'even factors of 1080'.",
     "Prime-factorise first. Apply (a+1)(b+1)… with the needed restriction (drop 2 for odd, force 2 for even, even exponents for squares)."),
 pat("Trailing zeros", "occasional",
     "'Number of zeros at the end of 250!' or at the end of a product like 5 × 10 × 15 × … × 500.",
     "Count 5s by successive division. For products of multiples, factor out the 5s. For a sum of factorials, the answer is the smaller count."),
 pat("Recurring decimal conversion and arithmetic", "common",
     r"Bars over digits: $2.4\overline{7}$, $0.\overline{3} + 0.\overline{47}$ etc.",
     "Convert each with the 9s-and-0s rule, then add fractions over a common 99/990 denominator. Check the answer by converting back mentally."),
 pat("Counting multiples in a range / series sums", "common",
     "'How many numbers between 200 and 600 are divisible by 4, 5 and 6' or 'sum of all two-digit multiples of 6'.",
     "Use LCM for 'divisible by all', inclusion–exclusion for 'or'. Watch between (exclusive) vs from–to (inclusive). AP sum = terms × middle term."),
]

# ------------------------------------------------------------------ solved examples
solved = []

ud = (pow(3, 65, 10) * pow(6, 59, 10) * pow(7, 71, 10)) % 10
assert ud == 4
solved.append(Q("ns-s01", r"What is the unit digit of $3^{65} \times 6^{59} \times 7^{71}$?",
  ["2", "4", "6", "8"], 1, ud,
  md(r"- $3^{65}$: $65 \bmod 4 = 1$ ⇒ unit digit of $3^1 = 3$.",
     r"- $6^{59}$: 6 raised to any power ends in 6.",
     r"- $7^{71}$: $71 \bmod 4 = 3$ ⇒ unit digit of $7^3 = 343$ is 3.",
     r"Product of unit digits: $3 \times 6 \times 3 = 54$ ⇒ unit digit **4**."),
  "Cyclicity 4 for 3 and 7: exponents 65 → 1, 71 → 3. Unit digits 3, 6, 3 → 3 × 6 = 18 → 8 × 3 = 24 → **4**.",
  "easy", "ns-unit-digit", "unit digit of power product", 40))

r = pow(25, 25, 9)
assert r == 7 and pow(7, 3, 9) == 1
solved.append(Q("ns-s02", r"What is the remainder when $25^{25}$ is divided by 9?",
  ["1", "4", "7", "8"], 2, r,
  md(r"$25 = 27 - 2$, so $25 \equiv 7 \pmod 9$ (or $\equiv -2$).",
     r"$7^3 = 343 = 38 \times 9 + 1$, so $7^3 \equiv 1 \pmod 9$.",
     r"$25 = 3 \times 8 + 1$ ⇒ $7^{25} = (7^3)^8 \times 7 \equiv 1 \times 7 = 7$.",
     "Remainder = **7**."),
  md(r"$25 \equiv -2 \pmod 9$ and $(-2)^3 = -8 \equiv 1 \pmod 9$.",
     r"$(-2)^{25} = ((-2)^3)^8 \times (-2) \equiv -2 \equiv 7$."),
  "medium", "ns-remainders", "remainder of large power", 60))

opts = [r"$\frac{5}{7}$", r"$\frac{7}{10}$", r"$\frac{9}{13}$", r"$\frac{11}{16}$"]
fv = [F(5, 7), F(7, 10), F(9, 13), F(11, 16)]
assert max(fv) == fv[0]
solved.append(Q("ns-s03", r"Which of the following fractions is the largest? $\frac{5}{7}, \frac{7}{10}, \frac{9}{13}, \frac{11}{16}$",
  opts, 0, fv[0],
  md("Convert to decimals:",
     r"$\frac{5}{7} \approx 0.714$, $\frac{7}{10} = 0.700$, $\frac{9}{13} \approx 0.692$, $\frac{11}{16} = 0.6875$.",
     r"Largest: $\frac{5}{7}$."),
  md("All fractions are a bit above 2/3, so compare the gap from 1:",
     r"$1 - \frac{5}{7} = \frac{2}{7} \approx 0.286$, $\frac{3}{10} = 0.3$, $\frac{4}{13} \approx 0.308$, $\frac{5}{16} \approx 0.313$.",
     r"Smallest gap ⇒ largest fraction: $\frac{5}{7}$."),
  "easy", "ns-fractions-decimals", "compare fractions", 45))

S = 3**25 + 3**26 + 3**27 + 3**28
assert S == 3**25 * 40
assert S % 30 == 0 and S % 16 != 0 and S % 25 != 0 and S % 11 != 0
solved.append(Q("ns-s04", r"The expression $3^{25} + 3^{26} + 3^{27} + 3^{28}$ is divisible by which of the following?",
  ["11", "16", "25", "30"], 3, "30",
  md(r"Take out the common factor $3^{25}$:",
     r"$3^{25}(1 + 3 + 9 + 27) = 3^{25} \times 40 = 3^{25} \times 2^3 \times 5$.",
     r"30 = 2 × 3 × 5 — all present ✓. 16 needs $2^4$ (only $2^3$) ✗, 25 needs $5^2$ ✗, 11 absent ✗.",
     "Answer: **30**."),
  "Factor the smallest power: bracket = 1 + 3 + 9 + 27 = 40. The number is 3^25 × 40, so any divisor must be built from 3s, at most three 2s and one 5 → 30.",
  "medium", "ns-divisibility", "factorise sum of powers", 50))

terms = list(range(12, 100, 6))
assert len(terms) == 15 and sum(terms) == 810
solved.append(Q("ns-s05", "What is the sum of all two-digit numbers that are divisible by 6?",
  ["756", "810", "864", "900"], 1, sum(terms),
  md("Two-digit multiples of 6: 12, 18, …, 96.",
     r"Number of terms $= \frac{96 - 12}{6} + 1 = 15$.",
     r"Sum $= \frac{15}{2}(12 + 96) = 15 \times 54 = 810$."),
  "15 terms (99 ÷ 6 = 16 minus the single-digit one, 6). Middle term = (12 + 96)/2 = 54. Sum = 15 × 54 = **810**.",
  "easy", "ns-types-counting", "AP sum of multiples", 45))

# ------------------------------------------------------------------ practice
P = []

xs = [x for x in range(10) if int("74%d5236" % x) % 11 == 0]
assert xs == [8]
P.append(Q("ns-q01", "If the seven-digit number 74x5236 is divisible by 11, what is the value of x?",
  ["3", "5", "6", "8"], 3, xs[0],
  md("Digits from the right: 6, 3, 2, 5, x, 4, 7.",
     "Sum at odd places = 6 + 2 + x + 7 = 15 + x; sum at even places = 3 + 5 + 4 = 12.",
     "Difference = (15 + x) − 12 = x + 3 must be 0 or 11 ⇒ x = 8."),
  "x + 3 = 11 is the only possibility for a digit, so x = 8. Check option: 7485236 → (6+2+8+7) − (3+5+4) = 23 − 12 = 11 ✓.",
  "easy", "ns-divisibility", "missing digit divisibility by 11", 40))

ud = pow(7, 95, 10) * pow(3, 58, 10) % 10
assert ud == 7
P.append(Q("ns-q02", r"What is the unit digit of $7^{95} \times 3^{58}$?",
  ["1", "3", "7", "9"], 2, ud,
  md(r"$95 \bmod 4 = 3$ ⇒ $7^{95}$ ends like $7^3 = 343$ → 3.",
     r"$58 \bmod 4 = 2$ ⇒ $3^{58}$ ends like $3^2 = 9$ → 9.",
     r"$3 \times 9 = 27$ ⇒ unit digit **7**."),
  "Cycle of 7: 7, 9, 3, 1 → 3rd = 3. Cycle of 3: 3, 9, 7, 1 → 2nd = 9. 3 × 9 → 7.",
  "easy", "ns-unit-digit", "unit digit of power product", 35))

assert 893 == 47 * 19 and 193 % 47 == 5
P.append(Q("ns-q03", "A number when divided by 893 leaves a remainder of 193. What will be the remainder when the same number is divided by 47?",
  ["5", "10", "19", "41"], 0, 193 % 47,
  md(r"Let $N = 893k + 193$. Since $893 = 47 \times 19$, $893k$ is a multiple of 47.",
     r"So the remainder is $193 \bmod 47$: $193 = 4 \times 47 + 5$ ⇒ **5**."),
  "47 divides 893, so just divide the old remainder: 193 − 188 = 5.",
  "easy", "ns-remainders", "remainder with factor of divisor", 35))

val = 2 + F(47 - 4, 90)
assert val == F(223, 90) and abs(float(val) - 2.4777777777) < 1e-9
P.append(Q("ns-q04", r"The value of $2.4\overline{7}$ in the form $\frac{p}{q}$ is:",
  [r"$\frac{247}{99}$", r"$\frac{223}{90}$", r"$\frac{223}{99}$", r"$\frac{245}{90}$"], 1, val,
  md(r"Let $x = 2.4777\ldots$ Then $10x = 24.777\ldots$ and $100x = 247.777\ldots$",
     r"$100x - 10x = 223$ ⇒ $x = \frac{223}{90}$."),
  r"9s-and-0s rule: $2 + \frac{47 - 4}{90} = 2 + \frac{43}{90} = \frac{223}{90}$.",
  "easy", "ns-fractions-decimals", "recurring decimal to fraction", 40))

assert sp.factorint(540) == {2: 2, 3: 3, 5: 1} and ndiv(540) == 24
P.append(Q("ns-q05", "How many factors does 540 have?",
  ["18", "20", "24", "30"], 2, ndiv(540),
  md(r"$540 = 2^2 \times 3^3 \times 5^1$.",
     r"Number of factors $= (2+1)(3+1)(1+1) = 3 \times 4 \times 2 = 24$."),
  "Add 1 to each exponent and multiply: 3 × 4 × 2 = 24.",
  "easy", "ns-factors", "number of factors", 35))

r = pow(2, 99, 17)
assert r == 8
P.append(Q("ns-q06", r"What is the remainder when $2^{99}$ is divided by 17?",
  ["1", "8", "9", "15"], 1, r,
  md(r"$2^4 = 16 \equiv -1 \pmod{17}$, so $2^8 \equiv 1 \pmod{17}$.",
     r"$99 = 8 \times 12 + 3$ ⇒ $2^{99} = (2^8)^{12} \times 2^3 \equiv 1 \times 8 = 8$."),
  r"Find the ±1 power: $2^4 \equiv -1$. $2^{99} = (2^4)^{24} \times 2^3 \equiv (+1) \times 8 = 8$.",
  "medium", "ns-remainders", "remainder of large power", 50))

z = zeros_fact(250)
assert z == 62
P.append(Q("ns-q07", "How many zeros are there at the end of 250! (factorial 250)?",
  ["50", "52", "60", "62"], 3, z,
  md("Each trailing zero needs a pair (2, 5); 5s are fewer, so count the 5s.",
     r"$\left\lfloor \frac{250}{5} \right\rfloor + \left\lfloor \frac{250}{25} \right\rfloor + \left\lfloor \frac{250}{125} \right\rfloor = 50 + 10 + 2 = 62$."),
  "250 → 50 → 10 → 2 (keep dividing by 5). 50 + 10 + 2 = 62.",
  "medium", "ns-factors", "trailing zeros in factorial", 40))

sols = [(x, y) for x in range(10) for y in range(10) if int("25%d6%d4" % (x, y)) % 72 == 0]
assert sols == [(4, 6), (8, 2)] and {x + y for x, y in sols} == {10}
P.append(Q("ns-q08", "If the six-digit number 25x6y4 is divisible by 72, what is the value of x + y?",
  ["1", "8", "10", "12"], 2, 10,
  md("72 = 8 × 9 (co-prime).",
     "**By 8:** last three digits 6y4 must be divisible by 8. Checking y = 0 to 9: only 624 and 664 work ⇒ y = 2 or 6.",
     "**By 9:** 2 + 5 + x + 6 + y + 4 = 17 + x + y must be a multiple of 9 ⇒ x + y = 1 or 10.",
     "y = 2 ⇒ x = 8; y = 6 ⇒ x = 4. In both cases x + y = **10** (x + y = 1 is impossible since y ≥ 2)."),
  "Digit sum 17 + (x + y) → next multiple of 9 is 27 ⇒ x + y = 10 (x + y = 1 fails because y is 2 or 6).",
  "medium", "ns-divisibility", "missing digits divisibility by 72", 60))

assert sp.factorint(1080) == {2: 3, 3: 3, 5: 1}
ev = sum(1 for d in sp.divisors(1080) if d % 2 == 0)
assert ev == 24 and ndiv(1080) == 32
P.append(Q("ns-q09", "How many even factors does 1080 have?",
  ["8", "16", "24", "32"], 2, ev,
  md(r"$1080 = 2^3 \times 3^3 \times 5$. Total factors $= 4 \times 4 \times 2 = 32$.",
     r"Odd factors (power of 2 = 0): $4 \times 2 = 8$.",
     r"Even factors $= 32 - 8 = 24$."),
  r"Force at least one 2: exponent of 2 has 3 choices (1, 2, 3) ⇒ $3 \times 4 \times 2 = 24$.",
  "medium", "ns-factors", "even factors", 45))

cnt = sum(1 for n in range(201, 600) if n % 4 == 0 and n % 5 == 0 and n % 6 == 0)
assert cnt == 6
P.append(Q("ns-q10", "How many numbers between 200 and 600 are divisible by 4, 5 and 6?",
  ["5", "6", "7", "8"], 1, cnt,
  md("Divisible by 4, 5 and 6 ⇔ divisible by LCM(4, 5, 6) = 60.",
     "Multiples of 60 strictly between 200 and 600: 240, 300, 360, 420, 480, 540 ⇒ **6**."),
  r"$\left\lfloor \frac{599}{60} \right\rfloor - \left\lfloor \frac{200}{60} \right\rfloor = 9 - 3 = 6$. (600 itself is excluded — 'between'.)",
  "medium", "ns-types-counting", "count multiples in range", 45))

N = 47**43 + 43**43
assert N % 90 == 0 and N % 4 != 0 and N % 86 != 0 and N % 94 != 0
P.append(Q("ns-q11", r"The number $47^{43} + 43^{43}$ is divisible by:",
  ["4", "86", "90", "94"], 2, "90",
  md(r"For odd $n$, $a^n + b^n$ is divisible by $a + b$. Here $n = 43$ is odd ⇒ divisible by $47 + 43 = 90$.",
     r"Check traps: mod 4, $47 \equiv 43 \equiv 3$ ⇒ sum $\equiv 2 \times 3^{43} \equiv 2 \pmod 4$ — not divisible by 4. Mod 43 the sum $\equiv 4^{43} \equiv 4$ (Fermat), so 86 fails; similarly 94 fails."),
  "Odd equal exponents + '+' sign ⇒ look for a + b = 90 in the options.",
  "medium", "ns-divisibility", "sum of odd powers divisibility", 40))

r = (1523 * 1527 * 1531) % 15
assert r == 6 and (1523 % 15, 1527 % 15, 1531 % 15) == (8, 12, 1)
P.append(Q("ns-q12", r"What is the remainder when $1523 \times 1527 \times 1531$ is divided by 15?",
  ["3", "6", "8", "12"], 1, r,
  md("Reduce each number mod 15: 1523 → 8, 1527 → 12, 1531 → 1 (since 1515 = 15 × 101).",
     r"$8 \times 12 \times 1 = 96$, and $96 \bmod 15 = 6$."),
  r"Use negatives: 1527 ≡ −3, 1523 ≡ −7, 1531 ≡ 1. $(-7)(-3)(1) = 21 \equiv 6$.",
  "medium", "ns-remainders", "remainder of product", 45))

# hard
Nn = 2**4 * 3**3 * 5**2 * 7
sq = sum(1 for d in sp.divisors(Nn) if sp.sqrt(d).is_integer)
assert sq == 12
P.append(Q("ns-q13", r"How many factors of $N = 2^4 \times 3^3 \times 5^2 \times 7$ are perfect squares?",
  ["6", "8", "12", "24"], 2, sq,
  md("A factor is a perfect square only if every prime appears with an even exponent.",
     "- 2: exponents 0, 2, 4 → 3 choices",
     "- 3: exponents 0, 2 → 2 choices",
     "- 5: exponents 0, 2 → 2 choices",
     "- 7: exponent 0 only → 1 choice",
     r"Total $= 3 \times 2 \times 2 \times 1 = 12$."),
  r"Square factors = product of $\left(\left\lfloor \frac{a}{2} \right\rfloor + 1\right)$: $(2+1)(1+1)(1+1)(0+1) = 12$.",
  "hard", "ns-factors", "perfect square factors", 75))

tot = F(3, 9) + F(47, 99) + F(15 - 1, 90)
assert tot == F(53, 55) and abs(1/3 + 47/99 + 0.155555555555 - 53/55) < 1e-9
P.append(Q("ns-q14", r"What is the value of $0.\overline{3} + 0.\overline{47} + 0.1\overline{5}$?",
  [r"$\frac{47}{55}$", r"$\frac{52}{55}$", r"$\frac{53}{55}$", r"$\frac{106}{99}$"], 2, tot,
  md(r"$0.\overline{3} = \frac{3}{9} = \frac{1}{3}$, $0.\overline{47} = \frac{47}{99}$, $0.1\overline{5} = \frac{15 - 1}{90} = \frac{14}{90} = \frac{7}{45}$.",
     r"LCM of 3, 99, 45 is 495: $\frac{165}{495} + \frac{235}{495} + \frac{77}{495} = \frac{477}{495} = \frac{53}{55}$."),
  r"Put all over 990: $\frac{330 + 470 + 154}{990} = \frac{954}{990} = \frac{53}{55}$. Sanity check: $0.333 + 0.475 + 0.156 \approx 0.964 \approx \frac{53}{55}$.",
  "hard", "ns-fractions-decimals", "sum of recurring decimals", 90))

c = sum(1 for n in range(1, 301) if (n % 3 == 0 or n % 5 == 0) and n % 7 != 0)
A = 300 // 3 + 300 // 5 - 300 // 15
B = 300 // 21 + 300 // 35 - 300 // 105
assert A == 140 and B == 20 and c == A - B == 120
P.append(Q("ns-q15", "How many numbers from 1 to 300 are divisible by 3 or 5 but NOT by 7?",
  ["118", "120", "126", "140"], 1, c,
  md("**Divisible by 3 or 5:** 100 + 60 − 20 (multiples of 15) = 140.",
     "**Of these, divisible by 7 as well** (i.e. by 21 or 35): 14 + 8 − 2 (multiples of 105) = 20.",
     "Required count = 140 − 20 = **120**."),
  "Inclusion–exclusion twice: (3 or 5) − (21 or 35) = 140 − 20 = 120. Trap option 140 ignores the 'not by 7' condition.",
  "hard", "ns-types-counting", "inclusion-exclusion counting", 90))

topic = {
 "id": "number-system", "sectionId": "quant", "title": "Number System", "order": 1,
 "importance": "high", "avgQuestions": {"tier1": 2, "tier2": 3},
 "summary": "Divisibility, remainders, unit digits, factors and recurring decimals — the base layer every other Quant topic uses. CGL asks 1–3 direct questions per Tier 1 shift (missing-digit divisibility, remainders and unit digit are near-certain) and a few more in Tier 2.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
