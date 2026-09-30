"""Readable rewrite of Computer > MS Excel (4 subtopics). Idempotent."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rl_common import pat, mis, trick, apply  # noqa: E402

# computable facts, asserted
ROWS, COLS = 1048576, 16384
assert ROWS == 2 ** 20 and COLS == 2 ** 14
assert ROWS * COLS == 17179869184
assert 65536 * 256 == 16777216
assert 65536 == 2 ** 16 and 256 == 2 ** 8
# XFD is column 16384: X=24, F=6, D=4 -> 24*676 + 6*26 + 4
assert 24 * 676 + 6 * 26 + 4 == COLS
# IV is column 256: I=9, V=22 -> 9*26 + 22
assert 9 * 26 + 22 == 256
assert 17 % 5 == 2 and len("EXCEL") == 5 and "COMPUTER"[2:5] == "MPU"
assert round(3.14159, 2) == 3.14 and abs(-7) == 7 and 2 ** 5 == 32 and 9 ** 0.5 == 3

SUBS = {}

SUBS["me-basics"] = dict(
    concept=(
        "**MS Excel** is a spreadsheet program. Its work area is a grid of **rows** and **columns**. "
        "Where a row and a column meet is a **cell**, named like **B3**. "
        "A file is a **workbook**, and each page inside it is a **worksheet**. "
        "A formula always begins with an equals sign."
    ),
    notes=r"""### What Excel does
Excel is a **spreadsheet** program. It stores numbers in a grid and calculates with them. People use it for marks, budgets, bills and charts. A file is a **workbook**. Each page inside it is a **worksheet**.

### Rows, columns and cells
- **Rows** run across and have numbers: 1, 2, 3 and so on.
- **Columns** run down and have letters: A, B, C, and after Z comes AA.
- A **cell** is the box where a row and a column cross. Its name is the **cell address**, such as **B3**. The column letter comes first.
- A **range** is a block of cells, written like **A1:C5**.
- The **active cell** is the one that is selected now. Its address shows in the **Name Box**.
- The **Formula Bar** shows what is inside the active cell.

### Size of a worksheet
| Version | Rows | Columns | Last column |
|---|---|---|---|
| Excel 2007 and later | **1,048,576** | **16,384** | **XFD** |
| Excel 97-2003 | 65,536 | 256 | IV |

The new sheet has 1,048,576 rows and 16,384 columns. That gives 17,179,869,184 cells in one sheet. A new workbook opens with one sheet in current versions (Sheet1). Older versions opened with three.

> **Tip:** 1,048,576 is 2 to the power 20. 16,384 is 2 to the power 14.

### Formulas start with =
Every formula begins with an **equals sign**. Without it, Excel treats your entry as plain text. For example, `=A1+B1` adds two cells. `=SUM(A1:A5)` adds five cells.

The operators are + (add), - (subtract), * (multiply), / (divide) and ^ (power). Excel calculates in the usual order: brackets, power, multiply and divide, then add and subtract.

> **Rule:** Text typed in a cell leans **left**. Numbers lean **right**.

### Cell references
| Type | Example | Behaviour when copied |
|---|---|---|
| **Relative** | A1 | Changes with the new position |
| **Absolute** | $A$1 | Never changes |
| **Mixed** | $A1 or A$1 | Only the part without $ changes |

This matters when you copy a formula down a column or across a row. Press **F4** while editing a formula. It cycles A1, $A$1, A$1 and $A1.

> **Watch:** A dollar sign locks what comes right after it. In `$A1` the column is locked. In `A$1` the row is locked.

### Counting functions
- **COUNT** counts cells that hold numbers.
- **COUNTA** counts all cells that are not empty.
- **COUNTBLANK** counts empty cells.
- **COUNTIF** counts cells that meet one condition.

