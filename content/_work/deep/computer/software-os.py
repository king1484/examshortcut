"""Phase-2 deep content for computer/software-os. Run: py -3 software-os.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from so_part1 import build_types, build_os_functions
from so_part2 import build_windows, build_file_systems


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Software classification odd-one-out", "very common",
      "A list mixes an operating system, utilities and applications and asks which is not like the others, or names one program (antivirus, driver, Word) and asks its class.",
      "Apply the SUApp test to each option: serves the machine = system (OS, driver, BIOS, compiler), maintains it = utility (antivirus, defragmenter, zip), does the user's work = application (Word, Chrome, games). The odd option is always the one serving a different master.",
      "so-types",
      "Disk Defragmenter, Antivirus, MS Excel, Disk Cleanup — which one is different?",
      "MS Excel — the other three are utilities that maintain the machine; Excel is an application that does the user's work."),
    P("OS function/feature match", "common",
      "'Which service allots RAM / chooses the next CPU task / manages folders?', 'multiprogramming vs time-sharing vs real-time', 'kernel vs shell'.",
      "Match the job to the service: CPU turn = process scheduling, RAM = memory management, folders = file management, passwords = security. For OS types, use the keywords: deadline = real-time, time slices = time-sharing, many programs resident = multiprogramming. Kernel stays in memory; the shell is only the interface.",
      "so-os-functions",
      "Which OS type guarantees a response within a fixed deadline?",
      "Real-time operating system (RTOS) — used in missile control, pacemakers and industrial robots where a late answer is a failure."),
    P("Booting and POST", "occasional",
      "'What happens first when the computer starts?', 'restarting without power off is called', 'arrange POST, boot loader, kernel, login'.",
      "Fix the order: POST (Power-On Self-Test from the BIOS) → boot loader → kernel loads into RAM → login screen. Cold boot = from powered-off; warm boot = restart without cutting power. Any option placing the boot loader before POST is wrong.",
      "so-os-functions",
      "Restarting a running computer through the Restart option is:",
      "Warm booting — the power stays on; a cold boot starts from a powered-off state."),
    P("File-system limits", "occasional",
      "'Maximum single-file size on FAT32', 'why won't this movie copy to my pen drive', 'which file system has permissions/journaling', 'default file system of Windows'.",
      "Three-column memory: FAT32 = 4 GB per file, pendrives; exFAT = FAT32 without the 4-GB wall, big flash media; NTFS = Windows default with permissions and journaling. Scenario stems about a big movie hiding the 4-GB FAT32 ceiling are the most common form.",
      "so-file-systems",
      "The default file system for the C: drive of a modern Windows PC is:",
      "NTFS — New Technology File System, with permissions, journaling and huge file support."),
    P("Windows tool and feature identification", "common",
      "'Which tool shows CPU usage / stuck programs?', 'which feature auto-detects new hardware?', 'where do you change settings?', 'Notepad vs WordPad'.",
      "Tool map: stuck program or CPU/RAM figures → Task Manager (Ctrl+Shift+Esc); hardware and drivers → Device Manager; settings → Control Panel/Settings; junk files → Disk Cleanup. Feature map: auto-detect hardware → Plug and Play; WIMP → GUI. Notepad = plain text, WordPad = formatted text.",
      "so-windows-features",
      "Which Windows tool lists installed hardware with its driver status?",
      "Device Manager — every component appears with its driver; problem devices carry a warning mark."),
    P("Mobile and desktop OS basics", "occasional",
      "'Android is developed by / based on which kernel?', 'iOS runs on which devices?', 'which OS is open source?', 'match OS to maker'.",
      "Pin the pairs: Android = Google, Linux kernel, open-source core, many brands; iOS = Apple only, closed source; Windows = Microsoft; macOS = Apple; Linux = open source (Linus Torvalds). Statement versions usually swap the kernel or the owner.",
      "so-windows-features",
      "The Android operating system is built on which kernel?",
      "The Linux kernel — Google's Android layers its own system and apps over Linux."),
]

if __name__ == "__main__":
    subs = [build_types(), build_os_functions(), build_windows(), build_file_systems()]
    apply_topic("software-os", subs, PYQ)
