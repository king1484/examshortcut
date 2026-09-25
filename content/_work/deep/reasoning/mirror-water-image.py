"""Phase-2 deep content for reasoning/mirror-water-image. Idempotent: `py -3 mirror-water-image.py`.

Models:
  * words/codes: a list of glyph states (char, flipped_lr, flipped_tb). Mirror = reverse
    order + toggle lr; water = toggle tb; half turn = both. Options are compared through a
    visual canonical form (symmetric letters collapse), so no two options look alike.
  * figures: nonverbal_lib.Shape on a lattice, transformed by exact isometries.
  * clocks: time in seconds -> hand angles; the mirror negates every angle, and the image
    time is read back from the hour hand and checked against the other hands.
"""
import math
import os
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from nonverbal_lib import *  # noqa
from mirror_water_image_notes import NOTES, PATTERNS, PYQS

T = "mirror-water-image"
d = load(T)
for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])
d["pyqPatterns"] = PYQS

NQ = []
_ctr = {}


def nid(sub):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    return f"{sub}-p{_ctr[sub]:02d}"


def add(sub, pat, q, ans, wrong, solution, diff="medium", shortcut=None, t=45, figure=None):
    NQ.append(Q(nid(sub), q, ans, wrong, solution, shortcut=shortcut, diff=diff, sub=sub,
                pat=pat, t=t, figure=figure))


def pick_distinct(ans_key, cands, keyf, n=3):
    """cands: list of (label, obj). Keep the first n whose keys differ from the answer and each other."""
    seen = {ans_key}
    out = []
    for lab, obj in cands:
        k = keyf(obj)
        if k in seen:
            continue
        seen.add(k)
        out.append((lab, obj))
        if len(out) == n:
            break
    assert len(out) == n, "not enough visually distinct distractors"
    return out


# ================================================================== checks of facts in the notes
MIRROR_SYM_LETTERS = set("AHIMOTUVWXY")
WATER_SYM_LETTERS = set("BCDEHIKOX")
assert MIRROR_SYM_LETTERS == {c for c in V_SYM if c.isalpha()}
assert WATER_SYM_LETTERS == {c for c in H_SYM if c.isalpha()}


def same_in_mirror(w):
    return glyph_key(g_mirror(g_plain(w))) == glyph_key(g_plain(w))


def same_in_water(w):
    return glyph_key(g_water(g_plain(w))) == glyph_key(g_plain(w))


def same_half_turn(w):
    return glyph_key(g_rot180(g_plain(w))) == glyph_key(g_plain(w))


for w in ("MOM", "WOW", "TOOT", "MAAM"):
    assert same_in_mirror(w), w
for w in ("NOON", "DEED", "BOB"):
    assert not same_in_mirror(w), w
for w in ("CHOICE", "BOX", "HIDE", "CODE", "DECIDE"):
    assert same_in_water(w), w
assert not same_in_water("CHANCE") and not same_in_water("DEFINE")
for w in ("SOS", "NOON", "XOX"):
    assert same_half_turn(w), w
assert sum(c in MIRROR_SYM_LETTERS for c in "MATHEMATICS") == 8
assert [c for c in "BUDGET" if c in WATER_SYM_LETTERS] == list("BDE")
assert [c for c in "83602" if c in H_SYM] == list("830")
assert [s[0] for s in g_mirror(g_plain("REASON"))] == list("NOSAER")
assert [s[0] for s in g_rot180(g_plain("SUN"))] == list("NUS")


# ================================================================== word / code image questions
DESC = {
    "mirror": "the mirror image (order reversed, letters flipped left-right)",
    "water": "the water image (order kept, characters upside down)",
    "rot180": "a 180° turn (order reversed and characters upside down)",
    "reverse_only": "only reversed in order, with the characters not flipped",
    "flip_in_place": "flipped characters left in the original order",
    "rev_water": "reversed in order with characters upside down but not flipped left-right",
    "plain": "the original, unchanged",
}
MAKE = {
    "mirror": g_mirror, "water": g_water, "rot180": g_rot180,
    "reverse_only": g_reverse_only, "flip_in_place": g_flip_in_place,
    "rev_water": lambda s: [(c, fx, 1 - fy) for c, fx, fy in reversed(s)],
    "plain": lambda s: list(s),
}


