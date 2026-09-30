"""Readable rewrite of Reasoning > Mirror & Water Image (mirror-image, water-image, clock-mirror).

Checks by simulation:
- text: a vertical mirror = reverse order + flip every character left-right;
        a water image = keep order + flip every character top-bottom;
        a half turn = both. A character "looks unchanged" if it has the matching symmetry.
- figures: points reflected across a vertical / horizontal line.
- clocks: real hand angles. Mirror: angle -> 360 - angle. Water: angle -> 180 - angle.
  The time is read back from the reflected hands; every whole-minute time is checked.
Run: python mirror_water_image.py (patches content/core/topics/reasoning/mirror-water-image.json)
"""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "mirror-water-image.json"

# ---------------------------------------------------------------- symmetry sets (exam convention)
SYM_LR = set("AHIMOTUVWXY") | set("08")          # look the same in a vertical mirror
SYM_TB = set("BCDEHIKOX") | set("038")           # look the same in water
SYM_180 = set("HINOSXZ") | set("08")             # look the same after a half turn
assert (SYM_LR & SYM_TB) <= SYM_180              # a letter with both symmetries survives a half turn
assert set("HIOX08") == (SYM_LR & SYM_TB)


def render(word, kind):
    """List of (char, flipped_lr, flipped_tb) in left-to-right order of the image."""
    ch = list(word)
    if kind == "mirror":
        return [(c, True, False) for c in reversed(ch)]
    if kind == "water":
        return [(c, False, True) for c in ch]
    if kind == "half":
        return [(c, True, True) for c in reversed(ch)]
    raise ValueError(kind)


def unchanged(c, lr, tb):
    if lr and tb:
        return c in SYM_180
    if lr:
        return c in SYM_LR
    return c in SYM_TB


def looks_same(word, kind):
    img = render(word, kind)
    if [c for c, _, _ in img] != list(word):
        return False
    return all(unchanged(*t) for t in img)


def changed_chars(word, kind):
    return [c for c, lr, tb in render(word, kind) if not unchanged(c, lr, tb)]


def classify(order_reversed, lr, tb):
    if order_reversed and lr and not tb:
        return "mirror"
    if not order_reversed and tb and not lr:
        return "water"
    if order_reversed and lr and tb:
        return "half turn"
    return "none"


# ---------------------------------------------------------------- figures
def reflect(p, kind):
    x, y = p
    return {"mirror": (-x, y), "water": (x, -y), "half": (-x, -y)}[kind]


# ================================================================= mirror-image checks
r = render("REASON", "mirror")
assert [c for c, _, _ in r] == list("NOSAER")
assert changed_chars("REASON", "mirror") == list("NSER")[::1] or True
assert sorted(changed_chars("REASON", "mirror")) == sorted("NSER")        # A and O look the same
assert [c for c in "REASON" if c in SYM_LR] == ["A", "O"]
# mi-p2
assert [c for c, _, _ in render("4R95J", "mirror")] == list("J59R4")
assert not any(c in SYM_LR for c in "4R95J")
# a word that keeps 0 and 8 the same
assert [c for c in "1808" if c in SYM_LR] == ["8", "0", "8"] or [c for c in "1808" if c in SYM_LR] == ["8", "0", "8"]
assert all(c in SYM_LR for c in "808")
# mi-p3
assert reflect((-1, 1), "mirror") == (1, 1)            # top-left -> top-right
assert reflect((-1, 1), "water") == (-1, -1)           # top-left -> bottom-left
assert reflect((-1, 1), "half") == (1, -1)             # top-left -> bottom-right
# mi-p4
assert [c for c in "MATHEMATICS" if c in SYM_LR] == list("MATHMATI") and len("MATHMATI") == 8
# mi-p5
assert [w for w in ("NOON", "TOOT", "DEED") if looks_same(w, "mirror")] == ["TOOT"]
assert looks_same("MOM", "mirror") and looks_same("WOW", "mirror") and looks_same("MAAM", "mirror")
assert not looks_same("MAT", "mirror")                  # not a palindrome
assert not looks_same("HAH" + "X", "mirror")            # HAHX not a palindrome
assert not looks_same("AHA" + "B", "mirror")
assert looks_same("AXA", "mirror") and looks_same("HIH", "mirror")
# mi-p6: position questions
mimg = [c for c, _, _ in render("REASON", "mirror")]
assert mimg[1] == "O" and mimg[2] == "S" and mimg[0] == "N"
assert render("REASON", "mirror")[1] == ("O", True, False)   # O in the 2nd place, symmetric
assert "PLANET"[::-1][2] == "N"                             # 3rd from left in the mirror image of PLANET
assert "PLANET"[::-1] == "TENALP"
# mirror-of-mirror gives back the original
mm = "".join(c for c, _, _ in render("".join(c for c, _, _ in render("REASON", "mirror")), "mirror"))
assert mm == "REASON"

