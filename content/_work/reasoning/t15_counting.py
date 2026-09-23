# build counting-figures topic (topic 15); every count comes from engines.count_triangles / count_rects
from math import comb
import common as C
from engines import count_triangles, count_rects, maximal_segments, seg_svg
from figs15 import FIG, cev, grid, by_area

QT = "How many triangles are there in the given figure?"


def fig(segs, scale=18):
    return seg_svg(segs, scale=scale, pad=5)


def cev_formula(k, h):
    return (k + 1) * (k + 2) // 2 * (h + 1)


def grid_rects(m, n):
    return comb(m + 1, 2) * comb(n + 1, 2)


def grid_squares(m, n):
    return sum((m - i) * (n - i) for i in range(min(m, n)))


# engine / formula cross-checks
for k, h in [(1, 0), (2, 0), (3, 0), (4, 0), (2, 1), (3, 1), (1, 2), (2, 2)]:
    assert count_triangles(cev(k, h)) == cev_formula(k, h), (k, h)
for m, n in [(2, 2), (3, 2), (3, 3), (4, 2), (4, 3), (5, 2)]:
    g = grid(m, n)
    assert count_rects(g) == grid_rects(m, n) and count_rects(g, True) == grid_squares(m, n), (m, n)

subs = []

subs.append(C.sub(
    'triangles', 'Counting triangles',
    "Never count by eye. Use one of two systematic methods:\n\n"
    "1. **Size-by-size**: count the smallest triangles, then triangles made of 2 pieces, then 3, and so on. Symmetric figures (square with diagonals) are fastest this way.\n"
    "2. **Vertex labelling**: name every corner and crossing point, then list triangles by their top vertex. Slow but fool-proof for irregular figures.\n\n"
    "**Formula for a triangle with lines from the apex**: if k lines are drawn from the apex to the base (splitting it into k + 1 parts), the number of triangles is (k + 1)(k + 2) ÷ 2 — it equals the number of ways to pick two of the k + 2 lines through the apex. Every horizontal line cutting all of them adds another full set: multiply by (h + 1).",
    formulas=[
        C.F('Apex lines', 'T = \\frac{(k+1)(k+2)}{2}', 'k lines from the apex to the base.'),
        C.F('Apex lines + horizontal cuts', 'T = \\frac{(k+1)(k+2)}{2}\\times(h+1)', 'h lines parallel to the base crossing every apex line.'),
    ],
    tricks=[
        C.T(
            'Square with both diagonals = 8',
            "A square (or any rectangle) with both diagonals always has 4 small triangles meeting at the centre and 4 half-squares — 8 in total. Add midlines and it becomes 16: 8 smallest, 4 made of two, 4 half-squares.",
            "**Q.** How many triangles are in a square with both diagonals and both midlines drawn?\n\n**Sol.** 8 smallest + 4 of two pieces (a full side of the square as base, apex at the centre) + 4 half-squares = **16**.",
            "Memorise 8 and 16; they recur inside bigger figures."),
        C.T(
            'Choose-two-lines view',
            "In a triangle with lines from the apex, each triangle is fixed by choosing its left and right side among the lines through the apex: C(k + 2, 2).",
            "**Q.** Apex with 4 lines to the base (base in 5 parts). Triangles?\n\n**Sol.** Lines through the apex = 4 + 2 sides = 6. C(6, 2) = **15**.",
            "Count the lines through the apex, then C(n, 2)."),
    ],
    mistakes=[
        "Forgetting the big outer triangle.",
        "Counting a four-sided region as a triangle because it looks pointed.",
        "Missing triangles made of two or three small pieces.",
    ]))

subs.append(C.sub(
    'squares-rectangles', 'Counting squares and rectangles',
    "For a grid of m columns and n rows of equal cells:\n\n"
    "- **Rectangles** (squares included): choose 2 of the m + 1 vertical lines and 2 of the n + 1 horizontal lines → C(m+1, 2) × C(n+1, 2).\n"
    "- **Squares**: count k × k squares for every size k: (m − k + 1)(n − k + 1), summed for k = 1 … min(m, n).\n\n"
    "For an n × n grid the square count is 1² + 2² + … + n² (a 3 × 3 grid has 9 + 4 + 1 = 14 squares).",
    formulas=[
        C.F('Rectangles in an m × n grid', 'R = \\binom{m+1}{2}\\binom{n+1}{2}', 'Pick two vertical and two horizontal lines.'),
        C.F('Squares in an m × n grid', 'S = \\sum_{k=1}^{\\min(m,n)} (m-k+1)(n-k+1)', 'n × n grid: 1² + 2² + … + n².'),
    ],
    tricks=[
        C.T(
            'Line-pair trick',
            "A rectangle is decided by its two vertical sides and two horizontal sides — so count line pairs, never shapes.",
            "**Q.** How many rectangles are in a 3 × 2 grid?\n\n**Sol.** Vertical lines 4 → C(4,2) = 6; horizontal lines 3 → C(3,2) = 3. 6 × 3 = **18**.",
            "R = C(vertical lines, 2) × C(horizontal lines, 2)."),
    ],
    mistakes=[
        "Forgetting that every square is also a rectangle.",
        "Using the number of cells instead of the number of lines in C( , 2).",
        "Missing the larger squares (2 × 2, 3 × 3) in a grid.",
    ]))

