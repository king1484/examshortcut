"""Phase-2 deep content for reasoning/mathematical-operations. Idempotent (upsert by id)."""
import os
import re
import sys
from fractions import Fraction as F
from itertools import combinations

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa

TOPIC = "mathematical-operations"
d = load(TOPIC)

# ---------------- evaluator helpers ----------------
TR = (("×", "*"), ("÷", "/"), ("−", "-"), ("[", "("), ("]", ")"), ("{", "("), ("}", ")"))


def ev(expr):
    """BODMAS value of an expression written with + − × ÷ and brackets (exact Fraction)."""
    s = expr
    for a, b in TR:
        s = s.replace(a, b)
    s = re.sub(r"\d+", lambda m: f"F({m.group()})", s)
    return eval(s, {"F": F})


def ltr(expr):
    """Strict left-to-right value (the 'BODMAS skipped' trap). No brackets."""
    toks = re.findall(r"\d+|[+−×÷]", expr)
    v = F(toks[0])
    for op, n in zip(toks[1::2], toks[2::2]):
        n = F(n)
        v = {"+": v + n, "−": v - n, "×": v * n, "÷": v / n}[op]
    return v


def fmt(v):
    v = F(v)
    if v.denominator == 1:
        return str(v.numerator)
    if 10 ** 6 % v.denominator == 0:
        return str(float(v))
    return f"{v.numerator}/{v.denominator}"


def mp(expr, m):
    """Simultaneous symbol substitution (each symbol converted once)."""
    return "".join(m.get(c, c) for c in expr)


def swapn(expr, a, b):
    a, b = str(a), str(b)
    return re.sub(r"\d+", lambda x: b if x.group() == a else a if x.group() == b else x.group(), expr)


def eq_true(eq):
    parts = eq.split("=")
    assert len(parts) == 2, eq
    return ev(parts[0]) == ev(parts[1])


def fill(template, signs):
    """Replace each '*' of the template, in order, with the given signs."""
    out = template
    for s in signs:
        out = out.replace("*", s, 1)
    assert "*" not in out
    return out


def only_one(cands, test, ans):
    ok = [c for c in cands if test(c)]
    assert ok == [ans], (ok, ans)


def num_swap_ok(lhs, rhs, pair):
    return ev(swapn(lhs, *pair)) == F(rhs)


def all_num_pairs(lhs):
    nums = list(dict.fromkeys(re.findall(r"\d+", lhs)))
    return list(combinations(nums, 2))


SIGNS = ["+", "−", "×", "÷"]


def sign_swap(expr, a, b):
    return mp(expr, {a: b, b: a})


# ---------------- verify + fix EXISTING questions ----------------
M4 = {"+": "×", "−": "÷", "×": "+", "÷": "−"}
assert ev(mp("6 + 2 × 4 ÷ 2 − 2", M4)) == 15  # ex1
assert ev(sign_swap("3 × 4 + 5 − 6", "+", "×")) == 17  # ex2
ex3_ok = [p for p in all_num_pairs("4 + 2 × 6 − 3") if num_swap_ok("4 + 2 × 6 − 3", 20, p)]
assert ex3_ok == [("2", "3")], ex3_ok
ex4 = ["7 × 2 + 8 ÷ 4 = 18", "24 ÷ 6 − 2 × 3 = 1", "5 × 4 + 6 ÷ 2 = 23", "9 + 6 ÷ 2 − 3 = 11"]
assert [e for e in ex4 if eq_true(e)] == ["5 × 4 + 6 ÷ 2 = 23"]
assert ev(mp("3 + 4 × 2", {"+": "×", "×": "−"})) == 10  # 1
assert ev(mp("16 ÷ 4 + 3 × 6 − 2", {"÷": "+", "+": "−", "×": "÷", "−": "×"})) == 19  # 2
assert ev(swapn(sign_swap("2 + 8 × 3 − 5", "+", "×"), 2, 8)) == 14  # 3
assert ev("12 ÷ 4 × 2") == 6  # 4
assert ev("5 × 2 + 3") == 13  # 5
ex6 = ["20 − 4 ÷ 2 + 6 = 16", "7 × 2 + 8 ÷ 4 = 18", "36 ÷ 6 × 2 + 1 = 14", "15 ÷ 3 + 2 × 4 = 13"]
assert [e for e in ex6 if eq_true(e)] == ["15 ÷ 3 + 2 × 4 = 13"]
assert ev(mp("(24 + 8) − 2 ÷ 4", {"+": "÷", "−": "×", "÷": "+"})) == 10  # 7
assert ev("(24 + 8) − 2 ÷ 4") == F(63, 2) and ev("(24 + 8) × 2 ÷ 4") == 16
ex8 = ["9 + 6 − 3 × 4 = 5", "15 − 5 + 4 × 2 = 13", "10 − 4 + 2 × 3 = 8", "12 + 3 − 6 ÷ 2 = 11"]
assert [e for e in ex8 if eq_true(sign_swap(e, "+", "−"))] == ["10 − 4 + 2 × 3 = 8"]
assert ev(mp("15 − 7 + 4 + 2", {"−": "+", "+": "−"})) == 16  # 9
L10 = "8 × 4 − 6 + 3"
sw10 = {p: ev(swapn(L10, *p)) for p in all_num_pairs(L10)}
assert [p for p, v in sw10.items() if v == 35] == [("6", "3")]
assert ev(mp("18 ÷ 6 − 3 × 2 + 4", {"÷": "+", "−": "÷", "×": "−", "+": "×"})) == 12  # 11
assert ev(sign_swap("36 ÷ 4 × 3 − 5", "×", "÷")) == 43  # 12
assert [s for s in ["+, ÷, ×", "÷, −, ×", "÷, +, ×", "÷, ×, +"]
        if ev(fill("24 * 8 * 4 * 2", s.split(", "))) == 11] == ["÷, +, ×"]  # 13
assert ev(mp("(16 + 8) × 2 − 6", {"+": "×", "×": "−"})) == 120  # 14
assert ev(mp("20 + 5 − 2", {"+": "÷", "−": "×"})) == 8  # 15

patch_q(d, "rsn-mathops-ex4", solution=(
    "Evaluate each option with BODMAS, in the order given:\n\n"
    "- 7 × 2 + 8 ÷ 4 = 14 + 2 = 16, not 18 ✗\n"
    "- 24 ÷ 6 − 2 × 3 = 4 − 6 = −2, not 1 ✗\n"
    "- 5 × 4 + 6 ÷ 2 = 20 + 3 = **23** ✓\n"
    "- 9 + 6 ÷ 2 − 3 = 9 + 3 − 3 = 9, not 11 ✗\n\n"
    "Only **5 × 4 + 6 ÷ 2 = 23** is correct."))
patch_q(d, "rsn-mathops-6", solution=(
    "Evaluate each option with BODMAS, in the order given:\n\n"
    "- 20 − 4 ÷ 2 + 6 = 20 − 2 + 6 = 24, not 16 ✗\n"
    "- 7 × 2 + 8 ÷ 4 = 14 + 2 = 16, not 18 ✗\n"
    "- 36 ÷ 6 × 2 + 1 = 6 × 2 + 1 = 13, not 14 ✗\n"
    "- 15 ÷ 3 + 2 × 4 = 5 + 8 = **13** ✓\n\n"
    "Only **15 ÷ 3 + 2 × 4 = 13** is correct."))
patch_q(d, "rsn-mathops-7", solution=(
    "Substitute every sign once (brackets stay where they are): (24 + 8) − 2 ÷ 4 → **(24 ÷ 8) × 2 + 4**. "
    "Bracket first: 24 ÷ 8 = 3. Then 3 × 2 = 6 and 6 + 4 = **10**.\n\n"
    "Trap check: 16 is what you get if you convert only the signs outside the bracket and forget the '+' inside it: "
    "(24 + 8) × 2 ÷ 4 = 32 × 2 ÷ 4 = 16. (The original expression, with no substitution at all, is 32 − 0.5 = 31.5.)"))
sw_txt = "; ".join(f"({a}, {b}) → {swapn(L10, a, b)} = {fmt(sw10[(a, b)])}{' ✓' if sw10[(a, b)] == 35 else ' ✗'}"
                   for a, b in sw10)
patch_q(d, "rsn-mathops-10", solution=(
    f"Sweep every pair of numbers and evaluate with BODMAS: {sw_txt}.\n\n"
    "Only interchanging **6 and 3** gives 8 × 4 − 3 + 6 = 32 − 3 + 6 = **35**."))

