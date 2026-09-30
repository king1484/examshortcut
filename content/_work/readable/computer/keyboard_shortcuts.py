"""Readable rewrite of Computer > Keyboard Shortcuts (5 subtopics). Idempotent."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rl_common import pat, mis, trick, apply  # noqa: E402

SUBS = {}

# =====================================================================
SUBS["ks-windows"] = dict(
    concept=(
        "The **Windows key** (Win) controls the desktop itself. Most Win shortcuts use the **first letter** of the job: "
        "E for Explorer, L for Lock, R for Run. Learn also the security pair **Ctrl+Shift+Esc** and **Ctrl+Alt+Del**, "
        "the File Explorer keys, and Alt+Tab and Alt+F4."
    ),
    notes=r"""### The Win key family
The **Win key** is the flag key between Ctrl and Alt. Most Win shortcuts use the first letter of the action.

| Shortcut | Action |
|---|---|
| **Win** | Open or close the Start menu |
| **Win+D** | Show the desktop. Press again to bring the windows back |
| **Win+E** | Open File Explorer |
| **Win+L** | **Lock** the computer |
| **Win+R** | Open the **Run** box, where you type cmd, calc or notepad |
| **Win+I** | Open Settings |
| **Win+S** | Open Search |
| **Win+M** | Minimise all windows |
| **Win+Shift+M** | Restore the minimised windows |
| **Win+Tab** | Task view. Shows all windows and virtual desktops |
| **Win+Left / Right / Up / Down** | Snap a window to half or a corner of the screen |
| **Win+PrtScn** | Save a screenshot in the Pictures folder |
| **Win+Shift+S** | Snip a chosen part of the screen |
| **Win+V** | Clipboard history |

> **Watch:** Win+D toggles. Win+M only minimises. Win+Shift+M is needed to restore.

### The security pair
| Combination | What appears |
|---|---|
| **Ctrl+Shift+Esc** | **Task Manager** directly. This is the fastest route |
| **Ctrl+Alt+Del** | A full-screen menu with Lock, Switch user, Sign out and Task Manager |
| **Alt+F4** | Closes the active program |

> **Tip:** On the desktop with no program open, Alt+F4 opens the Shut Down box.

### File Explorer keys
| Shortcut | Action |
|---|---|
| **Ctrl+Shift+N** | New folder |
| **F2** | Rename the selected item |
| **Alt+Enter** | Properties of the selected item |
| **Alt+Up arrow** | Go up one folder level |
| **Delete** | Send to the Recycle Bin |
| **Shift+Delete** | Delete permanently, skipping the Recycle Bin |
| **Ctrl+A** | Select everything |

### Switching and closing windows
- **Alt+Tab** switches between open windows. Hold Alt and tap Tab.
- **Win+D** or **Win+M** clears the screen to the desktop.
- **Win+arrow keys** park a window on half the screen. This is good for comparing two documents.
- **Alt+F4** closes the whole program. **Ctrl+F4** closes only one document inside it.

> **Rule:** Read the verb in the question: switch, close, open or lock. Then pick the key family.

