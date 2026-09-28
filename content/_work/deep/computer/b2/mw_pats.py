"""MS Word pattern builders (question types per subtopic)."""
from _lib import Sub


def build_interface():
    S = Sub("mw-interface")
    S.notes = __import__("mw_notes").MW_INTERFACE
    S.pattern("mw-i1", "Which tab holds this feature?", "very common",
        "The stem names a Word feature (Track Changes, Word Art, Page Number, Mail Merge, Spelling) and asks the ribbon tab it lives on, or gives a tab and asks what it contains.",
        None,
        "1. Recall the tab map: Home = formatting, Insert = objects (table, picture, chart, header/footer, page number, text box, symbol), Design = themes, Layout = margins/orientation/size, References = TOC/footnotes, Mailings = mail merge, Review = spelling/track changes/word count, View = views/zoom/navigation.\n2. File is not a ribbon tab — it opens Backstage (New, Open, Print, Options).\n3. Traps: Track Changes is Review (not Insert); page numbers are Insert (not Layout); TOC is References (not Insert).",
        "In MS Word, the Track Changes option is found on which tab?",
        "**Review** — the tab for checking and teamwork: spelling, thesaurus, comments, Track Changes and Compare.")
    S.pattern("mw-i2", "View identification and purpose", "common",
        "The stem describes a need (see the page as printed, read without distraction, reorder pages, plain text without pictures) or names a view and asks its purpose or which one is the default.",
        None,
        "1. Print Layout = default, shows the page as it prints. Read Mode = distraction-free reading. Web Layout = as a web page. Outline = headings only, restructure. Draft = plain text, hides images/headers.\n2. 'See margins and page breaks while typing' means Print Layout.\n3. Default-view questions: the answer is Print Layout, never Draft.",
        "Which view of MS Word is the default view?",
        "**Print Layout** — it shows the page, margins and breaks exactly as the document will print.")
    S.pattern("mw-i3", "Status bar, word count and zoom", "common",
        "The stem asks what the status bar shows, where the word count appears, or what zoom does to the print size.",
        None,
        "1. Status bar (bottom) shows Page x of y, word count, language, view buttons and zoom slider.\n2. Word count: status bar OR Review tab OR Ctrl+Shift+G.\n3. Zoom (Ctrl+scroll or slider) changes only the on-screen size — printing size is fixed by font size.",
        "In MS Word, the word count of a document can be seen on the —",
        "**Status bar and the Review tab** (also Ctrl+Shift+G). The status bar keeps a live count while you type.")
    S.pattern("mw-i4", "Word basics and Backstage view", "common",
        "Direct recall: which program is a word processor, what a Word file is called, what the File tab offers, what the Quick Access Toolbar holds.",
        None,
        "1. Word = word processor; its file = document; part of Microsoft Office suite.\n2. File tab opens **Backstage view**: New, Open, Save/Save As, Print, Share, Export, Options.\n3. QAT default = Save, Undo, Redo — customizable from its drop-down arrow.",
        "Clicking the File tab in MS Word opens the —",
        "**Backstage view** — the full-screen menu for New, Open, Save As, Print, Share, Export and Options. The other tabs show ribbon commands instead.")
    S.pattern("mw-i5", "Undo, Redo and word wrap", "occasional",
        "Questions on which keys cancel the last action, bring it back, or what Word does automatically when a line is full.",
        None,
        "1. Undo = Ctrl+Z, Redo = Ctrl+Y (both also on the Quick Access Toolbar).\n2. Word wrap: the next word moves to a new line automatically — pressing Enter at every line end creates broken paragraphs.\n3. Enter ends a **paragraph**, Shift+Enter ends a line within the same paragraph.",
        "When a typed line reaches the right margin, MS Word —",
        "**moves the next word to a new line automatically (word wrap)**. The Enter key is needed only to start a new paragraph.")
    return S


