"""Readable rewrite of Reasoning > Coding-Decoding (all 7 subtopics).

Every code in every example is produced by implementing the rule below and asserting
it equals the answer text. Sentence-code puzzles are checked by brute force over all
word-to-code matchings.
Run: python coding_decoding.py  (patches content/core/topics/reasoning/coding-decoding.json in place)
"""
import json
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "coding-decoding.json"

# ---------------- rule engine ----------------
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VOWELS = set("AEIOU")


def p(c):
    return ord(c) - 64


def L(n):
    return ABC[(n - 1) % 26]


def shift(w, d):
    ds = list(d) if isinstance(d, (list, tuple)) else [d] * len(w)
    assert len(ds) == len(w)
    return "".join(L(p(c) + k) for c, k in zip(w, ds))


def diffs(w, c):
    return [((p(y) - p(x)) + 12) % 26 - 12 for x, y in zip(w, c)]


def opp(w):
    return "".join(L(27 - p(c)) for c in w)


def rev(w):
    return w[::-1]


def pair_swap(w):
    out = []
    for i in range(0, len(w) - 1, 2):
        out += [w[i + 1], w[i]]
    if len(w) % 2:
        out.append(w[-1])
    return "".join(out)


def halves_rev(w):
    h = len(w) // 2
    if len(w) % 2 == 0:
        return w[:h][::-1] + w[h:][::-1]
    return w[:h][::-1] + w[h] + w[h + 1:][::-1]


def halves_swap(w):
    h = len(w) // 2
    if len(w) % 2 == 0:
        return w[h:] + w[:h]
    return w[h + 1:] + w[h] + w[:h]


def first_last(w, mid_shift=0):
    return w[-1] + shift(w[1:-1], mid_shift) + w[0]


def vowel_cons(w, dv, dc):
    return "".join(L(p(c) + (dv if c in VOWELS else dc)) for c in w)


def psum(w):
    return sum(p(c) for c in w)


def rsum(w):
    return sum(27 - p(c) for c in w)


def wsum(w):
    return sum((i + 1) * p(c) for i, c in enumerate(w))


def side_by_side(w):
    return "".join(str(p(c)) for c in w)


def solve_sentences(pairs):
    """All word->code matchings consistent with every sentence (code order jumbled)."""
    words = sorted({w for s, _ in pairs for w in s.split()})
    codes = sorted({x for _, c in pairs for x in c.split()})
    assert len(words) == len(codes), (words, codes)
    sols = []
    for perm in permutations(codes):
        m = dict(zip(words, perm))
        if all({m[w] for w in s.split()} == set(c.split()) for s, c in pairs):
            sols.append(m)
    assert sols, "inconsistent puzzle"
    return {w: sorted({m[w] for m in sols}) for w in words}


def chain(links, real):
    """'is called' chain: links maps real thing -> its new name."""
    return links[real]


# ---------------- checks: coding-idea ----------------
assert shift("CAT", 1) == "DBU" and diffs("HOME", "IPNF") == [1, 1, 1, 1]
assert pair_swap("PLANET") == "LPNATE" and halves_rev("MONKEY") == "NOMYEK"
assert halves_swap("MONKEY") == "KEYMON" and first_last("LEMON") == "NEMOL"
assert vowel_cons("BASKET", 1, -1) == "ABRJFS" and opp("BAD") == "YZW" and shift("YZW", 1) == "ZAX"
assert L(p("Y") + 3) == "B"
assert all(p(a) + p(b) == 27 for a, b in ["AZ", "BY", "CX", "DW", "EV", "FU", "GT", "HS", "IR", "JQ", "KP", "LO", "MN"])
assert [p(c) for c in "EJOTY"] == [5, 10, 15, 20, 25]
# patterns
assert pair_swap("BRIGHT") == "RBGITH" and pair_swap("SILVER") == "ISVLRE"
assert pair_swap("PENCIL") == "EPCNLI"
assert halves_rev("CANDLE") == "NACELD" and halves_rev("WINDOW") == "NIWWOD"
assert halves_rev("PICTURE") == "CIPTERU"
assert first_last("TIGER", 1) == "RJHFT" and first_last("HORSE", 1) == "EPSTH"
assert vowel_cons("PENCIL", 1, -1) == "OFMBJK"
assert shift(opp("BAD"), 1) == "ZAX" and opp("CUP") == "XFK" and shift(opp("CUP"), 1) == "YGL"
assert halves_swap("SILVER") == "VERSIL" and halves_swap("MARKET") == "KETMAR"
assert halves_swap("CAPTAIN") == "AINTCAP"
# trick
assert diffs("CAT", "FDW") == [3, 3, 3] and shift("DOG", 3) == "GRJ"

# ---------------- checks: letter-shift ----------------
assert diffs("KITE", "MKVG") == [2] * 4 and shift("KITE", 2) == "MKVG"
assert p("R") == 18 and p("H") == 8 and p("M") == 13 and p("N") == 14
assert L(25 + 3) == "B" and L(3 - 5) == "X"
assert shift("CAT", 3) == "FDW" and shift("FISH", 4) == "JMWL"
assert diffs("WORD", "XQUH") == [1, 2, 3, 4] and shift("BOOK", [1, 2, 3, 4]) == "CQRO"
assert shift("SILK", 2) == "UKNM" and shift("COTTON", 2) == "EQVVQP"
assert shift("PEN", 2) == "RGP" and shift("CAT", 2) == "ECV"
assert shift("LAMP", [-1, -2, -3, -4]) == "KYJL"
assert diffs("LAMP", "MCPT") == [1, 2, 3, 4] and shift("DESK", [1, 2, 3, 4]) == "EGVO"
assert shift("BIRD", 2) == "DKTF" and shift("HTQI", -2) == "FROG" and shift("FROG", 2) == "HTQI"
assert diffs("FLOWER", "GKPVFQ") == [1, -1, 1, -1, 1, -1] and shift("GARDEN", [1, -1] * 3) == "HZSCFM"
assert shift("DEER", 4) == "HIIV" and shift("PLANT", 5) == "UQFSY"
assert shift("MANGO", 2) == "OCPIQ" and shift("JUICE", 2) == "LWKEG" and shift("LWKEG", -2) == "JUICE"
assert shift("W", 4) == "A"

# ---------------- checks: reverse ----------------
assert rev("LOGIC") == "CIGOL" and rev("GARDEN") == "NEDRAG" and rev("FLOWER") == "REWOLF"
assert rev("PAINT") == "TNIAP" and diffs("TNIAP", "UOJBQ") == [1] * 5
assert shift(rev("BRUSH"), 1) == "ITVSC" and rev(shift("BRUSH", 1)) == "ITVSC"
assert L(27 - 11) == "P" and opp("WHITE") == "DSRGV" and opp("GREEN") == "TIVVM"
assert rev(opp("LAMP")) == "KNZO" and opp("LAMP") == "OZNK" and rev(opp("DESK")) == "PHVW"
assert L(27 - p("T")) == "G" and p("P") + p("K") == 27
assert shift(rev("BRAIN"), [1, 2, 3, 4, 5]) == "OKDVG"
assert shift(rev("CLOUD"), [1, 2, 3, 4, 5]) == "EWRPH"
assert rev(shift("CLOUD", [1, 2, 3, 4, 5])) == "IYRND"      # the wrong order gives a different code
assert shift(rev("TABLE"), 1) == "FMCBU" and shift(rev("CHAIR"), 1) == "SJBID"

# ---------------- checks: number coding ----------------
assert psum("SUN") == 54 and psum("DOG") == 26 and psum("MOON") == 57 and psum("CAT") == 24
assert rsum("CAT") == 57 and rsum("EAT") == 55 and rsum("TEN") == 42
assert side_by_side("BAD") == "214" and side_by_side("CAT") == "3120"
assert side_by_side("FACE") == "6135" and side_by_side("HIDE") == "8945"
assert wsum("DAB") == 12 and wsum("CAD") == 17
assert shift("TREE", 1) == "USFF" and psum("TREE") == 48
assert shift("LEAF", 1) + str(psum("LEAF")) == "MFBG24"
assert psum("HAT") == 29 and psum("PEN") == 35
assert psum("FISH") == 42 and psum("TEA") == 26 and psum("FACE") == 15
assert psum("BAT") * 2 == 46 and psum("DOG") * 2 == 52 and psum("DOG") + 23 != 52 and psum("CUP") * 2 == 80

# ---------------- checks: symbol coding ----------------
table = {"P": "3", "L": "@", "A": "7", "N": "#", "E": "5", "T": "%"}
code = lambda w, t: "".join(t[c] for c in w)
assert code("PLANET", table) == "3@7#5%" and code("PLANT", table) == "3@7#%"
assert code("MAT", {"M": "#", "A": "@", "T": "%"}) == "#@%"
assert code("ROSE", dict(R="6", O="8", S="3", E="1")) == "6831" and code("SORE", dict(R="6", O="8", S="3", E="1")) == "3861"
t2 = {"E": "&", "C": "@", "H": "%", "O": "#"}
cond = lambda w: code(w, t2)[::-1] if w[0] in VOWELS else code(w, t2)
assert cond("ECHO") == "#%@&" and code("ECHO", t2) == "&@%#"
# PEN = @ # %, NET = % # & with symbols in letter order
m = {}
for w, cs in [("PEN", "@#%"), ("NET", "%#&")]:
    for a, b in zip(w, cs):
        assert m.setdefault(a, b) == b
