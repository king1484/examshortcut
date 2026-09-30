"""Readable rewrite of Reasoning > Analogy (all six subtopics).

Plain English, one idea per section. Every letter shift and every number in an
example is recomputed below and asserted.
Run: python analogy.py  (patches content/core/topics/reasoning/analogy.json in place)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "analogy.json"


# ---------- letter helpers ----------
def P(c):
    """Alphabet position, A = 1 ... Z = 26."""
    return ord(c) - 64


def L(n):
    """Letter for a position, wrapping past Z and before A."""
    return chr((n - 1) % 26 + 65)


def sh(word, ks):
    """Shift each letter by k (int) or by the matching entry of a list."""
    if isinstance(ks, int):
        ks = [ks] * len(word)
    return "".join(L(P(c) + k) for c, k in zip(word, ks))


def diff(a, b):
    """Shift tuple from cluster a to cluster b, in the range -12..+13."""
    return [((P(y) - P(x) + 12) % 26) - 12 for x, y in zip(a, b)]


def opp(word):
    return "".join(L(27 - P(c)) for c in word)


def order(src, dst):
    """1-based positions of src letters as they appear in dst."""
    return [src.index(c) + 1 for c in dst]


def reorder(word, idx):
    return "".join(word[i - 1] for i in idx)


def psum(word):
    return sum(P(c) for c in word)


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


S = {}  # subtopic id -> dict of new fields

# =====================================================================
# 1. analogy-idea
# =====================================================================
assert sh("ACE", 1) == "BDF" and sh("GIK", 1) == "HJL"
assert 3 ** 3 == 27 and 5 ** 3 == 125
assert sh("C", 3) == "F" and sh("H", 3) == "K" and 5 * 2 == 10 and 8 * 2 == 16
assert (2, 4, 8) == (2, 2 ** 2, 2 ** 3) and (3, 9, 27) == (3, 3 ** 2, 3 ** 3)
assert round(64 ** (1 / 3)) ** 3 == 64 and round(64 ** (1 / 3)) == 4
# an-p1: ? : 170 :: 11 : 122 (a^2 + 1)
assert 11 ** 2 + 1 == 122 and 13 ** 2 + 1 == 170
# an-p3: 5 : 26 : 126 :: 7 : 50 : ?
assert (5 ** 2 + 1, 5 ** 3 + 1) == (26, 126) and (7 ** 2 + 1, 7 ** 3 + 1) == (50, 344)
# an-p30: 7 : 51 :: ? : 83 :: 11 : 123 (a^2 + 2)
assert 7 ** 2 + 2 == 51 and 11 ** 2 + 2 == 123 and 9 ** 2 + 2 == 83

S["analogy-idea"] = dict(
    concept=(
        "An analogy question gives one pair and asks you to copy its link. "
        "It is written A : B :: C : ?, read as \"A is to B as C is to what?\". "
        "You are not tested on facts about the words or numbers. "
        "You are tested on one skill: name the link exactly, then use it again in the same direction."
    ),
    notes=r"""### What the question asks
An analogy compares two pairs that share one link. Read the single colon ( : ) as "is to". Read the double colon ( :: ) as "as".

Teacher : School :: Doctor : Hospital. Both pairs say the same thing: *a person and the place where the person works*.

The question hides one term. You find the link in the full pair and use it to fill the gap.

### Say the link as one sentence
This is the whole method. Use it on every analogy.

1. Say the link of the full pair as one short sentence.
2. Check the direction: which term comes first?
3. Use the same sentence, in the same direction, on the other pair.
4. Test all four options. Only one should make a true sentence.

> **Example:** Cow : Calf :: Horse : ? The sentence is "the second is the young one of the first". A young horse is a **foal**. Mare is a trap: it is a female horse, not a young one.

> **Rule:** Keep the direction. If the first pair goes adult → young, the answer pair must also go adult → young.

### The five kinds you will meet
| Kind | Example | What decides the answer |
|---|---|---|
| Word | Pen : Write :: Knife : Cut | meaning or use |
| Letter | ACE : BDF :: GIK : HJL | alphabet positions (+1 here) |
| Number | 3 : 27 :: 5 : 125 | an arithmetic rule (cube here) |
| Mixed | C5 : F10 :: H8 : K16 | a letter rule and a number rule |
| Number set | (2, 4, 8) and (3, 9, 27) | one rule for all three numbers |

Each kind has its own lesson. The method above works for all of them.

### Where the blank can sit
- **At the end:** A : B :: C : ? This is the most common form.
- **At the start or middle:** ? : B :: C : D. Find the rule from the full pair. Then run it backwards. If 5 : 125 is "cube", then ? : 64 asks "which number cubed gives 64?" The answer is 4.
- **Three terms on each side:** A : B : C :: D : E : ? One rule joins all three terms in order.
- **Two blanks:** ? : B :: C : ? Each option gives two terms. Put both in and keep the option where both pairs share the link.
- **Two model pairs:** A : B :: ? : D :: E : F. Two full pairs fix the rule. Find the rule, then fill the middle gap.
- **Pick a pair:** "Select the pair related in the same way as X : Y." Test all four pairs with one sentence.

> **Tip:** When the blank is on the left, undo the rule. Multiply becomes divide. Add becomes subtract. Square becomes square root.

### Sharpen the sentence when two options fit
Setters put options from the same field on purpose. A loose sentence lets two of them through.

Take Thermometer : Temperature :: Odometer : ? The options are Distance, Speed, Kilometre and Car. All four are about vehicles.

- A loose sentence: "related to travel". Too many options pass.
- A sharp sentence: "an instrument and the quantity it measures". Only **distance** passes.
- Speed is measured by a speedometer. A kilometre is only a *unit* of distance.

