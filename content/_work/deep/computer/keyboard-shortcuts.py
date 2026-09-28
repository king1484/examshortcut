"""Phase-2 deep content for computer/keyboard-shortcuts. Run: py -3 keyboard-shortcuts.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from ks_part1 import build_windows, build_office
from ks_part2 import build_excel_ppt, build_browser, build_function_keys


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Direct 'which shortcut does X' recall", "very common",
      "'Which shortcut opens File Explorer / creates a new folder / locks the screen?', 'the shortcut to close the active program is'.",
      "Recall by first-letter logic on the Win-key row (Win+E Explorer, Win+L Lock, Win+R Run) and by family: Alt+F4 closes a program, Alt+Tab switches, Ctrl+Shift+Esc opens Task Manager directly while Ctrl+Alt+Del shows the security screen first. Eliminate options whose modifier contradicts the verb.",
      "ks-windows",
      "Which shortcut opens File Explorer?",
      "Win+E — E for Explorer. Win+X is the power-user menu, Win+P projection."),
    P("'What does key X do' reverse recall", "very common",
      "'Ctrl+H in Word opens…', 'Ctrl+D in Word/Excel does what?', 'What is the function of Ctrl+Y?' — the key is given, the action is asked.",
      "Reverse the table: key first, then app. Ctrl+H = Replace in Word but History in a browser; Ctrl+D = Font dialog in Word, fill down in Excel, duplicate in PowerPoint, bookmark in a browser; Ctrl+Y = redo. Always read which application the stem names before answering.",
      "ks-common-office",
      "In MS Word, Ctrl+D opens the:",
      "Font dialog box — not duplicate (PowerPoint) and not fill-down (Excel)."),
    P("Function key questions", "very common",
      "'F1 is used for', 'which key refreshes the page?', 'spell check runs on which function key?', 'which F-key starts the slideshow?'.",
      "Ladder recall: F1 help, F2 rename/edit cell, F3 search, F5 refresh/show/Go To, F7 spelling, F12 Save As (Office) or developer tools (browser). Then let the app decide: F5 in PowerPoint is the show, F5 on the desktop is refresh.",
      "ks-function-keys",
      "Which function key runs the spelling and grammar check?",
      "F7 — in Word, Excel and PowerPoint alike."),
    P("Same key in different applications", "common",
      "'F5 in MS PowerPoint starts… but on the desktop it…', 'Ctrl+D has different uses in Word, Excel and a browser', statement questions mixing apps.",
      "Build the cross-table: F5 = refresh/reload (Windows, browsers) vs slideshow (PPT) vs Go To (Word); F12 = Save As (Office) vs dev tools (browser); Ctrl+Shift+N = Incognito (browser) vs new folder (Explorer); Ctrl+H = Replace (Word) vs History (browser). The app named in the stem picks the answer.",
      "ks-excel-ppt",
      "F5 in MS PowerPoint starts the slideshow. What does F5 do on the Windows desktop?",
      "It refreshes the desktop or active window — same key, different job per application."),
    P("Browser vs Office double-duty keys", "very common",
      "'Ctrl+H in a browser opens…', 'shortcut for Incognito mode', 'which shortcut reopens a closed tab?', 'Ctrl+D in Chrome does what?'.",
      "Browser column: Ctrl+T new tab, Ctrl+W close, Ctrl+Shift+T reopen closed, Ctrl+Shift+N Incognito (Firefox = Ctrl+Shift+P), Alt+Left back, Ctrl+D bookmark, Ctrl+H history, Ctrl+J downloads, Ctrl+Shift+Delete clear data. Check the stem says 'browser' — Ctrl+H is Replace in Word and Ctrl+Shift+N is a new folder in Explorer.",
      "ks-browser",
      "In a web browser, Ctrl+H opens:",
      "Browsing history — the same keys open Find and Replace in MS Word."),
    P("Match-the-following shortcut tables", "common",
      "List A has shortcuts (or keys), List B has actions; options are four mappings like 'A-2, B-1, C-4, D-3'.",
      "Solve the sure pairs first: bold Ctrl+B, undo Ctrl+Z, Task Manager Ctrl+Shift+Esc, new folder Ctrl+Shift+N, slideshow F5. Strike every option mispairing a certain pair, then match the leftovers by elimination.",
      "ks-windows",
      "Match: A. Ctrl+Shift+N  B. Alt+F4  C. Win+E  D. Ctrl+Shift+Esc\n1. Close program 2. New folder 3. Task Manager 4. File Explorer",
      "A-2, B-1, C-4, D-3 — each certain pair removes two wrong options at once."),
]

if __name__ == "__main__":
    subs = [build_windows(), build_office(), build_excel_ppt(),
            build_browser(), build_function_keys()]
    apply_topic("keyboard-shortcuts", subs, PYQ)