subs.append(C.sub(
    'straight-lines', 'Counting straight lines',
    "Count each **complete straight line** once, however many shapes it passes through. Group lines by direction: horizontal, vertical, then each slant direction. Two drawn pieces lying on the same straight path and touching end to end form **one** line.",
    tricks=[
        C.T(
            'Direction sweep',
            "Sweep once for horizontals, once for verticals, once per slant direction; the running total is the answer.",
            "**Q.** A square with both diagonals — how many straight lines?\n\n**Sol.** Horizontal 2, vertical 2, slants 2 → **6**.",
            "Group by direction to avoid double counting."),
    ],
    mistakes=[
        "Counting a diagonal made of two joined pieces as two lines.",
        "Missing the outer boundary lines.",
    ]))

patterns = [
    C.P('Triangle with apex lines', 'very common',
        "A triangle with several lines from one vertex, possibly with horizontal cuts.",
        "(k+1)(k+2)/2 × (h+1)."),
    C.P('Square/rectangle with diagonals', 'very common',
        "Square or rectangle with diagonals, midlines or an inner square.",
        "Size-by-size count: smallest, two-piece, half-figure."),
    C.P('Irregular composite figure', 'common',
        "House/envelope shapes, kites, subdivided triangles.",
        "Label vertices; count by region combinations."),
    C.P('Squares in a grid', 'common',
        "A chessboard-style grid; count squares.",
        "Sum (m−k+1)(n−k+1) over sizes."),
    C.P('Rectangles in a grid', 'occasional',
        "A grid; count all rectangles.",
        "C(m+1,2) × C(n+1,2)."),
    C.P('Straight lines count', 'occasional',
        "Count the straight lines needed to draw a figure.",
        "Sweep by direction; joined collinear pieces are one line."),
]

examples = []

# ex1: apex lines
s = cev(3, 0)
n = count_triangles(s)
assert n == 10
examples.append(C.Q(
    'rsn-counting-ex1', QT, ['10', '8', '9', '12'], str(n),
    "Three lines run from the apex to the base, so there are 3 + 2 = 5 lines through the apex. Any two of them form a triangle with the base: C(5, 2) = **10**. (Size-wise: 4 single, 3 double, 2 triple, 1 whole.)",
    sc="(k+1)(k+2)/2 with k = 3 → 4 × 5 / 2 = 10.",
    d='easy', sub='triangles', pat='triangle with apex lines', t=30, fig=fig(s)))

# ex2: union-jack square
s = FIG['union']
n = count_triangles(s)
assert n == 16 and by_area(s) == [(2.0, 8), (4.0, 4), (8.0, 4)]
examples.append(C.Q(
    'rsn-counting-ex2', QT, ['16', '12', '14', '18'], str(n),
    "Smallest triangles: the diagonals and midlines cut the square into 8 → **8**. Two pieces together: a full side of the square as base with the apex at the centre (a midline splits each into 2 small ones) → 4. Half-squares cut off by a diagonal → 4. Total 8 + 4 + 4 = **16**.",
    sc="Square + diagonals + midlines is a standard 16.",
    d='medium', sub='triangles', pat='square/rectangle with diagonals', t=45, fig=fig(s)))

# ex3: grid rectangles
m, n_ = 3, 2
s = grid(m, n_)
r = count_rects(s)
assert r == grid_rects(m, n_) == 18
examples.append(C.Q(
    'rsn-counting-ex3', "How many rectangles (including squares) are there in the given figure?",
    ['18', '12', '15', '20'], str(r),
    "The grid has 4 vertical and 3 horizontal lines. Choose 2 verticals: C(4, 2) = 6; choose 2 horizontals: C(3, 2) = 3. Rectangles = 6 × 3 = **18**.",
    sc="C(4,2) × C(3,2).",
    d='easy', sub='squares-rectangles', pat='rectangles in a grid', t=35, fig=fig(s)))