assert m["P"] == "@" and "".join(m[c] for c in "TEN") == "&#%"
dbl = lambda w: "".join(str(2 * p(c)) for c in w)
assert dbl("CAB") == "624" and dbl("BEAD") == "41028" and 2 * p("E") == 10
grid = ["ABCDE", "FGHIK", "LMNOP", "QRSTU", "VWXYZ"]
rc = {ch: f"{r + 1}{c + 1}" for r, row in enumerate(grid) for c, ch in enumerate(row)}
assert "J" not in rc and [rc[c] for c in "HIDE"] == ["23", "24", "14", "15"]
assert rc["H"] == "23" and [rc[c] for c in "MOST"] == ["32", "34", "43", "44"]
assert [rc[c] for c in "TMH"] == ["44", "32", "23"]

# ---------------- checks: substitution ----------------
links = {"cloud": "rain", "rain": "wind", "wind": "sun"}
assert chain(links, "rain") == "wind"
links2 = {"train": "bus", "bus": "ship", "ship": "aeroplane", "aeroplane": "rocket", "rocket": "car"}
assert chain(links2, "aeroplane") == "rocket"
links3 = {"day": "night", "night": "morning", "morning": "evening"}
assert chain(links3, "night") == "morning"
links4 = {"sky": "sea", "sea": "water", "water": "air"}
assert chain(links4, "sky") == "sea"
assert chain({"pen": "pencil", "pencil": "eraser", "eraser": "book", "book": "bag"}, "pen") == "pencil"
assert solve_sentences([("red light", "pa ka"), ("green light", "ka na")])["red"] == ["pa"]
s = solve_sentences([("hot tea", "na pi"), ("cold tea", "pi ka"), ("hot milk", "na ru")])
assert s["milk"] == ["ru"] and s["cold"] == ["ka"]
s = solve_sentences([("good boy", "mi ra"), ("good girl smiles", "ra su to")])
assert s["good"] == ["ra"] and s["boy"] == ["mi"] and s["girl"] == ["su", "to"]
dic = {"1": "come", "2": "home", "3": "sweet", "4": "early"}
inv = {v: k for k, v in dic.items()}
assert " ".join(inv[w] for w in "come home early".split()) == "1 2 4"
assert " ".join(dic[n] for n in "2 3".split()) == "home sweet"
d5 = {"pen": "1", "book": "2", "bag": "3", "chair": "4"}
assert " ".join(d5[w] for w in "chair pen".split()) == "4 1"

# ---------------- checks: language coding ----------------
s = solve_sentences([("sun is hot", "ta mo ri"), ("sun is bright", "ri ze mo")])
assert s["hot"] == ["ta"] and s["bright"] == ["ze"] and s["sun"] == ["mo", "ri"]
s = solve_sentences([("sky is blue", "ta pa ka"), ("sea is deep", "pa za la")])
assert s["is"] == ["pa"] and s["blue"] == ["ka", "ta"]
s = solve_sentences([("delhi is big", "ja pa ni"), ("mumbai is big", "sa pa ni")])
assert s["delhi"] == ["ja"] and s["mumbai"] == ["sa"]
s = solve_sentences([("train runs fast", "la jo me"), ("bus runs fast", "la jo fi"), ("fast train", "me jo")])
assert s == {"bus": ["fi"], "fast": ["jo"], "runs": ["la"], "train": ["me"]}
s = solve_sentences([("come home", "1 2"), ("home sweet", "2 3")])
assert s["home"] == ["2"] and s["sweet"] == ["3"] and " ".join(s[w][0] for w in ["sweet", "home"]) == "3 2"
s = solve_sentences([("birds fly", "lo pe"), ("fly high", "pe ni"), ("birds sing", "lo ra")])
assert s["sing"] == ["ra"] and s["high"] == ["ni"]
s = solve_sentences([("good morning sir", "ta pa ni"), ("good night sir", "pa ni ro"), ("night is dark", "ro ki su")])
assert s["morning"] == ["ta"] and s["night"] == ["ro"] and s["dark"] == ["ki", "su"]


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
# 1. coding-idea
# =====================================================================
SUBS["coding-idea"] = dict(
    concept=(
        "A coding question shows a word and its code. You find the rule from that pair, "
        "then use the same rule on a new word. No vocabulary is tested. The rule is always "
        "mechanical: letters move, change places, or turn into numbers or symbols."
    ),
    notes=r"""### What a code is
A code hides a word with a fixed rule. If every letter moves one step forward, CAT becomes DBU.

- **Coding** means turning a word into its code.
- **Decoding** means turning a code back into the word.

In the exam you see one word with its code. You find the rule. Then you use the same rule on a new word.

> **Rule:** The rule comes only from the sample pair. Never invent a new rule for the new word.

### The families at a glance
| Family | What happens | Small example |
|---|---|---|
| Letter shift | every letter moves forward or back | CAT → DBU (+1) |
| Reversal | the word is written backwards | LOGIC → CIGOL |
| Opposite letters | A↔Z, B↔Y and so on | BAD → YZW |
| Rearrangement | same letters, new order | PLANET → LPNATE |
| Number coding | the word becomes a number | CAT → 24 |
| Symbol coding | each letter gets a symbol | M = #, A = @ |
| Substitution | things get new names | sky is called sea |
| Language coding | sentences become code words | good day = pa ki |

Each family has its own lesson. This lesson shows how to tell them apart. It also covers rearrangement and two-step rules.

### Find the rule in four checks
Do these checks in order. Stop at the first one that fits.

1. **Count the letters.** Same count? Compare the letters one by one.
2. **Same letters, new order?** It is a rearrangement. Mark where each letter went.
3. **Read the code backwards.** If you see the word, reversal is part of the rule.
4. **Different letters?** Write the positions (A = 1 … Z = 26). Subtract slot by slot.

A constant difference like +2 means a shift. Two positions that add up to 27 mean opposite letters.

> **Example:** HOME → IPNF. The letters are different. H→I, O→P, M→N, E→F are each +1. The rule is a +1 shift.

### Rearrangement: same letters, new order
The letters stay the same. Only their places change. Four orders come up again and again.

- **Pair swap:** swap the letters two at a time. PLANET → PL AN ET → LP NA TE → **LPNATE**.
- **Halves reversed:** split the word in two. Write each half backwards. MONKEY → MON KEY → **NOMYEK**.
- **Halves swapped:** write the second half first. MONKEY → **KEYMON**.
- **First–last swap:** only the end letters change places. LEMON → **NEMOL**.

In a word with an odd number of letters, the middle letter usually stays in place. In a pair swap, the last letter stays.

> **Tip:** Look at the first two letters of the code. They usually tell you which order was used.

### Two-step rules
Some codes use two simple rules one after the other. Find the first rule, then see what is still different.

- **Vowels one way, consonants another.** Vowels (A, E, I, O, U) move +1 and consonants move −1. BASKET → **ABRJFS**.
- **Opposite, then shift.** BAD → opposite YZW → +1 → **ZAX**.
- **Rearrange, then shift.** First swap the pairs, then move every letter +1.

> **Watch:** Do the steps in the same order as the sample. With a changing shift, a different order gives a different code.

### Alphabet facts to learn once
- **EJOTY:** E = 5, J = 10, O = 15, T = 20, Y = 25. Every letter is at most 2 steps from one of these.
- **Opposite pairs:** A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N. Each pair adds up to 27.
- **Wrap-around:** after Z comes A again. So Y + 3 = B.
""",
    tricks=[
        trick("Find the difference list first",
              "Write the sample word above its code. Subtract the positions slot by slot. The list of differences is the rule. Apply the same list to the new word.",
              "If CAT is written as FDW, how is DOG written?",
              ["C→F, A→D, T→W: each is +3.", "Apply +3 to DOG: D→G, O→R, G→J."],
              "GRJ"),
    ],
    mistakes=[
        {"wrong": "Using a different shift for the new word than the sample showed.", "right": "Apply exactly the rule you found on the sample pair."},
        {"wrong": "Checking only one letter and trusting the rule.", "right": "Check at least three letters. A rising shift looks flat on one letter."},
        {"wrong": "Taking Y + 3 as 'out of the alphabet'.", "right": "Wrap around after Z: Y + 3 = B."},
        {"wrong": "Doing a two-step rule in a different order from the sample.", "right": "Copy the order of the steps from the sample."},
        {"wrong": "Trying hard rules before the easy checks.", "right": "Check rearrangement and backwards reading first. They take seconds."},
    ],
    revision=[
        "Same letters, new order → rearrangement (pair swap, halves, first–last).",
        "Different letters → subtract positions: a constant = shift, a sum of 27 = opposite letters.",
        "Read the code backwards before trying anything complicated.",
        "EJOTY: E = 5, J = 10, O = 15, T = 20, Y = 25.",
        "Two-step rules: same steps, same order as the sample.",
        "Check the rule on three letters before coding the new word.",
    ],
    patterns=[
        pat("cd-p1", "Pair swap (neighbouring letters change places)", "common",
            "The code has the same letters as the word. Letters 1-2, 3-4, 5-6 have changed places.",
            None,
            ["Split the word into pairs from the left.", "Write each pair backwards.", "If one letter is left over at the end, keep it as it is."],
            "No letter changes, only the order, so checking pairs is enough.",
            "In a certain code language, BRIGHT is written as RBGITH. How will SILVER be written in that language?",
            ["BRIGHT → BR IG HT → RB GI TH. So the rule is a pair swap.", "SILVER → SI LV ER.", "Swap each pair: IS VL RE."],
            "ISVLRE"),
        pat("cd-p2", "Halves reversed (each half written backwards)", "common",
            "The code has the same letters. The first half and the second half each appear backwards.",
            None,
            ["Split the word into two equal halves.", "In an odd word, keep the middle letter in place.", "Write each half backwards.", "Add any extra shift only if the sample shows one."],
            "Reading each half of the sample backwards gives back the original halves.",
            "In a certain code language, CANDLE is written as NACELD. How will WINDOW be written in that language?",
            ["CANDLE → CAN DLE → NAC ELD. Each half is reversed.", "WINDOW → WIN DOW.", "Reverse each half: NIW WOD."],
            "NIWWOD"),
        pat("cd-p3", "First and last letters interchanged", "occasional",
            "The first letter of the word is at the end of the code, and the last letter is at the front.",
            None,
            ["Swap the first and last letters.", "Compare the middle letters with the sample: same, or all moved by the same steps?", "Apply both steps to the new word."],
            "The middle part tells you whether a second rule is hidden in the code.",
            "In a certain code language, TIGER is written as RJHFT. How will HORSE be written in that language?",
            ["T and R have changed places.", "Middle IGE → JHF: each letter is +1.", "HORSE: swap H and E, and move ORS +1 to PST."],
            "EPSTH"),
        pat("cd-p4", "Vowels and consonants change differently", "occasional",
            "The differences are not all equal. All vowels move one way, and all consonants move another way.",
            None,
            ["Write the difference under each letter of the sample.", "Group them: what happened to the vowels? What happened to the consonants?", "Code the new word letter by letter. First ask: vowel or consonant?"],
            "The rule depends on the type of letter, not on its place in the word.",
            "In a certain code language, BASKET is written as ABRJFS. How will PENCIL be written in that language?",
            ["Vowels move +1: A→B, E→F.", "Consonants move −1: B→A, S→R, K→J, T→S.", "PENCIL: P−1, E+1, N−1, C−1, I+1, L−1."],
            "OFMBJK"),
        pat("cd-p5", "Two rules in a row (mixed coding)", "common",
            "No single rule explains the sample. The letters are opposite and shifted, or reversed and shifted.",
            None,
            ["Test the simple rules first: shift, opposite, reverse.", "If one rule almost works, the leftover difference is the second step.", "Apply both steps to the new word in the same order."],
            "Every mixed rule is two basic rules, one after the other.",
            "In a certain code language, BAD is written as ZAX. How will CUP be written in that language?",
            ["Opposite of BAD is YZW. YZW +1 gives ZAX. So the rule is: opposite, then +1.", "Opposite of CUP is XFK.", "XFK +1 gives YGL."],
            "YGL"),
        pat("cd-p34", "Halves swapped (second half written first)", "common",
            "The code has the same letters. The second half of the word comes first, unchanged.",
            None,
            ["Split the word into two halves.", "Write the second half first, then the first half.", "In an odd word, keep the middle letter in the middle."],
            "Each half keeps its own letter order, so the two halves are easy to spot in the code.",
            "In a certain code language, SILVER is written as VERSIL. How will MARKET be written in that language?",
            ["SILVER → SIL VER → VER SIL. The halves are swapped.", "MARKET → MAR KET.", "Write KET first, then MAR."],
            "KETMAR"),
    ],
)