### Files
Data is saved under a file name in a folder, like any other file. The default extension is **.xlsx** (2007 and later). The older format is **.xls**. A macro file is **.xlsm**. A comma-separated text file is **.csv**. A template is **.xltx**.
""",
    tricks=[
        trick("Dollar locks what follows",
              "A dollar sign freezes the letter or number right after it. $A$1 is frozen both ways. $A1 freezes the column only. A$1 freezes the row only."),
        trick("Count family",
              "COUNT wants numbers only. COUNTA counts anything filled in. COUNTBLANK counts the empty ones. COUNTIF needs a condition.",
              "A1:A5 holds 10, 20, text, empty, 30. What does COUNT(A1:A5) give?",
              ["COUNT counts only numbers.", "The numbers are 10, 20 and 30.", "Text and empty cells are skipped."],
              "3"),
    ],
    mistakes=[
        mis("Typing 5+3 in a cell to add.", "Start with an equals sign: =5+3."),
        mis("Reading cell address B3 as row B, column 3.", "The column letter comes first. B3 is column B, row 3."),
        mis("Saying Excel has 256 columns in modern versions.", "Excel 2007 and later has 16,384 columns. 256 is the 97-2003 limit."),
        mis("Using COUNT to count text entries.", "COUNT counts numbers only. COUNTA counts all non-empty cells."),
        mis("Thinking $A1 locks the row.", "In $A1 only the column is locked."),
    ],
    revision=[
        "Excel is a spreadsheet program. A file is a workbook and a page is a worksheet.",
        "Cell address = column letter + row number, such as B3. A range looks like A1:C5.",
        "Modern sheet: 1,048,576 rows and 16,384 columns (last column XFD). Old: 65,536 rows and 256 columns (IV).",
        "Every formula starts with =. Text leans left. Numbers lean right.",
        "Relative A1, absolute $A$1, mixed $A1 or A$1. F4 cycles them.",
        "COUNT numbers, COUNTA non-empty, COUNTBLANK empty, COUNTIF with a condition.",
        "Files: .xlsx default, .xls old, .xlsm macro, .csv text, .xltx template.",
    ],
    patterns=[
        pat("me-b1", "Worksheet size and last cell", "very common",
            "The question asks the number of rows or columns, or the last column name.",
            ["Excel 2007 and later has 1,048,576 rows.", "It has 16,384 columns and the last one is XFD.",
             "Excel 97-2003 has 65,536 rows, 256 columns and last column IV."],
            "Both limits are round powers of two, and the exam asks for the version.",
            "The maximum number of columns in an Excel 2016 worksheet is:",
            ["Excel 2016 is newer than 2007.", "So the modern limit applies.", "The count is 16,384 and it ends at XFD."],
            "16,384"),
        pat("me-b2", "Cell address and range", "very common",
            "The question gives an address or range and asks what it means or how many cells it holds.",
            ["Read the column letter first, then the row number.", "A range uses a colon: start cell to end cell.",
             "Cells in a range = columns wide times rows tall."],
            "The address system is fixed, so the count is simple multiplication.",
            "How many cells are in the range A1:C5?",
            ["Columns A to C make 3 columns.", "Rows 1 to 5 make 5 rows.", "3 times 5 is 15."],
            "15"),
        pat("me-b3", "Relative, absolute and mixed references", "very common",
            "The question copies a formula and asks what changes, or asks what a dollar sign does.",
            ["Find the dollar signs in the formula.", "A locked letter or number never moves when copied.",
             "An unlocked part shifts with the destination.", "F4 cycles the four styles."],
            "A copied formula follows how far it moved, unless a dollar sign locks the part.",
            "A formula =A1 in cell B1 is copied to B2. What does B2 show?",
            ["The formula moved one row down.", "A relative reference moves too.", "A1 becomes A2."],
            "=A2"),
        pat("me-b4", "Formula rules and counting functions", "common",
            "The question asks how a formula starts, or which COUNT function fits a situation.",
            ["Every formula starts with =.", "Use COUNT for numbers and COUNTA for any filled cell.",
             "Use COUNTBLANK for empty cells and COUNTIF for one condition."],
            "The four COUNT functions differ only in what they count.",
            "Which function counts all non-empty cells in a range?",
            ["COUNT would skip text.", "COUNTA counts anything that is filled in."],
            "COUNTA"),
        pat("me-b5", "Workbook, worksheet and file types", "common",
            "The question asks the name of the file, the page, or the default extension.",
            ["A file is a workbook. A page inside it is a worksheet.", "The default extension is .xlsx.",
             "Old format .xls, macro .xlsm, text .csv, template .xltx."],
            "These names are used in every Excel question.",
            "The default file extension of an Excel 2019 workbook is:",
            ["2019 is after 2007.", "The X format applies."], ".xlsx"),
    ],
)

SUBS["me-functions"] = dict(
    concept=(
        "A **function** is a ready-made formula. It has a name and takes inputs in brackets. "
        "Excel groups the common ones into maths, text, logical, lookup and date functions. "
        "Learn the exact result of each function, because the exam asks for the output of a given formula."
    ),
    notes=r"""### How a function looks
