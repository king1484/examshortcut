"""Phase-2 deep content for quant/simplification. Run: py -3 simplification.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from _lib import Sub, apply_topic, nearest, fr, num

of = r"\text{ of }"


def bodmas_q(S, pat, diff, q, opts, ans, sol, sc=None, t=60):
    return S.q(pat, diff, q, opts, ans, sol, sc, t)


def build_bodmas():
    S = Sub("simp-bodmas")
    S.notes = r"""### What is VBODMAS?
When a long expression has $+, -, \times, \div$, brackets and bars, every calculator (and every examiner) follows one fixed order, called **VBODMAS**:
1. **V — Vinculum**: a bar over an expression, like $\overline{9-7}$, is cleared first.
2. **B — Brackets**: innermost first: $( )$ then $\{ \}$ then $[ ]$.
3. **O — Of**: 'of' means multiply, but it is done **before** ÷ and ×.
4. **D and M**: divisions and multiplications, strictly **left to right**.
5. **A and S**: additions and subtractions, again left to right.

### The 'of' trap
$64 \div 4 \text{ of } 2$ is $64 \div 8 = 8$, **not** $(64 \div 4) \times 2 = 32$.
Compare: $64 \div 4 \times 2 = 16 \times 2 = 32$ — no 'of', so left to right.
Another form: $\frac{3}{4}$ of $48 \div 2$ = $(\frac{3}{4} \times 48) \div 2 = 18$, because 'of' groups $48$ with $\frac{3}{4}$ before any $\div$ outside.

### Working through brackets
Always start from the innermost bracket. A minus sign in front of a bracket **flips every sign** inside: $25 - (10 - 6) = 25 - 10 + 6 = 21$. With three layers, clear $( )$, then $\{ \}$, then $[ ]$, one at a time. Do not try to open all brackets in one go.

### Continued fractions
A fraction written inside a fraction, like $1 + \cfrac{1}{1 + \cfrac{1}{2}}$, is simplified **from the bottom up**:
- bottom: $1 + \frac{1}{2} = \frac{3}{2}$
- next: $\frac{1}{3/2} = \frac{2}{3}$
- top: $1 + \frac{2}{3} = \frac{5}{3}$.

### Left-to-right chains
When only $\div$, $\times$ (and later $+, -$) appear, work strictly left to right: $60 \div 5 \times 3 = 12 \times 3 = 36$, **not** $60 \div 15 = 4$.

### Two speed tools
- **Digit-sum check (casting out 9s):** replace each number by its digit sum (9 becomes 0), do the same operations on the digit sums, and compare with the digit sum of each option. It catches most slips. Example: $48 + 36 = 84$; digit sums $3 + 0 = 3$, and $84 \to 3$ ✓.
- **Last-digit check:** for $\times$ and $+$ chains, the option's last digit must match the last digit you get by working only with last digits. $7 \times 8 + 6 = 62$; last digits $6 + 6 = 12 \to 2$ ✓.

### Approximate placement of values
Some questions ask "what comes in place of ?". Replace the ? by each option only after simplifying the fixed parts — do not solve with algebra when a check of two options is faster.

### Quick revision
- Order: vinculum → brackets → of → ÷/× (L→R) → +/− (L→R).
- 'of' beats ÷ and ×.
- Minus before a bracket flips signs inside.
- Continued fractions: bottom-up.
- Verify with digit sums or last digits.
"""

    S.pattern("simp-bm-p1", r"'of' before ÷ and × (including % of and missing value)", "very common",
        rf"The expression mixes $\div$, $\times$ and 'of' (or '% of'). Often '?' sits in place of one number.",
        rf"a \div b {of} c = a \div (b \times c)",
        rf"""1. Replace every 'of' by a bracket: $4 {of} 3 \to (4 \times 3)$.
2. Then do ÷ and × left to right, then + and −.
3. For a missing value, simplify the rest first and solve the small equation.

Why: 'of' is a multiplication that examiners rank above ÷ and ×.""",
        rf"Evaluate $64 \div 4 {of} 2 + 8 \times 3$.",
        rf"""$4 {of} 2 = 8$; $64 \div 8 = 8$; $8 \times 3 = 24$. Total $8 + 24 = 32$.
(Wrong: $(64 \div 4) \times 2 = 32$ → $56$.)""")
    S.pattern("simp-bm-p2", "Vinculum and three-layer brackets", "very common",
        "An expression with a bar over some digits and ( ), { }, [ ] nested inside each other.",
        None,
        r"""1. Clear the vinculum (bar) first.
2. Then the round bracket, then curly, then square.
3. A minus in front of a bracket flips every sign inside it.

