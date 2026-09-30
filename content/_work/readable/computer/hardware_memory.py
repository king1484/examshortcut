"""Readable rewrite of Computer > Hardware & Memory (all 6 subtopics).

Plain English, tables, one method per question type. Facts come from the existing notes only.
Number-system and unit arithmetic is asserted below. Old pattern ids kept; new ids continue each prefix.
Run: python hardware_memory.py  (patches content/core/topics/computer/hardware-memory.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "computer" / "hardware-memory.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


# ---- arithmetic checks for every number used in examples ----
assert 3 * 8 == 24
assert 4 * 1024 == 4096 and 2048 // 1024 == 2
assert 2 * 1024 * 8 == 16384
assert 10 * 8 == 80 and 80 // 16 == 5
assert 16 // 8 == 2
assert 1024 * 1024 == 1048576 and 1024 ** 3 == 1073741824
assert 2 ** 21 == 2097152
assert int("110101", 2) == 53 and int("1101", 2) == 13 and int("111010", 2) == 58
assert bin(45)[2:] == "101101"
assert oct(int("1101011", 2))[2:] == "153"
assert hex(int("11011011", 2))[2:].upper() == "DB"
assert oct(int("11010111", 2))[2:] == "327" and int("11010111", 2) == 215
assert int("2F", 16) == 47 and int("C8", 16) == 200 and int("FF", 16) == 255
assert int("67", 8) == 55 and int("777", 8) == 511 and 2 ** 8 == 256
assert bin(128)[2:] == "10000000" and hex(255)[2:].upper() == "FF"
assert 4 * 1024 // 1 == 4096 and int("101", 2) == 5 and int("1010", 2) == 10
assert int("10111", 2) == 23 and hex(45)[2:].upper() == "2D"
assert 1024 * 8 == 8192

SUBS = {}

# =====================================================================
# 1. Memory hierarchy
# =====================================================================
SUBS["hm-memory-hierarchy"] = dict(
    concept=(
        "A computer keeps data in several kinds of memory. The faster a memory is, the smaller and costlier it is. "
        "So the machine stacks them like a ladder: tiny and fast at the top, huge and slow at the bottom. "
        "Some memory forgets everything at power-off (volatile). The rest keeps its data."
    ),
    notes=r"""### The memory ladder
Fast memory costs more, so a computer has only a little of it. It stacks the types from fast and small to slow and large.

| Level | Technology | Volatile? | Typical size |
|---|---|---|---|
| Registers | Inside the CPU | Yes | Bytes |
| **Cache** (L1, L2, L3) | **SRAM**, on or near the CPU | Yes | KB to MB |
| **Main memory** | **RAM (DRAM)** | Yes | GB |
| SSD | Flash chips | No | 100s of GB |
| Hard disk, tape | Magnetic | No | TB |

Going up the ladder means faster, costlier and smaller.

> **Tip:** Speed order is Registers, Cache, RAM, SSD, HDD, Tape. Size order is the exact reverse.

### Volatile and non-volatile
Volatile memory loses its data when the power goes off. Registers, cache and RAM are volatile.

Non-volatile memory keeps data without power. ROM, flash (SSD, pen drive, memory card), hard disk and DVD are non-volatile.

> **Rule:** ROM is never volatile. Both SRAM and DRAM are volatile.

### RAM, the working desk
RAM holds the programs and data in use right now. You can read and write it freely. Power-off wipes it.

| Type | Full form | Main facts |
|---|---|---|
| **SRAM** | Static RAM | Flip-flop cells. No refresh needed. Fast and costly. Used for **cache**. |
| **DRAM** | Dynamic RAM | One transistor and one capacitor per bit. Cheaper and denser. Used for **main memory**. |

A DRAM capacitor leaks its charge. So DRAM needs constant refreshing. SRAM does not.

### The ROM family
ROM means Read Only Memory. It is non-volatile, and ordinary programs can only read it. The family differs in how each chip is written and erased.

| Type | Written | Erased |
|---|---|---|
| PROM | Once | Never |
| **EPROM** | Reprogrammable | **Ultraviolet (UV) light** |
| **EEPROM** | Reprogrammable | **Electrically**, in the circuit |
| Flash | Reprogrammable in blocks | Electrically (fast) |

SSDs and pen drives are flash. The start-up firmware of a PC (BIOS or UEFI) sits in ROM or flash. That is why it survives every power cut.

> **Tip:** More E's mean more electricity. EPROM is erased by UV light. EEPROM is erased electrically.

### Cache and virtual memory
**Cache** is a small SRAM buffer between the CPU and RAM. It keeps copies of recently used data. So the CPU rarely waits for slow RAM. L1 is smallest and fastest. Then comes L2, then L3.

**Virtual memory** uses disk space as extra RAM when RAM is full. It is called the page file. It stops the machine from crashing. But it is far slower than real RAM.

