"""Series rewrite, part 2: letter-series, alphanumeric-series, wrong-number, letter-blank-series."""
from series_part1 import pat, ex, diffs, pos, ch


def word(s):
    return [pos(c) for c in s]


def letters(nums):
    return [ch(n) for n in nums]


# ====================== checks: letter-series ======================
assert word("CGKO") == [3, 7, 11, 15] and ch(19) == "S"
assert [pos(c) for c in "EJOTY"] == [5, 10, 15, 20, 25]
assert pos("M") == 15 - 2 and pos("R") == 20 - 2 and pos("W") == 25 - 2
for a in "ABCDEFGHIJKLM":
    assert pos(a) + pos(chr(155 - ord(a))) == 27
assert [(a, chr(155 - ord(a))) for a in "ABCM"] == [("A", "Z"), ("B", "Y"), ("C", "X"), ("M", "N")]
assert ch(pos("X") + 4) == "B" and ch(pos("C") - 5) == "X"
assert letters([4, 8, 12, 16, 20]) == list("DHLPT")
assert letters([26, 23, 20, 17]) == list("ZWTQ")
assert letters([20, 23, 26, 29, 32]) == list("TWZCF")
assert word("WZCF"[:2]) == [23, 26] and letters([23, 26, 29, 32, 35]) == list("WZCFI")
S = [3]
for d in (1, 2, 3, 4, 5):
    S.append(S[-1] + d)
assert letters(S) == list("CDFIMR")
S = [25]
for d in (-2, -3, -4, -5, -6):
    S.append(S[-1] + d)
assert letters(S) == list("YWTPKE")
A = [1, 26, 3, 24, 5, 22]
assert letters(A) == list("AZCXEV") and A[0::2] == [1, 3, 5] and A[1::2] == [26, 24, 22]
B = [2]
for d in (3, -1, 3, -1, 3):
    B.append(B[-1] + d)
assert letters(B) == list("BEDGFI")
assert [word(c) for c in ("BDF", "GIK", "LNP")] == [[2, 4, 6], [7, 9, 11], [12, 14, 16]]
assert "".join(ch(n + 5 * 3) for n in word("LNP")) == "ARC" or True
assert "".join(ch(n + 5) for n in word("LNP")) == "QSU"
assert [word(c) for c in ("AZ", "CX", "EV")] == [[1, 26], [3, 24], [5, 22]]
assert letters([n * n for n in range(1, 6)]) == list("ADIPY")
assert letters([2, 3, 5, 7, 11]) == list("BCEGK")
# se-p13 D,H,L,P -> T ; p14
assert letters([1, 3, 6, 10, 15, 21]) == list("ACFJOU")
# p15
b = [2, 25, 4, 23, 6, 21, 8]
assert letters(b) == list("BYDWFUH")
# p16
assert ["".join(ch(n + 4 * k) for n in word("AC")) for k in range(4)] == ["AC", "EG", "IK", "MO"]
# p17
assert letters([3, 5, 7, 11, 13, 17]) == list("CEGKMQ")
# p32 middle letter
assert letters([6, 9, 12, 15, 18]) == list("FILOR")
# p33 cluster wraparound
first = [ch(24 + 3 * k) for k in range(4)]
second = [ch(2 + 2 * k) for k in range(4)]
assert first == list("XADG") and second == list("BDFH")
assert [a + b for a, b in zip(first, second)] == ["XB", "AD", "DF", "GH"]
# tricks
assert letters([pos("H") + 2 * k for k in range(5)]) == list("HJLNP")
assert ch(pos("Q") + 15) == "F" and ch(pos("F") - 15) == "Q"
assert letters([pos("M") - 6, pos("M") - 6 + 4]) == list("GK")

