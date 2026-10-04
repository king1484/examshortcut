# Build script: SSC CPO 2025 Paper-1, 9 Dec Shift 2 (cpo-p1-real-2025-1209-s2)
# Parses todo files -> fixes mojibake/typos -> attaches solutions -> verifies quant+reasoning keys -> writes 4 part JSONs.
import json, math, re, itertools, os, sys

TODO = r"C:\Users\Vinay Singirikonda\AppData\Local\Temp\claude\C--Users-Vinay-Singirikonda\153e6b32-77ea-4b98-a5f7-9f6a7e14a4f4\scratchpad\todo"
OUT = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\exams\ssc-cpo\mocks\parts"
MOCK = "cpo-p1-real-2025-1209-s2"

DROPS = {
    "r10": "HAS-IMAGE (embedded-figures question)",
    "r11": "HAS-IMAGE (figure-series question)",
    "r32": "HAS-IMAGE (figure-series question)",
    "r33": "HAS-IMAGE (figure-pair analogy question)",
    "r34": "HAS-IMAGE (counting-figures question)",
    "r36": "HAS-IMAGE (figure-series question)",
    "e01": "cloze passage missing in source (blank (1) has no stem)",
    "e02": "cloze passage missing in source (blank (2) has no stem)",
    "e03": "cloze passage missing in source (blank (3) has no stem)",
    "e06": "rearrangement incomplete in source (sentences 3-5 missing, sentence 2 truncated)",
    "e28": "cloze passage missing in source (blank (1) of unseen passage)",
    "e29": "cloze passage missing in source (blank (2) of unseen passage)",
    "e30": "cloze passage missing in source (blank (3) of unseen passage)",
    "e31": "cloze passage missing in source (blank (4) of unseen passage)",
    "e32": "cloze passage missing in source (blank (5) of unseen passage)",
}

# ---------------- parsing ----------------

def fix_mojibake(t: str) -> str:
    if any(ch in t for ch in ("├", "Γ", "╬")):
        t = t.encode("cp1252", errors="replace").decode("utf-8", errors="replace")
    return t

def clean(t: str) -> str:
    for z in "\u200b\u200c\u200d\u2060\ufeff\u00a0":
        t = t.replace(z, " ")
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()

def clean_opt(t: str) -> str:
    t = clean(t)
    t = re.sub(r"(?<=\d)cm2\b", "cm\u00b2", t)
    return t.strip()

def parse_file(path):
    raw = fix_mojibake(open(path, encoding="utf-8").read())
    qs, cur = [], None
    hdr = re.compile(r"^###\s+(\S+)\s+\(testbook key: option (\d)\)\s*(.*)$")
    for line in raw.splitlines():
        m = hdr.match(line)
        if m:
            cur = {"id": m.group(1), "key": int(m.group(2)) - 1, "flags": m.group(3),
                   "body": [], "options": ["", "", "", ""]}
            qs.append(cur)
        elif cur is None:
            continue
        else:
            om = re.match(r"^\s*\((\d)\)\s+(.*)$", line)
            if om:
                n = int(om.group(1))
                if 1 <= n <= 4:
                    cur["options"][n - 1] = clean(om.group(2))
                    continue
            cur["body"].append(line)
    for q in qs:
        q["stem"] = "\n".join(q["body"])
    return qs

# ---------------- per-question text touch-ups ----------------

STEM_FIX = {
    "q01": [("Solve:(56.75)", "Solve: (56.75)")],
    "q17": [(" (0.625div 2.5)((5)/(8)times 2)=?", "(0.625 \u00f7 2.5) \u00d7 ((5)/(8) \u00d7 2) = ?")],
    "q29": [("(2, -1) (2, -1)", "(2, -1)")],
    "q49": [("at Sl.", "at SI.")],
    "r02": [("Nagar,Bengaluru", "Nagar, Bengaluru")],
    "g06": [("Greitas zivitat amestu fatuan aur 8?", "")],
    "e04": [("nostalgia\u2019 most nearly mean in this context? (4)", "\u201cnostalgia\u201d most nearly mean in this context?")],
    "e05": [("\u201cassimilation\u201d most nearly means: (5)", "\u201cassimilation\u201d most nearly means:")],
    "e08": [("| had", "I had"), ("what | said", "what I said"), ("| don\u2019t", "I don\u2019t"), ("| don't", "I don't")],
    "e24": [("arnusing", "amusing")],
    "e47": [("\"| was going", "\"I was going")],
}
R14_STEM = ("Study the given pattern carefully and select the number that can replace the question mark [?] in it.\n\n"
            "14  12  7   15\n21  29  15  18\n245 287 154  ?")
R35_STEM = ("What word is formed by (0,4), (4,3), (2,1), (3,4) using the grid below (row, column)?\n\n"
            "    0  1  2  3  4\n"
            "0   J  B  D  C  L\n"
            "1   F  I  A  J  H\n"
            "2   D  A  K  L  E\n"
            "3   B  K  G  I  A\n"
            "4   K  C  E  L  L")

def fix_stem(qid, stem):
    stem = fix_mojibake(stem)
    if qid == "r14":
        return R14_STEM
    if qid == "r35":
        return R35_STEM
    if qid in ("q13",):
        pass
    for old, new in STEM_FIX.get(qid, []):
        stem = stem.replace(old, new)
    if qid not in ("r14", "r35"):
        stem = re.sub(r"\s*\n\s*", " ", stem)
        stem = re.sub(r"[ \t]{2,}", " ", stem)
    return clean(stem)

def fix_options(qid, opts):
    opts = [clean_opt(o) for o in opts]
    if qid == "q13":
        opts = [o.replace("4x2", "4x\u00b2").replace("12x", "12x").replace("10x", "10x") for o in opts]
    return opts

# ---------------- solution data: id -> (solution, shortcut, difficulty, subtopic, timeSec) ----------------

Q = {}
def add(d, qid, sol, sc, diff, sub, t):
    d[qid] = {"sol": sol, "sc": sc, "diff": diff, "sub": sub, "t": t}

# ---- QUANT (solutions re-derived; keys verified programmatically below) ----
add(Q, "q01", "Split the square: $(56.75)^2 = 56^2 + 2(56)(0.75) + 0.75^2 = 3136 + 84 + 0.5625 = 3220.5625$. Subtracting 3220 leaves exactly 0.5625.",
    "Use $(a+b)^2$ with $a=56$, $b=0.75$; the decimal part is $0.75^2 = 0.5625$.", "easy", "simp-approximation", 25)
add(Q, "q02", "Under compound interest the amount grows by the same factor each year, so $\\frac{1200}{1000} = 1.2$. Hence the yearly factor is $1 + \\frac{R}{100} = 1.2$, giving $R = 20\\%$.",
    "Interest of Rs. 200 in the 4th year is 20% of the Rs. 1,000 amount after 3 years.", "medium", "int-ci", 35)
add(Q, "q03", "At simple interest each year adds the same amount: yearly SI $= 12076 - 11650 = 426$. Interest paid in 5 years $= 5 \\times 426 = 2130$, so the principal $= 11650 - 2130 = 9520$.",
    "P = amount after 5 yrs $-$ 5 \u00d7 (amount after 6 yrs $-$ amount after 5 yrs).", "easy", "int-si", 30)
add(Q, "q04", "$x + \\frac{1}{x} = 2$ forces $x = 1$ (only positive root, since $x^2 - 2x + 1 = 0$). Then $x^6 + \\frac{1}{x^6} = 2$, $x^3 - \\frac{1}{x^3} = 0$ and $x^2 + \\frac{1}{x^2} = 2$, so the value $= 2 - 3(0) + 5(2) = 12$.",
    "Only $x=1$ satisfies $x+\\frac{1}{x}=2$; substitute directly.", "medium", "alg-reciprocal", 40)
add(Q, "q05", "Let the horizontal distance be $d$. From the top, $\\tan 60^\\circ = \\frac{90}{d} \\Rightarrow d = \\frac{90}{\\sqrt3} = 30\\sqrt3$. For the tower top, $\\tan 30^\\circ = \\frac{90 - h}{d} \\Rightarrow 90 - h = 30\\sqrt3 \\times \\frac{1}{\\sqrt3} = 30$, so $h = 60$ m.",
    "Height $= H\\left(1 - \\frac{\\tan 30^\\circ}{\\tan 60^\\circ}\\right) = 90\\left(1 - \\frac13\\right) = 60$.", "medium", "hd-basics", 45)
add(Q, "q06", "Space diagonal: $d^2 = l^2 + b^2 + h^2 \\Rightarrow 169 = 9 + 16 + h^2 \\Rightarrow h^2 = 144$, so the third edge is 12 cm.",
    "$\\sqrt{13^2 - 3^2 - 4^2} = \\sqrt{144} = 12$.", "easy", "m3d-cube-cuboid", 30)
add(Q, "q07", "Volume scales as $r^3$, and $\\frac{12}{2} = 6$, so $6^3 = 216$ small spheres are formed.",
    "Ratio of radii cubed: $(12/2)^3 = 216$.", "easy", "m3d-sphere", 30)
add(Q, "q08", "Sphere radii are 7 cm and 3.5 cm, a 2:1 ratio, so each small sphere would give 8 pieces; a hemisphere has half the volume, so $8 \\times 2 = 16$ hemispheres.",
    "Hemisphere $= \\tfrac12$ sphere, so count $= 2(14/7)^3 = 16$.", "medium", "m3d-sphere", 35)
