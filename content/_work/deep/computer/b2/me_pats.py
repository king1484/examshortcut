"""MS Excel pattern builders."""
from _lib import Sub


def build_basics():
    S = Sub("me-basics")
    S.notes = __import__("me_notes").ME_BASICS
    S.pattern("me-b1", "Grid arithmetic: rows, columns, cells", "common",
        "'How many rows/columns does an Excel 2007+ sheet have?', 'the last column letter', or multiplication of rows and columns into total cells.",
        None,
        "1. From Excel 2007: rows = 1,048,576; columns = 16,384 (last column XFD).\n2. Total cells = rows multiplied by columns (a calculator question, not memory).\n3. Excel 2003 and older: 65,536 rows, 256 columns (last column IV).",
        "How many cells does one Excel 2016 worksheet contain?",
        "16,384 columns x 1,048,576 rows = **17,179,869,184 cells** — about 17.18 billion.")
    S.pattern("me-b2", "Reference behaviour on copy", "very common",
        "A formula like =A1*$B$1 is copied from one cell to another and the changed formula is asked — or the type (relative/absolute/mixed) of a written reference is asked.",
        None,
        "1. Plain A1 is relative: both parts slide when copied. $A$1 is absolute: frozen. $A1 and A$1 are mixed: only the part without $ moves.\n2. Rewrite the row and column offsets, then rebuild the formula.\n3. F4 cycles A1 to $A$1 to A$1 to $A1 while the formula is being edited.",
        "Cell C1 holds =A1+B1. It is copied to C3. What does C3 contain?",
        "**=A3+B3** — both references are relative, so each moves down 2 rows with the copy.")
    S.pattern("me-b3", "Workbook, worksheet and cell-address recall", "very common",
        "Direct recall: a file is a workbook, a tab is a worksheet, the address is column letter plus row number, the Name Box shows the address, the Formula Bar shows content.",
        None,
        "1. Workbook = file; worksheet = tab inside it; cell = one box; range = A1:B5 with a colon.\n2. Name Box (left of formula bar) = address of the active cell; Formula Bar = its true content.\n3. Default worksheet count in new workbooks = 1 (older versions shipped 3).",
        "In MS Excel, the intersection of a row and a column is called a —",
        "**Cell**, addressed by column letter then row number, e.g. B7.")
    S.pattern("me-b4", "Data type and display basics", "common",
        "Questions on left/right alignment of text and numbers, what ##### means, or what Ctrl+A / Ctrl+Home do.",
        None,
        "1. Text left-aligns, numbers right-align automatically.\n2. ##### = column too narrow — widen it; the value is safe.\n3. Ctrl+A selects the sheet, Ctrl+Home jumps to A1, Freeze Panes pins headings.",
        "A cell shows ###### instead of a number because —",
        "**The column is too narrow to display the number** — widen the column; it is a display notice, not an error.")
    return S