### How questions sound
| The question says | Answer |
|---|---|
| Opens File Explorer | Win+E |
| Locks the computer | Win+L |
| Opens the Run dialog box | Win+R |
| Opens Task Manager directly | Ctrl+Shift+Esc |
| Switches between open programs | Alt+Tab |
| Closes the active program | Alt+F4 |
| Creates a new folder | Ctrl+Shift+N |
| Renames the selected file | F2 |
""",
    tricks=[
        trick("First-letter rule",
              "E is Explorer, L is Lock, R is Run, D is Desktop, S is Search, I is settIngs. The letter hints at the job."),
        trick("Direct vs menu",
              "Ctrl+Shift+Esc opens Task Manager straight away. Ctrl+Alt+Del first opens a menu, and Task Manager is one option there.",
              "Which shortcut opens Task Manager directly, with no menu first?",
              ["Ctrl+Alt+Del shows a menu first.", "The direct key uses Esc."],
              "Ctrl+Shift+Esc"),
    ],
    mistakes=[
        mis("Saying Win+M restores the windows.", "Win+M minimises. Win+Shift+M restores."),
        mis("Using Ctrl+Alt+Del to open Task Manager directly.", "It opens a menu. Ctrl+Shift+Esc is the direct key."),
        mis("Mixing Alt+F4 with Ctrl+F4.", "Alt+F4 closes the program. Ctrl+F4 closes only the document."),
        mis("Thinking Delete removes a file permanently.", "Delete sends it to the Recycle Bin. Shift+Delete removes it permanently."),
        mis("Using Win+R to lock the computer.", "Win+L locks. Win+R opens the Run box."),
    ],
    revision=[
        "First letter rule: E Explorer, L Lock, R Run, D Desktop, S Search.",
        "Win+D toggles the desktop. Win+M only minimises. Win+Shift+M restores.",
        "Ctrl+Shift+Esc opens Task Manager directly. Ctrl+Alt+Del shows the security screen.",
        "Explorer: Ctrl+Shift+N new folder, F2 rename, Alt+Enter properties, Alt+Up one level.",
        "Alt+Tab switches windows. Alt+F4 closes the program.",
        "Shift+Delete deletes permanently.",
    ],
    patterns=[
        pat("ks-win-p1", "Win-key shortcut recall", "very common",
            "The question describes a job and asks for a Win shortcut.",
            ["Take the first letter of the job.", "Add the Win key.", "Check the list: D, E, L, R, I, S, M, V."],
            "The first-letter rule covers most Win keys.",
            "Which shortcut opens the Run dialog box?",
            ["Run starts with R.", "The Win key comes first."], "Win+R"),
        pat("ks-win-p2", "Task Manager and security combos", "very common",
            "The question says direct, or asks about the security screen.",
            ["Direct Task Manager is Ctrl+Shift+Esc.", "The full-screen menu is Ctrl+Alt+Del.", "Alt+F4 closes a program."],
            "The two look alike, but only one is direct.",
            "The shortcut key to open Task Manager directly is:",
            ["Ctrl+Alt+Del shows a menu first.", "The direct one has Esc."], "Ctrl+Shift+Esc"),
        pat("ks-win-p3", "File Explorer shortcuts", "very common",
            "The question gives a file job, such as rename, new folder or properties.",
            ["F2 renames.", "Ctrl+Shift+N makes a new folder.", "Alt+Enter opens Properties.", "Shift+Delete deletes permanently."],
            "Explorer keys are a small set, each with one job.",
            "Which key renames the selected file in File Explorer?",
            ["Rename is the second name.", "The key is F2."], "F2"),
        pat("ks-win-p4", "Window switching and closing", "common",
            "The question asks how to switch windows or close a program.",
            ["Alt+Tab switches.", "Alt+F4 closes the program.", "Win+D shows the desktop."],
            "Alt is the key for switching and closing.",
            "Which shortcut switches between open windows?",
            ["Switching uses the Alt key.", "The second key is Tab."], "Alt+Tab"),
        pat("ks-win-p5", "Screenshot and snap keys", "occasional",
            "The question asks for a screenshot or window snapping.",
            ["Win+PrtScn saves a screenshot in Pictures.", "Win+Shift+S snips a chosen area.", "Win+arrows snap windows."],
            "Newer Windows keys appear in recent papers.",
            "Which shortcut lets you snip a selected part of the screen?",
            ["Snip starts with S.", "It needs Win and Shift."], "Win+Shift+S"),
    ],
)

# =====================================================================
SUBS["ks-common-office"] = dict(
    concept=(
        "A group of **Ctrl keys** works in almost every Windows program: N, O, S, P, X, C, V, Z, Y, A and F. "
        "Formatting keys are mainly for Word. Some keys have **double lives**, such as Ctrl+H, Ctrl+D and Ctrl+Shift+N. "
        "The app named in the question decides the answer."
    ),
    notes=r"""### The universal Ctrl keys
These keys work in nearly every Windows app.

| Key | Action | Key | Action |
|---|---|---|---|
| **Ctrl+N** | New file | **Ctrl+O** | Open |
| **Ctrl+S** | Save | **Ctrl+P** | Print |
| **Ctrl+Z** | **Undo** | **Ctrl+Y** | Redo |
| **Ctrl+X** | Cut | **Ctrl+C** | Copy |
| **Ctrl+V** | Paste | **Ctrl+A** | Select all |
| **Ctrl+F** | Find | **Ctrl+W** | Close the document or tab |
| **Ctrl+K** | Insert hyperlink | **Ctrl+B, I, U** | Bold, italic, underline |

Letter logic: X looks like scissors, so it cuts. V looks like a paste arrow. Z takes you back. A means all.

### Formatting keys
| Shortcut | Action |
|---|---|
| Ctrl+B / I / U | Bold / italic / underline |
| **Ctrl+L / E / R / J** | Left / centre / right / justify |
| **Ctrl+1 / Ctrl+2 / Ctrl+5** | Single / double / 1.5 line spacing |
| **Ctrl+Shift+D** | Double underline |
| **Shift+F3** | Cycles the case of selected text |

> **Tip:** C is taken by Copy, so Centre borrows E from "cEntre". Spacing uses the number itself, and 5 stands for 1.5.