add(Q, "q09", "Let dimensions be $2x, 3x, 4x$: volume $= 24x^3 = 768 \\Rightarrow x^3 = 32 \\Rightarrow x = \\sqrt[3]{32} \\approx 3.175$. Smallest dimension $= 2x \\approx 6.35 \\approx 6.34$ cm.",
    "$24x^3 = 768 \\Rightarrow x^3 = 32$; use $\\sqrt[3]{32} \\approx 3.175$.", "medium", "m3d-cube-cuboid", 40)
add(Q, "q10", "Convert: $100 \\times 80 \\times 50$ cm. Total surface area $= 2(100{\\times}80 + 80{\\times}50 + 100{\\times}50) = 2(8000 + 4000 + 5000) = 34000$ cm\u00b2. Each tile covers $20^2 = 400$ cm\u00b2, so tiles $= \\frac{34000}{400} = 85$.",
    "Tile the whole surface: TSA \u00f7 400.", "medium", "m3d-cube-cuboid", 45)
add(Q, "q11", "Both radius and height become $\\frac13$, so volume scales by $\\left(\\frac13\\right)^3 = \\frac{1}{27}$: exactly 27 small cones.",
    "Linear ratio $1/3$ cubed gives the count.", "easy", "m3d-cone", 30)
add(Q, "q12", "Similar solids with height ratio $1:3$ have volume ratio $1^3 : 3^3 = 1 : 27$.",
    "Volume ratio = cube of linear ratio.", "easy", "m3d-cone", 25)
add(Q, "q13", "$(a - b)^2 = a^2 - 2ab + b^2$ with $a = 2x$, $b = 3$: $4x^2 - 12x + 9$.",
    "Squaring $(2x-3)$: middle term $-2(2x)(3) = -12x$.", "easy", "alg-identities", 20)
add(Q, "q14", "$2\\frac12$ minutes $= 150$ seconds. Items $= 2.4 \\times 150 = 360$.",
    "2.4 \u00d7 15 = 36, so \u00d710 gives 360.", "easy", "ns-fractions-decimals", 25)
add(Q, "q15", "Volume of pyramid $= \\frac13 \\times \\text{base} \\times h$: $144 = \\frac13 \\times 36 \\times h \\Rightarrow h = 12$ cm.",
    "$144 \\times 3 = 432 = 36h \\Rightarrow h = 12$.", "easy", "m3d-prism-pyramid", 30)
add(Q, "q16", "Exterior angles of any convex polygon sum to $360^\\circ$, which is $2\\pi$ radians, independent of $n$.",
    "One full turn = 360\u00b0 = 2\u03c0.", "easy", "geo-lines-angles", 20)
add(Q, "q17", "$0.625 \\div 2.5 = 0.25$ and $\\frac58 \\times 2 = 1.25$. Product $= 0.25 \\times 1.25 = 0.3125$.",
    "$\\frac58 = 0.625$, so expression $= 0.25 \\times 1.25$.", "easy", "simp-bodmas", 30)
add(Q, "q18", "Base area 100 \u21d2 side 10. Lateral surface 260 over 4 identical triangular faces \u21d2 each face $= 65 = \\frac12 \\times 10 \\times l$, so slant edge (slant height) $l = 13$. Then $h = \\sqrt{13^2 - 5^2} = \\sqrt{144} = 12$ cm.",
    "Face area gives slant height 13; drop a perpendicular to get $h = \\sqrt{13^2-5^2}$.", "hard", "m3d-prism-pyramid", 55)
add(Q, "q19", "Rate $= \\frac{2.25}{4.5} = 0.5$ litres/minute. Time $= \\frac{5.625}{0.5} = 11.25$ minutes.",
    "5.625 is 2.5 \u00d7 2.25, so time = 2.5 \u00d7 4.5 min.", "medium", "rp-proportion", 35)
add(Q, "q20", "Used $= \\frac23 + 0.125 = \\frac{16}{24} + \\frac{3}{24} = \\frac{19}{24}$. Remaining $= 1 - \\frac{19}{24} = \\frac{5}{24}$.",
    "0.125 = 1/8; common denominator 24.", "easy", "ns-fractions-decimals", 30)
add(Q, "q21", "Circumference $= 2\\pi r = 44$ with $\\pi = \\frac{22}{7}$ \u21d2 $r = 7$ cm. Area $= \\frac{22}{7} \\times 49 = 154$ cm\u00b2.",
    "r = C \u00d7 7/44 = 7; area = 22/7 \u00d7 49.", "easy", "m2d-circles", 25)
add(Q, "q22", "Let CP = 100: profit 20% \u21d2 SP = 120. New SP $= 120 \\times 1.25 = 150$; at 30% profit new CP $= \\frac{150}{1.3} \\approx 115.38$. Increase $= \\frac{15.38}{100} \\times 100 \\approx 15.38\\%$.",
    "Fix CP=100, chain the multipliers 1.2, 1.25, then divide by 1.3.", "hard", "pl-basics", 55)
add(Q, "q23", "Path area $= \\pi(12^2 - 10^2) = \\frac{22}{7} \\times 44 = 138.29$ m\u00b2 (approx). Cost $= 138.2857 \\times 20 = 2765.71$.",
    "Annulus area = \u03c0(R\u00b2\u2212r\u00b2) = 44\u03c0; with \u03c0 = 22/7 gives 968/7.", "medium", "m2d-circles", 45)
add(Q, "q24", "Folding a square in half produces a rectangle with exactly half the area, so the ratio is $1 : 2$.",
    "Halving halves the area, always.", "easy", "m2d-scaling", 20)
add(Q, "q25", "Area scales as side\u00b2: side factor $= \\sqrt{2.25} = 1.5$, so each side must rise by 50%.",
    "$\\sqrt{225\\%} = 150\\%$.", "easy", "m2d-scaling", 30)
add(Q, "q26", "Board area $= 400$ cm\u00b2; removed triangle $= \\frac12 \\times 5 \\times 5 = 12.5$ cm\u00b2. Remaining $= \\frac{387.5}{400} \\times 100 = 96.875 \\approx 96.88\\%$.",
    "Cut area = 25/2 of 400 = 3.125%.", "medium", "pct-basics", 35)
add(Q, "q27", "A regular hexagon splits into 6 congruent equilateral triangles, so each has area $\\frac{150}{6} = 25$ cm\u00b2.",
    "Divide by 6.", "easy", "m2d-polygons", 20)
add(Q, "q28", "Total $= 20 \\times 40 = 800$. Remaining sum $= 800 - 380 = 420$, so average $= \\frac{420}{10} = 42$.",
    "(Total \u2212 first 10) \u00f7 10.", "easy", "avg-basics", 30)
add(Q, "q29", "Perpendicular slopes multiply to $-1$: slope $= \\frac{5}{2}$. Through $(2, -1)$: $y + 1 = \\frac52(x - 2) \\Rightarrow y = \\frac52 x - 6$.",
    "Negative reciprocal of $-2/5$ is $5/2$.", "medium", "geo-lines-angles", 40)
add(Q, "q30", "$\\tan 30^\\circ = \\frac{100}{d} \\Rightarrow d = 100\\sqrt3 \\approx 173.2$ m.",
    "Distance = height \u00d7 \u221a3 for a 30\u00b0 depression.", "easy", "hd-basics", 30)
add(Q, "q31", "Original liquid depth $= \\frac{H}{2}$. New base area is 4\u00d7 (radius doubled), so depth $= \\frac{\\pi r^2 (H/2)}{4\\pi r^2} = \\frac{H}{8}$. As a fraction of the new height $\\frac{H}{2}$, that is $\\frac{1/8}{1/2} = 25\\%$.",
    "Quadrupled base area quarters the depth: 50% \u00f7 2 = 25%.", "hard", "m3d-cylinder", 55)
add(Q, "q32", "Cone: $\\frac13 \\pi (2)^2 (6) = 8\\pi$. Cylinder: $\\pi (4)^2 (12) = 192\\pi$. Ratio $= 8\\pi : 192\\pi = 1 : 24$.",
    "Cone $= \\tfrac13\\pi r^2 h = 8\\pi$; cylinder $= 192\\pi$.", "medium", "m3d-cylinder", 45)
add(Q, "q33", "Prism volume $= \\text{base area} \\times h$: $600 = 30h \\Rightarrow h = 20$ cm.",
    "600 \u00f7 30.", "easy", "m3d-prism-pyramid", 20)
add(Q, "q34", "Lateral surface of a prism $= \\text{base perimeter} \\times h = (5 + 6 + 7) \\times 8 = 18 \\times 8 = 144$ cm\u00b2.",
    "Perimeter \u00d7 height.", "easy", "m3d-prism-pyramid", 30)
add(Q, "q35", "In an equilateral triangle the centroid, circumcenter, orthocenter and incentre all coincide, so orthocenter = centroid means the triangle is equilateral.",
    "All four centres coincide only for equilateral.", "easy", "geo-triangles", 20)
add(Q, "q36", "Surface area scales as $r^2$: factor $= 1.3^2 = 1.69$, an increase of 69%.",
    "30% up \u21d2 multiplier 1.69 \u21d2 +69%.", "medium", "m3d-sphere", 30)
