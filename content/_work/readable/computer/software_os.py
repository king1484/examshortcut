"""Readable rewrite of Computer > Software & Operating Systems (all 4 subtopics).

Facts are kept exactly as in the existing notes. Old pattern ids are kept; new ids continue each prefix.
Run: python software_os.py  (patches content/core/topics/computer/software-os.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "computer" / "software-os.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Types of software
# =====================================================================
SUBS["so-types"] = dict(
    concept=(
        "Every program is one of three kinds. **System software** runs the machine. "
        "**Utility software** keeps the machine clean and safe. **Application software** does the user's own work. "
        "Software is also grouped by licence: freeware, shareware, open source and proprietary."
    ),
    notes=r"""### The three classes of software
Ask one question about any program: **who does it serve?**

| Class | Serves | Examples |
|---|---|---|
| **System software** | The machine itself | Operating systems (Windows, Linux, macOS, Android), **device drivers**, **firmware/BIOS**, language translators (compiler, interpreter, assembler) |
| **Utility software** | Maintenance of the machine | Antivirus, disk defragmenter, disk cleanup, backup tools, file compressors, file manager, screen saver |
| **Application software** | The user's task | MS Word, Excel, PowerPoint, Chrome, Photoshop, games, WhatsApp, Tally |

> **Tip:** Use the **SUApp** test. Does it **S**erve the machine (system), **U**nclog it (utility), or do the user's **App** work (application)?

### Two boundary cases
Exams love the programs that sit near the border.

- A **device driver** is system software. You install it like an app. But it only teaches the OS to talk to one piece of hardware, such as a printer.
- A **utility** keeps the machine healthy. It does not make user documents. An **application** makes the user's output.

> **Watch:** Firmware is software burned into a hardware chip, such as the BIOS chip. It is system software too.

### Utility software
A utility is a small maintenance tool. Learn each job.

| Utility | Job |
|---|---|
| Antivirus | Finds and removes malware |
| Disk Defragmenter | Joins scattered pieces of files on a hard disk so reading is faster |
| Disk Cleanup | Deletes temporary and junk files to free space |
| Backup utility | Keeps a second copy of important data |
| Compression tool (WinZip, 7-Zip, WinRAR) | Shrinks files into smaller archives and opens them |
| File manager | Copies, moves, renames and organises files |

### Two kinds of application software
- **General purpose:** made for many users and many jobs. Examples: MS Office, browsers, media players.
- **Application-specific (custom):** made for one job. Examples: a payroll system, a railway reservation system.

### Licence types
A licence says how you may use a program. These four are one-mark favourites.

| Type | Meaning | Example |
|---|---|---|
| **Freeware** | Free of cost, but the **source code stays closed** | Adobe Reader |
| **Shareware** | Free trial first, then you pay | WinZip |
| **Open source** | Source code is available | Linux, LibreOffice, Firefox |
| **Proprietary** | Paid licence, closed source | MS Office |

> **Rule:** Free of **cost** is not the same as open **source**. Freeware is free, but nobody can see its code.

