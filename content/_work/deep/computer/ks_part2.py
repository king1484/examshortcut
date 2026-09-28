"""keyboard-shortcuts deep content — part 2: Excel/PowerPoint, browser, function keys."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_excel_ppt():
    S = Sub("ks-excel-ppt")
    S.notes = """### Excel: moving around
| Shortcut | Action |
|---|---|
| **Ctrl+Home** | Jump to cell **A1** |
| **Ctrl+End** | Jump to the last used cell |
| **Ctrl+Page Down / Up** | Next / previous **worksheet** |
| **Ctrl+Arrow key** | Edge of the current data region |
| **F5 / Ctrl+G** | Go To a named cell |
| **Ctrl+F** | Find |

### Excel: selecting and editing
| Shortcut | Action |
|---|---|
| **Ctrl+Space** | Select the whole **column** |
| **Shift+Space** | Select the whole **row** |
| **Ctrl+A** | Select the worksheet/data region |
| **F2** | **Edit** the active cell (also double-click) |
| **Alt+Enter** | New **line inside a cell** |
| **Ctrl+D** | **Fill down** from the cell above |
| **Ctrl+R** | **Fill right** from the cell on the left |
| **Ctrl+;** | Insert today's **date** |
| **Ctrl+Shift+;** | Insert the current **time** |
| **F4** | Cycle absolute and relative references; repeat last action |
| Ctrl+1 | Format Cells dialog |
| Ctrl+Shift+L | Toggle AutoFilter |
| Alt+= | AutoSum |
| Shift+F11 | New worksheet |

Memory hooks: **Ctrl+Space = one column tall and thin; Shift+Space = one row flat.** The **semicolon** gives the timestamp pair — plain ; is date, with Shift it is time (': ' shares the key, time is the shifted thing).

### PowerPoint: running the show
| Shortcut | Action |
|---|---|
| **F5** | Start the slideshow from the **beginning** |
| **Shift+F5** | Start from the **current slide** |
| **Esc** | End the slideshow |
| **B** | Black screen (press again to return); **W** = white screen |
| **N / Space / Right** | Next slide; **P / Left** = previous |
| number + Enter | Jump to that slide number |
| **Ctrl+M** | New slide |
| Ctrl+D | Duplicate the current slide |

Trap set: Ctrl+D **duplicates** a slide in PowerPoint but **fills down** in Excel and opens the **Font dialog** in Word — the same key with three jobs.

### Everyday anchors and worked pairs
| You want to… | Press |
|---|---|
| Put "Total" under every month's column | Type once, then Ctrl+D down the column |
| Jump to the last cell you ever filled | Ctrl+End |
| Type an address over two lines in one cell | Alt+Enter between the lines |
| Stamp today's date on a report | Ctrl+; |
| Check one slide without running the whole deck | Shift+F5 |
| Keep the audience looking at you, not the slide | B (black) during the show |

Ten-second method: the stem gives an action ("select the row", "fill down", "start the show") → recall the family (selection = Space pair, filling = D/R, show = F5/Shift+F5) → eliminate options that swap row/column or F5/Shift+F5.