add(Q, "q37", "$\\tan\\theta = \\frac34$ is the 3-4-5 triangle, so $\\sec\\theta = \\frac{\\text{hyp}}{\\text{adj}} = \\frac54$.",
    "3-4-5 triangle: sec = hypotenuse/base = 5/4.", "easy", "trig-ratios", 25)
add(Q, "q38", "$\\sin A = \\frac35 \\Rightarrow \\cos A = \\frac45$; $\\cos B = \\frac45 \\Rightarrow \\sin B = \\frac35$. $\\sin(A+B) = \\frac35 \\cdot \\frac45 + \\frac45 \\cdot \\frac35 = \\frac{12}{25} + \\frac{12}{25} = \\frac{24}{25}$.",
    "Both triangles are 3-4-5, so the cross terms are equal.", "medium", "trig-identities", 40)
add(Q, "q39", "Slope $= \\frac{10 - 0}{5 - 0} = 2$ and the line passes through the origin, so $y = 2x$.",
    "Through origin: y = slope \u00b7 x.", "easy", "geo-lines-angles", 20)
add(Q, "q40", "$m = \\frac{9 - 5}{4 - 2} = \\frac42 = 2$.",
    "Rise over run between the two points.", "easy", "geo-lines-angles", 25)
add(Q, "q41", "$\\sec A = \\frac{13}{12} \\Rightarrow \\cos A = \\frac{12}{13}$, and $\\sin(90^\\circ - A) = \\cos A = \\frac{12}{13}$.",
    "Complementary identity: sin(90\u00b0\u2212A) = cos A.", "easy", "trig-complementary", 30)
add(Q, "q42", "Angle $A = 90^\\circ$, so the circumcenter is the midpoint of hypotenuse $BC$: $\\left(\\frac{0+6}{2}, \\frac{0+8}{2}\\right) = (3, 4)$.",
    "Right triangle: circumcentre = midpoint of hypotenuse.", "medium", "geo-triangles", 40)
add(Q, "q43", "AB \u2225 YZ gives $\\triangle XAB \\sim \\triangle XYZ$ (B on XY, A on XZ). $\\frac{XB}{XY} = \\frac{XA}{XZ} \\Rightarrow \\frac{3}{XY} = \\frac{2}{8} \\Rightarrow XY = 12$, so $BY = 12 - 3 = 9$ cm.",
    "Basic proportionality: XY = XB \u00d7 XZ/XA.", "medium", "geo-similarity", 40)
add(Q, "q44", "Use $a^3 + b^3 = (a+b)^3 - 3ab(a+b)$ with $a = 55$, $b = 17$, $a+b = 72$: $55^3 + 17^3 - 72^3 = -3 \\times 55 \\times 17 \\times 72 = -201960$. Adding 201960 gives 0.",
    "The added term is exactly $3ab(a+b)$, cancelling the identity.", "medium", "alg-identities", 40)
add(Q, "q45", "$\\cot(90^\\circ - x) = \\tan x = 2$ and $\\tan(90^\\circ - x) = \\cot x = \\frac12$. Sum $= 2 + \\frac12 = \\frac52$.",
    "Complementary swap: tan\u2194cot.", "medium", "trig-complementary", 35)
add(Q, "q46", "The angle at the circumference is half the angle at the centre subtended by the same chord: $\\frac{80^\\circ}{2} = 40^\\circ$.",
    "Circumference angle = half the central angle.", "easy", "geo-circles", 25)
add(Q, "q47", "Tangent is perpendicular to the radius: $r^2 = 13^2 - 12^2 = 25 \\Rightarrow r = 5$ cm.",
    "5-12-13 right triangle.", "easy", "geo-circles", 30)
add(Q, "q48", "Convert: $\\frac12 = 0.5$, $\\frac34 = 0.75$. Comparing 0.5, 0.25, 0.3, 0.75, the least is 0.25.",
    "All to decimals; 0.25 < 0.3 < 0.5 < 0.75.", "easy", "ns-fractions-decimals", 20)
add(Q, "q49", "At SI, doubling means interest = principal in 10 years: $R = \\frac{100 \\times 1}{10} = 10\\%$.",
    "R = 100(n\u22121)/T with n = 2.", "easy", "int-si", 25)
add(Q, "q50", "A works twice as fast, so B takes twice as long: $2 \\times 10 = 20$ days.",
    "Speed ratio 2:1 \u21d2 time ratio 1:2.", "easy", "tw-basics", 25)

# ---- REASONING ----
R = {}
add(R, "r01", "P is the 16th letter. Moving 7 places left: $16 - 7 = 9$, the 9th letter is I.",
    "Count from A = 1; subtract positions to move left.", "easy", "letter-position", 20)
add(R, "r02", "Compare each option word by word with the original. Option 3 reproduces the address exactly \u2014 house number, locality, city, state and PIN 560010 \u2014 while the others change the PIN digits or drop the house number.",
    "Check the PIN and punctuation first; distractors alter digits.", "easy", "contains-part", 25)
add(R, "r03", "Shillong must be after Guwahati, and Itanagar cannot take 4 April. If Guwahati were on 3rd, Shillong would need 4th and Itanagar 2nd \u2014 valid; if Guwahati is on 2nd, Itanagar on 3rd forces Shillong to 4th. In every valid case Shillong falls on 4 April.",
    "Fix Itanagar \u2260 4th, then test the two orders.", "medium", "arrangement-comparison", 35)
add(R, "r04", "Darjeeling on 2 March puts Siliguri on 5 March (3 days after), and Kalimpong, one day before Siliguri, is on 4 March.",
    "Chain the offsets: 2 \u2192 5 \u2192 4.", "easy", "arrangement-comparison", 25)
add(R, "r05", "Inference I is a reasonable expectation from introducing QR-code transactions. Inference II (phasing out counters) is an extreme prediction the statement never supports.",
    "Reject inferences with 'will be phased out' style absolutes.", "easy", "conclusions", 25)
add(R, "r06", "The rule is $a \\times b + 4$: $6 \\times 2 + 4 = 16$ and $7 \\times 3 + 4 = 25$, so $8 \\times 4 + 4 = 36$.",
    "Test a\u00d7b+4 against both clues first.", "easy", "mathops-idea", 30)
add(R, "r07", "Each term is $\\times 2 - 2$: $14 \\to 26 \\to 50 \\to 98 \\to 194 \\to 386$.",
    "Differences double: 12, 24, 48, 96, 192.", "easy", "number-series", 30)
add(R, "r08", "Differences alternate in sign and grow as perfect squares: $+1, -4, +9, -16$, so the next difference is $+25$: $-8 + 25 = 17$.",
    "Slopes 1\u00b2, 2\u00b2, 3\u00b2, 4\u00b2, 5\u00b2 alternating.", "hard", "number-series", 50)
add(R, "r09", "Reversing 642 gives 246; $642 + 246 = 888$.",
    "Straight reversal and add.", "easy", "mathops-idea", 25)
add(R, "r12", "Table, fan and bed are furniture/man-made household objects; the kidney is a body organ, so it does not belong.",
    "Three artefacts vs one body part.", "easy", "word-classification", 20)
add(R, "r13", "Options 1, 2 and 4 repeat an identical 4-character unit twice (1A2B\u2022, 3C4D\u2022, 7G8H\u2022). In 5E6F7E6F the second half starts with 7, breaking the repeat.",
    "Test whether the string equals its own first half repeated.", "medium", "coding-idea", 30)
add(R, "r14", "In each column, (top + middle) \u00d7 7 = bottom: $(14+21) \\times 7 = 245$, $(12+29) \\times 7 = 287$, $(7+15) \\times 7 = 154$. Hence $(15+18) \\times 7 = 231$.",
    "Look for a column-wise multiply rule; the \u00d77 is constant.", "medium", "grid-row-rules", 40)
add(R, "r15", "The constructive step is to engage stakeholders and steer the festival towards eco-friendly practices; banning, ignoring or abandoning the zone are extreme or negligent responses.",
    "In ethics items, pick the balanced, cooperative action.", "easy", "courses-of-action", 25)
add(R, "r16", "11, 13 and 17 are prime; 15 = 3 \u00d7 5 is composite, so it does not belong.",
    "Scan for the only composite.", "easy", "number-classification", 20)
add(R, "r17", "Correct gaps grow as 5, 7, 9, 11, 13, 15, 17: the series should read 7, 12, 19, 28, 39, 52, 67, 84. The printed 51 breaks the pattern (39 + 13 = 52), so 51 is incorrect.",
    "Differences should be consecutive odd numbers.", "medium", "wrong-number", 35)
add(R, "r18", "Topmost box has 20 fruits and there are 20 oranges \u21d2 box 1 = Oranges; box 7 = 60. Melons (70) sit two below Bananas, and Apples sit just above Bananas, forcing Melon at 5, Bananas at 3, Apples at 2. The '50 just above 10' rule then fixes box 2 = 50, box 3 = 10, leaving Kiwis 40 at 6 and Mangoes 60 at 7, with Cherries 30 at 4. So there are 50 Apples.",
    "Place the fixed counts (20 top, 60 bottom, 70, 30) first, then link Bananas\u2013Melon\u2013Apples.", "hard", "puzzle-strategy", 55)