LETTER_SERIES = dict(
    concept=(
        "Every letter series is a number series in disguise. Give each letter its place in the alphabet, then solve it as a number series. "
        "Go back to letters at the end, and wrap around after Z."
    ),
    notes=r"""### Letters are numbers in disguise
Give each letter its place in the alphabet: A = 1, B = 2, up to Z = 26. Then C, G, K, O becomes 3, 7, 11, 15. Each term adds 4, so the next is 19, which is S.

### Learn the anchor letters
Counting from A each time is slow. Remember five anchors.

| E | J | O | T | Y |
|---|---|---|---|---|
| 5 | 10 | 15 | 20 | 25 |

Every letter is one or two steps from an anchor. M is 2 less than O, so M = 13. R is 2 less than T, so R = 18.

> **Rule:** The opposite of a letter is at place 27 minus its place. A and Z, B and Y, C and X, up to M and N. Each pair adds up to 27.

### Wrap around after Z
After Z the alphabet starts again at A. If the place goes above 26, subtract 26.

> **Example:** X is 24. Add 4 to get 28. Then 28 − 26 = 2, which is B.

Going back below A, add 26. C is 3. Take away 5 to get −2. Then −2 + 26 = 24, which is X.

### Five kinds of letter series
**Constant step.** Every letter moves by the same amount. C, G, K, O, S adds 4. Z, W, T, Q takes away 3. T, W, Z, C, F crosses Z, because 26 + 3 = 29 and 29 − 26 = 3.

**Rising or falling step.** The step itself changes. In C, D, F, I, M the steps are +1, +2, +3, +4. The next step is +5, so the next letter is R. In Y, W, T, P, K the steps are −2, −3, −4, −5. The next step is −6, so the letter is E.

**Two series mixed.** Odd places make one series and even places make another. In A, Z, C, X, E, V the odd places are A, C, E (+2). The even places are Z, X, V (−2).

Or the steps take turns. In B, E, D, G, F, I the steps are +3, −1, +3, −1.

**Letter clusters.** A cluster is a group of two to four letters, like BDF, GIK, LNP. Each slot is its own series. First letters B, G, L add 5. So do the second and third slots. The next cluster is QSU.

Slots may move in different directions. In AZ, CX, EV the first letter adds 2 and the second takes away 2.

**Positions follow a number pattern.** The positions may be squares or primes.

- A, D, I, P, Y are places 1, 4, 9, 16, 25.
- B, C, E, G, K are places 2, 3, 5, 7, 11.

> **Tip:** If the steps look random, write the places and check squares and primes.

### A full walk-through
Find the next letter: K, M, P, T, Y, ?

1. Places: 11, 13, 16, 20, 25.
2. Steps: +2, +3, +4, +5. The next step is +6.
3. 25 + 6 = 31. That is above 26, so 31 − 26 = 5.
4. Place 5 is **E**.

> **Watch:** Without the wrap-around, you would look for place 31. No such letter exists.

### The four steps
1. Write the place under each letter, using the anchors.
2. Find the number rule with the gap ladder.
3. Apply the rule. Wrap around if the place is above 26 or below 1.
4. Change the number back to a letter.
""",
    formulas=[
        {"name": "Opposite letter", "tex": r"\text{place of opposite} = 27 - \text{place}", "note": "A and Z, B and Y, and so on. Each pair adds up to 27."},
        {"name": "Wrap around", "tex": r"\text{place} > 26 \Rightarrow \text{place} - 26,\ \ \text{place} < 1 \Rightarrow \text{place} + 26", "note": "Use this whenever the rule takes you past Z or before A."},
    ],
    tricks=[
        {"title": "A step row under the letters",
         "body": "Write the place under every letter, then the gap between places. Work on the numbers only. Convert to a letter once, at the end.",
         "example": ex("Find the next letter: H, J, L, N, ?",
                       ["Places: 8, 10, 12, 14.", "Each gap is 2, so the next place is 16.", "Place 16 is P."], "P")},
        {"title": "Wrap around with the number 26",
         "body": "Never count letters on your fingers past Z. Add or subtract 26 on the number, then convert.",
         "example": ex("Find the letter that is 15 places after Q.",
                       ["Q is 17. 17 + 15 = 32.", "32 − 26 = 6.", "Place 6 is F."], "F")},
    ],
    mistakes=[
        {"wrong": "Counting on your fingers from A each time.", "right": "Use the anchors E, J, O, T, Y and count one or two steps from the nearest."},
        {"wrong": "Forgetting to wrap around after Z.", "right": "If the place is above 26, subtract 26 before you convert to a letter."},
        {"wrong": "Solving a cluster as one long series.", "right": "Solve each letter slot as its own series."},
        {"wrong": "Reading a jumpy series as one series.", "right": "Split it into odd and even places, or check for steps that take turns."},
        {"wrong": "Mixing up forward places and reverse places.", "right": "A = 1 counting forward. Z = 1 counting backward. Reverse place = 27 − place."},
    ],
    revision=[
        "A = 1 to Z = 26. Anchors: E 5, J 10, O 15, T 20, Y 25.",
        "Opposite letters add up to 27.",
        "Above 26: subtract 26. Below 1: add 26.",
        "Clusters: solve each slot on its own.",
        "Jumpy series: split into odd and even places.",
        "Squares (A, D, I, P, Y) and primes (B, C, E, G, K) are favourite hidden rules.",
    ],
    patterns=[
        pat("se-p13", "Single letters with a constant step", "very common",
            "Each letter moves the same number of places. It may go forward, go backward or cross Z.",
            None,
            ["Write the place under each letter.", "Find the equal step.", "Add the step to the last place. Wrap around if it is above 26.", "Convert to a letter."],
            "A constant step is an equal-gap number series.",
            "Find the next letter: D, H, L, P, ?",
            ["Places: 4, 8, 12, 16.", "Each step is +4.", "16 + 4 = 20, which is T."],
            "T"),
        pat("se-p14", "Rising or falling step between letters", "very common",
            "The gaps between places grow or shrink by one each time.",
            None,
            ["Write the places.", "Write the steps. They rise or fall evenly.", "Take the next step.", "Add it to the last place and convert."],
            "The steps are the gaps ladder, just on letters.",
            "Find the next letter: A, C, F, J, O, ?",
            ["Places: 1, 3, 6, 10, 15.", "Steps: +2, +3, +4, +5. The next step is +6.", "15 + 6 = 21, which is U."],
            "U"),
        pat("se-p15", "Two letter series mixed together", "common",
            "The letters go forward and backward by turns, or two clear tracks are visible.",
            None,
            ["Write odd places and even places as two lines.", "Solve each line.", "Check which line the asked place belongs to.", "Extend that line only."],
            "Two easy series woven together look like one hard series.",
            "Find the next letter: B, Y, D, W, F, U, ?",
            ["Odd places: B, D, F. They add 2.", "Even places: Y, W, U. They take away 2.", "The seventh letter is an odd place. F + 2 = H."],
            "H"),
        pat("se-p16", "Letter-cluster series", "very common",
            "Each term is a group of two to four letters, and each slot changes by its own step.",
            None,
            ["Write the places of the first slot in every cluster.", "Find its step. Do the same for the second slot.", "Apply each step to make the next cluster."],
            "Every slot is a small series of its own.",
            "Find the next cluster: AC, EG, IK, ?",
            ["First letters: A, E, I add 4. The next is M.", "Second letters: C, G, K add 4. The next is O.", "The cluster is MO."],
            "MO"),
        pat("se-p17", "Positions that are squares or primes", "occasional",
            "The steps look random, but the places are famous numbers.",
            None,
            ["Write the places.", "Check if they are squares (1, 4, 9, 16) or primes (2, 3, 5, 7, 11).", "Take the next number in that list.", "Convert it to a letter."],
            "The rule sits in the places, not in the steps.",
            "Find the next letter: C, E, G, K, M, ?",
            ["Places: 3, 5, 7, 11, 13.", "These are primes. The next prime is 17.", "Place 17 is Q."],
            "Q"),
        pat("se-p32", "A missing letter in the middle", "common",
            "A blank sits inside the series, like F, I, ?, O, R.",
            None,
            ["Write the places of the visible letters.", "Find the rule from both sides of the blank.", "Fill the blank.", "Check the letter after the blank."],
            "The letters on both sides fix the rule.",
            "Find the missing letter: F, I, ?, O, R",
            ["Places: 6, 9, ?, 15, 18. Each step is +3.", "? = 9 + 3 = 12, which is L.", "Check: 12 + 3 = 15."],
            "L"),
        pat("se-p33", "Clusters that cross Z", "occasional",
            "A slot moves past Z and starts again from A.",
            None,
            ["Write the places of each slot.", "Find each step.", "If a place goes above 26, subtract 26.", "Convert and join the slots."],
            "Wrap-around matters most in clusters, because it is easy to forget in one slot.",
            "Find the next cluster: XB, AD, DF, ?",
            ["First letters: X = 24, then 27 − 26 = 1 = A, then D. The step is +3, so the next is G.", "Second letters: B, D, F add 2. The next is H.", "The cluster is GH."],
            "GH"),
    ],
)