### Quick revision
- Excel corners: Ctrl+Home → A1, Ctrl+End → last cell; sheets via Ctrl+PgDn/PgUp.
- Whole column Ctrl+Space, whole row Shift+Space; F2 edits, Alt+Enter breaks a line.
- Fill down D, fill right R; date Ctrl+;, time Ctrl+Shift+;.
- Show: F5 from start, Shift+F5 from here, Esc to stop, B black, W white, Ctrl+M new slide."""
    S.pattern("ks-exc-p1", "Excel navigation shortcuts", "common",
        "'Ctrl+Home in Excel takes you to…', 'jump to the last cell', 'move to the next worksheet'.",
        None,
        "1. Ctrl+Home = **A1**, Ctrl+End = last used cell — corner recall.\n2. Worksheets: Ctrl+PgDn next, Ctrl+PgUp previous.\n3. Ctrl+Arrow jumps to the data edge; F5 opens Go To.",
        "In MS Excel, Ctrl+Home moves the cursor to:",
        "Cell **A1** — the home of every worksheet. Ctrl+End goes the other way, to the last used cell.")
    S.pattern("ks-exc-p2", "Row/column selection shortcuts", "common",
        "'Select the entire column', 'select the whole row', 'which selects the entire sheet?' — the Space pair.",
        None,
        "1. **Ctrl+Space = column, Shift+Space = row**; Ctrl+A = whole sheet.\n2. Trap: options swap the two, or offer plain Space (which just extends selection by a cell in some modes).\n3. Anchor line: 'Control the column, Shift the row.'",
        "Which shortcut selects the **entire column** of the active cell in Excel?",
        "**Ctrl+Space** — 'Control the column'; Shift+Space selects the entire row instead.")
    S.pattern("ks-exc-p3", "Excel editing and data-entry shortcuts", "very common",
        "'Edit the contents of a cell', 'enter a new line within a cell', 'fill down', 'insert current date with a shortcut'.",
        None,
        "1. F2 edits the cell; Alt+Enter puts a line break inside it; Ctrl+D fills down, Ctrl+R fills right.\n2. Ctrl+; stamps today's date; Ctrl+Shift+; stamps the time.\n3. F4 cycles dollar signs in a formula (and repeats the last action).",
        "Which key **edits the contents of the active cell** in Excel?",
        "**F2** — it turns the cell into edit mode (the same as double-clicking it).")
    S.pattern("ks-ppt-p4", "PowerPoint slideshow shortcuts", "common",
        "'Start the slide show from the beginning', 'shortcut to end a presentation', 'black screen during a show', 'new slide shortcut'.",
        None,
        "1. F5 = show from slide 1; **Shift+F5 = from the current slide**; Esc = end the show.\n2. B black / W white (press again to come back); N or Space = next; P = previous.\n3. Ctrl+M inserts a new slide; Ctrl+D duplicates the current one.",
        "The shortcut to run a PowerPoint presentation **from the beginning** is:",
        "**F5** — full show. Shift+F5 starts from whichever slide you are on.")
    S.q("ks-exc-p1", "easy", "In MS Excel, **Ctrl+Home** moves the cell pointer to —",
        ["Cell A1", "Cell A1048576", "The top of the visible screen", "The last used cell"], "Cell A1",
        "**Ctrl+Home** = A1. Ctrl+End = the last used cell of the sheet.",
        "Home = A1.", 20)
    S.q("ks-exc-p1", "medium", "Which shortcut moves to the **next worksheet** in the same workbook?",
        ["Ctrl+Page Down", "Alt+Right", "Ctrl+Right", "Shift+Enter"], "Ctrl+Page Down",
        "**Ctrl+PgDn / Ctrl+PgUp** flip through the sheet tabs.",
        "Page = the next sheet of the book.", 25)
    S.q("ks-exc-p1", "medium", "In Excel, **Ctrl+End** takes you to —",
        ["The last used cell of the worksheet", "Cell A1", "The bottom of the current column only", "A new row at the very end"], "The last used cell of the worksheet",
        "**Ctrl+End** jumps to the bottom-right of the used range — the last cell holding data or formatting.",
        "End of what you actually used.", 25)
    S.q("ks-exc-p2", "easy", "Which shortcut selects the **entire row** containing the active cell?",
        ["Shift+Space", "Ctrl+Space", "Alt+Space", "Ctrl+R"], "Shift+Space",
        "**Shift+Space = row**, Ctrl+Space = column.",
        "Shift the row.", 20)
    S.q("ks-exc-p2", "medium", "To select the **entire worksheet** at once, press —",
        ["Ctrl+A", "Ctrl+Space", "Ctrl+E", "F5"], "Ctrl+A",
        "**Ctrl+A** selects all; one press covers the sheet (a second press extends it in older versions).",
        "A = All, everywhere.", 25)
    S.q("ks-exc-p3", "easy", "Which key **edits the active cell** in Excel?",
        ["F2", "F4", "F8", "F10"], "F2",
        "**F2** puts the cell in edit mode — the keyboard version of a double-click.",
        "F2 = 2nd look at the cell.", 20)
    S.q("ks-exc-p3", "medium", "While typing in a cell, which shortcut starts a **new line within the same cell**?",
        ["Alt+Enter", "Ctrl+Enter", "Shift+Enter", "Ctrl+Alt+Enter"], "Alt+Enter",
        "**Alt+Enter** inserts a line break inside the cell. Ctrl+Enter fills all selected cells with the entry instead.",
        "Alt breaks inside.", 25)
    S.q("ks-exc-p3", "easy", "Which shortcut **copies the contents of the cell above** into the active cell?",
        ["Ctrl+D", "Ctrl+C", "Ctrl+V", "Alt+D"], "Ctrl+D",
        "**Ctrl+D = fill down** (from the cell above); **Ctrl+R = fill right**.",
        "D = down.", 20)
    S.q("ks-exc-p3", "medium", "Which shortcut inserts **today's date** into the active cell?",
        ["Ctrl+;", "Ctrl+Shift+;", "Ctrl+D", "Alt+T"], "Ctrl+;",
        "**Ctrl+;** stamps the date; **Ctrl+Shift+;** stamps the current time.",
        "; = date; Shift+; (:) = time.", 25)
    S.q("ks-exc-p3", "hard", "Which statement about **F4** in Excel is correct?",
        ["It cycles a cell reference between absolute, mixed and relative forms", "It saves the workbook", "It deletes the active cell", "It opens the Format Cells dialog"], "It cycles a cell reference between absolute, mixed and relative forms",
        "**F4** toggles absolute/mixed/relative addressing while editing a reference (and repeats the last action outside edit mode). Format Cells is Ctrl+1; saving is Ctrl+S.",
        "F4 = the dollar-sign cycler.", 30)
    S.q("ks-ppt-p4", "easy", "The shortcut to start a **slide show from the beginning** is —",
        ["F5", "F2", "F7", "F12"], "F5",
        "**F5** runs the show from slide 1; **Shift+F5** starts from the current slide.",
        "F5 = full show.", 20)
    S.q("ks-ppt-p4", "easy", "During a slideshow, pressing **B** turns the screen —",
        ["Black", "Blue", "Back one slide", "Brighter"], "Black",
        "**B = black screen, W = white screen**; press the same key again to bring the slide back.",
        "B blots it out.", 20)
    S.q("ks-ppt-p4", "medium", "Which shortcut ends a running **slideshow**?",
        ["Esc", "F4", "Ctrl+Q", "Alt+F4"], "Esc",
        "**Esc** ends the show and returns to the editor.",
        "Escape the stage.", 20)
    S.q("ks-ppt-p4", "medium", "Which shortcut starts the slideshow **from the current slide**?",
        ["Shift+F5", "Shift+F2", "Ctrl+F5", "F6"], "Shift+F5",
        "**Shift+F5** previews from the slide you are editing — ideal when polishing one slide.",
        "Shift = start here.", 25)
    S.q("ks-ppt-p4", "medium", "In PowerPoint, **Ctrl+M** —",
        ["Inserts a new slide", "Minimises the window", "Merges two slides", "Opens the media library"], "Inserts a new slide",
        "**Ctrl+M** adds a new slide (M = 'more slides').",
        "M = more.", 25)
    S.q("ks-exc-p3", "hard", "Match the Excel shortcut:\nA. Ctrl+D  B. Ctrl+R  C. Ctrl+;  D. Alt+Enter",
        ["A-fill down, B-fill right, C-current date, D-new line in cell",
         "A-fill right, B-fill down, C-current time, D-new line in cell",
         "A-fill down, B-new line in cell, C-current date, D-fill right",
         "A-current date, B-fill right, C-fill down, D-new line in cell"],
        "A-fill down, B-fill right, C-current date, D-new line in cell",
        "**D down, R right, ; date, Alt+Enter line-break.**",
        "D-R-date-line.", 35)
    return S


def build_browser():
    S = Sub("ks-browser")
    S.notes = """### Tabs