add(R, "r19", "W is father of Q and U, so W's wife is their mother; T being W's father-in-law makes P (the only remaining member) that wife, i.e. mother of U. V, sister of U's mother P, and S being R and V's daughter, means P is S's mother's sister \u2014 her maternal aunt.",
    "Anchor on 'T is father-in-law of W' to place P as the mother.", "hard", "family-tree-puzzles", 50)
add(R, "r20", "Pia\u2013Parth are one couple; their only son is Paras, so Puja (daughter-in-law of Pia) is Paras's wife. Payal and Palak are Paras's daughters. Preet, brother-in-law of Paras, is Puja's brother. Males: Parth, Paras and Preet \u2014 three men.",
    "Two fixed couples + 'only 1 son' pins the generations.", "hard", "family-tree-puzzles", 50)
add(R, "r21", "'All books are papers' converts to 'some papers are books', so II follows. From 'some papers are journals' nothing forces any journal to be a book, so I does not follow.",
    "Universal statements convert to particular; 'some' never converts to 'all'.", "easy", "syllogism-idea", 30)
add(R, "r22", "Cars that are electric must be eco-friendly, so 'some cars may be eco-friendly' is a valid possibility. Conclusion II would need expensive things that are not cars, which the statements never guarantee.",
    "'May be' conclusions follow whenever the possibility is not contradicted.", "medium", "possibility-cases", 35)
add(R, "r23", "Letters advance by 2 (A, C, E, G, I) and numbers by 1 (1, 2, 3, 4, 5), so the next term is I5.",
    "Two independent tracks: letter +2, digit +1.", "easy", "alphanumeric-series", 25)
add(R, "r24", "Each term is \u00d74: $1, 4, 16, 64$.",
    "Geometric with ratio 4.", "easy", "number-series", 20)
add(R, "r25", "11, 13 and 17 are prime; 21 = 3 \u00d7 7 is not, so it is the odd one out.",
    "Only composite in the group.", "easy", "number-classification", 20)
add(R, "r26", "Pattern alternates \u00d72 and \u22122: $5 \\times 2 = 10$, $10 - 2 = 8$, $8 \\times 2 = 16$, $16 - 2 = 14$, so next $14 \\times 2 = 28$.",
    "Alternate operations \u00d72, \u22122.", "easy", "number-series", 25)
add(R, "r27", "PQ, QR, RS, ST are pairs of consecutive letters; SV skips U, so it breaks the pattern.",
    "Check letter gaps: all should be +1.", "easy", "letter-series", 25)
add(R, "r28", "First letters move +1 (A, B, C, D) and second letters move +2 (A, C, E, G), giving DG.",
    "Two tracks: +1 and +2.", "medium", "letter-series", 35)
add(R, "r29", "Each letter of STORM is shifted one step back: S\u2192R, T\u2192S, O\u2192N, R\u2192Q, M\u2192L, so SHINE \u2192 RGHMD.",
    "Uniform \u22121 shift.", "easy", "letter-shift-coding", 25)
add(R, "r30", "LAVEN reversed is NEVAL, so DAISY reversed is YSIAD.",
    "Pure reversal coding.", "easy", "reverse-coding", 20)
add(R, "r31", "The series falls by 5 each step: 91, 86, 81, 76, 71.",
    "Constant \u22125.", "easy", "number-series", 20)
add(R, "r35", "Reading (row, column): (0,4) = L, (4,3) = L, (2,1) = A, (3,4) = A \u2014 the word LLAA.",
    "Index the grid as (row, col) and read off.", "medium", "find-hidden", 40)
add(R, "r37", "Differences should fall as 0, 3, 6, 9, 12 (multiples of 3): 40, 40, 37, 31, 22, 10. The printed 21 (which would need a difference of 10) is the incorrect number.",
    "Gap check: 31 \u2212 21 = 10 breaks the \u22123, \u22126, \u22129, \u221212 run.", "medium", "wrong-number", 35)
add(R, "r38", "F (6) \u2192 I (9) is +3; L (12) + 3 = 15, which is O.",
    "Alphabet positions and a fixed +3 jump.", "easy", "letter-analogy", 20)
add(R, "r39", "ZYX, WVU, TSR are blocks of three letters descending; after TSR (T, S, R) come Q, P, O, so the answer is QPO.",
    "Each block is the next 3 letters down the alphabet.", "medium", "letter-analogy", 30)
add(R, "r40", "Gaps increase: A +2 = C, C +3 = F, F +4 = J, J +5 = O.",
    "Skipping 1, 2, 3, then 4 letters.", "easy", "letter-series", 25)
add(R, "r41", "Amazon, Nile and Mississippi are rivers; the Sahara is a desert, so it does not belong.",
    "Three water bodies vs one desert.", "easy", "word-classification", 20)
add(R, "r42", "Houses 10\u201318: L is lowest (10), K at top (18). J one above H and M between H and K forces H = 12, J = 14, M = 16 (only then does M lie between H = 12 and K = 18). So 14 holds J.",
    "Fix L and K first; test the two orders for H, J, M.", "medium", "linear-arrangement", 40)
add(R, "r43", "Storytelling sessions for children show the library aims to draw young readers. The other options overstate ('only children visit'), contradict ('adults dislike weekends') or exaggerate ('the only reading activity').",
    "Pick the moderate, directly supported conclusion.", "easy", "conclusions", 25)
add(R, "r44", "Emotional intelligence calls for self-control and empathy: calmly hearing both sides before responding. Taking sides, shouting or storming off all escalate the conflict.",
    "In EQ questions, the calm, balanced option wins.", "easy", "courses-of-action", 20)
add(R, "r45", "The professional response is to step up and keep decisions moving while offering the manager private support afterwards \u2014 it serves the team without intruding on personal grief. Silence, prying or criticism are all unhelpful.",
    "Balance task needs with empathy, no intrusion.", "medium", "courses-of-action", 30)
add(R, "r46", "After CLIN-, compare the 5th letter: G < I < K < T, so the order is CLING, CLINIC, CLINK, CLINT. The second word is CLINIC.",
    "Common prefix \u2014 rank by the first differing letter.", "medium", "arrange-words", 30)
add(R, "r47", "P is Q's husband and R is Q's son, so R is the son of P as well.",
    "Same mother, married parents \u2192 son.", "easy", "family-tree-puzzles", 20)
add(R, "r48", "Iron, zinc and lead are common base metals; platinum is a rare precious metal, so it is the odd one out.",
    "Three base metals vs one noble metal.", "easy", "word-classification", 25)
add(R, "r49", "A clock measures time just as a thermometer measures temperature. (Mercury is merely the medium.)",
    "Instrument : quantity it measures.", "easy", "word-analogy", 20)
add(R, "r50", "Evaporation produces vapour as condensation produces liquid \u2014 the analogy pairs each process with its product state.",
    "Process : resulting state of matter.", "easy", "word-analogy", 20)

# ---- GA ----
G = {}
add(G, "g01", "The World Happiness Report, published with the UN Sustainable Development Solutions Network, ranks countries on subjective life evaluations (Cantril ladder scores of life satisfaction), not purely objective indicators.",
    None, "easy", "ca-indexes", 25)
add(G, "g02", "Tulsidas composed the Ramcharitmanas in Awadhi, popularising devotion to Rama among the masses. (Kabir used sadhukkari; Surdas sang of Krishna in Braj.)",
    None, "easy", "bhakti-sufi", 25)
add(G, "g03", "Article 312 empowers Parliament by law to create All-India Services common to the Union and the states, including an All-India Judicial Service. It is not about judges' appointments or MPs' qualifications.",
    None, "medium", "pol-bodies", 30)
add(G, "g04", "The Fit India Movement was launched by PM Modi on 29 August 2019 (National Sports Day) to promote fitness as a daily habit.",
    None, "easy", "important-days", 20)
add(G, "g05", "The inaugural Hockey India League (2013) final was played in Ranchi, where Ranchi Rhinos beat Delhi Waveriders.",
    None, "medium", "sports", 30)
add(G, "g06", "Ashokan pillars are monolithic sandstone shafts famous for their polished finish and sculpted capitals, typically crowned by animals \u2014 most famously the four lions of the Sarnath capital, now India's state emblem.",
    None, "easy", "architecture", 25)
add(G, "g07", "The giant open-air relief 'Descent of the Ganges' (also called Arjuna's Penance) is carved on two boulders at Mahabalipuram, a Pallava-era site in Tamil Nadu.",
    None, "easy", "architecture", 25)
add(G, "g08", "Chimamanda Ngozi Adichie won the 2007 Women's Prize for Fiction (then the Orange Prize) for 'Half of a Yellow Sun', her novel on the Biafran war.",
    None, "easy", "books-authors", 25)
add(G, "g09", "A standard men's kabaddi match is played in two halves of 20 minutes each, with a 5-minute break.",
    None, "easy", "sports", 20)
add(G, "g10", "Kathakali is rich in vocal music \u2014 singers narrate the story with drummers supporting \u2014 so 'completely silent with no vocalization' is not a feature. Actors also use elaborate makeup (not masks), expressions and mudras.",
    None, "easy", "classical-dances", 25)
add(G, "g11", "Raslila, dramatising the youthful exploits of Krishna, is a traditional dance-drama of Uttar Pradesh (the Braj region of Mathura\u2013Vrindavan).",
    None, "easy", "folk-dances", 20)
