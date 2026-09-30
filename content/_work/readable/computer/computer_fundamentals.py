"""Readable rewrite of Computer > Computer Fundamentals (all 5 subtopics).

Plain English, tables for facts, one method per question type.
Every fact comes from the existing lesson notes. Old pattern ids are kept; new ids continue each prefix.
Run: python computer_fundamentals.py  (patches content/core/topics/computer/computer-fundamentals.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "computer" / "computer-fundamentals.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Generations
# =====================================================================
SUBS["cf-generations"] = dict(
    concept=(
        "Computers are grouped into five **generations**. Each generation is named after the switching part "
        "at the heart of the machine. The order is vacuum tube, transistor, integrated circuit (IC), microprocessor, "
        "then artificial intelligence. Learn this ladder once and most questions answer themselves."
    ),
    notes=r"""### What a generation means
A **generation** is one stage in the history of computers. Each stage is named after its **switching part**. This part works like tiny on/off switches inside the machine.

When the switching part changed, computers became smaller, faster, cheaper and cooler. Exams ask which technology, which machine or which feature belongs to which generation.

| Generation | Period | Core technology | Example machines |
|---|---|---|---|
| First | 1940-1956 | **Vacuum tubes** | ENIAC, EDVAC, EDSAC, UNIVAC-I, IBM 701 |
| Second | 1956-1963 | **Transistors** | IBM 1401, IBM 7094 |
| Third | 1964-1971 | **Integrated Circuits (ICs)** | IBM 360, PDP-8 |
| Fourth | 1971-present | **Microprocessor** (VLSI/ULSI) | Intel 4004, IBM PC (1981) |
| Fifth | present and beyond | **Artificial intelligence** | AI systems, robots |

> **Tip:** Books differ slightly on the years. The technology order never changes, so answer by technology.

### What each technology was
- **Vacuum tube:** a sealed glass bulb that controls electric current. ENIAC used about **18,000 tubes**. It filled a room and gave off huge heat.
- **Transistor:** a tiny solid switch invented in **1947 at Bell Laboratories** by Bardeen, Brattain and Shockley. It was smaller, cheaper and more reliable than a tube.
- **Integrated Circuit (IC):** many transistors printed together on one silicon **chip**. Jack Kilby made it in 1958.
- **Microprocessor:** the whole CPU on **one chip**. **Intel 4004 (1971)** was the first commercial microprocessor.
- **Fifth generation:** still growing. Its ideas are artificial intelligence, parallel processing, natural-language input, robotics and quantum research.

### Features of each generation
| Generation | What marks it |
|---|---|
| First | Magnetic drums. Only **machine language** (0s and 1s). Programs fed by plugs and switches |
| Second | **Magnetic core memory**. Assembly language and first high-level languages (FORTRAN, COBOL) |
| Third | Keyboard and monitor. **Operating systems** appeared. Many users could share one machine |
| Fourth | Semiconductor RAM. **GUI**, personal computers, networks |
| Fifth | AI, parallel processing, natural-language and voice input, robotics |

> **Rule:** Each generation brought one big software jump. Second got high-level languages. Third got operating systems. Fourth got the GUI.

### Firsts that exams repeat
Read the exact word in the question. Each word points to a different machine.

| Word in the question | Machine |
|---|---|
| First **electronic digital** computer | **ABC** (Atanasoff-Berry Computer, 1942). It was special-purpose |
| First **general-purpose electronic** computer | **ENIAC** (1946), by J. P. Eckert and John Mauchly |
| First **stored-program** computer (practical) | **EDSAC** (1949, Cambridge) |
| First **commercial** computer | **UNIVAC-I** (1951) |
| First **microprocessor** | **Intel 4004** (1971) |

ENIAC stands for Electronic Numerical Integrator And Computer. John von Neumann proposed the stored-program design for EDVAC.