| Shortcut | Action |
|---|---|
| **Ctrl+T** | New tab |
| **Ctrl+W** (Ctrl+F4) | Close the current tab |
| **Ctrl+Shift+T** | **Reopen the last closed tab** — the undo of Ctrl+W |
| **Ctrl+Tab** | Next tab; Ctrl+Shift+Tab = previous |
| **Ctrl+1…8** | Jump to tab number 1–8 |
| **Ctrl+9** | Jump to the **last** tab (not number 9) |

### Windows and privacy
| Shortcut | Action |
|---|---|
| **Ctrl+N** | New window |
| **Ctrl+Shift+N** | New **Incognito/Private** window (Chrome/Edge) |
| **Ctrl+Shift+P** | Private window in **Firefox** (in Edge/Chrome it prints) |
| **Ctrl+Shift+Delete** | Open **Clear browsing data** |

### Getting around
| Shortcut | Action |
|---|---|
| **Alt+Left / Alt+Right** | Back / forward |
| **Alt+Home** | Open the home page |
| **F5** | Reload; Ctrl+F5 = reload ignoring cache |
| **F11** | Full screen on/off |
| **Ctrl+F** | Find on the page |
| **Ctrl+D** | **Bookmark** this page |
| **Ctrl+Shift+B** | Show/hide the bookmarks bar |
| **Ctrl+H** | **History** |
| **Ctrl+J** | **Downloads** |

### The Ctrl+H / Ctrl+N / Ctrl+D double lives
The same keys do different things in a browser than in Word/Excel:

| Key | Browser | Word / Excel |
|---|---|---|
| Ctrl+H | **History** | Replace (Word) |
| Ctrl+N | New **window** | New **document/workbook** |
| Ctrl+Shift+N | Incognito window | New **folder** (Explorer) |
| Ctrl+D | **Bookmark** | Font dialog (Word) / fill down (Excel) |
| Ctrl+F | Find on page | Find (same idea) |