# ---------------- notes ----------------
NOTES = {}
NOTES["mathops-idea"] = r"""### What this topic tests
In mathematical-operation questions the numbers are small and the sums are easy. What the examiner really checks is whether you follow the **order of operations** without a single slip. Think of a shop bill: 3 pens at ₹10 each and 2 notebooks at ₹40 each cost 3 × 10 + 2 × 40 = 30 + 80 = ₹110. Nobody adds 10 + 2 first. That habit of "multiply first, then add" is exactly the rule you need here.

### BODMAS in simple words
BODMAS tells you which part of an expression to work out first:

| Letter | Meaning | Example |
|---|---|---|
| B | Brackets | (6 + 2) is done first |
| O | Orders: powers, roots, "of" | $3^2$, $\sqrt{16}$, half of 10 |
| D, M | Division and Multiplication | same rank |
| A, S | Addition and Subtraction | same rank |

Example: 18 + 24 ÷ 6 × 3 − 5. First the ÷ and ×: 24 ÷ 6 = 4, then 4 × 3 = 12. Now 18 + 12 − 5 = **25**.

### Same rank means left to right
Division is **not** "before" multiplication, and addition is **not** "before" subtraction. When operators have the same rank, simply go from left to right.

- 96 ÷ 8 × 4 = 12 × 4 = **48** (not 96 ÷ 32 = 3).
- 60 − 12 + 8 = 48 + 8 = **56** (not 60 − 20 = 40).

This one rule decides many answers, because examiners love to put ÷ before × or − before +.

### Brackets inside brackets
When brackets are nested, open them from the inside: first ( ), then { }, then [ ].

Example: 100 − [20 + {30 − (12 − 4) × 2}]. Inner bracket: 12 − 4 = 8. Curly bracket: 30 − 8 × 2 = 30 − 16 = 14. Square bracket: 20 + 14 = 34. Finally 100 − 34 = **66**. Inside every bracket, BODMAS still applies (8 × 2 before 30 − ...).

### Finding a missing number
Some questions hide one number: 18 + 6 × ? − 4 = 38. Undo the steps in reverse order.

1. Move the loose terms: 6 × ? = 38 + 4 − 18 = 24.
2. Undo the multiplication: ? = 24 ÷ 6 = **4**.
3. Put 4 back and check: 18 + 24 − 4 = 38 ✓.

Always check the answer by putting it back. It takes five seconds and removes every doubt.

### How wrong options are built
Almost every wrong option in this topic comes from one of three slips:

- **Left-to-right slip**: the student ignored BODMAS. For 7 + 8 × 2 − 5, left to right gives 15 × 2 − 5 = 25, but the correct value is 7 + 16 − 5 = 18.
- **Sign slip**: a minus sign is carried wrongly, e.g. 45 − 5 × 6 + 9 read as 45 − (30 + 9).
- **Forgotten term**: the last "− 5" or "+ 4" is left out.

If your answer matches an option, still ask: "Did I do × and ÷ before + and −?" If yes, mark it and move on.

### Speed habits
- Circle every × and ÷ first; do those pieces; then read the line once more for + and −.
- Write the reduced line after each step (18 + 12 − 5). Short lines prevent mistakes.
- Use the last digit to check: 7 × 8 ends in 6, so 56 is right and 54 is not.

### Quick revision
- Order: Brackets → Orders → ÷ and × (left to right) → + and − (left to right).
- ÷ and × have equal rank; + and − have equal rank. Same rank = left to right.
- Nested brackets: ( ) then { } then [ ]; BODMAS works inside each bracket too.
- Missing number: undo the steps backwards, then put the number back to check.
- The left-to-right value is the examiner's favourite wrong option.
"""

NOTES["sign-substitution"] = r"""### What sign substitution means
Imagine a calculator whose keys have been relabelled: the key marked "+" now multiplies and the key marked "×" now adds. The question gives you such a list of new meanings and an expression. You must first convert the expression into normal maths and only then calculate. In SSC, Railway and Banking papers this is one of the most frequent reasoning questions, and it is almost pure marks if you are careful.

### The three-step method
1. **Write the mapping** in a small table in your rough space, e.g. + → ×, − → ÷, × → +, ÷ → −.
2. **Rewrite the whole line** with the new signs. Keep every number and every bracket exactly where it is.
3. **Calculate with BODMAS** on the rewritten line.

Example: If + means ×, − means ÷, × means + and ÷ means −, find 6 + 2 × 4 ÷ 2 − 2.
Rewrite: 6 × 2 + 4 − 2 ÷ 2. Now BODMAS: 6 × 2 = 12 and 2 ÷ 2 = 1, so 12 + 4 − 1 = **15**.

### Convert each sign only once
When the list says "+ means × and × means +", both changes happen **at the same time**. Look at the original line, and convert each symbol one time. Do not convert a sign that you have already changed. A good habit is to write the new line below the old one, symbol by symbol, looking only at the old line.

### Partial substitution
Sometimes only two signs are changed ("+ means ×, × means +"). The other signs keep their normal meaning. Example: 9 + 4 × 7 becomes 9 × 4 + 7 = 36 + 7 = **43**.

### Letter-coded signs
The signs may be replaced by letters: "A means +, B means −, C means ×, D means ÷". Then 18 C 4 D 6 A 9 B 5 means 18 × 4 ÷ 6 + 9 − 5. Left to right for × and ÷: 72 ÷ 6 = 12. Then 12 + 9 − 5 = **16**. The method is the same: rewrite first, then calculate.

### Substitution with brackets
Brackets never move and are always solved first, but the signs **inside** the brackets are also converted. Example: if + means ÷ and − means ×, then (24 + 8) − 2 becomes (24 ÷ 8) × 2 = 3 × 2 = 6. Forgetting to convert the sign inside the bracket is a very common loss.

### Choose the correct equation after substitution
A harder form gives a mapping and four equations. Convert each left side, evaluate it, and compare with the right side. Exactly one option balances. Work in writing, one option per line.

### Know the planted wrong answers
Most options are made from these slips:

| Slip | What the student did |
|---|---|
| Mapping ignored | calculated the original expression |
| BODMAS skipped | rewrote correctly but went left to right |
| Half substitution | converted some signs and missed others |

If your answer equals the original expression's value, you forgot to substitute. That quick check saves many marks.

### Quick revision
- Mapping table → rewrite the full line → BODMAS. Never substitute and calculate together.
- All changes are simultaneous: convert each symbol once, reading the ORIGINAL line.
- Signs not in the list keep their normal meaning.
- Letters for signs (A, B, P, Q...) are handled the same way.
- Convert signs inside brackets too; brackets are still solved first.
- Wrong options = original value, left-to-right value, half-substituted value.
"""

NOTES["interchange-signs"] = r"""### What "interchange" means
To interchange two things means to **swap** them: wherever the first stood, the second now stands, and the other way round. "Interchange + and ×" turns 3 × 4 + 5 into 3 + 4 × 5. It is like two students exchanging seats: both move. This is different from substitution, where the change may go in one direction only.

### Type 1: swap two signs, then find the value
Rewrite the line with the two signs exchanged, then use BODMAS.
Example: interchange + and ×; find 3 × 4 + 5 − 6. New line: 3 + 4 × 5 − 6 = 3 + 20 − 6 = **17**.

### Type 2: swap two numbers (and maybe two signs too)
"Interchange 2 and 8" means every 2 becomes 8 and every 8 becomes 2. Do all swaps in **one** rewrite, then calculate.
Example: interchange + and × and also 2 and 8 in 2 + 8 × 3 − 5. New line: 8 × 2 + 3 − 5 = 16 + 3 − 5 = **14**.
Careful: swap whole numbers only. If the swap is 2 and 5, the number 25 does not change.

### Type 3: which two numbers must be swapped to make the equation true?
You get a wrong equation, for example 4 + 2 × 6 − 3 = 20, and four pairs in the options. Do a **sweep**: try each option pair, evaluate the new left side, and stop when it equals the right side.

- (4, 2): 2 + 4 × 6 − 3 = 23 ✗
- (2, 3): 4 + 3 × 6 − 2 = 4 + 18 − 2 = 20 ✓

With 4 numbers there are only 6 possible pairs; with 5 numbers there are 10. You normally test only the 4 option pairs.

### Type 4: which two signs must be swapped?
Same sweep, but you swap two operators. Example: 12 + 6 ÷ 3 − 2 × 4 = 18. Try + and −: 12 − 6 ÷ 3 + 2 × 4 = 12 − 2 + 8 = 18 ✓.

### Type 5: after a given swap, which equation is correct?
The swap is stated first, and four equations follow. Apply the swap to each **left side**, evaluate, and compare with its right side. Only one balances.

### Shortcuts that save time
- **Swapping the two numbers around a single ×** (like 8 × 4 to 4 × 8) changes nothing, because order does not matter in multiplication. Skip such pairs.
- **Size check**: if the target is large (like 81) you need a big product; if it is small, look for a division or subtraction to be created.
- **Last-digit check**: 8 × 6 ends in 8; if the target ends in 5 you may drop that option at once.
- **Division must usually come out exact**: a swap that creates 7 ÷ 5 rarely gives a whole-number answer, so test it last.

### Traps
- Swapping only one direction (changing + to × but leaving the old × as it was).
- Forgetting a second occurrence of the same sign or number.
- Evaluating the swapped line left to right instead of by BODMAS.

### Quick revision
- Interchange = two-way swap; every occurrence of both items changes.
- Apply all swaps (signs and numbers) in ONE rewrite, then BODMAS.
- "Which pair to swap": sweep the option pairs in a fixed order and stop at the one that balances.
- Swapping the two numbers of one product changes nothing: skip it.
- Use size and last-digit checks to cut options fast.
"""

NOTES["balance-equation"] = r"""### What balancing means
An equation is like a weighing scale: the left side and the right side must have the same value. In these questions you either check which equation is already balanced, or choose the signs that will balance it. Nothing is hidden; you only need clean BODMAS and a fixed order of testing.

### Type 1: pick the correct equation
Four full equations are given; exactly one is true. Evaluate each left side and compare.
Example options: 16 ÷ 4 × 2 + 6 = 14, and 7 + 8 × 2 − 5 = 25. First one: 4 × 2 + 6 = 14 ✓. Second one: 7 + 16 − 5 = 18, not 25 ✗ (25 is the left-to-right value, a planted trap).

### Type 2: fill the blanks with a pair or set of signs
"Which pair of signs makes 14 ? 2 ? 3 = 21 true?" Put each option in and evaluate.
- ÷ and ×: 14 ÷ 2 × 3 = 7 × 3 = **21** ✓
- × and −: 28 − 3 = 25 ✗
With three or four blanks the options are full sets like "−, +, ×". Replace the blanks in order from left to right.

### Type 3: replace the * signs in order
Recent papers write the question as: "Select the correct combination of mathematical signs to sequentially replace the * signs and balance the equation", e.g. `21 * 7 * 5 * 4 * 3 = 27`. "Sequentially" means the first sign of the option goes into the first *, the second into the second *, and so on.
Option "÷, ×, +, ×": 21 ÷ 7 × 5 + 4 × 3 = 3 × 5 + 12 = 15 + 12 = **27** ✓.

### Type 4: the = sign is one of the options
Here the equation has no = sign yet: `12 * 4 * 3 * 16`, and one option sign is "=". After filling, check that the part before = equals the part after =.
"×, ÷, =" gives 12 × 4 ÷ 3 = 16 → 48 ÷ 3 = 16 ✓.
Tip: the = sign usually sits just before the last number, but always test; examiners move it to catch guessers.

### A fast testing order
1. Look at the right side. Is it big or small compared with the numbers? A big target needs ×; a small one needs ÷ or −.
2. Test options that create **exact** divisions first. 72 ÷ 8 = 9 is friendly; 7 ÷ 5 is usually a dead end.
3. Use the **last digit**: if the left side must end in 7 and your option gives a product ending in 0 plus 5, drop it.
4. Once one option balances, still glance at the rest only if time allows; in a correct question only one works.

### Common mistakes
- Applying BODMAS in your head and slipping on the order (× before +).
- Putting option signs in the wrong blanks (reading the option from the right).
- In "=" questions, calculating the whole line as one expression instead of comparing both sides.

### Quick revision
- Balanced = left value equals right value; test each option in writing.
- "Sequentially replace *" = first sign into first *, second into second, and so on.
- When "=" is among the signs, compare the two sides after filling.
- Target size tells you whether you need × (big) or ÷/− (small).
- Exact divisions and last digits cut options quickly.
- The left-to-right value is the usual trap option.
"""