> **Watch:** ENIAC came before UNIVAC-I, but ENIAC was never sold. So "first commercial" is UNIVAC-I.
""",
    tricks=[
        {"title": "Generation ladder mnemonic",
         "body": "Vacuum tube, Transistor, IC, Microprocessor, AI. Read the first letters as \"Very Tiny ICs Made AI\". Five words match five generations in order.",
         "example": {"q": "Which technology marks the third generation?",
                     "steps": ["Count along the ladder: tube, transistor, IC.", "The third word is IC."],
                     "answer": "Integrated Circuits (IC)"}},
        {"title": "Firsts trio",
         "body": "ENIAC 1946 was built. UNIVAC-I 1951 was sold. Intel 4004 1971 shrank the CPU onto a chip. Remember 1946, 1951, 1971.",
         "example": {"q": "Which was the first commercially available computer?",
                     "steps": ["The word is commercial, so look for the machine that was sold.", "ENIAC was never sold."],
                     "answer": "UNIVAC-I (1951)"}},
    ],
    mistakes=[
        mis("Choosing transistor for the third generation.", "Transistors are second generation. ICs are third."),
        mis("Calling UNIVAC-I the first computer.", "UNIVAC-I was the first commercial computer. ENIAC came earlier."),
        mis("Placing the microprocessor in the third generation.", "The microprocessor (Intel 4004) opens the fourth generation."),
        mis("Learning exact years and forgetting the technology.", "Years differ between books. The technology order never changes."),
        mis("Treating ABC and ENIAC as the same first.", "ABC is the first electronic digital computer. ENIAC is the first general-purpose electronic one."),
    ],
    revision=[
        "Ladder: Vacuum tube, Transistor, IC, Microprocessor, AI.",
        "First: machine language, huge heat. Second: transistor, core memory, assembly, FORTRAN, COBOL.",
        "Third: IC, operating system, keyboard, monitor. Fourth: microprocessor, PC, GUI. Fifth: AI.",
        "Transistor 1947 (Bell Labs). IC 1958 (Kilby). Intel 4004 1971.",
        "ABC first electronic digital. ENIAC first general-purpose. EDSAC first stored-program. UNIVAC-I first commercial.",
        "Answer generation questions by technology, not by exact years.",
    ],
    patterns=[
        pat("cf-gen-p1", "Generation and core technology", "very common",
            "The question names a technology (vacuum tube, transistor, IC, microprocessor, VLSI) and asks the generation. Or it gives a generation and asks the technology.",
            ["Write the ladder: tube, transistor, IC, microprocessor, AI.", "Number the rungs 1 to 5.", "Match the option to its rung.", "Watch the pairs: transistor is 2nd, IC is 3rd."],
            "Each generation is defined by exactly one switching technology.",
            "Which technology was the basic switching part of third-generation computers?",
            ["Ladder: tube (1st), transistor (2nd), IC (3rd).", "Kilby's ICs put many transistors on one silicon chip."],
            "Integrated Circuits (ICs)"),
        pat("cf-gen-p2", "Famous machine and its generation", "common",
            "A named machine such as ENIAC, UNIVAC-I, IBM 1401, IBM 360 or Intel 4004 is given. The question asks its generation or role.",
            ["Recall the table row that holds the machine.", "ENIAC, EDVAC, UNIVAC-I: first generation.", "IBM 1401, IBM 7094: second. IBM 360, PDP-8: third.", "Match by the technology inside, not by the year."],
            "Every machine belongs to the generation of its switching part.",
            "The IBM 1401, a business computer of the late 1950s, belongs to which generation?",
            ["The IBM 1401 is in the second-generation row.", "Second generation used transistors."],
            "Second generation"),
        pat("cf-gen-p3", "'First' in computing history", "very common",
            "Words such as first commercial, first electronic, first microprocessor or first stored-program appear with machine names as options.",
            ["Underline the exact adjective in the question.", "Electronic digital: ABC. General-purpose electronic: ENIAC.", "Stored-program: EDSAC. Commercial: UNIVAC-I. Microprocessor: Intel 4004.", "Cross out famous machines that fit a different adjective."],
            "One adjective points to one machine. A different adjective points to another.",
            "Which machine is regarded as the first commercial computer?",
            ["The key word is commercial.", "UNIVAC-I (1951) was sold to businesses. ENIAC (1946) was not sold."],
            "UNIVAC-I"),
        pat("cf-gen-p4", "Generation features and statements", "common",
            "A statement question asks about heat, size, machine or assembly language, operating systems, GUI or the fifth generation.",
            ["Name the generation the statement talks about.", "Read that generation's row in the features table.", "Test each option against the row.", "Pick the option that matches exactly."],
            "Each generation has a few fixed features, so every statement can be checked.",
            "Second-generation computers moved away from pure machine language mainly to which languages?",
            ["Second generation added assembly language.", "It also brought early high-level languages FORTRAN and COBOL."],
            "Assembly language and early high-level languages (FORTRAN, COBOL)"),
        pat("cf-gen-p5", "Ordering the generations", "occasional",
            "Four technologies or four generations must be put in time order. Or the question asks which generation came directly after another.",
            ["Write the ladder first.", "Give each option a rung number.", "Read the option letters in rung order."],
            "The ladder is fixed, so ordering is only a matching job.",
            "Arrange in time order: A. Integrated Circuit B. Vacuum tube C. Microprocessor D. Transistor",
            ["Vacuum tube is B (1st).", "Transistor is D (2nd), IC is A (3rd), microprocessor is C (4th)."],
            "B, D, A, C"),
        pat("cf-gen-p6", "Inventions and their years", "common",
            "The question asks who or where the transistor, IC or vacuum-tube machines came from, or asks a year (1947, 1958, 1971).",
            ["Recall the three anchors: transistor 1947, IC 1958, Intel 4004 1971.", "Transistor: Bell Laboratories, Bardeen, Brattain, Shockley.", "IC: Jack Kilby.", "Match the person or place to the invention."],
            "Three dates and three names cover almost every invention question.",
            "The transistor was invented in 1947 at which laboratory?",
            ["Recall the transistor anchor: 1947.", "It was made at Bell Laboratories by Bardeen, Brattain and Shockley."],
            "Bell Laboratories"),
    ],
)

# =====================================================================
# 2. Types of computers
# =====================================================================
SUBS["cf-types"] = dict(
    concept=(
        "Computers are classified in two independent ways. By **size and power**, they run from supercomputer down to "
        "microcomputer. By **working principle**, they are analog, digital or hybrid. Most questions simply ask "
        "which class a use-case belongs to."
    ),
    notes=r"""### Two ways to classify
Exams classify computers in two separate ways.

- **By size and power:** how much work it does and how many users it serves.
- **By working principle:** what kind of data it handles.

Learn both ladders. Then each question is a simple matching job.