> **Watch:** Virtual memory is not physical memory. It lives on the storage disk, not inside RAM.
""",
    tricks=[
        trick("Volatile means Vanishes",
              "Volatile memories vanish when power goes: registers, cache, RAM. Everything you keep files on (ROM, SSD, HDD, pen drive) is non-volatile.",
              "Which is volatile, ROM or DRAM?",
              ["ROM keeps data without power.", "DRAM loses data at power-off."], "DRAM"),
        trick("ROM family eraser",
              "PROM is written once. EPROM is erased by UV light. EEPROM is erased electrically. More E's, more electricity.",
              "How is EPROM erased?", ["EPROM is the UV member of the family."], "By ultraviolet light"),
        trick("Cache position",
              "Any question that says 'memory between the CPU and main memory' points to cache. L1 is inside the core and fastest.",
              "Which memory sits between the CPU and RAM?", ["It holds copies of frequently used data.", "It is built from SRAM."],
              "Cache memory"),
    ],
    mistakes=[
        mis("Calling ROM volatile.", "ROM keeps its data without power. It is non-volatile."),
        mis("Saying SRAM needs refreshing.", "DRAM needs refreshing because its capacitors leak. SRAM does not."),
        mis("Using SRAM for main memory and DRAM for cache.", "Cache uses fast, costly SRAM. Main memory uses cheaper DRAM."),
        mis("Treating virtual memory as part of RAM.", "Virtual memory is disk space used as overflow. It is slower than RAM."),
        mis("Picking cache for 'smallest and fastest'.", "Registers are smaller and faster than cache."),
    ],
    revision=[
        "Speed order: Registers, Cache (SRAM), RAM (DRAM), SSD, HDD, Tape.",
        "Volatile: registers, cache, RAM. Non-volatile: ROM, flash, disk.",
        "SRAM is for cache (fast, no refresh). DRAM is for main memory (cheap, needs refresh).",
        "PROM once, EPROM UV erase, EEPROM electrical erase, flash in blocks.",
        "BIOS or UEFI firmware sits in ROM or flash.",
        "Virtual memory is disk acting as RAM overflow, not real RAM.",
    ],
    patterns=[
        pat("hm-hie-p1", "Volatile vs non-volatile identification", "very common",
            "The words 'volatile', 'non-volatile', 'loses data when power is off' or 'permanent'.",
            ["Sort each option into volatile or non-volatile.", "Volatile: registers, cache, RAM (SRAM and DRAM).",
             "Non-volatile: ROM family, flash, magnetic disk, DVD.", "In statement questions, test each memory against this split."],
            "Only memory that needs power to hold its data is volatile.",
            "Which of the following is non-volatile?",
            ["RAM, cache and registers all lose data at power-off.", "ROM keeps its content without power."], "ROM"),
        pat("hm-hie-p2", "Hierarchy ordering and cache position", "very common",
            "'Arrange in order of speed', 'fastest', 'smallest' or 'between CPU and RAM'.",
            ["Write the order: Registers, Cache, RAM, SSD, HDD, Tape.", "Speed falls as you move right. Size grows.",
             "Cache is the SRAM buffer between CPU and RAM.", "'Smallest but fastest' means registers, not cache."],
            "Cost limits how much fast memory a machine can have.",
            "Arrange by access speed, fastest first: RAM, Registers, Hard disk, Cache.",
            ["Registers are inside the CPU, so they are fastest.", "Cache comes next, then RAM, then the hard disk."],
            "Registers, Cache, RAM, Hard disk"),
        pat("hm-hie-p3", "SRAM vs DRAM", "very common",
            "'Refresh', 'flip-flop', 'capacitor', 'static', 'dynamic' or 'used for cache'.",
            ["DRAM stores each bit in a capacitor that leaks, so it needs refreshing.", "DRAM is cheaper and denser. It is main memory.",
             "SRAM uses flip-flops. It is faster and costlier. It is cache.", "S is Static (stands still). D is Dynamic (must be refreshed)."],
            "The leaking capacitor is the reason DRAM needs refresh.",
            "DRAM needs to be refreshed periodically because...",
            ["Each DRAM bit sits in a tiny capacitor.", "The capacitor slowly loses its charge.", "So the cells are re-read and re-written again and again."],
            "Its capacitors leak charge"),
        pat("hm-hie-p4", "ROM family: PROM, EPROM, EEPROM, firmware", "common",
            "'Programmed only once', 'ultraviolet', 'electrically erasable', 'BIOS' or 'firmware'.",
            ["Match the erase method: PROM never, EPROM UV light, EEPROM electrically.", "Flash is electrically erased, in blocks.",
             "'Programmed only once' means PROM.", "BIOS or firmware lives in ROM or flash, because it must survive power cuts."],
            "Each ROM type is defined by how it is erased.",
            "Which memory holds the BIOS firmware of a PC?",
            ["Firmware must survive every power cut.", "So it cannot sit in volatile RAM."], "A ROM or flash (EEPROM-type) chip"),
        pat("hm-hie-p5", "Cache and virtual memory concepts", "common",
            "'Page file', 'overflow of RAM', 'L1, L2, L3' or 'copies of frequently used data'.",
            ["Cache is a small SRAM buffer between CPU and RAM.", "L1 is inside the core: fastest and smallest.",
             "Virtual memory is disk space used as RAM overflow.", "It is big but slow. It is not physical RAM."],
            "Cache saves the CPU from waiting. Virtual memory saves the system from running out of RAM.",
            "Virtual memory is best described as...",
            ["When RAM fills up, the OS uses disk space as an overflow area.", "That area is the page file."],
            "Disk space used as an extension of RAM"),
        pat("hm-hie-p6", "Fastest, costliest or largest memory", "occasional",
            "'Fastest memory', 'most expensive per byte' or 'largest capacity'.",
            ["Put the memories in ladder order.", "Fastest and costliest per byte is at the top: registers.",
             "Largest and cheapest per byte is at the bottom: tape and hard disk.", "Read the stem's word: fastest, smallest or largest."],
            "Speed and cost rise together. Size falls.",
            "Which memory in a computer is the fastest?",
            ["Registers are inside the CPU.", "They are the top rung of the ladder."], "Registers"),
    ],
)

# =====================================================================
# 2. Memory units
# =====================================================================
SUBS["hm-memory-units"] = dict(
    concept=(
        "Data is stored as bits. Eight bits make one byte. Each unit above the byte is 1024 times the one below it. "
        "File sizes use bytes (MB, GB). Internet speeds use bits (Mbps). Exams always test this difference."
    ),
    notes=r"""### The unit ladder
The smallest unit is the **bit**. It is one 0 or one 1. Above the byte, every step multiplies by **1024**, which is $2^{10}$.

| Unit | Equals |
|---|---|
| 1 Nibble | 4 bits |
| 1 Byte (B) | 8 bits |
| 1 KiloByte (KB) | 1024 B |
| 1 MegaByte (MB) | 1024 KB |
| 1 GigaByte (GB) | 1024 MB |
| 1 TeraByte (TB) | 1024 GB |
| 1 PetaByte (PB) | 1024 TB |

> **Rule:** Exams use 1024, never 1000.

Some exact values to remember. 1 MB is $2^{20}$ = 10,48,576 bytes. 1 GB is $2^{30}$ = 1,07,37,41,824 bytes.

### How to convert
Going up the ladder, divide by 1024. Going down, multiply by 1024.

- 4 GB to MB: 4 × 1024 = **4096 MB**.
- 2048 KB to MB: 2048 ÷ 1024 = **2 MB**.
- Bits in 2 KB: 2 × 1024 = 2048 bytes. Then 2048 × 8 = **16,384 bits**.

> **Tip:** For "which is largest", change every option to the same unit first. KB is usually easiest.

### Bits and bytes in speed questions
File sizes and storage are measured in **bytes** (MB, GB). Line speeds are measured in **bits**. Mbps means megabits per second.

Eight bits make one byte. So an 8 Mbps line moves about 1 MB of file data each second.