> **Watch:** If two options still fit, add one more detail: male or female, young or adult, tool or product, unit or quantity.
""",
    formulas=[],
    tricks=[
        {
            "title": "Say the link first, read the options second",
            "body": "Turn the full pair into a sentence before you look at the options. Then test each option with that same sentence. Options that are only from the same field fail the sentence at once.",
            "example": {
                "q": "Doctor : Hospital :: ? (a) Teacher : Student (b) Judge : Court (c) Tailor : Cloth (d) Doctor : Medicine",
                "steps": [
                    "Sentence: \"the second is the place where the first works\".",
                    "Teacher : Student is a person, not a place. Tailor : Cloth is a material. Doctor : Medicine is a thing used.",
                    "Only a court is the place where a judge works.",
                ],
                "answer": "(b) Judge : Court",
            },
        },
    ],
    mistakes=[
        {"wrong": "Picking an option because it is from the same topic (another animal, another instrument).", "right": "Pick the option that makes the same link sentence. Same topic is not enough."},
        {"wrong": "Reversing the direction: the model goes young → adult, the chosen pair goes adult → young.", "right": "Check which term comes first in the model pair and keep that order."},
        {"wrong": "Using one rule for the first pair and a slightly different rule for the second.", "right": "Write the rule once and use exactly that rule on the other pair."},
        {"wrong": "Stopping at the first option that looks right.", "right": "Test all four options. If two pass, make the sentence sharper."},
        {"wrong": "For ? : B :: C : D, applying the rule forwards to B.", "right": "When the blank is on the left, run the rule backwards (divide, subtract, take the root)."},
    ],
    revision=[
        "\":\" means \"is to\"; \"::\" means \"as\".",
        "Say the link as one sentence, then test all four options with it.",
        "Keep the direction: the answer pair must go the same way as the model pair.",
        "Blank on the left: run the rule backwards.",
        "Three-term analogy: one rule links all three terms in order.",
        "Two blanks: both pairs must share the same link.",
        "Two options fit: sharpen the sentence (gender, age, tool, product, unit).",
    ],
    patterns=[
        pat("an-p1", "Missing term in the first or second place (? : B :: C : D)", "common",
            "The question mark is not at the end, e.g. \"? : 64 :: 5 : 125\" or \"Dog : ? :: Horse : Neigh\".",
            r"A = f^{-1}(B)",
            ["Find the rule from the complete pair.", "Write it as a short equation or sentence.",
             "Run it backwards to get the missing term.", "Check your answer by running the rule forwards."],
            "The link is the same in both pairs; only the position of the gap has moved.",
            "Select the number that can replace the question mark. ? : 170 :: 11 : 122. (a) 12 (b) 13 (c) 14 (d) 15",
            [r"$11^2 = 121$ and $121 + 1 = 122$. Rule: square, then add 1.",
             r"Backwards: $170 - 1 = 169$.", r"$169 = 13^2$, so the missing number is 13."],
            "(b) 13"),
        pat("an-p2", "Close options: choose the exact relation", "common",
            "All four options come from the same field (all instruments, all family words). Two or three look right at first.",
            None,
            ["Write the link as a sharp sentence, not \"related to\".", "Test each option with that sentence.",
             "Reject units, tools, materials or places when the link needs a quantity, product or whole."],
            "The setter places same-field options as traps; only the exact relation survives a sharp sentence.",
            "Speedometer : Speed :: Ammeter : ? (a) Voltage (b) Ampere (c) Current (d) Circuit",
            ["Link: an instrument and the quantity it measures.", "An ammeter measures electric current.",
             "Ampere is the unit of current, not the quantity. Voltage is measured by a voltmeter."],
            "(c) Current"),
        pat("an-p3", "Three-term analogy (A : B : C :: D : E : ?)", "occasional",
            "Each side has three terms, e.g. \"2 : 4 : 8 :: 3 : 9 : ?\".",
            r"a : a^2 : a^3",
            ["Find how the 1st term becomes the 2nd.", "Find how the 2nd becomes the 3rd (or how the 1st makes the 3rd).",
             "Check the rule on the full group.", "Apply the same steps to the second group."],
            "Three terms fix the rule more firmly than two, so usually only one option fits.",
            "Select the number that can replace the question mark. 5 : 26 : 126 :: 7 : 50 : ? (a) 343 (b) 344 (c) 350 (d) 345",
            [r"$26 = 5^2 + 1$ and $126 = 5^3 + 1$.", r"Rule: $a,\ a^2 + 1,\ a^3 + 1$.",
             r"Check: $7^2 + 1 = 50$. Then $7^3 + 1 = 343 + 1 = 344$."],
            "(b) 344"),
        pat("an-p4", "Double blank: choose the pair that fills both blanks", "occasional",
            "Two question marks, e.g. \"? : Calf :: Horse : ?\". Each option gives two terms.",
            None,
            ["Put option 1 into both blanks.", "Say the link of each pair.",
             "Keep the option only if both links match, in the same direction.", "Check the other options the same way."],
            "A wrong option usually fits one blank but makes a different link in the other.",
            "? : Puppy :: Cat : ? (a) Dog, Kitten (b) Kennel, Kitten (c) Dog, Mouse (d) Bitch, Tom",
            ["(a) Dog : Puppy is adult : young. Cat : Kitten is adult : young. Both match.",
             "(b) Kennel : Puppy is home : young. It does not match.",
             "(c) and (d) give Cat : Mouse and Cat : Tom, which are not adult : young."],
            "(a) Dog, Kitten"),
        pat("an-p30", "Two model pairs with a gap in the middle (A : B :: ? : D :: E : F)", "common",
            "Three pairs are joined by \"::\" and the gap sits in the middle pair. The question says \"in the same way as the second is related to the first and the sixth to the fifth\".",
            r"B = f(A),\ F = f(E)",
            ["Guess the rule from the first pair.", "Confirm it on the last pair.",
             "Run the rule backwards on D to fill the gap."],
            "Two full pairs leave only one rule that fits both, so there is no guessing.",
            "Select the number that can replace the question mark. 7 : 51 :: ? : 83 :: 11 : 123 (a) 8 (b) 9 (c) 10 (d) 12",
            [r"$7^2 + 2 = 51$ and $11^2 + 2 = 123$. Rule: square, then add 2.",
             r"Backwards on 83: $83 - 2 = 81 = 9^2$."],
            "(b) 9"),
    ],
)

# =====================================================================
# 2. letter-analogy
# =====================================================================
assert [P(c) for c in "EJOTY"] == [5, 10, 15, 20, 25]
assert P("R") == 18 and P("L") == 12 and P("W") == 23
assert all(P(a) + P(b) == 27 for a, b in ["AZ", "BY", "CX", "DW", "EV", "FU", "GT", "HS", "IR", "JQ", "KP", "LO", "MN"])
assert diff("CAT", "FDW") == [3, 3, 3] and sh("PIN", 3) == "SLQ"
assert L(25 + 3) == "B" and L(2 - 3) == "Y"
assert diff("EHKN", "GJMP") == [2, 2, 2, 2]
assert opp("GOLD") == "TLOW"
assert sh("RING"[::-1], 1) == "HOJS"
assert order("PLAY", "LPYA") == [2, 1, 4, 3]
assert diff("DRIVE", "FUMAK") == [2, 3, 4, 5, 6] and sh("PLANT", [2, 3, 4, 5, 6]) == "ROESZ"
# patterns
assert sh("RUXA", 2) == "TWZC"
assert diff("CFIL", "DHLP") == [1, 2, 3, 4] and sh("GJMP", [1, 2, 3, 4]) == "HLPT"
assert opp("IRON") == "RILM"
assert sh("BELL"[::-1], 1) == "MMFC"
assert reorder("GIFT", [2, 1, 4, 3]) == "IGTF"
assert diff("RTVX", "TVXZ") == [2, 2, 2, 2] and sh("GJMP", -2) == "EHKN"
# tricks
assert diff("GKM", "IQN") == [2, 6, 1] and sh("SUX", [2, 6, 1]) == "UAY"
assert P("H") + P("S") == 27 and P("E") + P("V") == 27 and opp("GO") == "TL"
assert "DEB"[::-1] == "BED" and "LAP"[::-1] == "PAL"

S["letter-analogy"] = dict(
    concept=(
        "In a letter analogy the terms are letters or groups of letters, like CAT : FDW. "
        "There is no meaning to find. The link is always a rule about alphabet positions. "
        "Turn letters into numbers (A = 1 ... Z = 26), subtract, and copy the change to the next group."
    ),
    notes=r"""### Letters are numbers
Give each letter its place in the alphabet: A = 1, B = 2 ... Z = 26. Counting from A every time is slow. Learn five anchors instead.

| Letter | E | J | O | T | Y |
|---|---|---|---|---|---|
| Position | 5 | 10 | 15 | 20 | 25 |

Every other letter is a short hop from an anchor. R = T − 2 = 18. L = J + 2 = 12. W = Y − 2 = 23.

> **Tip:** Say "EJOTY" as one word. It gives you 5, 10, 15, 20, 25 in two seconds.

### Opposite letters
Fold the alphabet in the middle. Each letter faces its **opposite letter**. The two positions always add up to 27.

A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N

So the opposite of a letter at position p is at 27 − p. G is 7, and 27 − 7 = 20 = T.

### Subtract slot by slot
Write the positions of the first group. Write the positions of the second group below. Subtract each pair. The list of changes is the **shift pattern**. It is the whole rule.

CAT → FDW: C(3) → F(6) is +3. A(1) → D(4) is +3. T(20) → W(23) is +3. The shift pattern is (+3, +3, +3).

Apply it to PIN: P + 3 = S, I + 3 = L, N + 3 = Q. The answer is **SLQ**.

### Going past Z
After Z the alphabet starts again at A. Going back from A, you land on Z.

- Y + 3: 25 + 3 = 28. Take away 26 to get 2 = **B**.
- B − 3: 2 − 3 = −1. Add 26 to get 25 = **Y**.

> **Rule:** Above 26, subtract 26. Below 1, add 26.

### When the gap is on the left
Sometimes the first group is missing: ? : GJMP :: RTVX : TVXZ. The full pair is on the right. Find its shift pattern. Then apply the pattern backwards: +2 becomes −2.

RTVX → TVXZ is +2 on every letter. So the gap + 2 = GJMP. Go back 2: G − 2 = E, J − 2 = H, M − 2 = K, P − 2 = N. The answer is **EHKN**.

> **Tip:** Undo one letter at a time. Then check your answer by shifting it forwards again.

### The five rules setters use
1. **Same shift for every letter.** EHKN → GJMP is +2 on each letter.
2. **A different shift for each slot.** The changes form a pattern, like (+1, +2, +3, +4). Copy the whole pattern.
3. **Opposite letters.** GOLD → TLOW. Each letter becomes its opposite.
4. **Reversal.** The group is written backwards. It may also be shifted: RING → GNIR → +1 → HOJS.
5. **Rearrangement.** The same letters in a new order. PLAY → LPYA swaps each pair of letters.

### Which rule? Check in this order
1. Does the second group use the **same letters**? Then it is a rearrangement.
2. Read the second group **backwards**. Do you see the first group, or the first group shifted? Then it is reversal.
3. Do the first two letters add up to **27**? Then test opposite letters.
4. Otherwise, subtract slot by slot and read the shift pattern.