> **Tip:** **F**reeware = **F**ree forever. **S**hareware = **S**ample first. **O**pen source = **O**pen code. **P**roprietary = **P**ay.
""",
    tricks=[
        {"title": "SUApp test",
         "body": "Ask who the program serves. The machine means system. Cleaning or protecting the machine means utility. The user's own job means application. Windows is system, antivirus is a utility, Excel is an application.",
         "example": {"q": "Disk Defragmenter is which type of software?",
                     "steps": ["It does not run the machine.", "It does not make user documents.", "It keeps the disk healthy."],
                     "answer": "Utility software"}},
        {"title": "Licence four-word key",
         "body": "Freeware is free forever but closed. Shareware is a sample first. Open source has open code. Proprietary means pay.",
         "example": {"q": "Linux is which kind of software by licence?",
                     "steps": ["Its source code is available.", "That is the mark of open source."],
                     "answer": "Open-source software"}},
    ],
    mistakes=[
        mis("Counting device drivers as application software.", "Drivers serve the hardware, so they are system software."),
        mis("Calling an antivirus an operating system.", "An antivirus maintains and protects the machine. It is a utility."),
        mis("Thinking freeware is open source.", "Freeware costs nothing, but its source code stays closed."),
        mis("Thinking shareware is free forever.", "Shareware is a free trial. You pay to keep using it."),
    ],
    revision=[
        "System = the machine: OS, drivers, BIOS/firmware, translators.",
        "Utility = maintenance: antivirus, defragmenter, cleanup, backup, compression.",
        "Application = the user's task: Word, Chrome, games, payroll.",
        "Drivers and firmware are system software, not applications.",
        "Freeware = free but closed source. Open source = code available (Linux, Firefox).",
        "Shareware = try first, pay later. Proprietary = paid and closed (MS Office).",
    ],
    patterns=[
        pat("so-typ-p1", "System, application or utility", "very common",
            "A program is named (Word, antivirus, driver, Windows) and its class is asked. Or a list asks for the odd one out.",
            ["Ask who the program serves.", "The machine itself means system software.", "Cleaning or protecting the machine means utility.", "The user's own task means application."],
            "Drivers, BIOS and translators are system software, even though they look like apps.",
            "Which of these is application software? (A) Windows (B) Antivirus (C) MS Word (D) Device driver",
            ["Windows is an OS: system.", "Antivirus is a utility.", "A driver serves hardware: system.", "MS Word does the user's document work."],
            "(C) MS Word"),
        pat("so-typ-p2", "Utility and its job", "common",
            "A job is described (removes junk files, joins scattered file pieces, makes a second copy) and the tool is asked.",
            ["Read the job in the question.", "Match it to the utility table.", "Pick the utility whose job matches word for word."],
            "Each utility has one fixed job, so the job words give the answer.",
            "Which utility deletes temporary and junk files to free disk space?",
            ["Freeing space by deleting junk is cleanup.", "Defragmenter only rejoins file pieces."],
            "Disk Cleanup"),
        pat("so-typ-p3", "Licence classification", "very common",
            "A program is described as free, trial, source code available or paid. The licence type is asked.",
            ["Check the cost first: free, trial or paid.", "Then check the source code: open or closed.", "Free and closed is freeware. Free and open is open source."],
            "Two facts, cost and source code, separate all four licence types.",
            "A program is free to use, but its source code is not available. It is called",
            ["It costs nothing.", "Its source code is closed."],
            "Freeware"),
        pat("so-typ-p4", "Examples of each type", "common",
            "A list of program names is given and one class or licence is asked.",
            ["Sort each name into system, utility or application.", "Watch for drivers and firmware.", "Pick the option that fits the asked class."],
            "Knowing the standard examples makes the answer immediate.",
            "Which one is NOT application software? (A) MS Excel (B) Firefox (C) Device driver (D) Tally",
            ["Excel, Firefox and Tally serve the user.", "A driver serves the hardware."],
            "(C) Device driver"),
        pat("so-typ-p5", "Firmware", "occasional",
            "A question says software stored in a chip, or asks what the BIOS is.",
            ["Look for software burned into hardware.", "Match it to firmware.", "Remember firmware is system software."],
            "Firmware lives in the hardware chip and starts the machine.",
            "Software that is burned into a hardware chip, such as the BIOS chip, is called",
            ["It sits inside the hardware.", "It is not installed by the user like an app."],
            "Firmware"),
    ],
)

# =====================================================================
# 2. OS functions, types and booting
# =====================================================================
SUBS["so-os-functions"] = dict(
    concept=(
        "The **operating system (OS)** is system software. It manages the hardware and gives programs a place to run. "
        "It handles processes, memory, files, devices, security and the user screen. "
        "The **kernel** is its core. **Booting** is the start-up of the OS."
    ),
    notes=r"""### What an operating system is
The **operating system (OS)** manages all hardware and software. It gives applications a platform to run on. It is the first big program loaded, and it stays in memory until shutdown. Without an OS, the machine is only electronics.