> **Watch:** Capital B is a byte. Small b is a bit. Mb is a megabit. MB is a megabyte.

Try a quick one. A plan says 24 Mbps. Divide by 8. You get 3 MB per second. A 30 MB file then needs 10 seconds. Always divide the size in MB by the speed in MB per second.

### Download time in three steps
Take a 10 MB file on a 16 Mbps line.

1. Change the file to bits. 10 × 8 = 80 megabits.
2. Divide by the speed. 80 ÷ 16 = 5.
3. The answer is **5 seconds**.

You can also change the speed to bytes. 16 ÷ 8 = 2 MB per second. Then 10 ÷ 2 = 5 seconds.

### Which option is largest
Take the options 1024 KB, 1 MB, 10,00,000 bytes and 0.5 GB. Put everything in KB.

| Option | In KB |
|---|---|
| 1024 KB | 1024 |
| 1 MB | 1024 |
| 10,00,000 bytes | about 977 |
| 0.5 GB | 5,24,288 |

So **0.5 GB** is the largest.

### Other units you may meet
- **Word length** is the number of bits a CPU handles in one go. A 64-bit processor has a 64-bit word.
- The smallest unit of data is the bit.
- The smallest unit of memory usually addressed is 1 byte.
- Half a byte is a nibble (4 bits). One hexadecimal digit is exactly one nibble.

### Everyday sizes
Use these to reject silly options fast.

- A phone photo is about 2 to 5 MB.
- A movie is about 1 to 4 GB.
- A good laptop SSD is about 512 GB to 1 TB.
- Internet plans are sold in Mbps. Your browser shows MB per second. An 80 Mbps line downloads near 10 MB per second.
""",
    tricks=[
        trick("The 1024 ladder",
              "Every step up multiplies by 1024 ($2^{10}$), never 1000. Half a KB is 512 B.",
              "2 GB = ? KB",
              ["2 GB = 2 × 1024 MB = 2048 MB.", "2048 MB × 1024 = 20,97,152 KB."], "20,97,152 KB (which is $2^{21}$)"),
        trick("Bit or byte speed check",
              "Line speeds are in bits (Mbps). File sizes are in bytes (MB). To get MB per second, divide Mbps by 8.",
              "A 16 Mbps line moves how many MB per second?", ["Divide the bits by 8.", "16 ÷ 8 = 2."], "2 MB per second"),
    ],
    mistakes=[
        mis("Using 1000 instead of 1024 in a ladder question.", "Exams use 1024 at every step."),
        mis("Reading Mbps as megabytes per second.", "Mbps is megabits. Divide by 8 to get MB per second."),
        mis("Multiplying by 1024 when going up the ladder.", "Going up (KB to MB) divides by 1024. Going down multiplies."),
        mis("Forgetting to multiply by 8 when a question asks for bits.", "Bytes to bits is always × 8."),
        mis("Comparing options in different units.", "Convert all options to one unit before comparing."),
    ],
    revision=[
        "Bit, Nibble (4 bits), Byte (8 bits), KB, MB, GB, TB, PB. Each step is × 1024.",
        "4 GB = 4096 MB. 2048 KB = 2 MB. 1 TB = 1024 GB.",
        "Speeds are in bits. 8 Mbps is about 1 MB per second of file data.",
        "Nibble = 4 bits = one hex digit. Smallest unit is the bit.",
        "Word length is the bits a CPU handles at once.",
    ],
    patterns=[
        pat("hm-uni-p1", "Bit, nibble and byte definitions", "very common",
            "'How many bits in...', 'nibble' or 'smallest unit'.",
            ["Remember: 1 byte = 8 bits and 1 nibble = 4 bits.", "So one byte is two nibbles.",
             "For bigger counts, multiply. Bits = bytes × 8.", "One hex digit equals one nibble."],
            "Every larger unit is built from the byte.",
            "How many bits are there in 3 bytes?",
            ["Each byte has 8 bits.", "3 × 8 = 24."], "24 bits"),
        pat("hm-uni-p2", "KB, MB, GB, TB ladder conversion", "very common",
            "'How many MB in 4 GB', 'convert KB to MB' or 'which is largest'.",
            ["Decide: are you going up or down the ladder?", "Down: multiply by 1024. Up: divide by 1024.",
             "Do it one rung at a time.", "For 'largest', change all options to one unit."],
            "Every rung of the ladder is the same factor, 1024.",
            "A pen drive holds 4 GB. How many MB is that (exam convention)?",
            ["GB to MB goes down one rung.", "4 × 1024 = 4096."], "4096 MB"),
        pat("hm-uni-p3", "Bits vs bytes in data-transfer speed", "common",
            "'Mbps', 'download time', 'per second' or 'speed of the line'.",
            ["Check the units: Mb or MB?", "Change the file to bits (× 8), or the speed to bytes (÷ 8).",
             "Divide file size by speed, in the same unit.", "8 Mbps equals 1 MB per second."],
            "Speed is measured in bits but files are measured in bytes.",
            "A connection delivers 16 Mbps. How many megabytes is that per second?",
            ["Eight bits make one byte.", "So divide 16 by 8."], "2 MB per second"),
        pat("hm-uni-p4", "Unit odd-one-out and definitions", "common",
            "'Which is NOT a unit of data size' or 'word length'.",
            ["Size units: bit, nibble, byte, KB, MB, GB, TB, PB.", "Mbps is a speed unit, not a size unit.",
             "Word length is the bits a CPU processes in one operation.", "Cross out the speed unit."],
            "Odd-one-out questions usually hide a speed unit among size units.",
            "Which of the following is NOT a unit of data size?  KB, MB, Mbps, GB",
            ["KB, MB and GB measure size.", "Mbps is megabits per second, a speed."], "Mbps"),
        pat("hm-uni-p5", "Download time and bit counts", "common",
            "'How long to download', 'how many bits in 2 KB' or 'time for a file'.",
            ["Write the file size in one unit.", "Change bytes to bits with × 8.",
             "Divide bits by the line speed in bits per second.", "Check that the units cancel."],
            "Time is size divided by speed, so both must use bits.",
            "How long will a 10 MB file take on a 16 Mbps line?",
            ["10 MB = 10 × 8 = 80 megabits.", "80 ÷ 16 = 5."], "5 seconds"),
    ],
)

# =====================================================================
# 3. Number systems
# =====================================================================
SUBS["hm-number-systems"] = dict(
    concept=(
        "A number system is a way of writing numbers with a fixed set of digits. Computers use binary (base 2). "
        "People use decimal (base 10). Octal (base 8) and hexadecimal (base 16) are short ways to write binary. "
        "Every conversion in the exam follows one of three moves: multiply and add, divide and read upward, or group bits."
    ),
    notes=r"""### The four systems
