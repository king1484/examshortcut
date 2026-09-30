"""Readable rewrite of Reasoning > Mathematical Operations (5 subtopics).

Every number in every example is recomputed below and asserted.
Sweeps (which pair balances the equation) are verified over ALL pairs.
Run: python mathematical_operations.py  (patches content/core/topics/reasoning/mathematical-operations.json)
"""
import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "mathematical-operations.json"

# ---------------- checks: mathops-idea ----------------
assert 3 * 10 + 2 * 40 == 110                                              # shop bill
assert 18 + 24 // 6 * 3 - 5 == 25 and ((18 + 24) // 6) * 3 - 5 == 16        # BODMAS 25, left-to-right trap 16
assert 96 // 8 * 4 == 48 and 96 // (8 * 4) == 3
assert 60 - 12 + 8 == 56 and 60 - (12 + 8) == 40
assert 100 - (20 + (30 - (12 - 4) * 2)) == 66                               # nested brackets
assert 18 + 6 * 4 - 4 == 38 and (38 + 4 - 18) // 6 == 4                     # missing number 4
assert 7 + 8 * 2 - 5 == 18 and (7 + 8) * 2 - 5 == 25                        # wrong-option build
assert 45 - 5 * 6 + 9 == 24 and 45 - (30 + 9) == 6                          # sign slip
assert 48 // (2 * (10 - 4)) + 5 == 9                                        # mo-p3 example
assert 40 - 6 * 3 + 20 // 4 == 27
assert 12 // (3 * 4) == 1 and (12 // 3) * 4 == 16                           # mo-p23: 12 / 3 of 4

