"""Phase-2 deep content for computer/hardware-memory. Run: py -3 hardware-memory.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from hm_part1 import build_hierarchy, build_units, build_number_systems
from hm_part2 import build_io, build_ports, build_storage


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Memory-unit ladder conversion", "very common",
      "'4 GB = how many MB?', 'bits in a byte/nibble', 'which is largest: 1024 KB / 1 MB / …', or a speed question mixing megabits with megabytes.",
      "Convert step by step with the ×1024 ladder (bit → byte → KB → MB → GB → TB), never 1000. For speed questions, remember line speeds are in bits: divide Mbps by 8 to get megabytes per second. For 'which is largest', convert every option to one unit first.",
      "hm-memory-units",
      "How many MB are there in 2 GB?",
      "2 × 1024 = 2048 MB — each step up the ladder multiplies by 1024."),
    P("Binary/decimal/hex/octal conversion", "very common",
      "'The decimal value of (1101)₂', 'the binary equivalent of 45', '(11011011)₂ in hexadecimal', 'how many values can 8 bits represent'.",
      "Base→decimal: digit × base^position from the right. Decimal→base: divide repeatedly and read remainders bottom-to-top. Binary→octal/hex: group in 3s or 4s from the right. Always verify by converting back. Digit validity is a free elimination: no 8/9 in octal, nothing after F in hex.",
      "hm-number-systems",
      "The binary equivalent of decimal 45 is:",
      "Divide by 2 and read remainders upward: 101101. Check: 32+8+4+1 = 45."),
    P("Volatile memory / ROM family", "common",
      "'Which is volatile?', 'EPROM is erased by…', 'where is the BIOS stored?', 'SRAM vs DRAM refresh', 'cache lies where?'.",
      "Volatile = vanishes with power (registers, cache, RAM). Non-volatile = ROM family, flash, disk. ROM ladder: PROM once → EPROM (UV) → EEPROM (electrically) → flash. SRAM = cache (no refresh); DRAM = main memory (needs refresh); virtual memory = disk overflow, not RAM.",
      "hm-memory-hierarchy",
      "EPROM differs from PROM because it can be erased by:",
      "Ultraviolet light — EEPROM goes one step further and erases electrically."),
    P("Port/device identification", "common",
      "'Which port carries audio + video?', 'one bit at a time', 'RJ-45 is for…', 'hot-swappable means…', 'which port for the old keyboard?'.",
      "Port table recall: HDMI = digital video + audio, VGA = analog video only, Ethernet/RJ-45 = network, PS/2 = old keyboard/mouse, USB = universal + hot-swap + power. Serial = 1 bit at a time over long runs; parallel = 8 bits, the old printer (LPT) port.",
      "hm-ports",
      "Which port connects a computer to a wired LAN?",
      "The Ethernet port (RJ-45) — the tabbed socket for the network cable."),
    P("Printer/device classification", "common",
      "'Which is an impact printer?', 'OMR/OCR/MICR reads what?', 'plotter is used for', '3D printer produces'.",
      "Impact = physically strikes (dot matrix, daisy wheel); non-impact = laser, inkjet, thermal. Readers by one word: OMR marks, OCR characters, MICR magnetic ink on cheques. Plotter = large drawings; 3D printer = solid objects layer by layer.",
      "hm-io-devices",
      "Which is an impact printer?",
      "Dot matrix — its pins strike the ribbon against the paper; laser and inkjet never hit."),
    P("Input/output device classification", "common",
      "'Which is an input device?', 'which is NOT an input device?', 'soft copy vs hard copy', 'which device is both input and output?'.",
      "Direction test: data flowing INTO the computer = input (keyboard, mouse, scanner, mic, readers, biometrics); results OUT = output (monitor, printer, speaker, plotter, projector). Soft copy = screen; hard copy = paper. Touch screen does both — the standard both-direction answer.",
      "hm-io-devices",
      "A printout on paper is called a:",
      "Hard copy — permanent output; a monitor's display is a soft copy."),
    P("Storage media identification", "common",
      "'Capacity of a CD/DVD/Blu-ray', 'which storage has no moving parts', 'sequential access example', 'match medium to technology'.",
      "Capacity row: CD 700 MB, DVD 4.7 GB (dual 8.5), Blu-ray 25 GB with its blue-violet laser. Technology families: magnetic (HDD, tape), optical (CD/DVD/BD), flash (SSD, pen drive, card). Tape = sequential access, archival; disk/SSD = random access; SSD beats HDD on speed, loses on cost per GB.",
      "hm-storage",
      "A single-layer Blu-ray disc stores about:",
      "25 GB — its short-wavelength blue-violet laser packs far more data than a DVD's red laser."),
]

if __name__ == "__main__":
    subs = [build_hierarchy(), build_units(), build_number_systems(),
            build_io(), build_ports(), build_storage()]
    apply_topic("hardware-memory", subs, PYQ)