def word_q(sub, pat, word, kind, order, diff="medium", q=None, t=45):
    base = g_plain(word)
    ans = MAKE[kind](base)
    cands = [(k, MAKE[k](base)) for k in order]
    ws = pick_distinct(glyph_key(ans), cands, glyph_key)
    chars = list(word)
    if kind == "mirror":
        sym = sorted({c for c in chars if c in V_SYM})
        asym = [c for c in dict.fromkeys(chars) if c not in V_SYM]
        sol = (f"A vertical mirror reverses the order and flips every character left-right; top stays top. "
               f"Read left to right, the image shows **{' '.join(reversed(chars))}**. ")
        if sym:
            sol += f"{', '.join(sym)} look the same because they are symmetric about a vertical line; "
        sol += f"{', '.join(asym)} face the other way. "
        qq = q or f"Which option is the **mirror image** of **{word}** when the mirror is placed vertically on its right?"
        shortcut = f"The image must start with the last character, {chars[-1]}, and nothing may be upside down."
    elif kind == "water":
        sym = sorted({c for c in chars if c in H_SYM})
        asym = [c for c in dict.fromkeys(chars) if c not in H_SYM]
        sol = (f"Water (a horizontal mirror below) keeps the order and turns every character upside down; "
               f"left stays left. The image still reads **{' '.join(chars)}**. ")
        if sym:
            sol += f"{', '.join(sym)} look the same because they are symmetric about a horizontal line; "
        sol += f"{', '.join(asym)} appear upside down. "
        qq = q or f"Which option is the **water image** of **{word}**?"
        shortcut = f"The image must still start with {chars[0]}, with its characters upside down."
    else:  # rot180 = mirror followed by water
        sym = sorted({c for c in chars if c in R_SYM})
        sol = (f"A mirror image followed by a water image is a half turn (180°): the order is reversed "
               f"(**{' '.join(reversed(chars))}**) and every character is upside down and flipped. ")
        if sym:
            sol += f"{', '.join(sym)} look the same after a half turn. "
        qq = q or (f"The mirror image of **{word}** (mirror on the right) is seen again as a water image. "
                   f"Which option shows the final image?")
        shortcut = "Mirror + water = 180° turn: reversed order, characters upside down."
    parts = [f"one is {DESC[k]}" for k, _ in ws]
    sol += "Among the other options, " + "; ".join(parts) + "."
    add(sub, pat, qq, glyph_svg(ans), [glyph_svg(o) for _, o in ws], sol, diff=diff,
        shortcut=shortcut, t=t)


M_ORDER = ["water", "rot180", "reverse_only", "flip_in_place", "plain"]
W_ORDER = ["mirror", "rot180", "rev_water", "plain", "flip_in_place"]
R_ORDER = ["mirror", "water", "reverse_only", "plain"]

# mirror-image: words and codes
word_q("mirror-image", "mi-p1", "KINGDOM", "mirror", M_ORDER, "easy")
word_q("mirror-image", "mi-p1", "PLANETS", "mirror", ["reverse_only", "water", "rot180"], "medium")
word_q("mirror-image", "mi-p1", "JOURNEY", "mirror", ["flip_in_place", "rot180", "water"], "medium",
       q="Which option is the **mirror image** of **JOURNEY** when the mirror is placed vertically on its left?")
word_q("mirror-image", "mi-p2", "SK47R2", "mirror", ["rot180", "reverse_only", "water"], "medium")
word_q("mirror-image", "mi-p2", "N4J7E5", "mirror", ["flip_in_place", "water", "reverse_only"], "hard", t=50)
word_q("mirror-image", "mi-p2", "2024", "mirror", ["water", "reverse_only", "rot180"], "easy",
       q="Which option is the **mirror image** of the number **2024** (mirror placed vertically on its right)?")

# water-image: words and codes
word_q("water-image", "wi-p1", "GARDEN", "water", W_ORDER, "easy")
word_q("water-image", "wi-p1", "FRUITS", "water", ["rot180", "mirror", "rev_water"], "medium")
word_q("water-image", "wi-p1", "PLURAL", "water", ["rev_water", "mirror", "rot180"], "medium",
       q="A mirror is placed horizontally below the word **PLURAL** (along a line MN). Which option is its image?")
