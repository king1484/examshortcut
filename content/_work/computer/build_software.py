# -*- coding: utf-8 -*-
"""Topic 3: software-os"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

T = {
  "id": "software-os",
  "sectionId": "computer",
  "title": "Software & Operating Systems",
  "order": 3,
  "importance": "medium",
  "avgQuestions": {"tier1": 0, "tier2": 2},
  "summary": "System vs application vs utility software, what an OS does, Windows features, and file systems. Classification (odd-one-out) questions are the most frequent pattern here.",
  "subtopics": [
    {
      "id": "so-types",
      "title": "Types of software: system, application, utility",
      "concept": """| Class | What it does | Examples |
|---|---|---|
| System software | Runs/manages the machine itself | Operating systems (Windows, Linux, macOS, Android), device drivers, firmware/BIOS |
| Utility software | Maintains, protects, optimises | Antivirus, disk defragmenter, disk cleanup, backup tools, compressors (WinZip/7-Zip), file manager |
| Application software | User tasks | General purpose: MS Office, browsers, media players; Custom/application-specific: payroll system, railway reservation |

**Licence classes:** Freeware (free to use, source closed - Adobe Reader), Shareware (free trial, pay later - WinZip), Open source (source code available - Linux, LibreOffice, Firefox), Proprietary (paid licence - MS Office). **Firmware** is software burned into hardware (BIOS chip).""",
      "formulas": [],
      "tricks": [
        {"title": "SUApp test", "body": "Ask: does it **S**erve the machine (system), **U**nclog/maintain it (utility), or do the user's **App**-job (application)? Windows = system, antivirus = utility, Excel = application.", "example": {"q": "Disk Defragmenter is which type?", "solution": "Utility software - it maintains disk performance."}},
        {"title": "Licence 4-word key", "body": "**F**reeware = **F**ree forever (closed source); **S**hareware = **S**ample first (trial); **O**pen source = **O**pen code; **P**roprietary = **P**ay.", "example": {"q": "Linux is?", "solution": "Open-source software."}}
      ],
      "mistakes": [
        "Counting device drivers as application software - they are system software.",
        "Calling antivirus an operating system - it is a utility.",
        "Assuming freeware is open source - freeware is free of cost but source stays closed."
      ]
    },
    {
      "id": "so-os-functions",
      "title": "Operating system functions, types and booting",
      "concept": """An **Operating System** is the system software that manages hardware and provides the platform for applications.

**Functions:** process management (CPU scheduling of tasks), memory management (allocating RAM, virtual memory), file management (folders, FAT32/NTFS), device management (via drivers), security (users, passwords, permissions), user interface (GUI/CLI), error handling, networking and resource allocation. The **kernel** is the core of the OS that always stays in memory.

**Types:** single-user single-task (old DOS), single-user multi-task (Windows desktop), multi-user (UNIX/Linux servers), multiprogramming (several programs in RAM; CPU switches when one waits for I/O), multitasking, **time-sharing** (CPU time slices among users), **real-time (RTOS)** (guaranteed response within deadlines - missiles, robots, medical devices), distributed (many networked machines acting as one), embedded, mobile (Android - Linux kernel based; iOS; Windows).

**Booting** = starting the OS. **Cold boot** = power-on from off; **Warm boot** = restart without cutting power. Sequence: power-on -> **POST** (Power-On Self-Test) -> BIOS/UEFI finds the boot device -> boot loader loads the **kernel** -> login screen.""",
      "formulas": [],
      "tricks": [
        {"title": "PMF-SUIE services", "body": "OS gives six services: **P**rocess, **M**emory, **F**ile, **S**ecurity, **U**I, **E**rror handling. 'Manage + platform' answers are OS; anything computing payroll is application.", "example": {"q": "Which OS service allocates RAM to programs?", "solution": "Memory management."}},
        {"title": "Boot words", "body": "**C**old boot = **C**urrent was off (switched on from cold); **W**arm boot = **W**ithout power cut (restart). POST always comes first: 'Power On, Self-Test, then load'.", "example": {"q": "Restarting a running computer is?", "solution": "Warm booting."}}
      ],
      "mistakes": [
        "Calling the shell/GUI the kernel - the kernel is the in-memory core; the shell is its outer interface.",
        "Saying multiprogramming means several CPUs - it is one CPU juggling several resident programs.",
        "Ordering the boot loader before POST - POST always runs first."
      ]
    },
    {
      "id": "so-windows-features",
      "title": "Windows OS features",
      "concept": """Microsoft Windows (Windows 10, 2015; Windows 11, 2021) is a single-user, multitasking, GUI-based OS.