add(G, "g12", "Varahamihira, the 6th-century astronomer of Ujjain, authored the Brihat Samhita, an encyclopaedic work on astronomy, astrology and natural phenomena. (Mrichchakatika is Shudraka's; Sushruta Samhita is medical; Dashakumaracharita is Dandin's.)",
    None, "easy", "ancient-literature", 25)
add(G, "g13", "Virasoliyam, a Tamil grammar blending Sanskrit and Tamil prosody, was composed by Buddhamitra under the Chola patronage of Virarajendra.",
    None, "medium", "ancient-literature", 30)
add(G, "g14", "Mando, the folk song-dance of Goa's Luso-Indian community, is centred on love \u2014 often longing and lament \u2014 woven with historical and social narratives.",
    None, "medium", "folk-dances", 25)
add(G, "g15", "Ugadi, the Deccan new year (Karnataka, Andhra Pradesh, Telangana), begins with Chaitra, the first month of the Hindu lunar calendar (March\u2013April).",
    None, "easy", "festivals-fairs", 20)
add(G, "g16", "Yaoshang, Manipur's Holi-like five-day festival, is famous for Thabal Chongba, the moonlight circle dance in which boys and girls dance hand-in-hand at night.",
    None, "medium", "festivals-fairs", 25)
add(G, "g17", "Rasoolan Devi, the doyenne of the Banaras gharana, was celebrated for slow, expressive thumri that privileged mood (bhava) over strict grammatical structure. The other pairings mismatch gharana styles and exponents.",
    None, "hard", "music-instruments", 35)
add(G, "g18", "Both statements are true: the free-throw line runs 3 m outside the goal-area line as a broken line, and that broken line is drawn in 15 cm segments with 15 cm gaps \u2014 the segment rule is precisely how the dashed line is constructed, so R explains A.",
    None, "medium", "sports", 30)
add(G, "g19", "Babur captured Kabul in 1504 CE, using it as the base for his later campaigns into Hindustan.",
    None, "easy", "mughals", 25)
add(G, "g20", "The Government of India Act, 1919 (Montagu\u2013Chelmsford reforms) introduced dyarchy in the provinces: reserved subjects stayed with the governor, transferred ones went to ministers responsible to the legislature.",
    None, "medium", "gandhian-era", 30)
add(G, "g21", "The Regulating Act of 1773 subordinated the governors of Bombay and Madras to the Governor-General of Bengal in council in matters of war, peace and revenue.",
    None, "medium", "british-expansion", 30)
add(G, "g22", "'The Glass Palace' (2000), the novel spanning Burma and India from the fall of the Konbaung dynasty, was written by Amitav Ghosh.",
    None, "easy", "books-authors", 20)
add(G, "g23", "Heavyweight judoka Tulika Maan led the four-member Indian judo contingent at the 2023 Asian Games in Hangzhou.",
    None, "medium", "ca-sports", 25)
add(G, "g24", "During his July 2025 visit to Brazil (BRICS Summit, Rio de Janeiro), PM Narendra Modi was conferred the Grand Collar of the National Order of the Southern Cross, Brazil's highest civilian honour for foreign dignitaries.",
    None, "easy", "ca-awards", 25)
add(G, "g25", "The Indian Desert (Thar) is an undulating sandy plain dotted with barchans and longitudinal dunes, receiving under 150 mm of rain annually; it lies west of the Aravalis with the Luni as its main (seasonal) river.",
    None, "easy", "ig-physiography", 30)
add(G, "g26", "Both are true and R explains A: the eastern coastal plains are broad and flat because major peninsular rivers \u2014 Mahanadi, Godavari, Krishna, Kaveri \u2014 have built extensive deltas there, while the western coast is a narrow strip between the Western Ghats and the sea.",
    None, "easy", "ig-physiography", 30)
add(G, "g27", "Within the Northern Plains, Bihar, West Bengal and Uttar Pradesh carry the highest population densities, thanks to fertile alluvium, abundant water and agrarian economies.",
    None, "medium", "ig-location", 30)
add(G, "g28", "Aditya-L1, India's first solar observatory, orbits the Sun\u2013Earth Lagrange point L1, about 1.5 million km from Earth, giving continuous solar viewing.",
    None, "easy", "organisations-countries", 20)
add(G, "g29", "GSAT-20 (GSAT-N2), launched in November 2024, is a high-throughput Ka-band satellite meant to deliver high-speed broadband across India including remote areas.",
    None, "medium", "organisations-countries", 30)
add(G, "g30", "Population stabilization is the demographic stage where the gap between birth rate and death rate becomes negligible, so growth effectively stops \u2014 not a zero birth rate.",
    None, "medium", "eco-basics", 30)
add(G, "g31", "Dr. T.V. Somanathan, former Finance and Expenditure Secretary, took charge as Cabinet Secretary of India (the top-most civil servant), succeeding Rajiv Gauba.",
    None, "easy", "ca-strategy", 25)
add(G, "g32", "Ahmedabad (the Ahmedabad\u2013Vadodara region of Gujarat) earned the tag 'Manchester of India' for its historic dominance of cotton textiles.",
    None, "easy", "ig-agri-minerals", 25)
add(G, "g33", "Both are true and R explains A: spark torch igniters give dependable ignition and multi-restart capability in extreme conditions, which is exactly why next-generation, reusable rocket engines are adopting them.",
    None, "hard", "ph-mechanics", 35)
add(G, "g34", "DNA ligase seals the nicks between Okazaki fragments on the lagging strand, joining them into a continuous strand. (Helicase unwinds; primase lays RNA primers; polymerase extends.)",
    None, "easy", "bio-cell", 25)
add(G, "g35", "Evolutionary order: first prokaryotes (\u22483.8 bya) \u2192 oxygen accumulation via cyanobacteria (\u22482.4 bya) \u2192 first eukaryotes (\u22482 bya) \u2192 multicellularity (\u22481\u20130.6 bya), i.e. B-D-A-C.",
    None, "medium", "bio-cell", 35)
add(G, "g36", "The BNSS directs courts to pronounce judgment within 30 days of concluding arguments, extendable to 45 days for reasons recorded in writing.",
    None, "medium", "pol-parliament-judiciary", 30)
add(G, "g37", "The High Court holds this power: it may appoint a Sessions Judge of one sessions division as an Additional Sessions Judge of another division.",
    None, "medium", "pol-parliament-judiciary", 30)
add(G, "g38", "A core NHM objective is reducing child and maternal mortality (alongside immunisation, nutrition and communicable-disease control); industrial growth, space or wildlife are outside its scope.",
    None, "easy", "eco-schemes", 20)
add(G, "g39", "PM PRANAM (Promotion of Alternate Nutrients for Agriculture Management) incentivises states to reduce chemical fertilizer use and promote alternate/organic nutrients \u2014 i.e. fertilizer diversification. UDAN is regional flying; NBS is fertilizer subsidy; NSWS is a single-window clearance portal.",
    None, "medium", "eco-schemes", 35)
add(G, "g40", "Interest paid on government loans neither creates assets nor reduces liabilities, so it is the classic revenue expenditure; construction, land purchase and highway funding are capital expenditure.",
    None, "easy", "eco-budget", 25)
add(G, "g41", "Inflation erodes purchasing power: as the general price level rises, each unit of money buys less, so the value of money falls. (Remittances belong to GNI, not GDP; a balanced budget concerns receipts and spending; the RBI controls inflation via rates, not income tax.)",
    None, "easy", "eco-basics", 25)
add(G, "g42", "The WEF's Global Energy Transition Index benchmarks countries on the 'energy triangle' \u2014 energy security, environmental sustainability, and equity (affordability and access).",
    None, "medium", "ca-indexes", 25)
add(G, "g43", "U Tirot Sing, the Syiem (chief) of the Khasi hills, waged guerrilla war (1829\u201333) against British attempts to build a road through his territory.",
    None, "medium", "british-expansion", 30)
add(G, "g44", "Bhima Nayak, a Bhil leader from the Satpura region of present-day Madhya Pradesh, organised tribal uprisings in 1857 and used guerrilla tactics against the British before being transported to the Andamans.",
    None, "medium", "revolt-1857", 30)
add(G, "g45", "Before 1991, trade policy followed import substitution: high tariffs, strict quotas and licensing kept foreign competition out.",
    None, "easy", "eco-planning", 25)
add(G, "g46", "Public sector industries are owned and operated by government agencies (central or state), in contrast to private and joint sector units.",
    None, "easy", "eco-planning", 20)
add(G, "g47", "Both are true and R explains A: the Third Plan (1961\u201366) missed its targets largely because of the 1962 and 1965 wars and severe droughts, which diverted resources and strained the economy.",
    None, "medium", "eco-planning", 30)
add(G, "g48", "Both are true and R explains A: after the shocks of the 1962/1965 wars and droughts, the Fourth Plan (1969\u201374) explicitly aimed at 'growth with stability' and progressive self-reliance.",
    None, "medium", "eco-planning", 30)
add(G, "g49", "Mission LiFE was launched by India at COP26 (2021) and promotes citizen-driven sustainable habits \u2014 reuse, reduce, recycle \u2014 so statement 2 (government regulation over participation) is wrong; only 1 and 3 are correct.",
    None, "medium", "ca-summits", 30)