A function has a **name** and **arguments** in brackets. For example, `=SUM(A1:A5)`. The arguments are separated by commas. The formula still starts with =.

### Maths functions
| Function | Job | Example | Result |
|---|---|---|---|
| **SUM** | Adds | =SUM(2,3,5) | 10 |
| **AVERAGE** | Mean | =AVERAGE(2,4,6) | 4 |
| **MAX** / **MIN** | Largest / smallest | =MAX(2,9,4) | 9 |
| **ROUND** | Rounds to given digits | =ROUND(3.14159,2) | 3.14 |
| **INT** | Rounds down to whole number | =INT(7.9) | 7 |
| **MOD** | Remainder | =MOD(17,5) | 2 |
| **ABS** | Removes the minus sign | =ABS(-7) | 7 |
| **SQRT** | Square root | =SQRT(9) | 3 |
| **POWER** | Raises to a power | =POWER(2,5) | 32 |

> **Tip:** MOD gives the remainder after division. 17 divided by 5 leaves 2.

### Text functions
| Function | Job | Example | Result |
|---|---|---|---|
| **LEFT** | First characters | =LEFT("EXCEL",2) | EX |
| **RIGHT** | Last characters | =RIGHT("EXCEL",2) | EL |
| **MID** | From the middle | =MID("COMPUTER",3,3) | MPU |
| **LEN** | Counts characters | =LEN("EXCEL") | 5 |
| **UPPER** / **LOWER** | Change case | =UPPER("abc") | ABC |
| **PROPER** | Capital first letter of each word | =PROPER("ram kumar") | Ram Kumar |
| **CONCATENATE** | Joins text | =CONCATENATE("A","B") | AB |

**MID** takes three inputs: the text, the start position and the number of characters. Text inside a formula is written in double quotes.

### Logical function IF
`=IF(condition, value if true, value if false)`

For example, `=IF(A1>=40,"Pass","Fail")` shows Pass when A1 is 40 or more. Otherwise it shows Fail. You can put one IF inside another. That is called a **nested IF**.

> **Rule:** Use AND when all conditions must hold. Use OR when any one is enough.

### Lookup function VLOOKUP
`=VLOOKUP(lookup value, table, column number, FALSE)`

VLOOKUP searches the **first column** of the table. It then returns a value from the column you name. The last input **FALSE** asks for an **exact match**. TRUE (or leaving it out) allows an approximate match. **HLOOKUP** does the same across rows.

### Date functions
- **TODAY()** gives today's date. It has no arguments.
- **NOW()** gives the date and the time.

> **Watch:** Both update every time the sheet recalculates. They are not fixed stamps. Use Ctrl+; for a fixed date.

