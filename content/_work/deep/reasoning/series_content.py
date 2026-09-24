"""Notes + patterns for the `series` topic (imported by series.py)."""

NOTES = {}

NOTES["series-idea"] = """### What is a series?
A series is a list of numbers or letters written in a fixed order. Every term is made from the one before it by the same small rule. Think of a savings box: you put ₹100 in January, ₹150 in February and ₹200 in March. Anyone can tell that April will be ₹250, because the rule "add ₹50 every month" is clear. A series question hides such a rule and asks you to find it.

SSC, Railway and Banking papers ask series in three formats:
- **Next term**: '4, 9, 16, 25, ?' — find what comes after the last term.
- **Missing term**: '4, 9, ?, 25, 36' — a term in the middle is replaced by '?'.
- **Wrong term**: the series is complete but one term is incorrect (see the Wrong number lesson).

### Step 1: Look at the size of the numbers
Before any calculation, see how fast the terms grow.
- Slow, steady growth (5, 9, 13, 17) → the rule **adds** something.
- Terms roughly doubling or tripling (3, 7, 15, 31) → the rule **multiplies** (maybe with a small add or subtract).
- Terms going up and down (8, 20, 10, 18, 12) → **two series are mixed** (alternate terms).
- Terms close to famous numbers (3, 8, 15, 24 are just below 4, 9, 16, 25) → **squares or cubes**.

### Step 2: The difference ladder
Write the gaps (differences) between neighbours under the series. This is the first difference row.

Example: 2, 5, 10, 17, 26 → differences 3, 5, 7, 9. They rise by 2, so the next difference is 11 and the next term is 26 + 11 = 37.

If the first row is not clear, take differences again (second difference row). Most exam series become clear within two rows.

| What the ladder shows | Family |
|---|---|
| First differences equal | Add the same number (AP) |
| First differences rise evenly | Growing difference |
| Differences double | Powers of 2 are being added |
| Differences are 1, 4, 9, 16 | Squares are being added |
| Each term ≈ previous × k | Multiply family (×k ± r) |

### Step 3: When the ladder fails
Try, in this order: (1) **ratio** — divide a term by the one before it; (2) **alternate terms** — read positions 1, 3, 5 and 2, 4, 6 separately; (3) **squares and cubes** near the terms; (4) **mixed operations** such as ×1+1, ×2+2, ×3+3.

### Missing term in the middle
Find the rule from the terms you can see on **both sides** of the gap. Then check your answer twice: it must come correctly from the term before it, and the term after it must come correctly from your answer.

Example: 3, 7, ?, 31, 63 → each term is ×2 + 1, so ? = 7 × 2 + 1 = 15. Check: 15 × 2 + 1 = 31 ✓.

### Fractions, decimals and halving
Do not panic at decimals. 64, 32, 16, 8, 4, ? is just ÷2 → 2. 0.5, 1.5, 4.5, 13.5 is ×3 → 40.5. For fractions, read the top numbers (numerators) and the bottom numbers (denominators) as two separate series: 1/3, 3/5, 5/7 → tops 1, 3, 5 and bottoms 3, 5, 7 both rise by 2, so the next is 7/9.

### Two missing terms
Some questions blank two terms and give pairs as options. Find the rule from the visible terms, fill the first blank, then continue to the second blank. Check the term after each blank.

### Quick revision
- Look at size first: slow growth = add, fast growth = multiply, up-down = two series.
- Difference ladder: first row, then second row.
- If it fails: ratio → alternate terms → squares/cubes → mixed operations.
- Missing term: check with the term before AND the term after.
- Fractions: numerators and denominators are two separate series.
- Your rule must fit every given term, not just the last two."""