# =====================================================================
# 2. letter-shift-coding
# =====================================================================
SUBS["letter-shift-coding"] = dict(
    concept=(
        "Every letter moves forward or backward by some steps in the alphabet. "
        "Find the steps from the sample pair, slot by slot. Then move the letters of the new word "
        "by the same steps. After Z the alphabet starts again at A."
    ),
    notes=r"""### What a letter shift is
Each letter moves forward or back by a fixed number of steps. With +2, CAT becomes ECV.

Think of the alphabet as a circle of 26 letters. After Z it starts again at A. This is the most common coding question in SSC, Railway and Banking papers.

- **Coding:** the word is given, you write the code.
- **Decoding:** the code is given, you bring back the word.

### Know the positions fast
Each letter has a position: A = 1, B = 2, … Z = 26. Learn five anchors and you will never count on your fingers.

| E | J | O | T | Y |
|---|---|---|---|---|
| 5 | 10 | 15 | 20 | 25 |

Every letter is at most 2 steps from an anchor. R = T − 2 = 18. H = J − 2 = 8. W = Y − 2 = 23.

> **Tip:** Also remember M = 13 and N = 14. They sit in the middle of the alphabet.

### Find the shift from the sample
Write the word above its code. For each slot, work out code position − word position. This list is the **shift list**.

KITE → MKVG. K(11) → M(13) is +2. I → K is +2, T → V is +2, E → G is +2. The shift list is (+2, +2, +2, +2). This is a **flat shift**.

> **Rule:** Check at least three letters before you trust a shift. One letter can fool you.

### Wrap-around
If the new position is more than 26, subtract 26. If it is 0 or less, add 26.

- Y + 3: 25 + 3 = 28, and 28 − 26 = 2 = **B**.
- C − 5: 3 − 5 = −2, and −2 + 26 = 24 = **X**.
- W + 4: W is Y − 2, so W + 4 = Y + 2, which crosses Z and lands on **A**.

### A full question, start to finish
"In a certain code, PEN is written as RGP. How is CAT written in that code?"

1. Find the shift: P(16) → R(18) is +2. E(5) → G(7) is +2. N(14) → P(16) is +2.
2. The rule is a flat +2 shift.
3. Apply it to CAT: C → E, A → C, T → V.
4. Write the code: **ECV**.

For decoding, run the film backwards. RGP − 2 gives P, G − 2 gives E, P − 2 gives N. You are back at PEN.

### The five kinds of shift
1. **Flat:** every letter moves the same, like +2 or −3.
2. **Rising or falling:** +1, +2, +3, … or −1, −2, −3, … LAMP with −1, −2, −3, −4 gives KYJL.
3. **Alternating:** +1, −1, +1, −1, … Odd places go one way, even places the other.
4. **Length-based:** the shift equals the number of letters. CAT (3 letters) → FDW. FISH (4 letters) → JMWL.
5. **Decoding:** the code is given and the word is asked. Undo each step. Where the rule adds 2, you subtract 2.

> **Example:** WORD → XQUH. The shifts are +1, +2, +3, +4, a rising list. So BOOK → B+1, O+2, O+3, K+4 = **CQRO**. The two O's get different codes, because the place decides the shift.

### Use the options
- Code only the first letter. Usually one or two options survive.
- Then code the last letter to choose between them.
- For decoding, code your chosen option forward once. If it gives the code, you are right.
""",
    formulas=[
        {"name": "Shift list", "tex": r"\text{code}_i = \text{letter}_i + d_i \pmod{26}",
         "note": "d is the shift for place i, found from the sample. Above 26, subtract 26."},
        {"name": "Decoding", "tex": r"\text{letter}_i = \text{code}_i - d_i \pmod{26}",
         "note": "To decode, subtract the same shifts. At 0 or below, add 26."},
    ],
    tricks=[
        trick("Hop from an anchor, do not count",
              "To shift a letter, jump from the nearest EJOTY anchor. W is Y − 2, so W + 4 = Y + 2 = A. Two small hops are faster than counting W, X, Y, Z, A.",
              "If MANGO is written as OCPIQ, how is JUICE written?",
              ["MANGO → OCPIQ is +2 on every letter.", "J+2 = L, U+2 = W, I+2 = K, C+2 = E, E+2 = G."],
              "LWKEG"),
        trick("Decoding: run the shifts backwards",
              "When the code is given and the word is asked, subtract the shift instead of adding it.",
              "If MANGO is written as OCPIQ, which word is written as LWKEG?",
              ["The rule is +2, so decode with −2.", "L→J, W→U, K→I, E→C, G→E."],
              "JUICE"),
    ],
    mistakes=[
        {"wrong": "Adding the shift in a decoding question.", "right": "Decoding runs backwards. Subtract where the rule adds."},
        {"wrong": "Treating a rising list (+1, +2, +3) as flat after checking one letter.", "right": "Check three letters. Write the full shift list."},
        {"wrong": "Losing count when a shift crosses Z.", "right": "Above 26, subtract 26. At 0 or below, add 26."},
        {"wrong": "In a length-based rule, using the sample's shift for the new word.", "right": "Count the letters of the new word. That count is its shift."},
        {"wrong": "Giving a repeated letter the same code in a rising-shift rule.", "right": "In rising or alternating rules the place decides the shift, not the letter."},
    ],
    revision=[
        "Positions: A = 1 … Z = 26; anchors E5, J10, O15, T20, Y25.",
        "Shift = code position − word position, slot by slot.",
        "Flat, rising/falling, alternating and length-based are the main kinds.",
        "Wrap-around: above 26 subtract 26; at 0 or below add 26.",
        "Decode = subtract the shifts; check by coding your answer forward.",
        "Code the first letter of each option first to cut options fast.",
    ],
    patterns=[
        pat("cd-p6", "Flat shift (+k or −k on every letter)", "very common",
            "Every code letter is the same number of steps ahead of (or behind) its word letter.",
            r"\text{code}_i = \text{letter}_i + k",
            ["Subtract positions for three letters of the sample.", "If all differences are equal, that is k.", "Add k to each letter of the new word. Wrap after Z."],
            "A flat rule treats every letter the same way.",
            "In a certain code language, SILK is written as UKNM. How will COTTON be written in that language?",
            ["S→U, I→K, L→N, K→M: each is +2.", "COTTON +2: C→E, O→Q, T→V, T→V, O→Q, N→P."],
            "EQVVQP"),
        pat("cd-p7", "Rising or falling shift (+1, +2, +3, …)", "common",
            "The differences are not equal but grow or fall by place: +1, +2, +3, +4 or −1, −2, −3.",
            r"\text{code}_i = \text{letter}_i + d_i",
            ["Write the full shift list from the sample.", "Apply the same list to the new word, place by place.", "Expect a repeated letter to get different codes."],
            "The place of a letter decides its shift, not the letter itself.",
            "In a certain code language, LAMP is written as MCPT. How will DESK be written in that language?",
            ["L→M +1, A→C +2, M→P +3, P→T +4.", "DESK: D+1 = E, E+2 = G, S+3 = V, K+4 = O."],
            "EGVO"),
        pat("cd-p8", "Decoding (code given, word asked)", "common",
            "The question gives a code and asks: which word is written as …?",
            r"\text{letter}_i = \text{code}_i - d_i",
            ["Find the rule from the sample pair.", "Undo it: subtract where the rule adds, add where it subtracts.", "Code your answer forward once to confirm."],
            "Decoding is the same rule played backwards.",
            "In a certain code language, BIRD is written as DKTF. Which word is written as HTQI in that language?",
            ["BIRD → DKTF is +2 on every letter.", "Decode with −2: H→F, T→R, Q→O, I→G.", "Check: FROG +2 = HTQI."],
            "FROG"),
        pat("cd-p9", "Alternating shift (odd and even places)", "common",
            "The shifts swing: +1, −1, +1, −1, … Letters in odd places move one way, even places the other.",
            None,
            ["Write the shift list and find the 2-step cycle.", "Apply the cycle to the new word from the first letter.", "For a longer word, keep repeating the cycle."],
            "The rule depends only on whether the place is odd or even.",
            "In a certain code language, FLOWER is written as GKPVFQ. How will GARDEN be written in that language?",
            ["F→G +1, L→K −1, O→P +1, W→V −1, E→F +1, R→Q −1.", "GARDEN with +1, −1 repeating: G→H, A→Z, R→S, D→C, E→F, N→M."],
            "HZSCFM"),
        pat("cd-p10", "Shift equal to the number of letters", "occasional",
            "Two samples of different lengths have different flat shifts. Each shift equals the word's letter count.",
            None,
            ["Find the flat shift of each sample.", "Compare it with the number of letters.", "Count the letters of the new word and shift by that number."],
            "The shift is not fixed. It is tied to the length of the word.",
            "In a certain code language, CAT is written as FDW and DEER is written as HIIV. How will PLANT be written in that language?",
            ["CAT is +3 (3 letters). DEER is +4 (4 letters).", "PLANT has 5 letters, so shift +5.", "P→U, L→Q, A→F, N→S, T→Y."],
            "UQFSY"),
    ],
)

