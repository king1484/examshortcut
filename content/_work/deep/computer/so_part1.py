"""software-os deep content — part 1: software types, OS functions/types/booting."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_types():
    S = Sub("so-types")
    S.notes = """### The three classes of software
Every program on earth falls into one of three boxes. Ask one question: **who is the program serving?**

| Class | Serves | Examples |
|---|---|---|
| **System software** | The machine itself — runs and manages the hardware | Operating systems (Windows, Linux, macOS, Android), **device drivers**, **firmware/BIOS**, language translators (compiler, interpreter, assembler) |
| **Utility software** | Maintenance of the machine — clean, protect, repair, organise | Antivirus, **disk defragmenter**, disk cleanup, backup tools, file compressors (WinZip, 7-Zip, WinRAR), file manager, screen saver |
| **Application software** | The user's task | MS Word, Excel, PowerPoint, browsers (Chrome), Photoshop, games, WhatsApp, Tally |

Memory test — the **SUApp** test: does it **S**erve the machine (system), **U**nclog it (utility), or do the **user's App** work (application)?

Two boundary points exams love:
- A **device driver** is system software, even though you install it like an app — it teaches the OS to talk to one piece of hardware (printer, graphics card).
- A **utility** keeps the machine healthy but does not produce user documents; an **application** produces the user's output.

### Utility software — the maintenance crew
| Utility | Job |
|---|---|
| Antivirus | Finds and removes malware |
| Disk Defragmenter | Rejoins scattered pieces of files on a hard disk so reading is faster |
| Disk Cleanup | Deletes temporary and junk files to free space |
| Backup utility | Keeps a second copy of important data |
| Compression tool (WinZip, 7-Zip) | Shrinks files into smaller .zip archives and opens them |
| File manager | Copies, moves, renames and organises files |

### Licence types (one-mark favourites)
| Type | Meaning | Example |
|---|---|---|
| **Freeware** | Free of cost, but **source code stays closed** | Adobe Reader |
| **Shareware** | Free **trial** for a limited time or features, then pay | Trial antivirus |
| **Open source** | Source code is available; free to use and modify | **Linux**, LibreOffice, VLC |
| **Proprietary** | Paid licence, closed source | Windows, MS Office |

Trap: freeware is free of **cost** but not open **source** — the two ideas are different.