### The services an OS provides
| Service | What it does |
|---|---|
| **Process management** | Decides which waiting program gets the CPU next (scheduling) |
| **Memory management** | Gives RAM to programs and takes it back. **Virtual memory** uses the disk as extra RAM |
| **File management** | Folders, names, saving and finding files through the file system |
| **Device management** | Talks to hardware through **drivers** |
| **Security** | Usernames, passwords and permissions |
| **User interface** | The screen you work on: GUI (Windows) or command line (DOS) |

The OS also handles errors, networking and resource allocation.

> **Tip:** The six main services spell PMF-SUIE: **P**rocess, **M**emory, **F**ile, **S**ecurity, **U**ser interface, **E**rror handling.

### Types of operating systems
| Type | Idea | Where you meet it |
|---|---|---|
| Single-user, single-task | One user, one program at a time | Old MS-DOS |
| Single-user, multitasking | One user, many programs at once | Windows on a PC |
| **Multi-user** | Many users share one machine | UNIX/Linux servers |
| **Multiprogramming** | Several programs sit in RAM. The CPU switches when one waits for input or output | Server systems |
| **Time-sharing** | CPU time is cut into small slices shared among users | Mainframes |
| **Real-time (RTOS)** | Must answer within a fixed deadline | Missiles, robots, medical devices |
| **Distributed** | Many networked machines act as one | Data centres |
| **Embedded** | A small OS built into a device | Washing machine, router |
| **Mobile** | Made for smartphones | Android, iOS |

> **Rule:** In a real-time system, a late answer counts as a failure.

### Kernel and shell
- **Kernel:** the core of the OS. It always stays in memory. It does scheduling, memory work and device work.
- **Shell:** the outer layer. It takes your commands and passes them to the kernel. It can be a **CLI** (typed commands) or a **GUI** (desktop).

Picture the kernel as the engine and the shell as the steering wheel.

### Booting
Booting means starting the OS.

- **Cold boot:** power on from the off state.
- **Warm boot:** restart without cutting power.

The steps run in a fixed order.

1. Power on. The CPU jumps to the **BIOS/UEFI** firmware.
2. **POST** (Power-On Self-Test) checks the hardware.
3. BIOS/UEFI finds the boot device.
4. The **boot loader** loads the **kernel** into RAM.
5. The OS takes charge and the login screen appears.

