# -*- coding: utf-8 -*-
"""Topic 2: hardware-memory. All number-conversion answers computed + asserted."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

# ---- computational verification of every numeric answer used below ----
assert int("1011011", 2) == 91
assert bin(58)[2:] == "111010"
o = oct(int("11010111", 2))[2:]; assert o == "327" and int("11010111", 2) == 215
assert int("2F", 16) == 47
assert hex(200)[2:].upper() == "C8" and int("C8", 16) == 200
assert int("65", 8) == 53
assert bin(156)[2:] == "10011100"
assert 2**20 == 1048576 and 2**14 == 16384 and 2**10 == 1024 and 2**30 == 1073741824
assert 4 * 1024 == 4096            # 4 GB in MB
assert int("777", 8) == 511        # largest 3-digit octal
assert int("FF", 16) == 255
assert int("1010", 2) == 10 and int("1111", 2) == 15
assert 512 == 0.5 * 1024           # half KB
assert int("A", 16) == 10 and int("1A3", 16) == 419

T = {
  "id": "hardware-memory",
  "sectionId": "computer",
  "title": "Hardware, Memory & Number Systems",
  "order": 2,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 3},
  "summary": "Memory hierarchy and units, binary/octal/decimal/hex conversions, input-output devices, ports and storage media. Number-conversion and memory-unit questions are near-guaranteed marks because they need no theory recall - only method.",
  "subtopics": [
    {
      "id": "hm-memory-hierarchy",
      "title": "Memory hierarchy, RAM/ROM and cache",
      "concept": """Storage is arranged by speed vs cost vs size. Going up the ladder: faster, costlier, smaller.

| Level | Example | Volatile? | Typical size |
|---|---|---|---|
| Registers | Inside CPU | Yes | Bytes |
| Cache (L1/L2/L3) | SRAM on/near CPU | Yes | KB - MB |
| Main memory | RAM (DRAM) | Yes | GB |
| Solid-state storage | SSD, pen drive | No | GB - TB |
| Magnetic/optical | HDD, DVD | No | GB - TB |
| Archival | Magnetic tape, cloud cold storage | No | TB - PB |

**RAM (volatile - contents vanish at power-off):** **SRAM** - fast, costly, no refresh, used for cache; **DRAM** - slower, cheap, needs constant refreshing, used for main memory.

**ROM (non-volatile, firmware):** PROM (programmed once) -> EPROM (erased by **UV light**) -> EEPROM (erased **electrically**; the BIOS chip is EEPROM/flash). **Flash memory** (pen drives, SSDs) is electrically erasable like EEPROM but block-wise.

**Cache memory** sits between CPU and RAM and keeps copies of frequently used data (L1 smallest/fastest, L3 largest/slowest of the three). **Virtual memory** uses a disk area (page file) as an overflow extension of RAM - slow but lets big programs run.""",
      "formulas": [],
      "tricks": [
        {"title": "Volatile = Vanishes", "body": "**V**olatile memories **V**anish when power goes: registers, cache, RAM. Everything you *keep files on* (ROM, SSD, HDD, pen drive) is non-volatile.", "example": {"q": "Which is volatile - ROM or DRAM?", "solution": "DRAM. ROM = Read Only Memory 'Remembers' even without power."}},
        {"title": "ROM family eraser", "body": "P**ROM** (once) -> **EP**ROM (**E**rase with **P**hotons = UV) -> **EEP**ROM (**E**lectrically Erasable). The more E's, the more Electrical.", "example": {"q": "How is EPROM erased?", "solution": "Exposure to ultraviolet light through the quartz window."}},
        {"title": "Cache position", "body": "Cache is the CPU's personal notepad between CPU and RAM: L1 inside the core (fastest), then L2, then L3 shared. Any question 'memory between CPU and main memory' = cache.", "example": {"q": "Memory placed between CPU and RAM?", "solution": "Cache memory (SRAM)."}}
      ],
      "mistakes": [
        "Calling ROM volatile - RAM is volatile, ROM is not.",
        "Saying cache is bigger than RAM - cache is tiny but fast.",
        "Believing virtual memory is physical RAM - it is disk space acting as RAM overflow."
      ]
    },
    {
      "id": "hm-memory-units",
      "title": "Memory units and conversions",
      "concept": """The ladder (exam convention: each step is x1024):