word_q("water-image", "wi-p2", "Z5K2PQ", "water", ["mirror", "rot180", "rev_water"], "medium")
word_q("water-image", "wi-p2", "TR7A45", "water", ["rot180", "rev_water", "mirror"], "hard", t=50)
word_q("water-image", "wi-p5", "FRESH", "rot180", R_ORDER, "medium")
word_q("water-image", "wi-p5", "LJ42", "rot180", ["water", "mirror", "reverse_only"], "hard", t=50)


# ================================================================== symmetric letter questions (text)
def count_q(sub, pat, word, which, diff="easy"):
    sset = MIRROR_SYM_LETTERS if which == "mirror" else WATER_SYM_LETTERS
    hits = [c for c in word if c in sset]
    miss = [c for c in word if c not in sset]
    n = len(hits)
    other = sum(c in (WATER_SYM_LETTERS if which == "mirror" else MIRROR_SYM_LETTERS) for c in word)
    wrong = []
    for w in (other, n + 1, n - 1, n + 2, n - 2):
        if w != n and w > 0 and w not in wrong:
            wrong.append(w)
    lst = "A H I M O T U V W X Y" if which == "mirror" else "B C D E H I K O X"
    where = "in a vertical mirror" if which == "mirror" else "in a water image"
    sol = (f"Letters that look the same {where}: {lst}. In {' '.join(word)}, the matching letters are "
           f"{', '.join(hits)} = **{n}**. The rest ({', '.join(dict.fromkeys(miss))}) change.")
    add(sub, pat, f"How many letters of the word **{word}** look exactly the same {where} (checked one by one)?",
        n, wrong[:3], sol, diff=diff, shortcut=f"Tick letters from {lst}; count repeats.", t=35)


count_q("mirror-image", "mi-p4", "AUTOMOBILE", "mirror")
count_q("mirror-image", "mi-p4", "HYDROGEN", "mirror")
count_q("water-image", "wi-p4", "BIOCHEMIST", "water")


def same_word_q(sub, pat, words, test, where, diff="medium"):
    ok = [w for w in words if test(w)]
    assert len(ok) == 1, (words, ok)
    ans = ok[0]
    if where == "mirror":
        why = []
        for w in words:
            if w == ans:
                continue
            if w != w[::-1]:
                why.append(f"{w} does not read the same backwards")
            else:
                bad = [c for c in dict.fromkeys(w) if c not in MIRROR_SYM_LETTERS]
                why.append(f"{w} has {', '.join(bad)}, which {'is' if len(bad) == 1 else 'are'} not symmetric")
        sol = (f"In a mirror a word looks unchanged only if it reads the same backwards **and** every letter "
               f"is in A H I M O T U V W X Y. **{ans}** passes both tests. " + "; ".join(why) + ".")
        qq = "Which word will look **exactly the same** in a vertical mirror?"
    else:
        why = []
        for w in words:
            if w == ans:
                continue
            bad = [c for c in dict.fromkeys(w) if c not in WATER_SYM_LETTERS]
            why.append(f"{w} has {', '.join(bad)}")
        sol = (f"Water keeps the order, so a word looks unchanged if every letter is in B C D E H I K O X. "
               f"**{ans}** uses only these letters. " + "; ".join(why) + ".")
        qq = "Which word will look **exactly the same** in its water image?"
    add(sub, pat, qq, ans, [w for w in words if w != ans], sol, diff=diff, t=40)


same_word_q("mirror-image", "mi-p5", ["TOOT", "NOON", "DEED", "TOOK"], same_in_mirror, "mirror")
same_word_q("mirror-image", "mi-p5", ["MAAM", "RADAR", "LEVEL", "HAIM"], same_in_mirror, "mirror")
same_word_q("water-image", "wi-p4", ["BOXED", "BOXER", "MIXED", "FIXED"], same_in_water, "water")