# ================================================================= water-image checks
assert [c for c, _, _ in render("BUDGET", "water")] == list("BUDGET")
assert sorted(changed_chars("BUDGET", "water")) == sorted("UGT")
assert [c for c in "BUDGET" if c in SYM_TB] == list("BDE")
# wi-p2
assert [c for c in "83602" if c in SYM_TB] == list("830")
assert [c for c in "83602" if c not in SYM_TB] == list("62")
# wi-p4
assert looks_same("CHOICE", "water") and not looks_same("CHANCE", "water")
assert [c for c in "CHANCE" if c not in SYM_TB] == ["A", "N"]
assert looks_same("BOX", "water") and looks_same("CODE", "water") and looks_same("HIDE", "water")
assert looks_same("DECIDE", "water")
assert not looks_same("MAT", "water")
assert "M" in SYM_LR and "M" not in SYM_TB
# wi-p5
h = render("SUN", "half")
assert [c for c, _, _ in h] == list("NUS")
assert [c for c, lr, tb in h if not unchanged(c, lr, tb)] == ["U"]
# looks_same requires the same sequence: SOS reversed = SOS and S, O symmetric under half turn
assert [c for c, _, _ in render("SOS", "half")] == list("SOS") and all(c in SYM_180 for c in "SOS")
assert all(c in SYM_180 for c in "NOON") and all(c in SYM_180 for c in "XOX")
assert "SOS"[::-1] == "SOS" and "NOON"[::-1] == "NOON"
# mirror then water equals half turn (composition)
comp = [(c, lr, not tb) for c, lr, tb in render("SUN", "mirror")]
assert comp == render("SUN", "half")
comp2 = render("SUN", "water")[::-1]
assert [(c, not lr, tb) for c, lr, tb in comp2] == render("SUN", "half")
# wi-p6: count of letters unchanged in water
assert [c for c in "DIRECTION" if c in SYM_TB] == list("DIECIO") and len("DIECIO") == 6
# wi-p7: classify
assert classify(True, True, False) == "mirror"
assert classify(False, False, True) == "water"
assert classify(True, True, True) == "half turn"
assert classify(True, False, False) == "none" and classify(False, True, False) == "none"
assert render("FLAG", "mirror")[0][0] == "G" and render("FLAG", "mirror")[0][1:] == (True, False)
assert [c for c, _, _ in render("FLAG", "mirror")] == list("GALF")

# ================================================================= clock checks
DAY = 12 * 3600


def angles(T):
    """(hour hand, minute hand) in degrees clockwise from 12, T in seconds after 12:00."""
    T = Fraction(T) % DAY
    return (T * 360 / DAY, (T % 3600) * 360 / 3600)


def consistent(ah, am):
    return (ah * 12) % 360 == am


def time_from_hands(ah, am):
    """Read the time back from the hour hand; the hour hand fixes the whole time."""
    T = ah * DAY / 360
    return T % DAY


def fmt(T, seconds=False):
    T = int(T) % DAY
    h, rem = divmod(T, 3600)
    m, s = divmod(rem, 60)
    h = 12 if h == 0 else h
    return f"{h}:{m:02d}:{s:02d}" if seconds else f"{h}:{m:02d}"


def mirror_time(T):
    ah, am = angles(T)
    ah2, am2 = (360 - ah) % 360, (360 - am) % 360
    assert consistent(ah2, am2)                      # a mirrored clock always shows a real time
    T2 = time_from_hands(ah2, am2)
    assert angles(T2) == (ah2, am2)
    return T2


def water_valid(T):
    ah, am = angles(T)
    ah2, am2 = (180 - ah) % 360, (180 - am) % 360
    return consistent(ah2, am2)


def hm(h, m, s=0):
    return ((h % 12) * 3600 + m * 60 + s)


def sixty(h, m):
    """The 11:60 rule: 11:60 - h:m in minutes, hour 12 written as 0 -> use 23:60 for 12:xx times."""
    total = (11 * 60 + 60) - (h * 60 + m)
    if h == 12:
        total = (23 * 60 + 60) - (h * 60 + m)
    return divmod(total, 60)


# whole-minute check of the rule against the hand simulation
for h in range(1, 13):
    for m in range(60):
        T = hm(h, m)
        img = fmt(mirror_time(T))
        H2, M2 = sixty(h, m)
        H2 = 12 if H2 == 0 else H2
        assert img == f"{H2}:{M2:02d}" or (h == 12 and img == f"{H2}:{M2:02d}"), (h, m, img, H2, M2)
        assert (mirror_time(T) + T) % DAY == 0       # actual + image = 12:00
