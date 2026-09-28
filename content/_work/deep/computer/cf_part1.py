"""computer-fundamentals deep content — part 1: generations, types, basic-org."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_generations():
    S = Sub("cf-generations")
    S.notes = """### Dividing computer history into generations
A **generation** is a stage in the development of computers. Each generation is named after the **switching technology** at the heart of the machine — the part that works like lakhs of tiny on/off switches. When that part changed, computers became smaller, faster, cheaper and cooler. Exams ask three things: which technology belongs to which generation, which famous machine belongs to which generation, and which feature marks a generation.

| Generation | Period | Core technology | Memory / software | Example machines |
|---|---|---|---|---|
| First | 1940–1956 | **Vacuum tubes** | Magnetic drums; **machine language** | ENIAC, EDVAC, EDSAC, UNIVAC-I, IBM 701 |
| Second | 1956–1963 | **Transistors** | Magnetic core memory; assembly + FORTRAN, COBOL | IBM 1401, IBM 7094 |
| Third | 1964–1971 | **Integrated Circuits (ICs)** | Keyboard, monitor; **operating systems** | IBM 360, PDP-8 |
| Fourth | 1971–present | **Microprocessor** (VLSI/ULSI chips) | Semiconductor RAM; GUI, personal computers | Intel 4004, IBM PC (1981) |
| Fifth | present and beyond | **Artificial intelligence** + parallel processing (ULSI) | Natural-language / voice input, robotics | AI systems, robots |

Periods differ slightly from book to book; the **technology order never changes**, so answer by technology.

### What each technology actually was
- **Vacuum tube** — a sealed glass bulb (like the picture tube of an old TV) that controls electric current. ENIAC used about **18,000 tubes**, filled a whole room, produced enormous heat and broke down almost daily. Programs were fed by plugs and switches, so first-generation machines understood only **machine language** (0s and 1s).
- **Transistor** — a tiny solid-state switch invented in **1947 at Bell Laboratories** by Bardeen, Brattain and Shockley. It replaced the tube: smaller, cheaper, far more reliable, less heat. Second-generation machines got **magnetic core memory** and the first high-level languages (FORTRAN, COBOL) with **assembly language** in between.
- **Integrated Circuit (IC)** — many transistors and connections printed together on a single silicon **chip** (Jack Kilby, 1958). Machines became compact and affordable; keyboards, monitors and **operating systems** appeared; the same program could run at once for many users (multiprogramming).
- **Microprocessor** — the entire CPU placed on **one chip**. **Intel 4004 (1971)** was the first commercial microprocessor. Fourth-generation computers use **VLSI/ULSI** (Very/Ultra Large Scale Integration) chips, personal computers, GUI operating systems and networks.
- **Fifth generation** — still growing. The defining ideas are **artificial intelligence**, parallel processing, natural-language input, robotics and quantum research. No fixed "end year" is given.

### Firsts that exams repeat
- **ABC (Atanasoff–Berry Computer, 1942)** — first *electronic digital* computer (special-purpose, could not be reprogrammed).
- **ENIAC (1946)** — first *general-purpose electronic* computer.
- **EDSAC (1949, Cambridge)** — first practical *stored-program* computer.
- **UNIVAC-I (1951)** — first *commercial* computer sold to businesses.
- **Intel 4004 (1971)** — first *commercial microprocessor*.

