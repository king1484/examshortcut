"""hardware-memory deep content — part 1: hierarchy, units, number systems."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def N(correct, *wrongs):
    """Build (options, answer) for a computed numeric answer: distractors are the
    realistic mistakes passed in. Asserts 4 unique options with the answer present."""
    opts = [str(correct)] + [str(w) for w in wrongs]
    assert len(set(opts)) == 4, opts
    return opts, str(correct)


def build_hierarchy():
    S = Sub("hm-memory-hierarchy")
    S.notes = """### The memory ladder
Computer memory is a trade-off: the **faster** a memory is, the **smaller and costlier** it is. So machines stack several kinds, from tiny-fast to huge-slow:

| Level | Technology | Volatile? | Typical size |
|---|---|---|---|
| Registers | Inside the CPU | Yes | Bytes |
| **Cache** (L1/L2/L3) | **SRAM**, on/near the CPU | Yes | KB to MB |
| **Main memory** | **RAM (DRAM)** | Yes | GB |
| SSD | Flash chips | No | 100s of GB |
| Hard disk / tape | Magnetic | No | TB |

Climbing up = faster, costlier, smaller. The CPU keeps its most-wanted data as high on this ladder as possible.

### Volatile vs non-volatile
- **Volatile** memory **loses its content when power goes off**: registers, cache, RAM. The **V**ol **V**anishes rule.
- **Non-volatile** keeps data without power: ROM, flash (SSD, pen drive, memory card), hard disk, DVD.

### RAM — the working desk
RAM holds the programs and data currently in use; it is **read and written** freely but wiped at power-off. Two flavours:
| Type | Full form | Trait |
|---|---|---|
| **SRAM** | Static RAM | Flip-flop cells, no refresh needed, **fast, costly** → used for **cache** |
| **DRAM** | Dynamic RAM | One transistor + capacitor per bit; the capacitor **leaks, so it needs constant refreshing**; cheaper, denser → used for **main memory** |

### ROM family — the printed pages
ROM (**Read Only Memory**) is non-volatile; ordinary programs can only read it. Its family differs only in **how it can be written/erased**:
| Type | Written | Erased |
|---|---|---|
| PROM | Once, by the user/manufacturer | Never |
| **EPROM** | Reprogrammable | **Ultraviolet (UV) light** |
| **EEPROM** | Reprogrammable | **Electrically**, in circuit |
| Flash | Reprogrammable in blocks | Electrically (fast) — SSDs and pen drives are flash |

The PC's start-up firmware (**BIOS/UEFI**) lives in ROM/flash — that is why it survives every power cut.

### Two bridge concepts
- **Cache** — a small SRAM buffer between CPU and RAM (L1 inside the core is fastest and smallest, then L2, then L3). It keeps copies of recently used data so the CPU rarely waits for slow RAM.
- **Virtual memory** — when RAM is full, the OS uses **disk space as extra RAM** (page file). It saves the machine from crashing but is far slower than real RAM. It is **not** physical memory.