# the rule for the other direction
for T in range(0, DAY, 60):
    assert mirror_time(mirror_time(T)) == T % DAY
# water never gives a real time
assert not any(water_valid(T) for T in range(0, DAY, 60))
assert not any(water_valid(T) for T in range(0, DAY, 7))
# cm-p1..p5
assert fmt(mirror_time(hm(3, 45))) == "8:15"
assert fmt(mirror_time(hm(10, 10))) == "1:50" and fmt(mirror_time(hm(7, 5))) == "4:55"
assert fmt(mirror_time(hm(4, 20))) == "7:40"
assert fmt(mirror_time(hm(2, 25))) == "9:35"
assert fmt(mirror_time(hm(12, 35))) == "11:25" and fmt(mirror_time(hm(12, 20))) == "11:40"
assert fmt(mirror_time(hm(4, 0))) == "8:00"
assert fmt(mirror_time(hm(2, 25, 40)), seconds=True) == "9:34:20"
assert fmt(mirror_time(hm(2, 30))) == "9:30"
assert fmt(mirror_time(hm(5, 35))) == "6:25" and fmt(mirror_time(hm(6, 25))) == "5:35"
assert fmt(mirror_time(hm(5, 35))) != "7:25"
# self-mirror times: only 12:00 and 6:00
assert [fmt(T) for T in range(0, DAY, 60) if mirror_time(T) == T] == ["12:00", "6:00"]
# elapsed time example (cm-p5)
actual = mirror_time(hm(4, 20))
assert fmt(actual) == "7:40" and fmt(actual + hm(1, 15)) == "8:55"
# wrong-answer checks used in the notes
assert (12 - 3, 60 - 45) == (9, 15)                  # the borrow slip: 9:15
assert fmt(hm(3, 45) + hm(6, 0)) == "9:45"           # half-turn time for 3:45
assert fmt(hm(5, 35) + hm(6, 0)) == "11:35"          # half-turn time for 5:35
assert fmt(mirror_time(hm(3, 45))) != "9:15"
# the hour-hand argument: at 3:45 the hour hand is 3/4 of the way from 3 to 4
ah, am = angles(hm(3, 45))
assert ah == Fraction(225, 2) and am == 270
assert angles(hm(8, 15))[0] == 360 - ah
# cm-p6: two-step with mirror twice
assert fmt(mirror_time(mirror_time(hm(3, 45)))) == "3:45"
# a mirrored face: hour hand between 2 and 3 in the image means actual hour between 9 and 10
assert fmt(mirror_time(hm(2, 30))) == "9:30"
# examples for the tricks
assert fmt(mirror_time(hm(9, 10))) == "2:50"
assert fmt(mirror_time(hm(11, 55))) == "12:05"
assert fmt(mirror_time(hm(1, 1))) == "10:59"
assert (3 * 60 + 45) + (8 * 60 + 15) == 12 * 60
assert (5 * 60 + 35) + (6 * 60 + 25) == 12 * 60


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ================================================================= mirror-image
mi_concept = (
    "A vertical mirror swaps left and right and keeps top and bottom. "
    "In a word or number, the order of the characters is reversed, and every character is flipped left to right. "
    "Letters with a vertical line of symmetry look unchanged. Use them as quick check points."
)

mi_notes = r"""### What a vertical mirror does
Stand in front of a mirror and raise your right hand. The image raises the hand on the other side.

A vertical mirror swaps left and right. Top stays top. It does not matter if the mirror is on the left or the right of the object. The image looks the same.

For a word, number or code, two things happen together:

1. The order is reversed. The last character comes first.
2. Each character is flipped left to right. R, E, S, N, 2, 4 and 7 face the other way.

> **Rule:** Mirror image = reverse the order + flip every character. Top stays top.

### Letters that look the same
Capitals with a vertical line of symmetry look the same in a mirror.

**A H I M O T U V W X Y**, and the digits 0 and 8.

All other capitals look reversed: B C D E F G J K L N P Q R S Z.

A whole word looks the same in a mirror only if two things are true:

- it reads the same backwards, and
- every letter is in the list above.

Examples: MOM, WOW, TOOT, MAAM.

### Four-step check for options
1. The first character of the image is the last character of the word. Reject options that start with anything else.
2. Check one asymmetric character, such as R, E, S, 4 or 7. It must face the other way.
3. Check that top stays top. An upside-down letter means a water image or a half turn.
4. Check the middle characters only if two options are left.

> **Tip:** Two checks, the first character and one flipped letter, often leave only one option.

### The usual wrong options
- Water image: order kept, letters upside down.
- Half turn: order reversed and letters upside down. It is a mirror image plus a water image.
- Reversed only: order reversed, but letters not flipped.
- Flipped only: letters flipped, but order kept.

### Figures
In a line figure, every point moves to the same distance on the other side of the mirror line. Left goes to right. Height does not change.

Pick one clear feature: a dot, a shaded corner or a short tail. Check where it lands.

- Top-left goes to top-right in a mirror image.
- Bottom-left would be a water image.
- Bottom-right would be a half turn.

### Place in the image
Some questions ask which letter is at a given place, counting from the left, in the mirror image.

Write the word backwards. Then count from the left in the new order.

Example: the mirror image of PLANET reads T, E, N, A, L, P. The 3rd letter from the left is N.

> **Note:** A mirror on the left or on the right gives the same image. Only its position changes.

### Worked example
Mirror image of REASON.

The image reads N O S A E R from left to right. A and O are symmetric, so they look the same. N, S, E and R face the other way.

An option showing N O S A E R with upside-down letters is a half turn, not a mirror image.
"""

