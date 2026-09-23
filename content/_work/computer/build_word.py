# -*- coding: utf-8 -*-
"""Topic 4: ms-word"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

T = {
  "id": "ms-word",
  "sectionId": "computer",
  "title": "MS Word",
  "order": 4,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 3},
  "summary": "Word-processing features, formatting defaults, mail merge, references and the Word shortcut set. Shift analyses regularly put 2-4 CKT questions on Word - mostly shortcut keys and default settings.",
  "subtopics": [
    {
      "id": "mw-interface",
      "title": "Word interface, views and basics",
      "concept": """MS Word (part of Microsoft Office since 1983) is a word processor used for documents such as letters and reports.

**Interface:** Ribbon tabs (File, Home, Insert, Design, Layout, References, Mailings, Review, View) hold grouped commands; the Quick Access Toolbar sits above it (customisable); the Status bar (bottom) shows page number, word count and zoom; the **File tab** opens Backstage view (New/Open/Save/Print/Options).

**Document views:** Print Layout (**default**), Read Mode, Web Layout, Outline, Draft. Zoom from 10% to 500%. **Word wrap** moves text to the next line automatically - pressing Enter starts a new paragraph, not a new line. **AutoCorrect** fixes typos as you type (teh -> the); AutoText/Quick Parts stores reusable blocks. The Office Clipboard keeps up to **24** cut/copied items; the Format Painter copies formatting (double-click to lock it). Templates (.dotx) give ready-made layouts; the normal template is Normal.dotm.

**Document window keys:** Ctrl+N new, Ctrl+O open, Ctrl+S save, Ctrl+P print, Ctrl+W close document, Alt+F4 exit Word.""",
      "formulas": [],
      "tricks": [
        {"title": "Views ladder", "body": "Default view = **Print Layout** (what you print is what you see). Reading = book mode; Web = browser look; Outline = headings hierarchy; Draft = bare text. If a question says 'default', Print Layout is the answer.", "example": {"q": "Default document view in Word?", "solution": "Print Layout."}},
        {"title": "Backstage tab", "body": "New, Open, Save, Print, Options live under the **File** tab (Backstage view), not the Home ribbon. Any 'where do you find Print/Options' question -> File tab.", "example": {"q": "Which tab contains the Options dialog?", "solution": "File (Backstage view)."}}
      ],
      "mistakes": [
        "Pressing Enter at each line end - word wrap handles line breaks; Enter creates paragraphs.",
        "Calling the status bar's word-count the only count - Word Count is also a dialog (Ctrl+Shift+G, Review tab).",
        "Assuming Draft is the default view."
      ]
    },
    {
      "id": "mw-formatting",
      "title": "Formatting text, paragraphs and pages",
      "concept": """**Character formatting:** bold (Ctrl+B), italic (Ctrl+I), underline (Ctrl+U), font face/size, colour, highlight, Strikethrough, Subscript (Ctrl+=), Superscript (Ctrl+Shift+=), Change Case (Shift+F3: Sentence case -> lowercase -> UPPERCASE -> Capitalize Each Word -> tOGGLE cASE), Grow/Shrink font (Ctrl+Shift+> / < , or Ctrl+] / [ in 1-pt steps). Default font: Calibri 11 pt from Word 2007-2021; Office 365/2024 switched the default to **Aptos 12 pt** (2023).

**Paragraph formatting:** alignment - left (**default**), centre (Ctrl+E), right (Ctrl+R), justify (Ctrl+J); line spacing single/double (Ctrl+1/Ctrl+2)/1.5 (Ctrl+5); spacing before/after (Word 2013+ default 1.08 lines with 8 pt after); indentation (Ctrl+M in, Ctrl+Shift+M out; Ctrl+T hanging indent); bullets/numbering/multilevel lists; borders and shading; Drop Cap (Insert tab).

