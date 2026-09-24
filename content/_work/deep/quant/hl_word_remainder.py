"""Phase-2 deep content for quant/hcf-lcm — word problems & remainder cases."""
import os
import sys
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def lcm(a, b):
    return a * b // gcd(a, b)


def build_word():
    S = Sub("hl-word-problems")
    S.notes = r"""### The template table — decide HCF or LCM in five seconds
| Question wording | Tool |
|---|---|
| Greatest number that **divides** a, b, c (exactly, or with remainders) | HCF |
| Least number **divisible by** a, b, c | LCM |
| Largest tile / rod / measure / biggest equal group | HCF |
| Bells or lights ringing **together**, laps meeting again | LCM |
| Least number leaving **remainder r with every divisor** | LCM + r |
| Greatest number leaving **remainder r with every divisor** | HCF of (number − r) |
| Remainder = divisor − c in every case | LCM − c (least value) |

### Why the two remainder rules work
If N leaves remainder r with every divisor, then N − r is exactly divisible by all of them.
- The smallest positive value of N − r is the **LCM**, so the least such N is LCM + r.
- The **greatest** number dividing all the (number − r) values is their **HCF**.
Example: least number leaving remainder 5 with 12, 15, 20 → LCM $= 540$ → answer 545.

### When the remainders differ
If each remainder is exactly c less than its divisor, then N + c is divisible by every divisor, so the least N is **LCM − c**.
Example: remainders 5, 8, 11 with divisors 6, 9, 12 — each is divisor − 1 → N $= 36 - 1 = 35$. Check: $35 = 5 \times 6 + 5 = 3 \times 9 + 8 = 2 \times 12 + 11$ ✓.

### Bells, lights and laps
Convert all intervals to the **same unit**, take the LCM, then:
- next time together = start time + LCM;
- how many times together within T: divide T by the LCM (add 1 if the moment of starting counts).
Example: bells every 9, 12, 15 minutes, together at 8 a.m. → LCM $= 180$ min $= 3$ h → next together 11 a.m.

### Tiles, rods, measures and groups
- Largest square tile: side = HCF of the length and breadth (**same units first**); number of tiles = $\frac{L \times B}{\text{side}^2}$.
- Longest rod / biggest vessel: HCF of the dimensions or capacities; the count is total ÷ HCF.
- Biggest equal groups (men and women split into identical teams): HCF of the counts.
Example: containers of 144 L, 180 L, 240 L — largest vessel $= \gcd = 12$ L.

### Units and classic traps
- Convert everything first: 15 m 17 cm $= 1517$ cm; 2 hours $= 120$ minutes.
- "Divides … leaving remainder" → subtract the remainders, then HCF. "Divisible by" → LCM. Mixing these up is the number-one error in this topic.
- For LCM + r questions, other valid values are LCM·k + r — but the question asks for the **least**, so take k = 1.
- A remainder must be **smaller than its divisor**; if your answer is not, you stopped one step early.

### Quick revision
- Divides with remainders → subtract remainders, take HCF.
- Same remainder, least value → LCM + r; remainder = divisor − c → LCM − c.
- Bells and laps: LCM, then add to the clock or count windows.
- Tiles and rods: HCF first, then divide the area or the total.
"""

    S.pattern("hl-w1", "Greatest number dividing with given remainders (HCF of differences)", "very common",
        "'Find the greatest number which divides a, b, c leaving remainders r1, r2, r3.'",
        r"\text{answer} = \gcd(a - r_1,\ b - r_2,\ c - r_3)",
        r"""1. Subtract each remainder from its number: N − r is exactly divisible by the answer.
2. Take the HCF of the results.
3. Check the answer is bigger than every remainder.

Why: the unknown divisor divides N − r for every N, so it is a common factor — and the greatest one is the HCF.""",
        "Find the greatest number which divides 85 and 72 leaving remainders 1 and 2 respectively.",
        r"$85 - 1 = 84$, $72 - 2 = 70$; $\gcd(84, 70) = 14$. Check: $85 = 6 \times 14 + 1$, $72 = 5 \times 14 + 2$.")
    S.pattern("hl-w2", "Least number leaving the same remainder r (LCM + r)", "very common",
        "'Find the least number which when divided by a, b, c leaves remainder r in each case.'",
        r"N = \text{LCM}(a, b, c) \times k + r \ \ (k = 1 \text{ for the least positive value})",
        r"""1. Take the LCM of the divisors.
2. Add the remainder r.
3. If a bound appears (greater than 10 000, four-digit, …), fit N = LCM·k + r into the range.

Why: N − r must be a common multiple of all divisors; the least positive common multiple is the LCM.""",
        "Find the least number which when divided by 8, 12, 15 and 20 leaves remainder 4 in each case.",
        r"LCM$(8, 12, 15, 20) = 120$ → least number $= 120 + 4 = 124$. (244 also works but is not the least.)")
    S.pattern("hl-w3", "Remainder is (divisor − c) each time (LCM − c)", "common",
        "Remainders differ, but each one is a fixed amount less than its divisor: like 2, 3, 4 with divisors 3, 4, 5.",
        r"r_i = d_i - c \Rightarrow N = \text{LCM}(d_1, d_2, \dots) \times k - c",
        r"""1. Confirm each divisor minus its remainder is the same number c.
2. N + c is divisible by every divisor → N = LCM − c for the least value.
3. Bigger values are LCM·k − c if a bound is given.

Why: adding c to N repairs every division to an exact one, so N + c is a common multiple.""",
        "Find the least number which when divided by 6, 9 and 12 leaves remainders 5, 8 and 11 respectively.",
        r"Each remainder is divisor − 1 → N $= \text{LCM}(6, 9, 12) - 1 = 36 - 1 = 35$. Check: $35 \bmod 6 = 5$, $35 \bmod 9 = 8$, $35 \bmod 12 = 11$.")
    S.pattern("hl-w4", "Bells, lights and laps meeting again (LCM + clock)", "common",
        "Bells toll or lights change at different intervals, start together, and the question asks when they next coincide or how often in a window.",
        r"\text{gap} = \text{LCM}(\text{intervals}); \quad \#\text{times in } T = \left\lfloor \frac{T}{\text{LCM}} \right\rfloor \ (+1 \text{ if the start counts})",
        r"""1. Convert every interval to the same unit.
2. LCM of the intervals = the gap between coincidences.
3. Add to the start time, or divide the window by the gap to count.
4. Decide whether the start counts — the wording tells you.

Why: two events with periods a and b coincide exactly at common multiples of a and b; the least one is the LCM.""",
        "Three bells toll at intervals of 9, 12 and 15 minutes and toll together at 8 a.m. When do they next toll together?",
        r"LCM$(9, 12, 15) = 180$ minutes $= 3$ hours → 8 a.m. + 3 h $=$ **11 a.m.**")
    S.pattern("hl-w5", "Largest tile, rod, measure or equal group (HCF)", "common",
        "Pave with the largest square tiles, cut planks of greatest equal length, fill containers with the biggest vessel, form biggest equal groups.",
        r"\text{side/length} = \gcd(\text{dimensions}); \quad \#\text{tiles} = \frac{L \times B}{h^2}, \quad \#\text{pieces} = \frac{\text{total length}}{h}",
        r"""1. Convert all measurements to one unit.
2. HCF of the dimensions (or capacities / counts) is the answer's size.
3. Divide the total by the HCF to get how many tiles, pieces or groups.

Why: the tile or rod must fit each dimension a whole number of times — it is a common divisor, so the largest one is the HCF.""",
        "What is the largest vessel which can fill containers of 144 L, 180 L and 240 L exactly, and how many times does it fill the 240 L one?",
        r"$\gcd(144, 180, 240) = 12$ L; $240 \div 12 = 20$ fills.")

    assert gcd(gcd(40, 88), 180) == 4
    S.q("hl-w1", "easy",
        "Find the greatest number which divides 43, 91 and 183 leaving the same remainder 3 in each case.",
        ["4", "8", "12", "6"], "4",
        r"""Subtract 3 everywhere: 40, 88, 180.
$\gcd(40, 88) = 8$; $\gcd(8, 180) = 4$. Answer $= 4$ (and $4 > 3$ ✓).""",
        "Trap 8: it divides 40 and 88 but not 180 — check all three numbers.", 40)
    assert gcd(gcd(78, 143), 221) == 13
    assert 82 % 13 == 4 and 150 % 13 == 7 and 233 % 13 == 12
    S.q("hl-w1", "medium",
        "Find the greatest number which divides 82, 150 and 233 leaving remainders 4, 7 and 12 respectively.",
        ["13", "26", "39", "17"], "13",
        r"""Subtract the remainders: $82 - 4 = 78$, $150 - 7 = 143$, $233 - 12 = 221$.
$78 = 6 \times 13$, $143 = 11 \times 13$, $221 = 17 \times 13$ → HCF $= 13$ (greater than every remainder ✓).""",
        None, 50)
    assert lcm(lcm(lcm(8, 12), 15), 20) == 120
    S.q("hl-w2", "easy",
        "Find the least number which when divided by 8, 12, 15 and 20 leaves a remainder of 4 in each case.",
        ["124", "120", "116", "244"], "124",
        r"""LCM$(8, 12, 15, 20) = 120$ → least number $= 120 + 4 = 124$.
Check: $124 = 15 \times 8 + 4 = 10 \times 12 + 4 = 8 \times 15 + 4 = 6 \times 20 + 4$ ✓.""",
        None, 40)
    L = lcm(lcm(lcm(15, 18), 24), 30)
    assert L == 360
    N = 28 * 360 + 9
    assert N == 10089 and all(N % d == 9 for d in (15, 18, 24, 30)) and N > 10000 and (N - 360) < 10000
    S.q("hl-w2", "hard",
        "Find the least number greater than 10000 which when divided by 15, 18, 24 and 30 leaves a remainder of 9 in each case.",
        ["10089", "9731", "10080", "10449"], "10089",
        r"""LCM$(15, 18, 24, 30) = 360$ → numbers are $360k + 9$.
$27 \times 360 + 9 = 9729$ (too small); $28 \times 360 + 9 = 10089$ ✓.
Check: $10080$ is divisible by all four, so 10089 leaves 9 each time ✓.""",
        "9731 fits the pattern but is below 10000; 10080 leaves remainder 0.", 75)
    assert 36 - 1 == 35 and all(35 % d == d - 1 for d in (6, 9, 12))
    S.q("hl-w3", "easy",
        "Find the least number which when divided by 6, 9 and 12 leaves remainders 5, 8 and 11 respectively.",
        ["35", "36", "71", "107"], "35",
        r"""Each remainder is 1 less than its divisor → N + 1 is divisible by 6, 9 and 12.
LCM $= 36$ → N $= 36 - 1 = 35$.
Check: $35 = 5 \times 6 + 5 = 3 \times 9 + 8 = 2 \times 12 + 11$ ✓.""",
        None, 40)
    L = lcm(lcm(7, 8), 9)
    assert L == 504 and all(502 % d == d - 2 for d in (7, 8, 9))
    S.q("hl-w3", "medium",
        "Find the least number which when divided by 7, 8 and 9 leaves remainders 5, 6 and 7 respectively.",
        ["502", "504", "506", "495"], "502",
        r"""Each remainder is 2 less than its divisor → N + 2 is divisible by 7, 8 and 9.
LCM$(7, 8, 9) = 504$ → N $= 504 - 2 = 502$.
Check: $502 = 71 \times 7 + 5 = 62 \times 8 + 6 = 55 \times 9 + 7$ ✓.""",
        None, 45)
    assert lcm(lcm(12, 18), 24) == 72
    S.q("hl-w4", "medium",
        "Three runners start together on a circular track, completing one lap in 12, 18 and 24 minutes respectively. After how many minutes will they be together at the starting point again?",
        ["72", "54", "96", "36"], "72",
        r"""They meet at the start after a common multiple of 12, 18 and 24 minutes.
LCM $= 2^3 \times 3^2 = 72$ minutes.""",
        r"36 fails: $36 \div 24$ is not a whole number of laps for the third runner.", 45)
    assert lcm(lcm(lcm(lcm(lcm(2, 4), 6), 8), 10), 12) == 120
    assert 1800 // 120 == 15
    S.q("hl-w4", "medium",
        "Six bells commence tolling together and then toll at intervals of 2, 4, 6, 8, 10 and 12 seconds. In 30 minutes, how many times do they toll together, counting the toll at the very start?",
        ["16", "15", "17", "25"], "16",
        r"""LCM$(2, 4, 6, 8, 10, 12) = 120$ s $= 2$ min.
In 30 min there are $\frac{30}{2} = 15$ coincidences **after** the start; counting the start itself → $15 + 1 = 16$.""",
        None, 50)
    assert gcd(gcd(144, 180), 240) == 12 and 240 // 12 == 20
    S.q("hl-w5", "easy",
        "What is the capacity of the largest vessel which can fill containers of 144 litres, 180 litres and 240 litres an exact number of times? Also, how many such fills empty the 240-litre container?",
        ["12 L, 20 fills", "12 L, 18 fills", "24 L, 10 fills", "6 L, 40 fills"], "12 L, 20 fills",
        r"""Largest vessel $= \gcd(144, 180, 240) = 12$ litres.
Fills for the 240 L container: $240 \div 12 = 20$.""",
        None, 40)
    g = gcd(1260, 720)
    assert g == 180 and (1260 + 720) // g == 11
    S.q("hl-w5", "medium",
        "Two rods measure 12 m 60 cm and 7 m 20 cm. They are cut into pieces of equal length, the length being the greatest possible. Find the length of a piece and the total number of pieces.",
        ["1 m 80 cm, 11 pieces", "90 cm, 22 pieces", "3 m 60 cm, 5 pieces", "60 cm, 33 pieces"], "1 m 80 cm, 11 pieces",
        r"""In centimetres: 1260 and 720. Greatest length $= \gcd(1260, 720) = 180$ cm $= 1$ m 80 cm.
Total pieces $= \frac{1260 + 720}{180} = \frac{1980}{180} = 11$ (7 from the long rod + 4 from the short one).""",
        "90 cm and 60 cm also measure both rods exactly, but the question wants the greatest length.", 55)
    g = gcd(1296, 832)
    assert g == 16 and (1296 // 16) * (832 // 16) == 81 * 52 == 4212
    S.q("hl-w5", "hard",
        "A hall 12 m 96 cm long and 8 m 32 cm broad is to be paved with the least number of square tiles of the same size. Find the number of tiles.",
        ["4212", "4422", "4096", "4312"], "4212",
        r"""In centimetres: 1296 × 832. Largest tile side $= \gcd(1296, 832) = 16$ cm.
Tiles $= \frac{1296 \times 832}{16 \times 16} = 81 \times 52 = 4212$.""",
        "Convert metres to centimetres first — skipping that gives nonsense options.", 80)
    return S


def build_remainder():
    S = Sub("hl-remainder-cases")
    S.notes = r"""### The master frame: N = LCM·k + r
Every remainder question reduces to $N = L \cdot k + r$, where $L$ is the LCM of the divisors. $k = 1$ gives the least positive value; larger k gives later values in the same pattern. Any extra condition simply pins down k.

### Extra condition: the number must also be divisible by p
1. Write $N = Lk + r$.
2. Try $k = 1, 2, 3, \dots$ until $Lk + r$ is divisible by p (or solve $Lk \equiv -r \pmod p$).
Example: N divided by 4, 6, 9 leaves remainder 1 in each case, and N is divisible by 11.
$L = 36$ → $N = 36k + 1$: k = 7 gives $253 = 11 \times 23$ ✓ → N $= 253$.

### Least / greatest n-digit numbers
1. Take $L = $ LCM of the divisors.
2. Least n-digit: divide 10…0 by L and step up to the next multiple.
3. Greatest n-digit: divide 99…9 by L and subtract the remainder.
4. With a remainder r, fit $N = Lk + r$ inside the digit range.
Example: least 5-digit number divisible by 32, 36, 40, 45, 48 → $L = 1440$; $10000 = 6 \times 1440 + 1360$ → add $1440 - 1360 = 80$ → **10080**.

### Rebuilding numbers from HCF and LCM
Numbers with HCF h can be written $ha$ and $hb$ with $\gcd(a, b) = 1$, and $ab = \frac{\text{LCM}}{h}$.
1. Compute $ab$.
2. List the factor pairs of $ab$; keep only the **co-prime** pairs.
3. Use the given sum or difference to pick the pair; the numbers are $ha$ and $hb$.
Example: HCF 5, LCM 495, sum 100 → $ab = 99$ → pairs (1, 99) and (9, 11); the sum needs $a + b = 20$ → (9, 11) → numbers 45 and 55.

### How many pairs are possible?
Count the co-prime factor pairs of $ab = \frac{\text{LCM}}{h}$ (or $\frac{\text{product}}{h^2}$ when the product is given). Do not forget the pair (1, ab) itself, and never count (a, b) and (b, a) as different pairs.
Example: product 2160, HCF 12 → $ab = \frac{2160}{144} = 15$ → (1, 15), (3, 5) → **2 pairs**.

### Same unknown remainder → HCF of the pairwise differences
If a, b, c leave the **same** (unknown) remainder, the answer divides $a - b$, $b - c$, $a - c$ — so it is the HCF of the pairwise differences. The common remainder is then a mod (answer).
Example: greatest number dividing 84, 156, 204 leaving the same remainder: differences 72, 120, 48 → HCF $= 24$, and the remainder is $84 \bmod 24 = 12$ in each case.

### Quick revision
- $N = Lk + r$: extra condition → test k = 1, 2, 3, …
- n-digit: step up from 10…0 or step down from 99…9.
- Rebuild: numbers $= ha, hb$ with $ab = \text{LCM} \div h$, co-prime parts.
- Pair count: co-prime factor pairs of LCM/H (or product/H²).
- Unknown same remainder → HCF of the pairwise differences.
"""

    S.pattern("hl-r1", "Least / greatest n-digit number divisible by a set", "very common",
        "'Find the least four-digit number exactly divisible by 12, 15, 20' or the greatest such five-digit number.",
        r"\text{least: next multiple of } L \ge 10^{n-1}; \qquad \text{greatest: } 10^n - 1 - ((10^n - 1) \bmod L), \quad L = \text{LCM}",
        r"""1. Take L = LCM of the divisors.
2. Least: divide the smallest n-digit number by L, subtract the remainder from L, add to the base.
3. Greatest: divide 99…9 by L and subtract the remainder.
4. Add the remainder r first if the question says 'leaves remainder r': work with Lk + r inside the range.

Why: multiples of the LCM are exactly the numbers divisible by every divisor; the digit bounds just pick where to stop.""",
        "Find the least five-digit number exactly divisible by 32, 36, 40, 45 and 48.",
        r"$L = 1440$; $10000 = 6 \times 1440 + 1360$ → add $1440 - 1360 = 80$ → **10080**.")
    S.pattern("hl-r2", "LCM + r with an extra condition (divisible by p, or a digit bound)", "common",
        "'…leaves remainder r in each case, and is exactly divisible by 11' — an LCM + r question with one more filter.",
        r"N = Lk + r, \qquad Lk + r \equiv 0 \pmod p \ \Rightarrow\ \text{smallest } k \text{ wins}",
        r"""1. Write N = L·k + r with L = LCM of the divisors.
2. Test k = 1, 2, 3, … until L·k + r is divisible by p (small k values click fast).
3. If an n-digit bound is given, start k just above (bound − r) ÷ L.

Why: N − r is a multiple of L by construction; the extra condition only chooses which multiple.""",
        "Find the least number which divided by 4, 6 and 9 leaves remainder 1 in each case, and is exactly divisible by 11.",
        r"$L = 36$ → N = 37, 73, 109, …, and $253 = 11 \times 23$ (k = 7) → **253**.")
    S.pattern("hl-r3", "Rebuild numbers from HCF & LCM; count possible pairs", "common",
        "HCF and LCM are given, plus a sum/difference/bound — find the numbers or count how many pairs fit.",
        r"\text{numbers} = ha, hb;\ \ \gcd(a, b) = 1,\quad ab = \frac{\text{LCM}}{h} \ \left(= \frac{\text{product}}{h^2}\right)",
        r"""1. Compute $ab = \text{LCM} \div h$ (or product ÷ h²).
2. List factor pairs of ab; KEEP only co-prime pairs — the rest are impossible.
3. Use the given sum/difference/bound to pick the pair; numbers are h·a and h·b.
4. To count pairs: count the surviving co-prime pairs.

Why: two numbers with HCF h are h times two co-prime parts, and those parts must multiply to LCM ÷ h.""",
        "The HCF and LCM of two numbers are 5 and 495 and their sum is 100. Find the numbers.",
        r"$ab = 99$ → co-prime pairs (1, 99), (9, 11); sum needs $a + b = 20$ → (9, 11) → numbers **45 and 55**.")
    S.pattern("hl-r4", "Greatest number dividing with the same unknown remainder", "common",
        "'Find the greatest number which divides a, b, c leaving the same remainder in each case' — no remainder is given.",
        r"\text{answer} = \gcd(a - b,\ b - c,\ a - c), \qquad \text{remainder} = a \bmod \text{answer}",
        r"""1. Take the pairwise differences of the numbers.
2. Their HCF is the greatest such divisor.
3. The common remainder is any number mod that HCF — check it is the same for all.

Why: if a and b leave the same remainder r, their difference is exactly divisible by the divisor; so the divisor is a common factor of all differences.""",
        "Find the greatest number which divides 84, 156 and 204 leaving the same remainder in each case.",
        r"Differences: 72, 48, 120 → HCF $= 24$; remainder $84 \bmod 24 = 12$ (same for all three).")

    L = lcm(lcm(42, 63), 84)
    assert L == 252
    N = 99999 - 99999 % L
    assert N == 99792 and all(N % d == 0 for d in (42, 63, 84))
    S.q("hl-r1", "medium",
        "Find the greatest number of five digits which is exactly divisible by 42, 63 and 84.",
        ["99792", "99540", "99960", "99288"], "99792",
        r"""LCM$(42, 63, 84) = 2^2 \times 3^2 \times 7 = 252$.
$99999 \div 252$ leaves remainder 207 → greatest multiple $= 99999 - 207 = 99792$.
Check: $99792 = 396 \times 252$ ✓.""",
        "99540 and 99288 are earlier multiples of 252 — not the greatest.", 60)
    L = lcm(lcm(9, 12), 16)
    assert L == 144
    N = 7 * 144 + 3
    assert N == 1011 and all(N % d == 3 for d in (9, 12, 16)) and N >= 1000
    S.q("hl-r1", "hard",
        "Find the least four-digit number which when divided by 9, 12 and 16 leaves a remainder of 3 in each case.",
        ["1011", "1003", "1155", "1008"], "1011",
        r"""LCM$(9, 12, 16) = 144$ → numbers are $144k + 3$.
$6 \times 144 + 3 = 867$ (three digits); $7 \times 144 + 3 = 1011$ ✓.
Check: $1008$ is divisible by all three, so 1011 leaves remainder 3 each time ✓.""",
        "1003 is 1000 + 3 — it ignores the LCM structure.", 70)
    N = 253
    assert all(N % d == 1 for d in (4, 6, 9)) and N % 11 == 0 and lcm(lcm(4, 6), 9) == 36
    S.q("hl-r2", "hard",
        "Find the least number which when divided by 4, 6 and 9 leaves a remainder of 1 in each case, and which is exactly divisible by 11.",
        ["253", "109", "397", "541"], "253",
        r"""LCM$(4, 6, 9) = 36$ → $N = 36k + 1$.
Test k: 37, 73, 109, 145, 181, 217, 253 — and $253 = 11 \times 23$ ✓ → N $= 253$.""",
        "109 also leaves remainder 1 each time but is not divisible by 11.", 80)
    L = lcm(lcm(8, 12), 16)
    assert L == 48
    N = 99999 - (99999 % 48) + 3
    assert N == 99987 and all(N % d == 3 for d in (8, 12, 16))
    S.q("hl-r2", "medium",
        "Find the greatest number of five digits which when divided by 8, 12 and 16 leaves a remainder of 3 in each case.",
        ["99987", "99939", "99951", "99971"], "99987",
        r"""LCM$(8, 12, 16) = 48$; $99999 = 2083 \times 48 + 15$ → greatest multiple of 48 is 99984.
Answer $= 99984 + 3 = 99987$.
Check: $99984$ is divisible by all three, so 99987 leaves 3 each time ✓.""",
        "99939 is 48 less — valid but not the greatest.", 60)
    a, b = 18, 24
    assert gcd(a, b) == 6 and lcm(a, b) == 72 and a + b == 42 and b - a == 6
    valid = [(x * 6, y * 6) for x, y in [(1, 12), (3, 4)]]
    assert valid == [(6, 72), (18, 24)] and [p for p in valid if sum(p) == 42] == [(18, 24)]
    S.q("hl-r3", "medium",
        "The HCF and LCM of two numbers are 6 and 72 respectively. If their sum is 42, find their difference.",
        ["6", "12", "8", "42"], "6",
        r"""Numbers are $6a$ and $6b$ with $\gcd(a, b) = 1$ and $ab = \frac{72}{6} = 12$.
Co-prime pairs of 12: (1, 12) → numbers 6, 72 (sum 78); (3, 4) → numbers 18, 24 (sum 42 ✓).
Difference $= 24 - 18 = 6$.""",
        "42 is the sum, not the difference — read the question again.", 55)
    a, b = 65, 91
    assert gcd(a, b) == 13 and lcm(a, b) == 455 and b - a == 26
    S.q("hl-r3", "hard",
        "The HCF and LCM of two numbers are 13 and 455 respectively. If one number lies between 60 and 80, find that number.",
        ["65", "91", "13", "78"], "65",
        r"""$ab = \frac{455}{13} = 35$ → co-prime pairs (1, 35) and (5, 7).
Numbers: (13, 455) or (65, 91). Only 65 lies between 60 and 80 ✓.""",
        None, 70)
    M = 2160 // (12 ** 2)
    assert M == 15 and [(1, 15), (3, 5)] == [(x, 15 // x) for x in (1, 3) if 15 % x == 0 and gcd(x, 15 // x) == 1]
    S.q("hl-r3", "hard",
        "The product of two numbers is 2160 and their HCF is 12. How many pairs of such numbers are possible?",
        ["2", "3", "4", "6"], "2",
        r"""Numbers are $12a$ and $12b$ with $ab = \frac{2160}{144} = 15$.
Co-prime factor pairs of 15: (1, 15) and (3, 5) → **2 pairs**: (12, 180) and (36, 60).""",
        "Answer 3 or 4 usually forgets the co-prime check — e.g. ab = 15 has only these two.", 70)
    cnt = sum(1 for x in range(1, 31) if 30 % x == 0 and x <= 30 // x and gcd(x, 30 // x) == 1)
    assert cnt == 4
    S.q("hl-r3", "hard",
        "The HCF and LCM of two numbers are 4 and 120 respectively. How many different pairs of such numbers are possible?",
        ["4", "3", "2", "6"], "4",
        r"""$ab = \frac{120}{4} = 30$. Co-prime factor pairs of 30: (1, 30), (2, 15), (3, 10), (5, 6) → **4 pairs**.
The pairs of numbers: (4, 120), (8, 60), (12, 40), (20, 24).""",
        None, 75)
    assert gcd(gcd(40, 80), 40) == 40 and 70 % 40 == 110 % 40 == 150 % 40 == 30
    S.q("hl-r4", "easy",
        "Find the greatest number which divides 70, 110 and 150 leaving the same remainder in each case. What is that remainder?",
        ["40, remainder 30", "20, remainder 10", "10, remainder 0", "80, remainder 30"], "40, remainder 30",
        r"""Pairwise differences: $110 - 70 = 40$, $150 - 110 = 40$, $150 - 70 = 80$.
HCF of differences $= 40$. Remainder $= 70 \bmod 40 = 30$ (same for 110 and 150 ✓).""",
        None, 45)
    g = gcd(gcd(72, 120), 48)
    assert g == 24 and 84 % 24 == 156 % 24 == 204 % 24 == 12
    S.q("hl-r4", "medium",
        "Find the greatest number which divides 84, 156 and 204 leaving the same remainder in each case.",
        ["24", "12", "48", "36"], "24",
        r"""Pairwise differences: $156 - 84 = 72$, $204 - 156 = 48$, $204 - 84 = 120$.
HCF$(72, 48, 120) = 24$; the common remainder is $84 \bmod 24 = 12$ ✓.""",
        None, 50)
    return S