Read the stem: **'in a web browser'** changes the answer.

### Everyday anchors and worked pairs
| You just… | Do this |
|---|---|
| Closed a tab you still needed | Ctrl+Shift+T brings it back |
| Want a second, separate browsing session | Ctrl+N (normal) or Ctrl+Shift+N (private) |
| Filled a form and want nothing saved | Ctrl+Shift+N / Ctrl+Shift+P window |
| Lost the bookmarks bar | Ctrl+Shift+B |
| Need the page you visited last Tuesday | Ctrl+H |
| Want the installer you downloaded | Ctrl+J |
| Page stuck on an old version | F5 (Ctrl+F5 to bypass cache) |
| Text too small on a crowded page | Ctrl+F to jump straight to the word |

Privacy fact the exams like: Incognito/Private mode stops the browser from **saving history and cookies locally** on that computer — it does not hide your activity from websites, employers or internet providers.

### Quick revision
- Tab trio: T new, W close, Shift+T reopen. Ctrl+9 = last tab, not the 9th.
- Private: Ctrl+Shift+N (Chrome/Edge), Ctrl+Shift+P (Firefox). Clear data: Ctrl+Shift+Delete.
- Back/forward = Alt+Left/Right; home = Alt+Home; full screen = F11.
- Bookmarks Ctrl+D, history Ctrl+H, downloads Ctrl+J."""
    S.pattern("ks-bro-p1", "Browser tab management", "very common",
        "'Open a new tab', 'reopen the accidentally closed tab', 'switch tabs with keyboard', 'close the current tab'.",
        None,
        "1. Trio: Ctrl+**T** new, Ctrl+**W** close, Ctrl+**Shift+T** reopen closed.\n2. Switch: Ctrl+Tab next, Ctrl+Shift+Tab previous, Ctrl+1-8 numbered tabs.\n3. Ctrl+9 is the **last** tab, not the ninth — a classic twist.",
        "You closed a browser tab by mistake. Which shortcut brings it **back**?",
        "**Ctrl+Shift+T** reopens the most recently closed tab (press repeatedly to walk back through them).")
    S.pattern("ks-bro-p2", "Private/incognito windows", "very common",
        "'Shortcut for Incognito/Private mode', 'which browser uses Ctrl+Shift+P?', 'new window vs new tab'.",
        None,
        "1. Chrome/Edge private = **Ctrl+Shift+N**; Firefox private = **Ctrl+Shift+P**.\n2. Plain Ctrl+N = new ordinary window — not private.\n3. Incognito does not make you anonymous; it just avoids saving history/cookies locally (exam phrasing: 'not recorded in browsing history').",
        "Which shortcut opens an **Incognito window** in Google Chrome?",
        "**Ctrl+Shift+N** — N for the new, untracked window. (Firefox's private window uses Ctrl+Shift+P.)")
    S.pattern("ks-bro-p3", "Browser navigation and bookmarks", "common",
        "'Go back to the previous page', 'open the home page', 'bookmark a page with the keyboard', 'show the bookmarks bar'.",
        None,
        "1. Back/forward = **Alt+Left / Alt+Right**; home page = Alt+Home; full screen = F11.\n2. Bookmark = Ctrl+D; toggle the bookmarks bar = Ctrl+Shift+B.\n3. Reload = F5; find on page = Ctrl+F.",
        "In a web browser, which shortcut takes you **back to the previous page**?",
        "**Alt+Left arrow** (Backspace also worked historically, but the exam answer is Alt+Left). Alt+Right goes forward.")
    S.pattern("ks-bro-p4", "History, downloads and clearing data", "very common",
        "'Ctrl+H opens…', 'shortcut to open downloads', 'shortcut that opens the clear-browsing-data dialog'.",
        None,
        "1. **H = History, J = 'get list' → Downloads, Ctrl+Shift+Delete = Clear browsing data.**\n2. Trap: Ctrl+H in Word is Replace — read whether the stem says browser.\n3. Delete in the clear-data combo is the permanent-delete key — fitting for 'wipe history'.",
        "In a web browser, **Ctrl+H** opens —",
        "**Browsing History** — the list of pages you visited. (In MS Word the same keys open Find and Replace.)")
    S.q("ks-bro-p1", "easy", "Which shortcut opens a **new tab** in a web browser?",
        ["Ctrl+T", "Ctrl+N", "Ctrl+Tab", "Alt+T"], "Ctrl+T",
        "**Ctrl+T** = new tab; Ctrl+N = new whole window; Ctrl+Tab = move to the next existing tab.",
        "T = Tab.", 20)
    S.q("ks-bro-p1", "easy", "Which shortcut **closes the current browser tab**?",
        ["Ctrl+W", "Ctrl+Q", "Alt+W", "Shift+W"], "Ctrl+W",
        "**Ctrl+W** (or Ctrl+F4) closes the tab; Alt+F4 would close the entire browser window.",
        "W = wipe this tab.", 20)
    S.q("ks-bro-p1", "medium", "Which shortcut **reopens the last closed tab**?",
        ["Ctrl+Shift+T", "Ctrl+T", "Ctrl+R", "Ctrl+Y"], "Ctrl+Shift+T",
        "**Ctrl+Shift+T** is the undo of Ctrl+W — it restores recently closed tabs one by one.",
        "Shift rescues the closed tab.", 25)
    S.q("ks-bro-p1", "medium", "In a browser, **Ctrl+9** jumps to —",
        ["The last tab", "The ninth tab", "Nine new tabs", "Tab search"], "The last tab",
        "Ctrl+1–8 pick tab numbers 1–8, but **Ctrl+9 always goes to the rightmost (last) tab**, however many are open.",
        "9 = the end of the strip.", 25)
    S.q("ks-bro-p2", "easy", "Which shortcut opens an **Incognito (private) window** in Chrome/Edge?",
        ["Ctrl+Shift+N", "Ctrl+N", "Ctrl+Alt+N", "Ctrl+Shift+P"], "Ctrl+Shift+N",
        "**Ctrl+Shift+N** — Chrome and Edge. Firefox uses Ctrl+Shift+P.",
        "N = no history saved.", 20)
    S.q("ks-bro-p2", "medium", "In **Mozilla Firefox**, a private browsing window opens with —",
        ["Ctrl+Shift+P", "Ctrl+Shift+N", "Ctrl+P", "Alt+P"], "Ctrl+Shift+P",
        "**Ctrl+Shift+P** = Private window in Firefox. (The same keys open the Print dialog in Chrome/Edge.)",
        "Firefox picked P for Private.", 25)
    S.q("ks-bro-p2", "medium", "Which shortcut opens the **Clear browsing data** dialog?",
        ["Ctrl+Shift+Delete", "Ctrl+Delete", "Ctrl+Alt+Delete", "Shift+Delete"], "Ctrl+Shift+Delete",
        "**Ctrl+Shift+Delete** opens the panel to wipe history, cookies and cache.",
        "Delete history with Delete.", 25)
    S.q("ks-bro-p3", "easy", "Which shortcut goes **back to the previous page** in a browser?",
        ["Alt+Left arrow", "Ctrl+Left arrow", "Alt+Down", "Shift+Left"], "Alt+Left arrow",
        "**Alt+Left = back, Alt+Right = forward** — history direction keys.",
        "Alt walks the page trail.", 20)
    S.q("ks-bro-p3", "medium", "**Ctrl+D** in a web browser —",
        ["Bookmarks the current page", "Downloads the page", "Duplicates the tab", "Deletes history"], "Bookmarks the current page",
        "**Ctrl+D = bookmark** ('D for done reading'). Downloads are Ctrl+J.",
        "D = drop a bookmark.", 25)
    S.q("ks-bro-p3", "medium", "Which shortcut toggles the **bookmarks bar**?",
        ["Ctrl+Shift+B", "Ctrl+B", "Alt+B", "Ctrl+Shift+D"], "Ctrl+Shift+B",
        "**Ctrl+Shift+B** shows or hides the bookmarks bar; plain Ctrl+B is bold in documents.",
        "Shift+B = bar.", 25)
    S.q("ks-bro-p3", "hard", "Which statement is correct?",
        ["Ctrl+H shows history but Ctrl+H in Word opens Replace", "Ctrl+H shows history in every program", "Ctrl+D bookmarks a page and duplicates slides in Word", "Alt+Home opens the browser's download page"], "Ctrl+H shows history but Ctrl+H in Word opens Replace",
        "Ctrl+H is **History in browsers, Replace in Word** — same keys, different apps. Ctrl+D duplicates slides in PowerPoint, not Word; the browser home page is Alt+Home (that part of option D is right but its download-page tail is wrong).",
        "Same key, three apps, three jobs.", 30)
    S.q("ks-bro-p4", "easy", "In a web browser, **Ctrl+J** opens —",
        ["Downloads", "History", "Bookmarks", "JavaScript console"], "Downloads",
        "**Ctrl+J = Downloads** list — J for the 'just fetched' files.",
        "J = just downloaded.", 20)
    S.q("ks-bro-p4", "easy", "Which shortcut opens the **browser history** page?",
        ["Ctrl+H", "Ctrl+R", "Ctrl+G", "Alt+H"], "Ctrl+H",
        "**Ctrl+H = History** in Chrome, Edge and Firefox.",
        "H = history.", 20)
    S.q("ks-bro-p4", "medium", "Which shortcut switches the browser to **full screen**?",
        ["F11", "F5", "F12", "Ctrl+F"], "F11",
        "**F11** toggles full screen; F5 reloads; F12 opens developer tools.",
        "F11 fills the screen.", 25)
    S.q("ks-bro-p2", "hard", "Match the app to its private-window shortcut:\nA. Chrome  B. Edge  C. Firefox",
        ["A-Ctrl+Shift+N, B-Ctrl+Shift+N, C-Ctrl+Shift+P",
         "A-Ctrl+Shift+P, B-Ctrl+Shift+N, C-Ctrl+Shift+N",
         "A-Ctrl+Shift+N, B-Ctrl+Shift+P, C-Ctrl+Shift+P",
         "A-Ctrl+P, B-Ctrl+P, C-Ctrl+Shift+P"],
        "A-Ctrl+Shift+N, B-Ctrl+Shift+N, C-Ctrl+Shift+P",
        "Chrome and Edge (Chromium family) share **Ctrl+Shift+N**; only Firefox uses **Ctrl+Shift+P**.",
        "Chromium N, Firefox P.", 35)
    return S


def build_function_keys():
    S = Sub("ks-function-keys")
    S.notes = """### The F1–F12 row, one by one
