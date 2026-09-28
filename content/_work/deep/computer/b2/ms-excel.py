"""Phase-2 deep content for computer/ms-excel. Run: py -3 ms-excel.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from me_pats import build_basics, build_functions, build_errors_charts, build_shortcuts
import me_qs


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Function-output computation", "very common",
      "A small cell list (often with a text cell or a blank planted inside) is given and the output of SUM, AVERAGE, MAX, ROUND, MOD or LEN is asked.",
      "Add or work the function by hand first — and remember SUM and AVERAGE silently skip text and blank cells, so AVERAGE divides by the number of NUMERIC cells, not by the range length. Then match the computed value to the options.",
      "me-functions",
      "A1=10, A2=20, A3=30. What does =AVERAGE(A1:A3) return?",
      "60 — (10+20+30)/3. Blanks would be excluded from both the sum and the divisor."),
    P("Shortcut-key recall", "very common",
      "'Shortcut to insert the current date', 'which key runs AutoSum / edits a cell / toggles $ references' — with Ctrl+D planted as the fake date key.",
      "Keep the card: Ctrl+; date, Ctrl+Shift+; time, Alt+= AutoSum, F2 edit cell, F4 reference toggle (only while editing), Ctrl+1 Format Cells, F12 Save As, Shift+F11 new sheet, Ctrl+Home A1, Ctrl+End last used cell. Ctrl+D is FILL DOWN, never date.",
      "me-shortcuts",
      "The shortcut of AutoSum in MS Excel is:",
      "Alt+= — it writes =SUM() around the neighbouring numbers in one stroke."),
    P("Error-message identification", "very common",
      "A broken-formula story (divide by an empty cell, misspelt function, text plus number, deleted range, missing lookup) and the error code is asked — or the code is given and the cause.",
      "Map the story: empty divisor gives #DIV/0!, unknown text gives #NAME?, wrong data type gives #VALUE!, deleted cells give #REF!, lookup miss gives #N/A, impossible number gives #NUM!. ##### is not an error at all — it is a narrow column.",
      "me-errors-charts",
      "A cell shows #NAME?. The most likely reason is:",
      "Excel cannot recognise the text — usually a misspelt function name like =SUIM(A1:A5)."),
    P("Chart selection", "common",
      "'Which chart best shows a trend over time / share of one whole / comparison between categories / relationship of two variables?'",
      "Purpose decides the chart: Line = trend across time; Pie = shares of ONE whole (one series only); Column/Bar = compare categories; Scatter = two number variables. Words like 'over the years', 'percentage split', 'who scored most' are the spotters.",
      "me-errors-charts",
      "To display the monthly growth of users during a year, the best chart is:",
      "A line chart — trends across time are its exact purpose; a pie cannot show time."),
    P("Reference behaviour on copy", "common",
      "A formula like =A1*$B$1 is copied to another cell and the resulting formula is asked — or the type of a written reference (relative/absolute/mixed) is asked.",
      "Slide only the parts without dollar signs, by the exact rows/columns moved. A1 relative moves fully; $A$1 never moves; $A1 and A$1 move partially. F4 cycles A1, $A$1, A$1, $A1 while editing.",
      "me-basics",
      "C1 holds =A1+B1. Copied to C3 (two rows down), C3 contains:",
      "=A3+B3 — both references are relative and slide down with the copy."),
    P("COUNT family trap", "common",
      "A range mixing numbers, text and blanks is described and COUNT / COUNTA / COUNTBLANK is asked — options differ by exactly the text or blank cells.",
      "COUNT counts only numeric cells, COUNTA counts everything filled, COUNTBLANK counts empties, and COUNTA + COUNTBLANK = total cells. Read the mixture twice before choosing.",
      "me-functions",
      "A1=5, A2='word', A3 blank, A4=9. =COUNT(A1:A4) gives:",
      "2 — only 5 and 9 are numbers; COUNTA would give 3 and COUNTBLANK 1."),
    P("Grid facts (rows/columns/cells)", "common",
      "'How many rows/columns does an Excel 2007+ sheet have?', 'the last column letter', or a multiplication into total cells — with Excel 2003 numbers planted as traps.",
      "2007 onwards: 1,048,576 rows, 16,384 columns (last label XFD), about 17.18 billion cells. Excel 2003 and older: 65,536 rows, 256 columns (last label IV). Cell address = column letter + row number; ranges use a colon (A1:B5).",
      "me-basics",
      "The last column of an Excel 2016 worksheet is labelled:",
      "XFD — IV (the 256th column) was the limit of Excel 2003."),
]

if __name__ == "__main__":
    subs = []
    for build, add in ((build_basics, me_qs.add_basics), (build_functions, me_qs.add_functions),
                       (build_errors_charts, me_qs.add_errors_charts), (build_shortcuts, me_qs.add_shortcuts)):
        S = build()
        add(S)
        subs.append(S)
    apply_topic("ms-excel", subs, PYQ)