### Conditional counting and adding
- **COUNTIF(range, condition)** counts cells that meet the test. For example, `=COUNTIF(A1:A10,">40")`.
- **SUMIF(range, condition, sum range)** adds only the cells that meet the test.
- **AVERAGEIF** averages only the matching cells.
- **RANK** gives the position of a number in a list.
""",
    tricks=[
        trick("MOD is the leftover",
              "MOD(a, b) is what is left after a is divided by b. MOD(17,5) is 2, and MOD(10,5) is 0.",
              "What does =MOD(17,5) return?",
              ["17 divided by 5 gives 3 whole times.", "3 times 5 is 15.", "17 minus 15 leaves 2."],
              "2"),
        trick("MID has three inputs",
              "MID(text, start, count). MID(\"COMPUTER\",3,3) starts at the third letter and takes three letters. That gives MPU."),
        trick("FALSE means exact",
              "The last input of VLOOKUP decides how it matches. FALSE means exact match. TRUE means nearest smaller match."),
    ],
    mistakes=[
        mis("Thinking INT(7.9) gives 8.", "INT rounds down. INT(7.9) is 7."),
        mis("Reading MOD(17,5) as 3.", "MOD gives the remainder. That is 2. The 3 is the quotient."),
        mis("Leaving out the quotes around text in a formula.", "Write text in double quotes, such as \"EXCEL\"."),
        mis("Using VLOOKUP with TRUE when an exact match is needed.", "Use FALSE for an exact match."),
        mis("Treating TODAY() as a fixed date.", "TODAY() changes every day. Ctrl+; enters a fixed date."),
    ],
    revision=[
        "A function has a name and arguments in brackets. Formulas begin with =.",
        "ROUND(3.14159,2) is 3.14. INT(7.9) is 7. MOD(17,5) is 2. ABS(-7) is 7. SQRT(9) is 3. POWER(2,5) is 32.",
        "LEFT and RIGHT take from the ends. MID(text,start,count) takes from the middle. LEN counts characters.",
        "UPPER, LOWER, PROPER change case. CONCATENATE joins text.",
        "IF(condition, true value, false value). Nested IF puts one IF inside another.",
        "VLOOKUP searches the first column. FALSE means exact match. HLOOKUP works across rows.",
        "TODAY() gives the date. NOW() gives date and time.",
    ],
    patterns=[
        pat("me-f1", "Output of a maths function", "very common",
            "A formula with ROUND, INT, MOD, ABS, SQRT or POWER is given, and a result is asked.",
            ["Name the function and read its job.", "Work with the numbers inside the brackets.",
             "INT cuts down, ROUND goes to the nearest, MOD is the remainder."],
            "Each function has one clear rule, so the result can be worked out by hand.",
            "What is the result of =POWER(2,5)?",
            ["POWER raises the first number to the second.", "2 to the power 5 is 2 x 2 x 2 x 2 x 2.", "That equals 32."],
            "32"),
        pat("me-f2", "Output of a text function", "very common",
            "A LEFT, RIGHT, MID, LEN or PROPER formula on a word is given.",
            ["Number each letter from 1.", "Apply the start position and the count.", "Count characters for LEN, spaces included."],
            "Text functions work on positions, so counting letters gives the answer.",
            "What does =MID(\"COMPUTER\",3,3) return?",
            ["Letters are C(1) O(2) M(3) P(4) U(5).", "Start at position 3.", "Take three letters: M, P and U."],
            "MPU"),
        pat("me-f3", "IF and nested IF", "very common",
            "A formula with IF is given and a result is asked for some cell value.",
            ["Test the condition with the given cell value.", "If it is true, return the second argument.", "If it is false, return the third argument."],
            "IF picks one of two answers depending on a test.",
            "A1 holds 35. What does =IF(A1>=40,\"Pass\",\"Fail\") show?",
            ["Test 35 >= 40.", "The test is false.", "The third argument is returned."],
            "Fail"),
        pat("me-f4", "VLOOKUP inputs", "common",
            "The question asks what the fourth input of VLOOKUP does, or which column is searched.",
            ["The lookup value is searched in the first column of the table.", "The third input is the column number to return.",
             "FALSE gives an exact match. TRUE gives an approximate match."],
            "VLOOKUP always searches the leftmost column, which is why it cannot look left.",
            "In VLOOKUP, which last argument finds an exact match?",
            ["The last argument sets match type.", "Exact means no nearest guess.", "That is FALSE."],
            "FALSE"),
        pat("me-f5", "TODAY vs NOW", "common",
            "The question asks which function returns only the date, or the date and time.",
            ["TODAY() returns the date only.", "NOW() returns the date and time.", "Neither takes arguments."],
            "The two names hint at the output, and both refresh on recalculation.",
            "Which Excel function returns the current date and time?",
            ["TODAY gives only the date.", "The function with time also is NOW."],
            "NOW()"),
        pat("me-f6", "Text case and joining", "occasional",
            "The question asks which function changes case or joins two pieces of text.",
            ["UPPER makes capitals, LOWER makes small letters.", "PROPER capitalises the first letter of each word.", "CONCATENATE joins the pieces."],
            "Case functions are easy to confuse by name, so match the result.",
            "Which function converts \"ram kumar\" to \"Ram Kumar\"?",
            ["The result has a capital at the start of each word.", "That is the job of PROPER."],
            "PROPER"),
    ],
)

SUBS["me-errors-charts"] = dict(
    concept=(
        "Excel shows an **error value** that starts with # when a formula cannot work. Each error has one cause. "
        "**Charts** turn numbers into pictures: column, line, pie and scatter. "
        "Tools such as filter, PivotTable, Goal Seek and conditional formatting analyse data."
    ),
    notes=r"""### Error values