### Quick revision
- System = machine (OS, drivers, BIOS, translators); Utility = maintenance (antivirus, defrag, cleanup, backup, zip); Application = user's task (Word, Chrome, games).
- Drivers and firmware are system software, not applications.
- Freeware = free cost, closed source. Open source = source available (Linux, VLC).
- Shareware = try first, pay later."""
    S.pattern("so-typ-p1", "System vs application vs utility classification", "very common",
        "A program is named (Word, antivirus, driver, Windows, Photoshop) and its class is asked, or a list is given with 'which is not like the others'.",
        None,
        "1. Apply the SUApp test: serves the machine = system; maintains it = utility; does the user's task = application.\n2. Drivers, BIOS/firmware and translators are system software — the classic traps that look like apps.\n3. In odd-one-out, find the one program that serves a different master (three applications + one OS, or three utilities + one game).",
        "Which of the following is **application** software?",
        "**MS Word** — it does the user's task (documents). Windows is an OS, a driver serves hardware, antivirus is a utility.")
    S.pattern("so-typ-p2", "Utility identification by job", "very common",
        "A maintenance job is described — rearranging scattered files, removing malware, shrinking files, freeing disk space, keeping a second copy — and the utility is asked.",
        None,
        "1. Match job to crew member: scattered-file pieces → Defragmenter; junk/temporary files → Disk Cleanup; malware → Antivirus; second copy → Backup; smaller archive → Zip/7-Zip.\n2. 'Faster disk reading' on a hard disk points to defragmentation, not formatting.\n3. Freeing *space* = cleanup; speeding up *access* = defragmenter.",
        "Which utility joins the scattered pieces of a file spread across a hard disk so it opens faster?",
        "**Disk Defragmenter** — it rearranges fragments into contiguous blocks. Disk Cleanup only deletes junk; it does not rearrange anything.")
    S.pattern("so-typ-p3", "Licence types: freeware / shareware / open source / proprietary", "common",
        "'Linux is which type of software?', 'software free for a trial period is called', 'freeware vs open source' statements.",
        None,
        "1. Four boxes: freeware = free cost + closed source; shareware = trial then pay; open source = source available (Linux, VLC); proprietary = paid + closed (Windows, MS Office).\n2. The standard trap: 'freeware is open source' — false, cost and source are different things.\n3. Linux is the default open-source example in every exam.",
        "Linux is distributed as —",
        "**Free and open-source software** — its source code is public and can be used, modified and redistributed under its licence.")
    S.pattern("so-typ-p4", "Odd one out: which is / is not an operating system", "common",
        "A list mixes operating systems (Windows, Linux, macOS, Android) with applications and browsers; the odd one is asked.",
        None,
        "1. Know the OS list cold: Windows, Linux, macOS, Android, iOS, Unix, Chrome OS.\n2. Everything else famous — Word, Chrome, Firefox, Photoshop, WhatsApp — is an application, not an OS.\n3. For 'mismatched pair' versions, test each pair: is the left item really the right kind of thing?",
        "Which pair is **mismatched**?",
        "**Firefox – operating system** — Firefox is a web browser. Linux, Android and macOS are all genuine operating systems.")

    S.q("so-typ-p1", "easy", "Which of the following is **application** software?",
        ["Windows 11", "Device driver", "MS PowerPoint", "Disk Defragmenter"], "MS PowerPoint",
        "**MS PowerPoint** produces the user's slides — an application. Windows 11 is an OS, a driver is system software, and the Defragmenter is a utility.",
        "Serves the user's task = application.", 20)
    S.q("so-typ-p1", "medium", "A small program that teaches the operating system how to communicate with a newly attached **printer** is —",
        ["Application software", "Utility software", "A device driver (system software)", "Firmware in the printer's cartridge"], "A device driver (system software)",
        "A **device driver** is system software — it lets the OS control one specific hardware item. Without the driver, the OS cannot use the printer.",
        "Driver = system software, whatever it 'looks like'.", 25)
    S.q("so-typ-p2", "easy", "Which utility is used to **protect a computer from viruses**?",
        ["Disk Cleanup", "Antivirus software", "Disk Defragmenter", "File Explorer"], "Antivirus software",
        "**Antivirus** software scans, detects and removes malicious programs — the protective member of the utility crew.",
        "Virus → antivirus. Cleanup and defrag do other jobs.", 20)
    S.q("so-typ-p2", "easy", "**WinZip** and **7-Zip** are examples of —",
        ["Compression utilities", "Operating systems", "Device drivers", "Application suites"], "Compression utilities",
        "They **compress** one or more files into a smaller archive (.zip) and extract them again — utility software for storage economy and faster transfer.",
        "Zip = squeeze.", 20)
    S.q("so-typ-p2", "medium", "Which utility **automatically deletes temporary files** to free disk space in Windows?",
        ["Disk Cleanup", "Disk Defragmenter", "Task Manager", "Backup"], "Disk Cleanup",
        "**Disk Cleanup** removes temporary files, cache and Recycle Bin contents to free space. The Defragmenter rearranges files instead; Backup copies data.",
        "Space → Cleanup; speed → Defragmenter.", 20)
    S.q("so-typ-p3", "easy", "Software offered **free for a trial period**, after which payment is required, is called —",
        ["Freeware", "Shareware", "Open source", "Public domain"], "Shareware",
        "**Shareware** = 'sample first': free to try for a limited period or feature set, then you must pay to continue. Freeware is free forever.",
        "Share = try, then share the cost.", 20)
    S.q("so-typ-p3", "medium", "Which statement is **correct**?",
        ["Freeware is always open source", "Open-source software makes its source code available for use and modification", "Windows is open-source software", "Shareware can never be paid for"], "Open-source software makes its source code available for use and modification",
        "**Open source** means the source code is public (Linux, LibreOffice, VLC). Freeware is free of cost but closed source; Windows is proprietary; shareware asks for payment after the trial.",
        "Cost-free ≠ source-free — two different freedoms.", 25)
    S.q("so-typ-p4", "easy", "Which of the following is **NOT** an operating system?",
        ["Linux", "macOS", "Photoshop", "Android"], "Photoshop",
        "**Photoshop** is an image-editing **application**. Linux, macOS and Android are operating systems.",
        "Famous app names are the planted odd ones.", 20)
    S.q("so-typ-p4", "medium", "Which of the following is an operating system rather than an application?",
        ["Google Chrome", "MS Excel", "Ubuntu", "Adobe Reader"], "Ubuntu",
        "**Ubuntu** is one of the most widely used **Linux** distributions — an operating system. Chrome, Excel and Adobe Reader are applications.",
        "Ubuntu/Fedora/Debian = Linux family = OS.", 25)
    S.q("so-typ-p1", "hard", "Consider the statements:\n1. The operating system is system software.\n2. Firmware is typically stored in a ROM chip.\n3. A compiler is application software.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are standard. Statement 3 is wrong: a compiler is a **language translator, which is system software** — it serves the machine, not the user's document work.",
        "Translators sit on the system-software side of the line.", 35)
    S.q("so-typ-p2", "hard", "Consider the statements:\n1. Defragmentation speeds up access on traditional hard disks.\n2. Disk Cleanup rearranges file fragments.\n3. A backup utility protects data against loss.\nWhich are correct?",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "1 and 3 only",
        "Statement 2 swaps the jobs: **Disk Cleanup deletes** junk files; the **Defragmenter** does the rearranging. Statements 1 and 3 are correct.",
        "Cleanup deletes, defrag rearranges — never the reverse.", 35)
    return S


def build_os_functions():
    S = Sub("so-os-functions")
    S.notes = """### What an operating system is