| Unit | Equals | Value in bytes |
|---|---|---|
| 1 bit | smallest unit (0 or 1) | - |
| 1 Nibble | 4 bits | - |
| 1 Byte | 8 bits | 1 |
| 1 KiloByte (KB) | 1024 B | 2^10 |
| 1 MegaByte (MB) | 1024 KB | 2^20 = 1,048,576 B |
| 1 GigaByte (GB) | 1024 MB | 2^30 = 1,07,37,41,824 B |
| 1 TeraByte (TB) | 1024 GB | 2^40 |
| 1 PetaByte (PB) | 1024 TB | 2^50 |
| 1 ExaByte (EB) | 1024 PB | 2^60 |

A **word** is the number of bits a CPU handles at once (16/32/64-bit). Careful: lowercase **b = bit**, uppercase **B = byte** - 1 Mbps (megabit/s) = 0.125 MB/s. (Purists use KiB/MiB for the 1024-based values; SSC uses the KB = 1024 B convention.)""",
      "formulas": [
        {"name": "Step multiplier", "tex": "1\\ \\text{unit}_{next} = 2^{10} = 1024\\ \\text{units}_{prev}", "note": "KB->MB->GB->TB->PB all multiply by 1024"},
        {"name": "Byte identity", "tex": "1\\ \\text{Byte} = 8\\ \\text{bits},\\quad 1\\ \\text{Nibble} = 4\\ \\text{bits}", "note": "half a byte = nibble"},
        {"name": "Common ladders", "tex": "1\\ \\text{GB} = 1024\\ \\text{MB} = 2^{20}\\ \\text{KB} = 2^{30}\\ \\text{B}", "note": "4 GB = 4096 MB = 2^22 KB"},
        {"name": "bits vs bytes", "tex": "1\\ \\text{MB} = 8\\ \\text{Mb}", "note": "capital B = byte, small b = bit (speeds are usually bits)"}
      ],
      "tricks": [
        {"title": "x1024 ladder", "body": "Every step up multiplies by **1024** (2^10), never 1000 in SSC convention. 4 GB = 4 x 1024 = **4096 MB**. Half a KB = **512 B**.", "example": {"q": "2 GB = ? KB", "solution": "2 x 1024 x 1024 = 2^21 = 2,048 KB x 1024 = 20,97,152 KB - or 2^21 KB."}},
        {"title": "Bit-vs-byte speed check", "body": "Line speeds are in **bits** (Mbps), file sizes in **bytes** (MB). To convert a download speed to MB/s, divide by 8: 8 Mbps = 1 MB/s.", "example": {"q": "16 Mbps line - max MB downloaded per second?", "solution": "16/8 = 2 MB per second."}}
      ],
      "mistakes": [
        "Using 1000 instead of 1024 for unit steps in exam questions.",
        "Confusing Mb (megabit) with MB (megabyte) in speed questions.",
        "Saying a nibble is 8 bits - a nibble is 4 bits (half a byte)."
      ]
    },
    {
      "id": "hm-number-systems",
      "title": "Number systems: binary, octal, decimal, hexadecimal",
      "concept": """| System | Base | Digits | Example |
|---|---|---|---|
| Binary | 2 | 0,1 | 1101 |
| Octal | 8 | 0-7 | 65 |
| Decimal | 10 | 0-9 | 91 |
| Hexadecimal | 16 | 0-9, A-F (A=10 ... F=15) | 2F |

**Any base -> decimal:** multiply each digit by (base)^position, counting positions from 0 at the right. Example: 1011011 = 1x2^6 + 0x2^5 + 1x2^4 + 1x2^3 + 0x2^2 + 1x2^1 + 1x2^0 = 64+16+8+2+1 = **91**.

**Decimal -> base b:** repeatedly divide by b and read remainders **bottom to top**. 58 -> binary: 58/2=29 r0, 29/2=14 r1, 14/2=7 r0, 7/2=3 r1, 3/2=1 r1, 1/2=0 r1 -> **111010**.

**Binary -> octal:** group bits in **3s from the right** (each octal digit = 3 bits). 11010111 -> 011 010 111 -> **327**.

**Binary -> hexadecimal:** group bits in **4s from the right**. 10101111 -> 1010 1111 -> **AF**.