# =====================================================================
# 3. reverse-coding
# =====================================================================
SUBS["reverse-coding"] = dict(
    concept=(
        "The code is the word written backwards, sometimes with a shift added. "
        "A close cousin replaces each letter by its opposite letter (A↔Z, B↔Y). "
        "Test both in seconds: read the code backwards, and add the positions of matching letters."
    ),
    notes=r"""### What reverse coding is
The word is written from right to left. LOGIC becomes CIGOL.

Examiners often add one more step, like a shift. Some codes use opposite letters instead. This lesson covers all of these.

### Test for reversal in one move
Read the code from right to left. What you see names the rule.

| Reading the code backwards tells you | Rule |
|---|---|
| the word itself | pure reversal |
| the word with every letter moved by the same k | reverse, then shift by k |
| letters far from the word | try opposite letters |

- You see the word → **pure reversal**. GARDEN → NEDRAG.
- You see the word with every letter moved by the same steps → **reverse and shift**.
- You see nothing familiar → try opposite letters.

> **Tip:** This backwards read takes three seconds. Do it before any subtraction.

### Reverse and shift
PAINT → UOJBQ. Reverse PAINT to get TNIAP. Compare TNIAP with UOJBQ: T→U, N→O, I→J, A→B, P→Q. Each is +1. So the rule is: reverse, then +1.

With a flat shift, the order does not matter. "Reverse then shift" and "shift then reverse" give the same code.

> **Watch:** With a changing shift like +1, +2, +3, the order matters. Copy the order the sample used.

For example, CLOUD reversed is DUOLC, and +1, +2, +3, +4, +5 gives EWRPH. Shifting first and reversing after gives IYRND. Only one of them matches the sample's rule.

### Opposite letters
Fold the alphabet in the middle. A sits on Z, B on Y, C on X, and so on. These pairs are **opposite letters**. The positions in a pair always add up to 27.

| A-Z | B-Y | C-X | D-W | E-V | F-U | G-T |
|---|---|---|---|---|---|---|
| H-S | I-R | J-Q | K-P | L-O | M-N | |

To find an opposite, subtract the position from 27. Opposite of K (11) = 27 − 11 = 16 = P. Opposite of T (20) = 27 − 20 = 7 = G.

To spot it, add the positions of the first word letter and the first code letter. If the sum is 27, check one more letter. WHITE → DSRGV: W (23) + D (4) = 27 and H (8) + S (19) = 27.

> **Rule:** Opposite = 27 − position. Not 26.

### Opposite and reverse together
Some codes write the opposite letters and then reverse the result. LAMP → opposites OZNK → reversed **KNZO**.

Check it the same way, but on the far end. In DESK → PHVW, the first code letter P (16) and the last word letter K (11) add up to 27. That is the fingerprint of opposite plus reverse.

To spot it, check the first code letter against the **last** word letter. Here K is the opposite of P.

### Decoding these codes
- Reversal undoes itself. Reverse the code to get the word back.
- Opposite letters undo themselves too. The opposite of P is K, and the opposite of K is P.
- For reverse and shift, undo the shift first, then reverse.
""",
    tricks=[
        trick("Read the code backwards first",
              "Read the code from right to left. If you see the word, just reverse new words. If every letter is off by the same k, reverse and shift by k.",
              "If TABLE is written as FMCBU, how is CHAIR written?",
              ["TABLE reversed is ELBAT. ELBAT +1 gives FMCBU.", "CHAIR reversed is RIAHC.", "RIAHC +1 gives SJBID."],
              "SJBID"),
    ],
    mistakes=[
        {"wrong": "Reversing the word but forgetting the extra shift.", "right": "After reversing, compare with the code letter by letter for a leftover shift."},
        {"wrong": "Using 26 for opposites (26 − 11 = 15 = O for K).", "right": "Opposite = 27 − position. The opposite of K is P."},
        {"wrong": "Shifting before reversing when the sample reversed first, with a changing shift.", "right": "Copy the sample's order. With +1, +2, +3 the two orders give different codes."},
        {"wrong": "Leaving the middle letter of an odd word unchanged.", "right": "The middle letter stays in place on reversal, but it still gets the shift or opposite."},
        {"wrong": "Matching the first code letter with the first word letter only.", "right": "Also check it against the last word letter. That catches opposite + reverse."},
    ],
    revision=[
        "Read the code backwards first: the word appears → reversal.",
        "The word appears shifted → reverse and shift; find k from one letter.",
        "Positions add to 27 → opposite letters; opposite = 27 − position.",
        "First code letter pairs with the last word letter → opposite + reverse.",
        "Flat shift: order does not matter. Changing shift: copy the order.",
        "Reversal and opposite letters undo themselves when decoding.",
    ],
    patterns=[
        pat("cd-p11", "Pure reversal", "common",
            "The code has the same letters as the word, written from right to left.",
            None,
            ["Read the sample code backwards. You should see the word.", "Write the new word backwards.", "For decoding, reverse the code."],
            "Reversal is its own undo, so one read confirms the rule.",
            "In a certain code language, GARDEN is written as NEDRAG. How will FLOWER be written in that language?",
            ["NEDRAG read backwards is GARDEN, so the rule is pure reversal.", "FLOWER backwards is R-E-W-O-L-F."],
            "REWOLF"),
        pat("cd-p12", "Reverse and then shift", "common",
            "Reading the code backwards gives the word with every letter moved by the same steps.",
            r"\text{code} = \text{shift}_k(\text{reverse}(w))",
            ["Reverse the sample word.", "Compare it with the code letter by letter to find the shift.", "Reverse the new word and apply the same shift."],
            "The code is two simple rules in a row.",
            "In a certain code language, PAINT is written as UOJBQ. How will BRUSH be written in that language?",
            ["PAINT reversed is TNIAP. TNIAP → UOJBQ is +1 on each letter.", "BRUSH reversed is HSURB.", "HSURB +1 gives ITVSC."],
            "ITVSC"),
        pat("cd-p13", "Opposite letters (positions add to 27)", "common",
            "Code letters look far from the word letters. Each word letter and its code letter add up to 27.",
            r"\text{opposite}(p) = 27 - p",
            ["Add the positions of the first word letter and the first code letter.", "If the sum is 27, confirm with one more letter.", "Write the opposite of each letter of the new word."],
            "Opposite pairs are fixed, so the code is a simple look-up.",
            "In a certain code language, WHITE is written as DSRGV. How will GREEN be written in that language?",
            ["W (23) + D (4) = 27, so the code uses opposite letters.", "G↔T, R↔I, E↔V, E↔V, N↔M."],
            "TIVVM"),
        pat("cd-p14", "Opposite letters plus reversal", "occasional",
            "The first code letter is the opposite of the last word letter.",
            None,
            ["Pair the first code letter with the last word letter. Their sum should be 27.", "For the new word, write the opposite letters.", "Reverse the result."],
            "Both steps undo themselves, so the order of the two steps does not change the answer.",
            "In a certain code language, LAMP is written as KNZO. How will DESK be written in that language?",
            ["LAMP → opposites OZNK → reversed KNZO. The rule fits.", "DESK → opposites WVHP.", "Reverse WVHP to get PHVW."],
            "PHVW"),
        pat("cd-p36", "Reverse, then a rising shift (+1, +2, +3, …)", "occasional",
            "Reversing the word does not give a flat shift. The differences after reversing rise place by place.",
            None,
            ["Reverse the sample word.", "Find the shift list between the reversed word and the code.", "Reverse the new word, then apply the same list.", "Do not shift first. The order changes the answer here."],
            "With a changing shift, the place of each letter matters, so the order of steps matters.",
            "In a certain code language, BRAIN is written as OKDVG. How will CLOUD be written in that language?",
            ["BRAIN reversed is NIARB.", "NIARB → OKDVG is +1, +2, +3, +4, +5.", "CLOUD reversed is DUOLC.", "DUOLC with +1, +2, +3, +4, +5 gives EWRPH."],
            "EWRPH"),
    ],
)