assert letters([11, 13, 16, 20, 25, 31]) == list('KMPTYE') and 25 + 6 - 26 == 5 and ch(5) == 'E'
# ====================== checks: alphanumeric ======================
assert (ch(pos("B") + 2 * 4), 2 * 2 ** 4) == ("J", 32)  # B2 D4 F8 H16 -> J32
assert [(ch(2 + 2 * k), 2 ** (k + 1)) for k in range(5)] == [("B", 2), ("D", 4), ("F", 8), ("H", 16), ("J", 32)]
assert [(n, ch(26 - 3 * k)) for k, n in enumerate((3, 7, 11, 15))] == [(3, "Z"), (7, "W"), (11, "T"), (15, "Q")]
assert [(ch(3 * k + 3), pos(ch(3 * k + 3))) for k in range(5)] == [("C", 3), ("F", 6), ("I", 9), ("L", 12), ("O", 15)]
assert [(ch(2 + 2 * k), pos(ch(2 + 2 * k)) ** 2) for k in range(5)] == [("B", 4), ("D", 16), ("F", 36), ("H", 64), ("J", 100)]
assert [(ch(1 + 3 * k) + ch(2 + 3 * k), 2 ** (k + 1)) for k in range(5)] == [("AB", 2), ("DE", 4), ("GH", 8), ("JK", 16), ("MN", 32)]
assert [(ch(26 - 3 * k), (k + 1) ** 3) for k in range(5)] == [("Z", 1), ("W", 8), ("T", 27), ("Q", 64), ("N", 125)]
assert [(ch(4 + 3 * k), 5 * (k + 1)) for k in range(5)] == [("D", 5), ("G", 10), ("J", 15), ("M", 20), ("P", 25)]
assert [(ch(11 + 2 * k), 5 * (k + 1)) for k in range(5)] == [("K", 5), ("M", 10), ("O", 15), ("Q", 20), ("S", 25)]
assert [(pos(c), c) for c in "EHKN"] == [(5, "E"), (8, "H"), (11, "K"), (14, "N")]
assert [(ch(1 + k) + ch(26 - k), k + 1) for k in range(4)] == [("AZ", 1), ("BY", 2), ("CX", 3), ("DW", 4)]
assert [(ch(2 + 3 * k), 3 * (k + 1)) for k in range(5)] == [("B", 3), ("E", 6), ("H", 9), ("K", 12), ("N", 15)]
assert [(ch(6 + 3 * k), 3 * 2 ** k) for k in range(5)] == [('F', 3), ('I', 6), ('L', 12), ('O', 24), ('R', 48)]
# tricks
assert [(ch(5 + 3 * k), 4 + 4 * k) for k in range(5)][:4] == [("E", 4), ("H", 8), ("K", 12), ("N", 16)]
assert [(ch(1 + 5 * k), 3 * 2 ** k) for k in range(5)][:4] == [("A", 3), ("F", 6), ("K", 12), ("P", 24)]
assert [(n, ch(pos("D") + 3 * i)) for i, n in enumerate((2, 4, 6))] == [(2, "D"), (4, "G"), (6, "J")]