### Quick revision
- Technology ladder: **Vacuum tube → Transistor → IC → Microprocessor → AI**.
- 1st: machine language, huge heat. 2nd: transistors, core memory, assembly + FORTRAN/COBOL. 3rd: ICs, OS, keyboard/monitor. 4th: microprocessor, PC, GUI. 5th: AI + parallel processing.
- Transistor 1947 (Bell Labs); IC 1958 (Kilby); Intel 4004 1971.
- Firsts: ABC first electronic digital, ENIAC first general-purpose, EDSAC first stored-program, UNIVAC-I first commercial.
- Answer generation questions by technology, not by exact years."""
    S.pattern("cf-gen-p1", "Generation ↔ core technology mapping", "very common",
        "The stem names a technology (vacuum tube, transistor, IC, microprocessor, VLSI) and asks the generation, or gives a generation and asks its technology.",
        None,
        "1. Recall the ladder: vacuum tube (1st) → transistor (2nd) → IC (3rd) → microprocessor/VLSI (4th) → AI (5th).\n2. Trap pairs: transistor belongs to the 2nd generation, ICs to the 3rd; the microprocessor opens the 4th, not the 3rd.\n3. If the option list mixes technologies, remove the ones that are memory or software names (core memory, GUI) — the answer is a switching device.",
        "Which technology was used as the basic switching element of third-generation computers?",
        "**Integrated Circuits (ICs)** — many transistors printed on one silicon chip (Kilby, 1958). Vacuum tubes = 1st, transistors = 2nd, microprocessors = 4th.")
    S.pattern("cf-gen-p2", "Famous machine ↔ generation / milestone", "common",
        "A named machine (ENIAC, UNIVAC-I, IBM 1401, IBM 360, Intel 4004, EDSAC) is given and its generation or historical role is asked.",
        None,
        "1. Pin machines to generations: ENIAC/EDVAC/UNIVAC-I/IBM 701 → 1st; IBM 1401/7094 → 2nd; IBM 360/PDP-8 → 3rd; Intel 4004/IBM PC → 4th.\n2. Pin roles: ENIAC first general-purpose electronic, EDSAC first stored-program, UNIVAC-I first commercial.\n3. Match by technology inside the machine, not by the year alone.",
        "The IBM 1401, a widely used business computer of the late 1950s, belongs to which generation?",
        "**Second generation** — it was transistor-based. First-generation machines were tube-based (ENIAC, UNIVAC-I).")
    S.pattern("cf-gen-p3", "'First' in computing history", "very common",
        "'First commercial computer', 'first electronic computer', 'first microprocessor', 'first stored-program computer' — a superlative with machines as options.",
        None,
        "1. Keep the firsts chain ready: ABC (1942, first electronic digital) → ENIAC (1946, first general-purpose electronic) → EDSAC (1949, first stored-program) → UNIVAC-I (1951, first commercial) → Intel 4004 (1971, first microprocessor).\n2. Read the exact word: 'electronic' (ABC/ENIAC), 'commercial' (UNIVAC-I), 'general-purpose' (ENIAC), 'stored-program' (EDSAC).\n3. Eliminate machines that are famous but not firsts for that word (e.g. EDVAC for 'commercial').",
        "Which machine is regarded as the first commercial computer?",
        "**UNIVAC-I** (1951) — designed by Eckert and Mauchly, sold to businesses. ENIAC (1946) was earlier but experimental, not commercial.")
    S.pattern("cf-gen-p4", "Generation features and software statements", "common",
        "Statement questions: heat and size, machine vs assembly language, appearance of OS/keyboard/GUI, what defines the 5th generation.",
        None,
        "1. 1st: machine language only, huge heat, magnetic drums. 2nd: assembly + early high-level languages, core memory. 3rd: OS, keyboard, monitor, ICs. 4th: VLSI/ULSI, GUI, PCs. 5th: AI, parallel processing, natural language.\n2. For 'which is correct' statements, test each against its generation's table row.\n3. Remember the defining software jump of each generation: 2nd got high-level languages, 3rd got operating systems, 4th got GUI.",
        "Second-generation computers gradually replaced pure machine language mainly with —",
        "**Assembly language and early high-level languages (FORTRAN, COBOL)** — mnemonics like ADD replaced raw 0s and 1s; translators converted them to machine code.")
    S.pattern("cf-gen-p5", "Ordering the generations", "occasional",
        "Arrange four technologies or four generations in chronological order, or ask which generation came directly after another.",
        None,
        "1. Write the ladder first: Vacuum tube → Transistor → IC → Microprocessor → AI.\n2. Map each option letter to its rung, then read the letters in ladder order.\n3. 'Directly followed' questions need only neighbouring rungs — IC (3rd) is followed by the microprocessor (4th).",
        "Arrange in chronological order: A. Integrated Circuit B. Vacuum tube C. Microprocessor D. Transistor",
        "**B, D, A, C** — vacuum tube (1st), transistor (2nd), IC (3rd), microprocessor (4th).")

    S.q("cf-gen-p1", "easy", "Which technology was used in the **first** generation of computers?",
        ["Vacuum tubes", "Transistors", "Integrated Circuits", "Microprocessors"], "Vacuum tubes",
        "First-generation machines (ENIAC, UNIVAC-I, EDVAC) were built around **vacuum tubes**, which made them room-sized, hot and unreliable.",
        "1st = tube, 2nd = transistor, 3rd = IC, 4th = chip-CPU.", 20)
    S.q("cf-gen-p1", "medium", "**Jack Kilby** is associated with the invention of the —",
        ["Transistor", "Integrated Circuit", "Vacuum tube", "Microprocessor"], "Integrated Circuit",
        "**Jack Kilby** built the first **Integrated Circuit** in 1958 at Texas Instruments; Robert Noyce developed the planar version soon after. The transistor (1947) is Bardeen, Brattain and Shockley at Bell Labs.",
        "Kilby = Chip. Transistor = Bell Labs trio (1947).", 25)
    S.q("cf-gen-p2", "easy", "**IBM 360**, a family of computers released in 1964, belongs to which generation?",
        ["First", "Second", "Third", "Fourth"], "Third",
        "**IBM System/360** used **Integrated Circuits** and supported operating systems — the defining technology of the **third generation** (1964–71).",
        "360 → three → third generation.", 20)
    S.q("cf-gen-p2", "medium", "**EDSAC**, built at Cambridge University in 1949, is remembered as the first —",
        ["Commercial computer", "Practical stored-program computer", "Microprocessor-based computer", "Computer with a GUI"], "Practical stored-program computer",
        "**EDSAC** (Electronic Delay Storage Automatic Calculator), built under Maurice Wilkes, ran its first program in **1949** and was the first practical **stored-program** computer — instructions and data lived in the same memory.",
        "EDSAC = 'S' for Storage → stored program.", 25)
    S.q("cf-gen-p3", "easy", "Which machine is regarded as the first **general-purpose electronic digital** computer?",
        ["ENIAC", "UNIVAC-I", "EDSAC", "IBM 1401"], "ENIAC",
        "**ENIAC** (Electronic Numerical Integrator And Computer), completed in 1946, was the first electronic computer that could be reprogrammed for any task — hence general-purpose.",
        "ENIAC 1946 = first electronic general-purpose.", 20)
    S.q("cf-gen-p3", "medium", "The **Atanasoff–Berry Computer (ABC)** of 1942 is honoured in computer history as the —",
        ["First electronic digital computer", "First commercial computer", "First computer with a microprocessor", "First computer with a graphical interface"], "First electronic digital computer",
        "The **ABC**, built by John Atanasoff and Clifford Berry, was the first **electronic digital** computer, though it was special-purpose and never sold. ENIAC (1946) was the first *general-purpose* one.",
        "ABC comes before ENIAC alphabetically and historically.", 25)
    S.q("cf-gen-p3", "easy", "The first **microprocessor**, released by Intel in 1971, was the —",
        ["Intel 8086", "Intel 4004", "Intel 80286", "Intel Pentium"], "Intel 4004",
        "The **Intel 4004** (1971) placed a complete CPU on one chip — the first commercial **microprocessor**, which opened the fourth generation.",
        "4004 = four digits, fourth generation.", 20)
    S.q("cf-gen-p4", "medium", "Which feature is the defining characteristic of **fifth-generation** computers?",
        ["Natural-language processing and parallel processing", "Vacuum-tube circuitry", "Magnetic drum memory", "Batch processing on punched cards"], "Natural-language processing and parallel processing",
        "Fifth-generation work centres on **artificial intelligence**: machines that accept natural language and voice, use parallel processing and ULSI chips, and support robotics. Vacuum tubes, drums and punched cards belong to the first-generation era.",
        "5th gen talks to you — natural language + AI.", 25)
    S.q("cf-gen-p4", "medium", "A key software development that appeared during the **third generation** was the —",
        ["Operating system", "Machine language", "Punched-card interpreter", "Web browser"], "Operating system",
        "With IC-based hardware, third-generation machines ran **operating systems** that managed multiprogramming, and used keyboards and monitors instead of punched cards. Web browsers belong to the 1990s (fourth generation and later).",
        "OS + keyboard + monitor = 3rd generation marks.", 25)
    S.q("cf-gen-p5", "medium", "Arrange the technologies in the order computers used them: A. Microprocessor B. Transistor C. Vacuum tube D. Integrated Circuit",
        ["C, D, B, A", "C, B, D, A", "B, C, A, D", "D, B, C, A"], "C, B, D, A",
        "Ladder order: vacuum tube (1st) → transistor (2nd) → IC (3rd) → microprocessor (4th), i.e. **C, B, D, A**.",
        "V-T-I-M: 'Very Tiny ICs Multiply'.", 25)
    S.q("cf-gen-p5", "easy", "Which generation of computers **directly followed** the integrated-circuit generation?",
        ["Second generation", "Fourth generation", "Fifth generation", "First generation"], "Fourth generation",
        "ICs define the third generation (1964–71); the **fourth generation** (1971 onwards) followed it, built around the **microprocessor**.",
        "IC (3rd) → chip-CPU (4th) → AI (5th).", 20)
    return S


def build_types():
    S = Sub("cf-types")
    S.notes = """### Two ways of classifying computers