### Find, replace and go to
- **Ctrl+F** opens Find. In Word it opens the Navigation pane. In a browser it finds text on the page.
- **Ctrl+H** is **Replace** in Word and Excel.
- **Ctrl+G** and **F5** open Go To in Word.
- **Ctrl+Home** jumps to the start of the document. **Ctrl+End** jumps to the end.

### Undo and friends
- **Ctrl+Z** undoes the last action. Press again to undo more.
- **Ctrl+Y** redoes it.
- **Ctrl+S** saves. Save often.
- **F12** is Save As in Office programs.

### The double-life table
| Key | Word / Excel | Browser | Explorer |
|---|---|---|---|
| Ctrl+H | **Replace** | History | none |
| Ctrl+D | Font box (Word) or fill down (Excel) | **Bookmark** | none |
| Ctrl+Shift+N | none | Incognito window | **New folder** |
| Ctrl+F | Find | Find on page | Search box |
| Ctrl+W | Close document | Close tab | Close window |

### Moving and selecting text
| Shortcut | Action |
|---|---|
| **Ctrl+Left / Right arrow** | Move one word left or right |
| **Shift+Arrow** | Select one character or line at a time |
| **Ctrl+Shift+Arrow** | Select one word at a time |
| **Home / End** | Go to the start or end of the line |
| **Ctrl+Backspace** | Delete the word before the cursor |

> **Rule:** Read the app named in the question first. It changes the answer for half of the keys here.

### Copy and paste family
- **Ctrl+C** copies. **Ctrl+X** cuts. **Ctrl+V** pastes.
- Copy leaves the original in place. Cut removes it.
- **Ctrl+Shift+V** pastes without formatting in many programs.
- **Win+V** shows the clipboard history in Windows.

> **Example:** "In MS Excel, Ctrl+D will..." The answer is fill down. In Word it opens the Font box. In a browser it bookmarks the page.
""",
    tricks=[
        trick("N-O-S-P and X-C-V",
              "New, Open, Save, Print are N, O, S, P. Cut, Copy, Paste are X, C, V. Undo and Redo are Z and Y."),
        trick("App decides",
              "Ctrl+H is Replace in Word and History in a browser. Look for the app name in the question before choosing.",
              "In a web browser, Ctrl+H opens:",
              ["The app is a browser.", "In Word it would be Replace.", "In a browser it opens History."],
              "History"),
    ],
    mistakes=[
        mis("Reading Ctrl+Y as Undo.", "Ctrl+Z is Undo. Ctrl+Y is Redo."),
        mis("Using Ctrl+C to centre.", "Ctrl+C is Copy. Centre is Ctrl+E."),
        mis("Saying Ctrl+H is Replace everywhere.", "In a browser Ctrl+H opens History."),
        mis("Confusing Ctrl+W with Alt+F4.", "Ctrl+W closes a document or tab. Alt+F4 closes the program."),
        mis("Using Ctrl+5 for double spacing.", "Ctrl+2 is double. Ctrl+5 is 1.5."),
    ],
    revision=[
        "N-O-S-P: New, Open, Save, Print. X-C-V: Cut, Copy, Paste. Z Undo, Y Redo.",
        "Ctrl+L, E, R, J are left, centre, right, justify. Ctrl+1, 2, 5 are single, double, 1.5 spacing.",
        "Ctrl+F is Find. Ctrl+H is Replace in Word and Excel but History in a browser. Ctrl+K is Hyperlink.",
        "Ctrl+Home and Ctrl+End go to the document start and end.",
        "F12 is Save As in Office. Shift+F3 cycles case.",
        "Ctrl+D: fill down in Excel, Font box in Word, bookmark in a browser.",
    ],
    patterns=[
        pat("ks-off-p1", "Universal Ctrl-key recall", "very common",
            "The question gives an action such as copy, paste or select all.",
            ["Match the action to its letter.", "Use the letter logic: X for cut, V for paste, A for all.", "Check that the key works in every app."],
            "Common Ctrl keys are shared by all Windows programs.",
            "Which shortcut selects all the content of a document?",
            ["The word all starts with A.", "Ctrl is the base key."], "Ctrl+A"),
        pat("ks-off-p2", "Formatting keys", "very common",
            "The question asks for bold, alignment, spacing or case.",
            ["B, I and U are their own letters.", "L, E, R, J are the four alignments.", "1, 2, 5 are the spacing numbers.", "Shift+F3 cycles case."],
            "Formatting keys follow simple letter and number patterns.",
            "Which shortcut centre-aligns a paragraph?",
            ["Ctrl+C is taken by Copy.", "Centre uses E."], "Ctrl+E"),
        pat("ks-off-p3", "Find, replace and navigation", "common",
            "The question asks for Find, Replace or a jump key.",
            ["Ctrl+F is Find.", "Ctrl+H is Replace in Word and Excel.", "Ctrl+Home goes to the start. Ctrl+End goes to the end."],
            "Navigation keys pair up as opposites, like Home and End.",
            "Which shortcut moves the cursor to the end of a Word document?",
            ["End means the last position.", "Ctrl with End jumps there."], "Ctrl+End"),
        pat("ks-off-p4", "Same key in different apps", "very common",
            "The question names an app and a key that has more than one job.",
            ["Find the app named in the question.", "Recall the job of the key in that app.", "Ignore other apps' meaning."],
            "The same key has several jobs, so the app is the deciding clue.",
            "In Microsoft Excel, Ctrl+D is used to:",
            ["The app is Excel.", "In Excel it copies the cell above downward."], "Fill down"),
        pat("ks-off-p5", "Undo, redo and Save As", "common",
            "The question asks the difference between Undo and Redo, or for Save As.",
            ["Undo is Ctrl+Z.", "Redo is Ctrl+Y.", "F12 is Save As in Office."],
            "Z and Y are neighbours in the alphabet, so students swap them.",
            "The key that reverses an Undo is:",
            ["Reversing an undo means redoing.", "Redo uses Y."], "Ctrl+Y"),
    ],
)

# =====================================================================
SUBS["ks-excel-ppt"] = dict(
    concept=(
        "This subtopic collects the shortcuts most asked for **Excel** and **PowerPoint**. "
        "In Excel, learn the moving, selecting and data-entry keys. "
        "In PowerPoint, learn how to start, run and end a show. Ctrl+D has three different jobs across Word, Excel and PowerPoint."
    ),
    notes=r"""### Excel: moving around
