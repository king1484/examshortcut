"""software-os deep content — part 2: Windows features, file systems."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_windows():
    S = Sub("so-windows-features")
    S.notes = """### What Windows is
**Microsoft Windows** is the world's most used desktop operating system: **single-user, multitasking, GUI-based**. Windows 10 arrived in **2015**, Windows 11 in **2021**. The desktop you see is the OS's graphical shell — behind it, the Windows kernel does the real work.

### Feature table (each row is a one-mark question)
| Feature | Meaning |
|---|---|
| **GUI** | You point and click on **W**indows, **I**cons, **M**enus, **P**ointer (WIMP) instead of typing commands |
| **Multitasking** | Many programs run at once; the CPU switches between them so fast each seems continuous |
| **Plug and Play (PnP)** | Connect new hardware and Windows **detects and configures it automatically** — usually no manual driver hunt |
| **File management** | Files in folders, browsed in **File Explorer** |
| **Recycle Bin** | Deleted files land here first and can be restored; **Shift+Delete skips it** |
| **User accounts** | Separate login, password and personal folders per user |

### The Windows toolbox
| Tool | Job |
|---|---|
| **Task Manager** | Shows running programs, 'not responding' apps, CPU/RAM use; start it with **Ctrl+Shift+Esc** |
| **Control Panel / Settings** | Change system settings — display, sound, users, network |
| **Device Manager** | Lists all installed hardware and its drivers; flags problems |
| **File Explorer** | Browse, copy, move, rename files and folders |
| **Disk Cleanup** | Deletes junk and temporary files |
| **Disk Defragmenter** | Reorganises scattered file pieces on hard disks |

### Built-in accessories (know which does what)
- **Notepad** — plain **text only**: no bold, no pictures. Saves .txt.
- **WordPad** — light **formatting** (bold, fonts) in rich text; between Notepad and MS Word.
- **Paint** — simple drawing and image editing.
- **Calculator**, **Snipping Tool** (screenshots) — small single-purpose apps.

### The mobile half of the story
- **Android** — owned and developed by **Google**; built on the **Linux kernel**; open source at its core (AOSP); runs on phones of many brands.
- **iOS / iPadOS** — **Apple's** mobile OS; closed source; runs **only on Apple devices**.
- Windows, macOS, Linux — the desktop trio; Android, iOS — the mobile duo.