> **Watch:** POST always comes first. The order is POST, boot loader, kernel, login.
""",
    tricks=[
        {"title": "PMF-SUIE services",
         "body": "The OS gives Process, Memory, File, Security, User interface and Error handling. A 'manage the machine' answer is OS work. Computing payroll is application work.",
         "example": {"q": "Which OS service gives RAM to programs?",
                     "steps": ["The question is about RAM.", "RAM work belongs to memory management."],
                     "answer": "Memory management"}},
        {"title": "Boot words",
         "body": "Cold boot starts from a cold, switched-off machine. Warm boot restarts without a power cut. POST always comes first.",
         "example": {"q": "Restarting a running computer is called",
                     "steps": ["Power stays on.", "That is a warm boot."],
                     "answer": "Warm boot"}},
    ],
    mistakes=[
        mis("Mixing up multiprogramming and time-sharing.", "Multiprogramming keeps many programs in RAM. Time-sharing gives each user a slice of CPU time."),
        mis("Saying the shell stays in memory as the OS core.", "The kernel is the core that stays in memory. The shell is the interface."),
        mis("Putting the boot loader before POST.", "The order is POST, boot loader, kernel, login."),
        mis("Calling a restart a cold boot.", "A cold boot starts from power off. A restart is a warm boot."),
        mis("Thinking iOS runs on many brands of phone.", "iOS is Apple's mobile OS. Android runs on the Linux kernel."),
    ],
    revision=[
        "Main services: process, memory, file, device, security, user interface.",
        "Virtual memory uses the disk as extra RAM.",
        "Multiprogramming = many programs in RAM. Time-sharing = CPU time slices. RTOS = fixed deadline.",
        "Kernel = core, always in memory. Shell = interface (CLI or GUI).",
        "Boot order: POST, boot loader, kernel, login.",
        "Cold boot = from off. Warm boot = restart without power cut.",
        "Android is based on the Linux kernel.",
    ],
    patterns=[
        pat("so-fun-p1", "OS service identification", "very common",
            "A job is described (giving RAM, choosing the next CPU task, managing folders, usernames) and the OS function is asked.",
            ["Find the object of the job: RAM, CPU, files, devices or users.", "Match it to its service in the table.", "Pick that service."],
            "Each OS service handles exactly one kind of resource.",
            "Giving RAM to each running program is the function of",
            ["The resource is RAM.", "The service that handles RAM is memory management."],
            "Memory management"),
        pat("so-fun-p2", "OS type from the situation", "very common",
            "A scenario is given (missile guidance, many users on one server, a washing machine) and the OS type is asked.",
            ["Find the key word: deadline, many users, time slices, small device.", "Match it to the type table.", "Pick the matching type."],
            "Every OS type has one signature situation.",
            "An OS that must respond within a fixed deadline, as in missile guidance, is a",
            ["A fixed deadline is the key word.", "Late answers count as failure."],
            "Real-time operating system (RTOS)"),
        pat("so-fun-p3", "Kernel, shell and interface", "common",
            "The core of the OS, the part that takes commands, or CLI versus GUI is asked.",
            ["Core that stays in memory means kernel.", "Part that takes your commands means shell.", "Typed commands mean CLI. Icons and windows mean GUI."],
            "The kernel does the work. The shell only takes commands and passes them on.",
            "The part of the OS that accepts your commands and passes them to the core is the",
            ["The core is the kernel.", "The layer that accepts commands is the shell."],
            "Shell"),
        pat("so-fun-p4", "Boot sequence, POST, cold and warm boot", "common",
            "The first check at start-up, the order of boot steps, or restart without power-off is asked.",
            ["Recall the order: POST, boot loader, kernel, login.", "Cold boot means from off.", "Warm boot means restart without a power cut."],
            "The boot order is fixed, so it can be learned as one chain.",
            "Arrange in order: A. Boot loader  B. POST  C. Kernel loads  D. Login screen",
            ["POST runs first.", "The boot loader comes next.", "It loads the kernel.", "The login screen appears last."],
            "B, A, C, D"),
        pat("so-fun-p5", "Multiprogramming, time-sharing and multitasking", "occasional",
            "The question describes how the CPU is shared and asks for the name.",
            ["Check what is shared: RAM slots or CPU time.", "CPU switches when one program waits for I/O: multiprogramming.", "CPU time cut into slices among users: time-sharing."],
            "The trigger for the switch decides the name.",
            "An OS gives each user a small slice of CPU time in turn. This is called",
            ["Slices of CPU time are the key idea.", "That is time-sharing."],
            "Time-sharing"),
        pat("so-fun-p6", "Mobile operating systems", "occasional",
            "A question asks which OS a phone uses, or which kernel Android is built on.",
            ["Recall Android is Linux-kernel based.", "Recall iOS belongs to Apple.", "Pick the option that fits."],
            "Only two mobile names are usually asked.",
            "Android is based on which kernel?",
            ["Android is a mobile OS.", "It is built on Linux."],
            "The Linux kernel"),
    ],
)

# =====================================================================
# 3. Windows features
# =====================================================================
SUBS["so-windows-features"] = dict(
    concept=(
        "**Microsoft Windows** is a single-user, multitasking OS with a graphical screen (GUI). "
        "Windows 10 came in 2015 and Windows 11 in 2021. "
        "Learn the main features, the built-in tools and the small accessory programs."
    ),
    notes=r"""### What Windows is
**Microsoft Windows** is a **single-user, multitasking, GUI-based** OS. Windows 10 came in **2015**. Windows 11 came in **2021**. The desktop you see is the graphical shell. The kernel behind it does the real work.

