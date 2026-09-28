"""MS Excel deep notes, one string per subtopic."""

ME_BASICS = """### What Excel is
**Excel** is the **spreadsheet** program of Microsoft Office. A spreadsheet is a giant grid made for numbers: marksheets, budgets, attendance, bills. The file is called a **workbook** and each tab inside it is a **worksheet** (or sheet).

### The grid: rows, columns and cells
- **Rows** are numbered 1, 2, 3... and **columns** are lettered A, B, C... Z, then AA, AB... up to **XFD**.
- From Excel **2007 onwards** there are **1,048,576 rows** and **16,384 columns** — about **17.18 billion cells** per sheet. (Excel 2003 and older had only 65,536 rows and 256 columns — a favourite trap.)
- A **cell** is one box at the crossing of a column and a row. Its **cell address** = column letter + row number: **A1, C5, XFD1048576**.
- The **active cell** has a thick green border; the **Name Box** (top-left) shows its address and the **Formula Bar** shows what is really typed in it (text, number or formula).
- A **range** is a rectangle of cells written with a **colon**: A1:B5 means A1 to B5.

### References — what happens on copy
| Type | Written as | When copied |
|---|---|---|
| Relative | A1 | changes with the new position |
| Absolute | $A$1 | stays fixed (the dollar signs lock it) |
| Mixed | $A1 or A$1 | only the unmarked part moves |

While editing a formula, **F4** cycles a reference through A1, $A$1, A$1 and $A1.

### Working with sheets and data
- A new workbook contains **one worksheet** by default (older versions had three). Add another with the **+ button** or **Shift+F11**; rename by **double-clicking the sheet tab**.
- **Text aligns left, numbers align right** automatically — a quick check of what Excel thinks your data is.
- **#####** in a cell only means the **column is too narrow** — widen it; nothing is broken.
- **Ctrl+A** selects the whole sheet; **Ctrl+Home** jumps to A1; **Freeze Panes** (View tab) keeps headings visible while scrolling.
- **AutoFill** — drag the tiny square (fill handle) at the corner of the active cell to copy content or continue a series (Jan, Feb, Mar...). **Ctrl+D** fills the cell above down; **Ctrl+R** fills the cell to the left rightwards.
- Rows and columns can be **hidden** and unhidden (right-click the row number or column letter) — hidden is not deleted.
- **Wrap Text** shows long text on several lines inside one cell; **Merge and Centre** joins selected cells into one wide cell.

### Why the grid is powerful
Excel recalculates automatically: change one mark and every total, average and chart built on it updates at once. This single idea — **formulas store relationships, not fixed numbers** — is why spreadsheets replaced hand-written ledgers, and it is the idea behind most Excel questions: "if this cell changes, what does that formula show?"

### Quick revision
- Workbook = file; worksheet = tab; cell = column letter + row number.
- 2007+: 1,048,576 rows, 16,384 columns (XFD), ~17.18 billion cells.
- $A$1 absolute (locked), A1 relative (moves), F4 toggles while editing.
- Range separator = colon (A1:B5).
- Text left, numbers right; ##### = narrow column, not an error."""

