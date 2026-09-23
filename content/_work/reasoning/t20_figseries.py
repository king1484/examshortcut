# build figure-series topic (topic 20); every frame is generated from its rule, the answer is rule(n) and
# every distractor is checked to differ from it (and from each shown frame)
import copy
import common as C
from engines import series_row_svg, frame_only

QS = "Select the figure that will come next in the given series."


def st(slots=None, arrow=None, shade=None, lines=None):
    d = {}
    if slots:
        d['slots'] = dict(slots)
    if arrow is not None:
        d['arrow'] = arrow % 8
    if shade is not None:
        d['shade'] = shade % 4
    if lines:
        d['lines'] = lines
    return d


def key(s):
    return (tuple(sorted(s.get('slots', {}).items())), s.get('arrow'), s.get('shade'), s.get('lines'))


def series_q(id, rule, shown, wrong, sol, sc, d, sub, pat, t=45, place=None):
    frames = [rule(i) for i in range(shown)]
    ans = rule(shown)
    ks = [key(f) for f in frames]
    assert key(ans) not in ks[-1:], 'answer repeats the last frame'
    wr = [w for w in wrong]
    allk = [key(ans)] + [key(w) for w in wr]
    assert len(set(allk)) == 4, (id, allk)
    opts = [frame_only(ans)] + [frame_only(w) for w in wr]
    assert len(set(opts)) == 4
    return C.Q(id, QS, opts, opts[0], sol, sc=sc, d=d, sub=sub, pat=pat, t=t,
               fig=series_row_svg(frames), place=place)


def slots8(*pairs):
    """pairs of (slot, kind) with slot taken mod 8 (clockwise from top-left)."""
    out = {}
    for s, k in pairs:
        assert s % 8 not in out, 'slot clash'
        out[s % 8] = k
    return out


subs = [
    C.sub('movement-rotation', 'Movement and rotation',
          "Most figure series move an element step by step:\n\n"
          "- **Around the border**: a dot/shape jumps a fixed number of positions (1, 2, 3 …) clockwise or anticlockwise. Border positions: 4 corners + 4 edge mid-points = 8 places.\n"
          "- **Rotation**: an arrow or line turns by a fixed angle (45°, 90°, 135°) each step.\n"
          "- **Shading**: a shaded quarter moves round the square.\n\n"
          "Track **one element at a time** across all frames, write its step (e.g. +1 clockwise), then predict its next place. Do the same for each element and pick the option that agrees on all of them.",
          formulas=[C.F('Position after k steps', 'p_{k} = (p_{0} + k\\,s) \\bmod 8', 's = step (positive = clockwise) on the 8 border places.')],
          tricks=[C.T('One element, one line',
                      "Write a tiny table: element → positions in frames 1-4 → step → next. Options that fail any row are out.",
                      "**Q.** A dot sits at places 1, 3, 5, 7 (clockwise count). Next?",
                      "Step +2: 7 + 2 = 9 ≡ **1** (back to the first place)."),
                  C.T('Angles as clock hours',
                      "Treat 45° as 1.5 clock-hours; an arrow turning 90° clockwise each step goes 12 → 3 → 6 → 9 → 12.",
                      "**Q.** Arrow: up, right, down, … next?",
                      "Left (90° clockwise each step).")],
          mistakes=["Mixing up clockwise and anticlockwise because the first step looked like both.",
                    "Tracking only one element and choosing an option that is right for it but wrong for another.",
                    "Forgetting to wrap round after the 8th border position."]),
    C.sub('addition-change', 'Adding, removing and changing elements',
          "Some series change the **number** of elements: strokes grow 1, 2, 3, …; a new shape appears in the next corner each step; or shapes disappear one by one.\n\n"
          "Others **alternate**: an arrow flips up/down, a shape switches between two kinds. Count carefully, and check whether each new element is added at a fixed rotation (clockwise) from the previous one.",
          tricks=[C.T('Count first',
                      "Count the elements in each frame. If the counts go 1, 2, 3, 4, only options with 5 survive; then check positions.",
                      "**Q.** Strokes: 1, 2, 3, 4. Next?",
                      "**5** strokes.")],
          mistakes=["Ignoring an alternating element because it returns to an earlier state.",
                    "Counting a shape twice when it sits on a boundary."]),
]

patterns = [
    C.P('Element moving round the border', 'very common',
        "One or two small shapes change position along the edge of a square.",
        "Number the 8 border places; find the step of each shape."),
    C.P('Rotating arrow/line', 'very common',
        "An arrow turns each frame.",
        "Find the angle per step (45°, 90°, 135°) and its direction."),
    C.P('Moving shaded part', 'common',
        "A shaded quarter moves round the square.",
        "Quarter order TL → TR → BR → BL is clockwise."),
    C.P('Growing count', 'common',
        "Number of strokes/shapes rises by one each frame.",
        "Count first, then check positions."),
    C.P('Two or three rules together', 'common',
        "Several elements, each with its own rule.",
        "Solve each element separately; the answer satisfies all."),
]