### Main features
Each row is a one-mark question.

| Feature | Meaning |
|---|---|
| **GUI** | You work with **W**indows, **I**cons, **M**enus and a **P**ointer (WIMP), not typed commands |
| **Multitasking** | Many programs run at the same time |
| **Plug and Play (PnP)** | New hardware is found and set up automatically |
| **File management** | Files and folders are browsed in **File Explorer** |
| **Recycle Bin** | Deleted files land here first. **Shift+Delete** skips it |
| **User accounts** | Administrator or Standard, with a password or PIN |

> **Tip:** The words "detected automatically" in a question mean Plug and Play.

### Built-in tools
| Tool | Job | Shortcut |
|---|---|---|
| **Task Manager** | Shows processes, performance and start-up. Ends stuck programs | **Ctrl+Shift+Esc** |
| **Control Panel / Settings** | System settings. Windows 10 and 11 use the Settings app | |
| **Device Manager** | Lists hardware and drivers | |
| **File Explorer** | Browse, copy, move and rename files | **Win+E** |
| **Disk Management** | Partition and format drives | |
| **Windows Defender** | Built-in antivirus and firewall | |
| **Windows Update** | Keeps patches current | |
| **Command Prompt / PowerShell** | Typed commands (CLI) | |

> **Watch:** Ctrl+Shift+Esc opens Task Manager directly. Ctrl+Alt+Del opens a security menu first.

### More Windows features
- **Virtual desktops:** several desktops on one PC (Win+Ctrl+D).
- **Snap:** places a window at a screen edge (Win+arrow key).
- **OneDrive:** cloud sync.
- **BitLocker:** disk encryption, in Pro editions.

### Picking the right tool
Match the problem to the tool. Take three cases.

1. A program has frozen. Open **Task Manager** and end it.
2. A new printer is not working. Open **Device Manager** and check its driver.
3. You want to change the display or sound. Open **Settings** (Control Panel in older versions).

> **Example:** Files are deleted by mistake with a normal Delete. Open the **Recycle Bin** and restore them. With Shift+Delete, this is not possible.

### Accessories
- **Notepad:** plain text only. No bold, no pictures. It saves .txt files.
- **WordPad:** rich text with simple formatting. It was removed in Windows 11.
- **Paint:** simple drawing and picture editing.
- **Calculator** and **Snipping Tool:** small single-purpose apps.

### Desktop and mobile systems
- **Android:** made by **Google**. Built on the **Linux kernel**. Open source at its core.
- **iOS:** **Apple's** mobile OS. Closed source. Runs only on Apple devices.
- **Desktop trio:** Windows, macOS, Linux.

