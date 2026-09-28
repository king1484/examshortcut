"""MS Word practice questions."""


def add_interface(S):
    S.q("mw-i1", "easy", "In MS Word, bold, italic and underline buttons are found in the Font group of which tab?",
        ["Home", "Insert", "View", "Layout"], "Home",
        "Character formatting lives in the **Font group of the Home tab**. Insert adds objects, View changes views, Layout handles page setup.",
        "Formatting tab = Home.", 20)
    S.q("mw-i1", "medium", "The option to insert a page number in MS Word is available on the —",
        ["Insert tab", "Review tab", "File tab", "References tab"], "Insert tab",
        "Page numbers come from **Insert, Page Number** (usually placed in the header or footer). References holds TOC and footnotes; Review holds proofing tools.",
        "Page number = Insert, header/footer family.", 25)
    S.q("mw-i1", "medium", "Which pair of features is correctly matched with its ribbon tab?",
        ["Table of Contents — References tab", "Track Changes — Insert tab", "Margins — Home tab", "Zoom — File tab"],
        "Table of Contents — References tab",
        "TOC, footnotes, endnotes and citations are all on **References**. Track Changes is Review, margins are Layout, zoom is View/status bar.",
        "References = TOC + notes + citations.", 30)
    S.q("mw-i2", "easy", "Which MS Word view shows the document exactly as it will appear when printed?",
        ["Print Layout", "Web Layout", "Outline", "Draft"], "Print Layout",
        "**Print Layout** (the default view) displays pages, margins and breaks as they will print. Web Layout mimics a web page, Outline works on headings, Draft hides graphics.",
        "Default + print-true = Print Layout.", 20)
    S.q("mw-i2", "medium", "Reema wants to read a long report without editing tools distracting her. Which view should she use?",
        ["Read Mode", "Draft", "Web Layout", "Outline"], "Read Mode",
        "**Read Mode** hides the ribbon and shows the text like an e-book. Draft is for fast plain editing, not distraction-free reading.",
        "Reading without distraction = Read Mode.", 25)
    S.q("mw-i2", "medium", "Which view is best suited for rearranging the headings of a long report?",
        ["Outline", "Print Layout", "Read Mode", "Web Layout"], "Outline",
        "**Outline view** shows only headings and body levels, so whole sections can be dragged up and down to restructure the report.",
        "Headings only, movable = Outline.", 25)
    S.q("mw-i3", "easy", "The page number and word count of the open document are shown on the —",
        ["Status bar", "Title bar", "Ribbon", "Quick Access Toolbar"], "Status bar",
        "The **status bar** at the bottom shows Page x of y, the live word count, language and the zoom slider.",
        "Bottom strip = status bar.", 20)
    S.q("mw-i3", "medium", "Which statement about zoom in MS Word is correct?",
        ["Zoom changes only the on-screen size of the page, not the printed size",
         "Zoom changes the font size of the document permanently",
         "Zoom is available only in Draft view",
         "Zoom can be changed only from the File tab"],
        "Zoom changes only the on-screen size of the page, not the printed size",
        "Zoom (slider or Ctrl+scroll) is a viewing aid — printing always uses the real font and page sizes.",
        "Zoom = eyes, not print.", 30)
    S.q("mw-i3", "medium", "Which key combination opens the Word Count dialog box?",
        ["Ctrl+Shift+G", "Ctrl+Alt+W", "Shift+F7", "Ctrl+W"], "Ctrl+Shift+G",
        "**Ctrl+Shift+G** opens the Word Count dialog (also on the Review tab and the status bar). Shift+F7 is the thesaurus; Ctrl+W closes the document.",
        "Trap pair: Shift+F7 thesaurus vs Ctrl+Shift+G count.", 30)
    S.q("mw-i4", "easy", "MS Word is a —",
        ["Word processor", "Spreadsheet program", "Presentation program", "Database program"],
        "Word processor",
        "Word is the **word processor** of Microsoft Office; Excel is the spreadsheet, PowerPoint the presentation program, Access the database.",
        "Word = words.", 20)
    S.q("mw-i4", "medium", "Which of the following is NOT available in the Backstage view opened by the File tab?",
        ["Ribbon formatting commands", "Print", "Options", "Save As"],
        "Ribbon formatting commands",
        "Backstage view handles file-level work: New, Open, Save As, Print, Export, Options. **Formatting commands live on the ribbon**, not in Backstage.",
        "File tab = file work, not formatting.", 30)
    S.q("mw-i5", "easy", "Which shortcut key is used to undo the last action in MS Word?",
        ["Ctrl+Z", "Ctrl+Y", "Ctrl+U", "Ctrl+A"], "Ctrl+Z",
        "**Ctrl+Z = Undo**; Ctrl+Y = Redo, Ctrl+U = underline, Ctrl+A = select all.",
        "Z = zap the last step.", 20)
    S.q("mw-i5", "medium", "Why should the Enter key NOT be pressed at the end of every line while typing in Word?",
        ["Word wrap moves text to the next line automatically, so Enter would create broken paragraphs",
         "Enter deletes the previous line",
         "Word allows only one Enter per document",
         "Enter turns off word wrap permanently"],
        "Word wrap moves text to the next line automatically, so Enter would create broken paragraphs",
        "**Word wrap** breaks lines by itself. Enter should be pressed only to end a paragraph — otherwise editing later becomes messy.",
        "Enter = paragraph end only.", 30)