# half-turn text question (wi-p5)
def half_turn_q(words, diff="hard"):
    ok = [w for w in words if same_half_turn(w)]
    assert len(ok) == 1, ok
    ans = ok[0]
    why = []
    for w in words:
        if w == ans:
            continue
        bad = [c for c in dict.fromkeys(w) if c not in R_SYM]
        if bad:
            why.append(f"{w} has {', '.join(bad)}, which change{'s' if len(bad) == 1 else ''} in a half turn")
        else:
            why.append(f"{w} does not read the same backwards")
    sol = ("A mirror image followed by a water image is a 180° turn: the order is reversed and each "
           "letter is turned upside down. The word looks unchanged only if it reads the same backwards and "
           f"every letter is in H I N O S X Z. **{ans}** passes. " + "; ".join(why) + ".")
    add("water-image", "wi-p5",
        "A word is seen in a vertical mirror, and that image is then seen in water. Which word will look "
        "**exactly the same** at the end?", ans, [w for w in words if w != ans], sol, diff=diff, t=45)


half_turn_q(["SOS", "DAD", "TOT", "NUN"])


# ================================================================== figure questions (Shape model)
def region(p, W, H):
    x, y = p
    col = "left" if x < W / 2 else ("right" if x > W / 2 else "middle")
    row = "top" if y < H / 2 else ("bottom" if y > H / 2 else "middle")
    return f"{row}-{col}"


def make_shape(seed, n=4, need=None):
    """Random asymmetric lattice figure: a path, a dot and a small shaded triangle."""
    rnd = random.Random(seed)
    N = 4
    for _attempt in range(20000):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        p = (rnd.randint(0, N), rnd.randint(0, N))
        path = [p]
        for _ in range(n):
            opts = []
            for dx, dy in dirs:
                for L in (1, 2):
                    q = (path[-1][0] + dx * L, path[-1][1] + dy * L)
                    if 0 <= q[0] <= N and 0 <= q[1] <= N and q not in path:
                        opts.append(q)
            if not opts:
                break
            path.append(rnd.choice(opts))
        if len(path) < n + 1:
            continue
        els = [("L", path[i], path[i + 1]) for i in range(len(path) - 1)]
        # dot away from the path, not on a centre line
        def on_path(pt):
            for a, b in zip(path, path[1:]):
                if ((b[0] - a[0]) * (pt[1] - a[1]) - (b[1] - a[1]) * (pt[0] - a[0]) == 0
                        and min(a[0], b[0]) <= pt[0] <= max(a[0], b[0])
                        and min(a[1], b[1]) <= pt[1] <= max(a[1], b[1])):
                    return True
            return False

        free = [(x, y) for x in (0, 1, 3, 4) for y in (0, 1, 3, 4) if not on_path((x, y))]
        dot = rnd.choice(free)
        cx, cy = rnd.choice([(0, 0), (3, 0), (0, 3), (3, 3)])
        tri = rnd.choice([
            ((cx, cy), (cx + 1, cy), (cx, cy + 1)),
            ((cx + 1, cy), (cx + 1, cy + 1), (cx, cy)),
        ])
        els += [("D", dot), ("S", tri)]
        s = Shape(N, N, els)
        imgs = [s, s.mirror(), s.water(), s.rot180(), s.rot90(), s.rot270(), s.transpose(),
                s.rot90().water()]
        if len({i.key() for i in imgs}) != 8:
            continue
        if need and not need(s, dot):
            continue
        return s, dot
    raise RuntimeError("no asymmetric shape found")


FIG_DESC = {
    "mirror": "the mirror image (left and right swapped)",
    "water": "the water image (top and bottom swapped)",
    "rot180": "the figure turned through 180°",
    "rot90": "the figure turned through 90°",
    "near": "almost right, but the dot has not been moved",
    "plain": "the figure itself, unchanged",
}