When Excel cannot finish a formula, it shows an error that starts with #.

| Error | Cause |
|---|---|
| **#DIV/0!** | Division by zero, or by an empty cell |
| **#NAME?** | Excel does not know the name. Usually a misspelt function |
| **#VALUE!** | Wrong type of value, such as adding text to a number |
| **#REF!** | The formula points to a cell that was deleted |
| **#N/A** | A value is not available. Common when a lookup finds no match |
| **#NUM!** | A number problem, such as the square root of a negative number |

> **Watch:** Five hash signs (`#####`) do not mean an error. The column is too narrow to show the number. Widen the column.

### Handling errors
`=IFERROR(value, value if error)` catches any error and shows a replacement. For example, `=IFERROR(A1/B1,0)` shows 0 when B1 is empty or zero.

### Chart types
| Chart | Best for |
|---|---|
| **Column** | Comparing values between items |
| **Bar** | The same, with horizontal bars |
| **Line** | A trend over time |
| **Pie** | Parts of one whole. Uses a single data series |
| **Scatter (XY)** | The link between two numbers |
| **Area** | Change in total over time |

Create a chart from the Insert tab. Select the data first. The shortcut **F11** makes a chart on a new sheet. **Alt+F1** puts a chart on the current sheet.

A chart has a title, axes, a legend, data labels and gridlines. The **X axis** is the category axis. The **Y axis** is the value axis.

> **Tip:** If a question mentions percentages of a total, choose a pie chart.

### Data tools
- **Sort** puts rows in order, from A to Z or from small to large.
- **Filter** hides rows that do not match. The shortcut is **Ctrl+Shift+L**.
- **Conditional formatting** colours cells that meet a rule, such as marks below 40.
- **PivotTable** summarises a large table in a few clicks. It is on the Insert tab.
- **Goal Seek** finds the input that gives a result you want. It is under What-If Analysis on the Data tab.
- **Data Validation** limits what a cell accepts, such as a drop-down list.
- **Freeze Panes** keeps headings in view while you scroll.

> **Example:** Goal Seek answers "What mark do I need in the last test to average 75?"