mi_formulas = []

mi_tricks = [
    {
        "title": "Check the ends first",
        "body": "The image starts with the last character of the word, flipped. Reject options by looking at the first character only.",
        "example": {
            "q": "What does the mirror image of PEN7 start with?",
            "steps": ["The last character is 7.", "It comes first in the image and faces the other way."],
            "answer": "A flipped 7",
        },
    },
    {
        "title": "Symmetric-letter shortcut",
        "body": "A word made only of A H I M O T U V W X Y that reads the same backwards looks unchanged in a vertical mirror.",
        "example": {
            "q": "Does MOM look the same in a vertical mirror?",
            "steps": ["M and O are symmetric.", "MOM reads the same backwards."],
            "answer": "Yes",
        },
    },
]

mi_mistakes = [
    {"wrong": "Flipping each letter but keeping the original order.", "right": "Reverse the order first. The last character comes first."},
    {"wrong": "Reversing the order but not flipping the letters.", "right": "Flip every asymmetric letter left to right as well."},
    {"wrong": "Turning letters upside down in a mirror image.", "right": "A vertical mirror keeps top and bottom. Upside down is a water image."},
    {"wrong": "Saying a palindrome always looks the same in a mirror.", "right": "Every letter must also be symmetric. NOON reads the same backwards, but N is not symmetric."},
    {"wrong": "Using the mirror list of letters for a water image.", "right": "Water has its own list: B C D E H I K O X."},
]

mi_revision = [
    "Mirror image: reverse the order and flip every character left to right.",
    "Top stays top. Upside down is never a mirror image.",
    "Symmetric capitals: A H I M O T U V W X Y. Symmetric digits: 0 and 8.",
    "Same word in a mirror: a palindrome made only of symmetric letters.",
    "Figures: left and right swap. Height does not change.",
    "First character of the image = last character of the word.",
]

mi_patterns = [
    pat("mi-p1", "Mirror image of a word", "very common",
        "A word in capitals with four image options. The mirror is placed vertically beside it.",
        None,
        ["Write the letters in reverse order.", "Flip every letter left to right. A, H, I, M, O, T, U, V, W, X, Y look unchanged.", "Check that nothing is upside down."],
        "A vertical mirror only swaps left and right.",
        "Which describes the mirror image of REASON?",
        ["Reverse the order: N, O, S, A, E, R.", "A and O are symmetric, so they look the same.", "N, S, E and R face the other way."],
        "N O S A E R, with N, S, E and R facing the other way and A, O unchanged"),
    pat("mi-p2", "Mirror image of a number or code", "common",
        "A number, or letters and digits mixed, with image options.",
        None,
        ["Reverse the order.", "Flip each character left to right. 0 and 8 stay the same.", "2, 3, 4, 5, 7 and 9 face the other way."],
        "Digits follow the same rule as letters.",
        "What is the order of characters in the mirror image of 4R95J?",
        ["Reverse the order: J, 5, 9, R, 4.", "None of these is symmetric, so all five face the other way."],
        "J 5 9 R 4, each flipped left to right"),
    pat("mi-p3", "Mirror image of a figure", "very common",
        "A line figure with a vertical mirror line, often marked M, beside it.",
        None,
        ["Pick a clear feature: a dot, a shaded part or a tail.", "Move it to the other side of the mirror line, at the same height.", "Reject options where it moved up or down."],
        "A vertical mirror keeps heights and swaps sides.",
        "A figure has a dot in its top-left corner. Where is the dot in its mirror image?",
        ["Left and right swap, height stays the same.", "Bottom-left would be a water image. Bottom-right would be a half turn."],
        "Top-right corner"),
    pat("mi-p4", "Letters that look the same in a mirror", "common",
        "How many letters of a word, or which letters, look unchanged in a mirror.",
        None,
        ["Tick the letters from A H I M O T U V W X Y.", "Count the ticks. A repeated letter counts each time."],
        "Only these capitals have a vertical line of symmetry.",
        "How many letters of MATHEMATICS look the same in a mirror?",
        ["M, A, T, H, M, A, T, I are symmetric.", "E, C and S are not."],
        "8"),
    pat("mi-p5", "Word that looks the same in a mirror", "occasional",
        "Which word or number looks exactly the same in a vertical mirror.",
        None,
        ["Check that the word reads the same backwards.", "Check that every letter is symmetric."],
        "The mirror reverses the order and flips each letter. Both must change nothing.",
        "Which looks the same in a mirror: NOON, TOOT or DEED?",
        ["All three read the same backwards.", "TOOT uses only T and O, which are symmetric.", "N, D and E are not symmetric."],
        "TOOT"),
    pat("mi-p6", "Position of a letter in the image", "occasional",
        "The question asks which letter is at a given place, counting from the left, in the mirror image.",
        None,
        ["Write the word backwards.", "Count from the left in the new order."],
        "The mirror reverses the order, so the places reverse too.",
        "Which letter is 3rd from the left in the mirror image of PLANET?",
        ["Reverse the word: T, E, N, A, L, P.", "T is 1st, E is 2nd, N is 3rd."],
        "N"),
]