### Classification by size and power
| Type | Power and users | Typical use | Example |
|---|---|---|---|
| **Supercomputer** | Fastest machines. One huge problem at a time | Weather, nuclear simulation, space science, defence | PARAM (India), Frontier (USA) |
| **Mainframe** | Very large. **Thousands of users** at once | Bank records, railway reservation, census | IBM zSeries |
| **Minicomputer** | Mid-size. **Tens to hundreds of users** | Departmental billing, small plants, labs | PDP-11 |
| **Microcomputer (PC)** | One user at a time | Desktop, laptop, tablet, smartphone | Any personal computer |

Order from largest to smallest: **S**upercomputer, **M**ainframe, **M**ini, **M**icro. Say "Some Ministers Must Promise".

> **Note:** A **server** is a role, not a size class. It is a computer that serves others on a network. Smartwatches are small special-purpose microcomputers.

### Classification by working principle
| Type | How it works | Everyday picture | Example |
|---|---|---|---|
| **Analog** | **Measures** continuous quantities such as voltage or temperature | A speedometer needle moving smoothly | Temperature gauges |
| **Digital** | **Counts** separate values. Everything is 0 and 1 | Your calculator and laptop | All modern PCs |
| **Hybrid** | Measures (analog part), then computes and shows digits (digital part) | A petrol pump measuring fuel and showing the price | ICU monitors, petrol pumps |

> **Tip:** Measures a smooth quantity means analog. Works on 0 and 1 means digital. Does both means hybrid.

### India's supercomputer story
India could not buy a Cray supercomputer from the USA in the late 1980s. So the government set up **C-DAC** (Centre for Development of Advanced Computing) in Pune in **1988**.

Under **Dr Vijay Bhatkar**, the team built **PARAM 8000** in **1991**. It was India's first indigenous supercomputer. The PARAM series continues today.

**Seymour Cray** of the USA is called the **father of the supercomputer**. Do not confuse him with Bhatkar.

Weather supercomputers **Pratyush** and **Mihir** serve the India Meteorological Department.

### How to pick the class fast
Ask two questions in order. First, how many users? Second, what is the job?

| Clue in the question | Answer |
|---|---|
| Fastest, one huge calculation, weather, defence | Supercomputer |
| Thousands of users, bulk transactions, banks, railways, census | Mainframe |
| A department, tens to hundreds of users | Minicomputer |
| One user: desktop, laptop, tablet | Microcomputer |
| Measures voltage, temperature or speed smoothly | Analog |
| Works only on 0 and 1 | Digital |
| Measures and then shows digits | Hybrid |