> **Example:** DRIVE : FUMAK :: PLANT : ? The shifts are +2, +3, +4, +5, +6 (V + 5 = 27, which wraps to A). Apply them to PLANT: R, O, E, S, Z. The answer is **ROESZ**.
""",
    formulas=[
        {"name": "Shift rule", "tex": r"\text{new position} = \text{old position} + k", "note": "k is the shift. Above 26, subtract 26; below 1, add 26."},
        {"name": "Opposite letter", "tex": r"\text{opposite} = 27 - p", "note": "p is the position. A and Z, or M and N, always add to 27."},
        {"name": "Rising shift", "tex": r"\text{shift of slot } i = i", "note": "Slot 1 moves +1, slot 2 moves +2 and so on, e.g. ABCD → BDFH."},
    ],
    tricks=[
        {
            "title": "Subtract once, then copy the pattern",
            "body": "Write one row of subtractions for the model pair. The pattern you get is the rule. Apply the same pattern to the third group and read the letters with EJOTY.",
            "example": {
                "q": "GKM : IQN :: SUX : ?",
                "steps": ["G(7) → I(9) is +2, K(11) → Q(17) is +6, M(13) → N(14) is +1.",
                          "Pattern (+2, +6, +1). S + 2 = U, U + 6 = 27 → A, X + 1 = Y."],
                "answer": "UAY",
            },
        },
        {
            "title": "Spot opposite letters by the 27 total",
            "body": "If matching letters of the model pair add up to 27, the rule is opposite letters. Then write the opposite of each letter. No counting is needed.",
            "example": {
                "q": "HE : SV :: GO : ?",
                "steps": ["H(8) + S(19) = 27 and E(5) + V(22) = 27, so the rule is opposite letters.",
                          "Opposite of G is T. Opposite of O is L."],
                "answer": "TL",
            },
        },
        {
            "title": "Read the second group backwards",
            "body": "Before any counting, read the second group from right to left. If it gives the first group, the rule is plain reversal.",
            "example": {
                "q": "DEB : BED :: LAP : ?",
                "steps": ["BED read backwards is DEB, so the rule is reversal with no shift.",
                          "LAP read backwards is PAL."],
                "answer": "PAL",
            },
        },
    ],
    mistakes=[
        {"wrong": "Writing position 29 as a letter after adding 3 to Z's 26.", "right": "Subtract 26 above 26: 29 − 26 = 3 = C."},
        {"wrong": "Treating (+1, +2, +3) as \"about +2\" and shifting every letter by 2.", "right": "Check every slot and copy the full shift pattern slot by slot."},
        {"wrong": "Confusing opposite letters with a shift of 13.", "right": "Opposite letters add to 27 (A-Z). A shift of 13 sends A to N. Test the 27 total first."},
        {"wrong": "Counting from A for every letter and losing time.", "right": "Use EJOTY anchors: E5, J10, O15, T20, Y25, then hop one or two places."},
        {"wrong": "For a reverse-plus-shift rule, shifting first and reversing second in a different order than the model.", "right": "Keep the same two steps in the same order on the new group."},
    ],
    revision=[
        "EJOTY: E5, J10, O15, T20, Y25.",
        "Opposite letters add to 27: A-Z, B-Y ... M-N.",
        "Subtract slot by slot; the shift pattern is the rule.",
        "Above 26 subtract 26; below 1 add 26.",
        "Same letters in a new order: rearrangement. Backwards: reversal (maybe plus a shift).",
        "Blank on the left: apply the shift pattern backwards.",
    ],
    patterns=[
        pat("an-p5", "Same shift for every letter", "very common",
            "Every letter of the second group is the same number of places ahead of (or behind) the matching letter of the first group.",
            r"\text{new} = \text{old} + k",
            ["Subtract positions slot by slot (use EJOTY).", "Confirm every change is the same number k.",
             "Add k to every letter of the third group.", "Wrap past Z if needed."],
            "The whole group moves as one block, so one number describes the rule.",
            "Select the letter-cluster that can replace the question mark. EHKN : GJMP :: RUXA : ? (a) TWZB (b) TWZC (c) SVYB (d) TVZC",
            ["E → G, H → J, K → M, N → P: each is +2.", "R → T, U → W, X → Z, A → C."],
            "(b) TWZC"),
        pat("an-p6", "A different shift for each slot", "common",
            "The changes are not equal but form a pattern: +1, +2, +3, +4 or +2, −1, +2, −1.",
            None,
            ["Write the full shift pattern from the model pair.", "Do not round or average it.",
             "Give slot 1 its shift, slot 2 its shift, and so on."],
            "The rule belongs to the slot in the group, not to the letter in it.",
            "CFIL : DHLP :: GJMP : ? (a) HLPT (b) HKOS (c) ILPT (d) HLOT",
            ["C → D is +1, F → H is +2, I → L is +3, L → P is +4.",
             "G + 1 = H, J + 2 = L, M + 3 = P, P + 4 = T."],
            "(a) HLPT"),
        pat("an-p7", "Opposite-letter analogy", "common",
            "Matching letters of the model pair add up to 27 (G + T, O + L). Sometimes the result is also written backwards.",
            r"\text{opposite} = 27 - p",
            ["Add the positions of one matching pair. A total of 27 means opposite letters.",
             "Replace each letter of the third group by its opposite.",
             "If the model was also reversed, reverse your answer too."],
            "Opposite letters are a fixed swap table, so no counting is needed once you spot it.",
            "GOLD : TLOW :: IRON : ? (a) RILN (b) RJLM (c) RILM (d) SILM",
            ["G(7) + T(20) = 27, so the rule is opposite letters.",
             "I ↔ R, R ↔ I, O ↔ L, N ↔ M."],
            "(c) RILM"),
        pat("an-p8", "Reversal and reverse-plus-shift", "common",
            "Reading the second group backwards gives the first group, or gives it with every letter moved by the same step.",
            None,
            ["Reverse the second group and compare it with the first.",
             "Same letters means plain reversal. All letters off by k means reverse, then shift by k.",
             "Do the same two steps, in the same order, on the third group."],
            "Reversal changes the order and the shift changes the letters, so the two steps can be checked one at a time.",
            "RING : HOJS :: BELL : ? (a) MMFC (b) LLEB (c) CFMM (d) MMFD",
            ["RING backwards is GNIR. Each letter + 1 gives HOJS.",
             "BELL backwards is LLEB. Each letter + 1 gives MMFC."],
            "(a) MMFC"),
        pat("an-p9", "Rearrangement (same letters, new order)", "occasional",
            "The second group has exactly the same letters as the first, only in a new order.",
            None,
            ["Number the letters of the first group 1, 2, 3 ...",
             "Write the order they appear in the second group (e.g. 2-1-4-3).",
             "Rearrange the third group in the same order."],
            "The rule is a fixed map of places, so the letters themselves do not matter.",
            "PLAY : LPYA :: GIFT : ? (a) IGFT (b) GITF (c) IGTF (d) TFIG",
            ["PLAY is 1-2-3-4. LPYA is the order 2-1-4-3: each pair is swapped.",
             "GIFT in the order 2-1-4-3 is I, G, T, F."],
            "(c) IGTF"),
        pat("an-p31", "Missing first group: run the rule backwards", "common",
            "The gap is on the left, e.g. \"? : GJMP :: RTVX : TVXZ\". The full pair is on the other side.",
            None,
            ["Find the shift pattern from the full pair.", "Reverse every sign: +2 becomes −2.",
             "Apply the reversed pattern to the known partner of the gap.", "Check by shifting your answer forwards."],
            "Moving forwards and moving backwards are the same rule, so undoing it finds the start.",
            "Select the letter-cluster that can replace the question mark. ? : GJMP :: RTVX : TVXZ (a) EHKN (b) FIKO (c) EHLN (d) IKOR",
            ["R → T, T → V, V → X, X → Z: each is +2.", "So the gap + 2 = GJMP. Go back 2 from each letter.",
             "G − 2 = E, J − 2 = H, M − 2 = K, P − 2 = N."],
            "(a) EHKN"),
    ],
)

# =====================================================================
# 3. word-analogy (facts kept exactly as in the current notes)
# =====================================================================
S["word-analogy"] = dict(
    concept=(
        "A word analogy gives a pair of real words, like Chef : Kitchen, and asks for a pair with the same link. "
        "The exam uses a small bank of links again and again. "
        "Learn the bank, say the link as a sentence, and test every option with it."
    ),
    notes=r"""### What a word analogy asks
You get a pair such as **Chef : Kitchen** and a third word. Find the word that has the same link with the third word.

A chef works in a kitchen. So Pilot : ? needs the place where a pilot works: the cockpit.

### The two-question test
Ask two questions about every option.

1. **Is it the same kind of link?** Both pairs must be, say, "worker and workplace".
2. **Is it the same exact link, in the same direction?** "A pilot flies an aeroplane" is a different link. Reject it.

> **Rule:** Say the link out loud as a sentence. Then say the same sentence with each option. Only one sentence should be true.