Exams classify computers in two independent ways: by **size and power** (how much work, how many users) and by **working principle** (what kind of data it handles). Learn both ladders — most questions are simply "which class does this use-case belong to?"

### Classification by size and power
| Type | Power and users | Typical use | Examples |
|---|---|---|---|
| **Supercomputer** | Fastest machines on earth; one gigantic problem at a time | Weather forecasting, nuclear simulation, space science, defence | PARAM (India), Frontier (USA) |
| **Mainframe** | Very large; **thousands of users** at once; bulk transactions | Bank records, railway reservation, census, insurance | IBM zSeries |
| **Minicomputer** | Mid-size; **tens to hundreds of users**; department-level | Departmental billing, small plants, labs (classic: PDP-11) | PDP-11 |
| **Microcomputer (PC)** | One user at a time | Desktop, laptop, tablet, smartphone | Any personal computer |

Memory hook for descending order: **S**uper → **M**ainframe → **M**ini → **M**icro ("Some Ministers Must Promise").

Two small but asked points: a **server** is a role (a computer that serves others on a network), not a separate size class — it is usually a powerful microcomputer or a mainframe-class machine. **Handheld and wearable** devices (smartwatches) are small special-purpose microcomputers.

### Classification by working principle
| Type | How it works | Everyday picture | Example |
|---|---|---|---|
| **Analog** | **Measures** continuous quantities (voltage, temperature, speed) | A speedometer: the needle moves smoothly | Old slide-rule machines; temperature gauges |
| **Digital** | **Counts** discrete values — everything as 0 and 1 | Your calculator and laptop | All modern PCs |
| **Hybrid** | Measures (analog part) + computes and shows digits (digital part) | A petrol-pump unit that measures fuel flow and prints the rupee price | ICU monitors; petrol pumps |