> **Example:** A speedometer needle moves smoothly, so it is analog. A calculator counts, so it is digital.
""",
    tricks=[
        {"title": "Size ladder",
         "body": "\"Some Ministers Must Promise\" gives Supercomputer, Mainframe, Minicomputer, Microcomputer. It runs from largest to smallest.",
         "example": {"q": "A bank's central transaction system is which class?",
                     "steps": ["Thousands of users and bulk transactions.", "That fits the mainframe row."],
                     "answer": "Mainframe"}},
        {"title": "PARAM pin",
         "body": "PARAM is India's supercomputer series, built by C-DAC, Pune. PARAM 8000 came in 1991. Pair it with Vijay Bhatkar.",
         "example": {"q": "Who developed PARAM 8000?",
                     "steps": ["PARAM belongs to C-DAC.", "The year is 1991."],
                     "answer": "C-DAC (Centre for Development of Advanced Computing)"}},
    ],
    mistakes=[
        mis("Calling a mainframe a supercomputer.", "Mainframes handle many users and bulk transactions. Supercomputers do one huge calculation fast."),
        mis("Crediting PARAM to ISRO or BARC.", "PARAM is a C-DAC product."),
        mis("Thinking a laptop or tablet is a different class from a PC.", "Desktop, laptop, tablet and smartphone are all microcomputers."),
        mis("Calling a server a size class.", "A server is a role on a network, not a size class."),
        mis("Reading hybrid as half hardware, half software.", "Hybrid means analog measuring plus digital processing."),
    ],
    revision=[
        "Size ladder, largest first: Supercomputer, Mainframe, Minicomputer, Microcomputer.",
        "Banks, railways, census: mainframe. Weather, nuclear: supercomputer. Department: mini. One person: micro.",
        "Analog measures continuous data. Digital counts 0 and 1. Hybrid does both.",
        "Hybrid examples: petrol pump and ICU monitor.",
        "PARAM 8000 (1991), C-DAC Pune, Dr Vijay Bhatkar.",
        "Seymour Cray is the father of the supercomputer.",
    ],
    patterns=[
        pat("cf-typ-p1", "Size and power ladder", "very common",
            "The question asks to arrange supercomputer, mainframe, minicomputer and microcomputer by size. Or it asks which class a desktop or laptop is.",
            ["Write the ladder: Super, Mainframe, Mini, Micro.", "Read the direction: largest first or smallest first.", "Put desktop, laptop, tablet and smartphone under micro.", "For 'between mainframe and micro', pick mini."],
            "The ladder is fixed. Only the direction changes.",
            "Which option shows computer classes in descending order of size and power?",
            ["Descending means largest first.", "Order: Supercomputer, Mainframe, Minicomputer, Microcomputer."],
            "Supercomputer > Mainframe > Minicomputer > Microcomputer"),
        pat("cf-typ-p2", "Analog, digital or hybrid", "common",
            "A device or a working description is given. It measures temperature, works on 0 and 1, or is a petrol pump or ICU monitor.",
            ["Ask what the machine handles.", "Continuous measuring only: analog.", "Counting with 0 and 1 only: digital.", "Measuring plus digital display: hybrid."],
            "The type depends only on the kind of data the machine handles.",
            "A hospital monitor measures a patient's heartbeat (analog) and shows it as digital numbers. It is a -",
            ["Measuring the signal is the analog part.", "Showing digits is the digital part. Both together mean hybrid."],
            "Hybrid computer"),
        pat("cf-typ-p3", "Use-case to computer type", "very common",
            "A workplace is described: bank, railway reservation, census, weather forecast, a department or one home user.",
            ["Bulk transactions for thousands of users: mainframe.", "One giant calculation: supercomputer.", "A department with many users: mini.", "One person: micro."],
            "Each class is built for one kind of workload.",
            "The railway reservation system handles lakhs of ticket transactions for thousands of counters. It is best run on a -",
            ["Many simultaneous transactions and many users.", "That is the mainframe workload."],
            "Mainframe computer"),
        pat("cf-typ-p4", "Indian supercomputing facts", "common",
            "The question asks about PARAM, C-DAC, the year 1991 or the person behind India's first indigenous supercomputer.",
            ["Chain the facts: no Cray for India, then C-DAC (1988), then PARAM 8000 (1991).", "C-DAC is in Pune.", "Bhatkar is linked to PARAM. Cray is the father of the supercomputer."],
            "One short story answers every PARAM question.",
            "Who led the C-DAC team that built PARAM 8000?",
            ["PARAM 8000 was finished in 1991.", "The team leader was Dr Vijay Bhatkar."],
            "Dr Vijay Bhatkar"),
        pat("cf-typ-p5", "Full forms and places in the PARAM story", "occasional",
            "The question asks what C-DAC stands for, where it is based, or which weather machines serve the IMD.",
            ["C-DAC is Centre for Development of Advanced Computing.", "It was set up in Pune in 1988.", "Weather machines for the India Meteorological Department: Pratyush and Mihir."],
            "These are short facts that appear as one-mark questions.",
            "Which pair of supercomputers serves the India Meteorological Department?",
            ["Recall the weather machines.", "They are named Pratyush and Mihir."],
            "Pratyush and Mihir"),
    ],
)

# =====================================================================
# 3. Basic organisation
# =====================================================================
SUBS["cf-basic-org"] = dict(
    concept=(
        "Every computer follows the **von Neumann** (stored-program) plan. Data comes in through input, "
        "the **CPU** processes it, memory and storage hold it, and output shows the result. "
        "The CPU has an ALU, a control unit and registers. It repeats the machine cycle: fetch, decode, execute, store."
    ),
    notes=r"""### The basic block diagram
Every computer, from a desktop to a smartphone, follows one plan.

**Input devices, then the CPU, with Memory and Storage alongside, then Output devices.** The **motherboard** and its **buses** connect them all.

- **Input** brings data in (keyboard, mouse, scanner).
- **Processing** happens inside the **CPU**.
- **Storage** keeps data permanently (hard disk, SSD).
- **Output** shows results (monitor, printer).

This flow is the **IPO cycle**: Input, Process, Output. Storage is the fourth basic function.

### Inside the CPU
| Part | Job | Everyday picture |
|---|---|---|
| **ALU** (Arithmetic Logic Unit) | All arithmetic (+, -, x, /) and logic (compare, AND, OR) | The calculator inside the brain |
| **CU** (Control Unit) | Fetches and decodes instructions, sends signals. **Does no calculation** | The traffic constable |
| **Registers** | Tiny, very fast slots inside the CPU | The clerk's fingertips |

Four registers to know:

- **PC** (Program Counter) holds the address of the *next* instruction.
- **IR** (Instruction Register) holds the instruction being executed.
- **MAR and MDR** (Memory Address and Data Registers) talk to RAM.
- **Accumulator** holds ALU results.

> **Watch:** Registers are the fastest storage in the whole machine. They are faster than RAM.

### The machine cycle
The CPU repeats four steps millions of times each second.

1. **Fetch:** the CU brings the next instruction from memory. Its address comes from the PC.
2. **Decode:** the CU works out what the instruction wants.
3. **Execute:** the ALU or another unit does the work.
4. **Store:** the result is written to memory or a register.

Say "**F**at **D**ogs **E**at **S**nacks". CPU speed is measured in GHz, the billions of clock cycles per second.

### Buses
A **bus** is a set of wires between blocks.

| Bus | What it carries | Direction |
|---|---|---|
| **Data bus** | The data itself | Both ways |
| **Address bus** | Where the data lives | CPU to memory |
| **Control bus** | Command signals (read, write, interrupt) | Control signals |

More data-bus lines move more bits at once. That is what "32-bit" or "64-bit" processor measures.

### The stored-program idea
John von Neumann's idea: keep **instructions and data together in the same memory**. The CPU fetches, decodes and executes them one after another.

To change the program, you change memory. You do not rewire the machine. This separates modern computers from fixed machines.