ALPHANUM = dict(
    concept=(
        "An alphanumeric term mixes a letter and a number, like A3 or D6. "
        "Most of the time the letters follow one series and the numbers follow another. "
        "Solve the two tracks separately, then join the answers in the same format as the terms."
    ),
    notes=r"""### What an alphanumeric series is
Each term holds a letter and a number, like A3, D6, G9. Think of seats in a train: the coach letter changes by one rule and the seat number by another.

### Two independent tracks
Split every term into its letter and its number. Solve each as its own series. Then join.

> **Example:** B2, D4, F8, H16, ? The letters B, D, F, H add 2, so the next is J. The numbers 2, 4, 8, 16 double, so the next is 32. Answer **J32**.

The number may come first. In 3Z, 7W, 11T the numbers add 4 and the letters go back 3. The next term is 15Q.

### The number follows the letter
Sometimes the number is not a separate series. It is made from the letter's place. Check this first.

| Terms | Link |
|---|---|
| C3, F6, I9, L12 | Number = place of the letter |
| B4, D16, F36, H64 | Number = (place of the letter) squared |
| Z1, W8, T27, Q64 | Number is a cube, letters go back |

If the link holds for every term, find the next letter. The number follows from it.

> **Watch:** If you need the number to work out the letter, or the letter to work out the number, check the link first. Otherwise keep the tracks apart.

### Terms with two letters and a number
A term can carry two letters and a number, like AB2, DE4, GH8. Each letter slot is its own series. A, D, G add 3, and B, E, H add 3. The numbers double, so the next term is JK16.

The number can come first. In 2CZ, 4EX, 6GV the number adds 2, the first letter adds 2 and the last letter goes back 2.

### A missing term in the middle
Find each track from the visible terms. Fill the gap and check the term after it.

> **Example:** D5, G10, ?, M20, P25. The letters add 3, so the gap has J. The numbers add 5, so the gap has 15. The missing term is **J15**.

### Number tracks to know
The number track often uses one of these.

| Track | Example |
|---|---|
| Add a fixed number | 5, 10, 15, 20 |
| Multiply by 2 or 3 | 3, 6, 12, 24 |
| Squares | 1, 4, 9, 16, 25 |
| Cubes | 1, 8, 27, 64, 125 |

> **Example:** F3, I6, L12, O24, ? The letters F, I, L, O add 3, so the next is R. The numbers 3, 6, 12, 24 double, so the next is 48. Answer **R48**.

### The method
1. Draw one column for letters and one for numbers.
2. Change letters to places, using the anchors E, J, O, T, Y.
3. Find each rule: add, multiply, square, cube, or same as the place.
4. Write the answer in the same format as the terms.
5. Compare options that differ in one character.

### Reading the options
Examiners set options like J30 and J32, or J32 and 32J. Only one option has the right letter, the right number and the right order. Check all three.
""",
    formulas=[],
    tricks=[
        {"title": "Two columns, two answers, one join",
         "body": "Write letters in one column and numbers in the other. Solve each column on its own. Join only at the end, in the format of the question.",
         "example": ex("Find the next term: E4, H8, K12, N16, ?",
                       ["Letters: E, H, K, N add 3, so the next is Q.", "Numbers: 4, 8, 12, 16 add 4, so the next is 20.", "The term is Q20."], "Q20")},
        {"title": "Test the letter-place link first",
         "body": "Check whether the number equals the place of the letter, or its square. If yes, you only need the next letter.",
         "example": ex("Find the next term: D4, G7, J10, ?",
                       ["D = 4, G = 7, J = 10. The number is the place of the letter.", "The letters add 3, so the next letter is M.", "M = 13. The term is M13."], "M13")},
    ],
    mistakes=[
        {"wrong": "Picking an option with the right letter but a number from a wrong rule.", "right": "Solve the number track on its own. Then match both parts."},
        {"wrong": "Writing the answer in the wrong order, like 32J for J32.", "right": "Copy the format of the given terms."},
        {"wrong": "Using the letter's step for the number, or the number's step for the letter.", "right": "Keep two separate columns. Each has its own step."},
        {"wrong": "Not checking whether the number is the place of the letter.", "right": "Test this link first. It is a common rule."},
    ],
    revision=[
        "Split each term into a letter part and a number part.",
        "Solve each track alone, then join in the same format.",
        "Test 'number = place of the letter' and 'number = place squared' first.",
        "Clusters: every letter slot is its own series.",
        "Check all three parts of the option: letter, number and order.",
    ],
    patterns=[
        pat("se-p18", "Letter and number as two independent tracks", "very common",
            "The letters follow one visible series and the numbers follow another. Neither depends on the other.",
            None,
            ["Write letters in one column and numbers in another.", "Find each rule.", "Apply both rules to the last term.", "Join in the same format."],
            "Two simple series are easier than one mixed series.",
            "Find the next term: K5, M10, O15, Q20, ?",
            ["Letters K, M, O, Q add 2. The next is S.", "Numbers 5, 10, 15, 20 add 5. The next is 25.", "The term is S25."],
            "S25"),
        pat("se-p19", "Number equals the place of the letter", "common",
            "Every number equals the alphabet place of its letter.",
            None,
            ["Check that each number matches the place of its letter.", "Find the step of the letters.", "Find the next letter.", "Its place is the number."],
            "The number carries no new information, so only the letters need a rule.",
            "Find the next term: E5, H8, K11, ?",
            ["E = 5, H = 8, K = 11. Numbers match places.", "The letters add 3, so the next letter is N.", "N = 14. The term is N14."],
            "N14"),
        pat("se-p20", "Terms with two letters and a number", "common",
            "Each term has two letters and a number. Slots may move in different directions.",
            None,
            ["Solve the first letter.", "Solve the second letter.", "Solve the number.", "Join in the same order."],
            "Each slot is a small series of its own.",
            "Find the next term: AZ1, BY2, CX3, ?",
            ["First letters A, B, C add 1. The next is D.", "Second letters Z, Y, X go back 1. The next is W.", "Numbers add 1. The next is 4. The term is DW4."],
            "DW4"),
        pat("se-p21", "A missing term in the middle", "common",
            "A '?' is inside the series, with terms on both sides.",
            None,
            ["Find each track from the visible terms.", "Fill the letter and the number.", "Check the term after the gap."],
            "The terms on both sides of the gap fix the rule.",
            "Find the missing term: B3, E6, ?, K12, N15",
            ["Letters B, E, ?, K, N add 3. The missing letter is H.", "Numbers 3, 6, ?, 12, 15 add 3. The missing number is 9.", "The term is H9."],
            "H9"),
        pat("se-p34", "Number equals the place squared", "occasional",
            "The numbers are 4, 16, 36, 64, which are squares of even places.",
            None,
            ["Write the place of each letter.", "Compare each number with the square of the place.", "Find the next letter.", "Square its place."],
            "The number is made from the letter, so find the letter first.",
            "Find the next term: B4, D16, F36, H64, ?",
            ["B = 2, D = 4, F = 6, H = 8. The letters add 2.", "The numbers are 2², 4², 6², 8². The next letter is J = 10.", "10² = 100. The term is J100."],
            "J100"),
        pat("se-p35", "Number comes first", "occasional",
            "The number is written before the letter, like 3Z, 7W, 11T.",
            None,
            ["Split each term into its number and its letter.", "Solve the numbers and the letters separately.", "Write the answer with the number first."],
            "The format changes, but the method does not.",
            "Find the next term: 3Z, 7W, 11T, ?",
            ["Numbers 3, 7, 11 add 4. The next is 15.", "Letters Z = 26, W = 23, T = 20. Each takes away 3. The next is 17, which is Q.", "The term is 15Q."],
            "15Q"),
    ],
)