| Shortcut | Action |
|---|---|
| **Ctrl+Home** | Jump to cell **A1** |
| **Ctrl+End** | Jump to the last used cell |
| **Ctrl+Page Down / Up** | Next / previous **worksheet** |
| **Ctrl+Arrow key** | Edge of the current block of data |
| **F5 / Ctrl+G** | Go To a cell |
| **Ctrl+F** | Find |

### Excel: selecting and editing
| Shortcut | Action |
|---|---|
| **Ctrl+Space** | Select the whole **column** |
| **Shift+Space** | Select the whole **row** |
| **Ctrl+A** | Select the sheet or data block |
| **F2** | **Edit** the active cell |
| **Alt+Enter** | New line inside one cell |
| **Ctrl+D** | **Fill down** from the cell above |
| **Ctrl+R** | **Fill right** from the cell on the left |
| **Ctrl+;** | Enter today's **date** |
| **Ctrl+Shift+;** | Enter the current **time** |
| **F4** | Cycles reference styles. Also repeats the last action |
| **Ctrl+1** | Format Cells |
| **Ctrl+Shift+L** | Toggle filter |
| **Alt+=** | AutoSum |
| **Shift+F11** | New worksheet |

> **Tip:** Ctrl+Space is a tall thin column. Shift+Space is a flat row.

### PowerPoint: running the show
| Shortcut | Action |
|---|---|
| **F5** | Start the show from the **beginning** |
| **Shift+F5** | Start from the **current slide** |
| **Esc** | End the show |
| **B** | Black screen. Press again to return |
| **W** | White screen |
| **N, Space, Right arrow** | Next slide |
| **P, Left arrow** | Previous slide |
| **Number + Enter** | Jump to that slide |
| **Ctrl+M** | New slide |
| **Ctrl+D** | Duplicate the current slide |

> **Watch:** Ctrl+D duplicates a slide in PowerPoint. It fills down in Excel. It opens the Font box in Word.

### Formatting keys that carry over
Ctrl+B, Ctrl+I and Ctrl+U work in Excel cells and PowerPoint text boxes too. The alignment keys Ctrl+E, Ctrl+L and Ctrl+R also work in PowerPoint text.

### Everyday examples
| You want to... | Press |
|---|---|
| Copy a formula down a column | Ctrl+D |
| Jump to the last cell you filled | Ctrl+End |
| Type an address on two lines in one cell | Alt+Enter between lines |
| Put today's date on a report | Ctrl+; |
| Test one slide without the whole show | Shift+F5 |
| Keep the audience looking at you | B for black screen |

### Shared keys that also work here
- **Ctrl+C**, **Ctrl+X** and **Ctrl+V** copy, cut and paste in both Excel and PowerPoint.
- **Ctrl+Z** and **Ctrl+Y** undo and redo.
- **Ctrl+S** saves and **F12** opens Save As.
- **Ctrl+P** prints when you are editing.