# =====================================================================
# 4. number-coding
# =====================================================================
SUBS["number-coding"] = dict(
    concept=(
        "A word is coded as a number built from its letter positions (A = 1 … Z = 26). "
        "Most often the number is the sum of the positions. "
        "Test the plain sum first; if it does not match, look for one extra step."
    ),
    notes=r"""### What number coding is
A word is coded as a number. The number is built from the letter positions. SUN = 19 + 21 + 14 = 54.

Positions run A = 1, B = 2, … Z = 26. The EJOTY anchors make them fast: E = 5, J = 10, O = 15, T = 20, Y = 25.

### Start with the plain sum
Add the positions of the sample word. Compare the total with the code.

SUN is coded 54. S = 19, U = 21, N = 14, and the sum is 54. That equals the code, so the rule is the plain sum. Then DOG = 4 + 15 + 7 = **26**.

Add with anchors, not by counting. S is T − 1 = 19. U is T + 1 = 21. N = 14. The total comes out in seconds.

> **Rule:** Your rule must give the sample's code exactly. If it is off by even 1, it is the wrong rule.

### A full question, start to finish
"In a certain code, FISH is written as 42. How is TEA written in that code?"

1. Add the sample's positions: F(6) + I(9) + S(19) + H(8) = 42.
2. The sum equals the code, so the rule is the plain position sum.
3. Add the new word: T(20) + E(5) + A(1) = 26.
4. Write the answer: **26**.

One check like this settles the rule. Then every other word in the question uses the same sum.

### When the sum does not match
Compare the sum with the code and use this table.

| What you see | Rule |
|---|---|
| Code = sum | plain sum |
| Code = sum + a fixed number | sum + r |
| Code = 2 or 3 times the sum | sum × k |
| Short word, big code | reverse positions (A = 26 … Z = 1) |
| A long string of digits | positions written side by side |
| Letters followed by a number | mixed code |

> **Watch:** One sample can fit two rules. BAT = 46 fits "sum × 2" and also "sum + 23". A second sample decides.

### Reverse positions
Here A = 26, B = 25, … Z = 1. Each letter counts as 27 minus its normal position. CAT = 24 + 26 + 7 = **57**.

### Positions written side by side
Sometimes the positions are not added. They are written one after another. BAD = 2, 1, 4 → **214**. CAT = 3, 1, 20 → **3120**. FACE = 6, 1, 3, 5 → **6135**.

Letters from J onwards take two digits. So when decoding, split the digits carefully. 3120 is C, A, T and not C, A, B, T.

### Weighted sum
Each position is multiplied by the letter's place in the word, then everything is added.

DAB = 4×1 + 1×2 + 2×3 = 12. So CAD = 3×1 + 1×2 + 4×3 = **17**.

Suspect it when no plain sum, sum + r or sum × k fits.

### Mixed codes
TREE is written as USFF48. The letters moved +1 (TREE → USFF). The number is the position sum: 20 + 18 + 5 + 5 = 48.

> **Tip:** Solve the letter part and the number part separately. Then join them in the sample's order.

For a new word, work out the number part again. Never copy the sample's number.
""",
    formulas=[
        {"name": "Position sum", "tex": r"\text{code} = \sum p_i", "note": "p = position of a letter, A = 1 … Z = 26."},
        {"name": "Sum with an extra step", "tex": r"\text{code} = k \cdot \sum p_i + r", "note": "Find k (multiply) or r (add) from the sample. Check with a second sample if one is given."},
        {"name": "Weighted sum", "tex": r"\text{code} = \sum i \cdot p_i", "note": "i = place of the letter in the word (1st, 2nd, 3rd …)."},
        {"name": "Reverse positions", "tex": r"p^{\text{rev}} = 27 - p", "note": "Z counts as 1 and A as 26."},
    ],
    tricks=[
        trick("Plain sum first",
              "Work out the position sum of the sample. If it equals the code, you are done. If not, compare: code − sum, then code ÷ sum. Only then try weighted or side-by-side codes.",
              "If SUN is coded as 54, how is MOON coded?",
              ["S + U + N = 19 + 21 + 14 = 54. So the rule is the plain sum.", "M + O + O + N = 13 + 15 + 15 + 14."],
              "57"),
        trick("Anchors make sums quick",
              "Letters near E, J, O, T and Y are small hops from 5, 10, 15, 20 and 25. Group them to add fast.",
              "In position-sum coding, is CAT coded as 24?",
              ["C = 3, A = 1, T = 20.", "3 + 1 + 20 = 24."],
              "Yes, 24"),
    ],
    mistakes=[
        {"wrong": "Copying the sample's number into the code of a new word.", "right": "Work out the number part again for the new word."},
        {"wrong": "Summing normal positions when the question says A = 26.", "right": "Use 27 − position for every letter."},
        {"wrong": "Assuming the plain sum without checking the sample.", "right": "The rule must give the sample's code exactly."},
        {"wrong": "Adding the constant to each letter instead of the total.", "right": "In 'sum + r' add r once, to the total."},
        {"wrong": "Adding instead of multiplying in a weighted sum.", "right": "Multiply each position by its place, then add."},
    ],
    revision=[
        "Positions A = 1 … Z = 26; EJOTY anchors give fast look-ups.",
        "Test order: plain sum → sum + r or × k → reverse positions → side by side → weighted.",
        "The rule must reproduce the sample's code exactly.",
        "Reverse position = 27 − position (A = 26, Z = 1).",
        "Mixed codes: code the letters, then add the new word's own number.",
        "One sample can fit two rules; use the second sample to decide.",
    ],
    patterns=[
        pat("cd-p15", "Plain position sum", "very common",
            "A word is coded as a number, often between 20 and 80. The question may say 'sum of positions'.",
            r"\text{code} = \sum p_i",
            ["Add the positions of the sample word's letters.", "If the sum equals the code, the rule is the plain sum.", "Add the positions of the new word."],
            "The plain sum is the most common number code in these exams.",
            "In a certain code language, HAT is written as 29. How will PEN be written in that language?",
            ["H + A + T = 8 + 1 + 20 = 29. The rule is the plain sum.", "P + E + N = 16 + 5 + 14."],
            "35"),
        pat("cd-p16", "Reverse-position sum (A = 26 … Z = 1)", "common",
            "The question says A = 26, B = 25 … Z = 1, or a short word has a large code.",
            r"\text{code} = \sum (27 - p_i)",
            ["Change each letter to 27 − its position.", "Add them for the sample and confirm the code.", "Repeat for the new word."],
            "Reverse positions are the same table read from Z to A.",
            "In a certain code, EAT is written as 55. How will TEN be written in that code?",
            ["Reverse values: E = 22, A = 26, T = 7. The sum is 55, so the rule fits.", "TEN: T = 7, E = 22, N = 13."],
            "42"),
        pat("cd-p17", "Position sum with an extra step (× k or + r)", "common",
            "The plain sum of the sample is close to the code but not equal to it.",
            r"\text{code} = k\sum p_i + r",
            ["Work out the plain sum of each sample.", "Find the step: code − sum, or code ÷ sum.", "Keep the step that fits every sample.", "Apply it to the new word's sum."],
            "One extra operation turns the plain sum into the code.",
            "In a certain code language, BAT is written as 46 and DOG is written as 52. How will CUP be written in that language?",
            ["BAT: 2 + 1 + 20 = 23, and 23 × 2 = 46.", "DOG: 4 + 15 + 7 = 26, and 26 × 2 = 52. So the rule is sum × 2.", "CUP: 3 + 21 + 16 = 40, and 40 × 2 = 80."],
            "80"),
        pat("cd-p18", "Weighted sum (position × place in the word)", "occasional",
            "No plain sum, sum + r or sum × k explains the code.",
            r"\text{code} = \sum i \cdot p_i",
            ["Multiply each letter's position by its place: 1st × 1, 2nd × 2, and so on.", "Add the products and check the sample's code.", "Do the same for the new word."],
            "Weighting explains codes that no flat sum can reach.",
            "In a certain code language, DAB is written as 12. How will CAD be written in that language?",
            ["DAB: 4×1 + 1×2 + 2×3 = 4 + 2 + 6 = 12. The rule fits.", "CAD: 3×1 + 1×2 + 4×3 = 3 + 2 + 12."],
            "17"),
        pat("cd-p19", "Letters plus a number (mixed code)", "occasional",
            "The code is a string like USFF48: letters followed by a number.",
            None,
            ["Solve the letter part first. It is usually a shift.", "Work out the number part for the new word from scratch.", "Join both parts in the sample's order."],
            "The two parts are separate small codes, and the number changes with the word.",
            "In a certain code language, TREE is written as USFF48. How will LEAF be written in that language?",
            ["Letters: TREE +1 = USFF. Number: 20 + 18 + 5 + 5 = 48.", "LEAF +1 = MFBG.", "LEAF sum = 12 + 5 + 1 + 6 = 24."],
            "MFBG24"),
        pat("cd-p37", "Positions written side by side", "common",
            "The code is a long number with no obvious sum. Its digits match the letter positions in order.",
            None,
            ["Write the position of each letter of the sample.", "Check that joining them gives the code.", "Write the new word's positions side by side."],
            "Nothing is added, so the code is just the positions in a row.",
            "In a certain code language, BAD is written as 214 and FACE is written as 6135. How will HIDE be written in that language?",
            ["BAD = 2, 1, 4 and FACE = 6, 1, 3, 5. Positions are written side by side.", "HIDE = 8, 9, 4, 5."],
            "8945"),
    ],
)

