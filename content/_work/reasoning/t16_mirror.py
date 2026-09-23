# build mirror-water-image topic (topic 16)
from fractions import Fraction as Fr
import common as C
from engines import string_image_svg, seg_svg, PL, circ, svg, line, num

# letters that look unchanged under each flip (standard exam convention, block capitals)
SYM_V = set('AHIMOTUVWXY08')      # left-right symmetric -> unchanged in a vertical mirror
SYM_H = set('BCDEHIKOX038')       # top-bottom symmetric -> unchanged in water
ROT = set('HINOSXZ08')            # unchanged by a half-turn

MIRROR, WATER = (True, True, False), (False, False, True)


def sig(s, rev, hf, vf):
    chars = list(reversed(s)) if rev else list(s)
    out = []
    for c in chars:
        h, v = hf, vf
        if h and v and c in ROT:
            h = v = False
        if h and c in SYM_V:
            h = False
        if v and c in SYM_H:
            v = False
        out.append((c, h, v))
    return tuple(out)


def str_q(id, s, kind, sol, sc, d, pat, t=40, place=None):
    """kind 'mirror' or 'water'. Options are 4 transforms, verified visually distinct."""
    if kind == 'mirror':
        trs = [MIRROR, WATER, (True, False, False), (False, True, False)]
    else:
        trs = [WATER, MIRROR, (True, False, True), (True, True, True)]
    sigs = [sig(s, *tr) for tr in trs]
    assert len(set(sigs)) == 4, (id, 'options not visually distinct')
    opts = [string_image_svg(s, *tr) for tr in trs]
    where = 'placed vertically on the right side' if kind == 'mirror' else 'placed horizontally below it (water image)'
    q = "Which option shows the correct **%s image** of **%s** when the mirror is %s?" % (
        'mirror' if kind == 'mirror' else 'water', s, where)
    return C.Q(id, q, opts, opts[0], sol, sc=sc, d=d, sub='mirror-image' if kind == 'mirror' else 'water-image',
               pat=pat, t=t, place=place)


def clock_mirror(h, m):
    am = Fr(6 * m)
    ah = Fr(30 * (h % 12)) + Fr(m, 2)
    am2, ah2 = (360 - am) % 360, (360 - ah) % 360
    m2 = am2 / 6
    h2 = (ah2 - m2 / 2) / 30
    assert m2.denominator == 1 and h2.denominator == 1
    return int(h2) % 12 or 12, int(m2)


def fmt(h, m):
    return '%d:%02d' % (h, m)


def eleven60(h, m):
    tot = 11 * 60 + 60 - (h % 12) * 60 - m
    tot %= 720
    hh, mm = divmod(tot, 60)
    return hh or 12, mm


for h in range(1, 13):
    for m in range(60):
        assert clock_mirror(h, m) == eleven60(h, m)


# ---------------------------------------------------------------- figure transforms
def tf(segs, kind, W, H):
    f = {'orig': lambda x, y: (x, y), 'mirror': lambda x, y: (W - x, y),
         'water': lambda x, y: (x, H - y), 'rot': lambda x, y: (W - x, H - y)}[kind]
    return [(f(*a), f(*b)) for a, b in segs]


def canon(segs):
    return frozenset(tuple(sorted([tuple(map(Fr, a)), tuple(map(Fr, b))])) for a, b in segs)


def fig_svg(segs, W, H):
    # draw inside a fixed frame so every option has the same bounding box
    frame = [((0, 0), (0, 0))]
    body = ''.join(line(a[0] * 8 + 5, a[1] * 8 + 5, b[0] * 8 + 5, b[1] * 8 + 5) for a, b in segs)
    return svg(num(W * 8 + 10), num(H * 8 + 10), body)


FLAG = PL((1, 8), (1, 0), (5, 1.5), (1, 3)) + [((0, 8), (3, 8))]          # W=5, H=8
BOOT = PL((0, 0), (0, 6), (5, 6), (5, 4), (2, 4), (2, 0)) + [((0, 2), (2, 2))]  # W=5, H=6


