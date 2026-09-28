"""keyboard-shortcuts deep content — part 1: Windows, universal Ctrl/Word keys."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_windows():
    S = Sub("ks-windows")
    S.notes = """### The Windows key family
The **Win key** (the flag between Ctrl and Alt) controls the desktop itself. Most shortcuts use the **first letter of the action** — E for Explorer, L for Lock, R for Run:

| Shortcut | Action |
|---|---|
| Win | Open or close the Start menu |
| **Win+D** | Show the desktop; press again to restore windows |
| **Win+E** | Open File Explorer |
| **Win+L** | **Lock** the computer |
| **Win+R** | Open the **Run** dialog (type cmd, calc, notepad) |
| **Win+I** | Open Settings |
| **Win+S** | Search |
| Win+M / Win+Shift+M | Minimise all windows / restore them |
| Win+Tab | Task view (all virtual desktops and windows) |
| Win+Left/Right/Up/Down | Snap the window to half or quarter of the screen |
| Win+PrtScn | Screenshot saved to Pictures |
| Win+Shift+S | Snip a selected part of the screen |
| Win+V | Clipboard history (several copied items) |

Traps: **Win+M only minimises** (no toggle); Win+D toggles. Win+E is files; a browser is not Explorer.

### The security trio
| Combo | What appears |
|---|---|
| **Ctrl+Shift+Esc** | **Task Manager directly** — fastest route |
| **Ctrl+Alt+Del** | The full-screen security menu (Lock, Switch user, Task Manager…) |
| Alt+F4 | Close the active program (on the desktop it opens the shutdown dialog) |

### File Explorer moves
| Shortcut | Action |
|---|---|
| **Ctrl+Shift+N** | New folder |
| **F2** | Rename the selected item |
| **Alt+Enter** | Properties of the selected item |
| **Alt+Up arrow** | Go up one folder level |
| **Delete** | To Recycle Bin; **Shift+Delete** = permanent |
| Ctrl+A | Select everything |

### Switching and closing
- **Alt+Tab** — switch between open windows (hold Alt, tap Tab).
- **Win+D** or Win+M — clear the screen to the desktop.
- **Win+arrows** — park a window on half the screen (snapping), great for comparing two documents.

### How exam questions sound
| The stem says | Answer |
|---|---|
| "opens File Explorer" | Win+E |
| "locks the computer" | Win+L |
| "opens the Run dialog" | Win+R |
| "Task Manager directly" | Ctrl+Shift+Esc |
| "switches between open programs" | Alt+Tab |
| "closes the active program" | Alt+F4 |
| "creates a new folder" | Ctrl+Shift+N |
| "renames the selected file" | F2 |

Ten-second method: read the **verb** (switch / close / open / lock), pick the **family** (Win-key, Alt, Ctrl+Shift), then apply the first-letter rule and eliminate the planted nonsense option.

