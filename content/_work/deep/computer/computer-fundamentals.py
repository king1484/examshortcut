"""Phase-2 deep content for computer/computer-fundamentals. Run: py -3 computer-fundamentals.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from cf_part1 import build_generations, build_types, build_basic_org
from cf_part2 import build_pioneers, build_abbreviations
from cf_hard import add_hard


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Generation-to-technology mapping", "very common",
      "The stem names a technology (vacuum tube, transistor, IC, microprocessor) or a machine (ENIAC, IBM 360) and asks its generation, or the reverse. Statement variants ask which feature belongs to which generation.",
      "Recall the ladder vacuum tube (1st) → transistor (2nd) → IC (3rd) → microprocessor (4th) → AI (5th) and match the technology first, the years second — year ranges differ between books but the technology order never does.",
      "cf-generations",
      "Third-generation computers were built around:",
      "Integrated Circuits (ICs) — whole circuits printed on one silicon chip; they brought keyboards, monitors and operating systems."),
    P("Full form / abbreviation recall", "very common",
      "'What is the full form of BIOS / ALU / MICR / UPS?' or a wrongly-matched pair where one expansion has one wrong word.",
      "Expand letter by letter from the family table (CPU family, memory family, device family). The classic traps: UPS = Uninterruptible (not Uninterrupted), POST = Power-On Self-Test (not Power On System Test), VDU = Visual (not Video).",
      "cf-abbreviations",
      "The full form of POST is:",
      "Power-On Self-Test — the start-up diagnostic that checks hardware before the OS loads."),
    P("Firsts in computing history", "common",
      "'First commercial computer', 'first electronic digital computer', 'first microprocessor', 'first stored-program computer' — a superlative with machine names as options.",
      "Keep the firsts chain pinned: ABC 1942 (first electronic digital) → ENIAC 1946 (first general-purpose electronic) → EDSAC 1949 (first stored-program) → UNIVAC-I 1951 (first commercial) → Intel 4004 1971 (first microprocessor). Read the exact adjective in the stem.",
      "cf-generations",
      "Which machine is regarded as the first commercially available computer?",
      "UNIVAC-I (1951) — ENIAC was earlier but experimental; UNIVAC-I was the first sold to businesses."),
    P("CPU part / machine cycle", "common",
      "'Which unit performs arithmetic or comparison?', 'which register holds the next address?', 'the correct order of fetch/decode/execute/store'.",
      "CPU = ALU (all maths and logic) + CU (direction only, no calculation) + registers (fastest storage). The cycle is always Fetch → Decode → Execute → Store; reversed Decode/Fetch or Execute/Store pairs are the planted traps.",
      "cf-basic-org",
      "In the machine cycle, the step that interprets what the instruction means is:",
      "Decode — done by the Control Unit, between Fetch (bring it) and Execute (do it)."),
    P("Odd-one-out among translators/types", "common",
      "'Which is not a programming language?', 'which is not a translator?', 'which one is a markup language?' — three options from one family, one from another.",
      "Classify each option first: HTML = markup (not programming); assembler = assembly-language translator; compiler/interpreter = high-level translators. The odd option is usually a famous name placed in the wrong family.",
      "cf-pioneers-languages",
      "Which of the following is not a translator?",
      "HTML — it is a markup language. Assembler, compiler and interpreter are all translators."),
    P("Computer classification and use-case matching", "common",
      "A workplace or workload is described — bank records, railway reservation (mainframe), weather forecasting (supercomputer), a single user's laptop (micro), a hybrid petrol-pump unit — and the class is asked.",
      "Use the two ladders: size (Super → Mainframe → Mini → Micro) and principle (analog measures continuous, digital counts 0/1, hybrid does both). Bulk transactions for thousands of users = mainframe; one enormous calculation = supercomputer.",
      "cf-types",
      "A petrol-pump machine that measures fuel flow continuously and prints the price digitally is a:",
      "Hybrid computer — analog measurement combined with digital computation."),
    P("Pioneer and language-level matching", "common",
      "'Who invented the mouse / WWW / punched cards?', 'the first programmer was', 'SQL belongs to which language generation?' — name-contribution or language-level pairs.",
      "Hold the pioneer table (Babbage, Ada, Turing, von Neumann, Hopper, Berners-Lee, Engelbart, Hollerith) and the GL ladder (1GL machine → 2GL assembly → 3GL high-level → 4GL SQL → 5GL AI). Watch the classic swaps: Ada vs Hopper, WWW vs Internet, HTML vs programming language.",
      "cf-pioneers-languages",
      "The first-generation (1GL) language that needs no translator is:",
      "Machine language — pure 0s and 1s executed directly by the CPU; assembly (2GL) needs an assembler."),
]

if __name__ == "__main__":
    subs = [build_generations(), build_types(), build_basic_org(),
            build_pioneers(), build_abbreviations()]
    add_hard(subs)
    apply_topic("computer-fundamentals", subs, PYQ)
