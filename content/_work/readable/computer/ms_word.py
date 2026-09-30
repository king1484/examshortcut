"""Readable rewrite of Computer > MS Word (4 subtopics). Idempotent.
Run: python ms_word.py  (patches content/core/topics/computer/ms-word.json in place)
Facts are kept exactly as in the earlier notes; only the wording and structure change.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rl_common import pat, mis, trick, apply  # noqa: E402

SUBS = {}

# =====================================================================
SUBS["mw-interface"] = dict(
    concept=(
        "**MS Word** is a word processor. You use it to type, edit, format and print documents. "
        "Its commands sit on a **Ribbon** made of tabs. The **File** tab opens Backstage view. "
        "Print Layout is the default view. Pressing Enter starts a new paragraph, because Word wraps lines by itself."
    ),
    notes=r"""### What Word is
MS Word is a **word processor**. It makes letters, reports, applications and resumes. It belongs to the Microsoft Office suite and first appeared in **1983**. A file made in Word is called a **document**.

### Parts of the Word window
Read the window from top to bottom.

| Part | What it does |
|---|---|
| **Title bar** | Shows the file name and the program name |
| **Quick Access Toolbar (QAT)** | Small buttons at the top left. Default buttons: Save, Undo, Redo |
| **Ribbon** | The wide band of commands. Commands sit in groups, and groups sit in tabs |
| **Work area** | The white page where you type |
| **Status bar** | The bottom strip. Shows page number, word count, view buttons and zoom slider |

The Ribbon tabs are **File, Home, Insert, Design, Layout, References, Mailings, Review, View**. The small arrow in the corner of a group opens its full dialog box.

> **Note:** You can add more buttons to the QAT. Use the small drop-down arrow at its right end.

### File tab and Backstage view
The File tab is not an ordinary tab. It does not show a ribbon. It opens the full-screen **Backstage view**.

Backstage view holds New, Open, Save, Save As, Print, Share, Export, Close and **Options**. Every program setting lives under Options.

> **Tip:** If a question asks where to find Print, Save As or Options, answer File tab.

### The five views
Views change how the page looks on screen. You pick them on the View tab or on the status bar.

| View | Use |
|---|---|
| **Print Layout** | The **default view**. Shows the page as it will print |
| **Read Mode** | Full-screen reading. Hides most editing tools |
| **Web Layout** | Shows the text as a web page |
| **Outline** | Works with headings. Good for long reports |
| **Draft** | Plain text. Hides pictures, headers and footers |

> **Rule:** When a question says "default view", the answer is Print Layout.

### Everyday basics
- **Word wrap:** When a line is full, Word moves the next word down by itself. Press Enter only to end a paragraph.
- **Undo** is Ctrl+Z. **Redo** is Ctrl+Y. Both sit on the QAT.
- **Word count** shows on the status bar. You can also use the Review tab or Ctrl+Shift+G.
- **Zoom** runs from 10% to 500%. It changes the size on screen only. It never changes the printed size.
- **AutoCorrect** fixes typing errors as you type. For example, *teh* becomes *the*.
- **Office Clipboard** keeps up to **24** cut or copied items.
- **Format Painter** copies formatting. Double-click it to paint more than once.
- **Templates** are ready-made layouts. The normal template is Normal.dotm.
- **Help** opens with F1.

