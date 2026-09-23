# -*- coding: utf-8 -*-
"""Topic 1: computer-fundamentals"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

T = {
  "id": "computer-fundamentals",
  "sectionId": "computer",
  "title": "Computer Fundamentals",
  "order": 1,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 2},
  "summary": "Generations of computers, types, basic organisation (CPU, ALU, CU), pioneers and the abbreviations bank. Two to three guaranteed marks in the Tier-2 Computer Knowledge Test and the base for every other computer topic.",
  "subtopics": [
    {
      "id": "cf-generations",
      "title": "Five generations of computers",
      "concept": """Computers are classified into five generations by the switching technology used.

| Generation | Period | Technology | Examples | Character |
|---|---|---|---|---|
| 1st | 1940-56 | Vacuum tubes | ENIAC, UNIVAC-I, EDVAC | Room-sized, huge heat, machine language |
| 2nd | 1956-63 | Transistors | IBM 1401, IBM 7094 | Smaller, faster, more reliable |
| 3rd | 1964-71 | Integrated Circuits (IC) | IBM 360, PDP-8 | Keyboard/monitor input, OS appeared |
| 4th | 1971-present | Microprocessor (VLSI/ULSI) | Intel 4004, PCs, laptops | CPU on a single chip; personal computing |
| 5th | present & beyond | AI, parallel & quantum processing | Robotics, expert systems | Natural-language and learning machines |

Key firsts: **ENIAC** (Electronic Numerical Integrator And Computer, 1946) was the first general-purpose electronic digital computer, built by J. P. Eckert and John Mauchly. **UNIVAC-I** (1951) was the first commercially available computer. **Intel 4004** (1971) was the first microprocessor. The stored-program (von Neumann) architecture was proposed by John von Neumann for EDVAC.""",
      "formulas": [],
      "tricks": [
        {"title": "Generation ladder mnemonic", "body": "**V**acuum tube -> **T**ransistor -> **I**C -> **M**icroprocessor -> **A**I = \"**V**ery **T**iny **I**Cs **M**ade **A**I\". Five words = five generations, in order.", "example": {"q": "Which technology marks the 3rd generation?", "solution": "Third word = IC (Integrated Circuits)."}},
        {"title": "Firsts trio", "body": "**ENIAC 1946** = first electronic general-purpose computer; **UNIVAC-I 1951** = first *commercial* one; **Intel 4004 1971** = first *microprocessor*. Remember 1946 -> 1951 -> 1971 as \"built, sold, shrunk\".", "example": {"q": "First commercially produced computer?", "solution": "UNIVAC-I (1951), by Eckert-Mauchly. ENIAC was never sold."}}
      ],
      "mistakes": [
        "Choosing 'transistor' for the 3rd generation - transistors are 2nd generation; ICs are 3rd.",
        "Calling UNIVAC the first computer - it was the first *commercial* computer; ENIAC came first.",
        "Marking microprocessor as 3rd generation - microprocessors (Intel 4004) define the 4th."
      ]
    },
    {
      "id": "cf-types",
      "title": "Types of computers",
      "concept": """By size and power:

| Type | Use | Example |
|---|---|---|
| Supercomputer | Scientific simulation, weather, defence | PARAM series (C-DAC, India), Frontier (USA) |
| Mainframe | Bulk transaction processing - banks, railways, census | IBM zSeries |
| Minicomputer | Mid-size firms, multi-user departments | PDP-11 |
| Microcomputer / Personal computer | One user: desktop, laptop, tablet | PCs |
| Workstation | High-end single-user technical work (CAD, design) | Sun/HP workstations |
| Embedded computer | Inside one appliance - washing machine, car ECU, IoT | Microcontrollers |

India's first indigenous supercomputer was **PARAM 8000** (1991), built by **C-DAC** under Vijay Bhatkar. Weather supercomputers **Pratyush** and **Mihir** serve the India Meteorological Department.