def add_formatting(S):
    S.q("mw-f1", "easy", "The keyboard shortcut for Italics in MS Word is —",
        ["Ctrl+I", "Ctrl+K", "Ctrl+J", "Ctrl+P"], "Ctrl+I",
        "**Ctrl+I = Italic**; Ctrl+K inserts a hyperlink, Ctrl+J justifies, Ctrl+P prints.",
        "B-I-U: bold, italic, underline.", 20)
    S.q("mw-f1", "medium", "Which shortcut places selected text as a subscript?",
        ["Ctrl+=", "Ctrl+Shift+=", "Ctrl+Shift+S", "Ctrl+-"], "Ctrl+=",
        "**Ctrl+= = subscript** (H2O); the Shift version, Ctrl+Shift+=, gives superscript (x squared style).",
        "Subscript = plain =; superscript adds Shift.", 30)
    S.q("mw-f1", "medium", "Pressing Shift+F3 with a word selected in MS Word —",
        ["Cycles the case between lowercase, UPPERCASE and Capitalise Each Word",
         "Opens the thesaurus",
         "Inserts a footnote",
         "Repeats the last find"],
        "Cycles the case between lowercase, UPPERCASE and Capitalise Each Word",
        "**Shift+F3 is the Change Case shortcut** — tap it repeatedly to cycle. Thesaurus is Shift+F7.",
        "F3 = case cycle.", 30)
    S.q("mw-f1", "hard", "Which shortcut pair is correctly matched?",
        ["Grow font — Ctrl+Shift+>", "Grow font — Ctrl+<", "Subscript — Ctrl+Shift+=", "Underline — Ctrl+D"],
        "Grow font — Ctrl+Shift+>",
        "Ctrl+Shift+> grows the font size and Ctrl+< shrinks it. Ctrl+D opens the Font dialog, not underline (Ctrl+U).",
        "Bigger sign > = bigger font.", 40)
    S.q("mw-f2", "easy", "Which shortcut key centres the selected paragraph in MS Word?",
        ["Ctrl+E", "Ctrl+C", "Ctrl+J", "Ctrl+M"], "Ctrl+E",
        "**Ctrl+E = centre** (E for cEntrE). Ctrl+J justifies, Ctrl+M indents, Ctrl+C copies.",
        "E = cEntRE.", 20)
    S.q("mw-f2", "medium", "In MS Word, Ctrl+J is used to —",
        ["Justify the paragraph so both edges are aligned", "Jump to a page", "Insert a journal entry", "Join two paragraphs"],
        "Justify the paragraph so both edges are aligned",
        "**Ctrl+J = Justify** — the text is stretched so the left AND right margins are straight, as in newspapers.",
        "J = Justify.", 25)
    S.q("mw-f2", "medium", "What is the default text alignment of a new MS Word document?",
        ["Left", "Right", "Centre", "Justify"], "Left",
        "A new document is **left-aligned**: the right edge stays ragged unless you change it.",
        "Typing starts from the left.", 20)
    S.q("mw-f3", "medium", "Which shortcut applies single line spacing in MS Word?",
        ["Ctrl+1", "Ctrl+2", "Ctrl+5", "Ctrl+L"], "Ctrl+1",
        "**Ctrl+1 = single**, Ctrl+5 = 1.5 lines, Ctrl+2 = double line spacing.",
        "1-5-2 = single-1.5-double.", 25)
    S.q("mw-f3", "medium", "To start a new page immediately from the current cursor position, press —",
        ["Ctrl+Enter", "Shift+Enter", "Alt+Enter", "Ctrl+P"], "Ctrl+Enter",
        "**Ctrl+Enter inserts a page break**. Shift+Enter is only a soft line break; Ctrl+P prints.",
        "Big Enter = big break.", 25)
    S.q("mw-f3", "hard", "A student typed 1.5 at the start of a line and the paragraph spacing changed to 1.5 lines. Which key caused it?",
        ["Ctrl+5", "Ctrl+1.5", "Ctrl+Shift+5", "Alt+5"], "Ctrl+5",
        "**Ctrl+5 sets 1.5 line spacing** — a classic accidental shortcut. Ctrl+2 is double, Ctrl+1 single.",
        "5 on the number row = 1.5.", 40)
    S.q("mw-f4", "easy", "The default orientation of an MS Word page is —",
        ["Portrait", "Landscape", "Diagonal", "Depends on the printer"], "Portrait",
        "New pages are **Portrait** (taller than wide). Landscape is chosen manually on the Layout tab.",
        "Default = upright.", 20)
    S.q("mw-f4", "medium", "In the default (Normal) margin setting, the blank space around an MS Word page is —",
        ["1 inch on all four sides", "1.5 inches on all four sides", "0.5 inch on all four sides", "2 inches top, 1 inch others"],
        "1 inch on all four sides",
        "Normal margins are **1 inch (2.54 cm) on top, bottom, left and right**.",
        "Normal = 1 inch square ring.", 25)
    S.q("mw-f4", "medium", "A wide marksheet table keeps getting cut at the right edge. Which change helps most?",
        ["Change the page orientation to Landscape", "Change the font colour", "Increase the zoom to 150%", "Turn on word wrap"],
        "Change the page orientation to Landscape",
        "**Landscape** widens the page (Layout tab, Orientation) so wide tables fit. Zoom only changes the screen view.",
        "Wide table = wide page.", 30)
    S.q("mw-f5", "easy", "The default font of documents created in Word 2007 to Word 2019 is —",
        ["Calibri", "Times New Roman", "Arial", "Aptos"], "Calibri",
        "Office 2007 onwards used **Calibri 11 pt**. Times New Roman 12 was the pre-2007 default; Aptos 12 ships only in the newest Microsoft 365 builds.",
        "2007+ = Calibri 11.", 20)
    S.q("mw-f5", "medium", "Font size in MS Word is measured in —",
        ["Points", "Inches", "Pixels", "Centimetres"], "Points",
        "Font size uses **points** (72 points = 1 inch of character height). Page size uses inches or centimetres.",
        "Letters = points.", 20)


