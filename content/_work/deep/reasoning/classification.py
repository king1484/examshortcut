"""Classification topic runner: applies the three content modules, adds pyqPatterns, finishes."""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa

m1 = importlib.import_module("classification_1")
m2 = importlib.import_module("classification_2")
m3 = importlib.import_module("classification_3")

d = load("classification")
qs = m1.apply(d) + m2.apply(d) + m3.apply(d)
upsert(d["practice"], qs)

d["pyqPatterns"] = [
    PYQ("Standard odd one out (three alike, one different)", "very common",
        "Four items - numbers, letters, words or mixed - where exactly three share one clear feature.",
        "Test objective rules first (spelling, letter steps, number properties), then function, then category. "
        "The rule must keep exactly three items together; the item that breaks it is the answer.",
        "classification-idea", "**17, 26, 35, 44**", "All end in 5 or 6 (trap). Real rule: +9 each. That fits all - so go deeper: "
        "digit sums are 8, 8, 8, 8 too. Every option obeys +9, so the tie-break is another property: 17 is **prime**, the rest are not → **17**."),
    PYQ("Two-level (tie-break) odd one out", "common",
        "The first rule you find keeps all four (or none) together, so a second, deeper property decides.",
        "When level 1 fails (all squares, all even, all +7), test the next layer: are the roots prime? Is the digit "
        "sum odd? Keep going until exactly one item splits away.",
        "classification-idea", "**121, 169, 225, 289**", "All are perfect squares (11², 13², 15², 17²). Deeper: 11, 13, 17 are prime but 15 is not → **225**."),
    PYQ("Category break (animals, plants, living things)", "very common",
        "Four words from nearby nature groups: animals, birds, fruits, vegetables, flowers, trees.",
        "Name the group of three. The traps are words from the same habitat or colour - the answer is the one from a "
        "different biological category (mammal among reptiles, vegetable among fruits).",
        "word-classification", "**Snake, Lizard, Crocodile, Whale**", "All live in/near water, but snake, lizard and crocodile are reptiles; the whale is a **mammal** → **Whale**."),
    PYQ("Function / use break", "common",
        "Four objects or devices, three of which serve the same function.",
        "Ask 'what does it do?' rather than 'where is it found?'. Three input devices and one output device, or three "
        "measuring instruments and one storage item - the different function is the answer.",
        "word-classification", "**Keyboard, Mouse, Scanner, Monitor**", "Keyboard, mouse and scanner send data **into** the computer (input devices); the monitor only **displays** it (output) → **Monitor**."),
    PYQ("Prime vs composite", "very common",
        "Four numbers of similar size; three are prime or three are composite.",
        "Test divisibility by 2, 3, 5, 7 quickly. Watch traps: 91 = 7 × 13 and 87 = 3 × 29 look prime but are not; 2 is the only even prime.",
        "number-classification", "**17, 19, 23, 27**", "17, 19, 23 are prime. 27 = 3 × 9 (or 3³) is composite → **27**."),
    PYQ("Perfect square / perfect cube", "common",
        "Three numbers are squares (or cubes) and one is not, though all look 'special'.",
        "Know squares to 20² = 400 and cubes to 12³ = 1728. Then apply the tie-break if needed: of the squares, are "
        "three roots prime?",
        "number-classification", "**64, 125, 216, 100**", "64 = 4³, 125 = 5³, 216 = 6³ are cubes; 100 is only a square → **100**."),
    PYQ("Constant step inside the cluster", "common",
        "Four letter clusters; in three of them the letters move by the same step every time.",
        "Write the step tuple for each cluster (positions via EJOTY). Three clusters share one tuple (e.g. +2, +2); "
        "the odd one has a different tuple or unequal steps.",
        "letter-classification", "**BDF, HJL, NPR, PQR**", "B→D→F, H→J→L, N→P→R all jump **+2, +2**; P→Q→R jumps +1, +1 → **PQR**."),
    PYQ("Word pairs: relation break", "very common",
        "Four pairs; three share the same relation (adult : young, worker : tool, male : female).",
        "Say the relation of the first pair as a sentence, then test each option with the same sentence. The pair with "
        "a different relation (or a reversed direction) is the odd one.",
        "pair-classification", "**Cow : Calf, Horse : Foal, Dog : Kitten, Sheep : Lamb**",
        "Calf, foal and lamb are the correct **young ones**; a kitten is the young of a cat, not a dog → **Dog : Kitten**."),
    PYQ("GK pairs: one factually wrong pair", "common",
        "Four country-capital, country-currency or instrument-quantity pairs; one pair states a wrong fact.",
        "Check each fact, not the relation's shape - all four have the same shape, but one pairing is factually wrong.",
        "pair-classification", "**Rome : Italy, Oslo : Norway, Madrid : Portugal, Cairo : Egypt**",
        "Madrid is the capital of **Spain**, not Portugal → **Madrid : Portugal** is the wrong pair."),
    PYQ("Chain sets (a, b, c): same operation twice", "common",
        "Sets of three numbers such as (2, 4, 8), (3, 6, 12); three sets follow one rule, one set breaks it.",
        "Find the repeated step of each set (×2, ×2 or +5, +5). The set whose middle step or last number breaks the "
        "chain is the odd one.",
        "number-set-classification", "**(2, 4, 8), (3, 6, 12), (5, 10, 20), (4, 9, 16)**",
        "The first three double each step (×2, ×2). (4, 9, 16) is a squares chain (2², 3², 4²) → **(4, 9, 16)**."),
]

finish("classification", d)