### The relation bank
| Link | Examples |
|---|---|
| Worker : tool | Surgeon : Scalpel, Mason : Trowel, Woodcutter : Axe, Tailor : Needle |
| Worker : place of work | Chef : Kitchen, Judge : Court, Scientist : Laboratory |
| Worker : product | Poet : Poem, Cobbler : Shoes, Weaver : Cloth, Composer : Symphony |
| Adult : young one | Cow : Calf, Horse : Foal, Goat : Kid, Deer : Fawn, Frog : Tadpole |
| Animal : sound | Lion : Roar, Donkey : Bray, Frog : Croak, Horse : Neigh, Owl : Hoot |
| Animal : home | Lion : Den, Bee : Hive, Horse : Stable, Dog : Kennel, Pig : Sty |
| Male : female | Lion : Lioness, Peacock : Peahen, Drake : Duck, Ram : Ewe |
| Individual : group | Fish : Shoal, Wolf : Pack, Lion : Pride, Cattle : Herd, Ship : Fleet |
| Country : currency | India : Rupee, Japan : Yen, Thailand : Baht, Bangladesh : Taka |
| Country : capital | Nepal : Kathmandu, Bhutan : Thimphu, Egypt : Cairo, Canada : Ottawa |
| Instrument : quantity measured | Barometer : Pressure, Hygrometer : Humidity, Anemometer : Wind speed |
| Unit : quantity | Newton : Force, Pascal : Pressure, Joule : Energy, Ampere : Current |
| Study : subject | Ornithology : Birds, Ichthyology : Fishes, Entomology : Insects |
| Product : raw material | Glass : Sand, Paper : Wood, Butter : Milk, Jaggery : Sugarcane |
| Part : whole | Petal : Flower, Page : Book, Player : Team |
| Tool : action | Needle : Sew, Spade : Dig, Knife : Cut, Pen : Write |
| Cause : effect | Rain : Flood, Drought : Famine, Virus : Disease |
| Same meaning | Begin : Commence, Abandon : Desert |
| Opposite meaning | Ancient : Modern, Scarce : Abundant |
| Degree (mild : strong) | Warm : Hot, Breeze : Gale, Smile : Laugh |

### Keep the same type of word
Many traps are the right topic but the wrong type of word.

- **Unit, quantity or instrument.** Pascal is a unit. Pressure is a quantity. A barometer is an instrument.
- **Tool, material or product.** For a weaver, the loom is the tool. Thread is the material. Cloth is the product.
- **Young or female.** A foal is a young horse. A mare is a female horse.
- **Same or opposite meaning.** A synonym pair needs a synonym answer, not an antonym.

> **Watch:** Every worker has a tool, a place and a product. The setter puts the other two in the options as traps.

### Keep the direction
Warm : Hot goes from mild to strong. So Breeze : **Gale**, not Gale : Breeze.

Butter : Milk goes from product to material. So Jaggery : **Sugarcane**, not Sugarcane : Jaggery.

> **Example:** Cobbler : Shoes :: Weaver : ? (Loom / Cloth / Thread / Tailor). A cobbler makes shoes, so the link is worker : product. A weaver makes **cloth**. Loom is the tool and thread is the material.
""",
    formulas=[],
    tricks=[
        {
            "title": "Two ticks on every option",
            "body": "Give each option a tick for \"same kind of link\" and a tick for \"same exact link, same direction\". The option with two ticks is the answer.",
            "example": {
                "q": "Author : Novel :: ? (a) Poet : Poem (b) Editor : Newspaper (c) Reader : Library (d) Book : Print",
                "steps": ["Link: a person and the work the person creates.",
                          "Editor : Newspaper: an editor does not write the whole paper. Reader : Library is a person and a place. Book : Print is a thing and a process.",
                          "Poet : Poem gets both ticks."],
                "answer": "(a) Poet : Poem",
            },
        },
        {
            "title": "Tag animal pairs before reading options",
            "body": "For an animal pair, first tag it: adult : young, male : female, or animal : home, sound or group. Options often mix a young one with a female.",
            "example": {
                "q": "Drake : Duck :: ? (a) Horse : Mare (b) Bull : Ox (c) Ram : Ewe (d) Dog : Pup",
                "steps": ["Tag: male : female of the same animal.",
                          "Dog : Pup is adult : young. Bull : Ox is not male : female.",
                          "Horse is the general word, not the male. Ram : Ewe is male : female of sheep."],
                "answer": "(c) Ram : Ewe",
            },
        },
    ],
    mistakes=[
        {"wrong": "Choosing an option from the same topic (both medical, both animals).", "right": "Topics are decoys. Match the link sentence, not the topic."},
        {"wrong": "Missing the direction: taking Food : Hunger for Hunger : Food.", "right": "Say which word comes first in the model and keep that order."},
        {"wrong": "Mixing a unit with a quantity (Pascal for Pressure).", "right": "Name the type of each word (unit, quantity, instrument) and keep the same types."},
        {"wrong": "Picking the tool or raw material when the link is worker : product.", "right": "Decide first: tool, place or product. Then reject the other two."},
        {"wrong": "Adding a condition the pair does not state (\"a judge also works in chambers\").", "right": "Use the main, standard link that most people would name."},
    ],
    revision=[
        "Say the link as a sentence; test every option with the same sentence.",
        "Worker links: tool, place of work, product.",
        "Animal links: young one, sound, home, group, male : female.",
        "Keep word types the same: unit, quantity, instrument; tool, material, product.",
        "Keep the direction: mild : strong, product : material, whole : part.",
        "Synonym model needs a synonym answer; antonym model needs an antonym.",
    ],
    patterns=[
        pat("an-p10", "Worker : tool / workplace / product", "very common",
            "The first word is a person with a job (mason, cobbler, author, pilot).",
            None,
            ["Decide which link it is: tool used, place of work, or thing made.",
             "Find the same link for the new worker.",
             "Reject options that are one of the other two links."],
            "Every worker has a tool, a place and a product, and the setter uses the other two as traps.",
            "Cobbler : Shoes :: Weaver : ? (a) Loom (b) Cloth (c) Thread (d) Tailor",
            ["A cobbler makes shoes: worker : product.", "A weaver makes cloth.",
             "Loom is the tool and thread is the raw material."],
            "(b) Cloth"),
        pat("an-p11", "Animal : young one / sound / home / group", "very common",
            "One word is an animal or bird. The other is its baby, its cry, its shelter or its group name.",
            None,
            ["Name which animal fact is used.", "Recall the same fact for the new animal.",
             "Reject a different fact about the same animal (sound instead of home)."],
            "Each animal has one standard word for each fact, so only one option fits the chosen fact.",
            "Lion : Den :: Bee : ? (a) Honey (b) Hive (c) Swarm (d) Buzz",
            ["A den is the lion's home.", "A bee's home is a hive.",
             "Honey is what it makes, swarm is its group, buzz is its sound."],
            "(b) Hive"),
        pat("an-p12", "Country : currency / capital", "common",
            "A country is paired with its money or its capital city.",
            None,
            ["See whether the model pair is currency or capital.", "Recall the same for the new country.",
             "The other options are real currencies or capitals of other countries, so be exact."],
            "Only one option belongs to the given country.",
            "India : Rupee :: Thailand : ? (a) Yuan (b) Baht (c) Ringgit (d) Dong",
            ["Rupee is the currency of India.", "The currency of Thailand is the baht.",
             "Yuan is China's, ringgit is Malaysia's and dong is Vietnam's."],
            "(b) Baht"),
        pat("an-p13", "Instrument or unit : quantity", "common",
            "A measuring instrument (barometer, hygrometer) or a unit (newton, pascal) is paired with what it measures.",
            None,
            ["Name the type of each word: instrument, unit or quantity.",
             "Keep the same types for the answer.", "Recall the fact."],
            "The traps are usually a unit where a quantity is needed, or a nearby quantity.",
            "Newton : Force :: Pascal : ? (a) Power (b) Pressure (c) Energy (d) Current",
            ["The newton is the unit of force.", "The pascal is the unit of pressure.",
             "Power, energy and current have other units (watt, joule, ampere)."],
            "(b) Pressure"),
        pat("an-p14", "Study : subject, product : raw material, part : whole", "common",
            "A \"-logy\" science, or a product and what it is made from, or a small part and the whole thing.",
            None,
            ["Name the link: \"is the study of\", \"is made from\" or \"is a part of\".",
             "Apply it to the third word.", "Watch the direction: product → material, not material → product."],
            "Once the direction is fixed, each of these links has one clear answer.",
            "Butter : Milk :: Jaggery : ? (a) Sugar (b) Sugarcane (c) Sweet (d) Tea",
            ["Butter is made from milk: product : raw material.",
             "Jaggery is made from sugarcane.", "Sugar is another product, not the raw material."],
            "(b) Sugarcane"),
        pat("an-p15", "Same meaning, opposite meaning and degree", "common",
            "Two ordinary words that mean the same, the opposite, or a milder and a stronger form of one idea.",
            None,
            ["Decide: same meaning, opposite meaning, or mild → strong.",
             "Find the option with that link to the third word.",
             "Reject the option with the other type (an opposite when a same-meaning word is needed)."],
            "The setter usually places one same-meaning word and one opposite word among the options.",
            "Warm : Hot :: Breeze : ? (a) Air (b) Gale (c) Calm (d) Rain",
            ["Hot is a stronger form of warm.", "A stronger form of a breeze is a gale.",
             "Calm is the opposite; air is only the general word."],
            "(b) Gale"),
        pat("an-p16", "Tool : action and cause : effect", "common",
            "An object and what it is used to do (needle : sew), or an event and what it leads to (rain : flood).",
            None,
            ["Say \"X is used to ...\" or \"X leads to ...\".",
             "Complete the same sentence for the third word.",
             "Reject places, users and materials linked to the object."],
            "The answer must be an action or a result, which removes the noun traps quickly.",
            "Needle : Sew :: Spade : ? (a) Garden (b) Dig (c) Soil (d) Farmer",
            ["A needle is used to sew.", "A spade is used to dig.",
             "Garden is a place, soil is what is dug, farmer is the user."],
            "(b) Dig"),
        pat("an-p32", "Male : female", "common",
            "Both words name the same animal (or person), one male and one female: Drake : Duck, Ram : Ewe.",
            None,
            ["Check that the model is male : female, not adult : young.",
             "Note which comes first, male or female.", "Find the female (or male) of the new animal."],
            "Young-one and home words for the same animal are placed as traps; only the gender word fits.",
            "Gander : Goose :: Fox : ? (a) Cub (b) Vixen (c) Den (d) Pack",
            ["A gander is a male goose: male : female.", "A female fox is a vixen.",
             "Cub is the young one, den is the home, pack is a group."],
            "(b) Vixen"),
    ],
)

# =====================================================================
# 4. number-analogy
# =====================================================================
assert 4 * 5 == 20 and 7 * 5 == 35
assert 9 * 4 + 4 == 40 and 13 * 4 + 4 == 56
assert 6 ** 2 - 1 == 35 and 9 ** 2 - 1 == 80
assert 4 ** 3 + 1 == 65 and 5 ** 3 + 1 == 126
assert 4 * 7 == 28 and (3 + 6) ** 2 == 81
assert 4 * 5 == 20 and 6 * 7 == 42 and 8 * 9 == 72
assert 7 * 3 + 2 == 23 and 7 * 2 + 9 == 23 and 11 * 3 + 2 == 35 and 11 * 2 + 9 == 31
assert 8 * 9 == 72 and 12 * 13 == 156 and 12 ** 2 == 144 and 12 * 11 == 132
assert 7 ** 2 == 49 and 9 ** 2 == 81 and 8 ** 2 != 60
# patterns
assert 5 * 9 == 45 and 5 + 9 == 14
assert 13 * 3 + 2 == 41 and 17 * 3 + 2 == 53 and 15 * 3 + 2 != 44 and 19 * 3 + 2 != 55 and 21 * 3 + 2 != 62
assert 14 ** 2 == 196 and 14 + 2 == 16 and 18 ** 2 == 324 and 18 + 2 == 20
assert next_prime(19) == 23 and next_prime(23) == 29 and not is_prime(27) and not is_prime(25)
assert 19 + 4 == 23 and 23 + 4 == 27   # the +4 trap gives a non-prime
# tricks
assert 7 ** 2 + 1 == 50 and 9 ** 2 + 1 == 82
assert 6 * 7 == 42 and 8 * 9 == 72
assert 12 * 4 + 1 == 49

S["number-analogy"] = dict(
    concept=(
        "In a number analogy the first pair hides one arithmetic rule. "
        "You find that rule and apply it to the third number. "
        "Most rules are simple: multiply and add, square or cube, or work on the digits. "
        "Always check the rule on the model pair before you use it."
    ),
    notes=r"""### What a number analogy asks