def fig_q(sub, pat, seed, kind, order, diff="medium", t=45):
    if kind == "mirror":
        need = lambda s, dot: dot[0] != 2  # noqa
    else:
        need = lambda s, dot: dot[1] != 2  # noqa
    s, dot = make_shape(seed, need=need)
    dot_i = [i for i, e in enumerate(s.els) if e[0] == "D"][0]
    tf = {"mirror": s.mirror, "water": s.water}[kind]
    ans = tf()
    other_idx = set(range(len(s.els))) - {dot_i}
    cands_all = {
        "mirror": s.mirror(), "water": s.water(), "rot180": s.rot180(), "rot90": s.rot90(),
        "near": tf(only=other_idx), "plain": s,
    }
    ws = pick_distinct(ans.key(), [(k, cands_all[k]) for k in order], lambda x: x.key())
    D = Shape._p(dot)
    img_dot = [e for e in ans.els if e[0] == "D"][0][1]
    r0, r1 = region(D, s.W, s.H), region(img_dot, s.W, s.H)
    if kind == "mirror":
        qq = "Which option is the **mirror image** of the given figure, with the mirror placed vertically along MN on its right?"
        rule = "A vertical mirror swaps left and right and keeps every height."
        fig = s.svg(16, 6, frame=True, mirror_line="right")
    else:
        qq = "Which option is the **water image** of the given figure (mirror placed horizontally below it)?"
        rule = "Water swaps top and bottom and keeps left and right."
        fig = s.svg(16, 6, frame=True, mirror_line="below")
    sol = (f"{rule} Track the dot: it is in the {r0} part of the figure, so in the image it must be in the "
           f"{r1} part. The shaded triangle and the line path move the same way. "
           "Among the other options, " + "; ".join(f"one is {FIG_DESC[k]}" for k, _ in ws) + ".")
    add(sub, pat, qq, ans.svg(16, 6, frame=True), [o.svg(16, 6, frame=True) for _, o in ws], sol,
        diff=diff, t=t, shortcut="Follow one feature (the dot) to its new corner, then check one more.",
        figure=fig)


fig_q("mirror-image", "mi-p3", 11, "mirror", ["water", "rot180", "near", "plain"], "easy")
fig_q("mirror-image", "mi-p3", 23, "mirror", ["near", "rot180", "water"], "medium")
fig_q("mirror-image", "mi-p3", 37, "mirror", ["rot180", "near", "rot90"], "hard")
fig_q("water-image", "wi-p3", 41, "water", ["mirror", "rot180", "near"], "easy")
fig_q("water-image", "wi-p3", 53, "water", ["near", "mirror", "rot90"], "medium")
fig_q("water-image", "wi-p3", 67, "water", ["rot180", "near", "mirror"], "hard")


# ================================================================== clocks
DAY = 12 * 3600  # seconds on a 12-hour dial


def angles(ts):
    """hour, minute, second hand angles (degrees clockwise from 12), exact."""
    return (Fr(ts, 120) % 360, Fr(ts, 10) % 360, Fr(ts * 6) % 360)


def mirror_clock(ts):
    """Reflect every hand across the 12-6 line, then read the time back from the hour hand."""
    h, m, s = angles(ts)
    h2, m2, s2 = (-h) % 360, (-m) % 360, (-s) % 360
    ts2 = h2 * 120
    assert ts2.denominator == 1
    ts2 = int(ts2) % DAY
    assert angles(ts2) == (h2, m2, s2), "hands inconsistent"
    return ts2


def hm(h, m, s=0):
    return (h % 12) * 3600 + m * 60 + s


def fmt(ts, sec=False):
    ts %= DAY
    h, r = divmod(ts, 3600)
    m, s = divmod(r, 60)
    h = h or 12
    return f"{h}:{m:02d}:{s:02d}" if sec else f"{h}:{m:02d}"


# facts quoted in the notes
assert fmt(mirror_clock(hm(3, 45))) == "8:15" and fmt(mirror_clock(hm(10, 10))) == "1:50"
assert fmt(mirror_clock(hm(7, 5))) == "4:55" and fmt(mirror_clock(hm(12, 20))) == "11:40"
assert fmt(mirror_clock(hm(4, 0))) == "8:00" and fmt(mirror_clock(hm(12, 35))) == "11:25"
assert fmt(mirror_clock(hm(2, 25, 40)), True) == "9:34:20"
assert fmt(mirror_clock(hm(2, 25))) == "9:35" and fmt(mirror_clock(hm(2, 30))) == "9:30"
assert [t for t in range(0, DAY, 60) if mirror_clock(t) == t] == [0, hm(6, 0)]
assert fmt(mirror_clock(hm(4, 20)) + hm(1, 15)) == "8:55"
assert fmt(mirror_clock(hm(9, 10)) + hm(0, 30)) == "3:20"


def naive(ts):
    """12:00 minus time done digit-wise without borrowing: (12-h):(60-m)."""
    h, r = divmod(ts % DAY, 3600)
    m = r // 60
    h = h or 12
    return hm((12 - h) % 12, (60 - m) % 60)