def add_tools(S):
    S.q("mw-t1", "easy", "Mail merge in MS Word is used to —",
        ["Create many personalised documents from one template and a data list",
         "Merge two Word files into one",
         "Join two tables side by side",
         "Compress a document for e-mail"],
        "Create many personalised documents from one template and a data list",
        "**Mail merge** produces one finished copy per record — same letter body, different names and addresses.",
        "One letter, many receivers.", 20)
    S.q("mw-t1", "medium", "Which of the following is NOT a component of mail merge?",
        ["Header footer pair", "Main document", "Data source", "Merged document"],
        "Header footer pair",
        "The three components are the **main document, the data source and the merged output**. Headers/footers are page furniture, unrelated to merging.",
        "3 parts: letter + list + result.", 25)
    S.q("mw-t1", "medium", "In mail merge, the placeholder <<City>> inserted in the main document is called a —",
        ["Merge field", "Bookmark", "Hyperlink", "Cross-reference"],
        "Merge field",
        "**Merge fields** (shown inside double angle brackets) mark where each data-source value will be filled in.",
        "<< >> = slot from the list.", 25)
    S.q("mw-t1", "hard", "Arrange the mail-merge steps in order: 1. Preview results 2. Write the main document 3. Attach the data source 4. Insert merge fields",
        ["2, 3, 4, 1", "3, 2, 4, 1", "2, 4, 3, 1", "4, 3, 2, 1"],
        "2, 3, 4, 1",
        "Write the letter, attach the data source, insert merge fields, preview, then finish and merge.",
        "Letter, list, slots, check.", 40)
    S.q("mw-t2", "easy", "A footnote in MS Word appears at the —",
        ["Bottom of the same page", "End of the document", "Top of the page", "Left margin"],
        "Bottom of the same page",
        "**Footnotes print at the foot (bottom) of the page**; endnotes are collected at the end of the document or section.",
        "Foot of page = footnote.", 20)
    S.q("mw-t2", "medium", "The shortcut to insert an endnote in MS Word is —",
        ["Ctrl+Alt+D", "Ctrl+Alt+F", "Ctrl+Shift+E", "Alt+Ctrl+M"], "Ctrl+Alt+D",
        "**Ctrl+Alt+D = endnote** (D for enD); Ctrl+Alt+F = footnote (F is right under your fingers for 'foot').",
        "F = Foot, D = enD.", 30)
    S.q("mw-t2", "medium", "An automatic Table of Contents in Word can be generated only if the headings use —",
        ["Heading styles", "Bold formatting", "A larger font size", "Bulleted lists"],
        "Heading styles",
        "TOC reads the **style names** (Heading 1, Heading 2...), not the visual look — manually bolded lines are invisible to it.",
        "No style, no TOC.", 30)
    S.q("mw-t2", "hard", "After editing a report, its Table of Contents shows wrong page numbers. The fastest fix is —",
        ["Update the field (right-click, Update Field or F9)", "Retype the TOC manually", "Delete the headings", "Save as PDF"],
        "Update the field (right-click, Update Field or F9)",
        "The TOC is a **field** — one update (F9) re-reads the headings and refreshes every page number.",
        "Fields refresh, never retype.", 40)
    S.q("mw-t3", "easy", "Which key runs the spelling and grammar check in MS Word?",
        ["F7", "F5", "F2", "F12"], "F7",
        "**F7 = Spelling & Grammar**. F5 starts a slideshow in PowerPoint but in Word it opens Go To.",
        "F7 finds your typos.", 20)
    S.q("mw-t3", "medium", "Which feature marks every insertion and deletion made by co-authors?",
        ["Track Changes", "AutoCorrect", "Format Painter", "Mail merge"],
        "Track Changes",
        "**Track Changes** (Review tab, Ctrl+Shift+E) records each edit so reviewers can accept or reject it later.",
        "Review tab = teamwork tools.", 25)
    S.q("mw-t3", "medium", "To attach a virtual sticky note to a selected sentence for a reviewer, use —",
        ["New Comment (Ctrl+Alt+M)", "Footnote (Ctrl+Alt+F)", "Text highlight", "Word Count"],
        "New Comment (Ctrl+Alt+M)",
        "**Comments** are margin notes attached to text (Review tab, Ctrl+Alt+M). They print separately and can be resolved or deleted.",
        "Comment = sticky note.", 30)
    S.q("mw-t4", "medium", "Before enabling macros in a document, Word shows a warning mainly because —",
        ["Macros can carry viruses", "Macros change the font", "Macros delete the ribbon", "Macros need the internet"],
        "Macros can carry viruses",
        "A macro is runnable code, so a **macro virus** can hide inside a .docm file and run when opened — hence the warning bar.",
        "Running code = virus risk.", 30)
    S.q("mw-t4", "medium", "Which file extension is used for a macro-enabled Word document?",
        [".docm", ".docx", ".dotx", ".rtf"], ".docm",
        "**m = macro**: .docm for documents, .dotm for macro templates. Plain .docx cannot store macros.",
        "Macro = m.", 25)