### Quick revision
- Windows = single-user + multitasking + GUI (WIMP). Win10 2015, Win11 2021.
- Plug and Play = auto-detect and configure new hardware.
- Task Manager = processes and 'not responding'; Device Manager = hardware and drivers; Control Panel = settings.
- Notepad = plain text; WordPad = formatted text; Paint = drawing.
- Android = Google + Linux kernel; iOS = Apple only."""
    S.pattern("so-win-p1", "Windows feature identification (GUI, multitasking, PnP)", "very common",
        "'The feature that auto-detects new hardware is', 'running many programs at once is called', 'WIMP stands for' — a feature name with four definitions.",
        None,
        "1. Auto-detect + auto-configure hardware = **Plug and Play**.\n2. Many programs at once = **multitasking**; WIMP = Windows, Icons, Menus, Pointer.\n3. Windows = single-user multitasking GUI OS — a three-label line exams quote directly.",
        "The Windows feature that automatically detects and configures a newly connected USB device is —",
        "**Plug and Play (PnP)** — the OS identifies the device and loads a suitable driver without manual setup.")
    S.pattern("so-win-p2", "Windows tool ↔ purpose matching", "very common",
        "'Which tool shows CPU/RAM usage or stuck programs?', 'where do you change settings?', 'which tool lists hardware and drivers?'",
        None,
        "1. Processes and performance → **Task Manager** (Ctrl+Shift+Esc). Settings → **Control Panel/Settings**. Hardware + drivers → **Device Manager**. Files → **File Explorer**. Junk files → **Disk Cleanup**.\n2. 'Not responding' in the stem always points to Task Manager.\n3. Device Manager flags driver problems with warning marks.",
        "A program has stopped responding. Which Windows tool lets you end it forcibly?",
        "**Task Manager** (Ctrl+Shift+Esc) — select the app and choose End Task. It also shows CPU, memory and disk usage.")
    S.pattern("so-win-p3", "Windows accessories: Notepad / WordPad / Paint", "common",
        "'Notepad saves files as…', 'which accessory draws pictures?', 'difference between Notepad and WordPad'.",
        None,
        "1. Notepad = plain text (.txt), no formatting at all.\n2. WordPad = basic rich-text formatting; MS Word = full formatting.\n3. Paint = drawing; Snipping Tool = screenshots; Calculator = maths.",
        "Which statement about **Notepad** is correct?",
        "Notepad is a plain-text editor — it saves .txt files with **no formatting** (no bold, fonts or images). WordPad adds basic formatting.")
    S.pattern("so-win-p4", "Mobile and desktop OS facts (Android, iOS, Linux)", "common",
        "'Android is developed by…', 'Android is based on which kernel?', 'iOS runs on which devices?', 'which is open source?'",
        None,
        "1. Android = **Google**, built on the **Linux kernel**, open source at its core, many brands.\n2. iOS = **Apple**, closed source, only Apple hardware.\n3. Desktop trio: Windows (Microsoft), macOS (Apple), Linux (open source, Linus Torvalds).",
        "The Android mobile operating system is built on which kernel?",
        "**The Linux kernel** — Android is Google's mobile OS layered over Linux; that is why it is often called 'Linux-based'.")

    S.q("so-win-p1", "easy", "Windows is best described as a —",
        ["Single-user, multitasking, GUI operating system", "Multi-user, single-tasking, CLI OS", "Real-time embedded OS", "Programming language"], "Single-user, multitasking, GUI operating system",
        "One user at a time, many programs at once (multitasking), and a graphical desktop — the standard three-label description of Windows.",
        "One user, many apps, pictures on screen.", 20)
    S.q("so-win-p1", "easy", "**Multitasking** means —",
        ["Using two monitors", "The OS running several programs at the same time by switching the CPU among them", "Typing with both hands", "Two users sharing one password"], "The OS running several programs at the same time by switching the CPU among them",
        "Multitasking = the OS gives each open program a slice of CPU time so browsing, music and typing all appear simultaneous on one machine.",
        "One CPU, many programs, quick switching.", 20)
    S.q("so-win-p1", "medium", "The letters of **WIMP**, the classic GUI elements, stand for —",
        ["Windows, Icons, Menus, Pointer", "Write, Insert, Move, Print", "Wireless, Internet, Mouse, Program", "Windows, Internet, Memory, Processor"], "Windows, Icons, Menus, Pointer",
        "**WIMP** = Windows, Icons, Menus, Pointer — the four visible pieces of every graphical desktop.",
        "The desktop shows exactly these four things.", 20)
    S.q("so-win-p2", "easy", "Which Windows tool shows **running programs, CPU and memory usage**, and lets you end a stuck application?",
        ["Task Manager", "Device Manager", "Control Panel", "Recycle Bin"], "Task Manager",
        "**Task Manager** (Ctrl+Shift+Esc) lists processes with their CPU/RAM load and lets you End Task on a 'not responding' app.",
        "Stuck app → Task Manager.", 20)
    S.q("so-win-p2", "easy", "To **change the desktop background, date-time and user accounts**, you would open —",
        ["Settings / Control Panel", "Notepad", "Device Manager", "Task Scheduler"], "Settings / Control Panel",
        "**Settings (Control Panel)** is where system-wide choices live — display, sound, users, network, date and time.",
        "Settings change the machine; tools use it.", 20)
    S.q("so-win-p2", "medium", "Which tool **lists all installed hardware along with its drivers** and flags devices that are not working?",
        ["Device Manager", "Disk Cleanup", "File Explorer", "Snipping Tool"], "Device Manager",
        "**Device Manager** enumerates every hardware component with its driver status — problem devices show a warning mark.",
        "Hardware + drivers → Device Manager.", 25)
    S.q("so-win-p3", "medium", "How does **WordPad** differ from **Notepad**?",
        ["WordPad supports basic text formatting; Notepad saves plain text only", "Notepad supports formatting; WordPad does not", "WordPad cannot save files", "There is no difference"], "WordPad supports basic text formatting; Notepad saves plain text only",
        "**Notepad** = pure plain text (.txt). **WordPad** adds bold, fonts and colours (rich text) — a halfway house between Notepad and MS Word.",
        "Notepad is a pencil; WordPad is a pen with colours.", 25)
    S.q("so-win-p3", "easy", "Which built-in Windows accessory is used for **simple drawing and painting**?",
        ["Paint", "Notepad", "Calculator", "Command Prompt"], "Paint",
        "**Paint** — the drawing accessory for sketches and basic image edits. Notepad writes text; Calculator computes; Command Prompt types commands.",
        "Paint paints.", 20)
    S.q("so-win-p4", "easy", "The **Android** mobile operating system is owned and developed by —",
        ["Apple", "Microsoft", "Google", "Samsung"], "Google",
        "**Google** owns and leads Android (originally built by Android Inc., which Google acquired in 2005); many brands ship it.",
        "Android = Google's robot.", 20)
    S.q("so-win-p4", "easy", "**iOS**, the mobile operating system, runs only on —",
        ["Any Android phone", "Apple devices such as the iPhone and iPad", "Windows laptops", "Linux servers"], "Apple devices such as the iPhone and iPad",
        "**iOS/iPadOS** is Apple's closed-source mobile OS, licensed to run **only on Apple hardware**.",
        "iOS = 'i' = Apple only.", 20)
    S.q("so-win-p1", "hard", "Consider the statements:\n1. Plug and Play needs the user to install drivers manually for every new device.\n2. Windows is a single-user multitasking OS.\n3. The Recycle Bin catches files deleted from a USB pen drive by ordinary Delete.\nWhich are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "2 only",
        "Statement 1 reverses PnP — its whole point is **automatic** detection and configuration. Statement 2 is correct. Statement 3 is wrong: pen-drive deletions usually **bypass the Recycle Bin** (which serves fixed drives).",
        "PnP = automatic; Recycle Bin covers fixed drives, not removable ones.", 35)
    S.q("so-win-p4", "hard", "Match the OS to its maker:\nA. Android  B. iOS  C. Windows  D. macOS",
        ["A-Google, B-Apple, C-Microsoft, D-Apple", "A-Google, B-Microsoft, C-Apple, D-Apple", "A-Apple, B-Google, C-Microsoft, D-Google", "A-Google, B-Apple, C-Apple, D-Microsoft"],
        "A-Google, B-Apple, C-Microsoft, D-Apple",
        "Android → Google; iOS → Apple; Windows → Microsoft; macOS → Apple. Apple owns two OSes (mobile iOS, desktop macOS).",
        "Apple has two; Microsoft has one of each world.", 30)
    return S


def build_file_systems():
    S = Sub("so-file-systems")
    S.notes = """### What a file system does
