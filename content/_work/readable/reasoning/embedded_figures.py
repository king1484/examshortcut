"""Readable rewrite of Reasoning > Embedded Figures (find-hidden, contains-part).

Phase 3: plain English, anchor-stroke method, patterns with steps + why + worked example.
Figures are drawn as small text pictures on a grid of unit strokes (H, V, / and \\).
Every answer is computed by a stroke-set model: a part is "embedded" in a figure when
some translation of it (no rotation, no flip) lies inside the figure's stroke set.
Run: python embedded_figures.py  (patches content/core/topics/reasoning/embedded-figures.json)
"""
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "embedded-figures.json"
BS = chr(92)  # backslash


# ------------------------------------------------------------------ stroke model
def S(spec):
    """'H00 V10 D01 B11' -> set of unit strokes. H right, V up, D '/', B backslash (cell x,y)."""
    out = set()
    for t in spec.split():
        k, x, y = t[0], int(t[1]), int(t[2])
        if k == "H": a, b = (x, y), (x + 1, y)
        elif k == "V": a, b = (x, y), (x, y + 1)
        elif k == "D": a, b = (x, y), (x + 1, y + 1)
        elif k == "B": a, b = (x, y + 1), (x + 1, y)
        else: raise ValueError(t)
        out.add(tuple(sorted((a, b))))
    return frozenset(out)


def mv(s, f):
    return frozenset(tuple(sorted((f(a), f(b)))) for a, b in s)


def shift(s, dx, dy):
    return mv(s, lambda p: (p[0] + dx, p[1] + dy))


mirror = lambda s: mv(s, lambda p: (-p[0], p[1]))
water = lambda s: mv(s, lambda p: (p[0], -p[1]))
rot90 = lambda s: mv(s, lambda p: (-p[1], p[0]))
rot180 = lambda s: mv(s, lambda p: (-p[0], -p[1]))


def bbox(s):
    xs = [p[0] for a, b in s for p in (a, b)]
    ys = [p[1] for a, b in s for p in (a, b)]
    return min(xs), min(ys), max(xs), max(ys)


def norm(s):
    x0, y0, _, _ = bbox(s)
    return shift(s, -x0, -y0)


def where(part, host):
    part = norm(part)
    return [(dx, dy) for dx in range(-8, 9) for dy in range(-8, 9) if shift(part, dx, dy) <= host]


def embedded(part, host):
    return bool(where(part, host))


def kind(st):
    (x1, y1), (x2, y2) = st
    if y1 == y2: return "H"
    if x1 == x2: return "V"
    return "D" if (y2 > y1) == (x2 > x1) else "B"


def render(s):
    s = norm(s)
    _, _, W, Hh = bbox(s)
    g = [[" "] * (4 * W + 1) for _ in range(2 * Hh + 1)]
    for xx in range(W + 1):
        for yy in range(Hh + 1):
            g[2 * (Hh - yy)][4 * xx] = "."
    for a, b in s:
        for p in (a, b):
            g[2 * (Hh - p[1])][4 * p[0]] = "+"
        (x1, y1), (x2, y2) = a, b
        k = kind((a, b))
        if k == "H":
            for c in range(4 * x1 + 1, 4 * x1 + 4): g[2 * (Hh - y1)][c] = "-"
        elif k == "V":
            g[2 * (Hh - y2) + 1][4 * x1] = "|"
        else:
            r, c = 2 * (Hh - max(y1, y2)) + 1, 4 * x1 + 2
            ch = "/" if k == "D" else BS
            g[r][c] = "X" if g[r][c] not in (" ", ch) else ch
    return "\n".join("".join(r).rstrip() for r in g)


def blk(s):
    return "```\n" + render(s) + "\n```"


def connected(s):
    s = list(s)
    seen, fr = {s[0]}, [s[0]]
    while fr:
        a = fr.pop()
        for b in s:
            if b not in seen and set(a) & set(b):
                seen.add(b); fr.append(b)
    return len(seen) == len(s)


ALL32 = S(" ".join(
    [f"H{x}{y}" for x in range(3) for y in range(3)] + [f"V{x}{y}" for x in range(4) for y in range(2)]
    + [f"{k}{x}{y}" for x in range(3) for y in range(2) for k in "DB"]))