Why: each layer must become a single number before the layer outside it can act.""",
        r"Simplify $25 - [12 - \{8 - (7 - \overline{9 - 5})\}]$.",
        r"Bar: 4. Round: 7 − 4 = 3. Curly: 8 − 3 = 5. Square: 12 − 5 = 7. Answer $25 - 7 = 18$.")
    S.pattern("simp-bm-p3", "Continued (nested) fractions", "common",
        "Fractions stacked inside fractions, often written with cfrac in the paper as small 1s stacked.",
        r"\text{simplify from the bottom upwards}",
        r"""1. Start with the deepest (bottom) fraction and make it a single number.
2. Move one layer up, repeat.
3. The last step gives the value; keep fractions, not decimals.

Why: a fraction line is a division in disguise, and the deepest division must happen first.""",
        r"Find $1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{3}}}$.",
        r"$1+\frac13=\frac43 \to \frac{3}{4} \to 1+\frac34=\frac74 \to \frac47 \to 1+\frac47=\frac{11}{7}$.")
    S.pattern("simp-bm-p4", "Long ÷ × + − chains (left to right)", "very common",
        r"A plain chain like $96 \div 8 \times 4 + 12 \times 2 \div 3 - 10$ with no 'of' and no brackets.",
        r"\div \text{ and } \times \text{ share a level: go left to right}",
        r"""1. Walk through the expression once, left to right.
2. Do only ÷ and × in this pass (as they come).
3. Then do + and − in a second left-to-right pass.

Why: ÷ and × have equal rank; the leftmost one acts first.""",
        r"Simplify $60 \div 5 \times 3 - 18 \div 6 \times 2 + 7$.",
        r"$60 \div 5 = 12$, $\times 3 = 36$; $18 \div 6 = 3$, $\times 2 = 6$; $36 - 6 + 7 = 37$.")
    S.pattern("simp-bm-p5", "Full mixed expression (Tier-2 style, with fractions and %)", "common",
        "A longer question mixing 'of', brackets, a fraction term and a percentage term.",
        r"x\% \text{ of } N = \frac{x}{100} \times N",
        r"""1. Turn 'of' terms into products, percentages into fractions of 100.
2. Simplify each term separately, then combine.
3. Keep fractions (like 3/11 of 1331) exact — they usually divide neatly.

Why: term-by-term simplification avoids one giant unreadable line.""",
        rf"Simplify $\frac{{3}}{{11}}$ ${of}$ $1331 - 25\%$ ${of}$ $160 + 13$.",
        r"$363 - 40 + 13 = 336$.")

    v = F(64, 4 * 2) + 8 * 3 - F(12, 2 * 3)
    assert v == 30
    bodmas_q(S, "simp-bm-p1", "easy",
        rf"Evaluate: $64 \div 4 {of} 2 + 8 \times 3 - 12 \div 2 {of} 3$",
        ["30", "38", "54", "22"], str(v),
        r"""- 'of' first: $4 {of} 2 = 8$ and $2 {of} 3 = 6$.
- $64 \div 8 = 8$; $8 \times 3 = 24$; $12 \div 6 = 2$.
- $8 + 24 - 2 = 30$.""",
        r"Trap 38 comes from reading 'of' as plain ×: $(64 \div 4) \times 2 = 32$, then $32 + 24 - 18 = 38$.", 45)
    v = F(2, 3) * 54 - F(24, 4 * 3)
    assert v == 34
    bodmas_q(S, "simp-bm-p1", "easy",
        rf"Evaluate: $\frac{{2}}{{3}}$ ${of}$ $54 - 24 \div 4 {of} 3$",
        ["34", "18", "30", "26"], str(v),
        rf"""$\frac{{2}}{{3}}$ ${of}$ $54 = 36$; $4 {of} 3 = 12$; $24 \div 12 = 2$. So $36 - 2 = 34$.""",
        r"Trap 18: reading 'of' as plain × gives $24 \div 4 \times 3 = 18$, and $36 - 18 = 18$.", 40)
    v = F(48, 4 * 3) + 4
    assert v == 8
    bodmas_q(S, "simp-bm-p1", "medium",
        rf"What value in place of '?': $48 \div ? {of} 3 + 4 = 8$",
        ["4", "6", "12", "3"], "4",
        rf"""$48 \div ? {of} 3 = 48 \div (? \times 3) = \frac{{48}}{{3 \times ?}}$.
$\frac{{48}}{{3 \times ?}} = 8 - 4 = 4$ → $3 \times ? = 12$ → $? = 4$.""",
        r"Check: $48 \div 4 \text{ of } 3 = 48 \div 12 = 4$, and $4 + 4 = 8$ ✓.", 45)
    v = 7 + 8 - (6 - (5 + 4 - (3 - (9 - 7))))
    assert v == 17
    bodmas_q(S, "simp-bm-p2", "easy",
        r"Simplify: $7 + 8 - [6 - \{5 + 4 - (3 - \overline{9 - 7})\}]$",
        ["17", "13", "15", "9"], str(v),
        r"""Vinculum: $\overline{9-7} = 2$. Bracket: $(3 - 2) = 1$.
