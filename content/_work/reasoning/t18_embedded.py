# build embedded-figures topic (topic 18); every answer is checked with engines.embeds (translation only)
import random
import common as C
from engines import prims, embeds, grid_svg, normalize, PL

QE = ("In which option is the figure given in the question **embedded** as a part (rotation is not allowed)?")
QF = ("Which of the option figures is embedded in (hidden inside) the given figure? Rotation is not allowed.")


def N(segs):
    """normalised primitive set"""
    P = prims(segs)
    xs = [p[0] for s in P for p in s]
    ys = [p[1] for s in P for p in s]
    mx, my = min(xs), min(ys)
    return frozenset(tuple(sorted([(a[0] - mx, a[1] - my), (b[0] - mx, b[1] - my)])) for a, b in P)


def tf(P, f):
    return N([(f(a), f(b)) for a, b in P])


FL = {
    'mirror (left-right flip)': lambda p: (-p[0], p[1]),
    'water image (top-bottom flip)': lambda p: (p[0], -p[1]),
    'copy turned through 90 degrees': lambda p: (-p[1], p[0]),
    'copy turned through 180 degrees': lambda p: (-p[0], -p[1]),
    'copy turned through 270 degrees': lambda p: (p[1], -p[0]),
}


def pic(P, box=None):
    segs = sorted(P)
    return grid_svg(segs, scale=12, pad=5, size=box)


def found(main, part):
    return embeds(sorted(prims(main)), sorted(part))


def where(main, part, hit):
    xs = [p[0] for s in prims(main) for p in s]
    ys = [p[1] for s in prims(main) for p in s]
    W, H = max(xs), max(ys)
    pw = max(p[0] for s in part for p in s)
    ph = max(p[1] for s in part for p in s)
    cx, cy = hit[0] + pw / 2, hit[1] + ph / 2
    hx = 'left' if cx < W / 2 - 0.25 else ('right' if cx > W / 2 + 0.25 else 'centre')
    vy = 'upper' if cy < H / 2 - 0.25 else ('lower' if cy > H / 2 + 0.25 else 'middle')
    return ('%s-%s part' % (vy, hx)).replace('middle-centre', 'centre')


def connected_part(main, k, rng):
    M = sorted(prims(main))
    for _ in range(500):
        cur = {rng.choice(M)}
        while len(cur) < k:
            pts = {p for s in cur for p in s}
            nb = [s for s in M if s not in cur and (s[0] in pts or s[1] in pts)]
            if not nb:
                break
            cur.add(rng.choice(nb))
        if len(cur) != k:
            continue
        P = N(list(cur))
        dirs = {(b[0] - a[0], b[1] - a[1]) for a, b in P}
        if len(dirs) < 3:
            continue
        yield P


def find_q(id, main, k, seed, d, pat, t=50, extra_sol=''):
    """options = parts; exactly one embedded."""
    rng = random.Random(seed)
    for P in connected_part(main, k, rng):
        wrong = []
        why = []
        for name, f in FL.items():
            V = tf(P, f)
            if V == P or V in wrong or found(main, V):
                continue
            wrong.append(V)
            why.append(name)
        if len(wrong) < 3:
            continue
        hits = found(main, P)
        if len(hits) != 1:
            continue
        wrong, why = wrong[:3], why[:3]
        box = (max(max(p[0] for s in X for p in s) for X in [P] + wrong),
               max(max(p[1] for s in X for p in s) for X in [P] + wrong))
        opts = [pic(P, box)] + [pic(X, box) for X in wrong]
        assert len(set(opts)) == 4
        for X in wrong:
            assert not found(main, X)
        sol = ("The correct figure sits in the **%s** of the given figure, with every line matching in direction and length. "
               "The other three options are the same shape %s — none of them can be traced in the figure without "
               "turning it, and rotation is not allowed.%s"
               % (where(main, P, hits[0]), 'shown as a ' + ', a '.join(why[:2]) + ' and a ' + why[2] if len(why) == 3 else '', extra_sol))
        sol = sol.replace('shape shown as a mirror', 'shape shown as its mirror')
        return C.Q(id, QF, opts, opts[0], sol,
                   sc="Fix the most distinctive stroke (a lone diagonal or an odd-length line), locate it in the main figure, then check the rest.",
                   d=d, sub='find-hidden', pat=pat, t=t, fig=pic(prims(main)))
    raise AssertionError('no part found for ' + id)


def contain_q(id, part_segs, options, sol, d, pat, t=50):
    part = N(part_segs)
    ok = [i for i, o in enumerate(options) if found(o, part)]
    assert ok == [0], (id, ok)
    box = (max(max(p[0] for s in prims(o) for p in s) for o in options),
           max(max(p[1] for s in prims(o) for p in s) for o in options))
    opts = [pic(prims(o), box) for o in options]
    assert len(set(opts)) == 4
    return C.Q(id, QE, opts, opts[0], sol,
               sc="Look for the part's most unusual stroke first; reject options where it is missing or runs the wrong way.",
               d=d, sub='contains-part', pat=pat, t=t, fig=pic(part))