### India's supercomputer story (a favourite one-mark area)
India could not buy a Cray supercomputer from the USA in the late 1980s, so the government set up **C-DAC** (Centre for Development of Advanced Computing), Pune, in **1988**. Under **Dr Vijay Bhatkar** the team built **PARAM 8000** in **1991** — India's first indigenous supercomputer — which put India among the few countries able to build such machines. The PARAM series continues today.

**Seymour Cray** of the USA is called the **father of the supercomputer**.

### Quick revision
- Size ladder (descending): Supercomputer → Mainframe → Minicomputer → Microcomputer.
- Banks/railways/census = mainframe (thousands of users, bulk data); weather/nuclear = supercomputer; department = mini; personal = micro.
- Analog measures continuous data; digital counts 0/1; hybrid does both (petrol pump, ICU monitor).
- PARAM 8000 (1991), C-DAC Pune, Dr Vijay Bhatkar. Seymour Cray = father of the supercomputer.
- A server is a role on a network, not a size class."""
    S.pattern("cf-typ-p1", "Size/power ladder ordering and classification", "very common",
        "Arrange supercomputer, mainframe, minicomputer, microcomputer by size or power, or pick which class a device (desktop, laptop, tablet) belongs to.",
        None,
        "1. Write the descending ladder: Super → Mainframe → Mini → Micro.\n2. Desktop, laptop, tablet, smartphone, wearable are all microcomputers — 'smaller' does not mean a different class.\n3. For 'which lies between mainframe and micro' questions, the answer is the minicomputer.",
        "Which of the following shows computer classes in DESCENDING order of size and power?",
        "**Supercomputer > Mainframe > Minicomputer > Microcomputer.** A desktop or laptop is a microcomputer, the smallest class listed.")
    S.pattern("cf-typ-p2", "Analog / digital / hybrid classification", "common",
        "A device or a working description (measures temperature, works on 0 and 1, petrol pump, ICU monitor) and the type is asked.",
        None,
        "1. Analog = measures continuous quantities; digital = counts discrete 0/1 values; hybrid = both.\n2. Modern PCs, calculators and phones are digital. Thermometer-like gauges are analog.\n3. Two hybrid classics: the petrol-pump billing unit and hospital ICU monitors — measure continuously, display digits.",
        "A hospital monitor that continuously measures a patient's heartbeat (analog) and shows it as digital numbers is a —",
        "**Hybrid computer** — the analog part measures the continuous signal, the digital part converts and displays it.")
    S.pattern("cf-typ-p3", "Use-case → computer type", "very common",
        "A workplace is described — banks, railways reservation, census (mainframe); weather and defence simulation (super); a single user at home (micro); a university department (mini).",
        None,
        "1. Bulk transactions for thousands of users → mainframe. One enormous calculation → supercomputer. Department-level multi-user → mini. One person → micro.\n2. Watch the wording: 'lakhs of records per day' points to mainframe, 'largest and fastest' points to supercomputer.\n3. Reserve 'minicomputer' for mid-size multi-user departments, not for 'small personal computers'.",
        "The Indian Railways reservation system, which handles lakhs of ticket transactions daily for thousands of counters, is best run on a —",
        "**Mainframe computer** — mainframes optimise very large numbers of simultaneous transactions, which is exactly the reservation-system workload.")
    S.pattern("cf-typ-p4", "Indian supercomputing facts", "common",
        "Questions on PARAM, C-DAC, the year 1991, or the person behind India's first indigenous supercomputer.",
        None,
        "1. Chain the facts: USA refused a Cray → C-DAC set up in Pune (1988) → Dr Vijay Bhatkar's team → PARAM 8000 in 1991.\n2. C-DAC = Centre for Development of Advanced Computing.\n3. Seymour Cray (USA) = father of the supercomputer; do not confuse him with Bhatkar (father of PARAM/Indian supercomputing).",
        "Who led the C-DAC team that built PARAM 8000, India's first indigenous supercomputer?",
        "**Dr Vijay Bhatkar** — C-DAC (Centre for Development of Advanced Computing), Pune, completed PARAM 8000 in 1991.")

    S.q("cf-typ-p1", "easy", "Which of the following is the **correct descending** order of computers by size and processing power?",
        ["Supercomputer, Mainframe, Minicomputer, Microcomputer", "Mainframe, Supercomputer, Microcomputer, Minicomputer", "Microcomputer, Minicomputer, Mainframe, Supercomputer", "Supercomputer, Minicomputer, Mainframe, Microcomputer"], "Supercomputer, Mainframe, Minicomputer, Microcomputer",
        "The ladder is **Super → Mainframe → Mini → Micro**: the supercomputer is the fastest and largest, the personal computer the smallest.",
        "'Some Ministers Must Promise' = Super, Main, Mini, PC.", 20)
    S.q("cf-typ-p1", "medium", "A tablet and a laptop are both examples of —",
        ["Minicomputers", "Mainframe computers", "Microcomputers", "Supercomputers"], "Microcomputers",
        "Every single-user personal device — desktop, laptop, tablet, smartphone — is a **microcomputer**. 'Micro' refers to the class (CPU on microprocessor chips, one user), not to the physical smallness of a tablet.",
        "One user = micro, whatever the shape.", 20)
    S.q("cf-typ-p1", "medium", "A university department provides **many students simultaneous logins** on one mid-sized multi-user machine. This is the classic role of a —",
        ["Supercomputer", "Mainframe", "Minicomputer", "Microcomputer"], "Minicomputer",
        "Mid-size, **multi-user departmental** work (tens to hundreds of users) is the textbook role of a **minicomputer** (classic example: PDP-11). Mainframes serve thousands of users; micros serve one.",
        "Department with dozens of users = mini.", 25)
    S.q("cf-typ-p2", "easy", "Digital computers represent all data using —",
        ["Continuous voltage levels", "The digits 0 and 1", "Needle positions on a dial", "Punched holes only"], "The digits 0 and 1",
        "A **digital** computer converts every input into **discrete binary values (0 and 1)** and computes on them. Continuous quantities are the domain of analog machines.",
        "Digital = 0/1 digits; analog = smooth needle.", 20)
    S.q("cf-typ-p2", "medium", "A petrol-pump unit that **measures the flow of fuel continuously** and then **computes and prints the price in rupees** works on which principle?",
        ["Analog only", "Digital only", "Hybrid", "Neither analog nor digital"], "Hybrid",
        "Measuring the continuous fuel flow is the **analog** part; converting it to a digital rupee amount is the **digital** part. A machine combining both is a **hybrid computer**.",
        "Petrol pump and ICU monitor = the two hybrid classics.", 25)
    S.q("cf-typ-p2", "medium", "Which statement about **analog computers** is correct?",
        ["They work on discrete binary digits", "They measure continuous physical quantities", "They are faster than all digital supercomputers", "They were invented in the fourth generation"], "They measure continuous physical quantities",
        "Analog computers **measure** continuous quantities — temperature, pressure, voltage, speed — and work directly on those signals. They predate digital machines and are not used for general computing today.",
        "Analog = 'a needle that slides', not digits.", 25)
    S.q("cf-typ-p3", "easy", "Long-range **weather forecasting and nuclear simulation** are typical applications of —",
        ["Microcomputers", "Minicomputers", "Mainframe computers", "Supercomputers"], "Supercomputers",
        "One gigantic scientific computation at a time is the supercomputer's job — weather models, nuclear simulations, space and defence research.",
        "Weather + nuclear = supercomputer.", 20)
    S.q("cf-typ-p3", "easy", "A computer kept at home and used by **one student at a time** is a —",
        ["Mainframe computer", "Microcomputer", "Minicomputer", "Supercomputer"], "Microcomputer",
        "Single-user personal machines — desktops and laptops — are **microcomputers** (personal computers).",
        "One user at home = micro.", 20)
    S.q("cf-typ-p3", "medium", "A bank maintains **lakhs of customer accounts** and processes thousands of transactions every minute for many branches at once. The most suitable machine is a —",
        ["Microcomputer", "Minicomputer", "Mainframe computer", "Analog computer"], "Mainframe computer",
        "Very large, simultaneous **bulk transaction processing** for thousands of users is exactly what **mainframes** (e.g. IBM zSeries) are built for.",
        "Banks and railways = mainframe; speed for many users, not one big formula.", 25)
    S.q("cf-typ-p4", "medium", "**PARAM 8000**, delivered in 1991, made India one of the few countries able to build supercomputers. It was developed by —",
        ["ISRO", "BARC", "C-DAC, Pune", "DRDO"], "C-DAC, Pune",
        "**PARAM 8000** (1991) was built by **C-DAC** (Centre for Development of Advanced Computing), Pune, set up in 1988 after the USA refused to sell India a Cray supercomputer.",
        "PARAM = C-DAC, Pune. Not ISRO, not BARC.", 25)
    S.q("cf-typ-p4", "medium", "The full form of **C-DAC**, the centre that built the PARAM series, is —",
        ["Centre for Digital Advanced Computing", "Centre for Development of Advanced Computing", "Computer Development and Applications Centre", "Centre for Defence Analysis and Computing"], "Centre for Development of Advanced Computing",
        "**C-DAC = Centre for Development of Advanced Computing**, an organisation under the Department of Information Technology, headquartered in Pune.",
        "Development, not Digital — the classic trap.", 25)
    S.q("cf-typ-p4", "easy", "Who is known as the **father of the supercomputer**?",
        ["Dr Vijay Bhatkar", "Seymour Cray", "John von Neumann", "Alan Turing"], "Seymour Cray",
        "**Seymour Cray** (USA) designed the Cray series and is called the **father of the supercomputer**. Dr Vijay Bhatkar is honoured as the father of Indian supercomputing (PARAM).",
        "Cray builds Cray — same name.", 20)
    return S


def build_basic_org():
    S = Sub("cf-basic-org")
    S.notes = """### The basic block diagram