def fig_q(id, segs, W, H, kind, sol, sc, d, place=None):
    kinds = [kind] + [k for k in ('mirror', 'water', 'rot', 'orig') if k != kind][:3]
    cs = [canon(tf(segs, k, W, H)) for k in kinds]
    assert len(set(cs)) == 4, (id, 'figure options coincide')
    opts = [fig_svg(tf(segs, k, W, H), W, H) for k in kinds]
    q = ("Which option is the correct **mirror image** of the given figure when the mirror is placed vertically to its right?"
         if kind == 'mirror' else
         "Which option is the correct **water image** of the given figure?")
    return C.Q(id, q, opts, opts[0], sol, sc=sc, d=d, sub='mirror-image' if kind == 'mirror' else 'water-image',
               pat='figure mirror / water image', t=35, fig=fig_svg(segs, W, H), place=place)


subs = []

subs.append(C.sub(
    'mirror-image', 'Mirror images (vertical mirror)',
    "A mirror placed **vertically** (to the left or right of the object — the result is the same) swaps **left and right** but keeps **top and bottom**. For a word or number this does two things at once:\n\n"
    "1. the **order** of characters is reversed (the last character appears first), and\n"
    "2. **each character is flipped** left-to-right (R faces the other way, 4 turns round).\n\n"
    "Letters with a vertical axis of symmetry — **A H I M O T U V W X Y** — look unchanged when flipped, so they are the fastest check points; asymmetric ones like **B C D E F G J K L N P Q R S Z** and digits **2 3 4 5 6 7 9** decide between options.",
    tricks=[
        C.T(
            'Check the end characters first',
            "In a vertical-mirror image the last character of the original stands first, flipped. Eliminate options by looking only at the first and last characters.",
            "**Q.** Mirror image of PEN7?\n\n**Sol.** The image starts with a flipped 7 and ends with a flipped P. Any option starting with a normal P (order not reversed) or a normal 7 (not flipped) is wrong.",
            "Reversed order + flipped characters — test both on one end."),
        C.T(
            'Symmetric-letter shortcut',
            "A word made only of A H I M O T U V W X Y that reads the same backwards (a palindrome, e.g. TOOT, WOW) looks identical in a vertical mirror.",
            "**Q.** Does MOM look the same in a vertical mirror?\n\n**Sol.** M, O are symmetric and MOM is a palindrome → yes.",
            "Symmetric letters + palindrome → unchanged."),
    ],
    mistakes=[
        "Flipping each letter but keeping the original order.",
        "Reversing the order but not flipping the asymmetric letters.",
        "Confusing the mirror image with the water image (top-bottom flip).",
    ]))

subs.append(C.sub(
    'water-image', 'Water images (horizontal mirror)',
    "A water surface acts as a **horizontal** mirror below the object: it swaps **top and bottom** and keeps **left and right**. So in a water image:\n\n"
    "- the **order** of characters stays the same, and\n"
    "- each character is turned **upside down** (flipped top-to-bottom, not rotated).\n\n"
    "Letters with a horizontal axis of symmetry — **B C D E H I K O X** (and digits 0, 3, 8) — look unchanged in water. A word made only of these letters (CHOICE, CODE, HIDE, BOX) looks identical in water.\n\n"
    "A mirror image followed by a water image is the same as a **half-turn (180° rotation)**.",
    tricks=[
        C.T(
            'Order stays, letters go upside down',
            "Scan the options for the one that keeps the original order and has only asymmetric letters turned upside down.",
            "**Q.** Water image of BOX?\n\n**Sol.** B, O, X are all top-bottom symmetric, and water keeps the order → BOX looks unchanged.",
            "Water image: same order, top-bottom flip."),
    ],
    mistakes=[
        "Reversing the character order in a water image.",
        "Rotating letters by 180° instead of flipping them top-to-bottom.",
    ]))

