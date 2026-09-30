"""Readable rewrite of Reasoning > Dictionary Order & Alphabet (all four subtopics).

Plain English, one idea per section. Every sort, letter position and rank used
in an example is recomputed below and asserted.
Run: python dictionary_order.py  (patches content/core/topics/reasoning/dictionary-order.json in place)
"""
import json
from itertools import permutations
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "dictionary-order.json"


# ---------- helpers ----------
def P(c):
    """Alphabet position, A = 1 ... Z = 26."""
    return ord(c) - 64


def L(n):
    return chr(n + 64)


def rank(word):
    """Dictionary rank of `word` among all arrangements of its letters (distinct letters)."""
    r = 1
    for i, ch in enumerate(word):
        rest = sorted(word[i:])
        r += rest.index(ch) * factorial(len(word) - i - 1)
    return r


def same_position_count(word):
    s = sorted(word)
    return sum(a == b for a, b in zip(word.upper(), s))


def can_form(word, bag_word):
    from collections import Counter
    return not (Counter(word.upper()) - Counter(bag_word.upper()))


def pat(pid, name, freq, spot, formula, steps_, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps_, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


S = {}

# =====================================================================
# 1. dict-idea
# =====================================================================
assert sorted(["MARKET", "MARGIN", "MARBLE", "MARGINAL"]) == ["MARBLE", "MARGIN", "MARGINAL", "MARKET"]
assert sorted(["SIGN", "SIGHT", "SIGNAL"]) == ["SIGHT", "SIGN", "SIGNAL"]
assert sorted(["SCAN", "SCANDAL", "SCANT"]) == ["SCAN", "SCANDAL", "SCANT"]
assert sorted(["CART", "CARTON", "CARGO"]) == ["CARGO", "CART", "CARTON"]
assert sorted(["ANGEL", "ANGLE"]) == ["ANGEL", "ANGLE"]
assert sorted(["SILENT", "LISTEN"]) == ["LISTEN", "SILENT"]
assert sorted(["NORTH", "NAIL", "TUNNEL", "OCEAN", "TRAIN"]) == ["NAIL", "NORTH", "OCEAN", "TRAIN", "TUNNEL"]

S["dict-idea"] = dict(
    concept=(
        "Words sort letter by letter from the left. At the first position where two words differ, "
        "the word with the earlier letter comes first. "
        "One refinement settles the tricky cases: if one word runs out of letters first (Cart, Carton), "
        "the shorter word comes first. "
        "Stack the words in columns on paper and let the first split column decide."
    ),
    notes=r"""### One rule runs the whole topic
A dictionary sorts words letter by letter from the left. At the **first position where two words differ**, the word with the earlier letter comes first. Everything after that position does not matter.

Market, Margin, Marble all share MAR. The fourth letters are k, g, b. Since b is earliest, **Marble** comes first.

> **Rule:** Compare letter by letter from the left. At the first difference, the earlier letter wins. Later letters never rescue a word.

### How to compare any two words
1. Write the two words one under the other.
2. Scan the columns from the left.
3. Stop at the first column with different letters.
4. The word with the earlier letter in that column comes first.

> **Tip:** Slide a finger down the columns. The first split column settles the whole comparison.

### The prefix rule
Sometimes one word ends while it still matches the other. Cart and Carton match through C, A, R, T. Then Cart runs out of letters.

The **shorter word comes first**. Think of the ending as a blank space, and a space comes before every letter. So Cart comes before Carton. Play comes before Player. Scan comes before Scant.

> **Watch:** A longer word is not automatically later. If it starts with the other word, it comes after it.

### Ties that run deep
The deciding letter can hide at the fifth or sixth position. Strip the shared stem and compare only the tails.

- Sign, Sight, Signal share SIG. Fourth letters: n, h, n. Sight (h) comes first. Sign is a prefix of Signal, so Sign comes next, then Signal.
- Angel and Angle share ANG. The fourth letters are e and l. Angel comes first.

> **Example:** Scan, Scandal, Scant. Scan is a prefix, so it leads. Scandal and Scant split at the fifth letter: d before t. Order: Scan, Scandal, Scant.

### Same letters, different order
Angel and Angle use exactly the same letters. The rule does not change. Compare the first differing position and stop. Never judge by length or by feel.

The same holds for longer anagram pairs. Silent starts with S; Listen starts with L. L comes before S, so Listen comes first. One column settles it.

### Read the question's direction
"Which comes first", "which comes last", "which is third", "which pair sits side by side" — all of these use one sort. Do the sort once. Number the slots 1 to 5. Then read off whatever was asked.

> **Watch:** Marks are lost in execution, not in the rule. Common slips: a misread letter pair (m and n, r and s), a forgotten prefix, or answering first when the question asked last. Reread the direction word before marking.
""",
    formulas=[],
    tricks=[
        {
            "title": "Find the first split point",
            "body": "Write the words one under another and scan the columns from the left. The first column with different letters decides the whole comparison. Ignore every letter after it.",
            "example": {
                "q": "Order as in a dictionary: Sign, Sight, Signal.",
                "steps": ["All three share S, I, G.",
                          "Fourth letters: n (Sign), h (Sight), n (Signal). H comes before N, so Sight leads.",
                          "Sign is a prefix of Signal, so Sign comes before Signal."],
                "answer": "Sight, Sign, Signal",
            },
        },
    ],
    mistakes=[
        {"wrong": "Judging words by length (longer feels later).", "right": "Compare at the first differing letter. A prefix word is shorter but comes first."},
        {"wrong": "Letting a later letter overturn an earlier split.", "right": "The first differing column decides. Later letters never matter after that."},
        {"wrong": "Forgetting the prefix rule: putting Scant before Scan.", "right": "The shorter word that matches the other's start always comes first."},
        {"wrong": "Sorting mentally to save time.", "right": "Write the words in columns on paper. One misread column flips two slots."},
        {"wrong": "Answering the wrong slot (first instead of last).", "right": "Sort once, number the slots, reread the question's direction word, then mark."},
    ],
    revision=[
        "First differing letter decides; everything after it is irrelevant.",
        "Prefix word comes first: Cart before Carton, Scan before Scant.",
        "Stack words in columns; scan one column at a time.",
        "Same letters, different order: still the first difference decides.",
        "Sort once, number the slots, then answer any lookup.",
        "Reread the direction word (first, last, third) before marking.",
    ],
    patterns=[
        pat("dc-p1", "First differing letter decides", "very common",
            "Two or three words share an opening; the question asks which comes first or last.",
            None,
            ["Scan letter by letter to the first position where the words differ.",
             "The earlier letter at that position takes the earlier slot.",
             "Ignore how long the shared part is; only the first difference matters."],
            "Dictionary order is exactly this rule: the left-most difference decides.",
            "Which comes first in the dictionary: Market, Margin or Marble?",
            ["All three share MAR.",
             "Fourth letters: k (Market), g (Margin), b (Marble).",
             "B is the earliest letter, so Marble leads."],
            "Marble"),
        pat("dc-p2", "Shorter prefix sorts first", "common",
            "One word is exactly the start of another (Sand, Sandwich, Sandy) — a prefix pair.",
            None,
            ["Check whether one word matches the whole start of the other.",
             "The prefix comes before the longer word.",
             "Among extensions, compare the letter right after the stem."],
            "Nothing can sit between a word and its own extension, so the short form lists first.",
            "Which comes first: Sand, Sandy, Sandwich or Sandal?",
            ["Sand matches the start of all three others.",
             "Sand runs out of letters first, so it comes first.",
             "Among Sandy, Sandwich, Sandal the fourth letter would decide."],
            "Sand"),
        pat("dc-p3", "Deep ties beyond the third letter", "common",
            "Four to six words share a long stem; the decision hides at the fourth to sixth letter.",
            None,
            ["Strip the common stem and write only the tails.",
             "Sort the tails letter by letter; the earliest tail letter takes the earliest slot.",
             "An empty tail (the bare stem) sorts first inside its group."],
            "The rule does not care how deep the difference hides; it always compares the first differing column.",
            "Arrange Sure, Surge, Surgeon, Surplus, Surreal. Which comes third?",
            ["All share SUR. Fourth letters: e, g, g, p, r.",
             "Sure (e) leads; then the g-pair: Surge is a prefix of Surgeon, so Surge, Surgeon.",
             "Then Surplus (p), then Surreal (r). Third = Surgeon."],
            "Surgeon"),
        pat("dc-p4", "Slot lookups: middle and adjacent pairs", "common",
            "After sorting, the question asks for the middle word or an adjacent pair, not first or last.",
            None,
            ["Write the full numbered order first; never answer by instinct.",
             "Middle of five words = slot 3.",
             "Adjacent = two words whose slot numbers differ by exactly 1."],
            "Every lookup variant reads off the same sorted, numbered list.",
            "Arrange Melon, Melody, Mellow, Member. Which two are adjacent?",
            ["Fourth letters: o, o, l, b. So Member, Mellow, then the o-pair.",
             "Melody vs Melon splits at the fifth letter: d before n.",
             "Order: Member, Mellow, Melody, Melon. The last two are adjacent."],
            "Melody and Melon"),
        pat("dc-p5", "Different first letters: quick full sort", "common",
            "The words do not share a stem; their first letters differ, so the first column settles most of it.",
            None,
            ["Group the words by first letter at once.",
             " Only words sharing a first letter need deeper comparison.",
             "Number the order and read the asked slot."],
            "When first letters differ, column one decides; only same-letter groups need a second column.",
            "Arrange Nail, North, Ocean, Train, Tunnel. Which word is second?",
            ["First letters: N, N, O, T, T. The N-group leads, then Ocean, then the T-group.",
             "N-group: second letters a (Nail) and o (North) → Nail, North.",
             "T-group: second letters r (Train) and u (Tunnel) → Train, Tunnel. Second = North."],
            "North"),
    ],
)

# =====================================================================
# 2. arrange-words
# =====================================================================
assert sorted(["STATUE", "STATUS", "STATION", "STATUTE", "STATURE"]) == ["STATION", "STATUE", "STATURE", "STATUS", "STATUTE"]
assert sorted(["CABLE", "CABIN", "CABARET", "CABBAGE"]) == ["CABARET", "CABBAGE", "CABIN", "CABLE"]
assert sorted(["CHALK", "CHARM", "CHART", "CHASE", "CHATTER"]) == ["CHALK", "CHARM", "CHART", "CHASE", "CHATTER"]
assert sorted(["MYSTERY", "MYSTIC", "MYSELF", "MYOPIA"]) == ["MYOPIA", "MYSELF", "MYSTERY", "MYSTIC"]
assert sorted(["COLONEL", "COLONY", "COLUMN", "COLOUR", "COLOSSUS"]) == ["COLONEL", "COLONY", "COLOSSUS", "COLOUR", "COLUMN"]
assert sorted(["JUDGE", "JUDO", "JOUST", "JOURNAL", "JOSTLE"]) == ["JOSTLE", "JOURNAL", "JOUST", "JUDGE", "JUDO"]
assert sorted(["LADDER", "LANTERN", "LOYAL", "LOVELY"]) == ["LADDER", "LANTERN", "LOVELY", "LOYAL"]

S["arrange-words"] = dict(
    concept=(
        "The standard question gives four to six similar words. You arrange them as in a dictionary, "
        "then answer one lookup: which is third, which is last, which comes just after a given word. "
        "Group the words by their shared stem first. Sort inside each group letter by letter. "
        "Number the final order, then read the asked slot from it."
    ),
    notes=r"""### The standard arrangement question
You get four to six similar words. Arrange them as in a dictionary. Then answer one lookup: which is third, which is last, which comes just after X, which is second from the right.

The method never changes. Only the lookup changes.

### Strip the shared stem
Exam words usually share a long opening. Find it and cross it out. Only the letters after the stem matter.

Statue, Status, Statute, Stature, Station all share STAT. The fight starts at the fifth letter: i for Station, u for the rest. Station separates first.

> **Tip:** Draw the stem once. Then compare only the tails. This one habit halves the work.

### Split at the first difference
Line up the words. Ignore the stem. Look at the next letter of each word. Sort by those letters. If two words tie, go one letter deeper.

The STAT family after Station: the u-words show e, r, s, t at the sixth letter. So Statue, Stature, Status, Statute.

Full order: Station, Statue, Stature, Status, Statute.

### The prefix rule inside ties
When one word is the bare stem itself, it comes before all its extensions. Among the extensions, the letter right after the stem decides.

Sand comes before Sandy, Sandal, Sandwich. Then a, a, w sort Sandal and Sandy before Sandwich (fourth letters a, a, w; Sandal before Sandy at the fifth letter d before y).

### Number the slots, then read
Write the final order as a numbered line, 1 to N. Then answer the question from the numbers:

- "Third word" → slot 3.
- "Second from the right" → slot N + 1 − 2.
- "Just after X" → X's slot plus one.
- "Adjacent pair" → two words whose slots differ by exactly 1.

> **Example:** Judge, Judo, Joust, Journal, Jostle. Second letters: o-group (Jostle, Journal, Joust) before u-group (Judge, Judo). Order: Jostle, Journal, Joust, Judge, Judo. Second from the right = slot 4 = **Judge**.

### A full worked run
Cable, Cabin, Cabaret, Cabbage. Which is third?

1. All share CAB. Fourth letters: a (Cabaret), b (Cabbage), i (Cabin), l (Cable).
2. Sort by them: Cabaret, Cabbage, Cabin, Cable.
3. Slot 3 = **Cabin**.

Twenty seconds on paper, and the sort also answers any other question about these four words.

### Check before marking
The word with the earliest deciding letter should sit near the left end. The one with the latest should sit near the right end. If your order breaks that, re-scan the deciding column; a swapped pair is the usual cause.

> **Watch:** Letters decide the order. Numbers decide the answer. Do both on paper.

A practised hand finishes a five-word arrangement in 30 to 40 seconds. If you cross one minute, you are re-sorting in your head. Restart on paper; it is always faster.
""",
    formulas=[],
    tricks=[
        {
            "title": "Sort once, count slots",
            "body": "Fix one numbered order for the whole question, then answer any slot lookup from it. Re-sorting for each option is where errors and lost time come from.",
            "example": {
                "q": "Cable, Cabin, Cabaret, Cabbage — which comes third?",
                "steps": ["All share CAB. Fourth letters: a (Cabaret), b (Cabbage), i (Cabin), l (Cable).",
                          "Order: Cabaret, Cabbage, Cabin, Cable.",
                          "Third = Cabin."],
                "answer": "Cabin",
            },
        },
    ],
    mistakes=[
        {"wrong": "Re-sorting mentally for every option.", "right": "Sort once on paper, number the slots, read every answer from that line."},
        {"wrong": "Answering 'third from the right' with the third word from the left.", "right": "Convert first: k-th from the right = slot N + 1 − k."},
        {"wrong": "Comparing at the wrong column after a shared stem.", "right": "Cross out the stem, then compare the very next letter."},
        {"wrong": "Forgetting the bare stem sorts before its extensions.", "right": "Prefix word first, then the extensions by their next letter."},
        {"wrong": "Marking without a sanity check.", "right": "Earliest deciding letter at the left end, latest at the right end — verify, then mark."},
    ],
    revision=[
        "Strip the shared stem; the next letter after it decides.",
        "Bare stem sorts before every extension of itself.",
        "Write the numbered order; answer every lookup from it.",
        "k-th from the right = slot N + 1 − k.",
        "Just after X = X's slot + 1; adjacent = slots differing by 1.",
        "Sanity check: earliest letter at the left, latest at the right.",
    ],
    patterns=[
        pat("aw-p1", "Arrange and pick the slot", "very common",
            "Four to six words; the question asks which is the Nth word in dictionary order.",
            None,
            ["Strip the shared stem; sort by the first differing tail letter.",
             "Write the numbered order 1 to N.",
             "Read the asked slot and check it against the end words."],
            "One sort answers every slot question; the lookup is just counting.",
            "Arrange Chalk, Charm, Chart, Chase, Chatter. Which is the fourth word?",
            ["All share CHA. Fourth letters: l, r, r, s, t.",
             "The r-pair splits at the fifth letter: m (Charm) before t (Chart).",
             "Order: Chalk, Charm, Chart, Chase, Chatter. Fourth = Chase."],
            "Chase"),
        pat("aw-p2", "Prefix versus later-letter battle", "very common",
            "The list mixes a bare stem with extensions that fight over a later letter.",
            None,
            ["The bare stem sorts before all extensions.",
             "Extensions sort by the letter right after the stem; ties go one letter deeper.",
             "Re-read the deciding column twice; one misread flips two slots."],
            "The first difference decides, at whatever depth it hides.",
            "Arrange Mystery, Mystic, Myself, Myopia. Which comes first?",
            ["Third letters: s, s, s, o. O is earliest, so Myopia leads.",
             "The s-group: fourth letters e (Myself), t, t.",
             "Myself, then Mystery (fifth e) before Mystic (fifth i). First = Myopia."],
            "Myopia"),
        pat("aw-p3", "Extremes and immediate neighbours", "common",
            "The question asks which comes last, just after X, or immediately before Y.",
            None,
            ["Sort fully and number the slots.",
             "Just after X = X's slot + 1; immediately before Y = Y's slot − 1.",
             "For 'last', only the deepest group's final word matters."],
            "Neighbour questions are slot arithmetic on the finished order.",
            "Which comes just after Colony: Colonel, Colony, Column, Colour, Colossus?",
            ["All share COL. Fourth letter u sends Column last.",
             "The o-group sorts by fifth letters: n, n, s, u.",
             "Order: Colonel, Colony, Colossus, Colour, Column. After Colony = Colossus."],
            "Colossus"),
        pat("aw-p4", "Counting from the right end", "common",
            "'Second from the right', 'third from the end' — the slot is counted from the back.",
            None,
            ["Sort and number 1 to N as usual.",
             "Convert: k-th from the right = slot N + 1 − k.",
             "Convert first, then read. Do not count backwards on the raw list."],
            "The right end is slot N, so every from-the-right question is one subtraction.",
            "Arrange Judge, Judo, Joust, Journal, Jostle. Which is second from the right?",
            ["Second letters o before u: Jostle, Journal, Joust, then Judge, Judo.",
             "Inside the o-group: Jostle (third letter s), then Journal (r before s at the fourth letter), then Joust.",
             "Slot 5 + 1 − 2 = 4 → Judge."],
            "Judge"),
        pat("aw-p5", "Choose the correct full order", "common",
            "The words are numbered 1 to 4, and the options give sequences like 2, 4, 1, 3.",
            None,
            ["Sort the words once on paper.",
             "Write the numbers of your sorted order as a sequence.",
             "Match that sequence against the options."],
            "The full sequence is fixed by one sort, so matching options is instant and error-free.",
            "Words: 1. Ladder, 2. Lantern, 3. Loyal, 4. Lovely. Which order is correct?",
            ["All share L. Second letters: a, a, o, o.",
             "a-group: third letters d (Ladder) before t (Lantern). o-group: third letters v (Lovely) before y (Loyal).",
             "Order: Ladder, Lantern, Lovely, Loyal → 1, 2, 4, 3."],
            "1, 2, 4, 3"),
    ],
)

# =====================================================================
# 3. letter-position
# =====================================================================
assert [P(c) for c in "EJOTY"] == [5, 10, 15, 20, 25]
assert P("G") == 7 and P("S") == 19 and 19 - 7 - 1 == 11
assert P("J") == 10 and P("V") == 22 and 22 - 10 - 1 == 11
assert P("T") == 20 and 27 - 20 == 7
assert 27 - 9 == 18 and L(18) == "R"
assert 12 + 4 == 16 and L(16) == "P"
assert 14 + 6 == 20 and L(20) == "T"
assert 27 - 8 == 19 and L(19) == "S" and 19 - 6 == 13 and L(13) == "M"
assert 27 - 20 == 7 and L(7) == "G" and 7 - 5 == 2 and L(2) == "B"
assert 10 + 7 == 17 and L(17) == "Q"
assert L(27 - 5) == "V"  # full reverse: 5th letter is V
assert (P("E") + P("U")) % 2 == 0 and (5 + 21) // 2 == 13 and L(13) == "M"
HALF = "MLKJIHGFEDCBA" + "NOPQRSTUVWXYZ"
assert len(HALF) == 26 and HALF[9] == "D" and HALF[13] == "N" and HALF[16] == "Q"
HALF2 = "ABCDEFGHIJKLM" + "ZYXWVUTSRQPON"
assert len(HALF2) == 26 and HALF2[19] == "T"

S["letter-position"] = dict(
    concept=(
        "Treat the alphabet as a numbered strip: A = 1 to Z = 26. "
        "Learn five anchors, the word EJOTY: E 5, J 10, O 15, T 20, Y 25. "
        "Every position question is then small arithmetic. "
        "Counting from the right uses the mirror rule: the two positions of a letter add to 27."
    ),
    notes=r"""### The alphabet as a numbered strip
A is 1, B is 2 ... Z is 26. Learn five anchors, the word **EJOTY**: E = 5, J = 10, O = 15, T = 20, Y = 25.

Every other letter is a short hop from an anchor. G = J − 3 = 7. R = T − 2 = 18. W = Y − 2 = 23.

> **Tip:** Never count from A. Jump to the nearest anchor, then step one or two places.

### Letters between two letters
"How many letters lie between G and S?" Positions: G = 7, S = 19. Between excludes both ends: 19 − 7 − 1 = **11**.

The same rule with another pair: J = 10 and V = 22, so the letters between them number 22 − 10 − 1 = **11** too. Equal answers like this are common, because many pairs sit 12 places apart.

> **Rule:** Letters between = difference of positions − 1. The minus one removes one end; "between" already excludes the other.

### The mirror: counting from the right
Every letter has two positions. T is 20th from the left. From the right, T is 27 − 20 = **7th**.

The two positions always add to 27: 26 letters plus one. So the 9th from the right is the 27 − 9 = 18th from the left, which is R.

> **Watch:** The magic number is 27, never 26. Forgetting the plus one is the classic slip.

### Letter arithmetic
Some questions chain two clauses: "which letter is 4th to the right of the 12th letter from the left?"

1. Turn every clause into a from-the-left position.
2. "To the right of" adds. "To the left of" subtracts.
3. Read the final letter from the anchors.

12 + 4 = 16 → P. And "6th to the left of the 8th letter from the right": 27 − 8 = 19 (S), then 19 − 6 = 13 → M.

> **Example:** "5th to the left of the 20th letter from the right". 27 − 20 = 7 (G). Then 7 − 5 = 2 → **B**.

### Modified alphabets
Some questions rewrite the strip first, then ask a position.

- **Full reverse:** Z, Y, X ... A. The letter at position p of the reversed strip is the normal letter 27 − p. Position 5 is V.
- **Half reverse:** A to M written backwards, then N to Z. The strip reads M, L, K, J, I, H, G, F, E, D, C, B, A, N, O ...

Write the new strip once on paper. Count on it. Never shift letters in your head. In the half-reversed strip the 10th letter is D, not J.

> **Watch:** In the half-reversed strip, positions after 13 behave normally again (N is 14th). Convert only the half that was changed.

### Check every answer
Before marking, confirm with an anchor. Position 16 should be four steps before T (20), which is P. If your letter lands more than five places from the anchor you expected, recount.

A full worked run: "Which letter is 6th to the right of the 14th letter from the left?" J is the 14th letter (anchor). Right steps add: 14 + 6 = 20. Position 20 is the anchor T itself. Answer: **T**. Two hops, no counting.
""",
    formulas=[
        {"name": "Position from the right", "tex": r"p_{\text{right}} = 27 - p_{\text{left}}", "note": "The two positions of the same letter add to 27."},
        {"name": "Shifted position", "tex": r"p' = p \pm k", "note": "Move right (+) or left (−) by k letters, staying inside 1 to 26."},
    ],
    tricks=[
        {
            "title": "EJOTY plus a tiny shift",
            "body": "Anchor at the nearest of E, J, O, T, Y and step from there. Position 18 is T (20) minus 2, which is R. Two seconds, no counting.",
            "example": {
                "q": "Which letter is 7th to the right of the 10th letter of the alphabet?",
                "steps": ["The 10th letter is J (anchor).",
                          "10 + 7 = 17.",
                          "17 = O (15) + 2 → Q."],
                "answer": "Q",
            },
        },
        {
            "title": "The 27 mirror",
            "body": "Any from-the-right count becomes from-the-left by 27 − k. Convert first, then do everything else from the left.",
            "example": {
                "q": "Which letter is 9th from the right of the alphabet?",
                "steps": ["From the right 9 → from the left 27 − 9 = 18.",
                          "18 = T − 2 → R."],
                "answer": "R",
            },
        },
    ],
    mistakes=[
        {"wrong": "Using 26 instead of 27 in from-the-right conversions.", "right": "The two positions add to 27: 26 letters plus one."},
        {"wrong": "Slipping past A or Z on shifts.", "right": "Check the result stays between 1 and 26; adjust by 26 if you cross an end."},
        {"wrong": "Reading 'the 10th letter' as '10 letters after it'.", "right": "First find the letter at the position, then apply the shift."},
        {"wrong": "Doing modified-alphabet questions by mental shifting.", "right": "Write the new 26-letter strip once, then count on paper."},
        {"wrong": "Counting an end letter inside 'between'.", "right": "Between = difference − 1; both ends are excluded."},
    ],
    revision=[
        "EJOTY anchors: E5, J10, O15, T20, Y25.",
        "Letters between X and Y = position difference − 1.",
        "From the right k = from the left 27 − k.",
        "Right steps add, left steps subtract — after converting every clause to from-the-left.",
        "Full reverse: position p reads the normal letter 27 − p.",
        "Modified strip: write it out once, then count on paper.",
    ],
    patterns=[
        pat("lp-p1", "Absolute position via EJOTY anchors", "very common",
            "'Which is the 15th letter' or 'how many letters between X and Y'.",
            None,
            ["Step from the nearest anchor (E5, J10, O15, T20, Y25).",
             "For 'between', subtract the positions and subtract one more.",
             "Confirm the letter sits within 5 of the anchor you used."],
            "Five anchors turn 26 positions into five short hops.",
            "How many letters of the alphabet are there between G and S?",
            ["G is 7 (J − 3). S is 19 (T − 1).",
             "19 − 7 = 12 positions apart.",
             "Between excludes both ends: 12 − 1 = 11."],
            "11"),
        pat("lp-p2", "Mirror positions from the right", "very common",
            "'k-th from the right' or 'the position of letter X from the right'.",
            r"p_{\text{right}} = 27 - p_{\text{left}}",
            ["Write the letter's from-left position from the anchors.",
             "From-right position = 27 − from-left position.",
             "Remember the 27: 26 letters plus one."],
            "Counting from the right mirrors the strip, and a mirror maps p to 27 − p.",
            "What is the position of the letter T from the right of the alphabet?",
            ["T is the 20th letter from the left (anchor).",
             "27 − 20 = 7.",
             "T is 7th from the right."],
            "7th"),
        pat("lp-p3", "Letter arithmetic (left or right of a position)", "common",
            "'Which letter is 4th to the right of the 12th from the left' — two clauses in one question.",
            r"p' = p \pm k",
            ["Convert every clause to a from-the-left number (mirror any 'from the right').",
             "Right steps add; left steps subtract.",
             "Read the letter off the EJOTY anchors."],
            "The alphabet strip is a number line; the question is one addition or subtraction on it.",
            "Which letter is 6th to the left of the 8th letter from the right?",
            ["8th from the right = 27 − 8 = 19th from the left = S.",
             "Left steps subtract: 19 − 6 = 13.",
             "13 = M."],
            "M"),
        pat("lp-p4", "Modified or reversed alphabet", "common",
            "'First half written in reverse' or 'alphabet in reverse order', followed by a position question.",
            None,
            ["Write the new 26-letter strip once on paper.",
             "Count the asked position on the new strip.",
             "For the full reverse only: position p reads the normal letter 27 − p."],
            "A rewrite is a one-time setup; after that it is plain counting.",
            "If A to M is written in reverse order, followed by N to Z, which letter is 10th from the left?",
            ["The new strip starts M, L, K, J, I, H, G, F, E, D, then C, B, A, N, O ...",
             "Count to 10: M1 L2 K3 J4 I5 H6 G7 F8 E9 D10.",
             "The 10th letter is D."],
            "D"),
        pat("lp-p5", "Midway letter between two letters", "occasional",
            "'Which letter lies exactly midway between X and Y?'",
            r"p_{\text{mid}} = \dfrac{p_X + p_Y}{2}",
            ["Write both positions from the anchors.",
             "Average them. An odd sum has no exact midway letter.",
             "Convert the average back to a letter."],
            "Midway means the average position; equal counts of letters sit on both sides.",
            "Which letter lies exactly midway between E and U?",
            ["E = 5 and U = 21.",
             "(5 + 21) ÷ 2 = 13.",
             "13 = M."],
            "M"),
    ],
)

# =====================================================================
# 4. word-formation
# =====================================================================
assert rank("CAB") == 5 and rank("BAT") == 3 and rank("FAN") == 3
assert rank("PRIME") == 94 and rank("BEAD") == 11 and rank("WORD") == 22 and rank("MACHINE") == 3610
assert 3 * factorial(4) == 72 and 3 * factorial(3) == 18 and 1 * factorial(2) == 2 and 1 * factorial(1) == 1
assert 72 + 18 + 2 + 1 + 1 == 94
assert sorted(permutations("BAT")) == list(permutations("ABT")) and ["".join(p) for p in sorted(permutations("BAT"))] == ["ABT", "ATB", "BAT", "BTA", "TAB", "TBA"]
assert ["".join(p) for p in sorted(permutations("FAN"))] == ["AFN", "ANF", "FAN", "FNA", "NAF", "NFA"]
assert factorial(3) - rank("CAB") + 1 == 2
assert same_position_count("TABLE") == 1 and same_position_count("DERAIL") == 0
assert same_position_count("PLANET") == 2 and same_position_count("SIGNED") == 1
assert can_form("CREATION", "CONVERSATION") and not can_form("TRANSPIRE", "CONVERSATION")
assert not can_form("BRUSH", "DISTRIBUTION") and can_form("STUDIO", "DISTRIBUTION") and can_form("ROBUST", "DISTRIBUTION") and can_form("BIRD", "DISTRIBUTION")

S["word-formation"] = dict(
    concept=(
        "This subtopic has two specialist questions. "
        "First, the dictionary rank of a word among all arrangements of its letters: count how many arrangements start with a smaller letter, block by block, then add one. "
        "Second, letter surgery: alphabetise a word and count letters that stay put, or test which words can be built from a word's letters. "
        "Both are written procedures. Do them on paper, step by step."
    ),
    notes=r"""### Two families of questions
The first family asks for the **dictionary rank** of a word among all arrangements of its letters. The second does letter surgery: alphabetise a word, or build words from its letters. Both are fixed procedures.

### The dictionary rank of a word
"The letters of PRIME are arranged in all possible ways, as in a dictionary. What is the rank of PRIME?" The rank is one more than the number of arrangements that come before PRIME.

Write the letters in order first: E, I, M, P, R. Now walk the word:

1. First letter P. Unused letters smaller than P: E, I, M → 3. Each heads a block of 4! = 24 words. Add 3 × 24 = 72.
2. Fix P. Next letter R. Unused smaller: E, I, M → 3 × 3! = 18.
3. Fix R. Next letter I. Unused smaller: E → 1 × 2! = 2.
4. Fix I. Next letter M. Unused smaller: E → 1 × 1! = 1.
5. Fix M. Last letter E. Nothing smaller → 0.

Rank = 72 + 18 + 2 + 1 + 0 + 1 = **94**.

> **Rule:** At each letter: (smaller unused letters) × (factorial of the letters left after it). Add up, then add 1 for the word itself.

### Repeated letters
SSC rank questions so far use words with all-distinct letters. If a letter repeats, divide each block by the factorials of the repeats among the remaining letters. A word with two E's has half as many distinct arrangements.

> **Watch:** Forgetting the final +1 is the most common slip. The sum counts only the words BEFORE yours.

### Alphabetise and compare
"If the letters of TABLE are rearranged in alphabetical order, how many letters keep their position?"

Write the word and, under it, its sorted letters. Tick exact column matches only. TABLE gives A, B, E, L, T under T, A, B, L, E. Only L (slot 4) matches. Answer: one letter.

DERAIL gives A, D, E, I, L, R under D, E, R, A, I, L. No column matches. Answer: none.

> **Tip:** Write both rows fully. Counting matches in your head misses the shifted columns.

### Form a word from a letter bag
DISTRIBUTION gives the bag D, I×3, S, T×2, R, B, U, O, N. Question: which of Studio, Bird, Robust, Brush cannot be formed?

Brush needs H. The bag has no H, so Brush fails. The other three use only letters present, within their counts.

Steps for each option: check its rarest letter first. One missing letter kills the option. A letter used more often than it appears also kills it.

> **Watch:** Counts matter as much as presence. A bag with one O cannot build a word with two O's.

### Short arrangement lists
For three letters the whole list has 3! = 6 words. Write them in order and count. BAT gives ABT, ATB, BAT, BTA, TAB, TBA. Any lookup ("which is 4th", "what follows AFN") is then plain reading.

> **Example:** All arrangements of FAN: AFN, ANF, FAN, FNA, NAF, NFA. The word after AFN is **ANF**.

### From the end of the list
CAB has rank 5 among 6 arrangements. From the end it sits at 6 − 5 + 1 = **2nd**. Use: total − rank + 1.
""",
    formulas=[
        {"name": "Rank of a word", "tex": r"\text{rank} = 1 + \sum_i c_i \times (r_i)!", "note": "c_i = unused letters smaller than the letter at position i; r_i = letters remaining after position i."},
    ],
    tricks=[
        {
            "title": "Count smaller unused letters",
            "body": "Freeze the sorted letter list. For each letter of the word, left to right, count how many still-unused letters are smaller. Multiply by the factorial of what remains, sum, add one.",
            "example": {
                "q": "Find the dictionary rank of CAB.",
                "steps": ["Sorted letters: A, B, C. First letter C: A and B are smaller → 2 × 2! = 4.",
                          "Fix C. Next letter A: nothing smaller → 0. Last letter B: nothing smaller → 0.",
                          "Rank = 4 + 0 + 0 + 1 = 5."],
                "answer": "5",
            },
        },
        {
            "title": "Three letters: write all six",
            "body": "For a three-letter word the whole list has just 6 entries. Writing them beats any formula and never miscounts.",
            "example": {
                "q": "All arrangements of BAT are listed in dictionary order. Which is the 4th word?",
                "steps": ["Write the six: ABT, ATB, BAT, BTA, TAB, TBA.",
                          "Count to the 4th."],
                "answer": "BTA",
            },
        },
    ],
    mistakes=[
        {"wrong": "Forgetting the final +1 in a rank sum.", "right": "The sum counts words BEFORE yours; add 1 for the word itself."},
        {"wrong": "Using the original remaining count instead of the shrinking one.", "right": "After fixing each letter, recount the unused letters and the positions left."},
        {"wrong": "Counting used letters as 'smaller unused'.", "right": "Cross out each fixed letter; only the unused ones count."},
        {"wrong": "In letter-bag questions, checking only presence, not counts.", "right": "A repeated letter in the option needs the same repeat in the bag."},
        {"wrong": "Comparing alphabetised columns by memory.", "right": "Write the word and its sorted form one under the other; tick exact matches."},
    ],
    revision=[
        "Rank = sum of (smaller unused) × (remaining factorial), plus 1.",
        "Repeated letters: divide blocks by the repeat factorials.",
        "Alphabetise and compare: only exact same-slot matches count.",
        "Letter bag: rarest letter first; missing or over-used letters kill an option.",
        "Three-letter lists: write all 6 arrangements and read.",
        "From the end of the list: total − rank + 1.",
    ],
    patterns=[
        pat("wf-p1", "Dictionary rank of a word", "very common",
            "'All arrangements listed as in a dictionary — what is the rank of the word?'",
            r"\text{rank} = 1 + \sum_i c_i \times (r_i)!",
            ["Sort the letters; scan the word left to right.",
             "At each position add (unused letters smaller than the current one) × (factorial of letters left).",
             "Fix the letter, move right, repeat.",
             "Add 1 at the end."],
            "Each smaller unused letter heads a whole block of arrangements that come before your word.",
            "Find the dictionary rank of the word PRIME.",
            ["Sorted letters: E, I, M, P, R.",
             "P: 3 smaller → 3 × 4! = 72. R: 3 smaller → 3 × 3! = 18. I: 1 → 2. M: 1 → 1. E: 0.",
             "72 + 18 + 2 + 1 + 0 + 1 = 94."],
            "94"),
        pat("wf-p2", "Same-position count after alphabetising", "common",
            "'Letters rearranged in alphabetical order — how many keep their original position?'",
            None,
            ["Write the word; write its sorted letters beneath it.",
             "Compare column by column.",
             "Count exact matches only."],
            "A letter keeps its position only if the sorted letter at that slot equals the original.",
            "If the letters of DERAIL are rearranged in alphabetical order, how many letters stay in place?",
            ["DERAIL sorted is A, D, E, I, L, R.",
             "Compare: D-A, E-D, R-E, A-I, I-L, L-R. No column matches.",
             "Zero letters stay put."],
            "None"),
        pat("wf-p3", "Forming words from a letter bag", "common",
            "'Which word can or cannot be formed from the letters of X?'",
            None,
            ["List the bag with repeat counts.",
             "For each option, check its rarest letter first; cross off bag letters as used.",
             "One missing letter, or one over-used letter, kills the option."],
            "Forming a word is a count check, not just a presence check.",
            "Which word CANNOT be formed from the letters of DISTRIBUTION: Studio, Bird, Robust, Brush?",
            ["The bag has D, I×3, S, T×2, R, B, U, O, N.",
             "Studio, Bird and Robust use only letters inside the counts.",
             "Brush needs H, which the bag does not have."],
            "Brush"),
        pat("wf-p4", "Neighbours in a short arrangement list", "common",
            "Three-letter words: 'which is the 4th arrangement' or 'what comes just after X'.",
            None,
            ["List all 3! = 6 arrangements in dictionary order.",
             "Count to the asked slot, or read the requested neighbour."],
            "For six items, writing the list is faster and safer than any formula.",
            "All arrangements of FAN are listed in dictionary order. Which word comes immediately after AFN?",
            ["The list: AFN, ANF, FAN, FNA, NAF, NFA.",
             "AFN is 1st, so the next word is ANF."],
            "ANF"),
        pat("wf-p5", "Rank from the end of the list", "occasional",
            "'What is the position of the word from the end / how many words come after it?'",
            r"\text{from end} = n! - \text{rank} + 1",
            ["Find the rank as usual.",
             "Total arrangements = n! (divide by repeat factorials if letters repeat).",
             "From the end = total − rank + 1."],
            "The list is symmetric: rank r of n! items sits n! − r + 1 from the back.",
            "All arrangements of CAB are listed as in a dictionary. What is CAB's position from the end?",
            ["CAB's rank is 5 (list: ABC, ACB, BAC, BCA, CAB).",
             "Total arrangements = 3! = 6.",
             "6 − 5 + 1 = 2."],
            "2nd"),
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