### Formatting and printing
- **Format Cells** (Ctrl+1) sets number, date, currency and percentage looks.
- **Merge & Center** joins selected cells into one and centres the text.
- **Wrap Text** shows long text on several lines inside one cell.
- **Print Area** and **Page Break Preview** control what prints.
- **Comments** and **Notes** attach remarks to a cell.
- **Sparklines** are tiny charts drawn inside a single cell.
""",
    tricks=[
        trick("Read the error's name",
              "DIV is division. NAME is a spelling problem. VALUE is a wrong type. REF is a reference that is gone. N/A is not available. NUM is a number problem."),
        trick("Pie needs one series",
              "A pie chart shows parts of one whole. It uses a single data series. Use line for trends and scatter for two-number links.",
              "Which chart best shows each state's share of total sales?",
              ["Shares of one whole are needed.", "That is the pie chart's job."],
              "Pie chart"),
    ],
    mistakes=[
        mis("Calling ##### a formula error.", "It only means the column is too narrow. Widen it."),
        mis("Blaming #NAME? on a bad number.", "It usually comes from a misspelt function name."),
        mis("Using a line chart for parts of a whole.", "Use a pie chart for parts of a whole."),
        mis("Confusing Filter with Sort.", "Sort re-orders rows. Filter hides rows."),
        mis("Thinking #REF! comes from division by zero.", "Division by zero gives #DIV/0!. #REF! comes from a deleted cell."),
    ],
    revision=[
        "#DIV/0! divide by zero. #NAME? unknown name. #VALUE! wrong type. #REF! deleted cell. #N/A not available. #NUM! number problem.",
        "##### means the column is too narrow. It is not an error.",
        "IFERROR(value, replacement) replaces any error.",
        "Column compares, line shows trend, pie shows parts of a whole, scatter shows a link between two numbers.",
        "F11 makes a chart on a new sheet. Alt+F1 makes an embedded chart.",
        "Filter Ctrl+Shift+L. PivotTable summarises. Goal Seek finds a needed input. Conditional formatting colours cells.",
    ],
    patterns=[
        pat("me-e1", "Match the error to its cause", "very common",
            "A situation is described and the error name is asked.",
            ["Spot the cause: division, spelling, type, deleted cell, no match, number.", "Match it to the error name.",
             "Remember that ##### is a width problem."],
            "Every error has one cause, and the name hints at it.",
            "Which error appears when a formula divides a number by zero?",
            ["Division by zero is the cause.", "The error name has DIV in it."],
            "#DIV/0!"),
        pat("me-e2", "#NAME?, #VALUE! and #REF! compared", "very common",
            "Three look-alike errors are listed and one must be chosen for a cause.",
            ["Misspelt function gives #NAME?.", "Text used in arithmetic gives #VALUE!.", "A deleted cell gives #REF!."],
            "The three are easy to swap, so tie each to its cause.",
            "=SUMM(A1:A5) is typed by mistake. Which error appears?",
            ["SUMM is not a real function.", "Excel cannot recognise the name."],
            "#NAME?"),
        pat("me-e3", "Choose the right chart", "very common",
            "A data story is given, and the chart type is asked.",
            ["Comparing items points to a column chart.", "A trend over time points to a line chart.",
             "Parts of a whole point to a pie chart.", "Two-number links point to a scatter chart."],
            "Each chart is built for one kind of story.",
            "Monthly sales of a shop for 12 months should be shown as a:",
            ["The data runs over time.", "A trend is needed.", "A line chart shows a trend."],
            "Line chart"),
        pat("me-e4", "Data analysis tools", "common",
            "The question describes a task and asks for the tool.",
            ["Summary of a big table means PivotTable.", "Finding a needed input means Goal Seek.",
             "Colour by rule means conditional formatting.", "Hiding rows that do not match means Filter."],
            "Each tool answers one type of question.",
            "Which tool finds the input needed to reach a target result?",
            ["The target result is fixed.", "The input is unknown.", "Goal Seek works backwards."],
            "Goal Seek"),
        pat("me-e5", "Chart creation keys and parts", "occasional",
            "The question asks the key for a chart or the name of a chart part.",
            ["F11 makes a chart on a new sheet.", "Alt+F1 makes a chart on the same sheet.",
             "X axis holds categories. Y axis holds values."],
            "The shortcuts and axes are short facts asked directly.",
            "Which key creates a chart on a new chart sheet?",
            ["A separate chart sheet is wanted.", "The key is F11."], "F11"),
    ],
)

SUBS["me-shortcuts"] = dict(
    concept=(
        "Excel has its own shortcut keys. **Ctrl+;** enters the date and **Alt+=** adds a sum. "
        "**F2** edits a cell and **Ctrl+1** opens Format Cells. "
        "Learn them in small groups: entering data, editing, selecting and viewing."
    ),
    notes=r"""### Why learn them