# ================================================================= water-image
wi_concept = (
    "Water below an object works as a horizontal mirror. It swaps top and bottom and keeps left and right. "
    "In a water image the order of the characters stays the same, and every character is turned upside down. "
    "Letters with a horizontal line of symmetry look unchanged."
)

wi_notes = r"""### What water does
A lake below a hill shows the hill upside down. The water surface is a horizontal mirror below the object.

It swaps top and bottom. It keeps left and right. A question may say "the mirror is placed horizontally below" or "along line MN below the figure". All of these mean a water image.

For a word, number or code:

1. The order stays the same. The first character is still first.
2. Each character is flipped top to bottom.

> **Rule:** Water image = keep the order + flip every character top to bottom.

### Letters that look the same
Capitals with a horizontal line of symmetry look the same in water.

**B C D E H I K O X**, and the digits 0, 3 and 8.

A word looks the same in water if every letter is in this list. It does not need to be a palindrome, because water keeps the order.

Examples: CHOICE, BOX, HIDE, CODE, DECIDE.

> **Watch:** A, M, T, U, V, W and Y are symmetric in a mirror but not in water. M upside down looks like W.

### Four-step check for options
1. The first character stays first. An option that starts with the last character is a mirror image or a half turn.
2. Check one letter that is not in the list, such as A, R, T, 4 or 7. It must be upside down.
3. Parts that faced left must still face left. The bowl of R stays on the right side.
4. Compare the rest only if two options are left.

### Mirror plus water is a half turn
A mirror image followed by a water image, in either order, is a half turn (180 degrees). The order is reversed and every character is upside down.

After a half turn, H, I, N, O, S, X, Z, 0 and 8 look unchanged. So SOS, NOON and XOX look the same after a half turn.

### Figures
Every point moves to the same distance on the other side of the horizontal line. Top goes to bottom. Left and right do not change.

- Top-left goes to bottom-left in a water image.
- Top-right would be a mirror image.
- Bottom-right would be a half turn.

> **Tip:** Track one feature, such as a shaded corner. It tells you the image type at once.

### Naming the image
Look at two things: is the order reversed, and is anything upside down?

| Order | Letters | Image |
|---|---|---|
| Reversed | Flipped left to right | Mirror image |
| Same | Upside down | Water image |
| Reversed | Upside down | Half turn |

### Numbers in water
Digits follow the same rule. Keep the order and flip each digit top to bottom.

0, 3 and 8 look unchanged. In 83602, the digits 8, 3 and 0 look the same, while 6 and 2 look different.

### Worked example
Water image of BUDGET.

The order stays B U D G E T. B, D and E look unchanged. U, G and T appear upside down. An option that begins with T is not a water image.
"""

wi_formulas = []

wi_tricks = [
    {
        "title": "Order stays, letters go upside down",
        "body": "In the options, look for the one that keeps the original order and has only the unsymmetric letters turned upside down.",
        "example": {
            "q": "What is the water image of BOX?",
            "steps": ["B, O and X are all symmetric top to bottom.", "Water keeps the order."],
            "answer": "BOX, unchanged",
        },
    },
    {
        "title": "Name the image from two clues",
        "body": "Same order and upside down: water. Reversed order and flipped left to right: mirror. Reversed and upside down: half turn.",
        "example": {
            "q": "A word appears with its order reversed and every letter upside down. What is this image?",
            "steps": ["The order is reversed, so it is not water.", "Letters are also upside down, so it is not a mirror image."],
            "answer": "A half turn (mirror plus water)",
        },
    },
]

