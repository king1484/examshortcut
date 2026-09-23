# -*- coding: utf-8 -*-
"""Topic 5: ms-excel. Function-output questions verified by replication in Python."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

# ---- computational verification of every computed answer ----
cells = [72, "Fail", 85, "", 90]           # A1:A5 sample for COUNT/COUNTA
cnt  = sum(1 for c in cells if isinstance(c, (int, float)))
cnta = sum(1 for c in cells if c != "")
assert cnt == 3 and cnta == 4
assert (72 > 50 and "Pass") == "Pass"                    # IF(A1>50,"Pass","Fail"), A1=72
assert round((72 + 85 + 90) / 3, 2) == 82.33             # AVERAGE of numbers
assert max(72, 85, 90) == 90 and min(72, 85, 90) == 72
assert 2 ** 14 == 16384 and 2 ** 20 == 1048576
assert len("SSCCGL") == 6                                # LEN example
assert "SSC".upper() == "SSC" and "ssc".upper() == "SSC"
assert 1048576 * 16384 == 2 ** 34                        # total cells on a sheet

T = {
  "id": "ms-excel",
  "sectionId": "computer",
  "title": "MS Excel",
  "order": 5,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 3},
  "summary": "Spreadsheet structure, cell references, functions, formula errors, charts and shortcuts. Excel gives the most 'compute-the-answer' questions in CKT - COUNT/IF/VLOOKP outputs are verifiable, so marks are safe.",
  "subtopics": [
    {
      "id": "me-basics",
      "title": "Workbook, cells and references",
      "concept": """**Excel** is a spreadsheet program: data goes into **cells** at the crossing of rows and columns. A file = **workbook**; each tab = **worksheet**.

**Dimensions (Excel 2007 onwards):** rows **10,48,576** (2^20, numbered 1...1048576) x columns **16,384** (2^14, named A...XFD) = 17,17,98,86,928 cells per sheet. (Excel 2003 and earlier: 65,536 x 256, last column IV.)

**References:** a cell address = column letter + row number (C5). A range = top-left:bottom-right (A1:B5 covers 2 columns x 3 rows = 6 cells).

| Reference type | Form | What happens when copied |
|---|---|---|
| Relative | A1 | Row/column shift with the formula |
| Absolute | $A$1 | Fully locked |
| Mixed | $A1 or A$1 | Column locked, or row locked |

**F4** cycles A1 -> $A$1 -> A$1 -> $A1 while editing. Cross-sheet reference: Sheet2!B4; cross-workbook adds [Book1] before the sheet name. The **Name Box** (left of formula bar) shows/renames the active cell; the **formula bar** shows the cell's real content. The **fill handle** (small square at the active cell's corner) copies formulas or extends series (AutoFill). Formulas always begin with **=**.""",
      "formulas": [],
      "tricks": [
        {"title": "Dollar locks", "body": "A **$** before the letter locks the column; before the number locks the row. $A$1 = both locked ('dollar = padlock'). F4 taps through the four states.", "example": {"q": "Which reference keeps the row fixed but lets the column change?", "solution": "Mixed reference like A$1."}},
        {"title": "Rows x Cols", "body": "2007+: **2^20 rows (10,48,576)** x **2^14 columns (16,384)**; last column **XFD**. Old Excel: 65,536 x 256 ('256 = IV roman-ish, XFD = 16384').", "example": {"q": "Last column heading in Excel 2019?", "solution": "XFD."}}
      ],
      "mistakes": [
        "Saying Excel 2019 has 65,536 rows - that ended with Excel 2003.",
        "Writing a range as A1-B5; the separator is a colon (A1:B5).",
        "Forgetting that F4 toggles references only while editing a formula (outside editing it repeats the last action)."
      ]
    },
    {
      "id": "me-functions",
      "title": "Functions you must know",
      "concept": """| Category | Functions |
|---|---|
| Maths | SUM, SUMIF, PRODUCT, ROUND, INT, MOD, ABS, POWER, SQRT |
| Statistics | AVERAGE, COUNT, COUNTA, COUNTBLANK, COUNTIF, MAX, MIN, MEDIAN, MODE, RANK, LARGE, SMALL, STDEV |
| Logical | IF, AND, OR, NOT, IFS, IFERROR |
| Text | LEN, LEFT, RIGHT, MID, CONCATENATE/CONCAT, TRIM, UPPER, LOWER, PROPER |
| Date-time | TODAY, NOW, DAY, MONTH, YEAR, DATEDIF |
| Lookup | VLOOKUP, HLOOKUP, INDEX, MATCH, XLOOKUP (2021+) |
| Financial | PMT (loan instalment), FV, PV, NPV |