NOTES["defined-operations"] = r"""### What a defined operation is
Sometimes the examiner invents a new symbol, like ★, # or @, and tells you what it does. For example, "a ★ b = 2a + 3b". The symbol is just a short name for a small formula. To find 5 ★ 4 you put a = 5 and b = 4 into the formula: 2 × 5 + 3 × 4 = 10 + 12 = **22**. It is like a shop rule: "price of a combo = 2 × price of burger + 3 × price of drink" — you just plug in the prices.

### Type 1: the formula is given
Put the first number in place of a and the second in place of b. The **order matters**: with a ★ b = 2a + 3b, 5 ★ 4 = 22 but 4 ★ 5 = 8 + 15 = 23. Always check which number is a.

Common formulas: $a^2 + b^2$, $a^2 - ab + b^2$, $\frac{a+b}{a-b}$, $3a - b$, $ab + a + b$.

### Type 2: nested (chained) operations
(7 @ 5) @ 3 means: first work out 7 @ 5, then use that answer as the new a. With a @ b = (a + b) ÷ (a − b): 7 @ 5 = 12 ÷ 2 = 6. Then 6 @ 3 = 9 ÷ 3 = **3**. Brackets decide which operation is done first, just like BODMAS. When two symbols are defined, work out each bracket with its own formula, then combine.

### Type 3: find the hidden rule from examples
The question shows solved examples such as 5 # 3 = 34 and 6 # 2 = 40, and asks for 7 # 4. You must guess the rule and test it on **every** example.
Try the common rules in this order:

| Try | 5 and 3 give | 6 and 2 give |
|---|---|---|
| a + b, a × b | 8, 15 | 8, 12 |
| $a^2 + b^2$ | 34 ✓ | 40 ✓ |
| $a^2 - b^2$ | 16 | 32 |
| $(a+b)^2$ | 64 | 64 |

So the rule is $a^2 + b^2$ and 7 # 4 = 49 + 16 = **65**.
A rule that fits only one example is not the rule. Two different rules can fit one example; the second example decides.

### Type 4: conditional definitions
The formula may depend on a condition: "a ▲ b = a − b if a > b, and a + b if a ≤ b". Check the condition **every time** you use the symbol. 9 ▲ 4: 9 > 4, so 9 − 4 = 5. Then 5 ▲ 7: 5 ≤ 7, so 5 + 7 = **12**. Students often use the first case again without checking; that is the trap.

### Rules that appear most often
- Sum or difference of squares: $a^2 \pm b^2$.
- Square of sum or difference: $(a \pm b)^2$.
- Product plus sum: $ab + a + b$.
- Weighted sums: $2a + 3b$, $3a - b$.
- Mixed: $a^2 + b$, $a \times b - a$.

### How to avoid mistakes
- Write "a = __, b = __" before plugging in.
- In nested questions, finish the inner bracket fully and write its value.
- For hidden rules, test on all examples before answering.
- Negative or fraction results are allowed only if the question allows them; if every option is a whole number and yours is not, recheck.

### Quick revision
- Defined symbol = small formula; plug in a (first number) and b (second number).
- Order of a and b matters unless the formula is symmetric.
- Nested: inner bracket first; its result becomes the new input.
- Hidden rule: try a+b, ab, $a^2 \pm b^2$, $(a \pm b)^2$, ab+a+b; it must fit EVERY example.
- Conditional: re-check the condition at each step.
"""

