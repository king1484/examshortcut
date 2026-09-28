"""Phase-2 deep content for computer/ms-word. Run: py -3 ms-word.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from mw_pats import build_interface, build_formatting, build_tools, build_extensions
import mw_qs


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Shortcut-key recall", "very common",
      "The stem names a Word action (bold, case change, footnote, thesaurus, page break) and asks its shortcut, or gives a shortcut and asks the action. Wrong-pair variants shift one key to a neighbouring action.",
      "Hold the shortcut families: B/I/U formatting trio, Ctrl+= / Ctrl+Shift+= subscript-superscript, Shift+F3 case, Ctrl+Alt+F / Ctrl+Alt+D footnote-endnote, F7 spelling and Shift+F7 thesaurus, Ctrl+Enter page break. When two options look alike, the odd Shift/Alt is usually the truth-teller.",
      "mw-formatting",
      "The keyboard shortcut to change the case of selected text in MS Word is:",
      "Shift+F3 — it cycles lowercase, UPPERCASE and Capitalise Each Word. F7 alone runs the spelling check."),
    P("Default settings", "very common",
      "Questions on factory defaults: default font and size (Calibri 11 in Word 2007-2021), default view (Print Layout), default alignment (left), default orientation (Portrait), default margins (1 inch).",
      "Keep one default card: Calibri 11, Print Layout, left-aligned, Portrait, 1-inch margins, .docx. Beware the version trap — the newest Microsoft 365 builds moved to Aptos 12, so answer Calibri for 2007-2019 stems.",
      "mw-formatting",
      "The default font size in Word 2007 to Word 2019 is:",
      "11 point Calibri — Times New Roman 12 belonged to Word 97-2003."),
    P("Mail merge scenario", "very common",
      "A scenario: 'send the same letter to 400 customers with each name filled in' or 'print address labels for invitations' — the feature, its components or its tab is asked.",
      "Spot the shape: one fixed document + a list of receivers = mail merge (Mailings tab). Its three parts are the main document, the data source (Excel/Access/Outlook) and the merged output, and the slots in the letter are merge fields like <<Name>>.",
      "mw-tools-mailmerge",
      "To print 500 admission letters with each student's name and address, the best Word feature is:",
      "Mail merge — one main letter joined to a data-source list; Word generates a personalised copy per record."),
    P("Feature-tab matching", "common",
      "'On which tab is Track Changes / Page Number / Table of Contents / Margins?' or a matched pair where one feature sits on the wrong tab.",
      "Recite the tab map: Home formatting, Insert objects, Design themes, Layout page setup, References TOC-notes-citations, Mailings merge, Review proofing and changes, View views and zoom. The planted traps: Track Changes (Review, not Insert), page numbers (Insert, not Layout), TOC (References, not Insert).",
      "mw-interface",
      "In MS Word, the Table of Contents option is available on which tab?",
      "References — together with footnotes, endnotes and citations."),
    P("Odd-one-out among Office apps", "common",
      "'Which one is not a word processor?' or 'which pairing is wrong' with MS Word, Excel, PowerPoint, Access, Outlook in the options.",
      "Fix the family: Word = word processor, Excel = spreadsheet, PowerPoint = presentation, Access = database, Outlook = e-mail and personal organiser. The odd option is usually a famous program pushed into the wrong job (e.g. Excel called a word processor).",
      "mw-interface",
      "Which of the following is NOT a word processor?",
      "MS Excel — it is a spreadsheet program; Word, WordPad and LibreOffice Writer are word processors."),
    P("View and window-parts matching", "common",
      "The stem names a view (Print Layout, Draft, Read Mode, Outline, Web Layout) or a window part (status bar, Quick Access Toolbar, Backstage view) and asks its purpose or default status.",
      "Views: Print Layout is the default and print-true; Draft is plain and fast; Read Mode is distraction-free; Outline restructures headings; Web Layout mimics a browser. Window parts: status bar = page number, word count, zoom; File tab = Backstage (New, Open, Print, Options).",
      "mw-interface",
      "Which window part of MS Word shows 'Page 3 of 12' and the word count?",
      "The status bar at the bottom — the title bar only names the file."),
    P("Extension family (X = XML)", "common",
      "'Default extension of a Word 2007 document', 'which is the 97-2003 format', or mixed extensions (.docx, .xlsx, .pptx, .docm) where the family rule decides.",
      "The X rule: from Office 2007 every default file gained an X — .docx, .xlsx, .pptx (Office Open XML); the X-less forms (.doc, .xls, .ppt) are the 97-2003 formats; an m (.docm, .xlsm, .pptm) always means macro-enabled; t (.dotx) means template.",
      "mw-extensions",
      "A file named report.docm is best described as:",
      "A Word 2007+ document that contains macros — m = macro-enabled."),
]

def _subs():
    out = []
    for build, add in ((build_interface, mw_qs.add_interface), (build_formatting, mw_qs.add_formatting),
                       (build_tools, mw_qs.add_tools), (build_extensions, mw_qs.add_extensions)):
        S = build()
        add(S)
        out.append(S)
    return out


if __name__ == "__main__":
    apply_topic("ms-word", _subs(), PYQ)