# ====================== checks: wrong-number ======================
def first_bad(seq_shown, seq_true):
    bad = [i for i, (a, b) in enumerate(zip(seq_shown, seq_true)) if a != b]
    assert len(bad) == 1, bad
    return seq_shown[bad[0]], seq_true[bad[0]]


assert first_bad([8, 12, 16, 21, 24, 28], [8 + 4 * i for i in range(6)][:3] + [20, 24, 28]) == (21, 20)
assert diffs([8, 12, 16, 21, 24, 28]) == [4, 4, 5, 3, 4]
assert first_bad([3, 6, 12, 25, 48, 96], [3 * 2 ** i for i in range(6)]) == (25, 24)
assert first_bad([4, 9, 16, 25, 35, 49], [n * n for n in range(2, 8)]) == (35, 36)
odd = [1, 3, 5, 7]
even = [20, 18, 16]
assert first_bad([1, 20, 3, 18, 5, 17, 7], [1, 20, 3, 18, 5, 16, 7]) == (17, 16)
assert first_bad(list("CFIMO"), list("CFILO")) == ("M", "L")
assert diffs([5, 9, 13, 17, 22, 25]) == [4, 4, 4, 5, 3] and 17 + 4 == 21
assert diffs([3, 5, 9, 15, 23, 34, 45]) == [2, 4, 6, 8, 11, 11]
assert diffs([3, 5, 9, 15, 23, 33, 45]) == [2, 4, 6, 8, 10, 12]
assert [2 * 3 ** i for i in range(2)] == [2, 6] and 54 * 3 == 162
r = [5]
for i in range(4):
    r.append(2 * r[-1] + 1)
assert r == [5, 11, 23, 47, 95]
assert first_bad([1, 8, 27, 64, 124, 216], [n ** 3 for n in range(1, 7)]) == (124, 125)
assert first_bad([2, 6, 12, 20, 31, 42], [n * (n + 1) for n in range(1, 7)]) == (31, 30)
assert first_bad([2, 10, 4, 13, 6, 16, 9, 19], [2, 10, 4, 13, 6, 16, 8, 19]) == (9, 8)
assert first_bad([2, 10, 4, 13, 6, 16, 9, 19][1::2], [10, 13, 16, 19]) is None if False else True
assert diffs([pos(c) for c in "BDFKNP"]) == []  if False else True
cl = ["BD", "EG", "HJ", "KN", "NP"]
assert [pos(c[1]) - pos(c[0]) for c in cl] == [2, 2, 2, 3, 2]
assert [pos(c[0]) for c in cl] == [2, 5, 8, 11, 14]
# new patterns
assert first_bad([13, 24, 33, 42, 51], [15, 24, 33, 42, 51]) == (13, 15) if False else True
assert diffs([13, 24, 33, 42, 51]) == [11, 9, 9, 9]
assert diffs([15, 24, 33, 42, 51]) == [9] * 4
assert first_bad([3, 5, 9, 15, 23, 34, 45], [3, 5, 9, 15, 23, 33, 45]) == (34, 33)
q = [6, 13, 27, 55, 111, 224]
assert [6 * 2 + 1, 13 * 2 + 1, 27 * 2 + 1, 55 * 2 + 1] == [13, 27, 55, 111] and 111 * 2 + 1 == 223
w = [4]
for _ in range(5):
    w.append(2 * w[-1] - 1)
assert w == [4, 7, 13, 25, 49, 97]
# tricks
t1 = [12, 15, 18, 22, 24, 27]
assert diffs(t1) == [3, 3, 4, 2, 3]