The **operating system (OS)** is the system software that manages all hardware and software and gives applications a platform to run on. It is the first big program loaded and stays in memory till shutdown. Without an OS, the machine is just electronics.

### The six services every OS provides
| Service | What it does |
|---|---|
| **Process management** | Decides which waiting program gets the CPU next (scheduling) |
| **Memory management** | Allots RAM to programs; extends it with **virtual memory** (disk used as extra RAM) |
| **File management** | Folders, naming, saving, retrieving files through the file system |
| **Device management** | Talks to hardware through **drivers** |
| **Security** | Usernames, passwords, permissions |
| **User interface** | The screen you work on — GUI (Windows) or command line (DOS) |

### Types of operating systems
| Type | Idea | Where you meet it |
|---|---|---|
| Single-user, single-task | One user, one program at a time | Old MS-DOS |
| Single-user, multitasking | One user, many programs at once | Windows on a PC |
| **Multi-user** | Many users share one machine simultaneously | Unix/Linux servers |
| **Multiprogramming** | Several programs sit in memory; the CPU switches among them | Server systems |
| **Time-sharing** | CPU time sliced into small quanta shared round-robin among users/tasks | University mainframes |
| **Real-time (RTOS)** | Responds **within a fixed deadline**; late answer = failure | Missile control, pacemakers, industrial robots |
| **Distributed** | Many networked computers appear as one system | Cloud data centres |
| **Embedded** | Small OS baked into an appliance | Washing machine, router, smart TV |
| **Mobile** | For smartphones | **Android** (Google, **Linux** kernel), iOS (Apple) |

### Kernel and shell
- **Kernel** — the core of the OS, always in main memory; does scheduling, memory and device work.
- **Shell** — the outer layer that takes your commands and passes them to the kernel; may be a **CLI** (typing commands, like MS-DOS) or a **GUI** (Windows desktop).
Picture: kernel = the engine, shell = the steering wheel and dashboard.

### Booting — how the machine wakes up
1. Power on → CPU jumps to the **BIOS/UEFI** firmware chip.
2. **POST (Power-On Self-Test)** — hardware quick check (beep if fine).
3. BIOS finds the boot device and runs the **boot loader**.
4. Boot loader loads the **kernel** into RAM; OS takes charge; login screen appears.
- **Cold boot** — starting from a powered-off state.
- **Warm boot** — restarting without cutting power (Restart option).
Order is fixed: **POST → boot loader → kernel → login**.