### A ten-second method
1. Read the action in the question.
2. Recall the family: selection uses Space, filling uses D or R, the show uses F5.
3. Remove options that swap row and column, or F5 and Shift+F5.
""",
    tricks=[
        trick("Space pair",
              "Ctrl+Space selects a column. Shift+Space selects a row.",
              "Which shortcut selects an entire row in Excel?",
              ["A row is selected with the Shift key.", "The second key is Space."],
              "Shift+Space"),
        trick("Semicolon pair",
              "Ctrl+; enters the date. Adding Shift enters the time."),
        trick("Shift means here",
              "F5 starts from the first slide. Shift+F5 starts from the slide you are on."),
    ],
    mistakes=[
        mis("Using Ctrl+Space to select a row.", "Ctrl+Space selects a column. Shift+Space selects a row."),
        mis("Starting a show from the current slide with F5.", "F5 starts at the beginning. Shift+F5 starts at the current slide."),
        mis("Entering the time with Ctrl+;.", "Ctrl+; is the date. Ctrl+Shift+; is the time."),
        mis("Using Ctrl+D in PowerPoint to fill down.", "In PowerPoint it duplicates the slide. Fill down is an Excel action."),
        mis("Using Ctrl+N to add a slide.", "Ctrl+M adds a slide. Ctrl+N makes a new presentation."),
    ],
    revision=[
        "Excel corners: Ctrl+Home to A1, Ctrl+End to the last cell. Ctrl+PgDn and PgUp change sheets.",
        "Ctrl+Space selects a column. Shift+Space selects a row. F2 edits. Alt+Enter starts a new line in a cell.",
        "Ctrl+D fills down. Ctrl+R fills right. Ctrl+; date. Ctrl+Shift+; time.",
        "Show: F5 from start, Shift+F5 from here, Esc to end, B black, W white.",
        "Ctrl+M adds a slide. Ctrl+D duplicates a slide.",
        "Alt+= AutoSum. Shift+F11 new sheet. Ctrl+Shift+L filter.",
    ],
    patterns=[
        pat("ks-exc-p1", "Excel navigation shortcuts", "very common",
            "The question asks how to reach a corner, an edge or another sheet.",
            ["Ctrl+Home goes to A1.", "Ctrl+End goes to the last used cell.", "Ctrl+Page Down and Page Up move between sheets."],
            "The Home and End pair works like the top and bottom of the data.",
            "Which shortcut takes you to cell A1 in Excel?",
            ["A1 is the first cell.", "Home means the beginning."], "Ctrl+Home"),
        pat("ks-exc-p2", "Row and column selection shortcuts", "very common",
            "The question asks how to select a row or a column.",
            ["Column uses Ctrl+Space.", "Row uses Shift+Space.", "Ctrl+A selects everything."],
            "Both keys use Space, so options swap the modifiers.",
            "Ctrl+Space in Excel selects:",
            ["Ctrl+Space belongs to the column.", "It does not select the row."], "The entire column"),
        pat("ks-exc-p3", "Excel editing and data-entry shortcuts", "very common",
            "The question asks for date, time, edit, fill or new line in a cell.",
            ["F2 edits the cell.", "Ctrl+; is date and Ctrl+Shift+; is time.", "Ctrl+D fills down and Ctrl+R fills right.", "Alt+Enter starts a new line in the cell."],
            "Each key has one clear job.",
            "Which shortcut inserts a line break inside an Excel cell?",
            ["A line break inside one cell needs Alt.", "The second key is Enter."], "Alt+Enter"),
        pat("ks-ppt-p4", "PowerPoint slideshow shortcuts", "very common",
            "The question asks how to start, pause or end a show.",
            ["F5 starts from the beginning.", "Shift+F5 starts from the current slide.", "B and W give a black or white screen.", "Esc ends the show."],
            "The show keys are short letters that hint at their action.",
            "Which key ends a PowerPoint slide show?",
            ["The show must stop.", "The escape key does this."], "Esc"),
        pat("ks-exc-p5", "Ctrl+D across Word, Excel and PowerPoint", "common",
            "The question names an app and asks what Ctrl+D does.",
            ["In Excel it fills down.", "In PowerPoint it duplicates the slide.", "In Word it opens the Font box."],
            "One key has three jobs, so the app decides the answer.",
            "In PowerPoint, Ctrl+D:",
            ["The app is PowerPoint.", "There it makes a copy of the slide."], "Duplicates the selected slide"),
    ],
)

# =====================================================================
SUBS["ks-browser"] = dict(
    concept=(
        "Browser shortcuts handle tabs, windows, privacy and history. "
        "**Ctrl+T** opens a tab, **Ctrl+W** closes it and **Ctrl+Shift+T** brings it back. "
        "Ctrl+H, Ctrl+N and Ctrl+D do different jobs in a browser than in Word or Excel."
    ),
    notes=r"""### Tabs