| Feature | Meaning |
|---|---|
| GUI | Windows, Icons, Menus, Pointer (WIMP) instead of typed commands |
| Multitasking | Many programs run concurrently (preemptive scheduling) |
| Plug and Play (PnP) | New hardware is detected and configured automatically |
| File Explorer (Windows Explorer) | File/folder management shell (Win+E) |
| Control Panel / Settings | System configuration (Settings app in Win 10/11) |
| Task Manager | Processes, performance, startup (Ctrl+Shift+Esc) |
| Recycle Bin | Deleted files held here; Shift+Delete skips it (permanent) |
| Device Manager | Lists/controls hardware and drivers |
| Disk Management | Partition, format drives; Disk Cleanup/Defragmenter utilities |
| Windows Defender | Built-in antivirus/firewall; Windows Update keeps patches current |
| Command Prompt / PowerShell | CLI interfaces for typed commands |
| User accounts | Administrator vs Standard; login password/PIN |
| Virtual desktops / Snap | Multiple desktops (Win+Ctrl+D); window snapping (Win+arrow) |
| OneDrive / BitLocker | Cloud sync; disk encryption (BitLocker in Pro editions) |

Accessories: Notepad (plain text), WordPad (rich text, removed in Win 11), Paint, Calculator, Snipping Tool.""",
      "formulas": [],
      "tricks": [
        {"title": "PnP = Plug 'n' Pray-free", "body": "Plug and Play means the OS auto-detects and auto-configures new hardware - no driver hunt. The phrase 'automatically detected' in a question = PnP.", "example": {"q": "Windows feature that configures a newly attached printer automatically?", "solution": "Plug and Play."}},
        {"title": "Task Manager 3-2-Esc", "body": "Fastest route to Task Manager: **Ctrl+Shift+Esc** (direct). Ctrl+Alt+Del only opens the security menu first. 'Direct' is what SSC tests.", "example": {"q": "Shortcut that opens Task Manager directly?", "solution": "Ctrl+Shift+Esc."}}
      ],
      "mistakes": [
        "Believing Recycle Bin catches everything - Shift+Delete bypasses it, and flash-drive deletes often skip it too.",
        "Confusing File Explorer (files) with Internet Explorer/Edge (browser).",
        "Thinking Notepad saves rich formatting - Notepad is plain text only."
      ]
    },
    {
      "id": "so-file-systems",
      "title": "File systems and file management",
      "concept": """A file system defines how an OS names, stores and retrieves files on a volume.

| File system | Used by | Key facts |
|---|---|---|
| FAT32 | Windows 9x, pendrives | Max file size **4 GB** (minus 1 byte); max volume ~32 GB (Windows format limit); no permissions/journaling |
| exFAT | Flash drives, cameras | Removes FAT32's 4-GB file limit; lightweight |
| NTFS | Modern Windows | Journaling (crash-safe), file/folder **permissions/encryption**, huge files, compression; default for Windows installs |
| ext4 | Linux | Journaling; default on many distros |
| APFS | macOS/iOS | Snapshots, encryption |