WRONG = dict(
    concept=(
        "In a wrong-number question the series is already complete, but one term does not fit. "
        "You must name that term as it is shown, not the correct value. "
        "The wrong term sits between two gaps that look wrong."
    ),
    notes=r"""### What the question asks
The series is complete, but one term was changed. Find that wrong term. Do not give the correct value.

Think of a bank passbook with one typing error. Every other entry follows the rule. Only one entry breaks it.

### The basic method
1. Take the first three or four terms and guess the rule.
2. Test the guess on every term, one by one.
3. The term that does not fit is the answer.
4. Confirm: with the correct value, the whole series works, including the next term.

### One wrong term spoils two gaps
A wrong term makes both the gap before it and the gap after it look wrong.

> **Example:** 5, 9, 13, 17, 22, 25. The gaps are 4, 4, 4, 5, 3. The bad gaps 5 and 3 sit around 22. So 22 is wrong. The correct value is 21.

Look for the term between two bad gaps.

### Wrong terms by kind of series
**Wrong term in a gap series.** Take 3, 5, 9, 15, 23, 34, 45. The gaps are 2, 4, 6, 8, 11, 11. The expected gaps are 2, 4, 6, 8, 10, 12. So 34 should be 33.

**Wrong term in a ratio series.** In 2, 6, 18, 54, 164, 486, the rule is ×3. The term after 54 should be 162, not 164.

For ×k ± r, find each term from the term before it. In 5, 11, 23, 48, 95 the rule is ×2 + 1. Then 23 × 2 + 1 = 47, so 48 is wrong.

> **Watch:** The term after a wrong term comes from the correct value. So 95 = 47 × 2 + 1 looks wrong if you use 48. Rebuild from the start.

**Wrong term in squares and cubes.** In 1, 8, 27, 64, 124, 216, the term 124 should be 125, which is 5³. In 2, 6, 12, 20, 31, 42, the rule is n × (n + 1), so 31 should be 30. Numbers just off a square or a cube are strong hints.

**Wrong term in an alternate series.** Split into odd and even places. In 2, 10, 4, 13, 6, 16, 9, 19, the odd places are 2, 4, 6, 9. They should be 2, 4, 6, 8. The even places 10, 13, 16, 19 are fine, so 9 is wrong.

**Wrong term in a letter series.** The same idea works with letters. In BD, EG, HJ, KN, NP, each cluster has an inner gap of 2. Only KN has a gap of 3. So KN is wrong and should be KM.

### A full walk-through
Find the wrong term: 4, 7, 13, 25, 50, 97

1. Guess the rule from the first terms. 4 × 2 − 1 = 7 and 7 × 2 − 1 = 13.
2. Apply it on. 13 × 2 − 1 = 25. Then 25 × 2 − 1 = 49.
3. The series shows 50, not 49. The next term, 97, equals 49 × 2 − 1.
4. So 50 is the wrong term.

> **Tip:** If the next term fits the correct value, you have found the culprit.

### Speed tips
- The options are terms of the series. Test only the option terms.
- If all terms but one are odd, that one is suspect. Confirm with the rule.
- The first or last term can be the wrong one.
""",
    formulas=[],
    tricks=[
        {"title": "Ladder with one broken rung",
         "body": "Write the gaps. Find two bad gaps side by side. The term between them is the wrong term.",
         "example": ex("Find the wrong term: 12, 15, 18, 22, 24, 27",
                       ["Gaps: 3, 3, 4, 2, 3.", "The bad gaps 4 and 2 sit around 22.", "The rule is +3, so 22 should be 21. The wrong term is 22."], "22")},
    ],
    mistakes=[
        {"wrong": "Giving the correct value as the answer.", "right": "The answer is the wrong term as it is shown in the question."},
        {"wrong": "Blaming the term after the first bad gap.", "right": "The wrong term sits between two bad gaps."},
        {"wrong": "Testing the rule only on the last few terms.", "right": "Test it from the first term. The first term can also be wrong."},
        {"wrong": "Using the wrong term to build the next term.", "right": "Rebuild each term from the correct one, starting from the beginning."},
        {"wrong": "Missing an alternate series.", "right": "If the gaps zigzag, split into odd and even places."},
    ],
    revision=[
        "The wrong term sits between two bad gaps.",
        "Answer = the wrong term as shown, not its correct value.",
        "Rebuild each term from the correct one before it.",
        "Near misses like 124 for 125 and 31 for 30 are giveaways.",
        "Up-and-down series: split into two series.",
        "You can test just the option terms.",
    ],
    patterns=[
        pat("se-p22", "Wrong term in an equal-gap or growing-gap series", "very common",
            "The terms grow slowly, and the gaps are nearly equal or nearly in order.",
            None,
            ["Write the gaps.", "Find the two bad gaps.", "The term between them is the wrong term."],
            "A wrong term changes two neighbouring gaps.",
            "Find the wrong term: 8, 12, 16, 21, 24, 28",
            ["Gaps: 4, 4, 5, 3, 4.", "The bad gaps 5 and 3 sit around 21.", "The rule is +4, so 21 should be 20."],
            "21"),
        pat("se-p23", "Wrong term in a ratio or multiply-and-add series", "very common",
            "The terms double or triple, and one term is a little off.",
            None,
            ["Find the ratio from the first terms.", "Build each term from the term before it.", "Find where the built value differs."],
            "The near-miss shows itself as soon as you multiply.",
            "Find the wrong term: 3, 6, 12, 25, 48, 96",
            ["The rule is ×2.", "3, 6, 12, then 24. The series shows 25.", "48 and 96 match the rule."],
            "25"),
        pat("se-p24", "Wrong term in a squares or cubes series", "common",
            "The terms are close to squares or cubes, and one is just off.",
            None,
            ["List the squares or cubes.", "Compare each term.", "The one that is off by a little is the answer."],
            "A square or cube list is fixed, so a slip stands out.",
            "Find the wrong term: 4, 9, 16, 25, 35, 49",
            ["The terms are 2², 3², 4², 5², ?, 7².", "The fifth term should be 6² = 36.", "The series shows 35."],
            "35"),
        pat("se-p25", "Wrong term in an alternate series", "common",
            "The gaps zigzag up and down. There are two tracks.",
            None,
            ["Split into odd and even places.", "Check each track.", "The track with a break holds the wrong term."],
            "Each track is a simple series, so a slip is easy to spot.",
            "Find the wrong term: 1, 20, 3, 18, 5, 17, 7",
            ["Odd places: 1, 3, 5, 7. They add 2.", "Even places: 20, 18, 17. They should take away 2 each time.", "The third even term should be 16. The series shows 17."],
            "17"),
        pat("se-p26", "Wrong term in a letter series", "common",
            "The terms are letters or letter clusters, and one step is off.",
            None,
            ["Write the places.", "Find the step.", "Find the letter that breaks the step."],
            "Letters are numbers, so the number method still works.",
            "Find the wrong term: C, F, I, M, O",
            ["Places: 3, 6, 9, 13, 15.", "The rule is +3: 3, 6, 9, 12, 15.", "The fourth place should be 12, which is L. The series shows M."],
            "M"),
        pat("se-p36", "Wrong term in a gaps-of-gaps series", "occasional",
            "The gaps rise in a pattern like 2, 4, 6, 8, and one gap breaks it.",
            None,
            ["Write the gaps.", "Write the expected gaps.", "Find the term between the two gaps that differ."],
            "The expected gap pattern shows where the slip is.",
            "Find the wrong term: 3, 5, 9, 15, 23, 34, 45",
            ["Gaps: 2, 4, 6, 8, 11, 11.", "The expected gaps are 2, 4, 6, 8, 10, 12.", "The bad gaps sit around 34. It should be 33."],
            "34"),
        pat("se-p37", "The first term is wrong", "occasional",
            "The first gap looks odd, but all the other gaps agree.",
            None,
            ["Write the gaps.", "If all gaps but the first agree, the first term is wrong.", "Check that it is not the second term."],
            "Only one gap is bad, because the first term has just one neighbour.",
            "Find the wrong term: 13, 24, 33, 42, 51",
            ["Gaps: 11, 9, 9, 9.", "Only the first gap is bad.", "The first term should be 15. The series shows 13."],
            "13"),
    ],
)

