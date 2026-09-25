"""Build reasoning/embedded-figures: notes, patterns and practice questions.

Every figure is a set of unit edges on a square lattice (embedded_engine). A part is
"embedded" in a figure only if its edge set appears there under translation alone -
rotation is NOT allowed. Each answer is accepted only after embeds() proves it is
present, and every wrong option is proven absent by the same test, so no answer
rests on eyeball judgement.
"""
import random
from hashlib import md5

from _lib import load, set_sub, upsert, Q, finish
import embedded_engine as E
from embedded_notes import NOTES, PATTERNS, PYQS

d = load("embedded-figures")

# ================================================================ engine self-checks
_r = random.Random(7)
_p = E.random_part(_r, 5, 2, 2)
assert E.norm(E.transform(E.transform(_p, "mirrorV"), "mirrorV")) == E.norm(_p)
assert E.norm(E.transform(E.transform(E.transform(E.transform(_p, "rot90"), "rot90"),
                                      "rot90"), "rot90")) == E.norm(_p)
assert E.norm(E.transform(E.transform(_p, "mirrorV"), "mirrorH")) == E.norm(E.transform(_p, "rot180"))
assert len(E.lattice_edges(4, 4)) == 72
assert len(E.lattice_edges(3, 3)) == 42
assert len(E.lattice_edges(4, 3)) == 55

_q = E.norm(E.random_part(_r, 4, 2, 2))
assert E.embeds(_q, E.translate(_q, 1, 1) | _q) == (True, (0, 0))
assert E.embeds(_q, E.translate(_q, 2, 1))[0]
assert E.embeds(_q, frozenset()) == (False, None)
_mv = E.transform(_q, "mirrorV")
if E.norm(_mv) != E.norm(_q):
    assert not E.embeds(_mv, _q)[0]

# notes worked example (find-hidden): an L with a foot
_L = frozenset([frozenset(((0, 0), (1, 0))), frozenset(((0, 0), (0, 1))),
                frozenset(((0, 1), (0, 2)))])
assert E.stroke_desc(_L) == "1 horizontal stroke and 2 vertical strokes"
_Lflip = E.transform(_L, "mirrorV")
_bigL = E.translate(_L, 1, 1) | {frozenset(((3, 0), (4, 0))), frozenset(((4, 1), (4, 2))),
                                 frozenset(((2, 2), (3, 3))), frozenset(((0, 3), (1, 3)))}
assert E.embeds(_L, _bigL) == (True, (1, 1))
assert not E.embeds(_Lflip, _bigL)[0]

# notes worked example (contains-part): H + V + / slant
_P2 = frozenset([frozenset(((0, 0), (1, 0))), frozenset(((0, 0), (0, 1))),
                 frozenset(((1, 0), (0, 1)))])
assert E.stroke_desc(_P2) == "1 horizontal stroke, 1 vertical stroke and 1 slanting stroke"
_optA = E.translate(_P2, 1, 1) | {frozenset(((2, 0), (3, 0))), frozenset(((2, 1), (2, 2)))}
assert E.embeds(_P2, _optA) == (True, (1, 1))
_optB = frozenset([frozenset(((0, 0), (1, 0))), frozenset(((0, 0), (0, 1))),
                   frozenset(((0, 0), (1, 1)))])
assert not E.embeds(_P2, E.translate(_optB, 1, 1) | {frozenset(((2, 0), (3, 0))),
                                                     frozenset(((2, 1), (2, 2)))})[0]
_optC = frozenset([frozenset(((0, 0), (1, 0))), frozenset(((1, 0), (0, 1))),
                   frozenset(((1, 1), (2, 1)))])
assert not E.embeds(_P2, _optC)[0]

assert E.region_name(0, 0, 2, 2, 4, 4) == "upper-left"
assert E.region_name(2, 2, 2, 2, 4, 4) == "lower-right"
assert E.region_name(1, 1, 2, 2, 4, 4) == "the middle"
assert E.region_name(0, 1, 2, 2, 3, 3) == "lower-left"
_s = E.fig_svg(frozenset([frozenset(((0, 0), (1, 0)))]), 2)
assert 'x1="5" y1="5" x2="17" y2="5"' in _s and 'viewBox="0 0 34 34"' in _s
assert 'viewBox="0 0 46 46"' in E.fig_svg(_L, 3)

# ================================================================ builders
KINDS = ("mirrorV", "mirrorH", "rot90", "rot180")
KIND_TEXT = {
    "mirrorV": "flipped left-right (its mirror image)",
    "mirrorH": "flipped top-bottom (its water image)",
    "rot90": "turned through a right angle",
    "rot180": "turned through 180 degrees",
}


def seeded(name):
    return random.Random(int(md5(name.encode()).hexdigest(), 16))


def ndiag(fig):
    return sum(1 for e in fig for (x, y), (z, w) in [sorted(e)] if x != z and y != w)


