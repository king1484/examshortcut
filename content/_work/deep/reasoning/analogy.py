"""Analogy topic build: notes + patterns + new subtopic + practice + pyqPatterns."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from analogy_notes import NOTES, PATTERNS, NEW_SUB, PYQS

d = load("analogy")

# ---- fix broken existing question: D->J was +6, not +3; correct model to E6G ----
patch_q(d, "rsn-analogy-15",
        q="Select the related cluster: **B3D : E6G :: H12N : ?**",
        solution="Letters: B→E and D→G are both **+3** (B=2→5=E, D=4→7=G). Number: 3→6 is **×2**. "
                 "Apply to H12N: H+3 = K, N+3 = Q, 12×2 = 24 → **K24Q**.")

# ---- new subtopic ----
add_sub(d, NEW_SUB, after="number-analogy")

# ---- notes + patterns per subtopic ----
for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])

# ---- practice ----
NQ = []  # new questions
_ctr = {}

def A(sub, pat, q, ans, wrong, solution, diff="medium", shortcut=None, t=45, check=None):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    NQ.append(Q(f"{sub}-p{_ctr[sub]:02d}", q, ans, wrong, solution, shortcut=shortcut,
                diff=diff, sub=sub, pat=pat, t=t, check=check))

# ================= analogy-idea =================
c = 4; assert c ** 3 == 64
A("analogy-idea", "an-p1", "Select the related number: **? : 64 :: 5 : 125**", c, ["3", "6", "8"],
  "5 : 125 is a **cube** pair (5³ = 125). So ? must satisfy ?³ = 64, and 4³ = 64. **Answer: 4.**",
  diff="easy", shortcut="Blank first: read the rule from the full pair, then run it backwards (cube root here).")
c = "Hive"
A("analogy-idea", "an-p1", "Select the related word: **? : Bee :: Den : Lion**", c,
  ["Honey", "Buzz", "Swarm"],
  "A den is the **home** of a lion. The home of a bee is a **hive**. Honey is the product, buzz the sound, swarm the group — all different links.",
  diff="easy")
c = 15; assert c ** 2 == 225
A("analogy-idea", "an-p1", "Select the related number: **? : 225 :: 14 : 196**", c, ["16", "14", "25"],
  "196 = 14², so the second number is the **square** of the first. ?² = 225 gives ? = **15**.",
  shortcut="Run the rule backwards: square root instead of square.")
c = shift("FDW", -3); assert c == "CAT" and shift("DOG", 3) == "GRJ"
A("analogy-idea", "an-p1", "Select the related letters: **? : FDW :: DOG : GRJ**", c,
  ["BBX", "CAV", "DBU"],
  "GRJ is DOG with every letter moved **+3** (D→G, O→R, G→J). So ? = FDW moved **−3**: F→C, D→A, W→T → **CAT**.",
  diff="hard", t=50, shortcut="Blank on the left: apply the discovered tuple backwards (subtract 3).")
c = "Distance"
A("analogy-idea", "an-p2", "Select the related word: **Speedometer : Speed :: Odometer : ?**", c,
  ["Car", "Kilometre", "Petrol"],
  "Link: instrument : quantity it **measures**. A speedometer measures speed; an odometer measures **distance**. A kilometre is only the unit; the car merely carries the meter.",
  diff="medium")
c = "Current"
A("analogy-idea", "an-p2", "Select the related word: **Hygrometer : Humidity :: Ammeter : ?**", c,
  ["Voltage", "Resistance", "Electricity"],
  "A hygrometer measures humidity, so the link is instrument : quantity measured. An **ammeter measures current**. Voltage goes with a voltmeter and resistance with an ohmmeter; 'electricity' is too vague.",
  diff="medium")
c = "Shoes"
A("analogy-idea", "an-p2", "Select the related word: **Author : Book :: Cobbler : ?**", c,
  ["Leather", "Shop", "Needle"],
  "An author **produces** a book. A cobbler produces **shoes**. Leather is the raw material and the shop is the workplace — near, but different links.",
  diff="medium")
c = 125; assert 5 ** 3 == c and 3 ** 2 == 9 and 3 ** 3 == 27 and 5 ** 2 == 25
A("analogy-idea", "an-p3", "Select the related number: **3 : 9 : 27 :: 5 : 25 : ?**", c, ["75", "100", "50"],
  "3, 9, 27 are 3¹, 3², 3³ — each term is the cube of the first. So 5, 25, ? ends at 5³ = **125**. (Doubling 25 gives 50 — the trap, because 3 → 9 is not doubling.)",
  diff="easy")
c = "J"; assert pos(c) == pos("D") + 6 and pos("F") == pos("C") + 3 and pos("I") == pos("C") + 6
A("analogy-idea", "an-p3", "Select the related letters: **C : F : I :: D : G : ?**", c, ["K", "I", "H"],
  "Each side moves **+3** per step: C(3) → F(6) → I(9). So D(4) → G(7) → 4+6 = 10 = **J**.",
  diff="medium")
c = ("Cow", "Foal")
A("analogy-idea", "an-p4", "Select the pair that fills both blanks: **? : Calf :: Horse : ?**", "Cow, Foal",
  ["Bull, Stable", "Cow, Mare", "Goat, Kid"],
  "Put each option into both blanks. Cow : Calf and Horse : Foal are both **adult : young** ✓. Bull : Calf mixes male with young; Cow : Mare mixes young with female; Goat : Calf is the wrong baby.",
  diff="easy")
c = ("Pride", "Sheep")
A("analogy-idea", "an-p4", "Select the pair that fills both blanks: **Lion : ? :: ? : Flock**", "Pride, Sheep",
  ["Den, Goat", "Cub, Birds", "Roar, Crow"],
  "The missing pair must keep the link **animal : its group** on both sides. Lion : **Pride** ✓ and **Sheep** : Flock ✓. Den is a home, cub a young one, roar a sound — each breaks one side.",
  diff="medium")
c = ("Cat", "Puppy")
A("analogy-idea", "an-p4", "Select the pair that fills both blanks: **? : Kitten :: Dog : ?**", "Cat, Puppy",
  ["Cat, Kennel", "Bitch, Bark", "Lion, Den"],
  "Both sides must read **adult : young**. Cat : Kitten ✓ and Dog : Puppy ✓. Kennel is a home and bark a sound, so those options break the link.",
  diff="medium")

# ================= letter-analogy =================
c = shift("RUXA", 2); assert c == "TWZC" and diffs("EHKN", "GJMP") == [2, 2, 2, 2]
A("letter-analogy", "an-p5", "Select the related letters: **EHKN : GJMP :: RUXA : ?**", c, ["TWYC", "SVZC", "TXZB"],
  f"E→G, H→J, K→M, N→P: every letter moves **+2**. Apply +2 to RUXA: R→T, U→W, X→Z, A→C → **{c}** (A wraps past Z).",
  diff="easy", shortcut="Subtract positions slot by slot; a flat tuple means one shift for all letters.")
c = shift("TGA", -1); assert c == "SFZ" and diffs("NKQ", "MJP") == [-1, -1, -1]
A("letter-analogy", "an-p5", "Select the related letters: **NKQ : MJP :: TGA : ?**", c, ["SFY", "RFA", "SGZ"],
  f"N→M, K→J, Q→P: every letter moves **−1**. Apply −1 to TGA: T→S, G→F, A→Z (A wraps back) → **{c}**.",
  diff="medium")
c = shift("GJMP", [1, 2, 3, 4]); assert c == "HLPT" and diffs("CFIL", "DHLP") == [1, 2, 3, 4]
A("letter-analogy", "an-p6", "Select the related letters: **CFIL : DHLP :: GJMP : ?**", c, ["HLPS", "GLPT", "IMQT"],
  f"The shifts rise: C+1 = D, F+2 = H, I+3 = L, L+4 = P — tuple (+1, +2, +3, +4). Apply it to GJMP: G+1 = H, J+2 = L, M+3 = P, P+4 = T → **{c}**.",
  diff="medium", shortcut="Copy the whole tuple exactly; do not average or 'tidy' it.")
c = shift("CXDW", [1, -1, 1, -1]); assert c == "DWEV" and diffs("AZBY", "BYCX") == [1, -1, 1, -1]
A("letter-analogy", "an-p6", "Select the related letters: **AZBY : BYCX :: CXDW : ?**", c, ["DXEV", "DWEW", "CVFU"],
  f"A→B is +1, Z→Y is −1, B→C is +1, Y→X is −1: tuple (+1, −1, +1, −1). CXDW: C+1 = D, X−1 = W, D+1 = E, W−1 = V → **{c}**.",
  diff="hard", t=55)
c = opp("IRON"); assert c == "RILM" and pos("G") + pos("T") == 27
A("letter-analogy", "an-p7", "Select the related letters: **GOLD : TLOW :: IRON : ?**", c, ["RILN", "RHLM", "SJLM"],
  "G(7) + T(20) = 27, so each letter is replaced by its **opposite** (27 − position). I↔R, R↔I, O↔L, N↔M → **RILM**.",
  diff="easy", shortcut="Letter pairs adding to 27 mean the opposite-letter table (A-Z, B-Y ... M-N).")
c = opp("GE"); assert c == "TV" and pos("C") + pos("X") == 27
A("letter-analogy", "an-p7", "Select the related letters: **CA : XZ :: GE : ?**", c, ["TW", "UV", "SU"],
  "C(3) + X(24) = 27 and A(1) + Z(26) = 27 — **opposite letters**. So G(7) → T(20) and E(5) → V(22) → **TV**.",
  diff="easy")
c = shift(rev("BELL"), 1); assert c == "MMFC" and rev("RING") + "1" == "GNIR1" and shift("GNIR", 1) == "HOJS"
A("letter-analogy", "an-p8", "Select the related letters: **RING : HOJS :: BELL : ?**", c, ["LLEB", "MMFB", "KKDA"],
  "RING backwards is GNIR, and +1 on each gives HOJS — **reverse, then shift**. BELL backwards is LLEB; +1 on each → **MMFC**.",
  diff="medium", t=50, shortcut="Read the second cluster backwards first; if it nearly matches, it is reverse (+ shift).")
c = rev("TIME"); assert c == "EMIT" and rev("FLOW") == "WOLF"
A("letter-analogy", "an-p8", "Select the related letters: **FLOW : WOLF :: TIME : ?**", c, ["TIEM", "ETIM", "MEIT"],
  "WOLF is FLOW **written backwards** — a pure reversal. So TIME reversed is **EMIT**.",
  diff="easy")
c = "IGTF"; assert c == "GIFT"[1] + "GIFT"[0] + "GIFT"[3] + "GIFT"[2]
A("letter-analogy", "an-p9", "Select the related letters: **PLAY : LPYA :: GIFT : ?**", c, ["IFGT", "GITF", "TFGI"],
  "PLAY (positions 1-2-3-4) becomes LPYA — the order is **2-1-4-3** (pairs swapped). GIFT in the same order: I, G, T, F → **IGTF**.",
  diff="medium")
c = rev("SUMMER"); assert c == "REMMUS" and rev("WINTER") == "RETNIW"
A("letter-analogy", "an-p9", "Select the related letters: **WINTER : RETNIW :: SUMMER : ?**", c, ["SUMMRE", "REMMSU", "MUSMER"],
  "RETTIW-style check: WINTER written backwards is RETNIW — **pure reversal**. SUMMER backwards is **REMMUS**.",
  diff="easy")

# ================= word-analogy =================
c = "Axe"
A("word-analogy", "an-p10", "Select the related word: **Mason : Trowel :: Woodcutter : ?**", c,
  ["Forest", "Wood", "Tree"],
  "A mason **uses** a trowel — worker : tool. A woodcutter uses an **axe**. Forest is the workplace, wood and tree are what he works on.",
  diff="easy")
c = "Symphony"
A("word-analogy", "an-p10", "Select the related word: **Poet : Poem :: Composer : ?**", c,
  ["Piano", "Orchestra", "Musician"],
  "A poet **creates** a poem — worker : product. A composer creates a **symphony**. The piano is an instrument, an orchestra a group of players, and a musician is a fellow worker.",
  diff="medium")
c = "Croak"
A("word-analogy", "an-p11", "Select the related word: **Donkey : Bray :: Frog : ?**", c,
  ["Leap", "Pond", "Tadpole"],
  "Bray is the **sound** of a donkey. The sound of a frog is a **croak**. Leap is its action, pond its home, tadpole its young one.",
  diff="easy")
c = "Pack"
A("word-analogy", "an-p11", "Select the related word: **Fish : Shoal :: Wolf : ?**", c,
  ["Kennel", "Howl", "Cub"],
  "A shoal is the **group** of fish. The group of wolves is a **pack**. Kennel is a home, howl a sound, cub a young one.",
  diff="medium")
c = "Thimphu"
A("word-analogy", "an-p12", "Select the related word: **Nepal : Kathmandu :: Bhutan : ?**", c,
  ["Dhaka", "Colombo", "Naypyidaw"],
  "Kathmandu is the **capital** of Nepal. The capital of Bhutan is **Thimphu**. Dhaka is the capital of Bangladesh, Colombo of Sri Lanka, Naypyidaw of Myanmar.",
  diff="medium")
c = "Baht"
A("word-analogy", "an-p12", "Select the related word: **Japan : Yen :: Thailand : ?**", c,
  ["Yuan", "Ringgit", "Dong"],
  "The yen is the **currency** of Japan. Thailand's currency is the **baht**. Yuan = China, ringgit = Malaysia, dong = Vietnam.",
  diff="medium")
c = "Wind speed"
A("word-analogy", "an-p13", "Select the related word: **Barometer : Pressure :: Anemometer : ?**", c,
  ["Humidity", "Temperature", "Rainfall"],
  "A barometer measures **pressure** — instrument : quantity. An anemometer measures **wind speed**. Humidity goes with a hygrometer and temperature with a thermometer.",
  diff="medium")
c = "Electric current"
A("word-analogy", "an-p13", "Select the related word: **Joule : Energy :: Ampere : ?**", c,
  ["Power", "Voltage", "Resistance"],
  "The joule is the **unit of energy**. The ampere is the unit of **electric current**. Power is the watt, voltage the volt, resistance the ohm.",
  diff="hard", t=50)
c = "Fishes"
A("word-analogy", "an-p14", "Select the related word: **Ornithology : Birds :: Ichthyology : ?**", c,
  ["Insects", "Reptiles", "Mammals"],
  "Ornithology is the **study of** birds. Ichthyology is the study of **fishes**. Insects come under entomology.",
  diff="medium")
c = "Sand"
A("word-analogy", "an-p14", "Select the related word: **Paper : Wood :: Glass : ?**", c,
  ["Water", "Mud", "Stone"],
  "Paper is **made from** wood — product : raw material. Glass is made from **sand** (melted with other minerals).",
  diff="easy")
c = "Scarce"
A("word-analogy", "an-p15", "Select the related word: **Ancient : Modern :: Abundant : ?**", c,
  ["Plentiful", "Copious", "Rich"],
  "Modern is the **opposite** of ancient. The opposite of abundant (plentiful) is **scarce**. Plentiful, copious and rich are synonyms of abundant — the wrong direction.",
  diff="easy")
c = "Conclude"
A("word-analogy", "an-p15", "Select the related word: **Begin : Commence :: End : ?**", c,
  ["Start", "Initiate", "Open"],
  "Commence **means the same as** begin — a synonym pair. A synonym of end is **conclude**. Start, initiate and open go the other way.",
  diff="medium")
c = "Cut"
A("word-analogy", "an-p16", "Select the related word: **Spade : Dig :: Knife : ?**", c,
  ["Kitchen", "Sharp", "Chef"],
  "A spade is **used to** dig — tool : action. A knife is used to **cut**. Kitchen is a place, sharp a quality, chef a user.",
  diff="easy")
c = "Flood"
A("word-analogy", "an-p16", "Select the related word: **Drought : Famine :: Rain : ?**", c,
  ["Crop", "River", "Monsoon"],
  "A drought **leads to** famine — cause : effect. Heavy rain leads to a **flood**. Crops and rivers are affected objects, monsoon is the season.",
  diff="medium")

# ================= number-analogy =================
c = 13 * 4 + 4; assert c == 56 and 9 * 4 + 4 == 40
A("number-analogy", "an-p17", "Select the related number: **9 : 40 :: 13 : ?**", c, ["52", "60", "48"],
  f"40 = 9 × 4 + 4, so the rule is **×4 then +4**. 13 × 4 + 4 = **{c}**. (52 forgets the +4.)",
  diff="medium")
c = 11 * 3 + 2; assert c == 35 and 7 * 3 + 2 == 23
A("number-analogy", "an-p17", "Select the related number: **7 : 23 :: 11 : ?**", c, ["33", "32", "36"],
  f"23 ÷ 7 ≈ 3, and 23 − 21 = 2, so the rule is **×3 then +2**. 11 × 3 + 2 = **{c}**.",
  diff="medium", shortcut="Divide the second number by the first to guess the multiplier; the small leftover is the add-on.")
c = 9 ** 2 - 1; assert c == 80 and 6 ** 2 - 1 == 35
A("number-analogy", "an-p18", "Select the related number: **6 : 35 :: 9 : ?**", c, ["81", "79", "72"],
  f"35 = 36 − 1 = 6² − 1, so the rule is **square then minus 1**. 9² − 1 = **{c}**. (81 is the plain-square trap.)",
  diff="easy")
c = 6 ** 3 + 1; assert c == 217 and 4 ** 3 + 1 == 65
A("number-analogy", "an-p18", "Select the related number: **4 : 65 :: 6 : ?**", c, ["216", "212", "222"],
  f"65 = 64 + 1 = 4³ + 1, so the rule is **cube then plus 1**. 6³ + 1 = **{c}**. (216 is the plain cube.)",
  diff="hard", t=50)
c = 5 * 9; assert c == 45 and 4 * 7 == 28
A("number-analogy", "an-p19", "Select the related number: **47 : 28 :: 59 : ?**", c, ["14", "54", "36"],
  f"28 = 4 × 7 — the **product of the digits**. For 59: 5 × 9 = **{c}**. (14 is the digit sum trap.)",
  diff="easy")
c = (4 + 5) ** 2; assert c == 81 and (3 + 6) ** 2 == 81
A("number-analogy", "an-p19", "Select the related number: **36 : 81 :: 45 : ?**", c, ["9", "20", "72"],
  f"The digit sum of 36 is 9, and 9² = 81 — **square of the digit sum**. Digit sum of 45 is 9, so 9² = **{c}**.",
  diff="medium")
assert 17 * 3 + 2 == 53 and 15 * 3 + 2 == 47 and 19 * 3 + 2 == 59 and 21 * 3 + 2 == 65
A("number-analogy", "an-p20",
  "Select the pair in which the numbers are related in the same way as **13 : 41**.",
  "(17, 53)", ["(15, 44)", "(19, 55)", "(21, 62)"],
  "41 = 13 × 3 + 2. Test each pair with **×3 + 2**: 17 × 3 + 2 = 53 ✓. The others give 47, 59 and 65 — each misses by a few. **Answer: (17, 53).**",
  diff="medium")
assert 9 * 10 == 90 and 7 * 8 == 56 and 10 * 11 == 110 and 5 * 6 == 30
A("number-analogy", "an-p20",
  "Select the pair in which the numbers are related in the same way as **8 : 72**.",
  "(9, 90)", ["(7, 50)", "(10, 100)", "(5, 25)"],
  "72 = 8 × 9 — **a(a + 1)**. Test: 9 × 10 = 90 ✓, while 7 × 8 = 56, 10 × 11 = 110 and 5 × 6 = 30. **Answer: (9, 90).**",
  diff="medium")

# ================= mixed-analogy =================
c = shift("H", 3) + str(8 * 2); assert c == "K16" and shift("C", 3) == "F" and 5 * 2 == 10
A("mixed-analogy", "an-p22", "Select the related cluster: **C5 : F10 :: H8 : ?**", c, ["K15", "J16", "K18"],
  f"Letter track: C → F is **+3**, so H → K. Number track: 5 → 10 is **×2**, so 8 → 16. Join: **{c}**.",
  diff="medium", shortcut="Solve the letter shift and the number rule separately, then assemble.")
c = shift("T", 3) + str(5 * 2) + shift("V", 3); assert c == "W10Y" and pos("S") - pos("P") == 3 and pos("U") - pos("R") == 3
A("mixed-analogy", "an-p22", "Select the related cluster: **P7R : S14U :: T5V : ?**", c, ["W9Y", "V10Y", "W10X"],
  f"Letters: P → S and R → U are **+3**, so T → W and V → Y. Number: 7 → 14 is **×2**, so 5 → 10. Join: **{c}**.",
  diff="medium")
c = "J" + str(pos("J") ** 2); assert c == "J100" and pos("D") ** 2 == 16 and pos("F") ** 2 == 36
A("mixed-analogy", "an-p22", "Select the related cluster: **D16 : F36 :: H64 : ?**", c, ["H36", "J81", "K100"],
  f"The number is the **square of the letter's position**: D = 4 → 16, F = 6 → 36, H = 8 → 64. Next: J = 10 → 10² = 100 → **{c}**.",
  diff="hard", t=55)
c = str(psum("SHAM")); assert c == "41" and psum("RAM") == 32
A("mixed-analogy", "an-p23", "Select the related number: **RAM : 32 :: SHAM : ?**", c, ["40", "42", "44"],
  f"R + A + M = 18 + 1 + 13 = 32 — the plain **sum of letter positions**. SHAM = 19 + 8 + 1 + 13 = **{c}**.",
  diff="easy")
c = str(psum("PIN")); assert c == "39" and psum("CAT") == 24
A("mixed-analogy", "an-p23", "Select the related number: **CAT : 24 :: PIN : ?**", c, ["38", "40", "41"],
  f"C + A + T = 3 + 1 + 20 = 24 (plain sum). P + I + N = 16 + 9 + 14 = **{c}**.",
  diff="medium")
c = str(psum("COW") * 2); assert c == "82" and psum("DOG") * 2 == 52
A("mixed-analogy", "an-p23", "Select the related number: **DOG : 52 :: COW : ?**", c, ["41", "80", "84"],
  f"D + O + G = 4 + 15 + 7 = 26, and 26 × 2 = 52 — **sum of positions, doubled**. COW: 3 + 15 + 23 = 41, doubled = **{c}**. (41 alone is the trap.)",
  diff="medium")
c = "Painter : Brush"
A("mixed-analogy", "an-p24",
  "Choose the pair related in the same way as **Tailor : Needle**.", c,
  ["Doctor : Hospital", "Author : Book", "Farmer : Crop"],
  "A tailor **uses** a needle — worker : tool. A painter uses a **brush** ✓. Hospital is a workplace; book and crop are products.",
  diff="medium")
c = "Bee : Hive"
A("mixed-analogy", "an-p24",
  "Choose the pair related in the same way as **Lion : Den**.", c,
  ["Lion : Roar", "Dog : Puppy", "Horse : Neigh"],
  "A den is the **home** of a lion. The home of a bee is a **hive** ✓. Roar and neigh are sounds; puppy is a young one.",
  diff="medium")
c = "Deer : Fawn"
A("mixed-analogy", "an-p24",
  "Choose the pair related in the same way as **Cow : Calf**.", c,
  ["Horse : Mare", "Sheep : Wool", "Goat : Bleat"],
  "A calf is the **young one** of a cow. The young one of a deer is a **fawn** ✓. Mare is the female (not the baby), wool a product, bleat a sound.",
  diff="medium")
c = str(pos("E") ** 2); assert c == "25" and pos("C") ** 2 == 9
A("mixed-analogy", "an-p25", "Select the related number: **C : 9 :: E : ?**", c, ["10", "15", "5"],
  f"C is the 3rd letter and 9 = 3² — **square of the position**. E is 5th, so 5² = **{c}**.",
  diff="easy")
c = str(rpos("D")); assert c == "23" and rpos("B") == 25
A("mixed-analogy", "an-p25", "Select the related number: **B : 25 :: D : ?**", c, ["4", "8", "24"],
  f"B(2) pairs with 25 = 27 − 2 — the **reverse position** (Z = 1, Y = 2 ...). D is 4th, so 27 − 4 = **{c}**.",
  diff="medium", shortcut="Letter counts down while the number counts up? Try 27 − position.")
c = str(2 * pos("D")); assert c == "8" and 2 * pos("A") == 2
A("mixed-analogy", "an-p25", "Select the related number: **A : 2 :: D : ?**", c, ["4", "6", "5"],
  f"A is 1st and 2 = 2 × 1 — **twice the position**. D is 4th, so 2 × 4 = **{c}**.",
  diff="easy")

# ================= number-set-analogy =================
assert 5 * 2 + 1 == 11 and 11 * 2 + 1 == 23
assert 7 * 2 + 1 == 15 and 15 * 2 + 1 != 30
assert 9 * 2 + 1 == 19 and 19 * 2 + 1 != 38
assert 4 * 2 + 1 == 9 and 9 * 2 + 1 != 20
A("number-set-analogy", "an-p26",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(6, 13, 27)** and **(8, 17, 35)**",
  "(5, 11, 23)", ["(7, 15, 30)", "(9, 19, 38)", "(4, 9, 20)"],
  "Rule: **×2 then +1** each step — 6 → 13 → 27 and 8 → 17 → 35. Test: 5 → 11 → 23 ✓. "
  "The others fail at the last number: 15×2+1 = 31 ≠ 30, 19×2+1 = 39 ≠ 38, 9×2+1 = 19 ≠ 20. **Answer: (5, 11, 23).**",
  diff="medium", t=55)
assert 4 * 2 - 1 == 7 and 7 * 2 - 1 == 13
assert 4 * 2 - 1 != 8 and 6 * 2 - 1 == 11 and 11 * 2 - 1 != 20 and 9 * 2 - 1 != 18
A("number-set-analogy", "an-p26",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(3, 5, 9)** and **(5, 9, 17)**",
  "(4, 7, 13)", ["(4, 8, 15)", "(6, 11, 20)", "(9, 18, 35)"],
  "Rule: **×2 then −1** each step — 3 → 5 → 9 and 5 → 9 → 17. Test: 4 → 7 → 13 ✓. "
  "The others break at the second or third number (4×2−1 = 7 ≠ 8; 11×2−1 = 21 ≠ 20; 9×2−1 = 17 ≠ 18). **Answer: (4, 7, 13).**",
  diff="medium", t=55)
assert 5 * 3 == 15 and 15 * 3 == 45
assert 9 * 3 != 26 and 18 * 3 != 52 and 21 * 3 != 64
A("number-set-analogy", "an-p26",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(2, 6, 18)** and **(4, 12, 36)**",
  "(5, 15, 45)", ["(3, 9, 26)", "(6, 18, 52)", "(7, 21, 64)"],
  "Rule: **×3** each step — 2 → 6 → 18 and 4 → 12 → 36. Test: 5 → 15 → 45 ✓. "
  "The others fail at the third number (27, 54, 63 needed). **Answer: (5, 15, 45).**",
  diff="medium")
assert 7 * 4 == 28 and 6 * 5 != 32 and 9 * 3 != 36 and 8 * 2 != 18
A("number-set-analogy", "an-p27",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(3, 8, 24)** and **(5, 6, 30)**",
  "(7, 4, 28)", ["(6, 5, 32)", "(9, 3, 36)", "(8, 2, 18)"],
  "Rule: **third = first × second** — 3 × 8 = 24 and 5 × 6 = 30. Test: 7 × 4 = 28 ✓. "
  "The others give 30, 27 and 16 — not 32, 36, 18. **Answer: (7, 4, 28).**",
  diff="easy")
assert 2 ** 2 + 6 ** 2 == 40 and 5 ** 2 + 4 ** 2 != 40 and 6 ** 2 + 3 ** 2 != 36 and 1 + 8 ** 2 != 64
A("number-set-analogy", "an-p27",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(4, 5, 41)** and **(3, 7, 58)**",
  "(2, 6, 40)", ["(5, 4, 40)", "(6, 3, 36)", "(1, 8, 64)"],
  "Rule: **third = a² + b²** — 16 + 25 = 41 and 9 + 49 = 58. Test: 4 + 36 = 40 ✓. "
  "The others give 41, 45 and 65. **Answer: (2, 6, 40).**",
  diff="hard", t=60)
assert 2 * (3 + 7) == 20 and 2 * (4 + 6) != 22 and 2 * (2 + 12) != 26 and 2 * (7 + 7) != 26
A("number-set-analogy", "an-p27",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(5, 9, 28)** and **(6, 8, 28)**",
  "(3, 7, 20)", ["(4, 6, 22)", "(2, 12, 26)", "(7, 7, 26)"],
  "Rule: **third = 2 × (first + second)** — 2 × 14 = 28 in both sets. Test: 2 × 10 = 20 ✓. "
  "The others need 20, 28 and 28. **Answer: (3, 7, 20).**",
  diff="medium")
assert 5 ** 2 + 1 == 26 and 5 ** 3 + 1 == 126
assert 6 ** 3 + 1 != 215 and 2 ** 3 + 1 != 8 and 7 ** 3 + 1 != 342
A("number-set-analogy", "an-p28",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(3, 10, 28)** and **(4, 17, 65)**",
  "(5, 26, 126)", ["(6, 37, 215)", "(2, 5, 8)", "(7, 50, 342)"],
  "Rule: **(a, a² + 1, a³ + 1)** — 9 + 1, 27 + 1 and 16 + 1, 64 + 1. Test: 5 → 26 → 126 ✓. "
  "The others need 217, 9 and 344. **Answer: (5, 26, 126).**",
  diff="hard", t=60)
assert 5 ** 3 == 125 and 4 ** 3 != 60 and 6 ** 3 != 206 and 7 ** 3 != 334
A("number-set-analogy", "an-p28",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(2, 4, 8)** and **(3, 9, 27)**",
  "(5, 25, 125)", ["(4, 16, 60)", "(6, 36, 206)", "(7, 49, 334)"],
  "Rule: **(a, a², a³)** — 2, 4, 8 and 3, 9, 27. Test: 5, 25, 125 ✓. "
  "The others end in 60, 206, 334 instead of 64, 216, 343. **Answer: (5, 25, 125).**",
  diff="medium")
assert 6 + 6 ** 2 == 42 and 4 + 4 ** 2 != 22 and 8 + 8 ** 2 != 74 and 3 + 3 ** 2 != 15
A("number-set-analogy", "an-p28",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(7, 49, 56)** and **(5, 25, 30)**",
  "(6, 36, 42)", ["(4, 16, 22)", "(8, 64, 74)", "(3, 9, 15)"],
  "Rule: **(a, a², a + a²)** — 7, 49, 7 + 49 = 56 and 5, 25, 5 + 25 = 30. Test: 6, 36, 6 + 36 = 42 ✓. "
  "The others would need 20, 72 and 12 as last terms. **Answer: (6, 36, 42).**",
  diff="medium")
assert 6 * 8 == 48 and 3 * 9 != 24 and 7 * 9 != 56 and 2 * 8 != 18
A("number-set-analogy", "an-p29",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(5, 35, 7)** and **(4, 36, 9)**",
  "(6, 48, 8)", ["(3, 24, 9)", "(7, 56, 9)", "(2, 18, 8)"],
  "The **middle number = first × third**: 5 × 7 = 35 and 4 × 9 = 36. Test: 6 × 8 = 48 ✓. "
  "The others need 27, 63 and 16 in the middle. **Answer: (6, 48, 8).**",
  diff="medium", t=55)
assert (6 + 18) / 2 == 12 and (4 + 15) / 2 != 9 and (7 + 14) / 2 != 10 and (9 + 20) / 2 != 14
A("number-set-analogy", "an-p29",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(8, 13, 18)** and **(5, 11, 16)**",
  "(6, 12, 18)", ["(4, 9, 15)", "(7, 10, 14)", "(9, 14, 20)"],
  "The **middle number is the average of the outer two**: (8 + 18)/2 = 13 and (5 + 16)/2 = 11. "
  "Test: (6 + 18)/2 = 12 ✓. The others give averages 9.5, 10.5 and 14.5. **Answer: (6, 12, 18).**",
  diff="medium", t=55)
assert 9 + 8 == 17 and 7 + 9 != 15 and 6 + 5 != 12 and 10 + 14 != 25
A("number-set-analogy", "an-p29",
  "Select the set in which the numbers are related in the same way as the numbers of the following sets. "
  "(Operations on whole numbers only.) **(14, 5, 9)** and **(20, 8, 12)**",
  "(17, 9, 8)", ["(15, 7, 9)", "(12, 6, 5)", "(25, 10, 14)"],
  "The **first number = second + third**: 5 + 9 = 14 and 8 + 12 = 20. Test: 9 + 8 = 17 ✓. "
  "The others give 16, 11 and 24. **Answer: (17, 9, 8).**",
  diff="medium", t=55)

upsert(d["practice"], NQ)
d["pyqPatterns"] = PYQS

finish("analogy", d)