> **Rule:** Stored program means instructions and data live in one memory.
""",
    tricks=[
        {"title": "FDES chant",
         "body": "\"Fat Dogs Eat Snacks\" gives Fetch, Decode, Execute, Store. This is the order for every instruction.",
         "example": {"q": "What is the correct machine-cycle order?",
                     "steps": ["Say the chant: Fat Dogs Eat Snacks.", "Fetch, Decode, Execute, Store."],
                     "answer": "Fetch, Decode, Execute, Store"}},
        {"title": "ALU or CU",
         "body": "If the question says performs calculations or comparisons, answer ALU. If it says controls or coordinates, answer CU.",
         "example": {"q": "Which CPU part performs comparisons?",
                     "steps": ["Comparing is a logic operation.", "Logic belongs to the ALU."],
                     "answer": "ALU"}},
    ],
    mistakes=[
        mis("Saying the CU does arithmetic.", "The CU only controls. Arithmetic belongs to the ALU."),
        mis("Swapping Execute and Decode.", "Decode comes first, then Execute. Fetch is always first."),
        mis("Thinking registers are slower than RAM.", "Registers are the fastest storage in the machine."),
        mis("Placing RAM or the hard disk inside the CPU.", "The CPU has ALU, CU and registers. Memory and disk are outside."),
        mis("Forgetting storage in the basic functions.", "The four functions are Input, Processing, Output and Storage."),
    ],
    revision=[
        "Flow: Input, Process (CPU), Output, with Memory and Storage alongside.",
        "CPU = ALU (calculates) + CU (controls) + registers (fastest storage).",
        "Machine cycle: Fetch, Decode, Execute, Store.",
        "PC holds the next instruction's address. IR holds the current instruction. Accumulator holds ALU results.",
        "Data bus carries data. Address bus carries location. Control bus carries commands.",
        "Stored program (von Neumann): instructions and data in one memory.",
    ],
    patterns=[
        pat("cf-org-p1", "CPU part and its function", "very common",
            "The question asks which unit does arithmetic, which controls, or where a comparison happens. The options are CPU parts.",
            ["ALU: all arithmetic and logic.", "CU: direction only, no maths.", "Registers: fastest storage inside the CPU.", "Cross out RAM and hard disk. They are outside the CPU."],
            "Each CPU part has one job.",
            "Which part of the CPU performs comparison of two values?",
            ["Comparison is a logic operation.", "Logic operations belong to the ALU."],
            "Arithmetic Logic Unit (ALU)"),
        pat("cf-org-p2", "Machine cycle steps and order", "very common",
            "The question asks for the correct order of fetch, decode, execute and store. Or it asks what happens in one step.",
            ["Recall the chant: Fat Dogs Eat Snacks.", "Fetch: bring from memory. Decode: understand.", "Execute: do the work. Store: write the result.", "Reject options that put Decode before Fetch."],
            "The four steps always run in this fixed order.",
            "In the machine cycle, in which step does the CPU find out what an instruction means?",
            ["Understanding the instruction is decoding.", "Order: Fetch, Decode, Execute, Store."],
            "Decode"),
        pat("cf-org-p3", "Buses and stored-program idea", "common",
            "The question asks which bus carries addresses, data or commands. Or it asks who proposed the stored-program idea.",
            ["Data bus: the data, two ways.", "Address bus: the location, CPU to memory.", "Control bus: command signals.", "Stored program: John von Neumann."],
            "Each bus has one duty, and the stored-program idea has one owner.",
            "Who proposed the stored-program concept, the basis of modern computers?",
            ["The idea keeps instructions and data in the same memory.", "It is credited to John von Neumann."],
            "John von Neumann"),
        pat("cf-org-p4", "IPO cycle and block diagram", "common",
            "The question asks what IPO stands for, or which basic function an action such as saving belongs to.",
            ["IPO is Input, Process, Output.", "Typing: input. Calculating: processing.", "Showing a result: output. Saving for later: storage."],
            "Every action maps to one of four basic functions.",
            "Saving a document on the hard disk belongs to which basic function?",
            ["Saving keeps data for later use.", "That is storage, the fourth basic function."],
            "Storage"),
        pat("cf-org-p5", "Registers by name", "common",
            "The question describes what a register holds: the next instruction address, the current instruction or the ALU result.",
            ["Next instruction address: PC.", "Instruction being executed: IR.", "ALU results: Accumulator.", "Talking to RAM: MAR and MDR."],
            "Each named register holds one kind of value.",
            "Which register holds the address of the next instruction to be fetched?",
            ["The fetch step gets its address from one register.", "That register is the Program Counter."],
            "Program Counter (PC)"),
    ],
)

# =====================================================================
# 4. Pioneers and languages
# =====================================================================
SUBS["cf-pioneers-languages"] = dict(
    concept=(
        "Exams pair a person with one contribution, and a language with one level or use. "
        "Languages run from machine language (0s and 1s) up to AI-style languages. "
        "A compiler translates the whole program at once. An interpreter translates line by line."
    ),
    notes=r"""### The people who built the idea
Learn each pair as one row. No stories are needed.