### Quick revision
- First-letter rule: E = Explorer, L = Lock, R = Run, I = settings (I for 'yes, change it').
- Win+D toggles the desktop; Win+M only minimises (Win+Shift+M restores).
- Task Manager direct = Ctrl+Shift+Esc; the security screen = Ctrl+Alt+Del.
- Explorer: Ctrl+Shift+N new folder, F2 rename, Alt+Enter properties, Alt+Up up one level.
- Alt+Tab switches windows; Alt+F4 closes the program."""
    S.pattern("ks-win-p1", "Win-key shortcut recall", "very common",
        "'Which shortcut opens File Explorer / locks the PC / opens the Run dialog?' — a Win-key action with four combos as options.",
        None,
        "1. First-letter rule: Win+E Explorer, Win+L Lock, Win+R Run, Win+I settings.\n2. Distinguish near pairs: Win+D toggles the desktop, Win+M only minimises; Win+V clipboard history, Win+Shift+S snip.\n3. Eliminate combos whose letter contradicts the action (Win+P for Lock is planted nonsense — P is projection).",
        "Which shortcut **locks** the computer so a password is needed to return?",
        "**Win+L** — L for Lock. Win+D shows the desktop; Alt+F4 closes programs.")
    S.pattern("ks-win-p2", "Task Manager and security combos", "very common",
        "'Direct shortcut for Task Manager', 'what does Ctrl+Alt+Del show?', 'which combo ends a not-responding program fastest?'",
        None,
        "1. Direct Task Manager = **Ctrl+Shift+Esc**.\n2. Ctrl+Alt+Del opens the **security screen** first (Lock, Switch user, Sign out, Task Manager).\n3. Alt+F4 closes the active program; it does not open Task Manager.",
        "Which combination opens **Task Manager directly**, without any intermediate screen?",
        "**Ctrl+Shift+Esc** — Ctrl+Alt+Del first shows the security menu, from which Task Manager is one more click away.")
    S.pattern("ks-win-p3", "File Explorer shortcuts", "common",
        "'Shortcut to create a new folder', 'which key renames a file?', 'properties of a file with keyboard', 'move up one folder'.",
        None,
        "1. New folder = **Ctrl+Shift+N** (in Explorer; in a browser the same combo makes an Incognito window — classic cross-app trap).\n2. F2 = rename, Alt+Enter = properties, Alt+Up = parent folder, Shift+Delete = permanent delete.\n3. Ordinary Delete goes to the Recycle Bin; the Shift version skips it.",
        "In File Explorer, the keyboard shortcut to create a **new folder** is —",
        "**Ctrl+Shift+N**. (The same combo in Chrome opens an Incognito window — read which app the stem names.)")
    S.pattern("ks-win-p4", "Window switching and closing", "very common",
        "'Which combination switches between open windows?', 'closing the active program', 'snapping a window to half the screen'.",
        None,
        "1. Switch = **Alt+Tab**; close the active program = **Alt+F4**; close a document/tab inside a program = Ctrl+W or Ctrl+F4.\n2. Snap = Win+arrow keys (left/right halves, up maximise, down restore/minimise).\n3. Shift+Alt+Tab walks the switcher backwards — a rare but asked variant.",
        "Which key combination **closes the active program window**?",
        "**Alt+F4** — it closes the program in front. Alt+Tab only switches between programs; Ctrl+W closes the current document or tab inside them.")

    S.q("ks-win-p1", "easy", "Which shortcut opens **File Explorer**?",
        ["Win+E", "Win+F", "Win+X", "Win+P"], "Win+E",
        "**Win+E** opens File Explorer (E for Explorer). Win+X opens the power-user menu; Win+P handles projection.",
        "E = Explorer.", 20)
    S.q("ks-win-p1", "easy", "The **Run** dialog, where you can type 'cmd' or 'calc', opens with —",
        ["Win+R", "Win+U", "Ctrl+R", "Alt+R"], "Win+R",
        "**Win+R** = Run — type a program name and press Enter.",
        "R = Run.", 20)
    S.q("ks-win-p1", "medium", "Pressing **Win+D** and then pressing it again will —",
        ["Shut down the PC", "Show the desktop, then restore the open windows", "Open Documents", "Delete temporary files"], "Show the desktop, then restore the open windows",
        "**Win+D toggles**: first press hides all windows to show the desktop, second press brings them back. Win+M, by contrast, only minimises.",
        "D = Desktop toggle.", 25)
    S.q("ks-win-p1", "easy", "Which shortcut captures a **selected part of the screen** with the Snipping overlay?",
        ["Win+Shift+S", "Win+P", "Ctrl+S", "Alt+S"], "Win+Shift+S",
        "**Win+Shift+S** opens the snip bar — drag to capture a rectangle, window or full screen.",
        "S = Snip.", 20)
    S.q("ks-win-p1", "medium", "Windows **clipboard history**, which remembers several recent copied items, opens with —",
        ["Win+V", "Ctrl+V", "Win+C", "Alt+V"], "Win+V",
        "**Win+V** shows the clipboard history (paste any of your recent copies). Plain Ctrl+V pastes only the latest item.",
        "V = the clipboard's view.", 25)
    S.q("ks-win-p2", "easy", "Which key combination opens **Task Manager directly**?",
        ["Ctrl+Alt+Del", "Ctrl+Shift+Esc", "Alt+F4", "Ctrl+Esc"], "Ctrl+Shift+Esc",
        "**Ctrl+Shift+Esc** jumps straight to Task Manager. Ctrl+Alt+Del first shows the security screen.",
        "Esc = escape straight into Task Manager.", 20)
    S.q("ks-win-p2", "medium", "Pressing **Ctrl+Alt+Del** shows —",
        ["Task Manager immediately", "The Windows security screen (Lock, Switch user, Sign out, Task Manager)", "The Run dialog", "The shutdown timer"], "The Windows security screen (Lock, Switch user, Sign out, Task Manager)",
        "Ctrl+Alt+Del opens the **security screen**; Task Manager is one option on it. For the direct route, use Ctrl+Shift+Esc.",
        "Three keys, one menu, then your pick.", 25)
    S.q("ks-win-p3", "easy", "In File Explorer, which shortcut creates a **new folder**?",
        ["Ctrl+N", "Ctrl+Shift+N", "Alt+N", "Ctrl+Alt+N"], "Ctrl+Shift+N",
        "**Ctrl+Shift+N** makes a new folder in the current location. Plain Ctrl+N opens a new window.",
        "Shift raises the stakes: window → folder.", 20)
    S.q("ks-win-p3", "easy", "Which key **renames** a selected file in File Explorer?",
        ["F2", "F5", "F4", "F8"], "F2",
        "**F2** renames the selected item — give it a second name.",
        "F2 = 2nd name.", 20)
    S.q("ks-win-p3", "medium", "With a file selected, **Alt+Enter** shows —",
        ["The file's Properties", "The file in a new window", "The open-with list", "The print dialog"], "The file's Properties",
        "**Alt+Enter** opens Properties (size, dates, attributes) — the keyboard way of right-clicking and choosing Properties.",
        "Alt+Enter = 'tell me about it'.", 25)
    S.q("ks-win-p3", "medium", "You are deep inside C:\\Users\\Me\\Photos\\2026. Which shortcut moves **up one folder** (to Photos)?",
        ["Alt+Up arrow", "Alt+Left arrow", "Ctrl+Up arrow", "Shift+Up"], "Alt+Up arrow",
        "**Alt+Up** climbs to the parent folder. Alt+Left goes *back* to wherever you came from — not the same thing.",
        "Up = one level up; Left = back in history.", 25)
    S.q("ks-win-p4", "easy", "Which combination **switches between open application windows**?",
        ["Alt+Tab", "Ctrl+Tab", "Shift+Esc", "Win+A"], "Alt+Tab",
        "**Alt+Tab** cycles through open programs (Ctrl+Tab switches tabs inside one app instead).",
        "Alt = across apps; Ctrl = across tabs.", 20)
    S.q("ks-win-p4", "easy", "Which shortcut **closes the active program**?",
        ["Alt+F4", "Ctrl+F", "Win+F4", "Shift+Del"], "Alt+F4",
        "**Alt+F4** closes the window in front. On the desktop, it opens the shutdown dialog.",
        "F4 with Alt = full exit.", 20)
    S.q("ks-win-p4", "medium", "**Win + Left arrow** does what to the current window?",
        ["Closes it", "Snaps it to the left half of the screen", "Moves it to another monitor only", "Minimises it to the taskbar"], "Snaps it to the left half of the screen",
        "**Snap**: Win+Left/Right parks the window on that half; Win+Up maximises; Win+Down restores or minimises.",
        "Arrows park windows like cars.", 25)
    S.q("ks-win-p4", "medium", "While holding **Alt**, pressing **Shift+Tab** in the switcher —",
        ["Restarts the PC", "Moves through the windows in the reverse direction", "Opens Task Manager", "Cancels Alt+Tab"], "Moves through the windows in the reverse direction",
        "Shift reverses direction in almost every Windows cycle — in Alt+Tab it walks the window list backwards.",
        "Shift = step back.", 30)
    return S


def build_office():
    S = Sub("ks-common-office")
    S.notes = """### The universal Ctrl keys (every Windows app)