# ---------------- patterns ----------------
PATS = {}
PATS["mathops-idea"] = [
    P("mo-p1", "Evaluate a mixed expression with BODMAS", "common",
      "A plain expression with + − × ÷ and no brackets; options include the left-to-right value.",
      "1. Circle × and ÷; work them out left to right.\n2. Then do + and − left to right.\n3. Match with options; the left-to-right value is the trap.\n\nWhy: × and ÷ bind the numbers next to them more tightly than + and −.",
      "Find the value of **18 + 24 ÷ 6 × 3 − 5**.",
      "24 ÷ 6 = 4, 4 × 3 = 12. Then 18 + 12 − 5 = **25**. (Left to right would give 16 — wrong.)"),
    P("mo-p2", "Same-rank operators: left to right", "common",
      "A chain of only ÷ and × (or only + and −), where ÷ comes before × or − before +.",
      "1. Same rank means no priority between them.\n2. Work strictly from left to right.\n\nWhy: BODMAS lists D and M (and A and S) together; the letter order is only for memory.",
      "Find **96 ÷ 8 × 4**.", "96 ÷ 8 = 12, then 12 × 4 = **48** (not 96 ÷ 32 = 3)."),
    P("mo-p3", "Nested brackets", "common",
      "The expression has ( ), { } and [ ] brackets.",
      "1. Solve the innermost ( ) first.\n2. Then { }, then [ ].\n3. Use BODMAS inside every bracket.\n\nWhy: each bracket is a complete small expression whose value feeds the outer one.",
      "Find **[48 ÷ {2 × (10 − 4)}] + 5**.", "10 − 4 = 6; 2 × 6 = 12; 48 ÷ 12 = 4; 4 + 5 = **9**."),
    P("mo-p4", "Find the missing number in an equation", "common",
      "An equation with a '?' in place of one number.",
      "1. Move the known terms to the other side (undo + and −).\n2. Undo × or ÷ around the '?'.\n3. Put the value back to check.\n\nWhy: undoing steps in reverse order keeps both sides equal.",
      "**18 + 6 × ? − 4 = 38**. Find ?", "6 × ? = 38 + 4 − 18 = 24, so ? = **4**. Check: 18 + 24 − 4 = 38 ✓."),
]
PATS["sign-substitution"] = [
    P("mo-p5", "Full four-operator substitution", "very common",
      "'If + means ×, − means ÷, × means +, ÷ means −, then ... = ?' — all four signs are re-assigned.",
      "1. Write the mapping table.\n2. Rewrite the whole line, converting each sign once.\n3. Evaluate with BODMAS.\n\nWhy: separating 'rewrite' from 'calculate' removes sign slips.",
      "If + means ×, − means ÷, × means +, ÷ means −, find **6 + 2 × 4 ÷ 2 − 2**.",
      "Rewrite: 6 × 2 + 4 − 2 ÷ 2 = 12 + 4 − 1 = **15**."),
    P("mo-p6", "Partial (two-sign) substitution", "common",
      "Only two signs are given new meanings; the others stay normal.",
      "1. Change only the listed signs.\n2. Keep the other signs as they are.\n3. BODMAS.\n\nWhy: an unlisted sign keeps its usual job.",
      "If + means × and × means +, find **9 + 4 × 7**.", "Rewrite: 9 × 4 + 7 = 36 + 7 = **43**."),
    P("mo-p7", "Substitution with brackets", "common",
      "The expression under substitution contains brackets.",
      "1. Convert the signs inside AND outside the brackets.\n2. Solve the brackets first, then the rest.\n\nWhy: brackets fix the order, but their signs are still coded.",
      "If + means ÷ and − means ×, find **(24 + 8) − 2**.", "Rewrite: (24 ÷ 8) × 2 = 3 × 2 = **6**."),
    P("mo-p8", "Letter-coded operators", "common",
      "Letters like A, B, C, D (or P, Q, R, S) stand for the four signs.",
      "1. Replace each letter by its sign.\n2. Evaluate with BODMAS.\n\nWhy: a letter is just another name for a sign.",
      "A means +, B means −, C means ×, D means ÷. Find **18 C 4 D 6 A 9 B 5**.",
      "18 × 4 ÷ 6 + 9 − 5 = 12 + 9 − 5 = **16**."),
    P("mo-p9", "Substitute, then pick the correct equation", "occasional",
      "A mapping is given, and the options are four equations; one becomes true after substitution.",
      "1. Convert the left side of each option.\n2. Evaluate and compare with its right side.\n3. Only one balances.\n\nWhy: the right side is already a plain number; only the left side is coded.",
      "If × means + and + means ×, which is correct: 4 × 3 + 2 = 10 or 4 + 3 × 2 = 14?",
      "4 × 3 + 2 → 4 + 3 × 2 = 10 ✓; 4 + 3 × 2 → 4 × 3 + 2 = 14 ✓ — here both hold, so exam versions change one right side. Always evaluate every option."),
]
PATS["interchange-signs"] = [
    P("mo-p10", "Interchange two signs, then evaluate", "common",
      "'If + and ÷ are interchanged, find the value of ...'",
      "1. Swap both signs everywhere (two-way).\n2. BODMAS on the new line.\n\nWhy: interchange is symmetric, so both signs change places.",
      "Interchange + and ×: **3 × 4 + 5 − 6**.", "3 + 4 × 5 − 6 = 3 + 20 − 6 = **17**."),
    P("mo-p11", "Interchange numbers (with or without signs), then evaluate", "common",
      "'If 2 and 8 are interchanged (and + and ×) ...' — numbers are swapped too.",
      "1. Do every swap in one rewrite.\n2. Swap whole numbers only (25 is not changed by swapping 2 and 5).\n3. BODMAS.\n\nWhy: doing swaps one after another invites double swaps.",
      "Interchange + and × and 2 and 8: **2 + 8 × 3 − 5**.", "8 × 2 + 3 − 5 = 16 + 3 − 5 = **14**."),
    P("mo-p12", "Which two numbers to interchange to balance", "common",
      "A false equation and options like '4 and 2', '6 and 3'.",
      "1. For each option, swap the two numbers.\n2. Evaluate the left side; stop when it equals the right side.\n\nWhy: only one pair can restore the balance in a well-set question.",
      "Which two numbers should be interchanged: **4 + 2 × 6 − 3 = 20**?", "Swap 2 and 3: 4 + 3 × 6 − 2 = 20 ✓ → **2 and 3**."),
    P("mo-p13", "Which two signs to interchange to balance", "common",
      "A false equation and options like '+ and −', '× and ÷'.",
      "1. For each option, swap the two signs everywhere.\n2. Evaluate; stop at the one that balances.\n\nWhy: same sweep idea as number swaps, applied to operators.",
      "Which two signs should be interchanged: **12 + 6 ÷ 3 − 2 × 4 = 18**?", "Swap + and −: 12 − 2 + 8 = 18 ✓ → **+ and −**."),
    P("mo-p14", "After a given interchange, which equation is correct", "occasional",
      "The swap is stated; four equations follow.",
      "1. Apply the swap to each left side.\n2. Evaluate and compare with the right side.\n\nWhy: the right sides are plain numbers and do not change.",
      "If + and − are interchanged, is **10 − 4 + 2 × 3 = 8** correct?", "Swap: 10 + 4 − 2 × 3 = 14 − 6 = 8 ✓ — correct."),
]
PATS["balance-equation"] = [
    P("mo-p15", "Pick the arithmetically correct equation", "very common",
      "'Which of the following equations is correct?' with four complete equations.",
      "1. Evaluate each left side with BODMAS.\n2. Compare with the right side; exactly one matches.\n\nWhy: wrong options are usually left-to-right values.",
      "Is **16 ÷ 4 × 2 + 6 = 14** correct?", "4 × 2 + 6 = 8 + 6 = 14 ✓ — yes."),
    P("mo-p16", "Fill the blanks with a sign pair or sign set", "common",
      "'Which pair/set of signs will make 14 ? 2 ? 3 = 21 correct?'",
      "1. Put each option's signs into the blanks, left to right.\n2. Evaluate; keep the one that equals the right side.\n\nWhy: testing is faster and safer than guessing.",
      "**14 ? 2 ? 3 = 21**: try ÷ and ×.", "14 ÷ 2 × 3 = 7 × 3 = **21** ✓."),
    P("mo-p17", "Sequentially replace the * signs", "very common",
      "`21 * 7 * 5 * 4 * 3 = 27` — 'select the combination of signs to sequentially replace *'.",
      "1. First sign → first *, second sign → second *, and so on.\n2. BODMAS.\n3. Check against the right side.\n\nWhy: 'sequentially' fixes the order of placement.",
      "`21 * 7 * 5 * 4 * 3 = 27` with ÷, ×, +, ×.", "21 ÷ 7 × 5 + 4 × 3 = 15 + 12 = **27** ✓."),
    P("mo-p18", "Replace * signs when '=' is one of the options", "common",
      "`12 * 4 * 3 * 16` — there is no = sign yet; options contain '='.",
      "1. Place the signs in order, including '='.\n2. Evaluate the left part and the right part separately.\n3. They must be equal.\n\nWhy: '=' splits the line into two expressions.",
      "`12 * 4 * 3 * 16` with ×, ÷, =.", "12 × 4 ÷ 3 = 16 → 16 = 16 ✓."),
]
PATS["defined-operations"] = [
    P("mo-p19", "Defined formula: a ★ b = given expression", "common",
      "The question defines a new symbol with a formula in a and b.",
      "1. Write a = first number, b = second number.\n2. Put them into the formula.\n3. Calculate.\n\nWhy: the symbol is only a short name for the formula.",
      "If a ★ b = 2a + 3b, find **5 ★ 4**.", "2 × 5 + 3 × 4 = 10 + 12 = **22**.", formula=r"a \star b = 2a + 3b"),
    P("mo-p20", "Hidden rule from solved examples", "common",
      "Examples like 5 # 3 = 34, 6 # 2 = 40, then '7 # 4 = ?'.",
      "1. Try common rules: a+b, ab, $a^2 \\pm b^2$, $(a \\pm b)^2$, ab+a+b.\n2. Keep the rule that fits EVERY example.\n3. Apply it.\n\nWhy: two examples are given so that only one rule survives.",
      "5 # 3 = 34, 6 # 2 = 40. Find **7 # 4**.", "25 + 9 = 34 ✓, 36 + 4 = 40 ✓: rule $a^2 + b^2$. 49 + 16 = **65**.",
      formula=r"a \# b = a^2 + b^2"),
    P("mo-p21", "Conditional definition", "occasional",
      "The symbol does different things depending on a condition (a > b, both even, etc.).",
      "1. Check the condition for the given pair.\n2. Use the matching formula.\n3. Re-check the condition at every new step.\n\nWhy: the second step often falls in the other case.",
      "a ▲ b = a − b if a > b, a + b if a ≤ b. Find **(9 ▲ 4) ▲ 7**.", "9 ▲ 4 = 5; 5 ▲ 7 = 5 + 7 = **12**."),
    P("mo-p22", "Nested or two-symbol defined operations", "common",
      "Brackets combine defined operations: (7 @ 5) @ 3, or two symbols in one line.",
      "1. Solve the inner bracket with its own formula.\n2. Use that result as an input to the outer operation.\n\nWhy: brackets decide the order, as in BODMAS.",
      "a ⊗ b = 3a − b. Find **(4 ⊗ 2) ⊗ 5**.", "4 ⊗ 2 = 12 − 2 = 10; 10 ⊗ 5 = 30 − 5 = **25**.", formula=r"a \otimes b = 3a - b"),
]

# ---------------- new subtopic ----------------
add_sub(d, {
    "id": "defined-operations",
    "title": "Hidden-rule and defined operations",
    "concept": "A new symbol such as ★, # or @ is given its own meaning — either as a formula (a ★ b = 2a + 3b) or through solved examples (5 # 3 = 34) from which you find the rule. Plug the numbers in carefully, keep the order of a and b, and test a hidden rule on every example before using it.",
    "formulas": [
        {"name": "Sum of squares", "tex": r"a \# b = a^2 + b^2", "note": "Very common hidden rule: 5 # 3 = 34."},
        {"name": "Difference of squares", "tex": r"a @ b = a^2 - b^2 = (a+b)(a-b)", "note": "8 @ 2 = 60."},
        {"name": "Product plus sum", "tex": r"a \$ b = ab + a + b", "note": "4 $ 3 = 19."},
    ],
    "tricks": [
        {"title": "Rule ladder for hidden operations",
         "body": "Test in this order: a + b, a × b, $a^2 + b^2$, $a^2 - b^2$, $(a+b)^2$, $(a-b)^2$, ab + a + b. Stop at the first rule that fits **all** the examples.",
         "example": {"q": "8 @ 2 = 60 and 7 @ 3 = 40. Find 9 @ 4.",
                     "solution": "64 − 4 = 60 ✓ and 49 − 9 = 40 ✓, so the rule is $a^2 - b^2$: 81 − 16 = **65**."}},
    ],
    "mistakes": [
        "Swapping a and b in a formula that is not symmetric (2a + 3b ≠ 3a + 2b).",
        "Accepting a rule after checking only one example.",
        "Using the first case of a conditional definition again without re-checking the condition.",
    ],
}, after="balance-equation")

for sid in NOTES:
    set_sub(d, sid, notes=NOTES[sid].strip(), patterns=PATS[sid])

# ---------------- practice ----------------
QS = []


def val_q(qid, sub, pat, expr_shown, expr_eval, wrong, sol, sc, diff, t=40, prefix="Find the value of"):
    v = fmt(ev(expr_eval))
    QS.append(Q(qid, f"{prefix} **{expr_shown}**.", v, wrong, sol, sc, diff, sub, pat, t, check=fmt(ev(expr_eval))))


# ---- mathops-idea ----
S = "mathops-idea"
val_q(f"{S}-p01", S, "mo-p1", "18 + 24 ÷ 6 × 3 − 5", "18 + 24 ÷ 6 × 3 − 5",
      [fmt(ltr("18 + 24 ÷ 6 × 3 − 5")), "23", "30"],
      "Do ÷ and × first, left to right: 24 ÷ 6 = 4, 4 × 3 = 12. Now 18 + 12 − 5 = **25**.",
      "Left to right gives 16 — that is the trap option.", "easy", 30)
val_q(f"{S}-p02", S, "mo-p1", "45 − 5 × 6 + 36 ÷ 4", "45 − 5 × 6 + 36 ÷ 4",
      [fmt(ltr("45 − 5 × 6 + 36 ÷ 4")), "6", "33"],
      "5 × 6 = 30 and 36 ÷ 4 = 9. Then 45 − 30 + 9 = **24**. (Reading it as 45 − (30 + 9) = 6 is a sign slip.)",
      "Circle × and ÷ first; the rest is left to right.", "easy", 35)
val_q(f"{S}-p03", S, "mo-p1", "7 × 8 − 72 ÷ 9 + 3 × 5", "7 × 8 − 72 ÷ 9 + 3 × 5",
      ["33", "48", "71"],
      "7 × 8 = 56, 72 ÷ 9 = 8, 3 × 5 = 15. Then 56 − 8 + 15 = **63**. (56 − (8 + 15) = 33 is the sign-slip trap; 48 forgets the + 15.)",
      "Three products first, then one left-to-right pass.", "medium", 40)
assert ev("45 − 5 × 6 + 36 ÷ 4") == 24 and ev("7 × 8 − 72 ÷ 9 + 3 × 5") == 63
val_q(f"{S}-p04", S, "mo-p2", "96 ÷ 8 × 4", "96 ÷ 8 × 4", ["3", "12", "36"],
      "÷ and × have the same rank, so go left to right: 96 ÷ 8 = 12, then 12 × 4 = **48**. Doing 8 × 4 first gives 96 ÷ 32 = 3 — wrong.",
      "Same rank → left to right.", "easy", 25)
