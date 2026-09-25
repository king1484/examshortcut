"""Notes, patterns and topic PYQ patterns for reasoning/embedded-figures.
Every claim used in the notes worked examples is re-checked by the lattice engine in
embedded-figures.py (see the NOTE_FACTS asserts there)."""
from _lib import P, PYQ

NOTES, PATTERNS = {}, {}

# ======================================================================= find-hidden
NOTES["find-hidden"] = r"""### What "embedded" means
One of the four option figures is hiding inside the given figure. It is drawn there with the **same strokes, same lengths and same directions**, just sitting among extra lines. Your job is to spot it. Two rules make this checkable: every stroke is one grid step long, and **rotation is not allowed**.

### Rotation is not allowed
The hidden copy must keep every stroke in its own direction: a horizontal stroke stays horizontal, a slant keeps its lean. So a figure flipped left-right (its **mirror image**), flipped top-bottom (its **water image**) or turned through 90 degrees or 180 degrees is a **different figure** and a wrong answer. Most wrong options are exactly these copies of the right answer, so direction checking settles most of the question.

### Anchor on a distinctive stroke
Do not compare whole figures. Pick the part's rarest stroke - usually a **slant**, or a stroke that forms a **T-joint** with two others. Find every place in the given figure where that anchor appears in the same direction; there are only a few. Each anchor spot is a candidate position. Around each candidate, check the remaining strokes of the part one by one, in order, sharing endpoints. If every stroke is found with matching direction, that is the answer; if even one stroke fails, drop that spot and move on.

### Compare strokes, not areas
Count first: if the part has 2 horizontal strokes, 1 vertical and 2 slants, the hidden copy must show exactly those five strokes in the same connected arrangement. A region of the figure can look "full" and still not contain the part, and a sparse-looking corner may hold it.

### Method in the exam
1. Count the part's strokes; note each direction.
2. Choose the rarest stroke as the anchor; locate it in the given figure.
3. At each anchor spot, trace the remaining strokes around it.
4. Reject options that are mirror images (a slant leaning the other way), water images (upside down) or turned copies - these need no tracing.
5. Between two surviving options, compare the strokes touching the anchor first.

### Worked example
Part: an L with a foot - one horizontal stroke, and two vertical strokes rising from its left end. In a 4 x 4 grid figure it sits one step right and one step down from the top-left, every stroke matching. Its left-right flipped version, whose foot points the other way, appears **nowhere** in the figure - the flipped L needs a horizontal on the other side of the corner, and no such pair of strokes exists there. So only the true L is embedded.

### Common mistakes
- Choosing a turned or mirrored copy because the silhouette looks right.
- Accepting an option where one stroke of the part is missing or re-angled.
- Checking only the first anchor spot when a second one also looks promising.
- Comparing sizes - all strokes in these figures are one grid step long, so size never decides.

### Quick revision
- Embedded = same strokes, same lengths, same directions, anywhere in the figure.
- Rotation is NOT allowed; mirror and water images are wrong answers.
- Anchor on the rarest stroke (a slant or a T-joint), then trace around it.
- Reject flips and turns first by direction; trace only what survives.
- One missing or re-angled stroke means the part is not there.
"""

PATTERNS["find-hidden"] = [
    P("fh-p1", "Hidden part in a square grid figure", "very common",
      "A 4 x 4 grid figure full of horizontal, vertical and slanting strokes; the options are small open figures.",
      "Anchor on the part's rarest stroke, locate it in the grid, and trace the remaining strokes around each anchor spot.",
      "**Q.** An open figure with 2 horizontals, 2 verticals and a slant is hidden in a 4 x 4 grid figure. Find it.",
      "Locate the slant, trace the box strokes around it; the flipped copy leans the other way and fails."),
    P("fh-p2", "Hidden part in an irregular figure", "common",
      "The given figure is not square (4 x 3) or its strokes stop early, so whole-figure matching misleads.",
      "Work stroke by stroke from the anchor; do not require the host figure to be a full grid.",
      "**Q.** A 4 x 3 figure hides a small open part; two options are flipped copies of it.",
      "Only the unflipped copy completes at its anchor spot; flips fail on the first re-angled stroke."),
    P("fh-p3", "Near-miss option figures", "common",
      "The options are not flips of each other - each differs from the part by a single stroke (missing, replaced or re-angled).",
      "Check each option's strokes against the part one at a time; then confirm the surviving option really appears in the figure.",
      "**Q.** Three options each differ from the part by one stroke; one matches exactly.",
      "Trace the exact-match option in the figure; the one-stroke-off options never complete."),
    P("fh-p4", "Slant-heavy parts", "occasional",
      "The part carries two or more slanting strokes, so direction errors are easy to make.",
      "Fix each slant's lean first (/ rises left-to-right, \\ falls left-to-right); only then check the straight strokes.",
      "**Q.** A part with two slants and one vertical is hidden in a busy grid figure.",
      "Match both slant leans at the anchor; flipped copies reverse at least one lean and fail."),
]

