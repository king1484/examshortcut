"""computer-fundamentals deep content — part 2: pioneers-languages, abbreviations."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_pioneers():
    S = Sub("cf-pioneers-languages")
    S.notes = """### The people who built the idea
Exams pair a name with a contribution. Learn the pairs as a table — no stories needed.

| Person | Remembered as / for |
|---|---|
| **Charles Babbage** | Father of the computer; designed the **Analytical Engine** (1837) and the Difference Engine (1822) |
| **Ada Lovelace** | **First programmer** — wrote notes/programs for the Analytical Engine |
| **Alan Turing** | Father of theoretical computer science; Turing machine (1936), Turing test (1950) |
| **John von Neumann** | **Stored-program** architecture |
| **Blaise Pascal** | **Pascaline** (1642), an early mechanical adding machine |
| **Gottfried Leibniz** | Stepped Reckoner — calculator that could also multiply |
| **Joseph Jacquard** | **Punched cards** for his weaving loom (1801) |
| **Herman Hollerith** | Punched-card **tabulating machine** for the 1890 US Census; his firm later became IBM |
| **Grace Hopper** | COBOL pioneer; wrote one of the first **compilers** |
| **Tim Berners-Lee** | Invented the **World Wide Web** (not the Internet) |
| **Douglas Engelbart** | Invented the computer **mouse** |
| **Seymour Cray** | Father of the supercomputer |

### Language levels (GL = Generation of Language)
| Level | Name | Looks like | Needs a translator? |
|---|---|---|---|
| 1GL | **Machine language** | Pure 0s and 1s | No — the CPU reads it directly |
| 2GL | **Assembly language** | Mnemonics: ADD, MOV | Yes — **assembler** |
| 3GL | High-level languages | FORTRAN, COBOL, C, Java, Python | Yes — **compiler / interpreter** |
| 4GL | Very high level | SQL, report generators | Yes |
| 5GL | Constraint/logic based | PROLOG, LISP-style AI work | Yes |

The lower the level, the closer to the machine; the higher, the closer to human language. **HTML is a markup language, not a programming language** — it only structures a page.

### The three translators
| Translator | Input | How it works | Error behaviour |
|---|---|---|---|
| **Assembler** | Assembly language | Converts mnemonics to machine code | — |
| **Compiler** | Whole high-level program | Translates **all at once**, then runs fast | Lists **all errors together** |
| **Interpreter** | High-level program | Translates and runs **line by line** | **Stops at the first error** |

Memory hook: **C**ompiler = **C**omplete translation first; Interpreter = instant, one line at a time (slower to run).

### Famous languages and their use
- **FORTRAN** (1957) — science and engineering formulas (FORmula TRANslation).
- **COBOL** (1959) — business and banking data processing (COmmon Business Oriented Language).
- **BASIC** — beginners' teaching language. **C** (Dennis Ritchie, 1972) — system programming, built UNIX's world.
- **C++** (Bjarne Stroustrup) — object-oriented C. **Java** (James Gosling) — platform-independent ("write once, run anywhere").
- **Python** (Guido van Rossum) — simple syntax, data science and AI. **SQL** — database queries (a 4GL).