examples = []
R = lambda i: st(arrow=i)
examples.append(series_q(
    'rsn-figseries-ex1', R, 4, [st(arrow=5), st(arrow=3), st(arrow=0)],
    "The arrow points up, then up-right, right, down-right — it turns **45° clockwise** each step. Next it points **straight down**.",
    "45° clockwise per step.", 'easy', 'movement-rotation', 'rotating arrow/line', 30))

R = lambda i: st(slots={(2 * i) % 8: 'dot'})
examples.append(series_q(
    'rsn-figseries-ex2', R, 4, [st(slots={7: 'dot'}), st(slots={1: 'dot'}), st(slots={6: 'dot'})],
    "Number the 8 border places clockwise from the top-left corner. The dot is at places 0, 2, 4, 6 — two places clockwise each step (corner to corner). Next: 6 + 2 = 8 → place 0, the **top-left corner**.",
    "Step +2 on the border; wrap round after 8.", 'easy', 'movement-rotation', 'element moving round the border', 35))

R = lambda i: st(lines=i + 1, arrow=0 if i % 2 == 0 else 4)
examples.append(series_q(
    'rsn-figseries-ex3', R, 4, [st(lines=5, arrow=4), st(lines=4, arrow=0), st(lines=6, arrow=0)],
    "Two rules. The strokes increase by one: 1, 2, 3, 4 → **5**. The arrow alternates up, down, up, down → next **up**. Only the figure with 5 strokes and an upward arrow fits both.",
    "Count first, then the alternating arrow.", 'medium', 'addition-change', 'two or three rules together', 40))

R = lambda i: st(slots=slots8((i, 'dot'), (7 - 2 * i, 'tri')))
examples.append(series_q(
    'rsn-figseries-ex4', R, 4, [st(slots=slots8((4, 'dot'), (1, 'tri'))), st(slots=slots8((5, 'dot'), (7, 'tri'))),
                                st(slots=slots8((4, 'dot'), (3, 'tri')))],
    "Border places numbered clockwise from the top-left corner (0-7). The dot is at 0, 1, 2, 3 — **one place clockwise** each step → next 4 (bottom-right corner). The triangle is at 7, 5, 3, 1 (the edge mid-points) — **two places anticlockwise** each step → next 1 − 2 = −1 → 7 (left-middle). The answer has the dot at the bottom-right corner and the triangle at the middle of the left side.",
    "Solve each shape separately.", 'hard', 'movement-rotation', 'two or three rules together', 55))

pr = []
specs = []

specs.append(('movement-rotation', 'rotating arrow/line', 'easy', 30,
              lambda i: st(arrow=2 * i), 4, [st(arrow=6), st(arrow=2), st(arrow=7)],
              "The arrow turns **90° clockwise** each step: up → right → down → left. Next it points **up** again.",
              "90° clockwise per step."))
specs.append(('movement-rotation', 'rotating arrow/line', 'medium', 40,
              lambda i: st(arrow=3 * i), 4, [st(arrow=5), st(arrow=3), st(arrow=2)],
              "The arrow turns **135° clockwise** each step (three 45° steps): up → down-right → left → up-right. Next: up-right + 135° = **down**.",
              "Count 45° units: +3 each step."))
specs.append(('movement-rotation', 'rotating arrow/line', 'medium', 40,
              lambda i: st(arrow=-i + 2), 4, [st(arrow=0), st(arrow=4), st(arrow=5)],
              "The arrow starts pointing right and turns **45° anticlockwise** each step: right → up-right → up → up-left. Next: **left**.",
              "45° anticlockwise per step."))
specs.append(('movement-rotation', 'element moving round the border', 'easy', 35,
              lambda i: st(slots={(1 + i) % 8: 'ring'}), 4, [st(slots={6: 'ring'}), st(slots={4: 'ring'}), st(slots={0: 'ring'})],
              "The ring moves **one place clockwise** round the border each step: top-middle → top-right corner → right-middle → bottom-right corner. Next: **bottom-middle**.",
              "Step +1 clockwise."))
specs.append(('movement-rotation', 'element moving round the border', 'medium', 40,
              lambda i: st(slots={(7 - 3 * i) % 8: 'sq'}), 4, [st(slots={1: 'sq'}), st(slots={0: 'sq'}), st(slots={2: 'sq'})],
              "Number the border places clockwise from the top-left corner (0-7). The square is at 7, 4, 1, 6 — it moves **three places anticlockwise** each step. Next: 6 − 3 = 3, the **right-middle** place.",
              "Step −3 on the 8-place border."))
