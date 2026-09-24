import math
from _lib import Sub, ind


def build():
    S = Sub("ns-types-counting")
    S.notes = r"""### What is a number system?
A number system is simply the family tree of numbers. Every number you meet in an exam belongs to one or more families. Knowing the families helps you answer "which of these is rational / prime / whole?" questions in seconds.

### The number families
- **Natural numbers**: counting numbers 1, 2, 3, … (0 is **not** natural).
- **Whole numbers**: 0, 1, 2, 3, … (natural numbers plus 0).
- **Integers**: …, −3, −2, −1, 0, 1, 2, 3, … 0 is neither positive nor negative.
- **Rational numbers**: can be written as $\frac{p}{q}$ with integers $p, q$ and $q \neq 0$. Every terminating decimal (0.25) and every recurring decimal ($0.\overline{3}$) is rational.
- **Irrational numbers**: decimal never ends and never repeats, e.g. $\sqrt{2}$, $\sqrt{3}$, $\pi$. Careful: $\sqrt{8} \times \sqrt{2} = 4$ is rational, and $(2+\sqrt{3}) + (2-\sqrt{3}) = 4$ is rational.
- **Real numbers**: rational + irrational together.

### Prime, composite and co-prime
- A **prime** has exactly two factors: 1 and itself (2, 3, 5, 7, 11, …). 2 is the only even prime.
- A **composite** number has more than two factors (4, 6, 9, …).
- **1 is neither prime nor composite.**
- There are **25 primes up to 100** (15 up to 50, 10 from 51 to 100).
- **Co-prime** numbers have HCF 1, e.g. 8 and 15. They need not be prime themselves.
- To test if a number $N$ is prime, divide it by primes up to $\sqrt{N}$. Example: 221 → $\sqrt{221} \approx 14.9$; 221 = 13 × 17, so not prime.

### Place value and face value
In 5,63,847 the **face value** of 6 is just 6. Its **place value** is 6 × 10,000 = 60,000 because it sits in the ten-thousands place. Place value − face value = digit × (position value − 1).

### Counting multiples in a range
Multiples of $k$ from 1 to $n$ = $\lfloor n/k \rfloor$ (whole-number part of the division).
Multiples of $k$ from $a$ to $b$ = $\lfloor b/k \rfloor - \lfloor (a-1)/k \rfloor$.
Example: multiples of 7 from 100 to 300 = 42 − 14 = 28.

- "Divisible by 4 **and** 6" means divisible by LCM(4, 6) = 12 (not 24).
- "Divisible by 4 **or** 6" uses inclusion–exclusion: $n(A) + n(B) - n(A \cap B)$.
- "Divisible by **neither**" = total − (divisible by 4 or 6).
- Read the words: "between 1 and 100" usually excludes the ends; "from 1 to 100" includes them.

### Sums you must know
| Series | Sum |
|---|---|
| 1 + 2 + … + n | $\frac{n(n+1)}{2}$ |
| $1^2 + 2^2 + … + n^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $1^3 + 2^3 + … + n^3$ | $\left[\frac{n(n+1)}{2}\right]^2$ |
| first n odd numbers | $n^2$ |
| first n even numbers | $n(n+1)$ |
| any AP | number of terms × (first + last) ÷ 2 |

For a sum that starts in the middle (like $11^2$ to $20^2$), find the sum up to 20 and subtract the sum up to 10.

### Digits and pages
To number pages 1 to 350: 1-digit pages 1–9 use 9 digits, 2-digit pages 10–99 use 90 × 2 = 180 digits, and pages 100–350 use 251 × 3 = 753 digits. Total 942. Going backwards (digits given, find pages) just reverses these steps.

### Two-digit numbers and reversal
A two-digit number with tens digit $a$ and units digit $b$ is $10a + b$. Its reverse is $10b + a$.
- Difference = $9(a - b)$. Sum = $11(a + b)$.
- So "number − reverse = 36" tells you the digits differ by 4 straight away.

### Quick revision
- 0 is whole but not natural; 1 is neither prime nor composite; 2 is the only even prime.
- 25 primes below 100.
- Count multiples with floor division; "and" means LCM, "or" means inclusion–exclusion.
- Sum formulas: $\frac{n(n+1)}{2}$, $\frac{n(n+1)(2n+1)}{6}$, $\left[\frac{n(n+1)}{2}\right]^2$, $n^2$.
- Reversal: difference = 9 × (digit difference), sum = 11 × (digit sum).
"""

    # ---------------- patterns ----------------
    S.pattern("ns-tc-p1", "Counting numbers divisible by k in a range (and / or / neither)", "very common",
        "The question asks 'how many numbers between/from A to B are divisible by …'. Words like 'and', 'or', 'neither', 'but not' decide the method.",
        r"\left\lfloor \frac{b}{k} \right\rfloor - \left\lfloor \frac{a-1}{k} \right\rfloor",
        r"""1. For one divisor $k$: count up to $b$, subtract the count up to $a-1$.
2. "Divisible by $x$ and $y$" → use $k = \text{LCM}(x, y)$.
3. "By $x$ or $y$" → $n(x) + n(y) - n(\text{LCM})$.
4. "Neither" → total − (or-count). "By $x$ but not $y$" → $n(x) - n(\text{LCM})$.

Why it works: every $k$-th number is a multiple of $k$, so floor division counts them without listing.""",
        "How many numbers from 1 to 200 are divisible by 6 or 8?",
        r"By 6: $\lfloor 200/6 \rfloor = 33$. By 8: $\lfloor 200/8 \rfloor = 25$. By LCM 24: $\lfloor 200/24 \rfloor = 8$. Answer $= 33 + 25 - 8 = 50$.")
    S.pattern("ns-tc-p2", "Sum of series: natural numbers, squares, cubes, odd numbers, AP", "very common",
        r"A long sum like $1^2 + 2^2 + \dots$, 'sum of all two-digit multiples of 7', or 'sum of first n odd numbers'.",
        r"\frac{n(n+1)}{2},\ \frac{n(n+1)(2n+1)}{6},\ \left[\frac{n(n+1)}{2}\right]^2,\ S_{AP} = \frac{n}{2}(a+l)",
        r"""1. Identify the series type.
2. If it does not start at 1, take (sum up to the last term) − (sum up to the term just before the first).
3. For multiples/AP: number of terms $n = \frac{l-a}{d} + 1$, then sum $= \frac{n}{2}(a + l)$.

Why it works: an AP pairs up first-and-last, second-and-second-last … each pair has the same total.""",
        r"Find $1^3 + 2^3 + \dots + 10^3$.",
        r"$\left[\frac{10 \times 11}{2}\right]^2 = 55^2 = 3025$.")
    S.pattern("ns-tc-p3", "Place value and face value", "common",
        "A number is given in Indian commas and the question asks the place value, face value, their sum/difference/product for one or two digits.",
        r"\text{Place value} = \text{digit} \times 10^{\text{position}}",
        r"""1. Mark positions from the right: ones, tens, hundreds, thousands, ten-thousands, lakhs, ten-lakhs, crores.
2. Place value = digit × that position's value. Face value = the digit itself.
3. Do the asked operation.

Why: our system is positional — the same digit is worth more as it moves left.""",
        "Find the difference between the place value and the face value of 4 in 7,64,219.",
        r"4 is in the thousands place → place value 4000. Face value 4. Difference $= 4000 - 4 = 3996$.")
    S.pattern("ns-tc-p4", "Classifying numbers: prime, rational/irrational, co-prime", "common",
        "Options list numbers and the question asks which is prime / rational / irrational, or asks how many primes lie in a range.",
        None,
        r"""1. For rational vs irrational, simplify first ($\sqrt{8}\times\sqrt{2} = 4$ is rational).
2. For primes, test divisibility by primes up to $\sqrt{N}$.
3. Remember: 1 is not prime; 2 is the only even prime; 25 primes up to 100.

Why: a number is irrational only if its simplified value still has a non-ending, non-repeating decimal.""",
        "Is 391 a prime number?",
        r"$\sqrt{391} \approx 19.8$, so test primes up to 19. $391 = 17 \times 23$. So 391 is **not** prime.")
    S.pattern("ns-tc-p5", "Digits used in page numbering / counting a digit", "common",
        "'How many digits are needed to number a book of N pages?' or the reverse, or 'how many times does digit 5 appear from 1 to 100?'",
        r"\text{Digits} = 9 + 180 + 3(N - 99) \quad (100 \le N \le 999)",
        r"""1. Pages 1–9 use 9 digits, pages 10–99 use 180 digits, each 3-digit page uses 3 digits.
2. Reverse problem: subtract 189, divide the rest by 3, add 99.
3. For counting a digit $d$ (not 0) from 1 to 99: it appears 10 times in the units place and 10 times in the tens place = 20.

Why: each group of numbers has a fixed number of digits.""",
        "How many digits are used to number the pages of a 125-page book?",
        r"$9 + 180 + 3 \times (125 - 99) = 9 + 180 + 78 = 267$.")
    S.pattern("ns-tc-p6", "Two-digit numbers, digit reversal and consecutive numbers", "very common",
        "'If the digits are reversed, the number increases by 27', 'sum of three consecutive even numbers is …'.",
        r"(10a+b) - (10b+a) = 9(a-b),\quad (10a+b) + (10b+a) = 11(a+b)",
        r"""1. Write the number as $10a + b$.
2. Reversal difference gives $a - b$ (divide by 9); reversal sum gives $a + b$ (divide by 11).
3. Consecutive numbers: take the middle one as $x$ (for evens/odds the neighbours are $x \pm 2$). Sum ÷ count = middle number.
4. Or simply test the options.

Why: the tens digit is worth 10 times the units digit, so swapping them changes the value by 9 per unit of difference.""",
        "The sum of five consecutive odd numbers is 135. Find the largest.",
        r"Middle number $= 135 \div 5 = 27$. The numbers are 23, 25, 27, 29, 31. Largest $= 31$.")

    # ---------------- practice ----------------
    def cnt(a, b, k):
        return b // k - (a - 1) // k

    # p1
    v = 499 // 7
    assert v == 71
    S.q("ns-tc-p1", "easy", "How many numbers between 1 and 500 are divisible by 7?",
        ["71", "72", "70", "69"], str(v),
        r"Multiples of 7 below 500: $\lfloor 499/7 \rfloor = 71$ (the largest is $7 \times 71 = 497$).",
        r"$500 \div 7 = 71.4$ → 71.", 30)
    n4, n6, n12 = 1000 // 4, 1000 // 6, 1000 // 12
    v = 1000 - (n4 + n6 - n12)
    assert (n4, n6, n12, v) == (250, 166, 83, 667)
    S.q("ns-tc-p1", "medium", "How many integers from 1 to 1000 are divisible by neither 4 nor 6?",
        ["667", "584", "625", "333"], str(v),
        r"""Divisible by 4: 250. Divisible by 6: 166. Divisible by both = divisible by LCM 12: 83.
Divisible by 4 or 6 $= 250 + 166 - 83 = 333$.
Neither $= 1000 - 333 = 667$.""",
        "Use LCM 12 (not 4 × 6 = 24) for 'both'. Subtracting 250 + 166 directly gives the trap answer 584.", 60)
    a6 = cnt(100, 999, 6)
    a18 = cnt(100, 999, 18)
    v = a6 - a18
    assert (a6, a18, v) == (150, 50, 100)
    S.q("ns-tc-p1", "hard", "How many three-digit numbers are divisible by 6 but not by 9?",
        ["100", "150", "50", "117"], str(v),
        r"""Three-digit multiples of 6: $\lfloor 999/6 \rfloor - \lfloor 99/6 \rfloor = 166 - 16 = 150$.
Those also divisible by 9 are multiples of LCM(6, 9) = 18: $\lfloor 999/18 \rfloor - \lfloor 99/18 \rfloor = 55 - 5 = 50$.
Required $= 150 - 50 = 100$.""",
        "'By 6 but not 9' = multiples of 6 − multiples of 18.", 75)

    # p2
    v = sum(i * i for i in range(1, 16))
    assert v == 15 * 16 * 31 // 6 == 1240
    S.q("ns-tc-p2", "easy", r"What is the value of $1^2 + 2^2 + 3^2 + \dots + 15^2$?",
        ["1240", "1225", "1360", "1180"], str(v),
        r"$\frac{n(n+1)(2n+1)}{6} = \frac{15 \times 16 \times 31}{6} = 1240$.", None, 35)
    v = sum(i ** 3 for i in range(11, 21))
    assert v == 44100 - 3025 == 41075
    S.q("ns-tc-p2", "medium", r"What is the value of $11^3 + 12^3 + 13^3 + \dots + 20^3$?",
        ["41075", "39744", "44100", "40075"], str(v),
        r"""Sum of cubes up to 20 $= \left[\frac{20 \times 21}{2}\right]^2 = 210^2 = 44100$.
Sum of cubes up to 10 $= 55^2 = 3025$.
Required $= 44100 - 3025 = 41075$.""",
        "Subtract the sum up to 10, not up to 11 (that gives the trap 39744).", 60)
    terms = list(range(105, 1000, 7))
    v = sum(terms)
    assert len(terms) == 128 and v == 70336
    S.q("ns-tc-p2", "medium", "What is the sum of all three-digit numbers that are divisible by 7?",
        ["70336", "69237", "71435", "70436"], str(v),
        r"""First three-digit multiple = 105, last = 994.
Number of terms $= \frac{994 - 105}{7} + 1 = 128$.
Sum $= \frac{128}{2}(105 + 994) = 64 \times 1099 = 70336$.""",
        "Sum = number of terms × average of first and last = 128 × 549.5.", 75)

    # p3
    num_s = "34762781"  # 3,47,62,781
    pos = [i for i, c in enumerate(num_s) if c == "7"]
    pv = [7 * 10 ** (len(num_s) - 1 - i) for i in pos]
    v = pv[0] - pv[1]
    assert pv == [700000, 700] and v == 699300
    S.q("ns-tc-p3", "easy", "What is the difference between the place values of the two 7s in 3,47,62,781?",
        [ind(699300), ind(700700), ind(699930), ind(69300)], ind(v),
        r"The first 7 is in the lakhs place → 7,00,000. The second 7 is in the hundreds place → 700. Difference $= 7,00,000 - 700 = 6,99,300$.",
        None, 35)
    v = 3000 * 30
    assert v == 90000
    S.q("ns-tc-p3", "easy", "What is the product of the place values of the two 3s in 53,432?",
        [ind(90000), ind(9000), "9", "900"], ind(v),
        r"In 53,432 the first 3 is in the thousands place (3000) and the second is in the tens place (30). Product $= 3000 \times 30 = 90,000$.",
        None, 30)

    # p4
    def isprime(n):
        return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    v = sum(1 for n in range(51, 100) if isprime(n))
    assert v == 10
    S.q("ns-tc-p4", "easy", "How many prime numbers are there between 50 and 100?",
        ["10", "9", "11", "12"], str(v),
        "The primes are 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 — that is **10** primes.",
        "Remember: 25 primes up to 100 and 15 up to 50, so 25 − 15 = 10.", 40)
    v = sum(n for n in range(61, 80) if isprime(n))
    assert v == 61 + 67 + 71 + 73 + 79 == 351
    S.q("ns-tc-p4", "medium", "What is the sum of all prime numbers between 60 and 80?",
        ["351", "290", "280", "420"], str(v),
        "Primes between 60 and 80: 61, 67, 71, 73, 79. Sum $= 61 + 67 + 71 + 73 + 79 = 351$.",
        "Numbers ending in 1, 3, 7, 9 are the only candidates; strike out 63 (÷3), 69 (÷3), 77 (÷7).", 50)
    assert math.isclose(math.sqrt(8) * math.sqrt(2), 4)
    S.q("ns-tc-p4", "medium", "Which of the following is a rational number?",
        [r"$\sqrt{8} \times \sqrt{2}$", r"$\sqrt{3} + \sqrt{2}$", r"$2\pi$", r"$\sqrt{5} - 1$"], r"$\sqrt{8} \times \sqrt{2}$",
        r"$\sqrt{8} \times \sqrt{2} = \sqrt{16} = 4$, which is rational. $\sqrt{3} + \sqrt{2}$, $2\pi$ and $\sqrt{5} - 1$ are all irrational.",
        "Simplify each option first; only the one that becomes a perfect square root is rational.", 30)

    # p5
    def digits_upto(n):
        return sum(len(str(i)) for i in range(1, n + 1))
    v = digits_upto(350)
    assert v == 942
    S.q("ns-tc-p5", "medium", "How many digits are needed to number the pages of a book having 350 pages?",
        ["942", "939", "1050", "891"], str(v),
        r"""Pages 1–9: 9 digits. Pages 10–99: $90 \times 2 = 180$ digits.
Pages 100–350: $251 \times 3 = 753$ digits.
Total $= 9 + 180 + 753 = 942$.""",
        r"$3N - 108$ for $100 \le N \le 999$: $3 \times 350 - 108 = 942$.", 50)
    v = sum(str(i).count("3") for i in range(1, 101))
    assert v == 20
    S.q("ns-tc-p5", "easy", "How many times does the digit 3 appear when all numbers from 1 to 100 are written?",
        ["20", "19", "11", "21"], str(v),
        "Units place: 3, 13, 23, …, 93 → 10 times. Tens place: 30 to 39 → 10 times. (33 is counted in both, correctly, because it has two 3s.) Total 20.",
        None, 35)
    pages = next(n for n in range(1, 2000) if digits_upto(n) == 1392)
    assert pages == 500
    S.q("ns-tc-p5", "hard", "A total of 1,392 digits were used to number the pages of a book. How many pages does the book have?",
        ["500", "464", "501", "499"], str(pages),
        r"""Digits used by pages 1–99 $= 9 + 180 = 189$.
Remaining digits $= 1392 - 189 = 1203$, each 3-digit page uses 3 → $1203 \div 3 = 401$ pages.
Total pages $= 99 + 401 = 500$.""",
        r"$(1392 + 108) \div 3 = 500$.", 60)

    # p6
    sols = [10 * a + b for a in range(1, 10) for b in range(10)
            if 10 * a + b == 4 * (a + b) and (10 * b + a) - (10 * a + b) == 27]
    assert sols == [36]
    S.q("ns-tc-p6", "medium", "A two-digit number is 4 times the sum of its digits. If 27 is added to the number, its digits are reversed. Find the number.",
        ["36", "63", "24", "48"], "36",
        r"""Let the number be $10a + b$.
$10a + b = 4(a + b) \Rightarrow 6a = 3b \Rightarrow b = 2a$.
Reversal adds 27: $9(b - a) = 27 \Rightarrow b - a = 3$.
So $a = 3, b = 6$ → number $= 36$.""",
        "Check options: 36 = 4 × 9 ✓ and 36 + 27 = 63 ✓.", 45)
    x = 162 // 3
    v = x + 2
    assert (x - 2) + x + (x + 2) == 162 and v == 56
    S.q("ns-tc-p6", "easy", "The sum of three consecutive even numbers is 162. What is the largest of them?",
        ["56", "54", "58", "52"], str(v),
        r"Middle number $= 162 \div 3 = 54$. Numbers: 52, 54, 56. Largest $= 56$.", None, 25)
    sols = [10 * a + b for a in range(1, 10) for b in range(10)
            if (10 * a + b) - (10 * b + a) == 36 and a + b == 10]
    assert sols == [73]
    S.q("ns-tc-p6", "medium", "The sum of the digits of a two-digit number is 10. The number exceeds the number obtained by reversing its digits by 36. Find the number.",
        ["73", "37", "64", "82"], "73",
        r"""Let the number be $10a + b$ with $a + b = 10$.
$(10a + b) - (10b + a) = 9(a - b) = 36 \Rightarrow a - b = 4$.
$a = 7, b = 3$ → number $= 73$.""",
        "Only 73 and 37 have digit sum 10 with gap 4; the number is bigger than its reverse, so 73.", 40)
    return S
