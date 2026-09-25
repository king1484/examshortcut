"""Notes, patterns and topic-level PYQ patterns for reasoning/counting-figures."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P, PYQ  # noqa

NOTES = {}
PATTERNS = {}

# ======================================================================= triangles
NOTES["triangles"] = r"""### What the question asks
You get a line drawing and must say **how many triangles** are hidden in it. A triangle is any closed shape with exactly three straight sides. The sides may be made of several small drawn pieces joined in a straight line. Small triangles, medium ones made of several pieces, and the big outer triangle all count.

Think of a samosa cut by a knife. Each cut makes new small pieces, but a big piece made of two small pieces is still a triangle. Most wrong answers come from missing these bigger joined triangles.

### Method 1: size by size
1. Count the **smallest** triangles (the ones with no line inside).
2. Count triangles made of **2 pieces**, then **3 pieces**, then **4**, and so on.
3. Do not forget the **whole figure** if it is itself a triangle.
4. Add all the groups.

Example: a square with both diagonals. Smallest triangles = 4 (meeting at the centre). Triangles made of 2 pieces = 4 (each is half of the square). Total = **8**.

### Method 2: name the corners
Put a letter on every corner and every crossing point. Take one point at a time and list every triangle that has it as a corner, using only points joined by drawn lines. This is slow but safe for odd, irregular figures.

### Ready formulas for standard figures
**Lines from the apex.** A triangle with k lines drawn from the top corner (apex) to the base splits the base into k + 1 parts. Every triangle here has the apex as its top and two of the lines through the apex as its sides. There are k + 2 such lines, so

$$T = \frac{(k+1)(k+2)}{2}$$

With 3 apex lines: $\frac{4 \times 5}{2} = 10$.

**Adding horizontal cuts.** Each line parallel to the base that crosses all the apex lines gives one more full set. With h such lines: $T = \frac{(k+1)(k+2)}{2} \times (h+1)$. With 2 apex lines and 1 cut: $6 \times 2 = 12$.

**Triangle cut into rows of small triangles.** A big triangle whose sides are divided into n equal parts and joined by lines parallel to the sides:

| Rows n | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Triangles | 1 | 5 | 13 | 27 | 48 |

Remember that upside-down triangles also count (a 3-row figure has 3 upside-down small ones).

**Square with diagonals.** Both diagonals: 8. Both diagonals and both midlines: 16 (8 smallest + 4 of two pieces + 4 half-squares).

**Triangle with its three medians** (lines from each corner to the middle of the opposite side): 16 triangles.

**Pentagon with all its diagonals** (a star inside a pentagon): 35 triangles. This one appears again and again, so remember it.

### Special cases
- A four-sided piece is never a triangle, even if it looks pointed.
- Three points on one straight line do not make a triangle.
- Two drawn pieces that lie in one straight line act as one side.
- When a figure is symmetric, count one half and double, but add any triangle that sits across the middle line only once.