# ======================================================================= contains-part
NOTES["contains-part"] = r"""### The task
The question gives a **small part**; each option is a bigger figure. Exactly one option contains the part inside it, with the same strokes, lengths and directions, anywhere among extra filling lines. **Rotation is not allowed** - a turned copy of the part does not count.

### Check stroke by stroke
Write down the part's strokes with their directions, say 2 horizontal, 1 vertical and 1 slant. The correct option must show all of them, connected in the same way, just shifted. Sliding is allowed; turning is not. Extra strokes in the option are fine - the part only needs to be **present**, and filling lines never disqualify an option.

### Use anchors
A slant is rarer than a horizontal or vertical, so start there: check its lean (/ has its lower end on the left, \ has its lower end on the right), then find where it sits in the option. A **T-joint** - one stroke ending on the middle of another - is the second-best anchor. Parts often sit along an **edge or in a corner** of the correct option, so scan the border first when the part has a flat side.

### Near-miss figures
Most wrong options are built one stroke away from the part: one stroke **missing**, one slant **re-angled** (a / swapped for a \), or one stroke **replaced** (a horizontal where the part has a vertical). This is why a quick count is not enough - the wrong option has the same number of strokes as the part. Check the endpoints: each stroke must begin and end where the part's strokes begin and end, relative to each other.

### Method in the exam
1. Count and list the part's strokes with directions.
2. In each option, find the anchor stroke with the right lean.
3. Around it, check the remaining strokes in order, endpoint to endpoint.
4. Left with two finalists? Compare the strokes touching the anchor first; the difference is usually one re-angled slant.
5. Never reject an option for having extra lines.

### Worked example
Part: a horizontal stroke, a vertical stroke down from its left end, and a / slant from the horizontal's right end to the vertical's bottom. One option holds all three in its lower-left; another has the same box but the slant leans the other way (\ instead of /); a third has no vertical at all. Only the first option contains the part.

### Common mistakes
- Rejecting the correct option because of extra filling strokes.
- Accepting an option whose copy of the part is turned through 90 degrees.
- Counting strokes only - a one-stroke swap keeps the count but breaks the shape.
- Checking the slant's length but not its lean.

### Quick revision
- The part must appear complete: same strokes, same directions, only shifted.
- Extra filling strokes never disqualify an option.
- Anchor on slants and T-joints; scan edges and corners first.
- Wrong options are usually one stroke away: missing, re-angled or replaced.
- A / and a \ are different strokes; direction decides.
"""