**Hex/octal -> binary:** expand each digit into 4/3 bits. **Hex -> decimal:** digits x 16^position (2F = 2x16 + 15 = **47**).

ASCII anchors: 'A'=65, 'B'=66, ..., 'Z'=90; 'a'=97; '0'=48. Largest 8-bit binary value 11111111 = **255**.""",
      "formulas": [
        {"name": "Positional value", "tex": "N = \\sum d_i \\cdot b^{i}", "note": "digit d_i at position i (from 0, rightmost), base b"},
        {"name": "Decimal to base b", "tex": "N = (\\ldots r_2 r_1 r_0)_b\\ \\text{from repeated division by } b", "note": "read remainders bottom to top"},
        {"name": "Grouping shortcuts", "tex": "1\\ \text{octal digit} \\leftrightarrow 3\\ \text{bits},\\quad 1\\ \text{hex digit} \\leftrightarrow 4\\ \text{bits}", "note": "group binary from the RIGHT; pad with leading zeros"}
      ],
      "tricks": [
        {"title": "3-4 grouping", "body": "**Octal = 3-bit groups, Hex = 4-bit groups**, always made **from the right** (pad the left with zeros). Binary -> octal/hex needs no division at all.", "example": {"q": "11010111 in octal?", "solution": "011 010 111 -> 3 2 7 = 327."}},
        {"title": "Hex letter wheel", "body": "A=10, B=11, C=12, D=13, E=14, F=15. So 2F = 2x16+15 = 47; FF = 15x16+15 = **255** = 11111111. 'F fills: F=15, FF=255'.", "example": {"q": "Decimal value of C8?", "solution": "12x16 + 8 = 200."}},
        {"title": "Power-of-2 positions", "body": "Memorise 1,2,4,8,16,32,64,128 - then any binary->decimal is just picking positions: 11010111 = 128+64+16+8+4+2+1 = 215. No working needed beyond addition.", "example": {"q": "111010 in decimal?", "solution": "32+16+8+2 = 58."}}
      ],
      "mistakes": [
        "Grouping binary digits from the LEFT for octal/hex - groups always start at the right end.",
        "Treating hex A-F as invalid digits or computing 2F as 2x10+15.",
        "Reading division remainders top-to-bottom - the answer reads bottom-to-top.",
        "Forgetting 0-7 are legal octal digits; an option containing 8 or 9 cannot be octal."
      ]
    },
    {
      "id": "hm-io-devices",
      "title": "Input and output devices",
      "concept": """**Input devices** feed data to the CPU: keyboard, mouse, trackball, joystick, light pen, touch screen, scanner, digital camera, webcam, microphone, barcode/QR reader, biometric (fingerprint/retina) scanner, stylus, and the classic readers:

| Device | Reads | Used in |
|---|---|---|
| OMR (Optical Mark Recognition) | Pencil/ink marks (bubbles) | OMR answer sheets, surveys |
| OCR (Optical Character Recognition) | Printed/written characters into editable text | Digitising documents |
| MICR (Magnetic Ink Character Recognition) | Iron-oxide ink characters | Cheque processing (9-digit code) |
| Barcode reader | Parallel black-white bars | Shops, libraries |

**Output devices:** monitor/VDU (CRT -> LCD/LED/OLED), printer, plotter, speaker, projector, headphone.

**Printers:** **Impact** (physical strike - Dot Matrix, Daisy Wheel; noisy, carbon-copy possible) vs **Non-impact** (no strike - **Inkjet** (sprays ink), **Laser** (electrophotographic, fast, office standard), Thermal (bills, ATMs)). **Plotter** draws large precise hard copies (engineering drawings).