### Quick revision
- Ladder (fast→slow): Registers → Cache (SRAM) → RAM (DRAM) → SSD → HDD → Tape.
- Volatile = vanishes: registers, cache, RAM. Non-volatile: ROM, flash, disk.
- SRAM = cache (fast, no refresh); DRAM = main RAM (cheap, needs refresh).
- PROM once → EPROM (UV erase) → EEPROM (electrical erase) → flash (blocks).
- Virtual memory = disk acting as RAM overflow, not real RAM."""
    S.pattern("hm-hie-p1", "Volatile vs non-volatile identification", "very common",
        "'Which of these is volatile?', 'content of which memory is lost on power failure?', statement lists mixing RAM, ROM, cache, disk.",
        None,
        "1. Volatile = vanishes with power: registers, cache, RAM (SRAM and DRAM both).\n2. Non-volatile: ROM and its family, flash (SSD, pen drive), magnetic disk, DVD.\n3. In statement questions, test each memory against this split — ROM is never volatile.",
        "Which of the following is **non-volatile**?",
        "**ROM** — it keeps its content without power. RAM, cache and registers are all volatile.")
    S.pattern("hm-hie-p2", "Hierarchy ordering and cache position", "very common",
        "Arrange memories by speed or size, or identify the memory between CPU and RAM, or the levels L1/L2/L3.",
        None,
        "1. Speed order: Registers > Cache > RAM > SSD > HDD > Tape; size order is the exact reverse.\n2. Cache = small SRAM buffer between CPU and RAM; L1 smallest-fastest, then L2, L3.\n3. 'Smallest but fastest' always points to registers, not cache.",
        "Arrange by access speed (fastest first): RAM, Registers, Hard disk, Cache",
        "**Registers → Cache → RAM → Hard disk.** Each step down trades speed for size and cheapness.")
    S.pattern("hm-hie-p3", "SRAM vs DRAM", "common",
        "'Why does DRAM need refreshing?', 'which RAM is used in cache?', 'SRAM vs DRAM statements'.",
        None,
        "1. DRAM stores each bit in a capacitor that leaks charge → needs **constant refreshing**; cheaper, denser → main memory.\n2. SRAM uses flip-flops, no refresh, faster, costlier → **cache**.\n3. S = Static (stands still), D = Dynamic (must be refreshed).",
        "DRAM needs to be refreshed periodically because —",
        "Each DRAM bit sits in a tiny **capacitor that gradually loses its charge**, so the cells are re-read and re-written thousands of times a second to keep the data alive.")
    S.pattern("hm-hie-p4", "ROM family: PROM / EPROM / EEPROM / firmware", "common",
        "'EPROM is erased by…', 'EEPROM differs from EPROM because…', 'where is the BIOS stored?', 'which ROM can be programmed only once?'",
        None,
        "1. Erasing ladder: PROM (never) → EPROM (UV light) → EEPROM (electrically) → flash (electrically, in blocks).\n2. BIOS/firmware lives in ROM/flash — non-volatile by definition.\n3. 'Programmed only once' = PROM; 'electrically erasable' = EEPROM.",
        "Which memory is used to store the **BIOS** firmware of a PC?",
        "A **ROM/flash (EEPROM-type) chip** on the motherboard — the firmware must survive every power cut, so volatile RAM is impossible.")
    S.pattern("hm-hie-p5", "Cache and virtual memory concepts", "common",
        "'Virtual memory is…', 'cache memory is placed…', 'which is faster, L1 or L3?', 'cache is made of which RAM?'.",
        None,
        "1. Cache = SRAM buffer between CPU and RAM; L1 (inside the core) fastest-smallest, then L2, L3.\n2. Virtual memory = **disk space** used as RAM overflow — big but slow, not physical RAM.\n3. Trap: 'virtual memory is part of RAM' — false; it lives on the storage disk.",
        "**Virtual memory** is best described as —",
        "Disk space managed by the OS as an overflow area when RAM fills up (the page file) — it prevents crashes but works far slower than real RAM.")

    S.q("hm-hie-p1", "easy", "Which of the following is **volatile** memory?",
        ["ROM", "Flash drive", "RAM", "DVD"], "RAM",
        "**RAM** loses all its content the moment power is cut — the definition of volatile. ROM, flash and DVD are non-volatile.",
        "Volatile = Vanishes with power.", 20)
    S.q("hm-hie-p1", "hard", "Consider the statements:\n1. Cache memory is volatile.\n2. ROM is used to store start-up firmware.\n3. The content of RAM survives a system shutdown.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Cache (SRAM) is volatile and ROM holds the BIOS firmware — both correct. Statement 3 is wrong: RAM is volatile, so shutdown wipes it.",
        "One vanishing statement ruins the set — RAM never survives.", 35)
    S.q("hm-hie-p2", "easy", "Which shows memories in **decreasing order of speed**?",
        ["RAM, Cache, Registers, Hard disk", "Registers, Cache, RAM, Hard disk", "Cache, Registers, RAM, Hard disk", "Hard disk, RAM, Cache, Registers"], "Registers, Cache, RAM, Hard disk",
        "Speed falls as you move away from the CPU: **Registers → Cache → RAM → Hard disk** (size and cheapness rise in the same direction).",
        "Closest to the CPU = fastest.", 20)
    S.q("hm-hie-p2", "medium", "**L1, L2 and L3** are levels of —",
        ["Virtual memory", "Cache memory", "ROM", "Secondary storage"], "Cache memory",
        "L1/L2/L3 are the levels of **cache** — small SRAM buffers between the CPU and RAM. L1 is smallest and fastest; L3 is the largest and slowest of the three.",
        "L = Level of cache.", 25)
    S.q("hm-hie-p2", "hard", "Arrange in **increasing** order of access time: A. DRAM  B. SRAM cache  C. Registers  D. Hard disk",
        ["D, A, B, C", "C, B, A, D", "B, C, D, A", "A, B, C, D"], "D, A, B, C",
        "Slowest first: hard disk (D), then DRAM (A), then SRAM cache (B), and registers (C) are fastest. Increasing access time = slow → fast = **D, A, B, C**.",
        "Disk, DRAM, SRAM, registers — away from the CPU is slow.", 35)
    S.q("hm-hie-p3", "medium", "**SRAM** is preferred for cache memory mainly because it —",
        ["Is cheaper than DRAM", "Is faster and needs no refreshing", "Holds more data than DRAM", "Is non-volatile"], "Is faster and needs no refreshing",
        "SRAM's flip-flop cells answer instantly and **stay valid without refresh** — perfect for cache — but cost more and hold fewer bits per chip than DRAM.",
        "S = Static = stands still, no refresh.", 25)
    S.q("hm-hie-p3", "medium", "The full form of **DRAM** hints at its weakness. DRAM stands for —",
        ["Direct Random Access Memory", "Dynamic Random Access Memory", "Data Retention Access Memory", "Drive Random Access Module"], "Dynamic Random Access Memory",
        "**DRAM = Dynamic Random Access Memory** — 'dynamic' because its capacitor cells must be **dynamically refreshed** thousands of times per second.",
        "D = Dynamic = always being refreshed.", 20)
    S.q("hm-hie-p4", "easy", "Which ROM can be **erased electrically**, without ultraviolet light?",
        ["PROM", "EPROM", "EEPROM", "CD-ROM"], "EEPROM",
        "**EEPROM = Electrically Erasable Programmable ROM** — erased by applying an electrical signal in the circuit. EPROM needs a UV lamp; PROM cannot be erased at all.",
        "E-E = Electrically Erasable.", 20)
    S.q("hm-hie-p4", "medium", "Which statement about **PROM** is correct?",
        ["It can be erased with UV light", "It can be written (programmed) only once", "It is volatile", "It is faster than all RAM"], "It can be written (programmed) only once",
        "**PROM** (Programmable ROM) is programmed exactly once after manufacture; after that it is permanent. UV erasing is EPROM's feature; volatility belongs to RAM.",
        "PROM = Program **Once** ROM.", 25)
    S.q("hm-hie-p5", "easy", "The small, very fast memory placed **between the CPU and main memory** is —",
        ["Virtual memory", "Cache memory", "ROM", "Tape"], "Cache memory",
        "**Cache** (SRAM) holds copies of the most-used data so the CPU rarely waits for slower RAM.",
        "Cache = the CPU's personal notepad.", 20)
    S.q("hm-hie-p5", "medium", "Cache memory is normally built using —",
        ["DRAM", "SRAM", "Magnetic cores", "Optical discs"], "SRAM",
        "Cache uses **SRAM** for its speed and zero-refresh cells. DRAM (cheaper, denser) fills main memory instead.",
        "Cache = Static (SRAM); main RAM = Dynamic (DRAM).", 25)
    S.q("hm-hie-p5", "hard", "Consider the statements:\n1. Virtual memory is a part of physical RAM.\n2. Cache memory lies between the CPU and main memory.\n3. L1 cache is smaller and faster than L3 cache.\nWhich are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], "2 and 3 only",
        "Statements 2 and 3 are standard cache facts. Statement 1 is the classic error — virtual memory is **disk space** used as a RAM overflow, not physical RAM.",
        "Virtual = on disk; cache = near CPU.", 35)
    return S


def build_units():
    S = Sub("hm-memory-units")
    S.notes = """### The unit ladder