By working principle: **Analog** (measures continuous quantities, e.g. speedometer-type devices), **Digital** (counts with 0/1, general purpose), **Hybrid** (both - ICU monitors, petrol pumps).""",
      "formulas": [],
      "tricks": [
        {"title": "Size ladder", "body": "\"**S**ome **M**inisters **M**ust **P**romise **S**peed\" - Supercomputer > Mainframe > Minicomputer > PC (Micro) > Smartphone/embedded, largest to smallest.", "example": {"q": "A bank's central transaction server is which class?", "solution": "Mainframe - designed for massive, reliable bulk transactions."}},
        {"title": "PARAM pin", "body": "PARAM = India's supercomputer series, built by **C-DAC, Pune**; PARAM 8000 came in **1991**. Pair it with 'Vijay Bhatkar = father of Indian supercomputing'.", "example": {"q": "PARAM 8000 was developed by?", "solution": "C-DAC (Centre for Development of Advanced Computing), 1991."}}
      ],
      "mistakes": [
        "Calling a mainframe a supercomputer - mainframes optimise many simultaneous transactions, supercomputers optimise raw calculation speed.",
        "Attributing PARAM to ISRO or BARC - it is a C-DAC product.",
        "Hybrid computers are not 'half hardware-software'; they combine analog measurement with digital processing."
      ]
    },
    {
      "id": "cf-basic-org",
      "title": "Basic organisation: CPU, memory, I/O",
      "concept": """A computer follows the **von Neumann (stored-program) architecture**: instructions and data live in the same memory, and the machine repeatedly fetches and executes them.

**Block diagram:** Input devices -> **CPU** <-> **Memory** -> Output devices, with the system bus (data bus, address bus, control bus) carrying signals on the motherboard.

**CPU (Central Processing Unit)** - the 'brain' - has three parts:

| Part | Job |
|---|---|
| ALU (Arithmetic Logic Unit) | Arithmetic (+, -, x, /) and logic (compare, AND/OR) operations |
| CU (Control Unit) | Directs traffic: fetches, decodes, coordinates all units; does NOT process data itself |
| Registers | Fastest, tiny storage inside CPU (accumulator, program counter, instruction register) |

**Machine cycle** for one instruction: **Fetch -> Decode -> Execute -> Store**. CPU speed is measured in GHz (billions of clock cycles per second). Other board parts: chipset, expansion slots, CMOS battery, ports. **BIOS/UEFI** firmware wakes the hardware at power-on (see software-os topic).""",
      "formulas": [],
      "tricks": [
        {"title": "FDES chant", "body": "\"**F**at **D**ogs **E**at **S**nacks\" = Fetch, Decode, Execute, Store - the machine cycle order. Every instruction, every time.", "example": {"q": "Correct machine-cycle order?", "solution": "Fetch -> Decode -> Execute -> Store."}},
        {"title": "ALU vs CU", "body": "**ALU = Actual Labour Unit** (does the sums); **CU = traffic Constable, Untouched by maths** (only directs). If a question says 'performs calculations' -> ALU; 'coordinates/controls' -> CU.", "example": {"q": "Which CPU part performs comparisons?", "solution": "ALU - comparisons are logic operations."}}
      ],
      "mistakes": [
        "Saying the CU performs arithmetic - it only controls; arithmetic belongs to the ALU.",
        "Reversing Execute and Decode in the machine cycle.",
        "Thinking registers are slower than RAM - registers are the fastest storage in the whole machine."
      ]
    },
    {
      "id": "cf-pioneers-languages",
      "title": "Pioneers and programming-language levels",
      "concept": """| Person | Known as |
|---|---|
| Charles Babbage | Father of the computer (designed the Analytical Engine, 1837) |
| Ada Lovelace | First programmer (notes on the Analytical Engine) |
| Alan Turing | Father of theoretical computer science & AI (Turing machine, Turing test) |
| John von Neumann | Stored-program architecture |
| Tim Berners-Lee | Inventor of the WWW |
| Grace Hopper | COBOL pioneer, coined 'debugging' (moth in Mark II) |
| Blaise Pascal | Early mechanical adder (Pascaline) |
| Gottfried Leibniz | Stepped reckoner (multiply/divide) |

**Language levels:**