**Both input & output:** touch screen, modem, network card, headsets with mic, and storage devices generally.""",
      "formulas": [],
      "tricks": [
        {"title": "Mark-Character-Ink", "body": "**OMR = Marks** (bubbles), **OCR = Characters** (text), **MICR = Ink on cheques** (banks). Marks, Characters, Ink - match the noun in the question.", "example": {"q": "Bank cheque reading uses?", "solution": "MICR - magnetic ink characters."}},
        {"title": "Impact = hit", "body": "If the printer physically *hits* paper (dot matrix, daisy wheel) it is impact - noisy but makes carbon copies. Inkjet/Laser/Thermal never touch with force: non-impact.", "example": {"q": "Which is a non-impact printer - Dot Matrix or Laser?", "solution": "Laser (dot matrix strikes the ribbon)."}}
      ],
      "mistakes": [
        "Marking a touch screen as input-only - it is both input and output.",
        "Calling MICR an optical technology - it reads magnetic ink.",
        "Saying plotters are for office documents - plotters are for large-format drawings/graphs."
      ]
    },
    {
      "id": "hm-ports",
      "title": "Ports and connectors",
      "concept": """A port is an interface on the cabinet for connecting peripherals.

| Port | Purpose / notes |
|---|---|
| Serial (COM/RS-232) | Sends **one bit at a time**; suits slow data over long distances; old modems/mice |
| Parallel (LPT, 25-pin) | Sends **8 bits (a byte) at once**; traditional printer port; short distance |
| PS/2 | 6-pin round; keyboard (purple) & mouse (green); legacy |
| USB | Universal Serial Bus; hot-swappable, power + data. USB 2.0 = 480 Mbps, USB 3.x = 5-20 Gbps; Type-A/B/C |
| VGA (DB-15) | **15-pin, analog video only** to monitors/projectors |
| DVI | Digital video (older digital standard) |
| HDMI | **Digital audio + video** in one cable; TVs/monitors |
| DisplayPort | Digital audio + video, daisy-chaining; PCs |
| Thunderbolt | Combines DisplayPort + PCIe over USB-C; very high speed |
| Ethernet (RJ-45) | Wired LAN |
| Audio jacks (3.5 mm) | Green = line-out/speakers, Pink = mic, Blue = line-in |
| Game port / FireWire (IEEE 1394) | Legacy joystick; high-speed media, superseded by USB |

**Hot-swappable** = connect/disconnect while the PC runs (USB, FireWire) - serial/parallel ports are not.""",
      "formulas": [],
      "tricks": [
        {"title": "Serial = Single lane", "body": "**S**erial sends a **S**ingle stream (1 bit at a time, slow, long distance); **P**arallel sends a **P**acket (whole byte across 8 wires, fast, short distance - old printers).", "example": {"q": "Which port transmits one bit at a time?", "solution": "Serial port."}},
        {"title": "VGA vs HDMI", "body": "**V**GA = **V**ideo only (15 pins, analog); **HDMI** = **H**ome-theatre cable: **audio + video**, digital. If the question says 'sound and picture together' -> HDMI.", "example": {"q": "Which port carries digital audio and video?", "solution": "HDMI."}}
      ],
      "mistakes": [
        "Calling VGA capable of audio - VGA is video-only.",
        "Saying serial ports are faster than parallel - parallel moves a byte per transfer (over short runs).",
        "Forgetting USB is hot-swappable - that phrase in the question usually points to USB."
      ]
    },
    {
      "id": "hm-storage",
      "title": "Storage and backup media",
      "concept": """| Medium | Technology | Capacity (typical) |
|---|---|---|
| Hard Disk Drive (HDD) | Magnetic platters, spinning | 500 GB - 20 TB |
| SSD / NVMe | Flash chips, no moving parts | 128 GB - 8 TB, much faster than HDD |
| CD-ROM | Optical, 1 side | ~700 MB |
| DVD (single layer) | Optical | **4.7 GB** (dual-layer 8.5 GB) |
| Blu-ray (single layer) | Blue-violet laser | **25 GB** (dual 50 GB) |
| Pen drive / SD card | Flash | GBs - TBs |
| Magnetic tape (LTO) | Sequential magnetic | TBs per cartridge; archival backup |
| Cloud storage | Remote servers | TB plans; off-site backup |