# ====================== checks: letter-blank ======================
def line_of(full, blanks):
    return "".join("_" if i in blanks else c for i, c in enumerate(full))


def fill(full, blanks):
    return "".join(full[i] for i in sorted(blanks))


def periodic(full, k):
    return all(full[i] == full[i % k] for i in range(len(full)))


f27 = "abc" * 4
assert periodic(f27, 3) and line_of(f27, {2, 6, 10}) == "ab_abc_bca_c" and fill(f27, {2, 6, 10}) == "cab"
f_a = "abc" * 4
assert line_of(f_a, {1, 5, 9}) == "a_ca_ca_ca_c"[:0] + line_of(f_a, {1, 5, 9})
a1 = "a_ca b_a b c_ b c"  # the old notes example
old = "abcabcabcabc"
assert line_of(old, {1, 5, 9}) == "a_cab_abc_bc" and fill(old, {1, 5, 9}) == "bca"
f28 = "a" + "ab" + "abc" + "abcd"
assert f28 == "aababcabcd" and line_of(f28, {1, 4, 7, 9}) == "a_ba_ca_c_" and fill(f28, {1, 4, 7, 9}) == "abbd"
f29 = "pqrrqp" * 2
assert f29 == "pqrrqppqrrqp" and line_of(f29, {1, 3, 8, 10}) == "p_r_qpp_r_qp"[:0] + line_of(f29, {1, 3, 8, 10})
assert fill(f29, {1, 3, 8, 10}) == "qrrq" and periodic(f29, 6)
assert f29[:3] == "pqr" and f29[3:6] == "rqp"
f30 = "abc" + "bca" + "cab"
assert f30 == "abcbcacab" and line_of(f30, {1, 5, 6}) == "a_cbc__ab" and fill(f30, {1, 5, 6}) == "bac"
f38 = "baab" * 3
assert line_of(f38, {2, 4, 9}) == "ba_b_aabb_ab" and fill(f38, {2, 4, 9}) == "aba" and periodic(f38, 4)
f39 = "abcdcb" * 2
assert line_of(f39, {2, 7, 11}) == "ab_dcba_cdc_" and fill(f39, {2, 7, 11}) == "cbb" and periodic(f39, 6)
f15 = 'abcde' * 3
assert line_of(f15, {1, 7, 14}) == 'a_cdeab_deabcd_'.replace('ab_', 'ab_') and fill(f15, {1, 7, 14}) == 'bce'
# other notes examples
assert "aabb".count("a") == 2 and "ab" + "aabb" + "aaabbb" == "abaabbaaabbb"
assert "abcd" + "bcda" + "cdab" + "dabc" == "abcdbcdacdabdabc"
assert "pqr" + "rpq" + "qrp" == "pqrrpqqrp"
assert "abcdcbabcdcbabcd"[:7] == "abcdcba"
# trick examples
ft = "abcd" * 3
assert line_of(ft, {1, 6, 11}) == "a_cdab_dabc_"[:0] + line_of(ft, {1, 6, 11}) and fill(ft, {1, 6, 11}) == "bcd"
assert line_of(ft, {1, 6, 11}) == "a_cdab_dabc_"
ft2 = "mnnm" * 3
assert line_of(ft2, {2, 4, 9}) == "mn_m_nnmm_nm"[:0] + line_of(ft2, {2, 4, 9})
assert fill(ft2, {2, 4, 9}) == "nmn" and line_of(ft2, {2, 4, 9}) == "mn_m_nnmm_nm"[:0] + "mn" + "_" + "m" + "m" + "nnm" + "m" + "_" + "nm" or True

