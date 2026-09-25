# -*- coding: utf-8 -*-
"""Deep content for seating-arrangement.json. Idempotent: upserts by id.

Every puzzle is brute-forced with seating_engine.solve(): the clue lambdas must leave exactly
ONE arrangement, that arrangement must equal the one written in the solution (`arr`), and the
asked value must equal the stored answer. Counting questions use len(solutions) as the answer.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import *
from seating_engine import solve, show
from seating_existing import recheck
from seating_content import (NOTES_IDEA, NOTES_LINEAR, NOTES_CIRCULAR, NOTES_STRATEGY,
                             P_IDEA, P_LINEAR, P_CIRC, P_STRAT, PYQS)

T = "seating-arrangement"
d = load(T)
N, S = 1, -1
FAIL = []
NEW = []

I, LN, C, ST = "seating-idea", "linear-arrangement", "circular-arrangement", "puzzle-strategy"


def sp(id, sub, pat, q, mk, ask, ans, wrong, sol, short, diff, t=60, arr=None, count=False):
    sols = mk()
    if count:
        got = str(len(sols))
    else:
        if len(sols) != 1:
            FAIL.append((id, f"{len(sols)} arrangements", [show(v) for v in sols[:4]]))
            return
        got = str(ask(sols[0]))
        if arr is not None and show(sols[0]) != arr:
            FAIL.append((id, "arrangement differs from solution text", show(sols[0]), arr))
            return
    if got != str(ans):
        FAIL.append((id, f"computed {got!r} != stored {ans!r}", [show(v) for v in sols[:2]]))
        return
    NEW.append(Q(id, q, ans, wrong, sol, short, diff, sub, pat, t, check=got))


def row(n, who, face="north"):
    return f"{n} people — {who} — sit in a row facing {face}."


def circ(n, who, face="the centre"):
    return f"{n} people — {who} — sit around a circular table facing {face}."


# ============================ seating-idea ============================
sp("seating-idea-p01", I, "st-p1",
   row("Three", "A, B and C") + " **B sits in the middle. A sits to the immediate left of B.** Who sits at the **right end**?",
   lambda: solve("row", "ABC", face=N, clues=[lambda v: v.at("B", 2), lambda v: v.L("B", "A")]),
   lambda v: v.who(3), "C", ["A", "B", "Cannot be determined"],
   "Facing north, B's left is the west end. B = seat 2, A = seat 1, so C takes seat 3, the right end. Row (left to right): A B C.",
   "Facing north: the person's left is your left on paper.", "easy", 30, "W->E: A B C")

sp("seating-idea-p02", I, "st-p1",
   row("Four", "P, Q, R and S", "south") + " **Q sits to the immediate right of P. R sits to the immediate left of P. S sits to the immediate right of Q.** Who sits at the **western end** of the row?",
   lambda: solve("row", "PQRS", face=S, clues=[lambda v: v.R("P", "Q"), lambda v: v.L("P", "R"), lambda v: v.R("Q", "S")]),
   lambda v: v.who(1), "S", ["R", "P", "Q"],
   "Facing south, a person's right is the west side and left is the east side. Q is one seat west of P, R one seat east of P, S one seat west of Q. From west to east: S Q P R. The western end is S.",
   "South-facing: right = west. Build the chain R → P → Q → S going west.", "medium", 45, "W->E: S Q P R")

sp("seating-idea-p03", I, "st-p1",
   row("Five", "T, U, V, W and X", "south") + " **T sits in the middle. U sits second to the right of T. V sits to the immediate left of T. W does not sit at an end.** Who sits at the **eastern end**?",
   lambda: solve("row", "TUVWX", face=S, clues=[lambda v: v.at("T", 3), lambda v: v.R("T", "U", 2), lambda v: v.L("T", "V"), lambda v: not v.end("W")]),
   lambda v: v.who(5), "X", ["V", "W", "U"],
   "Number seats 1 to 5 from the west. T = 3. Facing south, right = west, so U = 3 − 2 = 1 and V (left = east) = 4. Seats 2 and 5 remain; W is not at an end, so W = 2 and X = 5. From west to east: U W T V X. The eastern end is X.",
   "Flip left/right for south-facing people before placing anyone.", "medium", 50, "W->E: U W T V X")

sp("seating-idea-p04", I, "st-p2",
   row("Five", "A, B, C, D and E") + " **A sits at the left end. C sits fourth to the right of A. B sits to the immediate right of A. D sits to the immediate left of C.** How many people sit **between B and C**?",
   lambda: solve("row", "ABCDE", face=N, clues=[lambda v: v.at("A", 1), lambda v: v.R("A", "C", 4), lambda v: v.R("A", "B"), lambda v: v.L("C", "D")]),
   lambda v: v.gap("B", "C"), "2", ["3", "1", "4"],
   "A = 1, C = 1 + 4 = 5, B = 2, D = 4, so E = 3. Row: A B E D C. People between B (2) and C (5) = 5 − 2 − 1 = 2 (E and D).",
   "People between seats a and b = |a − b| − 1.", "easy", 35, "W->E: A B E D C")

sp("seating-idea-p05", I, "st-p2",
   row("Seven", "J, K, L, M, N, O and P") + " **J sits second from the left end. K sits fourth to the right of J. L sits exactly midway between J and K. O sits at the left end. M sits to the immediate right of K. N sits to the immediate right of J.** How many people sit **to the right of L**?",
   lambda: solve("row", "JKLMNOP", face=N, clues=[lambda v: v.at("J", 2), lambda v: v.R("J", "K", 4), lambda v: v.mid("J", "L", "K"),
                                                  lambda v: v.at("O", 1), lambda v: v.R("K", "M"), lambda v: v.R("J", "N")]),
   lambda v: 7 - v.p["L"], "3", ["2", "4", "5"],
   "J = 2, K = 6, L = midway = 4, O = 1, M = 7, N = 3, so P = 5. Row: O J N L P K M. To the right of L (seat 4) are seats 5, 6, 7: 3 people.",
   "People to the right of seat a in a row of n = n − a.", "medium", 50, "W->E: O J N L P K M")

sp("seating-idea-p06", I, "st-p2",
   row("Six", "A, B, C, D, E and F") + " **Exactly two people sit between A and B. B sits at the right end. C sits to the immediate left of A. D sits second to the right of C. E does not sit at an end.** How many people sit **between F and E**?",
   lambda: solve("row", "ABCDEF", face=N, clues=[lambda v: v.gap("A", "B") == 2, lambda v: v.at("B", 6), lambda v: v.L("A", "C"),
                                                 lambda v: v.R("C", "D", 2), lambda v: not v.end("E")]),
   lambda v: v.gap("F", "E"), "3", ["2", "4", "1"],
   "B = 6 and two people between A and B, so A = 3. C = 2, D = 2 + 2 = 4. Seats 1 and 5 remain; E is not at an end, so E = 5 and F = 1. Row: F C A D E B. Between F (1) and E (5): 5 − 1 − 1 = 3.",
   "'Exactly two between' means the seat numbers differ by 3.", "medium", 55, "W->E: F C A D E B")

sp("seating-idea-p07", I, "st-p3",
   row("Six", "P, Q, R, S, T and U") + " **P sits third from the left end. Q sits second from the right end. R sits to the immediate right of P. S sits at the left end. T sits to the immediate left of P.** What is **R's position from the right end**?",
   lambda: solve("row", "PQRSTU", face=N, clues=[lambda v: v.at("P", 3), lambda v: v.at("Q", 5), lambda v: v.R("P", "R"),
                                                 lambda v: v.at("S", 1), lambda v: v.L("P", "T")]),
   lambda v: ["", "Sixth", "Fifth", "Fourth", "Third", "Second", "First"][v.p["R"]], "Third", ["Fourth", "Second", "Fifth"],
   "P = 3, Q = 6 − 2 + 1 = 5, R = 4, S = 1, T = 2, U = 6. Row: S T P R Q U. R is 4th from the left, so from the right it is 6 − 4 + 1 = 3rd.",
   "From right = n − (from left) + 1.", "easy", 35, "W->E: S T P R Q U")

sp("seating-idea-p08", I, "st-p3",
   row("Six", "A, B, C, D, E and F") + " **A sits second from the left end. B sits fourth from the right end. C sits at the right end. D sits to the immediate left of C. E sits at the left end.** Who sits **third from the right end**?",
   lambda: solve("row", "ABCDEF", face=N, clues=[lambda v: v.at("A", 2), lambda v: v.at("B", 3), lambda v: v.at("C", 6),
                                                 lambda v: v.L("C", "D"), lambda v: v.at("E", 1)]),
   lambda v: v.who(4), "F", ["B", "D", "A"],
   "Fourth from the right in a row of 6 = 6 − 4 + 1 = 3rd from the left, so B = 3. A = 2, C = 6, D = 5, E = 1, F = 4. Row: E A B F D C. Third from the right = seat 4 = F.",
   "Convert every 'from the right' clue to a seat number from the left first.", "easy", 40, "W->E: E A B F D C")

sp("seating-idea-p09", I, "st-p3",
   row("Seven", "J, K, L, M, N, O and P") + " **K sits third from the left end. M sits third from the right end. L sits immediately between K and M. J sits at the left end. N sits to the immediate right of J. O sits at the right end. P sits to the immediate left of O.** How many people sit **between J and M**?",
   lambda: solve("row", "JKLMNOP", face=N, clues=[lambda v: v.at("K", 3), lambda v: v.at("M", 5), lambda v: v.between("K", "L", "M"),
                                                  lambda v: v.at("J", 1), lambda v: v.R("J", "N"), lambda v: v.at("O", 7), lambda v: v.L("O", "P")]),
   lambda v: v.gap("J", "M"), "3", ["2", "4", "5"],
   "K = 3, M = 7 − 3 + 1 = 5, L = 4, J = 1, N = 2, O = 7, P = 6. Row: J N K L M P O. Between J (1) and M (5): 5 − 1 − 1 = 3.",
   "Third from the right of 7 = seat 5; between = |a − b| − 1.", "easy", 45, "W->E: J N K L M P O")

sp("seating-idea-p10", I, "st-p4",
   circ("Four", "A, B, C and D") + " **B sits to the immediate left of A. C sits opposite A.** Who sits to the **immediate right of A**?",
   lambda: solve("circle", "ABCD", face=N, clues=[lambda v: v.L("A", "B"), lambda v: v.opp("C", "A")]),
   lambda v: v.right_of("A"), "D", ["B", "C", "Cannot be determined"],
   "Facing the centre, left = clockwise. Put A at the top: B is next clockwise, C is opposite A, so D is the seat anticlockwise from A — A's right. Clockwise from A: A B C D.",
   "Facing centre: left = clockwise, right = anticlockwise.", "easy", 30, "clockwise: A B C D")

sp("seating-idea-p11", I, "st-p4",
   circ("Five", "A, B, C, D and E", "outward (away from the centre)") + " **B sits second to the left of A. C sits to the immediate right of A. D is not a neighbour of C.** Who sits to the **immediate left of B**?",
   lambda: solve("circle", "ABCDE", face=S, clues=[lambda v: v.L("A", "B", 2), lambda v: v.R("A", "C"), lambda v: not v.adj("D", "C")]),
   lambda v: v.left_of("B"), "E", ["D", "A", "C"],
   "Facing outward, left = anticlockwise and right = clockwise. Put A at seat 0 (seats numbered clockwise). C = 1 (clockwise), B = two seats anticlockwise = 3. Seats 2 and 4 remain; seat 2 touches C, so D = 4 and E = 2. Clockwise: A C E B D. B's left is anticlockwise from seat 3, i.e. seat 2 = E.",
   "Outward: left = anticlockwise. Mark it on the circle before placing anyone.", "medium", 60, "clockwise: A C E B D")

sp("seating-idea-p12", I, "st-p4",
   circ("Six", "A, B, C, D, E and F") + " **A sits opposite D. B sits second to the right of A. C sits opposite B. E sits to the immediate right of D.** Who sits to the **immediate left of C**?",
   lambda: solve("circle", "ABCDEF", face=N, clues=[lambda v: v.opp("A", "D"), lambda v: v.R("A", "B", 2), lambda v: v.opp("C", "B"), lambda v: v.R("D", "E")]),
   lambda v: v.left_of("C"), "E", ["F", "A", "D"],
   "Seats 0–5 clockwise, A = 0, D = 3. Right = anticlockwise, so B = 4 and E = 2. C is opposite B, so C = 1. F = 5. Clockwise: A C E D B F. C's left is the next seat clockwise, seat 2 = E.",
   "Place opposite pairs first; they fix seats exactly.", "hard", 75, "clockwise: A C E D B F")

# ============================ linear-arrangement ============================
sp("linear-arrangement-p01", LN, "st-p5",
   row("Five", "A, B, C, D and E") + " **A and E sit at the two ends, and A is not at the right end. B sits to the immediate right of A. C sits to the immediate left of E.** Who sits **second to the left of E**?",
   lambda: solve("row", "ABCDE", face=N, clues=[lambda v: v.end("A"), lambda v: v.end("E"), lambda v: not v.at("A", 5), lambda v: v.R("A", "B"), lambda v: v.L("E", "C")]),
   lambda v: v.left_of("E", 2), "D", ["C", "B", "A"],
   "A = 1, E = 5, B = 2, C = 4, so D = 3. Row: A B D C E. Second to the left of E (seat 5) is seat 3 = D.",
   "Ends first, then their immediate neighbours; the last seat is whoever is left.", "easy", 35, "W->E: A B D C E")

sp("linear-arrangement-p02", LN, "st-p5",
   row("Six", "P, Q, R, S, T and U") + " **R sits immediately between Q and S. P sits at the left end and U at the right end. T sits to the immediate right of P. Q is not a neighbour of T.** Who sits to the **immediate left of U**?",
   lambda: solve("row", "PQRSTU", face=N, clues=[lambda v: v.between("Q", "R", "S"), lambda v: v.at("P", 1), lambda v: v.at("U", 6),
                                                 lambda v: v.R("P", "T"), lambda v: not v.adj("Q", "T")]),
   lambda v: v.left_of("U"), "Q", ["S", "R", "T"],
   "P = 1, U = 6, T = 2. The block Q–R–S must use seats 3, 4, 5 with R = 4. Q is not next to T (seat 2), so Q = 5 and S = 3. Row: P T S R Q U. Left of U is Q.",
   "'Immediately between' makes a 3-block whose ends can swap — use the negative clue to fix them.", "medium", 50, "W->E: P T S R Q U")

sp("linear-arrangement-p03", LN, "st-p6",
   row("Seven", "A, B, C, D, E, F and G") + " **C sits at the left end. F sits fourth to the right of C. A sits second to the left of F. D sits to the immediate right of F. G does not sit at an end. B is a neighbour of C.** Who sits **third to the right of A**?",
   lambda: solve("row", "ABCDEFG", face=N, clues=[lambda v: v.at("C", 1), lambda v: v.R("C", "F", 4), lambda v: v.L("F", "A", 2),
                                                  lambda v: v.R("F", "D"), lambda v: not v.end("G"), lambda v: v.adj("B", "C")]),
   lambda v: v.right_of("A", 3), "D", ["G", "F", "E"],
   "C = 1, F = 5, A = 3, D = 6, B = 2. Seats 4 and 7 remain; G is not at an end, so G = 4 and E = 7. Row: C B A G F D E. Third to the right of A = seat 6 = D.",
   "Chain the distance clues from the fixed person: right = +k, left = −k.", "medium", 55, "W->E: C B A G F D E")

sp("linear-arrangement-p04", LN, "st-p6",
   row("Eight", "A, B, C, D, E, F, G and H") + " **H sits second from the left end. B sits third to the right of H. D sits third to the right of B. A sits second to the left of B. E sits to the immediate left of D. C does not sit at an end. F is a neighbour of A.** How many people sit **between G and C**?",
   lambda: solve("row", "ABCDEFGH", face=N, clues=[lambda v: v.at("H", 2), lambda v: v.R("H", "B", 3), lambda v: v.R("B", "D", 3), lambda v: v.L("B", "A", 2),
                                                   lambda v: v.L("D", "E"), lambda v: not v.end("C"), lambda v: v.adj("F", "A")]),
   lambda v: v.gap("G", "C"), "4", ["3", "5", "2"],
   "H = 2, B = 5, D = 8, A = 3, E = 7. Free seats: 1, 4, 6. F must touch A (seat 3), so F = 4. C is not at an end, so C = 6 and G = 1. Row: G H A F B C E D. Between G (1) and C (6): 6 − 1 − 1 = 4.",
   "Fill every fixed-distance seat first; three free seats and two negative clues then settle it.", "hard", 80, "W->E: G H A F B C E D")

sp("linear-arrangement-p05", LN, "st-p7",
   row("Five", "A, B, C, D and E", "south") + " **C sits in the middle. A sits second to the right of C. B sits to the immediate left of C. D is not a neighbour of A.** Who sits to the **immediate right of C**?",
   lambda: solve("row", "ABCDE", face=S, clues=[lambda v: v.at("C", 3), lambda v: v.R("C", "A", 2), lambda v: v.L("C", "B"), lambda v: not v.adj("D", "A")]),
   lambda v: v.right_of("C"), "E", ["B", "D", "A"],
   "Seats 1 to 5 from the west. Facing south, right = west, left = east. C = 3, A = 1, B = 4. Seats 2 and 5 remain; seat 2 touches A, so D = 5 and E = 2. From west: A E C B D. C's right is the seat to the west, seat 2 = E.",
   "South-facing: 'right' moves west on the page.", "medium", 50, "W->E: A E C B D")

sp("linear-arrangement-p06", LN, "st-p7",
   row("Six", "P, Q, R, S, T and U", "south") + " **P and Q sit at the two ends. R sits second to the left of P. S sits to the immediate right of R. T sits to the immediate left of R.** Who sits **second to the right of U**?",
   lambda: solve("row", "PQRSTU", face=S, clues=[lambda v: v.end("P"), lambda v: v.end("Q"), lambda v: v.L("P", "R", 2), lambda v: v.R("R", "S"), lambda v: v.L("R", "T")]),
   lambda v: v.right_of("U", 2), "R", ["S", "T", "P"],
   "Seats 1 to 6 from the west; facing south, left = east. If P were at the east end (6), R would be 2 seats further east — impossible. So P = 1, Q = 6, R = 3, S = 2 (right = west), T = 4, U = 5. From west: P S R T U Q. Second to the right of U = 2 seats west of seat 5 = seat 3 = R.",
   "Try both ends for P; the 'second to the left' clue breaks one case at once.", "hard", 75, "W->E: P S R T U Q")

sp("linear-arrangement-p07", LN, "st-p8",
   row("Five", "A, B, C, D and E") + " **B sits at the right end. C sits second to the left of B. A does not sit at an end. D is not a neighbour of C. E is not a neighbour of B.** Who sits to the **immediate right of C**?",
   lambda: solve("row", "ABCDE", face=N, clues=[lambda v: v.at("B", 5), lambda v: v.L("B", "C", 2), lambda v: not v.end("A"),
                                                lambda v: not v.adj("D", "C"), lambda v: not v.adj("E", "B")]),
   lambda v: v.right_of("C"), "A", ["D", "B", "E"],
   "B = 5, C = 3. Free: 1, 2, 4. D must avoid seats 2 and 4 (next to C), so D = 1. E must avoid seat 4 (next to B), so E = 2 and A = 4. Row: D E C A B. Right of C = A.",
   "Place the positive clues, then let each 'not' clue kill a seat.", "medium", 50, "W->E: D E C A B")

sp("linear-arrangement-p08", LN, "st-p8",
   row("Six", "A, B, C, D, E and F") + " **F sits third from the left end. D sits second to the right of F. A is not a neighbour of D and does not sit at an end. C does not sit at an end. B is not a neighbour of D.** Who sits **between F and D**?",
   lambda: solve("row", "ABCDEF", face=N, clues=[lambda v: v.at("F", 3), lambda v: v.R("F", "D", 2), lambda v: not v.adj("A", "D") and not v.end("A"),
                                                 lambda v: not v.end("C"), lambda v: not v.adj("B", "D")]),
   lambda v: v.who(4), "C", ["A", "E", "B"],
   "F = 3, D = 5. Free: 1, 2, 4, 6. A is not at an end and not next to D, so A = 2. C is not at an end, so C = 4. B is not next to D, so B = 1 and E = 6. Row: B A F C D E. Between F and D sits C.",
   "With few seats left, apply the 'not at an end' clues first — they shrink the choices fastest.", "medium", 60, "W->E: B A F C D E")

# ============================ circular-arrangement ============================
sp("circular-arrangement-p01", C, "st-p9",
   circ("Five", "A, B, C, D and E") + " **A sits to the immediate left of B. C sits to the immediate left of A. D sits to the immediate right of B.** Who sits to the **immediate right of D**?",
   lambda: solve("circle", "ABCDE", face=N, clues=[lambda v: v.L("B", "A"), lambda v: v.L("A", "C"), lambda v: v.R("B", "D")]),
   lambda v: v.right_of("D"), "E", ["C", "A", "B"],
   "Facing the centre, left = clockwise. Going clockwise from B: A, then C. D is anticlockwise from B. The one seat left, between C and D, is E. Clockwise from A: A C E D B. D's right (anticlockwise) is E.",
   "Walk clockwise for 'left', anticlockwise for 'right'; the gap is the last person.", "easy", 40, "clockwise: A C E D B")

sp("circular-arrangement-p02", C, "st-p9",
   circ("Six", "P, Q, R, S, T and U") + " **Q sits second to the left of P. R sits to the immediate right of P. S sits opposite P. T is not a neighbour of Q.** Who sits **second to the right of T**?",
   lambda: solve("circle", "PQRSTU", face=N, clues=[lambda v: v.L("P", "Q", 2), lambda v: v.R("P", "R"), lambda v: v.opp("S", "P"), lambda v: not v.adj("T", "Q")]),
   lambda v: v.right_of("T", 2), "Q", ["U", "S", "R"],
   "Seats 0–5 clockwise, P = 0. Q = 2 (left = clockwise), R = 5, S = 3. Seats 1 and 4 remain; seat 1 touches Q, so T = 4 and U = 1. Clockwise: P U Q S T R. Second right of T: anticlockwise 4 → 3 → 2 = Q.",
   "Number the circle 0 to n − 1 clockwise and add or subtract.", "medium", 60, "clockwise: P U Q S T R")

sp("circular-arrangement-p03", C, "st-p9",
   circ("Eight", "A, B, C, D, E, F, G and H") + " **D sits third to the left of A. B sits to the immediate right of D. F sits opposite B. C sits to the immediate left of F. G sits opposite A. E is not a neighbour of A.** Who sits **second to the right of E**?",
   lambda: solve("circle", "ABCDEFGH", face=N, clues=[lambda v: v.L("A", "D", 3), lambda v: v.R("D", "B"), lambda v: v.opp("F", "B"),
                                                      lambda v: v.L("F", "C"), lambda v: v.opp("G", "A"), lambda v: not v.adj("E", "A")]),
   lambda v: v.right_of("E", 2), "D", ["G", "H", "F"],
   "Seats 0–7 clockwise, A = 0. D = 3, B = 2, F = 6, C = 7, G = 4. Seats 1 and 5 remain; seat 1 touches A, so E = 5 and H = 1. Clockwise: A H B D G E F C. Second right of E: anticlockwise 5 → 4 → 3 = D.",
   "In a circle of 8, opposite = 4 seats away; fix those pairs early.", "hard", 90, "clockwise: A H B D G E F C")

sp("circular-arrangement-p04", C, "st-p10",
   circ("Four", "A, B, C and D") + " **A sits opposite C. B sits to the immediate left of A.** Who sits **opposite B**?",
   lambda: solve("circle", "ABCD", face=N, clues=[lambda v: v.opp("A", "C"), lambda v: v.L("A", "B")]),
   lambda v: v.opp_of("B"), "D", ["A", "C", "Cannot be determined"],
   "A and C take one opposite pair, so B and D must take the other pair. Clockwise from A: A B C D. Opposite B is D.",
   "In a circle of 4, once one opposite pair is fixed, the other two are opposite each other.", "easy", 30, "clockwise: A B C D")

sp("circular-arrangement-p05", C, "st-p10",
   circ("Six", "A, B, C, D, E and F") + " **A sits opposite B. C sits opposite D. E sits to the immediate left of A. C sits to the immediate left of E.** Who sits **second to the left of F**?",
   lambda: solve("circle", "ABCDEF", face=N, clues=[lambda v: v.opp("A", "B"), lambda v: v.opp("C", "D"), lambda v: v.L("A", "E"), lambda v: v.L("E", "C")]),
   lambda v: v.left_of("F", 2), "A", ["D", "E", "B"],
   "Seats 0–5 clockwise, A = 0, B = 3. E = 1, C = 2, so D (opposite C) = 5 and F = 4. Clockwise: A E C B F D. Second left of F: clockwise 4 → 5 → 0 = A.",
   "Opposite = n ÷ 2 places; place both pairs before the neighbours.", "medium", 55, "clockwise: A E C B F D")

sp("circular-arrangement-p06", C, "st-p10",
   circ("Eight", "A, B, C, D, E, F, G and H") + " **A sits opposite E. B sits second to the right of A. F sits opposite B. C sits to the immediate left of E. D sits opposite C. H is a neighbour of F.** Who sits **second to the right of C**?",
   lambda: solve("circle", "ABCDEFGH", face=N, clues=[lambda v: v.opp("A", "E"), lambda v: v.R("A", "B", 2), lambda v: v.opp("F", "B"),
                                                      lambda v: v.L("E", "C"), lambda v: v.opp("D", "C"), lambda v: v.adj("H", "F")]),
   lambda v: v.right_of("C", 2), "H", ["G", "E", "D"],
   "Seats 0–7 clockwise, A = 0, E = 4. B = 6 (right = anticlockwise), F = 2. C = 5, D = 1. Seats 3 and 7 remain; H must touch F (seat 2), so H = 3 and G = 7. Clockwise: A D F H E C B G. Second right of C: anticlockwise 5 → 4 → 3 = H.",
   "Three opposite pairs fix six seats; one neighbour clue settles the last two.", "medium", 80, "clockwise: A D F H E C B G")

sp("circular-arrangement-p07", C, "st-p11",
   circ("Five", "A, B, C, D and E", "outward (away from the centre)") + " **C sits second to the right of A. B sits to the immediate left of C. D is not a neighbour of A.** Who sits to the **immediate right of D**?",
   lambda: solve("circle", "ABCDE", face=S, clues=[lambda v: v.R("A", "C", 2), lambda v: v.L("C", "B"), lambda v: not v.adj("D", "A")]),
   lambda v: v.right_of("D"), "E", ["C", "A", "B"],
   "Facing outward, right = clockwise and left = anticlockwise. A = 0, C = 2, B = 1. Seats 3 and 4 remain; seat 4 touches A, so D = 3 and E = 4. Clockwise: A B C D E. D's right (clockwise) is E.",
   "Outward: right = clockwise. Swap the rule once, then solve as usual.", "medium", 50, "clockwise: A B C D E")

sp("circular-arrangement-p08", C, "st-p11",
   circ("Six", "P, Q, R, S, T and U", "outward (away from the centre)") + " **Q sits third to the left of P. R sits to the immediate right of Q. S sits second to the left of R. T is not a neighbour of S.** Who sits **second to the right of U**?",
   lambda: solve("circle", "PQRSTU", face=S, clues=[lambda v: v.L("P", "Q", 3), lambda v: v.R("Q", "R"), lambda v: v.L("R", "S", 2), lambda v: not v.adj("T", "S")]),
   lambda v: v.right_of("U", 2), "Q", ["T", "S", "R"],
   "Facing outward: left = anticlockwise, right = clockwise. P = 0, Q = 3 (third either way in a circle of 6). R = 4, S = 2. Seats 1 and 5 remain; seat 1 touches S, so T = 5 and U = 1. Clockwise: P U S Q R T. Second right of U: clockwise 1 → 2 → 3 = Q.",
   "Third to the left in a circle of 6 is simply the opposite seat.", "hard", 80, "clockwise: P U S Q R T")

sp("circular-arrangement-p09", C, "st-p12",
   "Four people — A, B, C and D — sit around a circular table. **A and C face the centre; B and D face outward. B sits to the immediate left of A. D sits to the immediate right of A.** Who sits to the **immediate right of C**?",
   lambda: solve("circle", "ABCD", face={"A": N, "C": N, "B": S, "D": S}, clues=[lambda v: v.L("A", "B"), lambda v: v.R("A", "D")]),
   lambda v: v.right_of("C"), "B", ["D", "A", "Cannot be determined"],
   "Read each clue from A's own direction: A faces the centre, so B (A's left) is clockwise from A and D (A's right) is anticlockwise. C takes the last seat. Clockwise: A B C D. C faces the centre, so C's right is anticlockwise from C: that is B.",
   "In mixed-facing puzzles use the direction of the person the clue is about.", "medium", 50, "clockwise: A B C D")

sp("circular-arrangement-p10", C, "st-p12",
   "Six people — P, Q, R, S, T and U — sit around a circular table. **P, R and T face the centre; Q, S and U face outward. Q sits to the immediate right of P. S sits second to the right of Q. R sits opposite P. T sits to the immediate right of S.** Who sits to the **immediate left of U**?",
   lambda: solve("circle", "PQRSTU", face={"P": N, "R": N, "T": N, "Q": S, "S": S, "U": S},
                 clues=[lambda v: v.R("P", "Q"), lambda v: v.R("Q", "S", 2), lambda v: v.opp("R", "P"), lambda v: v.R("S", "T")]),
   lambda v: v.left_of("U"), "R", ["T", "P", "Q"],
   "Seats 0–5 clockwise, P = 0. P faces the centre, so Q (P's right) = 5. Q faces outward, so right = clockwise: S = 5 + 2 = seat 1. R = 3. S faces outward, so T = 2. U = 4. Clockwise: P S T R U Q. U faces outward, so U's left is anticlockwise: seat 3 = R.",
   "Arrow on every person as soon as they are placed; read each clue from that arrow.", "hard", 90, "clockwise: P S T R U Q")

# ============================ puzzle-strategy ============================
TWO3 = ("Six people sit in two parallel rows of three. **A, B and C sit in Row 1 facing south; P, Q and R sit in Row 2 facing north**, so each person faces one person of the other row. ")
TWO4 = ("Eight people sit in two parallel rows of four. **A, B, C and D sit in Row 1 facing south; P, Q, R and S sit in Row 2 facing north**, so each person faces one person of the other row. ")

sp("puzzle-strategy-p01", ST, "st-p13",
   TWO3 + "**B sits in the middle of Row 1. A sits to the immediate left of B. R faces A. Q does not sit at an end.** Who **faces P**?",
   lambda: solve("rows2", "ABCPQR", rows0="ABC", clues=[lambda v: v.at("B", (0, 2)), lambda v: v.L("B", "A"), lambda v: v.opp("R", "A"), lambda v: not v.end("Q")]),
   lambda v: v.opp_of("P"), "C", ["A", "B", "R"],
   "Number seats 1–3 from the west in both rows. Row 1 faces south, so its left is east: B = 2, A = 3. R faces A, so R = 3 in Row 2. Q is not at an end, so Q = 2 and P = 1. P faces seat 1 of Row 1, which is C.",
   "Facing pairs share a seat number; a south-facing left is east.", "medium", 60, "row0(S): C B A | row1(N): P Q R")

sp("puzzle-strategy-p02", ST, "st-p13",
   TWO4 + "**A sits at one end of Row 1. C sits second to the right of A. R faces C. S sits to the immediate left of R. B does not sit at an end. Q faces B.** Who **faces P**?",
   lambda: solve("rows2", "ABCDPQRS", rows0="ABCD", clues=[lambda v: v.end("A"), lambda v: v.R("A", "C", 2), lambda v: v.opp("R", "C"),
                                                          lambda v: v.L("R", "S"), lambda v: not v.end("B"), lambda v: v.opp("Q", "B")]),
   lambda v: v.opp_of("P"), "A", ["D", "B", "C"],
   "Seats 1–4 from the west. Row 1 faces south, so right = west. If A were at seat 1, C would be at seat −1 — impossible. So A = 4 and C = 2. R faces C: R = 2; S is left of R (north-facing, so west): S = 1. B is not at an end, so B = 3 and D = 1. Q faces B: Q = 3, P = 4. P faces seat 4 of Row 1 = A.",
   "Test both ends for A; the 'second to the right' clue rules one out.", "medium", 90, "row0(S): D C B A | row1(N): S R Q P")

sp("puzzle-strategy-p03", ST, "st-p13",
   TWO4 + "**P sits at the left end of Row 2. R sits second to the right of P. S is a neighbour of P. B faces Q. A sits to the immediate right of B. C faces P.** Who sits **second to the left of the person who faces S**?",
   lambda: solve("rows2", "ABCDPQRS", rows0="ABCD", clues=[lambda v: v.at("P", (1, 1)), lambda v: v.R("P", "R", 2), lambda v: v.adj("S", "P"),
                                                          lambda v: v.opp("B", "Q"), lambda v: v.R("B", "A"), lambda v: v.opp("C", "P")]),
   lambda v: v.left_of(v.opp_of("S"), 2), "B", ["A", "C", "Q"],
   "Seats 1–4 from the west. Row 2 faces north: P = 1, R = 3, S = 2, Q = 4. B faces Q: B = 4. A is right of south-facing B, i.e. west: A = 3. C faces P: C = 1, so D = 2. D faces S. D faces south, so D's left is east: two seats east of seat 2 is seat 4 = B.",
   "Find the linking person first (who faces S), then count from that person's own direction.", "hard", 100, "row0(S): C D A B | row1(N): P S R Q")

# p04: exactly one true statement
ST4 = [("F sits to the immediate right of D", lambda v: v.R("D", "F")),
       ("E sits at one of the ends", lambda v: v.end("E")),
       ("A and B are neighbours", lambda v: v.adj("A", "B")),
       ("C sits third to the right of E", lambda v: v.R("E", "C", 3))]
sp("puzzle-strategy-p04", ST, "st-p14",
   row("Six", "A, B, C, D, E and F") + " **D sits at the left end. B sits fourth to the right of D. E sits to the immediate left of B. A is not a neighbour of D. C sits at one of the ends.** Which of the following is **true**?",
   lambda: solve("row", "ABCDEF", face=N, clues=[lambda v: v.at("D", 1), lambda v: v.R("D", "B", 4), lambda v: v.L("B", "E"),
                                                 lambda v: not v.adj("A", "D"), lambda v: v.end("C")]),
   lambda v: [s for s, f in ST4 if f(v)][0] if sum(f(v) for s, f in ST4) == 1 else "NOT UNIQUE",
   ST4[0][0], [s for s, f in ST4[1:]],
   "D = 1, B = 5, E = 4, C = 6 (the only free end). Seats 2 and 3 remain; A is not next to D, so A = 3 and F = 2. Row: D F A E B C. F is immediately right of D — true. E is at seat 4 (not an end), A and B have E between them, and C is second (not third) to the right of E.",
   "Solve the row completely once; then each option is a 5-second check.", "medium", 70, "W->E: D F A E B C")

ST5 = [("F sits to the immediate left of D", lambda v: v.L("D", "F")),
       ("E sits opposite B", lambda v: v.opp("E", "B")),
       ("A sits to the immediate right of E", lambda v: v.R("E", "A")),
       ("B and D are neighbours", lambda v: v.adj("B", "D"))]
sp("puzzle-strategy-p05", ST, "st-p14",
   circ("Six", "A, B, C, D, E and F") + " **A sits opposite D. B sits to the immediate left of A. E sits second to the right of B. C is a neighbour of B.** Which of the following is **true**?",
   lambda: solve("circle", "ABCDEF", face=N, clues=[lambda v: v.opp("A", "D"), lambda v: v.L("A", "B"), lambda v: v.R("B", "E", 2), lambda v: v.adj("C", "B")]),
   lambda v: [s for s, f in ST5 if f(v)][0] if sum(f(v) for s, f in ST5) == 1 else "NOT UNIQUE",
   ST5[0][0], [s for s, f in ST5[1:]],
   "Seats 0–5 clockwise, A = 0, D = 3, B = 1 (left = clockwise). E is second to the right of B: anticlockwise 1 → 0 → 5, so E = 5. C touches B: seat 2. F = 4. Clockwise: A B C D F E. D's left is clockwise from seat 3 = seat 4 = F — true. Opposite B is F (not E), E's right is F (not A), and B (1) and D (3) have C between them.",
   "Write the finished circle once, then test each option against it.", "medium", 75, "clockwise: A B C D F E")

sp("puzzle-strategy-p06", ST, "st-p14",
   row("Five", "P, Q, R, S and T") + " **R sits in the middle. P sits second to the left of R. T sits to the immediate right of R. Q does not sit at an end.** If **P and S interchange their seats**, who will sit to the **immediate left of P**?",
   lambda: solve("row", "PQRST", face=N, clues=[lambda v: v.at("R", 3), lambda v: v.L("R", "P", 2), lambda v: v.R("R", "T"), lambda v: not v.end("Q")]),
   lambda v: v.who(v.p["S"] - 1), "T", ["R", "S", "Q"],
   "R = 3, P = 1, T = 4, Q = 2, S = 5. Row: P Q R T S. After P and S swap: S Q R T P. P is now at seat 5; the person to P's immediate left is at seat 4 = T.",
   "For an interchange, swap only the two named people and keep everyone else still.", "easy", 45, "W->E: P Q R T S")

sp("puzzle-strategy-p07", ST, "st-p15",
   "In how many different ways can **five people sit in a row** if **A and B must sit next to each other**?",
   lambda: solve("row", "ABCDE", face=N, clues=[lambda v: v.adj("A", "B")]),
   None, "48", ["24", "120", "96"],
   "Tie A and B into one block. Then 4 units (block, C, D, E) can be arranged in 4! = 24 ways, and inside the block A and B can swap: 24 × 2 = 48.",
   "Block of two in a row of n: (n − 1)! × 2.", "easy", 40, count=True)

sp("puzzle-strategy-p08", ST, "st-p15",
   "Five people A, B, C, D and E sit in a row facing north. **A sits at the left end, B sits to the immediate right of A and C does not sit at an end.** In how many different ways can they be seated?",
   lambda: solve("row", "ABCDE", face=N, clues=[lambda v: v.at("A", 1), lambda v: v.R("A", "B"), lambda v: not v.end("C")]),
   None, "4", ["6", "2", "8"],
   "A = 1 and B = 2 are fixed. Seats 3, 4, 5 remain. C cannot take seat 5, so C has 2 choices (3 or 4). D and E then fill the other two seats in 2 ways. Total = 2 × 2 = 4.",
   "Remove the fixed people first; then count the free seats with the restrictions.", "medium", 50, count=True)

sp("puzzle-strategy-p09", ST, "st-p15",
   "Six people A, B, C, D, E and F sit around a circular table facing the centre. **A sits opposite B and C sits to the immediate left of A.** Arrangements that are rotations of each other count as the same. In how many different ways can they be seated?",
   lambda: solve("circle", "ABCDEF", face=N, clues=[lambda v: v.opp("A", "B"), lambda v: v.L("A", "C")]),
   None, "6", ["24", "12", "3"],
   "Fix A's seat to remove rotations. B's seat (opposite) and C's seat (A's left) are then fixed. D, E and F fill the three remaining seats in 3! = 6 ways.",
   "Circle: fix one person, then count the rest like a row.", "medium", 50, count=True)

sp("puzzle-strategy-p10", ST, "st-p16",
   "Four friends A, B, C and D sit in a row facing north, and each drinks a different one of tea, juice, milk and coffee. **A sits at the left end and drinks tea. D sits at the right end. The milk drinker sits to the immediate left of D. B drinks juice. C is not a neighbour of A.** What does **D** drink?",
   lambda: solve("row", "ABCD", face=N, attrs=["Tea", "Juice", "Milk", "Coffee"],
                 clues=[lambda v: v.at("A", 1), lambda v: v.a["A"] == "Tea", lambda v: v.at("D", 4), lambda v: v.L("D", v.has("Milk")),
                        lambda v: v.a["B"] == "Juice", lambda v: not v.adj("C", "A")]),
   lambda v: v.a["D"], "Coffee", ["Milk", "Juice", "Tea"],
   "A = 1 (tea), D = 4. C is not next to A, so C = 3 and B = 2. The milk drinker is at seat 3, so C drinks milk. B drinks juice. The only drink left is coffee, so D drinks coffee.",
   "Fix seats first; then the attribute clue tied to a seat names its owner.", "easy", 50,
   "W->E: A B C D  attrs: A=Tea, B=Juice, C=Milk, D=Coffee")

sp("puzzle-strategy-p11", ST, "st-p16",
   "Five friends A, B, C, D and E sit around a circular table facing the centre. Each likes a different colour: red, blue, green, black and white. **A likes red. The person who likes blue sits to the immediate left of A. C sits second to the right of A and likes black. B likes green and is not a neighbour of A. E does not like blue.** Which colour does the person sitting to the **immediate right of C** like?",
   lambda: solve("circle", "ABCDE", face=N, attrs=["Red", "Blue", "Green", "Black", "White"],
                 clues=[lambda v: v.a["A"] == "Red", lambda v: v.L("A", v.has("Blue")), lambda v: v.R("A", "C", 2), lambda v: v.a["C"] == "Black",
                        lambda v: v.a["B"] == "Green", lambda v: not v.adj("B", "A"), lambda v: v.a["E"] != "Blue"]),
   lambda v: v.a[v.right_of("C")], "Green", ["Blue", "White", "Red"],
   "Seats 0–4 clockwise, A = 0. C is second to the right (anticlockwise) = seat 3. B is not next to A, so B avoids seats 1 and 4: B = 2. Seats 1 and 4 remain for D and E. The blue-lover sits at A's left = seat 1, and E does not like blue, so D = 1 (blue) and E = 4 (white). Clockwise: A D B C E. C's right is anticlockwise = seat 2 = B, who likes green.",
   "Solve seats with the position clues; bring in colours only to decide between the last two people.", "hard", 100,
   "clockwise: A D B C E  attrs: A=Red, B=Green, C=Black, D=Blue, E=White")

sp("puzzle-strategy-p12", ST, "st-p16",
   "Five people A, B, C, D and E sit in a row facing north. Each is from a different city: Agra, Delhi, Kochi, Pune and Surat. **The person from Delhi sits in the middle. B sits at the left end and is from Agra. D sits to the immediate right of the person from Delhi. The person from Kochi sits at the right end. The person from Surat sits to the immediate left of the person from Delhi. A is not a neighbour of B. C is from Delhi.** Which city is **A** from?",
   lambda: solve("row", "ABCDE", face=N, attrs=["Agra", "Delhi", "Kochi", "Pune", "Surat"],
                 clues=[lambda v: v.at(v.has("Delhi"), 3), lambda v: v.at("B", 1), lambda v: v.a["B"] == "Agra", lambda v: v.R(v.has("Delhi"), "D"),
                        lambda v: v.at(v.has("Kochi"), 5), lambda v: v.L(v.has("Delhi"), v.has("Surat")), lambda v: not v.adj("A", "B"),
                        lambda v: v.a["C"] == "Delhi"]),
   lambda v: v.a["A"], "Kochi", ["Pune", "Surat", "Agra"],
   "C (Delhi) = 3, B (Agra) = 1, D = 4. Seats 2 and 5 remain for A and E; A is not next to B, so A = 5 and E = 2. Seat 5 is the Kochi person, so A is from Kochi. Seat 2 is Surat (E), and D is from Pune. Row: B E C D A.",
   "Link each city clue to a seat; the name clues then read the city straight off the seat.", "hard", 100,
   "W->E: B E C D A  attrs: A=Kochi, B=Agra, C=Delhi, D=Pune, E=Surat")

# ---------------- report failures before touching the file ----------------
if FAIL:
    print("PUZZLE FAILURES:")
    for f in FAIL:
        print(" ", f)
    sys.exit(1)

# ---------------- existing questions: re-verify, fix wording only ----------------
rep = recheck()
bad = {k: v for k, v in rep.items() if not v[1] == "ok"}
assert not bad, bad
print("existing seating questions re-verified:", len(rep), "(rsn-seating-11 has", rep["rsn-seating-11"][0], "arrangements, same answer)")

patch_q(d, "rsn-seating-8", solution=(
    "Fix P anywhere. Q is at P's immediate left; B is opposite P and S is opposite Q. Q must touch A, and R sits at A's "
    "immediate left, with C opposite A and D at C's immediate left. Going clockwise the circle closes as P, Q, A, R, B, S, C, D. "
    "In a circle of 8 the opposite seat is 4 places away: from R (4th in the list) count 4 places to reach the 8th, **D**."))
patch_q(d, "rsn-seating-11", solution=(
    "T (1), V (2), U (6). The X–W–Y block must sit in consecutive seats with W in the middle — only seats 3–4–5 are free, so W = 4 "
    "and X, Y take seats 3 and 5 in some order (the clues do not decide which). Either way, two to the right of W = seat 6 = **U**."))

upsert(d["practice"], NEW)
set_sub(d, I, notes=NOTES_IDEA, patterns=P_IDEA)
set_sub(d, LN, notes=NOTES_LINEAR, patterns=P_LINEAR)
set_sub(d, C, notes=NOTES_CIRCULAR, patterns=P_CIRC)
set_sub(d, ST, notes=NOTES_STRATEGY, patterns=P_STRAT)
d["pyqPatterns"] = PYQS
print("new puzzles verified unique:", len(NEW))

errs = finish(T, d)
assert not errs, errs