All data is stored as bits. The units stack up by **1024 (2 to the power 10)** at each step — exam convention, never 1000:

| Unit | Equals | In bytes |
|---|---|---|
| 1 **bit** | smallest unit — one 0 or 1 | — |
| 1 **Nibble** | **4 bits** | — |
| 1 **Byte (B)** | **8 bits** | 1 |
| 1 **KiloByte (KB)** | 1024 B | 2¹⁰ |
| 1 **MegaByte (MB)** | 1024 KB | 2²⁰ = 10,48,576 B |
| 1 **GigaByte (GB)** | 1024 MB | 2³⁰ = 1,07,37,41,824 B |
| 1 **TeraByte (TB)** | 1024 GB | 2⁴⁰ |
| 1 **PetaByte (PB)** | 1024 TB | 2⁵⁰ |

**How to convert:** going up → divide by 1024 at each step; going down → multiply by 1024. Example: 4 GB = 4 × 1024 = **4096 MB**; 2048 KB = 2048 ÷ 1024 = **2 MB**.

### Bits vs bytes — the speed trap
- File sizes and storage are measured in **bytes** (MB, GB).
- **Line speeds are measured in bits**: Mbps = **megaBITS** per second.
- 8 bits = 1 byte, so an **8 Mbps** line moves about **1 MB** of file data per second. A 16 Mbps connection downloads a 10 MB file in about 10 × 8 ÷ 16 = **5 seconds**.
Watch the case: **Mb** = megabit, **MB** = megabyte.