### Quick revision
- Count size by size: smallest, then 2-piece, 3-piece, and finally the whole figure.
- Apex lines: (k+1)(k+2)/2; with h horizontal cuts multiply by (h+1).
- Square + 2 diagonals = 8; add 2 midlines = 16.
- Triangle rows: 1, 5, 13, 27, 48.
- Triangle with 3 medians = 16; pentagon with all diagonals = 35.
- Name the corners for any irregular figure.
"""

PATTERNS["triangles"] = [
    P("ct-p1", "Triangle with lines from the apex (and horizontal cuts)", "very common",
      "One big triangle. Several lines start at the top corner and fall on the base. Sometimes one or two lines run parallel to the base.",
      "1. Count k = lines from the apex (not the two sides).\n2. Count h = lines parallel to the base that cross every apex line.\n3. Triangles = (k+1)(k+2)/2 × (h+1).\n\n**Why:** every triangle uses the apex and any 2 of the k + 2 lines through it; each horizontal line gives a new base for the same set.",
      "A triangle has 3 lines drawn from its apex to the base and 1 line parallel to the base cutting all of them. How many triangles are there?",
      "k = 3 → (4 × 5)/2 = 10 triangles for one base. h = 1, so there are 2 bases. Total = 10 × 2 = **20**.",
      formula=r"T=\frac{(k+1)(k+2)}{2}\times(h+1)"),
    P("ct-p2", "Square or rectangle with diagonals and midlines", "very common",
      "A square or rectangle with one or both diagonals, often with the lines joining the middles of opposite sides.",
      "1. Smallest triangles first (usually 4 or 8 around the centre).\n2. Triangles made of 2 pieces (a full side of the square as base).\n3. Half-squares made by each diagonal (4 of them when both diagonals are drawn).\n4. Add.\n\n**Why:** these figures are symmetric, so each size comes in a set of 4.",
      "A square has both diagonals and both midlines drawn. How many triangles are there?",
      "Smallest: 8. Two-piece triangles with a side of the square as base: 4. Half-squares: 4. Total = 8 + 4 + 4 = **16**."),
    P("ct-p3", "Triangle divided into rows of small triangles", "common",
      "A big triangle filled with a honeycomb of small triangles, some pointing up and some pointing down.",
      "1. Find n = number of rows.\n2. Use the table 1, 5, 13, 27, 48 for n = 1 to 5.\n3. If you must count: upright triangles of each size, then upside-down ones.\n\n**Why:** upright triangles of side s number (n−s+1)(n−s+2)/2; upside-down ones are rarer and are the ones people miss.",
      "A triangle is divided into 3 rows of small triangles (9 small triangles in all). How many triangles are there?",
      "Upright: size 1 = 6, size 2 = 3, size 3 = 1 → 10. Upside-down: 3 small ones. Total = **13**."),
    P("ct-p4", "Triangle with lines from its corners (medians and cevians)", "common",
      "A triangle with lines from one or more corners to the opposite sides, which cross inside the triangle.",
      "1. Label every corner and crossing point.\n2. Count triangles that use each drawn line as one side.\n3. Check the big outer triangle.\n\n**Why:** the lines cross at inner points, so triangles appear at several levels; labelling stops double counting.",
      "In a triangle, all three medians are drawn (each joins a corner to the middle of the opposite side). How many triangles are formed?",
      "6 smallest triangles around the centre. 3 made of 2 pieces (a full side as base, the centre point as top). 6 made of 3 pieces (each median cuts the big triangle into two halves). The whole triangle: 1. Total = 6 + 3 + 6 + 1 = **16**."),
    P("ct-p5", "Irregular composite figures (house, star, pentagon)", "common",
      "A figure built from several shapes: a house (square with a roof), a star inside a pentagon, two overlapping triangles, an envelope.",
      "1. Break the figure into known parts (square with diagonals = 8, and so on).\n2. Count triangles fully inside each part.\n3. Count triangles that cross from one part into another.\n4. Add; confirm symmetric counts.\n\n**Why:** known sub-figures give quick totals; only the crossing triangles need fresh work.",
      "A regular pentagon has all 5 of its diagonals drawn (a star inside it). How many triangles are there?",
      "Sort by how many of the 5 outer corners a triangle uses. Three corners: any 3 corners are joined, so C(5, 3) = 10. Two corners: 20. One corner (the points of the star): 5. Total = 10 + 20 + 5 = **35**."),
]

# ======================================================================= squares-rectangles
NOTES["squares-rectangles"] = r"""### What the question asks
The figure is usually a grid, like a chessboard or a window with bars, and you must count **squares** or **rectangles**. A rectangle is a four-sided shape with four right angles. A square is a rectangle whose four sides are equal. So **every square is also a rectangle**. When a question asks for rectangles, squares are included unless it says "rectangles that are not squares".

### Counting squares in a grid
In a grid of m columns and n rows of equal cells, count squares size by size.

- 1 × 1 squares: m × n
- 2 × 2 squares: (m − 1)(n − 1)
- 3 × 3 squares: (m − 2)(n − 2) ... until one side reaches 1.

$$S = \sum_{k=1}^{\min(m,n)} (m-k+1)(n-k+1)$$

For a square grid of n × n this becomes $1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$.

Example: a chessboard (8 × 8) has $\frac{8 \times 9 \times 17}{6} = 204$ squares. A 4 × 3 grid has 12 + 6 + 2 = 20 squares.