NOTES["number-series"] = """### What this lesson covers
Number series is the most common series type in competitive exams. Almost every question uses one of eight families. Learn the families and every question becomes a quick check against a short list.

### 1. Constant or growing difference
Add the same number every time: 7, 12, 17, 22 (+5). This is called an arithmetic progression (AP). In the growing type, the amount added itself grows: 11, 13, 17, 23, 31 → add 2, 4, 6, 8, so next add 10 → 41. It can also fall: 120, 119, 116, 111 (subtract 1, 3, 5).

### 2. Multiply, then add or subtract (×k ± r)
Each term is the previous term multiplied by a fixed number, sometimes with a small add or subtract. 3, 6, 12, 24 is ×2. 3, 7, 15, 31 is ×2 + 1. 4, 10, 28, 82 is ×3 − 2.

Test: divide a big term by the one before. If the result is near 2 or 3, try ×2 or ×3 and see what small number is left over. That left-over is r.

### 3. Squares and cubes
Know squares up to 30 and cubes up to 15. Look for terms just above or below them:
- 3, 8, 15, 24, 35 = 2²−1, 3²−1, 4²−1 ...
- 2, 9, 28, 65 = 1³+1, 2³+1, 3³+1, 4³+1
- 2, 6, 12, 20, 30 = 1×2, 2×3, 3×4 ... (n × (n+1))

### 4. Two-level difference
The first difference row is not constant, but the second row follows a clear rule.

Example: 2, 5, 11, 21, 36 → differences 3, 6, 10, 15 → second differences 3, 4, 5. Next second difference is 6, so the next difference is 21 and the next term is 57.

### 5. Differences that are famous numbers
The difference row itself may be squares (1, 4, 9, 16), cubes (1, 8, 27, 64), primes (2, 3, 5, 7, 11) or powers of 2 (1, 2, 4, 8).

Example: 10, 11, 13, 17, 25 → differences 1, 2, 4, 8 → next 16 → 41.

### 6. Alternate (interleaved) series
Two separate series are mixed. Terms 1, 3, 5, 7 form one series; terms 2, 4, 6, 8 form another.

Example: 3, 50, 6, 45, 12, 40, 24, ? → odd places 3, 6, 12, 24 (×2); even places 50, 45, 40 (−5). The 8th term is an even place → 35. Suspect this when the series goes up and down.

### 7. Mixed operations
The operation changes in a fixed way:
- ×1+1, ×2+2, ×3+3 ...: 2, 3, 8, 27, 112 → next 112×5+5 = 565.
- Two operations taking turns (+1, ×2, +1, ×2): 5, 6, 12, 13, 26, 27 → 54.
- Changing signs (+2, −3, +4, −5): 10, 12, 9, 13, 8 → 14.

### 8. Fibonacci type
Each term is the sum of the previous two (2, 3, 5, 8, 13, 21) or of the previous three (1, 2, 3, 6, 11, 20, 37). Spot it when the difference row looks like the series itself.

### How to choose quickly
1. Growth is slow → difference ladder (families 1, 4, 5).
2. Growth is fast → ratio test (families 2, 7).
3. Terms go up and down → alternate series (family 6).
4. Terms near squares or cubes → family 3.
5. Each term is close to the sum of the two before it → Fibonacci (family 8).

### Quick revision
| Family | Example | Next |
|---|---|---|
| Constant difference | 7, 12, 17, 22 | 27 |
| Growing difference | 11, 13, 17, 23, 31 | 41 |
| ×k ± r | 3, 7, 15, 31 | 63 |
| Squares/cubes | 3, 8, 15, 24 | 35 |
| Two-level difference | 2, 5, 11, 21, 36 | 57 |
| Famous differences | 10, 11, 13, 17, 25 | 41 |
| Alternate | 3, 50, 6, 45, 12, 40 | 24 |
| Mixed operations | 2, 3, 8, 27, 112 | 565 |
| Fibonacci | 2, 3, 5, 8, 13 | 21 |"""

NOTES["letter-series"] = """### Letters are numbers in disguise
Every letter series is a number series written in letters. Give each letter its place in the alphabet: A=1, B=2 ... Z=26. Now 'C, G, K, O' is just 3, 7, 11, 15 — add 4 each time. The next is 19 = S.

### Learn the anchors: EJOTY
Counting from A every time is slow and causes mistakes. Remember five anchor letters:

| E | J | O | T | Y |
|---|---|---|---|---|
| 5 | 10 | 15 | 20 | 25 |

Any letter is one or two steps from an anchor: M = O − 2 = 13, R = T − 2 = 18, W = Y − 2 = 23.

Also learn the **reverse position** (Z=1, Y=2 ... A=26). Rule: reverse position = 27 − position. The **opposite pairs** add up to 27: A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N.

### Wrap-around
After Z the alphabet starts again at A. If a rule gives a number above 26, subtract 26: X(24) + 4 = 28 → 28 − 26 = 2 = B. Going backwards below A, add 26: C(3) − 5 = −2 → −2 + 26 = 24 = X.

### Type 1: constant step
Every letter moves by the same number: C, G, K, O, S (+4). It can go backwards too: Z, W, T, Q (−3). It can cross Z: T, W, Z, C, F (+3).

### Type 2: rising or falling step
The step itself changes: C, D, F, I, M (+1, +2, +3, +4, so next +5 → R). Or Y, W, T, P, K (−2, −3, −4, −5, so next −6 → E).

### Type 3: two series mixed
Positions 1, 3, 5 form one series and positions 2, 4, 6 another: A, Z, C, X, E, V → A, C, E (+2) and Z, X, V (−2). Or the steps take turns: B, E, D, G, F, I (+3, −1, +3, −1).

### Type 4: letter clusters
Each term is a group of 2-4 letters: BDF, GIK, LNP. Treat each position as its own series: first letters B, G, L (+5), second letters D, I, N (+5), third letters F, K, P (+5). Next: QSU. The slots can move in different directions: AZ, CX, EV (first letter +2, second letter −2).

### Type 5: positions follow a number pattern
The positions themselves may be squares (A, D, I, P, Y = 1, 4, 9, 16, 25) or primes (B, C, E, G, K = 2, 3, 5, 7, 11).

### Method in four steps
1. Write the position number under every letter (use EJOTY).
2. Find the number rule with the difference ladder.
3. Apply it, using wrap-around if the result passes 26 or goes below 1.
4. Convert back to a letter and match the option.

### Quick revision
- A=1 ... Z=26; anchors E5, J10, O15, T20, Y25.
- Reverse position = 27 − position; opposite pairs add to 27.
- Above 26 → subtract 26; below 1 → add 26.
- Clusters: solve each slot separately.
- Letters going forward and back → split into two series.
- Squares (A, D, I, P, Y) and primes (B, C, E, G, K) are favourite hidden rules."""