def add_extensions(S):
    S.q("mw-e1", "easy", "The default extension of a Word 2007 or later document is —",
        [".docx", ".doc", ".xlsx", ".dot"], ".docx",
        "**.docx** is the Office Open XML default from Word 2007 onwards; .doc is the 97-2003 file.",
        "2007+ = X formats.", 20)
    S.q("mw-e1", "medium", "In the extension .docx, the letter X stands for —",
        ["XML", "Extended", "Extra", "Executable"], "XML",
        "The X marks the **Office Open XML** format introduced with Office 2007 — the same X appears in .xlsx and .pptx.",
        "X = XML, 2007 onwards.", 25)
    S.q("mw-e2", "easy", "A document saved in Word 97-2003 format carries which extension?",
        [".doc", ".docx", ".docm", ".dotx"], ".doc",
        "The old binary format is **.doc**; X-less extensions are always the pre-2007 formats.",
        "Old = no X.", 20)
    S.q("mw-e2", "medium", "Word 2003 cannot open a .docx file directly. What did Microsoft provide for this?",
        ["Compatibility Pack", "Service Pack 3 only", "A new licence", "Nothing at all"],
        "Compatibility Pack",
        "The free **Compatibility Pack** let old Word versions open and save the new XML formats.",
        "Old Word + pack = opens new files.", 30)
    S.q("mw-e3", "medium", "Which extension belongs to a Word template?",
        [".dotx", ".docx", ".xlsx", ".pptx"], ".dotx",
        "Templates carry **t**: .dotx (plain) and .dotm (with macros). Opening one creates a fresh untitled copy.",
        "t = template.", 25)
    S.q("mw-e3", "medium", "What happens when a .dotx template file is opened?",
        ["A new untitled document based on the template opens", "The template itself opens for editing",
         "The file converts to .docx", "Word restarts"],
        "A new untitled document based on the template opens",
        "Templates protect their design: Word gives you a **fresh copy** (Document1, Document2...) built on the template.",
        "Template = mould, not the cake.", 30)
    S.q("mw-e4", "easy", "Which format should be used to e-mail a document that must print identically everywhere?",
        [".pdf", ".docx", ".txt", ".rtf"], ".pdf",
        "**PDF** freezes fonts, layout and pictures on every device and printer.",
        "Fixed layout = PDF.", 20)
    S.q("mw-e4", "medium", "Which extension stores plain text with NO formatting at all?",
        [".txt", ".rtf", ".odt", ".docx"], ".txt",
        "**.txt** keeps only characters — no bold, fonts, colours or images. .rtf keeps simple formatting, .odt and .docx keep full formatting.",
        "txt = typing only.", 25)
    S.q("mw-e4", "hard", "Match the column: 1. .rtf 2. .odt 3. .pdf — a. OpenDocument text b. fixed print layout c. Rich Text Format",
        ["1-c, 2-a, 3-b", "1-a, 2-c, 3-b", "1-b, 2-a, 3-c", "1-c, 2-b, 3-a"],
        "1-c, 2-a, 3-b",
        ".rtf = Rich Text Format, .odt = OpenDocument Text (free office suites), .pdf = fixed print layout.",
        "R = Rich, O = Open, P = Print.", 40)
    S.q("mw-e1", "medium", "Which file CANNOT be created by MS Word's own Save As list?",
        [".pptx", ".pdf", ".odt", ".rtf"], ".pptx",
        "Word saves documents (.docx, .doc, .dotx, .docm), PDF, XPS, web page, .rtf and .odt — but **.pptx belongs to PowerPoint**, a different program.",
        "Slides are not Word's job.", 30)