### Other asked units
- **Word length** — the number of bits a CPU handles in one go (a '64-bit processor').
- **Smallest unit of data** = bit; **smallest unit of memory addressable** = usually 1 byte.
- Half a byte (4 bits) = **nibble** — one hexadecimal digit is exactly one nibble.

### Worked examples in exam style
1. **4 GB to MB:** climb down one rung — 4 × 1024 = **4096 MB**.
2. **2048 KB to MB:** climb up — 2048 ÷ 1024 = **2 MB**.
3. **Bits in 2 KB:** 2 × 1024 = 2048 bytes, then × 8 = **16,384 bits**.
4. **Download time:** a 10 MB file on a 16 Mbps line: file = 10 × 8 = 80 megabits; 80 ÷ 16 = **5 seconds**.
5. **Which is largest** among 1024 KB, 1 MB, 10,00,000 bytes, 0.5 GB: put everything in KB — 1024, 1024, about 977, 5,24,288 → **0.5 GB** wins.

### Where you already use this ladder
- Internet plans are sold in **Mbps (bits)**, but your browser shows **MB/s (bytes)** — an 80 Mbps line downloads near 10 MB/s.
- A phone photo ≈ 2–5 MB, a movie ≈ 1–4 GB, a good laptop SSD ≈ 512 GB–1 TB. These everyday anchors help you reject absurd options instantly.

### Two traps that decide the mark
1. Using 1000 instead of 1024 — every ladder question in exams assumes **1024**.
2. Confusing Mb (bits) with MB (bytes) in speed questions — divide by 8 to go bits → bytes.