def transforms_of(part, rng, k=3):
    cand = [kk for kk in KINDS if E.norm(E.transform(part, kk)) != E.norm(part)]
    rng.shuffle(cand)
    out = []
    for kk in cand:
        if all(E.norm(E.transform(part, kk)) != E.norm(E.transform(part, k2)) for k2 in out):
            out.append(kk)
        if len(out) == k:
            break
    return out


def region_phrase(region):
    return "in the **middle** of the given figure" if region == "the middle" \
        else f"in the **{region} part** of the given figure"


def fh(name, pat, diff, cells, mode="transform", min_diag=0, t=60):
    """Hidden-part question: the part appears in the big figure; each wrong option is
    proven NOT to appear there."""
    cx, cy = cells
    rng = seeded(name)
    pool = sorted(E.lattice_edges(cx, cy))
    nfill = rng.randrange(14, 19) if cx == 4 and cy == 4 else rng.randrange(11, 15)
    for _outer in range(600):
        part = E.norm(E.random_part(rng, rng.choice((4, 5, 5, 6)), 2, 2))
        if ndiag(part) < min_diag:
            continue
        kinds = transforms_of(part, rng) if mode == "transform" else []
        if mode == "transform" and not kinds:
            continue
        pwo, pho = E.bbox(part)
        ox = rng.randrange(cx - pwo + 1)
        oy = rng.randrange(cy - pho + 1)
        pabs = E.translate(part, ox, oy)
        avail = [e for e in pool if e not in pabs]
        big = None
        for _f in range(90):
            rng.shuffle(avail)
            cand_big = frozenset(pabs | set(avail[:nfill]))
            if mode == "transform":
                if any(E.embeds(E.transform(part, kk), cand_big)[0] for kk in kinds):
                    continue
            else:
                variants = [q for q, kind in E.near_miss(rng, part, E.lattice_edges(2, 2), want=8)
                            if kind != "missing"]
                if len(variants) < 3:
                    break
                variants = variants[:3]
                if any(E.embeds(q, cand_big)[0] for q in variants):
                    continue
            big = cand_big
            break
        if big is None:
            continue
        found, _off = E.embeds(part, big)
        assert found
        if mode == "transform":
            wrongs = [E.transform(part, kk) for kk in kinds]
            detail = (f"The other three options are the same shape "
                      f"{KIND_TEXT[kinds[0]]}, {KIND_TEXT[kinds[1]]} and {KIND_TEXT[kinds[2]]} - "
                      "none of them appears in the given figure in that form.")
        else:
            wrongs = variants
            detail = ("The other three options each differ from the part by a single stroke - "
                      "one line missing, re-angled or replaced - so none of them appears in "
                      "the figure.")
        opts = [part] + wrongs
        assert len({E.norm(o) for o in opts}) == 4
        region = E.region_name(ox, oy, pwo, pho, cx, cy)
        sol = (f"The correct figure sits {region_phrase(region)}, with every line matching "
               f"in direction and length. {detail}")
        if min_diag:
            sol += (" Both slants of the part keep their lean in the correct copy; the flipped "
                    "options reverse at least one slant.")
        return Q(name,
                 "Which of the option figures is embedded in (hidden inside) the given "
                 "figure? Rotation is not allowed.",
                 E.fig_svg(part, 3), [E.fig_svg(w, 3) for w in wrongs], sol,
                 diff=diff, sub="find-hidden", pat=pat, t=t,
                 figure=E.fig_svg(big, cx, cy))
    raise AssertionError("no puzzle: " + name)