# =====================================================================
# 5. symbol-coding
# =====================================================================
SUBS["symbol-coding"] = dict(
    concept=(
        "Each letter is replaced by a fixed symbol or digit. Either a table is given, or you find the symbols "
        "by matching the letters that two coded words share. Once a letter has a symbol, it keeps it for the whole question."
    ),
    notes=r"""### What symbol coding is
Each letter gets a fixed symbol or digit. If M = #, A = @ and T = %, then MAT = #@%.

Two looks come in exams:

1. **A table is given.** You code the word letter by letter.
2. **No table.** You get two or three coded words. You find each symbol by matching.

Once a letter has a symbol, it keeps it for the whole question.

### Coding from a table
Write the symbol under each letter, in order. Then join the symbols.

> **Example:** R = 6, O = 8, S = 3, E = 1. So ROSE = **6831** and SORE = **3861**.

The same letters in a different order give a different code. So check the order of the word, not just its letters.

### Conditions come before the table
Many table questions add conditions, such as:

- If the first letter is a vowel, write the codes in reverse order.
- If the first and last letters are both consonants, swap their codes.

Check every condition first. Then code from the table. If the question says "only the first condition that applies", stop at the first match.

> **Watch:** One option is always the plain table code. It is the answer of a student who skipped the condition.

### Matching without a table
When two coded words share letters, their codes share symbols.

PEN = @ # % and NET = % # &. The common letters are E and N. The common symbols are # and %. So P, the letter left in PEN, takes @, the symbol left in its code.

If the symbols follow the letter order, you can also match by place. E is 2nd in PEN, and # is 2nd in its code.

> **Rule:** If the symbols may be in any order, match only common letters with common symbols. If two symbols still fit a letter, its code cannot be found.

### Digit tables
Digits can stand for letters by a simple build. "A = 2, B = 4, C = 6" means double the position. So CAB = 6, 2, 4 = **624**.

Some letters need two digits. With this build, E = 10. So count letters, not digits.

### Matrix coding
Letters sit in a 5 × 5 grid. Rows and columns are numbered 1 to 5. A letter's code is its row number, then its column number.

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | A | B | C | D | E |
| **2** | F | G | H | I | K |
| **3** | L | M | N | O | P |
| **4** | Q | R | S | T | U |
| **5** | V | W | X | Y | Z |

H is in row 2, column 3, so H = 23. This grid has 25 cells, so J is left out.

Decoding works the same way backwards. The code 44 32 23 reads as T (row 4, column 4), M (row 3, column 2), H (row 2, column 3), so the word is **TMH**.

Some papers show two grids, so one letter has two codes. Any correct pair is accepted. Choose the option in which every pair is correct.
""",
    tricks=[
        trick("Common letters match common symbols",
              "When two coded words share letters, circle the shared letters and the shared symbols. They belong together. The letters left over take the symbols left over.",
              "PEN is coded as @ # % and NET as % # & (symbols in the same order as the letters). What is the code for P?",
              ["Common letters E and N match common symbols # and %.", "P is the only letter left in PEN. @ is the only symbol left in its code."],
              "@"),
        trick("Conditions before the table",
              "Read the conditions and test them on the word before you touch the table. The table gives the symbols; the condition only changes their order.",
              None),
    ],
    mistakes=[
        {"wrong": "Coding straight from the table without checking the conditions.", "right": "Test every condition on the word first. Then use the table."},
        {"wrong": "Matching by position when the question says the symbol order may differ.", "right": "Match only common letters with common symbols."},
        {"wrong": "Applying two conditions when the question says only the first one applies.", "right": "Stop at the first condition that matches."},
        {"wrong": "Reading a two-digit code like 10 as two letters.", "right": "Count letters, not digits."},
        {"wrong": "Writing (column, row) in matrix coding.", "right": "Row first, then column, unless the question says otherwise."},
    ],
    revision=[
        "Table given: map letter by letter, in order.",
        "Conditions: test them before coding; stop at the first that applies if told so.",
        "No table: common letters ↔ common symbols; leftovers pair up.",
        "Symbols in any order: two possible symbols means the code cannot be found.",
        "Digit codes: count letters, not digits.",
        "Matrix code = row number, then column number, for each letter.",
    ],
    patterns=[
        pat("cd-p24", "Direct table look-up", "very common",
            "A table of letters and their symbols or digits is printed with the question.",
            None,
            ["Write the symbol under each letter of the word, in order.", "Join the symbols.", "Double-check each letter against the table."],
            "The table fixes every letter, so nothing needs to be worked out.",
            "In a code, P = 3, L = @, A = 7, N = #, E = 5 and T = %. What is the code for PLANT?",
            ["P → 3, L → @, A → 7, N → #, T → %.", "Join them in the order of the word."],
            "3@7#%"),
        pat("cd-p25", "Condition before the table", "common",
            "Conditions like 'if the word begins with a vowel, reverse the codes' are listed with the table.",
            None,
            ["Test the conditions on the word, in order.", "Note the first condition that applies.", "Code from the table, then apply that condition."],
            "The condition changes the order of the symbols, not what each letter stands for.",
            "Codes: E = &, C = @, H = %, O = #. Condition: if the word begins with a vowel, write the codes in reverse order. What is the code for ECHO?",
            ["ECHO begins with the vowel E, so the condition applies.", "Table codes in order: & @ % #.", "Reverse them."],
            "#%@&"),
        pat("cd-p26", "Match common letters with common symbols (no table)", "common",
            "Two coded words are given with no table, like PEN = @ # % and NET = % # &.",
            None,
            ["Circle the letters shared by the two words.", "Circle the symbols shared by their codes and pair them.", "Give each leftover letter the leftover symbol of the same word."],
            "Each letter has one symbol, so shared letters force shared symbols.",
            "In a certain code, PEN is written as @ # % and NET is written as % # &. The symbols follow the order of the letters. How is TEN written?",
            ["E and N are common; # and % are common. By place, E = # and N = %.", "The leftovers give P = @ and T = &.", "TEN = T, E, N."],
            "& # %"),
        pat("cd-p27", "Digits stand for letters by a rule", "common",
            "Letters are matched to digits by a pattern, such as A = 2, B = 4, C = 6.",
            None,
            ["Find the build rule from the examples (for example, double the position).", "Convert the word letter by letter.", "Keep one number per letter; some numbers have two digits."],
            "The build rule is a small step on the positions, so every letter follows it.",
            "In a code, A = 2, B = 4, C = 6 and so on. What is the code for BEAD?",
            ["The rule is: code = 2 × position.", "B = 4, E = 10, A = 2, D = 8.", "Join them in order."],
            "41028"),
        pat("cd-p28", "Matrix coding (row, column)", "very common",
            "A 5 × 5 grid of letters with numbered rows and columns. Each letter is coded as a two-digit pair.",
            None,
            ["Find each letter's row and column in the grid.", "Write the pair as row, then column.", "Join the pairs for the whole word."],
            "The grid is just a table, and the pair is the letter's address.",
            "Rows 1 to 5 (top to bottom) are ABCDE, FGHIK, LMNOP, QRSTU, VWXYZ. Columns are numbered 1 to 5 from the left. What is the code for HIDE?",
            ["H is in row 2, column 3 → 23. I is row 2, column 4 → 24.", "D is row 1, column 4 → 14. E is row 1, column 5 → 15."],
            "23, 24, 14, 15"),
    ],
)