| Shortcut | Action |
|---|---|
| **Ctrl+T** | New tab |
| **Ctrl+W** (or Ctrl+F4) | Close the current tab |
| **Ctrl+Shift+T** | **Reopen the last closed tab**. This is the undo of Ctrl+W |
| **Ctrl+Tab** | Next tab |
| **Ctrl+Shift+Tab** | Previous tab |
| **Ctrl+1 to Ctrl+8** | Jump to tab 1 to 8 |
| **Ctrl+9** | Jump to the **last** tab |

> **Watch:** Ctrl+9 goes to the last tab. It does not go to the ninth tab.

### Windows and privacy
| Shortcut | Action |
|---|---|
| **Ctrl+N** | New window |
| **Ctrl+Shift+N** | New **Incognito** (Chrome) or **InPrivate** (Edge) window |
| **Ctrl+Shift+P** | Private window in **Firefox** |
| **Ctrl+Shift+Delete** | Open Clear browsing data |

> **Note:** Incognito mode stops the browser from saving history and cookies on that computer. It does not hide your activity from websites or your internet provider.

### Getting around a page
| Shortcut | Action |
|---|---|
| **Alt+Left** | Back |
| **Alt+Right** | Forward |
| **Alt+Home** | Open the home page |
| **F5** | Reload |
| **Ctrl+F5** | Reload and skip the cache |
| **F11** | Full screen on or off |
| **Ctrl+F** | Find on the page |
| **Ctrl+D** | **Bookmark** this page |
| **Ctrl+Shift+B** | Show or hide the bookmarks bar |
| **Ctrl+H** | **History** |
| **Ctrl+J** | **Downloads** |

### Keys with double lives
The same key can do different jobs in a browser and in Office.

| Key | Browser | Word / Excel |
|---|---|---|
| Ctrl+H | **History** | Replace (Word) |
| Ctrl+N | New **window** | New **document** or **workbook** |
| Ctrl+Shift+N | Incognito window | New **folder** (Explorer) |
| Ctrl+D | **Bookmark** | Font box (Word) or fill down (Excel) |
| Ctrl+F | Find on page | Find |

> **Rule:** If the question says "in a web browser", use the browser column.

### Why the browser keys matter
A browser holds many pages at once, and shortcuts save clicks. The tab keys use letters T and W. The private window key adds Shift to N. Learn these first because the exam asks them most.

### Address bar and page keys
- **Ctrl+L** or **F6** puts the cursor in the address bar.
- **Ctrl+P** prints the page.
- **Ctrl+S** saves the page.
- **Ctrl++** zooms in. **Ctrl+-** zooms out. **Ctrl+0** returns to normal zoom.
- **Esc** stops a page that is still loading.