You get a pair like **4 : 20** and a third number, say 7. Find the rule that turns 4 into 20. Use it on 7.

Here 20 = 4 × 5. So 7 × 5 = **35**.

### Step one: the size test
Compare the second number with the first. The size tells you which rule to try first.

| What you see | Try first |
|---|---|
| A little bigger | add, or × 2 ± a small number |
| About k times bigger | × k ± r |
| Close to the square of the first | a² ± r, a(a + 1), (a + 1)² |
| Very large | a³ ± r |
| Smaller than the first | square root, cube root, ÷ k |
| Two-digit numbers, small answer | digit sum or digit product |

> **Tip:** Here a is the first number of the pair, r a small number and k a multiplier.

### Know squares and cubes by heart
Squares 1 to 20: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400.

Cubes 1 to 12: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728.

When you see 35, think 36 − 1. When you see 126, think 125 + 1. When you see 72, think 8 × 9.

### The rule bank
1. **Multiply and add:** 9 : 40 is 9 × 4 + 4. So 13 gives 13 × 4 + 4 = 56.
2. **Square based:** 6 : 35 is 6² − 1. So 9 gives 80.
3. **Cube based:** 4 : 65 is 4³ + 1. So 5 gives 126.
4. **Product form:** 8 : 72 is 8 × 9, a number times the next number.
5. **Digit based:** product of digits (47 gives 28), square of the digit sum (36 gives 81), digits reversed (34 gives 43).
6. **Two model pairs:** 4 : 20 :: 6 : 42 :: 8 : ? Here 4 × 5 and 6 × 7, so 8 × 9 = 72.

### Why you must check the options
One pair can fit two rules. 7 : 23 fits 7 × 3 + 2. It also fits 7 × 2 + 9. For 11 these give 35 and 31.

The setter keeps only one of them in the options. So:
- Find the simplest rule and work out the answer.
- If the answer is **not** in the options, try the next family. Do not force it.
- If two model pairs are given, the rule must fit **both**.

> **Rule:** Before you use a rule, check it gives the second number of the model pair exactly.

### The whole-number note
Many papers add a note: "operations should be performed on the whole numbers, without breaking them into digits". When you see it, **do not** use digit sums or digit products. Use only +, −, ×, ÷, squares and cubes of the full number.

> **Example:** 8 : 72 :: 12 : ? Here 72 = 8 × 9, a number times the next number. So 12 × 13 = **156**. The traps are 144 (just 12²) and 132 (12 × 11).

### Pair-selection questions
"Select the pair related in the same way as 7 : 49." Here 49 = 7², so the rule is square.

Test all four option pairs with the square rule. 9 : 81 fits, because 81 = 9². A near miss like 8 : 60 fails, because 8² = 64. Compute each pair fully before you mark.