The base is the number of different digits the system uses.

| System | Base | Digits | Example |
|---|---|---|---|
| Binary | 2 | 0, 1 | 1101 |
| Octal | 8 | 0 to 7 | 65 |
| Decimal | 10 | 0 to 9 | 91 |
| Hexadecimal | 16 | 0 to 9, A to F | 2F |

In hexadecimal, A is 10, B is 11, C is 12, D is 13, E is 14 and F is 15.

### Any base to decimal
Each digit is worth digit × base^position. Count positions from 0 at the right.

$$(1101)_2 = 1\times8 + 1\times4 + 0\times2 + 1\times1 = 13$$

- $(2F)_{16} = 2\times16 + 15 = 47$.
- $(67)_8 = 6\times8 + 7 = 55$.

> **Tip:** Learn the powers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024. Then binary to decimal is just adding the places that hold a 1.

### Decimal to any base
Divide again and again by the new base. Write each remainder. Read the remainders from **bottom to top**.

For 45 in binary:

1. 45 ÷ 2 = 22, remainder **1**.
2. 22 ÷ 2 = 11, remainder **0**.
3. 11 ÷ 2 = 5, remainder **1**.
4. 5 ÷ 2 = 2, remainder **1**.
5. 2 ÷ 2 = 1, remainder **0**.
6. 1 ÷ 2 = 0, remainder **1**.

Reading upward gives $(101101)_2$. Check: 32 + 8 + 4 + 1 = 45.

### Grouping shortcut for octal and hex
One octal digit is 3 bits. One hex digit is 4 bits. Make groups **from the right**. Pad the left with zeros.

- $(1101011)_2$ becomes 001 101 011, which is 1, 5, 3. So it is $(153)_8$.
- $(11011011)_2$ becomes 1101 1011, which is D, B. So it is $(DB)_{16}$.

> **Rule:** Octal uses 3-bit groups. Hex uses 4-bit groups. Always start from the right.

### Ranges and valid digits
n bits hold $2^n$ different values, from 0 to $2^n - 1$. So 8 bits hold 256 values, from 0 to 255.

- FF in hex is 255. It is the largest 8-bit value.
- 777 in octal is 511. It is the largest 3-digit octal number.
- An octal number never has 8 or 9.
- A hex number never has a letter after F.

### More worked pairs
Use these as anchors to test your answers.

- $(1010)_2 = 8 + 2 = 10$.
- $(1111)_2 = 8 + 4 + 2 + 1 = 15$.
- $(255)_{10} = 15\times16 + 15 = (FF)_{16}$.
- $(128)_{10} = (10000000)_2$.
- $(100)_8 = 64$, $(20)_{16} = 32$, $(11)_2 = 3$.
- $(10000)_2 = 16$, because only the 16 place holds a 1.
- $(777)_8 = 7\times64 + 7\times8 + 7 = 511$.

### Quick checks on the options
Strike out options before you calculate.

1. An option with 8 or 9 is never octal.
2. An option with G or beyond is never hexadecimal.
3. A binary number ending in 0 is even. One ending in 1 is odd.

> **Watch:** Check the source base first. A digit that does not exist in that base means the option is wrong.
""",
    tricks=[
        trick("3 and 4 grouping",
              "Octal uses 3-bit groups. Hex uses 4-bit groups. Both start from the right. Pad the left with zeros. No division is needed.",
              "Write 11010111 in octal.", ["Group from the right: 011 010 111.", "Read each group: 3, 2, 7."], r"$(327)_8$"),
        trick("Hex letter wheel",
              "A = 10, B = 11, C = 12, D = 13, E = 14, F = 15. So FF = 15 × 16 + 15 = 255, which is 11111111.",
              "Find the decimal value of C8 in hex.", ["C is 12.", "12 × 16 + 8 = 200."], "200"),
        trick("Power-of-2 positions",
              "Memorise 1, 2, 4, 8, 16, 32, 64, 128. Then binary to decimal means adding the places that hold a 1.",
              "Convert 111010 to decimal.", ["The 1s are at 32, 16, 8 and 2.", "32 + 16 + 8 + 2 = 58."], "58"),
    ],
    mistakes=[
        mis("Reading the remainders from top to bottom.", "Read the remainders from bottom to top."),
        mis("Counting positions from 1 instead of 0.", "The rightmost digit is position 0. Its value is digit × 1."),
        mis("Grouping bits from the left.", "Group from the right and pad the left with zeros."),
        mis("Using 3-bit groups for hex or 4-bit groups for octal.", "Octal is 3 bits per digit. Hex is 4 bits per digit."),
        mis("Treating F as 16.", "F is 15. That is why FF is 255."),
        mis("Accepting 8 or 9 in an octal number.", "Octal digits stop at 7. Such an option is wrong."),
    ],
    revision=[
        "Bases: binary 2 (0, 1), octal 8 (0 to 7), decimal 10, hex 16 (0 to 9, A to F).",
        "To decimal: digit × base^position, positions from 0 at the right.",
        "From decimal: divide by the base, read remainders bottom to top.",
        "Octal is 3-bit groups. Hex is 4-bit groups. Group from the right.",
        "F = 15. FF = 255. 8 bits give 256 values (0 to 255).",
        "Octal has no 8 or 9. Hex has nothing after F.",
    ],
    patterns=[
        pat("hm-num-p1", "Any base to decimal", "very common",
            "'Decimal value of', 'equivalent decimal' or a number written with a subscript base.",
            ["Write the position of each digit, from 0 at the right.", "Multiply each digit by base^position.",
             "For hex, change letters to numbers first (A = 10 to F = 15).", "Add the products."],
            "Each place is worth a power of the base.",
            "The decimal value of the binary number 110101 is...",
            ["The 1s sit at 32, 16, 4 and 1.", "32 + 16 + 4 + 1 = 53."], "53"),
        pat("hm-num-p2", "Decimal to any base", "very common",
            "'Binary equivalent of', 'convert decimal to octal' or 'to hex'.",
            ["Divide the number by the target base.", "Write the remainder. Divide the quotient again.",
             "Stop when the quotient is 0.", "Read the remainders bottom to top."],
            "Each remainder is one digit of the new number, starting from the right.",
            "The binary equivalent of decimal 45 is...",
            ["The remainders in order are 1, 0, 1, 1, 0, 1.", "Read them upward: 101101.", "Check: 32 + 8 + 4 + 1 = 45."], "101101"),
        pat("hm-num-p3", "Binary to octal or hex by grouping", "very common",
            "'Binary number in octal' or 'in hexadecimal'.",
            ["Octal: group bits in 3s from the right. Hex: group in 4s.", "Pad the left with zeros.",
             "Convert each group to one digit.", "For hex, write 10 to 15 as A to F."],
            "One octal digit is exactly 3 bits. One hex digit is exactly 4 bits.",
            "The binary number 1101011 in octal is...",
            ["Group in 3s from the right: 001 101 011.", "The groups are 1, 5 and 3."], r"$(153)_8$"),
        pat("hm-num-p4", "n-bit range and digit validity", "common",
            "'How many values can n bits represent', 'largest number' or 'which is a valid octal number'.",
            ["n bits give $2^n$ different values.", "They run from 0 to $2^n - 1$.",
             "Octal digits are 0 to 7 only.", "Hex digits are 0 to 9 and A to F only."],
            "Each extra bit doubles the number of values.",
            "How many different values can be represented by 8 bits?",
            [r"Each bit has 2 choices, so the count is $2^8$.", "The largest value is one less: 255."], "256 values (0 to 255)"),
        pat("hm-num-p5", "Hex and binary conversions", "common",
            "A number with letters A to F, or 'hexadecimal equivalent'.",
            ["Turn each hex digit into a number (A = 10 to F = 15).", "For hex to decimal, use digit × 16^position.",
             "For binary to hex, group in 4s from the right.", "Change each group back to a hex digit."],
            "Hex is a short way to write binary, four bits at a time.",
            "The binary number 11011011 in hexadecimal is...",
            ["Group in 4s: 1101 and 1011.", "1101 is 13, which is D. 1011 is 11, which is B."], r"$(DB)_{16}$"),
        pat("hm-num-p6", "Largest values and anchors", "occasional",
            "'Largest 3-digit octal', 'FF in decimal' or 'value of 10000'.",
            ["Use the top digit in every place (7 for octal, F for hex).", "Multiply out by the place values.",
             "Or use the anchors: FF is 255, 777 in octal is 511.", "Check by adding 1 to reach the next power."],
            "Every base has one largest number for each number of digits.",
            "What is the decimal value of the octal number 777?",
            ["7 × 64 = 448.", "7 × 8 = 56, and 448 + 56 + 7 = 511."], "511"),
    ],
)

# =====================================================================
# 4. Input and output devices
# =====================================================================
SUBS["hm-io-devices"] = dict(
    concept=(
        "An input device sends data or commands into the computer. An output device brings results out. "
        "Some devices, such as a touch screen, do both. Exams ask you to sort devices, match each device to its job, "
        "and tell impact printers from non-impact printers."
    ),
    notes=r"""### Input devices