| Key | Everywhere / Windows | In Office | Elsewhere |
|---|---|---|---|
| **F1** | **Help** | Help | — |
| **F2** | Rename file (Explorer) | Edit cell (Excel) | — |
| **F3** | Search (Explorer) | Insert Function (Shift+F3) | — |
| **F4** | Address-bar dropdown | Repeat last action; cycles absolute refs in formulas | Alt+F4 closes the program |
| **F5** | **Refresh** | Slideshow (PPT) / Go To (Word) | Hard reload Ctrl+F5 |
| **F6** | Cycle screen elements/panes | — | — |
| **F7** | — | **Spelling & grammar** | Caret browsing in browsers |
| **F8** | Safe Mode at start-up (older Windows) | Extend selection | — |
| **F9** | Update fields (Word) | Recalculate | Send/Receive (Outlook) |
| **F10** | Activate the menu bar | — | **Shift+F10 = right-click** |
| **F11** | Full screen (browsers) | Chart sheet (Excel) | — |
| **F12** | Developer tools (browsers) | **Save As** | — |

Memory hooks:
- **One = on-demand help. Two = second name (rename). Five = fresh (refresh). Seven = spellcheck's number. Twelve = twelve dollars — Save As your work.**
- The **Shift+F10 = right-click** rule: F10 summons the menu bar, Shift makes it act where your cursor is — the keyboard's right-click.
- **Alt+F4 closes** the program; **Ctrl+F4 closes only the document/tab** inside it.