def oneoff(part, n=0):
    """Change exactly one stroke of the part; n picks the n-th legal change in a fixed order."""
    pl = sorted(part)
    seen = []
    for rem in pl:
        rest = frozenset(pl) - {rem}
        for c in sorted(ALL32):
            if c in part: continue
            if not any(set(c) & set(k) for k in rest): continue
            new = frozenset(rest | {c})
            if connected(new) and norm(new) != norm(part) and kind(c) != kind(rem) and norm(new) not in seen:
                seen.append(norm(new))
    if n >= len(seen): raise RuntimeError("no such variant")
    return seen[n * max(1, len(seen) // 4)]


def missing_one(part):
    """Drop the last stroke that keeps the part connected."""
    for rem in reversed(sorted(part)):
        rest = frozenset(part) - {rem}
        if connected(rest): return norm(rest)


def big(rng, core, extras, avoid=(), no_kinds="", pos=None):
    """Place core at a random offset in a 3 x 2 box and add filler strokes."""
    core = norm(core)
    _, _, w, h = bbox(core)
    for _ in range(300):
        dx, dy = pos if pos else (rng.randint(0, 3 - w), rng.randint(0, 2 - h))
        c = shift(core, dx, dy)
        pool = sorted(x for x in ALL32 if x not in c and kind(x) not in no_kinds)
        f = frozenset(c | set(rng.sample(pool, extras)))
        if all(not embedded(a, f) for a in avoid):
            return f
    raise RuntimeError


def dist_of(part, name):
    if name.startswith("oneoff"): return oneoff(part, int(name[6:] or 0))
    if name == "missing": return missing_one(part)
    return norm({"mirror": mirror, "water": water, "rot90": rot90, "rot180": rot180}[name](part))


LABEL = {
    "mirror": "is the mirror image (left and right swapped)",
    "water": "is the water image (upside down)",
    "rot90": "is a turned copy",
    "rot180": "is a turned copy",
    "oneoff": "has one stroke changed",
    "oneoff1": "has one stroke changed",
    "oneoff2": "has one stroke changed",
    "missing": "is missing one stroke",
}
CL = {"mirror": "a mirror-image copy", "water": "an upside-down copy", "rot90": "a turned copy", "rot180": "a turned copy",
      "oneoff": "a copy with one stroke changed", "oneoff1": "a copy with one stroke changed", "oneoff2": "a copy with one stroke changed", "missing": "a copy with one stroke missing"}
LET = "ABCD"


def desc(part):
    c = {"H": 0, "V": 0, "D": 0, "B": 0}
    for st in part: c[kind(st)] += 1
    bits = []
    if c["H"]: bits.append(f"{c['H']} flat")
    if c["V"]: bits.append(f"{c['V']} upright")
    if c["D"]: bits.append(f"{c['D']} rising slant (`/`)")
    if c["B"]: bits.append(f"{c['B']} falling slant (`{BS}`)")
    return ", ".join(bits[:-1]) + " and " + bits[-1] if len(bits) > 1 else bits[0]


def rarest(part):
    c = {}
    for st in part: c[kind(st)] = c.get(kind(st), 0) + 1
    order = sorted(c, key=lambda k: (c[k], "DBVH".index(k)))
    return order[0]


KNAME = {"H": "flat stroke", "V": "upright stroke", "D": f"rising slant (`/`)", "B": f"falling slant (`{BS}`)"}


def place_words(part, host, off):
    x0, y0, x1, y1 = bbox(host)
    _, _, pw, ph = bbox(norm(part))
    dx, dy = off
    hw, hh = x1 - x0, y1 - y0
    v = h = None
    if hh > ph:
        v = "bottom" if dy - y0 == 0 else ("top" if dy - y0 == hh - ph else "middle")
    if hw > pw:
        h = "left" if dx - x0 == 0 else ("right" if dx - x0 == hw - pw else "centre")
    if v and h:
        return "the middle" if (v, h) == ("middle", "centre") else f"the {v}-{h} of the figure".replace("middle-", "").replace("-centre", "")
    if h: return f"the {h} side of the figure" if h != "centre" else "the middle of the figure"
    if v: return f"the {v} part of the figure" if v != "middle" else "the middle of the figure"
    return "the place where every stroke lines up"


def order_with_correct(correct, others, k):
    lst = list(others)
    lst.insert(k, correct)
    return lst


# ------------------------------------------------------------------ example builders
def hidden(part_spec, seed, extras, names, k, no_kinds=""):
    """Given figure + options. names = distractor kinds. k = index of correct option."""
    rng = random.Random(seed)
    part = norm(S(part_spec))
    ds = [dist_of(part, n) for n in names]
    for _ in range(2000):
        host = big(rng, part, extras, no_kinds=no_kinds)
        if len(where(part, host)) != 1: continue
        if all(not embedded(d, host) for d in ds): break
    else:
        raise RuntimeError(f"no host for {part_spec} seed {seed}")
    opts = order_with_correct(part, ds, k)
    assert [embedded(o, host) for o in opts].count(True) == 1 and embedded(opts[k], host)
    off = where(part, host)[0]
    q = "Which option is hidden in the given figure? Rotation is not allowed.\n\n**Figure**\n" + blk(host)
    for i, o in enumerate(opts):
        q += f"\n\n**({LET[i]})**\n" + blk(o)
    a = rarest(part)
    n_anchor = sum(1 for st in host if kind(st) == a)
    lines = [f"Part strokes: {desc(part)}.",
             f"Anchor on the {KNAME[a]}. The figure has {n_anchor} of them."]
    wrong = [(LET[i], names[j]) for j, i in enumerate([x for x in range(len(opts)) if x != k])]
    for L, n in wrong[:2]:
        lines.append(f"({L}) {LABEL[n]}, so it does not fit anywhere.")
    lines.append(f"Only ({LET[k]}) fits, in {place_words(part, host, off)}.")
    return dict(q=q, steps=lines, answer=f"({LET[k]})", host=host, opts=opts, part=part)


def contains(part_spec, seed, extras, names, k, pos=None):
    """Given part + big options. names = lookalike kinds used to build the wrong options."""
    rng = random.Random(seed)
    part = norm(S(part_spec))
    good = big(rng, part, extras, pos=pos)
    wrongs = []
    for n in names:
        d = dist_of(part, n)
        wrongs.append(big(rng, d, extras, avoid=(part,)))
    opts = order_with_correct(good, wrongs, k)
    assert [embedded(part, o) for o in opts].count(True) == 1 and embedded(part, opts[k])
    off = where(part, good)[0]
    q = "Which option contains the given part exactly as drawn? Rotation is not allowed.\n\n**Part**\n" + blk(part)
    for i, o in enumerate(opts):
        q += f"\n\n**({LET[i]})**\n" + blk(o)
    a = rarest(part)
    lines = [f"Part strokes: {desc(part)}.", f"Anchor on the {KNAME[a]} and trace the other strokes around it."]
    wrong_idx = [x for x in range(len(opts)) if x != k]
    for j, i in enumerate(wrong_idx[:2]):
        n = names[j]
        lines.append(f"({LET[i]}) only has {CL[n]}, so the part is not there.")
    lines.append(f"({LET[k]}) holds the part in {place_words(part, good, off).replace('of the figure', 'of the option')}.")
    return dict(q=q, steps=lines, answer=f"({LET[k]})", part=part, opts=opts)




# ------------------------------------------------------------------ examples (all verified by the model above)
EX_NOTE = hidden("H00 H10 D20", 2, 4, ["mirror", "oneoff"], 1)
FH1 = hidden("V00 V01 B01", 5, 5, ["mirror", "water", "rot90"], 2)
FH2 = hidden("H00 V10 D10", 3, 2, ["water", "oneoff"], 1)
FH3 = hidden("H00 D10 V20 H01", 4, 3, ["oneoff", "oneoff1"], 2)
FH4 = hidden("D00 B10 V00", 4, 3, ["water", "oneoff"], 0)
FH5 = hidden("H00 D10 V10", 6, 5, ["mirror", "rot90"], 1, no_kinds="B")
assert not any(kind(st) == "B" for st in FH5["host"])
assert any(kind(st) == "B" for i, o in enumerate(FH5["opts"]) if i != 1 for st in o)

CN_NOTE = contains("H00 H10 V00 D10", 2, 3, ["mirror", "oneoff"], 1, pos=(0, 0))
CP1 = contains("H00 V00 D00 V10", 1, 3, ["mirror", "water", "oneoff"], 2)
CP2 = contains("H00 D10 V10 V00", 5, 2, ["oneoff", "oneoff1", "missing"], 1)
CP3 = contains("H00 H10 V00 D10", 2, 3, ["mirror", "oneoff"], 1, pos=(0, 0))
CP4 = contains("D00 B10 H01", 3, 3, ["mirror", "oneoff"], 0)
CP5 = contains("H00 V00 D00 B01", 4, 3, ["oneoff"], 1)
CP6 = contains("H00 V10 D10", 3, 1, ["missing", "oneoff"], 2)
CP7 = contains("H00 V00 V10 H01", 1, 2, ["missing", "oneoff"], 0, pos=(0, 0))

# ---- quick sanity checks on the ideas quoted in the text
_p = norm(S("H00 D10 V20 H01"))
assert not embedded(mirror(_p), FH3["host"]) and embedded(_p, FH3["host"])
_only_rising = S("H00 H10 V00 D00 D10 V20")
assert not embedded(S("B00"), _only_rising)          # trick: a falling slant is impossible
assert not embedded(S("H00 H10 H20 V00"), S("H00 H10 V00 V10 H01"))   # trick: needs 3 flat strokes in a row
assert len(S("H00 H10 D20 V30 H01")) == 5 and len(S("H00 H10 D20 V30")) == 4   # trick: stroke count


def steps_md(ex):
    return "\n".join(f"- {x}" for x in ex["steps"])


FH_CONCEPT = (
    "A big figure hides one of the small option figures. The hidden figure has the same strokes, "
    "the same lengths and the same directions. Your job is to find which option it is.\n\n"
    "You may slide the small figure around. You may **not** turn it or flip it."
)

FH_NOTES = f"""### What hidden means
One small figure sits inside the big figure. Extra lines are drawn around it to hide it.

The four options are small figures. Pick the option that appears **exactly** inside the big one.

> **Rule:** Sliding is allowed. Turning and flipping are not allowed.

### How the pictures look here
The exam shows drawings. We draw them with text.

- `+` is a corner point. `.` is an empty point.
- `-` is a flat stroke. `|` is an upright stroke.
- `/` is a rising slant. `{BS}` is a falling slant. `X` means both slants cross in that square.

Every stroke is one square long. So the size of a stroke never decides the answer.

### Flips and turns are wrong answers
Most wrong options are copies of the right answer with one simple change.

| Copy | What changes | Allowed? |
|---|---|---|
| Mirror image | Left and right swap | No |
| Water image | Top and bottom swap | No |
| Turned copy | Turned by 90 or 180 degrees | No |

A `/` slant becomes a `{BS}` slant in a mirror image. So check the slants first.

### Pick a rare stroke first
Do not compare whole figures. Pick **one stroke** that is rare in the small figure. A slant is the best choice.

1. Find that stroke in the big figure. Match its direction.
2. Check the strokes that touch it. Are they there too?
3. Trace the other strokes one by one.
4. If one stroke is missing, drop that place and try the next one.

> **Tip:** A flat or upright stroke appears many times. A slant appears only a few times. Fewer places means less work.

### Count strokes by type
Count the part's strokes: flat, upright, rising slant and falling slant. The big figure must have **at least** that many of each type.

If the part has a `{BS}` slant and the big figure has none, that option is out. You do not need to trace anything.

> **Watch:** Two options can have the same number of strokes and still differ in direction.

### A worked example
{EX_NOTE["q"]}

**Solution**
{steps_md(EX_NOTE)}

Answer: **{EX_NOTE["answer"]}**.
"""

FH_MISTAKES = [
    {"wrong": "Choosing an option because the overall shape looks right.", "right": "Check every stroke and its direction. Shape alone hides flips and turns."},
    {"wrong": "Accepting a turned or mirrored copy.", "right": "Rotation is not allowed. A `/` slant in the figure never matches a `\\` slant in the option."},
    {"wrong": "Accepting an option that misses one stroke, or has one stroke in another direction.", "right": "Every stroke of the option must be present. One missing or re-angled stroke means reject."},
    {"wrong": "Checking only the first place where the anchor stroke appears.", "right": "Try every place where the anchor appears before you reject an option."},
    {"wrong": "Comparing stroke sizes.", "right": "All strokes are one square long here. Size never decides. Direction does."},
]
FH_REVISION = [
    "Hidden = same strokes, same lengths, same directions, anywhere in the figure.",
    "Rotation is not allowed. Mirror and water images are wrong answers.",
    "Anchor on the rarest stroke, usually a slant. Then trace the other strokes around it.",
    "Count strokes by type first. A type missing from the figure kills the option at once.",
    "Reject flipped and turned options by direction. Trace only the ones that are left.",
    "One missing or re-angled stroke means the option is not hidden there.",
]

FH_TRICKS = [
    {
        "title": "Reject by a missing direction",
        "body": "Look at which slants the big figure has. An option with a slant the figure lacks cannot be hidden in it.",
        "example": {
            "q": "The big figure has only rising slants (`/`). An option has one falling slant (`\\`). Can that option be hidden in it?",
            "steps": ["The figure has no `\\` stroke anywhere.", "Sliding cannot change a `\\` into a `/`.", "So the option cannot fit."],
            "answer": "No. Reject it at once.",
        },
    },
    {
        "title": "Count strokes by type",
        "body": "Count the flat, upright and slanting strokes in the part. The big figure must have at least as many of each type.",
        "example": {
            "q": "An option has 3 flat strokes in a row. The big figure has only 2 flat strokes in each row. Can it be hidden?",
            "steps": ["A row of 3 flat strokes needs 3 flat strokes in one line.", "No line in the figure has 3.", "So the option cannot fit."],
            "answer": "No.",
        },
    },
    {
        "title": "Two finalists: compare at the anchor",
        "body": "If two options look alike, compare only the strokes that touch the anchor. The wrong one usually breaks there.",
    },
]
assert not embedded(S("H00 H10 H20 V00"), S("H00 H10 V00 V10 H01"))

FH_PATTERNS = [
    dict(id="fh-p1", name="Hidden part in a full grid figure", frequency="very common",
         howToSpot="A busy grid of short strokes is given. The four options are small open figures. Most options are flipped copies of one figure.",
         formula=None,
         steps=["Count the part's strokes by type.", "Pick the rarest stroke as the anchor. Find it in the figure.", "Trace the other strokes around each anchor place.", "Reject mirror, water and turned copies by direction."],
         why="A slant has only two directions, so a flipped copy fails at the first stroke.",
         ex=FH1),
    dict(id="fh-p2", name="Hidden part in an irregular figure", frequency="common",
         howToSpot="The big figure is not a full grid. Some strokes are missing or stop early, so matching the whole shape does not help.",
         formula=None,
         steps=["Ignore the outline of the figure.", "Start at the anchor stroke of each option.", "Trace stroke by stroke. Do not expect a full grid.", "Keep the option that completes."],
         why="A hidden part only needs its own strokes to be present. The figure's outline does not matter.",
         ex=FH2),
    dict(id="fh-p3", name="Options that differ by one stroke", frequency="common",
         howToSpot="The options are not flips of each other. Each one differs from the part by one stroke that is changed.",
         formula=None,
         steps=["Compare each option with the part, stroke by stroke.", "Mark the changed stroke in each wrong option.", "Confirm that the option left really appears in the figure."],
         why="A wrong option that has one stroke changed cannot be found in the figure, however close it looks.",
         ex=FH3),
    dict(id="fh-p4", name="Parts with two or more slants", frequency="occasional",
         howToSpot="The part has two or more slanting strokes. Direction mistakes are easy to make.",
         formula=None,
         steps=["Write the lean of each slant: `/` rises to the right, `\\` falls to the right.", "Match both slants in the figure.", "Then check the flat and upright strokes that touch them."],
         why="Flipped copies reverse at least one slant, so they fail as soon as you match the leans.",
         ex=FH4),
    dict(id="fh-p5", name="A direction the figure does not have", frequency="common",
         howToSpot="Look at the big figure. It has no falling slant (or no rising slant). At least one option needs that slant.",
         formula=None,
         steps=["List the stroke types in the big figure.", "Cross out every option that needs a type the figure lacks.", "Trace only the options that are left."],
         why="Sliding cannot change the direction of a stroke, so a missing direction ends the check at once.",
         ex=dict(FH5, steps=[f"Part strokes: {desc(FH5['part'])}.", f"The figure has no falling slant (`{BS}`).",
                             f"Options with a `{BS}` slant are out: ({LET[0]}), ({LET[2]}).",
                             f"Only ({LET[1]}) is left, and it fits in {place_words(FH5['part'], FH5['host'], where(FH5['part'], FH5['host'])[0])}."])),
]

CP_CONCEPT = (
    "This is the reverse question. One small part is given, and each option is a bigger figure. "
    "Choose the option that contains the part **exactly as drawn**.\n\n"
    "Extra lines never matter. You may slide the part but not turn it or flip it."
)

CP_NOTES = f"""### The task
A small **part** is given. Each option is a bigger figure. Exactly one option contains the part. It has the same strokes, lengths and directions.

The option may have extra strokes around the part. That is fine.

> **Rule:** The part must be present in full. Extra lines never disqualify an option.

### Read the pictures
- `+` is a corner point. `.` is an empty point.
- `-` is a flat stroke. `|` is an upright stroke.
- `/` is a rising slant. `{BS}` is a falling slant. `X` means both slants cross in that square.

Every stroke is one square long.

### List the part's strokes
Write down the strokes with their directions. For example: 2 flat, 1 upright, 1 rising slant.

The right option shows all of them, joined in the same way. Sliding is allowed. Turning is not.

### Use a rare stroke as anchor
A slant is rarer than a flat or upright stroke. Start with it.

1. Check its lean: `/` rises to the right, `{BS}` falls to the right.
2. Find it in the option.
3. Check the strokes that touch it, one by one.
4. Also try a **T-joint**: one stroke that ends on the middle of another. It is the next best anchor.

> **Tip:** Parts often sit against an edge or in a corner of the correct option. Scan the border first.

### Near-miss options
Wrong options are usually one step away from the part. One stroke is **missing**, **changed** or **turned**.

Counting strokes is not enough. A wrong option can have the same number of strokes as the part.

> **Watch:** Check each stroke's direction and its end points. They must match the part.

### A good scan order
Do the same steps for every option. This keeps you fast and calm.

1. Count the strokes. Drop any option with fewer strokes than the part.
2. Check the directions. Drop any option that lacks a direction the part needs.
3. Trace the anchor stroke and its neighbours in each option that is left.
4. Choose the option where every stroke lines up.

Most questions end after step 2 or 3. You rarely need to trace all four options in full.

### A worked example
{CN_NOTE["q"]}

**Solution**
{steps_md(CN_NOTE)}

Answer: **{CN_NOTE["answer"]}**.
"""

CP_MISTAKES = [
    {"wrong": "Rejecting the right option because it has extra lines.", "right": "Extra strokes are allowed. Only the part's own strokes must be present."},
    {"wrong": "Accepting an option where the part fits only after turning it.", "right": "Rotation is not allowed. A turned copy is a wrong option."},
    {"wrong": "Comparing only the number of strokes.", "right": "A one-stroke change keeps the count but breaks the shape. Check each direction."},
    {"wrong": "Checking a slant's length but not its lean.", "right": "A `/` and a `\\` are different strokes. The lean decides."},
    {"wrong": "Stopping at the first partial match.", "right": "Trace every stroke of the part. One missing stroke means the option is out."},
]
CP_REVISION = [
    "The part must appear in full: same strokes, same directions, only slid.",
    "Extra filling lines never disqualify an option.",
    "Anchor on a slant or a T-joint. Scan edges and corners first.",
    "Wrong options are one stroke away: missing, changed or turned.",
    "A `/` and a `\\` are different strokes. Direction decides.",
    "An option with fewer strokes than the part cannot contain it.",
]
CP_TRICKS = [
    {
        "title": "Reject by a missing direction",
        "body": "List the directions in the part: flat, upright, `/` and `\\`. An option that lacks one of them is out at once.",
        "example": {
            "q": "The part has a flat stroke, an upright stroke and a falling slant (`\\`). Option B has no falling slant at all. Keep B?",
            "steps": ["The part needs a `\\` stroke.", "Option B has none.", "Sliding cannot create one."],
            "answer": "No. Reject B without tracing.",
        },
    },
    {
        "title": "Count the strokes first",
        "body": "The option must have at least as many strokes as the part. Fewer strokes means it cannot contain the part.",
        "example": {
            "q": "The part has 5 strokes. Option C has 4 strokes in total. Can C contain the part?",
            "steps": ["A figure with 4 strokes cannot hold 5 strokes.", "So C cannot contain the part."],
            "answer": "No.",
        },
    },
    {
        "title": "Two finalists: compare at the anchor",
        "body": "If two options survive, compare only the strokes that touch the anchor. The wrong one usually breaks a stroke there.",
    },
]

CP_PATTERNS = [
    dict(id="cp-p1", name="Part among busy figures", frequency="very common",
         howToSpot="Four options of similar size, each full of short strokes. The part is small.",
         formula=None,
         steps=["List the part's strokes by type.", "Find the anchor stroke in each option.", "Trace the other strokes around it.", "Keep the option that completes."],
         why="Only one option has every stroke of the part in the right place.",
         ex=CP1),
    dict(id="cp-p2", name="Options one stroke away from the part", frequency="very common",
         howToSpot="Every option has about as many strokes as the part, but one stroke differs: missing, changed or turned.",
         formula=None,
         steps=["Do not stop at the stroke count.", "Check the direction of each stroke.", "Check that the end points meet as in the part.", "Reject any option with one wrong stroke."],
         why="A near-miss figure looks right at a glance but always breaks on one stroke.",
         ex=CP2),
    dict(id="cp-p3", name="Part along an edge or corner", frequency="common",
         howToSpot="The part has a flat side, like two flat strokes in a row. The options place it against a border.",
         formula=None,
         steps=["Scan the border of each option first.", "Look in the corners for the flat side.", "Then check the slant and upright strokes."],
         why="A part with a flat base usually sits on an edge, not in the middle.",
         ex=CP3),
    dict(id="cp-p4", name="Slants as anchors", frequency="common",
         howToSpot="The part has two or more slants. The options differ in how their slants lean.",
         formula=None,
         steps=["Write the lean of every slant in the part.", "Find slants with the same leans in each option.", "Check the flat and upright strokes that join them."],
         why="Mirror and water copies reverse a slant, so matching the leans removes them.",
         ex=CP4),
    dict(id="cp-p5", name="Two finalists", frequency="common",
         howToSpot="After the first pass, two options are left. Their filler lines make them look equal.",
         formula=None,
         steps=["Go back to the anchor stroke in both options.", "Compare only the strokes that touch it.", "Drop the option with a wrong or missing stroke there."],
         why="The wrong finalist breaks one stroke next to the anchor.",
         ex=CP5),
    dict(id="cp-p6", name="Sparse options", frequency="occasional",
         howToSpot="The options have very few extra lines, so the part stands out.",
         formula=None,
         steps=["Still trace stroke by stroke.", "Look for the one stroke each wrong option is missing.", "Pick the option with no gaps."],
         why="Sparse options often lack exactly the stroke you assume is there.",
         ex=CP6),
    dict(id="cp-p7", name="Part with a closed shape", frequency="occasional",
         howToSpot="The part contains a closed shape, like a box or a triangle. Some options leave it open.",
         formula=None,
         steps=["Note that the shape is closed.", "In each option, find all its sides.", "Reject options where one side is missing or points another way."],
         why="One missing side turns a closed shape into an open one, which is a different figure.",
         ex=CP7),
]


def pat(d):
    ex = d["ex"]
    return {"id": d["id"], "name": d["name"], "frequency": d["frequency"], "howToSpot": d["howToSpot"],
            "formula": d["formula"], "steps": d["steps"], "why": d["why"],
            "example": {"q": ex["q"], "steps": ex["steps"], "answer": ex["answer"]}}


def apply(data, sid, concept, notes, patterns, mistakes, revision, tricks):
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, "never drop a pattern id"
    other = {p["id"] for s in data["subtopics"] if s["id"] != sid for p in s.get("patterns", [])}
    assert not (other & {p["id"] for p in patterns}), "pattern id clash"
    assert 2500 <= len(notes) <= 5000, (sid, len(notes))
    sub.update(concept=concept, notes=notes.strip() + "\n", patterns=patterns, mistakes=mistakes, revision=revision, tricks=tricks)
    print(sid, "updated:", len(notes), "chars,", len(patterns), "patterns")


data = json.loads(TOPIC.read_text(encoding="utf-8"))
apply(data, "find-hidden", FH_CONCEPT, FH_NOTES, [pat(d) for d in FH_PATTERNS], FH_MISTAKES, FH_REVISION, FH_TRICKS)
apply(data, "contains-part", CP_CONCEPT, CP_NOTES, [pat(d) for d in CP_PATTERNS], CP_MISTAKES, CP_REVISION, CP_TRICKS)
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")