| Level | Form | Translated by | Examples |
|---|---|---|---|
| 1GL Machine | 0s and 1s | Needs no translator | CPU instructions |
| 2GL Assembly | Mnemonics (ADD, MOV) | Assembler | 8086 assembly |
| 3GL High-level | English-like | Compiler or interpreter | FORTRAN (1957, first major HLL), COBOL (1959), C, Java, Python |
| 4GL | Declarative, close to results | Built into DBMS/tools | SQL, report generators |
| 5GL | Constraint/AI based | Inference engines | Prolog, Lisp (used in AI) |

**Compiler** converts the whole program to object code in one pass before running (C, C++). **Interpreter** translates and runs line by line (classic Python, JavaScript). **Assembler** converts assembly mnemonics to machine code. HTML is a *markup* language, not a programming language.""",
      "formulas": [],
      "tricks": [
        {"title": "Compiler vs Interpreter", "body": "**C**ompiler = **C**omplete (whole program first, fast execution, shows all errors together); **I**nterpreter = **I**nstant (line by line, stops at first error). C/C++ -> compiler; Python/JS -> interpreter.", "example": {"q": "A language translated line by line, stopping at the first error, uses?", "solution": "An interpreter."}},
        {"title": "Who-does-what chain", "body": "**B**abbage **B**uilt (the idea), **A**da **A**dded (first program), **T**uring **T**hought (theory), **v**on **N**eumann **N**oted (stored program), **B**erners-Lee **B**rowsed (WWW).", "example": {"q": "Father of the computer?", "solution": "Charles Babbage - the Analytical Engine."}}
      ],
      "mistakes": [
        "Calling HTML a programming language - it only structures/markups content.",
        "Saying machine language needs an assembler - assembly (2GL) does; 1GL needs no translation.",
        "Mixing Ada Lovelace (first programmer) with Grace Hopper (COBOL pioneer)."
      ]
    },
    {
      "id": "cf-abbreviations",
      "title": "Core abbreviations and full forms",
      "concept": """High-frequency full forms (learn as a table, SSC asks these directly):

| Short | Full form |
|---|---|
| CPU / ALU / CU | Central Processing Unit / Arithmetic Logic Unit / Control Unit |
| RAM / ROM | Random Access Memory / Read Only Memory |
| PROM / EPROM / EEPROM | Programmable / Erasable Programmable / Electrically Erasable Programmable ROM |
| VDU | Visual Display Unit (monitor) |
| USB | Universal Serial Bus |
| LCD / LED / OLED | Liquid Crystal Display / Light Emitting Diode / Organic LED |
| UPS | Uninterruptible Power Supply |
| BIOS | Basic Input Output System |
| POST | Power-On Self-Test |
| GUI / CLI | Graphical / Command Line Interface |
| OCR / OMR / MICR | Optical Character Recognition / Optical Mark Recognition / Magnetic Ink Character Recognition |
| DPI | Dots Per Inch (printer resolution) |
| AI | Artificial Intelligence |
| PCB | Printed Circuit Board |
| PDA | Personal Digital Assistant |
| CRT | Cathode Ray Tube (old bulky monitor) |
| HDD / SSD | Hard Disk Drive / Solid State Drive |
| CAD | Computer-Aided Design |
| IC / VLSI | Integrated Circuit / Very Large Scale Integration |