# ---------------------------------------------------------------- main figures (integer grid, H/V/45-degree lines)
def box(x0, y0, x1, y1):
    return PL((x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0))


M = {}
M['a'] = box(0, 0, 4, 4) + [((0, 0), (4, 4)), ((2, 0), (2, 4)), ((0, 2), (2, 0))]
M['b'] = box(0, 0, 4, 4) + [((0, 2), (4, 2)), ((0, 4), (4, 0)), ((2, 2), (2, 4)), ((2, 0), (4, 2))]
M['c'] = box(0, 0, 4, 4) + PL((2, 0), (4, 2), (2, 4), (0, 2), (2, 0)) + [((2, 0), (2, 2)), ((0, 4), (2, 2))]
M['d'] = box(0, 0, 4, 3) + [((1, 0), (1, 3)), ((1, 1), (4, 1)), ((1, 3), (3, 1)), ((3, 1), (4, 0)), ((0, 3), (1, 2))]
M['e'] = PL((0, 2), (2, 0), (4, 2)) + box(0, 2, 4, 4) + [((2, 0), (2, 4)), ((0, 4), (2, 2)), ((2, 3), (4, 3))]
M['f'] = box(0, 0, 3, 3) + [((1, 0), (1, 3)), ((0, 1), (3, 1)), ((1, 1), (3, 3)), ((0, 3), (1, 2)), ((2, 1), (3, 0))]
M['g'] = box(0, 0, 4, 4) + [((0, 0), (2, 2)), ((2, 2), (0, 4)), ((2, 2), (4, 2)), ((3, 0), (3, 2)), ((2, 4), (4, 2))]
M['h'] = box(0, 0, 4, 4) + box(1, 1, 3, 3) + [((0, 0), (1, 1)), ((4, 0), (3, 1)), ((2, 1), (2, 3)), ((3, 3), (4, 4))]
M['i'] = PL((0, 3), (3, 0), (3, 3), (0, 3)) + [((1, 2), (3, 2)), ((2, 1), (2, 3)), ((0, 3), (1, 4)), ((1, 4), (3, 4)), ((3, 3), (3, 4))]
M['j'] = box(0, 0, 4, 2) + [((0, 0), (2, 2)), ((2, 0), (4, 2)), ((2, 0), (2, 2)), ((3, 0), (3, 1)), ((0, 2), (1, 1))]

subs = [
    C.sub('find-hidden', 'Finding the hidden part in a figure',
          "A complex figure is given and you must find which option figure is **hidden inside it exactly as drawn** — same size, same angles, same orientation. The standard SSC instruction is *rotation is not allowed*.\n\n"
          "Method:\n1. In each option, pick its most unusual stroke — a lone slanting line, an odd-length side, a T-junction.\n"
          "2. Search the main figure for that stroke in the **same direction**.\n3. Trace the rest of the option from there; every line must be present in the main figure (it may be part of a longer line).\n\n"
          "Distractors are usually the correct part flipped, rotated or with one line changed. That is why orientation matters more than the general shape.",
          tricks=[C.T('Anchor on the slant',
                      "A slanting line has only two possible directions (/ or \\). Check whether the main figure even has the option's slant in the right place; this rejects mirror-image distractors in seconds.",
                      "**Q.** The main figure has only \\ diagonals. An option contains a / slant. Can it be embedded?",
                      "No — without a / line anywhere in the main figure that option is impossible.")],
          mistakes=["Accepting a part that fits only after rotating or flipping it.",
                    "Ignoring length: a line in the option that is longer than any matching line in the figure cannot fit.",
                    "Forgetting that a short option line may be a piece of a longer line in the figure."]),
    C.sub('contains-part', 'Which figure contains the given part',
          "The reverse form: one small figure is given and each option is a bigger figure. Choose the option in which the small figure appears **as it is**.\n\n"
          "Scan each option for the part's key stroke, then confirm the rest. Options that nearly contain it usually lack one line or have it running the other way.",
          tricks=[C.T('Eliminate by the missing line',
                      "Count the part's line directions (horizontal, vertical, /, \\). Any option missing one of these directions is out immediately.",
                      "**Q.** The part has a horizontal, a vertical and a \\ line. Option B has no \\ line at all. Keep B?",
                      "No — reject it without tracing.")],
          mistakes=["Choosing an option where the part fits only after rotation.",
                    "Stopping at the first partial match without checking every line."]),
]