### Same key, different apps (the exam's favourite twist)
| Key | Windows | Word | Excel | PowerPoint | Browser |
|---|---|---|---|---|---|
| F5 | Refresh | Go To | Go To | **Slideshow** | Reload |
| F2 | Rename | — | Edit cell | — | — |
| F7 | — | Spellcheck | Spellcheck | Spellcheck | Caret browsing |
| F12 | Dev tools | Save As | Save As | Save As | Dev tools |
| F11 | — | Full screen (Alt) | Chart sheet | — | Full screen |

The stem names the app — **F5 in PowerPoint is the show, F5 on the desktop is refresh**.

### Everyday anchors and worked pairs
| You want to… | Press |
|---|---|
| Understand a button you have never clicked | F1 |
| Give a file a better name | F2 |
| Search a folder full of files | F3 |
| Reload a page that misbehaves | F5 |
| Fix every red squiggle at once | F7 |
| Send the file with a different name | F12 |
| Open the menu without the mouse | F10 (Shift+F10 = right-click menu) |

Ten-second method: the stem gives an action → say the ladder out loud ("help, rename, search, refresh, …") and stop at the match → then check the app named, because F5 and F12 change jobs between Office and the browser.

### Quick revision
- F1 help, F2 rename/edit, F3 search, F5 refresh/show, F7 spelling, F12 save-as/dev-tools.
- Alt+F4 close program; Ctrl+F4 close document; Shift+F10 = right-click; F10 = menu bar.
- F4 repeats the last action (Office) and cycles absolute/relative references (Excel); F8 = Safe Mode at boot (older Windows).
- Shift+F3 toggles case in Word; Shift+F11 adds a worksheet; Ctrl+F5 = reload without cache."""
    S.pattern("ks-fun-p1", "Core F-key identification", "very common",
        "'F1 is used for…', 'which function key refreshes the page?', 'which key is pressed to rename a file?', 'save-as key'.",
        None,
        "1. Ladder recall: **F1 help → F2 rename/edit → F3 search → F5 refresh → F7 spelling → F12 save-as.**\n2. Anchor each with a hook: one = on-demand help, five = fresh, twelve = save.\n3. Check the app named in the stem before locking F5 or F12.",
        "Which function key **refreshes** the active window or web page?",
        "**F5** — the refresh/reload key everywhere on Windows.")
    S.pattern("ks-fun-p2", "F-keys inside Office apps", "very common",
        "'Which key runs the spell check?', 'which key starts the slideshow?', 'Shift+F3 does what in Word?', 'Shift+F11 inserts…'.",
        None,
        "1. Office ladder: F2 edit cell (Excel), F4 repeat/absolute refs, F5 show (PPT)/Go To (Word), F7 spelling, F12 Save As.\n2. Shift variants: Shift+F3 case (Word), Shift+F5 show from current slide, Shift+F11 new worksheet (Excel), Shift+F10 right-click.\n3. The app decides: F5 in PowerPoint = show, F5 in Word = Go To.",
        "Which function key runs **Spelling & Grammar check** in MS Word?",
        "**F7** — the spellchecker's key in Word, Excel and PowerPoint alike.")
    S.pattern("ks-fun-p3", "Modifier + F-key combinations", "common",
        "'Alt+F4 does what?', 'which combination works like right-click?', 'Ctrl+F4 vs Alt+F4', 'Shift+F10 opens'.",
        None,
        "1. Alt+F4 closes the whole program; Ctrl+F4 closes only the open document/tab inside it.\n2. Shift+F10 = the context (right-click) menu; F10 alone activates the menu bar.\n3. Alt+Enter = properties of a file; Alt+Tab = switch windows.",
        "Which key combination works like a **right-click** (opens the shortcut menu)?",
        "**Shift+F10** — it opens the context menu at the current selection, no mouse needed.")
    S.pattern("ks-fun-p4", "One key, many apps (application-dependent F-keys)", "common",
        "'In PowerPoint F5 does what but on the desktop?', 'F12 in a browser vs in Word', 'F11 in Excel vs in a browser', 'which is NOT true about F-keys'.",
        None,
        "1. Build the cross-table: F5 = refresh (Windows/browser) vs slideshow (PPT) vs Go To (Word/Excel).\n2. F12 = Save As (Office) vs developer tools (browsers). F11 = full screen (browser) vs chart sheet (Excel).\n3. Statement questions: verify each clause against the right app before judging true/false.",
        "Which statement about the function keys is **correct**?",
        "F12 has two lives: **Save As** in Office apps, **developer tools** in browsers. F5 shows slides in PowerPoint and refreshes elsewhere; F11 is full screen in browsers, a chart sheet in Excel.")

    S.q("ks-fun-p1", "easy", "Which function key opens **Help** in most programs?",
        ["F1", "F2", "F4", "F12"], "F1",
        "**F1** is the universal help key — one key, one demand for help.",
        "F1 = first resort.", 20)
    S.q("ks-fun-p1", "easy", "Which function key **renames** a selected file or folder?",
        ["F2", "F3", "F5", "F6"], "F2",
        "**F2** renames in File Explorer and edits the active cell in Excel — a second look at the item.",
        "F2 = 2nd name.", 20)
    S.q("ks-fun-p1", "easy", "Which function key **refreshes** the desktop or a web page?",
        ["F5", "F2", "F8", "F10"], "F5",
        "**F5** refreshes; Ctrl+F5 reloads even harder (ignoring the cache).",
        "Five = fresh.", 20)
    S.q("ks-fun-p1", "medium", "Which function key opens the **Save As** dialog in MS Word?",
        ["F12", "F5", "F2", "F9"], "F12",
        "**F12 = Save As** in all Office apps; plain saving stays on Ctrl+S.",
        "12 dollars — save your work.", 25)
    S.q("ks-fun-p1", "medium", "Pressing **F3** in File Explorer opens —",
        ["Search", "The format dialog", "A new folder", "File properties"], "Search",
        "**F3** opens the search box in File Explorer (in Word, Shift+F3 cycles letter case instead).",
        "F3 = find things.", 25)
    S.q("ks-fun-p2", "easy", "Which function key runs the **Spelling & Grammar** check in MS Word?",
        ["F7", "F5", "F3", "F11"], "F7",
        "**F7** spells — in Word, Excel and PowerPoint.",
        "Seven spells.", 20)
    S.q("ks-fun-p2", "easy", "In MS Excel, which key **edits the active cell**?",
        ["F2", "F1", "F7", "F10"], "F2",
        "**F2** puts the cell into edit mode (rename in Explorer, edit in Excel).",
        "Same key, edit sense.", 20)
    S.q("ks-fun-p2", "medium", "**Shift+F11** in MS Excel —",
        ["Inserts a new worksheet", "Saves the workbook", "Opens a chart sheet", "Full screen"], "Inserts a new worksheet",
        "**Shift+F11** adds a fresh worksheet; plain **F11** turns the selection into a **chart sheet**.",
        "Shifted F11 = a blank sheet.", 25)
    S.q("ks-fun-p2", "medium", "In MS Word, **F5** opens the —",
        ["Go To dialog (Find and Replace)", "Slideshow", "Save As dialog", "Print dialog"], "Go To dialog (Find and Replace)",
        "In Word, F5 (like Ctrl+G) opens **Go To** for jumping to a page or line. The slideshow F5 belongs to PowerPoint.",
        "F5 by app: Word = go, PPT = show.", 25)
    S.q("ks-fun-p3", "easy", "Which combination **closes the active program**?",
        ["Alt+F4", "Ctrl+F4", "Shift+F4", "Alt+F8"], "Alt+F4",
        "**Alt+F4** quits the program; **Ctrl+F4** closes only the current document or tab inside it.",
        "Alt = all the way out.", 20)
    S.q("ks-fun-p3", "medium", "**Shift+F10** —",
        ["Opens the shortcut (right-click) menu", "Saves the file", "Maximises the window", "Restarts the PC"], "Opens the shortcut (right-click) menu",
        "**Shift+F10** = the keyboard's right-click; F10 alone highlights the menu bar.",
        "Shifted F10 clicks right.", 25)
    S.q("ks-fun-p3", "medium", "Which combination closes **only the current document**, keeping the application open?",
        ["Ctrl+F4", "Alt+F4", "Ctrl+F2", "Alt+F1"], "Ctrl+F4",
        "**Ctrl+F4** closes the document window inside the app; **Alt+F4** closes the app itself.",
        "Ctrl = close content; Alt = close app.", 25)
    S.q("ks-fun-p3", "hard", "Which pair is **correctly matched**?",
        ["F10 — activates the menu bar; Shift+F10 — right-click menu", "F10 — refresh; Shift+F10 — full screen", "F10 — spellcheck; Shift+F10 — save", "F10 — help; Shift+F10 — rename"],
        "F10 — activates the menu bar; Shift+F10 — right-click menu",
        "**F10** lights up the menu bar; add **Shift** and it behaves as the right-click at your cursor. Refresh is F5, spellcheck F7, help F1, rename F2.",
        "F10 menu, Shift+F10 click.", 30)
    S.q("ks-fun-p4", "medium", "In a web browser, **F12** opens —",
        ["Developer tools", "Save As dialog", "Full screen", "Find bar"], "Developer tools",
        "F12 flips meaning by app: **Save As in Office, developer tools in browsers**.",
        "F12 in a browser = build mode.", 25)
    S.q("ks-fun-p4", "medium", "In MS Excel, **F11** creates —",
        ["A chart sheet from the selected data", "A new worksheet", "A pivot table", "A hyperlink"], "A chart sheet from the selected data",
        "**F11** = chart on its own sheet; **Shift+F11** = new blank worksheet; F11 in a **browser** = full screen.",
        "F11 draws; Shift+F11 adds.", 25)
    S.q("ks-fun-p4", "medium", "Traditionally, pressing which key **during Windows start-up** entered Safe Mode?",
        ["F8", "F2", "F5", "F12"], "F8",
        "**F8** at boot opened the advanced start-up menu with Safe Mode on older Windows versions — a classic exam fact.",
        "Eight = safe escape.", 25)
    S.q("ks-fun-p4", "hard", "Which statement about **F5** is correct?",
        ["It refreshes a web page and starts the slideshow in PowerPoint", "It spell-checks in every application", "It saves the file in Word", "It closes the active program"], "It refreshes a web page and starts the slideshow in PowerPoint",
        "F5 = **refresh/reload** on desktops and browsers, **slideshow** in PowerPoint, **Go To** in Word. Spellcheck is F7; save-as is F12; closing is Alt+F4.",
        "F5: fresh pages, running shows.", 30)
    S.q("ks-fun-p1", "hard", "Arrange the function-key ladder correctly:\nHelp, Rename, Refresh, Save As (Office)",
        ["F1, F2, F5, F12", "F1, F3, F5, F12", "F2, F1, F5, F11", "F1, F2, F7, F12"],
        "F1, F2, F5, F12",
        "Help = **F1**, rename = **F2**, refresh = **F5**, Save As = **F12**.",
        "1-2-5-12 ladder.", 30)
    return S