An input device feeds data or commands **into** the computer.

| Group | Devices |
|---|---|
| Typing and pointing | Keyboard, mouse, trackball, touchpad, joystick, light pen, stylus |
| Capture | Scanner, digital camera, webcam, microphone |
| Readers | Barcode or QR reader, OMR, OCR, MICR, biometric scanner |

> **Tip:** OMR reads **marks** (pencil bubbles). OCR reads **characters** (printed text). MICR reads **magnetic ink** on cheques.

### Output devices
An output device brings results **out** of the computer.

| Device | What it gives |
|---|---|
| **Monitor** | **Soft copy**: you can see it but not touch it |
| **Printer** | **Hard copy**: output on paper |
| Speaker, headphones | Sound |
| **Plotter** | Hard copy of large drawings and maps |
| Projector | A big soft copy on a screen |

A 3D printer builds a solid object layer by layer. It is also an output device.

### Impact and non-impact printers
An impact printer physically strikes the paper through a ribbon. A non-impact printer does not hit the paper.

| Type | How it works | Examples |
|---|---|---|
| **Impact** | Strikes the paper | Dot matrix, daisy wheel |
| **Non-impact** | Sprays ink, fuses toner or heats paper | Laser, inkjet, thermal |

Impact printers are noisy and cheap. They can print multi-copy forms. Laser printers use toner and are fast. Inkjet printers use liquid ink.

> **Rule:** If the printer hits the paper, it is impact. Dot matrix is the standard example.

### Devices that do both
A **touch screen** takes your finger as input and shows output. A headset has a microphone (input) and speakers (output).

> **Watch:** Touch screen is the standard answer to "both input and output". It is also the trap inside output-only lists.

### Pointing devices
- **Mouse:** the standard pointing device. A ball or an optical sensor tracks movement.
- **Trackball:** an upside-down mouse. You roll the ball and the device stays still.
- **Touchpad:** the flat mouse replacement on a laptop.
- **Joystick:** direction control for games and flight simulators.
- **Light pen and stylus:** draw or point directly on the screen.

Every pointing device sends position data in. So all of them are input devices.