> **Note:** Android and iOS are the two mobile names exams ask most.
""",
    tricks=[
        {"title": "Plug and Play",
         "body": "Plug and Play means the OS detects and sets up new hardware by itself. The phrase 'automatically detected' in a question points to PnP.",
         "example": {"q": "Which Windows feature sets up a newly attached printer automatically?",
                     "steps": ["The setup is automatic.", "Automatic hardware setup is Plug and Play."],
                     "answer": "Plug and Play"}},
        {"title": "Task Manager shortcut",
         "body": "The direct route to Task Manager is Ctrl+Shift+Esc. Ctrl+Alt+Del opens a security menu first. Exams ask for the direct one.",
         "example": {"q": "Which shortcut opens Task Manager directly?",
                     "steps": ["Ctrl+Alt+Del opens a menu first.", "The direct key set is the other one."],
                     "answer": "Ctrl+Shift+Esc"}},
    ],
    mistakes=[
        mis("Choosing Ctrl+Alt+Del as the direct Task Manager shortcut.", "Ctrl+Shift+Esc opens Task Manager directly."),
        mis("Thinking Shift+Delete moves a file to the Recycle Bin.", "Shift+Delete skips the Recycle Bin. The file is deleted permanently."),
        mis("Saying Notepad can bold text or insert pictures.", "Notepad is plain text only. WordPad gives simple formatting."),
        mis("Using Device Manager to end a stuck program.", "Task Manager ends stuck programs. Device Manager lists hardware and drivers."),
        mis("Saying iOS runs on any phone.", "iOS runs only on Apple devices."),
    ],
    revision=[
        "Windows is single-user, multitasking and GUI (WIMP). Windows 10 came in 2015, Windows 11 in 2021.",
        "Plug and Play = new hardware is detected and configured automatically.",
        "Task Manager (Ctrl+Shift+Esc) = processes and stuck programs.",
        "Device Manager = hardware and drivers. Control Panel/Settings = system settings.",
        "Shift+Delete skips the Recycle Bin.",
        "Notepad = plain text. WordPad = formatted text. Paint = drawing.",
        "Android = Google, Linux kernel. iOS = Apple only.",
    ],
    patterns=[
        pat("so-win-p1", "Windows feature identification", "very common",
            "A feature is described (auto-detects hardware, many programs at once, WIMP) and its name is asked.",
            ["Read the description.", "Match it to the feature table.", "Watch for near-twin options."],
            "Each feature has one short definition to recall.",
            "The Windows feature that automatically detects and sets up a newly connected USB device is",
            ["The setup is automatic.", "That is Plug and Play."],
            "Plug and Play (PnP)"),
        pat("so-win-p2", "Windows tool and its purpose", "very common",
            "A job is described (stuck program, hardware list, settings) and the tool is asked.",
            ["Find the job in the question.", "Match it to the tool table.", "Check the shortcut if one is given."],
            "Each tool has one job, so the job words give the tool.",
            "A program has stopped responding. Which tool lets you end it?",
            ["Ending a stuck program is a process job.", "Task Manager does this (Ctrl+Shift+Esc)."],
            "Task Manager"),
        pat("so-win-p3", "Notepad, WordPad and Paint", "common",
            "A question asks which accessory saves text only, does formatting, or draws pictures.",
            ["Plain text only means Notepad.", "Simple formatting means WordPad.", "Drawing means Paint."],
            "The three accessories differ in how much they can format.",
            "Which statement about Notepad is correct?",
            ["Notepad saves .txt files.", "It has no bold, fonts or images."],
            "Notepad is a plain-text editor with no formatting"),
        pat("so-win-p4", "Mobile and desktop OS facts", "common",
            "Who makes Android, its kernel, iOS devices, or which OS is open source.",
            ["Android means Google and the Linux kernel.", "iOS means Apple and Apple devices only.", "Pick the option that fits."],
            "Only a few facts about each OS are ever asked.",
            "The Android OS is built on which kernel?",
            ["Android is Google's mobile OS.", "It is built on Linux."],
            "The Linux kernel"),
        pat("so-win-p5", "Windows shortcuts", "common",
            "A shortcut is given and its action is asked, or the reverse.",
            ["Recall Win+E is File Explorer.", "Recall Ctrl+Shift+Esc is Task Manager.", "Recall Win+arrow snaps windows and Win+Ctrl+D adds a virtual desktop."],
            "Only a handful of Windows shortcuts are asked.",
            "Which shortcut opens File Explorer?",
            ["File Explorer uses the Windows key.", "The letter is E."],
            "Win+E"),
        pat("so-win-p6", "Recycle Bin behaviour", "occasional",
            "A question asks what Shift+Delete does or where deleted files go.",
            ["Normal delete sends a file to the Recycle Bin.", "Shift+Delete skips the bin.", "A skipped file is deleted permanently."],
            "The bin is only a holding place for normal deletes.",
            "What happens when you press Shift+Delete on a file?",
            ["Shift skips the Recycle Bin.", "So the file cannot be restored from it."],
            "The file is deleted permanently"),
    ],
)

# =====================================================================
# 4. File systems and file management
# =====================================================================
SUBS["so-file-systems"] = dict(
    concept=(
        "A **file system** is the set of rules an OS uses to name, store and find files on a disk. "
        "FAT32, exFAT and NTFS are the three most asked. "
        "FAT32 cannot hold a single file larger than 4 GB."
    ),
    notes=r"""### What a file system does
