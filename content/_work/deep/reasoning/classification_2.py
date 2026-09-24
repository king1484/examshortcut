"""classification: subtopics number-classification and letter-classification."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P, Q, set_sub, steps, pos  # noqa: E402
from classification_checks import (isprime, issq, iscube, dsum, dprod, alt_num, one_breaks,  # noqa: E402
                                   alt_letters)

ODD = "Three of the following four are alike in a certain way and one is different. Find the odd one out."
ODDL = ("Three of the following four letter-clusters are alike in a certain way and one is different. "
        "Find the odd one out. (The letters follow English alphabetical order.)")

# ---------------------------------------------------------------- number-classification
NUM_NOTES = r"""### What is number classification?
Four numbers are given. Three share a **number property**; one does not. You do not need long calculation - you need a list of properties to test in a fixed order.

Everyday example: *2, 4, 6, 9*. Three are even; 9 is odd. So 9 is the odd one.

### The property list (test in this order)
**1. Prime or composite.** A prime number has exactly two factors: 1 and itself (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47...). A composite number has more factors. To test a number up to 200, divide by 2, 3, 5, 7, 11 and 13 only.
- Tricky composites that look prime: **51 = 3 × 17, 57 = 3 × 19, 87 = 3 × 29, 91 = 7 × 13, 119 = 7 × 17, 133 = 7 × 19, 143 = 11 × 13, 161 = 7 × 23**.

**2. Perfect square or cube.** Learn squares up to 30² (900) and cubes up to 12³ (1728). A square never ends in 2, 3, 7 or 8.

**3. Multiples (divisibility).**
- By 3 or 9: digit sum divisible by 3 or 9. (45 → 4 + 5 = 9)
- By 11: (sum of digits at odd places) − (sum at even places) is 0 or a multiple of 11. For 2849: (2 + 4) − (8 + 9) = −11, so 2849 is divisible by 11.
- By 7 and 13: just divide; the numbers are small.

**4. Digit property.** All four may have the same digit sum or digit product, except one. 138, 234 and 164 all have digit product 24; 326 has 36.

**5. Parity (odd/even).** Usually a **second-level** rule: all four are squares, but three are squares of odd numbers.

**6. Number forms.** Three numbers fit a formula such as $n^2+1$ (50, 65, 82), $n^3-1$ (124, 215, 342) or $n(n+1)$ (30, 42, 56). One does not.

### Worked example
Odd one: 79, 83, 89, 91.
- All odd, all two-digit - no help.
- Prime check: 79, 83, 89 have no divisor from 2, 3, 5, 7. But 91 = 7 × 13.
- Answer: **91**.

### Two-level questions
Sometimes all four numbers pass the first test. Example: 27, 125, 343, 512 are all cubes ($3^3, 5^3, 7^3, 8^3$). Look at the roots: 3, 5, 7 are odd; 8 is even. Answer **512**. When the first rule fits all four, always look at the **roots** or at **parity** next.

### Checking your answer
A good rule makes **exactly one** number odd. After you find your answer, quickly test one more property (prime, parity, digit sum). If another property points to a different number and looks equally natural, re-read the options. In a well-made question every natural rule points to the same answer.

### Common traps
- Treating 1 as prime (it is not) or 2 as composite (2 is the only even prime).
- Forgetting that a number can be both a square and a cube (64 = 8² = 4³, 729 = 27² = 9³).
- Stopping at "all are odd" or "all are even" - parity is almost never the whole rule when all four match.