### Device and use pairs
| Device | Classic use |
|---|---|
| Barcode reader | Supermarket billing |
| OMR | Checking pencil-bubble answer sheets |
| MICR | Reading the code line on bank cheques |
| OCR | Turning a scanned page into editable text |
| Biometric scanner | Attendance, Aadhaar-style identity checks |
| Plotter | Engineering drawings, maps, posters |
| Webcam and microphone | Video calls |
""",
    tricks=[
        trick("Marks, Characters, Ink",
              "OMR is Marks (bubbles). OCR is Characters (text). MICR is Ink on cheques (banks). Match the noun in the question.",
              "Which reader is used for bank cheques?", ["Cheques carry magnetic ink characters.", "That is MICR."], "MICR"),
        trick("Impact means hit",
              "If a printer physically hits the paper (dot matrix, daisy wheel), it is impact. It is noisy but can make copies. Inkjet, laser and thermal never strike the paper.",
              "Which is a non-impact printer: dot matrix or laser?", ["Dot matrix pins strike the ribbon.", "A laser fuses toner without hitting."], "Laser"),
    ],
    mistakes=[
        mis("Calling a scanner or microphone an output device.", "Scanner, camera and microphone send data in. They are input devices."),
        mis("Choosing 'touch screen' as output only.", "A touch screen is both input and output."),
        mis("Mixing up OMR, OCR and MICR.", "OMR is marks, OCR is characters, MICR is magnetic ink on cheques."),
        mis("Calling a laser printer an impact printer.", "Laser, inkjet and thermal printers are non-impact."),
        mis("Calling a monitor's display a hard copy.", "Monitor output is soft copy. Paper output is hard copy."),
    ],
    revision=[
        "Input: keyboard, mouse, scanner, microphone, camera, barcode, OMR, OCR, MICR, biometrics.",
        "OMR is marks. OCR is characters. MICR is magnetic ink (cheques).",
        "Output: monitor (soft copy), printer and plotter (hard copy), speaker, projector.",
        "Impact printers hit the paper (dot matrix). Non-impact are laser, inkjet and thermal.",
        "Touch screen is both input and output. A 3D printer makes solid objects.",
    ],
    patterns=[
        pat("hm-io-p1", "Input device identification", "very common",
            "'Which is an input device' or a list with one device that sends data in.",
            ["Ask: does data flow into the computer or out of it?", "Scanner, microphone and camera are input devices.",
             "Monitor, printer, speaker, plotter and projector are output devices.", "Pick the option that feeds data in."],
            "The direction of data flow decides the class.",
            "Which of the following is an input device?  Monitor, Scanner, Plotter, Speaker",
            ["Monitor, plotter and speaker all send data out.", "A scanner brings a paper document in as an image."], "Scanner"),
        pat("hm-io-p2", "Output devices, soft copy and hard copy", "very common",
            "'Soft copy', 'hard copy', 'printout' or 'displayed on screen'.",
            ["Soft copy is on a screen: monitor, projector.", "Hard copy is on paper: printer, plotter.",
             "Speaker and headphones give sound output.", "Watch for the touch screen trap."],
            "Hard copy is permanent and touchable. Soft copy is not.",
            "Output shown on paper is called a...",
            ["Paper output can be touched and kept.", "That is a hard copy."], "Hard copy"),
        pat("hm-io-p3", "Both input and output, odd one out", "common",
            "'Both input and output' or 'which is NOT an input device'.",
            ["Classify every option as input, output or both.", "Both: touch screen, headset.",
             "For 'not an input', look for a printer, monitor or speaker.", "Use the table, not guesswork."],
            "A device that takes and gives data is both.",
            "Which device acts as both an input and an output device?",
            ["Your touch is input.", "The display is output."], "Touch screen"),
        pat("hm-io-p4", "Printer types and reader classification", "common",
            "'Impact printer', 'non-impact', 'plotter' or 'OMR, OCR, MICR'.",
            ["Impact means a physical strike: dot matrix, daisy wheel.", "Non-impact: laser, inkjet, thermal.",
             "Readers: OMR marks, OCR characters, MICR magnetic ink.", "Plotter draws large drawings. A 3D printer builds objects."],
            "Each printer type is defined by how it puts marks on paper.",
            "Which of the following is an impact printer?",
            ["Dot matrix pins strike the ribbon against the paper.", "Laser, inkjet and thermal never hit the paper."], "Dot matrix"),
        pat("hm-io-p5", "Device and use matching", "common",
            "'Used for', 'used in a supermarket', 'answer sheets' or 'cheque'.",
            ["Underline the job in the question.", "Find the device with that job in the pairs table.",
             "Barcode is billing. OMR is answer sheets. MICR is cheques.", "Biometric is identity. Plotter is large drawings."],
            "Each device has one classic job in exams.",
            "Which device is used to check pencil-bubble answer sheets?",
            ["Pencil bubbles are marks.", "The reader for marks is OMR."], "OMR"),
    ],
)

# =====================================================================
# 5. Ports
# =====================================================================
SUBS["hm-ports"] = dict(
    concept=(
        "A port is a socket on the computer where a cable or device plugs in. Each port has one job, such as video, "
        "network or keyboard. Exams ask which port fits which job. Learn the job of each port and the serial and parallel difference."
    ),
    notes=r"""### What a port is
A **port** is a socket on the cabinet. A cable or device plugs into it. Every port has a job: carry video, join a network, take a keyboard.

Ask one question in the exam: what does the stem want the port to carry?

- Video: VGA, HDMI, DisplayPort.
- Network: Ethernet.
- Old keyboard and mouse: PS/2.
- Everything else today: USB.
- Sound: the 3.5 mm audio jack.

### Serial and parallel ports
| | Serial port | Parallel port |
|---|---|---|
| Bits per transfer | **One bit at a time** | **A whole byte (8 bits) at once** |
| Wires | Few | Many |
| Distance | Long, less interference | Short |
| Classic use | Old modems and mice (COM port) | Old printers (LPT port) |

> **Tip:** Serial is a single lane. Parallel is a multi-lane highway.

### The port table
| Port | Job |
|---|---|
| **USB** (Universal Serial Bus) | Pen drives, keyboards, phones. Hot-swappable. Supplies 5 V power. |
| **HDMI** | Digital video and audio in one cable |
| **VGA** | Analog video only. 15 pins, blue. No sound. |
| **DisplayPort** | Digital video and audio |
| **Ethernet (RJ-45)** | Wired network or LAN |
| **PS/2** | Round 6-pin socket for old keyboard and mouse |
| **Audio jack (3.5 mm)** | Speakers, headphones, microphone |
| **Serial (COM or RS-232)** | One-bit-at-a-time old data link |
| **Parallel (LPT)** | Old 25-pin printer port |

On the audio jack, green is for output and pink is for the microphone.

### USB facts
- **Hot-swappable** means you connect or remove it while the computer runs. No restart is needed.
- USB **supplies power**. So pen drives and small keyboards need no adapter.
- Speeds grow with each version. USB 2.0 is about 480 Mbps. USB 3.0 is about 5 Gbps.
- USB Type-C is the small, reversible oval plug on phones and laptops.

### Stem words and their answers
| Stem words | Answer |
|---|---|
| Picture and sound, one digital cable | HDMI |
| Old blue connector, video only | VGA |
| One bit at a time | Serial (COM) |
| Printer port of old machines | Parallel (LPT) |
| Network cable socket | Ethernet or RJ-45 |
| Round old keyboard and mouse sockets | PS/2 |
| Plug in without restarting | USB |
| Speakers, green round hole | 3.5 mm audio jack |

### A 10-second method
1. Underline the job in the stem: video, sound, network or data direction.
2. Match that job to a row in the port table.
3. If two options look close, drop the one that lacks a feature the stem asks for.