val_q(f"{S}-p05", S, "mo-p2", "60 − 12 + 8 − 6", "60 − 12 + 8 − 6", ["34", "46", "38"],
      "+ and − have the same rank: 60 − 12 = 48, 48 + 8 = 56, 56 − 6 = **50**. Adding 12 + 8 first (60 − 20 − 6 = 34) is the trap.",
      "Same rank → left to right.", "easy", 25)
val_q(f"{S}-p06", S, "mo-p2", "144 ÷ 12 ÷ 2 × 6 + 4", "144 ÷ 12 ÷ 2 × 6 + 4",
      [fmt(ev("144 ÷ (12 ÷ 2) × 6 + 4")), "5", "76"],
      "Left to right for ÷ and ×: 144 ÷ 12 = 12, 12 ÷ 2 = 6, 6 × 6 = 36. Then 36 + 4 = **40**. (Working 12 ÷ 2 first gives 148; working 2 × 6 first gives 5.)",
      "Never jump to a later ÷ or ×; walk left to right.", "medium", 40)
assert ev("144 ÷ 12 ÷ (2 × 6) + 4") == 5
val_q(f"{S}-p07", S, "mo-p3", "(36 − 4 × 5) ÷ 4 + 3 × (8 − 2)", "(36 − 4 × 5) ÷ 4 + 3 × (8 − 2)",
      ["58", "40", "7"],
      "Bracket 1: 36 − 20 = 16 (× inside the bracket first). Bracket 2: 8 − 2 = 6. Then 16 ÷ 4 + 3 × 6 = 4 + 18 = **22**. (Doing 36 − 4 first inside the bracket gives 160 ÷ 4 + 18 = 58.)",
      "BODMAS works inside each bracket too.", "medium", 45)
assert ev("(36 − 4) × 5 ÷ 4 + 3 × (8 − 2)") == 58
val_q(f"{S}-p08", S, "mo-p3", "[48 ÷ {2 × (10 − 4)}] + 5", "[48 ÷ {2 × (10 − 4)}] + 5",
      ["149", "29", "13"],
      "Innermost first: 10 − 4 = 6. Curly bracket: 2 × 6 = 12. Square bracket: 48 ÷ 12 = 4. Finally 4 + 5 = **9**. (Ignoring the brackets gives 48 ÷ 2 × 6 + 5 = 149.)",
      "( ) → { } → [ ].", "medium", 40)
assert ev("48 ÷ 2 × 6 + 5") == 149
val_q(f"{S}-p09", S, "mo-p3", "100 − [20 + {30 − (12 − 4) × 2}]", "100 − [20 + {30 − (12 − 4) × 2}]",
      ["36", "54", "62"],
      "12 − 4 = 8. Inside { }: 30 − 8 × 2 = 30 − 16 = 14. Inside [ ]: 20 + 14 = 34. Finally 100 − 34 = **66**. (Doing (30 − 8) × 2 = 44 inside { } gives 100 − 64 = 36 — a BODMAS slip.)",
      "Inside the curly bracket, × still comes before −.", "hard", 50)
assert ev("100 − [20 + {(30 − (12 − 4)) × 2}]") == 36


def miss_q(qid, pat, shown, fn, ans, wrong, sol, sc, diff, t=40):
    assert fn(F(ans)), qid
    for w in wrong:
        assert not fn(F(w)), (qid, w)
    QS.append(Q(qid, f"Find the missing number: **{shown}**", ans, wrong, sol, sc, diff, S, pat, t))


miss_q(f"{S}-p10", "mo-p4", "18 + 6 × ? − 4 = 38", lambda x: 18 + 6 * x - 4 == 38, "4", ["6", "3", "5"],
       "Move the loose numbers: 6 × ? = 38 + 4 − 18 = 24. So ? = 24 ÷ 6 = **4**. Check: 18 + 24 − 4 = 38 ✓.",
       "Put each option back in: only 4 balances.", "easy", 35)
miss_q(f"{S}-p11", "mo-p4", "? ÷ 4 + 7 × 3 = 36", lambda x: x / 4 + 21 == 36, "60", ["15", "48", "64"],
       "7 × 3 = 21, so ? ÷ 4 = 36 − 21 = 15. Then ? = 15 × 4 = **60**. (15 is the trap of forgetting to multiply back by 4.)",
       "Undo the steps in reverse order.", "medium", 40)
miss_q(f"{S}-p12", "mo-p4", "56 ÷ ? × 3 − 10 = 11", lambda x: 56 / x * 3 - 10 == 11, "8", ["7", "6", "9"],
       "56 ÷ ? × 3 = 11 + 10 = 21, so 56 ÷ ? = 21 ÷ 3 = 7. Then ? = 56 ÷ 7 = **8**. Check: 56 ÷ 8 = 7, 7 × 3 = 21, 21 − 10 = 11 ✓. (7 is the value of 56 ÷ ?, not of ?.)",
       "Try options: 56 ÷ 8 × 3 = 21 → 21 − 10 = 11.", "medium", 45)

# ---- sign-substitution ----
S = "sign-substitution"


def sub_q(qid, pat, cond, expr, m, wrong, sol, sc, diff, t=45):
    new = mp(expr, m)
    v = fmt(ev(new))
    QS.append(Q(qid, f"{cond}, then what is the value of **{expr}**?", v, wrong, sol.replace("NEW", new), sc,
                diff, S, pat, t, check=fmt(ev(new))))
    return new


m = {"+": "−", "−": "×", "×": "÷", "÷": "+"}
n = sub_q(f"{S}-p01", "mo-p5", "If **+ means −**, **− means ×**, **× means ÷** and **÷ means +**", "48 × 6 + 3 − 2 ÷ 9", m,
          [fmt(ltr("48 ÷ 6 − 3 × 2 + 9")), "15", "23"],
          "Rewrite: **NEW**. BODMAS: 48 ÷ 6 = 8 and 3 × 2 = 6. Then 8 − 6 + 9 = **11**. (Left to right on the new line gives 19.)",
          "Rewrite first; compute ÷ and × before − and +.", "medium")
assert n == "48 ÷ 6 − 3 × 2 + 9" and ltr(n) == 19
m = {"×": "+", "+": "÷", "÷": "−", "−": "×"}
n = sub_q(f"{S}-p02", "mo-p5", "If **× means +**, **+ means ÷**, **÷ means −** and **− means ×**", "27 + 9 × 6 − 4 ÷ 10", m,
          [fmt(ltr("27 ÷ 9 + 6 × 4 − 10")), "13", "37"],
          "Rewrite: **NEW**. 27 ÷ 9 = 3 and 6 × 4 = 24. Then 3 + 24 − 10 = **17**. (Going left to right gives 26.)",
          "Mapping table → rewrite → BODMAS.", "easy", 40)
assert n == "27 ÷ 9 + 6 × 4 − 10" and ltr(n) == 26
m = {"÷": "×", "×": "−", "−": "+", "+": "÷"}
n = sub_q(f"{S}-p03", "mo-p5", "If **÷ means ×**, **× means −**, **− means +** and **+ means ÷**", "84 + 12 ÷ 5 × 18 − 9", m,
          ["8", "44", "21"],
          "Rewrite: **NEW**. 84 ÷ 12 = 7, 7 × 5 = 35. Then 35 − 18 + 9 = **26**. (Taking 35 − (18 + 9) = 8 is the sign-slip trap.)",
          "After ÷ and ×, go left to right for − and +.", "medium")
assert n == "84 ÷ 12 × 5 − 18 + 9"
m = {"+": "×", "×": "+"}
n = sub_q(f"{S}-p04", "mo-p6", "If **+ means ×** and **× means +**", "9 + 4 × 7", m,
          [fmt(ev("9 + 4 × 7")), "99", "63"],
          "Only + and × change. Rewrite: **NEW** = 36 + 7 = **43**. (37 is the value of the original expression — mapping ignored.)",
          "Change only the listed signs.", "easy", 30)
m = {"÷": "−", "−": "÷"}
n = sub_q(f"{S}-p05", "mo-p6", "If **÷ means −** and **− means ÷**", "50 ÷ 30 − 5 + 8", m,
          [fmt(ltr("50 − 30 ÷ 5 + 8")), "36", "44"],
          "Rewrite: **NEW**. 30 ÷ 5 = 6. Then 50 − 6 + 8 = **52**. (Left to right gives 12; 50 − (6 + 8) = 36 is a sign slip.)",
          "+ is not in the list, so it stays +.", "easy", 35)
assert ltr("50 − 30 ÷ 5 + 8") == 12
m = {"+": "×", "−": "÷", "×": "−", "÷": "+"}
n = sub_q(f"{S}-p06", "mo-p7", "If **+ means ×**, **− means ÷**, **× means −** and **÷ means +**", "(18 − 3) + 4 × (5 ÷ 7)", m,
          ["24", "36", "6"],
          "Convert the signs inside the brackets too. Rewrite: **NEW**. Brackets: 18 ÷ 3 = 6 and 5 + 7 = 12. Then 6 × 4 − 12 = 24 − 12 = **12**.",
          "Brackets first, but their signs are coded as well.", "medium", 45)
assert n == "(18 ÷ 3) × 4 − (5 + 7)"
m = {"×": "÷", "÷": "+", "+": "−", "−": "×"}
n = sub_q(f"{S}-p07", "mo-p7", "If **× means ÷**, **÷ means +**, **+ means −** and **− means ×**", "[(60 × 4) + 5] − 2 ÷ 7", m,
          ["90", "17", "37"],
          "Rewrite: **NEW**. Inner bracket: 60 ÷ 4 = 15. Square bracket: 15 − 5 = 10. Then 10 × 2 + 7 = 20 + 7 = **27**. (10 × (2 + 7) = 90 is the trap of adding before multiplying.)",
          "Solve the brackets fully, then × before +.", "hard", 55)
assert n == "[(60 ÷ 4) − 5] × 2 + 7"


