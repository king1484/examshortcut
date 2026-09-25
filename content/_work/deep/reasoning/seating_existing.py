# -*- coding: utf-8 -*-
"""Brute-force re-check of the existing seating questions (report only)."""
from seating_engine import solve, show

N, S = 1, -1
EXIST = {
 "rsn-seating-ex1": (lambda: solve("row", "ABCDE", face=N, clues=[
     lambda v: v.at("B", 1), lambda v: v.at("E", 5), lambda v: v.R("B", "D"), lambda v: v.L("E", "C")]),
     lambda v: v.who(3), "A"),
 "rsn-seating-ex2": (lambda: solve("circle", "ABCDE", face=N, clues=[
     lambda v: v.R("B", "A"), lambda v: v.L("B", "D"), lambda v: v.L("D", "C"), lambda v: v.L("C", "E")]),
     lambda v: v.left_of("A", 2), "D"),
 "rsn-seating-ex3": (lambda: solve("row", "PQRS", face=N, clues=[
     lambda v: v.at("Q", 4), lambda v: not v.adj("P", "Q"), lambda v: v.L("P", "R")]),
     lambda v: v.who(2), "P"),
 "rsn-seating-1": (lambda: solve("row", "ABCDEF", face=N, clues=[
     lambda v: v.at("C", 3), lambda v: v.R("C", "A", 2), lambda v: v.adj("B", "C") and v.adj("B", "A"),
     lambda v: v.at("D", 1), lambda v: v.at("E", 6)]),
     lambda v: v.who(4), "B"),
 "rsn-seating-2": (lambda: solve("row", "JKLMNOP", face=N, clues=[
     lambda v: v.at("M", 4), lambda v: v.L("M", "L"), lambda v: v.R("M", "O"), lambda v: v.at("J", 1),
     lambda v: v.at("K", 7), lambda v: v.between("O", "P", "K")]),
     lambda v: v.who(2), "N"),
 "rsn-seating-3": (lambda: solve("row", "RSTUV", face=S, clues=[
     lambda v: v.at("R", 3), lambda v: v.L("R", "T", 2), lambda v: v.R("R", "V"), lambda v: v.end("S")]),
     lambda v: v.left_of("R"), "U"),
 "rsn-seating-4": (lambda: solve("row", "PQRSTW", face=N, clues=[
     lambda v: v.at("P", 1), lambda v: v.at("Q", 6), lambda v: v.R("P", "R"), lambda v: not v.adj("T", "R"),
     lambda v: v.L("S", "W") and v.R("S", "T")]),
     lambda v: v.who(3), "W"),
 "rsn-seating-5": (lambda: solve("row", "ABCDEFG", face=N, clues=[
     lambda v: v.end("E"), lambda v: v.L("E", "D"), lambda v: v.L("D", "G", 2), lambda v: v.R("G", "B"),
     lambda v: not v.adj("A", "B"), lambda v: v.end("C"), lambda v: v.R("C", "F")]),
     lambda v: v.who(4), "G"),
 "rsn-seating-6": (lambda: solve("circle", "KLMNOP", face=N, clues=[
     lambda v: v.opp("P", "M"), lambda v: v.opp("K", "L"), lambda v: v.L("K", "N"), lambda v: v.R("M", "O"),
     lambda v: v.R("O", "L")]),
     lambda v: v.opp_of("N"), "O"),
 "rsn-seating-7": (lambda: solve("circle", "RSTUV", face=S, clues=[
     lambda v: v.R("R", "S"), lambda v: v.R("S", "T"), lambda v: v.R("U", "V"), lambda v: v.R("V", "R")]),
     lambda v: v.left_of("T"), "S"),
 "rsn-seating-8": (lambda: solve("circle", "ABCDPQRS", face=N, clues=[
     lambda v: v.opp("C", "A"), lambda v: v.opp("B", "P"), lambda v: v.opp("S", "Q"), lambda v: v.L("A", "R"),
     lambda v: v.L("P", "Q"), lambda v: v.L("C", "D"), lambda v: v.adj("Q", "A")]),
     lambda v: v.opp_of("R"), "D"),
 "rsn-seating-9": (lambda: solve("row", "HIJKLMN", face=N, clues=[
     lambda v: v.at("K", 4), lambda v: v.R("K", "I", 2), lambda v: v.adj("M", "I"), lambda v: v.L("M", "J", 3),
     lambda v: v.adj("L", "K"), lambda v: v.at("H", 1), lambda v: v.at("N", 7)]),
     lambda v: v.who(5), "M"),
 "rsn-seating-10": (lambda: solve("circle", "ABCDE", face=N, clues=[
     lambda v: v.between("C", "E", "B"), lambda v: v.L("B", "D"), lambda v: v.R("C", "A")]),
     lambda v: v.right_of("B", 2), "C"),
 "rsn-seating-11": (lambda: solve("row", "TUVWXY", face=N, clues=[
     lambda v: v.at("V", 2), lambda v: v.between("X", "W", "Y"), lambda v: v.at("T", 1), lambda v: v.at("U", 6)]),
     lambda v: v.right_of("W", 2), "U"),
 "rsn-seating-12": (lambda: solve("row", "ABCDEFGH", face=N, clues=[
     lambda v: v.L("E", "A", 2), lambda v: v.L("D", "E", 3), lambda v: {v.p["G"], v.p["D"]} == {1, 8},
     lambda v: v.L("A", "C"), lambda v: v.R("E", "B"), lambda v: v.R("B", "F")]),
     lambda v: v.who(6), "B"),
}


def recheck():
    report = {}
    for qid, (mk, ask, stored) in EXIST.items():
        sols = mk()
        answers = {ask(v) for v in sols}
        status = "ok" if answers == {stored} else f"MISMATCH answers={answers} stored={stored}"
        report[qid] = (len(sols), status, [show(v) for v in sols[:2]])
    return report


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in recheck().items():
        print(k, v)