ME_FUNCTIONS = """### Formulas start with =
Every Excel calculation begins with the **= sign**: =A1+B1. Without it, Excel treats "A1+B1" as text. Calculations follow BODMAS order; functions are written as **=NAME(arguments)** with commas between arguments.

### The counting family — the classic exam trap
Range for all examples below: A1=50, A2=70, A3="exam", A4 empty.
| Function | Job | Result here |
|---|---|---|
| =SUM(A1:A4) | adds **numbers** | 120 |
| =AVERAGE(A1:A4) | mean of the **numbers** | 60 |
| =MAX / =MIN | largest / smallest number | 70 / 50 |
| =COUNT | counts cells holding **numbers** | 2 |
| =COUNTA | counts all **non-empty** cells | 3 |
| =COUNTBLANK | counts empty cells | 1 |

**COUNT counts Numbers; COUNTA counts Anything.** Text and blank cells are silently skipped by SUM, AVERAGE and COUNT — that is why COUNTA exists.

### Maths and logic functions
- **=ROUND(1234.567, 2)** gives 1234.57 (round to 2 decimals); **=INT(8.9)** gives 8 (chops the fraction); **=MOD(10, 3)** gives the remainder 1; **=ABS(-9)** gives 9; **=SQRT(144)** gives 12; **=POWER(2, 10)** gives 1024.
- **=IF(test, yes-value, no-value)**: =IF(A1>=40, "Pass", "Fail") prints Pass when A1 holds 50.
- **=COUNTIF(range, criteria)**: =COUNTIF(A1:A10, ">50") counts how many cells exceed 50.

### Text functions
**=LEFT("EXAM", 2)** gives EX; **=RIGHT("EXAM", 3)** gives XAM; **=MID("computer", 4, 3)** gives put (start at 4th letter, take 3); **=LEN("computer")** gives 8; **=UPPER/**=LOWER/**=PROPER change case (PROPER("india gate") gives India Gate); **=CONCATENATE("SS","C")** or "SS"&"C" joins text.

### Lookup and date
- **=VLOOKUP(value, table, column-number, FALSE)** searches for the value in the **first (leftmost) column** of the table and returns the matching entry from the chosen column. The FALSE asks for an **exact match**. The V means the search runs **vertically** down the first column.
- **=TODAY()** shows today's date, **=NOW()** shows date and time — both **recalculate** every time the sheet opens. For a fixed stamp, press **Ctrl+;** (date) or **Ctrl+Shift+;** (time).

### Reading a function question in the exam
1. Write down the cell values from the stem in a small table.
2. Apply the function's rule, remembering what it IGNORES (text, blanks) or where it LOOKS (first column for VLOOKUP).
3. Compute with the ignored cells removed — then match. Distractors are always built from the mistakes: dividing by the full range length, counting text in COUNT, or taking MID from position 0.

### Quick revision
- Every formula starts with =; arguments separated by commas.
- COUNT = numbers only, COUNTA = anything non-empty, COUNTBLANK = empties.
- ROUND rounds, INT chops, MOD gives remainder, SQRT, POWER.
- IF(test, yes, no); COUNTIF counts cells meeting a condition.
- LEFT/RIGHT/MID/LEN/PROPER for text; & joins text.
- VLOOKUP searches the first column vertically; TODAY/NOW recalculate."""

ME_ERRORS_CHARTS = """### Excel error messages — what each one means
| Error | Why it appears |
|---|---|
| **#DIV/0!** | division by **zero or an empty cell** (=A1/B1 with B1 empty) |
| **#NAME?** | Excel does not recognise the text — usually a **misspelt function** (=SUIM) |
| **#VALUE!** | wrong **type** of data (=A1+5 where A1 holds "exam") |
| **#REF!** | a formula points to cells that were **deleted** |
| **#N/A** | a lookup **found nothing** (VLOOKUP misses) |
| **#NUM!** | impossible number, like =SQRT(-4) |
| **#####** | **not an error** — the column is just too narrow |

Memory hooks: DIVide by zero, NAME unknown, VALUE wrong type, REFerence lost.

### Charts — pick by the question the picture must answer
| Chart | Use it for |
|---|---|
| **Column / Bar** | comparing values between categories (sales of 5 branches) |
| **Line** | a **trend over time** (monthly temperature) |
| **Pie** | **shares of one whole** (budget split) — one data series only |
| **Scatter** | relationship between **two number variables** (height vs weight) |

Chart furniture: **chart title**, **legend** (which colour is which series), **axes** with titles, **data labels** (numbers printed on bars), plot area. Insert charts from the Insert tab.

### Data tools
- **Sort** reorders rows A-Z or Z-A (largest to smallest); **Filter** hides rows that do not match a condition — filtering never deletes data.
- **Conditional formatting** paints cells automatically when a rule is true (marks below 35 turn red).
- **PivotTable** summarises thousands of rows into a compact cross-tab in seconds.
- **Goal Seek** (What-If Analysis) works backwards: it changes an input cell until the formula gives the result you want — e.g. what marks are needed to average 80.

### Choosing a chart in three seconds
Ask: what should the reader SEE?
1. A **rise or fall across time** → line chart.
2. **Who is bigger** among a few categories → column (vertical bars) or bar (horizontal bars) chart.
3. **How the total is divided** → pie or doughnut chart (one series only).
4. **Do two measurements move together?** → scatter chart.
Wrong-chart questions reuse this list: a pie for a time trend, a line for a share split, a 3-D explosion of a simple comparison — all wrong picks. Charts live on the **Insert tab**; a selected range plus **F11** makes an instant chart sheet.

### Quick revision
- #DIV/0! zero, #NAME? spelling, #VALUE! wrong type, #REF! deleted cells, #N/A lookup miss, ##### narrow column.
- Column/Bar compare, Line trend, Pie share, Scatter relation.
- Legend tells which colour is which series.
- Sort orders, Filter hides, conditional formatting colours by rule.
- PivotTable summarises; Goal Seek answers "what input gives this result?"."""