### Quick revision
| Test | Fast check |
|---|---|
| Prime | Divide by 2, 3, 5, 7, 11, 13 |
| Square | Last digit not 2, 3, 7, 8; know 1²-30² |
| Cube | Know 1³-12³ |
| Multiple of 3 / 9 | Digit sum |
| Multiple of 11 | Alternate-digit difference 0 or 11 |
| Digit rule | Same digit sum / product |
| Two-level | Look at roots, then parity |
| Forms | $n^2 \pm 1$, $n^3 \pm 1$, $n(n+1)$ |
"""

NUM_PATTERNS = [
    P("cl-p10", "Prime vs composite", "very common",
      "Four numbers, mostly odd, that 'look' prime. One is a hidden product like 91 or 143 (or one is prime among composites).",
      "1. Divide each number by 2, 3, 5, 7, 11, 13.\n2. Mark which ones have a factor.\n3. The single number on the other side is the answer.\n\n**Why it works:** primes are the setter's favourite group; hidden composites (91, 119, 143) are the trap.",
      "Find the odd one: 61, 67, 71, 77.",
      "61, 67, 71 are prime. 77 = 7 × 11 is composite. Answer: **77**.",
      formula=r"p \text{ prime} \iff \text{no divisor } 2 \le d \le \sqrt{p}"),
    P("cl-p11", "Perfect square / perfect cube", "very common",
      "Numbers such as 169, 196, 225 or 216, 343, 512 - familiar powers with one stranger.",
      "1. Recall the square/cube table.\n2. Mark which numbers are exact squares or cubes.\n3. The one that is not is odd.\n\n**Why it works:** a number between two known powers cannot be a power.",
      "Find the odd one: 169, 196, 225, 250.",
      "169 = 13², 196 = 14², 225 = 15². 250 lies between 15² and 16² = 256. Answer: **250**.",
      formula=r"n^2,\; n^3"),
    P("cl-p12", "Multiples / divisibility", "common",
      "Three numbers are multiples of one number (7, 9, 11, 13...), often shown by a digit rule.",
      "1. Find the common divisor of most of the numbers (try 7, 9, 11, 13).\n2. Use divisibility rules for big numbers (digit sum for 9, alternate sum for 11).\n3. The number that is not a multiple is odd.\n\n**Why it works:** the setter picks a divisor, writes three multiples and one near-miss.",
      "Find the odd one: 39, 65, 91, 111.",
      "39 = 13 × 3, 65 = 13 × 5, 91 = 13 × 7. 111 = 3 × 37 is not a multiple of 13. Answer: **111**.",
      formula=r"11 \mid n \iff (\text{odd-place sum}) - (\text{even-place sum}) \equiv 0 \pmod{11}"),
    P("cl-p13", "Digit sum / digit product", "common",
      "Numbers with no clear prime/square pattern, often three-digit, whose digits look shuffled.",
      "1. Add the digits of each number.\n2. If sums differ, multiply the digits.\n3. The number whose sum or product differs is odd.\n\n**Why it works:** digits can be rearranged freely while keeping the same sum and product.",
      "Find the odd one: 345, 453, 534, 546.",
      "Digit sums: 12, 12, 12, 15. Answer: **546**.",
      formula=r"S(n) = \sum \text{digits},\; P(n) = \prod \text{digits}"),
    P("cl-p14", "Two-level: same power, odd/even root", "common",
      "All four are squares (or all cubes), so the first rule does not decide.",
      "1. Write the root of each number.\n2. Check roots for odd/even or prime/composite.\n3. The number whose root breaks the pattern is odd.\n\n**Why it works:** the first property is shared by all four to trap you; the answer hides in the roots.",
      "Find the odd one: 27, 125, 343, 512.",
      "All cubes: 3³, 5³, 7³, 8³. Roots 3, 5, 7 are odd; 8 is even. Answer: **512**."),
    P("cl-p15", "Number forms (n²±1, n³±1, n(n+1))", "occasional",
      "Numbers sit just beside squares or cubes (50, 65, 82 or 63, 124, 215), or are products of two consecutive numbers.",
      "1. Check each number against the nearest square and cube.\n2. Write it as $n^2 \\pm 1$, $n^3 \\pm 1$ or $n(n+1)$.\n3. The number that does not fit the common form is odd.\n\n**Why it works:** the setter builds three numbers from one formula and changes the sign or the base for the fourth.",
      "Find the odd one: 50, 65, 82, 99.",
      "50 = 7² + 1, 65 = 8² + 1, 82 = 9² + 1. 99 = 10² − 1. Answer: **99**.",
      formula=r"n^2+1,\; n^3-1,\; n(n+1)"),
]


def num_q(qid, items, ans, rule, sol, sc, diff, pat, t, check_alt=True):
    one_breaks(items, rule, ans)
    if check_alt:
        alt_num(items, ans)
    wrong = [str(x) for x in items if x != ans]
    return Q(qid, f"{ODD}\n\n**{', '.join(str(x) for x in items)}**", str(ans), wrong, sol, sc, diff,
             "number-classification", pat, t)


def num_questions():
    qs = []
    qs.append(num_q("number-classification-p01", [61, 67, 71, 77], 77, isprime,
                    "61, 67 and 71 are **prime**. 77 = 7 × 11 is composite → **77**.",
                    "Numbers ending in 7 are the usual hidden multiples of 7 - test 77 first.", "easy", "cl-p10", 25))
    qs.append(num_q("number-classification-p02", [79, 83, 89, 91], 91, isprime,
                    "79, 83 and 89 are **prime** (no divisor among 2, 3, 5, 7). 91 = 7 × 13 → **91**.",
                    "91 is the most famous 'fake prime' - remember 7 × 13 = 91.", "medium", "cl-p10", 30))
    qs.append(num_q("number-classification-p03", [113, 127, 131, 143], 143, isprime,
                    "113, 127 and 131 are **prime** (test 2, 3, 5, 7, 11). 143 = 11 × 13 → **143**.",
                    "11 test on 143: 1 − 4 + 3 = 0 → divisible by 11.", "medium", "cl-p10", 40))
    qs.append(num_q("number-classification-p04", [216, 343, 512, 625], 625, iscube,
                    "216 = 6³, 343 = 7³, 512 = 8³ are **perfect cubes**. 625 = 25² = 5⁴ is not a cube (8³ = 512, 9³ = 729) → **625**.",
                    "Cube table 6³-9³: 216, 343, 512, 729.", "medium", "cl-p11", 30))
    qs.append(num_q("number-classification-p05", [169, 196, 225, 250], 250, issq,
                    "169 = 13², 196 = 14², 225 = 15² are **perfect squares**. 250 lies between 15² = 225 and 16² = 256 → **250**.",
                    "A square never ends in a single 0 - 250 is out at a glance.", "easy", "cl-p11", 25))
    qs.append(num_q("number-classification-p06", [39, 65, 91, 111], 111, lambda n: n % 13 == 0,
                    "39 = 13 × 3, 65 = 13 × 5, 91 = 13 × 7 - all **multiples of 13**. 111 = 3 × 37 → **111**.",
                    None, "medium", "cl-p12", 35))
    qs.append(num_q("number-classification-p07", [2849, 5214, 7381, 6352], 6352, lambda n: n % 11 == 0,
                    "Test for 11: (1st + 3rd digit) − (2nd + 4th digit).\n- 2849: (2 + 4) − (8 + 9) = −11 ✓\n- 5214: (5 + 1) − (2 + 4) = 0 ✓\n- 7381: (7 + 8) − (3 + 1) = 11 ✓\n- 6352: (6 + 5) − (3 + 2) = 6 ✗\n\nThree are **multiples of 11** → **6352**.",
                    "Alternate-sum test takes 5 seconds per number - no long division.", "hard", "cl-p12", 60))
    qs.append(num_q("number-classification-p08", [345, 453, 534, 546], 546, lambda n: dsum(n) == 12,
                    "Digit sums: 3+4+5 = 12, 4+5+3 = 12, 5+3+4 = 12, 5+4+6 = **15**. (The first three also use the same digits 3, 4, 5.) → **546**.",
                    "Same three digits shuffled in three options - the fourth uses a new digit.", "easy", "cl-p13", 25))
    qs.append(num_q("number-classification-p09", [138, 234, 164, 326], 326, lambda n: dprod(n) == 24,
                    "Digit products: 1×3×8 = 24, 2×3×4 = 24, 1×6×4 = 24, 3×2×6 = **36** → **326**.",
                    "Digit sums (12, 9, 11, 11) show no clear rule, so try products.", "medium", "cl-p13", 40))
    qs.append(num_q("number-classification-p10", [125, 343, 729, 512], 512, lambda n: n % 2 == 1,
                    "All four are **cubes**: 5³, 7³, 9³, 8³. Level two: roots 5, 7, 9 are odd; 8 is even (so 512 is the only even number) → **512**.",
                    "All cubes? Compare the roots.", "medium", "cl-p14", 35))
    qs.append(num_q("number-classification-p11", [16, 36, 64, 81], 81, lambda n: n % 2 == 0,
                    "All four are **squares**: 4², 6², 8², 9². Roots 4, 6, 8 are even; 9 is odd → **81**.",
                    None, "easy", "cl-p14", 25))
    qs.append(num_q("number-classification-p12", [50, 65, 82, 99], 99, lambda n: issq(n - 1),
                    "50 = 7² + 1, 65 = 8² + 1, 82 = 9² + 1 - form **n² + 1**. 99 = 10² − 1 → **99**.",
                    "Each number sits just above a square except 99, which sits just below 100.", "medium", "cl-p15", 40))
    qs.append(num_q("number-classification-p13", [124, 217, 342, 999], 217, lambda n: iscube(n + 1),
                    "124 = 5³ − 1, 342 = 7³ − 1, 999 = 10³ − 1 - form **n³ − 1**. 217 + 1 = 218 is not a cube (in fact 217 = 6³ + 1) → **217**.",
                    "Add 1 to each number and look for a cube.", "hard", "cl-p15", 50))
    qs.append(num_q("number-classification-p14", [30, 42, 56, 80], 80,
                    lambda n: any(k * (k + 1) == n for k in range(1, 40)),
                    "30 = 5 × 6, 42 = 6 × 7, 56 = 7 × 8 - each is a **product of two consecutive numbers**, n(n + 1). 80 = 8 × 10 is not (8 × 9 = 72, 9 × 10 = 90) → **80**.",
                    "Take the square root roughly: √80 ≈ 8.9, so check 8 × 9 = 72 - not 80.", "hard", "cl-p15", 50))
    return qs


# ---------------------------------------------------------------- letter-classification
LET_NOTES = """### What is letter-cluster classification?
Each option is a small group of letters, such as **ACE** or **BDFH**. Three groups are built by the same rule; one is not. The rule is almost always about **positions in the alphabet**, so first turn letters into numbers.