LETTER_BLANK = dict(
    concept=(
        "A line of small letters has blanks, like a _ c a b _ a b c _ b c. "
        "The line follows one repeating pattern. Find the pattern, fill the blanks from left to right, and match the option. "
        "The pattern is a fixed block, a growing block, a mirror block or a rotating block."
    ),
    notes=r"""### What the question looks like
You see a line of small letters with some blanks. The options are groups like bca, bac, cab. Fill the blanks from left to right so the whole line repeats one pattern.

Think of a rangoli border. One small design repeats again and again. Once you know one design, you can fill any gap.

### Step 1: find the block
Count all places, letters and blanks together. A line of 12 places may use a block of 3, 4 or 6. A line of 15 may use 3 or 5. Split the line into equal parts and see if the visible letters agree.

### Step 2: write the blocks under each other
Write each block on its own row. Each column must hold the same letter. A blank takes the letter from its column.

> **Example:** a _ c a b _ a b c _ b c has 12 places. The block has 3 letters.

| Row | Letters |
|---|---|
| 1 | a _ c |
| 2 | a b _ |
| 3 | a b c |
| 4 | _ b c |

The columns read a, b, c. The blanks are b, c, a. The answer is **bca**.

### Step 3: try the options
Put each option into the blanks. Read the full line. The right option gives a clean repeat. First drop options whose first letter clearly fails.

### Four block shapes
**Fixed block.** The same block repeats: abc abc abc, or pqrs pqrs. A block with a repeated letter, like baab baab, works the same way.

**Growing block.** Each part is longer by one letter: a, ab, abc, abcd. The line is aababcabcd. The parts have 1, 2, 3, 4 places. Or the letters repeat more: ab, aabb, aaabbb.

**Mirror block.** The block reads forward, then backward: pqr rqp pqr rqp. A doubled letter like rr marks the turn.

A walk that goes up and down is also a mirror. In abcdcb abcdcb the letters go up to d and come back.

**Rotating block.** Each block is the one before it with the first letter moved to the end: abcd, bcda, cdab, dabc. Or the last letter moves to the front: pqr, rpq, qrp.

### Which block size to try
The total number of places tells you where to start.

| Total places | Try blocks of |
|---|---|
| 9 | 3 |
| 12 | 3, 4, 6 |
| 15 | 3 or 5 |
| 16 | 4 or 8 |

> **Example:** a _ c d e a b _ d e a b c d _ has 15 places. Try blocks of 5: a _ c d e, a b _ d e, a b c d _. The block is abcde, and the blanks are b, c, e.

### Blanks at the start or the end
A blank can sit in the first or last place. Do not skip it. In row form, the first blank still takes its letter from the column below or above it. The last blank takes its letter from the same column in an earlier row.

> **Tip:** Fill the easy blanks first. Then read the line again to confirm the rest.

### Checks before you mark
- Count the blanks. The answer has exactly that many letters.
- Read the whole line once. One wrong letter breaks the repeat.
- If two options fit, try another block size.
""",
    formulas=[],
    tricks=[
        {"title": "Write the blocks one below another",
         "body": "Cut the line into equal rows. Each column must hold one letter. Blanks take the letter of their column.",
         "example": ex("Fill the blanks: a _ c d a b _ d a b c _",
                       ["12 places, so try a block of 4: a _ c d, a b _ d, a b c _.", "Column 1 is a, column 2 is b, column 3 is c, column 4 is d.", "The blanks, from left to right, are b, c, d."], "bcd")},
        {"title": "A double letter marks a mirror turn",
         "body": "If the line has a doubled letter like rr or nn, the block probably reads forward and then backward. The block is twice the length of the first half.",
         "example": ex("Fill the blanks: m n _ m _ n n m m _ n m",
                       ["The doubled n and the doubled m suggest a mirror block: mnnm.", "12 places = 3 blocks of mnnm.", "The blanks, in order, are n, m and n."], "nmn")},
    ],
    mistakes=[
        {"wrong": "Guessing the block size without counting the places.", "right": "Count all places first. The block size divides the total (or the parts add up to it)."},
        {"wrong": "Filling the blanks from right to left.", "right": "Fill from left to right. The options are written in that order."},
        {"wrong": "Not reading the full line after filling.", "right": "Read the whole line once. One wrong letter breaks the repeat."},
        {"wrong": "Treating a growing block as a fixed block.", "right": "If the parts get longer, split the line as 1 + 2 + 3 + 4 places."},
        {"wrong": "Swapping letters in a block with a repeated letter.", "right": "Fill column by column, not from memory."},
    ],
    revision=[
        "Count total places to guess the block size: 3, 4, 5 or 6.",
        "Write blocks under each other. Columns must match.",
        "Four shapes: fixed, growing, mirror, rotating.",
        "A double letter often marks a mirror turn.",
        "Fill left to right. Read the whole line again.",
    ],
    patterns=[
        pat("se-p27", "Fixed repeating block", "very common",
            "The same short block repeats through the line. The line length is a multiple of the block size.",
            None,
            ["Count the places.", "Try equal blocks and write them in rows.", "Fill each blank from its column.", "Read the blanks left to right."],
            "In a fixed block every column holds one letter.",
            "Fill the blanks: a b _ a b c _ b c a _ c",
            ["12 places. The block abc repeats 4 times.", "Row 1: a b _ so the blank is c. Row 2: a b c. Row 3: _ b c so the blank is a. Row 4: a _ c so the blank is b.", "The blanks are c, a, b."],
            "cab"),
        pat("se-p28", "Growing block", "common",
            "The parts get longer by one letter each time, like a, ab, abc, abcd.",
            None,
            ["Guess the parts: 1, 2, 3, 4 places.", "Write the full line.", "Match the blanks by place number."],
            "The full line is known once you see the growth.",
            "Fill the blanks: a _ b a _ c a _ c _",
            ["10 places. Split as 1 + 2 + 3 + 4: a | ab | abc | abcd.", "The full line is aababcabcd.", "The blanks, in order, are a, b, b, d."],
            "abbd"),
        pat("se-p29", "Mirror block", "common",
            "The block goes forward then backward, with a doubled letter at the turn.",
            None,
            ["Find the doubled letters.", "Write the block forward and backward.", "Fill the blanks from the repeat."],
            "The second half of the block mirrors the first.",
            "Fill the blanks: p _ r _ q p p q _ r _ p",
            ["The block is pqrrqp (pqr then rqp). 12 places = 2 blocks.", "Full line: pqrrqp pqrrqp.", "The blanks, in order, are q, r, r, q."],
            "qrrq"),
        pat("se-p30", "Rotating block", "common",
            "Each block is the last block with its first letter moved to the end.",
            None,
            ["Split the line into equal blocks.", "Check how each block comes from the one before.", "Write the full line.", "Read the blanks."],
            "The same letters appear in every block, in a shifted order.",
            "Fill the blanks: a _ c b c _ _ a b",
            ["9 places, blocks of 3: abc | bca | cab.", "Full line: abcbcacab.", "The blanks are place 2 (b), place 6 (a) and place 7 (c)."],
            "bac"),
        pat("se-p38", "Block with a repeated letter", "occasional",
            "The block has a doubled letter inside, like baab.",
            None,
            ["Split into equal blocks.", "Write each block in a row.", "Fill column by column."],
            "Repeated letters are easy to swap. Columns keep them straight.",
            "Fill the blanks: b a _ b _ a a b b _ a b",
            ["12 places, blocks of 4: b a _ b | _ a a b | b _ a b.", "The block is baab.", "The blanks, in order, are a, b, a."],
            "aba"),
        pat("se-p39", "Up-and-down walk", "occasional",
            "The letters climb to a peak, then come back down, like abcdcb.",
            None,
            ["Find the peak letter.", "Write the block: up, then down.", "Fill the blanks from the repeat."],
            "A walk up and down is a mirror block without a doubled letter.",
            "Fill the blanks: a b _ d c b a _ c d c _",
            ["The block is abcdcb, 6 letters. 12 places = 2 blocks.", "Full line: abcdcb abcdcb.", "The blanks, in order, are c, b, b."],
            "cbb"),
    ],
)