def letter_q(qid, pat, cond, shown, codes, wrong, sol, sc, diff, t=40):
    real = "".join(codes.get(c, c) for c in shown)
    v = fmt(ev(real))
    QS.append(Q(qid, f"{cond}, then what is the value of **{shown}**?", v, wrong, sol.replace("NEW", real), sc,
                diff, S, pat, t, check=fmt(ev(real))))
    return real


r = letter_q(f"{S}-p08", "mo-p8", "If **A** means '+', **B** means '−', **C** means '×' and **D** means '÷'", "18 C 4 D 6 A 9 B 5",
             {"A": "+", "B": "−", "C": "×", "D": "÷"}, ["22", "10", "14"],
             "Replace the letters: **NEW**. 18 × 4 = 72, 72 ÷ 6 = 12. Then 12 + 9 − 5 = **16**.",
             "Letters are just signs in disguise.", "easy", 35)
r = letter_q(f"{S}-p09", "mo-p8", "If **P** denotes '÷', **Q** denotes '×', **R** denotes '+' and **S** denotes '−'", "64 P 8 R 7 Q 6 S 11",
             {"P": "÷", "Q": "×", "R": "+", "S": "−"}, [fmt(ltr("64 ÷ 8 + 7 × 6 − 11")), "45", "33"],
             "Replace the letters: **NEW**. 64 ÷ 8 = 8 and 7 × 6 = 42. Then 8 + 42 − 11 = **39**. (Left to right gives 79.)",
             "Rewrite, then BODMAS.", "medium", 40)
assert ltr("64 ÷ 8 + 7 × 6 − 11") == 79


def pick_sub_q(qid, pat, cond, m, ans, wrong, diff, t=60):
    cands = [ans] + wrong
    rows = []
    for e in cands:
        lhs, rhs = e.split(" = ")
        new = mp(lhs, m)
        rows.append((e, new, ev(new), F(rhs)))
    only_one(cands, lambda e: eq_true(mp(e.split(" = ")[0], m) + " = " + e.split(" = ")[1]), ans)
    lines = "\n".join(f"- {e}: {new} = {fmt(v)}{' ✓' if v == rv else f', not {fmt(rv)} ✗'}" for e, new, v, rv in rows)
    sol = f"Convert only the left side of each option, then evaluate:\n\n{lines}\n\nOnly **{ans}** balances after substitution."
    QS.append(Q(qid, f"{cond}, which of the following equations is **correct**?", ans, wrong, sol,
                "Rewrite each left side on its own line; the right sides never change.", diff, S, pat, t))


pick_sub_q(f"{S}-p10", "mo-p9", "If **+ means ×**, **× means −**, **− means ÷** and **÷ means +**",
           {"+": "×", "×": "−", "−": "÷", "÷": "+"},
           "8 + 3 ÷ 12 − 4 × 5 = 22", ["6 + 4 × 10 − 5 ÷ 3 = 17", "9 − 3 + 4 × 2 ÷ 6 = 14", "20 − 5 ÷ 6 + 2 × 4 = 14"], "hard", 70)
pick_sub_q(f"{S}-p11", "mo-p9", "If **× means +**, **+ means −**, **− means ÷** and **÷ means ×**",
           {"×": "+", "+": "−", "−": "÷", "÷": "×"},
           "15 × 3 ÷ 4 + 6 = 21", ["12 − 4 × 5 + 2 = 18", "7 ÷ 2 × 9 − 3 = 20", "36 − 6 + 2 ÷ 5 = 30"], "medium", 60)

# ---- interchange-signs ----
S = "interchange-signs"


def isw_q(qid, pat, cond, expr, new, wrong, sol, sc, diff, t=40):
    v = fmt(ev(new))
    QS.append(Q(qid, f"{cond}, what is the value of **{expr}**?", v, wrong, sol.replace("NEW", new), sc, diff, S, pat, t,
                check=fmt(ev(new))))


e = "63 + 9 ÷ 14 − 3 × 2"
new = sign_swap(e, "+", "÷")
assert new == "63 ÷ 9 + 14 − 3 × 2"
isw_q(f"{S}-p01", "mo-p10", "If the signs **+ and ÷ are interchanged**", e, new, [fmt(ltr(new)), "21", "9"],
      "After the swap: **NEW**. 63 ÷ 9 = 7 and 3 × 2 = 6. Then 7 + 14 − 6 = **15**. (Left to right gives 36.)",
      "Swap both signs everywhere, then BODMAS.", "easy", 35)
e = "12 − 4 × 3 + 20 ÷ 5"
new = sign_swap(e, "−", "×")
assert new == "12 × 4 − 3 + 20 ÷ 5"
isw_q(f"{S}-p02", "mo-p10", "If the signs **− and × are interchanged**", e, new, [fmt(ev(e)), fmt(ltr(new)), "41"],
      "After the swap: **NEW**. 12 × 4 = 48 and 20 ÷ 5 = 4. Then 48 − 3 + 4 = **49**. (4 is the unswapped value; 13 is the left-to-right value.)",
      "Interchange is two-way: − becomes × and × becomes −.", "easy", 35)
e = "18 × 3 − 6 ÷ 2 + 5"
new = sign_swap(sign_swap(e, "×", "÷"), "+", "−")
assert new == "18 ÷ 3 + 6 × 2 − 5"
isw_q(f"{S}-p03", "mo-p10", "If **× and ÷ are interchanged** and **+ and − are interchanged**", e, new,
      [fmt(ev(e)), fmt(ltr(new)), "23"],
      "Both swaps in one rewrite: **NEW**. 18 ÷ 3 = 6 and 6 × 2 = 12. Then 6 + 12 − 5 = **13**. (56 is the unswapped value; 19 is left to right.)",
      "Two swaps, one rewrite.", "medium", 45)
e = "8 + 4 × 6 − 12 ÷ 3"
new = swapn(sign_swap(e, "+", "×"), 6, 3)
assert new == "8 × 4 + 3 − 12 ÷ 6"
isw_q(f"{S}-p04", "mo-p11", "If the signs **+ and ×** are interchanged and the numbers **3 and 6** are interchanged", e, new,
      [fmt(ev(sign_swap(e, "+", "×"))), fmt(ev(swapn(e, 6, 3))), fmt(ev(e))],
      "Apply both swaps: **NEW**. 8 × 4 = 32 and 12 ÷ 6 = 2. Then 32 + 3 − 2 = **33**. (34 swaps only the signs, 18 swaps only the numbers, 28 swaps nothing.)",
      "Do the sign swap and the number swap together in one rewrite.", "medium", 50)
e = "40 − 8 ÷ 2 × 3 + 6"
new = swapn(sign_swap(e, "÷", "−"), 8, 2)
assert new == "40 ÷ 2 − 8 × 3 + 6"
isw_q(f"{S}-p05", "mo-p11", "If the signs **÷ and −** are interchanged and the numbers **2 and 8** are interchanged", e, new,
      [fmt(ev(e)), fmt(ev(sign_swap(e, "÷", "−"))), fmt(ltr(new))],
      "Apply both swaps: **NEW**. 40 ÷ 2 = 20 and 8 × 3 = 24. Then 20 − 24 + 6 = **2**. (34 is the unswapped value, 5 swaps only the signs, 42 is left to right.)",
      "One rewrite; then × and ÷ before − and +.", "hard", 55)


def nsw_q(qid, lhs, rhs, ans, wrong, diff, t=60):
    pairs = all_num_pairs(lhs)
    good = [p for p in pairs if num_swap_ok(lhs, rhs, p)]
    assert len(good) == 1, (qid, good)
    a, b = good[0]
    assert ans == f"{a} and {b}", (qid, ans)
    cands = [ans] + wrong
    only_one(cands, lambda c: num_swap_ok(lhs, rhs, tuple(c.split(" and "))), ans)
    lines = "\n".join(f"- {c}: {swapn(lhs, *c.split(' and '))} = {fmt(ev(swapn(lhs, *c.split(' and '))))}"
                      f"{' ✓' if num_swap_ok(lhs, rhs, tuple(c.split(' and '))) else ' ✗'}" for c in cands)
    sol = f"Right now the left side is {fmt(ev(lhs))}, not {rhs}. Try each option pair:\n\n{lines}\n\nOnly interchanging **{ans}** balances the equation."
    QS.append(Q(qid, f"Which two numbers should be interchanged to make the following equation correct?\n\n**{lhs} = {rhs}**",
                ans, wrong, sol, "Sweep the option pairs in order; skip pairs that only swap the two sides of one ×.",
                diff, S, "mo-p12", t))


nsw_q(f"{S}-p06", "6 × 4 + 8 ÷ 2 − 5", 9, "4 and 2", ["6 and 8", "4 and 8", "6 and 5"], "medium")
nsw_q(f"{S}-p07", "15 ÷ 5 × 3 + 7 − 2", 22, "3 and 7", ["5 and 3", "3 and 2", "7 and 2"], "hard", 70)


def ssw_q(qid, lhs, rhs, ans, wrong, diff, t=60):
    allpairs = list(combinations(SIGNS, 2))
    good = [p for p in allpairs if ev(sign_swap(lhs, *p)) == F(rhs)]
    assert len(good) == 1, (qid, good)
    cands = [ans] + wrong
    only_one(cands, lambda c: ev(sign_swap(lhs, *c.split(" and "))) == F(rhs), ans)
    lines = "\n".join(f"- {c}: {sign_swap(lhs, *c.split(' and '))} = {fmt(ev(sign_swap(lhs, *c.split(' and '))))}"
                      f"{' ✓' if ev(sign_swap(lhs, *c.split(' and '))) == F(rhs) else ' ✗'}" for c in cands)
    sol = f"Right now the left side is {fmt(ev(lhs))}, not {rhs}. Swap each option's signs everywhere and evaluate:\n\n{lines}\n\nOnly interchanging **{ans}** makes it correct."
    QS.append(Q(qid, f"Which two signs should be interchanged to make the following equation correct?\n\n**{lhs} = {rhs}**",
                ans, wrong, sol, "Use the target's size: a small target needs a new ÷ or −, a large one a new ×.",
                diff, S, "mo-p13", t))