# ex4: straight lines in envelope/house
s = FIG['env']
ln = len(maximal_segments(s))
assert ln == 8
examples.append(C.Q(
    'rsn-counting-ex4', "What is the minimum number of straight lines needed to draw the given figure?",
    ['8', '7', '9', '10'], str(ln),
    "Horizontal: top and bottom of the rectangle → 2. Vertical: two sides → 2. Diagonals of the rectangle → 2. Roof slopes → 2. Total **8**.",
    sc="Sweep by direction: 2 + 2 + 2 + 2.",
    d='easy', sub='straight-lines', pat='straight lines count', t=30, fig=fig(s)))

# ---------------------------------------------------------------- practice
pr = []


def tq(i, segs, opts, sol, sc, d, sub='triangles', pat='irregular composite figure', t=45, place=None, expect=None):
    n = count_triangles(segs)
    if expect is not None:
        assert n == expect, (i, n)
    pr.append(C.Q('rsn-counting-%d' % i, QT, opts, str(n), sol, sc=sc, d=d, sub=sub, pat=pat, t=t,
                  fig=fig(segs), place=place))


tq(1, cev(4, 0), ['15', '10', '12', '14'],
   "Four lines from the apex divide the base into 5 parts. Lines through the apex = 4 + 2 = 6; any two form a triangle: C(6, 2) = **15**.",
   "(k+1)(k+2)/2 = 5 × 6 / 2 = 15.", 'easy', pat='triangle with apex lines', t=30, expect=15)

tq(2, cev(2, 1), ['12', '6', '9', '10'],
   "Two apex lines give (3 × 4)/2 = 6 triangles above the base. The horizontal line crosses all apex lines and creates another complete set of 6 above it. Total 6 × 2 = **12**.",
   "6 × (h + 1) with h = 1.", 'medium', pat='triangle with apex lines', t=40, expect=12)

tq(3, cev(3, 1), ['20', '10', '15', '16'],
   "Three apex lines → 10 triangles on the base; the horizontal line gives a second set of 10 on itself. Total **20**.",
   "10 × 2.", 'medium', pat='triangle with apex lines', t=40, expect=20)

s = FIG['mid']
assert by_area(s) == [(6.0, 4), (24.0, 1)]
tq(4, s, ['5', '4', '6', '7'],
   "Joining the midpoints of the sides makes 4 small triangles (the middle one is upside down). Plus the whole triangle → **5**. No two small triangles combine into a triangle.",
   "4 + 1.", 'easy', t=30, expect=5)

s = FIG['sqdiag']
assert by_area(s) == [(4.0, 4), (8.0, 4)]
tq(5, s, ['8', '4', '6', '10'],
   "The diagonals make 4 small triangles meeting at the centre. Each diagonal also cuts the square into 2 half-squares, so 4 more. Total **8**.",
   "Square + both diagonals = 8, always.", 'easy', pat='square/rectangle with diagonals', t=25, expect=8)

s = FIG['rect2diag']
assert by_area(s) == [(4.0, 8), (8.0, 8), (16.0, 2)]
tq(6, s, ['18', '16', '14', '20'],
   "Each of the two squares has both its diagonals → 8 triangles each = 16. Two larger triangles use the whole bottom or whole top side of the rectangle with the two inner diagonals meeting at the midpoint of the opposite side → 2. Total **18**.",
   "8 + 8 + 2 spanning triangles.", 'hard', pat='square/rectangle with diagonals', t=60, expect=18)

s = FIG['sq_inner_d']
assert by_area(s) == [(1.0, 8), (2.0, 4), (4.0, 4), (8.0, 4)]
tq(7, s, ['20', '16', '18', '24'],
   "The inner square joins the midpoints; the diagonals of the outer square cross everything. Size by size: each corner triangle is split by a diagonal into 2 tiny ones → 8; the 4 corner triangles themselves → 4; the 4 triangles with a full side of the square as base and apex at the centre → 4; the 4 half-squares → 4. Total 8 + 4 + 4 + 4 = **20**.",
   "Work outward: tiny, corner, centre-apex, half-square.", 'hard', pat='square/rectangle with diagonals', t=75, place=1, expect=20)