Shortcut questions repeat every year. Each key has one fixed job. Learn the groups below.

### Entering data
| Key | Action |
|---|---|
| **Ctrl+;** | Enters today's date as a fixed value |
| **Ctrl+Shift+;** | Enters the current time |
| **Alt+=** | AutoSum. Adds the numbers next to the cell |
| **Ctrl+E** | Flash Fill. Fills a pattern from an example |
| **Alt+Enter** | Starts a new line inside one cell |
| **Ctrl+Enter** | Fills the selected cells with the same entry |

> **Tip:** Ctrl+; gives a fixed date. TODAY() changes every day.

### Editing and formatting
| Key | Action |
|---|---|
| **F2** | Edits the active cell |
| **F4** | Cycles reference type. Also repeats the last action |
| **Ctrl+1** | Opens Format Cells |
| **Ctrl+D** | Fill down. Copies the top cell downward |
| **Ctrl+R** | Fill right. Copies the left cell to the right |
| **Ctrl+T** | Makes a table |
| **Ctrl+Shift+L** | Turns Filter on or off |

### Selecting, rows and columns
| Key | Action |
|---|---|
| **Ctrl+Space** | Selects the whole column |
| **Shift+Space** | Selects the whole row |
| **Ctrl+A** | Selects all cells |
| **Ctrl+9** | Hides the selected rows |
| **Ctrl+0** | Hides the selected columns |
| **Ctrl+Home** | Goes to A1 |
| **Ctrl+End** | Goes to the last used cell |