### Document window keys
| Key | Action |
|---|---|
| Ctrl+N | New document |
| Ctrl+O | Open |
| Ctrl+S | Save |
| Ctrl+P | Print |
| Ctrl+W | Close the document |
| Alt+F4 | Exit Word |
""",
    tricks=[
        trick("Views ladder",
              "Default view is Print Layout: what you print is what you see. Read Mode is for reading. Web Layout is the browser look. Outline shows headings. Draft is bare text."),
        trick("Backstage tab",
              "New, Open, Save, Print and Options live under the File tab. They are not on the Home ribbon.",
              "Where do you find the Options setting in MS Word?",
              ["Options controls all program settings.", "All such settings live in Backstage view.", "Backstage view opens from the File tab."],
              "File tab, then Options"),
    ],
    mistakes=[
        mis("Pressing Enter at the end of every line.", "Let word wrap work. Press Enter only to end a paragraph."),
        mis("Choosing Draft as the default view.", "The default view is Print Layout."),
        mis("Looking for Print or Options on the Home tab.", "Both are in Backstage view, under the File tab."),
        mis("Thinking zoom changes the printed size.", "Zoom changes only the size on screen."),
        mis("Placing Track Changes on the Insert tab.", "Track Changes is on the Review tab."),
    ],
    revision=[
        "Word is a word processor in MS Office, first released in 1983. The file is a document.",
        "Tabs: File, Home, Insert, Design, Layout, References, Mailings, Review, View.",
        "The File tab opens Backstage view: New, Open, Save, Print, Options.",
        "QAT default buttons: Save, Undo (Ctrl+Z), Redo (Ctrl+Y).",
        "Status bar: page number, word count, view buttons, zoom. Print Layout is the default view.",
        "Enter ends a paragraph. Word wrap ends lines by itself.",
        "Office Clipboard holds 24 items. Format Painter: double-click to lock.",
    ],
    patterns=[
        pat("mw-i1", "Which tab holds this feature?", "very common",
            "The question names a feature and asks for its tab: Track Changes, page numbers, mail merge, margins.",
            ["Recall the tab map: Home is formatting, Insert is objects, Layout is page setup.",
             "References holds TOC and footnotes. Mailings holds mail merge.", "Review holds spelling and Track Changes. View holds views and zoom.",
             "Remember that File is not a ribbon tab. It opens Backstage."],
            "Each feature belongs to one tab, and the options mix them up on purpose.",
            "In MS Word, the Track Changes option is found on which tab?",
            ["Track Changes records edits for a reviewer.", "Checking and teamwork tools sit on one tab.", "That tab is Review."],
            "Review"),
        pat("mw-i2", "View identification and purpose", "very common",
            "The question describes a view, or asks for the default view.",
            ["Print Layout is the default. It shows the page as it prints.", "Read Mode is for reading. Web Layout shows a web-page look.",
             "Outline works with headings. Draft shows plain text.", "For \"see margins and page breaks\", choose Print Layout."],
            "Each view has one purpose, and the default is always Print Layout.",
            "Which view of MS Word is the default view?",
            ["Name the view that shows the page as it prints.", "That is the one Word opens with."],
            "Print Layout"),
        pat("mw-i3", "Status bar, word count and zoom", "common",
            "The question asks where the word count shows, or what zoom changes.",
            ["The status bar sits at the bottom. It shows Page x of y, word count, view buttons and zoom.",
             "Word count also has Review tab and Ctrl+Shift+G.", "Zoom changes only the screen size, not the print size."],
            "Word count and zoom sit in familiar places, so this is a recall question.",
            "In MS Word, the word count of a document can be seen on the status bar and on which tab?",
            ["The status bar shows a live count.", "The Review tab has the Word Count tool.", "Ctrl+Shift+G also opens it."],
            "Review tab"),
        pat("mw-i4", "Word basics and Backstage view", "common",
            "The question asks what the File tab opens, or what Word and its file are called.",
            ["Word is a word processor and its file is a document.", "The File tab opens Backstage view.",
             "Backstage holds New, Open, Save As, Print, Share, Export and Options.", "The QAT default is Save, Undo and Redo."],
            "Backstage view is the one place for file-level jobs.",
            "Clicking the File tab in MS Word opens the:",
            ["The File tab shows no ribbon.", "It shows a full-screen menu of file jobs."],
            "Backstage view"),
        pat("mw-i5", "Undo, Redo and word wrap", "common",
            "The question describes a line reaching the margin, or asks for Undo and Redo keys.",
            ["Undo is Ctrl+Z. Redo is Ctrl+Y.", "Word wrap moves the next word to a new line by itself.",
             "Enter ends a paragraph. Shift+Enter ends a line inside the same paragraph."],
            "Students press Enter too often, so the exam checks word wrap.",
            "When a typed line reaches the right margin, MS Word:",
            ["The next word does not fit on the line.", "Word moves it down automatically.", "Enter is needed only for a new paragraph."],
            "Moves the next word to a new line (word wrap)"),
        pat("mw-i6", "Clipboard, Format Painter and AutoCorrect", "occasional",
            "The question asks how many items the Office Clipboard holds, or what copies formatting.",
            ["The Office Clipboard keeps up to 24 items.", "Format Painter copies formatting only. Double-click locks it.",
             "AutoCorrect fixes typing errors as you type."],
            "These three helpers are small facts that are easy to test.",
            "Which Word tool copies the formatting of selected text to other text?",
            ["The tool must copy looks, not words.", "It sits in the Clipboard group.", "Double-clicking it lets you paint again and again."],
            "Format Painter"),
    ],
)

# =====================================================================
SUBS["mw-formatting"] = dict(
    concept=(
        "Word formats at three levels: **characters**, **paragraphs** and the **page**. "
        "Most exam questions ask for a shortcut key. The main ones are Ctrl+B, I, U for style, Ctrl+L, E, R, J for alignment, "
        "and Ctrl+1, 5, 2 for line spacing. Page setup facts are portrait, 1 inch margins and Calibri 11."
    ),
    notes=r"""### Three levels of formatting