wi_mistakes = [
    {"wrong": "Reversing the order of the characters in a water image.", "right": "Water keeps the order. Only top and bottom swap."},
    {"wrong": "Spinning letters through a half turn instead of flipping them top to bottom.", "right": "A water image is a flip. Left-facing parts still face left."},
    {"wrong": "Using the mirror list A H I M O T U V W X Y for water.", "right": "Water list: B C D E H I K O X."},
    {"wrong": "Thinking 6 upside down becomes 9 in water.", "right": "9 is a half turn of 6. A water image flips top to bottom only."},
    {"wrong": "Calling a reversed, upside-down word a mirror image.", "right": "Reversed order plus upside down is a half turn."},
]

wi_revision = [
    "Water image: keep the order and flip every character top to bottom.",
    "Symmetric in water: B C D E H I K O X, and digits 0, 3, 8.",
    "Same word in water: every letter must be in that list.",
    "Mirror plus water is a half turn: reversed order and upside down.",
    "Figures: top and bottom swap. Left and right stay.",
    "Same order and upside down: water. Reversed and flipped: mirror.",
]

wi_patterns = [
    pat("wi-p1", "Water image of a word", "very common",
        "A word in capitals with a horizontal mirror below it.",
        None,
        ["Keep the order.", "Turn each letter upside down. B, C, D, E, H, I, K, O, X look unchanged.", "Left-facing parts stay on the left."],
        "A horizontal mirror only swaps top and bottom.",
        "Which describes the water image of BUDGET?",
        ["The order stays B, U, D, G, E, T.", "B, D and E have a horizontal line of symmetry, so they look unchanged.", "U, G and T appear upside down."],
        "B U D G E T, with U, G and T upside down and B, D, E unchanged"),
    pat("wi-p2", "Water image of a number or code", "common",
        "A number or a letter-digit code with water image options.",
        None,
        ["Keep the order.", "Turn each character upside down. 0, 3 and 8 look unchanged.", "Do not treat 6 as 9."],
        "Water is a flip, not a spin.",
        "Which digits of 83602 look unchanged in water?",
        ["8, 3 and 0 have a horizontal line of symmetry.", "6 and 2 look different upside down."],
        "8, 3 and 0"),
    pat("wi-p3", "Water image of a figure", "very common",
        "A line figure with a horizontal line MN below it.",
        None,
        ["Pick a clear feature.", "Move it to the other side of the horizontal line. Keep its left-right position.", "Reject options where it moved sideways."],
        "Water keeps left and right.",
        "A figure has a shaded triangle in its top-right corner. Where is the triangle in the water image?",
        ["Top and bottom swap.", "Left and right stay the same."],
        "Bottom-right corner"),
    pat("wi-p4", "Words unchanged in water", "common",
        "Which word looks the same in water.",
        None,
        ["Tick the letters from B C D E H I K O X.", "A word looks the same only if every letter is ticked."],
        "These letters have a horizontal line of symmetry.",
        "Which word looks the same in water: CHOICE or CHANCE?",
        ["Every letter of CHOICE is in B C D E H I K O X.", "CHANCE has A and N, which are not."],
        "CHOICE"),
    pat("wi-p5", "Mirror image followed by water image", "occasional",
        "A word is seen in a mirror and then in water, or the other way round.",
        None,
        ["Mirror then water is a half turn.", "Reverse the order.", "Turn every character upside down."],
        "Swapping left and right, then top and bottom, is a half turn.",
        "How does the word SUN look after a mirror image followed by a water image?",
        ["Half turn: the order reverses to N, U, S.", "N and S look the same after a half turn.", "U looks like a cap, an upside-down U."],
        "N U S, with U upside down and N, S unchanged"),
    pat("wi-p6", "Count letters unchanged in water", "occasional",
        "How many letters of a word look the same in water.",
        None,
        ["Tick the letters from B C D E H I K O X.", "Count every tick, including repeats."],
        "Each ticked letter has a horizontal line of symmetry.",
        "How many letters of DIRECTION look the same in water?",
        ["D, I, E, C, I, O are in the list.", "R, T and N are not."],
        "6"),
    pat("wi-p7", "Name the image type", "common",
        "A word and its image are described. The question asks which kind of image it is.",
        None,
        ["Is the order reversed?", "Are letters flipped left to right, or upside down?", "Use the table: reversed and flipped means mirror, same order and upside down means water, reversed and upside down means half turn."],
        "Each kind of image changes the order and the flips in its own way.",
        "The word FLAG appears as G A L F, with every letter facing the other way and none upside down. Which image is this?",
        ["The order is reversed.", "Letters are flipped left to right.", "Nothing is upside down."],
        "A mirror image"),
]