### Counting rectangles in a grid
A rectangle is fixed the moment you choose its **two vertical sides** and **two horizontal sides**. A grid of m columns has m + 1 vertical lines, and n rows give n + 1 horizontal lines. So

$$R = \binom{m+1}{2} \times \binom{n+1}{2} = \frac{m(m+1)}{2} \times \frac{n(n+1)}{2}$$

Example: a 3 × 2 grid has 4 vertical and 3 horizontal lines: C(4, 2) × C(3, 2) = 6 × 3 = 18 rectangles.

A single strip of m cells has $\frac{m(m+1)}{2}$ rectangles (choose a start cell and an end cell).

Rectangles that are **not** squares = R − S.

### Tilted squares
Joining the middles of the four sides of a square makes a **tilted square** (a diamond). Joining the middles again makes another upright square, and so on. Each tilted square counts once. Grid lines passing through a diamond cut it into triangles, not squares, so do not invent extra squares there.

### Irregular grids
Plus signs, L-shapes and grids with missing lines break the formula. Then:
1. Count the 1 × 1 cells.
2. Look for each bigger size and check that **all four sides are drawn**.
3. For rectangles, pick each cell as the top-left corner and count how far you can extend right and down.

### Special cases
- A line missing from the middle of a grid kills every rectangle that needs it as a side.
- Cells must be equal for the square formula. If they are not, count by hand.
- The outer boundary counts as one rectangle (and one square if it is square).

### Quick revision
| Figure | Squares | Rectangles |
|---|---|---|
| n × n grid | 1² + 2² + … + n² | [n(n+1)/2]² |
| m × n grid | Σ (m−k+1)(n−k+1) | C(m+1,2) × C(n+1,2) |
| Strip of m cells | m | m(m+1)/2 |

- 2 × 2 → 5 squares, 9 rectangles; 3 × 3 → 14 squares, 36 rectangles; 4 × 4 → 30 squares, 100 rectangles.
- Every square is a rectangle.
- Irregular figure: check all four sides of every candidate.
"""

PATTERNS["squares-rectangles"] = [
    P("sr-p1", "Squares in a grid", "very common",
      "A chessboard-like grid; the question asks for squares.",
      "1. Note m columns and n rows.\n2. Add (m−k+1)(n−k+1) for k = 1, 2, … up to the smaller side.\n3. For n × n use 1² + 2² + … + n².\n\n**Why:** a k × k square fits in (m−k+1) places across and (n−k+1) places down.",
      "How many squares are there in a 4 × 4 grid?",
      "1 + 4 + 9 + 16 = **30**.",
      formula=r"S=\sum_{k=1}^{\min(m,n)}(m-k+1)(n-k+1)"),
    P("sr-p2", "Rectangles in a grid", "common",
      "A grid of cells; the question asks for rectangles (squares included).",
      "1. Count vertical lines (m + 1) and horizontal lines (n + 1).\n2. Rectangles = C(m+1, 2) × C(n+1, 2).\n3. For a single strip of m cells: m(m+1)/2.\n\n**Why:** choosing 2 vertical and 2 horizontal lines fixes exactly one rectangle.",
      "How many rectangles are there in a grid of 4 columns and 3 rows?",
      "Vertical lines 5 → C(5,2) = 10. Horizontal lines 4 → C(4,2) = 6. Rectangles = 10 × 6 = **60**.",
      formula=r"R=\binom{m+1}{2}\binom{n+1}{2}"),
    P("sr-p3", "Squares with a tilted (diamond) square inside", "common",
      "A square or grid with lines joining the middles of the sides, forming a diamond, sometimes repeated.",
      "1. Count the upright squares of the grid.\n2. Add each tilted square whose four sides are fully drawn.\n3. Do not count triangles formed where grid lines cut the diamond.\n\n**Why:** a tilted square is a square too, but grid lines through it only make triangles.",
      "A square is divided into 4 equal squares by its two midlines, and the midpoints of its four sides are joined to form a diamond. How many squares are there?",
      "Upright squares: 4 small + 1 big = 5. Tilted square: 1. Total = **6**."),
    P("sr-p4", "Irregular grids (plus, L-shape, missing lines)", "occasional",
      "Cells joined in a cross, L or step shape, or a grid with a line missing.",
      "1. Count single cells.\n2. For each bigger shape, check all four sides are drawn.\n3. For rectangles, fix a top-left cell and extend right/down while the region stays filled.\n\n**Why:** the grid formula assumes every line runs the full width; here it does not.",
      "Five equal squares form a plus sign (one in the centre, one on each side). How many rectangles are there?",
      "Single cells: 5. Two-cell rectangles: 4 (centre with each arm). Three-cell rectangles: 2 (the full row and the full column). Total = **11**."),
]

# ======================================================================= straight-lines
NOTES["straight-lines"] = r"""### What the question asks
"How many straight lines are there in the figure?" or "What is the least number of straight lines needed to draw it?" Both mean the same: count each **complete straight line** once, even if it passes through many shapes or is drawn as several touching pieces.