### Quick revision
- Babbage = father of computer + Analytical Engine; Ada = first programmer; Turing = theory + AI test; von Neumann = stored program.
- Pascal 1642 Pascaline; Jacquard punched cards (loom); Hollerith punched-card census tabulator → IBM.
- Hopper = COBOL + first compiler; Berners-Lee = WWW; Engelbart = mouse; Cray = supercomputer.
- 1GL machine → 2GL assembly (assembler) → 3GL FORTRAN/COBOL/C (compiler/interpreter) → 4GL SQL → 5GL AI logic.
- Compiler = whole at once + all errors; interpreter = line by line + stops at first error.
- HTML = markup, not programming."""
    S.pattern("cf-pio-p1", "Pioneer ↔ contribution matching", "very common",
        "'Who is called the father of the computer?', 'who invented the mouse/WWW/punched cards?', 'the first programmer was' — a name with four contributors as options.",
        None,
        "1. Run the table top to bottom: Babbage (father, Analytical Engine), Ada (first programmer), Turing (theory/AI), von Neumann (stored program), Hopper (COBOL/compiler), Berners-Lee (WWW), Engelbart (mouse), Hollerith (census tabulator).\n2. Classic confusions: Ada vs Hopper (first programmer vs COBOL pioneer); Berners-Lee invented the WWW, not the Internet.\n3. Eliminate options whose person belongs to a different row you already know.",
        "Who invented the **punched-card tabulating machine** used to process the 1890 United States Census?",
        "**Herman Hollerith** — his tabulating machine read punched cards; his company later merged into **IBM**.")
    S.pattern("cf-pio-p2", "Translator identification (assembler / compiler / interpreter)", "very common",
        "A translation behaviour is described — whole program at once, line by line, mnemonics to machine code — and the translator is asked.",
        None,
        "1. Mnemonics (ADD, MOV) → **assembler**. Whole program translated before running → **compiler**. Line-by-line translate-and-run → **interpreter**.\n2. Error clue: 'shows all errors together' = compiler; 'stops at the first error' = interpreter.\n3. Speed clue: compiled programs run faster; interpreted ones are easier to test.",
        "A program is translated **all at once**, after which it runs fast and reports all errors together. This translator is a —",
        "**Compiler** — it converts the complete high-level program into machine code in one pass. Line-by-line translation with a stop at the first error is an interpreter.")
    S.pattern("cf-pio-p3", "Language level (1GL–5GL) and classification", "common",
        "Which level machine/assembly/SQL belongs to, or 'which is not a programming language' (HTML trap).",
        None,
        "1. Levels: 1GL machine (0/1, no translation) → 2GL assembly (assembler) → 3GL FORTRAN/COBOL/C → 4GL SQL → 5GL AI logic languages.\n2. HTML is a **markup** language — the standard 'odd one out' answer.\n3. Machine language needs **no** translator; assembly needs an assembler (not a compiler).",
        "Which of the following is a **markup** language rather than a programming language?",
        "**HTML** — HyperText Markup Language only structures and formats a page; it contains no logic, loops or conditions.")
    S.pattern("cf-pio-p4", "Language ↔ purpose pairing", "common",
        "'COBOL is mainly used for…', 'FORTRAN was designed for…', 'SQL is used to…' — a language with four uses as options.",
        None,
        "1. Science/engineering formulas → FORTRAN. Business/banking data processing → COBOL. Beginners → BASIC. Databases → SQL. System programming → C.\n2. Java = platform-independent apps; Python = AI/data science with simple syntax.\n3. Swap-traps pair COBOL with science and FORTRAN with business — remember the initials: COBOL = **CO**mmon **B**usiness.",
        "**FORTRAN**, one of the earliest high-level languages (1957), was designed mainly for —",
        "**Scientific and engineering calculations** — the name means FORmula TRANslation. Business data processing belongs to COBOL.")

    S.q("cf-pio-p1", "easy", "Who is known as the **father of the computer** for designing the Analytical Engine?",
        ["Alan Turing", "Charles Babbage", "John von Neumann", "Bill Gates"], "Charles Babbage",
        "**Charles Babbage** designed the Difference Engine (1822) and the **Analytical Engine** (1837), the blueprint of the modern computer — hence the father of the computer.",
        "Babbage Built the idea.", 20)
    S.q("cf-pio-p1", "medium", "The **Pascaline**, an early mechanical adding machine built in 1642, was invented by —",
        ["Gottfried Leibniz", "Blaise Pascal", "Joseph Jacquard", "Howard Aiken"], "Blaise Pascal",
        "**Blaise Pascal** built the Pascaline to help his tax-clerk father add long columns of figures. Leibniz later improved on it with a machine that could also multiply.",
        "Pascaline → Pascal. The computer language Pascal also honours him.", 25)
    S.q("cf-pio-p1", "medium", "Who is called the **father of theoretical computer science**, known for the 1936 'Turing machine' and the 1950 Turing test?",
        ["Alan Turing", "Charles Babbage", "Grace Hopper", "Tim Berners-Lee"], "Alan Turing",
        "**Alan Turing** described the Turing machine (a model of computation) in 1936 and proposed the Turing test for machine intelligence in 1950.",
        "Turing = Theory + Test.", 20)
    S.q("cf-pio-p2", "easy", "Which translator converts **assembly language mnemonics** (ADD, MOV) into machine code?",
        ["Compiler", "Interpreter", "Assembler", "Linker"], "Assembler",
        "An **assembler** translates assembly language (2GL) into machine code. Compilers and interpreters work on high-level languages (3GL).",
        "Assembly → Assembler (both start with A).", 20)
    S.q("cf-pio-p2", "easy", "A translator that processes a high-level program **line by line, stopping at the first error**, is a(n) —",
        ["Compiler", "Interpreter", "Assembler", "Utility"], "Interpreter",
        "An **interpreter** translates and executes one line at a time and stops at the first error — handy for testing. A compiler translates the whole program first.",
        "Interpreter = instant, line-by-line.", 20)
    S.q("cf-pio-p2", "medium", "Which statement about a **compiler** is correct?",
        ["It translates and runs one line at a time", "It translates the entire program before execution and reports all errors together", "It converts assembly mnemonics only", "It is not needed for high-level languages"], "It translates the entire program before execution and reports all errors together",
        "A **compiler** takes the complete source program, produces machine code in one go, and lists **all errors together** — compiled programs then run fast.",
        "Compiler = Complete + all errors at once.", 25)
    S.q("cf-pio-p2", "medium", "Before a program written in **C** can run on a computer, it must first be converted into —",
        ["Assembly language by an assembler", "Machine language by a compiler or interpreter", "HTML by a browser", "Punched cards"], "Machine language by a compiler or interpreter",
        "The CPU executes only **machine language (1GL)**. Every high-level language program (C, Java, Python) must be translated into machine code by a compiler or an interpreter.",
        "CPU's mother tongue = 0s and 1s only.", 25)
    S.q("cf-pio-p3", "medium", "Machine language is called the **first generation (1GL)** of programming languages because it —",
        ["Is the oldest written language", "Consists of 0s and 1s that the CPU executes directly, with no translation", "Was the first to use a compiler", "Runs the fastest on all machines"], "Consists of 0s and 1s that the CPU executes directly, with no translation",
        "**1GL = machine language**: pure binary that the processor understands natively. Assembly (2GL) needs an assembler; high-level languages (3GL) need a compiler or interpreter.",
        "1GL needs no translator at all.", 25)
    S.q("cf-pio-p3", "medium", "**SQL**, used to query databases, is generally classified as a —",
        ["First-generation language", "Second-generation language", "Fourth-generation language", "Markup language"], "Fourth-generation language",
        "**SQL is a 4GL** — very high level, close to plain English ('SELECT … FROM …'). 1GL = machine code, 2GL = assembly, HTML is markup, not a language generation.",
        "SQL speaks almost English → high generation (4GL).", 25)
    S.q("cf-pio-p4", "easy", "**COBOL** is a high-level language designed mainly for —",
        ["Scientific calculations", "Business data processing", "Operating-system kernels", "Web-page styling"], "Business data processing",
        "**COBOL** (COmmon **Business** Oriented Language, 1959) handles bulk business records — banking and insurance still run on it.",
        "COBOL = Common Business.", 20)
    S.q("cf-pio-p4", "medium", "The language chosen for **platform-independent** application development — 'write once, run anywhere' — is —",
        ["FORTRAN", "COBOL", "Java", "Assembly"], "Java",
        "**Java** (James Gosling) compiles to bytecode that runs on any machine with a Java virtual machine — hence 'write once, run anywhere'.",
        "Java = Jugaad-free portability.", 25)
    return S


def build_abbreviations():
    S = Sub("cf-abbreviations")
    S.notes = """### Why this subtopic is pure marks