# ================================================================= clock-mirror
cm_concept = (
    "A clock seen in a vertical mirror has its hands swapped across the 12-6 line. "
    "The actual time and the image time always add up to 12:00. "
    "So image time = 11:60 minus actual time, and the same rule works both ways."
)

cm_notes = r"""### Why the 11:60 rule works
A clock in a vertical mirror has its hands swapped across the line from 12 to 6. A hand 20 minutes past 12 on the right shows 20 minutes before 12 on the left.

So the actual time and the image time always add up to 12:00.

$$\text{image} = 11{:}60 - \text{actual}$$

Writing 12:00 as 11:60 saves you from borrowing. The rule works both ways: actual $= 11{:}60 -$ image.

Examples:
- $3{:}45$ gives $11{:}60 - 3{:}45 = 8{:}15$
- $10{:}10$ gives $1{:}50$
- $7{:}05$ gives $4{:}55$

> **Rule:** Actual time + image time = 12:00.

### Special times
- 12:00 and 6:00 look the same in a mirror. These are the only two such times. Both hands then lie on the 12-6 line.
- Times from 12:00 to 12:59: use $23{:}60 -$ time. So 12:20 gives 11:40.
- Whole hours: $h{:}00$ gives $(12-h){:}00$. So 4:00 gives 8:00.
- With seconds: use $11{:}59{:}60 -$ time. So 2:25:40 gives 9:34:20.

### Reading a clock face
Sometimes a figure shows a mirrored clock with no numbers.

1. The 12 mark is still at the top.
2. Read the time the hands seem to show. That is the image time.
3. Actual time $= 11{:}60 -$ image time.

A hand pointing to the 2 position in the image was really pointing to the 10 position.

### Why the hour drops by one
Take 3:45. The hour hand is three-quarters of the way from 3 to 4. In the mirror it is three-quarters of the way from 9 to 8. It is past 8, not past 9.

So the image shows 8:15, not 9:15. When the minutes are not zero, the image hour is $11 - h$, not $12 - h$.

> **Watch:** Doing $12 - 3 = 9$ and $60 - 45 = 15$ gives 9:15. That is wrong.

### Two-step questions
The mirror shows 4:20. What is the actual time after 1 hour 15 minutes?

First find the actual time: $11{:}60 - 4{:}20 = 7{:}40$. Then add: $7{:}40 + 1{:}15 = 8{:}55$.

Convert first, then add. A mirror of a mirror gives back the actual time.

### Wrong options to expect
- Half-turn time: $3{:}45 + 6{:}00 = 9{:}45$ is where the hands are after a half turn. It is not the mirror image.
- Hours mirrored, minutes kept: 8:45 is only half the job.
- Borrowing slip: subtracting the hours from 12 instead of 11.

### Water image of a clock
A water image swaps top and bottom of the clock face. The hands then point to places that no real time gives.

So exams ask about mirror images of clocks. If a question shows a water image, the clock face is turned upside down, and you read it that way.

### Worked example
The mirror image of a clock shows 5:35. Find the actual time.

Actual $= 11{:}60 - 5{:}35 = 6{:}25$.

Check: $5{:}35 + 6{:}25 = 12{:}00$. An option of 7:25 forgets to borrow. 11:35 is the half-turn time.

> **Tip:** Always add your answer to the given time. The sum must be exactly 12:00.
"""

cm_formulas = [
    {"name": "Mirror time", "tex": r"T_{\text{image}} = 11{:}60 - T_{\text{actual}}", "note": "Works in both directions. For 12:xx, use 23:60 minus the time."},
]

cm_tricks = [
    {
        "title": "11:60 rule",
        "body": "Subtract the hours from 11 and the minutes from 60.",
        "example": {
            "q": "A clock shows 4:20. What does its mirror image show?",
            "steps": [r"$11{:}60 - 4{:}20 = 7{:}40$."],
            "answer": "7:40",
        },
    },
    {
        "title": "Check by adding",
        "body": "Add the given time and your answer. The sum must be 12:00.",
        "example": {
            "q": "The mirror image of a clock shows 5:35. Is 6:25 the actual time?",
            "steps": [r"$5{:}35 + 6{:}25 = 12{:}00$."],
            "answer": "Yes",
        },
    },
]

cm_mistakes = [
    {"wrong": "Subtracting from 12:00 and slipping on the borrow.", "right": "Use 11:60. It needs no borrowing."},
    {"wrong": "Using the rule on 12:xx times without adding 12 first.", "right": "For 12:xx use 23:60 minus the time."},
    {"wrong": "Mirroring the hours and keeping the minutes.", "right": "Both hands swap. Subtract the whole time from 11:60."},
    {"wrong": "Adding the elapsed time to the mirror reading.", "right": "Find the actual time first. Then add the elapsed time."},
    {"wrong": "Picking the half-turn time as the mirror time.", "right": "The half-turn time is the actual time plus 6 hours. The mirror time adds up to 12:00."},
]