Formatting means changing how text looks. Word does it at three levels.

- **Character:** the letters you select.
- **Paragraph:** a whole block of text.
- **Page:** the whole sheet.

### Character formatting
These tools sit on the Home tab, in the Font group.

| Action | Shortcut |
|---|---|
| **Bold** | Ctrl+B |
| **Italic** | Ctrl+I |
| **Underline** | Ctrl+U |
| **Subscript** (H2O style) | Ctrl+= |
| **Superscript** (x2 style) | Ctrl+Shift+= |
| Grow font / shrink font | Ctrl+Shift+> / Ctrl+Shift+< |
| Change case | Shift+F3 |

**Shift+F3** cycles the selected text through the case styles. Other font tools are font face, font size, colour, highlight and **Strikethrough**. Font size is measured in **points**.

> **Tip:** Superscript is the subscript key with one extra Shift.

### Paragraph formatting
These tools sit in the Paragraph group.

| Alignment | Shortcut | Look |
|---|---|---|
| Left (default) | Ctrl+L | Ragged right edge |
| Centre | Ctrl+E | Even on both sides |
| Right | Ctrl+R | Ragged left edge |
| Justify | Ctrl+J | **Both edges straight** |

Justified text is used in newspapers and formal reports.

The line spacing keys use the number itself.

| Spacing | Shortcut |
|---|---|
| Single | Ctrl+1 |
| 1.5 lines | Ctrl+5 |
| Double | Ctrl+2 |

Other paragraph keys: Ctrl+M increases the indent. Ctrl+Shift+M decreases it. Ctrl+T makes a hanging indent. A page break is **Ctrl+Enter**.

> **Watch:** Ctrl+H is Replace. Ctrl+K is Hyperlink. Exams often swap them.

### Page setup on the Layout tab
- **Margins** are the blank space around the text. Normal margins are **1 inch** on all four sides.
- **Orientation** is **portrait** by default. Landscape turns the page sideways for wide tables.
- **Size** is usually A4 in India. Letter and Legal are other sizes.
- **Columns** split text into newspaper-style columns. The default is one column.
- **Header** and **footer** repeat at the top and bottom of every page. You insert them from the Insert tab.

### Default look of a new document
A new document starts with these settings.

- Font: **Calibri 11 point** in Word 2007 to 2021.
- Newer Microsoft 365 builds use **Aptos 12** (from 2023).
- Alignment: left.
- Orientation: portrait.

> **Note:** Read the version in the question. Calibri 11 is the usual exam answer.