### Quick revision
- Six services: process, memory, file, device, security, interface.
- Multiprogramming = many programs in memory, one CPU switching. Time-sharing = time slices. RTOS = deadline.
- Kernel in memory (engine); shell is the interface (CLI or GUI).
- Boot order: POST → boot loader → kernel. Cold = from off; warm = restart.
- Android runs on the Linux kernel; iOS is Apple-only."""
    S.pattern("so-fun-p1", "OS service identification", "very common",
        "A job is described — allotting RAM, choosing the next CPU task, managing folders, drivers for hardware, usernames — and the OS function is asked.",
        None,
        "1. Match the job: CPU turn → process management; RAM → memory management; folders/files → file management; drivers → device management; passwords → security; screen → user interface.\n2. 'Which program gets the CPU next' is the single most asked service — process scheduling.\n3. Virtual memory (disk acting as extra RAM) belongs to memory management.",
        "Allotting RAM to each running program is the function of —",
        "**Memory management** — the OS tracks every byte of RAM and allots/frees it for each process, using virtual memory when RAM runs short.")
    S.pattern("so-fun-p2", "OS type from the situation", "very common",
        "A scenario is given — missile guidance, many students sharing one server, ATM deadlines, a washing machine's controller — and the OS type is asked.",
        None,
        "1. Deadline = real-time; many users at once = multi-user/time-sharing; many programs resident = multiprogramming; appliance = embedded; network-as-one = distributed; one user many apps = multitasking.\n2. RTOS keywords: 'immediately', 'within a fixed time', 'missile', 'industrial control'.\n3. Embedded = inside a machine, single purpose, no user programs.",
        "An operating system that **must respond within a fixed deadline** (missile guidance, industrial robots) is a —",
        "**Real-time operating system (RTOS)** — a late response is as bad as a wrong one; ordinary desktop OSes give no such guarantee.")
    S.pattern("so-fun-p3", "Kernel, shell and interface questions", "common",
        "'The core of the OS that always stays in memory is', 'the part that takes user commands is', CLI vs GUI identification.",
        None,
        "1. Kernel = in-memory core (scheduling, memory, devices). Shell = the interface layer (CLI or GUI) between user and kernel.\n2. CLI = typed commands (MS-DOS, Linux terminal); GUI = windows, icons, menus, pointer (Windows).\n3. Trap: calling the desktop/shell the kernel.",
        "The part of the operating system that **accepts your commands** and passes them to the core is the —",
        "**Shell** — the interface layer (command line or GUI desktop). The kernel is the in-memory core that actually executes the work.")
    S.pattern("so-fun-p4", "Booting sequence, POST, cold vs warm", "common",
        "'What is the first check when the computer starts?', 'restart without power off is called', 'correct order of boot steps'.",
        None,
        "1. Order: POST (Power-On Self-Test) → boot loader → kernel loads → login.\n2. Cold boot = power was off; warm boot = restart without cutting power.\n3. POST always precedes the boot loader — reversing them is the standard trap.",
        "Put in order: A. Boot loader  B. POST  C. Kernel loads  D. Login screen",
        "**B, A, C, D** — BIOS runs POST first, then hands to the boot loader, which loads the kernel, and finally the login screen appears.")

    S.q("so-fun-p1", "easy", "Which OS service decides **which waiting program gets the CPU next**?",
        ["Memory management", "Process scheduling", "File management", "Device management"], "Process scheduling",
        "**Process management** schedules the CPU among all ready programs — choosing who runs next is its daily job.",
        "CPU turn-taking = process scheduling.", 20)
    S.q("so-fun-p1", "easy", "Checking **usernames and passwords** before allowing access is part of which OS service?",
        ["Security management", "Process management", "File management", "User interface"], "Security management",
        "**Security** covers user accounts, passwords and permissions — deciding who may enter and what they may touch.",
        "Passwords → security.", 20)
    S.q("so-fun-p1", "medium", "When RAM is full, Windows uses **disk space as extra working memory**. This is called —",
        ["Cache memory", "Virtual memory", "ROM", "Flash memory"], "Virtual memory",
        "**Virtual memory** is disk space acting as an overflow for RAM (page file). It saves the day when RAM runs out but is far slower than real RAM. Cache is a different, much faster thing near the CPU.",
        "Disk-as-RAM = virtual memory.", 25)
    S.q("so-fun-p2", "easy", "A **washing machine** or router contains a small special-purpose OS inside the appliance. This is a(n) —",
        ["Embedded operating system", "Multi-user OS", "Time-sharing OS", "Network OS"], "Embedded operating system",
        "**Embedded OS** = a compact OS fixed inside an appliance, running one dedicated job for its whole life.",
        "Inside the machine = embedded.", 20)
    S.q("so-fun-p2", "medium", "In a **time-sharing** operating system, the CPU —",
        ["Runs only one program per day", "Is shared among many users/tasks in small time slices", "Needs at least two processors", "Works without a scheduler"], "Is shared among many users/tasks in small time slices",
        "**Time-sharing** cuts CPU time into tiny slices and gives each user or task a slice in rotation — so fast that everyone feels the machine is theirs alone.",
        "Slices round the table = time-sharing.", 25)
    S.q("so-fun-p2", "medium", "**Unix** servers allow **hundreds of users to log in simultaneously** on separate terminals. This capability marks Unix as a —",
        ["Single-user OS", "Multi-user OS", "Embedded OS", "Batch OS"], "Multi-user OS",
        "Many users working at the same instant on one machine defines a **multi-user** operating system (Unix, Linux servers).",
        "Many logins at once = multi-user.", 25)
    S.q("so-fun-p3", "easy", "The **core of the operating system**, which remains permanently in main memory and handles scheduling and devices, is the —",
        ["Shell", "Kernel", "Desktop", "BIOS"], "Kernel",
        "The **kernel** is the OS's in-memory core — it schedules processes, allots memory and drives devices. The shell is only its interface.",
        "Kernel = engine, always running.", 20)
    S.q("so-fun-p3", "medium", "**MS-DOS**, where you typed commands like DIR and COPY on a black screen, used which type of interface?",
        ["GUI", "CLI (command-line interface)", "Touch interface", "Voice interface"], "CLI (command-line interface)",
        "DOS used a **command-line interface** — you typed commands; no windows, icons or mouse pointer. Windows brought the GUI style.",
        "Typed commands = CLI; point-and-click = GUI.", 20)
    S.q("so-fun-p4", "easy", "The diagnostic routine that checks RAM, keyboard and disks the moment a computer is **switched on** is —",
        ["POST (Power-On Self-Test)", "Booting the shell", "Defragmentation", "Logging in"], "POST (Power-On Self-Test)",
        "**POST** runs from the BIOS firmware before anything else loads — it beeps if the hardware passes.",
        "First check = POST.", 20)
    S.q("so-fun-p4", "medium", "Put the booting steps in order:\nA. Boot loader runs  B. POST  C. Kernel is loaded into RAM  D. Login screen appears",
        ["B, A, C, D", "A, B, C, D", "B, C, A, D", "C, A, B, D"], "B, A, C, D",
        "**POST → boot loader → kernel → login.** The BIOS tests hardware first (POST), then hands over to the boot loader, which loads the OS kernel.",
        "Self-test before anything loads.", 25)
    S.q("so-fun-p4", "medium", "Switching on a computer that was **powered off** is called —",
        ["Warm booting", "Cold booting", "Soft rebooting", "Hybrid booting"], "Cold booting",
        "**Cold boot** = the machine starts from a powered-off ('cold') state. **Warm boot** = restarting without cutting the power (the Restart option).",
        "Cold = from off; warm = restart.", 20)
    S.q("so-fun-p2", "hard", "Consider the statements:\n1. Multiprogramming requires multiple CPUs.\n2. In multiprogramming, several programs stay in memory while one CPU switches among them.\n3. A real-time OS guarantees a response within a deadline.\nWhich are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], "2 and 3 only",
        "Statement 1 is the classic trap — multiprogramming uses **one CPU juggling** resident programs, not many CPUs. Statements 2 and 3 are the correct definitions.",
        "One CPU, many programs — multiprogramming in one line.", 35)
    S.q("so-fun-p4", "hard", "Consider the statements:\n1. POST runs before the boot loader.\n2. Warm booting restarts the machine without switching off the power.\n3. The BIOS loads the operating system directly into the Recycle Bin.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are the standard booting facts. Statement 3 is nonsense — the boot loader loads the **kernel into RAM**; the Recycle Bin is a desktop folder for deleted files.",
        "One absurd statement marks the wrong set.", 35)
    return S