| Key | Action | Key | Action |
|---|---|---|---|
| **Ctrl+N** | New file | **Ctrl+O** | Open |
| **Ctrl+S** | Save | **Ctrl+P** | Print |
| **Ctrl+Z** | **Undo** | **Ctrl+Y** | Redo |
| **Ctrl+X** | Cut | **Ctrl+C** | Copy |
| **Ctrl+V** | Paste | **Ctrl+A** | Select all |
| **Ctrl+F** | Find | **Ctrl+W** | Close document/tab |
| **Ctrl+K** | Insert hyperlink | **Ctrl+B/I/U** | Bold / italic / underline |

Letter logic: X looks like scissors (cut), V is a paste-down arrow, Z takes you back (undo), A = all.

### Formatting keys (Word especially)
| Shortcut | Action |
|---|---|
| Ctrl+B / I / U | Bold / italic / underline |
| **Ctrl+L / E / R / J** | Align **L**eft / c**E**ntre / **R**ight / **J**ustify |
| **Ctrl+1 / Ctrl+2 / Ctrl+5** | Single / double / 1.5 line spacing |
| Ctrl+Shift+D | Double underline |
| Shift+F3 | Cycle CASE (lower → UPPER → Capitalise) |

Memory hooks: **C is taken by Copy, so centre borrows E** ('cEntre'). Spacing uses the number itself — 1 single, 2 double — and 5 is the odd one for 1.5.