def build_functions():
    S = Sub("me-functions")
    S.notes = __import__("me_notes").ME_FUNCTIONS
    S.pattern("me-f1", "SUM / AVERAGE output computation", "very common",
        "A small cell list is given and the output of =SUM or =AVERAGE is asked; options include realistic wrong totals.",
        None,
        "1. Add the numeric cells for SUM; divide the total by the count of NUMERIC cells for AVERAGE.\n2. Text and blank cells are skipped by both — AVERAGE never counts them in the denominator.\n3. Verify by hand once, then match the option.",
        "A1=10, A2=20, A3=30. What does =AVERAGE(A1:A3) return?",
        "(10+20+30)/3 = **60**.")
    S.pattern("me-f2", "COUNT family trap", "very common",
        "A range mixing numbers, text and blanks is described and COUNT / COUNTA / COUNTBLANK outputs are asked — the options differ by exactly the text or blank cells.",
        None,
        "1. COUNT counts only numeric cells; COUNTA counts every non-empty cell; COUNTBLANK counts empties.\n2. Count the mixture carefully: numbers first, then everything filled, then the gaps.\n3. COUNTA + COUNTBLANK = total cells in the range.",
        "A1=5, A2='word', A3 blank, A4=9. =COUNT(A1:A4) and =COUNTA(A1:A4) give —",
        "**COUNT = 2** (only 5 and 9 are numbers); **COUNTA = 3** (all filled cells, text included).")
    S.pattern("me-f3", "Maths function output", "common",
        "Outputs of ROUND, INT, MOD, ABS, SQRT, POWER on given numbers, or the function that returns a remainder / square root / rounded value.",
        None,
        "1. ROUND(number, digits) rounds to that many decimals; INT chops the fraction for positives.\n2. MOD(a, b) = remainder of a divided by b; ABS removes the minus; SQRT is the square root; POWER(a, b) raises a to the power b.\n3. Beware INT of a negative number rounds DOWN (towards minus infinity).",
        "What does =MOD(23, 5) return?",
        "**3** — 23 divided by 5 is 4 with remainder 3; MOD returns the remainder.")
    S.pattern("me-f4", "Text and date functions", "common",
        "Outputs of LEFT, RIGHT, MID, LEN, PROPER, CONCATENATE, or the function that stamps today's date / joins text.",
        None,
        "1. LEFT takes letters from the start, RIGHT from the end, MID(text, start, how-many) from the middle; LEN counts characters (spaces included).\n2. UPPER/LOWER/PROPER set the case; CONCATENATE or the & sign joins text.\n3. TODAY() and NOW() recalculate on every open; Ctrl+; and Ctrl+Shift+; stamp fixed values.",
        "What does =LEN('keyboard') return?",
        "**8** — LEN counts the characters of the text; keyboard has 8 letters.")
    S.pattern("me-f5", "IF and VLOOKUP logic", "common",
        "The output of =IF(condition, x, y) for a given cell value, or which column VLOOKUP searches / what the FALSE argument means.",
        None,
        "1. IF tests the condition and returns the second argument when true, the third when false.\n2. VLOOKUP searches the FIRST (leftmost) column of the table vertically and returns from the chosen column number; FALSE asks for an exact match.\n3. Write the condition with the given value substituted, then pick the branch.",
        "=IF(B2>=40, 'Pass', 'Fail') with B2 = 38 returns —",
        "**Fail** — 38 is not greater than or equal to 40, so the third argument is chosen.")
    return S


def build_errors_charts():
    S = Sub("me-errors-charts")
    S.notes = __import__("me_notes").ME_ERRORS_CHARTS
    S.pattern("me-e1", "Error-message identification", "very common",
        "A formula situation is described (divide by empty cell, misspelt function, deleted range, lookup miss) and the error shown is asked — or an error like #NAME? is given and its cause asked.",
        None,
        "1. #DIV/0! = divide by zero/blank; #NAME? = text Excel cannot recognise; #VALUE! = wrong data type; #REF! = deleted reference; #N/A = lookup found nothing.\n2. ##### is NOT an error — it is a narrow column.\n3. Match the story: spelling gives #NAME?, deletion gives #REF!, empty divisor gives #DIV/0!.",
        "Amit types =SUIM(A1:A5) and Excel shows #NAME?. Why?",
        "**The function name is misspelt** — Excel cannot recognise SUIM, and unknown text produces #NAME?.")
    S.pattern("me-e2", "Chart selection by purpose", "very common",
        "'Which chart best shows a trend over time / share of a whole / comparison between categories?' — four chart types as options.",
        None,
        "1. Trend across time = **Line**. Share of one whole = **Pie**. Compare categories = **Column/Bar**. Relation of two number variables = **Scatter**.\n2. A pie handles ONE data series only.\n3. 'Over the years / month-wise growth' words point to a line chart.",
        "To display the monthly sales trend of a year, the best chart is —",
        "**Line chart** — trends across time are its exact purpose; a pie only shows shares of one total.")
    S.pattern("me-e3", "Data tools: sort, filter, pivot, goal seek", "common",
        "A need is described (hide non-matching rows, summarise thousands of rows, find the input that achieves a target) and the tool is asked.",
        None,
        "1. Sort reorders; Filter hides non-matching rows (data is never deleted).\n2. Conditional formatting colours cells by a rule; PivotTable summarises big data into a compact table.\n3. Goal Seek works backwards from a wanted result to the needed input.",
        "Which Excel feature finds the marks needed in the last test so that the average becomes 80?",
        "**Goal Seek** (What-If Analysis) — it adjusts the input cell until the formula reaches the target value.")
    S.pattern("me-e4", "Chart parts and labels", "occasional",
        "The stem asks the name of the chart key that explains colours (legend), the axis holding categories, or the numbers printed on bars (data labels).",
        None,
        "1. **Legend** = the key that says which colour stands for which series.\n2. Category labels usually sit on the horizontal (x) axis, values on the vertical (y) axis — bar charts swap them.\n3. Data labels print the value on each bar or slice.",
        "In an Excel chart, the small key that explains what each colour represents is called the —",
        "**Legend** — without it the reader cannot tell the series apart.")
    return S