ssw_q(f"{S}-p08", "12 + 6 ÷ 3 − 2 × 4", 18, "+ and −", ["+ and ×", "− and ×", "+ and ÷"], "medium")
ssw_q(f"{S}-p09", "20 − 4 × 3 + 8 ÷ 2", 21, "− and ÷", ["× and +", "− and +", "× and −"], "hard", 70)


def after_swap_q(qid, a, b, ans, wrong, diff, t=60):
    cands = [ans] + wrong

    def ok(eq):
        lhs, rhs = eq.split(" = ")
        return ev(sign_swap(lhs, a, b)) == F(rhs)
    only_one(cands, ok, ans)
    lines = "\n".join(f"- {c}: {sign_swap(c.split(' = ')[0], a, b)} = {fmt(ev(sign_swap(c.split(' = ')[0], a, b)))}"
                      f"{' ✓' if ok(c) else ' ✗'}" for c in cands)
    sol = f"Swap {a} and {b} on each left side, then evaluate:\n\n{lines}\n\nOnly **{ans}** becomes correct."
    QS.append(Q(qid, f"If the signs **{a} and {b} are interchanged**, which of the following equations becomes **correct**?",
                ans, wrong, sol, "Apply the swap to the left side only; the right side is a plain number.", diff, S, "mo-p14", t))


after_swap_q(f"{S}-p10", "×", "+", "7 + 4 × 2 ÷ 2 = 29", ["5 × 6 + 2 − 4 = 30", "8 + 3 × 4 − 6 = 26", "9 × 2 + 5 − 3 = 18"], "medium")
after_swap_q(f"{S}-p11", "−", "÷", "36 − 4 + 5 ÷ 2 = 12", ["24 − 6 ÷ 2 + 3 = 7", "18 − 3 ÷ 4 × 2 = 10", "40 ÷ 8 − 2 + 6 = 30"], "medium")

# ---- balance-equation ----
S = "balance-equation"


def pick_eq_q(qid, ans, wrong, diff, t=50):
    cands = [ans] + wrong
    only_one(cands, eq_true, ans)
    lines = "\n".join(f"- {c.split(' = ')[0]} = {fmt(ev(c.split(' = ')[0]))}"
                      f"{' ✓' if eq_true(c) else f', not {c.split(' = ')[1]} ✗'}" for c in cands)
    sol = f"Evaluate each left side with BODMAS:\n\n{lines}\n\nOnly **{ans}** is correct."
    QS.append(Q(qid, "Which of the following equations is **correct**?", ans, wrong, sol,
                "Wrong right-hand sides are usually left-to-right values — BODMAS exposes them.", diff, S, "mo-p15", t))


pick_eq_q(f"{S}-p01", "16 ÷ 4 × 2 + 6 = 14", ["9 × 3 − 12 ÷ 4 = 21", "25 − 15 ÷ 5 + 2 = 4", "7 + 8 × 2 − 5 = 25"], "easy", 45)
assert ltr("25 − 15 ÷ 5 + 2") == 4 and ltr("7 + 8 × 2 − 5") == 25
pick_eq_q(f"{S}-p02", "13 + 7 × 2 − 18 ÷ 3 = 21", ["48 ÷ 6 + 4 × 3 − 5 = 31", "60 − 5 × 8 + 12 ÷ 4 = 26", "11 × 4 − 20 ÷ 5 + 2 = 44"], "medium", 55)
assert ltr("48 ÷ 6 + 4 × 3 − 5") == 31


def set_q(qid, pat, template, rhs, ans, wrong, diff, t=60, star=False):
    cands = [ans] + wrong
    ok = lambda c: ev(fill(template, c.split(", "))) == F(rhs)
    only_one(cands, ok, ans)
    lines = "\n".join(f"- {c}: {fill(template, c.split(', '))} = {fmt(ev(fill(template, c.split(', '))))}"
                      f"{' ✓' if ok(c) else ' ✗'}" for c in cands)
    shown = template if star else template.replace("*", "?")
    if star:
        q = (f"Select the correct combination of mathematical signs to sequentially replace the * signs and balance the equation.\n\n"
             f"`{shown} = {rhs}`")
    elif len(ans.split(", ")) == 2:
        q = f"Which pair of signs will make **{shown} = {rhs}** correct?"
    else:
        q = f"Which set of signs will make **{shown} = {rhs}** correct?"
    sol = f"Put each option's signs into the blanks from left to right, then use BODMAS:\n\n{lines}\n\nOnly **{ans}** balances."
    QS.append(Q(qid, q, ans, wrong, sol, "Check the target size first: a big right side needs ×; a small one needs ÷ or −.",
                diff, S, pat, t))


set_q(f"{S}-p03", "mo-p16", "14 * 2 * 3", 21, "÷, ×", ["×, −", "+, ×", "−, +"], "easy", 35)
set_q(f"{S}-p04", "mo-p16", "18 * 6 * 3 * 4", 24, "−, +, ×", ["+, ÷, ×", "÷, ×, +", "×, ÷, −"], "medium", 50)
set_q(f"{S}-p05", "mo-p16", "72 * 8 * 3 * 5 * 2", 37, "÷, ×, +, ×", ["÷, +, ×, −", "÷, ×, −, +", "×, ÷, +, −"], "hard", 70)
set_q(f"{S}-p06", "mo-p17", "21 * 7 * 5 * 4 * 3", 27, "÷, ×, +, ×", ["÷, ×, −, ×", "÷, +, ×, −", "×, ÷, −, +"], "medium", 60, star=True)
set_q(f"{S}-p07", "mo-p17", "13 * 4 * 6 * 3 * 2", 19, "+, ×, ÷, −", ["×, +, ÷, −", "−, ×, ÷, +", "+, ×, −, ÷"], "medium", 60, star=True)


def eqsign_q(qid, template, ans, wrong, diff, t=60):
    cands = [ans] + wrong
    ok = lambda c: eq_true(fill(template, c.split(", ")))
    only_one(cands, ok, ans)

    def show(c):
        f_ = fill(template, c.split(", "))
        l_, r_ = f_.split("=")
        return f"- {c}: {f_.strip()} → {fmt(ev(l_))} vs {fmt(ev(r_))}{' ✓' if ok(c) else ' ✗'}"
    lines = "\n".join(show(c) for c in cands)
    q = (f"Select the correct combination of mathematical signs to replace the * signs and balance the given equation.\n\n"
         f"`{template}`")
    sol = f"Fill the signs in order, then compare the two sides of '=':\n\n{lines}\n\nOnly **{ans}** balances."
    QS.append(Q(qid, q, ans, wrong, sol, "'=' splits the line: evaluate the left part and the right part separately.",
                diff, S, "mo-p18", t))


eqsign_q(f"{S}-p08", "12 * 4 * 3 * 16", "×, ÷, =", ["÷, ×, =", "+, =, ÷", "=, +, ×"], "medium", 45)
eqsign_q(f"{S}-p09", "18 * 3 * 4 * 2 * 14", "÷, +, ×, =", ["÷, ×, −, =", "×, −, ÷, =", "÷, +, =, ×"], "hard", 70)

# ---- defined-operations ----
S = "defined-operations"


def dq(qid, pat, q, ans, wrong, sol, sc, diff, t=45, check=None):
    QS.append(Q(qid, q, ans, wrong, sol, sc, diff, S, pat, t, check=check))


star = lambda a, b: 2 * a + 3 * b
dq(f"{S}-p01", "mo-p19", "If **a ★ b = 2a + 3b**, find the value of **5 ★ 4**.", "22",
   [str(3 * 5 + 2 * 4), "20", "26"],
   "Here a = 5 and b = 4. So 5 ★ 4 = 2 × 5 + 3 × 4 = 10 + 12 = **22**. (23 comes from swapping a and b.)",
   "First number is a, second is b — never swap.", "easy", 30, check=star(5, 4))
hsh = lambda a, b: a * a - a * b + b * b
dq(f"{S}-p02", "mo-p19", "If **a # b = a² − ab + b²**, find **6 # 3**.", "27",
   [str(36 + 18 + 9), "9", "36"],
   "a = 6, b = 3: 6² − 6 × 3 + 3² = 36 − 18 + 9 = **27**. (63 uses + ab by mistake.)",
   "Write the three terms separately: 36, 18, 9.", "easy", 35, check=hsh(6, 3))
at = lambda a, b: F(a + b, a - b)
dq(f"{S}-p03", "mo-p22", "If **a @ b = (a + b) ÷ (a − b)**, find **(7 @ 5) @ 3**.", "3",
   ["6", "9", "2"],
   "Inner bracket first: 7 @ 5 = 12 ÷ 2 = 6. Then 6 @ 3 = (6 + 3) ÷ (6 − 3) = 9 ÷ 3 = **3**.",
   "Solve the bracket, then use its value as the new a.", "medium", 45, check=fmt(at(at(7, 5), 3)))
rule = lambda a, b: a * a + b * b
assert rule(5, 3) == 34 and rule(6, 2) == 40
assert not (5 * 5 - 9 == 34)
dq(f"{S}-p04", "mo-p20", "If **5 # 3 = 34** and **6 # 2 = 40**, then **7 # 4 = ?**", "65",
   [str(49 + 8), str(49 - 16), "45"],
   "Test the rule $a^2 + b^2$: 25 + 9 = 34 ✓ and 36 + 4 = 40 ✓. So 7 # 4 = 49 + 16 = **65**.",
   "Try $a^2 + b^2$ early — it is the most common hidden rule.", "medium", 45, check=rule(7, 4))
rule = lambda a, b: a * a - b * b
assert rule(8, 2) == 60 and rule(7, 3) == 40
dq(f"{S}-p05", "mo-p20", "If **8 @ 2 = 60** and **7 @ 3 = 40**, then **9 @ 4 = ?**", "65",
   [str(81 + 16), "72", "13"],
   "Test $a^2 - b^2$: 64 − 4 = 60 ✓ and 49 − 9 = 40 ✓. So 9 @ 4 = 81 − 16 = **65**. (97 uses $a^2 + b^2$, which fails the examples.)",
   "Difference of squares = (a + b)(a − b): 13 × 5 = 65.", "medium", 45, check=rule(9, 4))