def build_formatting():
    S = Sub("mw-formatting")
    S.notes = __import__("mw_notes").MW_FORMATTING
    S.pattern("mw-f1", "Character-formatting shortcuts", "very common",
        "'The shortcut of Bold/Italic/Underline/Subscript/Superscript', 'which key changes the case', or a matched pair where one shortcut is shifted to the wrong action.",
        None,
        "1. Core trio: Bold Ctrl+B, Italic Ctrl+I, Underline Ctrl+U (B-I-U = the letters themselves).\n2. Subscript Ctrl+= , Superscript Ctrl+Shift+= (superscript needs the extra Shift).\n3. Case cycle = Shift+F3 (lower, UPPER, Capitalise Each Word). Grow/shrink = Ctrl+Shift+> / Ctrl+<.",
        "The keyboard shortcut to apply superscript in MS Word is:",
        "**Ctrl+Shift+=** — the same key as subscript (Ctrl+=) with Shift added. Both are toggles: press again to return to normal text.")
    S.pattern("mw-f2", "Alignment shortcut matching", "very common",
        "The stem gives an alignment (left, right, centre, justify) and asks the shortcut, or shows Ctrl+E / Ctrl+J and asks what they do.",
        None,
        "1. Ctrl+L left, Ctrl+R right, Ctrl+E centre, Ctrl+J justify — remember **J = Justify (both edges)**.\n2. Default alignment of Word = left.\n3. Justify is used in newspapers and formal documents; centre is used in titles and invitations.",
        "Which shortcut justifies the selected paragraph in MS Word?",
        "**Ctrl+J** — straightens both the left and right edges. Ctrl+E centres, Ctrl+L/Ctrl+R align left/right.")
    S.pattern("mw-f3", "Line spacing and paragraph keys", "common",
        "'Single / 1.5 / double line spacing shortcut', 'which shortcut inserts a page break', bullets and numbering questions.",
        None,
        "1. Ctrl+1 single, Ctrl+5 (five = one-and-a-half on the number row) 1.5, Ctrl+2 double.\n2. Page break = Ctrl+Enter; a hard break starts the next text on a fresh page.\n3. Bullets/numbering sit in the Home tab, Paragraph group.",
        "In MS Word, double line spacing is applied by —",
        "**Ctrl+2** (Ctrl+1 = single, Ctrl+5 = 1.5 lines). All three are toggles for the selected paragraphs.")
    S.pattern("mw-f4", "Page setup: margins, orientation, size", "common",
        "The stem asks the default orientation, the default margin width, where page size or columns are set, or a scenario needing landscape.",
        None,
        "1. Default orientation = **Portrait**; Landscape = sideways, used for wide tables.\n2. Default (Normal) margins = **1 inch** on all four sides.\n3. Margins, Orientation, Size and Columns all live on the **Layout** tab (older name: Page Layout).",
        "The default orientation of a page in MS Word is:",
        "**Portrait** — height greater than width. Landscape (width greater than height) must be chosen manually from the Layout tab.")
    S.pattern("mw-f5", "Default font facts", "common",
        "'Default font of MS Word 2007/2010/2016' or a pair-matching of Office version with its default font and size.",
        None,
        "1. Word 2007 to 2021 default font = **Calibri 11 point** (before 2007 it was Times New Roman 12).\n2. Newer Microsoft 365 builds ship with **Aptos 12** — beware version wording in the stem.\n3. Font size is measured in **points** (72 points = 1 inch).",
        "The default font of Word 2007 to Word 2019 documents is:",
        "**Calibri, 11 point** — replacing Times New Roman 12 of Word 97-2003. Newest Microsoft 365 versions have moved to Aptos 12.")
    return S