> **Watch:** The traps pass a quick glance. Only a full check catches them.
""",
    formulas=[
        {"name": "Multiply-and-add rule", "tex": r"b = k a + r", "note": "a is the first number, b the second. Find k and r from the model pair, then check."},
        {"name": "Square family", "tex": r"b = a^2 \pm r,\ a(a+1),\ (a+1)^2", "note": "Try these when b is close to the square of a."},
        {"name": "Digit rules", "tex": r"b = \text{digit sum},\ \text{digit product},\ (\text{digit sum})^2", "note": "Not allowed when the whole-number note is given."},
    ],
    tricks=[
        {
            "title": "The size test picks the family",
            "body": "Compare b with a before anything else. A few times a: multiply and add. Near a squared: square family. Very large: cubes. Smaller: roots or digit rules.",
            "example": {
                "q": "7 : 50 :: 9 : ?",
                "steps": [r"50 is close to $7^2 = 49$, so the rule is square + 1.", r"$9^2 + 1 = 82$."],
                "answer": "82",
            },
        },
        {
            "title": "Check the rule on the model pair",
            "body": "Whatever rule you guess, make sure it gives b from a exactly. The check takes two seconds and prevents most wrong answers.",
            "example": {
                "q": "6 : 42 :: 8 : ?",
                "steps": [r"Guess a number times the next: $6 \times 7 = 42$. It checks.", r"$8 \times 9 = 72$."],
                "answer": "72",
            },
        },
    ],
    mistakes=[
        {"wrong": "Using a rule that nearly fits (12 : 49 read as 12 × 4).", "right": "The rule must give the exact number: 12 × 4 + 1 = 49."},
        {"wrong": "Using squares for the model pair and cubes for the new number.", "right": "Use exactly the same rule on both pairs."},
        {"wrong": "Using digit sums when the whole-number note is printed.", "right": "With that note, use only operations on the full number."},
        {"wrong": "Forcing a rule when the answer is not in the options.", "right": "If your answer is missing, try the next family in the size table."},
        {"wrong": "Missing a simple reversal: 27 : 72 read as × 2 + 18.", "right": "If the digits are just swapped, the rule is reversal. Prefer the simpler rule."},
    ],
    revision=[
        "Size test first: a little bigger, k times, near a square, very large, or smaller.",
        "Know squares to 20 and cubes to 12.",
        r"Common forms: $ka + r$, $a^2 \pm r$, $a^3 \pm r$, $a(a+1)$.",
        "Check the rule on the model pair before using it.",
        "Answer not in the options: change the family.",
        "Whole-number note: no digit tricks.",
    ],
    patterns=[
        pat("an-p17", "Multiply and add: b = k × a ± r", "very common",
            "The second number is a few times the first, plus or minus a small number (7 : 23, 9 : 40).",
            r"b = k\,a + r",
            ["Divide b by a to guess k.", "Find r = b − k × a.",
             "Apply k × c + r to the third number.", "Check the answer is in the options."],
            "Most setters build number pairs with one multiplication and one small addition.",
            "Select the number that can replace the question mark. 9 : 40 :: 13 : ? (a) 52 (b) 54 (c) 56 (d) 60",
            [r"$9 \times 4 = 36$ and $36 + 4 = 40$. Rule: × 4, then + 4.", r"$13 \times 4 + 4 = 52 + 4 = 56$."],
            "(c) 56"),
        pat("an-p18", "Square or cube based rule", "very common",
            "The second number is close to a square or a cube of the first (6 : 35, 4 : 65, 8 : 72).",
            r"b = a^2 \pm r,\ a^3 \pm r,\ a(a+1)",
            ["Compare b with a² and a³.", "Note the gap (35 = 36 − 1) or the product form (72 = 8 × 9).",
             "Apply the same form to the third number."],
            "Squares and cubes grow fast, so a big jump almost always means a power.",
            "6 : 35 :: 9 : ? (a) 81 (b) 80 (c) 82 (d) 72",
            [r"$6^2 = 36$ and $36 - 1 = 35$. Rule: square, then − 1.", r"$9^2 - 1 = 80$."],
            "(b) 80"),
        pat("an-p19", "Digit rule (sum, product, reversal)", "common",
            "Two-digit numbers where the second number is small, or looks like the digits rearranged (47 : 28, 36 : 81, 34 : 43). No whole-number note is given.",
            None,
            ["Try the digit product and the digit sum.", "Try the square of the digit sum.",
             "Try reversing the digits.", "Use this family only when the whole-number note is absent."],
            "Digit rules explain pairs that no multiply-and-add rule can.",
            "47 : 28 :: 59 : ? (a) 14 (b) 45 (c) 95 (d) 54",
            [r"$4 \times 7 = 28$: the product of the digits.", r"$5 \times 9 = 45$. (14 is the digit-sum trap.)"],
            "(b) 45"),
        pat("an-p20", "Select the number pair with the same relation", "common",
            "\"Select the option in which the numbers share the same relationship as 13 : 41.\" The options are complete pairs.",
            r"b = f(a)",
            ["Find the rule of the model pair.", "Test all four option pairs with it.",
             "If two pairs fit, look for a sharper rule that fits the model and only one option."],
            "The traps are near misses (off by 1 to 3), which a full calculation catches.",
            "Select the pair related in the same way as 13 : 41. (a) 17 : 53 (b) 15 : 44 (c) 19 : 55 (d) 21 : 62",
            [r"$13 \times 3 + 2 = 41$. Rule: × 3, then + 2.",
             r"$17 \times 3 + 2 = 53$ fits. 15, 19 and 21 would need 47, 59 and 65."],
            "(a) 17 : 53"),
        pat("an-p33", "Second number smaller: root or division", "common",
            "The second number is smaller than the first and the first is a perfect square or cube (196 : 16, 343 : 7).",
            r"b = \sqrt{a} \pm r,\ \sqrt[3]{a},\ a \div k",
            ["Check if the first number is a square or a cube.", "Take the root and compare it with b.",
             "Note any ± r.", "Apply the same steps to the third number."],
            "A root is the reverse of a square, so perfect squares and cubes in the first place point straight to it.",
            "196 : 16 :: 324 : ? (a) 18 (b) 20 (c) 22 (d) 16",
            [r"$\sqrt{196} = 14$ and $14 + 2 = 16$. Rule: square root, then + 2.",
             r"$\sqrt{324} = 18$ and $18 + 2 = 20$."],
            "(b) 20"),
        pat("an-p34", "Next prime number", "occasional",
            "Both numbers of the model pair are prime, and no other prime lies between them (19 : 23, 29 : 31).",
            None,
            ["Check that both model numbers are prime.", "Check that no prime lies between them.",
             "Find the next prime after the third number."],
            "A fixed gap like + 4 breaks as soon as it lands on a non-prime, so the prime rule is the only one that holds.",
            "19 : 23 :: 23 : ? (a) 25 (b) 27 (c) 29 (d) 31",
            ["19 and 23 are prime, and 20, 21, 22 are not. Rule: the next prime.",
             "After 23: 24, 25, 26, 27, 28 are not prime. 29 is prime.",
             "The + 4 trap gives 27, which is 3 × 9."],
            "(c) 29"),
    ],
)

# =====================================================================
# 5. number-set-analogy
# =====================================================================
def chain(a, k, r):
    b = k * a + r
    return (a, b, k * b + r)


assert chain(6, 2, 1) == (6, 13, 27) and chain(8, 2, 1) == (8, 17, 35)
assert 4 + 5 == 9 and 9 * 3 == 27
assert 3 * 8 == 24 and 4 ** 2 + 5 ** 2 == 41 and 2 * (5 + 9) == 28
assert (3 ** 2 + 1, 3 ** 3 + 1) == (10, 28) and 7 + 7 ** 2 == 56
assert 5 * 7 == 35 and (8 + 18) // 2 == 13 and 5 + 9 == 14
# speed-check numbers
assert [n * n + 1 for n in (5, 6, 7, 8)] == [26, 37, 50, 65]
assert [n ** 3 + 1 for n in (3, 4, 5)] == [28, 65, 126]
# worked example
assert 4 ** 2 + 5 ** 2 == 41 and 3 ** 2 + 7 ** 2 == 58
ex = [(2, 6, 40), (5, 4, 40), (6, 3, 36), (1, 8, 64)]
assert [a * a + b * b == c for a, b, c in ex] == [True, False, False, False]
# patterns
opts = [(5, 11, 23), (7, 15, 30), (9, 19, 38), (4, 9, 20)]
assert [chain(a, 2, 1) == (a, b, c) for a, b, c in opts] == [True, False, False, False]
opts = [(7, 4, 28), (6, 5, 32), (9, 3, 36), (8, 2, 18)]
assert (3 * 8, 5 * 6) == (24, 30) and [a * b == c for a, b, c in opts] == [True, False, False, False]
opts = [(5, 26, 126), (6, 37, 215), (2, 5, 8), (7, 50, 342)]
assert (4 ** 2 + 1, 4 ** 3 + 1) == (17, 65)
assert [(a * a + 1, a ** 3 + 1) == (b, c) for a, b, c in opts] == [True, False, False, False]
opts = [(6, 48, 8), (3, 24, 9), (7, 56, 9), (2, 18, 8)]
assert (5 * 7, 4 * 9) == (35, 36) and [a * c == b for a, b, c in opts] == [True, False, False, False]
opts = [(18, 11, 28), (16, 10, 20), (25, 19, 20), (14, 6, 36)]
assert ((15 - 9) * 4, (20 - 13) * 4) == (24, 28)
assert [(a - b) * 4 == c for a, b, c in opts] == [True, False, False, False]
# trick
opts = [(4, 16, 60), (5, 25, 125), (6, 36, 206), (7, 49, 334)]
assert [(a * a, a ** 3) == (b, c) for a, b, c in opts] == [False, True, False, False]

S["number-set-analogy"] = dict(
    concept=(
        "You are shown two or more sets of three numbers, such as (6, 13, 27) and (8, 17, 35). "
        "One hidden rule links the numbers inside every set. "
        "Find that rule, check it on every set, then pick the option set that follows it. "
        "Most papers say to use whole numbers only, so digit tricks are not allowed."
    ),
    notes=r"""### What the question looks like
You see sets like (6, 13, 27) and (8, 17, 35). The same rule links the three numbers in each set. You pick the option set that follows the same rule.

The question usually has a note. It says to work on **whole numbers** only. For 13, you may add, subtract or multiply 13. You may not break it into 1 and 3.

> **Rule:** With the whole-number note, use only +, −, ×, ÷, squares and cubes of full numbers. No digit sums.

### Family one: a chain
The same step turns the 1st number into the 2nd, and the 2nd into the 3rd.

(6, 13, 27): 6 × 2 + 1 = 13, and 13 × 2 + 1 = 27. Check (8, 17, 35): 8 × 2 + 1 = 17, and 17 × 2 + 1 = 35.

The two steps can also differ: (4, 9, 27) is + 5, then × 3.

### Family two: the third from the first two
The first two numbers are the inputs. The third is the output.

- Product: (3, 8, 24), since 3 × 8 = 24.
- Sum of squares: (4, 5, 41), since 16 + 25 = 41.
- Twice the sum: (5, 9, 28), since 2 × 14 = 28.
- Difference times k: (15, 9, 24), since (15 − 9) × 4 = 24.

### Family three: powers
The numbers are powers of the first, or close to them.

- (2, 4, 8) is a, a², a³.
- (3, 10, 28) is a, a² + 1, a³ + 1.
- (7, 49, 56) is a, a², a + a².

> **Tip:** 26, 37, 50, 65 are squares + 1. 28, 65, 126 are cubes + 1. Spot them on sight.

### Family four: the middle links the outer two
- (5, 35, 7): the middle is the product, 5 × 7 = 35.
- (8, 13, 18): the middle is the average of 8 and 18.
- (14, 5, 9): the first is the sum of the other two.

### Method
1. Take the first model set. Try a chain: does one step work twice?
2. If not, try the third from the first two: sum, product, sum of squares, difference × k.
3. If not, try powers, then the middle-link family.
4. **Check the rule on the second model set.** A rule that fits one set only is wrong.
5. Test the options. Exactly one fits.

> **Example:** Sets (4, 5, 41) and (3, 7, 58). A chain fails. Sum of squares works: 16 + 25 = 41 and 9 + 49 = 58. Options: (2, 6, 40), (5, 4, 40), (6, 3, 36), (1, 8, 64). Only 4 + 36 = 40 fits. The answer is **(2, 6, 40)**.