# =====================================================================
# 6. substitution-coding
# =====================================================================
SUBS["substitution-coding"] = dict(
    concept=(
        "The question gives things new names, like 'sky is called sea'. "
        "You work out the real-life answer first, then reply with its new name. "
        "A second format writes sentences in code words; a word shared by two sentences has the code they share."
    ),
    notes=r"""### What substitution means
The question gives things new names. You answer with the new name.

"If sky is called sea, where do birds fly?" Birds fly in the sky. The sky is called sea. So the answer is **sea**.

No calculation is needed. The only skill is keeping the real world and the renamed world apart.

### The two-world method
1. Answer the question in real life first. Where do birds fly? In the sky.
2. Find the new name of that real thing in the chain. Sky is called sea.
3. Give the new name as the answer: sea.

> **Rule:** Use the real world for the fact. Use the renamed world for the answer.

Try one more. "If cold is called hot, what do we use to make ice?" Real answer: cold. Cold is called hot. So the answer is **hot**. The fact never changes. Only the name does.

### Read each link in one direction
"Cloud is called rain" gives the new name of **cloud** only. It tells you nothing about the new name of rain. That comes from another link.

Take the chain: cloud is called rain, rain is called wind, wind is called sun. What do farmers wait for? Real answer: rain. Rain is called wind. So the answer is **wind**, not rain.

> **Watch:** The real answer's word often appears in the chain as someone else's new name. Here "rain" is the new name of cloud. Picking "rain" is the trap.

### Write long chains as a list
Long chains are easy to mix up. Write them as "real → new name":

- day → night
- night → morning
- morning → evening

When do we sleep? Real answer: night. And night → morning. So the answer is **morning**.

### Word-code matching
Some questions write whole sentences in code words. 'red light' = 'pa ka' and 'green light' = 'ka na'.

The word 'light' is in both sentences. The code 'ka' is in both codes. So light = ka, and red = pa.

The full method is in the language coding lesson. In short:

1. A word common to two sentences has the code common to them.
2. Remove fixed codes. A leftover word takes the leftover code.
3. If two codes still fit a word, its code cannot be determined.

Walk it once. 'hot tea' is 'na pi' and 'cold tea' is 'pi ka'. The word 'tea' sits in both sentences, and 'pi' sits in both codes, so tea = pi. The leftovers give hot = na and cold = ka. A third line, 'hot milk' = 'na ru', then fixes milk = ru.

> **Tip:** Never match code words by position. The code order is usually jumbled.

### Numbers standing for words
Some questions give a small dictionary: 1 = come, 2 = home, 3 = sweet, 4 = early. To code "come home early", write the numbers in the same word order: **1 2 4**.

Decoding runs the dictionary the other way. The code '2 3' reads as home, then sweet: **home sweet**.
""",
    tricks=[
        trick("Line up the sentences",
              "Write each sentence above its code. Tick the words that repeat and the code words that repeat. The word you need is either matched directly or is the one item left over.",
              "'red light' = 'pa ka' and 'green light' = 'ka na'. What is the code for 'red'?",
              ["'light' is in both sentences and 'ka' is in both codes, so light = ka.", "In the first sentence, red takes the other code."],
              "pa"),
    ],
    mistakes=[
        {"wrong": "Answering with the real-world word ('rain') instead of its new name.", "right": "Find the real answer, then look up what it is called."},
        {"wrong": "Reading a link backwards ('cloud is called rain' taken as the new name of rain).", "right": "A link names only the word on its left."},
        {"wrong": "Matching code words by their position in the sentence.", "right": "Match by common words and common codes. The order is jumbled."},
        {"wrong": "Picking one of two possible codes.", "right": "If two codes still fit, the answer is 'cannot be determined'."},
        {"wrong": "Missing a repeated word written as a plural (light and lights).", "right": "Treat them as different words unless the question says otherwise."},
    ],
    revision=[
        "Real answer first, then its new name.",
        "Each link names only the word on its left.",
        "Write long chains as a list: real → new name.",
        "Sentence codes: common word ↔ common code; then remove fixed codes.",
        "Two codes still possible → cannot be determined.",
        "Codes for a phrase follow the phrase's own word order.",
    ],
    patterns=[
        pat("cd-p20", "Simple 'is called' chain", "very common",
            "Lines like 'if pen is called pencil, pencil is called eraser …' end with an everyday question.",
            None,
            ["Answer the everyday question with the real thing.", "Find the new name of that real thing in the chain.", "Give the new name as the answer."],
            "The chain only renames things; the fact is real, but the answer must use the new name.",
            "If pen is called pencil, pencil is called eraser, eraser is called book and book is called bag, what do we use to write with ink?",
            ["Real answer: we write with ink using a pen.", "Pen is called pencil."],
            "Pencil"),
        pat("cd-p21", "Word-code matching by elimination", "common",
            "Two or three English sentences are given with code words, usually in jumbled order.",
            None,
            ["Find words common to two sentences; their code is the common code.", "Fix those codes and remove them from each sentence.", "A leftover word takes the leftover code."],
            "A word's code must appear in every sentence that contains the word.",
            "In a code language, 'hot tea' is 'na pi', 'cold tea' is 'pi ka' and 'hot milk' is 'na ru'. What is the code for 'milk'?",
            ["'hot' is in sentences 1 and 3; 'na' is in both codes. So hot = na.", "In 'hot milk' = 'na ru', milk takes the other code."],
            "ru"),
        pat("cd-p22", "Cannot be determined (two codes left)", "common",
            "The asked word appears in only one sentence, and two codes in that sentence are still unclaimed.",
            None,
            ["Fix every code you can with common words.", "Count the codes still possible for the asked word.", "If two remain, answer 'cannot be determined'. Never guess."],
            "With jumbled codes, two leftover codes are equally possible until something pins one down.",
            "In a code language, 'good boy' is 'mi ra' and 'good girl smiles' is 'ra su to'. What is the code for 'girl'?",
            ["'good' is common and 'ra' is common, so good = ra.", "In the second sentence, 'girl' and 'smiles' share 'su' and 'to'.", "Nothing tells them apart."],
            "Cannot be determined"),
        pat("cd-p23", "Long chains", "common",
            "A chain of four or five renames, often with the real answer hidden in the middle.",
            None,
            ["Write the chain as a list: real → new name.", "Answer the question in real life.", "Walk from that real thing to its new name."],
            "A written list stops you from mixing up the two worlds.",
            "If train is called bus, bus is called ship, ship is called aeroplane, aeroplane is called rocket and rocket is called car, what flies in the sky carrying passengers?",
            ["Real answer: an aeroplane.", "In the list, aeroplane → rocket."],
            "Rocket"),
        pat("cd-p35", "A small dictionary of numbers and words", "common",
            "A short list like '1 means pen, 2 means book' is given. The code of a phrase, or the meaning of a number pair, is asked.",
            None,
            ["Read the dictionary once and write it as word → number.", "For a phrase, replace each word by its number.", "Keep the phrase's own word order.", "For decoding, read the numbers back as words."],
            "The dictionary fixes every word, so only the order needs care.",
            "In a certain code, 1 means pen, 2 means book, 3 means bag and 4 means chair. How is 'chair pen' written in this code?",
            ["chair → 4 and pen → 1.", "Write the numbers in the phrase's order."],
            "4 1"),
    ],
)