s = FIG['grid22diag']
assert by_area(s) == [(2.0, 8), (8.0, 2)]
tq(8, s, ['10', '8', '12', '9'],
   "Each of the 4 cells has one diagonal → 8 small triangles. The diagonals of the top-left and bottom-right cells lie on one straight line (the main diagonal of the whole square), so the square's two halves on either side of it are 2 more big triangles. The other two cell-diagonals do not line up with anything. Total **10**.",
   "Check which small diagonals join into one long line.", 'hard', pat='square/rectangle with diagonals', t=60, expect=10)

s = FIG['kite']
assert count_triangles(s) == 8
tq(9, s, ['8', '4', '6', '10'],
   "The two diagonals cut the kite into 4 small triangles. The vertical diagonal cuts it into 2 halves (each a triangle) and the horizontal diagonal cuts it into 2 more. Total 4 + 2 + 2 = **8**.",
   "Same as square with diagonals: 4 + 4.", 'easy', t=30, expect=8)

s = FIG['env']
assert by_area(s) == [(6.0, 5), (12.0, 4)]
tq(10, s, ['9', '8', '10', '7'],
   "The rectangle with both diagonals gives 8 triangles (4 small + 4 half-rectangles). The roof is 1 more. The roof cannot combine with any lower piece, since its sides do not continue down. Total **9**.",
   "8 (rectangle with diagonals) + 1 (roof).", 'easy', t=35, expect=9)

s = FIG['tri_mid_diag']
assert by_area(s) == [(6.0, 4), (12.0, 2), (24.0, 1)]
tq(11, s, ['7', '5', '6', '8'],
   "The vertical line from the apex splits the triangle into 2 halves. Two lines from the base midpoint to the midpoints of the slanted sides cut each half into 2 → 4 smallest. The 2 halves themselves → 2. The whole triangle → 1. Total **7**.",
   "4 small + 2 halves + 1 whole.", 'medium', t=45, expect=7)

s = grid(3, 3)
sq_ = count_rects(s, True)
assert sq_ == 14
pr.append(C.Q('rsn-counting-12', "How many squares are there in the given figure?", ['14', '9', '10', '13'], str(sq_),
              "1 × 1 squares: 9. 2 × 2 squares: 4. 3 × 3 square: 1. Total 9 + 4 + 1 = **14**.",
              sc="n × n grid: 1² + 2² + … + n².", d='easy', sub='squares-rectangles', pat='squares in a grid', t=30, fig=fig(s)))

s = grid(4, 2)
r = count_rects(s)
assert r == 30
pr.append(C.Q('rsn-counting-13', "How many rectangles (including squares) are there in the given figure?", ['30', '24', '18', '36'], str(r),
              "Vertical lines: 5 → C(5, 2) = 10. Horizontal lines: 3 → C(3, 2) = 3. Rectangles = 10 × 3 = **30**.",
              sc="C(5,2) × C(3,2).", d='medium', sub='squares-rectangles', pat='rectangles in a grid', t=40, fig=fig(s)))

s = grid(4, 3)
sq_ = count_rects(s, True)
assert sq_ == 20
pr.append(C.Q('rsn-counting-14', "How many squares are there in the given figure?", ['20', '12', '18', '17'], str(sq_),
              "1 × 1: 4 × 3 = 12. 2 × 2: 3 × 2 = 6. 3 × 3: 2 × 1 = 2. Total 12 + 6 + 2 = **20**.",
              sc="Σ (m−k+1)(n−k+1).", d='medium', sub='squares-rectangles', pat='squares in a grid', t=45, fig=fig(s), place=3))

s = FIG['grid22diag']
ln = len(maximal_segments(s))
assert ln == 9
pr.append(C.Q('rsn-counting-15', "What is the minimum number of straight lines needed to draw the given figure?",
              ['9', '10', '8', '11'], str(ln),
              "Horizontal: 3. Vertical: 3. Slanting: the top-left and bottom-right cell diagonals lie on one straight line → 1; the other two cell diagonals are separate → 2. Total 3 + 3 + 1 + 2 = **9**.",
              sc="Joined collinear pieces count once.", d='medium', sub='straight-lines', pat='straight lines count', t=45, fig=fig(s)))

assert len(pr) == 15

t = C.topic(
    'counting-figures', 'Counting Figures', 'medium', {'tier1': '0-1', 'tier2': '1-2'},
    "Count triangles, squares, rectangles or straight lines in a figure. Recognise the standard shapes first (square with diagonals = 8, with midlines too = 16; apex lines (k+1)(k+2)/2; grid rectangles C(m+1,2)C(n+1,2); squares 1² + … + n²), and count anything irregular size by size so nothing is missed or counted twice.",
    subs, patterns, examples, pr)
C.write_topic(t)
print('OK counting-figures')