File management terms: file (named collection of related data), folder/directory (container), path (drive:\\folders\\file.ext), file name + extension (name.type), attributes (read-only, hidden, archive, system), wildcard characters **?** (one character) and ***** (any characters) used in searches. Format = preparing a disk with a file system (erases the directory, not physically shredding data).""",
      "formulas": [],
      "tricks": [
        {"title": "FAT32's four-wall", "body": "**FAT32 cannot hold a single file bigger than 4 GB** - the classic exam line. NTFS breaks that wall and adds security permissions + journaling.", "example": {"q": "A 5-GB video won't copy to a FAT32 pendrive because?", "solution": "FAT32 limits file size to 4 GB; use NTFS/exFAT."}},
        {"title": "Wildcards", "body": "In Windows search, **?** masks exactly one character and ***** masks any number: `*.docx` finds all Word files, `s?t` finds sat/set/sit.", "example": {"q": "Wildcard for 'any number of characters' in file search?", "solution": "The asterisk *."}}
      ],
      "mistakes": [
        "Reversing the limits: 4-GB single-file cap belongs to FAT32, not NTFS.",
        "Saying formatting improves disk capacity - formatting only lays down the file system.",
        "Using ? for many characters - ? is exactly one, * is any."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Software classification odd-one-out", "frequency": "very common", "howToSpot": "'Which of the following is NOT system software?' or options mixing an OS with apps and utilities.", "approach": "Tag each option: runs the machine (system), maintains it (utility), does user work (application), then pick the odd tag."},
    {"pattern": "OS function/feature match", "frequency": "common", "howToSpot": "'Which OS component allocates memory?' / 'Plug and Play means?'.", "approach": "Recall the six services and Windows feature table; match the verb in the question (allocates = memory mgmt, schedules = process mgmt, detects hardware = PnP)."},
    {"pattern": "Booting and POST", "frequency": "occasional", "howToSpot": "'Cold vs warm boot', 'first step when the computer starts'.", "approach": "Cold = power-on from off, Warm = restart; order is always POST -> boot loader -> kernel."},
    {"pattern": "File-system limits", "frequency": "occasional", "howToSpot": "'Maximum file size on FAT32?' / 'Which file system supports encryption?'.", "approach": "FAT32 = 4 GB file wall, no security; NTFS = permissions, journaling, encryption."}
  ],
  "solvedExamples": [
    Q("so-se01",
      "Which of the following is NOT an operating system?",
      ["Windows 11", "Linux", "Oracle", "Android"], 2,
      "Oracle is a database management system (application software). Windows 11, Linux and Android are operating systems (Android is built on the Linux kernel).",
      "Scan for a DBMS/browser/office-suite name hiding among OS names - DBMS, Photoshop, Chrome are never operating systems.",
      "easy", "so-types", "odd-one-out classification", 30),
    Q("so-se02",
      "Arrange the booting steps in order:\nA. POST  B. Kernel loads  C. Boot loader runs  D. Power switched on",
      ["A-D-C-B", "D-A-C-B", "D-A-B-C", "D-C-A-B"], 1,
      "Power on (D) triggers the POST self-test (A), then the firmware hands control to the boot loader (C), which loads the OS kernel (B).",
      "POST always precedes the loader; the kernel always comes last. Only D-A-C-B satisfies both.",
      "easy", "so-os-functions", "boot-sequence ordering", 35),
    Q("so-se03",
      "Disk Defragmenter, Disk Cleanup and WinZip are examples of:",
      ["Operating systems", "Utility software", "Application software", "Programming languages"], 1,
      "All three maintain or organise the system - defragmenting files, clearing junk, compressing archives - which is the definition of utility software.",
      "If the tool's job is 'clean, compress, protect, back up', it is a utility, not an application.",
      "easy", "so-types", "utility software identification", 30),
    Q("so-se04",
      "Statement 1: NTFS supports file-level security permissions.\nStatement 2: A FAT32 volume can store a single file larger than 4 GB.",
      ["Only 1 is correct", "Only 2 is correct", "Both correct", "Both incorrect"], 0,
      "NTFS provides per-file/folder permissions, encryption and journaling, so Statement 1 is correct. FAT32 caps any single file at 4 GB (minus 1 byte), so Statement 2 is wrong - large files need NTFS or exFAT.",
      "Remember the 'four-wall' of FAT32; any statement letting FAT32 hold >4-GB files is false.",
      "medium", "so-file-systems", "file-system facts", 40)
  ],
  "practice": [
    Q("so-q01",
      "Which of the following is system software?",
      ["MS PowerPoint", "Windows 11", "Adobe Photoshop", "Tally"], 1,
      "Windows 11 is an operating system - system software that manages the machine. PowerPoint, Photoshop and Tally are application programs that run on top of an OS.",
      "The OS is the platform everything else installs on; look for Windows/Linux/macOS/Android among the options.",
      "easy", "so-types", "system vs application software", 30),
    Q("so-q02",
      "An antivirus program is best classified as:",
      ["Application software", "Utility software", "System software", "Firmware"], 1,
      "Antivirus maintains and protects the system, which places it in utility software (along with defragmenters, backup tools, compressors).",
      "'Protect/maintain/clean' verbs -> utility. Antivirus is the most-asked utility example.",
      "easy", "so-types", "utility software identification", 30),
    Q("so-q03",
      "The core part of an operating system that remains permanently in main memory is the:",
      ["Shell", "Kernel", "BIOS", "Boot sector"], 1,
      "The kernel is the OS core - it manages CPU, memory and devices and always stays resident in RAM. The shell is the user interface layer; BIOS is motherboard firmware; the boot sector merely starts the loading process.",
      "Kernel = king in the castle (always resident); shell = gate you talk to.",
      "easy", "so-os-functions", "OS structure", 30),
    Q("so-q04",
      "Restarting a computer without switching off the power is called:",
      ["Cold booting", "Warm booting", "Cold starting", "Shut down"], 1,
      "Warm booting (restart) reloads the OS without removing power. Cold booting means starting from a fully powered-off state.",
      "Warm = restart (machine stays 'warm'); cold = switch on from off.",
      "easy", "so-os-functions", "booting types", 30),
    Q("so-q05",
      "Which OS service decides which waiting program gets the CPU next?",
      ["Memory management", "Process scheduling", "File management", "Device management"], 1,
      "Process management (scheduling) shares CPU time among ready processes. Memory management allocates RAM, file management handles storage, device management drives peripherals.",
      "Verb match: 'gets the CPU' -> process scheduling; 'gets RAM' -> memory management.",
      "medium", "so-os-functions", "OS function matching", 35),
    Q("so-q06",
      "A real-time operating system (RTOS) is most appropriate for:",
      ["Preparing a payroll", "Controlling a missile guidance system", "Browsing the web", "Designing a poster"], 1,
      "An RTOS guarantees a response within a strict deadline - essential in missiles, robotics, medical devices and plant control. Payroll, browsing and design have no hard deadlines.",
      "Life-or-deadline control jobs -> RTOS; office jobs -> general-purpose OS.",
      "medium", "so-os-functions", "OS type selection", 35),
    Q("so-q07",
      "Multiprogramming means:",
      ["Several CPUs in one computer", "Several programs kept in memory with the CPU switching among them", "Several users sharing one password", "Several monitors on one PC"], 1,
      "In multiprogramming, multiple programs reside in main memory and the single CPU switches to another whenever the current one waits (e.g. for I/O), raising CPU utilisation. It does not require multiple CPUs or users.",
      "One CPU, many resident programs = multiprogramming; time-sliced fairness = time-sharing.",
      "medium", "so-os-functions", "OS concepts", 40),
    Q("so-q08",
      "The Windows feature that automatically detects and configures a newly connected USB printer is:",
      ["Plug and Play", "Hot swapping", "Disk mirroring", "Overclocking"], 0,
      "Plug and Play lets the OS identify new hardware, install its driver and configure it without manual setup. Hot swapping is only the connect/disconnect-while-running part; overclocking raises clock speed; mirroring is disk redundancy.",
      "'Automatically detects AND configures' = Plug and Play.",
      "easy", "so-windows-features", "Windows features", 30),
    Q("so-q09",
      "Deleting a file with Shift+Delete in Windows Explorer:",
      ["Moves it to Recycle Bin", "Deletes it permanently without moving it to Recycle Bin", "Renames the file", "Compresses the file"], 1,
      "Shift+Delete bypasses the Recycle Bin and permanently deletes the file (after confirmation). Plain Delete sends it to the Recycle Bin.",
      "Add Shift = skip the bin. That single fact answers most Recycle-Bin questions.",
      "easy", "so-windows-features", "Windows features", 30),
    Q("so-q10",
      "Which utility shows running processes, CPU/RAM usage and startup programs in Windows?",
      ["Device Manager", "Task Manager", "Disk Management", "Event Viewer"], 1,
      "Task Manager (Ctrl+Shift+Esc) displays processes, performance graphs, startup impact and lets you end tasks. Device Manager lists hardware/drivers; Disk Management handles partitions; Event Viewer logs system events.",
      "Running apps + performance = Task Manager; hardware + drivers = Device Manager.",
      "easy", "so-windows-features", "Windows tools", 30),
    Q("so-q11",
      "Notepad, the basic Windows text editor, saves files as:",
      ["Rich text with fonts", "Plain text (ANSI/UTF-8) only", "Word documents", "PDF files"], 1,
      "Notepad writes plain text with no bold/italic formatting - its default extension is .txt. Formatted text needs WordPad or a word processor.",
      "No formatting = Notepad; any option promising fonts/bold is WordPad/Word territory.",
      "easy", "so-windows-features", "Windows accessories", 30),
    Q("so-q12",
      "The maximum size of a single file on a FAT32 volume is:",
      ["2 GB", "4 GB", "16 GB", "No limit"], 1,
      "FAT32 cannot store any single file larger than 4 GB (minus 1 byte); NTFS and exFAT lift this limit. This is why pendrives formatted as FAT32 reject large videos.",
      "The 'four-wall' of FAT32: 4 GB per file, straight recall.",
      "medium", "so-file-systems", "file-system limits", 35),
    Q("so-q13",
      "In a Windows file search, the pattern *report*.xlsx will find:",
      ["Only files named exactly report.xlsx", "All .xlsx files whose names contain the word report", "All files of any type containing report", "Only files starting with report"], 1,
      "The asterisk matches any number of characters, so *report*.xlsx matches any Excel workbook with 'report' anywhere in its name - e.g. annual-report-2026.xlsx and report-final.xlsx.",
      "Prefix * = anything before, suffix * = anything after; .xlsx at the end restricts the type.",
      "medium", "so-file-systems", "wildcard search", 40),
    Q("so-q14",
      "Android, the mobile operating system, is built on which kernel?",
      ["Windows NT", "Linux", "UNIX BSD", "Mach"], 1,
      "Android uses the Linux kernel at its core with Java/Kotlin application layers on top - a standard exam fact.",
      "Android = Linux kernel; iOS/macOS = Darwin (UNIX-based).",
      "medium", "so-os-functions", "OS facts", 35)
  ]
}

validate_and_dump_topic(T)