**Page setup (Layout tab):** margins, size (A4/Letter), orientation **portrait (default) / landscape**; columns (1 default); line numbers, hyphenation. Insert: **page break (Ctrl+Enter)**, section breaks (change layout mid-document), page numbers, header/footer (default header/footer position is 1.25 cm / 0.5 inch from edge), watermark, page colour, page border, cover page. Headers/footers repeat automatically on every page unless sections differ.""",
      "formulas": [],
      "tricks": [
        {"title": "Alignment letters", "body": "The shortcut letter sits inside the word: c**t**rE? No - simply: **L**eft=Ctrl+**L**, C**E**nter=Ctrl+**E**, **R**ight=Ctrl+**R**, **J**ustify=Ctrl+**J**. Only Centre breaks the pattern with E.", "example": {"q": "Shortcut for justify alignment?", "solution": "Ctrl+J."}},
        {"title": "Spacing numbers", "body": "Line-spacing shortcuts ARE the spacing: Ctrl+**1** single, Ctrl+**2** double, Ctrl+**5** 1.5. (Five looks like S for single-and-a-half.)", "example": {"q": "Shortcut for 1.5 line spacing?", "solution": "Ctrl+5."}},
        {"title": "Case cycle", "body": "**Shift+F3** cycles case: start at 'hello world' -> HELLO WORLD -> Hello World. Press it repeatedly to see all five styles; no menu needed.", "example": {"q": "Shortcut to cycle through case styles?", "solution": "Shift+F3."}}
      ],
      "mistakes": [
        "Using Ctrl+H for hyperlink - Ctrl+H is Replace; hyperlink is **Ctrl+K**.",
        "Thinking landscape is the default orientation - portrait is.",
        "Confusing subscript (Ctrl+=) with superscript (Ctrl+Shift+=)."
      ]
    },
    {
      "id": "mw-tools-mailmerge",
      "title": "Mail merge, references, review and macros",
      "concept": """**Mail merge** creates many personalised documents from one template: (1) write the main document, (2) attach a data source (Excel list, Access table, Outlook contacts), (3) insert merge fields («Name»), (4) preview, (5) merge to letters, e-mails, envelopes or labels. Tabs: Mailings -> Start Mail Merge. Used for certificates, call letters, mailing labels.

**Tables:** Insert -> Table; a table is rows x columns of cells. Table formulas work like `=SUM(ABOVE)`, `=AVERAGE(LEFT)` (Layout tab -> Formula). Convert text to table and vice versa.

**References tab:** automatic **Table of Contents** (needs Heading 1-3 **styles** applied first), footnotes (**Alt+Ctrl+F** - note at page bottom) vs endnotes (**Alt+Ctrl+D** - at document end), citations/bibliography, captions, index.

**Review tab:** Spelling & Grammar (**F7**), Thesaurus (**Shift+F7**), Word Count (**Ctrl+Shift+G**; words/characters/paragraphs/lines), **Track Changes** (edits recorded for review), Comments (Ctrl+Alt+M), Compare, Restrict Editing, Protect Document (password to open/modify; Mark as Final).

**Macros:** recorded/written sequences of commands (VBA); run with **Alt+F8**; files with macros saved as **.docm**; macro security warns about macro viruses.""",
      "formulas": [],
      "tricks": [
        {"title": "No style, no TOC", "body": "An automatic Table of Contents is built from **Heading styles**. If the headings were bolded by hand (not styled), the TOC comes out empty - the classic trap.", "example": {"q": "Auto TOC requires?", "solution": "Headings formatted with built-in Heading styles."}},
        {"title": "Footnote = F below, Endnote = D for 'enD'", "body": "**Alt+Ctrl+F** = **F**ootnote (bottom of page); **Alt+Ctrl+D** = en**D**note (end of document/section).", "example": {"q": "Shortcut to insert a footnote?", "solution": "Alt+Ctrl+F."}},
        {"title": "Merge field marks", "body": "Mail-merge placeholders appear inside guillemets - «Name». Data comes from the **data source**; the letter layout lives in the **main document**. Two parts, always.", "example": {"q": "In mail merge, the Excel list of recipients is the?", "solution": "Data source."}}
      ],
      "mistakes": [
        "Believing Track Changes is on the Insert tab - it is on Review.",
        "Trying to build an automatic TOC from manually bolded text - styles are compulsory.",
        "Calling Ctrl+Shift+G the Thesaurus - that opens Word Count; Shift+F7 is Thesaurus."
      ]
    },
    {
      "id": "mw-extensions",
      "title": "File types and defaults",
      "concept": """| Extension | Meaning |
|---|---|
| .docx | Word document, Word 2007+ (Office Open XML; the X = XML) |
| .doc | Word 97-2003 document (still opens in new Word) |
| .dotx / .dotm / .docm | Template / macro-enabled template / macro-enabled document |
| .rtf | Rich Text Format (portable formatting) |
| .odt | OpenDocument text (LibreOffice) |
| .pdf | Portable Document Format (Word can Save As/Export to PDF) |