PATTERNS["contains-part"] = [
    P("cp-p1", "Part among busy figures", "very common",
      "Four options of similar density, each full of short strokes.",
      "Anchor on the part's rarest stroke and trace; only one option completes all strokes.",
      "**Q.** A 4-stroke part must be found inside one of four busy 3 x 3 figures.",
      "Trace from the slant anchor; three options miss at least one stroke."),
    P("cp-p2", "One-stroke-difference options", "very common",
      "Every option has the same stroke count as the part but one stroke differs (missing, re-angled or replaced).",
      "Counting is not enough; check each stroke's direction and endpoints against the part.",
      "**Q.** Four options each have 5 strokes like the part; only one arranges them as the part does.",
      "The / vs \\ lean and one horizontal-vs-vertical swap separate the wrong three."),
    P("cp-p3", "Part along an edge or corner", "common",
      "The part has a flat side (two or more horizontal strokes), and options place it along a border.",
      "Scan the option's border first; the part usually sits against an edge, not in the middle.",
      "**Q.** The part's flat base sits on the lower-left corner of the correct option.",
      "Border scan finds the full part; the middle of the other options only shows part of it."),
    P("cp-p4", "Slant strokes as anchors", "common",
      "The part carries two or more slants; options differ in slant leans.",
      "Fix each slant's lean first, then check which straight strokes touch its ends.",
      "**Q.** A part with two slants of opposite lean hides in one of four options.",
      "Only one option shows both leans with the connecting strokes; the rest flip at least one slant."),
    P("cp-p5", "Two finalists", "common",
      "After the first pass two options survive; the filler strokes make them look equal.",
      "Compare the strokes touching the anchor first - the loser breaks one endpoint or re-angles one slant.",
      "**Q.** Two options both show a / slant with a horizontal at its foot; only one adds the part's vertical.",
      "The extra stroke at the slant's top decides; the loser is one stroke short."),
    P("cp-p6", "Sparse options", "occasional",
      "Options are lightly drawn (few filling strokes), so the part stands out.",
      "Still trace stroke by stroke - sparse options often drop exactly the stroke you assume is there.",
      "**Q.** Three sparse options each miss one stroke of the part; one is complete.",
      "Endpoint check finds the missing stroke in each wrong option."),
]

# ======================================================================= topic PYQ patterns
PYQS = [
    PYQ("Hidden part in a square grid figure", "very common",
        "A busy 4 x 4 grid of short strokes; four small option figures, most of them flips of one another.",
        "Anchor on the part's rarest stroke (a slant or T-joint), locate it in the figure, trace the rest; reject mirror and water images by direction.",
        "find-hidden",
        "**Q.** Which option figure is hidden in the given 4 x 4 figure?",
        "The unflipped option completes at its anchor spot; the mirror copy leans the other way and appears nowhere."),
    PYQ("Hidden part in an irregular figure", "common",
        "The host figure is 4 x 3 or has strokes missing, so overall shape matching misleads.",
        "Work stroke by stroke from the anchor; do not expect a full grid.",
        "find-hidden",
        "**Q.** Which option is embedded in the 4 x 3 figure?",
        "Only the true part completes; its flipped copies fail on the first re-angled stroke."),
    PYQ("Near-miss options (flips and turns)", "very common",
        "Options are the same figure shown as mirror image, water image and turned copies.",
        "Direction of every stroke decides: horizontal stays horizontal, a / never becomes a \\.",
        "find-hidden",
        "**Q.** Which of the four similar options is actually inside the figure?",
        "The copy with all stroke directions preserved; every flip or turn breaks at least one stroke's direction."),
    PYQ("Trace the part stroke by stroke", "occasional",
        "The part has five or more strokes and the figure is dense.",
        "Count the part's strokes, anchor on the rarest one, and tick off the remaining strokes in order around each anchor spot.",
        "find-hidden",
        "**Q.** A 6-stroke part hides in a dense grid figure.",
        "The anchor spot where all six strokes complete is the answer."),
    PYQ("Which option contains the part", "very common",
        "A small part figure is given; four larger figures are the options.",
        "Anchor on the part's slant or T-joint, then trace the remaining strokes endpoint to endpoint; extra filling strokes are fine.",
        "contains-part",
        "**Q.** In which option is the given part embedded?",
        "The option holding every stroke with matching directions; the others miss or re-angle at least one stroke."),
    PYQ("Part along an edge or corner", "common",
        "The part has a flat run of horizontal or vertical strokes.",
        "Scan the borders of the options first; parts with a flat side usually sit against an edge.",
        "contains-part",
        "**Q.** Where is the flat-based part embedded?",
        "Against the border of the correct option; the other options carry only fragments of it."),
    PYQ("One-stroke difference", "common",
        "Wrong options match the part's stroke count but break one stroke.",
        "Check direction and endpoints of every stroke; a count alone cannot separate the options.",
        "contains-part",
        "**Q.** Which option truly contains the part?",
        "The one with no missing, replaced or re-angled stroke."),
]