### Find, replace, go to
- **Ctrl+F** — Find (in Word it opens the Navigation pane; in browsers 'find in page').
- **Ctrl+H** — **Replace** in Word/Excel (but History in a browser — a favourite cross-app trap).
- **Ctrl+G** and **F5** — Go To a page/line in Word.
- **Ctrl+Home / Ctrl+End** — jump to the start / end of the document.

### Undo and friends
- **Ctrl+Z** undoes the last action (press again to undo more); **Ctrl+Y** redoes it.
- Ctrl+S saves — press often; **F12** is Save As (Office).

### The double-life table (same key, different app)
| Key | Word / Excel | Browser | Explorer |
|---|---|---|---|
| Ctrl+H | **Replace** | History | — |
| Ctrl+D | Font dialog / fill down | **Bookmark** | — |
| Ctrl+Shift+N | — | Incognito window | **New folder** |
| Ctrl+F | Find (Navigation pane) | Find on page | Search box |
| Ctrl+W | Close document | Close tab | Close window |

How the exam uses it: the stem names the app in italics or bold — "in **MS Word**", "in a **web browser**". Read that phrase before anything else; it flips half the answers in this topic.

Worked example: "In MS Excel, pressing Ctrl+D will —" → fill down (copy the cell above). The same keys in Word open the Font dialog, and in Chrome they bookmark the page. One key, three lives, and only the stem's app decides.