subs.append(C.sub(
    'clock-mirror', 'Mirror image of a clock',
    "When a clock is seen in a vertical mirror, both hands swap sides of the 12–6 line. The time shown by the image and the actual time always **add up to 12:00** (on a 12-hour clock).\n\n"
    "So: **image time = 11:60 − actual time** (and actual = 11:60 − image, the same rule both ways). Writing 12:00 as 11:60 avoids borrowing.\n\n"
    "Exception: if the actual time is 12:00 or 6:00, the image shows the same time. For times between 12:00 and 1:00 (like 12:20), use 23:60 − time (answer 11:40).\n\n"
    "Water images of clocks usually put the hour hand in a position that no real time matches, so exams mostly ask about mirror images.",
    formulas=[
        C.F('Mirror time', 'T_{\\text{image}} = 11{:}60 - T_{\\text{actual}}', 'Works in both directions; for 12:xx use 23:60 − T.'),
    ],
    tricks=[
        C.T(
            '11:60 rule',
            "Subtract the time from 11:60 digit-group-wise: hours from 11, minutes from 60.",
            "**Q.** A clock shows 4:20. What does its mirror image show?\n\n**Sol.** 11:60 − 4:20 = **7:40**.",
            "Mirror time + actual time = 12:00."),
    ],
    mistakes=[
        "Subtracting from 12:00 and mis-borrowing the minutes.",
        "Applying the rule to 12:xx without adding 12 first.",
    ]))

patterns = [
    C.P('Mirror image of word / number', 'very common',
        "A word, code or number with four image options.",
        "Reversed order + each letter flipped; check first and last characters."),
    C.P('Water image of word / number', 'common',
        "Same, with the mirror below (water).",
        "Order unchanged; asymmetric letters upside down."),
    C.P('Clock mirror time', 'common',
        "Time seen in a mirror, or actual time from a mirror reading.",
        "11:60 − time."),
    C.P('Symmetric letters count', 'occasional',
        "How many letters of a word look the same in a mirror / in water.",
        "Match against A H I M O T U V W X Y (mirror) or B C D E H I K O X (water)."),
    C.P('Figure mirror / water image', 'common',
        "A line figure with four image options.",
        "Track one asymmetric feature (a flag, a notch) to its reflected position."),
    C.P('Identical image words', 'occasional',
        "Which word looks exactly the same in the mirror / in water.",
        "Mirror: symmetric letters + palindrome. Water: all letters top-bottom symmetric."),
]

examples = []

examples.append(str_q(
    'rsn-mirror-ex1', 'PLANK', 'mirror',
    "A vertical mirror reverses the order and flips every letter left-to-right. So the image reads K N A L P from left to right, with K, N, L, P facing the other way (A is symmetric and looks the same). The option with reversed order **and** flipped letters is correct; the others show the water image, only a reversed order, or only flipped letters.",
    "Look at the first character: it must be a flipped K.", 'easy', 'mirror image of word / number'))

h, m = 4, 20
ih, im = clock_mirror(h, m)
assert (ih, im) == (7, 40)
examples.append(C.Q(
    'rsn-mirror-ex2', "A clock shows the time **4:20**. What time does its mirror image show?",
    [fmt(ih, im), '8:40', '7:20', '8:20'], fmt(ih, im),
    "Mirror time = 11:60 − 4:20 = **7:40**. Check: 4:20 + 7:40 = 12:00.",
    sc="11:60 − 4:20.", d='easy', sub='clock-mirror', pat='clock mirror time', t=30))

examples.append(str_q(
    'rsn-mirror-ex3', 'GR8547', 'water',
    "A water image keeps the order G R 8 5 4 7 and turns each character upside down. 8 is top-bottom symmetric and stays the same; G, R, 5, 4, 7 appear upside down. The option with the original order and upside-down characters is correct.",
    "Water: order unchanged, characters flipped top-to-bottom.", 'medium', 'water image of word / number'))

word = 'MATHEMATICS'
cnt = sum(c in SYM_V for c in word)
assert cnt == 8
examples.append(C.Q(
    'rsn-mirror-ex4', "How many letters of the word **MATHEMATICS** look exactly the same in a vertical mirror (considered one by one)?",
    [str(cnt), '7', '9', '6'], str(cnt),
    "Left-right symmetric capitals: A H I M O T U V W X Y. In M A T H E M A T I C S, the symmetric ones are M, A, T, H, M, A, T, I = **8**; E, C, S are not.",
    sc="Tick letters from AHIMOTUVWXY.", d='easy', sub='mirror-image', pat='symmetric letters count', t=35))