# =====================================================================
# 7. language-coding
# =====================================================================
SUBS["language-coding"] = dict(
    concept=(
        "Whole sentences are written as code words, like 'good morning sir' = 'ta pa ni'. "
        "The code words are jumbled, so you never match them by position. "
        "Compare sentences: a word shared by two sentences has the code word they share."
    ),
    notes=r"""### What language coding is
A whole sentence is written in a code language. 'good morning sir' becomes 'ta pa ni'.

You get two or three such sentences with their codes. You must find the code of a word, or the meaning of a code.

> **Rule:** The code order is jumbled. 'good morning' = 'ta pa' does not mean good = ta. Never match by position.

### Intersect, then subtract
1. **Intersect.** Find every sentence that contains your word. The word's code is among the code words those sentences share.
2. **Subtract.** Remove codes already fixed for other words. If one code is left, that is the answer.

> **Example:** 'sun is hot' = 'ta mo ri' and 'sun is bright' = 'ri ze mo'. 'sun is' is common, so 'mo ri' belongs to them. The leftover word 'hot' takes the leftover code **ta**.

### When the answer is "cannot be determined"
Sometimes two codes still fit after all the subtraction. Then stop. The answer is **cannot be determined**.

'sky is blue' = 'ta pa ka' and 'sea is deep' = 'pa za la'. Only 'is' is common, so is = pa. 'blue' can be 'ta' or 'ka'. Both are possible.

The same happens in the 'sun is hot' example above. 'sun' can be 'mo' or 'ri'. We know the pair, not which is which.

> **Watch:** Picking one of the two codes is the classic wrong answer. The option "cannot be determined" is there for exactly this case.

### A full question, start to finish
"'good morning sir' is 'ta pa ni', 'good night sir' is 'pa ni ro' and 'night is dark' is 'ro ki su'. What is the code for 'morning'?"

1. Lines 1 and 2 share 'good' and 'sir'. Their codes are 'pa' and 'ni' in some order.
2. Lines 2 and 3 share only 'night'. The common code is 'ro', so night = ro.
3. Line 1 is now short of one word: 'morning'. It takes the leftover code 'ta'.

Answer: **ta**. One fixed code unlocked the rest, line by line.

### Three sentences
More sentences give more information. Work in this order:

1. Find words common to two sentences.
2. Find the codes common to the same two sentences.
3. A word common to two different pairs is fixed by the code common to both pairs.
4. Subtract the fixed codes and assign the leftovers.

With three good sentences, every word usually gets its own code.

### Phrases and digit codes
- To code a phrase like 'sweet home', find each word's code. Then write them in the order the phrase asks.
- Some papers use digits: 'come home' = '1 2' and 'home sweet' = '2 3'. Then home = 2, come = 1 and sweet = 3. The method is the same.

### Reverse questions
"What does 'ra' mean?" Work exactly the same way, then read your mapping backwards. If sing = ra, then 'ra' means **sing**.

> **Tip:** Check your final mapping on every sentence. Each word must have its code in that sentence's code line.
""",
    tricks=[
        trick("Intersect, then subtract",
              "For a word, take the code words shared by all sentences that contain it. Remove codes already fixed for other words. One left is the answer; two left means cannot be determined.",
              "'sun is hot' = 'ta mo ri' and 'sun is bright' = 'ri ze mo'. What is the code for 'hot'?",
              ["'sun is' is common to both, and 'mo ri' is common to both codes.", "In the first sentence, 'hot' takes the leftover code."],
              "ta"),
    ],
    mistakes=[
        {"wrong": "Matching code words by position.", "right": "The order is jumbled. Match by common words and common codes."},
        {"wrong": "Picking one of two equally possible codes.", "right": "Answer 'cannot be determined' when two codes still fit."},
        {"wrong": "Using a code already fixed for another word.", "right": "Each code belongs to one word only. Subtract fixed codes first."},
        {"wrong": "Writing a phrase code in the order you found the words.", "right": "Write it in the phrase's own word order."},
        {"wrong": "Stopping after two sentences when a third one is given.", "right": "Use every sentence. The third one often breaks the tie."},
    ],
    revision=[
        "Never match by position; the code order is jumbled.",
        "A word's code is among the codes shared by every sentence containing it.",
        "Subtract fixed codes; one code left is the answer.",
        "Two codes still possible → cannot be determined.",
        "Phrase codes follow the phrase's word order; digits work the same way.",
        "Check the final mapping on every sentence.",
    ],
    patterns=[
        pat("cd-p29", "Two sentences with common words", "very common",
            "Two sentence–code pairs share one or two words. This is the basic form.",
            None,
            ["Find the words common to both sentences; their codes are the common codes.", "In one sentence, the leftover word takes the leftover code.", "Read the asked word from your mapping."],
            "Codes of common words must sit in both code lines, so the leftover is forced.",
            "In a code language, 'delhi is big' is 'ja pa ni' and 'mumbai is big' is 'sa pa ni'. What is the code for 'delhi'?",
            ["'is big' is common, and 'pa ni' is common.", "In the first sentence, 'delhi' takes the leftover code."],
            "ja"),
        pat("cd-p30", "Three sentences, step-by-step elimination", "common",
            "Three sentence–code pairs; the asked word needs two rounds of subtraction.",
            None,
            ["Compare each pair of sentences for common words and codes.", "A word common to two pairs gets the code common to both.", "Subtract the fixed codes from the asked word's sentence.", "The last code left is the answer."],
            "Each fixed code shrinks the leftovers; three sentences usually finish the job.",
            "In a code language, 'train runs fast' is 'la jo me', 'bus runs fast' is 'la jo fi' and 'fast train' is 'me jo'. What is the code for 'bus'?",
            ["Sentences 1 and 2 share 'runs fast' and 'la jo'.", "Sentences 1 and 3 share 'fast train' and 'me jo'.", "'fast' is in both pairs, so fast = jo. Then runs = la and train = me.", "Sentence 2 leaves bus with the last code."],
            "fi"),
        pat("cd-p31", "Cannot be determined (two codes left)", "common",
            "The asked word appears in only one sentence, and two codes there are still unclaimed.",
            None,
            ["Fix every code you can with common words.", "Count the codes still possible for the asked word.", "If two remain, answer 'cannot be determined'."],
            "Jumbled order makes both leftover codes equally possible.",
            "In a code language, 'sky is blue' is 'ta pa ka' and 'sea is deep' is 'pa za la'. What is the code for 'blue'?",
            ["Only 'is' is common, so is = pa.", "'sky' and 'blue' share 'ta' and 'ka'.", "Nothing tells them apart."],
            "Cannot be determined"),
        pat("cd-p32", "Phrase codes and digit codes", "common",
            "The question asks for the code of a phrase, or the codes are digits like '1 2'.",
            None,
            ["Find each word's code by the usual method.", "Write the codes in the phrase's own word order.", "Treat digit codes exactly like word codes."],
            "A phrase code is just its word codes written in the asked order.",
            "In a code language, 'come home' is '1 2' and 'home sweet' is '2 3'. What is the code for 'sweet home'?",
            ["'home' is common and '2' is common, so home = 2.", "Then come = 1 and sweet = 3.", "'sweet home' = sweet, then home."],
            "3 2"),
        pat("cd-p33", "Reverse: what does the code mean?", "occasional",
            "The question gives a code word and asks which English word it stands for.",
            None,
            ["Fix the mapping word by word with intersect and subtract.", "Find the given code in your mapping.", "Give the English word as the answer."],
            "The mapping works both ways; only the reading direction changes.",
            "In a code language, 'birds fly' is 'lo pe', 'fly high' is 'pe ni' and 'birds sing' is 'lo ra'. What does 'ra' mean?",
            ["birds = lo (sentences 1 and 3). fly = pe (sentences 1 and 2).", "In 'birds sing' = 'lo ra', sing takes 'ra'."],
            "sing"),
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
print("coding-decoding updated")
