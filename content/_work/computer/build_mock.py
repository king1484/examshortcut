# -*- coding: utf-8 -*-
"""Mock part: t2-mock-1--computer (20 Q, subtopic = topic id)"""
import sys, os, json, glob, difflib
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, _dump, OUT_MOCK, OUT_TOPIC, TOPIC_IDS

# ---- computed answers ----
b1 = int("1100101", 2);  assert b1 == 101
h1 = format(int("10101110", 2), "X"); assert h1 == "AE"
o1 = int("75", 8); assert o1 == 61
vals = [10, 20, None, 30]            # AVERAGE ignores blank cells
nums = [v for v in vals if v is not None]
avg = sum(nums) / len(nums); assert avg == 20

QS = [
  Q("t2c-q01",
    "Vacuum tubes were the main electronic component of which generation of computers?",
    ["First", "Second", "Third", "Fourth"], 0,
    "First-generation computers (about 1940-56), such as ENIAC and UNIVAC, used vacuum tubes. Transistors came in the second generation, ICs in the third and microprocessors (VLSI) in the fourth.",
    "V-T-I-M: Vacuum tube, Transistor, IC, Microprocessor = generations 1-2-3-4.",
    "easy", "computer-fundamentals", "generations", 25),
  Q("t2c-q02",
    "Who is known as the 'Father of the Computer'?",
    ["Alan Turing", "Charles Babbage", "John von Neumann", "Blaise Pascal"], 1,
    "Charles Babbage designed the Difference Engine and the Analytical Engine. The Analytical Engine had a mill (processor), a store (memory) and punched-card input, the same parts a modern computer has. Turing is linked to computation theory, von Neumann to the stored-program architecture, and Pascal to the Pascaline adder.",
    "Babbage = 'Father of the Computer'; Turing = 'Father of computer science / AI'.",
    "easy", "computer-fundamentals", "pioneers", 25),
  Q("t2c-q03",
    "The binary number 1100101 is equal to which decimal number?",
    ["99", "101", "103", "105"], 1,
    "1100101 = 64 + 32 + 0 + 0 + 4 + 0 + 1 = 101.",
    "Write the place values 64-32-16-8-4-2-1 above the digits and add the ones under a 1.",
    "medium", "hardware-memory", "number conversion", 45),
  Q("t2c-q04",
    "Convert (10101110) base 2 into its base-16 equivalent.",
    ["AE", "EA", "BE", "A6"], 0,
    "Split into groups of 4 bits from the right: 1010 | 1110 = 10 | 14 = A | E, so the answer is AE.",
    "Binary to hex: 4-bit groups; binary to octal: 3-bit groups.",
    "medium", "hardware-memory", "number conversion", 45),
  Q("t2c-q05",
    "Which of the following is the FASTEST memory in a computer?",
    ["Cache memory", "CPU registers", "Main memory (RAM)", "Solid-state drive"], 1,
    "Registers sit inside the CPU and work at processor speed. Speed order: registers > cache > RAM > SSD > HDD. Capacity runs the other way.",
    "The closer to the CPU, the faster, smaller and costlier.",
    "easy", "hardware-memory", "memory hierarchy", 30),
  Q("t2c-q06",
    "Pick the operating system whose source code is freely available to study, modify and redistribute (open source).",
    ["Windows 11", "macOS", "Linux", "iOS"], 2,
    "Linux (Linus Torvalds, 1991) is released under the GPL, so its source code is free to view, change and share. Windows, macOS and iOS are proprietary.",
    "Open source = source code published under a free licence: Linux, Ubuntu, Fedora.",
    "easy", "software-os", "software types", 25),
  Q("t2c-q07",
    "In computing, the abbreviation GUI stands for:",
    ["General User Interface", "Graphical User Interface", "Graphical Unified Interface", "Guided User Instruction"], 1,
    "A Graphical User Interface lets users work through windows, icons, menus and a pointer (WIMP) instead of typed commands (CLI). Windows and macOS are GUI operating systems; MS-DOS is CLI.",
    "GUI = click on pictures; CLI = type commands.",
    "easy", "software-os", "abbreviations", 25),
  Q("t2c-q08",
    "In MS Word, Header and Footer options are available on which tab?",
    ["Home", "Insert", "Layout", "Review"], 1,
    "Insert -> Header & Footer group has Header, Footer and Page Number. Double-clicking the top or bottom margin also opens the header or footer.",
    "Things you ADD to a page (tables, pictures, headers, page numbers) live on Insert.",
    "easy", "ms-word", "ribbon tabs", 30),
  Q("t2c-q09",
    "Which keyboard shortcut centres the selected text in MS Word?",
    ["Ctrl+C", "Ctrl+E", "Ctrl+J", "Ctrl+R"], 1,
    "Ctrl+E centres text. Ctrl+C copies, Ctrl+J justifies and Ctrl+R right-aligns.",
    "L-E-R-J: Left, cEntre, Right, Justify.",
    "easy", "ms-word", "shortcut recall", 25),
  Q("t2c-q10",
    "A student enters =AVERAGE(B2:B5) where B2 = 10, B3 = 20, B4 is left empty and B5 = 30. The result shown is:",
    ["15", "20", "60", "#DIV/0!"], 1,
    "AVERAGE ignores empty cells, so it computes (10 + 20 + 30) / 3 = 20. Answering 15 means dividing by 4, which wrongly counts the blank as a value.",
    "Blank cells are skipped; a cell containing 0 is counted.",
    "medium", "ms-excel", "function output", 40),
  Q("t2c-q11",
    "Every formula in MS Excel must begin with which character?",
    ["#", "=", "$", "@"], 1,
    "A formula starts with the equals sign (for example =A1+B1). # starts error values, $ marks an absolute reference, and @ is the implicit-intersection operator.",
    "No '=' means Excel treats the entry as text or a number, not a formula.",
    "easy", "ms-excel", "basics", 20),
  Q("t2c-q12",
    "In MS PowerPoint, the Rehearse Timings and Set Up Slide Show commands are found on which tab?",
    ["Transitions", "Slide Show", "View", "Review"], 1,
    "The Slide Show tab has From Beginning, From Current Slide, Set Up Slide Show, Rehearse Timings and Record. The View tab switches editing views such as Normal and Slide Sorter.",
    "Anything about RUNNING the show lives on the Slide Show tab.",
    "medium", "ms-powerpoint", "ribbon tabs", 30),
  Q("t2c-q13",
    "HTTP, the protocol used to transfer web pages, stands for:",
    ["HyperText Transfer Protocol", "High Transfer Text Protocol", "HyperText Transmission Process", "Hyperlink Text Transfer Protocol"], 0,
    "HyperText Transfer Protocol (port 80) carries web pages between server and browser. HTTPS is the same protocol secured with TLS, on port 443.",
    "HTML is the language of the page; HTTP is the protocol that transfers it.",
    "easy", "internet-email", "abbreviations", 20),
  Q("t2c-q14",
    "An e-mail that has been written and saved but not yet sent is stored in which folder?",
    ["Inbox", "Outbox", "Drafts", "Sent Items"], 2,
    "Unsent, saved messages stay in Drafts until you send or delete them. The Outbox briefly holds mail that has been sent but not yet delivered to the server, Sent Items keeps delivered copies, and the Inbox holds received mail.",
    "Drafts = saved but not sent; Outbox = sent but waiting in the queue.",
    "easy", "internet-email", "e-mail folders", 25),
  Q("t2c-q15",
    "In which network topology are all computers connected to a single common cable (backbone) with terminators at both ends?",
    ["Star", "Ring", "Bus", "Mesh"], 2,
    "A bus topology shares one backbone cable, and a break in that cable stops the whole network. Star uses a central hub or switch, ring forms a closed loop, and mesh links every node to every other node.",
    "Bus = one road that everyone rides.",
    "easy", "networking", "topologies", 25),
  Q("t2c-q16",
    "An FTP client sends its login and file commands to the server on which well-known port?",
    ["21", "23", "25", "110"], 0,
    "FTP uses port 21 for control (commands) and port 20 for data in active mode. 23 is Telnet, 25 is SMTP and 110 is POP3.",
    "20/21 FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 80 HTTP, 110 POP3, 143 IMAP, 443 HTTPS.",
    "medium", "networking", "port numbers", 30),
  Q("t2c-q17",
    "Software that automatically shows unwanted pop-up advertisements, often bundled with free programs, is called:",
    ["Adware", "Rootkit", "Worm", "Ransomware"], 0,
    "Adware displays or injects ads to earn money for its author. A rootkit hides deep in the system to keep privileged access, a worm spreads over networks by itself, and ransomware encrypts files for a ransom.",
    "AD-ware = ADvertisements.",
    "easy", "cyber-security", "malware types", 25),
  Q("t2c-q18",
    "The padlock icon and 'https://' in a browser's address bar mean that:",
    ["The website is guaranteed to be free of fraud", "Data between the browser and the site is encrypted using SSL/TLS", "The site is hosted by the government", "The page is loaded from the local cache"], 1,
    "The padlock shows that the connection is encrypted with TLS (the successor to SSL) and that the site's certificate is valid for that domain. It does NOT prove the site is honest: phishing sites can also use HTTPS.",
    "Padlock = private channel, not a trustworthy owner.",
    "medium", "cyber-security", "preventive measures", 35),
  Q("t2c-q19",
    "Which Windows shortcut opens File Explorer?",
    ["Win+E", "Win+F", "Win+X", "Ctrl+E"], 0,
    "Win+E opens File Explorer. Win+X opens the Quick Link menu, Win+F opens Feedback Hub on Windows 10/11, and Ctrl+E centres text in Word or focuses the search box inside Explorer.",
    "E = Explorer.",
    "easy", "keyboard-shortcuts", "windows shortcuts", 25),
  Q("t2c-q20",
    "A browser tab was closed by mistake. Which shortcut reopens it?",
    ["Ctrl+Shift+T", "Ctrl+Shift+N", "Ctrl+Z", "Ctrl+T"], 0,
    "Ctrl+Shift+T restores the most recently closed tab (press again for older ones). Ctrl+T opens a blank new tab, Ctrl+Shift+N opens an incognito window, and Ctrl+Z undoes only text edits.",
    "Shift turns 'new tab' (Ctrl+T) into 'bring the tab back'.",
    "medium", "keyboard-shortcuts", "browser shortcuts", 25),
]

assert len(QS) == 20
cnt = Counter(q["subtopic"] for q in QS)
assert set(cnt) == set(TOPIC_IDS), cnt

# ---- no duplicates of topic questions ----
existing = []
for f in glob.glob(os.path.join(OUT_TOPIC, "*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for q in d["solvedExamples"] + d["practice"]:
        existing.append((q["id"], q["q"].lower(), q["options"][q["answer"]].lower()))
for q in QS:
    for eid, eq, ea in existing:
        r = difflib.SequenceMatcher(None, q["q"].lower(), eq).ratio()
        assert r < 0.75, f"{q['id']} too close to {eid} ({r:.2f})"
        assert not (q["options"][q["answer"]].lower() == ea and r > 0.5), f"{q['id']} same fact as {eid}"

_dump({"mockId": "t2-mock-1", "sectionId": "computer", "questions": QS},
      os.path.join(OUT_MOCK, "t2-mock-1--computer.json"))
print(dict(cnt))