NOTES["alphanumeric-series"] = """### What an alphanumeric series is
'Alpha' means letters and 'numeric' means numbers. Each term mixes both, like A3, D6, G9. Think of seats in a train: S1, S2, S3 is the coach series and 12, 13, 14 is the seat series. The two parts usually move by their own separate rules.

### Rule 1: two independent tracks
Split every term into its letter part and its number part. Solve each as a separate series, then join the answers.

Example: B2, D4, F8, H16, ? → letters B, D, F, H (+2) → J; numbers 2, 4, 8, 16 (×2) → 32. Answer **J32**.

The letter can come before or after the number: 3Z, 7W, 11T → numbers +4, letters −3 → 15Q.

### Rule 2: number linked to the letter
Sometimes the number is not a separate series. It is the **position of the letter**, or something made from it:
- C3, F6, I9 → number = position of the letter.
- B4, D16, F36 → number = (position)².
- Z26, X24, V22 → number = position, letters going backwards.

Check this link first. If it holds for every term, you only need the next letter; the number follows.

### Rule 3: clusters with numbers
Terms can have two letters and a number: AB2, DE4, GH8. Each letter slot is its own series (A, D, G and B, E, H, both +3) and the number doubles → JK16. Or the number comes first: 2CZ, 4EX, 6GV → numbers +2, first letters +2, last letters −2.

### Rule 4: missing term in the middle
When the '?' sits in the middle, find each track from the visible terms and fill the gap. Always check the term after the gap.

Example: D5, G10, ?, M20, P25 → letters +3 → J; numbers +5 → 15. Answer **J15**.

### Method
1. Draw two (or three) columns: letters and numbers.
2. Convert letters to positions (EJOTY anchors) and find the step.
3. Find the number rule: +k, ×k, squares, cubes, or 'same as the letter position'.
4. Build the answer in the **same format** as the terms (letter first or number first).
5. Before marking, compare options that differ in only one character — examiners pair the right letter with a wrong number and the right number with a wrong letter.

### Common traps
- An option with the correct letter but a number from a wrong rule (J30 instead of J32).
- An option in the wrong order (32J instead of J32).
- Moving the letter by the number's step, or the number by the letter's step.

### Quick revision
| Series | Letter rule | Number rule | Next |
|---|---|---|---|
| B2, D4, F8, H16 | +2 | ×2 | J32 |
| C3, F6, I9, L12 | +3 | = position | O15 |
| B4, D16, F36, H64 | +2 | position² | J100 |
| AB2, DE4, GH8, JK16 | +3 each slot | ×2 | MN32 |
| Z1, W8, T27, Q64 | −3 | cubes | N125 |

- Split, solve, join.
- Test 'number = letter position' first.
- Keep the answer in the same format as the terms."""