### Other Home-tab tools
- **Bullets** mark a list with dots. **Numbering** counts the items. Both sit in the Paragraph group.
- **Find** is Ctrl+F. **Replace** is Ctrl+H. **Go To** is Ctrl+G.
- **Select All** is Ctrl+A. Copy is Ctrl+C. Cut is Ctrl+X. Paste is Ctrl+V.
- **Shading** colours the background of a paragraph. **Borders** draw lines around it.
- **Styles** save a full set of formats under one name, such as Heading 1 or Normal.
- **Drop cap** makes the first letter of a paragraph large. It is on the Insert tab.
- **Clear All Formatting** removes every format from the selected text.
""",
    tricks=[
        trick("Alignment letters",
              "Each shortcut letter starts the word: Left is Ctrl+L, Right is Ctrl+R, Justify is Ctrl+J. Centre breaks the pattern and uses E, because Ctrl+C is Copy."),
        trick("Spacing numbers",
              "The number in the shortcut is the spacing: Ctrl+1 is single, Ctrl+2 is double. Ctrl+5 is the odd one and means 1.5.",
              "Which shortcut gives 1.5 line spacing in MS Word?",
              ["Ctrl+1 is single spacing.", "Ctrl+2 is double spacing.", "The middle value uses Ctrl+5."],
              "Ctrl+5"),
        trick("Case cycle",
              "Press Shift+F3 again and again on selected text. Word cycles through the case styles. No menu is needed."),
    ],
    mistakes=[
        mis("Using Ctrl+C to centre text.", "Ctrl+C is Copy. Centre is Ctrl+E."),
        mis("Using Ctrl+5 for double spacing.", "Ctrl+2 is double. Ctrl+5 is 1.5."),
        mis("Writing superscript as Ctrl+=.", "Ctrl+= is subscript. Superscript is Ctrl+Shift+=."),
        mis("Mixing up Ctrl+H and Ctrl+K.", "Ctrl+H is Replace. Ctrl+K is Hyperlink."),
        mis("Saying landscape is the default orientation.", "Portrait is the default. Landscape is a manual choice on the Layout tab."),
    ],
    revision=[
        "Ctrl+B, I, U are bold, italic, underline. Ctrl+= is subscript. Ctrl+Shift+= is superscript.",
        "Shift+F3 changes case. Ctrl+L, E, R, J are left, centre, right, justify.",
        "Ctrl+1, Ctrl+5, Ctrl+2 are single, 1.5 and double line spacing.",
        "Ctrl+M and Ctrl+Shift+M change the indent. Ctrl+T is a hanging indent. Ctrl+Enter is a page break.",
        "Portrait is the default orientation. Normal margins are 1 inch.",
        "Default font is Calibri 11 (Office 2007 to 2021). Newer Microsoft 365 uses Aptos 12.",
        "Ctrl+H is Replace. Ctrl+K is Hyperlink.",
    ],
    patterns=[
        pat("mw-f1", "Character-formatting shortcuts", "very common",
            "The question asks the key for bold, italic, underline, subscript, superscript or case.",
            ["Bold, italic and underline use their own letters: B, I, U.", "Subscript is Ctrl+=. Superscript adds Shift.",
             "The case cycle is Shift+F3.", "Grow and shrink font use Ctrl+Shift+> and Ctrl+Shift+<."],
            "Each key has one fixed job, so plain recall is enough.",
            "The keyboard shortcut to apply superscript in MS Word is:",
            ["Subscript uses Ctrl+=.", "Superscript needs one extra key, Shift."],
            "Ctrl+Shift+="),
        pat("mw-f2", "Alignment shortcut matching", "very common",
            "The question gives an alignment and asks for the key, or gives a key and asks for the alignment.",
            ["Match the letters: L left, R right, E centre, J justify.", "Left is the default alignment.",
             "Justify makes both edges straight."],
            "Only Centre breaks the first-letter pattern.",
            "Which shortcut justifies the selected paragraph in MS Word?",
            ["Justify means both edges straight.", "Its key is the first letter, J."],
            "Ctrl+J"),
        pat("mw-f3", "Line spacing and paragraph keys", "common",
            "The question asks for single, 1.5 or double spacing, or for a page break.",
            ["Ctrl+1 is single. Ctrl+5 is 1.5. Ctrl+2 is double.", "A page break is Ctrl+Enter.",
             "Bullets and numbering are in the Home tab, Paragraph group."],
            "The spacing keys use the number, with only 5 as the twist.",
            "In MS Word, double line spacing is applied by:",
            ["Double means two lines.", "The key uses the number 2."],
            "Ctrl+2"),
        pat("mw-f4", "Page setup: margins, orientation, size", "common",
            "The question asks for a default of page setup, or which tab holds it.",
            ["Default orientation is portrait.", "Normal margins are 1 inch on all four sides.",
             "Margins, orientation, size and columns are all on the Layout tab."],
            "These defaults are short facts asked in the same words each year.",
            "The default orientation of a page in MS Word is:",
            ["Portrait means height is greater than width.", "Landscape must be chosen by hand."],
            "Portrait"),
        pat("mw-f5", "Default font facts", "common",
            "The question asks for the default font of a Word version.",
            ["Word 2007 to 2021 use Calibri 11 point.", "Newer Microsoft 365 builds use Aptos 12.",
             "Font size is measured in points."],
            "The answer depends on the version named in the question.",
            "The default font of Word 2007 to Word 2019 documents is:",
            ["The version range is 2007 to 2019.", "That range uses Calibri.", "The size is 11 points."],
            "Calibri, 11 point"),
        pat("mw-f6", "Indent, replace and hyperlink keys", "occasional",
            "The question asks for the indent, hanging indent, Replace or Hyperlink key.",
            ["Ctrl+M increases the indent. Ctrl+Shift+M decreases it.", "Ctrl+T makes a hanging indent.",
             "Ctrl+H is Replace. Ctrl+K is Hyperlink."],
            "These keys are less used, so the options pair them with look-alikes.",
            "Which shortcut inserts a hyperlink in MS Word?",
            ["Replace is Ctrl+H.", "Hyperlink uses the K key."],
            "Ctrl+K"),
    ],
)

# =====================================================================
SUBS["mw-tools-mailmerge"] = dict(
    concept=(
        "This subtopic covers four Word tools. **Mail merge** makes many personal letters from one. "
        "The **References** tab builds a table of contents, footnotes and endnotes. "
        "The **Review** tab checks spelling and records changes. **Macros** replay recorded steps."
    ),
    notes=r"""### Mail merge