ME_SHORTCUTS = """### The Excel shortcut families
| Action | Shortcut |
|---|---|
| Insert today's **date** (fixed) | **Ctrl+;** |
| Insert current **time** (fixed) | **Ctrl+Shift+;** |
| **AutoSum** | **Alt+=** |
| Edit the active cell | **F2** |
| Toggle $A$1 reference types (while editing) | **F4** |
| Format Cells dialog | **Ctrl+1** |
| Fill down / fill right | Ctrl+D / Ctrl+R |
| New workbook / open / save / print | Ctrl+N / Ctrl+O / Ctrl+S / Ctrl+P |
| Save As | **F12** |

The date trap repeats every year: **Ctrl+;** stamps the date — Ctrl+D instead fills the cell above down.

### Moving around a filled sheet
- **Ctrl+Home** jumps to **A1**; **Ctrl+End** jumps to the **last used cell** of the data.
- **Ctrl + arrow key** jumps to the edge of the data block in that direction.
- **Ctrl+Page Down / Page Up** moves between worksheets.
- **Shift+F11** inserts a new worksheet.

### F-key row for Excel
**F2** edit cell, **F4** toggle references (or repeat last action outside editing), **F7** spell check, **F11** instant chart of the selection, **F12** Save As, **Shift+F11** new sheet.

### File formats of Excel
| Extension | Meaning |
|---|---|
| **.xlsx** | default workbook, Excel 2007+ (X = XML) |
| **.xls** | Excel 97-2003 workbook |
| **.xlsm** | macro-enabled workbook |
| **.csv** | comma-separated plain text — opens anywhere, no formatting, one sheet |
| **.xltx / .xltm** | template / macro template |

The same X/m/t rule of Office applies: X = 2007+ default, m = macro, t = template. A **.csv** stores one sheet only and loses formulas' formatting — plain values separated by commas.

### How shortcut questions are framed
Competitive exams ask shortcuts in three shapes: the **direct recall** ("shortcut of AutoSum"), the **reverse** ("Ctrl+; does what?"), and the **trap pair** ("Ctrl+D inserts the date — true or false?"). The trap pairs to burn in:
1. **Ctrl+;** (date) vs **Ctrl+D** (fill down).
2. **F2** (edit cell) vs **F12** (Save As).
3. **Shift+F11** (new sheet) vs **F11** (new chart) vs **Ctrl+N** (new workbook).
4. **Ctrl+1** opens the Format Cells dialog — a plain 1, no Shift, no Ctrl partner.
A few more that appear: **Ctrl+Shift+L** switches filters on and off, **Ctrl+Tab** moves between open workbooks, **Ctrl+W** closes the workbook, and **Ctrl+P** prints — the same Print shortcut as every Office program.

### Quick revision
- Ctrl+; date, Ctrl+Shift+; time, Alt+= AutoSum, F2 edit, F4 reference toggle.
- Ctrl+1 Format Cells, F12 Save As, Shift+F11 new sheet, F11 quick chart.
- Ctrl+Home A1, Ctrl+End last cell, Ctrl+arrows edges of data.
- Default file .xlsx; .xls old; .xlsm macro; .csv = comma-separated plain text."""