| Person | Remembered for |
|---|---|
| **Charles Babbage** | Father of the computer. **Analytical Engine** (1837), Difference Engine (1822) |
| **Ada Lovelace** | **First programmer**. Notes and programs for the Analytical Engine |
| **Alan Turing** | Father of theoretical computer science. Turing machine (1936), Turing test (1950) |
| **John von Neumann** | **Stored-program** architecture |
| **Blaise Pascal** | **Pascaline** (1642), an early mechanical adding machine |
| **Gottfried Leibniz** | Stepped Reckoner, which could also multiply |
| **Joseph Jacquard** | **Punched cards** for his weaving loom (1801) |
| **Herman Hollerith** | Punched-card **tabulating machine** for the 1890 US Census. His firm later became IBM |
| **Grace Hopper** | COBOL pioneer. Wrote one of the first **compilers** |
| **Tim Berners-Lee** | Invented the **World Wide Web** |
| **Douglas Engelbart** | Invented the computer **mouse** |
| **Seymour Cray** | Father of the supercomputer |

> **Watch:** Berners-Lee invented the Web, not the Internet. Ada Lovelace was the first programmer. Grace Hopper is the COBOL pioneer.

### Language levels
GL means generation of language. The lower the level, the closer to the machine.

| Level | Name | Looks like | Translator |
|---|---|---|---|
| 1GL | **Machine language** | Only 0s and 1s | None. The CPU reads it directly |
| 2GL | **Assembly language** | Short codes such as ADD, MOV | **Assembler** |
| 3GL | High-level language | FORTRAN, COBOL, C, Java, Python | **Compiler or interpreter** |
| 4GL | Very high level | SQL, report generators | Built into tools |
| 5GL | Constraint or logic based | PROLOG, LISP-style AI work | Inference engines |

> **Rule:** HTML is a markup language, not a programming language. It only structures a page.

### The three translators
| Translator | Input | How it works | Errors |
|---|---|---|---|
| **Assembler** | Assembly language | Turns short codes into machine code | Not asked |
| **Compiler** | Whole high-level program | Translates **all at once**, then runs fast | Shows **all errors together** |
| **Interpreter** | High-level program | Translates and runs **line by line** | **Stops at the first error** |

**C**ompiler means **C**omplete translation first. Interpreter means instant, one line at a time. C and C++ use compilers. Python and JavaScript are interpreted.

### Famous languages and their use
- **FORTRAN** (1957): science and engineering formulas. The name means FORmula TRANslation.
- **COBOL** (1959): business and banking data processing. COmmon Business Oriented Language.
- **BASIC**: a language for beginners.
- **C** (Dennis Ritchie, 1972): system programming.
- **C++** (Bjarne Stroustrup): object-oriented C.
- **Java** (James Gosling): platform-independent, "write once, run anywhere".
- **Python** (Guido van Rossum): simple syntax, data science and AI.
- **SQL**: database queries, a 4GL.