Mail merge makes many personalised copies of one document. Each receiver gets their own name and address. The body text is typed only once. The tool is on the **Mailings** tab.

Mail merge has **three parts**.

1. **Main document:** the letter, envelope or label with fixed text and empty slots.
2. **Data source:** the list of receivers. It can be an Excel sheet, an Access table or Outlook contacts. Each column holds one detail, such as Name or City.
3. **Merged document:** the final output, with one finished copy per record.

Follow these steps.

1. Write the main document.
2. Connect the data source (Start Mail Merge, Select Recipients).
3. Insert merge fields where details should appear. A field looks like <<Name>>.
4. Preview Results.
5. Finish & Merge. You can print, make a new document or send e-mails.

> **Example:** Admission letters, result letters, certificates, envelopes and address labels are all mail merge jobs.

### References tab
- **Table of Contents (TOC):** an automatic chapter list with page numbers. It is built from **heading styles** (Heading 1, Heading 2). Apply the styles first, then insert the TOC. Press **F9** to update it.
- **Footnote:** a note at the **bottom of the page**. Shortcut: **Ctrl+Alt+F**.
- **Endnote:** a note at the **end of the document**. Shortcut: **Ctrl+Alt+D**.
- **Citations and bibliography:** tools that record sources and build the reference list.

> **Watch:** Text made bold by hand is not a heading style. A TOC cannot find it.

### Review tab
| Tool | Shortcut | Job |
|---|---|---|
| Spelling & Grammar | **F7** | Checks mistakes |
| Thesaurus | **Shift+F7** | Suggests synonyms |
| Word Count | Ctrl+Shift+G | Counts words and characters |
| Track Changes | Ctrl+Shift+E | Marks every edit |
| New Comment | Ctrl+Alt+M | Adds a note on selected text |

Track Changes and Comments let two people edit one file safely. **Compare** shows the differences between two versions.

### Tables and formulas
A table is made of rows and columns of cells. Insert it from the Insert tab. Word tables can calculate. The Formula tool on the Layout tab accepts formulas such as `=SUM(ABOVE)` and `=AVERAGE(LEFT)`.