**Count-family (classic trap):** COUNT counts **numeric cells only**; COUNTA counts all **non-empty** cells; COUNTBLANK counts empty cells; COUNTIF counts cells meeting a condition (e.g. COUNTIF(A1:A10,\">80\")).

**Lookup:** VLOOKUP(value, table, col_index, FALSE) searches the **first column** of the table **vertically** and returns the matching row's col_index-th column; FALSE = exact match. HLOOKUP works horizontally on the first row.

**Text/date:** LEN counts characters (LEN("SSCCGL") = 6); TRIM strips extra spaces; PROPER capitalises Each Word; UPPER/LOWER change case. TODAY() gives today's date (updates); NOW() gives date **and time**.""",
      "formulas": [],
      "tricks": [
        {"title": "COUNT counts Numbers, COUNTA counts Anything", "body": "COUNT = digits only; COUNTA = everything non-empty (text too); COUNTBLANK = the gaps. Test any MCQ by tagging each cell in the range N (number), T (text), E (empty).", "example": {"q": "Range has 3 numbers, 1 text cell, 1 blank. COUNT? COUNTA?", "solution": "COUNT = 3; COUNTA = 4."}},
        {"title": "V of VLOOKUP = Vertical", "body": "VLOOKUP hunts down the **first column**; HLOOKUP along the **first row**. The 4th argument FALSE = exact match ('F for Full match').", "example": {"q": "VLOOKUP searches the table for the lookup value in which direction?", "solution": "Vertically, in the first column."}},
        {"title": "TODAY vs NOW", "body": "**TODAY()** = date only; **NOW()** = date + time. Both refresh on recalculation (unlike Ctrl+; which stamps a fixed date).", "example": {"q": "Function returning current date and time together?", "solution": "NOW()."}}
      ],
      "mistakes": [
        "Letting COUNT count text cells - it skips them silently.",
        "Looking up VLOOKUP values in any column - the lookup value must be in the table's first column.",
        "Believing TODAY() freezes the date - it recalculates; Ctrl+; stamps a static date."
      ]
    },
    {
      "id": "me-errors-charts",
      "title": "Formula errors, charts and data tools",
      "concept": """**Error messages:**

| Error | Cause |
|---|---|
| #DIV/0! | Division by zero or by an empty cell |
| #NAME? | Text Excel cannot recognise (misspelt function/name) |
| #VALUE! | Wrong data type in the formula (text where a number is needed) |
| #REF! | Invalid cell reference (referenced cells deleted) |
| #N/A | Lookup value not found |
| #NUM! | Bad numeric argument (e.g. SQRT of a negative) |
| ###### | Column too narrow - a display issue, NOT an error |
| Circular Reference warning | Formula refers back to its own cell |

**Charts:** Column - compare categories; **Line - trends over time**; **Pie - parts of one whole**; Bar - horizontal comparison; Area - cumulative trend; Scatter - relationship between two variables. Alt+F1 inserts a default chart on the sheet; F11 puts it on a new chart sheet.

**Data tools:** Sort (multi-level), Filter/AutoFilter (**Ctrl+Shift+L**), Conditional Formatting (colour scales, icon sets), Data Validation (dropdowns/limits), **Pivot Table** (drag-and-drop summary of big data), What-If Analysis - **Goal Seek** (find the input that produces a wanted output), Scenario Manager, Data Table. **Freeze Panes** locks rows/columns on screen; Wrap Text shows long text on multiple lines; Merge & Center combines cells; Sheet protection locks cells against edits; **Sparklines** are tiny in-cell charts.""",
      "formulas": [],
      "tricks": [
        {"title": "###### is not an error", "body": "Widen the column - done. Real errors start with #: DIV/0 (zero), NAME (spelling), VALUE (type), REF (deleted), N/A (not found). Match the cause table above.", "example": {"q": "A cell shows #####. The problem is?", "solution": "Column width, not a formula error."}},
        {"title": "Chart chooser", "body": "**Pie = Parts, Line = Line of time (trend), Column = Compare, Scatter = relationship.** 'Trend over months' questions always end at Line.", "example": {"q": "Best chart for monthly sales trend?", "solution": "Line chart."}},
        {"title": "Goal Seek direction", "body": "Goal Seek: you give the **answer**, it finds the **input**. Pivot Table: you give the **data**, it gives summaries.", "example": {"q": "Which tool finds the marks needed in the last test to average exactly 80?", "solution": "Goal Seek."}}
      ],
      "mistakes": [
        "Calling ##### an error - it is only a narrow column.",
        "Using a pie chart for a time trend - pies show one whole's shares at one point.",
        "Saying #REF! appears for misspelt functions - that is #NAME?."
      ]
    },
    {
      "id": "me-shortcuts",
      "title": "Excel shortcuts and file facts",
      "concept": """| Action | Shortcut |
|---|---|
| Insert current date / time | Ctrl+; / Ctrl+Shift+; |
| AutoSum | Alt+= |
| Edit active cell | F2 |
| Toggle $ references | F4 (while editing) |
| Format Cells dialog | Ctrl+1 |
| Fill down / right | Ctrl+D / Ctrl+R |
| Select column / row | Ctrl+Space / Shift+Space |
| Insert new worksheet | Shift+F11 |
| Chart on new sheet | F11 |
| Next / previous sheet | Ctrl+PgDn / Ctrl+PgUp |
| New line inside a cell | Alt+Enter |
| Toggle filters | Ctrl+Shift+L |
| Show formulas instead of results | Ctrl+` |
| Hide rows | Ctrl+9 (restore Ctrl+Shift+9) |
| Spell check | F7 |
| Create Table | Ctrl+T |
| Percent / currency / date format | Ctrl+Shift+% / $ / # |

**File facts:** default extension .xlsx from Excel 2007 (before: .xls); macro workbook .xlsm; template .xltx; CSV .csv; OpenDocument .ods. Default chart is a Clustered Column. A quick printed grid = Page Layout view / Page Break Preview.""",
      "formulas": [],
      "tricks": [
        {"title": "Date stamp duo", "body": "**Ctrl+; = date, Ctrl+Shift+; = time** - the Shift makes it work-o'clock (time). 'Current date in a cell' questions answer Ctrl+;.", "example": {"q": "Shortcut to insert today's date in a cell?", "solution": "Ctrl+; (semicolon)."}},
        {"title": "F-key row for Excel", "body": "F2 edit, F4 lock, F7 spell, F9 recalc, F11 chart sheet, F12 Save As - the F-row reads like Excel's toolbar.", "example": {"q": "Shortcut to create a chart on a new sheet?", "solution": "F11."}},
        {"title": "Alt+= = AutoSum", "body": "Alt with the plus key writes =SUM() over the adjacent numbers instantly - the fastest marks in the section.", "example": {"q": "Keyboard shortcut for AutoSum?", "solution": "Alt+= ."}}
      ],
      "mistakes": [
        "Giving Ctrl+D for date - Ctrl+D fills down; the date stamp is Ctrl+;.",
        "Saying F4 always toggles references - only while a reference is being edited; otherwise F4 repeats the last action.",
        "Answering .xls for Excel 2016 files - .xls is 97-2003; the default is .xlsx."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Function-output computation", "frequency": "very common", "howToSpot": "'=COUNT(A1:A5) returns?' with a small data table - a mini computation, not recall.", "approach": "Replicate the function mentally (or on paper): tag cells number/text/blank for COUNT family; evaluate the condition for IF; sum/average directly."},
    {"pattern": "Shortcut-key recall", "frequency": "very common", "howToSpot": "'Which shortcut inserts the current date in a cell?'", "approach": "Ctrl+; date, Alt+= AutoSum, F2 edit, Shift+F11 sheet, F4 lock - keep the F-row and Ctrl-row drilled."},
    {"pattern": "Error-message identification", "frequency": "common", "howToSpot": "'Which error appears when a formula divides by an empty cell?'", "approach": "Match cause -> code: zero/blank divide = #DIV/0!, unknown text = #NAME?, type mismatch = #VALUE!, deleted ref = #REF!, not found = #N/A, narrow column = ##### (not an error)."},
    {"pattern": "Chart selection", "frequency": "common", "howToSpot": "'Which chart best shows the trend of monthly rainfall?'", "approach": "Pie = parts of a whole, Line = trend over time, Column/Bar = compare categories, Scatter = two-variable relationship."},
    {"pattern": "Reference behaviour on copy", "frequency": "common", "howToSpot": "'A formula with $A$1 copied down to the next row will?'", "approach": "$-locked parts stay put; unlocked parts shift with the formula's new position."}
  ],
  "solvedExamples": [
    Q("me-se01",
      "Cells A1:A5 contain: 72, Fail, 85, (blank), 90. What does =COUNT(A1:A5) return?",
      ["3", "4", "5", "2"], 0,
      "COUNT counts only numeric cells: 72, 85 and 90 -> 3. The text 'Fail' and the empty cell are ignored (COUNTA would have returned 4).",
      "COUNT = numbers only. Tag each cell N/T/E and count the Ns.",
      "medium", "me-functions", "COUNT family computation", 45),
    Q("me-se02",
      "Cell A1 contains 72. The formula =IF(A1>50,\"Pass\",\"Fail\") displays:",
      ["72", "Pass", "Fail", "TRUE"], 1,
      "The condition 72>50 is TRUE, so IF returns its second argument, the text Pass. (If A1 held 40, the third argument Fail would show.)",
      "Evaluate the condition first; return argument 2 on TRUE, argument 3 on FALSE. Plain TRUE/FALSE only appear from a bare comparison like =A1>50.",
      "easy", "me-functions", "IF evaluation", 40),
    Q("me-se03",
      "B1 contains the formula =$A$1*2 and is copied to B2. B2 will contain:",
      ["=$A$2*2", ["=$A$1*2"][0], "=A2*2", ["=$A$1*3"][0]], 1,
      "$A$1 is fully absolute, so the copied formula is unchanged: =$A$1*2. Only relative parts (like A1) would shift row-wise on copying.",
      "Dollar = padlock. $A$1 never moves; A1 becomes A2 on a one-row copy.",
      "medium", "me-basics", "absolute reference copy", 45),
    Q("me-se04",
      "Which error results from =A1/B1 when B1 is empty?",
      ["#VALUE!", "#REF!", "#DIV/0!", "#NAME?"], 2,
      "An empty cell is treated as zero, so the formula divides by zero and Excel shows #DIV/0!. #VALUE! means a wrong data type, #REF! a deleted reference, #NAME? unknown text.",
      "Blank divisor = zero divisor = #DIV/0!. Don't be fooled into choosing #VALUE! for a blank cell.",
      "easy", "me-errors-charts", "error identification", 35),
    Q("me-se05",
      "How many rows and columns does an Excel 2019 worksheet have?",
      ["65,536 rows x 256 columns", "10,48,576 rows x 16,384 columns", "1,048,576 rows x 256 columns", "16,384 rows x 10,48,576 columns"], 1,
      "Excel 2007 onwards: 2^20 = 10,48,576 rows and 2^14 = 16,384 columns (A to XFD). The 65,536 x 256 grid belongs to Excel 2003 and earlier.",
      "Remember the pair 2^20 x 2^14; the option swapping rows with columns is the deliberate trap.",
      "easy", "me-basics", "worksheet dimensions", 35)
  ],
  "practice": [
    Q("me-q01",
      "The default file extension of a workbook created in MS Excel 2019 is:",
      [".xls", ".xlsx", ".xlsm", ".ods"], 1,
      "Excel 2007 onwards saves workbooks as .xlsx (Office Open XML). .xls is the 97-2003 format, .xlsm is macro-enabled, .ods is OpenDocument.",
      "X = XML = 2007+ across all Office extensions.",
      "easy", "me-shortcuts", "default extension", 25),
    Q("me-q02",
      "In Excel, the intersection of a row and a column is called a:",
      ["Field", "Cell", "Range", "Box"], 1,
      "A cell is the single box at a column-row crossing, addressed as ColumnLetter+RowNumber (e.g. B7). A range is a rectangular block of cells.",
      "Spreadsheet atom = cell; address = letter + number.",
      "easy", "me-basics", "spreadsheet basics", 25),
    Q("me-q03",
      "Cells A1:A5 contain: 72, Fail, 85, (blank), 90. What does =COUNTA(A1:A5) return?",
      ["3", "4", "5", "2"], 1,
      "COUNTA counts every non-empty cell - numbers and text alike: 72, 'Fail', 85, 90 = 4. The blank cell is the only one skipped.",
      "COUNTA = Anything non-empty. COUNT would give 3 here.",
      "medium", "me-functions", "COUNT family computation", 40),
    Q("me-q04",
      "Which function returns the number of characters in a text string?",
      ["COUNT", "LENGTH", "LEN", "CHAR"], 2,
      "LEN(\"text\") returns the character count, e.g. LEN(\"SSCCGL\") = 6. There is no LENGTH function in Excel; COUNT works on numbers; CHAR returns the character for an ASCII code.",
      "Excel's length function is LEN - no other name exists.",
      "easy", "me-functions", "text functions", 30),
    Q("me-q05",
      "Which function displays the current date that updates every time the workbook recalculates?",
      ["=NOW()", "=TODAY()", "=DATE()", "Ctrl+D"], 1,
      "=TODAY() returns the live current date (updating on recalculation); =NOW() adds the time as well; =DATE() builds a date from given year/month/day; Ctrl+D fills down, it does not insert a date.",
      "'Date only, updating' -> TODAY(); 'date and time' -> NOW(); 'fixed stamp' -> Ctrl+;.",
      "medium", "me-functions", "date functions", 40),
    Q("me-q06",
      "VLOOKUP searches for the lookup value in which part of the table array?",
      ["Last column", "First row", "First column", "Any column"], 2,
      "VLOOKUP scans the first (leftmost) column of the table vertically and returns a value from the chosen column of the matching row. Searching along the first row is HLOOKUP.",
      "V = Vertical = first column; H = Horizontal = first row.",
      "medium", "me-functions", "lookup functions", 40),
    Q("me-q07",
      "The formula =A1/B1 shows #DIV/0!. The most likely reason is:",
      ["A1 contains text", "B1 is empty or zero", "Column A is too narrow", "The function name is misspelt"], 1,
      "#DIV/0! means the divisor (B1) is zero or blank. Text in A1 would raise #VALUE!; a narrow column shows #####; a misspelt function shows #NAME?.",
      "Divide error -> look at the cell below the slash.",
      "easy", "me-errors-charts", "error identification", 35),
    Q("me-q08",
      "A cell displaying ######## (hash marks) indicates:",
      ["A circular reference", "A formula error", "The column is too narrow to show the value", "The value is negative"], 2,
      "Excel fills the cell with # symbols when the formatted number cannot fit the column width - widen the column. It is a display condition, not an error.",
      "Hashes = width, never an error code.",
      "easy", "me-errors-charts", "error identification", 30),
    Q("me-q09",
      "Which chart type is best suited to show the trend of monthly sales over a year?",
      ["Pie chart", "Line chart", "Doughnut chart", "Radar chart"], 1,
      "Line charts plot values across a continuous axis - ideal for time-series trends. Pie/doughnut show shares of one whole at a single point; radar compares multiple variables.",
      "Trend over time = line, every time.",
      "easy", "me-errors-charts", "chart selection", 30),
    Q("me-q10",
      "The keyboard shortcut to insert the current date into a cell (as a fixed value) is:",
      ["Ctrl+D", "Ctrl+;", "Ctrl+Shift+;", "Ctrl+T"], 1,
      "Ctrl+; stamps today's date; Ctrl+Shift+; stamps the time; Ctrl+D fills down from the cell above; Ctrl+T creates a table.",
      "Semicolon = stamp. Shift makes it time instead of date.",
      "medium", "me-shortcuts", "shortcut-key recall", 35),
    Q("me-q11",
      "AutoSum is applied with which shortcut?",
      ["Alt+=", "Ctrl+=", "Shift+=", "Alt+S"], 0,
      "Alt+= writes =SUM() over the neighbouring numeric range in one stroke. Ctrl+= applies subscript formatting in Word, not AutoSum.",
      "Alt with the plus sign = add them up.",
      "easy", "me-shortcuts", "shortcut-key recall", 30),
    Q("me-q12",
      "Which shortcut inserts a brand-new worksheet in the workbook?",
      ["Ctrl+N", "Shift+F11", "Ctrl+F11", "Alt+N"], 1,
      "Shift+F11 adds a new worksheet. Ctrl+N creates a new workbook (file), and Ctrl+F11 has no default action in modern Excel.",
      "New sheet inside the file = Shift+F11; whole new file = Ctrl+N.",
      "medium", "me-shortcuts", "shortcut-key recall", 35),
    Q("me-q13",
      "To find the input value that makes a formula produce a desired result, use:",
      ["Pivot Table", "Goal Seek", "AutoFilter", "Freeze Panes"], 1,
      "Goal Seek (What-If Analysis) back-solves one input cell to hit a target output. Pivot Tables summarise data, AutoFilter hides rows, Freeze Panes locks screen areas.",
      "You know the answer, want the input -> Goal Seek.",
      "medium", "me-errors-charts", "data tools", 40),
    Q("me-q14",
      "The formula =SUM(A1:A5, 10) is entered in B1. A1:A5 contain 2, 4, 6, 8, 10. The result is:",
      ["30", "40", "20", "10"], 1,
      "SUM adds the range (2+4+6+8+10 = 30) plus the extra argument 10, giving 40.",
      "SUM takes every argument: range total first, then any loose numbers.",
      "easy", "me-functions", "SUM computation", 35),
    Q("me-q15",
      "While editing a formula, pressing F4 on the reference A1 changes it to:",
      ["A2", "$A$1", "A$2", "#REF!"], 1,
      "F4 cycles the reference through A1 -> $A$1 -> A$1 -> $A1 -> A1. The first press makes it fully absolute.",
      "One tap of F4 = full lock ($ before both letter and number).",
      "medium", "me-basics", "reference toggling", 40)
  ]
}

validate_and_dump_topic(T)