### Sheets and views
| Key | Action |
|---|---|
| **Shift+F11** | Inserts a new worksheet |
| **F11** | Makes a chart on a new sheet |
| **Ctrl+`** | Shows formulas instead of results |
| **Ctrl+Page Down** | Next sheet |
| **Ctrl+Page Up** | Previous sheet |
| **F12** | Save As |

> **Watch:** Shift+F11 inserts a sheet. F11 alone makes a chart. Exams put them side by side.

### Common keys shared with other programs
Ctrl+C copy, Ctrl+X cut, Ctrl+V paste, Ctrl+Z undo, Ctrl+Y redo, Ctrl+S save, Ctrl+P print, Ctrl+F find, Ctrl+H replace, Ctrl+B bold.

> **Note:** Ctrl+; uses the semicolon key, which sits beside the L key.

### Moving around
| Key | Action |
|---|---|
| **Arrow keys** | Move one cell |
| **Tab** | Move one cell right |
| **Enter** | Move one cell down |
| **Ctrl+Arrow** | Jump to the edge of the data block |
| **Ctrl+G** or **F5** | Go To a cell |

### Clipboard and file keys
| Key | Action |
|---|---|
| **Ctrl+Z** | Undo |
| **Ctrl+Y** | Redo |
| **Ctrl+S** | Save |
| **Ctrl+N** | New workbook |
| **Ctrl+O** | Open a workbook |
| **Ctrl+P** | Print |
| **Ctrl+W** | Close the workbook |

> **Tip:** These file keys work the same in Word and PowerPoint. Learn them once and use them in all three programs.
""",
    tricks=[
        trick("Semicolon for date and time",
              "Ctrl+; enters the date. Add Shift and it enters the time.",
              "Which shortcut enters the current time in Excel?",
              ["Ctrl+; enters the date.", "Adding Shift changes it to the time."],
              "Ctrl+Shift+;"),
        trick("Space picks a line",
              "Ctrl+Space picks the column. Shift+Space picks the row. Remember: Ctrl is the taller shape, a column."),
        trick("D goes down, R goes right",
              "Ctrl+D fills down. Ctrl+R fills right."),
    ],
    mistakes=[
        mis("Using F11 to insert a worksheet.", "Shift+F11 inserts a worksheet. F11 makes a chart."),
        mis("Mixing Ctrl+Space and Shift+Space.", "Ctrl+Space selects a column. Shift+Space selects a row."),
        mis("Using Ctrl+; for time.", "Ctrl+; is date. Ctrl+Shift+; is time."),
        mis("Using Ctrl+D to copy a cell to the right.", "Ctrl+D fills down. Ctrl+R fills right."),
        mis("Thinking Ctrl+9 hides columns.", "Ctrl+9 hides rows. Ctrl+0 hides columns."),
    ],
    revision=[
        "Ctrl+; date. Ctrl+Shift+; time. Alt+= AutoSum. Ctrl+E Flash Fill.",
        "F2 edit cell. F4 cycle references. Ctrl+1 Format Cells.",
        "Ctrl+D fill down. Ctrl+R fill right. Ctrl+T table. Ctrl+Shift+L filter.",
        "Ctrl+Space selects a column. Shift+Space selects a row.",
        "Shift+F11 new sheet. F11 chart sheet. Ctrl+` shows formulas.",
        "Ctrl+9 hides rows. Ctrl+0 hides columns.",
        "Ctrl+Home goes to A1. Ctrl+End goes to the last used cell.",
    ],
    patterns=[
        pat("me-s1", "Date, time and AutoSum keys", "very common",
            "The question asks the key for date, time or automatic sum.",
            ["Ctrl+; enters the date.", "Ctrl+Shift+; enters the time.", "Alt+= inserts AutoSum."],
            "These three are the most repeated Excel shortcuts.",
            "The shortcut key for AutoSum in Excel is:",
            ["AutoSum needs the Alt key.", "It uses the equals sign."], "Alt+="),
        pat("me-s2", "Edit, format and fill keys", "very common",
            "The question asks the key for editing a cell, opening Format Cells or filling.",
            ["F2 edits the cell.", "Ctrl+1 opens Format Cells.", "Ctrl+D fills down. Ctrl+R fills right."],
            "Each key has a memorable link: D for down, R for right.",
            "Which key puts the active cell into edit mode?",
            ["Editing a cell needs the cell to be active.", "The function key F2 does this."], "F2"),
        pat("me-s3", "Row and column selection and hiding", "common",
            "The question asks how to select or hide a row or a column.",
            ["Ctrl+Space selects a column.", "Shift+Space selects a row.", "Ctrl+9 hides rows. Ctrl+0 hides columns."],
            "Row and column keys are close, so options swap them.",
            "Which shortcut selects an entire row in Excel?",
            ["A row has a low, flat shape.", "The key is Shift+Space."], "Shift+Space"),
        pat("me-s4", "Sheet, chart and formula-view keys", "common",
            "The question asks for a new sheet, a chart or the formula view.",
            ["Shift+F11 inserts a sheet.", "F11 makes a chart sheet.", "Ctrl+` shows formulas."],
            "F11 with or without Shift does two different jobs.",
            "Which shortcut inserts a new worksheet?",
            ["A chart uses F11 alone.", "A sheet adds Shift."], "Shift+F11"),
        pat("me-s5", "Flash Fill, filter and table keys", "occasional",
            "The question asks for the key that fills a pattern, or turns on filter or table.",
            ["Ctrl+E starts Flash Fill.", "Ctrl+Shift+L toggles filter.", "Ctrl+T makes a table."],
            "These newer keys are asked in recent papers.",
            "Which shortcut turns Filter on or off in Excel?",
            ["Filter uses Ctrl and Shift.", "The letter is L."], "Ctrl+Shift+L"),
    ],
)

def esc(o):
    """Escape literal dollar signs so they are not read as math (site convention: backslash-dollar)."""
    if isinstance(o, str):
        return o.replace("$", "\\$")
    if isinstance(o, list):
        return [esc(x) for x in o]
    if isinstance(o, dict):
        return {k: esc(v) for k, v in o.items()}
    return o


SUBS = esc(SUBS)
apply("ms-excel.json", SUBS)