### Quick revision
- Bit → Nibble (4) → Byte (8) → KB (1024) → MB → GB → TB → PB; each step ×1024.
- 4 GB = 4096 MB; 2048 KB = 2 MB; 1 TB = 1024 GB.
- Speeds are in bits: 8 Mbps ≈ 1 MB/s of file data.
- Nibble = 4 bits = one hex digit. Smallest unit = bit."""
    S.pattern("hm-uni-p1", "Bit / nibble / byte definitions", "very common",
        "'How many bits in a byte/nibble?', 'how many nibbles in a byte?', 'bits in 3 bytes?' — direct small-number questions.",
        None,
        "1. Fixed facts: 1 byte = 8 bits, 1 nibble = 4 bits, so a byte = 2 nibbles.\n2. Multiply for bigger counts: 3 bytes = 3 × 8 = 24 bits.\n3. One hex digit = one nibble — a free link to hexadecimal questions.",
        "How many **bits** are there in 3 bytes?",
        "3 × 8 = **24 bits** — one byte always carries exactly 8 bits.")
    S.pattern("hm-uni-p2", "KB → MB → GB → TB ladder conversion", "very common",
        "'4 GB = how many MB?', '2 TB = how many GB?', 'which is largest', 'a folder of n files of 512 KB is how many MB'.",
        None,
        "1. Every step is ×1024 going up, ÷1024 going down — never 1000.\n2. 4 GB = 4 × 1024 = 4096 MB; 2048 KB = 2 MB; 1 TB = 1024 GB.\n3. For 'which is largest', convert everything to one unit (say KB) before comparing.",
        "A pen drive holds **4 GB**. How many **MB** is that (exam convention)?",
        "4 × 1024 = **4096 MB**. Each step up the ladder multiplies by 1024, so going from GB to MB multiplies by 1024.")
    S.pattern("hm-uni-p3", "Bits vs bytes in data-transfer speed", "common",
        "'A 16 Mbps line downloads a 10 MB file in how long?', '8 Mbps equals how many MB/s?' — speed given in megabits, file in megabytes.",
        None,
        "1. Convert the file to bits (×8) or the speed to bytes (÷8) before dividing.\n2. 8 Mbps = 1 MB/s; 16 Mbps = 2 MB/s.\n3. Time = file size ÷ effective speed, both in the same unit.",
        "A connection delivers **16 Mbps** (megabits per second). How many **megabytes** is that per second?",
        "16 ÷ 8 = **2 MB per second** — eight bits make one byte, so divide the bit-rate by 8.")
    S.pattern("hm-uni-p4", "Unit odd-one-out and definitions", "common",
        "'The smallest unit of data is', 'word length means', 'which is not a unit of memory'.",
        None,
        "1. Bit = smallest unit; byte = 8 bits; nibble = 4 bits.\n2. Word length = bits the CPU processes in one operation (hence '64-bit processor').\n3. Odd-one-out versions usually slip in a speed unit (Mbps) among size units (KB, MB, GB).",
        "Which of the following is **NOT** a unit of data size?",
        "**Mbps** — megabits per **second**, a speed unit. KB, MB and GB measure size.")

    S.q("hm-uni-p1", "easy", "One **byte** consists of how many bits?",
        ["4", "8", "16", "32"], "8",
        "**1 byte = 8 bits** — the definition every other conversion builds on.",
        "Byte = 8, Nibble = 4.", 20)
    S.q("hm-uni-p1", "easy", "How many **nibbles** make one byte?",
        ["1", "2", "4", "8"], "2",
        "A nibble is 4 bits, a byte is 8 bits — so one byte = **2 nibbles**.",
        "Two nibbles nibble one byte.", 20)
    computed = 3 * 8
    o, a = N(computed, computed + 3, computed - 4, computed * 2)
    S.q("hm-uni-p1", "easy", "A short message of **3 bytes** contains how many **bits**?",
        o, a,
        "3 bytes × 8 bits = **24 bits**. Multiply by 8 to go from bytes to bits.",
        "Bytes → bits: multiply by 8.", 20)
    S.q("hm-uni-p2", "easy", "How many **megabytes** are there in **2 GB**?",
        N(2 * 1024, 2000, 1024, 2 * 100)[0], N(2 * 1024, 2000, 1024, 2 * 100)[1],
        "2 × 1024 = **2048 MB** — each step up the ladder multiplies by 1024, never 1000.",
        "GB → MB: ×1024.", 20)
    v = 4 * 1024
    o, a = N(v, 4000, v // 2, v * 2)
    S.q("hm-uni-p2", "medium", "A movie file of **4 GB** equals how many **MB**?",
        o, a,
        "4 GB = 4 × 1024 = **4096 MB**. The 4000 option is the classic 1000-based trap.",
        "4 GB = 4096 MB (4 × 1024).", 25)
    v = 2048 // 1024
    o, a = N(v, 2048, 1024, 24)
    S.q("hm-uni-p2", "easy", "**2048 KB** equals —",
        o, a,
        "2048 ÷ 1024 = **2 MB**. Going up the ladder means dividing by 1024.",
        "KB → MB: ÷1024.", 20)
    v = 1 * 1024
    o, a = N(v, 1000, 512, 2 * 1024)
    S.q("hm-uni-p2", "easy", "One **gigabyte** equals how many **megabytes**?",
        o, a,
        "**1 GB = 1024 MB** = 10,48,576 KB = 2³⁰ bytes.",
        "The ladder: 1024 at every step.", 20)
    total_kb = 3 * 512
    o, a = N("1.5 MB", "1536 MB", "3 MB", "0.5 MB")
    assert total_kb == 1536 and total_kb / 1024 == 1.5
    S.q("hm-uni-p2", "hard", "A folder contains **3 files of 512 KB each**. The total size is —",
        o, a,
        "3 × 512 = 1536 KB; 1536 ÷ 1024 = **1.5 MB**. Convert first, then divide up the ladder.",
        "512 KB × 3 = 1536 KB = 1.5 MB.", 35)
    o, a = N("0.5 GB", "1024 KB", "1 MB", "10,00,000 bytes")
    assert 0.5 * 1024 * 1024 == 524288 and 524288 > 1024 and 524288 > 1000000 / 1024
    S.q("hm-uni-p2", "medium", "Which of the following is the **largest**?",
        o, a,
        "Convert to KB: 0.5 GB = 5,24,288 KB; 1 MB = 1024 KB; 10,00,000 bytes ≈ 977 KB. **0.5 GB wins**.",
        "Everything into one unit, then compare.", 30)
    computed = 2 * 1024 * 8
    o, a = N(computed, computed // 8, 16000, 16)
    S.q("hm-uni-p3", "medium", "A text file of **2 KB** contains how many **bits**?",
        o, a,
        "2 KB = 2048 bytes; 2048 × 8 = **16384 bits**. Two conversions: ×1024 (KB→B), then ×8 (B→bits).",
        "KB → bytes (×1024) → bits (×8).", 30)
    o, a = N("1 MB", "8 MB", "100 MB", "0.125 MB")
    S.q("hm-uni-p3", "easy", "A line speed of **8 Mbps** (megabits per second) moves how much **file data** per second?",
        o, a,
        "8 bits = 1 byte, so 8 megabits/s = **1 megabyte/s** of file data. Line speeds are always in bits; files are in bytes.",
        "Mbps ÷ 8 = MB/s.", 20)
    o, a = N("5 seconds", "40 seconds", "1.25 seconds", "160 seconds")
    assert 10 * 8 / 16 == 5
    S.q("hm-uni-p3", "hard", "At a steady **16 Mbps**, downloading a **10 MB** file takes about —",
        o, a,
        "File in bits: 10 × 8 = 80 megabits. Time = 80 ÷ 16 = **5 seconds**. Same-unit division does it in one line.",
        "File ×8 to bits, then ÷ speed.", 35)
    S.q("hm-uni-p4", "easy", "The **smallest unit** of data in a computer is —",
        ["Byte", "Nibble", "Bit", "Word"], "Bit",
        "A **bit** (binary digit) — one 0 or 1 — is the smallest unit. A nibble is 4 bits and a byte is 8.",
        "Bit first, always.", 20)
    S.q("hm-uni-p4", "medium", "**Word length** of a computer refers to —",
        ["The dictionary size of its software", "The number of bits the CPU processes in one operation", "The length of its password", "The number of bytes on its disk"], "The number of bits the CPU processes in one operation",
        "Word length = the CPU's natural chunk size — 32-bit and 64-bit processors are named by it.",
        "'64-bit processor' = 64-bit words.", 25)
    S.q("hm-uni-p4", "medium", "Which of the following is **NOT** a memory-size unit?",
        ["Terabyte", "Petabyte", "Mbps", "Gigabyte"], "Mbps",
        "**Mbps** = megabits per second — a data-transfer **speed**. TB, PB and GB are size units.",
        "Speed units end in 'per second'.", 20)
    return S


def build_number_systems():
    S = Sub("hm-number-systems")
    S.notes = """### The four systems