# ---------------------------------------------------------------- practice
pr = []

pr.append(str_q(
    'rsn-mirror-1', 'REASON', 'mirror',
    "Mirror image = reversed order N O S A E R, each letter flipped left-to-right. O and A are symmetric; N, S, E, R appear reversed. Only one option has both the reversed order and the flipped letters.",
    "First character must be a flipped N.", 'easy', 'mirror image of word / number', t=35))

pr.append(str_q(
    'rsn-mirror-2', 'FLIGHT27', 'mirror',
    "Reverse the order (7 2 T H G I L F) and flip each character left-to-right. T, H, I are symmetric; 7, 2, G, L, F face the other way. The correct option shows a flipped 7 first and a flipped F last.",
    "Check both ends: flipped 7 … flipped F.", 'medium', 'mirror image of word / number', t=40))

pr.append(str_q(
    'rsn-mirror-3', 'BUDGET', 'water',
    "Water image: same order B U D G E T, each letter upside down. B, D, E are top-bottom symmetric and look unchanged; U, G, T appear upside down. The option keeping the order with U, G, T inverted is correct.",
    "Order unchanged; only U, G, T visibly change.", 'medium', 'water image of word / number', t=40))

pr.append(str_q(
    'rsn-mirror-4', '4R95JQ', 'water',
    "Keep the order 4 R 9 5 J Q and turn every character upside down; none of these is top-bottom symmetric, so all six change. The option with the same order and inverted characters is correct; the half-turned option (order reversed as well) is the classic trap.",
    "Water never changes the order.", 'hard', 'water image of word / number', t=45))

pr.append(str_q(
    'rsn-mirror-5', 'EXAM25', 'mirror',
    "Reverse the order (5 2 M A X E) and flip each character left-to-right. M, A, X are symmetric; 5, 2 and E face the other way. Only one option has both features.",
    "The image starts with a flipped 5.", 'easy', 'mirror image of word / number', t=35, place=2))

for i, (h, m, dists, d) in enumerate([(3, 45, ['9:15', '8:45', '9:45'], 'easy'),
                                      (10, 10, ['2:50', '1:10', '2:10'], 'easy'),
                                      (6, 35, ['6:25', '5:35', '6:35'], 'medium')], start=6):
    ih, im = clock_mirror(h, m)
    ans = fmt(ih, im)
    pr.append(C.Q(
        'rsn-mirror-%d' % i, "A wall clock shows **%s**. What time will its mirror image show?" % fmt(h, m),
        [ans] + dists, ans,
        "Mirror time = 11:60 − %s = **%s**. Check: %s + %s = 12:00." % (fmt(h, m), ans, fmt(h, m), ans),
        sc="11:60 − time.", d=d, sub='clock-mirror', pat='clock mirror time', t=30))

# reverse direction: actual time from image
ih, im = 2, 25
ah, am = clock_mirror(ih, im)
assert clock_mirror(ah, am) == (ih, im) and (ah, am) == (9, 35)
pr.append(C.Q(
    'rsn-mirror-9', "Seen in a mirror, a clock appears to show **2:25**. What is the actual time?",
    [fmt(ah, am), '10:35', '9:25', '10:25'], fmt(ah, am),
    "The rule works both ways: actual = 11:60 − 2:25 = **9:35**. Check: mirror of 9:35 = 11:60 − 9:35 = 2:25.",
    sc="Same 11:60 rule in reverse.", d='medium', sub='clock-mirror', pat='clock mirror time', t=35))

