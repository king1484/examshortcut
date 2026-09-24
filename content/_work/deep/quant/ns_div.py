from _lib import Sub, ind


def build():
    S = Sub("ns-divisibility")
    S.notes = r"""### What does "divisible" mean?
A number $N$ is **divisible** by $d$ if $d$ goes into $N$ exactly, with remainder 0. For example 84 is divisible by 7 because 84 = 7 × 12. Divisibility rules let you check this without long division — a big time saver in exams.

### The basic rules
| Divisor | Test | Example |
|---|---|---|
| 2 | last digit even | 3,578 ✓ |
| 3 | sum of digits divisible by 3 | 4,521 → 12 ✓ |
| 4 | last two digits divisible by 4 | 7,316 → 16 ✓ |
| 5 | last digit 0 or 5 | 4,215 ✓ |
| 8 | last three digits divisible by 8 | 91,224 → 224 ✓ |
| 9 | sum of digits divisible by 9 | 6,453 → 18 ✓ |
| 10 | last digit 0 | 560 ✓ |
| 11 | (sum of digits at odd places) − (sum at even places) = 0 or a multiple of 11 | 9,48,475 ✓ |
| 7, 11, 13 | alternating sum of 3-digit groups from the right | 2,47,247 → 247 − 247 = 0 ✓ |

**Rule of 11, step by step.** Take 948475. From the right, odd places hold 5, 4, 4 (sum 13) and even places hold 7, 8, 9 (sum 24). Difference 24 − 13 = 11 → divisible by 11.

### Composite divisors: split into co-prime parts
To test 72, there is no "rule of 72". Write 72 = 8 × 9 (8 and 9 share no factor) and check both rules. Useful splits: 12 = 3 × 4, 18 = 2 × 9, 24 = 3 × 8, 36 = 4 × 9, 44 = 4 × 11, 72 = 8 × 9, 88 = 8 × 11, 99 = 9 × 11.
Do **not** split 24 as 4 × 6 — they share the factor 2, so a number divisible by 4 and 6 (like 36) need not be divisible by 24.

### Missing digits
When digits are hidden (x, y), apply the rule with the **fewest choices first**. The rule of 8 fixes the last three digits; the rule of 11 gives one equation; the digit-sum rule gives another. Often two or three pairs (x, y) work, but x + y (or x − y) is the same in all of them — that is exactly what the question asks.

### Algebraic divisibility (very popular)
- $a^n - b^n$ is always divisible by $a - b$.
- $a^n - b^n$ is divisible by $a + b$ when $n$ is **even**.
- $a^n + b^n$ is divisible by $a + b$ when $n$ is **odd**.
Example: $17^{25} + 23^{25}$ has an odd power, so it is divisible by 17 + 23 = 40.

### Take out the common power
$3^{25} + 3^{26} + 3^{27} = 3^{25}(1 + 3 + 9) = 3^{25} \times 13$. So the sum is divisible by 13. Always factor out the smallest power first.

### Special number forms
- $abcabc = abc \times 1001 = abc \times 7 \times 11 \times 13$.
- $aaa = a \times 111 = a \times 3 \times 37$, so it is always divisible by 37.
- $ab + ba = 11(a + b)$, always divisible by 11. $ab - ba = 9(a - b)$.
- The product of any 3 consecutive integers is divisible by 6 (= 3!).

### Nearest multiple questions
- **Least number to add** to $N$ to make it divisible by $d$: $d - (N \bmod d)$ (0 if already divisible).
- **Least number to subtract**: $N \bmod d$.
- **Largest $n$-digit number** divisible by $d$: $99\dots9 - (99\dots9 \bmod d)$.
- **Smallest $n$-digit number** divisible by $d$: $10\dots0 + (d - 10\dots0 \bmod d)$.
Example: 8,357 ÷ 12 leaves 5, so add 12 − 5 = 7 to get 8,364.

### Quick revision
- 2/5/10 → last digit; 4 → last 2 digits; 8 → last 3 digits; 3/9 → digit sum; 11 → alternating sum.
- Composite divisor → split into co-prime factors only.
- $a^n + b^n$ divisible by $(a+b)$ needs odd $n$; $a^n - b^n$ divisible by $(a-b)$ always.
- abcabc → 7, 11, 13; aaa → 37.
- To reach a multiple: add $d - r$ or subtract $r$.
"""

    S.pattern("ns-dv-p1", "Missing digits for a composite divisor (72, 88, 36, 99)", "very common",
        "A number with blanks x and y 'is divisible by 72/88/99'; the options are values of x + y or x − y.",
        r"72 = 8 \times 9,\ 88 = 8 \times 11,\ 99 = 9 \times 11",
        r"""1. Split the divisor into co-prime factors.
2. Use the rule with fewer possibilities first (8 → last three digits, 11 → alternating sum).
3. Put that value into the second rule (digit sum for 9, alternating sum for 11).
4. List the few cases; the asked quantity is the same in all cases.

Why: a number divisible by two co-prime numbers is divisible by their product, and vice versa.""",
        "If the five-digit number 3x5y2 is divisible by 88, find x + y.",
        r"""$88 = 8 \times 11$. Rule of 8: $5y2$ divisible by 8 → 512, 552, 592 → $y = 1, 5, 9$.
Rule of 11 (from the right): odd places $2 + 5 + 3 = 10$, even places $y + x$. So $10 - (x + y) = 0$ → $x + y = 10$.
Pairs (9, 1), (5, 5), (1, 9) all give **x + y = 10**.""")
    S.pattern("ns-dv-p2", "Divisibility by 11 (single missing digit or pick the number)", "very common",
        "'If 9x8475 is divisible by 11, find x', or 'which of these numbers is divisible by 11?'.",
        r"(\text{sum of odd-place digits}) - (\text{sum of even-place digits}) \in \{0, \pm 11, \pm 22, \dots\}",
        r"""1. Number the digits from the right: 1st, 2nd, 3rd …
2. Add the odd-place digits and the even-place digits separately.
3. The difference must be 0, 11, 22 … Solve for the missing digit (0 to 9).

Why: $10$ leaves remainder $-1$ with 11, so place values alternate between +1 and −1.""",
        "Is 7,29,135 divisible by 11?",
        r"From the right: odd places 5, 1, 2 → 8; even places 3, 9, 7 → 19. Difference $= 11$ → yes, divisible.")
    S.pattern("ns-dv-p3", r"Algebraic divisibility: $a^n \pm b^n$", "very common",
        "Big powers with the same exponent added or subtracted, e.g. '$17^{25} + 23^{25}$ is divisible by'.",
        r"(a-b) \mid a^n - b^n;\quad (a+b) \mid a^n - b^n\ (n \text{ even});\quad (a+b) \mid a^n + b^n\ (n \text{ odd})",
        r"""1. Note whether it is a sum or a difference and whether $n$ is odd or even.
2. Compute $a + b$ and $a - b$ and match with the options.
3. For $a^n - 1$: any $a^k - 1$ where $k$ divides $n$ is a factor.

Why: $a^n - b^n = (a-b)(a^{n-1} + \dots + b^{n-1})$; the sum version works for odd $n$ by replacing $b$ with $-b$.""",
        r"Is $29^{16} - 13^{16}$ divisible by 42?",
        r"$n = 16$ is even, so $a^n - b^n$ is divisible by $a + b = 29 + 13 = 42$. **Yes.**")
    S.pattern("ns-dv-p4", "Sum of powers of the same base: factor out the smallest power", "common",
        r"A sum like $3^{25} + 3^{26} + 3^{27}$ or $5^{21} + 5^{22} + 5^{23}$ and 'is divisible by'.",
        r"a^m + a^{m+1} + a^{m+2} = a^m(1 + a + a^2)",
        r"""1. Take the smallest power outside the bracket.
2. Simplify the bracket to a small number.
3. The number is divisible by that bracket value (and by powers of the base).

Why: every term shares the smallest power as a common factor.""",
        r"Find a factor of $4^{61} + 4^{62} + 4^{63}$ other than a power of 2.",
        r"$4^{61}(1 + 4 + 16) = 4^{61} \times 21$. So it is divisible by 21 (and by 3 and 7).")
    S.pattern("ns-dv-p5", "Least number to add/subtract; largest or smallest n-digit multiple", "very common",
        "'What least number must be added to/subtracted from N so that it is divisible by d?', 'largest five-digit number divisible by 47'.",
        r"\text{add} = d - (N \bmod d),\quad \text{subtract} = N \bmod d",
        r"""1. Divide $N$ by $d$ and find the remainder $r$.
2. Subtract $r$ (goes down to the lower multiple) or add $d - r$ (goes up to the next multiple).
3. Largest $n$-digit multiple: $99\dots9 - r$. Smallest $n$-digit multiple: $10\dots0 + (d - r)$.

Why: multiples of $d$ are $d$ apart, and the remainder tells how far $N$ is above the lower one.""",
        "What least number must be subtracted from 4,527 to make it divisible by 16?",
        r"$4527 = 16 \times 282 + 15$. Subtract the remainder **15**. Check: $4512 = 16 \times 282$.")
    S.pattern("ns-dv-p6", "Special forms: abcabc, aaa, ab + ba", "common",
        "'A six-digit number formed by repeating a three-digit number is always divisible by …', 'a three-digit number with all digits equal'.",
        r"abcabc = 1001 \times abc = 7 \times 11 \times 13 \times abc,\quad aaa = 3 \times 37 \times a",
        r"""1. Write the number in expanded form.
2. Take out the fixed factor (1001, 111, 11, 9).
3. Choose the option that divides this fixed factor.

Why: the pattern of the digits builds in a fixed multiplier, whichever digits are used.""",
        "Is 4,84,484 divisible by 13? (It is 484 written twice.)",
        r"$484484 = 484 \times 1001$ and $1001 = 7 \times 11 \times 13$. So **yes**, it is divisible by 13.")

    # practice ---------------------------------------------------------
    def sols(tmpl, d):
        out = []
        for x in range(10):
            for y in range(10):
                s = tmpl.replace("x", str(x)).replace("y", str(y))
                if s[0] != "0" and int(s) % d == 0:
                    out.append((x, y))
        return out

    s = sols("6x52y4", 72)
    assert s == [(4, 6), (8, 2)] and {a + b for a, b in s} == {10}
    S.q("ns-dv-p1", "hard", "If the six-digit number 6x52y4 is divisible by 72, what is the value of x + y?",
        ["10", "8", "12", "14"], "10",
        r"""$72 = 8 \times 9$.
**Rule of 8:** $2y4$ must be divisible by 8 → 224 or 264 → $y = 2$ or $y = 6$.
**Rule of 9:** digit sum $6 + x + 5 + 2 + y + 4 = 17 + x + y$ must be a multiple of 9 → $x + y = 1$ or $10$.
- $y = 2$: $x + y$ cannot be 1, so $x + y = 10$ → $x = 8$ (685224 ✓).
- $y = 6$: $x + y = 10$ → $x = 4$ (645264 ✓).
In both cases $x + y = 10$.""",
        "Digit sum 17 + (x + y) must reach 27 because y ≥ 2 rules out x + y = 1. So x + y = 10.", 90)
    s = sols("8x6y4", 88)
    assert s == [(1, 6), (5, 2)] and {a + b for a, b in s} == {7}
    S.q("ns-dv-p1", "medium", "If the five-digit number 8x6y4 is divisible by 88, what is the value of x + y?",
        ["7", "9", "5", "11"], "7",
        r"""$88 = 8 \times 11$.
**Rule of 8:** $6y4$ divisible by 8 → 624 or 664 → $y = 2$ or $6$.
**Rule of 11:** from the right, odd places $4 + 6 + 8 = 18$ and even places $y + x$. So $18 - (x + y)$ must be 0 or 11 → $x + y = 18$ or $7$.
$x + y = 18$ needs $x = y = 9$, but $y$ is 2 or 6. So $x + y = 7$ (numbers 85624 and 81664 both work).""",
        "Rule of 11 gives x + y = 7 or 18; 18 is impossible here → 7.", 75)
    s = sols("4x7y8", 72)
    assert s == [(2, 6), (6, 2)] and {abs(a - b) for a, b in s} == {4}
    S.q("ns-dv-p1", "medium", r"If the five-digit number 4x7y8 is divisible by 72, what is the value of $|x - y|$?",
        ["4", "8", "2", "6"], "4",
        r"""**Rule of 8:** $7y8$ divisible by 8 → 728 or 768 → $y = 2$ or $6$.
**Rule of 9:** $4 + x + 7 + y + 8 = 19 + x + y$ must be 27 → $x + y = 8$.
$y = 2 \Rightarrow x = 6$; $y = 6 \Rightarrow x = 2$. In both cases $|x - y| = 4$.""",
        None, 75)

    t = "9x8475"
    xs = [x for x in range(10) if int(t.replace("x", str(x))) % 11 == 0]
    assert xs == [4]
    S.q("ns-dv-p2", "easy", "If the six-digit number 9x8475 is divisible by 11, what is the value of x?",
        ["4", "3", "5", "7"], "4",
        r"""From the right: odd places 5, 4, x → $9 + x$; even places 7, 8, 9 → 24.
Difference $24 - (9 + x) = 15 - x$ must be 0 or 11 → $x = 4$.""",
        "15 − x = 11 → x = 4.", 35)
    opts = ["4,74,881", "4,74,871", "5,38,921", "5,83,261"]
    div = [o for o in opts if int(o.replace(",", "")) % 11 == 0]
    assert div == ["4,74,881"]
    S.q("ns-dv-p2", "medium", "Which of the following numbers is divisible by 11?",
        opts, div[0],
        r"""Use (odd-place sum) − (even-place sum), places counted from the right.
- 474881: odd places 1, 8, 7 → 16; even places 8, 4, 4 → 16; difference 0 ✓.
- 474871: 1 + 8 + 7 = 16 vs 7 + 4 + 4 = 15 → 1 ✗.
- 538921: 1 + 9 + 3 = 13 vs 2 + 8 + 5 = 15 → 2 ✗.
- 583261: 1 + 2 + 8 = 11 vs 6 + 3 + 5 = 14 → 3 ✗.""",
        None, 50)

    b = 17 ** 25 + 23 ** 25
    opts = ["40", "6", "17", "23"]
    assert [o for o in opts if b % int(o) == 0] == ["40"]
    S.q("ns-dv-p3", "easy", r"The number $17^{25} + 23^{25}$ is divisible by:",
        opts, "40",
        r"$a^n + b^n$ with odd $n$ is divisible by $a + b$. Here $n = 25$ is odd, so it is divisible by $17 + 23 = 40$.",
        "Odd power + sum → divide by (a + b). 6 = 23 − 17 would need a difference.", 30)
    c = 7 ** 24 - 1
    opts = ["48", "49", "46", "56"]
    assert [o for o in opts if c % int(o) == 0] == ["48"]
    S.q("ns-dv-p3", "medium", r"Which of the following divides $7^{24} - 1$?",
        opts, "48",
        r"""$7^{24} - 1 = (7^2)^{12} - 1^{12}$, which is divisible by $7^2 - 1 = 48$.
It is not divisible by 49 or 56 (both are multiples of 7, but $7^{24} - 1$ leaves remainder $-1$ with 7), and not by 46.""",
        r"$a^n - 1$ is divisible by $a^k - 1$ whenever $k$ divides $n$: $k = 2$ gives 48.", 50)
    x = 19 ** 32 - 11 ** 32
    opts = ["30", "8", "both 30 and 8", "neither 30 nor 8"]
    assert x % 30 == 0 and x % 8 == 0
    S.q("ns-dv-p3", "hard", r"$19^{32} - 11^{32}$ is divisible by:",
        opts, "both 30 and 8",
        r"""$a^n - b^n$ is always divisible by $a - b = 8$.
Since $n = 32$ is even, it is also divisible by $a + b = 30$.
So it is divisible by **both 30 and 8**.""",
        "Even power difference → both (a − b) and (a + b).", 45)

    e = 5 ** 21 + 5 ** 22 + 5 ** 23
    opts = ["31", "29", "21", "23"]
    assert [o for o in opts if e % int(o) == 0] == ["31"]
    S.q("ns-dv-p4", "easy", r"$5^{21} + 5^{22} + 5^{23}$ is divisible by:",
        opts, "31",
        r"$5^{21}(1 + 5 + 25) = 5^{21} \times 31$. So the number is divisible by **31**.",
        None, 30)
    e = 2 ** 30 + 2 ** 31 + 2 ** 32 + 2 ** 33
    opts = ["15", "13", "7", "9"]
    assert [o for o in opts if e % int(o) == 0] == ["15"]
    S.q("ns-dv-p4", "medium", r"Which of the following is a factor of $2^{30} + 2^{31} + 2^{32} + 2^{33}$?",
        opts, "15",
        r"$2^{30}(1 + 2 + 4 + 8) = 2^{30} \times 15$. So **15** is a factor. The other options (13, 7, 9) do not divide $2^{30} \times 15$.",
        "Bracket 1 + 2 + 4 + 8 = 15.", 35)

    r = 8357 % 12
    v = 12 - r
    assert (r, v) == (5, 7)
    S.q("ns-dv-p5", "easy", "What least number must be added to 8,357 so that the sum is exactly divisible by 12?",
        ["7", "5", "3", "11"], str(v),
        r"$8357 = 12 \times 696 + 5$. The remainder is 5, so add $12 - 5 = 7$. Check: $8364 = 12 \times 697$.",
        "Trap: 5 is the number to subtract, not add.", 35)
    v = 99999 - 99999 % 47
    assert v == 99969
    S.q("ns-dv-p5", "medium", "What is the largest five-digit number exactly divisible by 47?",
        [ind(99969), ind(99952), ind(99999), ind(99922)], ind(v),
        r"$99999 = 47 \times 2127 + 30$. Subtract the remainder: $99999 - 30 = 99969$.",
        None, 45)
    v = 100000 + (111 - 100000 % 111)
    assert v == 100011 and v % 111 == 0
    S.q("ns-dv-p5", "medium", "What is the smallest six-digit number exactly divisible by 111?",
        [ind(100011), ind(100000), ind(100111), ind(100089)], ind(v),
        r"$100000 = 111 \times 900 + 100$. Remainder 100, so add $111 - 100 = 11$ → $1,00,011$.",
        "Smallest n-digit multiple = 10…0 + (d − r).", 45)

    assert all(int(f"{n}{n}") == n * 1001 for n in range(100, 1000))
    S.q("ns-dv-p6", "easy", "A six-digit number is formed by writing a three-digit number twice (for example 257257). Such a number is always divisible by:",
        ["7, 11 and 13", "only 7", "only 11 and 13", "3 and 7"], "7, 11 and 13",
        r"$abcabc = abc \times 1000 + abc = abc \times 1001$ and $1001 = 7 \times 11 \times 13$. So it is always divisible by 7, 11 and 13.",
        None, 30)
    assert all(int(str(a) * 3) % 37 == 0 for a in range(1, 10))
    assert any(int(str(a) * 3) % 27 for a in range(1, 10)) and any(int(str(a) * 3) % 11 for a in range(1, 10)) and any(int(str(a) * 3) % 19 for a in range(1, 10))
    S.q("ns-dv-p6", "medium", "A three-digit number has all its digits equal (like 444). It is always divisible by:",
        ["37", "27", "11", "19"], "37",
        r"$aaa = 100a + 10a + a = 111a = 3 \times 37 \times a$. So it is always divisible by **37**. (It is divisible by 27 only for some digits, e.g. 999.)",
        None, 30)
    return S