### Macros
A **macro** is a recorded series of commands. Word replays it with one click or one key. You run macros with **Alt+F8**.

- Macros are useful for repeated jobs.
- A macro-enabled document is saved as **.docm**.
- Macro viruses spread through such files. So Word warns you before it enables macros.

> **Tip:** Open a macro file only if you trust its sender.

### Other tools worth knowing
- **Find** is Ctrl+F. **Replace** is Ctrl+H.
- **Header and footer** text repeats on every page. **Page Number** is on the Insert tab.
- **Watermark** puts faint text behind the page text. It is on the Design tab.
""",
    tricks=[
        trick("No style, no TOC",
              "A table of contents is built from heading styles. If headings are only bolded by hand, the TOC comes out empty."),
        trick("Footnote is F, Endnote is D",
              "Ctrl+Alt+F is Footnote, at the bottom of the page. Ctrl+Alt+D is enDnote, at the end of the document.",
              "Which shortcut inserts an endnote in MS Word?",
              ["Footnote is Ctrl+Alt+F.", "Endnote is the D key."],
              "Ctrl+Alt+D"),
        trick("Merge field marks",
              "Placeholders look like <<Name>>. The data comes from the data source. The layout lives in the main document."),
    ],
    mistakes=[
        mis("Building a TOC from lines made bold by hand.", "Apply Heading 1, Heading 2 styles first, then insert the TOC."),
        mis("Swapping footnote and endnote.", "Footnote is at the bottom of the page. Endnote is at the end of the document."),
        mis("Using Ctrl+Shift+G for the thesaurus.", "Ctrl+Shift+G is Word Count. The thesaurus is Shift+F7."),
        mis("Saying mail merge needs no data source.", "It always needs a main document and a data source."),
        mis("Saving a macro file as .docx.", "Macro-enabled documents use .docm."),
    ],
    revision=[
        "Mail merge parts: main document, data source, merged document. It is on the Mailings tab.",
        "A merge field looks like <<Name>>.",
        "TOC needs heading styles. Update it with F9.",
        "Footnote is Ctrl+Alt+F (page bottom). Endnote is Ctrl+Alt+D (document end).",
        "F7 spelling, Shift+F7 thesaurus, Ctrl+Shift+E Track Changes, Ctrl+Alt+M comment.",
        "A macro is a recorded series of commands. Alt+F8 runs it. Macro files are .docm.",
    ],
    patterns=[
        pat("mw-t1", "Mail-merge components and steps", "very common",
            "One letter must go to many people with a different name each time.",
            ["Name the three parts: main document, data source, merged document.", "Recall the order: write, connect data, insert fields, preview, merge.",
             "Remember that the tool is on the Mailings tab."],
            "The word merge always points to a main document plus a data list.",
            "To send the same offer letter to 300 applicants with each name filled in, the Word feature used is:",
            ["One letter body is needed.", "300 different names come from a list.", "That combination is mail merge."],
            "Mail merge (Mailings tab)"),
        pat("mw-t2", "Footnote vs endnote vs TOC", "very common",
            "The question describes where a note appears, or how a chapter list is made.",
            ["Footnote sits at the page bottom (Ctrl+Alt+F).", "Endnote sits at the document end (Ctrl+Alt+D).",
             "TOC is built from heading styles and refreshed with F9.", "All three are on the References tab."],
            "The two note types differ only in where they print.",
            "In MS Word, a note printed at the bottom of the same page is called a:",
            ["The note is on the same page.", "It is at the bottom.", "Notes at the document end are endnotes."],
            "Footnote"),
        pat("mw-t3", "Review-tab tools and shortcuts", "very common",
            "The question asks for a Review shortcut such as spelling, thesaurus or Track Changes.",
            ["F7 is Spelling and Grammar.", "Shift+F7 is Thesaurus.", "Ctrl+Shift+G is Word Count. Ctrl+Shift+E is Track Changes.",
             "Ctrl+Alt+M adds a comment."],
            "Adding Shift changes the job, so options use near matches.",
            "In MS Word, the Thesaurus opens with which key?",
            ["F7 alone is the spelling check.", "Thesaurus adds Shift to that key."],
            "Shift+F7"),
        pat("mw-t4", "Macro purpose and macro files", "common",
            "The question asks what a macro is, or which extension holds one.",
            ["A macro is a recorded series of commands.", "One click or one key replays it (Alt+F8).",
             "Macro-enabled files carry the letter m: .docm and .dotm."],
            "Macros save time on repeated jobs, and they can also carry viruses.",
            "A macro in MS Word is best described as:",
            ["It is recorded once.", "It replays many commands at one click."],
            "A recorded series of commands replayed with one click or key"),
        pat("mw-t5", "Tables and table formulas", "occasional",
            "The question asks how to add rows and columns, or how a table adds numbers.",
            ["Insert a table from the Insert tab.", "The Formula tool is on the Layout tab.",
             "SUM(ABOVE) adds the cells above. AVERAGE(LEFT) averages the cells on the left."],
            "Word tables support small formulas, and the word inside the brackets gives the direction.",
            "In a Word table, which formula adds all the numbers above the current cell?",
            ["Adding means SUM.", "Numbers above means the direction is ABOVE."],
            "=SUM(ABOVE)"),
    ],
)

# =====================================================================
SUBS["mw-extensions"] = dict(
    concept=(
        "A file extension is the dot and letters at the end of a file name. "
        "**.docx** is the default Word format since 2007. **.doc** is the old 97-2003 format. "
        "The letter **m** means macro and **t** means template. The **X** in the new names stands for XML."
    ),
    notes=r"""### Why extensions matter