Optical discs store bits as pits/lands read by laser; the shorter the wavelength (IR -> red -> blue-violet), the denser the storage (CD -> DVD -> Blu-ray). **Backup rule of thumb:** keep at least one copy **off-site** and on a different medium than the live data. **NAS** (Network Attached Storage) gives shared disk over the LAN.""",
      "formulas": [],
      "tricks": [
        {"title": "Optical capacity ladder", "body": "**CD 700 MB -> DVD 4.7 GB -> Blu-ray 25 GB** (single layer). Roughly: CD 0.7, DVD 4.7, BR 25 - '700, 4.7, 25'.", "example": {"q": "Storage capacity of a single-layer DVD?", "solution": "4.7 GB."}},
        {"title": "SSD vs HDD one-liner", "body": "SSD = **no moving parts** (flash), silent, shock-proof, faster, costlier per GB. HDD = spinning platters, cheap bulk storage. 'No moving parts' in a question = SSD.", "example": {"q": "Which storage has no moving parts?", "solution": "Solid State Drive (flash memory)."}}
      ],
      "mistakes": [
        "Quoting 700 MB for a DVD - that is a CD; a single-layer DVD is 4.7 GB.",
        "Saying Blu-ray uses a red laser - Blu-ray uses the shorter blue-violet laser.",
        "Believing tape is obsolete - LTO tape is still standard for archival backups."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Memory-unit ladder conversion", "frequency": "very common", "howToSpot": "'1 GB = ? MB', 'How many KB make 4 GB?' - pure x1024 arithmetic.", "approach": "Multiply/divide by 1024 per step; keep powers of 2 (2^10, 2^20, 2^30) ready."},
    {"pattern": "Binary/decimal/hex/octal conversion", "frequency": "very common", "howToSpot": "'Convert 1011011 to decimal', 'hexadecimal 2F = ?' - one short computation per question.", "approach": "Use positional powers for to-decimal, repeated division for from-decimal, and 3/4-bit grouping for binary-octal-hex."},
    {"pattern": "Port/device identification", "frequency": "common", "howToSpot": "'Which port transmits one bit at a time?', 'which carries audio and video?'.", "approach": "Serial=1-bit stream, Parallel=byte, VGA=video-only analog, HDMI=audio+video digital, USB=hot-swappable."},
    {"pattern": "Printer/device classification", "frequency": "common", "howToSpot": "'Which is a non-impact printer?' or 'OMR is used for?'.", "approach": "Impact = physical strike (dot matrix, daisy wheel); non-impact = inkjet/laser/thermal. OMR marks, OCR characters, MICR cheque ink."},
    {"pattern": "Volatile memory / ROM family", "frequency": "common", "howToSpot": "'Which memory loses data on power failure?', 'EPROM is erased by?'.", "approach": "Volatile = registers/cache/RAM; EPROM=UV, EEPROM=electrical; ROM family is non-volatile."}
  ],
  "solvedExamples": [
    Q("hm-se01",
      "What is the decimal equivalent of the binary number 1011011?",
      ["87", "89", "91", "93"], 2,
      "Write positional powers of 2 under the digits: 1x64 + 0x32 + 1x16 + 1x8 + 0x4 + 1x2 + 1x1 = 64+16+8+2+1 = 91.",
      "Powers row 64 32 16 8 4 2 1; pick the positions with 1s: 64+16+8+2+1 = 91. (Verified computationally.)",
      "medium", "hm-number-systems", "binary to decimal conversion", 45),
    Q("hm-se02",
      "The decimal number 58 in binary is:",
      ["111010", "110110", "101110", "111100"], 0,
      "Repeated division by 2: 58->29 r0, 29->14 r1, 14->7 r0, 7->3 r1, 3->1 r1, 1->0 r1. Reading remainders bottom to top: 111010. Check: 32+16+8+2 = 58.",
      "Subtract powers of 2 from 58: 32 leaves 26, 16 leaves 10, 8 leaves 2, 2 leaves 0 -> bits at 32,16,8,2 -> 111010.",
      "medium", "hm-number-systems", "decimal to binary conversion", 50),
    Q("hm-se03",
      "The octal equivalent of the binary number 11010111 is:",
      ["327", "315", "647", "326"], 0,
      "Group the bits in threes from the right: 011 010 111. Convert each group: 011=3, 010=2, 111=7, giving 327 (octal). Cross-check: 327 in octal = 3x64+2x8+7 = 215 = value of 11010111 in decimal.",
      "3-bit groups from the right; pad the left with zero. Octal digits can never include 8 or 9 - that kills two options instantly.",
      "medium", "hm-number-systems", "binary to octal grouping", 50),
    Q("hm-se04",
      "How many megabytes are there in 4 GB (exam convention)?",
      ["1024", "2048", "4096", "8192"], 2,
      "1 GB = 1024 MB, so 4 GB = 4 x 1024 = 4096 MB. In powers of two: 4 GB = 2^2 x 2^30 B = 2^32 B = 2^22 KB x 1024 = 4096 MB.",
      "Each ladder step is x1024, so GB->MB is just 4 x 1024 = 4096. Options 1024/2048/8192 are the x1024 answers for 1, 2 and 8 GB - read the question's number carefully.",
      "easy", "hm-memory-units", "memory-unit ladder", 35),
    Q("hm-se05",
      "Which of the following devices reads the characters printed at the bottom of bank cheques using magnetic ink?",
      ["OCR", "OMR", "MICR", "Barcode reader"], 2,
      "MICR (Magnetic Ink Character Recognition) reads the 9-digit code printed in iron-oxide ink along a cheque's bottom strip. OCR reads ordinary printed text, OMR reads pencil marks/bubbles, barcode readers read retail bar patterns.",
      "Cheque -> MICR (Ink). Marks -> OMR. Characters -> OCR. Bars -> barcode.",
      "easy", "hm-io-devices", "input-device identification", 30)
  ],
  "practice": [
    Q("hm-q01",
      "A nibble consists of how many bits?",
      ["2", "4", "8", "16"], 1,
      "A nibble is half a byte: 4 bits. A byte is 8 bits; a word is CPU-dependent (16/32/64 bits).",
      "Nibble = half a byte = 4 bits ('nybble nibbles off half').",
      "easy", "hm-memory-units", "memory-unit definition", 25),
    Q("hm-q02",
      "Which of the following is a volatile memory?",
      ["ROM", "DRAM", "PROM", "SSD"], 1,
      "DRAM (dynamic RAM) loses its contents the moment power is cut. The ROM family (PROM, EPROM, EEPROM) and flash-based SSDs are non-volatile.",
      "Volatile = Vanishes: registers, cache, RAM. Everything with 'ROM' or flash in the name stays put.",
      "easy", "hm-memory-hierarchy", "volatile memory identification", 30),
    Q("hm-q03",
      "The small, very fast memory placed between the CPU and main memory is:",
      ["Virtual memory", "Cache memory", "Buffer register", "CMOS memory"], 1,
      "Cache (usually SRAM, levels L1-L3) stores frequently used data between the CPU and RAM. Virtual memory is disk-based overflow; buffers smooth I/O transfers; CMOS holds BIOS settings.",
      "'Between CPU and RAM' is the exact address of cache.",
      "easy", "hm-memory-hierarchy", "memory hierarchy position", 30),
    Q("hm-q04",
      "EPROM differs from PROM because it can be erased by:",
      ["Electrical signals", "Ultraviolet light", "Magnetic field", "X-rays"], 1,
      "EPROM (Erasable Programmable ROM) is erased by exposing the quartz window to ultraviolet light. PROM cannot be erased once programmed; EEPROM is the electrically erasable version.",
      "One E = light (EPROM, UV); two E's = electricity (EEPROM).",
      "medium", "hm-memory-hierarchy", "ROM family differences", 35),
    Q("hm-q05",
      "The decimal value of the binary number 111010 is:",
      ["54", "56", "58", "60"], 2,
      "32+16+8+0+2+0 = 58.",
      "Powers 32 16 8 4 2 1; pick 1-positions: 32+16+8+2 = 58.",
      "easy", "hm-number-systems", "binary to decimal conversion", 40),
    Q("hm-q06",
      "The binary equivalent of decimal 156 is:",
      ["10011100", "10100110", "11001100", "10010110"], 0,
      "156 = 128+16+8+4, so bits at 2^7, 2^4, 2^3, 2^2: 10011100. Division check: 156->78 r0, 78->39 r0, 39->19 r1, 19->9 r1, 9->4 r1, 4->2 r0, 2->1 r0, 1->0 r1 -> bottom-up 10011100.",
      "Subtract 128 first (156-128 = 28), then 16 (12), then 8 (4), then 4 (0): bits 128,16,8,4 = 10011100.",
      "medium", "hm-number-systems", "decimal to binary conversion", 50),
    Q("hm-q07",
      "The decimal number 200 in hexadecimal is:",
      ["B8", "C8", "C9", "D8"], 1,
      "200 = 12x16 + 8 = C8 (C = 12).",
      "Divide by 16: 200/16 = 12 r 8 -> C8. The remainder is the last hex digit, the quotient the first.",
      "medium", "hm-number-systems", "decimal to hexadecimal conversion", 45),
    Q("hm-q08",
      "The hexadecimal number 2F equals which decimal number?",
      ["37", "45", "47", "57"], 2,
      "2F = 2x16^1 + 15x16^0 = 32 + 15 = 47 (F = 15).",
      "F=15: so 32+15 = 47. Options built from F=5, 7 or 13 are the traps.",
      "easy", "hm-number-systems", "hexadecimal to decimal conversion", 40),
    Q("hm-q09",
      "The largest decimal number that can be stored in 8 binary bits is:",
      ["127", "128", "255", "256"], 2,
      "11111111 = 2^8 - 1 = 255. (256 needs 9 bits; 127 is the largest for 7-bit or the max of a signed 8-bit byte.)",
      "n bits -> largest unsigned value 2^n - 1. 8 bits -> 255.",
      "easy", "hm-number-systems", "range of n-bit numbers", 35),
    Q("hm-q10",
      "Which input device is used to evaluate answers marked with pencil bubbles on an OMR answer sheet?",
      ["OCR", "OMR", "MICR", "Plotter"], 1,
      "OMR (Optical Mark Recognition) detects the presence/absence of marks in fixed positions - exactly the bubble-sheet use case.",
      "Bubbles/marks -> OMR. Printed text -> OCR. Cheques -> MICR. Plotter is an output device.",
      "easy", "hm-io-devices", "input-device identification", 30),
    Q("hm-q11",
      "Which of the following is a non-impact printer?",
      ["Dot Matrix printer", "Daisy Wheel printer", "Laser printer", "Ball printer"], 2,
      "Laser printers form images with electrostatic toner - no physical strike - so they are non-impact (as are inkjet and thermal). Dot matrix and daisy wheel strike an inked ribbon.",
      "Impact family is short: dot matrix + daisy wheel. Almost every other printer is non-impact.",
      "easy", "hm-io-devices", "printer classification", 30),
    Q("hm-q12",
      "A hard copy of large engineering drawings is best produced on a:",
      ["Laser printer", "Plotter", "Thermal printer", "Scanner"], 1,
      "Plotters draw precise, large-format line art (A0/A1 sheets) with a pen or cutting head - standard for CAD output. Printers handle page-size documents; a scanner is an input device.",
      "Drawings/CAD/large sheets -> plotter.",
      "easy", "hm-io-devices", "output-device selection", 30),
    Q("hm-q13",
      "Which port carries digital audio and video signals over a single cable to a monitor or TV?",
      ["VGA", "PS/2", "HDMI", "Serial COM"], 2,
      "HDMI transmits uncompressed digital video plus audio in one cable. VGA is analog video-only, PS/2 is for keyboard/mouse, and serial COM ports carry slow bit-serial data.",
      "Audio AND video together -> HDMI (or DisplayPort, if listed).",
      "medium", "hm-ports", "port identification", 35),
    Q("hm-q14",
      "The port that transmits data one bit at a time as a single stream, traditionally used for slow data over long distances, is the:",
      ["Parallel port", "Serial port", "SCSI port", "FireWire port"], 1,
      "A serial port (COM/RS-232) sends bits sequentially over one channel - slower but reliable over longer cable runs. Parallel ports send a byte across 8 wires simultaneously but only over short distances.",
      "'One bit at a time / single stream' = serial, word for word.",
      "easy", "hm-ports", "serial vs parallel port", 30),
    Q("hm-q15",
      "Which statement about SSDs and HDDs is correct?",
      ["SSDs use spinning magnetic platters", "HDDs have no moving parts", "SSDs use flash memory with no moving parts", "HDDs are always faster than SSDs"], 2,
      "An SSD stores data in NAND flash chips with no mechanical parts, making it faster and shock-resistant; an HDD stores data magnetically on spinning platters with a moving head, and is slower but cheaper per GB.",
      "'No moving parts' -> SSD, always. Any option giving moving parts to SSD or calling HDD faster is upside down.",
      "easy", "hm-storage", "SSD vs HDD", 35)
  ]
}

validate_and_dump_topic(T)