Abbreviations for internet/networking (HTTP, URL, ISP...) are collected in the internet-email and networking topics.""",
      "formulas": [],
      "tricks": [
        {"title": "ROM family ladder", "body": "P -> EP -> EEPROM: each generation gets *easier* to erase - PROM (once, at manufacture/programming), EPROM (erase with **UV light**), EEPROM (erase **electrically**, in circuit). \"UV for EPROM, Electricity for EEPROM.\"", "example": {"q": "EPROM is erased using?", "solution": "Ultraviolet light."}},
        {"title": "OCR-OMR-MICR trio", "body": "OCR reads **Characters** (printed text -> editable text), OMR reads **Marks** (exam bubbles), MICR reads **Ink** on **cheques** (banks). Characters, Marks, Ink = CRM.", "example": {"q": "Bank cheque reading uses?", "solution": "MICR (Magnetic Ink Character Recognition)."}}
      ],
      "mistakes": [
        "Expanding UPS as 'Uninterrupted' - the accepted form is **Uninterruptible** Power Supply.",
        "Reading POST as 'Power On System Test' - it is **Power-On Self-Test**.",
        "Confusing DPI (dots per inch, printers) with PPI (pixels per inch, screens)."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Generation-to-technology mapping", "frequency": "very common", "howToSpot": "'Which generation used transistors/ICs/vacuum tubes?' or a statement asking the generation of ENIAC/IBM 1401.", "approach": "Recall the ladder Vacuum tube -> Transistor -> IC -> Microprocessor -> AI and match the technology or the named machine."},
    {"pattern": "Full form / abbreviation recall", "frequency": "very common", "howToSpot": "'What is the full form of BIOS/ALU/MICR?' - plain expansion questions.", "approach": "Use the abbreviation table; eliminate options that expand the letters plausibly but wrongly (e.g. 'Uninterrupted' for UPS)."},
    {"pattern": "Firsts in computing history", "frequency": "common", "howToSpot": "'First commercial computer', 'first microprocessor', 'father of computer'.", "approach": "Keep the trio ENIAC 1946 (first electronic), UNIVAC-I 1951 (first commercial), Intel 4004 1971 (first microprocessor) plus Babbage/Ada/Turing pinned."},
    {"pattern": "CPU part / machine cycle", "frequency": "common", "howToSpot": "'Which unit performs arithmetic?', 'correct order of fetch/decode/execute/store'.", "approach": "ALU calculates, CU controls; cycle is always Fetch -> Decode -> Execute -> Store."},
    {"pattern": "Odd-one-out among translators/types", "frequency": "common", "howToSpot": "'Which is not system software / not an operating system / which is a markup language?'.", "approach": "Classify each option into OS / utility / application / markup before answering."}
  ],
  "solvedExamples": [
    Q("cf-se01",
      "Arrange the computer generations in order of their defining technology:\nA. Integrated Circuits  B. Vacuum Tubes  C. Microprocessor  D. Transistors",
      ["B-A-C-D", "B-D-A-C", "D-B-A-C", "B-A-D-C"], 1,
      "Generation order: 1st vacuum tubes (B) -> 2nd transistors (D) -> 3rd ICs (A) -> 4th microprocessor (C). So the sequence B-D-A-C is correct.",
      "Ladder mnemonic \"Very Tiny ICs Made AI\" - just map the four options onto the ladder; no dates needed.",
      "easy", "cf-generations", "generation-technology mapping", 40),
    Q("cf-se02",
      "Which of the following statements is/are correct?\n1. ENIAC was the first general-purpose electronic digital computer.\n2. UNIVAC-I was the first computer to use vacuum tubes.",
      ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0,
      "Statement 1 is correct - ENIAC (1946) was the first general-purpose electronic digital computer. Statement 2 is wrong: UNIVAC-I (1951) was the first *commercial* computer, and vacuum tubes were the 1st-generation technology used already by ENIAC.",
      "If a statement pairs UNIVAC with 'first', check the exact phrase: 'first commercial' is right, almost anything else ('first computer', 'first vacuum-tube computer') is the trap.",
      "medium", "cf-generations", "statement analysis on computing firsts", 50),
    Q("cf-se03",
      "Which CPU unit coordinates and controls all parts of the computer but does not itself perform calculations?",
      ["ALU", "Control Unit", "Register", "Memory"], 1,
      "The Control Unit directs the flow of data and instructions and coordinates all units; actual arithmetic/logic is done by the ALU. Registers are tiny storage locations, and memory only holds data.",
      "'Coordinates/controls/directs' -> CU; 'calculates/compares' -> ALU. The verbs in the question are the answer.",
      "easy", "cf-basic-org", "CPU part identification", 30),
    Q("cf-se04",
      "In a language translated line by line with execution stopping at the first erroneous line, the translator is a:",
      ["Compiler", "Assembler", "Interpreter", "Linker"], 2,
      "An interpreter converts and executes high-level code one line at a time and halts at the first error. A compiler translates the entire program before execution (reporting all errors together), an assembler handles assembly language, and a linker joins compiled modules.",
      "\"Line by line\" in the question points straight to interpreter; \"whole program at once\" would mean compiler.",
      "easy", "cf-pioneers-languages", "translator identification", 35)
  ],
  "practice": [
    Q("cf-q01",
      "Transistors were used as the basic technology of which generation of computers?",
      ["First", "Second", "Third", "Fourth"], 1,
      "The 2nd generation (1956-63) replaced vacuum tubes with transistors, making computers smaller, faster and more reliable. 1st = vacuum tubes, 3rd = ICs, 4th = microprocessors.",
      "Generation ladder: Vacuum -> Transistor -> IC -> Microprocessor -> AI. Transistor is the 2nd rung.",
      "easy", "cf-generations", "generation-technology mapping", 30),
    Q("cf-q02",
      "ENIAC, completed in 1946, stands for:",
      ["Electronic Numerical Integrator And Computer", "Electrical Numerical Integrated Automatic Calculator", "Electronic Number Integrating and Computing Engine", "Electronic Numerical Index Analyser and Computer"], 0,
      "ENIAC = Electronic Numerical Integrator And Computer, built by Eckert and Mauchly at the University of Pennsylvania.",
      "Trap options all start with 'Electronic/Electrical'; remember the key words 'Numerical Integrator And Computer'.",
      "easy", "cf-generations", "full form recall", 30),
    Q("cf-q03",
      "Which of the following is regarded as the first commercially available computer?",
      ["ENIAC", "EDVAC", "UNIVAC-I", "IBM 360"], 2,
      "UNIVAC-I (1951) was the first computer produced and sold commercially. ENIAC was a one-off military project; EDVAC was a stored-program research machine; IBM 360 is a 3rd-generation family (1964).",
      "UNIVAC = the first computer you could BUY; ENIAC = the first one ever BUILT electronically.",
      "easy", "cf-generations", "computing firsts", 30),
    Q("cf-q04",
      "The Intel 4004, released in 1971, is historically important because it was the first:",
      ["16-bit operating system", "Commercial microprocessor", "Supercomputer", "Graphical user interface"], 1,
      "Intel 4004 (1971) was the world's first commercially available microprocessor - an entire CPU on one chip - and it launched the 4th generation of computers.",
      "4004 = 4th generation's flag-bearer: 'the 4004 started Gen 4'.",
      "medium", "cf-generations", "computing firsts", 35),
    Q("cf-q05",
      "Which of the following areas characterises fifth-generation computers?",
      ["Vacuum tube miniaturisation", "Artificial intelligence and parallel processing", "Batch processing with punched cards", "Assembly-language programming"], 1,
      "The 5th generation targets AI, natural-language processing, parallel and quantum-style computing. Punched cards belong to the pre-1st/1st era, assembly is a 2nd-generation language habit, and vacuum tubes are 1st generation.",
      "Anything with 'intelligence, learning, robotics, parallel' = 5th generation.",
      "easy", "cf-generations", "generation-technology mapping", 30),
    Q("cf-q06",
      "PARAM 8000, India's first indigenous supercomputer (1991), was developed by:",
      ["ISRO", "BARC", "C-DAC", "TCS"], 2,
      "PARAM 8000 was built in 1991 by C-DAC (Centre for Development of Advanced Computing), Pune, under Dr Vijay Bhatkar, after the USA denied Cray supercomputer imports.",
      "PARAM always pairs with C-DAC; the denial story (' PARAM = Perform Anvaya Reusable Module') is extra trivia - the developer is what SSC asks.",
      "medium", "cf-types", "Indian computing milestones", 35),
    Q("cf-q07",
      "Banks handling lakhs of cheque and transaction records centrally typically deploy:",
      ["Microcontrollers", "Mainframe computers", "Analog computers", "Wearable computers"], 1,
      "Mainframes (e.g. IBM zSeries) are built for very high-volume, reliable, simultaneous transaction processing - exactly banking, railways and census workloads.",
      "Bulk transactions -> mainframe; raw scientific speed -> supercomputer; one appliance control -> embedded/microcontroller.",
      "medium", "cf-types", "computer type classification", 35),
    Q("cf-q08",
      "A device that measures continuous physical quantities like temperature or pressure and outputs a voltage-based result is classified as:",
      ["Digital computer", "Hybrid computer", "Analog computer", "Quantum computer"], 2,
      "Analog computers work on continuous signals (voltage, speed, temperature) rather than discrete 0/1 digits. Hybrid machines combine analog measurement with digital processing; quantum computers use qubits.",
      "'Continuous quantities' is the keyword for analog; 'counts with digits 0/1' means digital.",
      "medium", "cf-types", "working-principle classification", 40),
    Q("cf-q09",
      "Which part of the CPU performs subtraction and comparison operations?",
      ["Control Unit", "Arithmetic Logic Unit", "Program counter", "Cache memory"], 1,
      "Arithmetic (add, subtract) and logical (compare, AND/OR) operations are executed in the ALU. The program counter is a register holding the next instruction's address; the CU only coordinates.",
      "Any verb like add/subtract/compare/AND-OR -> ALU, no matter how the question dresses it up.",
      "easy", "cf-basic-org", "CPU part identification", 30),
    Q("cf-q10",
      "The correct sequence of steps in a single machine cycle is:",
      ["Decode, Fetch, Execute, Store", "Fetch, Execute, Decode, Store", "Fetch, Decode, Execute, Store", "Execute, Store, Fetch, Decode"], 2,
      "The CPU first Fetches the instruction from memory, Decodes it in the control unit, Executes it in the ALU, and Stores the result.",
      "Fat Dogs Eat Snacks: Fetch -> Decode -> Execute -> Store. Any option starting with Decode/Execute is out.",
      "easy", "cf-basic-org", "machine-cycle ordering", 30),
    Q("cf-q11",
      "Assembly language mnemonics such as ADD and MOV are converted into machine code by a(n):",
      ["Compiler", "Interpreter", "Assembler", "Preprocessor"], 2,
      "An assembler translates assembly (2GL) mnemonics into machine language. Compilers/interpreters work on high-level (3GL) languages; preprocessors transform source text before compilation.",
      "Assembly -> Assembler (same first letters); high-level -> compiler/interpreter.",
      "easy", "cf-pioneers-languages", "translator identification", 30),
    Q("cf-q12",
      "Which of the following is a markup language rather than a programming language?",
      ["Python", "C++", "HTML", "Java"], 2,
      "HTML (HyperText Markup Language) only structures and presents content using tags; it has no logic/control-flow constructs of its own, so it is a markup language. Python, C++ and Java are programming languages.",
      "Markup = tags for layout (HTML, XML, Markdown). If the option 'structures web pages', it is not a programming language.",
      "easy", "cf-pioneers-languages", "markup vs programming language", 30),
    Q("cf-q13",
      "Who is known as the first computer programmer for her notes on the Analytical Engine?",
      ["Grace Hopper", "Ada Lovelace", "Jean Bartik", "Hedy Lamarr"], 1,
      "Ada Lovelace wrote the first published algorithm intended for Charles Babbage's Analytical Engine, making her the first programmer. Grace Hopper pioneered COBOL and coined 'debugging'.",
      "Ada = first program (on paper); Hopper = COBOL + debugging. Don't swap them.",
      "easy", "cf-pioneers-languages", "pioneers recall", 30),
    Q("cf-q14",
      "The full form of POST, the diagnostic routine that runs when a computer is switched on, is:",
      ["Power-On Self-Test", "Primary Operating System Task", "Power-On System Trial", "Program of System Testing"], 0,
      "POST = Power-On Self-Test: the BIOS/UEFI checks RAM, keyboard, disk controllers etc. before handing over to the boot loader. A failed POST usually beeps.",
      "'Self-Test' is the giveaway - any option without 'Self-Test' is wrong.",
      "easy", "cf-abbreviations", "full form recall", 30)
  ]
}

validate_and_dump_topic(T)