> **Tip:** COBOL starts with CO for Common Business. So COBOL is for business, and FORTRAN is for science.
""",
    tricks=[
        {"title": "Compiler or interpreter",
         "body": "Compiler means Complete first: whole program, fast run, all errors together. Interpreter means Instant: line by line, stops at the first error.",
         "example": {"q": "A language is translated line by line and stops at the first error. What translates it?",
                     "steps": ["Line by line points to one translator.", "Stopping at the first error confirms it."],
                     "answer": "An interpreter"}},
        {"title": "Who did what",
         "body": "Babbage Built the idea. Ada Added the first program. Turing Thought up the theory. Von Neumann Noted the stored program. Berners-Lee Browsed the Web.",
         "example": {"q": "Who is called the father of the computer?",
                     "steps": ["The first name in the chain is Babbage.", "He designed the Analytical Engine."],
                     "answer": "Charles Babbage"}},
    ],
    mistakes=[
        mis("Calling HTML a programming language.", "HTML is markup. It only structures content."),
        mis("Saying machine language needs an assembler.", "Assembly (2GL) needs an assembler. Machine language (1GL) needs no translator."),
        mis("Mixing Ada Lovelace with Grace Hopper.", "Ada Lovelace is the first programmer. Grace Hopper is the COBOL pioneer."),
        mis("Saying Berners-Lee invented the Internet.", "He invented the World Wide Web."),
        mis("Pairing COBOL with science and FORTRAN with business.", "FORTRAN is for science. COBOL is for business."),
    ],
    revision=[
        "Babbage: father of the computer, Analytical Engine. Ada: first programmer. Turing: theory and test. Von Neumann: stored program.",
        "Pascal 1642 Pascaline. Jacquard punched cards. Hollerith census tabulator, later IBM.",
        "Hopper: COBOL and first compiler. Berners-Lee: WWW. Engelbart: mouse. Cray: supercomputer.",
        "1GL machine, 2GL assembly (assembler), 3GL FORTRAN, COBOL, C (compiler or interpreter), 4GL SQL, 5GL AI logic.",
        "Compiler: whole program at once, all errors together. Interpreter: line by line, stops at first error.",
        "HTML is markup, not programming.",
    ],
    patterns=[
        pat("cf-pio-p1", "Pioneer and contribution", "very common",
            "The question asks who is father of the computer, or who invented the mouse, the Web or punched cards. Four names are options.",
            ["Run down the people table.", "Match the contribution to one row.", "Watch the confusions: Ada vs Hopper, Web vs Internet.", "Cross out names that fit a different row."],
            "Each contribution belongs to exactly one name.",
            "Who invented the punched-card tabulating machine used for the 1890 US Census?",
            ["Punched cards and census point to one row.", "That is Herman Hollerith. His firm later became IBM."],
            "Herman Hollerith"),
        pat("cf-pio-p2", "Translator identification", "very common",
            "The question describes how a program is translated: whole program at once, line by line, or short codes to machine code.",
            ["Short codes to machine code: assembler.", "Whole program before running: compiler.", "Line by line: interpreter.", "Use the error clue to confirm."],
            "The translation style tells you the translator.",
            "A program is translated all at once, then runs fast and reports all errors together. The translator is a -",
            ["All at once points to a compiler.", "All errors together confirms it."],
            "Compiler"),
        pat("cf-pio-p3", "Language level and classification", "common",
            "The question asks the level of machine, assembly or SQL, or asks which item is not a programming language.",
            ["Recall the levels: 1GL machine to 5GL AI logic.", "Machine language needs no translator.", "Assembly needs an assembler.", "HTML is the usual odd one out."],
            "Levels are fixed, and HTML is markup.",
            "Which of these is a markup language, not a programming language?",
            ["Markup only structures a page.", "HTML has no logic, loops or conditions."],
            "HTML"),
        pat("cf-pio-p4", "Language and its purpose", "common",
            "The question asks what COBOL, FORTRAN, SQL, Java or Python is mainly used for.",
            ["Science and engineering: FORTRAN.", "Business and banking: COBOL.", "Databases: SQL. System programming: C.", "Java: platform-independent. Python: AI and data science."],
            "Each language has one main use.",
            "FORTRAN, an early high-level language of 1957, was designed mainly for -",
            ["The name means FORmula TRANslation.", "So it serves science and engineering calculations."],
            "Scientific and engineering calculations"),
        pat("cf-pio-p5", "Language creators", "occasional",
            "The question asks who created C, C++, Java or Python.",
            ["C: Dennis Ritchie (1972).", "C++: Bjarne Stroustrup.", "Java: James Gosling.", "Python: Guido van Rossum."],
            "Four names cover all creator questions.",
            "Java was created by -",
            ["Recall the creator list.", "Java goes with James Gosling."],
            "James Gosling"),
        pat("cf-pio-p6", "Early calculating machines", "occasional",
            "The question names the Pascaline, Stepped Reckoner, Analytical Engine or Jacquard loom and asks the inventor or the year.",
            ["Pascaline (1642): Pascal, adds.", "Stepped Reckoner: Leibniz, also multiplies.", "Analytical Engine (1837): Babbage.", "Punched cards on a loom (1801): Jacquard."],
            "Each early machine has one inventor.",
            "The Pascaline, an early mechanical adding machine of 1642, was made by -",
            ["The name gives the clue.", "Pascaline belongs to Blaise Pascal."],
            "Blaise Pascal"),
    ],
)

# =====================================================================
# 5. Abbreviations
# =====================================================================
SUBS["cf-abbreviations"] = dict(
    concept=(
        "Almost every exam has one to three direct full-form questions. There is no logic to apply. "
        "Learn the full forms in families, and read every word of every option. "
        "Wrong options usually change just one word."
    ),
    notes=r"""### Why this subtopic is pure marks
Every exam asks one to three direct full-form questions. You only need to know a table. Learn the table in families, so one wrong word cannot slip past you.

### CPU and system family
| Short | Full form |
|---|---|
| CPU, ALU, CU | Central Processing Unit, Arithmetic Logic Unit, Control Unit |
| BIOS | Basic Input Output System |
| POST | **Power-On Self-Test** |
| UPS | **Uninterruptible** Power Supply |
| USB | Universal Serial Bus |
| GUI, CLI | Graphical User Interface, Command Line Interface |

### Memory family
| Short | Full form |
|---|---|
| RAM, ROM | Random Access Memory, Read Only Memory |
| PROM, EPROM, EEPROM | Programmable, Erasable Programmable, Electrically Erasable Programmable ROM |
| SRAM, DRAM | Static RAM, Dynamic RAM |
| Cache | Fast memory between CPU and RAM. Not an abbreviation |

### Device and media family
| Short | Full form |
|---|---|
| VDU | Visual Display Unit (the monitor) |
| LCD, LED, OLED | Liquid Crystal Display, Light Emitting Diode, Organic LED |
| CRT | Cathode Ray Tube (the old heavy monitor) |
| HDD, SSD | Hard Disk Drive, Solid State Drive |
| CD, DVD | Compact Disc, Digital Versatile Disc |
| OCR, OMR, MICR | Optical Character Recognition, Optical Mark Recognition, Magnetic Ink Character Recognition |
| DPI, PPI | Dots Per Inch (printers), Pixels Per Inch (screens) |
| CAD, PCB, PDA | Computer-Aided Design, Printed Circuit Board, Personal Digital Assistant |
| IC, VLSI | Integrated Circuit, Very Large Scale Integration |

### How wrong options are built
Exams do not ask hard full forms. They give you **plausible wrong ones**.

- UPS as "Uninterrupted". The correct word is **Uninterruptible**.
- POST as "Power On System Test". The correct form is **Power-On Self-Test**.
- VDU as "Video Display Unit". The correct word is **Visual**.
- PPI for printers. Printers use **DPI**. PPI is for screens.

> **Watch:** One wrong adjective decides the answer. Read every word of every option.

### Two hooks that settle many questions
**Reader trio.** OCR reads **C**haracters, such as a scanned page turned into editable text. OMR reads **M**arks, such as bubble answer sheets. MICR reads magnetic **I**nk, such as the code line on a bank cheque.