> **Watch:** VGA fails any stem that mentions audio. Parallel fails any stem that mentions long distance.
""",
    tricks=[
        trick("Serial is a single lane",
              "Serial sends one bit at a time over few wires. It suits long distance. Parallel sends a whole byte across 8 wires. It suits short distance, like old printers.",
              "Which port transmits one bit at a time?", ["One bit at a time means a single lane."], "Serial port"),
        trick("VGA or HDMI",
              "VGA carries video only and is analog with 15 pins. HDMI is digital and carries audio and video together. 'Sound and picture together' means HDMI.",
              "Which port carries digital audio and video?", ["VGA has no audio.", "HDMI carries both."], "HDMI"),
    ],
    mistakes=[
        mis("Saying a serial port sends 8 bits at once.", "Serial sends 1 bit at a time. Parallel sends 8 bits."),
        mis("Choosing VGA for a stem that mentions sound.", "VGA is video only. HDMI or DisplayPort carries audio too."),
        mis("Thinking VGA is digital.", "VGA is analog. HDMI and DisplayPort are digital."),
        mis("Saying you must restart to plug in USB.", "USB is hot-swappable. You plug it in while the computer runs."),
        mis("Confusing the Ethernet port with the audio jack.", "Ethernet (RJ-45) is the wide socket for the network cable. The 3.5 mm jack is for sound."),
    ],
    revision=[
        "Serial: 1 bit at a time, long distance (COM). Parallel: 8 bits at once, printers (LPT).",
        "HDMI is digital audio and video. VGA is analog video only.",
        "Ethernet (RJ-45) is for the network. PS/2 is old keyboard and mouse. 3.5 mm is audio.",
        "USB is hot-swappable and supplies power (5 V).",
        "USB 2.0 is about 480 Mbps. USB 3.0 is about 5 Gbps.",
    ],
    patterns=[
        pat("hm-por-p1", "Serial vs parallel comparison", "very common",
            "'One bit at a time', 'byte at once', 'COM port' or 'LPT port'.",
            ["Serial: 1 bit at a time, few wires, long distance.", "Parallel: 8 bits (a byte) at once, short distance.",
             "Parallel was the old printer port (LPT).", "In statements, check each number for a reversal."],
            "The two ports differ in how many bits move together.",
            "A parallel port transfers how much data per transfer?",
            ["A parallel port has 8 wires side by side.", "So a whole byte moves at once."], "A full byte (8 bits)"),
        pat("hm-por-p2", "Port identification by purpose", "very common",
            "'Which port connects...' or 'used to connect a...'.",
            ["Underline the job in the stem.", "Network: Ethernet or RJ-45.", "Digital audio and video: HDMI or DisplayPort.",
             "Old keyboard and mouse: PS/2. Speakers: 3.5 mm jack."],
            "Ports are defined by what they carry.",
            "Which port connects a computer to a wired LAN?",
            ["A LAN needs a network cable.", "That cable plugs into the RJ-45 socket."], "Ethernet port (RJ-45)"),
        pat("hm-por-p3", "USB facts", "very common",
            "'Hot-swappable', 'supplies power' or 'USB 3.0 speed'.",
            ["Hot-swappable: plug and unplug while the PC runs.", "USB carries 5 V power with the data.",
             "USB 2.0 is about 480 Mbps. USB 3.0 is about 5 Gbps.", "Type-C is the small reversible plug."],
            "USB is the universal port on modern machines.",
            "USB is called hot-swappable because...",
            ["You can connect or remove a device while the computer runs.", "No shutdown or restart is needed."],
            "It can be plugged in or removed while the computer is running"),
        pat("hm-por-p4", "Display and audio ports", "common",
            "'Analog video only', 'audio and video', 'green socket' or 'pink socket'.",
            ["VGA is analog, video only, 15 pins.", "HDMI and DisplayPort are digital and carry video and audio.",
             "On the audio jack, green is output for speakers.", "Pink is the microphone."],
            "Only HDMI and DisplayPort carry sound with video.",
            "Which port carries analog video only, with no audio?",
            ["It is the 15-pin blue connector.", "HDMI and DisplayPort are digital, so they are out."], "VGA"),
        pat("hm-por-p5", "Old ports: PS/2, COM and LPT", "occasional",
            "'Round 6-pin', 'legacy', 'RS-232' or '25-pin'.",
            ["PS/2 is a round 6-pin socket for keyboard and mouse.", "COM (RS-232) is the serial port.",
             "LPT is the 25-pin parallel printer port.", "Match the shape or pin count to the port."],
            "These ports are old, but exams still ask their names.",
            "Which port was used for the keyboard and mouse of old PCs?",
            ["It is a round 6-pin socket.", "That is the PS/2 port."], "PS/2"),
    ],
)

# =====================================================================
# 6. Storage
# =====================================================================
SUBS["hm-storage"] = dict(
    concept=(
        "Primary memory (RAM and cache) is fast but small. Secondary storage is large, permanent and cheaper per GB. "
        "Secondary storage comes in three kinds: magnetic, optical and flash. Exams ask capacities, the HDD and SSD difference, and backup methods."
    ),
    notes=r"""### Primary and secondary storage
Primary memory (RAM and cache) is fast but small. RAM is also volatile. Secondary storage is large and permanent. It costs less per GB. Everything below is secondary storage.

### The three technologies
| Family | How it stores | Examples |
|---|---|---|
| **Magnetic** | Magnetised spots on spinning platters or tape | HDD, old floppy, magnetic tape (LTO) |
| **Optical** | Tiny pits read by a **laser** | CD, DVD, Blu-ray |
| **Flash** | Memory chips with no moving parts | SSD, pen drive, memory card, phone storage |

### Optical disc capacities
This row is the exam favourite.

| Disc | Capacity (single layer) | Laser |
|---|---|---|
| **CD** | **700 MB** | Infrared or red |
| **DVD** | **4.7 GB** (dual layer about 8.5 GB) | Red |
| **Blu-ray** | **25 GB** (dual layer about 50 GB) | **Blue-violet** |

The order is CD (0.7 GB), then DVD (4.7 GB), then Blu-ray (25 GB). A blue-violet laser has a shorter wavelength. So it reads tighter pits and stores more data.

> **Tip:** Remember "700, 4.7, 25". A CD holding 4.7 GB should feel wrong at once.