ih, im = clock_mirror(12, 20)
assert (ih, im) == (11, 40)
pr.append(C.Q(
    'rsn-mirror-10', "A clock shows **12:20**. What time does its mirror image show?",
    ['11:40', '12:40', '11:20', '12:20'], '11:40',
    "For 12:xx times use 23:60: 23:60 − 12:20 = 11:40. Check: 12:20 + 11:40 = 24:00, i.e. the hands mirror across the 12–6 line → **11:40**.",
    sc="12:xx → subtract from 23:60.", d='hard', sub='clock-mirror', pat='clock mirror time', t=45))

words = ['WOW', 'NOON', 'DEED', 'BOB']
same = [w for w in words if w == w[::-1] and all(c in SYM_V for c in w)]
assert same == ['WOW']
pr.append(C.Q(
    'rsn-mirror-11', "Which of the following words will look **exactly the same** in a vertical mirror?",
    words, 'WOW',
    "A word looks unchanged in a vertical mirror only if (i) it reads the same backwards and (ii) every letter is left-right symmetric (A H I M O T U V W X Y). All four are palindromes, but N, D and B are not left-right symmetric. Only **WOW** passes both tests.",
    sc="Palindrome + only AHIMOTUVWXY letters.", d='medium', sub='mirror-image', pat='identical image words', t=40))

words = ['CHOICE', 'BRIDGE', 'CHANCE', 'EXPECT']
same = [w for w in words if all(c in SYM_H for c in w)]
assert same == ['CHOICE']
pr.append(C.Q(
    'rsn-mirror-12', "Which of the following words will look **exactly the same** in its water image?",
    words, 'CHOICE',
    "Water keeps the order, so a word is unchanged only if every letter is top-bottom symmetric (B C D E H I K O X). CHOICE = C, H, O, I, C, E — all symmetric. BRIDGE has R and G, CHANCE has A and N, EXPECT has P and T. Answer: **CHOICE**.",
    sc="Every letter must be in BCDEHIKOX.", d='medium', sub='water-image', pat='identical image words', t=40, place=3))

word = 'BACKGROUND'
cnt = sum(c in SYM_H for c in word)
assert cnt == 5, cnt
pr.append(C.Q(
    'rsn-mirror-13', "How many letters of the word **BACKGROUND** look exactly the same in a water image (considered one by one)?",
    [str(cnt), '4', '6', '3'], str(cnt),
    "Top-bottom symmetric capitals: B C D E H I K O X. Letter by letter in B A C K G R O U N D: B ✓, A ✗, C ✓, K ✓, G ✗, R ✗, O ✓, U ✗, N ✗, D ✓ → **5**.",
    sc="Tick letters from BCDEHIKOX.", d='easy', sub='water-image', pat='symmetric letters count', t=35))

pr.append(fig_q(
    'rsn-mirror-14', FLAG, 5, 8, 'mirror',
    "A vertical mirror swaps left and right only. The flag, which points to the right of the pole, will point to the **left** in the image, and it stays at the **top**; the foot line (which extends to the right of the pole) moves to the left side. The option showing a left-pointing flag at the top is correct — a flag at the bottom is the water image, and a flag at the bottom pointing left is the half-turn.",
    "Left-right swaps; top stays top.", 'easy'))

pr.append(fig_q(
    'rsn-mirror-15', BOOT, 5, 6, 'water',
    "A water image swaps top and bottom only. The boot's toe (the wide part) is at the bottom-right in the figure; in water it moves to the **top-right**, and the shaft with its strap line now hangs downward on the left. Left and right do not change, so the toe must still be on the right. The option with the toe at the top-right is correct.",
    "Top-bottom swaps; left-right stays.", 'medium', place=0))

assert len(pr) == 15

t = C.topic(
    'mirror-water-image', 'Mirror & Water Images', 'medium', {'tier1': '0-1', 'tier2': '1-2'},
    "A vertical mirror reverses left-right (character order reversed and every character flipped); water reverses top-bottom (order kept, characters upside down). Know the symmetric letters for each (AHIMOTUVWXY for mirrors, BCDEHIKOX for water), use 11:60 − time for clock mirrors, and track one asymmetric feature in figure questions.",
    subs, patterns, examples, pr)
C.write_topic(t)
print('OK mirror-water-image')