A **file system** is the OS's rulebook for a disk: how files are named, stored in folders, found again, and protected. When you 'format' a drive, you are writing that rulebook onto it.

### The three file systems exams test
| File system | Best for | Single-file limit | Extra points |
|---|---|---|---|
| **FAT32** | Pen drives, memory cards, maximum compatibility | **4 GB** (minus 1 byte) | No permissions, no journaling; Windows formats volumes only up to 32 GB in it |
| **exFAT** | Big flash drives, cameras | Practically unlimited | Built to remove FAT32's 4-GB wall |
| **NTFS** | Windows system drives (default since XP) | Enormous (far beyond real disks) | **Permissions, journaling** (crash recovery), encryption, huge volumes |

The single most asked line: **a file bigger than 4 GB will not copy into FAT32** — use exFAT or NTFS.
Full forms: FAT = File Allocation Table; NTFS = New Technology File System.

### File names and extensions
A file name has two parts: **name.extension** — e.g. *report.docx*. The **extension** tells the OS which program opens it.

| Extension | File type | Extension | File type |
|---|---|---|---|
| .txt | Plain text | .docx | Word document |
| .xlsx | Excel workbook | .pptx | PowerPoint show |
| .pdf | Portable Document | .jpg/.png | Images |
| .mp3 / .wav | Audio | .mp4 | Video |
| .zip | Compressed archive | .html | Web page |
| .exe | Executable program | .bat | Batch (command) file |

**Forbidden characters in Windows file names:** \\ / : * ? " < > | — a name like *report:final.docx* is rejected.

### Wildcards in search
- **?** masks **exactly one** character: *file?.txt* finds file1.txt, fileA.txt.
- ***** masks **any number** of characters: ***.pdf** finds every PDF; ***report*.xlsx** every Excel file containing 'report'.

### Paths
- **Absolute path** — the full address from the drive: C:\\Users\\Me\\notes.txt
- **Relative path** — the address from the current folder: ..\\notes.txt

### Copy, move and delete — the housekeeping trio
- **Copy** leaves the original in place and creates a duplicate at the destination (Ctrl+C, Ctrl+V).
- **Move** (cut, Ctrl+X) shifts the file — the original disappears.
- **Delete** sends the file to the **Recycle Bin**; restoring brings it back. **Shift+Delete** skips the bin, and files deleted from **removable drives** usually bypass it altogether.
- A file's **Properties** (Alt+Enter) shows its size, dates and the 'read-only' switch that stops accidental edits.

