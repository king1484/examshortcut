# -*- coding: utf-8 -*-
"""Topic 10: keyboard-shortcuts"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

T = {
  "id": "keyboard-shortcuts",
  "title": "Keyboard Shortcuts",
  "sectionId": "computer",
  "order": 10,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 3},
  "summary": "One consolidated bank of Windows, Word, Excel, PowerPoint, browser and function-key shortcuts. The syllabus names keyboard shortcuts explicitly, and 2-4 of the 20 CKT questions are pure shortcut recall, so these are the cheapest marks in the module.",
  "subtopics": [
    {
      "id": "ks-windows",
      "title": "Windows 10/11 and File Explorer shortcuts",
      "concept": """The **Windows key (Win)** shortcuts control the desktop itself. Most are the same in Windows 10 and Windows 11.

| Shortcut | Action |
|---|---|
| Win | Open/close Start menu |
| Win+D | Show desktop (press again to restore windows) |
| Win+M / Win+Shift+M | Minimise all windows / restore them |
| Win+E | Open File Explorer |
| Win+L | Lock the PC |
| Win+R | Run dialog (type cmd, calc, notepad...) |
| Win+I | Settings |
| Win+S | Search |
| Win+X | Quick Link (power user) menu |
| Win+V | Clipboard history (multiple copied items) |
| Win+Shift+S | Snip part of the screen (Snipping Tool) |
| Win+PrtScn | Save a full-screen screenshot to Pictures\\Screenshots |
| Alt+PrtScn | Copy only the active window to the clipboard |
| Win+. (or Win+;) | Emoji panel |
| Win+Tab | Task View (all open windows + desktops) |
| Win+Ctrl+D / Win+Ctrl+F4 | New virtual desktop / close current one |
| Win+Ctrl+Left/Right | Switch virtual desktops |
| Win+Left/Right/Up/Down | Snap left/right, maximise, minimise/restore |
| Win+Z | Snap layouts (Windows 11) |
| Win+P | Project/display mode (second screen) |
| Alt+Tab | Switch between open windows |
| Alt+F4 | Close the active window (on the desktop: Shut Down dialog) |
| Ctrl+Shift+Esc | Open Task Manager directly |
| Ctrl+Alt+Del | Security screen (lock, sign out, Task Manager) |

**File Explorer:** F2 rename; F3 search box; F5 refresh; Ctrl+Shift+N new folder; Alt+Enter Properties; Alt+Up go up one folder; Alt+Left back; Delete moves to Recycle Bin, **Shift+Delete deletes permanently**; Ctrl+A select all; Ctrl+click selects scattered files; Shift+click selects a range.""",
      "formulas": [],
      "tricks": [
        {"title": "Win + first letter", "body": "Most Win shortcuts use the first letter of the action: **E**xplorer, **L**ock, **R**un, **I** (settIngs), **S**earch, **D**esktop, **M**inimise, **P**roject, **V** (paste history, like Ctrl+V). Learn the letter and you know the key.", "example": {"q": "Win+R opens?", "solution": "The Run dialog (R = Run)."}},
        {"title": "Alt = Active window", "body": "Alt shortcuts act on the window in front of you: Alt+Tab switches it, Alt+F4 closes it, Alt+PrtScn captures only it, Alt+Enter shows the selected item's properties.", "example": {"q": "Which key captures only the active window?", "solution": "Alt+PrtScn."}}
      ],
      "mistakes": [
        "Mixing up Ctrl+Shift+Esc (Task Manager directly) and Ctrl+Alt+Del (security screen with a Task Manager option).",
        "Thinking Win+M toggles like Win+D - Win+M only minimises; Win+Shift+M or Win+D brings windows back.",
        "Saying Delete removes a file permanently - it goes to the Recycle Bin; only Shift+Delete skips it."
      ]
    },
    {
      "id": "ks-common-office",
      "title": "Universal Ctrl keys and MS Word shortcuts",
      "concept": """**Universal Ctrl keys** (work in almost every Windows app):

| Key | Action | Key | Action |
|---|---|---|---|
| Ctrl+N | New file | Ctrl+O | Open |
| Ctrl+S | Save | Ctrl+P | Print |
| Ctrl+Z | Undo | Ctrl+Y | Redo / repeat |
| Ctrl+X / C / V | Cut / copy / paste | Ctrl+A | Select all |
| Ctrl+F | Find | Ctrl+W | Close document/tab |