Every computer, from a desktop PC to a smartphone, follows the same plan (the **von Neumann** or stored-program design):

**Input devices → CPU (processes) ↔ Memory ↔ Storage → Output devices**, all connected by the **motherboard** and its **buses**.

- **Input** brings data in (keyboard, mouse, scanner).
- **Processing** happens inside the **CPU**.
- **Storage** keeps data permanently (hard disk, SSD).
- **Output** presents results (monitor, printer).
This Input → Process → Output (+ Storage) flow is called the **IPO cycle**.

### Inside the CPU — the three parts
| Part | Job | Everyday picture |
|---|---|---|
| **ALU** (Arithmetic Logic Unit) | Does all arithmetic (+, −, ×, ÷) and logic (comparisons, AND/OR) | The calculator inside the brain |
| **CU** (Control Unit) | Directs everything: fetches instructions, decodes them, sends signals; **does no calculation itself** | The traffic constable |
| **Registers** | Tiny, extremely fast working slots inside the CPU | The clerk's fingertips |

Registers you should know by name: **PC** (Program Counter — address of the *next* instruction), **IR** (Instruction Register — holds the instruction being executed), **MAR/MDR** (Memory Address / Data Registers — talk to RAM), and the **Accumulator** (holds ALU results).

### The machine cycle
The CPU repeats four steps millions of times per second:
1. **Fetch** — CU brings the next instruction from memory (its address comes from the PC).
2. **Decode** — CU interprets what the instruction wants.
3. **Execute** — ALU (or another unit) does the work.
4. **Store** — the result is written back to memory or a register.
Memory hook: **F**at **D**ogs **E**at **S**nacks.

