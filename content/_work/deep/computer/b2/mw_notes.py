"""MS Word deep notes, one string per subtopic."""

MW_INTERFACE = """### What MS Word is
**MS Word** is a **word processor** — software used to create, edit, format and print text documents such as letters, reports, applications and resumes. It was first released in **1983** and has been part of the **Microsoft Office** suite since Office began. A file made in Word is called a **document**.

### The parts of the Word window
- **Title bar** — the top strip showing the file name and the program name.
- **Quick Access Toolbar (QAT)** — tiny buttons at the very top-left; by default it holds **Save, Undo and Redo**. You can add more buttons.
- **Ribbon** — the wide band of commands below the title bar. Commands sit in **groups** (like Clipboard, Font, Paragraph) inside **tabs**: **File, Home, Insert, Design, Layout, References, Mailings, Review, View**. The small arrow at the bottom-right corner of a group opens that group's full dialog box.
- **File tab (Backstage view)** — clicking File does not show a ribbon; it opens a full-screen menu called the **Backstage view**: New, Open, Save, Save As, Print, Share, Export, Close and **Options** (all settings live here). Document properties and printing are managed here.
- **Work area / page** — the white sheet where you type.
- **Status bar** — the bottom strip. It shows the **page number (Page x of y), the word count**, the proofing/language icon, the **view buttons** and the **zoom slider**. You can right-click it to choose what it shows.
- **Scroll bars and zoom** — Ctrl + mouse scroll zooms in and out; zoom changes only how large the page looks, never the print size.

### The five views of Word (View tab, also on the status bar)
| View | What it is for |
|---|---|
| **Print Layout** | **Default view**; shows the page exactly as it will print |
| **Read Mode** | Full-screen reading; hides most editing tools |
| **Web Layout** | Shows how the text would look as a web page |
| **Outline** | Works with headings; good for restructuring long reports |
| **Draft** | Plain text view; hides pictures, headers and footers to save time |

### Everyday basics exams keep asking
- **Word wrap** — when a line is full, Word moves the next word to a new line by itself. You press **Enter only to end a paragraph**, not at the end of every line.
- **Undo (Ctrl+Z)** cancels your last action and **Redo (Ctrl+Y)** brings it back; both sit on the QAT.
- **Word count** — on the status bar, or Review tab, or Ctrl+Shift+G.
- **Navigation pane** (View tab, or Ctrl+F) finds words and jumps between headings.
- **Templates** — ready-made designs (resume, invoice, calendar) listed under File, New.
- **Help** — F1 opens Word's help.

### Quick revision
- Word = word processor, part of MS Office, first released 1983; document file.
- Ribbon tabs: File, Home, Insert, Design, Layout, References, Mailings, Review, View.
- File tab opens **Backstage view** (New, Open, Print, Options).
- QAT default buttons: Save, Undo (Ctrl+Z), Redo (Ctrl+Y).
- Status bar: page number, word count, zoom; **Print Layout is the default view**.
- Enter ends a paragraph — word wrap ends lines automatically."""

MW_FORMATTING = """### Three levels of formatting
Formatting means changing how text looks. Word formats at three levels: **character** (letters), **paragraph** (whole blocks) and **page** (the whole sheet).

### Character formatting (Home tab, Font group)
| Action | Shortcut |
|---|---|
| **Bold** | Ctrl+B |
| **Italic** | Ctrl+I |
| **Underline** | Ctrl+U |
| **Subscript** (H2O style) | Ctrl+= |
| **Superscript** (x2 style) | Ctrl+Shift+= |
| Grow / shrink font | Ctrl+Shift+> / Ctrl+< |
| Change case cycle | Shift+F3 |

**Shift+F3** cycles selected text through UPPERCASE, lowercase and Capitalise Each Word — a favourite exam shortcut. Other font tools: font face (type style), font size (measured in **points**), colour, **text highlight colour** (marker behind text), **Strikethrough**, and **Format Painter** (copies formatting from one place to another).

### Paragraph formatting (Home tab, Paragraph group)
| Alignment | Shortcut | Look |
|---|---|---|
| Left (default) | Ctrl+L | ragged right edge |
| Centre | Ctrl+E | symmetric |
| Right | Ctrl+R | ragged left edge |
| Justify | Ctrl+J | **both edges straight** |

**Justified** text is aligned on both the left and the right edge — used in newspapers and formal reports. Line spacing shortcuts: **Ctrl+1 = single, Ctrl+5 = 1.5 lines, Ctrl+2 = double**. Other paragraph tools: bullets and numbering (a numbered/ bulleted list starts automatically when a line begins with 1. or *), indentation, borders and shading. A hard **page break** is inserted with **Ctrl+Enter**.

### Page formatting (Layout tab)
- **Margins** — blank space around the text; default (Normal) margins are **1 inch on all four sides**.
- **Orientation** — **Portrait** (taller than wide) is the **default**; **Landscape** turns the page sideways for wide tables.
- **Paper size** — A4 is the common default in India; Legal and Letter are other sizes.
- **Columns** — splits text into newspaper-style columns.
- **Header** (text at the top of every page) and **Footer** (bottom of every page) come from the Insert tab; page numbers are inserted in the footer.

### Default look of a new document
A new document uses the **Calibri** font at **11 points** (Word 2007 to 2021; newer Microsoft 365 builds ship with Aptos 12), left alignment and single spacing. Theme colours and the default style set can be changed from the Design tab.

### Quick revision
- Ctrl+B/I/U bold-italic-underline; Ctrl+= subscript, Ctrl+Shift+= superscript.
- Shift+F3 changes case; Ctrl+L/E/R/J left-centre-right-justify.
- Ctrl+1 / Ctrl+5 / Ctrl+2 = single / 1.5 / double line spacing.
- Portrait is the default orientation; Normal margins = 1 inch.
- Default font Calibri 11 (Office 2007-2021); Ctrl+Enter = page break.
- Ctrl+H is Replace, **Ctrl+K is hyperlink** — the classic trap pair."""