def build_shortcuts():
    S = Sub("me-shortcuts")
    S.notes = __import__("me_notes").ME_SHORTCUTS
    S.pattern("me-s1", "Date, time and AutoSum shortcuts", "very common",
        "'Shortcut to insert the current date', 'which key runs AutoSum', 'which key edits the active cell' — with Ctrl+D planted as the date trap.",
        None,
        "1. Date = Ctrl+; (semicolon), time = Ctrl+Shift+;, AutoSum = Alt+= , edit cell = F2.\n2. Ctrl+D is FILL DOWN, not date — the recurring trap.\n3. F4 toggles $ references only while a formula is being edited.",
        "The keyboard shortcut to insert the current date into a cell is:",
        "**Ctrl+;** — it stamps a fixed date. Ctrl+Shift+; stamps the time; Ctrl+D fills the cell above down.")
    S.pattern("me-s2", "Excel file-format facts", "very common",
        "'Default extension of an Excel 2007+ file', identification of .xls/.xlsm/.csv, or which format stores only comma-separated plain values.",
        None,
        "1. Default = .xlsx (2007+, X = XML); .xls = 97-2003; .xlsm = macro-enabled; .csv = comma-separated plain text, one sheet, no formatting.\n2. The X/m/t rule is shared with Word and PowerPoint files.\n3. Macro questions point to the m extension.",
        "The default file extension of an Excel 2016 workbook is:",
        "**.xlsx** — Office Open XML since Excel 2007; .xls is the 97-2003 format.")
    S.pattern("me-s3", "Navigation shortcuts", "common",
        "'Which key jumps to cell A1 / to the last used cell / to the next sheet?' or identification of Ctrl+Home, Ctrl+End, Ctrl+Page Down.",
        None,
        "1. Ctrl+Home = A1; Ctrl+End = last used cell of the data; Ctrl+arrow = edge of the data block.\n2. Ctrl+Page Down / Page Up = next / previous worksheet; Shift+F11 = new sheet.\n3. Ctrl+Tab switches between open workbooks.",
        "Which key combination takes the cursor to the last used cell of a worksheet?",
        "**Ctrl+End** — Ctrl+Home goes to A1, the opposite corner of the used area.")
    S.pattern("me-s4", "Sheet and workbook actions", "occasional",
        "How a new sheet is added, how a sheet is renamed, or the shortcut of Save As / Format Cells.",
        None,
        "1. New worksheet = Shift+F11 (or the + button); rename = double-click the sheet tab.\n2. Save As = F12; Format Cells dialog = Ctrl+1.\n3. Deleting a sheet cannot be undone — Excel warns first.",
        "The shortcut to insert a new worksheet in the open workbook is:",
        "**Shift+F11** — a fresh sheet appears to the left of the current one. F11 alone builds a chart sheet.")
    return S