Think of a road: it may cross ten junctions, but it is still one road. Two pieces lying on the same path and touching end to end are **one** line. Two pieces on the same path with a gap between them are **two** lines.

### The direction sweep
1. Count all **horizontal** lines (left to right), from top to bottom.
2. Count all **vertical** lines (top to bottom), from left to right.
3. Count **slanting** lines of each direction separately: first those going down to the right, then those going down to the left.
4. Add the groups.

Doing one direction at a time stops you from counting a line twice.

Example: a square with both diagonals and both midlines. Horizontal 3 (top side, midline, bottom side), vertical 3, slanting 2. Total = **8**.

### Grids
A grid of m columns and n rows has m + 1 vertical and n + 1 horizontal lines, so
$$L = (m+1) + (n+1)$$
A 3 × 2 grid needs 4 + 3 = 7 lines.

If both long diagonals of the whole grid are also drawn, add 2. If every small cell has its own diagonals, cell diagonals that meet end to end on one path join into a single long line, so count paths, not pieces.

### Stars and polygons
- A **five-point star** (pentagram) is drawn with only **5** lines.
- A **six-point star** made of two triangles has **6** lines.
- A regular hexagon with its 3 long diagonals has 6 + 3 = 9 lines.
- A triangle split into rows of small triangles: 3 directions, and each direction has as many lines as there are rows. So 3 rows give 3 × 3 = 9 lines.

### Special cases
- A curve is not a straight line. Circles and arcs are ignored.
- Lines that only look close are different unless they are exactly in line.
- In "how many vertical lines" questions, count only that direction.