NOTES["wrong-number"] = """### What the question asks
The series is complete, but one term was changed. You must find that **wrong** term — not the correct value. Think of a bank passbook with one typing mistake: every other entry follows the rule, only one breaks it.

### The basic method
1. Take the first three or four terms and guess the rule.
2. Check the guess on every term, one by one.
3. The single term that does not fit is the answer.
4. Confirm: if you replace it with the correct value, the whole series must work, including the term just after it.

### Why one wrong term spoils two differences
When a term is wrong, both the gap before it and the gap after it look wrong. Example: 5, 9, 13, 17, 22, 25 → differences 4, 4, 4, 5, 3. Two gaps (5 and 3) are off, and the term between them, 22, is the culprit. The correct value is 21. So look for the term that sits between two bad gaps.

### Type 1: difference series
Constant or growing gaps: 3, 5, 9, 15, 23, 34, 45 → differences 2, 4, 6, 8, 11, 11. The expected gaps are 2, 4, 6, 8, 10, 12, so 34 should be 33.

### Type 2: ratio and ×k ± r series
2, 6, 18, 54, 164, 486 → ×3 gives 162, not 164. For ×k ± r, calculate each term from the previous one: 5, 11, 23, 48, 95 → ×2 + 1 gives 47, not 48.

Careful: the term after the wrong one is made from the **correct** value. So 95 = 47 × 2 + 1 looks wrong if you use 48. Rebuild the series from the start instead of jumping between neighbours.

### Type 3: squares and cubes
1, 8, 27, 64, 124, 216 → 124 should be 125 (5³). 2, 6, 12, 20, 31, 42 → n × (n+1) gives 30, not 31. Near-miss numbers like 124, 31 or 65 are strong hints.

### Type 4: alternate and mixed series
Split the series into odd and even positions. 2, 10, 4, 13, 6, 16, 9, 19 → odd places 2, 4, 6, 9 (should be 8); even places 10, 13, 16, 19 are fine. For mixed operations like ×1+1, ×2+2, check each step with its own multiplier.

### Type 5: wrong term in a letter series
The same idea works with letters. BD, EG, HJ, KN, NP → every cluster has a gap of 2 inside, so KN (gap 3) should be KM.

### Speed tips
- The options are terms of the series. When short of time, test only the four option terms.
- Odd/even check: if all terms but one are odd, that one is suspicious — but confirm with the rule.
- The first term can also be wrong; check it against the second.

### Quick revision
- The wrong term sits between two bad gaps.
- Rebuild each term from the correct previous term.
- Near-miss values (124 vs 125, 31 vs 30) are giveaways.
- Split up-down series into two series.
- Answer = the wrong term as shown, not its correct value."""

NOTES["letter-blank-series"] = """### What this question looks like
You see a line of small letters with some blanks, for example: a _ c a b _ a b c _ b c. You must choose the group of letters that fills the blanks, in order from left to right, so that the whole line follows a repeating pattern. The options look like 'bca', 'bac', 'cab'.

Think of a rangoli border: the same small design repeats again and again. Once you know one design unit, you can fill any gap in the border. SSC and Railway papers ask this type almost every shift.

### Step 1: Find the block
Most such series repeat a small block of 3, 4, 5 or 6 letters. Count the total number of places (letters + blanks). If the total is 12, the block is often 3, 4 or 6 letters long; if it is 15, often 3 or 5. Try splitting the line into equal parts and see whether the visible letters agree.

### Step 2: Fill using the same place in other blocks
Write the line in blocks, one below another. Each column must have the same letter. A blank takes the letter shown elsewhere in its column.

Example: a _ c a b _ a b c _ b c (12 places, block of 3)
- a _ c
- a b _
- a b c
- _ b c

Columns read a, b, c. The blanks are b, c, a → answer **bca**.

### Step 3: Try the options when stuck
Put each option into the blanks and read the full line. The right option makes a clean repeat. This takes 10-15 seconds per option, so first cut options whose first letter clearly fails.

### Pattern 1: fixed repeating block
The same block repeats: abc abc abc, pqrs pqrs pqrs, baab baab baab.

### Pattern 2: growing block
Each block adds a letter: a, ab, abc, abcd (line: aababcabcd). Or letter counts grow: ab, aabb, aaabbb. Here the block length changes, so read the line as 1 + 2 + 3 + 4 places, or 2 + 4 + 6 places.

### Pattern 3: mirror block
The block reads forwards and then backwards: pqr rqp pqr rqp. A doubled letter in the middle (rr, cc) marks the turning point. Another form walks up and down: a b c d c b a b c d c b a.

### Pattern 4: rotating block
Each new block is the previous block with its first letter moved to the end: abcd, bcda, cdab, dabc. Or the last letter moves to the front: pqr, rpq, qrp. Split the line into equal blocks and check how each block is built from the one before.

### Checks before you mark
- Count the blanks: the answer must have exactly that many letters.
- Fill in and read the whole line once. One wrong letter breaks the repeat.
- If two options both seem to fit, you have picked the wrong block size — try the next size.
- Blanks inside a word-like block (like 'baab') are easy to swap by mistake; fill column by column.

### Quick revision
- Count total places → guess block size (3, 4, 5, 6).
- Write blocks one below another; columns must match.
- Four shapes: fixed block, growing block, mirror block, rotating block.
- A double letter (rr, cc) often marks a mirror turn.
- Always fill and re-read the full line."""