### Everyday examples
| You just... | Do this |
|---|---|
| Closed a tab you still needed | Ctrl+Shift+T |
| Want a private session | Ctrl+Shift+N |
| Lost the bookmarks bar | Ctrl+Shift+B |
| Need a page you visited last week | Ctrl+H |
| Want the file you downloaded | Ctrl+J |
| Have a page stuck on an old version | Ctrl+F5 |
""",
    tricks=[
        trick("Tab trio",
              "T opens a tab, W closes it and Shift+T reopens the one you closed.",
              "Which shortcut reopens the most recently closed tab?",
              ["Ctrl+W closes a tab.", "The undo of that adds Shift and T."],
              "Ctrl+Shift+T"),
        trick("H, J, D",
              "H is History, J is downloads (the next letter) and D is a bookmark (Dog-ear a page)."),
    ],
    mistakes=[
        mis("Reading Ctrl+9 as the ninth tab.", "Ctrl+9 jumps to the last tab."),
        mis("Using Ctrl+H for Replace in a browser.", "In a browser Ctrl+H is History."),
        mis("Thinking Incognito hides you from websites.", "It only stops local saving of history and cookies."),
        mis("Using Ctrl+N for a private window.", "Ctrl+N is a normal new window. Ctrl+Shift+N is private."),
        mis("Confusing F5 with Ctrl+F5.", "F5 reloads. Ctrl+F5 reloads without the cache."),
    ],
    revision=[
        "Tab keys: Ctrl+T new, Ctrl+W close, Ctrl+Shift+T reopen. Ctrl+9 goes to the last tab.",
        "Private: Ctrl+Shift+N in Chrome and Edge. Ctrl+Shift+P in Firefox. Clear data: Ctrl+Shift+Delete.",
        "Alt+Left back. Alt+Right forward. Alt+Home home page. F11 full screen.",
        "Ctrl+D bookmark. Ctrl+H history. Ctrl+J downloads.",
        "F5 reload. Ctrl+F5 reload ignoring the cache.",
        "Incognito stops local history saving only.",
    ],
    patterns=[
        pat("ks-bro-p1", "Browser tab management", "very common",
            "The question asks for a tab job: open, close, reopen or switch.",
            ["Ctrl+T opens.", "Ctrl+W closes.", "Ctrl+Shift+T reopens.", "Ctrl+Tab switches."],
            "The tab keys are built around the letters T and W.",
            "Which shortcut opens a new tab in a browser?",
            ["Tab starts with T.", "Ctrl is the base."], "Ctrl+T"),
        pat("ks-bro-p2", "Private and incognito windows", "very common",
            "The question asks for a private window or what it stores.",
            ["Chrome and Edge use Ctrl+Shift+N.", "Firefox uses Ctrl+Shift+P.", "History and cookies are not saved locally."],
            "The key depends on the browser, and the privacy claim is limited.",
            "Which shortcut opens an Incognito window in Google Chrome?",
            ["Chrome is named.", "Its private key is Ctrl+Shift+N."], "Ctrl+Shift+N"),
        pat("ks-bro-p3", "Navigation and bookmarks", "common",
            "The question asks for back, forward, reload, full screen or bookmark.",
            ["Alt+Left is back and Alt+Right is forward.", "F5 reloads.", "F11 is full screen.", "Ctrl+D bookmarks."],
            "Alt with arrows moves through history.",
            "Which shortcut adds the current page to bookmarks?",
            ["Bookmark uses D.", "Ctrl is the base."], "Ctrl+D"),
        pat("ks-bro-p4", "History, downloads and clearing data", "common",
            "The question asks for the history page, downloads page or the clear-data dialog.",
            ["Ctrl+H opens History.", "Ctrl+J opens Downloads.", "Ctrl+Shift+Delete opens Clear browsing data."],
            "Three neighbouring keys open the three pages.",
            "Which shortcut opens the Downloads page in a browser?",
            ["History is H.", "Downloads uses the next letter, J."], "Ctrl+J"),
        pat("ks-bro-p5", "Browser vs Office double lives", "very common",
            "The question names a browser and a key that also works in Office.",
            ["Note that the app is a browser.", "Ctrl+H is History, Ctrl+D is Bookmark, Ctrl+N is a new window.", "Do not use the Word or Excel meaning."],
            "The stem's app decides the meaning.",
            "In a browser, Ctrl+H opens:",
            ["The app is a browser.", "In Word it would be Replace."], "History"),
    ],
)

# =====================================================================
SUBS["ks-function-keys"] = dict(
    concept=(
        "The **F1 to F12** keys have fixed jobs, but some change with the program. "
        "F1 is Help, F2 renames, F5 refreshes or starts a slide show, F7 checks spelling and F12 is Save As. "
        "Read the program named in the question."
    ),
    notes=r"""### The F1 to F12 row
| Key | Windows | Office | Other |
|---|---|---|---|
| **F1** | **Help** | Help | none |
| **F2** | Rename a file | Edit a cell in Excel | none |
| **F3** | Search in Explorer | Shift+F3 changes case in Word | none |
| **F4** | Address bar list | Repeats the last action. Cycles references in Excel | Alt+F4 closes a program |
| **F5** | **Refresh** | Slide show (PowerPoint), Go To (Word) | Ctrl+F5 hard reload |
| **F6** | Moves between screen parts | none | none |
| **F7** | none | **Spelling and grammar** | Caret browsing in browsers |
| **F8** | Safe Mode at start-up (older Windows) | Extend selection | none |
| **F9** | none | Update fields (Word), recalculate (Excel) | Send/Receive (Outlook) |
| **F10** | Activate the menu bar | none | **Shift+F10 is right-click** |
| **F11** | Full screen in browsers | Chart sheet (Excel) | none |
| **F12** | Developer tools in browsers | **Save As** | none |

### Memory hooks
- One is help on demand. Two is the second name, a rename. Five is fresh, a refresh. Seven is for spelling.
- Twelve saves your work under a new name, Save As.
- **Shift+F10** gives the right-click menu. F10 opens the menu bar, and Shift makes it act at your cursor.
- **Alt+F4** closes the program. **Ctrl+F4** closes only the document or tab.

> **Tip:** Say the ladder aloud: help, rename, search, refresh. Stop when you reach the match.

### Same key, different program
| Key | Windows | Word | Excel | PowerPoint | Browser |
|---|---|---|---|---|---|
| F5 | Refresh | Go To | Go To | **Slide show** | Reload |
| F2 | Rename | none | Edit cell | none | none |
| F7 | none | Spelling | Spelling | Spelling | Caret browsing |
| F12 | none | Save As | Save As | Save As | Developer tools |
| F11 | none | none | Chart sheet | none | Full screen |

> **Watch:** F5 in PowerPoint runs the show. F5 on the desktop refreshes.