# ---------------- checks: sign-substitution ----------------
# + means x, - means /, x means +, / means -
assert 6 * 2 + 4 - 2 // 2 == 15                                             # mo-p5
assert 9 * 4 + 7 == 43                                                      # mo-p6 partial
assert (24 // 8) * 2 == 6                                                   # mo-p7 brackets
assert 18 * 4 // 6 + 9 - 5 == 16                                            # mo-p8 letters
assert 9 + 4 * 2 == 17 and 9 * 4 + 2 == 38 and 8 + 5 * 1 == 13 and 6 + 3 * 1 == 9  # mo-p9: only first balances
assert 9 * 6 // 3 == 18                                                     # notes: + -> x, - -> /
assert 8 // 4 + 2 == 4 and 8 + 4 * 2 == 16                                  # notes trick: substituted 4, original 16

# ---------------- checks: interchange-signs ----------------
assert 3 + 4 * 5 - 6 == 17                                                  # mo-p10: swap + and x
assert 8 * 2 + 3 - 5 == 14                                                  # mo-p11: also 2 and 8
assert 20 * 4 // 5 == 16 and 20 // 4 * 5 == 25 and 20 * 4 % 5 == 0          # notes: swap x and / in 20 / 4 x 5
# mo-p12: 4 + 2 x 6 - 3 = 20 -> swap two numbers; sweep ALL 6 pairs
base12 = [4, 2, 6, 3]
ops12 = ["+", "*", "-"]
def eval_line(nums, ops):
    vals, i = [nums[0]], 0
    # BODMAS: * first, then + and - left to right (ops have equal rank pairs)
    line = f"{nums[0]}"
    for o, v in zip(ops, nums[1:]):
        line += f" {o} {v}"
    return eval(line)
hits12 = []
for i, j in combinations(range(4), 2):
    nums = base12[:]
    nums[i], nums[j] = nums[j], nums[i]
    if eval_line(nums, ops12) == 20:
        hits12.append((base12[i], base12[j]))
assert hits12 == [(2, 3)], hits12                                           # unique pair 2 and 3
assert 4 + 3 * 6 - 2 == 20
# notes sweep: 8 x 4 - 6 + 3 = 35
base_s = [8, 4, 6, 3]
hits_s = []
for i, j in combinations(range(4), 2):
    nums = base_s[:]
    nums[i], nums[j] = nums[j], nums[i]
    if eval_line(nums, ["*", "-", "+"]) == 35:
        hits_s.append((base_s[i], base_s[j]))
assert hits_s == [(6, 3)] and 8 * 4 - 3 + 6 == 35
# mo-p13: 12 + 6 / 3 - 2 x 4 = 18 -> swap two SIGNS; sweep all sign pairs
def eval_expr(s):
    return eval(s)
line13 = "12 {0} 6 {1} 3 {2} 2 {3} 4"
ops13 = ["+", "//", "-", "*"]
hits13 = []
for a, b in combinations(range(4), 2):
    o = ops13[:]
    o[a], o[b] = o[b], o[a]
    if eval_expr(line13.format(*o)) == 18:
        hits13.append((["+", "/", "-", "x"][a], ["+", "/", "-", "x"][b]))
assert hits13 == [("+", "-")], hits13                                        # unique: + and -
assert 12 - 6 // 3 + 2 * 4 == 18
# mo-p14: interchange + and -, then 10 - 4 + 2 x 3 = 8
assert 10 + 4 - 2 * 3 == 8

# ---------------- checks: balance-equation ----------------
assert 24 // 6 - 2 * 3 == -2 and 5 * 4 + 6 // 2 == 23 and 9 + 6 // 2 - 3 == 9 and 7 * 2 + 8 // 4 == 16  # only 2nd matches
assert 16 // 4 * 2 + 6 == 14 and 7 + 8 * 2 - 5 == 18 and (7 + 8) * 2 - 5 == 25  # idea p15 + trap
assert 30 * 6 - 4 == 176 and 30 // 6 + 4 == 9 and 6 % 4 != 0 and 30 - 6 * 4 == 6   # notes walk-through
# mo-p16: 14 ? 2 ? 3 = 21 over the 4 offered pairs
assert 14 + 2 * 3 == 20 and 14 * 2 - 3 == 25 and 14 // 2 * 3 == 21 and 14 - 2 + 3 == 15
# mo-p17
assert 21 // 7 * 5 + 4 * 3 == 27
# mo-p18
assert 12 * 4 // 3 == 16 and 12 // 4 * 3 == 9 and 12 + 4 - 3 == 13
# mo-p24: (7 ? 3) ? 5 = 50
assert (7 + 3) * 5 == 50 and 7 * 3 + 5 == 26 and (7 - 3) * 5 == 20 and 7 // 3 + 5 == 7

# ---------------- checks: defined-operations ----------------
star = lambda a, b: 2 * a + 3 * b
assert star(5, 4) == 22 and star(4, 5) == 23                                # mo-p19: order matters
sq = lambda a, b: a * a + b * b
assert sq(5, 3) == 34 and sq(6, 2) == 40 and sq(7, 4) == 65                 # mo-p20 hidden rule
assert 5 + 3 == 8 and 5 * 3 == 15 and 25 - 9 == 16 and (5 + 3) ** 2 == 64   # rejected candidates
cond = lambda a, b: a - b if a > b else a + b
assert cond(9, 4) == 5 and cond(5, 7) == 12                                 # mo-p21
otimes = lambda a, b: 3 * a - b
assert otimes(4, 2) == 10 and otimes(10, 5) == 25                           # mo-p22
at = lambda a, b: (a + b) // (a - b)
assert at(7, 5) == 6 and at(6, 3) == 3                                      # notes nested
# mo-p25: hidden input
assert star(5, 6) == 28 and (28 - 2 * 5) // 3 == 6
# formulas / trick
assert 8 * 8 - 2 * 2 == 60 and 7 * 7 - 3 * 3 == 40 and 9 * 9 - 4 * 4 == 65  # a^2 - b^2 trick
assert 6 * 2 + 6 + 2 == 20
assert 4 * 3 + 4 + 3 == 19                                                 # a $ b = ab + a + b
assert 5 * 5 + 4 * 4 == 41                                                  # notes quick check


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


SUBS = {}

# =====================================================================
# 1. mathops-idea
# =====================================================================
SUBS["mathops-idea"] = dict(
    concept=(
        "These questions give you a plain arithmetic line, or an equation with a missing number. "
        "The sums are easy. What is checked is the **order of operations**, called BODMAS. "
        "Do brackets first, then powers and 'of', then multiply and divide, then add and subtract."
    ),
    notes=r"""### What this topic tests
The numbers are small and the sums are easy. The examiner checks one thing: do you follow the **order of operations** without a slip?

Think of a shop bill. 3 pens at ₹10 each and 2 notebooks at ₹40 each cost $3 \times 10 + 2 \times 40 = 30 + 80 = 110$ rupees. Nobody adds 10 + 2 first. That habit is the whole topic.

### BODMAS in simple words
BODMAS tells you which part to work out first.

| Letter | Meaning | Example |
|---|---|---|
| B | Brackets | (6 + 2) is done first |
| O | Orders: powers, roots, "of" | $3^2$, $\sqrt{16}$, half **of** 10 |
| D, M | Division and Multiplication | same rank |
| A, S | Addition and Subtraction | same rank |

> **Example:** 18 + 24 ÷ 6 × 3 − 5. First 24 ÷ 6 = 4, then 4 × 3 = 12. Now 18 + 12 − 5 = **25**.

### Same rank means left to right
Division is **not** before multiplication. Addition is **not** before subtraction. Same-rank signs are worked from left to right.

- 96 ÷ 8 × 4 = 12 × 4 = **48**, not 96 ÷ 32 = 3.
- 60 − 12 + 8 = 48 + 8 = **56**, not 60 − 20 = 40.

> **Watch:** Examiners love to put ÷ before ×, or − before +. That one rule decides many answers.

### The word "of" counts early
"Of" means multiply, but it is done **before** ÷. It sits with the O of BODMAS.

> **Example:** 12 ÷ 3 of 4. First 3 of 4 = 12. Then 12 ÷ 12 = **1**. Left to right would give 16 — that is the planted wrong answer.

### Brackets inside brackets
Open brackets from the inside: first ( ), then { }, then [ ].

100 − [20 + {30 − (12 − 4) × 2}]. Inner: 12 − 4 = 8. Then 30 − 8 × 2 = 30 − 16 = 14. Then 20 + 14 = 34. Finally 100 − 34 = **66**.

> **Rule:** BODMAS works inside every bracket too. Do 8 × 2 before 30 − 8 × 2.

### A method for long lines
Long lines look scary. They are only small steps in a row.

1. Circle every bracket and "of". Solve them first.
2. Circle every × and ÷. Solve them from left to right.
3. Rewrite the shorter line after each step.
4. Finish with + and −, from left to right.

> **Example:** 40 − 6 × 3 + 20 ÷ 4. Circle 6 × 3 = 18 and 20 ÷ 4 = 5. The line is now 40 − 18 + 5 = **27**.

### Finding a missing number
One number is hidden: 18 + 6 × ? − 4 = 38. Undo the steps in reverse.

1. Move the loose terms: 6 × ? = 38 + 4 − 18 = 24.
2. Undo the multiply: ? = 24 ÷ 6 = **4**.
3. Put 4 back: 18 + 24 − 4 = 38. It fits.

> **Tip:** Always put your answer back. It takes five seconds and removes every doubt.

### How wrong options are built
Three slips build almost every wrong option.

- **Left-to-right slip:** 7 + 8 × 2 − 5 gives 25 left to right, but 7 + 16 − 5 = **18** is correct.
- **Sign slip:** 45 − 5 × 6 + 9 is 45 − 30 + 9 = **24**, not 45 − (30 + 9) = 6.
- **Forgotten term:** the last − 5 or + 4 is left out.

> **Tip:** Write the reduced line after each step, such as 18 + 12 − 5. Short lines prevent slips.
""",
    formulas=[
        {"name": "BODMAS order", "tex": r"B \to O \to D/M \to A/S", "note": "D and M share a rank and go left to right; so do A and S."},
        {"name": "Missing number", "tex": r"? = \dfrac{\text{RHS} - \text{loose terms}}{\text{factor}}", "note": "Undo + and − first, then the multiply or divide around the ?."},
    ],
    tricks=[
        trick("Circle the × and ÷ first",
              "Read the line once and circle every × and ÷. Work those pieces first. Then read the line again for + and −. Your eye lands on the high-rank work before any arithmetic.",
              "Find 7 + 8 × 2 − 5.",
              [r"Circled: $8 \times 2 = 16$.", r"Line becomes $7 + 16 - 5$.", "Add and subtract left to right."],
              "18"),
    ],
    mistakes=[
        {"wrong": "Working strictly left to right when BODMAS applies.", "right": "Do × and ÷ first, then + and −, left to right within each rank."},
        {"wrong": "Doing × before a ÷ that comes earlier in the line.", "right": "÷ and × have equal rank. Go left to right."},
        {"wrong": "Opening brackets from the outside in.", "right": "Open the innermost ( ) first, then { }, then [ ]."},
        {"wrong": "Treating 'of' like an ordinary multiply at its place.", "right": "'Of' belongs to the O of BODMAS and is done before ÷."},
        {"wrong": "Finding the missing number and moving on without checking.", "right": "Put the value back into the equation. Confirm both sides match."},
        {"wrong": "Dropping the last small term, like − 5 at the end.", "right": "After each step, rewrite the full reduced line before continuing."},
    ],
    revision=[
        "Order: Brackets, then Orders (powers, 'of'), then ÷ and ×, then + and −.",
        "÷ and × have equal rank; + and − have equal rank. Same rank = left to right.",
        "'Of' means multiply, but it is done before ÷.",
        "Nested brackets: ( ) first, then { }, then [ ]; BODMAS inside each.",
        "Missing number: undo the steps backwards, then put the value back.",
        "The left-to-right value is the examiner's favourite wrong option.",
    ],
    patterns=[
        pat("mo-p1", "Evaluate a mixed expression with BODMAS", "common",
            "A plain expression with + − × ÷ and no brackets. Options include the left-to-right value.",
            None,
            ["Circle every × and ÷ and work them out, left to right.", "Replace each piece with its value.", "Finish with + and −, left to right.", "Match with the options."],
            "× and ÷ bind the numbers next to them more tightly than + and −.",
            "Find the value of 18 + 24 ÷ 6 × 3 − 5.",
            ["24 ÷ 6 = 4, then 4 × 3 = 12.", "Line: 18 + 12 − 5.", "18 + 12 = 30, 30 − 5 = 25."],
            "25"),
        pat("mo-p2", "Same-rank operators: left to right", "common",
            "A chain of only ÷ and × (or only + and −), where ÷ comes before × or − before +.",
            None,
            ["Notice that every operator has the same rank.", "Work strictly from left to right.", "Keep the running value after each step."],
            "BODMAS lists D and M together, and A and S together. The letter order is only a memory aid.",
            "Find 96 ÷ 8 × 4.",
            ["96 ÷ 8 = 12.", "12 × 4 = 48."],
            "48"),
        pat("mo-p3", "Nested brackets", "common",
            "The expression has ( ), { } and [ ] brackets.",
            None,
            ["Solve the innermost ( ) first.", "Then the { }, then the [ ].", "Use BODMAS inside every bracket.", "Finish outside the brackets."],
            "Each bracket is a complete small expression whose value feeds the next one.",
            "Find [48 ÷ {2 × (10 − 4)}] + 5.",
            ["10 − 4 = 6.", "2 × 6 = 12.", "48 ÷ 12 = 4.", "4 + 5 = 9."],
            "9"),
        pat("mo-p4", "Find the missing number in an equation", "common",
            "An equation with a '?' in place of one number.",
            None,
            ["Undo the + and − terms: move them to the other side.", "Undo the × or ÷ around the '?'.", "Put the value back and check both sides."],
            "Undoing the steps in reverse keeps both sides equal at every move.",
            "18 + 6 × ? − 4 = 38. Find ?.",
            ["6 × ? = 38 + 4 − 18 = 24.", "? = 24 ÷ 6 = 4.", "Check: 18 + 6 × 4 − 4 = 38."],
            "4"),
        pat("mo-p23", "The word 'of' inside an expression", "occasional",
            "A ÷ line containing the word 'of', like 12 ÷ 3 of 4.",
            r"\text{of} \equiv \times \text{, done before } \div",
            ["Read 'of' as multiply.", "Do the 'of' piece first, before any ÷.", "Then finish with BODMAS as usual."],
            "'Of' sits in the O of BODMAS, one rank above division.",
            "Find 12 ÷ 3 of 4.",
            ["3 of 4 = 3 × 4 = 12.", "12 ÷ 12 = 1.", "Left to right would give 16 — the planted answer."],
            "1"),
    ],
)

# =====================================================================
# 2. sign-substitution
# =====================================================================
SUBS["sign-substitution"] = dict(
    concept=(
        "The question gives the signs new meanings: '+' means '×', '−' means '÷', and so on. "
        "First rewrite the whole expression with the new signs. Only then calculate with BODMAS. "
        "Rewriting and calculating at the same time is where every slip happens."
    ),
    notes=r"""### What sign substitution means
Picture a calculator with relabelled keys. The key printed "+" now multiplies. The key printed "×" now adds.

The question gives such a list and an expression. You must first convert the line into normal maths, then calculate. In SSC, Railway and Banking papers this is one of the most frequent reasoning questions. Done carefully, it is pure marks.

### The three-step method
1. **Write the mapping** in rough space, e.g. + → ×, − → ÷, × → +, ÷ → −.
2. **Rewrite the whole line** with the new signs. Keep every number and bracket in place.
3. **Calculate with BODMAS** on the rewritten line.

> **Example:** If + means ×, − means ÷, × means + and ÷ means −, find 6 + 2 × 4 ÷ 2 − 2. Rewrite: 6 × 2 + 4 − 2 ÷ 2. Then 12 + 4 − 1 = **15**.

### Change each sign once
"+ means × and × means +" is a **swap**: both changes happen at the same time.

Look only at the original line. Convert each symbol one time. Never convert a sign you have already changed. Writing the new line directly under the old one, symbol by symbol, keeps you honest.

### Partial substitution
Sometimes only two signs change: "+ means × and × means +". The other signs keep their normal meaning.

9 + 4 × 7 becomes 9 × 4 + 7 = 36 + 7 = **43**. The − or ÷ in the line, if any, stays as it is.

### Letters standing for signs
Signs may arrive as letters: "A means +, B means −, C means ×, D means ÷".

Then 18 C 4 D 6 A 9 B 5 means 18 × 4 ÷ 6 + 9 − 5. Left to right for × and ÷: 72 ÷ 6 = 12. Then 12 + 9 − 5 = **16**. The method does not change: rewrite first, calculate second.

### Signs inside brackets
Brackets never move and are always solved first. But the signs **inside** them are also coded.

If + means ÷ and − means ×, then (24 + 8) − 2 becomes (24 ÷ 8) × 2 = 3 × 2 = **6**. Forgetting the sign inside the bracket is a very common loss.

> **Watch:** After substitution, a ÷ may sit where a + used to be. The BODMAS order changes with the signs.

### Pick the correct equation after substitution
A harder form gives a mapping and four full equations. Convert each left side, evaluate, and compare with its right side. Exactly one balances.

If × means + and + means ×, test 9 × 4 + 2 = 17. Substituted: 9 + 4 × 2 = 9 + 8 = 17. It balances.

> **Tip:** Work one option per line, in writing. The right sides are plain numbers; only the left sides are coded.

### Know the planted wrong answers
| Slip | What the student did |
|---|---|
| Mapping ignored | calculated the original expression |
| BODMAS skipped | rewrote correctly, then went left to right |
| Half substitution | converted some signs and missed others |

> **Tip:** Compute the original expression once as a cross-check. If your answer equals that value, you forgot to substitute.
""",
    tricks=[
        trick("Compute the trap value too",
              "After the correct value, evaluate the original expression once. If that number sits among the options, the examiner planted it. Seeing it confirms your substitution is the different one.",
              "If '+' means '÷' and '×' means '+', evaluate 8 + 4 × 2.",
              [r"Substituted: $8 \div 4 + 2 = 2 + 2 = 4$.", r"Original: $8 + 4 \times 2 = 16$ — the 'mapping ignored' trap."],
              "4"),
    ],
    mistakes=[
        {"wrong": "Substituting and calculating at the same time.", "right": "Rewrite the full line first, then calculate."},
        {"wrong": "Converting a sign twice while handling a swap.", "right": "Read only the original line. Convert each symbol once."},
        {"wrong": "Changing signs that the question did not list.", "right": "Unlisted signs keep their normal meaning."},
        {"wrong": "Leaving the signs inside brackets as they were.", "right": "Convert them too. Brackets fix the order, not the meanings."},
        {"wrong": "Marking the value of the original expression.", "right": "Cross-check: if your answer equals the original value, redo the substitution."},
    ],
    revision=[
        "Mapping table, then rewrite the full line, then BODMAS. Never mix the steps.",
        "A swap like '+ means × and × means +' works both ways at once.",
        "Signs not in the list keep their normal meaning.",
        "Letters for signs are handled exactly the same way.",
        "Convert signs inside brackets; solve brackets first.",
        "Wrong options: original value, left-to-right value, half-substituted value.",
    ],
    patterns=[
        pat("mo-p5", "Full four-sign substitution", "very common",
            "'If + means ×, − means ÷, × means + and ÷ means −, then … = ?' All four signs are reassigned.",
            None,
            ["Write the four-row mapping table.", "Rewrite the whole line, converting each sign once.", "Evaluate with BODMAS.", "Compare with the options."],
            "Separating 'rewrite' from 'calculate' removes every sign slip.",
            "If + means ×, − means ÷, × means + and ÷ means −, find 6 + 2 × 4 ÷ 2 − 2.",
            ["Rewrite: 6 × 2 + 4 − 2 ÷ 2.", "6 × 2 = 12 and 2 ÷ 2 = 1.", "12 + 4 − 1 = 15."],
            "15"),
        pat("mo-p6", "Partial (two-sign) substitution", "common",
            "Only two signs are given new meanings; the others stay normal.",
            None,
            ["Change only the listed signs.", "Keep the other signs as they are.", "Evaluate with BODMAS."],
            "An unlisted sign keeps its usual job.",
            "If + means × and × means +, find 9 + 4 × 7.",
            ["Rewrite: 9 × 4 + 7.", "36 + 7 = 43."],
            "43"),
        pat("mo-p7", "Substitution with brackets", "common",
            "The expression under substitution contains brackets.",
            None,
            ["Convert the signs inside and outside the brackets.", "Solve the bracket first.", "Finish with BODMAS."],
            "Brackets fix the order, but their inner signs are still coded.",
            "If + means ÷ and − means ×, find (24 + 8) − 2.",
            ["Rewrite: (24 ÷ 8) × 2.", "24 ÷ 8 = 3.", "3 × 2 = 6."],
            "6"),
        pat("mo-p8", "Letter-coded operators", "common",
            "Letters like A, B, C, D stand for the four signs.",
            None,
            ["Write the letter-to-sign table.", "Replace each letter by its sign.", "Evaluate with BODMAS."],
            "A letter is just another name for a sign.",
            "A means +, B means −, C means × and D means ÷. Find 18 C 4 D 6 A 9 B 5.",
            ["Rewrite: 18 × 4 ÷ 6 + 9 − 5.", "18 × 4 = 72, then 72 ÷ 6 = 12.", "12 + 9 − 5 = 16."],
            "16"),
        pat("mo-p9", "Substitute, then pick the correct equation", "occasional",
            "A mapping is given, and the options are four complete equations. One becomes true after substitution.",
            None,
            ["Convert the left side of the first option.", "Evaluate it and compare with its right side.", "Repeat for every option in writing.", "Mark the one that balances."],
            "The right side is already a plain number; only the left side is coded.",
            "If × means + and + means ×, which equation is correct: 9 × 4 + 2 = 17, 9 + 4 × 2 = 17, 8 × 5 + 1 = 14 or 6 × 3 + 1 = 20?",
            ["First: 9 + 4 × 2 = 9 + 8 = 17 ✓.", "Second: 9 × 4 + 2 = 38 ✗.", "Third: 8 + 5 × 1 = 13 ✗. Fourth: 6 + 3 × 1 = 9 ✗."],
            "9 × 4 + 2 = 17"),
    ],
)

# =====================================================================
# 3. interchange-signs
# =====================================================================
SUBS["interchange-signs"] = dict(
    concept=(
        "Interchange means a two-way swap: 'interchange + and ×' puts + wherever × stood and × wherever + stood. "
        "Sometimes two numbers are swapped instead, or both. Apply every swap in one rewrite, then use BODMAS. "
        "The fix-the-equation variant asks which pair, when swapped, makes a false equation true — sweep the pairs in order."
    ),
    notes=r"""### What interchange means
To interchange two things is to **swap** them, both ways at once. "Interchange + and ×" turns 3 × 4 + 5 into 3 + 4 × 5.

Think of two students exchanging seats: both move. This differs from sign substitution, where the mapping can go one way.

### Swap two signs, then find the value
Rewrite the line with the two signs exchanged, then use BODMAS.

Interchange + and × in 3 × 4 + 5 − 6. New line: 3 + 4 × 5 − 6 = 3 + 20 − 6 = **17**.

> **Rule:** Every occurrence of both signs changes. A sign that appears twice is swapped twice.

### A swap of × and ÷
This swap changes the order of work too, so go slowly.

Interchange × and ÷ in 20 ÷ 4 × 5. New line: 20 × 4 ÷ 5. Left to right: 20 × 4 = 80, then 80 ÷ 5 = **16**.

The original line gives 20 ÷ 4 × 5 = 5 × 5 = 25. That value is the usual wrong option.

> **Tip:** After any swap, rewrite the line and read it fresh. Do not reuse the old order of work.

### Swap numbers too
"Interchange 2 and 8" means every 2 becomes 8 and every 8 becomes 2. Do all swaps in **one** rewrite, then calculate.

Interchange + and ×, and also 2 and 8, in 2 + 8 × 3 − 5. New line: 8 × 2 + 3 − 5 = 16 + 3 − 5 = **14**.

> **Watch:** Swap whole numbers only. If the swap is 2 and 5, a number like 25 does not change at all.

### Fix the equation: sweep the pairs
You get a false equation, for example 4 + 2 × 6 − 3 = 20, and pairs in the options. Do a **sweep**: swap each pair, evaluate, stop at the one that balances.

- (4, 2): 2 + 4 × 6 − 3 = 23 ✗
- (4, 6): 6 + 2 × 4 − 3 = 11 ✗
- (2, 3): 4 + 3 × 6 − 2 = **20** ✓

With 4 numbers there are only 6 possible pairs. You normally test just the 4 option pairs.

### Which two signs to swap
Same sweep, but on operators. 12 + 6 ÷ 3 − 2 × 4 = 18. Try + and −: 12 − 6 ÷ 3 + 2 × 4 = 12 − 2 + 8 = **18** ✓.

Work in a fixed order: (+, −), (+, ×), (+, ÷), (−, ×), (−, ÷), (×, ÷). One written value per row.

### After a given swap, which equation is correct?
The swap is stated first; four equations follow. Apply the swap to each **left side**, evaluate, and compare with its right side.

Interchange + and −, then test 10 − 4 + 2 × 3 = 8. Swapped: 10 + 4 − 2 × 3 = 14 − 6 = 8 ✓.

### Checks that save time
- **Skip pointless pairs:** swapping the two numbers of one product, like 8 × 4 to 4 × 8, changes nothing.
- **Size check:** a big target like 81 needs a big product. A small target needs ÷ or −.
- **Last-digit check:** 8 × 6 ends in 8. If the target ends in 5, drop that pair at once.
- **Exact division:** a swap creating 7 ÷ 5 rarely gives a whole number. Test it last.

> **Tip:** If no row balances, you mis-evaluated a row — redo the row, not the method.
""",
    tricks=[
        trick("One rewrite for every swap",
              "Write the swaps on the left, like + ↔ × and 2 ↔ 8. Then rewrite the expression once with all swaps applied. Evaluate. Piececemeal swapping invites double swaps.",
              "Interchange + with × and 2 with 6 in 2 + 6 × 3.",
              ["Both swaps at once: 6 × 2 + 3.", "6 × 2 = 12, then 12 + 3 = 15."],
              "15"),
        trick("Fixed-order sweep for fix-the-equation",
              "Sweep number pairs left to right: (n1,n2), (n1,n3), (n1,n4), (n2,n3), (n2,n4), (n3,n4). One written value per row. The row matching the right side is the answer.",
              "Make 8 × 4 − 6 + 3 = 35 correct by interchanging two numbers.",
              ["(8,4): 4 × 6 − 8 + 3 = 19 ✗; (8,6): 6 × 4 − 8 + 3 = 19 ✗.", "(8,3): 3 × 4 − 6 + 8 = 14 ✗; (4,6): 8 × 6 − 4 + 3 = 47 ✗.", "(4,3): 8 × 3 − 6 + 4 = 22 ✗; (6,3): 8 × 4 − 3 + 6 = 35 ✓."],
              "Interchange 6 and 3"),
    ],
    mistakes=[
        {"wrong": "Swapping one way only (+ becomes ×, the old × stays).", "right": "Interchange is two-way. Both signs change places, everywhere."},
        {"wrong": "Swapping digits inside a number (changing 25 when told 2 and 5).", "right": "Swap whole numbers only."},
        {"wrong": "Applying two swaps in two separate rewrites.", "right": "One rewrite with every swap applied at once."},
        {"wrong": "Guessing which pair balances the equation.", "right": "Sweep the option pairs in a fixed order and evaluate each in writing."},
        {"wrong": "Evaluating the swapped line left to right.", "right": "BODMAS still rules after any swap."},
    ],
    revision=[
        "Interchange = two-way swap; every occurrence of both items changes.",
        "Apply all swaps, signs and numbers, in ONE rewrite, then BODMAS.",
        "Fix-the-equation: sweep pairs in a fixed order; stop at the row that balances.",
        "Swapping the two numbers of one product changes nothing. Skip it.",
        "Size, last digit and exact division cut option pairs fast.",
        "Numbers and signs can be swapped in the same question.",
    ],
    patterns=[
        pat("mo-p10", "Interchange two signs, then evaluate", "common",
            "'If + and ÷ are interchanged, find the value of …'",
            None,
            ["Swap both signs everywhere, two-way.", "Rewrite the line once.", "Evaluate with BODMAS."],
            "Interchange is symmetric, so both signs move.",
            "The signs + and × are interchanged. What is the value of 3 × 4 + 5 − 6?",
            ["New line: 3 + 4 × 5 − 6.", "4 × 5 = 20.", "3 + 20 − 6 = 17."],
            "17"),
        pat("mo-p11", "Interchange numbers with or without signs", "common",
            "'If 2 and 8 are interchanged (and + and ×)…' Numbers are swapped too.",
            None,
            ["Do every swap in one rewrite.", "Swap whole numbers only.", "Evaluate with BODMAS."],
            "Doing swaps one after another invites double swaps.",
            "Interchange + and ×, and also 2 and 8. What is 2 + 8 × 3 − 5?",
            ["New line: 8 × 2 + 3 − 5.", "8 × 2 = 16.", "16 + 3 − 5 = 14."],
            "14"),
        pat("mo-p12", "Which two numbers make the equation true", "common",
            "A false equation, with pairs like '4 and 2', '6 and 3' in the options.",
            None,
            ["Swap the first option pair.", "Evaluate the left side with BODMAS.", "Compare with the right side.", "Repeat until one pair balances."],
            "Only one pair restores the balance in a well-set question.",
            "Which two numbers should be interchanged to make 4 + 2 × 6 − 3 = 20 correct?",
            ["Swap 4 and 2: 2 + 4 × 6 − 3 = 23 ✗.", "Swap 4 and 6: 6 + 2 × 4 − 3 = 11 ✗.", "Swap 2 and 3: 4 + 3 × 6 − 2 = 20 ✓."],
            "2 and 3"),
        pat("mo-p13", "Which two signs make the equation true", "common",
            "A false equation, with sign pairs like '+ and −', '× and ÷' in the options.",
            None,
            ["Swap the first option pair everywhere.", "Evaluate the left side.", "Compare with the right side.", "Repeat until one pair balances."],
            "The same sweep works on operators as on numbers.",
            "Which two signs should be interchanged to make 12 + 6 ÷ 3 − 2 × 4 = 18 correct?",
            ["Try + and −: 12 − 6 ÷ 3 + 2 × 4.", "6 ÷ 3 = 2 and 2 × 4 = 8.", "12 − 2 + 8 = 18 ✓."],
            "+ and −"),
        pat("mo-p14", "After a given interchange, which equation is correct", "occasional",
            "The swap is stated first; four complete equations follow.",
            None,
            ["Apply the swap to each left side.", "Evaluate with BODMAS.", "Compare with the right side.", "Mark the only one that balances."],
            "The right sides are plain numbers and do not change.",
            "The signs + and − are interchanged. Is 10 − 4 + 2 × 3 = 8 correct?",
            ["Swapped line: 10 + 4 − 2 × 3.", "2 × 3 = 6.", "10 + 4 − 6 = 8 ✓ — correct."],
            "Yes, it is correct"),
    ],
)

# =====================================================================
# 4. balance-equation
# =====================================================================
SUBS["balance-equation"] = dict(
    concept=(
        "An equation is a scale: the left side must equal the right side. "
        "Three question shapes test it. Pick the equation that is already true, fill sign blanks so the line balances, "
        "or place a full set of signs (sometimes including =) in order. "
        "Evaluate every option in writing; exactly one balances."
    ),
    notes=r"""### What balancing means
An equation is like a weighing scale. The left side and the right side must show the same value.

Here you either check which equation is already balanced, or choose signs that balance it. Nothing is hidden. You need clean BODMAS and a fixed order of testing.

### Pick the correct equation
Four full equations are given; exactly one is true. Build a value column: one row per option, left-side value against the right side.

- 24 ÷ 6 − 2 × 3 = 1 → 4 − 6 = **−2** ✗
- 5 × 4 + 6 ÷ 2 = 23 → 20 + 3 = **23** ✓
- 9 + 6 ÷ 2 − 3 = 11 → 9 + 3 − 3 = **9** ✗
- 7 × 2 + 8 ÷ 4 = 18 → 14 + 2 = **16** ✗

> **Tip:** A wrong option is often the left-to-right value. 7 + 8 × 2 − 5 is 18 by BODMAS, but 25 left to right. Both 18 and 25 can sit among the options.

### Fill the blanks with signs
"Which pair of signs makes 14 ? 2 ? 3 = 21 true?" Put each option pair in and evaluate.

- (+, ×): 14 + 2 × 3 = 20 ✗
- (÷, ×): 14 ÷ 2 × 3 = **21** ✓
- (×, −): 28 − 3 = 25 ✗

The first sign of the pair goes into the **first** blank, always.

### Sequentially replace the * signs
Recent papers write: "Select the combination of signs to sequentially replace the * signs and balance the equation", like 21 * 7 * 5 * 4 * 3 = 27.

"Sequentially" fixes the placement: first sign into the first *, second into the second, and so on. Option ÷, ×, +, × gives 21 ÷ 7 × 5 + 4 × 3 = 15 + 12 = **27** ✓.

### When = is one of the signs
The line has no = yet: 12 * 4 * 3 * 16, and one option sign is "=". Place the signs in order, then compare the two sides.

×, ÷, = gives 12 × 4 ÷ 3 = 16, that is 48 ÷ 3 = 16 ✓. Both sides match.

> **Watch:** The = usually sits just before the last number, but not always. Test the placement; examiners move it to catch guessers.

### Fill blanks inside brackets
Brackets can hold a blank too: (7 ? 3) ? 5 = 50. The bracket is solved first, so a sign inside it is powerful.

(+, ×) gives (7 + 3) × 5 = 50 ✓, while (×, +) gives only 7 × 3 + 5 = 26.

### One full walk-through
Find the pair that makes 30 ? 6 ? 4 = 9 true. The options are (×, −), (÷, +), (+, ÷) and (−, ×).

1. (×, −): 30 × 6 − 4 = 180 − 4 = 176. Too big. ✗
2. (÷, +): 30 ÷ 6 + 4 = 5 + 4 = **9**. ✓
3. (+, ÷): 30 + 6 ÷ 4 is not a whole number. ✗
4. (−, ×): 30 − 6 × 4 = 30 − 24 = 6. ✗

Only the second row matches, so the answer is (÷, +).

### Test in a smart order
1. Look at the right side. Big target → you need ×. Small target → look for ÷ or −.
2. Test options that create **exact** divisions first. 72 ÷ 8 = 9 is friendly; 7 ÷ 5 is a dead end.
3. Use the **last digit**. If the target ends in 7 and an option's arithmetic ends in 0, drop it.
4. Once one option balances, mark it. In a well-set question only one works.

> **Tip:** Never judge an equation by looks. A four-row value column is faster than staring.
""",
    tricks=[
        trick("Value column for pick-the-equation",
              "List the four options in a column. Evaluate each left side in one written line. Exactly one row matches its right side. The column doubles as your final check.",
              "Which is correct: 24 ÷ 6 − 2 × 3 = 1, 5 × 4 + 6 ÷ 2 = 23, 9 + 6 ÷ 2 − 3 = 11 or 7 × 2 + 8 ÷ 4 = 18?",
              ["24 ÷ 6 − 2 × 3 = 4 − 6 = −2 ✗.", "5 × 4 + 6 ÷ 2 = 20 + 3 = 23 ✓.", "9 + 6 ÷ 2 − 3 = 9 + 3 − 3 = 9 ✗.", "7 × 2 + 8 ÷ 4 = 14 + 2 = 16 ✗."],
              "5 × 4 + 6 ÷ 2 = 23"),
    ],
    mistakes=[
        {"wrong": "Scanning the options for a nice-looking equation.", "right": "Evaluate every option in a written value column."},
        {"wrong": "Putting the option signs into the blanks from the right.", "right": "First sign into the first blank, left to right."},
        {"wrong": "Treating ÷ as always after ×.", "right": "Equal rank: ÷ and × go left to right."},
        {"wrong": "Computing the whole line when = is one of the signs.", "right": "The = splits the line. Compare the two sides separately."},
        {"wrong": "Stopping at the first option that looks close.", "right": "Finish each row's arithmetic. Only an exact match counts."},
    ],
    revision=[
        "Balanced means left value equals right value. Test each option in writing.",
        "Sign pairs: first sign into the first blank, always.",
        "'Sequentially replace *': first sign to first *, in order.",
        "When = is among the signs, compare the part before it with the part after it.",
        "Brackets with blanks are solved first, so signs inside them are powerful.",
        "Target size, exact division and last digit cut options fast.",
    ],
    patterns=[
        pat("mo-p15", "Pick the arithmetically correct equation", "very common",
            "'Which of the following equations is correct?' with four complete equations.",
            None,
            ["Evaluate each left side with BODMAS.", "Write one value per row.", "Compare with the right side.", "Mark the only match."],
            "Wrong options are usually left-to-right values of a correct-looking line.",
            "Which equation is correct: 24 ÷ 6 − 2 × 3 = 1, 5 × 4 + 6 ÷ 2 = 23, 9 + 6 ÷ 2 − 3 = 11 or 7 × 2 + 8 ÷ 4 = 18?",
            ["Row values: −2, 23, 9, 16.", "Right sides: 1, 23, 11, 18.", "Only the second row matches."],
            "5 × 4 + 6 ÷ 2 = 23"),
        pat("mo-p16", "Fill the blanks with a sign pair", "common",
            "'Which pair of signs will make 14 ? 2 ? 3 = 21 correct?'",
            None,
            ["Put the first option pair into the blanks, in order.", "Evaluate with BODMAS.", "Compare with the right side.", "Repeat until one pair works."],
            "Testing is faster and safer than guessing the signs.",
            "Which pair of signs makes 14 ? 2 ? 3 = 21 correct: (+, ×), (÷, ×), (×, −) or (−, +)?",
            ["(+, ×): 14 + 2 × 3 = 20 ✗.", "(÷, ×): 14 ÷ 2 × 3 = 7 × 3 = 21 ✓.", "(×, −): 28 − 3 = 25 ✗. (−, +): 14 − 2 + 3 = 15 ✗."],
            "÷ and ×"),
        pat("mo-p17", "Sequentially replace the * signs", "very common",
            "A line like 21 * 7 * 5 * 4 * 3 = 27. 'Select the combination of signs to sequentially replace the * signs.'",
            None,
            ["Send the first sign into the first *, second into the second, and so on.", "Evaluate with BODMAS.", "Check against the right side."],
            "'Sequentially' fixes the placement, so each option makes exactly one line.",
            "Which signs balance 21 * 7 * 5 * 4 * 3 = 27 when placed in order: ÷, ×, +, ×?",
            ["Line: 21 ÷ 7 × 5 + 4 × 3.", "21 ÷ 7 = 3, then 3 × 5 = 15. Also 4 × 3 = 12.", "15 + 12 = 27 ✓."],
            "Yes: ÷, ×, +, × balances it"),
        pat("mo-p18", "Replace * signs when = is one of them", "common",
            "A line like 12 * 4 * 3 * 16 has no = yet; the options contain '='.",
            None,
            ["Place the signs in order, including the =.", "Evaluate the part before the =.", "Evaluate the part after the =.", "The two values must match."],
            "The = splits the line into two separate expressions.",
            "Where do ×, ÷ and = go in 12 * 4 * 3 * 16 to balance it?",
            ["Try ×, ÷, = in order: 12 × 4 ÷ 3 = 16.", "Left: 48 ÷ 3 = 16.", "Right: 16. They match."],
            "12 × 4 ÷ 3 = 16"),
        pat("mo-p24", "Fill blanks inside brackets", "occasional",
            "The blank sits inside a bracket, like (7 ? 3) ? 5 = 50.",
            None,
            ["Solve the bracket with the first option's inside sign.", "Apply the outside sign.", "Compare with the right side.", "Repeat with the other options."],
            "The bracket is solved first, so the sign inside it shapes the whole line.",
            "Which pair of signs makes (7 ? 3) ? 5 = 50 correct: (+, ×), (×, +), (−, ×) or (÷, +)?",
            ["(+, ×): (7 + 3) × 5 = 50 ✓.", "(×, +): 7 × 3 + 5 = 26 ✗.", "(−, ×): (7 − 3) × 5 = 20 ✗. (÷, +): 7 ÷ 3 + 5 is not whole ✗."],
            "+ and ×"),
    ],
)

# =====================================================================
# 5. defined-operations
# =====================================================================
SUBS["defined-operations"] = dict(
    concept=(
        "A new symbol like ★, # or @ is given its own meaning. Either a formula is stated (a ★ b = 2a + 3b), "
        "or solved examples are shown and you must find the rule. "
        "Put the first number into a and the second into b. The order matters."
    ),
    notes=r"""### What a defined operation is
The examiner invents a symbol and tells you what it does. "a ★ b = 2a + 3b" is just a short name for a small formula.

To find 5 ★ 4, put a = 5 and b = 4: $2 \times 5 + 3 \times 4 = 10 + 12 = 22$.

Think of a shop rule: "combo price = 2 × burger + 3 × drink". You just plug in the prices.

### The order of a and b matters
The first number is a. The second is b. Swap them and the answer can change.

With a ★ b = 2a + 3b: 5 ★ 4 = 22, but 4 ★ 5 = 8 + 15 = **23**. A formula like $a^2 + b^2$ does not care about order. One like 2a + 3b does.

> **Tip:** Write "a = __, b = __" before plugging anything in. It sounds slow; it saves the question.

### Nested operations
(7 @ 5) @ 3 means: work out 7 @ 5 first, then feed that answer back in.

With a @ b = (a + b) ÷ (a − b): 7 @ 5 = 12 ÷ 2 = 6. Then 6 @ 3 = 9 ÷ 3 = **3**. Brackets decide the order, exactly as in BODMAS. When two symbols are defined, give each bracket its own formula, then combine.

### Find the hidden rule from examples
The question shows solved pairs, like 5 # 3 = 34 and 6 # 2 = 40, and asks for 7 # 4. Climb a ladder of common rules and test each on **every** example.

| Try | 5 and 3 give | 6 and 2 give |
|---|---|---|
| a + b, a × b | 8, 15 | 8, 12 |
| $a^2 + b^2$ | **34 ✓** | **40 ✓** |
| $a^2 - b^2$ | 16 | 32 |
| $(a+b)^2$ | 64 | 64 |

The rule is $a^2 + b^2$, so 7 # 4 = 49 + 16 = **65**.

> **Rule:** A rule that fits only one example is not the rule. Two examples are given so that only one rule survives.

### Rules that appear most often
- Sum or difference of squares: $a^2 + b^2$, $a^2 - b^2$.
- Square of sum or difference: $(a+b)^2$, $(a-b)^2$.
- Product plus sum: $ab + a + b$.
- Weighted sums: $2a + 3b$, $3a - b$.
- Mixed: $a^2 + b$, $ab - a$.

### Formulas with three parts
Some rules add more than two parts. Take $a \diamond b = ab + a + b$.

- 4 ◇ 3 = 12 + 4 + 3 = **19**.
- 6 ◇ 2 = 12 + 6 + 2 = **20**.

Work out each part on its own line. Then add. A missed part is the most common slip.

### Conditional definitions
The formula can depend on a condition: "a ▲ b = a − b if a > b, and a + b if a ≤ b". Check the condition **every time**.

9 ▲ 4: since 9 > 4, use a − b, giving 5. Then 5 ▲ 7: since 5 ≤ 7, use a + b, giving **12**.

> **Watch:** Students reuse the first case without checking. The second step often falls in the other case.

### Keep your answer sane
If every option is a whole number and yours is a fraction, recheck the rule. Negative results are fine only when the options allow them.

> **Tip:** After finding the rule, run it once more on a sample you already know. Two seconds, zero doubt.
""",
    formulas=[
        {"name": "Sum of squares", "tex": r"a \# b = a^2 + b^2", "note": "A very common hidden rule: 5 # 3 = 34."},
        {"name": "Difference of squares", "tex": r"a @ b = a^2 - b^2", "note": "Also equals (a+b)(a−b): 8 @ 2 = 60."},
        {"name": "Product plus sum", "tex": r"a \diamond b = ab + a + b", "note": "Multiply, then add both numbers: 4 ◇ 3 = 19."},
    ],
    tricks=[
        trick("Rule ladder for hidden operations",
              "Test in this order: a + b, a × b, a² + b², a² − b², (a+b)², (a−b)², ab + a + b. Stop at the first rule that fits ALL examples.",
              "8 @ 2 = 60 and 7 @ 3 = 40. Find 9 @ 4.",
              ["64 − 4 = 60 ✓ and 49 − 9 = 40 ✓.", "The rule is a² − b².", "9 @ 4 = 81 − 16 = 65."],
              "65"),
    ],
    mistakes=[
        {"wrong": "Swapping a and b in a formula that is not symmetric.", "right": "a is the first number, b the second. Write both down before plugging in."},
        {"wrong": "Accepting a rule after checking one example.", "right": "The rule must fit every example given."},
        {"wrong": "Reusing the first case of a conditional definition.", "right": "Check the condition again at every new step."},
        {"wrong": "Feeding the outer number into an inner bracket.", "right": "Finish the inner bracket fully; its value is the new input."},
        {"wrong": "Keeping a fraction answer when all options are whole numbers.", "right": "Recheck which rule fits both examples."},
    ],
    revision=[
        "Defined symbol = a small formula. Plug a = first number, b = second.",
        "Order matters unless the formula is symmetric.",
        "Nested: inner bracket first; its result becomes the new input.",
        "Hidden rule ladder: a+b, ab, a²+b², a²−b², (a±b)², ab+a+b. Must fit ALL examples.",
        "Conditional: re-check the condition at each step.",
        "Answers must match the options' shape: whole, positive, and so on.",
    ],
    patterns=[
        pat("mo-p19", "Defined formula: a ★ b = given expression", "common",
            "The question defines a new symbol with a formula in a and b.",
            r"a \star b = 2a + 3b",
            ["Write a = first number, b = second number.", "Put both into the formula.", "Calculate."],
            "The symbol is only a short name for the formula.",
            "If a ★ b = 2a + 3b, find 5 ★ 4.",
            ["a = 5, b = 4.", "2 × 5 = 10 and 3 × 4 = 12.", "10 + 12 = 22."],
            "22"),
        pat("mo-p20", "Hidden rule from solved examples", "common",
            "Examples like 5 # 3 = 34, 6 # 2 = 40, then '7 # 4 = ?'.",
            r"a \# b = a^2 + b^2",
            ["Climb the rule ladder: a+b, ab, a²+b², a²−b², (a±b)², ab+a+b.", "Keep the rule that fits EVERY example.", "Apply it to the asked pair."],
            "Two examples are given so that only one rule survives the test.",
            "If 5 # 3 = 34 and 6 # 2 = 40, find 7 # 4.",
            ["25 + 9 = 34 ✓ and 36 + 4 = 40 ✓.", "The rule is a² + b².", "49 + 16 = 65."],
            "65"),
        pat("mo-p21", "Conditional definition", "occasional",
            "The symbol does different things depending on a condition, like a > b.",
            None,
            ["Check the condition for the given pair.", "Use the matching formula.", "Re-check the condition at every new step."],
            "The second step often falls in the other case.",
            "a ▲ b = a − b if a > b, and a + b if a ≤ b. Find (9 ▲ 4) ▲ 7.",
            ["9 > 4, so 9 ▲ 4 = 9 − 4 = 5.", "5 ≤ 7, so use a + b.", "5 + 7 = 12."],
            "12"),
        pat("mo-p22", "Nested or two-symbol defined operations", "common",
            "Brackets combine defined operations: (7 @ 5) @ 3, or two symbols in one line.",
            r"a \otimes b = 3a - b",
            ["Solve the inner bracket with its own formula.", "Write its value clearly.", "Use that value as the input to the outer operation."],
            "Brackets decide the order, as in BODMAS.",
            "If a ⊗ b = 3a − b, find (4 ⊗ 2) ⊗ 5.",
            ["4 ⊗ 2 = 12 − 2 = 10.", "Now 10 ⊗ 5 = 30 − 5.", "30 − 5 = 25."],
            "25"),
        pat("mo-p25", "Find a hidden input", "occasional",
            "The formula and the full result are given; one of the two input numbers is asked.",
            None,
            ["Write the equation with the unknown in place.", "Undo the arithmetic step by step.", "Check by computing the operation fully."],
            "It is the same formula read backwards, one undo at a time.",
            "If a ★ b = 2a + 3b and 5 ★ b = 28, what is b?",
            ["2 × 5 + 3b = 28, so 10 + 3b = 28.", "3b = 18, so b = 6.", "Check: 2 × 5 + 3 × 6 = 28 ✓."],
            "6"),
    ],
)

# ---------------- apply ----------------
dfrac = lambda x: x.replace(r"\frac", r"\dfrac")
data = json.loads(TOPIC.read_text(encoding="utf-8"))
all_new_ids = [p_["id"] for s in SUBS.values() for p_ in s["patterns"]]
assert len(all_new_ids) == len(set(all_new_ids)), "duplicate pattern id"
for sub in data["subtopics"]:
    new = SUBS.pop(sub["id"])
    old_ids = {p_["id"] for p_ in sub.get("patterns", [])}
    new_ids = {p_["id"] for p_ in new["patterns"]}
    assert old_ids <= new_ids, (sub["id"], old_ids - new_ids)
    notes = new["notes"].strip() + "\n"
    assert 2500 <= len(notes) <= 5000, (sub["id"], len(notes))
    sub["concept"] = new["concept"]
    sub["notes"] = notes
    sub["patterns"] = new["patterns"]
    sub["mistakes"] = [{k: dfrac(v) for k, v in m_.items()} for m_ in new["mistakes"]]
    sub["revision"] = [dfrac(r) for r in new["revision"]]
    if "tricks" in new:
        sub["tricks"] = new["tricks"]
    if "formulas" in new:
        sub["formulas"] = new["formulas"]
    print(f"{sub['id']}: {len(notes)} chars, {len(new['patterns'])} patterns (was {len(old_ids)})")
assert not SUBS, f"unused subtopics: {list(SUBS)}"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("mathematical-operations updated")