Braces: $\{5 + 4 - 1\} = 8$. Square: $[6 - 8] = -2$.
$7 + 8 - (-2) = 17$.""",
        "Minus before $[6 - 8]$ changes it to $+2$.", 50)
    v = 25 - (12 - (8 - (7 - 4)))
    assert v == 18
    bodmas_q(S, "simp-bm-p2", "medium",
        r"Simplify: $25 - [12 - \{8 - (7 - \overline{9 - 5})\}]$",
        ["18", "22", "4", "16"], str(v),
        r"""Vinculum: $9 - 5 = 4$. Round: $(7 - 4) = 3$. Curly: $\{8 - 3\} = 5$. Square: $[12 - 5] = 7$.
$25 - 7 = 18$.""",
        None, 50)
    v = 1 + 1 / (1 + 1 / (1 + F(1, 3)))
    assert v == F(11, 7)
    bodmas_q(S, "simp-bm-p3", "medium",
        r"Find the value of $1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{3}}}$",
        [fr(v), fr(F(8, 5)), fr(F(5, 8)), fr(F(4, 3))], fr(v),
        r"""Bottom-up: $1 + \frac{1}{3} = \frac{4}{3}$ → $\frac{1}{4/3} = \frac{3}{4}$ → $1 + \frac{3}{4} = \frac{7}{4}$.
Then $\frac{1}{7/4} = \frac{4}{7}$, and $1 + \frac{4}{7} = \frac{11}{7}$.""",
        None, 50)
    v = 1 / (1 + 1 / (1 + 1 / (1 + F(1, 2))))
    assert v == F(5, 8)
    bodmas_q(S, "simp-bm-p3", "hard",
        r"Find the value of $1 \div \left(1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{2}}}\right)$",
        [fr(v), fr(F(8, 5)), fr(F(5, 7)), fr(F(3, 5))], fr(v),
        r"""Bottom-up: $1 + \frac{1}{2} = \frac{3}{2}$ → $\frac{2}{3}$ → $1 + \frac{2}{3} = \frac{5}{3}$ → $\frac{3}{5}$ → $1 + \frac{3}{5} = \frac{8}{5}$.
Finally $1 \div \frac{8}{5} = \frac{5}{8}$.""",
        r"The whole $1 + \frac{1}{\dots}$ block sits under the first division.", 60)
    v = F(96, 8) * 4 + 12 * 2 // 3 - 10
    v = F(96, 8) * 4 + F(12 * 2, 3) - 10
    assert v == 46
    bodmas_q(S, "simp-bm-p4", "easy",
        r"Simplify: $96 \div 8 \times 4 + 12 \times 2 \div 3 - 10$",
        ["46", "58", "40", "34"], str(v),
        r"""Left to right: $96 \div 8 = 12$, $12 \times 4 = 48$; $12 \times 2 = 24$, $24 \div 3 = 8$.
$48 + 8 - 10 = 46$.""",
        r"Trap 40: doing $96 \div (8 \times 4)$ — division is only by 8.", 35)
    v = F(60, 5) * 3 - F(18, 6) * 2 + 7
    assert v == 37
    bodmas_q(S, "simp-bm-p4", "easy",
        r"Simplify: $60 \div 5 \times 3 - 18 \div 6 \times 2 + 7$",
        ["37", "33", "41", "25"], str(v),
        r"""Left to right: $60 \div 5 = 12$, $12 \times 3 = 36$; $18 \div 6 = 3$, $3 \times 2 = 6$.
$36 - 6 + 7 = 37$.""",
        r"Trap 25 comes from multiplying before dividing ($60 \div 15 = 4$).", 35)
    v = F(40 * 4, 8) + (12 - (5 * 2 - 6))
    assert v == 28
    bodmas_q(S, "simp-bm-p5", "medium",
        rf"Simplify: $40 {of} 4 \div 8 + [12 - (5 {of} 2 - 6)]$",
        ["28", "20", "42", "24"], str(v),
        rf"""$40 {of} 4 = 160$, then $160 \div 8 = 20$.
Round bracket: $(10 - 6) = 4$. Square: $[12 - 4] = 8$.
$20 + 8 = 28$.""",
        "Trap 20: stopping after the first part.", 50)
    v = F(3, 11) * 1331 - F(25, 100) * 160 + 13
    assert v == 336
    bodmas_q(S, "simp-bm-p5", "medium",
        rf"Simplify: $\frac{{3}}{{11}}$ ${of}$ $1331 - 25\%$ ${of}$ $160 + 13$",
        ["336", "296", "376", "350"], str(v),
        rf"""$\frac{{3}}{{11}}$ ${of}$ $1331 = 363$ (since $1331 = 11^3$, $1331 \div 11 = 121$, $\times 3$).
$25\%$ ${of}$ $160 = 40$. So $363 - 40 + 13 = 336$.""",
        None, 45)
    return S