Every exam asks 1–3 direct full-form questions. There is no logic to apply — only a table to know. Learn them in families so one wrong expansion cannot slip past you.

### CPU and system family
| Short | Full form |
|---|---|
| CPU / ALU / CU | Central Processing Unit / Arithmetic Logic Unit / Control Unit |
| BIOS | Basic Input Output System |
| POST | **Power-On Self-Test** (not 'Power On System Test') |
| UPS | **Uninterruptible** Power Supply (not 'Uninterrupted') |
| USB | Universal Serial Bus |
| GUI | Graphical User Interface |

### Memory family
| Short | Full form |
|---|---|
| RAM / ROM | Random Access Memory / Read Only Memory |
| PROM / EPROM / EEPROM | (Erasable) (Electrically Erasable) Programmable Read Only Memory |
| SRAM / DRAM | Static / Dynamic RAM |
| Cache | Fast memory between CPU and RAM (not an abbreviation) |

### Device and media family
| Short | Full form |
|---|---|
| VDU | Visual Display Unit (the monitor) |
| LCD / LED | Liquid Crystal Display / Light Emitting Diode |
| CRT | Cathode Ray Tube (the old heavy monitors) |
| HDD / SSD | Hard Disk Drive / Solid State Drive |
| CD / DVD | Compact Disc / Digital Versatile Disc |
| OCR / OMR / MICR | Optical Character Recognition / Optical Mark Recognition / Magnetic Ink Character Recognition |
| DPI / PPI | Dots Per Inch (printers) / Pixels Per Inch (screens) |

### How wrong options are built
Exams do not ask tricky full forms — they ask **plausible wrong ones**:
- UPS → 'Uninterrupted' (correct: **Uninterruptible**).
- POST → 'Power On System Test' (correct: **Power-On Self-Test**).
- VDU → 'Video Display Unit' (correct: **Visual** Display Unit).
- PPI for printers (PPI is for screens; printers use **DPI**).
Read every word of every option — one wrong adjective decides the answer.