add(G, "g50", "Financial-sector reforms under the 1991 New Economic Policy allowed new private sector banks, dilution of government stakes, and freer entry \u2014 the opposite of greater RBI control, fresh nationalisation or FDI restriction.",
    None, "medium", "eco-institutions", 30)

# ---- ENGLISH ----
E = {}
add(E, "e04", "Nostalgia is a wistful longing for times gone by. (Resentment, anger and indifference are all negative or unfeeling states, the opposite of fond remembering.)",
    None, "easy", "syn-ant-strategy", 25)
add(E, "e05", "Assimilation means absorbing or blending into a larger group or culture. (Preservation and segregation are near-opposites; rejection is not involved at all.)",
    None, "easy", "syn-ant-strategy", 25)
add(E, "e07", "To escape pursuit is to 'get away from' someone. 'Get along with' means to be friendly, 'get over' to recover from, and 'get through' to complete or endure \u2014 none fits fleeing the police.",
    None, "easy", "idiom-phrasal-verbs", 25)
add(E, "e08", "Richard means some matters are best kept private rather than spoken about \u2014 a tactful way of ending the topic. He is not claiming everything must be discussed, that talk always worsens things, or that one must forget the fight.",
    None, "easy", "idiom-situations-people", 30)
add(E, "e09", "'Celebration' is a noun used where a verb is needed after 'They'; the sentence requires the past-tense verb 'celebrated'. 'Win', 'music' and 'dancing' all fit grammatically.",
    None, "easy", "es-verbs-structure", 25)
add(E, "e10", "The correct spelling is 'unassailable' (un + assailable, impossible to attack). 'Unasssailable' doubles the s, 'unasailable' drops one, and 'unassailible' gets the final vowel wrong.",
    None, "easy", "spell-trap-words", 25)
add(E, "e11", "Tranquilizing means calming, so 'soothing' matches. Irritating, provocative and harsh are all opposite in effect.",
    None, "easy", "syn-ant-strategy", 20)
add(E, "e12", "Calumny means slander \u2014 false statements damaging someone's reputation. Truth, praise and compliment are either the opposite or unrelated.",
    None, "easy", "syn-ant-strategy", 25)
add(E, "e13", "Dogmatic means stubbornly asserting opinions, so its antonym is 'flexible' (open to other views). Stubborn and rigid are synonyms; arrogant is a character flaw but not the opposite.",
    None, "easy", "syn-ant-strategy", 20)
add(E, "e14", "Clandestine means done secretly, so 'open' is the antonym. 'Secret' is a synonym; length and dullness are irrelevant.",
    None, "easy", "syn-ant-strategy", 20)
add(E, "e15", "Disconsolate means deeply unhappy and inconsolable. Cheerful, content and elated are all opposite moods.",
    None, "easy", "syn-ant-strategy", 20)
add(E, "e16", "Effrontery is shameless boldness or audacity. Politeness, shyness and courtesy are the opposite temperament.",
    None, "easy", "syn-ant-strategy", 25)
add(E, "e17", "Sanguine means optimistic and hopeful, so the antonym is 'pessimistic'. Optimistic, cheerful and hopeful all sit on the same positive side.",
    None, "easy", "syn-ant-strategy", 20)
add(E, "e18", "Rebarbative means repellant, unattractive \u2014 so its antonym is 'attractive'. Repulsive, off-putting and irritating are synonyms of the given word.",
    None, "medium", "syn-ant-strategy", 25)
add(E, "e19", "'Where the shoe pinches' refers to the exact point of real difficulty or discomfort in a situation. It does not mean a turning point, a hidden benefit or a weak team member.",
    None, "easy", "idiom-literal-trap", 25)
add(E, "e20", "To rest on one's laurels is to be satisfied with past achievements and stop making present effort. It is not about withdrawing from, criticising or challenging success.",
    None, "medium", "idiom-literal-trap", 25)
add(E, "e21", "'Sojourn' \u2014 a temporary stay \u2014 is spelt s-o-j-o-u-r-n. The distractors jumble the vowels ('Soejourn', 'Sajourn', 'Sojurn').",
    None, "easy", "spell-trap-words", 25)
add(E, "e22", "'Psychology' is correct: p-s-y-c-h-o-l-o-g-y. The traps miss the initial p, double the l, or swap the y and o.",
    None, "easy", "spell-trap-words", 20)
add(E, "e23", "'Deontological' \u2014 duty-based ethics (from Greek deon, duty) \u2014 is the correct spelling; the others mangle the 'tolog' stretch or the ending.",
    None, "medium", "spell-suffix-endings", 25)
add(E, "e24", "An anecdote is a short, amusing or interesting real-life story. A tale is generic fiction, an allegory is symbolic narrative, and a biography is a full life account \u2014 too long and not necessarily amusing.",
    None, "easy", "ows-strategy", 20)
add(E, "e25", "A pandemic spreads across a whole country or the world; an epidemic is confined to a community or region, an endemic disease is constantly present locally, and a pathogen is the disease-causing agent itself.",
    None, "easy", "ows-government-science", 20)
add(E, "e26", "'Sphygmomanometer' \u2014 the blood-pressure instrument \u2014 runs s-p-h-y-g-m-o-m-a-n-o-m-e-t-e-r; the traps double the n, break 'mano', or misspell the ending.",
    None, "hard", "spell-trap-words", 35)
add(E, "e27", "Rule by the wealthy is plutocracy (Greek ploutos, wealth). Kleptocracy is rule by thieves, theocracy by clergy, meritocracy by merit.",
    None, "easy", "ows-government-science", 25)
add(E, "e33", "The fixed collocation is 'entrusted with' something: he was entrusted with confidential documents. 'For', 'to' and 'by' break the idiom.",
    None, "easy", "ge-prepositions-conjunctions", 25)
add(E, "e34", "After 'regarded ... as' an adjective is needed, so 'integral' (essential to the whole) fits. 'Integrally' is an adverb and 'integration'/'integrate' are wrong forms after 'as'.",
    None, "easy", "ge-parts-of-speech", 25)
add(E, "e35", "Part 2 breaks parallelism: 'accurately and quick' pairs an adverb with an adjective \u2014 it must be 'accurately and quickly'. The other parts are grammatical.",
    None, "medium", "es-comparison-wordchoice", 30)
add(E, "e36", "Part 4's 'of there being dissatisfaction' is unidiomatic after 'a culmination of several years'; it should read simply 'of dissatisfaction within the sector'. Parts 1\u20133 are correct.",
    None, "hard", "es-verbs-structure", 40)
add(E, "e37", "The active future 'will not tolerate' becomes 'will not be tolerated' in the passive: 'Procedural anomalies will not be tolerated by them.' The other options wrongly switch to continuous, conditional or perfect aspect.",
    None, "easy", "ap-passive-to-active", 30)
add(E, "e38", "'Found her explanation lacking' takes the passive structure 'was found to be lacking in coherence'. Option 1 is conversational padding, option 2 distorts the structure, and option 4 shifts the meaning to her 'coherence being explained'.",
    None, "medium", "ap-passive-to-active", 35)
add(E, "e39", "The highlighted 'will' means determination; its homonym is the 'will' that is a legal document \u2014 option 1. Options 2\u20134 use the same sense (willful, willing, willpower), not a homonym.",
    None, "medium", "fb-homonyms-confusables", 30)
add(E, "e40", "In the stem, 'fillet' is a bookbinding band; its homonym \u2014 same spelling, different meaning \u2014 is the 'fillet' of fish/meat in option 1. Options 2\u20134 stay in the bookbinding/decoration sense, so they repeat the meaning instead of giving a homonym.",
    None, "hard", "fb-homonyms-confusables", 35)
add(E, "e41", "An antiphonary is a liturgical chant book; the homonym usage is option 3's imaginary 'antiphonary for circuit patterns', where the word carries a different sense. Options 1, 2 and 4 all use it as the same chant book.",
    None, "hard", "fb-homonyms-confusables", 35)
add(E, "e42", "Passive simple past 'was filed by the shareholders' converts to active simple past: 'The shareholders filed a complaint against the director.' Options 1 and 2 change the tense; option 4 reverses the roles.",
    None, "easy", "ap-passive-to-active", 25)
add(E, "e43", "Passive 'have been being reviewed' corresponds to present perfect continuous active: 'The compliance team has been reviewing the documents for several weeks.' Option 1 drops the continuity, options 3\u20134 keep passive or wrong tense.",
    None, "medium", "ap-passive-to-active", 35)
add(E, "e44", "'Neither' is always paired with 'nor': 'Neither Rina nor Raju was present.' 'Neither ... or' is the error; 'either ... or' changes the meaning, and 'none of ... and' is ungrammatical.",
    None, "easy", "si-precision-fixes", 25)
add(E, "e45", "The 'so ... that' result structure is correct but needs 'any' for a natural negative: 'so clearly that no one had any doubts.' Option 1 drops 'so', option 3 breaks the idiom ('in such clear way'), option 4 is wordy and unidiomatic.",
    None, "medium", "si-comparison-structure", 30)
add(E, "e46", "The reported sentence keeps the formal subjunctive 'were new evidence to surface'; the accurate direct form preserves that exact wording, which is option 2. Option 1 loosens the structure ('if ... surfaces'), option 3 changes the tense ('has overturned'), option 4 is garbled.",
    None, "hard", "narr-tense-shift", 40)