Every file name ends in a dot and a few letters. This is the **extension**. It tells Windows which program opens the file and which format holds the data. Exams test the default format, the old format and the special formats.

### The Word extension family
| Extension | Meaning |
|---|---|
| **.docx** | **Default** Word document from **Word 2007 onwards**. Office Open XML format |
| **.doc** | Word **97-2003** format |
| **.docm** | Macro-enabled document |
| **.dotx** | Template |
| **.dotm** | Macro-enabled template |
| **.pdf** | Fixed print-ready file. Word can Export or Save As PDF |
| **.rtf** | Rich Text Format. Keeps simple formatting and opens in many editors |
| **.odt** | OpenDocument Text, used by free office suites |
| **.txt** | Plain text only. No formatting |

### The X rule
From Office **2007**, every Office program moved to **Office Open XML**. The new extensions gained an **X**.

- Word: .doc becomes .doc**x**
- Excel: .xls becomes .xls**x**
- PowerPoint: .ppt becomes .ppt**x**

If two options differ only by the X, the one with X is the modern default. The plain one is the 97-2003 file.

> **Rule:** A last letter **m** means macro-enabled (docm, xlsm, pptm). A last letter **t** in dotx means template.

### Facts about formats
- Word 2003 cannot open .docx directly. Microsoft released a **Compatibility Pack** to help.
- **Save As** (F12) lets you pick a format. The default format can be changed under File, Options, Save.
- **PDF** is the best choice when a document must look the same on every computer and printer.
- **.rtf** and **.odt** open outside Microsoft Office too.
- A template (.dotx) opens as a fresh **untitled copy**. This protects the original design.
- **.txt** loses bold, italic, fonts and pictures. Only characters survive.

### Word defaults in one place
| Setting | Default |
|---|---|
| New file name | Document1 |
| Font | Calibri 11 (2007 to 2021), Aptos 12 (Microsoft 365, from 2023) |
| Alignment | Left |
| Line spacing | 1.08 lines with 8 pt after (Word 2013 onwards) |
| View | Print Layout |
| Orientation | Portrait |
| Paper size | A4 (Letter on US installs) |
| Normal template | Normal.dotm |

> **Tip:** Word 2003 used Times New Roman 12. Calibri 11 is the most asked answer.