A **file system** is the OS's rulebook for a disk. It says how files are named, stored in folders, found again and protected. **Formatting** a drive writes this rulebook onto it.

### File systems compared
| File system | Used by | Key facts |
|---|---|---|
| **FAT32** | Windows 9x, pen drives | Single file up to **4 GB** (minus 1 byte). No permissions, no journaling |
| **exFAT** | Flash drives, cameras | Removes the 4 GB file limit. Light and simple |
| **NTFS** | Modern Windows | Journaling, permissions, encryption, compression, huge files. Default for Windows |
| **ext4** | Linux | Journaling. Default on many distros |
| **APFS** | macOS and iOS | Snapshots and encryption |

Full forms: FAT is File Allocation Table. NTFS is New Technology File System.

> **Rule:** A file larger than 4 GB will not copy into a FAT32 drive. Use exFAT or NTFS.

Windows formats FAT32 volumes only up to about 32 GB. **Journaling** means the system keeps a log, so it can recover after a crash.

### File names and extensions
A file name has two parts: **name.extension**, such as *report.docx*. The extension tells the OS which program opens the file.

| Extension | File type | Extension | File type |
|---|---|---|---|
| .txt | Plain text | .docx | Word document |
| .xlsx | Excel workbook | .pptx | PowerPoint show |
| .pdf | Portable Document | .jpg / .png | Images |
| .mp3 / .wav | Audio | .mp4 | Video |
| .zip | Compressed archive | .html | Web page |
| .exe | Executable program | .bat | Batch (command) file |

> **Watch:** A Windows file name cannot contain any of these: \ / : * ? " < > |

### Wildcards in search
- **?** stands for exactly **one** character. *file?.txt* finds file1.txt and fileA.txt.
- **\*** stands for **any number** of characters. **\*.pdf** finds every PDF.

> **Tip:** `s?t` finds sat, set and sit. `*.docx` finds all Word files.

### Paths and file terms
- **File:** a named collection of related data.
- **Folder (directory):** a container for files.
- **Path:** the address of a file, written drive:\folders\file.ext.
- **Attributes:** read-only, hidden, archive and system.

### Copy, move and delete
- **Copy** (Ctrl+C, Ctrl+V) keeps the original and makes a duplicate.
- **Move** (Ctrl+X, Ctrl+V) shifts the file. The original disappears.
- **Delete** sends the file to the **Recycle Bin**. **Shift+Delete** skips the bin.
- **Properties** (Alt+Enter) shows size, dates and the read-only switch.