### Tool 1: alphabet positions
A = 1, B = 2, ... Z = 26. Remember **EJOTY**: E = 5, J = 10, O = 15, T = 20, Y = 25. Any letter is at most two steps from one of these. Example: R is T − 2 = 18.

### Tool 2: steps inside a cluster
Write the jump from each letter to the next. **ACE**: A→C is +2, C→E is +2, so the step tuple is (+2, +2). After Z the count wraps back to A (Y + 3 = B). Backward steps are negative (Z→X is −2).

### The rule families
**1. Constant step.** Same jump every time. DGJ (+3, +3), KNQ (+3, +3), PSV (+3, +3); TWY is (+3, +2) → odd.

**2. Mixed but repeated steps.** The jumps are not equal but the same pattern repeats in every cluster. ACF (+2, +3), GIL (+2, +3), MOR (+2, +3); SUW (+2, +2) → odd. For four letters: MPOR is (+3, −1, +3).

**3. Opposite letters.** Letters that sit at the same distance from both ends: A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N. Their positions always **add up to 27**. In DW, GT, KP each pair adds to 27; MO adds to 28 → odd.

**4. Vowel structure.** A, E, I, O, U are vowels. Three clusters may have a vowel in the same place (NOP, HIJ, DEF have the vowel in the middle) while one has none (RST).