> **Watch:** Traps usually change only the last number, by 1 to 3. Compute the last number for every option.

### Speed checks
- Check the **last number** of each option first. Traps usually change only that one.
- Numbers growing about twice each step: try × 2, then ± 1. Growing about three times: try × 3, then ± 1.
- Learn the near-power numbers on sight. 26, 37, 50 and 65 are squares + 1. 28, 65 and 126 are cubes + 1.
""",
    formulas=[
        {"name": "Chain rule", "tex": r"b = ka + r,\quad c = kb + r", "note": "a, b, c are the three numbers of a set. One step is used twice."},
        {"name": "Third from first two", "tex": r"c = ab,\ a^2 + b^2,\ k(a+b),\ k(a-b)", "note": "Test on every model set."},
        {"name": "Power set", "tex": r"(a,\ a^2 \pm r,\ a^3 \pm r)", "note": "Near-squares and near-cubes of the first number."},
    ],
    tricks=[
        {
            "title": "Compute only the last number",
            "body": "Once you have the rule, work out what the last number of each option should be. Traps nearly always change only that number, so one pass finds the answer.",
            "example": {
                "q": "Sets (2, 4, 8) and (3, 9, 27). Which set follows the same rule? (a) (4, 16, 60) (b) (5, 25, 125) (c) (6, 36, 206) (d) (7, 49, 334)",
                "steps": ["Rule: a, a², a³.", "The last numbers should be 64, 125, 216 and 343.",
                          "Only option (b) has the right last number."],
                "answer": "(b) (5, 25, 125)",
            },
        },
    ],
    mistakes=[
        {"wrong": "Breaking numbers into digits when the whole-number note is given.", "right": "Use only operations on full numbers: +, −, ×, ÷, squares, cubes."},
        {"wrong": "Accepting a rule that fits the first model set but not the second.", "right": "Check the rule on every model set before looking at the options."},
        {"wrong": "Checking only the first two numbers of an option.", "right": "Compute the third number too. Traps are usually off by 1 to 3 there."},
        {"wrong": "Trying only chains and giving up.", "right": "Go through the four families in order: chain, third from two, powers, middle link."},
    ],
    revision=[
        "Whole-number note: no digit tricks.",
        "Four families: chain, third from the first two, powers, middle links the outer two.",
        "The rule must fit every model set.",
        "Compute the last number of every option; traps change only that.",
        "Squares + 1: 10, 17, 26, 37, 50, 65. Cubes + 1: 9, 28, 65, 126.",
    ],
    patterns=[
        pat("an-p26", "Chain sets (the same step twice)", "very common",
            "In each set the numbers grow step by step, e.g. (6, 13, 27) and (8, 17, 35).",
            r"b = ka + r,\ c = kb + r",
            ["Find the step from the 1st to the 2nd number.", "Check that the same step takes the 2nd to the 3rd.",
             "Confirm on the other model set.", "Test each option."],
            "A repeated step is the simplest rule that links three numbers.",
            "Sets (6, 13, 27) and (8, 17, 35). Which set follows the same rule? (a) (5, 11, 23) (b) (7, 15, 30) (c) (9, 19, 38) (d) (4, 9, 20)",
            ["Rule: × 2, then + 1, at each step.", r"(a): $5 \times 2 + 1 = 11$ and $11 \times 2 + 1 = 23$. It fits.",
             "The others need 31, 39 and 19 as the last number."],
            "(a) (5, 11, 23)"),
        pat("an-p27", "Third number from the first two", "common",
            "The third number is bigger than both others and looks like a product, a sum of squares or a multiple of the sum.",
            r"c = ab,\ a^2 + b^2,\ k(a+b)",
            ["Try a × b, a + b, a² + b² and k(a + b) on the model sets.",
             "Keep the one that fits every model set.", "Apply it to each option's first two numbers."],
            "The first two numbers act as inputs and the third as the output.",
            "Sets (3, 8, 24) and (5, 6, 30). Which set follows the same rule? (a) (7, 4, 28) (b) (6, 5, 32) (c) (9, 3, 36) (d) (8, 2, 18)",
            [r"Rule: third = first × second. $3 \times 8 = 24$, $5 \times 6 = 30$.",
             r"(a): $7 \times 4 = 28$. It fits.", "The others give 30, 27 and 16, not their third numbers."],
            "(a) (7, 4, 28)"),
        pat("an-p28", "Power sets (a, a², a³ and near-powers)", "common",
            "The second number is the square of the first, and the third looks like a cube (sometimes each + 1).",
            r"(a,\ a^2+1,\ a^3+1)",
            ["Compare the 2nd number with a² and the 3rd with a³.", "Note any ± r.",
             "Build a² and a³ from each option's first number and compare."],
            "Powers grow so fast that they are easy to recognise.",
            "Sets (3, 10, 28) and (4, 17, 65). Which set follows the same rule? (a) (5, 26, 126) (b) (6, 37, 215) (c) (2, 5, 8) (d) (7, 50, 342)",
            [r"Rule: $a,\ a^2 + 1,\ a^3 + 1$.", r"(a): $25 + 1 = 26$ and $125 + 1 = 126$. It fits.",
             "6 needs 217, 2 needs 9 and 7 needs 344."],
            "(a) (5, 26, 126)"),
        pat("an-p29", "Middle number links the outer two", "occasional",
            "The middle number is the product or the average of the outer two, or the first equals the sum of the other two.",
            r"b = a \times c,\ b = \dfrac{a+c}{2}",
            ["Multiply, add and average the outer numbers; compare with the middle.",
             "Also test first = second + third.", "Confirm on all model sets, then test the options."],
            "Setters sometimes hide the output in the middle instead of at the end.",
            "Sets (5, 35, 7) and (4, 36, 9). Which set follows the same rule? (a) (6, 48, 8) (b) (3, 24, 9) (c) (7, 56, 9) (d) (2, 18, 8)",
            [r"Rule: middle = first × third. $5 \times 7 = 35$, $4 \times 9 = 36$.",
             r"(a): $6 \times 8 = 48$. It fits.", "The others give 27, 63 and 16."],
            "(a) (6, 48, 8)"),
        pat("an-p35", "Third number from the difference", "occasional",
            "The third number is not close to the product or the sum, but the first two numbers are close to each other.",
            r"c = k(a - b)",
            ["Find a − b for each model set.", "See how a − b becomes the third number (often × k).",
             "Check on the second model set.", "Apply to each option."],
            "When the sum and product are too big, the small gap between the first two is the next thing to test.",
            "Sets (15, 9, 24) and (20, 13, 28). Which set follows the same rule? (a) (18, 11, 28) (b) (16, 10, 20) (c) (25, 19, 20) (d) (14, 6, 36)",
            [r"$(15 - 9) \times 4 = 24$ and $(20 - 13) \times 4 = 28$. Rule: difference × 4.",
             r"(a): $(18 - 11) \times 4 = 28$. It fits.", "The others give 24, 24 and 32."],
            "(a) (18, 11, 28)"),
    ],
)

# =====================================================================
# 6. mixed-analogy
# =====================================================================
assert sh("C", 3) == "F" and sh("H", 3) == "K" and 5 * 2 == 10 and 8 * 2 == 16
assert [P(c) ** 2 for c in "DFH"] == [16, 36, 64]
assert psum("CAT") == 24 and psum("BAT") == 23
assert psum("DOG") == 26 and psum("DOG") * 2 == 52
assert P("C") ** 2 == 9 and P("E") ** 2 == 25
# patterns
assert psum("RAM") == 32 and psum("SHAM") == 41
rev = lambda w: sum(27 - P(c) for c in w)
assert rev("DOG") == 55 and psum("DOG") == 26 and rev("CAT") == 57 and 27 * 3 - psum("CAT") == 57
# tricks
assert diff("A", "D") == [3] and diff("C", "F") == [3] and 5 * 2 == 10
assert sh("G", 3) == "J" and sh("I", 3) == "L" and 15 * 2 == 30

S["mixed-analogy"] = dict(
    concept=(
        "Mixed analogies join letters with numbers, or words with numbers. "
        "Each part follows its own small rule. "
        "Split the term into parts, solve each part on its own, then join the answer. "
        "The same-relation form gives four full pairs and asks which one matches the model pair."
    ),
    notes=r"""### Split, solve, join
A mixed term has two kinds of parts, like letters and numbers. Each part has its own simple rule. The two rules do not affect each other.

1. Split each term into its parts.
2. Find one small rule for each part from the model pair.
3. Apply each rule to the matching part of the new term.
4. Join the parts and find that exact answer in the options.

> **Watch:** Options often differ in only one part. Check both parts before you mark.

### Letter and number clusters
C5 : F10 :: H8 : ?

- Letter part: C(3) → F(6) is + 3. So H(8) + 3 = K.
- Number part: 5 → 10 is × 2. So 8 × 2 = 16.
- Answer: **K16**.

If a cluster has two letters, like B3D, each letter slot has its own shift.