| System | Base | Digits used | Example |
|---|---|---|---|
| Binary | 2 | 0, 1 | 1101 |
| Octal | 8 | 0–7 | 65 |
| Decimal | 10 | 0–9 | 91 |
| Hexadecimal | 16 | 0–9, A–F (A=10 … F=15) | 2F |

A digit's value = digit × (base ^ position), counting positions **from 0 at the right**.

### Any base → decimal (multiply and add)
(1101)₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = **13**.
(2F)₁₆ = 2×16 + 15 = **47** (F = 15). (67)₈ = 6×8 + 7 = **55**.

### Decimal → any base (divide and read upward)
Divide repeatedly by the base and read the **remainders bottom to top**:
45 ÷ 2 = 22 r **1** → 22 ÷ 2 = 11 r **0** → 11 ÷ 2 = 5 r **1** → 5 ÷ 2 = 2 r **1** → 2 ÷ 2 = 1 r **0** → 1 ÷ 2 = 0 r **1**; reading up: (101101)₂ = 45. ✔ (32+8+4+1 = 45)

### The grouping shortcuts (seconds-saving)
- **1 octal digit = 3 bits**, **1 hex digit = 4 bits**; make groups **from the right**, padding the left with zeros.
- (1101011)₂ → 001 101 011 → **153**₈; (11011011)₂ → 1101 1011 → **DB**₁₆.
- Hex letters: A=10, B=11, C=12, D=13, E=14, **F=15**; FF = 255 = the largest 8-bit value.

### Ranges and validity
- **n bits hold 2ⁿ different values**, from 0 to 2ⁿ − 1: 8 bits → 256 values (0–255).
- **Octal digits stop at 7** — any number containing 8 or 9 cannot be octal.
- Hex digits stop at F: 'G' or '2H' cannot be hexadecimal.

### Exam workflow
1. Read the stem: which base to which base?
2. Conversions through **binary** are fastest for octal/hex (grouping), direct division/multiplication for decimal.
3. Always check: does each digit exist in the source base? Is the remainder order bottom-to-top?

### More worked pairs you can reuse
- (1010)₂ = 8 + 2 = **10**; (1111)₂ = 8+4+2+1 = **15**; (10000)₂ = **16**.
- (255)₁₀ = **FF**₁₆ (15×16 + 15); (128)₁₀ = **(10000000)₂**.
- (777)₈ = 7×64 + 7×8 + 7 = **511** — the largest 3-digit octal, exactly like FF caps hex.
- (100)₈ = 64, (20)₁₆ = 32, (11)₂ = 3 — small anchors to sanity-check options.

### Powers of 2 worth memorising
2⁰=1, 2¹=2, 2²=4, 2³=8, 2⁴=16, 2⁵=32, 2⁶=64, 2⁷=128, 2⁸=256, 2⁹=512, 2¹⁰=1024.
Ten lines that answer half the number-system paper: binary→decimal becomes addition, ranges become 2ⁿ, and KB/MB conversions reuse the same ladder.