def build_tools():
    S = Sub("mw-tools-mailmerge")
    S.notes = __import__("mw_notes").MW_TOOLS_MAILMERGE
    S.pattern("mw-t1", "Mail-merge components and steps", "very common",
        "The stem names the three components, orders the steps, or gives a scenario (result letters to 500 students) and asks the feature or the tab used.",
        None,
        "1. Components: **main document + data source + merged document**.\n2. Steps: write main letter, attach data source, insert merge fields (<<Name>>), preview, finish & merge.\n3. Data source = Excel sheet / Access table / Outlook contacts; everything happens on the **Mailings** tab.",
        "To send the same offer letter to 300 applicants with each name filled in, the Word feature used is:",
        "**Mail merge** (Mailings tab) — one main document plus a data source list; Word generates 300 personalised copies in one run.")
    S.pattern("mw-t2", "Footnote vs endnote vs TOC", "common",
        "The stem contrasts footnotes and endnotes, asks their shortcuts, or asks what an automatic Table of Contents is built from.",
        None,
        "1. Footnote = bottom of the **page** (Ctrl+Alt+F); Endnote = **end of document/section** (Ctrl+Alt+D).\n2. TOC is built only from **heading styles**, not from manually bolded lines; refresh with F9.\n3. All three tools sit on the **References** tab.",
        "In MS Word, a note printed at the bottom of the same page is called a:",
        "**Footnote** (inserted with Ctrl+Alt+F or References, Insert Footnote). The same note collected at the end of the document would be an endnote (Ctrl+Alt+D).")
    S.pattern("mw-t3", "Review-tab tools and shortcuts", "common",
        "Shortcut recall — spelling, thesaurus, word count, comment — or a statement question about Track Changes and Comments.",
        None,
        "1. Spelling & Grammar = **F7**; Thesaurus = **Shift+F7**; Word Count dialog = Ctrl+Shift+G; New Comment = Ctrl+Alt+M; Track Changes = Ctrl+Shift+E.\n2. Track Changes **records every edit** so co-authors can accept or reject it; it is on the Review tab.\n3. Classic trap: Ctrl+Shift+G opens Word Count, not the thesaurus.",
        "In MS Word, the Thesaurus opens with which key?",
        "**Shift+F7** — it suggests synonyms for the selected word. F7 (without Shift) runs the spelling and grammar check.")
    S.pattern("mw-t4", "Macro purpose and macro files", "occasional",
        "'A macro is', 'which file stores macros', or a scenario of a repeated task being automated with one click.",
        None,
        "1. Macro = a **recorded series of commands** replayed by one click or shortcut key.\n2. Macro-enabled files carry **m**: .docm (document), .dotm (template).\n3. Macro viruses travel inside macro files — Word asks before enabling them.",
        "A macro in MS Word is best described as:",
        "**A recorded series of commands that can be replayed with a single click or key** — used to automate repeated steps. Macro files use the .docm extension.")
    return S


def build_extensions():
    S = Sub("mw-extensions")
    S.notes = __import__("mw_notes").MW_EXTENSIONS
    S.pattern("mw-e1", "Default extension of a Word file", "very common",
        "'The default extension of MS Word 2007/2010/2016 is' — four extensions, one right. Sometimes reversed: an extension is given, the program is asked.",
        None,
        "1. Modern default = **.docx** (Word 2007 onwards); the X means Office Open XML.\n2. .doc = Word 97-2003 legacy file.\n3. For Excel the pair is .xlsx/.xls and for PowerPoint .pptx/.ppt — the X rule works across all three programs.",
        "The default file extension of a Word 2016 document is:",
        "**.docx** — Office Open XML format, standard since Word 2007. .doc belongs to Word 97-2003.")
    S.pattern("mw-e2", "doc vs docx legacy trap", "very common",
        "A pair like .doc/.docx (or all four Office pairs) with the question 'which is the older format' or 'which will a Word 2003 file carry'.",
        None,
        "1. 97-2003 = .doc; 2007+ = .docx. Older Word could not open .docx without the **Compatibility Pack**.\n2. In mixed-option questions, the X-less option is always the older format.\n3. .docx files are also smaller and recover data better (XML parts) than .doc.",
        "Which file format was used by Word 97-2003?",
        "**.doc** — the binary format before Office Open XML (.docx) arrived with Word 2007.")
    S.pattern("mw-e3", "Template and macro extensions", "common",
        "The stem asks the extension of a template or a macro-enabled file, or shows .dotx/.docm and asks what it is.",
        None,
        "1. Template = .dotx; macro-enabled document = .docm; macro-enabled template = .dotm.\n2. m always = macro; t = template.\n3. Opening a template creates a fresh untitled copy, so the design stays safe.",
        "A Word file saved with macros enabled carries which extension?",
        "**.docm** — m = macro. A macro-enabled template is .dotm and a plain template is .dotx.")
    S.pattern("mw-e4", "Export and cross-software formats", "common",
        "'To share a document that prints identically everywhere, save as —' or identification of .rtf / .odt / .txt / .pdf meanings.",
        None,
        "1. **PDF** = fixed layout, prints identically on any machine — the sharing choice.\n2. .rtf = Rich Text Format (basic formatting, opens in many editors); .odt = OpenDocument (free office suites); .txt = plain characters only, no formatting.\n3. Save As (F12) is where the format is changed.",
        "Ravi wants his resume to look exactly the same on any computer or printer. He should save it as —",
        "**PDF** — a fixed-layout format that keeps fonts and layout frozen. Word exports or Save-As to PDF from the File menu.")
    return S