**ROM ladder.** PROM can be programmed **once**. EPROM is erased with **U**ltraviolet light. EEPROM is erased **electrically**, right in the circuit. Each step makes erasing easier.

> **Tip:** Expand the letters yourself before you look at the options. Then match word by word.
""",
    tricks=[
        {"title": "ROM ladder",
         "body": "PROM, then EPROM, then EEPROM. Each step is easier to erase. UV light for EPROM, Electricity for EEPROM.",
         "example": {"q": "How is an EPROM erased?",
                     "steps": ["The E in EPROM stands for erasable.", "Recall the hook: UV for EPROM."],
                     "answer": "With ultraviolet light"}},
        {"title": "OCR, OMR, MICR trio",
         "body": "OCR reads Characters. OMR reads Marks. MICR reads Ink on cheques. Say Characters, Marks, Ink.",
         "example": {"q": "Which technology reads bank cheques?",
                     "steps": ["Cheques carry magnetic ink.", "Magnetic ink points to MICR."],
                     "answer": "MICR (Magnetic Ink Character Recognition)"}},
    ],
    mistakes=[
        mis("Expanding UPS as Uninterrupted Power Supply.", "The accepted form is Uninterruptible Power Supply."),
        mis("Reading POST as Power On System Test.", "POST is Power-On Self-Test."),
        mis("Expanding VDU as Video Display Unit.", "VDU is Visual Display Unit."),
        mis("Mixing DPI and PPI.", "DPI (dots) is for printers. PPI (pixels) is for screens."),
        mis("Picking an option after reading only its first words.", "Compare every word. One swapped adjective is the trap."),
    ],
    revision=[
        "Know CPU, ALU, CU, BIOS, GUI and USB cold.",
        "UPS is Uninterruptible. POST is Power-On Self-Test. VDU is Visual Display Unit.",
        "ROM ladder: PROM (program once), EPROM (erase with UV light), EEPROM (erase electrically).",
        "OCR reads characters, OMR reads marks, MICR reads magnetic ink on cheques.",
        "DPI is for printers (dots). PPI is for screens (pixels).",
        "SRAM is Static RAM. DRAM is Dynamic RAM. Cache is not an abbreviation.",
    ],
    patterns=[
        pat("cf-abb-p1", "Direct full-form recall", "very common",
            "The question asks the full form of BIOS, ALU, GUI or USB. Four expansions are options.",
            ["Recall the family table the term belongs to.", "Expand the letters yourself first.", "Compare word by word with the options."],
            "Expanding first stops the options from tempting you.",
            "The full form of GUI is -",
            ["G is Graphical, U is User, I is Interface.", "It means windows and icons, not typed commands."],
            "Graphical User Interface"),
        pat("cf-abb-p2", "Plausible wrong expansions", "common",
            "All four options look almost the same. The wrong ones change one word, such as Uninterrupted, Video or Power On System Test.",
            ["Read every word of every option.", "Recall the fixed traps: Uninterruptible, Power-On Self-Test, Visual.", "Trust the table, not the sound of the option."],
            "The setter swaps a single word to test careful reading.",
            "The accepted full form of UPS is -",
            ["Recall the trap word: Uninterruptible.", "A UPS is a battery backup that switches in when mains power fails."],
            "Uninterruptible Power Supply"),
        pat("cf-abb-p3", "Abbreviation and its use", "common",
            "The question gives an abbreviation such as DPI, MICR or VDU and asks its use or device.",
            ["Readers: OCR characters, OMR marks, MICR magnetic ink.", "Resolution: DPI for printers, PPI for screens.", "VDU is the monitor. BIOS starts the machine."],
            "Each abbreviation has one home use.",
            "MICR technology is mainly used in -",
            ["MICR is Magnetic Ink Character Recognition.", "It reads the characters printed on a cheque."],
            "Cheque processing in banks"),
        pat("cf-abb-p4", "Odd one out or wrong pair", "common",
            "The question asks which item is not a memory term, or which pair is wrongly matched.",
            ["Expand each option.", "Memory family: RAM, ROM, PROM, EPROM, EEPROM, SRAM, DRAM, Cache.", "The option outside the family is the answer."],
            "Family tables make the odd item easy to spot.",
            "Which of these is NOT related to memory? RAM, ROM, PROM, RTOS",
            ["RAM, ROM and PROM are memory terms.", "RTOS is Real-Time Operating System, an OS type."],
            "RTOS"),
        pat("cf-abb-p5", "ROM family questions", "common",
            "The question asks how PROM, EPROM or EEPROM is programmed or erased.",
            ["PROM: programmed once.", "EPROM: erased with ultraviolet light.", "EEPROM: erased electrically, in the circuit."],
            "One idea covers all three: each step is easier to erase.",
            "Which memory can be erased electrically without leaving the circuit?",
            ["Erasing by electricity is the last rung.", "That is EEPROM."],
            "EEPROM"),
    ],
)


# ---------------------------------------------------------------------
def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


data = json.loads(TOPIC.read_text(encoding="utf-8"))
assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
for sub in data["subtopics"]:
    new = SUBS[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in new["patterns"]]
    assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
    assert len(new_ids) == len(set(new_ids))
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sub["id"], len(n))
    assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
    for p in new["patterns"]:
        assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:80])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
    sub["formulas"] = sub.get("formulas", [])
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