### Quick revision
- FAT32 = 4-GB single-file wall, pendrives; exFAT removes it; NTFS = Windows default with permissions + journaling.
- Formatting lays down the file system; defragmenting reorganises files; cleanup deletes junk.
- ? = exactly one character; * = any number.
- Forbidden name characters: \\ / : * ? " < > |.
- .exe = program, .zip = archive, .docx/.xlsx/.pptx = Office trio."""
    S.pattern("so-fil-p1", "FAT32 / NTFS / exFAT limits", "very common",
        "'Maximum single-file size on FAT32', 'default file system of Windows', 'why will this 6-GB movie not copy to my pendrive', 'which file system supports permissions'.",
        None,
        "1. FAT32 = 4 GB per file, pendrives, no permissions. exFAT = FAT32 without the 4-GB wall, for big flash drives. NTFS = Windows default, permissions + journaling, huge files.\n2. Scenario stems ('cannot copy a movie bigger than …') hide the 4-GB FAT32 limit.\n3. NTFS = New Technology File System; FAT = File Allocation Table.",
        "A 16-GB pen drive formatted as **FAT32** refuses a 6-GB movie file because —",
        "**FAT32 cannot store any single file larger than 4 GB** (minus 1 byte). Reformat the drive as exFAT or NTFS to carry the movie.")
    S.pattern("so-fil-p2", "Wildcards in file search", "very common",
        "'*.pdf will find…', 'which wildcard matches exactly one character?', 'a pattern to find all Excel files containing report'.",
        None,
        "1. ? = exactly one character; * = any number (including zero).\n2. Read the pattern in pieces: *.pdf = name anything + extension pdf.\n3. Trap options swap the two symbols.",
        "In a Windows search, what does the pattern **file?.txt** match?",
        "Any name of exactly **five letters starting with 'file'** — file1.txt, fileA.txt — because ? replaces exactly one character. The * would replace any number.")
    S.pattern("so-fil-p3", "Extension ↔ file-type matching", "common",
        "'.xlsx is a…', 'which extension is an executable?', '.pdf stands for', 'match the column of extensions and programs'.",
        None,
        "1. Office trio: .docx (Word), .xlsx (Excel), .pptx (PowerPoint).\n2. Executable = .exe; batch = .bat; archive = .zip; page = .html; document = .pdf.\n3. For match-the-columns, pair by the program that opens the file.",
        "The file extension **.exe** marks a file as —",
        "An **executable program** — double-clicking it runs the code. That is also why email attachments ending in .exe are treated as dangerous.")
    S.pattern("so-fil-p4", "Formatting and disk housekeeping", "occasional",
        "'Formatting a disk means', 'what does defragmentation do', 'which action deletes everything on a drive and prepares the file system'.",
        None,
        "1. Formatting = laying down a fresh file system on the disk (erasing the file table; a full format also checks the surface).\n2. Defragmentation = rejoining scattered file pieces; Cleanup = deleting junk.\n3. Formatting does **not** increase the disk's capacity — a classic wrong option.",
        "Formatting a hard disk primarily —",
        "**Prepares it by laying down a file system** so the OS can store and find files (and removes existing file records). It does not enlarge the disk or repair files.")

    S.q("so-fil-p1", "easy", "Which file system is the **default for the system drive (C:)** of modern Windows installations?",
        ["FAT32", "exFAT", "NTFS", "ext4"], "NTFS",
        "**NTFS** (New Technology File System) has been the Windows default for hard disks and SSDs since Windows XP — it adds permissions and journaling.",
        "Windows drives = NTFS; pen drives = FAT32/exFAT.", 20)
    S.q("so-fil-p1", "easy", "You cannot copy a **5-GB movie** to a pen drive formatted as **FAT32** because —",
        ["The drive is slower than the disk", "FAT32 cannot hold a single file larger than 4 GB", "Movies need NTFS codecs", "FAT32 supports only text files"], "FAT32 cannot hold a single file larger than 4 GB",
        "The **4-GB single-file limit** is FAT32's most quoted ceiling. The drive's 16–64 GB total size is irrelevant to this per-file wall.",
        "4 GB — FAT32's four walls.", 20)
    S.q("so-fil-p1", "medium", "A photographer needs a **64-GB SD card** that stores individual video files larger than 4 GB and still works in cameras. The best format is —",
        ["FAT32", "exFAT", "NTFS", "ext4"], "exFAT",
        "**exFAT** (extended FAT) removes FAT32's 4-GB file limit and stays light enough for cameras and flash media — the standard choice for large SD cards.",
        "exFAT = FAT32 grown up.", 25)
    S.q("so-fil-p1", "medium", "Which feature does **NTFS** support but **FAT32 does not**?",
        ["Folders", "Long file names", "File and folder permissions with journaling", "Storing more than one file"], "File and folder permissions with journaling",
        "NTFS brings **security permissions** and **journaling** (a log that helps recovery after a crash). Folders and long names exist in both systems.",
        "NTFS = New Technology = new powers: permissions + journal.", 25)
    S.q("so-fil-p2", "easy", "In Windows search, the wildcard **?** stands for —",
        ["Any number of characters", "Exactly one character", "Only a space", "The end of the name"], "Exactly one character",
        "**?** = exactly one character (file?.txt matches file1.txt, fileA.txt). **\\*** = any number of characters.",
        "One question mark, one letter.", 20)
    S.q("so-fil-p2", "easy", "The search pattern **\\*.pdf** will find —",
        ["Only a file literally named *.pdf", "All PDF files in the searched location", "All files except PDFs", "One randomly chosen file"], "All PDF files in the searched location",
        "The **\\*** masks any name, and the extension fixes the type — so every file ending in .pdf is listed.",
        "Star = anything, extension decides the type.", 20)
    S.q("so-fil-p2", "medium", "Which of the following is **NOT a valid** file name in Windows?",
        ["my report_2026.docx", "budget-final (v2).xlsx", "notes:chapter1.pdf", "Photos.JPG"], "notes:chapter1.pdf",
        "The colon (**:**) is one of the forbidden characters (\\ / : * ? \" < > |) because Windows reserves it for drive letters. The other names are legal.",
        "Drive letters use the colon, so file names cannot.", 25)
    S.q("so-fil-p2", "medium", "To find **all Excel files whose names contain the word 'bank'**, the best search pattern is —",
        ["bank.xlsx", "*.xlsx", "*bank*.xlsx", "bank?.xlsx"], "*bank*.xlsx",
        "The first * absorbs anything before 'bank', the second anything after it, and .xlsx fixes the type. bank.xlsx matches only that exact name; *bank*.xlsx catches 'bank2026.xlsx' and 'mybank.xlsx' alike.",
        "Star on both sides of the word, type at the end.", 25)
    S.q("so-fil-p3", "easy", "A file named **result.xlsx** was created in —",
        ["MS Word", "MS Excel", "MS PowerPoint", "Notepad"], "MS Excel",
        "**.xlsx** is the Excel workbook extension (Word = .docx, PowerPoint = .pptx, plain text = .txt).",
        "x is for Excel.", 20)
    S.q("so-fil-p3", "easy", "**.zip** files are —",
        ["Compressed archives of one or more files", "Executables", "Image files", "System drivers"], "Compressed archives of one or more files",
        "A **.zip** stores one or more files in compressed form; tools like 7-Zip or Explorer extract the originals.",
        "Zip = squeezed bag of files.", 20)
    S.q("so-fil-p3", "medium", "**PDF** (the extension .pdf) stands for —",
        ["Printed Document Format", "Portable Document Format", "Public Document File", "Personal Data File"], "Portable Document Format",
        "**Portable Document Format** — a fixed-layout document that looks identical on every device, opened in readers like Adobe Reader or a browser.",
        "P = Portable, always.", 20)
    S.q("so-fil-p4", "medium", "Which statement about **formatting** a disk is correct?",
        ["It increases the disk's storage capacity", "It prepares the disk by laying down a file system", "It repairs damaged files", "It defragments the disk"], "It prepares the disk by laying down a file system",
        "Formatting writes a fresh **file system** (and erases existing file records) so the OS can store and retrieve files. It does not enlarge capacity, repair files or defragment.",
        "Format = new rulebook, not new space.", 25)
    S.q("so-fil-p4", "hard", "Consider the statements:\n1. NTFS keeps a journal that helps recovery after a sudden power cut.\n2. exFAT has the same 4-GB single-file limit as FAT32.\n3. A file name in Windows may contain the * character.\nWhich are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "1 only",
        "Statement 1 is NTFS's headline safety feature. Statement 2 is wrong — removing the 4-GB wall is exFAT's purpose. Statement 3 is wrong: * is a reserved wildcard character, illegal in names.",
        "One right fact, two reversed classics — read slowly.", 35)
    return S