### Quick revision
- One straight path = one line, however many pieces it is drawn in.
- Sweep: horizontal, vertical, then each slant direction.
- m × n grid: (m + 1) + (n + 1) lines.
- Square + diagonals + midlines = 8 lines.
- Pentagram 5, six-point star 6, hexagon with long diagonals 9.
"""

PATTERNS["straight-lines"] = [
    P("sl-p1", "Total straight lines in a square/rectangle figure", "common",
      "A square or rectangle with diagonals, midlines or cell diagonals; asks for straight lines.",
      "1. Horizontal lines.\n2. Vertical lines.\n3. Slanting lines, one direction at a time, joining pieces that are in one straight path.\n4. Add.\n\n**Why:** grouping by direction makes double counting impossible.",
      "A square has both diagonals and both midlines drawn. How many straight lines are there?",
      "Horizontal 3, vertical 3, slanting 2. Total = **8**."),
    P("sl-p2", "Count lines of one direction only", "occasional",
      "The question asks only for horizontal, vertical or slanting lines.",
      "1. Pick the asked direction.\n2. Scan across the figure and tick each separate line in that direction.\n3. Pieces on one path that touch are one line.\n\n**Why:** the other directions do not matter; slow down only on the asked one.",
      "A 3 × 2 grid of cells also has both long diagonals of the whole rectangle drawn. How many vertical lines are there?",
      "A grid with 3 columns has 3 + 1 = **4** vertical lines. The diagonals are slanting, so they do not count."),
    P("sl-p3", "Stars, polygons and triangle grids", "common",
      "A star, a hexagon with diagonals, or a triangle filled with small triangles.",
      "1. Find the long straight paths that make the figure (a star's points are made by long lines).\n2. Count paths, not the small pieces between crossings.\n\n**Why:** each long line is cut into many pieces by the others; the pieces are not separate lines.",
      "How many straight lines are needed to draw a five-point star?",
      "Each point is formed by two long lines; there are 5 such lines in all. Answer **5**."),
    P("sl-p4", "Straight lines in a grid", "occasional",
      "A plain grid, sometimes with long diagonals drawn across it.",
      "1. Vertical lines = columns + 1.\n2. Horizontal lines = rows + 1.\n3. Add any diagonal paths, counting each long path once.\n\n**Why:** each grid line runs the full width or height.",
      "How many straight lines are there in a grid of 5 columns and 4 rows?",
      "Vertical 5 + 1 = 6, horizontal 4 + 1 = 5. Total = **11**.",
      formula=r"L=(m+1)+(n+1)"),
]

# ======================================================================= topic PYQ patterns
PYQS = [
    PYQ("Triangle with apex lines", "very common",
        "A triangle with several lines from the top corner to the base, sometimes with lines parallel to the base.",
        "Count the apex lines k and the parallel cuts h. Use (k+1)(k+2)/2 × (h+1). No need to count by eye.",
        "triangles", "A triangle has 4 lines from the apex to the base. How many triangles?",
        "(5 × 6)/2 = **15**."),
    PYQ("Square/rectangle with diagonals", "very common",
        "A square or rectangle with diagonals and midlines, or a row of such squares.",
        "Count by size: smallest pieces, then 2-piece triangles, then half-squares. Square with diagonals = 8; with midlines too = 16.",
        "triangles", "How many triangles are in a square with both diagonals?",
        "4 small + 4 half-squares = **8**."),
    PYQ("Triangle divided into rows", "common",
        "A big triangle made of small upright and upside-down triangles.",
        "Use 1, 5, 13, 27, 48 for 1 to 5 rows. Do not forget the upside-down triangles.",
        "triangles", "A triangle is split into 4 rows of small triangles. How many triangles?",
        "Standard value for 4 rows = **27**."),
    PYQ("Irregular composite figure", "common",
        "House shapes, pentagon with a star, two overlapping triangles, a triangle with medians.",
        "Label corners and crossings; count triangles part by part, then the ones crossing parts. Known values: medians 16, pentagon with diagonals 35.",
        "triangles", "How many triangles are formed when all three medians of a triangle are drawn?",
        "6 small + 3 two-piece + 6 half-triangles + 1 whole = **16**."),
    PYQ("Squares in a grid", "common",
        "A chessboard-style grid; count squares.",
        "Add (m−k+1)(n−k+1) for every size k. For n × n: 1² + … + n².",
        "squares-rectangles", "How many squares are there on a 5 × 5 grid?",
        "1 + 4 + 9 + 16 + 25 = **55**."),
    PYQ("Rectangles in a grid", "occasional",
        "A grid; count all rectangles, squares included.",
        "Choose 2 vertical and 2 horizontal lines: C(m+1,2) × C(n+1,2).",
        "squares-rectangles", "How many rectangles are there in a 3 × 3 grid?",
        "C(4,2) × C(4,2) = 6 × 6 = **36**."),
    PYQ("Tilted and irregular squares", "occasional",
        "A diamond drawn inside a square or grid, or cells arranged in a plus or L shape.",
        "Count upright squares first, then add each tilted square whose four sides are drawn. For irregular grids, check all four sides of each candidate.",
        "squares-rectangles", "A 2 × 2 grid has a diamond joining the middles of its outer sides. How many squares?",
        "4 + 1 upright + 1 tilted = **6**."),
    PYQ("Straight lines count", "occasional",
        "How many straight lines are there, or the least number of lines needed to draw a figure.",
        "Sweep direction by direction; pieces on one straight path count once. Pentagram = 5, grid = (m+1)+(n+1).",
        "straight-lines", "How many straight lines are there in a square with both diagonals?",
        "Horizontal 2 + vertical 2 + slanting 2 = **6**."),
]