def PATTERNS(P, blank_example):
    """Return {subtopic_id: [pattern, ...]}. P is the builder from _lib."""
    out = {}
    out["series-idea"] = [
        P("se-p1", "Find the next term — choose the family with the difference ladder", "very common",
          "The question gives 5-7 terms ending in '?'. Nothing is hidden in the middle.",
          "1. Look at growth: slow = add, fast = multiply, up-down = two series.\n"
          "2. Write the first difference row; if needed, the second row.\n"
          "3. Continue the row that is regular and climb back up to the next term.\n"
          "4. Check the rule on every given term.\n\n"
          "**Why it works:** every exam series is built by one small repeated rule, and differences expose adding-type rules at once.",
          "**6, 11, 21, 36, 56, ?**",
          "Differences: 5, 10, 15, 20 → next difference 25. 56 + 25 = **81**.",
          r"d_n = a_{n+1} - a_n"),
        P("se-p2", "Missing term in the middle of the series", "very common",
          "A '?' sits between given terms (e.g. 7, 15, ?, 63, 127).",
          "1. Find the rule from the terms on both sides of the gap.\n"
          "2. Fill the gap from the term before it.\n"
          "3. Check that the term after the gap follows from your answer.\n\n"
          "**Why it works:** a middle term must fit twice — with its left neighbour and its right neighbour — so the double check removes wrong guesses.",
          "**7, 15, ?, 63, 127**",
          "15 = 7×2 + 1 and 127 = 63×2 + 1, so the rule is ×2 + 1. ? = 15×2 + 1 = **31**. Check: 31×2 + 1 = 63 ✓."),
        P("se-p3", "Series with fractions, decimals or halving", "common",
          "Terms are decimals (0.5, 1.5 ...), fractions, or keep getting halved (240, 120, 60 ...).",
          "1. Treat decimals exactly like whole numbers: try ×k or ÷k first.\n"
          "2. For fractions, write the numerators as one series and the denominators as another.\n"
          "3. Build the answer in the same form as the terms.\n\n"
          "**Why it works:** decimals and fractions only change how the numbers look, not the rule behind them.",
          "**81, 27, 9, 3, 1, ?**",
          r"Each term is ÷3. 1 ÷ 3 = **$\frac{1}{3}$**."),
        P("se-p4", "Two missing terms — choose the correct pair", "common",
          "Two '?' marks in one series; each option is a pair of numbers.",
          "1. Find the rule from the visible terms.\n"
          "2. Fill the first blank, then keep going to the second blank.\n"
          "3. Check the terms right after each blank.\n"
          "4. Eliminate options where only one of the two numbers is right.\n\n"
          "**Why it works:** both numbers come from the same rule, so one wrong number kills the option.",
          "**5, ?, 15, 20, ?, 30**",
          "The rule is +5. First blank = 5 + 5 = 10; second blank = 20 + 5 = 25. Answer **10, 25**."),
    ]
    out["number-series"] = [
        P("se-p5", "Constant or growing difference (AP and near-AP)", "very common",
          "Terms grow slowly and steadily; the gaps are equal or rise/fall by the same amount.",
          "1. Write the differences.\n"
          "2. If they are equal, add the same number again.\n"
          "3. If they change by a fixed amount (2, 4, 6, 8), continue that row.\n\n"
          "**Why it works:** an adding rule shows itself directly in the difference row.",
          "**4, 6, 10, 16, 24, ?**",
          "Differences: 2, 4, 6, 8 → next 10. 24 + 10 = **34**.",
          r"a_{n+1} = a_n + d,\quad d \text{ constant or rising evenly}"),
        P("se-p6", "Multiply and add/subtract (×k ± r)", "very common",
          "Terms roughly double or triple each time; the ratio is almost (but not exactly) constant.",
          "1. Divide a term by the previous one to guess k (2, 3, 4 ...).\n"
          "2. Compute k × previous and see the small left-over r.\n"
          "3. Confirm the same k and r for every step, then apply.\n\n"
          "**Why it works:** a fixed multiply-then-add rule makes the ratio almost constant, and the left-over is the same each time.",
          "**2, 5, 14, 41, ?**",
          "2×3 − 1 = 5, 5×3 − 1 = 14, 14×3 − 1 = 41. Next: 41×3 − 1 = **122**.",
          r"a_{n+1} = k\,a_n \pm r"),
        P("se-p7", "Squares, cubes and n(n+1) based terms", "very common",
          "Terms sit on or just beside squares (4, 9, 16, 25) or cubes (8, 27, 64), or look like 2, 6, 12, 20.",
          "1. Compare every term with the nearest square or cube.\n"
          "2. Find the fixed adjustment (−1, +1, +2) or the n(n+1) form.\n"
          "3. Use the next n.\n\n"
          "**Why it works:** squares and cubes grow in a special way, so terms near them are easy to recognise once you know the tables.",
          "**0, 3, 8, 15, 24, ?**",
          "Terms are 1²−1, 2²−1, 3²−1, 4²−1, 5²−1. Next: 6² − 1 = **35**.",
          r"a_n = n^2 \pm k,\ \ n^3 \pm k,\ \ n(n+1)"),
        P("se-p8", "Two-level difference (second differences follow a rule)", "common",
          "The first differences are not equal, but they themselves rise in a pattern (1, 3, 6, 10 ...).",
          "1. Write the first difference row.\n"
          "2. Write the second difference row under it.\n"
          "3. Continue the second row, then the first row, then the series.\n\n"
          "**Why it works:** each extra ladder row removes one layer of the rule until a plain pattern remains.",
          "**3, 4, 7, 13, 23, ?**",
          "First differences: 1, 3, 6, 10. Second: 2, 3, 4 → next 5. Next first difference = 10 + 5 = 15. 23 + 15 = **38**.",
          r"\Delta^2 a_n \text{ follows a simple rule}"),
        P("se-p9", "Alternate (interleaved) two-in-one series", "common",
          "The series goes up and down, or big and small numbers take turns.",
          "1. Separate the terms in odd places (1st, 3rd, 5th ...) and even places (2nd, 4th ...).\n"
          "2. Solve each small series on its own.\n"
          "3. Decide whether the '?' is an odd or even place, and take the answer from that series.\n\n"
          "**Why it works:** two independent rules are simply written one after the other.",
          "**1, 10, 2, 20, 3, 30, ?**",
          "Odd places: 1, 2, 3 → next 4. Even places: 10, 20, 30. The 7th term is an odd place → **4**."),
        P("se-p10", "Mixed operations (×1+1, ×2+2 ... or operations taking turns)", "common",
          "Terms grow faster and faster with no constant ratio; or operations clearly take turns (+, ×, +, ×).",
          "1. Try ×1+1, ×2+2, ×3+3 (or ×1−1, ×2−2 ...).\n"
          "2. Try two operations taking turns (+1 then ×2).\n"
          "3. Try gaps with changing signs (+2, −3, +4, −5).\n"
          "4. Continue the operation pattern for the next step.\n\n"
          "**Why it works:** the operation itself forms a simple series, so the next operation is predictable.",
          "**1, 2, 6, 21, 88, ?**",
          "1×1+1 = 2, 2×2+2 = 6, 6×3+3 = 21, 21×4+4 = 88. Next: 88×5+5 = **445**.",
          r"a_{n+1} = n\,a_n + n"),
        P("se-p11", "Fibonacci type (sum of previous terms)", "occasional",
          "Each term is close to the sum of the two (or three) terms before it.",
          "1. Add the previous two terms and compare with the next term.\n"
          "2. If that fails, add the previous three.\n"
          "3. Continue the same addition.\n\n"
          "**Why it works:** such a series grows by feeding on itself, so its difference row copies the series.",
          "**1, 1, 2, 3, 5, 8, ?**",
          "Each term = sum of the previous two. 5 + 8 = **13**.",
          r"a_{n+2} = a_{n+1} + a_n"),
        P("se-p12", "Differences are squares, cubes, primes or powers of 2", "common",
          "The difference row is itself a famous list: 1, 4, 9, 16 / 1, 8, 27 / 2, 3, 5, 7, 11 / 1, 2, 4, 8.",
          "1. Write the differences.\n"
          "2. Match the row to squares, cubes, primes or powers of 2.\n"
          "3. Take the next member of that list and add it.\n\n"
          "**Why it works:** the examiner simply adds a famous list term by term.",
          "**5, 6, 10, 19, 35, ?**",
          "Differences: 1, 4, 9, 16 (squares) → next 25. 35 + 25 = **60**.",
          r"a_{n+1} = a_n + n^2 \ (\text{or } n^3,\ p_n,\ 2^n)"),
    ]
    out["letter-series"] = [
        P("se-p13", "Single letters with a constant step (forward, backward, wrap-around)", "very common",
          "Single letters that move the same distance each time, e.g. D, H, L, P.",
          "1. Convert letters to positions (EJOTY anchors).\n"
          "2. Find the constant step.\n"
          "3. Add it; if the result passes 26, subtract 26 (below 1, add 26).\n\n"
          "**Why it works:** a letter series is a number series in disguise.",
          "**D, H, L, P, ?**",
          "Positions 4, 8, 12, 16 → +4. 16 + 4 = 20 = **T**.",
          r"L_{n+1} = L_n + k \pmod{26}"),
        P("se-p14", "Rising or falling step between letters", "very common",
          "The gaps between letters grow (+1, +2, +3) or shrink by a fixed amount.",
          "1. Write positions and the step row.\n"
          "2. Continue the step row.\n"
          "3. Add the next step to the last letter.\n\n"
          "**Why it works:** it is the letter version of the growing-difference number series.",
          "**A, C, F, J, O, ?**",
          "Steps +2, +3, +4, +5 → next +6. O(15) + 6 = 21 = **U**."),
        P("se-p15", "Two letter series mixed (alternate letters or alternating steps)", "common",
          "Letters jump forward and back, or the same two steps keep taking turns.",
          "1. Split odd places and even places, or write the step row.\n"
          "2. Solve each small series, or continue the step cycle.\n"
          "3. Pick the series that the '?' belongs to.\n\n"
          "**Why it works:** two simple rules written one after the other look messy only when read together.",
          "**B, Y, D, W, F, U, ?**",
          "Odd places B, D, F (+2) → next H. Even places Y, W, U (−2). The 7th term is an odd place → **H**."),
        P("se-p16", "Letter-cluster series (each slot is its own series)", "very common",
          "Every term is a group of 2-4 letters, e.g. AC, EG, IK.",
          "1. Take the first letter of every cluster — find its rule.\n"
          "2. Do the same for the second letter, third letter ...\n"
          "3. Join the next letters of all slots.\n\n"
          "**Why it works:** each slot moves by its own rule, often the same step, sometimes opposite directions.",
          "**AC, EG, IK, ?**",
          "First letters A, E, I (+4) → M. Second letters C, G, K (+4) → O. Answer **MO**."),
        P("se-p17", "Letter positions follow squares or primes", "occasional",
          "The steps look irregular, but the positions are 1, 4, 9, 16 ... or 2, 3, 5, 7, 11 ...",
          "1. Write the positions of all letters.\n"
          "2. Check squares and primes directly on the positions.\n"
          "3. Take the next square or prime and convert it to a letter.\n\n"
          "**Why it works:** the examiner hides a famous number list behind letters.",
          "**C, E, G, K, M, ?**",
          "Positions 3, 5, 7, 11, 13 are primes. Next prime 17 = **Q**."),
    ]
    out["alphanumeric-series"] = [
        P("se-p18", "Letter + number terms with two independent tracks", "very common",
          "Each term is one letter and one number (B2, D4 ...), and the number does not match the letter position.",
          "1. Write the letters in one column and the numbers in another.\n"
          "2. Solve the letter track (positions, step) and the number track (+k, ×k, squares) separately.\n"
          "3. Join the answers in the same format.\n\n"
          "**Why it works:** the two parts are two separate series written side by side.",
          "**K5, M10, O15, Q20, ?**",
          "Letters K, M, O, Q (+2) → S. Numbers 5, 10, 15, 20 (+5) → 25. Answer **S25**."),
        P("se-p19", "Number linked to the letter's position", "common",
          "The number equals the letter's position, its square, or its reverse position (C3, F6 / B4, D16).",
          "1. Check if number = position (or position², or 27 − position) for every term.\n"
          "2. Find the next letter.\n"
          "3. Compute its number by the same link.\n\n"
          "**Why it works:** once the link is confirmed, the whole question reduces to one letter series.",
          "**E5, H8, K11, ?**",
          "Numbers equal positions (E=5, H=8, K=11). Letters +3 → N = 14. Answer **N14**."),
        P("se-p20", "Clusters with two or more letters and a number", "common",
          "Terms like AB2, DE4 or 2CZ, 4EX — more than one letter slot plus a number.",
          "1. Make one column per slot (each letter place, the number).\n"
          "2. Solve every column separately.\n"
          "3. Assemble the next term in the same order.\n\n"
          "**Why it works:** every slot is independent; three small series are easier than one big cluster.",
          "**AZ1, BY2, CX3, ?**",
          "First letters A, B, C (+1) → D; second letters Z, Y, X (−1) → W; numbers +1 → 4. Answer **DW4**."),
        P("se-p21", "Missing alphanumeric term in the middle", "common",
          "The '?' is in the middle of an alphanumeric series.",
          "1. Find each track from the visible terms on both sides.\n"
          "2. Fill the letter and the number of the gap.\n"
          "3. Check the term after the gap.\n\n"
          "**Why it works:** each track must pass through the gap smoothly.",
          "**B3, E6, ?, K12, N15**",
          "Letters B, E, _, K, N (+3) → H. Numbers 3, 6, _, 12, 15 (+3) → 9. Answer **H9**."),
    ]
    out["wrong-number"] = [
        P("se-p22", "Wrong term in a difference (AP / growing gap) series", "very common",
          "Gaps are almost equal or almost evenly rising, with two neighbouring gaps spoilt.",
          "1. Write the differences.\n"
          "2. Find the two neighbouring bad gaps.\n"
          "3. The term between them is wrong; confirm by putting the correct value back.\n\n"
          "**Why it works:** one wrong term changes both the gap before it and the gap after it.",
          "**8, 12, 16, 21, 24, 28**",
          "Differences 4, 4, 5, 3, 4 — the bad gaps 5 and 3 sit around **21** (should be 20)."),
        P("se-p23", "Wrong term in a ratio or ×k ± r series", "common",
          "Terms roughly double or triple; one term is slightly off.",
          "1. Find k (and r) from the first few terms.\n"
          "2. Rebuild the series from the first term.\n"
          "3. The first term that does not match is the wrong one.\n\n"
          "**Why it works:** the next term is made from the correct value, so rebuilding from the start finds the break.",
          "**3, 6, 12, 25, 48, 96**",
          "Rule ×2: 3, 6, 12, 24, 48, 96. The term **25** is wrong (should be 24)."),
        P("se-p24", "Wrong term in a square / cube series", "common",
          "Terms are near squares or cubes; one term misses by 1 or 2.",
          "1. Match every term with n², n³ or n(n+1) plus a fixed adjustment.\n"
          "2. The term that does not fit the adjustment is wrong.\n\n"
          "**Why it works:** squares and cubes are exact, so a near-miss stands out.",
          "**4, 9, 16, 25, 35, 49**",
          "Squares 2² to 7²: 4, 9, 16, 25, 36, 49. **35** is wrong (should be 36)."),
        P("se-p25", "Wrong term in an alternate or mixed-operation series", "common",
          "The series goes up and down, or uses ×1+1, ×2+2 type steps.",
          "1. Split into odd and even places, or list the operation for each step.\n"
          "2. Check each small series or each step separately.\n"
          "3. The one term that breaks its own series is wrong.\n\n"
          "**Why it works:** the error hides inside one of the two small series.",
          "**1, 20, 3, 18, 5, 17, 7**",
          "Odd places 1, 3, 5, 7 fine. Even places 20, 18, _ should be 16 → **17** is wrong."),
        P("se-p26", "Wrong term in a letter / letter-cluster series", "common",
          "Letters or clusters in a series; one of them does not follow the step.",
          "1. Convert letters to positions.\n"
          "2. Find the step pattern (between terms and inside clusters).\n"
          "3. The letter or cluster that breaks it is the answer.\n\n"
          "**Why it works:** it is the same wrong-term method on positions instead of numbers.",
          "**C, F, I, M, O**",
          "Step +3: C, F, I, L, O. **M** is wrong (should be L)."),
    ]
    out["letter-blank-series"] = [
        P("se-p27", "Fixed repeating block", "very common",
          "The line is made of the same 3-6 letter block repeated (abc abc abc ...).",
          "1. Count total places; try block sizes that divide it.\n"
          "2. Write blocks one below another.\n"
          "3. Each column has one letter; fill each blank from its column.\n"
          "4. Read the answer letters in order of the blanks.\n\n"
          "**Why it works:** in a repeating block, every place in a column must hold the same letter.",
          blank_example["fixed"][0], blank_example["fixed"][1]),
        P("se-p28", "Growing block (a, ab, abc ... or ab, aabb, aaabbb)", "common",
          "Letters appear more and more times, or each part is one letter longer than the last.",
          "1. Split the line into parts of length 1, 2, 3, 4 ... (or 2, 4, 6 ...).\n"
          "2. Check that each part adds one letter (or one more of each letter).\n"
          "3. Fill the blanks from the expected parts.\n\n"
          "**Why it works:** the block is not fixed, but its growth rule is.",
          blank_example["growing"][0], blank_example["growing"][1]),
        P("se-p29", "Mirror block (forward then backward)", "common",
          "A doubled letter in the middle (rr, cc) or the letters climb and come back (a b c d c b a).",
          "1. Find the turning point (double letter or highest letter).\n"
          "2. The second half repeats the first half in reverse.\n"
          "3. Use the mirror to fill each blank.\n\n"
          "**Why it works:** a mirror block is a fixed block whose second half copies the first half backwards.",
          blank_example["mirror"][0], blank_example["mirror"][1]),
        P("se-p30", "Rotating block (first letter moves to the end)", "occasional",
          "Equal blocks use the same letters, but each block starts one letter later (abcd, bcda, cdab).",
          "1. Split into equal blocks (size = number of different letters).\n"
          "2. See how each block is the previous one rotated.\n"
          "3. Build every block and read off the blanks.\n\n"
          "**Why it works:** rotation keeps the letters and just shifts the starting point.",
          blank_example["rotating"][0], blank_example["rotating"][1]),
    ]
    return out