**MS Word:**

| Shortcut | Action |
|---|---|
| Ctrl+B / I / U | Bold / italic / underline |
| Ctrl+Shift+D | Double underline |
| Ctrl+L / E / R / J | Align left / centre / right / justify |
| Ctrl+1 / Ctrl+2 / Ctrl+5 | Single / double / 1.5 line spacing |
| Ctrl+] / Ctrl+[ | Font size +1 / -1 point |
| Ctrl+Shift+> / < | Next / previous size in the font list |
| Ctrl+D | Font dialog box |
| Ctrl+Shift+A / Ctrl+Shift+K | ALL CAPS / Small Caps |
| Shift+F3 | Change case (cycles) |
| Ctrl+= / Ctrl+Shift+= | Subscript / superscript |
| Ctrl+Space / Ctrl+Q | Remove character / paragraph formatting |
| Ctrl+Shift+C / Ctrl+Shift+V | Copy / paste formatting only |
| Ctrl+H / Ctrl+G (or F5) | Replace / Go To |
| Ctrl+K | Insert hyperlink |
| Ctrl+Enter | Page break |
| Ctrl+M / Ctrl+Shift+M | Increase / decrease indent |
| Ctrl+T | Hanging indent |
| Ctrl+Alt+1/2/3 | Heading 1/2/3 style |
| Ctrl+Shift+8 | Show/hide formatting marks (the pilcrow) |
| Alt+Shift+D / Alt+Shift+T | Insert date / time |
| Ctrl+Home / Ctrl+End | Start / end of the document |
| Ctrl+F2 | Print preview |
| Ctrl+F1 | Collapse/expand the ribbon |
| Alt+Ctrl+F / Alt+Ctrl+D | Footnote / endnote |
| F7 / Shift+F7 | Spelling and grammar / thesaurus |
| Ctrl+Shift+G | Word count |
| F12 | Save As |""",
      "formulas": [],
      "tricks": [
        {"title": "L-E-R-J alignment", "body": "**L**eft, c**E**ntre, **R**ight, **J**ustify. C is already taken by Copy, so centre borrows the E from cEntre.", "example": {"q": "Shortcut to centre a heading in Word?", "solution": "Ctrl+E."}},
        {"title": "Spacing = the number itself", "body": "Ctrl+1 gives single spacing, Ctrl+2 gives double, and Ctrl+5 gives 1.5. Five is the odd one out: read it as 1.5.", "example": {"q": "Ctrl+5 in Word sets?", "solution": "1.5 line spacing."}}
      ],
      "mistakes": [
        "Using Ctrl+C for centre - Ctrl+C copies; centre is Ctrl+E.",
        "Thinking Ctrl+D is 'duplicate' in Word - in Word it opens the Font dialog (duplicate is PowerPoint).",
        "Confusing Ctrl+H: Replace in Word, but History in a web browser."
      ]
    },
    {
      "id": "ks-excel-ppt",
      "title": "MS Excel and PowerPoint shortcuts",
      "concept": """**MS Excel:**

| Shortcut | Action |
|---|---|
| Ctrl+Home / Ctrl+End | Go to A1 / last used cell |
| Ctrl+Arrow | Jump to the edge of the data region |
| Ctrl+PageDown / Ctrl+PageUp | Next / previous worksheet |
| Ctrl+Space / Shift+Space | Select entire column / row |
| Ctrl+D / Ctrl+R | Fill down / fill right |
| Ctrl+Enter | Fill every selected cell with the same entry |
| Ctrl+; / Ctrl+Shift+; | Insert current date / time |
| Alt+= | AutoSum |
| Alt+Enter | New line inside a cell |
| F2 | Edit active cell |
| F4 | Cycle $ reference types (or repeat last action) |
| Shift+F3 | Insert Function dialog |
| F9 | Recalculate all workbooks |
| F11 / Alt+F1 | Chart on a new chart sheet / embedded chart |
| Shift+F11 | Insert new worksheet |
| Ctrl+1 | Format Cells dialog |
| Ctrl+Shift+$ / % / # | Currency / percentage / date format |
| Ctrl+9 / Ctrl+0 | Hide rows / hide columns |
| Ctrl+- / Ctrl+Shift++ | Delete / insert cells |
| Ctrl+T | Create a table |
| Ctrl+E | Flash Fill |
| Ctrl+Shift+L | Toggle filter |
| Ctrl+` | Show formulas instead of results |

**MS PowerPoint:** F5 show from slide 1; Shift+F5 show from the current slide; Esc ends the show; B/W black/white screen; N/P next/previous; number+Enter jumps to a slide; Ctrl+P pen and E erases ink during a show; Ctrl+M new slide; Ctrl+D duplicate; Alt+F5 presenter view.""",
      "formulas": [],
      "tricks": [
        {"title": "Same key, different app", "body": "**Shift+F3**: change case in Word, Insert Function in Excel. **Ctrl+D**: Font dialog in Word, fill down in Excel, duplicate in PowerPoint, bookmark in a browser. **F5**: Go To in Word/Excel, slide show in PowerPoint, refresh in a browser. Always read which application the question names.", "example": {"q": "Shift+F3 in MS Excel opens?", "solution": "The Insert Function dialog (not change case)."}},
        {"title": "Page keys move pages (sheets)", "body": "In Excel, Ctrl+PageDown moves to the next sheet and Ctrl+PageUp to the previous one, as if turning pages of the workbook.", "example": {"q": "Move to the previous worksheet?", "solution": "Ctrl+PageUp."}}
      ],
      "mistakes": [
        "Choosing Ctrl+Shift+; for the date - that inserts the time; the date is Ctrl+;.",
        "Mixing Ctrl+Space (column) with Shift+Space (row).",
        "Answering F11 for 'insert worksheet' - F11 makes a chart sheet; Shift+F11 inserts a worksheet."
      ]
    },
    {
      "id": "ks-browser",
      "title": "Web browser shortcuts (Chrome, Edge, Firefox)",
      "concept": """| Shortcut | Action |
|---|---|
| Ctrl+T / Ctrl+W | New tab / close tab |
| Ctrl+Shift+T | Reopen the last closed tab |
| Ctrl+N | New window |
| Ctrl+Shift+N | Incognito (Chrome) / InPrivate (Edge) window |
| Ctrl+Shift+P | Private window in Firefox |
| Ctrl+Tab / Ctrl+Shift+Tab | Next / previous tab |
| Ctrl+1 ... Ctrl+8 / Ctrl+9 | Jump to tab 1-8 / last tab |
| Alt+Left / Alt+Right | Back / forward |
| Alt+Home | Home page |
| Ctrl+D | Bookmark the current page |
| Ctrl+Shift+B | Show/hide the bookmarks (favourites) bar |
| Ctrl+H / Ctrl+J | History / downloads |
| Ctrl+Shift+Delete | Clear browsing data |
| F5 or Ctrl+R / Ctrl+F5 | Reload / hard reload (skip cache) |
| Esc | Stop loading the page |
| Ctrl+L, Alt+D or F6 | Select the address bar |
| Ctrl+F, then F3 | Find on page, then find next |
| Ctrl++ / Ctrl+- / Ctrl+0 | Zoom in / zoom out / reset zoom |
| Ctrl+U | View page source |
| F12 or Ctrl+Shift+I | Developer tools |
| F11 | Full screen |
| Ctrl+Enter (in address bar) | Adds www. and .com around a typed word |""",
      "formulas": [],
      "tricks": [
        {"title": "Shift = undo the tab", "body": "Ctrl+T opens a tab and **Ctrl+Shift+T** brings back the one you closed. Shift adds 'the opposite' or 'the stronger version': Ctrl+Shift+N is a stronger (private) new window, and Ctrl+Shift+Delete is a stronger delete (all browsing data).", "example": {"q": "You closed a tab by mistake. Shortcut to restore it?", "solution": "Ctrl+Shift+T."}},
        {"title": "Alt+arrows = time travel", "body": "Alt+Left goes back in history and Alt+Right goes forward. Backspace no longer goes back in Chrome.", "example": {"q": "Go back to the previous page?", "solution": "Alt+Left arrow."}}
      ],
      "mistakes": [
        "Saying Ctrl+Shift+N opens a private window in Firefox - Firefox uses Ctrl+Shift+P.",
        "Confusing Ctrl+H (history) with Ctrl+J (downloads).",
        "Thinking Ctrl+W closes the whole browser - it closes only the current tab."
      ]
    },
    {
      "id": "ks-function-keys",
      "title": "Function keys F1-F12",
      "concept": """| Key | Windows / Explorer | MS Office | Browser |
|---|---|---|---|
| F1 | Help | Help | Help |
| F2 | Rename selected item | Edit active cell (Excel) | - |
| F3 | Search in Explorer | Shift+F3: change case (Word), Insert Function (Excel) | Find next |
| F4 | Alt+F4 closes window; address-bar list in Explorer | Repeat last action; cycle $ references (Excel) | - |
| F5 | Refresh | Go To (Word/Excel); start slide show (PowerPoint) | Reload |
| F6 | Cycle through screen elements | Move between panes/ribbon | Focus address bar |
| F7 | - | Spelling and grammar; Shift+F7 thesaurus | Caret browsing |
| F8 | Boot options on older PCs | Extend selection (Word/Excel) | - |
| F9 | - | Recalculate (Excel); update field (Word) | - |
| F10 | Activate menu bar; **Shift+F10 = right-click menu** | Show KeyTips | Menu |
| F11 | Full screen | New chart sheet (Excel); Shift+F11 new worksheet | Full screen |
| F12 | - | Save As | Developer tools |

Exam favourites: **F1 Help, F2 Rename/Edit, F5 Refresh/Slide show, F7 Spell check, F12 Save As, Shift+F10 context menu, Alt+F4 close.**""",
      "formulas": [],
      "tricks": [
        {"title": "1-2-5-7-12 ladder", "body": "F**1** = help (first thing you need), F**2** = rename (give it a 2nd name), F**5** = refresh/show (5 = S for Show), F**7** = spell check (7 letters in 'SPELLER'), F**12** = Save As (end of the row, you save at the end).", "example": {"q": "Which key opens Save As in Word?", "solution": "F12."}},
        {"title": "Shift+F10 = right-click", "body": "Shift+F10 opens the context menu, the same one you get with a right mouse click. The Menu key next to right Ctrl does the same.", "example": {"q": "Keyboard equivalent of a right-click?", "solution": "Shift+F10."}}
      ],
      "mistakes": [
        "Answering F2 for 'refresh' - refresh is F5; F2 renames.",
        "Saying F12 saves normally - F12 is Save As; plain save is Ctrl+S.",
        "Treating F11 the same in every app - full screen in browsers, chart sheet in Excel."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Direct 'which shortcut does X' recall", "frequency": "very common", "howToSpot": "'The shortcut key to ... in MS Word/Excel/Windows is:' with four key combinations as options.", "approach": "Find the app named in the stem first, then use the letter mnemonic (E = cEntre, R = Run, L = Lock). Rule out options that belong to other apps."},
    {"pattern": "'What does key X do' reverse recall", "frequency": "very common", "howToSpot": "'Pressing Shift+F10 / Win+D / Ctrl+Shift+T will:'", "approach": "Translate the modifier: Win = system, Alt = active window, Ctrl+Shift = stronger or opposite version of the Ctrl action."},
    {"pattern": "Function key questions", "frequency": "common", "howToSpot": "'The function key used to rename / refresh / check spelling / Save As is:'", "approach": "Use the ladder F1 help, F2 rename, F5 refresh/show, F7 spelling, F12 Save As; then add Shift/Alt variants."},
    {"pattern": "Same key in different applications", "frequency": "occasional", "howToSpot": "The stem names an app, and a distractor is that key's meaning in another app (Ctrl+D, Shift+F3, F5, Ctrl+H).", "approach": "Keep the 'same key, different app' table in mind and answer only for the app named in the stem."}
  ],
  "solvedExamples": [
    Q("ks-se01",
      "Which Windows shortcut locks the computer immediately, so a password or PIN is needed to return?",
      ["Win+D", "Win+L", "Win+M", "Ctrl+Alt+L"], 1,
      "Win+L locks the workstation and shows the lock screen. Win+D shows the desktop and Win+M minimises all windows, but neither locks anything. Ctrl+Alt+L is not a Windows lock key.",
      "L = Lock.",
      "easy", "ks-windows", "direct recall", 25),
    Q("ks-se02",
      "Pressing Shift+F10 in Windows has the same effect as:",
      ["A double-click", "A right-click (opens the context menu)", "Pressing Alt+Tab", "Pressing the Start button"], 1,
      "Shift+F10 opens the shortcut (context) menu for the selected item, exactly like a right mouse click. F10 on its own activates the menu bar.",
      "Shift+F10 = right-click; F10 alone = menu bar.",
      "medium", "ks-function-keys", "reverse recall", 30),
    Q("ks-se03",
      "In MS Excel, which shortcut moves to the NEXT worksheet in the workbook?",
      ["Ctrl+PageDown", "Ctrl+PageUp", "Ctrl+Tab", "Shift+F11"], 0,
      "Ctrl+PageDown moves to the next sheet and Ctrl+PageUp to the previous one. Shift+F11 inserts a new worksheet rather than moving to one. Ctrl+Tab switches between open workbooks.",
      "Page keys turn the workbook's pages: Down = next, Up = previous.",
      "medium", "ks-excel-ppt", "direct recall", 30),
    Q("ks-se04",
      "In MS Word, Excel and PowerPoint, the F12 key opens the:",
      ["Print dialog", "Save As dialog", "Help pane", "Spelling check"], 1,
      "F12 opens Save As in all Office apps. Ctrl+P prints, F1 opens Help and F7 runs the spelling check.",
      "F12 is at the end of the row, and you Save As at the end of your work.",
      "easy", "ks-function-keys", "function keys", 25)
  ],
  "practice": [
    Q("ks-q01",
      "Which shortcut minimises all open windows to show the desktop, and restores them when pressed again?",
      ["Win+E", "Win+D", "Win+Tab", "Alt+Tab"], 1,
      "Win+D toggles the desktop: the first press hides every window and the second press brings them back. Win+E opens File Explorer, and Win+Tab/Alt+Tab switch windows.",
      "D = Desktop.",
      "easy", "ks-windows", "direct recall", 25),
    Q("ks-q02",
      "In Windows 10/11, pressing Win+V opens:",
      ["The Run dialog", "Clipboard history", "The volume mixer", "Voice typing"], 1,
      "Win+V shows clipboard history, a list of recently copied items you can paste again (it must be switched on the first time). Run is Win+R and voice typing is Win+H.",
      "Ctrl+V pastes one item; Win+V opens the whole paste history.",
      "medium", "ks-windows", "reverse recall", 30),
    Q("ks-q03",
      "Which shortcut lets you drag a box to capture a chosen part of the screen with the Snipping Tool?",
      ["Win+Shift+S", "Ctrl+Shift+S", "Alt+PrtScn", "Win+P"], 0,
      "Win+Shift+S opens the screen snip toolbar (rectangle, free-form, window, full screen). Alt+PrtScn captures only the active window, Win+P changes display projection, and Ctrl+Shift+S is Save As in some apps.",
      "S = Snip; Win+Shift makes it a system-wide snip.",
      "medium", "ks-windows", "direct recall", 30),
    Q("ks-q04",
      "Which key combination switches between open application windows?",
      ["Ctrl+Tab", "Alt+Tab", "Shift+Tab", "Alt+F4"], 1,
      "Alt+Tab cycles through all open windows. Ctrl+Tab switches tabs inside one application, Shift+Tab moves focus backwards, and Alt+F4 closes the window.",
      "Alt = Active window: Alt+Tab switches it, Alt+F4 closes it.",
      "easy", "ks-windows", "direct recall", 25),
    Q("ks-q05",
      "The Run dialog box, used to launch programs such as 'cmd' or 'calc' by name, opens with:",
      ["Win+R", "Win+X", "Ctrl+R", "Alt+R"], 0,
      "Win+R opens Run. Win+X opens the Quick Link (power user) menu. Ctrl+R reloads a browser page and does Fill Right in Excel.",
      "R = Run.",
      "easy", "ks-windows", "direct recall", 25),
    Q("ks-q06",
      "In Windows File Explorer, which shortcut creates a new folder in the current location?",
      ["Ctrl+N", "Ctrl+Shift+N", "Ctrl+Shift+F", "Alt+N"], 1,
      "Ctrl+Shift+N creates a new folder in Explorer. Plain Ctrl+N opens a new Explorer window. In Chrome, Ctrl+Shift+N opens an incognito window.",
      "Ctrl+N = new window; add Shift for a new folder.",
      "medium", "ks-windows", "direct recall", 30),
    Q("ks-q07",
      "A file is selected in File Explorer. Pressing Alt+Enter will:",
      ["Open the file", "Rename the file", "Show the file's Properties", "Delete the file"], 2,
      "Alt+Enter opens the Properties dialog (size, location, dates, attributes). Enter opens the file, F2 renames it and Delete sends it to the Recycle Bin.",
      "Alt+Enter = About this item (Properties).",
      "medium", "ks-windows", "reverse recall", 30),
    Q("ks-q08",
      "In MS Word, Ctrl+J applies which alignment to the selected paragraph?",
      ["Left", "Centre", "Right", "Justify"], 3,
      "Ctrl+J justifies text so both margins are straight. Left is Ctrl+L, centre is Ctrl+E and right is Ctrl+R.",
      "L-E-R-J: Left, cEntre, Right, Justify.",
      "easy", "ks-common-office", "reverse recall", 25),
    Q("ks-q09",
      "Which shortcut sets double line spacing in MS Word?",
      ["Ctrl+1", "Ctrl+2", "Ctrl+5", "Ctrl+D"], 1,
      "Ctrl+2 gives double spacing, Ctrl+1 single spacing and Ctrl+5 1.5 spacing. Ctrl+D opens the Font dialog.",
      "The digit is the spacing; 5 means 1.5.",
      "medium", "ks-common-office", "direct recall", 30),
    Q("ks-q10",
      "The Find and Replace dialog in MS Word opens directly on the Replace tab with:",
      ["Ctrl+F", "Ctrl+H", "Ctrl+R", "Ctrl+G"], 1,
      "Ctrl+H opens Replace. Ctrl+F opens the Navigation (find) pane, Ctrl+G opens Go To, and Ctrl+R right-aligns text.",
      "H = cHange/replace in Word (but History in a browser).",
      "medium", "ks-common-office", "direct recall", 30),
    Q("ks-q11",
      "In MS Excel, pressing Ctrl+Space selects:",
      ["The entire row", "The entire column", "The whole worksheet", "The current region"], 1,
      "Ctrl+Space selects the whole column of the active cell and Shift+Space selects the whole row. Ctrl+A selects the data region, or the whole sheet if pressed again.",
      "Ctrl and Column both start with C; Shift+Space = row.",
      "medium", "ks-excel-ppt", "reverse recall", 30),
    Q("ks-q12",
      "A value is in A2 and the range A2:A10 is selected. Which shortcut copies A2 into A3:A10?",
      ["Ctrl+R", "Ctrl+D", "Ctrl+C", "Ctrl+E"], 1,
      "Ctrl+D (Fill Down) copies the top cell of the selection into the cells below it. Ctrl+R fills right, Ctrl+C only copies to the clipboard, and Ctrl+E is Flash Fill.",
      "D = Down, R = Right.",
      "medium", "ks-excel-ppt", "direct recall", 35),
    Q("ks-q13",
      "In MS Excel, the shortcut Shift+F3 opens the:",
      ["Change Case option", "Insert Function dialog", "Name Manager", "Find dialog"], 1,
      "In Excel, Shift+F3 opens Insert Function (the fx dialog). The change-case meaning belongs to MS Word, which is the trap. Name Manager is Ctrl+F3.",
      "Same key, different app: Word = case, Excel = function.",
      "hard", "ks-excel-ppt", "same key different app", 40),
    Q("ks-q14",
      "In Chrome and Edge, which shortcut opens the 'Clear browsing data' dialog?",
      ["Ctrl+Shift+Delete", "Ctrl+Shift+H", "Ctrl+Delete", "Shift+Delete"], 0,
      "Ctrl+Shift+Delete opens the dialog for clearing history, cookies and cached files. Shift+Delete is permanent file deletion in File Explorer, not a browser command.",
      "Ctrl+Shift = the strong version; the strongest delete wipes browsing data.",
      "medium", "ks-browser", "direct recall", 30),
    Q("ks-q15",
      "Which shortcut takes a web browser back to the previously visited page?",
      ["Alt+Left arrow", "Ctrl+Left arrow", "Alt+Home", "Ctrl+Backspace"], 0,
      "Alt+Left goes back and Alt+Right goes forward. Alt+Home opens the home page, and Ctrl+Left moves the cursor one word left in a text box.",
      "Alt+arrows = time travel through history.",
      "easy", "ks-browser", "direct recall", 25)
  ]
}

validate_and_dump_topic(T)