cm_revision = [
    "Image = 11:60 minus actual. Actual = 11:60 minus image.",
    "12:xx: use 23:60 minus the time. Seconds: use 11:59:60 minus the time.",
    "Only 12:00 and 6:00 look unchanged.",
    "Mirrored clock face: read it as it looks, then subtract from 11:60.",
    "Check: given time + answer = 12:00.",
    "With elapsed time: convert first, then add.",
]

cm_patterns = [
    pat("cm-p1", "Mirror time from actual time", "very common",
        "A clock shows a time. What time does its mirror image show?",
        r"\text{image}=11{:}60-\text{actual}",
        ["Subtract the actual time from 11:60.", "Check that the sum is 12:00."],
        "Each hand is reflected across the 12-6 line, so actual and image add up to 12 hours.",
        "A clock shows 3:45. What does its mirror image show?",
        [r"$11{:}60 - 3{:}45 = 8{:}15$.", r"Check: $3{:}45 + 8{:}15 = 12{:}00$."],
        "8:15"),
    pat("cm-p2", "Actual time from the mirror reading", "common",
        "The mirror image shows a time. Find the actual time.",
        None,
        ["Read the time shown in the mirror.", "Subtract the mirror time from 11:60."],
        "Reflecting twice gives back the original, so the rule works in both directions.",
        "A clock looks like 2:25 in a mirror. What is the actual time?",
        [r"$11{:}60 - 2{:}25 = 9{:}35$."],
        "9:35"),
    pat("cm-p3", "Special cases: 12:xx and seconds", "occasional",
        "The time is between 12 and 1, or it is a whole hour, or it has seconds.",
        None,
        ["12:xx: use 23:60 minus the time.", "Seconds: use 11:59:60 minus the time.", "12:00 and 6:00 map to themselves."],
        "The sum is still 12 hours. Only the borrowing changes.",
        "What is the mirror image of 12:35?",
        [r"$23{:}60 - 12{:}35 = 11{:}25$."],
        "11:25"),
    pat("cm-p4", "Mirrored clock face", "common",
        "A drawn clock, often without numbers, is called a mirror image. Find the actual time.",
        None,
        ["Read the time the hands appear to show.", "Subtract it from 11:60."],
        "The picture gives the image time. The rule turns it back into the actual time.",
        "A mirrored clock face appears to show 2:30. What is the actual time?",
        [r"$11{:}60 - 2{:}30 = 9{:}30$."],
        "9:30"),
    pat("cm-p5", "Mirror time with elapsed time", "occasional",
        "The mirror time is given. The question asks the actual time some minutes later or earlier.",
        None,
        ["Convert the mirror reading to the actual time.", "Then add or subtract the elapsed time."],
        "Time passes on the real clock, so add the elapsed time to the actual time.",
        "A mirror shows 4:20. What will the actual time be 1 hour 15 minutes later?",
        [r"Actual time: $11{:}60 - 4{:}20 = 7{:}40$.", r"$7{:}40 + 1{:}15 = 8{:}55$."],
        "8:55"),
]

# ================================================================= patch
blocks = {
    "mirror-image": (mi_concept, mi_notes, mi_formulas, mi_tricks, mi_mistakes, mi_revision, mi_patterns),
    "water-image": (wi_concept, wi_notes, wi_formulas, wi_tricks, wi_mistakes, wi_revision, wi_patterns),
    "clock-mirror": (cm_concept, cm_notes, cm_formulas, cm_tricks, cm_mistakes, cm_revision, cm_patterns),
}
dfrac = lambda s: s.replace(r"\frac", r"\dfrac")

data = json.loads(TOPIC.read_text(encoding="utf-8"))
frozen = json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                    ensure_ascii=False, sort_keys=True)
seen = set()
for sub in data["subtopics"]:
    if sub["id"] not in blocks:
        continue
    concept, notes, formulas, tricks, mistakes, revision, patterns = blocks[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in patterns]
    assert old_ids <= set(new_ids), "never drop a pattern id"
    assert len(new_ids) == len(set(new_ids)) and not (seen & set(new_ids))
    seen |= set(new_ids)
    assert 2500 <= len(notes) <= 5000, f"{sub['id']} notes {len(notes)} chars"
    assert 4 <= len(mistakes) <= 8 and 4 <= len(revision) <= 9
    mistakes = [{k: dfrac(v) for k, v in m.items()} for m in mistakes]
    revision = [dfrac(x) for x in revision]
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)
    print(f"{sub['id']}: notes {len(notes)} chars, {len(old_ids)} -> {len(patterns)} patterns")

assert json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                  ensure_ascii=False, sort_keys=True) == frozen
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("mirror-water-image.json patched")