Sometimes the number is built **from** the letter. In D16, F36, H64 the number is the square of the letter's position. D is 4, and 4² = 16.

### A table keeps the parts apart
Write the two tracks in two columns. Fill the model row first. Then copy each rule down one row.

| Part | C5 → F10 | H8 → ? |
|---|---|---|
| Letter | C → F is + 3 | H + 3 = K |
| Number | 5 → 10 is × 2 | 8 × 2 = 16 |

Read the answer from the last column: **K16**. An error stays inside one cell, so each part is easy to check on its own.

### Word to number
CAT : 24 :: BAT : ? The number comes from the letter positions of the word.

1. **Sum of positions.** CAT = 3 + 1 + 20 = 24. So BAT = 2 + 1 + 20 = 23.
2. **Sum, then × k or ± r.** DOG = 4 + 15 + 7 = 26. If DOG is coded 52, the extra step is × 2.
3. **Reverse positions.** Count A = 26, B = 25 ... Z = 1. Each letter is worth 27 − p. In reverse positions D = 23, O = 12, G = 20, so DOG adds up to 55. A model like DOG : 55 means reverse positions.

> **Tip:** Always find the plain sum of the model word first. Then compare it with the given number to see the extra step.

### Letter to number
C : 9 :: E : ? C is the 3rd letter, and 9 = 3². E is the 5th letter, so the answer is 5² = **25**.

Other common rules: 2 × position, reverse position (27 − p), position + a fixed number.

### Same-relation word pairs
"Select the pair related in the same way as Tailor : Needle."

Say the link: *a worker and the tool the worker uses*. Test all four pairs with that sentence. The traps are pairs from the same world with a different link:

- Doctor : Hospital is a worker and a workplace.
- Author : Book is a worker and a product.
- Farmer : Crop is a worker and a product.

> **Rule:** One link sentence, tested on every option. The pair that makes a true sentence in the same direction is the answer.
""",
    formulas=[
        {"name": "Word to number", "tex": r"\text{code} = k \times (\text{sum of positions}) + r", "note": "Often k = 1 and r = 0: the plain sum of letter positions."},
        {"name": "Reverse position", "tex": r"\text{reverse value} = 27 - p", "note": "A = 26, B = 25 ... Z = 1."},
        {"name": "Reverse sum shortcut", "tex": r"\text{reverse sum} = 27n - \text{plain sum}", "note": "n is the number of letters in the word."},
    ],
    tricks=[
        {
            "title": "Two columns: letters and numbers",
            "body": "Make one column for the letters and one for the numbers. Solve each column on its own. An error then stays inside one column.",
            "example": {
                "q": "A5C : D10F :: G15I : ?",
                "steps": ["Letters: A → D and C → F are + 3. So G → J and I → L.",
                          r"Number: 5 → 10 is × 2. So $15 \times 2 = 30$."],
                "answer": "J30L",
            },
        },
        {
            "title": "One sentence for all four pairs",
            "body": "In same-relation questions, make the link sentence once from the model pair. Test every option against that same sentence, in the same order.",
            "example": {
                "q": "Sword : Sheath. Select the pair related in the same way. (a) Gun : Trigger (b) Knife : Blade (c) Spectacles : Case (d) Letter : Stamp",
                "steps": ["Sentence: \"the second is the cover the first is kept in\".",
                          "Trigger and blade are parts. A stamp is stuck on a letter.",
                          "Spectacles are kept in a case."],
                "answer": "(c) Spectacles : Case",
            },
        },
    ],
    mistakes=[
        {"wrong": "Assuming the number part follows the letter part's rule.", "right": "Solve each part on its own. The two rules are independent."},
        {"wrong": "Getting the letters right but copying the wrong number.", "right": "Options differ in one part only. Check both parts before marking."},
        {"wrong": "Counting A = 0 instead of A = 1.", "right": "A = 1, B = 2 ... Z = 26 unless the model shows reverse positions."},
        {"wrong": "For word to number, stopping at the plain sum when the model needs × k or ± r.", "right": "Compare the model's plain sum with its number to find the extra step, then use it."},
        {"wrong": "In pair selection, choosing a pair from the same topic.", "right": "Choose the pair with the same link, like worker : tool."},
    ],
    revision=[
        "Split the term, solve each part, then join.",
        "Letter parts: positions and shifts. Number parts: +, ×, squares.",
        "Word to number: plain sum first, then look for × k or ± r.",
        "Reverse value of a letter = 27 − its position.",
        "Letter to number: position, 2 × position, position squared, 27 − position.",
        "Pair selection: one link sentence tested on all four pairs.",
    ],
    patterns=[
        pat("an-p22", "Letter and number cluster", "common",
            "Terms like \"C5 : F10\" or \"P7R : S14U\" mix letters and numbers.",
            None,
            ["Split each term into a letter part and a number part.",
             "Find the letter shift and the number rule separately.",
             "Apply both to the new term and join the parts."],
            "The parts are independent, so each one is a small, easy question.",
            "C5 : F10 :: H8 : ? (a) K16 (b) J16 (c) K18 (d) L16",
            ["Letters: C → F is + 3, so H → K.", "Numbers: 5 → 10 is × 2, so 8 → 16."],
            "(a) K16"),
        pat("an-p23", "Word to number (sum of letter positions)", "common",
            "A word is paired with a number, e.g. \"CAT : 24 :: BAT : ?\".",
            r"\text{code} = k \times \text{sum} + r",
            ["Add the positions of the model word's letters.",
             "Compare the sum with the given number: equal, × k, or ± r.",
             "Find the sum for the new word and apply the same extra step."],
            "Setters build the number from letter positions in one or two simple steps.",
            "RAM : 32 :: SHAM : ? (a) 40 (b) 41 (c) 42 (d) 45",
            ["R + A + M = 18 + 1 + 13 = 32. The rule is the plain sum.",
             "S + H + A + M = 19 + 8 + 1 + 13 = 41."],
            "(b) 41"),
        pat("an-p24", "Select the word pair with the same relation", "common",
            "A model pair is followed by four complete word pairs: \"Select the pair related in the same way as Tailor : Needle\".",
            None,
            ["Write the link of the model pair as a sentence.", "Put each option pair into that sentence.",
             "Keep the one pair that makes a true sentence in the same direction."],
            "Traps share the topic but not the link (workplace instead of tool).",
            "Tailor : Needle. Select the pair related in the same way. (a) Painter : Brush (b) Doctor : Hospital (c) Author : Book (d) Farmer : Crop",
            ["Link: a worker and the tool the worker uses.", "A painter uses a brush.",
             "Hospital is a workplace. Book and crop are products."],
            "(a) Painter : Brush"),
        pat("an-p25", "Letter to number (position based)", "occasional",
            "A single letter is paired with a number, e.g. \"C : 9 :: E : ?\" or \"B : 25 :: D : ?\".",
            r"n = p^2,\ 2p,\ 27 - p",
            ["Write the letter's position p and its reverse position 27 − p.",
             "See how the number is built: p², 2p, 27 − p or p + r.",
             "Build the new letter's number the same way."],
            "Only a few simple formulas are used, and each takes seconds to test.",
            "C : 9 :: E : ? (a) 10 (b) 15 (c) 25 (d) 22",
            ["C is the 3rd letter, and 9 = 3².", "E is the 5th letter, so 5² = 25."],
            "(c) 25"),
        pat("an-p36", "Word to number using reverse positions", "occasional",
            "The plain sum of positions does not match the model number, and the number is larger than the plain sum.",
            r"\text{reverse sum} = 27n - \text{plain sum}",
            ["Find the plain sum of the model word.", "Find 27 × (number of letters) − plain sum.",
             "If that matches, use reverse positions for the new word."],
            "Reverse positions count Z = 1 ... A = 26, so each letter is worth 27 − p.",
            "DOG : 55 :: CAT : ? (a) 24 (b) 48 (c) 57 (d) 59",
            ["DOG plain sum = 4 + 15 + 7 = 26, not 55.", r"$27 \times 3 - 26 = 55$. So the rule is reverse positions.",
             r"CAT plain sum = 24. $81 - 24 = 57$."],
            "(c) 57"),
    ],
)

# ---------- write back ----------
data = json.loads(TOPIC.read_text(encoding="utf-8"))
before = {s["id"]: len(s.get("patterns", [])) for s in data["subtopics"]}
all_new = [p["id"] for v in S.values() for p in v["patterns"]]
assert len(all_new) == len(set(all_new)), "duplicate pattern id"
for sub in data["subtopics"]:
    new = S[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in new["patterns"]}, (sub["id"], "dropped a pattern id")
    assert 2500 <= len(new["notes"]) <= 5000, (sub["id"], len(new["notes"]))
    new["notes"] = new["notes"].strip() + "\n"
    sub.update(new)
assert set(S) == set(before), "every subtopic must be rewritten"
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
for sid in S:
    print(f"{sid}: notes {len(S[sid]['notes'])} chars, patterns {before[sid]} -> {len(S[sid]['patterns'])}")