### Quick revision
- N-O-S-P: New, Open, Save, Print. X-C-V: cut-copy-paste. Z-Y: undo-redo.
- Alignment LERJ: Left, cEntre, Right, Justify. Spacing: 1-2-5 = single-double-1.5.
- Ctrl+F find, Ctrl+H replace (Word) but history (browser). Ctrl+K hyperlink.
- Ctrl+Home/Ctrl+End = document start/end. F12 = Save As in Office."""
    S.pattern("ks-off-p1", "Universal Ctrl-key recall", "very common",
        "'Which shortcut pastes / cuts / undoes / selects all?' — the everyday edit keys.",
        None,
        "1. Edit trio: Ctrl+X cut, Ctrl+C copy, Ctrl+V paste; Ctrl+Z undo, Ctrl+Y redo; Ctrl+A select all.\n2. File quartet: Ctrl+N new, Ctrl+O open, Ctrl+S save, Ctrl+P print.\n3. Memory hooks: X = scissors, V = paste-down, Z = back. Eliminate combos using Win or Alt where the stem says Ctrl.",
        "Which shortcut **undoes** the last action in almost every Windows program?",
        "**Ctrl+Z** — Z walks you back; Ctrl+Y redoes what you undid.")
    S.pattern("ks-off-p2", "Formatting keys (bold, align, spacing, case)", "very common",
        "'Which shortcut justifies text?', 'double line spacing', 'which key makes text bold?', 'Shift+F3 does what?'.",
        None,
        "1. Bold/italic/underline = Ctrl+B/I/U. Alignments = Ctrl+L/E/R/J (LERJ: Left, cEntre, Right, Justify).\n2. Line spacing = the number itself: Ctrl+1 single, Ctrl+2 double, Ctrl+5 = 1.5.\n3. Shift+F3 cycles the case of selected text in Word.",
        "Which shortcut sets **double line spacing** on the selected paragraphs in Word?",
        "**Ctrl+2** — the number is the spacing itself: Ctrl+1 single, Ctrl+2 double, Ctrl+5 = 1.5 lines.")
    S.pattern("ks-off-p3", "Find / Replace / Go To / navigation", "common",
        "'Shortcut for Find and Replace', 'jump to the beginning of the document', 'which opens the Go To dialog?'.",
        None,
        "1. Ctrl+F find, Ctrl+H replace (Word/Excel), Ctrl+G or F5 = Go To (Word).\n2. Ctrl+Home jumps to the document start, Ctrl+End to the end.\n3. Cross-app trap: Ctrl+H is Replace in Office but History in browsers.",
        "Which shortcut opens **Find and Replace** directly on the Replace tab in MS Word?",
        "**Ctrl+H** — H for 'hunt and swap'. Ctrl+F only finds; F5 or Ctrl+G goes to a page or line.")
    S.pattern("ks-off-p4", "Trap pairs and reverse recall in Office", "common",
        "'Ctrl+D in Word does what?' (Font dialog, not duplicate), 'Ctrl+E in Excel vs Word', statements that swap Replace/History or centre/copy.",
        None,
        "1. Ctrl+D: **Font dialog in Word**, fill-down in Excel, bookmark in browsers — same key, three lives.\n2. Ctrl+E: centre in Word, but 'export' nowhere — in Excel it centres too; beware options inventing actions.\n3. Reverse recall: read the action in the stem, then recall the key, then check which app the stem names.",
        "In **MS Word**, pressing Ctrl+D opens the —",
        "**Font dialog box** — not 'duplicate' (that is PowerPoint's Ctrl+D) and not fill-down (that is Excel's).")
    S.q("ks-off-p1", "easy", "Which shortcut **pastes** copied content?",
        ["Ctrl+V", "Ctrl+P", "Ctrl+X", "Ctrl+B"], "Ctrl+V",
        "**Ctrl+V** pastes; Ctrl+X cuts, Ctrl+C copies, Ctrl+P prints.",
        "V is the paste-down arrow.", 20)
    S.q("ks-off-p1", "easy", "**Ctrl+Y** in MS Word —",
        ["Undoes the last action", "Redoes the last undone action", "Yanks the file offline", "Opens styles"], "Redoes the last undone action",
        "**Ctrl+Y = redo** (it can also repeat the last action). Undo is Ctrl+Z.",
        "Z back, Y forward.", 20)
    S.q("ks-off-p1", "easy", "To **select the entire document** in one stroke, press —",
        ["Ctrl+A", "Ctrl+E", "Ctrl+D", "Shift+A"], "Ctrl+A",
        "**Ctrl+A** = select **A**ll — the whole document or every cells/rows in the active region.",
        "A = All.", 20)
    S.q("ks-off-p1", "medium", "Which shortcut **inserts a hyperlink** in Word or Excel?",
        ["Ctrl+K", "Ctrl+H", "Ctrl+L", "Ctrl+Y"], "Ctrl+K",
        "**Ctrl+K** opens the hyperlink dialog (K sits next to L for 'link' on the keyboard).",
        "K = linK.", 25)
    S.q("ks-off-p2", "easy", "Which shortcut makes selected text **bold**?",
        ["Ctrl+B", "Ctrl+D", "Ctrl+B+U", "Shift+B"], "Ctrl+B",
        "**Ctrl+B** = bold, Ctrl+I = italic, Ctrl+U = underline — the initial letters.",
        "B-I-U in order.", 20)
    S.q("ks-off-p2", "easy", "Which shortcut **centres** the selected paragraph in Word?",
        ["Ctrl+E", "Ctrl+C", "Ctrl+M", "Alt+C"], "Ctrl+E",
        "**Ctrl+E = cEntre.** Ctrl+C is copy; C was taken, so centre borrowed E.",
        "cEntre with a capital E.", 20)
    S.q("ks-off-p2", "medium", "The correct set of Word alignment shortcuts is —",
        ["Ctrl+L, Ctrl+E, Ctrl+R, Ctrl+J", "Ctrl+A, Ctrl+B, Ctrl+C, Ctrl+D", "Ctrl+1, Ctrl+2, Ctrl+3, Ctrl+4", "Alt+L, Alt+E, Alt+R, Alt+J"], "Ctrl+L, Ctrl+E, Ctrl+R, Ctrl+J",
        "**LERJ**: Left, cEntre, Right, Justify.",
        "LERJ — left to right across the line.", 25)
    S.q("ks-off-p2", "medium", "**Shift+F3** in MS Word —",
        ["Changes the case of selected text (lower/UPPER/Capitalise)", "Inserts a function", "Refreshes the page", "Saves the file"], "Changes the case of selected text (lower/UPPER/Capitalise)",
        "**Shift+F3** cycles the case of the selection in Word — press repeatedly to march lower → UPPER → Capitalise Each Word. (In Excel, plain Shift+F3 opens Insert Function instead.)",
        "F3 = three case forms.", 25)
    S.q("ks-off-p3", "easy", "Which shortcut jumps to the **beginning of the document**?",
        ["Ctrl+Home", "Ctrl+End", "Page Up", "Alt+Home"], "Ctrl+Home",
        "**Ctrl+Home** = document start; **Ctrl+End** = document end.",
        "Home is where you start.", 20)
    S.q("ks-off-p3", "medium", "In Word, **Ctrl+G** opens the same dialog as —",
        ["F5 (Go To)", "F12 (Save As)", "F7 (Spelling)", "F1 (Help)"], "F5 (Go To)",
        "**Ctrl+G and F5 both open Go To**, for jumping to a page, section or line number.",
        "G = Go = F5.", 25)
    S.q("ks-off-p3", "medium", "Which shortcut closes the **current document** without closing the Word application?",
        ["Ctrl+W", "Alt+F4", "Ctrl+Q", "Shift+W"], "Ctrl+W",
        "**Ctrl+W** (or Ctrl+F4) closes the document window; **Alt+F4** quits the whole program.",
        "W = window, not whole app.", 25)
    S.q("ks-off-p4", "medium", "In **MS Word**, Ctrl+D opens the —",
        ["Font dialog box", "Duplicate copy of the document", "Fill-down dialog", "Document properties"], "Font dialog box",
        "Ctrl+D opens the **Font** dialog in Word. 'Duplicate' belongs to PowerPoint (Ctrl+D duplicates a slide/object); fill-down is Excel's Ctrl+D.",
        "Same key, three apps, three jobs.", 25)
    S.q("ks-off-p4", "medium", "The **Office key that saves with a new name/ location** (Save As) is —",
        ["F12", "F5", "Ctrl+S", "F2"], "F12",
        "**F12 = Save As** in Word, Excel and PowerPoint. Plain save stays Ctrl+S.",
        "12 = one bigger save.", 25)
    S.q("ks-off-p1", "hard", "Which statement is **correct**?",
        ["Ctrl+Z undoes and Ctrl+Y redoes", "Ctrl+Z saves and Ctrl+Y prints", "Ctrl+X copies and Ctrl+C cuts", "Ctrl+P pastes and Ctrl+V prints"], "Ctrl+Z undoes and Ctrl+Y redoes",
        "The undo pair is **Ctrl+Z (undo) / Ctrl+Y (redo)**. The cut-copy pair is Ctrl+X / Ctrl+C; printing is Ctrl+P.",
        "Z back, Y forward; X cuts, C copies.", 30)
    S.q("ks-off-p2", "hard", "Match the Word shortcut to its effect:\nA. Ctrl+J  B. Ctrl+2  C. Shift+F3  D. Ctrl+U",
        ["A-justify, B-double spacing, C-change case, D-underline",
         "A-underline, B-change case, C-double spacing, D-justify",
         "A-justify, B-change case, C-double spacing, D-underline",
         "A-double spacing, B-justify, C-underline, D-change case"],
        "A-justify, B-double spacing, C-change case, D-underline",
        "Ctrl+**J** = **J**ustify; Ctrl+**2** = double spacing; Shift+**F3** = case cycling; Ctrl+**U** = **U**nderline.",
        "J-2-F3-U: justify, double, case, underline.", 35)
    return S