MW_TOOLS_MAILMERGE = """### Mail merge — one letter, many receivers
**Mail merge** creates many personalised copies of one document — each receiver sees their own name and address, but the body text is typed only once. It lives on the **Mailings** tab and has **three components**:

1. **Main document** — the letter (or envelope, label, e-mail) with fixed text and empty slots.
2. **Data source** — the list of receivers: an Excel sheet, an Access table or Outlook contacts, with one column per detail (Name, City, PIN...).
3. **Merged document** — the final output: one finished copy per record.

**Steps:** write the main document, connect the data source (Start Mail Merge, Select Recipients), place **merge fields** (Insert Merge Field — the slot shows as <<Name>>) where each detail should appear, **Preview Results**, then **Finish & Merge** (print, or create a new document, or send e-mails). Classic exam uses: admission letters, result letters, address labels, envelopes, certificates and ID cards.

### References tab — TOC, footnotes and citations
- **Table of Contents (TOC)** — an automatic chapter list with page numbers. It can only be built from **heading styles** (Heading 1, Heading 2...): apply the styles first, then References, Table of Contents. After editing, right-click and **Update Field** (or press **F9**) to refresh page numbers.
- **Footnote** — a small note at the **bottom of the page**; insert with References, Insert Footnote or **Ctrl+Alt+F**.
- **Endnote** — a note collected at the **end of the document (or section)**; **Ctrl+Alt+D**.
- **Citations and bibliography** — References tab tools that record sources of quotes and generate the reference list automatically.

### Review tab — checking and teamwork
| Tool | Shortcut | Work |
|---|---|---|
| Spelling & Grammar | **F7** | checks mistakes |
| Thesaurus | **Shift+F7** | suggests synonyms |
| Word Count dialog | Ctrl+Shift+G | counts pages, words, characters |
| Track Changes | Ctrl+Shift+E | marks every edit for reviewers |
| New Comment | Ctrl+Alt+M | sticky note on selected text |

Track Changes and Comments are how two people edit one file without losing anyone's work. **Compare** shows differences between two versions of a document.

### Macros — record and replay
A **macro** is a **recorded series of commands** that Word replays with one click or shortcut — useful for repeated jobs (a fixed header block, a standard table). You record it (View tab or Developer tab, Record Macro), and Word saves the steps. Macro-enabled documents use the **.docm** extension, and **macro viruses** spread through such files, which is why Word warns before enabling macros.

### Quick revision
- Mail merge = main document + data source + merged output (Mailings tab).
- Merge field placeholder looks like <<Name>>.
- TOC needs **heading styles**; update with F9.
- Footnote = bottom of page (Ctrl+Alt+F); Endnote = end of document (Ctrl+Alt+D).
- F7 spelling, Shift+F7 thesaurus, Ctrl+Shift+E Track Changes, Ctrl+Alt+M comment.
- Macro = recorded command series; macro files are .docm."""

MW_EXTENSIONS = """### Why file extensions matter
Every Word file ends with a **dot + letters** called the **extension**. It tells Windows which program should open the file and which format the data is stored in. Exams test whether you know the default modern format, the old format and the special formats.

### The Word extension family
| Extension | Meaning |
|---|---|
| **.docx** | **Default** Word document from **Word 2007 onwards**; Office Open XML format — the **X stands for XML** |
| **.doc** | Word **97-2003** format (older files still open in new Word) |
| **.docm** | Macro-enabled document (m = macro) |
| **.dotx** | Template — a ready pattern for new documents |
| **.dotm** | Macro-enabled template |
| **.pdf** | Fixed print-ready file; Word can **export or Save As** PDF |
| **.rtf** | Rich Text Format — keeps simple formatting, opens in many editors |
| **.odt** | OpenDocument Text — the format of free office suites |
| **.txt** | Plain text only — no formatting at all |

### The X = XML rule
From Office **2007**, every Office program switched to **Office Open XML** formats, and the new extensions gained an **X**: Word .doc**x**, Excel .xls**x**, PowerPoint .ppt**x**. If the exam shows an option with an X and an identical option without, the X one is the modern default and the plain one is the 97-2003 file. A fourth letter **m** (dotm, xlsm, pptm) always means **macro-enabled**. This one rule answers a whole family of questions across Word, Excel and PowerPoint.

### Facts asked about formats
- A **.docx** file cannot be opened by Word 2003 **natively**, but Microsoft released a **Compatibility Pack** that lets the old Word open the new format.
- **Save As** (F12) is where you pick a different format; the default can be changed in File, Options, Save.
- **PDF** is the format chosen when a document must look identical on every computer and printer — ideal for forms and e-books.
- **.rtf** and **.odt** are cross-program formats: they open outside Microsoft Office too.
- Templates (.dotx) open as an **untitled new copy**, protecting the original design.
- **.txt** loses all bold, italic, fonts and pictures — only characters survive.

### Quick revision
- Default: **.docx** (Word 2007+, X = XML); legacy: .doc (97-2003).
- m = macro: .docm document, .dotm template; .dotx = template.
- Export/Save As **.pdf** for fixed printing; .rtf and .odt are cross-software; .txt = no formatting.
- The X rule: docx/xlsx/pptx are all 2007+ Office Open XML formats.
- Word 2003 opens .docx only with the Compatibility Pack.
- Templates open as a fresh untitled copy."""