Formatting prepares a disk with a file system. It erases the directory, but it does not physically shred the data.
""",
    tricks=[
        {"title": "FAT32 four-GB wall",
         "body": "FAT32 cannot hold a single file bigger than 4 GB. This is the classic exam line. NTFS and exFAT do not have this limit.",
         "example": {"q": "A 5 GB video will not copy to a FAT32 pen drive. Why?",
                     "steps": ["5 GB is more than 4 GB.", "FAT32 has a 4 GB single-file limit."],
                     "answer": "FAT32 limits a file to 4 GB. Use NTFS or exFAT."}},
        {"title": "Wildcards",
         "body": "The question mark masks exactly one character. The asterisk masks any number. So *.docx finds all Word files.",
         "example": {"q": "Which wildcard stands for any number of characters?",
                     "steps": ["? is exactly one character.", "The other symbol is the asterisk."],
                     "answer": "The asterisk (*)"}},
    ],
    mistakes=[
        mis("Thinking FAT32 can store a 6 GB movie.", "FAT32 stops at 4 GB per file. Use exFAT or NTFS."),
        mis("Using ? to match many characters.", "? matches exactly one character. Use * for any number."),
        mis("Thinking a format makes the disk bigger or repairs files.", "Formatting lays down a file system. It does not add space."),
        mis("Using \\ or : in a file name.", "Windows rejects \\ / : * ? \" < > | in names."),
        mis("Thinking move leaves a copy behind.", "Copy leaves the original. Move removes it from the old place."),
    ],
    revision=[
        "FAT32 = pen drives, 4 GB single-file limit. exFAT removes the limit.",
        "NTFS = Windows default, with permissions, journaling and encryption.",
        "FAT = File Allocation Table. NTFS = New Technology File System.",
        "Formatting lays down the file system. Cleanup deletes junk. Defragmenting joins file pieces.",
        "? = exactly one character. * = any number of characters.",
        "Forbidden name characters: \\ / : * ? \" < > |",
        ".exe = program, .zip = archive, .docx/.xlsx/.pptx = Word, Excel, PowerPoint.",
    ],
    patterns=[
        pat("so-fil-p1", "FAT32, NTFS and exFAT limits", "very common",
            "Maximum file size on FAT32, the default Windows file system, or why a large file will not copy.",
            ["Note the file size in the question.", "Compare it to the FAT32 limit of 4 GB.", "If it is larger, the answer is the FAT32 limit."],
            "The 4 GB limit is the single most asked file system fact.",
            "A 16 GB pen drive formatted as FAT32 refuses a 6 GB movie file. Why?",
            ["6 GB is more than 4 GB.", "FAT32 cannot store one file that large.", "Reformat as exFAT or NTFS."],
            "FAT32 cannot store a single file larger than 4 GB"),
        pat("so-fil-p2", "Wildcards in file search", "very common",
            "A pattern like *.pdf or file?.txt is given, and what it finds is asked.",
            ["Read each symbol in the pattern.", "? replaces exactly one character.", "* replaces any number of characters."],
            "The two symbols work differently, and the pattern decides the match.",
            "In a Windows search, which name does file?.txt match?",
            ["The name starts with file.", "One character comes next.", "Then .txt follows."],
            "file1.txt or fileA.txt (exactly one character after file)"),
        pat("so-fil-p3", "Extension and file type", "very common",
            "An extension is given and its file type is asked, or a matching table is shown.",
            ["Read the extension after the dot.", "Match it to the extension table.", "Check the column pairs."],
            "The extension tells the OS which program opens the file.",
            "The file extension .exe marks a file as",
            ["The extension is .exe.", "Double-clicking it runs the code."],
            "An executable program"),
        pat("so-fil-p4", "Formatting and disk housekeeping", "common",
            "Formatting, defragmentation or disk cleanup is defined and the term is asked.",
            ["Formatting lays down a file system.", "Defragmenting joins scattered pieces.", "Cleanup deletes junk and temporary files."],
            "Each action does one different job on a disk.",
            "Formatting a hard disk mainly",
            ["It writes a file system onto the disk.", "It does not enlarge the disk."],
            "Prepares the disk with a file system so files can be stored and found"),
        pat("so-fil-p5", "Copy, move and delete", "common",
            "A question asks what happens to the original file, or which shortcut is used.",
            ["Copy keeps the original.", "Move removes the original.", "Delete goes to the Recycle Bin. Shift+Delete skips it."],
            "The fate of the original file separates the three actions.",
            "After you cut a file and paste it into another folder, what happens to the original?",
            ["Cut is Ctrl+X.", "Paste places the file in the new folder."],
            "The original disappears from the old folder"),
        pat("so-fil-p6", "Illegal characters and paths", "occasional",
            "A list of file names is given and the valid one is asked. Or a path is shown.",
            ["Scan each name for \\ / : * ? \" < > |.", "Cross out any name with these.", "A path is written drive:\\folder\\file.ext."],
            "Windows rejects names containing these nine characters.",
            "Which of these is a valid Windows file name? (A) report:final.docx (B) report_final.docx (C) report*final.docx (D) report?final.docx",
            ["A has a colon.", "C has an asterisk.", "D has a question mark.", "B has none of the banned characters."],
            "(B) report_final.docx"),
    ],
)


def long_lines(text, limit=20):
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
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