assert fmt(mirror_clock(hm(5, 35))) == "6:25" and fmt(naive(hm(5, 35))) == "7:25" and fmt(hm(5, 35) + 6 * 3600) == "11:35"
assert fmt(naive(hm(3, 45))) == "9:15"


def time_opts(ans, given, extra=(), sec=False):
    cands = list(extra) + [naive(given) if not sec else ans + 3600, (given + 6 * 3600),
                           ans + 3600, ans - 3600, (ans // 3600) * 3600 + given % 3600, given]
    out = []
    for c in cands:
        f = fmt(c, sec)
        if f != fmt(ans, sec) and f not in out:
            out.append(f)
    return out[:3]


def clock_q(sub, pat, h, m, s=None, diff="easy", direction="to_image", t=30):
    sec = s is not None
    given = hm(h, m, s or 0)
    ans = mirror_clock(given)
    base = "11:59:60" if sec else ("23:60" if h == 12 else "11:60")
    g, a = fmt(given, sec), fmt(ans, sec)
    if direction == "to_image":
        qq = f"A wall clock shows **{g}**. What time will its mirror image show?"
    else:
        qq = f"In a mirror, a wall clock appears to show **{g}**. What is the actual time?"
    sol = (f"Actual time + image time = 12:00, so the answer is {base} − {g} = **{a}**. "
           f"Check: {g} + {a} = {'24:00' if h == 12 else '12:00'}.")
    if h == 12:
        sol += " For a time between 12 and 1, borrow from 24:00 (23:60)."
    if sec:
        sol += " With seconds, write 12:00:00 as 11:59:60."
    add(sub, pat, qq, a, time_opts(ans, given, sec=sec), sol, diff=diff, t=t,
        shortcut=f"Subtract from {base}.")


clock_q("clock-mirror", "cm-p1", 4, 40, diff="easy")
clock_q("clock-mirror", "cm-p1", 8, 5, diff="easy")
clock_q("clock-mirror", "cm-p1", 1, 55, diff="medium")
clock_q("clock-mirror", "cm-p2", 5, 35, diff="easy", direction="to_actual")
clock_q("clock-mirror", "cm-p2", 11, 20, diff="medium", direction="to_actual")
clock_q("clock-mirror", "cm-p3", 12, 35, diff="medium")
clock_q("clock-mirror", "cm-p3", 2, 25, 40, diff="hard", t=45)

# which times look unchanged (text, cm-p3)
same_times = [fmt(t) for t in range(0, DAY, 60) if mirror_clock(t) == t]
assert same_times == ["12:00", "6:00"]
add("clock-mirror", "cm-p3",
    "At which of these times will a clock and its mirror image show **the same time**?",
    "6:00", ["3:00", "9:30", "12:30"],
    "The image equals the actual time only when both hands lie on the 12–6 line, because only that line "
    "is its own mirror image. That happens at 12:00 and **6:00**. At 3:00 the image shows 9:00; at 9:30 it "
    "shows 2:30; at 12:30 it shows 11:30.", diff="medium", t=35,
    shortcut="Only 12:00 and 6:00 are unchanged.")
assert fmt(mirror_clock(hm(3, 0))) == "9:00" and fmt(mirror_clock(hm(9, 30))) == "2:30"
assert fmt(mirror_clock(hm(12, 30))) == "11:30"


def elapsed_q(h, m, dh, dm, later=True, diff="medium"):
    R = hm(h, m)
    D = (dh * 3600 + dm * 60) * (1 if later else -1)
    act = mirror_clock(R)
    ans = act + D
    trap = mirror_clock((R + D) % DAY)  # converting after adding
    extra = [trap, R + D, act - D]
    dtxt = (f"{dh} hour{'s' if dh != 1 else ''} " if dh else "") + (f"{dm} minutes" if dm else "")
    dtxt = dtxt.strip()
    word = "later" if later else "earlier"
    qq = (f"A clock seen in a mirror shows **{fmt(R)}**. What will the **actual** time be {dtxt} {word}?")
    sol = (f"First convert the mirror reading: actual = 11:60 − {fmt(R)} = {fmt(act)}. "
           f"Then {'add' if later else 'subtract'} {dtxt}: **{fmt(ans)}**. "
           f"Adding first and converting afterwards gives {fmt(trap)}, which is wrong because time passes on "
           f"the real clock.")
    add("clock-mirror", "cm-p5", qq, fmt(ans), time_opts(ans, R, extra=extra), sol, diff=diff, t=45,
        shortcut="Convert to the actual time first, then add or subtract.")


elapsed_q(4, 20, 1, 15, True, "medium")
elapsed_q(9, 10, 0, 30, True, "medium")
elapsed_q(3, 40, 2, 25, False, "hard")


# ---- clock faces (cm-p4)
CX = CY = 40
RR = 34


def hand(angle, L, w):
    a = math.radians(float(angle))
    return ln(CX, CY, CX + L * math.sin(a), CY - L * math.cos(a), f' stroke-width="{w}"')


def clock_svg(ts):
    h, m, _ = angles(ts)
    b = circ(CX, CY, RR)
    for k in range(12):
        a = math.radians(30 * k)
        r1 = RR - (6 if k % 3 == 0 else 3)
        b += ln(CX + r1 * math.sin(a), CY - r1 * math.cos(a), CX + RR * math.sin(a), CY - RR * math.cos(a))
    b += circ(CX, CY - RR + 10, 1.8, True)  # marker below the 12
    b += hand(h, 17, 3) + hand(m, 27, 1.5) + circ(CX, CY, 2, True)
    return svg(80, 80, b)


def face_q(h, m, diff="medium"):
    img = hm(h, m)             # what the picture looks like
    act = mirror_clock(img)
    assert mirror_clock(act) == img
    fig = clock_svg(img)
    sol = (f"The dot marks 12. Read the picture as it is: the hands show **{fmt(img)}**. That is the mirror "
           f"image, so the actual time = 11:60 − {fmt(img)} = **{fmt(act)}**. Check: {fmt(img)} + {fmt(act)} = 12:00.")
    add("clock-mirror", "cm-p4",
        "The figure shows the **mirror image** of a wall clock (the dot marks 12). What is the actual time?",
        fmt(act), time_opts(act, img), sol, diff=diff, t=40, figure=fig,
        shortcut="Read the picture, then subtract from 11:60.")


face_q(2, 30, "easy")
face_q(10, 15, "medium")
face_q(7, 50, "hard")


def face_options_q(h, m, diff="medium"):
    act = hm(h, m)
    ans_ts = mirror_clock(act)
    # distractors: half turn, the clock itself, and a top-bottom flip (drawn from reflected angles)
    rot = (act + 6 * 3600) % DAY
    hA, mA, _ = angles(act)

    def flip_tb_svg():
        b = circ(CX, CY, RR)
        for k in range(12):
            a = math.radians(30 * k)
            r1 = RR - (6 if k % 3 == 0 else 3)
            b += ln(CX + r1 * math.sin(a), CY - r1 * math.cos(a), CX + RR * math.sin(a), CY - RR * math.cos(a))
        b += circ(CX, CY - RR + 10, 1.8, True)
        b += hand((180 - hA) % 360, 17, 3) + hand((180 - mA) % 360, 27, 1.5) + circ(CX, CY, 2, True)
        return svg(80, 80, b)

    ans = clock_svg(ans_ts)
    opts = {"half turn": clock_svg(rot), "unchanged": clock_svg(act), "top-bottom flip": flip_tb_svg()}
    assert len(set(opts.values()) | {ans}) == 4
    # visually distinct: hand angles differ between every pair
    angs = [angles(ans_ts)[:2], angles(rot)[:2], angles(act)[:2], ((180 - hA) % 360, (180 - mA) % 360)]
    assert len(set(angs)) == 4
    sol = (f"A vertical mirror reflects each hand across the 12–6 line, so the image shows 11:60 − {fmt(act)} = "
           f"**{fmt(ans_ts)}**. Pick the clock whose hands read {fmt(ans_ts)}. The other options show the clock turned "
           f"through 180° ({fmt(rot)}), the clock unchanged ({fmt(act)}), and the hands flipped top to bottom (a water image).")
    add("clock-mirror", "cm-p4",
        f"A wall clock shows **{fmt(act)}**. Which option is its mirror image (the dot marks 12)?",
        ans, list(opts.values()), sol, diff=diff, t=40,
        shortcut="Work out the mirror time first, then find the clock that shows it.")


face_options_q(4, 10, "medium")

upsert(d["practice"], NQ)
finish(T, d)