rule = lambda a, b: a * b + a + b
assert rule(4, 3) == 19 and rule(5, 2) == 17
assert (4 * 4 + 3 == 19) and not (5 * 5 + 2 == 17)  # a²+b fits the first example only
dq(f"{S}-p06", "mo-p20", "If **4 $ 3 = 19** and **5 $ 2 = 17**, then **7 $ 2 = ?**", "23",
   [str(49 + 2), str(14 + 2), str(14 + 7)],
   "Try $a^2 + b$: 16 + 3 = 19 ✓ but 25 + 2 = 27 ✗ — rejected. Try ab + a + b: 12 + 4 + 3 = 19 ✓ and 10 + 5 + 2 = 17 ✓. So 7 $ 2 = 14 + 7 + 2 = **23**.",
   "A rule must fit EVERY example; the second example kills $a^2 + b$.", "hard", 60, check=rule(7, 2))
rule = lambda a, b: (a + b) ** 2
assert rule(3, 4) == 49 and rule(5, 2) == 49
dq(f"{S}-p07", "mo-p20", "If **3 ⊕ 4 = 49** and **5 ⊕ 2 = 49**, then **6 ⊕ 3 = ?**", "81",
   [str(36 + 9), str(36 - 9), "18"],
   "Both examples give 49 although the numbers differ — but both pairs add up to 7, and 7² = 49. Rule: $(a+b)^2$. So 6 ⊕ 3 = 9² = **81**.",
   "Same answer for different pairs → look at the sum or product of the pair.", "medium", 45, check=rule(6, 3))
tri = lambda a, b: a - b if a > b else a + b
dq(f"{S}-p08", "mo-p21", "If **a ▲ b = a − b** when a > b and **a ▲ b = a + b** when a ≤ b, find **(9 ▲ 4) ▲ 7**.", "12",
   ["−2", str(tri(9, tri(4, 7))), "18"],
   "9 ▲ 4: 9 > 4, so 9 − 4 = 5. Then 5 ▲ 7: 5 ≤ 7, so 5 + 7 = **12**. (−2 re-uses the first case without checking.)",
   "Check the condition again at every step.", "medium", 45, check=tri(tri(9, 4), 7))
dot = lambda a, b: a * b if a % 2 == 0 and b % 2 == 0 else a + b
dq(f"{S}-p09", "mo-p21", "If **a ● b = a × b** when both a and b are even, and **a ● b = a + b** otherwise, find **(4 ● 6) + (3 ● 8)**.", "35",
   ["48", "21", "34"],
   "4 ● 6: both even → 4 × 6 = 24. 3 ● 8: 3 is odd → 3 + 8 = 11. Total = 24 + 11 = **35**. (48 multiplies both pairs.)",
   "Test the condition for each pair separately.", "easy", 40, check=dot(4, 6) + dot(3, 8))
assert dot(4, 6) + 3 * 8 == 48 and 10 + 11 == 21
dia = lambda a, b: a * a if a > b else (b * b if a < b else a * b)
dq(f"{S}-p10", "mo-p21", "If **a ◆ b = a²** when a > b, **b²** when a < b, and **ab** when a = b, find **(3 ◆ 5) ◆ 20**.", "625",
   ["400", "500", "9"],
   "3 ◆ 5: 3 < 5, so the answer is 5² = 25. Then 25 ◆ 20: 25 > 20, so 25² = **625**. (400 wrongly uses 20² again.)",
   "Work out the bracket, then re-check which case applies.", "medium", 45, check=dia(dia(3, 5), 20))
ot = lambda a, b: 3 * a - b
dq(f"{S}-p11", "mo-p22", "If **a ⊗ b = 3a − b**, find **(4 ⊗ 2) ⊗ 5**.", "25",
   [str(ot(4, ot(2, 5))), "35", "20"],
   "4 ⊗ 2 = 12 − 2 = 10. Then 10 ⊗ 5 = 30 − 5 = **25**. (11 comes from doing 2 ⊗ 5 first — ignoring the bracket.)",
   "The bracket decides which operation is done first.", "medium", 40, check=ot(ot(4, 2), 5))
st = lambda a, b: a + 2 * b
hs = lambda a, b: 2 * a - b
dq(f"{S}-p12", "mo-p22", "If **a ★ b = a + 2b** and **a # b = 2a − b**, find **(3 ★ 4) # (5 ★ 1)**.", "15",
   [str(hs(7, 11)), str(st(11, 7)), "18"],
   "3 ★ 4 = 3 + 8 = 11. 5 ★ 1 = 5 + 2 = 7. Then 11 # 7 = 22 − 7 = **15**. (3 swaps the inputs of #; 25 uses ★ instead of # at the last step.)",
   "Each symbol keeps its own formula; the first bracket is a, the second is b.", "hard", 55, check=hs(st(3, 4), st(5, 1)))

upsert(d["practice"], QS)

# ---------------- pyqPatterns ----------------
d["pyqPatterns"] = [
    PYQ("Full four-operator substitution", "very common",
        "The question says 'If + means ×, − means ÷, × means +, ÷ means −' (or similar) and gives an expression.",
        "Write the mapping, rewrite the whole line converting each sign once, then apply BODMAS. The original value and the left-to-right value are always planted as wrong options.",
        "sign-substitution",
        "If + means ×, − means ÷, × means +, ÷ means −, find 6 + 2 × 4 ÷ 2 − 2.",
        "Rewrite: 6 × 2 + 4 − 2 ÷ 2 = 12 + 4 − 1 = **15**."),
    PYQ("Letter-coded or partial substitution", "common",
        "Letters (A, B, C, D or P, Q, R, S) stand for signs, or only two signs change meaning.",
        "Replace each code by its real sign, leave the unlisted signs as they are, and calculate with BODMAS. Signs inside brackets are converted too.",
        "sign-substitution",
        "A means +, B means −, C means ×, D means ÷. Find 18 C 4 D 6 A 9 B 5.",
        "18 × 4 ÷ 6 + 9 − 5 = 12 + 9 − 5 = **16**."),
    PYQ("Interchange signs or numbers, then evaluate", "common",
        "'If + and × are interchanged (and 2 and 8 are interchanged), find the value of ...'.",
        "Interchange is a two-way swap. Do all swaps in one rewrite, change whole numbers only, then apply BODMAS.",
        "interchange-signs",
        "Interchange + and ×: find 3 × 4 + 5 − 6.",
        "3 + 4 × 5 − 6 = 3 + 20 − 6 = **17**."),
    PYQ("Which two numbers or signs to interchange", "common",
        "A false equation is given; options are pairs like '2 and 3' or '+ and −'.",
        "Sweep the option pairs in a fixed order. Swap, evaluate the left side, and stop at the pair that equals the right side. Use target size and last digits to skip hopeless pairs.",
        "interchange-signs",
        "Which two numbers should be interchanged: 4 + 2 × 6 − 3 = 20?",
        "Swap 2 and 3: 4 + 3 × 6 − 2 = 4 + 18 − 2 = 20 ✓ → **2 and 3**."),
    PYQ("Pick the correct equation", "very common",
        "Four complete equations are given and only one is arithmetically true.",
        "Evaluate every left side with BODMAS in writing and compare. Wrong options are usually built from left-to-right working, so careful BODMAS finds the answer fast.",
        "balance-equation",
        "Which is correct: 7 + 8 × 2 − 5 = 25 or 16 ÷ 4 × 2 + 6 = 14?",
        "7 + 16 − 5 = 18 ✗; 4 × 2 + 6 = 14 ✓ → **16 ÷ 4 × 2 + 6 = 14**."),
    PYQ("Sequentially replace the * signs", "very common",
        "`21 * 7 * 5 * 4 * 3 = 27` or `12 * 4 * 3 * 16` with options such as '÷, ×, +, ×' (sometimes including '=').",
        "Place the option's signs into the * marks from left to right and evaluate. If '=' is one of the signs, compare the two sides after filling.",
        "balance-equation",
        "`21 * 7 * 5 * 4 * 3 = 27` — does '÷, ×, +, ×' work?",
        "21 ÷ 7 × 5 + 4 × 3 = 15 + 12 = 27 ✓."),
    PYQ("Fill the blanks with a sign pair or set", "common",
        "'Which set of signs will make 18 ? 6 ? 3 ? 4 = 24 correct?'",
        "Test each option in order with BODMAS. A big right side needs ×; a small one needs ÷ or −.",
        "balance-equation",
        "18 ? 6 ? 3 ? 4 = 24 — test '−, +, ×'.",
        "18 − 6 + 3 × 4 = 12 + 12 = **24** ✓."),
    PYQ("Hidden rule from solved examples", "occasional",
        "Two or three worked examples like 5 # 3 = 34, 6 # 2 = 40 are given and a new pair is asked.",
        "Try the common rules — a + b, ab, a² ± b², (a ± b)², ab + a + b — and keep only the rule that fits every example. Then apply it.",
        "defined-operations",
        "5 # 3 = 34, 6 # 2 = 40. Find 7 # 4.",
        "a² + b² fits both examples: 49 + 16 = **65**."),
    PYQ("Defined symbol with a formula", "occasional",
        "'If a ★ b = 2a + 3b ...' or a conditional/nested definition.",
        "Write a and b before plugging in; solve inner brackets first; re-check any condition at each step.",
        "defined-operations",
        "If a ★ b = 2a + 3b, find 5 ★ 4.",
        "2 × 5 + 3 × 4 = **22**."),
    PYQ("BODMAS value or missing number", "common",
        "A plain expression to evaluate, or an equation with one '?'.",
        "Do brackets, then ÷ and × left to right, then + and − left to right. For a missing number, undo the steps backwards and put the value back to check.",
        "mathops-idea",
        "18 + 6 × ? − 4 = 38. Find ?",
        "6 × ? = 24, so ? = **4**."),
]

finish(TOPIC, d)
