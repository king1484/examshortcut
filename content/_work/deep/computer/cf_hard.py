"""computer-fundamentals — hard-difficulty additions, appended after the part builders."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def add_hard(subs):
    by = {s.id: s for s in subs}

    S = by["cf-generations"]
    S.q("cf-gen-p4", "hard",
        "Consider the statements:\n1. First-generation computers used magnetic drums for memory.\n2. Multiprogramming became practical with the second generation.\n3. Integrated circuits made operating systems practical.\nWhich are correct?",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "1 and 3 only",
        "Statement 1 is correct — magnetic drums were first-generation memory. Statement 2 is wrong: **multiprogramming belongs to the third generation** (IC era, with OS support). Statement 3 is correct — IC-based third-generation machines ran operating systems.",
        "2nd generation = transistors + languages; OS + multiprogramming = 3rd generation.", 35)
    S.q("cf-gen-p2", "hard",
        "Match the machine to its generation:\nA. UNIVAC-I  B. IBM 1401  C. IBM 360  D. Intel 4004",
        ["A-1, B-2, C-3, D-4", "A-2, B-1, C-3, D-4", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1"],
        "A-1, B-2, C-3, D-4",
        "UNIVAC-I (1951, vacuum tubes) → 1st; IBM 1401 (transistors) → 2nd; IBM 360 (1964, ICs) → 3rd; Intel 4004 (1971, single-chip CPU) → 4th.",
        "The four machines walk the four rungs in order.", 35)

    S = by["cf-types"]
    S.q("cf-typ-p2", "hard",
        "Consider the statements:\n1. An analog computer works directly on measurements of continuous quantities.\n2. Every digital computer is also a hybrid computer.\n3. A minicomputer is more powerful than a mainframe.\nWhich are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "1 only",
        "Statement 1 is the definition of analog computing. Statement 2 is wrong — digital and hybrid are separate classes. Statement 3 is wrong — the mainframe is **more** powerful than a minicomputer (Super → Mainframe → Mini → Micro).",
        "Two wrong statements use reversed ladders — check each against its definition.", 35)
    S.q("cf-typ-p1", "hard",
        "Four computers are arranged as: P (weather simulation), Q (bank's central ledger for thousands of branches), R (a college department server for 60 users), S (a student's laptop). Which assignment of class is correct?",
        ["P-Super, Q-Mainframe, R-Mini, S-Micro", "P-Mainframe, Q-Super, R-Mini, S-Micro", "P-Super, Q-Mainframe, R-Micro, S-Mini", "P-Mainframe, Q-Mainframe, R-Super, S-Micro"],
        "P-Super, Q-Mainframe, R-Mini, S-Micro",
        "One giant scientific problem → **supercomputer**; thousands of simultaneous transactions → **mainframe**; department-level multi-user → **minicomputer**; single personal user → **microcomputer**.",
        "Workload size maps to the ladder rung: one problem / one organisation / one department / one person.", 40)

    S = by["cf-basic-org"]
    S.q("cf-org-p1", "hard",
        "Match the CPU register to its job:\nA. Program Counter  B. Instruction Register  C. Accumulator  D. Memory Address Register",
        ["A-next instruction's address, B-current instruction, C-ALU result, D-address being accessed in memory",
         "A-current instruction, B-next instruction's address, C-ALU result, D-address being accessed in memory",
         "A-ALU result, B-current instruction, C-next instruction's address, D-address being accessed in memory",
         "A-next instruction's address, B-ALU result, C-current instruction, D-address being accessed in memory"],
        "A-next instruction's address, B-current instruction, C-ALU result, D-address being accessed in memory",
        "**PC** points to the next instruction; **IR** holds the instruction being executed; the **Accumulator** collects ALU results; the **MAR** holds the memory address currently being read or written.",
        "PC-Next, IR-Now, ACC-Answer, MAR-Address.", 40)
    S.q("cf-org-p3", "hard",
        "Consider the statements about the system bus:\n1. The data bus carries information in both directions.\n2. The address bus is unidirectional, from CPU to memory.\n3. The width of the data bus decides how many bits move at a time.\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are standard: data flows both ways on the **data bus**; the **address bus** goes one way (CPU → memory); a '32-bit/64-bit' label on a processor describes the **data-bus/register width**.",
        "Data both ways, address one way, width = bits at once.", 35)

    S = by["cf-pioneers-languages"]
    S.q("cf-pio-p1", "hard",
        "Match the person to the contribution:\nA. Herman Hollerith  B. Grace Hopper  C. Douglas Engelbart  D. Tim Berners-Lee",
        ["A-punched-card tabulating machine, B-COBOL and early compiler, C-computer mouse, D-World Wide Web",
         "A-computer mouse, B-COBOL and early compiler, C-punched-card tabulating machine, D-World Wide Web",
         "A-punched-card tabulating machine, B-World Wide Web, C-computer mouse, D-COBOL and early compiler",
         "A-COBOL and early compiler, B-punched-card tabulating machine, C-World Wide Web, D-computer mouse"],
        "A-punched-card tabulating machine, B-COBOL and early compiler, C-computer mouse, D-World Wide Web",
        "Hollerith's punched-card machine processed the 1890 US Census (his firm fed into IBM); Hopper pioneered COBOL and wrote an early **compiler**; Engelbart built the first **mouse**; Berners-Lee created the **WWW**.",
        "Census, COBOL, click, web — four different decades, four different people.", 40)
    S.q("cf-pio-p3", "hard",
        "Consider the statements:\n1. Assembly language needs an assembler, not a compiler.\n2. A 4GL such as SQL is closer to human language than C.\n3. HTML is a third-generation programming language.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are standard (assembly → assembler; SQL is a 4GL near plain English). Statement 3 is wrong: **HTML is a markup language**, not a programming language at any GL level.",
        "The HTML option is almost always the planted error.", 35)

    S = by["cf-abbreviations"]
    S.q("cf-abb-p3", "hard",
        "Match the technology to its typical use:\nA. OMR  B. OCR  C. MICR  D. DPI",
        ["A-pencil-marked answer sheets, B-scanning printed text into editable form, C-bank cheque code line, D-print resolution",
         "A-bank cheque code line, B-pencil-marked answer sheets, C-print resolution, D-scanning printed text into editable form",
         "A-pencil-marked answer sheets, B-bank cheque code line, C-scanning printed text into editable form, D-print resolution",
         "A-print resolution, B-scanning printed text into editable form, C-pencil-marked answer sheets, D-bank cheque code line"],
        "A-pencil-marked answer sheets, B-scanning printed text into editable form, C-bank cheque code line, D-print resolution",
        "**OMR** detects marks (bubbles), **OCR** reads characters into editable text, **MICR** reads the magnetic-ink code line on cheques, and **DPI** (dots per inch) measures print resolution.",
        "Marks, Characters, Ink, Dots — one word per technology.", 40)
    S.q("cf-abb-p2", "hard",
        "Which set of expansions is **fully correct**?",
        ["UPS – Uninterruptible Power Supply; POST – Power-On Self-Test; VDU – Visual Display Unit",
         "UPS – Uninterrupted Power Supply; POST – Power On System Test; VDU – Video Display Unit",
         "UPS – Uninterruptible Power Supply; POST – Power On System Test; VDU – Visual Display Unit",
         "UPS – Uninterrupted Power Supply; POST – Power-On Self-Test; VDU – Video Display Unit"],
        "UPS – Uninterruptible Power Supply; POST – Power-On Self-Test; VDU – Visual Display Unit",
        "The three fixed traps in one row: **Uninterruptible**, **Power-On Self-Test**, **Visual** Display Unit. Every other set contains at least one wrong word.",
        "Memorise the trap row once — it answers all variants.", 35)
    return subs