### Modifier plus F key
- **Shift+F3** cycles the case in Word.
- **Shift+F5** starts the show from the current slide.
- **Shift+F7** opens the thesaurus in Word.
- **Shift+F11** adds a worksheet in Excel.
- **Ctrl+F4** closes a document. **Alt+F4** closes a program.
- **Ctrl+F5** reloads a browser page and skips the cache.

### A quick ladder to say aloud
F1 help. F2 rename. F3 search. F4 repeat. F5 refresh. F6 next pane. F7 spelling. F8 select or Safe Mode. F9 update. F10 menu. F11 full screen. F12 Save As.

> **Note:** The same ladder works for most exam questions. Then check which program the question names.

### Everyday examples
| You want to... | Press |
|---|---|
| Learn what a button does | F1 |
| Rename a file | F2 |
| Reload a misbehaving page | F5 |
| Fix red underlines | F7 |
| Save with a different name | F12 |
| Open the menu without the mouse | F10 |
""",
    tricks=[
        trick("Alt closes programs",
              "Alt+F4 closes the whole program. Ctrl+F4 closes only the current document or tab.",
              "Which key closes only the current document, leaving the program open?",
              ["Alt+F4 closes the program.", "The document-only key uses Ctrl."],
              "Ctrl+F4"),
        trick("Twelve is Save As",
              "F12 opens Save As in Office. In a browser the same key opens developer tools."),
    ],
    mistakes=[
        mis("Using F2 to open Help.", "F1 opens Help. F2 renames or edits."),
        mis("Thinking F5 always refreshes.", "In PowerPoint F5 starts the slide show."),
        mis("Reading Alt+F4 as Close Document.", "Alt+F4 closes the whole program. Ctrl+F4 closes the document."),
        mis("Using F10 for the right-click menu.", "Shift+F10 gives the right-click menu."),
        mis("Assuming F7 always means spelling.", "In browsers F7 turns on caret browsing."),
    ],
    revision=[
        "F1 Help. F2 rename or edit cell. F3 search. F5 refresh or slide show. F7 spelling. F12 Save As or developer tools.",
        "Alt+F4 closes a program. Ctrl+F4 closes a document. Shift+F10 is right-click. F10 opens the menu bar.",
        "F4 repeats the last action in Office and cycles references in Excel.",
        "F8 is Safe Mode at boot in older Windows.",
        "Shift+F3 case in Word. Shift+F11 new worksheet in Excel. Ctrl+F5 reloads without cache.",
        "F11 is full screen in a browser and a chart sheet in Excel.",
    ],
    patterns=[
        pat("ks-fun-p1", "Core F-key identification", "very common",
            "The question describes a job and asks for its F key.",
            ["Say the ladder: help, rename, search, refresh.", "Stop at the job described.", "Check that the app matches."],
            "Each F key has a well-known main job.",
            "Which function key opens Help in most programs?",
            ["Help is the first job.", "The first key is F1."], "F1"),
        pat("ks-fun-p2", "F-keys inside Office apps", "very common",
            "The question names an Office app and asks for a job.",
            ["F7 is spelling and grammar.", "F12 is Save As.", "F2 edits a cell in Excel.", "F5 starts the show in PowerPoint."],
            "Office gives F keys special jobs.",
            "Which function key opens Save As in MS Office?",
            ["Save As makes a copy under a new name.", "The key is F12."], "F12"),
        pat("ks-fun-p3", "Modifier plus F-key combinations", "common",
            "The question adds Shift, Ctrl or Alt to an F key.",
            ["Alt+F4 closes a program.", "Ctrl+F4 closes a document.", "Shift+F10 is right-click.", "Shift+F3 changes case."],
            "A modifier changes the F key's job.",
            "Which combination gives the right-click menu from the keyboard?",
            ["The F10 key opens menus.", "Shift makes it act at the cursor."], "Shift+F10"),
        pat("ks-fun-p4", "One key, many apps", "very common",
            "The question names an app and a single F key with many jobs.",
            ["Note the app.", "F5 is refresh in Windows, show in PowerPoint and Go To in Word.", "F12 is Save As in Office and developer tools in browsers."],
            "The app decides the answer.",
            "In MS PowerPoint, the F5 key:",
            ["The app is PowerPoint.", "There F5 begins the show."], "Starts the slide show"),
        pat("ks-fun-p5", "Reload and refresh keys", "occasional",
            "The question asks the difference between reload keys.",
            ["F5 reloads.", "Ctrl+F5 reloads and skips the cache.", "F11 is full screen."],
            "The cache-free reload is a small favourite.",
            "Which key combination reloads a page and ignores the cache?",
            ["A plain reload is F5.", "Ignoring the cache adds Ctrl."], "Ctrl+F5"),
    ],
)

apply("keyboard-shortcuts.json", SUBS)