### Saving a file
- **Save** is Ctrl+S. The first save asks for a name and a place.
- **Save As** is F12. It makes a copy under a new name or in a new format.
- **AutoSave** and **AutoRecover** keep a backup copy while you work. They help after a power cut.
- A **read-only** file can be opened but not changed under the same name.
- A **password** can be set under File, Info, Protect Document.
""",
    tricks=[
        trick("X means XML, 2007 and later",
              "docx, xlsx and pptx are all 2007 and later. The three-letter doc, xls and ppt are 97-2003. The X stands for XML.",
              "Which extension belongs to an Excel 97-2003 workbook?",
              ["The 2007 and later format has an X.", "The older format has no X."],
              ".xls"),
        trick("Font eras",
              "Word 2003 used Times New Roman 12. Word 2007 to 2021 use Calibri 11. Microsoft 365 from 2023 uses Aptos 12."),
    ],
    mistakes=[
        mis("Saying .doc is the default Word format today.", "The default since Word 2007 is .docx."),
        mis("Thinking a macro document ends in .docx.", "A macro-enabled document ends in .docm."),
        mis("Confusing .dotx with .docm.", "Dotx is a template. Docm is a macro-enabled document."),
        mis("Saving a file as .txt and expecting bold text.", "Plain text keeps only characters."),
        mis("Assuming Word 2003 opens .docx by itself.", "It needs the Compatibility Pack."),
    ],
    revision=[
        "Default: .docx (Word 2007 onwards). Old format: .doc (97-2003).",
        "m means macro: .docm document, .dotm template. .dotx is a plain template.",
        "PDF keeps a fixed layout. .rtf and .odt work outside Office. .txt has no formatting.",
        "The X rule: docx, xlsx and pptx are all 2007+ formats.",
        "Word 2003 opens .docx only with the Compatibility Pack.",
        "A template opens as a fresh untitled copy.",
        "F12 is Save As. Normal template is Normal.dotm. New file name is Document1.",
    ],
    patterns=[
        pat("mw-e1", "Default extension of a Word file", "very common",
            "The question asks for the default or current extension of a Word document.",
            ["The modern default is .docx (Word 2007 onwards).", "The X means Office Open XML.",
             "The old format is .doc (97-2003).", "Use the same X rule for Excel and PowerPoint."],
            "One rule answers Word, Excel and PowerPoint questions.",
            "The default file extension of a Word 2016 document is:",
            ["Word 2016 is newer than 2007.", "So the extension has an X."],
            ".docx"),
        pat("mw-e2", "doc vs docx legacy trap", "very common",
            "The question asks which format the older Word 97-2003 used.",
            ["The X-less name is the older format.", "Older Word could not open .docx without the Compatibility Pack.",
             ".docx files are also smaller because they use XML parts."],
            "The options show doc and docx side by side, and only the X tells them apart.",
            "Which file format was used by Word 97-2003?",
            ["That era is before Office 2007.", "Formats before 2007 have no X."],
            ".doc"),
        pat("mw-e3", "Template and macro extensions", "common",
            "The question gives a description and asks for dotx, dotm or docm.",
            ["Template is .dotx. Macro-enabled document is .docm.", "Macro-enabled template is .dotm.",
             "The letter m means macro. The letter t means template."],
            "Two letters carry all the meaning.",
            "A Word file saved with macros enabled carries which extension?",
            ["The file is a document.", "It also has macros, so the last letter is m."],
            ".docm"),
        pat("mw-e4", "Export and cross-software formats", "common",
            "The question asks for the format that looks the same on every computer, or the plain-text format.",
            ["PDF has a fixed layout and prints the same everywhere.", ".rtf keeps basic formatting and opens in many editors.",
             ".odt is used by free office suites. .txt keeps no formatting.", "Change the format with Save As (F12)."],
            "Each format solves a sharing problem.",
            "Ravi wants his resume to look exactly the same on any computer or printer. He should save it as:",
            ["He needs a fixed layout.", "The fixed-layout format is PDF."],
            "PDF"),
        pat("mw-e5", "Word defaults and Document1", "occasional",
            "The question asks for a default such as the first file name or normal template.",
            ["New file name is Document1.", "Normal template is Normal.dotm.",
             "Default view is Print Layout and orientation is portrait."],
            "Defaults are small facts and are asked in single-line questions.",
            "What is the name of the default template file in MS Word?",
            ["Every new document is based on one template.", "It is the Normal template, and it allows macros."],
            "Normal.dotm"),
    ],
)

apply("ms-word.json", SUBS)