specs.append(('movement-rotation', 'moving shaded part', 'easy', 30,
              lambda i: st(shade=i), 4, [st(shade=2), st(shade=1), st(shade=3)],
              "The shaded quarter moves **clockwise**: top-left → top-right → bottom-right → bottom-left. Next it returns to the **top-left** quarter.",
              "Quarter moves one step clockwise."))
specs.append(('movement-rotation', 'two or three rules together', 'medium', 45,
              lambda i: st(shade=-i, arrow=2 * i + 1), 4, [st(shade=1, arrow=1), st(shade=0, arrow=7), st(shade=3, arrow=3)],
              "Two elements. Shading moves **anticlockwise**: TL → BL → BR → TR → next **TL**. The arrow turns **90° clockwise**: up-right → down-right → down-left → up-left → next **up-right**. The answer has the top-left quarter shaded and the arrow pointing up-right.",
              "Shading and arrow separately."))
specs.append(('addition-change', 'growing count', 'easy', 30,
              lambda i: st(lines=2 * i + 1), 3, [st(lines=6), st(lines=5), st(lines=8)],
              "Strokes: 1, 3, 5 — **two more** each step. Next: **7** strokes.",
              "Odd numbers: +2."))
specs.append(('addition-change', 'growing count', 'medium', 40,
              lambda i: st(slots={2 * k: 'dot' for k in range(i + 1)}), 3,
              [st(slots={0: 'dot', 2: 'dot', 4: 'dot'}), st(slots={0: 'dot', 2: 'dot', 4: 'dot', 5: 'dot'}),
               st(slots={0: 'dot', 1: 'dot', 2: 'dot', 4: 'dot'})],
              "A dot is **added at the next corner clockwise** each step: top-left; then top-right; then bottom-right. Next: **4 dots, one in every corner** (the new one at the bottom-left).",
              "Count first."))
specs.append(('addition-change', 'two or three rules together', 'medium', 45,
              lambda i: st(slots={(2 * i) % 8: 'tri'}, lines=4 - i), 3, [st(slots={6: 'tri'}, lines=2), st(slots={4: 'tri'}, lines=2), st(slots={6: 'tri'}, lines=0)],
              "Two rules. The triangle moves **two places clockwise** (corner to corner): top-left → top-right → bottom-right → next **bottom-left**. The strokes decrease by one: 4, 3, 2 → next **1**. The answer has the triangle at the bottom-left corner and a single stroke.",
              "Moving corner + falling count."))
specs.append(('addition-change', 'two or three rules together', 'hard', 55,
              lambda i: st(slots=slots8((i, 'x' if i % 2 == 0 else 'plus'), (5 + i, 'dot'))), 4,
              [st(slots=slots8((4, 'plus'), (1, 'dot'))), st(slots=slots8((4, 'x'), (0, 'dot'))), st(slots=slots8((3, 'x'), (1, 'dot')))],
              "Border places numbered clockwise from the top-left corner (0-7). The cross-shaped mark is at 0, 1, 2, 3 (one step clockwise each time) and **alternates** between × and + (×, +, ×, +) → next: place 4 (bottom-right corner) as **×**. The dot is at 5, 6, 7, 0 (one step clockwise) → next place **1** (top-middle). The answer has × at the bottom-right corner and the dot at the top-middle.",
              "Movement + alternation."))
specs.append(('movement-rotation', 'two or three rules together', 'hard', 60,
              lambda i: st(slots=slots8((2 * i, 'sq'), (7 - i, 'ring')), arrow=4 + i), 4,
              [st(slots=slots8((0, 'sq'), (4, 'ring')), arrow=0), st(slots=slots8((0, 'sq'), (3, 'ring')), arrow=1),
               st(slots=slots8((6, 'sq'), (3, 'ring')), arrow=0)],
              "Three rules (places numbered clockwise from the top-left corner, 0-7). Square: 0, 2, 4, 6 — two places clockwise → next **0** (top-left corner). Ring: 7, 6, 5, 4 — one place anticlockwise → next **3** (right-middle). Arrow: down, down-left, left, up-left — 45° clockwise → next **up**. Only one option satisfies all three.",
              "One rule per element."))

for n, (sb, pat, d, t, rule, shown, wrong, sol, sc) in enumerate(specs, start=1):
    pr.append(series_q('rsn-figseries-%d' % n, rule, shown, wrong, sol, sc, d, sb, pat, t))

assert len(pr) == 12
t = C.topic('figure-series', 'Figure Series', 'low', {'tier1': '0-1', 'tier2': '0-1'},
            "A row of figures changes by fixed rules — an element moves round the border, an arrow rotates, a shaded quarter turns, or a count grows. Track each element separately, find its step, and pick the only option that satisfies every rule.",
            subs, patterns, examples, pr)
C.write_topic(t)
print('OK figure-series')