def cp(name, pat, diff, mode="mix", min_diag=0, place="any", t=50):
    """Contains-part question: exactly one option holds the part; every wrong option is
    proven NOT to hold it."""
    rng = seeded(name)
    pool3 = sorted(E.lattice_edges(3, 3))
    for _outer in range(600):
        part = E.norm(E.random_part(rng, rng.choice((4, 5, 5, 6)), 2, 2))
        if ndiag(part) < min_diag:
            continue
        pwo, pho = E.bbox(part)
        if place == "corner":
            ox = rng.choice([0, 3 - pwo])
            oy = rng.choice([0, 3 - pho])
        else:
            ox = rng.randrange(3 - pwo + 1)
            oy = rng.randrange(3 - pho + 1)
        ans_abs = E.translate(part, ox, oy)
        avail_a = [e for e in pool3 if e not in ans_abs]
        rng.shuffle(avail_a)
        ans_opt = frozenset(ans_abs | set(avail_a[:rng.randrange(3, 7)]))
        assert E.embeds(part, ans_opt)[0]
        cores = []
        kinds = []
        if mode in ("near", "mix"):
            want = 3 if mode == "near" else 2
            vs = [(q, kind) for q, kind in E.near_miss(rng, part, set(pool3), want=10)][:want]
            if len(vs) < want:
                continue
            cores += [q for q, _k in vs]
            kinds += [k for _q, k in vs]
        if mode in ("other", "mix"):
            need = 3 if mode == "other" else 1
            extra = []
            guard = 0
            while len(extra) < need and guard < 200:
                guard += 1
                q = E.norm(E.random_part(rng, rng.choice((4, 5, 5, 6)), 2, 2))
                if E.norm(q) != E.norm(part) and all(E.norm(q) != E.norm(x) for x in cores + extra):
                    extra.append(q)
            if len(extra) < need:
                continue
            cores += extra
            kinds += ["different"] * need
        wrongs = []
        ok = True
        for core in cores:
            cwo, cho = E.bbox(core)
            cabs0 = E.translate(core, 0, 0)
            done = False
            for _f in range(60):
                dx = rng.randrange(3 - cwo + 1)
                dy = rng.randrange(3 - cho + 1)
                cabs = E.translate(core, dx, dy)
                avail = [e for e in pool3 if e not in cabs]
                rng.shuffle(avail)
                cand = frozenset(cabs | set(avail[:rng.randrange(2, 7)]))
                if not E.embeds(part, cand)[0]:
                    wrongs.append(cand)
                    done = True
                    break
            if not done:
                ok = False
                break
        if not ok:
            continue
        opts = [ans_opt] + wrongs
        assert len({E.norm(o) for o in opts}) == 4
        assert not any(E.embeds(part, w)[0] for w in wrongs)
        region = E.region_name(ox, oy, pwo, pho, 3, 3)
        rp = "in its **middle**" if region == "the middle" else f"in its **{region}**"
        sd = E.stroke_desc(part)
        if mode == "near":
            tail = ("Each wrong option is one stroke away from the part: a stroke missing, "
                    "re-angled or replaced - so the part does not actually appear there.")
        elif mode == "other":
            tail = ("The other three figures are different shapes that only look similar; "
                    "each misses at least one stroke of the part or has one pointing "
                    "another way.")
        else:
            tail = ("Of the wrong options, some are one stroke away from the part (a stroke "
                    "missing, re-angled or replaced) and the rest are different shapes that "
                    "only look similar - in none of them does the whole part appear.")
        sol = (f"The part is made of {sd}. All of its strokes appear together, in the same "
               f"directions, only in the correct option, {rp}. {tail}")
        if min_diag:
            sol += " The slants decide: only the correct option keeps both slant leans."
        return Q(name,
                 "In which option is the figure given in the question **embedded** as a "
                 "part (rotation is not allowed)?",
                 E.fig_svg(ans_opt, 3), [E.fig_svg(w, 3) for w in wrongs], sol,
                 diff=diff, sub="contains-part", pat=pat, t=t,
                 figure=E.fig_svg(part, 2, 2))
    raise AssertionError("no puzzle: " + name)


# ================================================================ questions
QS = [
    # find-hidden: 2 per pattern
    fh("find-hidden-p01", "fh-p1", "medium", (4, 4)),
    fh("find-hidden-p02", "fh-p1", "easy", (4, 4)),
    fh("find-hidden-p03", "fh-p2", "medium", (4, 3)),
    fh("find-hidden-p04", "fh-p2", "hard", (4, 3)),
    fh("find-hidden-p05", "fh-p3", "medium", (4, 4), mode="near"),
    fh("find-hidden-p06", "fh-p3", "hard", (4, 4), mode="near"),
    fh("find-hidden-p07", "fh-p4", "medium", (4, 4), min_diag=2),
    fh("find-hidden-p08", "fh-p4", "hard", (4, 3), min_diag=2),
    # contains-part: 2 per pattern
    cp("contains-part-p01", "cp-p1", "medium", mode="mix"),
    cp("contains-part-p02", "cp-p1", "easy", mode="mix"),
    cp("contains-part-p03", "cp-p2", "medium", mode="near"),
    cp("contains-part-p04", "cp-p2", "hard", mode="near"),
    cp("contains-part-p05", "cp-p3", "medium", mode="other", place="corner"),
    cp("contains-part-p06", "cp-p3", "easy", mode="other", place="corner"),
    cp("contains-part-p07", "cp-p4", "medium", mode="mix", min_diag=2),
    cp("contains-part-p08", "cp-p4", "medium", mode="near", min_diag=2),
    cp("contains-part-p09", "cp-p5", "hard", mode="mix"),
    cp("contains-part-p10", "cp-p5", "hard", mode="near"),
    cp("contains-part-p11", "cp-p6", "easy", mode="other"),
    cp("contains-part-p12", "cp-p6", "medium", mode="other"),
]

upsert(d["practice"], QS)
set_sub(d, "find-hidden", notes=NOTES["find-hidden"], patterns=PATTERNS["find-hidden"])
set_sub(d, "contains-part", notes=NOTES["contains-part"], patterns=PATTERNS["contains-part"])
d["pyqPatterns"] = PYQS
finish("embedded-figures", d)
