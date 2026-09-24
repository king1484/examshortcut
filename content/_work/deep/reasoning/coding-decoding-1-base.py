"""coding-decoding step 1: fix existing errors, clean garbled trick examples, add the two new
subtopic shells (symbol-coding, language-coding), rewrite topic-level pyqPatterns."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _lib import *  # noqa

_spec = importlib.util.spec_from_file_location("cdh", os.path.join(HERE, "coding-decoding-helpers.py"))
cdh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cdh)

T = "coding-decoding"
d = load(T)

# ---------- 1. fix rsn-coding-15 (TREE +1 is USFF, not USFD) ----------
assert shift("TREE", 1) == "USFF" and psum("TREE") == 48
assert shift("LEAF", 1) == "MFBG" and psum("LEAF") == 24
patch_q(d, "rsn-coding-15",
        q="In a certain code, **'TREE' is written as 'USFF48'** — each letter moves one step forward "
          "(TREE → USFF) and the word's position sum (20+18+5+5 = 48) is written after it. "
          "How is **LEAF** written?",
        solution="Letter part: LEAF +1 → M, F, B, G = **MFBG**. Number part: L(12)+E(5)+A(1)+F(6) = **24**. "
                 "Code = **MFBG24**.")

# ---------- 2. clean garbled trick examples (titles unchanged) ----------
assert shift("CAT", 3) == "FDW" and shift("DOG", 3) == "GRJ"
s = get_sub(d, "coding-idea")
s["tricks"][0]["example"] = {
    "q": "**Q.** If CAT is coded as **FDW**, how is DOG coded?\n\n**Sol.** C→F is +3, A→D is +3, T→W is +3, "
         "so the rule is a flat +3. D+3 = G, O+3 = R, G+3 = J → **GRJ**.",
    "solution": "The tuple you computed on the sample pair is the rule — apply the same tuple to the new word "
                "and never guess a fresh rule.",
}
assert shift("MANGO", 2) == "OCPIQ" and shift("LWKEG", -2) == "JUICE"
s = get_sub(d, "letter-shift-coding")
# existing text had JUICE +2 = LWKGE; the correct code is LWKEG
assert shift("JUICE", 2) == "LWKEG"
s["concept"] = s["concept"].replace("**LWKGE**", "**LWKEG**")
s["tricks"][0]["example"]["q"] = s["tricks"][0]["example"]["q"].replace(
    "C+2 = E, E+2 = G → **LWKGE**", "C+2 = E, E+2 = G → **LWKEG**")
assert "LWKGE" not in s["concept"] + s["tricks"][0]["example"]["q"]
s["tricks"][1]["example"] = {
    "q": "**Q.** If MANGO is coded as **OCPIQ**, which word is coded as **LWKEG**?\n\n**Sol.** MANGO → OCPIQ is "
         "+2 on every letter, so decoding means −2 on every letter: L→J, W→U, K→I, E→C, G→E → **JUICE**.",
    "solution": "Decoding is the same question played backwards — subtract the shift, don't invent a new rule.",
}
assert psum("CAT") == 24
s = get_sub(d, "number-coding")
s["tricks"][1]["example"] = {
    "q": "**Q.** In position-sum coding, is CAT coded as 24?\n\n**Sol.** C = 3, A = 1 and T = Y − 5 = 25 − 5 = 20. "
         "Total = 3 + 1 + 20 = **24** ✓.",
    "solution": "Anchors (E=5, J=10, O=15, T=20, Y=25) turn position look-ups into small ± adjustments.",
}

# ---------- 3. new subtopic shells ----------
add_sub(d, {
    "id": "symbol-coding",
    "title": "Symbol and digit coding",
    "concept": "Letters (or digits) are replaced by **symbols or digits**, one fixed code per letter. Either a "
               "code table is given (sometimes with extra conditions), or you get a few words with their codes "
               "and must work out which symbol stands for which letter by matching common letters. Once a "
               "letter's code is known it never changes inside the question.",
    "formulas": [],
    "tricks": [
        {
            "title": "Common letters ↔ common symbols",
            "body": "When two coded words share letters, their codes share exactly the same number of symbols. "
                    "Circle the shared letters and the shared symbols — they belong to each other. What is left "
                    "over in each word belongs to the left-over letters.",
            "example": {
                "q": "**Q.** 'PEN' is coded '@ # %' and 'NET' is coded '% & #' (order of symbols may differ). "
                     "What is the code for P?",
                "solution": "Common letters E, N ↔ common symbols #, %. So P takes the remaining symbol of PEN → "
                            "**@** (and T = &).",
            },
        },
        {
            "title": "Conditions before the table",
            "body": "In condition-type questions, first check the conditions on the letter group (first letter "
                    "vowel? last letter consonant?). Only if no condition applies do you code straight from the table.",
            "example": None,
        },
    ],
    "mistakes": [
        "Assuming symbols appear in the same order as the letters when the question says the order may differ.",
        "Coding straight from the table without first checking whether a condition applies.",
        "Applying two conditions at once when the question says only the first matching condition applies.",
    ],
}, after="number-coding")

add_sub(d, {
    "id": "language-coding",
    "title": "Language (sentence) coding with common words",
    "concept": "A 'code language' writes whole sentences as code words: 'pa ka ni' for 'good morning sir'. The "
               "code words are usually **jumbled** (not in the same order as the words). You find a word's code "
               "by comparing sentences: a word common to two sentences has its code among the code words common "
               "to those two sentences. When the comparison leaves two choices, the code **cannot be determined**.",
    "formulas": [],
    "tricks": [
        {
            "title": "Intersect, then subtract",
            "body": "For a word, take the code words of every sentence that contains it (intersect), then remove "
                    "code words already fixed for other words. One code left = answer; two left = cannot be "
                    "determined (unless the options force it).",
            "example": {
                "q": "**Q.** 'sun is hot' = 'ta mo ri', 'sun is bright' = 'ri ze mo'. Code for 'hot'?",
                "solution": "'sun is' is common → 'ri mo' is common. Sentence 1 left: hot ↔ **ta**.",
            },
        }
    ],
    "mistakes": [
        "Matching code words by position — the code order is usually jumbled.",
        "Picking one of two equally possible codes instead of answering 'cannot be determined'.",
        "Forgetting that a code word already fixed for another word cannot be reused.",
    ],
}, after="substitution-coding")

# ---------- 4. topic-level pyqPatterns ----------
assert shift("PEN", 2) == "RGP" and shift("RING", 2) == "TKPI"
assert shift("TKPI", -2) == "RING"
assert rev(shift("GOLD", 1)) == "EMPH"
assert opp("MILK") == "NROP"
assert psum("BAT") == 23 and psum("CAR") == 22
d["pyqPatterns"] = [
    PYQ("Letter-shift coding of a new word", "very common",
        "A sample word and its code are given ('If PEN is written as RGP...'). Every letter of the code is a "
        "fixed number of places ahead of or behind the original letter, or the shift changes slot by slot.",
        "Write the shift under each letter of the sample (e.g. +2, +2, +2). Apply exactly the same shifts to the "
        "new word. Remember that after Z you come back to A.",
        "letter-shift-coding",
        "If PEN is written as RGP, how is RING written?",
        "P→R, E→G, N→P: +2 each. R+2 = T, I+2 = K, N+2 = P, G+2 = I → **TKPI**."),
    PYQ("Decoding: find the original word", "common",
        "The code of the new word is given and the real word is asked ('Which word is written as TKPI?').",
        "Find the rule from the sample, then run it backwards: subtract where the rule adds, un-reverse where it "
        "reverses. Check the answer by coding it forward once.",
        "letter-shift-coding",
        "If PEN is written as RGP, which word is written as TKPI?",
        "The rule is +2, so decode with −2: T→R, K→I, P→N, I→G → **RING**."),
    PYQ("Reversal and reverse-plus-shift coding", "common",
        "Read the code from right to left. If you see the original word, or the original word with every letter "
        "moved by the same amount, the rule contains a reversal.",
        "Reverse the new word, then apply the same shift as the sample. Keep the same order of steps (reverse "
        "then shift, or shift then reverse) that the sample used.",
        "reverse-coding",
        "If GOLD is written as EMPH, how is SILK written?",
        "GOLD +1 = HPME; reversed = EMPH ✓. SILK +1 = TJML; reversed = **LMJT**."),
    PYQ("Opposite-letter coding", "common",
        "Each code letter and its original letter add up to 27 in position (A↔Z, M↔N). Codes look 'far away' "
        "from the word, e.g. MILK → NROP.",
        "Confirm the 27 total on two letters, then write the opposite of each letter of the new word. If the "
        "code is also reversed, reverse at the end.",
        "reverse-coding",
        "If MILK is written as NROP, how is CAKE written?",
        "M(13)+N(14) = 27, so opposite letters. C↔X, A↔Z, K↔P, E↔V → **XZPV**."),
    PYQ("Word to number coding", "very common",
        "A word is given a number ('BAT = 23'). The number is built from alphabet positions: plain sum, sum "
        "plus/minus or times a constant, weighted sum, reverse positions, or the letter positions written side by side.",
        "Find the plain position sum of the sample first and compare it with the code. The gap (+k, ×k, or a "
        "letter-count link) is the rule. Apply the same rule to the new word.",
        "number-coding",
        "If BAT = 23, what is CAR?",
        "B+A+T = 2+1+20 = 23, a plain sum. C+A+R = 3+1+18 = **22**."),
    PYQ("Substitution (renaming) chains", "common",
        "'Sky is called sea, sea is called water...' followed by a real-life question such as 'where do fish live?'",
        "First answer the real-life question in your head (fish live in the sea). Then give the code name of that "
        "answer (sea is called water) — rename exactly once.",
        "substitution-coding",
        "If milk is called water, water is called juice and juice is called tea, what do we drink when thirsty?",
        "Real answer: water. 'Water' is called **juice** in this code."),
    PYQ("Language coding with common words", "very common",
        "Two to four sentences with jumbled code words ('good morning sir' = 'pa ka ni'); code of one word asked, "
        "or 'which could be the code', or 'cannot be determined'.",
        "Take the sentences that contain the word, keep the code words common to all of them, remove codes already "
        "fixed for other words. One code left = answer; two left = cannot be determined.",
        "language-coding",
        "'sun is hot' = 'ta mo ri' and 'sun is bright' = 'ri ze mo'. What is the code for 'bright'?",
        "'sun is' ↔ 'ri mo' (common). Sentence 2 left over: bright ↔ **ze**."),
    PYQ("Letter-to-symbol / digit coding", "common",
        "Letters or digits are replaced by symbols, either from a given table (sometimes with conditions) or "
        "from a few coded words that share letters.",
        "Match shared letters with shared symbols across the given words. For tables, check the conditions first, "
        "then code letter by letter.",
        "symbol-coding",
        "If ROSE = 6821 and SORE = 2861, what is the code for O?",
        "The digits follow the letter order: R = 6, O = 8, S = 2, E = 1. Check: SORE = 2 8 6 1 ✓. So O = **8**."),
    PYQ("Rearrangement and mixed-rule coding", "occasional",
        "The code uses the same letters as the word but in a new order (pairs swapped, halves reversed, first "
        "and last interchanged), or two rules act together (vowels +1 and consonants −1).",
        "Compare letter by letter: are the letters the same (rearrangement) or changed (shift)? For rearrangement, "
        "note which slot went where; for mixed rules, note which group of letters got which change.",
        "coding-idea",
        "If PLANET is written as LPNATE, how is FOREST written?",
        "Letters are swapped in pairs: PL→LP, AN→NA, ET→TE. FO→OF, RE→ER, ST→TS → **OFERTS**."),
]
assert "".join(a[1] + a[0] for a in ["PL", "AN", "ET"]) == "LPNATE"
assert "".join(a[1] + a[0] for a in ["FO", "RE", "ST"]) == "OFERTS"
assert cdh.fixed([["sun", "is", "hot"], ["sun", "is", "bright"]],
                 [["ta", "mo", "ri"], ["ri", "ze", "mo"]], "bright") == "ze"
assert cdh.fixed([["sun", "is", "hot"], ["sun", "is", "bright"]],
                 [["ta", "mo", "ri"], ["ri", "ze", "mo"]], "hot") == "ta"
finish(T, d)