### Two elimination shortcuts
1. **Digit validity:** an option with 8 or 9 is never octal; one with G or beyond is never hexadecimal — strike it out before computing.
2. **Parity check:** a binary number ending in 0 is even, ending in 1 is odd — if the decimal in the stem is even, the correct binary must end in 0.

### Quick revision
- Bases: 2 (0,1), 8 (0–7), 10 (0–9), 16 (0–9, A–F).
- Base→decimal: digit × base^position, right to left. Decimal→base: divide, read remainders upward.
- Octal = 3-bit groups, hex = 4-bit groups, grouped from the right.
- F = 15; FF = 255; 8 bits = 256 values (0–255).
- Octal has no 8 or 9; hex has nothing after F."""
    S.pattern("hm-num-p1", "Any base → decimal conversion", "very common",
        "'The decimal value of (1101)₂ is', '(2F)₁₆ in decimal is', '(67)₈ equals' — a number with a base subscript and four plain decimals.",
        None,
        "1. Multiply each digit by base^position, positions counted from 0 at the right.\n2. Hex: convert letters first (A=10 … F=15) — 2F = 2×16 + 15 = 47.\n3. Sanity-check with the binary powers 1, 2, 4, 8, 16, 32, 64, 128.",
        "The decimal value of the binary number **110101** is —",
        "1×32 + 1×16 + 0×8 + 1×4 + 0×2 + 1×1 = **53**. Pick the positions where 1s sit (32, 16, 4, 1) and add.")
    S.pattern("hm-num-p2", "Decimal → any base conversion", "very common",
        "'The binary equivalent of 45 is', '100 in hexadecimal is', '58 in octal is' — a plain decimal and four base-tagged options.",
        None,
        "1. Divide repeatedly by the target base, writing each remainder.\n2. Read the remainders **bottom to top** — the top-to-bottom reading is the standard trap.\n3. Verify by converting back: expand your answer's digits by powers of the base; it must return the original number.",
        "The **binary** equivalent of decimal **45** is —",
        "Repeated division by 2 gives remainders 1, 0, 1, 1, 0, 1 read upward → **101101**. Check: 32+8+4+1 = 45. ✔")
    S.pattern("hm-num-p3", "Binary ↔ octal / hex by grouping", "common",
        "'1101011 in octal', '11011011 in hexadecimal', 'convert binary using grouping' — a long binary string and base-8 or base-16 options.",
        None,
        "1. Octal: group the bits in **3s from the right**; hex: group in **4s from the right**; pad the left with zeros.\n2. Convert each group separately: 001 101 011 → 1 5 3 → 153₈.\n3. Cross-check the hex letters: 10–15 map to A–F.",
        "The binary number **1101011** in **octal** is —",
        "Group in 3s from the right: 001 101 011 → 1, 5, 3 → **153₈**. (Each octal digit is exactly 3 bits.)")
    S.pattern("hm-num-p4", "n-bit range and digit validity", "common",
        "'How many values can 8 bits represent?', 'largest number in n bits', 'which of these cannot be an octal/hexadecimal number'.",
        None,
        "1. n bits → 2ⁿ values, spanning 0 to 2ⁿ − 1: 8 bits = 256 values, largest 255.\n2. Digit check: octal allows only 0–7; hexadecimal only 0–9 and A–F.\n3. An option containing 8 or 9 cannot be octal; one containing G or H cannot be hex.",
        "How many **different values** can be represented by **8 bits**?",
        "2⁸ = **256** different values (0 to 255). The largest value is one less: 2⁸ − 1 = 255.")

    o, a = N(int("1101", 2), int("1101", 2) + 2, int("1100", 2), 11)
    S.q("hm-num-p1", "easy", "The decimal value of the binary number **(1101)₂** is —",
        o, a,
        "1×8 + 1×4 + 0×2 + 1×1 = **13**. Add the powers of 2 wherever a 1 appears.",
        "Powers 8-4-2-1; add where there is a 1.", 20)
    o, a = N(int("1A", 16), int("1A", 16) + 6, int("A1", 16), 10)
    S.q("hm-num-p1", "medium", "The hexadecimal number **(1A)₁₆** equals which decimal number?",
        o, a,
        "1×16 + 10 = **26** (A = 10). Watch the digit order — A1 would be 161.",
        "Left digit ×16, right digit added; A=10.", 25)
    o, a = N(int("67", 8), int("67", 8) + 2, int("76", 8), 67)
    S.q("hm-num-p1", "medium", "The octal number **(67)₈** equals which decimal number?",
        o, a,
        "6×8 + 7 = **55**. Position values in octal are 1, 8, 64, …",
        "Left digit ×8, right digit added.", 25)
    o, a = N(int("3E", 16), int("3E", 16) - 1, int("E3", 16), int("3E", 16) + 16)
    S.q("hm-num-p1", "hard", "The hexadecimal number **(3E)₁₆** equals which decimal number?",
        o, a,
        "3×16 + 14 = **62** (E = 14). Converting back: 62 = 48 + 14 = 3×16 + E. ✔",
        "E = 14; multiply the left digit by 16.", 30)
    n = 45
    o, a = N(bin(n)[2:], bin(n + 1)[2:], bin(n + 8)[2:], bin(n + 16)[2:])
    S.q("hm-num-p2", "medium", "The **binary** equivalent of decimal **45** is —",
        o, a,
        "45 ÷ 2 chain: remainders 1,0,1,1,0,1 read upward → **101101**. Verify: 32 + 8 + 4 + 1 = 45. ✔",
        "Divide by 2, read remainders bottom-to-top.", 25)
    n = 100
    o, a = N(format(n, "X"), format(n + 1, "X"), format(n, "X")[::-1], format(n + 16, "X"))
    S.q("hm-num-p2", "medium", "The decimal number **100** in **hexadecimal** is —",
        o, a,
        "100 ÷ 16 = 6 remainder 4 → **(64)₁₆**. Check: 6×16 + 4 = 100. ✔",
        "Divide by 16; 6 and 4 give 64.", 25)
    n = 58
    o, a = N(format(n, "o"), format(n + 1, "o"), format(n, "o")[::-1], format(n + 8, "o"))
    S.q("hm-num-p2", "medium", "The decimal number **58** in **octal** is —",
        o, a,
        "58 ÷ 8 = 7 remainder 2 → **(72)₈**. Check: 7×8 + 2 = 58. ✔",
        "Divide by 8; read remainders upward.", 25)
    n = 1000
    o, a = N(format(n, "X"), format(n + 1, "X"), format(n, "b"), format(n - 1, "X"))
    S.q("hm-num-p2", "hard", "The decimal number **1000** in **hexadecimal** is —",
        o, a,
        "1000 ÷ 16 = 62 r **8**; 62 ÷ 16 = 3 r **14(E)**; read upward → **(3E8)₁₆**. Check: 3×256 + 14×16 + 8 = 1000. ✔",
        "Two rounds of division by 16; E = 14.", 35)
    b = "1101011"
    o, a = N(format(int(b, 2), "o"), format(int(b, 2) + 8, "o"), "651", format(int(b, 2), "X"))
    assert int("110", 2) == 6 and int("101", 2) == 5 and int("1", 2) == 1
    S.q("hm-num-p3", "medium", "The binary number **(1101011)₂** in **octal** is —",
        o, a,
        "Groups of 3 from the right: 001 101 011 → **(153)₈**. Check via decimal: 107 = 1×64 + 5×8 + 3. ✔",
        "3-bit groups from the right: 1-5-3.", 30)
    b = "11011011"
    o, a = N(format(int(b, 2), "X"), format(int(b, 2) + 1, "X"), "BD", format(int(b, 2), "o"))
    assert format(int(b, 2), "o") == "333"
    S.q("hm-num-p3", "medium", "The binary number **(11011011)₂** in **hexadecimal** is —",
        o, a,
        "Groups of 4 from the right: 1101 1011 → 13, 11 → **(DB)₁₆**. Check: 219 = 13×16 + 11. ✔",
        "4-bit groups: D-B.", 30)
    o, a = N(2 ** 8, 2 ** 8 - 1, 2 ** 7, 2 ** 8 + 1)
    S.q("hm-num-p4", "medium", "How many **different values** can **8 bits** represent?",
        o, a,
        "2⁸ = **256** values, from 0 up to 255. 'Largest value' would be 255; 'number of values' is 256.",
        "2ⁿ values; largest is 2ⁿ − 1.", 25)
    o, a = N("789", "707", "645", "777")
    S.q("hm-num-p4", "easy", "Which of the following **cannot** be an **octal** number?",
        o, a,
        "Octal uses only the digits 0–7. **789** contains 8 and 9, so it is impossible in base 8.",
        "Spot the 8 or 9 — instant elimination.", 20)
    o, a = N("2H4", "2F4", "1AB", "9C0")
    S.q("hm-num-p4", "medium", "Which of the following **cannot** be a **hexadecimal** number?",
        o, a,
        "Hexadecimal digits run 0–9 and A–F. **2H4** contains H, which does not exist in base 16 (letters stop at F).",
        "Letters stop at F — anything beyond is fake hex.", 25)
    return S