### Buses — the roads between blocks
- **Data bus** — carries the actual data (both directions).
- **Address bus** — carries *where* the data lives (CPU → memory, one direction).
- **Control bus** — carries command signals (read, write, interrupt).
More data-bus lines mean more bits moved at once — that is what "32-bit/64-bit processor" measures.

### Why it is called "stored program"
John von Neumann's idea: keep **instructions and data together in the same memory**, written as numbers. The CPU then simply fetches, decodes and executes them one after another — changing the program needs no rewiring. This single idea separates modern computers from fixed machines like calculators-in-hardware.

### Quick revision
- Block flow: Input → Process (CPU) → Output, with Memory and Storage alongside.
- CPU = ALU (calculates) + CU (controls) + registers (fastest storage).
- Machine cycle: **Fetch → Decode → Execute → Store**.
- PC = next instruction's address; IR = current instruction; Accumulator = ALU result holder.
- Data bus carries data; address bus carries location; control bus carries commands.
- Stored-program (von Neumann) = instructions and data in one memory."""
    S.pattern("cf-org-p1", "CPU part ↔ function", "very common",
        "'Which unit performs arithmetic?', 'which unit controls and coordinates?', 'where does the comparison happen?' — a CPU part with units as options.",
        None,
        "1. ALU = all arithmetic and logic (add, subtract, compare AND/OR). CU = direction only, no maths. Registers = fastest storage slots inside the CPU.\n2. Named registers: PC holds the next instruction's address, IR holds the current instruction, the Accumulator holds ALU results.\n3. In 'not a CPU part' questions, memory (RAM) and hard disk are outside the CPU.",
        "Which part of the CPU performs **comparison** of two values?",
        "The **Arithmetic Logic Unit (ALU)** — logic operations such as compare, AND, OR belong to the ALU. The Control Unit only directs traffic; it computes nothing.")
    S.pattern("cf-org-p2", "Machine cycle steps and order", "very common",
        "Give the correct order of fetch/decode/execute/store, or ask what happens in one of the four steps.",
        None,
        "1. Always **Fetch → Decode → Execute → Store** (Fat Dogs Eat Snacks).\n2. Meanings: fetch = bring from memory, decode = interpret, execute = do the work (ALU), store = write the result back.\n3. Reversed pairs (Decode before Fetch, Store before Execute) are the planted traps.",
        "In the machine cycle, the step in which the CPU **finds out what an instruction means** is —",
        "**Decode** — the Control Unit interprets the fetched instruction before the ALU executes it. Order: Fetch → Decode → Execute → Store.")
    S.pattern("cf-org-p3", "Buses and stored-program architecture", "common",
        "Which bus carries addresses/data/commands; what the stored-program (von Neumann) concept means; what the motherboard holds.",
        None,
        "1. Data bus = the data itself (two-way). Address bus = the location (CPU → memory). Control bus = command signals.\n2. Stored program = instructions and data kept together in the same memory, so programs can be changed without rewiring.\n3. 'Bits moved at once' describes the data bus width (32-bit/64-bit processors).",
        "The **stored-program concept**, the basis of modern computers, was proposed by —",
        "**John von Neumann** — instructions and data are stored together in the same memory, and the CPU fetches and executes them one after another.")
    S.pattern("cf-org-p4", "IPO cycle and block-diagram flow", "common",
        "What IPO stands for, which function saving a file is, or which arrow is correct in the Input–Process–Output block diagram.",
        None,
        "1. IPO = Input → Process → Output; Storage is the fourth basic function.\n2. Typing = input; calculating = processing; showing a result = output; saving for later = storage.\n3. In diagram statements, data always flows input → CPU → output, with the CPU connected to memory.",
        "Typing a document, printing it, and **saving it on the hard disk** — saving belongs to which basic computer function?",
        "**Storage** — the four basic functions are Input, Processing, Output and Storage. Saving for future use is storage.")

    S.q("cf-org-p1", "easy", "Which unit of the CPU **coordinates and controls** all other units but does not perform calculations?",
        ["ALU", "Control Unit", "Register", "ROM"], "Control Unit",
        "The **Control Unit (CU)** fetches, decodes and sends direction signals — the traffic constable. All arithmetic and logic belong to the ALU.",
        "CU = Constable, Untouched by maths.", 20)
    S.q("cf-org-p1", "easy", "The **fastest** data-holding locations inside a computer are —",
        ["Cache memory", "RAM", "Registers", "Hard disk"], "Registers",
        "**Registers** are tiny slots **inside the CPU itself** — the fastest storage in the whole machine. Cache comes next, then RAM, then the hard disk.",
        "Speed order: Registers > Cache > RAM > Disk.", 20)
    S.q("cf-org-p1", "medium", "Which register holds the **address of the next instruction** to be executed?",
        ["Instruction Register", "Program Counter", "Accumulator", "Memory Data Register"], "Program Counter",
        "The **Program Counter (PC)** stores the memory address of the *next* instruction. The IR holds the instruction currently being executed; the Accumulator holds ALU results.",
        "PC = 'Points to Come'.", 25)
    S.q("cf-org-p1", "medium", "All **arithmetic and logical** operations of a computer are performed by the —",
        ["Control Unit", "ALU", "CU + registers together", "Motherboard"], "ALU",
        "The **Arithmetic Logic Unit** does the maths (add, subtract, multiply, divide) and the logic (compare, AND, OR).",
        "ALU = Actual Labour Unit.", 20)
    S.q("cf-org-p2", "easy", "The correct sequence of steps in a **machine cycle** is —",
        ["Decode, Fetch, Execute, Store", "Fetch, Decode, Execute, Store", "Fetch, Execute, Decode, Store", "Execute, Store, Fetch, Decode"], "Fetch, Decode, Execute, Store",
        "The CPU **fetches** the instruction, **decodes** it, **executes** it and **stores** the result — repeating crores of times per second.",
        "Fat Dogs Eat Snacks.", 20)
    S.q("cf-org-p2", "medium", "During **execution** of an instruction, the actual work (say adding two numbers) is done by the —",
        ["Control Unit", "ALU", "Program Counter", "Address bus"], "ALU",
        "After fetch and decode, the **execute** step hands real computation to the **ALU**; the CU only supervises, and the PC merely points to the next instruction.",
        "Decode is CU's job; the sums are ALU's job.", 25)
    S.q("cf-org-p2", "easy", "In which machine-cycle step is the **result written back** to memory or a register?",
        ["Fetch", "Decode", "Execute", "Store"], "Store",
        "**Store** — the final step saves the executed result into memory or a register before the next fetch begins.",
        "Last step = Store.", 20)
    S.q("cf-org-p2", "medium", "'**Fetching**' an instruction in the machine cycle means —",
        ["Translating the instruction", "Bringing the instruction from main memory to the CPU", "Carrying out the instruction", "Printing the result"], "Bringing the instruction from main memory to the CPU",
        "**Fetch** = the CU picks up the next instruction from memory (its address comes from the Program Counter) and places it in the Instruction Register.",
        "Fetch = get it, Decode = read it, Execute = do it.", 25)
    S.q("cf-org-p3", "easy", "Which bus carries the **memory location** (not the data) from the CPU to memory?",
        ["Data bus", "Address bus", "Control bus", "Power bus"], "Address bus",
        "The **address bus** carries the location where data is to be read or written. The data itself travels on the data bus, and commands travel on the control bus.",
        "Address bus = the house number; data bus = the parcel.", 20)
    S.q("cf-org-p3", "medium", "In the **von Neumann (stored-program)** architecture, programs and data are —",
        ["Kept in two separate memories", "Kept together in the same memory", "Wired permanently into the hardware", "Loaded only from punched cards"], "Kept together in the same memory",
        "The stored-program idea places **instructions and data in one memory**, both as numbers, so the CPU can fetch and execute them in sequence — and programs can change without rewiring the machine.",
        "One memory for both = von Neumann.", 25)
    S.q("cf-org-p4", "easy", "The basic working cycle of a computer, **IPO**, stands for —",
        ["Input, Program, Output", "Input, Process, Output", "Internet, Process, Output", "Input, Print, Organise"], "Input, Process, Output",
        "**Input → Process → Output**: data enters, the CPU works on it, results leave (with Storage keeping them for later).",
        "IPO — like a share issue: data in, work done, result out.", 20)
    S.q("cf-org-p4", "medium", "Which of the following correctly lists the **four basic functions** of a computer?",
        ["Input, Processing, Output, Storage", "Booting, Processing, Printing, Saving", "Typing, Browsing, Gaming, Printing", "RAM, ROM, CPU, Monitor"], "Input, Processing, Output, Storage",
        "A computer takes **input**, **processes** it in the CPU, gives **output**, and **stores** data — everything else (gaming, browsing) is an application of these four.",
        "IPOS: Input, Process, Output, Storage.", 25)
    return S
