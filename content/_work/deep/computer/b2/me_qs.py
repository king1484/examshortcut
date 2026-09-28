"""MS Excel practice questions. Every numeric answer is computed here and asserted."""
from _lib import Sub


def numq(S, pat, diff, q, correct, distract, sol, sc=None, t=25):
    """Numeric answer: options are strings of computed correct + distractors."""
    assert correct not in distract
    S.q(pat, diff, q, [str(correct)] + [str(d) for d in distract], str(correct), sol, sc, t)


def add_basics(S):
    rows, cols = 1048576, 16384
    cells = rows * cols
    assert cells == 17179869184
    old_cells = 65536 * 256
    assert old_cells == 16777216
    numq(S, "me-b1", "easy", "How many rows does a worksheet of MS Excel 2007 or later contain?",
        rows, [65536, cols, 2097152],
        "Excel 2007 onwards has **10,48,576 rows** (1,048,576) and 16,384 columns. 65,536 rows belonged to Excel 2003 and older.",
        "1,048,576 = 2 to the power 20.", 25)
    numq(S, "me-b1", "hard", "The total number of cells in one Excel 2016 worksheet is —",
        cells, [cells // 10, cells * 10, old_cells],
        "16,384 columns multiplied by 1,048,576 rows = **17,179,869,184 cells** (about 17.18 billion).",
        "rows x columns = cells.", 45)
    S.q("me-b1", "medium", "The label of the LAST column of an Excel 2007+ worksheet is —",
        ["XFD", "IV", "XFE", "ZZZ"], "XFD",
        "Columns run A to Z, AA to ZZ, ... up to **XFD** (the 16,384th column). IV (256th) was the last column of Excel 2003.",
        "2003 ended at IV; 2007+ ends at XFD.", 30)
    numq(S, "me-b1", "easy", "How many rows did a Microsoft Excel 2003 worksheet contain?",
        65536, [1048576, 256, 16384],
        "Excel 2003 and earlier: **65,536 rows and 256 columns**. The 1,048,576-row grid arrived with Excel 2007.",
        "Old limit 64K rows.", 25)
    S.q("me-b2", "easy", "Which cell reference stays COMPLETELY fixed when a formula is copied?",
        ["$A$1", "A1", "$A1", "A$1"], "$A$1",
        "**$A$1 is absolute** — dollar signs lock both the column and the row. $A1 and A$1 are mixed; only the plain part moves.",
        "Two dollars = fully locked.", 25)
    S.q("me-b2", "medium", "Cell C1 holds =A1*$B$1. It is copied to cell C2 (one row down). C2 will contain —",
        ["=A2*$B$1", "=A1*$B$1", "=A2*B2", "=A3*$B$1"], "=A2*$B$1",
        "A1 is relative, so it slides to A2; $B$1 is absolute, so it stays. Result: **=A2*$B$1**.",
        "Relative moves, absolute sits.", 35)
    S.q("me-b2", "medium", "While editing the formula =A1*2, pressing F4 once changes A1 to —",
        ["$A$1", "A$1", "$A1", "B1"], "$A$1",
        "**F4 adds both dollars first** (A1 to $A$1); further presses cycle A$1, $A1 and back to A1.",
        "First press = full lock.", 30)
    S.q("me-b2", "hard", "Cell D2 holds =B2+$C$3. It is copied to E2 (one column right). E2 will contain —",
        ["=C2+$C$3", "=C2+$D$3", "=B2+$C$3", "=C2+C3"], "=C2+$C$3",
        "Moving right by one column shifts relative references one letter (B2 to C2); $C$3 is locked, so it stays $C$3.",
        "Slide only the unmarked parts.", 40)
    S.q("me-b3", "easy", "A file created in MS Excel is called a —",
        ["Workbook", "Worksheet", "Cell range", "Document"], "Workbook",
        "The file = **workbook**; each tab inside it = a worksheet; each box = a cell.",
        "Book contains sheets.", 20)
    S.q("me-b3", "easy", "The cell at the crossing of column C and row 5 has the address —",
        ["C5", "5C", "C:5", "R5C"], "C5",
        "Addresses read **column letter first, then row number**: C5.",
        "Letter before number.", 20)
    S.q("me-b3", "medium", "Which screen element shows the address of the active cell?",
        ["Name Box", "Formula Bar", "Status bar", "Title bar"], "Name Box",
        "The **Name Box** (left end of the formula bar) shows where you are; the Formula Bar shows what the cell contains.",
        "Name = address.", 25)
    S.q("me-b3", "medium", "How many worksheets does a new Excel 2016 workbook contain by default?",
        ["1", "3", "16", "255"], "1",
        "One worksheet by default (Excel 2007 onwards; the older default of 3 sheets ended in 2013). More sheets are one click away.",
        "Modern default = single sheet.", 25)
    S.q("me-b4", "easy", "When a number is typed in a cell, Excel aligns it to the —",
        ["Right", "Left", "Centre", "Top"], "Right",
        "**Numbers right-align, text left-aligns** automatically — a quick test of what Excel thinks your data is.",
        "Numbers sit right.", 20)
    S.q("me-b4", "easy", "A cell shows a row of #### symbols. This means —",
        ["The column is too narrow to show the value", "The formula has an error", "The file is corrupted",
         "The cell contains a password"], "The column is too narrow to show the value",
        "##### is only a **display notice** — widen the column and the number appears. Error values look like #DIV/0!.",
        "Hashes = narrow house.", 20)
    numq(S, "me-b4", "medium", "How many cells does the range A1:B5 contain?",
        2 * 5, [5, 15, 25],
        "A to B = 2 columns, rows 1 to 5 = 5 rows: 2 x 5 = **10 cells**.",
        "cols x rows of the rectangle.", 30)
    S.q("me-b4", "medium", "Freeze Panes is used to —",
        ["Keep selected rows or columns visible while scrolling", "Protect the file with a password",
         "Stop all editing on the sheet", "Fix broken formulas"],
        "Keep selected rows or columns visible while scrolling",
        "**Freeze Panes** (View tab) pins headings — the title row stays on screen while long data scrolls under it.",
        "Frozen headings stay put.", 25)


def add_functions(S):
    total = 10 + 20 + 30
    assert total == 60
    numq(S, "me-f1", "easy", "What does =SUM(10, 20, 30) return?",
        total, [600, 30, 20],
        "=SUM adds its arguments: 10+20+30 = **60**.",
        "SUM = total.", 20)
    vals = [40, 60, 80]
    avg = sum(vals) / len(vals)
    assert avg == 60.0
    numq(S, "me-f1", "medium", "A1=40, A2=60, A3 blank, A4=80. What does =AVERAGE(A1:A4) return?",
        int(avg), [45, 90, 40],
        "AVERAGE ignores the blank cell: (40+60+80)/3 = **60**. Dividing by 4 (giving 45) is the classic trap.",
        "Blank cells never join the count.", 35)
    s = 100 + 50
    assert s == 150
    numq(S, "me-f1", "medium", "A1=100, A2='exam', A3=50. What does =SUM(A1:A3) return?",
        s, [200, 0, 100],
        "SUM skips text cells: 100+50 = **150**. The word 'exam' contributes nothing and raises no error.",
        "Text is invisible to SUM.", 30)
    t = 2 + 3 + 4 + 10
    assert t == 19
    numq(S, "me-f1", "hard", "A1=2, A2=3, A3=4. What does =SUM(A1:A3, 10) return?",
        t, [9, 29, 10],
        "SUM adds the range AND the extra argument: 2+3+4+10 = **19**.",
        "Ranges and numbers mix freely.", 35)
    nums = [x for x in [5, None, "word", 9] if isinstance(x, (int, float))]
    assert len(nums) == 2
    numq(S, "me-f2", "medium", "A1=5, A2='word', A3 blank, A4=9. What does =COUNT(A1:A4) return?",
        2, [3, 4, 1],
        "**COUNT counts only numeric cells**: 5 and 9 give **2**. The text and the blank are skipped.",
        "COUNT = numbers only.", 30)
    filled = [x for x in [5, "word", None, 9] if x is not None]
    assert len(filled) == 3
    numq(S, "me-f2", "medium", "A1=5, A2='word', A3 blank, A4=9. What does =COUNTA(A1:A4) return?",
        3, [2, 4, 1],
        "**COUNTA counts every non-empty cell** — numbers and text: 5, 'word', 9 give **3**.",
        "COUNTA = anything filled.", 30)
    blanks = [x for x in [10, "na", 30, None, 50, None] if x is None]
    assert len(blanks) == 2
    numq(S, "me-f2", "hard", "A1=10, A2='na', A3=30, A4 blank, A5=50, A6 blank. What does =COUNTBLANK(A1:A6) return?",
        2, [1, 3, 4],
        "**COUNTBLANK counts empty cells** — A4 and A6 give **2**. (COUNTA here would be 4.)",
        "Only the true empties.", 40)
    S.q("me-f2", "easy", "Which function counts ALL non-empty cells, text or number alike?",
        ["COUNTA", "COUNT", "COUNTBLANK", "COUNTIF"], "COUNTA",
        "**COUNTA = count anything filled.** COUNT takes numbers only; COUNTBLANK takes empties; COUNTIF adds a condition.",
        "A = Anything.", 20)
    assert 144 ** 0.5 == 12.0
    numq(S, "me-f3", "easy", "What does =SQRT(144) return?",
        12, [14, 24, 72],
        "SQRT is the square root: the square root of 144 is **12**.",
        "12 x 12 = 144.", 20)
    assert 23 % 5 == 3
    numq(S, "me-f3", "medium", "What does =MOD(23, 5) return?",
        23 % 5, [4, 4.6, 18],
        "**MOD gives the remainder**: 23 = 4x5 + 3, so the answer is **3**.",
        "MOD = remainder.", 25)
    r = round(1234.567, 2)
    assert r == 1234.57
    numq(S, "me-f3", "medium", "What does =ROUND(1234.567, 2) return?",
        1234.57, [1234.56, 1234.5, 1235],
        "ROUND to 2 decimals: 1234.567 becomes **1234.57** (the third decimal 7 rounds the 6 up).",
        "Count the decimals wanted.", 25)
    assert 2 ** 10 == 1024
    numq(S, "me-f3", "medium", "What does =POWER(2, 10) return?",
        1024, [20, 100, 512],
        "POWER raises the first number to the second: 2 to the power 10 = **1024**.",
        "2, 4, 8 ... doubles ten times.", 25)
    v = (8 // 1) + (10 % 4)
    assert v == 10
    numq(S, "me-f3", "hard", "What does =INT(8.9) + =MOD(10, 4) evaluate to?",
        10, [11, 9, 10.9],
        "INT chops the fraction: INT(8.9) = 8. MOD(10, 4) = 2 (remainder). 8 + 2 = **10**.",
        "INT = floor for positives; MOD = remainder.", 45)
    assert len("keyboard") == 8
    numq(S, "me-f4", "easy", "What does =LEN('keyboard') return?",
        len("keyboard"), [7, 9, 1],
        "**LEN counts the characters**: keyboard has 8 letters, so **8**.",
        "Count the letters.", 20)
    assert "EXAM"[:2] == "EX"
    S.q("me-f4", "medium", "What does =LEFT('EXAM', 2) return?",
        ["EX", "AM", "EA", "XM"], "EX",
        "**LEFT takes letters from the start**: the first 2 letters of EXAM are **EX**. RIGHT('EXAM',2) would give AM.",
        "LEFT = leftmost letters.", 25)
    assert "computer"[3:6] == "put"
    S.q("me-f4", "medium", "What does =MID('computer', 4, 3) return?",
        ["put", "ute", "omp", "ter"], "put",
        "**MID(text, start, count)**: from the 4th letter take 3 — c-o-m-**p-u-t**-e-r gives **put**.",
        "Start counting from 1.", 30)
    assert "india gate".title() == "India Gate"
    S.q("me-f4", "medium", "What does =PROPER('india gate') return?",
        ["India Gate", "INDIA GATE", "india gate", "India gate"], "India Gate",
        "**PROPER capitalises the first letter of every word.** UPPER would shout INDIA GATE, LOWER goes the other way.",
        "PROPER = title style.", 25)
    assert "SS" + "C" == "SSC"
    S.q("me-f4", "hard", "What does =CONCATENATE('SS', 'C') return?",
        ["SSC", "SS C", "SS&C", "C"], "SSC",
        "**CONCATENATE joins text end to end** with no gap: SS + C = **SSC**. The & sign does the same job.",
        "Concatenate = stick together.", 35)
    S.q("me-f5", "medium", "B2 holds 38. What does =IF(B2>=40, 'Pass', 'Fail') display?",
        ["Fail", "Pass", "38", "TRUE"], "Fail",
        "38 is not greater than or equal to 40, so the condition is FALSE and the third value, **Fail**, is shown.",
        "Substitute and test.", 25)
    S.q("me-f5", "medium", "VLOOKUP searches for the lookup value in which part of the table?",
        ["The first (leftmost) column", "Any column you name", "The last column", "The header row"],
        "The first (leftmost) column",
        "**V = vertical search down the FIRST column**; the column-number argument only decides what is returned after the match is found.",
        "VLOOKUP always enters from the left door.", 25)
    lookup = {101: "Pen", 102: "Pencil", 103: "Eraser"}
    price = {101: 10, 102: 5, 103: 3}
    assert lookup[102] == "Pencil" and price[102] == 5
    numq(S, "me-f5", "hard",
        "A1:C3 holds: 101 Pen 10 / 102 Pencil 5 / 103 Eraser 3. What does =VLOOKUP(102, A1:C3, 3, FALSE) return?",
        5, [102, "Pencil", 3],
        "It finds 102 in the first column and returns the 3rd column value of that row: the price **5**.",
        "Row of 102, third value across.", 40)
    S.q("me-f5", "medium", "In VLOOKUP, the FALSE (or 0) argument asks for —",
        ["An exact match of the lookup value", "An approximate match", "A vertical search only", "No formatting"],
        "An exact match of the lookup value",
        "FALSE = **exact match**; TRUE (or omitted) allows the nearest smaller value in sorted data. Exact is the safe choice with codes.",
        "FALSE = fussy matching.", 25)


def add_errors_charts(S):
    S.q("me-e1", "easy", "B1 is empty. What will =A1/B1 display?",
        ["#DIV/0!", "#NAME?", "#VALUE!", "#REF!"], "#DIV/0!",
        "An empty cell counts as zero, so the formula divides by zero: **#DIV/0!**.",
        "Empty divisor = DIV/0.", 25)
    S.q("me-e1", "medium", "You type =SUIM(A1:A5). What does Excel show?",
        ["#NAME?", "#VALUE!", "#DIV/0!", "#REF!"], "#NAME?",
        "SUIM is not a function Excel knows — unrecognisable text gives **#NAME?**.",
        "Unknown name = #NAME?", 25)
    S.q("me-e1", "medium", "A1 contains the text 'exam'. What does =A1+5 show?",
        ["#VALUE!", "#NAME?", "#DIV/0!", "exam5"], "#VALUE!",
        "Adding a number to text is the wrong data type: **#VALUE!**.",
        "Wrong type = VALUE problem.", 25)
    S.q("me-e1", "medium", "A formula refers to cells in column D, and those cells are deleted. The formula shows —",
        ["#REF!", "#NAME?", "#N/A", "0"], "#REF!",
        "The reference is gone, so Excel reports **#REF!** (invalid reference).",
        "Deleted address = lost REFerence.", 25)
    S.q("me-e1", "hard", "A VLOOKUP searches for code 999 which does not exist in the table. The result is —",
        ["#N/A", "#REF!", "#NAME?", "#NUM!"], "#N/A",
        "**#N/A means 'not available'** — the lookup value was not found in the first column.",
        "Not found = N/A.", 35)
    S.q("me-e2", "easy", "Which chart type best shows the trend of temperature month by month?",
        ["Line chart", "Pie chart", "Scatter chart", " Doughnut chart"], "Line chart",
        "**Line charts draw trends across time** — the eye follows the rise and fall directly.",
        "Time trend = line.", 20)
    S.q("me-e2", "easy", "To show how the annual budget is split among departments, use a —",
        ["Pie chart", "Line chart", "Scatter chart", "Stock chart"], "Pie chart",
        "A **pie chart shows shares of one whole** — each slice is one department's percentage of the budget.",
        "Slice the pie = share.", 20)
    S.q("me-e2", "medium", "To compare the marks of five students in one test, the clearest chart is —",
        ["Column chart", "Pie chart", "Line chart", "Radar chart"], "Column chart",
        "**Column (or bar) charts compare values between categories** — five students, five columns, tallest wins.",
        "Compare = columns side by side.", 25)
    S.q("me-e2", "medium", "To study the relationship between height and weight of 50 people, use a —",
        ["Scatter chart", "Pie chart", "Doughnut chart", "Area chart"], "Scatter chart",
        "**Scatter plots two number variables** as points — clusters and trends reveal the relationship.",
        "Two numbers = dots on a grid.", 25)
    S.q("me-e3", "medium", "You want to see only the rows where the city is Pune, without deleting anything. Use —",
        ["Filter", "Sort", "Delete rows", "Hide columns"], "Filter",
        "**Filter hides** the non-matching rows; the data stays safe and comes back when the filter is cleared.",
        "Filter = sieve, not scissors.", 25)
    S.q("me-e3", "medium", "Which feature summarises lakhs of sales rows into a compact category-wise table?",
        ["PivotTable", "AutoFill", "Freeze Panes", "Wrap Text"], "PivotTable",
        "A **PivotTable** drags fields into rows, columns and values to summarise huge data within seconds.",
        "Pivot = turn data into summary.", 25)
    S.q("me-e3", "medium", "Failing marks (below 35) should automatically turn red. Use —",
        ["Conditional formatting", "Filter", "Sort", "Data validation"],
        "Conditional formatting",
        "**Conditional formatting** paints cells when a rule (here <35) is true — the colour updates itself as values change.",
        "Rule-based colouring.", 25)
    S.q("me-e3", "easy", "Which tool arranges selected rows from A to Z or smallest to largest?",
        ["Sort", "Filter", "Format Painter", "Chart Wizard"], "Sort",
        "**Sort reorders** data ascending or descending; Filter only hides; both keep every row intact.",
        "Sort = order.", 20)
    S.q("me-e4", "medium", "In a chart, the small key that tells which colour belongs to which series is the —",
        ["Legend", "Gridline", "Axis title", "Data label"], "Legend",
        "The **legend is the chart's key** — e.g. blue = 2024, orange = 2025.",
        "Legend = colour key.", 25)
    S.q("me-e4", "medium", "The exact value printed on top of each bar is called a —",
        ["Data label", "Legend", "Tick mark", "Trendline"], "Data label",
        "**Data labels print the number on each bar or slice**, so the reader need not measure against the axis.",
        "Label = number on the bar.", 25)
    S.q("me-e4", "hard", "In a normal column chart, category names (like city names) usually appear on the —",
        ["Horizontal (x) axis", "Vertical (y) axis", "Legend", "Chart title"], "Horizontal (x) axis",
        "Column charts put **categories on the x-axis and values on the y-axis**; bar charts swap them.",
        "Columns stand on categories.", 35)


def add_shortcuts(S):
    S.q("me-s1", "easy", "The shortcut to insert today's date as a fixed value in a cell is —",
        ["Ctrl+;", "Ctrl+D", "Ctrl+T", "Shift+D"], "Ctrl+;",
        "**Ctrl+; stamps today's date** (fixed text). Ctrl+D fills down — the planted trap.",
        "Semicolon = stamp.", 20)
    S.q("me-s1", "medium", "Which shortcut runs AutoSum on the selected cells?",
        ["Alt+=", "Ctrl+S", "Shift+=", "Ctrl+="], "Alt+=",
        "**Alt+= is AutoSum** — it writes =SUM() over the neighbouring numbers in one stroke.",
        "Alt and = together sum.", 25)
    S.q("me-s1", "medium", "Which key edits the content of the active cell directly?",
        ["F2", "F4", "Ctrl+E", "F12"], "F2",
        "**F2 puts the cursor inside the cell** for editing. F4 toggles references, F12 is Save As.",
        "F2 = enter the cell.", 25)
    S.q("me-s1", "hard", "Pressing Ctrl+D with a cell selected in Excel will —",
        ["Copy the content of the cell above into it (fill down)", "Insert the current date",
         "Open the Format Cells dialog", "Delete the cell"],
        "Copy the content of the cell above into it (fill down)",
        "**Ctrl+D = fill down** — the date stamp is Ctrl+;. Mixing these two is the most repeated Excel trap.",
        "D = Down, not Date.", 35)
    S.q("me-s2", "easy", "The default file extension of an Excel 2007 or later workbook is —",
        [".xlsx", ".xls", ".xlsm", ".csv"], ".xlsx",
        "**.xlsx** is the Office Open XML default (X = XML); .xls is the 97-2003 file.",
        "2007+ = X formats.", 20)
    S.q("me-s2", "medium", "A workbook that contains macros should be saved as —",
        [".xlsm", ".xlsx", ".xls", ".csv"], ".xlsm",
        "**m = macro**: .xlsm keeps macros; .xlsx silently drops them.",
        "Macro needs the m.", 25)
    S.q("me-s2", "medium", "A .csv file stores data as —",
        ["Plain text values separated by commas", "Formatted worksheets with charts",
         "Macro-enabled workbooks", "Compressed backups"], "Plain text values separated by commas",
        "**CSV = Comma Separated Values** — one sheet, no formatting, opens in any program.",
        "Commas do all the work.", 25)
    S.q("me-s2", "medium", "Which extension belongs to the Excel 97-2003 format?",
        [".xls", ".xlsx", ".xlsm", ".xltx"], ".xls",
        "The X-less **.xls** is the pre-2007 format; every X variant is 2007 or later.",
        "Old = no X.", 25)
    S.q("me-s3", "easy", "Which key combination jumps to cell A1?",
        ["Ctrl+Home", "Ctrl+End", "Alt+Home", "Shift+A1"], "Ctrl+Home",
        "**Ctrl+Home goes to A1**; Ctrl+End jumps to the last used cell.",
        "Home = first cell.", 20)
    S.q("me-s3", "medium", "Ctrl+End takes the cursor to —",
        ["The last used cell of the data", "Cell XFD1048576 always", "The end of the current row",
         "The last open workbook"], "The last used cell of the data",
        "**Ctrl+End lands on the bottom-right of the USED area** — not necessarily the grid's absolute corner.",
        "End of your data, not of Excel.", 25)
    S.q("me-s3", "medium", "To move to the next worksheet of a workbook, press —",
        ["Ctrl+Page Down", "Ctrl+Right arrow", "Alt+Down arrow", "Shift+Enter"], "Ctrl+Page Down",
        "**Ctrl+Page Down / Page Up** walk through the sheet tabs; Ctrl+arrows move within the data.",
        "Page keys change pages (sheets).", 25)
    S.q("me-s4", "easy", "Which shortcut inserts a new worksheet into the open workbook?",
        ["Shift+F11", "Ctrl+N", "F11", "Ctrl+Shift+N"], "Shift+F11",
        "**Shift+F11 adds a worksheet**. Ctrl+N opens a whole new workbook; F11 alone makes a chart sheet.",
        "Shifted F11 = new sheet.", 20)
    S.q("me-s4", "medium", "The fastest way to rename a worksheet is to —",
        ["Double-click its tab, type the new name", "Press F2 on the workbook",
         "Use Ctrl+R", "Retype in the Name Box"],
        "Double-click its tab, type the new name",
        "A **double-click on the sheet tab** opens the rename box (right-click, Rename also works).",
        "Double-click the tab.", 25)
    S.q("me-s4", "medium", "Which key opens the Save As dialog in Excel?",
        ["F12", "Ctrl+S", "Shift+S", "F2"], "F12",
        "**F12 = Save As** (in every Office program); Ctrl+S saves in place.",
        "F12 saves elsewhere.", 20)