**5. Position property.** The positions follow a number rule: sum of positions is the same (AMP = 1 + 13 + 16 = 30), or all positions are even (B, H, L = 2, 8, 12).

### Method in five steps
1. Write positions under every letter of all four options.
2. Write the step tuple of each option.
3. If three tuples match, the fourth option is the answer.
4. If all four tuples match, test vowels and opposite pairs.
5. If tuples are all different, test position sums and even/odd positions.

### Worked example
Odd one: ACF, GIL, MOR, SUW.
- ACF: 1, 3, 6 → (+2, +3)
- GIL: 7, 9, 12 → (+2, +3)
- MOR: 13, 15, 18 → (+2, +3)
- SUW: 19, 21, 23 → (+2, +2)
- Answer: **SUW**.

### Exam note
Some papers add a note such as "the odd one is not based on the number of consonants/vowels or their position in the cluster". That note simply removes the vowel family - use steps or opposite letters instead.

### Common mistakes
- Counting letters on fingers and slipping by one. Use EJOTY and subtract positions.
- Forgetting the wrap after Z (X + 4 = B).
- Checking only the first step of each cluster; the second or third step is often where the odd cluster breaks.

### Quick revision
| Rule | Check | Example of odd one |
|---|---|---|
| Constant step | All jumps equal | TWY among DGJ, KNQ, PSV |
| Repeated mixed steps | Same tuple | SUW among ACF, GIL, MOR |
| Opposite letters | Positions add to 27 | MO among DW, GT, KP |
| Vowel place | Vowel in same slot | RST among NOP, HIJ, DEF |
| Position sum | Same total | BHS (29) among sums of 30 |
| Even positions | All letters even | GLR among BHL, DJP, FNT |
"""

LET_PATTERNS = [
    P("cl-p16", "Constant step inside the cluster", "very common",
      "Every cluster has letters with equal gaps (ACE, DGJ, BFJN), forward or backward.",
      "1. Convert letters to positions.\n2. Write the step tuple for each cluster.\n3. Three clusters have equal steps with the same value; the fourth changes one step.\n\n**Why it works:** the setter copies one constant jump and spoils one step in the odd cluster.",
      "Find the odd one: DGJ, KNQ, PSV, TWY.",
      "Steps: (+3, +3), (+3, +3), (+3, +3), (+3, **+2**). Answer: **TWY**.",
      formula=r"\text{step} = Q(\text{next}) - Q(\text{this}) \pmod{26}"),
    P("cl-p17", "Mixed step tuple (same pattern repeated)", "very common",
      "Steps inside each cluster are unequal (+2, +3) or go up and down (+3, −1, +3), but look similar across options.",
      "1. Write the full step tuple for each cluster.\n2. Three tuples will be identical.\n3. The cluster with a different tuple is odd.\n\n**Why it works:** the pattern is the tuple as a whole, not any single step.",
      "Find the odd one: ACF, GIL, MOR, SUW.",
      "Tuples: (+2, +3) three times, SUW is (+2, +2). Answer: **SUW**."),
    P("cl-p18", "Opposite-letter pairs (position sum 27)", "common",
      "Pairs like AZ, BY, DW or clusters where one letter mirrors another from the other end of the alphabet.",
      "1. Add the positions of the two letters that should be opposite.\n2. Opposite letters add to 27.\n3. The cluster whose pair does not make 27 is odd.\n\n**Why it works:** A↔Z, B↔Y ... M↔N all sum to 27, so one addition tests each option.",
      "Find the odd one: DW, GT, KP, MO.",
      "D + W = 4 + 23 = 27, G + T = 27, K + P = 27, M + O = 13 + 15 = 28. Answer: **MO**.",
      formula=r"Q(x) + Q(\bar{x}) = 27"),
    P("cl-p19", "Vowel position / vowel structure", "common",
      "All clusters have the same steps, so steps cannot decide; vowels sit in a fixed slot in three clusters.",
      "1. Circle the vowels (A, E, I, O, U) in each cluster.\n2. Note the number and position of vowels.\n3. The cluster that differs is odd.\n\n**Why it works:** when step tuples are identical, the setter has used vowels.",
      "Find the odd one: NOP, HIJ, DEF, RST.",
      "NOP, HIJ, DEF each have a vowel in the middle (O, I, E). RST has no vowel. Answer: **RST**."),
    P("cl-p20", "Position-number property (sum, even/odd positions)", "occasional",
      "Step tuples are all different and there is no vowel pattern; the letters look random.",
      "1. Write positions of all letters.\n2. Test: equal position sums? all even or all odd positions? squares?\n3. The cluster that fails the common property is odd.\n\n**Why it works:** the setter chose letters to meet a number condition, not a step condition.",
      "Find the odd one: AMP, DGT, EKN, BHS.",
      "Sums: 1+13+16 = 30, 4+7+19 = 30, 5+11+14 = 30, 2+8+19 = 29. Answer: **BHS**.",
      formula=r"\sum Q(\text{letters}) = \text{constant}"),
]


def let_q(qid, items, ans, rule, sol, sc, diff, pat, t, alt=True):
    one_breaks(items, rule, ans)
    if alt:
        alt_letters(items, ans)
    wrong = [x for x in items if x != ans]
    return Q(qid, f"{ODDL}\n\n**{', '.join(items)}**", ans, wrong, sol, sc, diff, "letter-classification", pat, t)


def let_questions():
    qs = []
    qs.append(let_q("letter-classification-p01", ["DGJ", "KNQ", "PSV", "TWY"], "TWY", lambda w: steps(w) == [3, 3],
                    "Steps: D→G→J (+3, +3), K→N→Q (+3, +3), P→S→V (+3, +3), T→W→Y (+3, **+2**) → **TWY**.",
                    "Check only the last jump: J, Q, V are 3 after G, N, S; Y is 2 after W.", "easy", "cl-p16", 30))
    qs.append(let_q("letter-classification-p02", ["ZXV", "TRP", "NLJ", "HFC"], "HFC", lambda w: steps(w) == [-2, -2],
                    "Backward steps: Z(26)→X(24)→V(22) (−2, −2); T(20)→R(18)→P(16) (−2, −2); N(14)→L(12)→J(10) (−2, −2); H(8)→F(6)→C(3) (−2, **−3**) → **HFC**.",
                    None, "medium", "cl-p16", 35))
    qs.append(let_q("letter-classification-p03", ["BFJN", "CGKO", "DHLP", "EIMR"], "EIMR", lambda w: steps(w) == [4, 4, 4],
                    "Steps of +4: B(2) F(6) J(10) N(14); C(3) G(7) K(11) O(15); D(4) H(8) L(12) P(16). E(5) I(9) M(13) R(18) - last step is **+5** → **EIMR**.",
                    "Compare the last letters: N, O, P are 12 after B, C, D; R is 13 after E.", "medium", "cl-p16", 40))
    qs.append(let_q("letter-classification-p04", ["ACF", "GIL", "MOR", "SUW"], "SUW", lambda w: steps(w) == [2, 3],
                    "Tuples: ACF (+2, +3), GIL (+2, +3), MOR (+2, +3), SUW (+2, **+2**) → **SUW**.",
                    None, "medium", "cl-p17", 35))
    qs.append(let_q("letter-classification-p05", ["MPOR", "JMLO", "DGFI", "SVUY"], "SVUY", lambda w: steps(w) == [3, -1, 3],
                    "Tuples: M(13)→P(16)→O(15)→R(18) = (+3, −1, +3); JMLO = (+3, −1, +3); DGFI = (+3, −1, +3); S(19)→V(22)→U(21)→Y(25) = (+3, −1, **+4**) → **SVUY**.",
                    "Pattern 'forward 3, back 1, forward 3': only the last jump of SVUY is 4.", "hard", "cl-p17", 50))
    qs.append(let_q("letter-classification-p06", ["DW", "GT", "KP", "MO"], "MO", lambda w: pos(w[0]) + pos(w[1]) == 27,
                    "Opposite letters add to 27: D + W = 4 + 23 = 27, G + T = 7 + 20 = 27, K + P = 11 + 16 = 27, M + O = 13 + 15 = **28** (M's opposite is N) → **MO**.",
                    "Remember the pair M-N: MO cannot be an opposite pair.", "easy", "cl-p18", 25))
    qs.append(let_q("letter-classification-p07", ["CXD", "GTH", "JQK", "PLQ"], "PLQ",
                    lambda w: pos(w[0]) + pos(w[1]) == 27 and pos(w[2]) == pos(w[0]) + 1,
                    "Rule: 2nd letter = opposite of 1st, 3rd letter = next letter after 1st.\n- CXD: C↔X ✓, D = C + 1 ✓\n- GTH: G↔T ✓, H = G + 1 ✓\n- JQK: J↔Q ✓, K = J + 1 ✓\n- PLQ: P(16) + L(12) = 28 ✗ (P's opposite is K)\n\n→ **PLQ**.",
                    None, "hard", "cl-p18", 50))
    qs.append(let_q("letter-classification-p08", ["NOP", "HIJ", "DEF", "RST"], "RST",
                    lambda w: w[1] in "AEIOU",
                    "All four have steps (+1, +1), so steps cannot decide. NOP, HIJ and DEF have a **vowel in the middle** (O, I, E). RST has no vowel → **RST**.",
                    "Same steps everywhere? Circle vowels.", "easy", "cl-p19", 25))
    qs.append(let_q("letter-classification-p09", ["OPQR", "UVWX", "ABCD", "STUV"], "STUV",
                    lambda w: w[0] in "AEIOU",
                    "All four are four consecutive letters and each contains exactly one vowel. In OPQR, UVWX and ABCD the vowel is the **first** letter. In STUV the vowel U is third → **STUV**.",
                    None, "medium", "cl-p19", 35))
    qs.append(let_q("letter-classification-p10", ["AMP", "GJM", "EKN", "BHS"], "BHS",
                    lambda w: sum(pos(c) for c in w) == 30,
                    "Step tuples are all different, so try position sums: A+M+P = 1+13+16 = 30, G+J+M = 7+10+13 = 30, E+K+N = 5+11+14 = 30, B+H+S = 2+8+19 = **29** → **BHS**.",
                    "EJOTY makes the sums quick: M = O − 2 = 13, P = O + 1 = 16, S = T − 1 = 19, K = J + 1 = 11, N = O − 1 = 14.", "hard", "cl-p20", 55))
    qs.append(let_q("letter-classification-p11", ["BHL", "DJP", "FNT", "GLR"], "GLR",
                    lambda w: all(pos(c) % 2 == 0 for c in w),
                    "Positions: B(2) H(8) L(12); D(4) J(10) P(16); F(6) N(14) T(20) - every letter is at an **even** position. G(7) is odd in GLR → **GLR**.",
                    None, "medium", "cl-p20", 40))
    return qs


def apply(d):
    set_sub(d, "number-classification", notes=NUM_NOTES, patterns=NUM_PATTERNS)
    set_sub(d, "letter-classification", notes=LET_NOTES, patterns=LET_PATTERNS)
    return num_questions() + let_questions()