patterns = [
    C.P('Hidden part in square grid figure', 'very common',
        "Square with diagonals/midlines; options are small line clusters.",
        "Anchor on the slant direction, then trace; reject flips and rotations."),
    C.P('Hidden part in irregular figure', 'common',
        "House, arrow or triangle-based figure.",
        "Match lengths as well as directions."),
    C.P('Which option contains the part', 'common',
        "One small figure in the question, bigger figures in the options.",
        "Eliminate options lacking one of the part's line directions."),
    C.P('Near-miss distractors', 'occasional',
        "Options are rotations/flips of the same shape.",
        "Only the orientation that matches the figure is correct."),
]

examples = [
    find_q('rsn-embedded-ex1', M['a'], 4, 11, 'easy', 'hidden part in square grid figure', 40),
    find_q('rsn-embedded-ex2', M['e'], 4, 12, 'medium', 'hidden part in irregular figure', 45),
    find_q('rsn-embedded-ex3', M['h'], 5, 13, 'medium', 'near-miss distractors', 50),
]
part = PL((0, 0), (1, 1), (2, 1)) + [((1, 0), (1, 1))]
examples.append(contain_q('rsn-embedded-ex4', part, [
    box(0, 0, 3, 2) + [((0, 0), (2, 2)), ((2, 0), (2, 2)), ((1, 1), (3, 1))],
    box(0, 0, 3, 2) + [((0, 2), (2, 0)), ((2, 0), (2, 2)), ((1, 1), (3, 1))],
    box(0, 0, 3, 2) + [((0, 0), (1, 1)), ((1, 1), (3, 1))],
    box(0, 0, 3, 2) + [((1, 0), (2, 1)), ((0, 1), (1, 1)), ((2, 0), (2, 2))],
],
    "The part is a \\ slant whose lower end meets a vertical line coming down and a horizontal line going off to the right. In the first figure this happens at the bottom: the lower half of the long diagonal ends where the vertical line meets the bottom edge, and the bottom edge supplies the horizontal line. The second figure has only a / slant; the third has no vertical line at the lower end of its slant; in the fourth the horizontal line at the slant's lower end runs to the left, not the right.",
    'easy', 'which option contains the part', 45))

pr = []
specs = [('a', 5, 21, 'medium'), ('b', 4, 22, 'easy'), ('b', 5, 23, 'medium'), ('c', 4, 24, 'medium'),
         ('c', 5, 25, 'hard'), ('d', 4, 26, 'medium'), ('d', 5, 27, 'hard'), ('e', 5, 28, 'hard'),
         ('f', 4, 29, 'medium'), ('g', 4, 30, 'medium'), ('g', 5, 31, 'hard'), ('i', 4, 32, 'medium'),
         ('j', 4, 33, 'easy')]
pats = {'a': 'hidden part in square grid figure', 'b': 'hidden part in square grid figure', 'c': 'near-miss distractors',
        'd': 'hidden part in irregular figure', 'e': 'hidden part in irregular figure', 'f': 'hidden part in square grid figure',
        'g': 'near-miss distractors', 'i': 'hidden part in irregular figure', 'j': 'hidden part in irregular figure'}
for n, (m, k, seed, d) in enumerate(specs, start=1):
    pr.append(find_q('rsn-embedded-%d' % n, M[m], k, seed, d, pats[m], {'easy': 40, 'medium': 50, 'hard': 60}[d]))

part2 = PL((0, 1), (1, 0), (2, 0)) + [((1, 0), (1, 2))]
pr.append(contain_q('rsn-embedded-14', part2, [
    box(0, 0, 3, 3) + [((0, 1), (1, 0)), ((1, 0), (1, 3)), ((1, 2), (3, 2))],
    box(0, 0, 3, 3) + [((0, 0), (1, 1)), ((1, 0), (1, 3)), ((1, 2), (3, 2))],
    box(0, 0, 3, 3) + [((0, 1), (1, 0)), ((2, 0), (2, 3)), ((0, 2), (2, 2))],
    box(0, 0, 3, 3) + [((0, 2), (1, 3)), ((1, 0), (1, 3)), ((0, 1), (3, 1))],
],
    "The part is a / slant rising to a point, a horizontal line going right from that point and a vertical line going down from it. Only the first figure has the / slant cutting the top-left corner exactly where the vertical line meets the top edge; the top edge supplies the horizontal line. The second has the slant the other way; in the third no vertical line goes down from the upper end of the slant; in the fourth the slant is at the bottom.",
    'medium', 'which option contains the part', 50))

assert len(pr) == 14
t = C.topic('embedded-figures', 'Embedded Figures', 'low', {'tier1': '0-1', 'tier2': '0-1'},
            "Find a small figure hidden inside a bigger one exactly as drawn — same size and orientation (rotation is not allowed). Anchor on the most distinctive stroke, usually a slant, and reject options that are flips or rotations of the true part.",
            subs, patterns, examples, pr)
C.write_topic(t)
print('OK embedded-figures')