### HDD and SSD
| | HDD | SSD |
|---|---|---|
| Parts | Spinning magnetic platters and moving heads | Flash chips, no moving parts |
| Speed | Slower (heads must seek) | Much faster |
| Shock and noise | Sensitive, some noise | Shock-resistant, silent |
| Cost per GB | Cheaper | Costlier |

> **Rule:** "No moving parts" in a question means SSD.

### Choosing a medium
- Need speed, silence and shock resistance: SSD.
- Need cheap bulk storage: HDD.
- Need to keep archives for years at low cost: magnetic tape.
- Need to carry small files: pen drive or memory card.

### Access methods
- **Random (direct) access:** jump straight to any address. RAM, HDD and SSD work this way.
- **Sequential access:** read in order, like a cassette. Magnetic tape works this way.

Tape is cheap. So it suits archival backups, not daily use.

### Backup ideas
- **Cloud storage or backup:** your files are copied to internet servers. You can reach them from anywhere.
- **Tape libraries:** banks and research labs still archive petabytes on tape.
- **The 3-2-1 habit:** three copies, on two media, with one copy off-site.

### Small facts exams quote
- A **floppy disk** stored 1.44 MB. It is obsolete but still asked.
- A **memory card** is flash storage for cameras and phones (SD, microSD).
- Blu-ray gets its name from the blue-violet laser.
- **Formatting** prepares a disk's file system. It does not add capacity.
- Everyday anchors: an MP3 song is about 4 to 8 MB. A phone holds about 64 to 256 GB.
""",
    tricks=[
        trick("Optical capacity ladder",
              "CD is 700 MB. DVD is 4.7 GB. Blu-ray is 25 GB (single layer). Say it as '700, 4.7, 25'.",
              "What is the capacity of a single-layer DVD?", ["The DVD is the middle rung of the ladder."], "4.7 GB"),
        trick("SSD or HDD in one line",
              "SSD has no moving parts. It is silent, shock-proof, faster and costlier per GB. HDD has spinning platters and gives cheap bulk storage.",
              "Which storage has no moving parts?", ["Flash chips have nothing that spins."], "SSD (solid state drive)"),
    ],
    mistakes=[
        mis("Giving 4.7 GB as the capacity of a CD.", "A CD holds 700 MB. 4.7 GB is a DVD."),
        mis("Calling a hard disk an optical medium.", "A hard disk is magnetic. CD, DVD and Blu-ray are optical."),
        mis("Saying an SSD has spinning platters.", "An SSD uses flash chips. HDDs have the platters."),
        mis("Thinking tape gives random access.", "Tape is sequential. Disks and SSDs are random access."),
        mis("Thinking formatting adds capacity.", "Formatting only prepares the file system."),
    ],
    revision=[
        "Magnetic: HDD, tape. Optical: CD, DVD, Blu-ray. Flash: SSD, pen drive, memory card.",
        "CD 700 MB, DVD 4.7 GB (dual 8.5 GB), Blu-ray 25 GB (dual 50 GB).",
        "Blu-ray uses a blue-violet laser.",
        "SSD has no moving parts and is faster and costlier. HDD is cheaper per GB.",
        "Tape is sequential and used for archival backup. Disk and SSD are random access.",
        "Cloud backup keeps copies on internet servers. A floppy held 1.44 MB.",
    ],
    patterns=[
        pat("hm-sto-p1", "Optical media capacity matching", "very common",
            "'Capacity of a CD, DVD or Blu-ray' or 'blue-violet laser'.",
            ["Recall the row: CD 700 MB, DVD 4.7 GB, Blu-ray 25 GB.", "Dual layer: DVD about 8.5 GB, Blu-ray about 50 GB.",
             "For ordering, use CD, then DVD, then Blu-ray.", "Blue-violet laser means Blu-ray."],
            "Shorter laser wavelength packs data tighter.",
            "A single-layer DVD stores about...",
            ["The 700 MB figure is a CD.", "25 GB is Blu-ray."], "4.7 GB"),
        pat("hm-sto-p2", "HDD vs SSD vs flash", "very common",
            "'No moving parts', 'faster', 'spinning platters' or 'shock-resistant'.",
            ["HDD: spinning magnetic platters and heads.", "SSD and pen drive: flash chips, no moving parts.",
             "SSD is faster, silent and shock-resistant.", "Flash keeps data without power."],
            "Moving parts make an HDD slower than an SSD.",
            "Why is an SSD faster than an HDD?",
            ["An SSD has no platters to spin.", "It has no heads to seek."], "It has no mechanical parts"),
        pat("hm-sto-p3", "Backup and access methods", "common",
            "'Sequential', 'random access', 'archival' or 'cloud backup'.",
            ["Archival backup: magnetic tape, cheapest per TB.", "Sequential means read in order (tape).",
             "Random means jump to any address (disk, SSD).", "Copies on internet servers are cloud backup."],
            "Access method decides how fast a medium finds data.",
            "Which storage medium uses sequential access?",
            ["The drive must wind past earlier data.", "Disks and SSDs jump directly instead."], "Magnetic tape"),
        pat("hm-sto-p4", "Media odd-one-out and matching", "common",
            "'Which is NOT an optical medium' or 'match the medium to its type'.",
            ["Optical: CD, DVD, Blu-ray.", "Magnetic: HDD, floppy, tape.",
             "Flash: SSD, pen drive, memory card.", "Find the option that breaks the family."],
            "Each medium belongs to exactly one family.",
            "Which of the following is NOT an optical storage medium?  CD, DVD, Hard disk, Blu-ray",
            ["CD, DVD and Blu-ray are read by lasers.", "A hard disk is magnetic."], "Hard disk"),
        pat("hm-sto-p5", "Primary vs secondary storage", "occasional",
            "'Secondary storage', 'permanent', 'primary memory' or 'formatting'.",
            ["Primary memory: RAM and cache. Fast and small.", "Secondary storage: disks, tape, flash. Large and permanent.",
             "Formatting prepares the file system only.", "Use everyday sizes to reject silly options."],
            "Primary is for speed. Secondary is for keeping data.",
            "Which of these is secondary storage?  RAM, Cache, SSD, Registers",
            ["RAM, cache and registers are primary memory.", "An SSD keeps data without power."], "SSD"),
    ],
)

# =====================================================================
# write back
# =====================================================================
def long_lines(text, limit=30):
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
        assert 3 <= len(p["steps"]) <= 5 and 1 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:80])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