### Two memory hooks that settle half the family questions
- **Reader trio:** OCR reads **C**haracters (a scanned page becomes editable text), OMR reads **M**arks (bubble answer sheets), MICR reads magnetic **I**nk (the code line at the bottom of bank cheques). C–M–I: Characters, Marks, Ink.
- **ROM ladder:** PROM can be programmed **once**; **EP**ROM is erased with **U**ltraviolet light; **EEP**ROM is erased **electrically**, right in the circuit. Each step makes erasing easier — that single idea answers every PROM/EPROM/EEPROM question.

### A five-second checking habit
1. Expand the letters yourself **before** looking at the options.
2. Match word by word — first noun, then every adjective.
3. If two options differ by one word (Uninterrupted/Uninterruptible), trust the table, not the ear.

### Quick revision
- CPU/ALU/CU, BIOS, GUI, USB — know them cold.
- UPS = Uninterruptible; POST = Power-On Self-Test; VDU = Visual Display Unit.
- ROM ladder: PROM (program once) → EPROM (erase with UV light) → EEPROM (erase electrically).
- OCR = Characters, OMR = Marks, MICR = magnetic **Ink on cheques**.
- DPI = printers (dots); PPI = screens (pixels)."""
    S.pattern("cf-abb-p1", "Direct full-form recall", "very common",
        "'What is the full form of BIOS / ALU / GUI / USB?' — a plain expansion question with four expansions.",
        None,
        "1. Recall the family table the abbreviation belongs to (CPU family, memory family, device family).\n2. Expand letter by letter and compare word by word; do not recognise the option 'as a whole'.\n3. BIOS = Basic Input Output System; GUI = Graphical User Interface; USB = Universal Serial Bus.",
        "The full form of **GUI** is —",
        "**Graphical User Interface** — the windows-icons-menus-pointer style of working, as against typing commands.")
    S.pattern("cf-abb-p2", "Plausible-wrong expansion traps", "common",
        "All four options look almost identical — the wrong ones change one adjective (Uninterrupted/Uninterruptible, Power On System Test/Power-On Self-Test, Video/Visual).",
        None,
        "1. Read every word of each option; the trap is one swapped word.\n2. Fixed traps: UPS = **Uninterruptible** Power Supply; POST = **Power-On Self-Test**; VDU = **Visual** Display Unit.\n3. If two options look nearly right, the longer-worded standard form is usually correct (Uninterruptible, Self-Test).",
        "The accepted full form of **UPS** is —",
        "**Uninterruptible Power Supply** — a battery backup that switches in instantly when mains power fails. 'Uninterrupted' is the planted trap.")
    S.pattern("cf-abb-p3", "Abbreviation ↔ device/domain matching", "common",
        "'DPI measures…', 'MICR is used in…', 'VDU refers to…' — the abbreviation is given with its use or device asked.",
        None,
        "1. Reader trio: OCR = characters (scanned text), OMR = marks (exam bubbles), MICR = magnetic ink (bank cheques).\n2. Resolution pair: DPI = dots per inch → printers; PPI = pixels per inch → screens.\n3. VDU = the monitor; BIOS = firmware chip that starts the machine.",
        "**MICR** technology is used mainly in —",
        "**Cheque processing in banks** — MICR (Magnetic Ink Character Recognition) reads the characters printed at the bottom of a cheque in special magnetic ink.")
    S.pattern("cf-abb-p4", "Odd one out / mismatched pair among abbreviations", "common",
        "'Which is not a memory term?', 'which pair is wrongly matched?' — one option breaks the family.",
        None,
        "1. Test each option's full form against the family table.\n2. Memory family: RAM, ROM, PROM, EPROM, EEPROM, SRAM, DRAM, Cache. Anything else (RTOS, HTTP, GUI) breaks the family.\n3. For mismatched pairs, expand both halves and compare word by word.",
        "Which of the following is **NOT** related to memory?",
        "**RTOS** — Real-Time Operating System, an OS type. RAM, ROM, PROM and DRAM are all memory terms.")

    S.q("cf-abb-p1", "easy", "The full form of **ALU** is —",
        ["Arithmetic Logic Unit", "Applied Logic Unit", "Arithmetic Local Unit", "Array Logic Unit"], "Arithmetic Logic Unit",
        "**ALU = Arithmetic Logic Unit** — the CPU part that does arithmetic and logical operations.",
        "ALU: Arithmetic first, Logic second.", 20)
    S.q("cf-abb-p1", "easy", "The full form of **BIOS** is —",
        ["Basic Input Output System", "Binary Input Output Storage", "Basic Integrated Operating System", "Built In Operating Software"], "Basic Input Output System",
        "**BIOS = Basic Input Output System** — firmware on the motherboard that wakes the hardware and hands over to the operating system.",
        "BIOS says hello to the hardware first.", 20)
    S.q("cf-abb-p1", "easy", "**USB**, the standard connector for pen drives and keyboards, stands for —",
        ["Universal System Bus", "Universal Serial Bus", "United Serial Bus", "Universal Storage Box"], "Universal Serial Bus",
        "**USB = Universal Serial Bus** — sends data as a serial stream, connects almost everything (hence universal), and is hot-swappable.",
        "Serial = one-by-one bits; Universal = fits everything.", 20)
    S.q("cf-abb-p2", "easy", "The correct expansion of **EPROM** is —",
        ["Electrically Programmable Read Only Memory", "Erasable Programmable Read Only Memory", "Electronic Programmable Random Only Memory", "Extended Program Erasable Memory"], "Erasable Programmable Read Only Memory",
        "**EPROM = Erasable Programmable Read Only Memory** — it can be erased by **ultraviolet light** and reprogrammed. The 'Electrically' version is EEPROM.",
        "EP = Erasable Programmable; EEP = Electrically Erasable Programmable.", 20)
    S.q("cf-abb-p2", "medium", "Which expansion of **EEPROM** is correct?",
        ["Extra Erasable Programmable Read Only Memory", "Electrically Erasable Programmable Random Access Memory", "Electrically Erasable Programmable Read Only Memory", "Electronic Erasable Program Execution Memory"], "Electrically Erasable Programmable Read Only Memory",
        "**EEPROM = Electrically Erasable Programmable Read Only Memory** — erased by applying an electrical signal, no UV lamp needed. It is still ROM, not RAM.",
        "E-E = Electrically Erasable; the last word stays ROM.", 25)
    S.q("cf-abb-p2", "easy", "**VDU**, another name for the computer monitor, stands for —",
        ["Video Display Unit", "Visual Display Unit", "Virtual Display Utility", "Viewing Data Unit"], "Visual Display Unit",
        "**VDU = Visual Display Unit** — the screen on which the computer shows output. 'Video' is the planted wrong word.",
        "V = Visual, not Video.", 20)
    S.q("cf-abb-p3", "medium", "**DPI** printed on a printer's specification box measures —",
        ["Dots per inch — printing resolution", "Digits per inch — typing speed", "Data per inch — disk density", "Depth per inch — paper thickness"], "Dots per inch — printing resolution",
        "**DPI = Dots Per Inch**, the number of ink dots a printer places in one inch — higher DPI, sharper print. Screens use PPI (pixels per inch).",
        "Printers spray dots (DPI); screens light pixels (PPI).", 25)
    S.q("cf-abb-p3", "easy", "**OMR**, used to evaluate answer sheets filled with pencil bubbles, stands for —",
        ["Optical Mark Recognition", "Optical Memory Reader", "Online Mark Reading", "Optical Magnetic Reader"], "Optical Mark Recognition",
        "**OMR = Optical Mark Recognition** — the machine detects where marks (bubbles) are placed. OCR reads characters; MICR reads magnetic ink.",
        "OMR = Marks, OCR = Characters, MICR = Ink.", 20)
    S.q("cf-abb-p3", "easy", "The full form of **LCD**, the technology of most laptop screens, is —",
        ["Light Crystal Display", "Liquid Crystal Display", "Liquid Colour Diode", "Low Current Display"], "Liquid Crystal Display",
        "**LCD = Liquid Crystal Display** — crystals twist to block or pass light. LED screens are LCD panels lit by light-emitting diodes.",
        "LCD = Liquid Crystal; LED = Light Emitting Diode.", 20)
    S.q("cf-abb-p4", "medium", "Which pair is **wrongly matched**?",
        ["RAM – Random Access Memory", "ROM – Read Only Memory", "CRT – Cathode Ray Tube", "UPS – Uninterrupted Power Supply"], "UPS – Uninterrupted Power Supply",
        "The accepted form is **Uninterruptible** Power Supply. The other three pairs are standard expansions.",
        "One adjective decides it: Uninterruptible.", 25)
    S.q("cf-abb-p4", "medium", "Which of the following is **NOT** an input or output device term?",
        ["VDU", "OMR", "MICR", "RTOS"], "RTOS",
        "**RTOS = Real-Time Operating System**, an OS type. VDU is an output device (monitor); OMR and MICR are input readers.",
        "Operating-system words are never device words.", 25)
    return S