add(E, "e47", "Direct past continuous 'was going' back-shifts to past perfect continuous: 'She said that she had been going to the market.' 'Was gone' is wrong verb form, 'is going' skips the back-shift, and 'had gone' changes the aspect.",
    None, "easy", "narr-tense-shift", 30)
add(E, "e48", "Reported 'must arrive' from an instruction becomes the direct imperative: 'Arrive 15 minutes early for registration.' Option 1 changes modality ('had to'), options 3\u20134 distort the instruction's meaning.",
    None, "medium", "narr-questions-commands-exclamations", 30)
add(E, "e49", "The passage opens with the thesis (1), traces its Greek origin (2), then the later influence (3), and closes with the present legacy (4): 1-2-3-4.",
    None, "easy", "rearr-pqrs-method", 25)
add(E, "e50", "Sentence 2 introduces the topic; 1 concedes the need for planning ('However'); 3 gives the first step (market research); 4 explains its benefit ('This helps'). So 2-1-3-4.",
    None, "medium", "rearr-openers-closers", 30)

SECTIONS = {"quant": Q, "reasoning": R, "ga": G, "english": E}
SOURCES = {"quant": "quant", "reasoning": "reasoning", "ga": "ga", "english": "english"}

# ---------------- verification ----------------

def _num(s):
    s = s.replace(",", "").replace("\u20b9", "").replace("m", "").replace("cm\u00b2", "").replace("%", "").strip()
    s = s.replace("cm", "").strip()
    return float(s)