**Defaults to memorise:** new file name **Document1**; default font Calibri 11 pt (2007-2021) / Aptos 12 pt (Office 365, 2023 onwards); default alignment left; default line spacing 1.08 (Word 2013+) with 8 pt space-after; default view Print Layout; default orientation portrait; default A4 (or Letter in US installs); normal template **Normal.dotm**; default author name from Office account settings.""",
      "formulas": [],
      "tricks": [
        {"title": "X = XML = 2007+", "body": "Across Office: **docx/xlsx/pptx = 2007 and later** (Office Open XML, zip-compressed); the 3-letter .doc/.xls/.ppt = 97-2003. If a question mentions the X, it means XML.", "example": {"q": "Default extension of Word 2019 documents?", "solution": ".docx."}},
        {"title": "Font eras", "body": "Word 2003 default = Times New Roman 12. Word 2007-2021 = **Calibri 11**. Office 365 (mid-2023) & Office 2024 = **Aptos 12**. Exams still ask Calibri 11 most often.", "example": {"q": "Default font of Word 2016?", "solution": "Calibri, 11 pt."}}
      ],
      "mistakes": [
        "Answering .doc for a Word 2007+ default - .doc is the 97-2003 format.",
        "Saying Calibri 12 or Aptos 11 - pairings are Calibri 11 and Aptos 12.",
        "Thinking .docx files cannot be opened in Word 2003 - compatibility packs/converters exist."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Shortcut-key recall", "frequency": "very common", "howToSpot": "'Shortcut key of Hyperlink/Thesaurus/Page break?' - one key combo per question.", "approach": "Learn the shortcut tables as pairs (Ctrl+K link, Shift+F7 thesaurus, Ctrl+Enter break); eliminate look-alikes (Ctrl+H is Replace, not hyperlink)."},
    {"pattern": "Default settings", "frequency": "common", "howToSpot": "'Default font/extension/view/orientation of MS Word?'.", "approach": "Fix the default set: .docx, Calibri 11 (2007-21), Print Layout, portrait, left align."},
    {"pattern": "Mail merge scenario", "frequency": "common", "howToSpot": "'Sending the same letter to many applicants' or asking for the data source.", "approach": "Two parts - main document + data source; merge fields come from the source; output can be letters/labels/envelopes/e-mail."},
    {"pattern": "Feature-tab matching", "frequency": "common", "howToSpot": "'Track Changes is available under which tab?'", "approach": "Tab map: References = TOC/footnotes, Review = spell/track/word count, Mailings = merge, Layout = margins/columns."},
    {"pattern": "Odd-one-out among Office apps", "frequency": "occasional", "howToSpot": "Options list Word, Excel, PowerPoint and one intruder (Access/Outlook or a non-Office app).", "approach": "Know the suite: Word (documents), Excel (spreadsheets), PowerPoint (slides), Access (databases), Outlook (mail) - then spot the odd tag."}
  ],
  "solvedExamples": [
    Q("mw-se01",
      "Which shortcut key inserts a hyperlink in MS Word?",
      ["Ctrl+H", "Ctrl+K", "Ctrl+N", "Ctrl+L"], 1,
      "Ctrl+K opens the Insert Hyperlink dialog in all Office apps. Ctrl+H is Find & Replace, Ctrl+N opens a new document, Ctrl+L left-aligns a paragraph.",
      "'K = linK'. Ctrl+H is the classic trap because H looks like 'hyperlink' but actually means replace.",
      "easy", "mw-formatting", "shortcut-key recall", 30),
    Q("mw-se02",
      "The default file extension of a document saved in MS Word 2016 is:",
      [".doc", ".docm", ".docx", ".dotx"], 2,
      "Word 2007 onwards (including 2016) saves documents in Office Open XML format with the .docx extension. .doc is the 97-2003 format, .docm holds macros, .dotx is a template.",
      "X = XML = 2007+. Plain documents take .docx; only macro documents take .docm.",
      "easy", "mw-extensions", "default extension", 30),
    Q("mw-se03",
      "Statement 1: Mail merge needs a main document and a data source.\nStatement 2: An automatic Table of Contents can be generated from manually bolded headings.",
      ["Only 1 is correct", "Only 2 is correct", "Both are correct", "Both are incorrect"], 0,
      "Mail merge indeed combines a main document with a data source (Statement 1 correct). An automatic TOC is built only from Heading styles applied via the Styles gallery - manual bolding carries no heading information, so Statement 2 is wrong.",
      "Remember 'no style, no TOC'. Bold text is formatting, not structure.",
      "medium", "mw-tools-mailmerge", "feature statement analysis", 45),
    Q("mw-se04",
      "Match: (a) Thesaurus (b) Word Count (c) Spelling & Grammar with shortcuts: (i) F7 (ii) Shift+F7 (iii) Ctrl+Shift+G",
      ["a-ii, b-iii, c-i", "a-iii, b-ii, c-i", "a-ii, b-i, c-iii", "a-i, b-iii, c-ii"], 0,
      "F7 runs Spelling & Grammar, Shift+F7 opens the Thesaurus, Ctrl+Shift+G opens the Word Count dialog. Hence a-ii, b-iii, c-i.",
      "F7 = spell; add Shift = thesaurus; add Ctrl as well = word count. The key gets 'heavier' as the tool gets less common.",
      "medium", "mw-formatting", "shortcut matching", 45),
    Q("mw-se05",
      "Which of the following CANNOT be done from the References tab?",
      ["Insert a table of contents", "Insert a footnote", "Start mail merge", "Insert a caption"], 2,
      "Mail merge lives on the Mailings tab, not References. TOC, footnotes/endnotes, citations and captions are all Reference-tab tools.",
      "Mnemonic: 'Mailings does the Merging'. References only cites and lists.",
      "easy", "mw-tools-mailmerge", "tab-feature matching", 35)
  ],
  "practice": [
    Q("mw-q01",
      "In MS Word, the keyboard shortcut to change the case of selected text (cycling through UPPERCASE, lowercase and Capitalize) is:",
      ["Shift+F3", "Ctrl+F3", "Alt+F3", "F3"], 0,
      "Shift+F3 cycles the case of the selection through Sentence case, lowercase, UPPERCASE, Capitalize Each Word and tOGGLE cASE.",
      "Three states at your fingertips = F3 (the 3 helps you remember).",
      "easy", "mw-formatting", "shortcut-key recall", 30),
    Q("mw-q02",
      "A page break is inserted in MS Word using:",
      ["Ctrl+P", "Ctrl+B", "Ctrl+Enter", "Alt+Enter"], 2,
      "Ctrl+Enter forces the following text to start on a new page. Ctrl+P prints, Ctrl+B bolds, Alt+Enter has no page-break role in Word.",
      "'Break the page' = press Enter with Ctrl's help: Ctrl+Enter.",
      "easy", "mw-formatting", "shortcut-key recall", 30),
    Q("mw-q03",
      "The default alignment of text in a new MS Word paragraph is:",
      ["Centre", "Justify", "Right", "Left"], 3,
      "New paragraphs are left-aligned (ragged right). Justify must be applied deliberately with Ctrl+J.",
      "Word starts everything plain: left align, Calibri 11, Print Layout, portrait.",
      "easy", "mw-formatting", "default settings", 25),
    Q("mw-q04",
      "Which shortcut key runs the spelling and grammar check in MS Word?",
      ["F5", "F7", "F9", "F12"], 1,
      "F7 opens Spelling & Grammar. F5 opens Find & Replace's Go To (and starts a PowerPoint show), F9 refreshes fields, F12 is Save As.",
      "F7 = spell-check in every Office app.",
      "easy", "mw-formatting", "shortcut-key recall", 30),
    Q("mw-q05",
      "Mail merge in MS Word is used to:",
      ["Merge two documents into one file", "Create personalised copies of a document for many recipients", "Merge cells of a table", "Combine multiple fonts"], 1,
      "Mail merge generates letters/labels/envelopes/e-mails where a common main document is personalised from a data source - one template, many recipients.",
      "'Same letter, many names' = mail merge; the trap options play on the word 'merge'.",
      "easy", "mw-tools-mailmerge", "mail merge purpose", 30),
    Q("mw-q06",
      "In mail merge, the list of names and addresses (e.g. an Excel sheet) is called the:",
      ["Main document", "Data source", "Merge field", "Template"], 1,
      "The data source supplies the variable values; the main document holds the fixed text; merge fields like «Name» mark where source values appear.",
      "Fixed letter = main document; variable list = data source. Fields just point at the source.",
      "easy", "mw-tools-mailmerge", "mail merge components", 30),
    Q("mw-q07",
      "To generate an automatic Table of Contents, the document's headings must first be formatted with:",
      ["Bold and underline", "Any font colour", "Built-in Heading styles", "Bullet points"], 2,
      "The TOC engine reads Heading 1-3 styles (and custom TOC styles). Manually bolded text carries no outline level, so it is ignored.",
      "'No style, no TOC' - the styles gallery, not formatting, feeds the TOC.",
      "medium", "mw-tools-mailmerge", "table of contents", 40),
    Q("mw-q08",
      "Track Changes in MS Word is found under which tab?",
      ["Insert", "Review", "View", "Home"], 1,
      "Track Changes, Comments, Compare, Protect and Word Count are all on the Review tab.",
      "Anything about checking/editing text collectively lives in Review.",
      "easy", "mw-tools-mailmerge", "tab-feature matching", 30),
    Q("mw-q09",
      "Which shortcut opens the Word Count dialog box?",
      ["Ctrl+Shift+C", "Ctrl+Shift+G", "Ctrl+Shift+V", "Ctrl+Shift+K"], 1,
      "Ctrl+Shift+G opens Word Count (words, characters with/without spaces, paragraphs, lines). Ctrl+Shift+C copies formatting, Ctrl+Shift+V pastes formatting, Ctrl+Shift+K formats small caps.",
      "Word Count = Ctrl+Shift+G ('G for enGlish count' helps some aspirants).",
      "medium", "mw-formatting", "shortcut-key recall", 35),
    Q("mw-q10",
      "The default font of MS Word 2016 documents is:",
      ["Times New Roman 12", "Arial 11", "Calibri 11", "Calibri 12"], 2,
      "From Word 2007 to 2021 the default body font is Calibri 11 pt (Times New Roman 12 was the Word 2003 default; Office 365 moved to Aptos 12 in 2023).",
      "Eras: 2003 Times New Roman 12 -> 2007-21 Calibri 11 -> 2023+ Aptos 12.",
      "easy", "mw-extensions", "default font", 30),
    Q("mw-q11",
      "Which of the following is a macro-enabled Word document extension?",
      [".docx", ".dotx", ".docm", ".rtf"], 2,
      ".docm stores macro-enabled documents; .dotm stores macro-enabled templates. .docx forbids macros, .dotx is a plain template, .rtf is Rich Text Format.",
      "The M = Macro: docm/dotm/xlsm/pptm all carry macros.",
      "medium", "mw-extensions", "file extensions", 35),
    Q("mw-q12",
      "Footnotes inserted with Alt+Ctrl+F appear:",
      ["At the end of the document", "At the bottom of the page where the reference occurs", "In the header", "In a separate file"], 1,
      "Footnotes sit at the foot (bottom) of the same page; endnotes (Alt+Ctrl+D) collect at the end of the document or section.",
      "Foot = foot of the page; end = end of the document.",
      "easy", "mw-tools-mailmerge", "footnotes vs endnotes", 35),
    Q("mw-q13",
      "The keyboard shortcut to increase the indent of a paragraph in MS Word is:",
      ["Ctrl+M", "Ctrl+I", "Ctrl+Shift+M", "Tab"], 0,
      "Ctrl+M increases indent, Ctrl+Shift+M decreases it. (Tab indents only at the start of a paragraph/list item; Ctrl+I is italic.)",
      "M = More indent; add Shift = less.",
      "medium", "mw-formatting", "shortcut-key recall", 35),
    Q("mw-q14",
      "The superscript formatting shortcut in MS Word is:",
      ["Ctrl+=", "Ctrl+Shift+=", "Ctrl+Shift+S", "Ctrl+Alt+S"], 1,
      "Ctrl+Shift+= applies superscript (x squared style); Ctrl+= applies subscript (H2O style). Ctrl+Shift+S opens the Apply Styles box.",
      "Shift pushes the number UP: Shift with = gives the raised (super) script.",
      "medium", "mw-formatting", "shortcut-key recall", 35)
  ]
}

validate_and_dump_topic(T)