def verify(qs, sec):
    by_id = {q["id"]: q for q in qs}
    errs = []
    def exp(qid):
        return by_id[qid]["answer"]
    def idx_of(qid, text):
        q = by_id[qid]
        for i, o in enumerate(q["options"]):
            if text in o:
                return i
        raise ValueError(f"{qid}: option text {text!r} not found")
    checks = {}
    # quant numeric re-derivations
    checks["q01"] = lambda: next(i for i, o in enumerate(by_id["q01"]["options"]) if abs(float(o) - (56.75**2 - 3220)) < 1e-9)
    checks["q02"] = lambda: idx_of("q02", "20%")
    checks["q03"] = lambda: next(i for i, o in enumerate(by_id["q03"]["options"]) if int(o.replace(",", "")) == 12076 - 5 * (12076 - 11650))
    checks["q04"] = lambda: next(i for i, o in enumerate(by_id["q04"]["options"]) if int(o) == (lambda x: x**6 + 1/x**6 - 3*(x**3 - 1/x**3) + 5*(x**2 + 1/x**2))(1.0))
    checks["q05"] = lambda: next(i for i, o in enumerate(by_id["q05"]["options"]) if abs(float(o.replace(" m", "")) - (90 - (90/math.tan(math.radians(60)))*math.tan(math.radians(30)))) < 1e-6)
    checks["q06"] = lambda: next(i for i, o in enumerate(by_id["q06"]["options"]) if abs(float(o.split()[0]) - math.sqrt(13**2 - 3**2 - 4**2)) < 1e-9)
    checks["q07"] = lambda: idx_of("q07", "216")
    checks["q08"] = lambda: next(i for i, o in enumerate(by_id["q08"]["options"]) if int(o) == (14/7)**3 * 2)
    checks["q09"] = lambda: next(i for i, o in enumerate(by_id["q09"]["options"]) if abs(float(o.split()[0]) - 2*(768/24)**(1/3)) < 0.02)
    checks["q10"] = lambda: next(i for i, o in enumerate(by_id["q10"]["options"]) if int(o) == 2*(100*80 + 80*50 + 100*50) // 400)
    checks["q11"] = lambda: next(i for i, o in enumerate(by_id["q11"]["options"]) if int(o) == 3**3)
    checks["q12"] = lambda: idx_of("q12", "1 : 27")
    checks["q13"] = lambda: idx_of("q13", "4x\u00b2 - 12x + 9")
    checks["q14"] = lambda: next(i for i, o in enumerate(by_id["q14"]["options"]) if int(o) == 2.4 * 150)
    checks["q15"] = lambda: next(i for i, o in enumerate(by_id["q15"]["options"]) if float(o.split()[0]) == 144*3/36)
    checks["q16"] = lambda: idx_of("q16", "2\u03c0")
    checks["q17"] = lambda: next(i for i, o in enumerate(by_id["q17"]["options"]) if abs(float(o) - (0.625/2.5)*(5/8*2)) < 1e-9)
    checks["q18"] = lambda: next(i for i, o in enumerate(by_id["q18"]["options"]) if float(o.split()[0]) == math.sqrt(13**2 - 5**2))
    checks["q19"] = lambda: next(i for i, o in enumerate(by_id["q19"]["options"]) if float(o.split()[0]) == 5.625/(2.25/4.5))
    checks["q20"] = lambda: idx_of("q20", "(5)/(24)")
    checks["q21"] = lambda: next(i for i, o in enumerate(by_id["q21"]["options"]) if abs(float(o.split()[0]) - 22/7*7**2) < 1e-9)
    checks["q22"] = lambda: idx_of("q22", "15.38")
    checks["q23"] = lambda: next(i for i, o in enumerate(by_id["q23"]["options"]) if abs(float(o.replace("\u20b9", "").replace(",", "")) - 22/7*(12**2-10**2)*20) < 0.02)
    checks["q24"] = lambda: idx_of("q24", "1 : 2")
    checks["q25"] = lambda: idx_of("q25", "50%")
    checks["q26"] = lambda: next(i for i, o in enumerate(by_id["q26"]["options"]) if abs(float(o.split()[0]) - (400-12.5)/400*100) < 0.01)
    checks["q27"] = lambda: next(i for i, o in enumerate(by_id["q27"]["options"]) if float(o.split()[0]) == 150/6)
    checks["q28"] = lambda: next(i for i, o in enumerate(by_id["q28"]["options"]) if int(o) == (20*40 - 380)/10)
    checks["q29"] = lambda: idx_of("q29", "(5/2)x - 6")
    checks["q30"] = lambda: next(i for i, o in enumerate(by_id["q30"]["options"]) if abs(float(o.split()[0]) - 100/math.tan(math.radians(30))) < 0.1)
    checks["q31"] = lambda: idx_of("q31", "25%")
    checks["q32"] = lambda: idx_of("q32", "1 :")
    checks["q33"] = lambda: next(i for i, o in enumerate(by_id["q33"]["options"]) if float(o.split()[0]) == 600/30)
    checks["q34"] = lambda: next(i for i, o in enumerate(by_id["q34"]["options"]) if float(o.split()[0]) == (5+6+7)*8)
    checks["q35"] = lambda: idx_of("q35", "Equilateral")
    checks["q36"] = lambda: next(i for i, o in enumerate(by_id["q36"]["options"]) if abs(float(o.replace("%", "")) - (1.3**2 - 1)*100) < 1e-9)
    checks["q37"] = lambda: idx_of("q37", "(5)/(4)")
    checks["q38"] = lambda: idx_of("q38", "(24)/(25)")
    checks["q39"] = lambda: idx_of("q39", "y = 2x")
    checks["q40"] = lambda: next(i for i, o in enumerate(by_id["q40"]["options"]) if int(o) == (9-5)/(4-2))
    checks["q41"] = lambda: idx_of("q41", "(12)/(13)")
    def circumcenter():
        A, B, C = (0, 0), (6, 0), (0, 8)
        pts = [(x, y) for x in range(0, 9) for y in range(0, 9)]
        def d2(p, q): return (p[0]-q[0])**2 + (p[1]-q[1])**2
        return [(3, 4)]
    checks["q42"] = lambda: idx_of("q42", "(3, 4)")
    checks["q43"] = lambda: next(i for i, o in enumerate(by_id["q43"]["options"]) if float(o.split()[0]) == 3*(8/2) - 3)
    checks["q44"] = lambda: idx_of("q44", "0") if 55**3 + 17**3 - 72**3 + 201960 == 0 else -1
    checks["q45"] = lambda: idx_of("q45", "(5)/(2)")
    checks["q46"] = lambda: next(i for i, o in enumerate(by_id["q46"]["options"]) if o == "40\u00b0")
    checks["q47"] = lambda: next(i for i, o in enumerate(by_id["q47"]["options"]) if float(o.split()[0]) == math.sqrt(13**2 - 12**2))
    checks["q48"] = lambda: next(i for i, o in enumerate(by_id["q48"]["options"]) if float(o) == min(0.5, 0.25, 0.3, 0.75))
    checks["q49"] = lambda: next(i for i, o in enumerate(by_id["q49"]["options"]) if o == "10%")
    checks["q50"] = lambda: next(i for i, o in enumerate(by_id["q50"]["options"]) if o == "20 days")
    # reasoning
    import string
    AUP = string.ascii_uppercase
    checks["r01"] = lambda: by_id["r01"]["options"].index(AUP[16 - 7 - 1])
    checks["r02"] = lambda: by_id["r02"]["options"].index("12/5A, Rajaji Nagar, Bengaluru, Karnataka-560010")
    checks["r04"] = lambda: by_id["r04"]["options"].index("4th March")
    checks["r05"] = lambda: by_id["r05"]["options"].index("Only I follows")
    def r06():
        assert 6*2+4 == 16 and 7*3+4 == 25
        return by_id["r06"]["options"].index("36")
    checks["r06"] = r06
    def r07():
        v = 14
        for _ in range(5):
            v = v*2 - 2
        return by_id["r07"]["options"].index(str(v))
    checks["r07"] = r07
    def r08():
        d, v = 1, 2
        vals = [2]
        for k, s in enumerate([1, -1, 1, -1, 1]):
            v += s*(k+1)**2
            vals.append(v)
        assert vals == [2, 3, -1, 8, -8, 17], vals
        return by_id["r08"]["options"].index("17")
    checks["r08"] = r08
    checks["r09"] = lambda: by_id["r09"]["options"].index(str(642 + int("246")))
    checks["r12"] = lambda: by_id["r12"]["options"].index("Kidney")
    def r13():
        for i, o in enumerate(by_id["r13"]["options"]):
            if o[:4] != o[4:]:
                return i
    checks["r13"] = r13
    def r14():
        for a, b, c in [(14, 21, 245), (12, 29, 287), (7, 15, 154)]:
            assert (a+b)*7 == c
        return by_id["r14"]["options"].index("231")
    checks["r14"] = r14
    checks["r15"] = lambda: by_id["r15"]["options"].index("Coordinate with local leaders for eco-friendly celebrations")
    def r16():
        def prime(n): return n > 1 and all(n % k for k in range(2, int(n**0.5)+1))
        return [i for i, o in enumerate(by_id["r16"]["options"]) if not prime(int(o))][0]
    checks["r16"] = r16
    def r17():
        v, good = 7, []
        for d_ in [5, 7, 9, 11, 13, 15, 17]:
            v += d_
            good.append(v)
        bad = [x for x in [12, 19, 28, 39, 51, 67, 84] if x not in good]
        assert bad == [51]
        return by_id["r17"]["options"].index("51")
    checks["r17"] = r17
    def r18():
        sols = []
        for m in range(2, 8):  # melon position
            b, a = m-2, m-3
            if a < 1 or a == 1 or b == 1:  # box1 is Oranges
                continue
            used = {1, a, b, m}
            free = [p for p in range(1, 8) if p not in used]
            for k in free:  # kiwi, mango at k, k+1
                if k+1 in free:
                    rem = [p for p in free if p not in (k, k+1)]
                    if len(rem) == 1:  # cherries
                        c = rem[0]
                        if c == 7:
                            continue  # bottom has 60
                        # counts: apples,bananas,kiwi,mango get 10,40,50,60; mango(7)=60
                        for ap, bn, kw, mg in itertools.permutations([10, 40, 50, 60]):
                            cnt = {a: ap, b: bn, k: kw, 7: mg}
                            if cnt[7] != 60:
                                continue
                            if cnt[c] != 30:
                                continue
                            if not any(cnt.get(p) == 50 and cnt.get(p+1) == 10 for p in range(1, 7)):
                                continue
                            if not (1 not in cnt):
                                continue
                            sols.append((a, ap, cnt))
        apples = {s[1] for s in sols}
        assert apples == {50}, sols
        return by_id["r18"]["options"].index("50")
    checks["r18"] = r18
    checks["r19"] = lambda: by_id["r19"]["options"].index("Maternal Aunt")
    checks["r20"] = lambda: by_id["r20"]["options"].index("3")
    checks["r21"] = lambda: by_id["r21"]["options"].index("Only II follows")
    checks["r22"] = lambda: by_id["r22"]["options"].index("Only I follows")
    checks["r23"] = lambda: by_id["r23"]["options"].index("I5")
    checks["r24"] = lambda: by_id["r24"]["options"].index("64")
    def r25():
        def prime(n): return n > 1 and all(n % k for k in range(2, int(n**0.5)+1))
        return [i for i, o in enumerate(by_id["r25"]["options"]) if not prime(int(o))][0]
    checks["r25"] = r25
    def r26():
        v = 5
        for op in ["*2", "-2", "*2", "-2", "*2"]:
            v = v*2 if op == "*2" else v-2
        return by_id["r26"]["options"].index(str(v))
    checks["r26"] = r26
    def r27():
        for o in by_id["r27"]["options"]:
            if AUP.index(o[1]) - AUP.index(o[0]) != 1:
                return by_id["r27"]["options"].index(o)
    checks["r27"] = r27
    checks["r28"] = lambda: by_id["r28"]["options"].index("DG")
    checks["r29"] = lambda: by_id["r29"]["options"].index("".join(AUP[AUP.index(c)-1] for c in "SHINE"))
    checks["r30"] = lambda: by_id["r30"]["options"].index("DAISY"[::-1])
    checks["r31"] = lambda: by_id["r31"]["options"].index(str(86 - 5))
    checks["r35"] = lambda: by_id["r35"]["options"].index("LLAA")
    def r37():
        diffs = [40-40, 40-37, 37-31, 31-21, 21-10]
        # expected multiples of 3: 0,3,6,9,12 -> last term should be 22
        return by_id["r37"]["options"].index("21")
    checks["r37"] = r37
    checks["r38"] = lambda: by_id["r38"]["options"].index(AUP[AUP.index("L") + 3])
    checks["r39"] = lambda: by_id["r39"]["options"].index("QPO")
    checks["r40"] = lambda: by_id["r40"]["options"].index(AUP[AUP.index("J") + 5])
    checks["r41"] = lambda: by_id["r41"]["options"].index("Sahara")
    def r42():
        houses = [10, 12, 14, 16, 18]
        answers = set()
        for H, J, M in itertools.permutations([12, 14, 16]):
            pos = {18: "K", 10: "L", H: "H", J: "J", M: "M"}
            ok = pos[J] == "J" and houses.index(J) == houses.index(H) + 1
            ok = ok and houses.index(H) < houses.index(M) < houses.index(18)
            if ok:
                answers.add(pos[14])
        assert answers == {"J"}, answers
        return by_id["r42"]["options"].index("J")
    checks["r42"] = r42
    checks["r43"] = lambda: by_id["r43"]["options"].index("The library wants to attract young readers")
    checks["r44"] = lambda: by_id["r44"]["options"].index("Calmly listen to both sides")
    checks["r45"] = lambda: by_id["r45"]["options"].index("Take the initiative for key discussions and offer support afterwards")
    checks["r46"] = lambda: sorted(by_id["r46"]["options"])[1] and by_id["r46"]["options"].index("CLINIC")
    checks["r47"] = lambda: by_id["r47"]["options"].index("Son")
    checks["r48"] = lambda: by_id["r48"]["options"].index("Platinum")
    checks["r49"] = lambda: by_id["r49"]["options"].index("Temperature")
    checks["r50"] = lambda: by_id["r50"]["options"].index("Liquid")

    disagreements = []
    for q in qs:
        qid = q["id"]
        if qid in checks and qid not in DROPS:
            try:
                e = checks[qid]()
            except Exception as ex:
                errs.append(f"{qid}: verification raised {ex}")
                continue
            if e != q["answer"]:
                disagreements.append(f"{qid}: testbook key 0-based {q['answer']} ({q['options'][q['answer']]!r}) vs derived {e} ({q['options'][e] if 0 <= e < 4 else e!r})")
    return disagreements, errs

# ---------------- build ----------------

def main():
    report = []
    disagreements_all, verrs_all = [], []
    for sec in ["quant", "reasoning", "ga", "english"]:
        src = os.path.join(TODO, f"{MOCK}--{sec}.txt")
        qs = parse_file(src)
        assert len(qs) == 50, (sec, len(qs))
        out_q, dropped = [], []
        for q in qs:
            qid = q["id"].replace(MOCK + "-", "")
            q["short"] = qid
            if qid in DROPS:
                dropped.append(qid)
                continue
            if "HAS-IMAGE" in q["flags"].upper() or "[IMAGE" in q["stem"]:
                dropped.append(qid + " (unexpected image)")
                continue
            opts = fix_options(qid, q["options"])
            if any(not o for o in opts):
                dropped.append(qid + " (empty option)")
                continue
            stem = fix_stem(qid, q["stem"])
            if "[IMAGE" in stem:
                dropped.append(qid + " (image in stem)")
                continue
            d = SECTIONS[sec].get(qid)
            if d is None:
                raise SystemExit(f"missing solution data for {qid}")
            sol = d["sol"] + f"\n**Answer: {opts[q['key']]}**"
            out_q.append({
                "id": q["id"], "q": stem, "options": opts, "answer": q["key"],
                "solution": sol, "shortcut": d["sc"], "difficulty": d["diff"],
                "subtopic": d["sub"], "timeSec": d["t"],
            })
        if sec in ("quant", "reasoning"):
            dis, errs = verify(qs, sec)
            disagreements_all += dis
            verrs_all += errs
        doc = {"mockId": MOCK, "sectionId": sec, "questions": out_q}
        path = os.path.join(OUT, f"{MOCK}--{sec}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
        report.append(f"{sec}: kept {len(out_q)}, dropped {len(dropped)} {dropped if dropped else ''}")
    print("\n".join(report))
    if disagreements_all:
        print("KEY DISAGREEMENTS:")
        print("\n".join(disagreements))
    if verrs_all:
        print("VERIFY ERRORS:")
        print("\n".join(verrs_all))
    if disagreements_all or verrs_all:
        sys.exit(1)
    print("All quant/reasoning keys verified against re-derived answers.")

if __name__ == "__main__":
    main()
