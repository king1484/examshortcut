"""hardware-memory deep content — part 2: I/O devices, ports, storage media."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_io():
    S = Sub("hm-io-devices")
    S.notes = """### Input devices — data goes IN
Anything that feeds data or commands to the computer is an **input** device.

| Group | Devices |
|---|---|
| Typing / pointing | Keyboard, mouse, trackball, touchpad, joystick, light pen, stylus |
| Capture | Scanner, digital camera, webcam, microphone |
| Readers | **Barcode/QR reader** (shops), **OMR** (answer sheets), **OCR** (scanned text), **MICR** (bank cheques), biometric scanner (fingerprint, iris) |

The reader trio by one word each: **OMR = Marks** (pencil bubbles), **OCR = Characters** (printed text becomes editable text), **MICR = Ink** (magnetic characters on cheques).

### Output devices — results come OUT
| Device | Gives |
|---|---|
| **Monitor** | **Soft copy** — output you can see but not touch |
| **Printer** | **Hard copy** — output on paper |
| **Speaker / headphones** | Sound |
| **Plotter** | Hard copy of **large drawings and maps** (engineering, architecture) |
| **Projector** | A big soft copy on a screen |

### Printers: impact vs non-impact
| Type | How it works | Examples |
|---|---|---|
| **Impact** | Physically **strikes** the paper through a ribbon | **Dot matrix**, daisy wheel — noisy, cheap, multi-copy forms |
| **Non-impact** | No hitting — sprays ink, fuses toner, or heats paper | **Laser** (toner, fast, office), **inkjet** (liquid ink, home), thermal (bills) |

### Devices that do BOTH
A **touch screen** takes your finger's input and displays output. A **headset** has a mic (in) and speakers (out). Exams ask 'which is both input and output?' — touch screen is the standard answer.

### Pointing devices in one line each
- **Mouse** — the standard pointing device; a ball or optical sensor tracks movement.
- **Trackball** — an upside-down mouse: you roll the ball, the device stays put.
- **Touchpad** — the laptop's flat mouse replacement.
- **Joystick** — direction control for games and flight simulators.
- **Light pen / stylus** — draw or point directly on the screen.
- **Touchpad + pointers all feed position data IN — every one is an input device.**

### Pairing questions (device ↔ use)
| Device | Classic use in exams |
|---|---|
| Barcode reader | Supermarket billing |
| OMR | Evaluating pencil-bubble answer sheets |
| MICR | Reading the cheque code line in banks |
| OCR | Converting a scanned page into editable text |
| Biometric scanner | Attendance, Aadhaar-style identity checks |
| Plotter | Engineering drawings, maps, posters |
| Webcam + mic | Video calls |

### Modern extras
- **3D printer** — builds a physical solid object layer by layer (an output device).
- **Webcam + microphone** — the video-call input pair.

### Quick revision
- Input: keyboard, mouse, scanner, mic, camera, barcode/OMR/OCR/MICR readers, biometrics.
- OMR = Marks, OCR = Characters, MICR = magnetic Ink (cheques).
- Output: monitor (soft copy), printer/plotter (hard copy), speaker, projector.
- Impact = hits paper (dot matrix); non-impact = laser, inkjet, thermal.
- Touch screen = both input and output. 3D printer = solid object output."""
    S.pattern("hm-io-p1", "Input device identification", "very common",
        "'Which is an input device?', 'a barcode reader is used to…', 'joystick is used in…' — pick the device that feeds data in.",
        None,
        "1. Test each option: does data flow INTO the computer (input) or OUT (output)?\n2. Scanner, microphone and camera are input even though they feel like 'media' devices.\n3. Monitor, printer, speaker, plotter, projector are always output.",
        "Which of the following is an **input** device?",
        "**Scanner** — it feeds a paper document into the computer as an image. Monitor, speaker and plotter all send data out.")
    S.pattern("hm-io-p2", "Output device identification; soft vs hard copy", "very common",
        "'Which is an output device?', 'printed output is called a … copy', 'monitor output is called a … copy'.",
        None,
        "1. Soft copy = on screen (monitor, projector); hard copy = on paper (printer, plotter).\n2. Speaker and headphones are output (sound).\n3. 'Touch screen' is the planted trap in output-only questions — it is both.",
        "Output shown **on paper** (a printout) is called a —",
        "**Hard copy** — permanent, touchable output. Output on a monitor is a soft copy.")
    S.pattern("hm-io-p3", "Both input and output / odd one out", "common",
        "'Which device works as both input and output?', 'which is NOT an input device?' — one option breaks the family.",
        None,
        "1. Both-direction devices: touch screen, headset (mic + speaker), fax machine (classic), smart TV with voice remote.\n2. For 'not an input', look for the printer, monitor or speaker hiding in the list.\n3. Classify each option before reading the stem twice — speed comes from the table.",
        "Which device acts as **both an input and an output** device?",
        "**Touch screen** — your touch is input and the display is output. A mouse is input-only; a monitor is output-only.")
    S.pattern("hm-io-p4", "Printer technology and reader classification", "common",
        "'Which is an impact printer?', 'laser printer is non-impact because…', 'OCR converts…', 'plotter is used for…', '3D printer makes…'.",
        None,
        "1. Impact = physical strike (dot matrix, daisy wheel); non-impact = laser, inkjet, thermal.\n2. Readers by one word: OMR marks, OCR characters, MICR magnetic ink.\n3. Plotter = large-format drawings; 3D printer = solid objects layer by layer.",
        "Which of the following is an **impact** printer?",
        "**Dot matrix** — its pins physically strike the ribbon against the paper. Laser, inkjet and thermal printers never touch the paper with force.")

    S.q("hm-io-p1", "easy", "Which of the following is an **input** device?",
        ["Plotter", "Monitor", "Scanner", "Speaker"], "Scanner",
        "A **scanner** converts a paper document into digital data flowing **into** the computer. The other three all receive data from it.",
        "Data in = input. Plotters, monitors, speakers push data out.", 20)
    S.q("hm-io-p1", "easy", "A **joystick** is mainly used as an input device for —",
        ["Printing documents", "Playing games and flight simulation", "Scanning photographs", "Producing sound"], "Playing games and flight simulation",
        "A **joystick** feeds direction commands into the computer — the classic controller for games and flight simulators.",
        "Joystick = steering stick for games.", 20)
    S.q("hm-io-p1", "medium", "In supermarkets, the device that reads the **black-and-white striped code** on products is the —",
        ["OMR reader", "Barcode reader", "MICR reader", "Plotter"], "Barcode reader",
        "A **barcode reader** (or scanner) reads the striped product code and sends it to the billing system. OMR reads bubbles, MICR reads cheque ink.",
        "Stripes on products = barcode.", 20)
    S.q("hm-io-p1", "medium", "A **biometric device** that opens a laptop by reading your fingerprint works as a(n) —",
        ["Output device", "Input device", "Storage device", "Processing device"], "Input device",
        "The fingerprint scanner feeds your biometric data **into** the system — an input device (same family as iris and face readers).",
        "It reads you, then the computer checks — data flows in.", 25)
    S.q("hm-io-p2", "easy", "Which of the following is an **output** device?",
        ["Keyboard", "Microphone", "Monitor", "Scanner"], "Monitor",
        "The **monitor** displays processed results — output. Keyboard, microphone and scanner all send data in.",
        "Screens show; they don't type.", 20)
    S.q("hm-io-p2", "easy", "Output on a **monitor** (seen but not printed) is called a —",
        ["Hard copy", "Soft copy", "Printout", "Backup"], "Soft copy",
        "**Soft copy** = screen output, temporary and intangible. Paper output is a hard copy.",
        "Soft = screen, hard = paper.", 20)
    S.q("hm-io-p2", "medium", "**Large engineering drawings and maps** are best printed on a —",
        ["Dot matrix printer", "Plotter", "Thermal printer", "Webcam"], "Plotter",
        "A **plotter** draws continuous large-format lines — the standard output device for CAD drawings, maps and posters.",
        "Big drawings need a plotter's pen arm.", 25)
    S.q("hm-io-p3", "easy", "Which of the following is **NOT** an input device?",
        ["Keyboard", "Mouse", "Printer", "Microphone"], "Printer",
        "The **printer** produces output. Keyboard, mouse and microphone are all input devices.",
        "Three inputs and one output — spot the odd direction.", 20)
    S.q("hm-io-p3", "easy", "Which device serves as **both** input and output?",
        ["Touch screen", "Mouse", "Speaker", "Scanner"], "Touch screen",
        "A **touch screen** takes your taps as input and shows results as output — both roles in one panel.",
        "You touch it (in) and read it (out).", 20)
    S.q("hm-io-p3", "medium", "A **headset** used for a video call contains which input–output pair?",
        ["Scanner and printer", "Microphone (input) and speakers (output)", "Monitor and keyboard", "Plotter and webcam"], "Microphone (input) and speakers (output)",
        "The **mic sends your voice in** (input); the **speakers bring the other voice out** (output) — one device, both directions.",
        "Mic in, speaker out.", 25)
    S.q("hm-io-p4", "easy", "Which of the following is an **impact** printer?",
        ["Laser printer", "Inkjet printer", "Dot matrix printer", "Thermal printer"], "Dot matrix printer",
        "**Dot matrix** pins strike an inked ribbon against the paper — the definition of impact printing. Laser and inkjet never hit the paper.",
        "If it hits, it's impact.", 20)
    S.q("hm-io-p4", "medium", "**OCR** technology is used to —",
        ["Read pencil bubbles on answer sheets", "Convert scanned/printed characters into editable text", "Read magnetic ink on cheques", "Print 3D objects"], "Convert scanned/printed characters into editable text",
        "**OCR = Optical Character Recognition** — it turns an image of printed or handwritten characters into real editable text. Bubbles = OMR; cheque ink = MICR.",
        "OCR = Characters.", 25)
    S.q("hm-io-p4", "medium", "A **3D printer** differs from ordinary printers because it —",
        ["Prints faster on paper", "Builds a physical solid object layer by layer", "Uses magnetic ink", "Works without a computer"], "Builds a physical solid object layer by layer",
        "A **3D printer** is an output device that adds material layer after layer to create a real solid model — no paper involved.",
        "Layers, not pages.", 25)
    S.q("hm-io-p4", "hard", "Consider the statements:\n1. Dot matrix is an impact printer.\n2. Laser printer is a non-impact printer.\n3. A plotter is mainly used for printing text documents.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are the standard printer classification. Statement 3 is wrong — plotters are for **large drawings, maps and CAD**, not text.",
        "Plotters draw; printers type.", 35)
    return S


def build_ports():
    S = Sub("hm-ports")
    S.notes = """### What a port is
A **port** is a socket on the cabinet where a cable or device plugs in. Each port has a job — carry video, connect a network, take a keyboard — and exams ask "which port for which job?".

### Serial vs parallel — the classic comparison
| | Serial port | Parallel port |
|---|---|---|
| Bits per transfer | **One bit at a time** | **A whole byte (8 bits) at once** |
| Wires | Few | Many |
| Distance | Long distances, less interference | Short distances |
| Classic use | Old modems, mice (COM port) | Old printers (LPT port) |

Memory hook: **S**erial = **S**ingle lane; **P**arallel = multi-lane highway.

### The port table
| Port | Job |
|---|---|
| **USB** (Universal Serial Bus) | Everything today — pen drives, keyboards, phones. **Hot-swappable** and **supplies power (5 V)** |
| **HDMI** | **Digital video + audio** in one cable — monitor, TV, projector |
| **VGA** | **Analog video only** (15-pin, blue) — older monitors; no sound |
| **DisplayPort** | Digital video + audio, common on PCs and monitors |
| **Ethernet (RJ-45)** | Wired network/LAN connection |
| **PS/2** | Round 6-pin — old **keyboard and mouse** |
| **Audio jack (3.5 mm)** | Speakers, headphones, mic (green = out, pink = mic) |
| **Serial (COM/RS-232)** | One-bit-at-a-time legacy data link |
| **Parallel (LPT)** | Legacy 25-pin printer port |

### USB facts exams like
- **Hot-swappable** — connect or remove **while the computer runs**, no restart.
- USB **supplies power**, so pen drives and small keyboards need no adapter.
- Speeds grew by generation: USB 2.0 ≈ 480 Mbps, USB 3.0 ≈ 5 Gbps.
- USB Type-C — the small reversible oval plug now common on phones and laptops.

### How exam questions sound
| Stem words | Answer |
|---|---|
| 'Picture and sound, one digital cable' | HDMI |
| 'Old blue connector, video only' | VGA |
| 'One bit at a time' | Serial (COM) |
| 'Printer port of old machines' | Parallel (LPT) |
| 'Network cable socket' | Ethernet / RJ-45 |
| 'Round purple and green sockets' | PS/2 keyboard and mouse |
| 'Plug in without restarting' | USB (hot-swap) |
| 'Speakers, green round hole' | 3.5 mm audio jack |

### A 10-second method
1. Underline the JOB in the stem (video? sound? network? data direction?).
2. Match the job to the table row — ports are defined by what they carry.
3. If two options look close, drop the one whose extra capability the stem excludes (VGA fails any 'audio' stem; parallel fails any 'long distance' stem).

### Quick revision
- Serial = 1 bit at a time, long distance; parallel = 8 bits (a byte), printers (LPT).
- HDMI = digital audio + video; VGA = analog video only, no audio.
- Ethernet/RJ-45 = network; PS/2 = old keyboard/mouse; 3.5 mm = audio.
- USB = hot-swappable + supplies power; USB 2.0 ≈ 480 Mbps, USB 3.0 ≈ 5 Gbps."""
    S.pattern("hm-por-p1", "Serial vs parallel comparison", "very common",
        "'How many bits does a parallel port send?', 'which port sends one bit at a time?', 'which port was used for printers (LPT)?', statement pairs on wires and distance.",
        None,
        "1. Serial = 1 bit at a time, few wires, long distance. Parallel = 8 bits (a byte) at once, short distance, old printer port (LPT).\n2. 'One bit at a time' always means serial — even if USB is also serial inside.\n3. Statement versions plant a reversal (serial = 8 bits) — check each number.",
        "A **parallel port** transfers how much data per transfer?",
        "**A full byte (8 bits) at once** — eight wires side by side. A serial port moves the same byte as 8 single bits in sequence.")
    S.pattern("hm-por-p2", "Port identification by purpose", "very common",
        "'Which port connects to a network?', 'video + audio in one digital cable', 'the round port for an old keyboard', 'green socket for speakers'.",
        None,
        "1. Network = Ethernet/RJ-45; digital AV = HDMI/DisplayPort; analog video only = VGA; old keyboard/mouse = PS/2; speakers/headphones = 3.5 mm audio jack.\n2. 'Single cable, picture and sound, digital' = HDMI in exam language.\n3. USB is the universal fallback — if no specific job matches, USB fits.",
        "Which port connects a computer to a **wired LAN/network**?",
        "The **Ethernet port (RJ-45)** — the wide tabbed socket that takes the network cable.")
    S.pattern("hm-por-p3", "USB facts (hot-swap, power, versions)", "common",
        "'Hot-swappable means…', 'why does a pen drive work without its own power?', 'USB 3.0 is faster than 2.0 because…'.",
        None,
        "1. Hot-swappable = plug/unplug **while the PC is running**, no restart.\n2. USB carries **power (5 V)** along with data — that is why pen drives need no adapter.\n3. Version speeds: USB 2.0 ≈ 480 Mbps, USB 3.0 ≈ 5 Gbps (about 10× faster).",
        "USB is called **hot-swappable** because —",
        "You can connect or remove a USB device **while the computer is running** — no shutdown or restart needed.")
    S.pattern("hm-por-p4", "Display and audio ports", "common",
        "'Which port carries only video?', 'VGA vs HDMI', 'which port for speakers?', statements about analog/digital video.",
        None,
        "1. VGA = analog, **video only**, 15 pins. HDMI and DisplayPort = digital, video **+ audio**.\n2. The green 3.5 mm socket = line-out for speakers; pink = microphone.\n3. 'No sound from my VGA monitor cable' is the everyday proof of the exam line.",
        "Which port carries **analog video only**, with no audio?",
        "**VGA** — the 15-pin blue connector of older monitors. HDMI and DisplayPort carry both video and audio in digital form.")

    S.q("hm-por-p1", "easy", "A **parallel** port transfers data —",
        ["One bit at a time", "Eight bits (a byte) at a time", "One file at a time", "Only in one direction, never back"], "Eight bits (a byte) at a time",
        "A parallel port lays **8 wires side by side** and moves a whole byte per transfer — the old printer (LPT) port.",
        "Parallel = 8 lanes.", 20)
    S.q("hm-por-p1", "easy", "Which port was traditionally used to connect **printers** (the LPT port)?",
        ["Serial port", "Parallel port", "PS/2 port", "Ethernet port"], "Parallel port",
        "The 25-pin **parallel (LPT)** port was the standard printer connection before USB took over.",
        "LPT = printer port = parallel.", 20)
    S.q("hm-por-p1", "medium", "**Serial** ports suit slow data over long distances mainly because they —",
        ["Send 8 bits together", "Need fewer wires, so the signal stays stable over long cables", "Carry audio and video", "Work only with printers"], "Need fewer wires, so the signal stays stable over long cables",
        "Sending **one bit after another** needs only a few conductors — cheaper, less interference, reliable across long cables. Parallel's many wires limit it to short runs.",
        "Fewer wires = longer reach.", 25)
    S.q("hm-por-p2", "easy", "Which port carries **digital video and audio** to a TV through a **single cable**?",
        ["VGA", "PS/2", "HDMI", "Serial"], "HDMI",
        "**HDMI** (High-Definition Multimedia Interface) sends picture and sound together in one digital cable.",
        "HDMI = Home theatre: both signals, one wire.", 20)
    S.q("hm-por-p2", "easy", "The **RJ-45** socket on a computer is used for —",
        ["Connecting a printer", "Wired network (LAN) connection", "Plugging headphones", "Attaching an old keyboard"], "Wired network (LAN) connection",
        "**RJ-45** is the Ethernet port — the tabbed socket that accepts the LAN cable.",
        "RJ-45 = network plug.", 20)
    S.q("hm-por-p2", "medium", "The round **6-pin PS/2** ports on older PCs were used for —",
        ["Monitor and speaker", "Keyboard and mouse", "Network and modem", "Scanner and printer"], "Keyboard and mouse",
        "**PS/2** was the dedicated pair of round ports for the keyboard (purple) and mouse (green) before USB replaced them.",
        "PS/2 = the two round holes at the back.", 25)
    S.q("hm-por-p2", "medium", "The **green 3.5 mm socket** at the back of a desktop PC is for —",
        ["Speakers/headphones (line-out)", "Microphone", "Network cable", "Monitor"], "Speakers/headphones (line-out)",
        "On the standard colour code, **green = audio out** (speakers/headphones), pink = microphone, blue = line-in.",
        "Green grows sound out.", 25)
    S.q("hm-por-p3", "easy", "**Hot-swappable** means a device can be —",
        ["Used only when the PC is switched off", "Connected or removed while the computer is running", "Heated for faster data", "Swapped with another brand only"], "Connected or removed while the computer is running",
        "**Hot-swap = plug or unplug with the system running** — no restart. USB is the everyday example.",
        "Hot = PC is on.", 20)
    S.q("hm-por-p3", "easy", "A **pen drive works without its own battery** because —",
        ["It stores its own electricity", "The USB port supplies power (5 V) along with data", "It uses solar cells", "Batteries are built into cables"], "The USB port supplies power (5 V) along with data",
        "USB carries **both data and power** — about 5 volts — so bus-powered devices like pen drives and small keyboards need no adapter.",
        "One cable, two jobs: data + power.", 20)
    S.q("hm-por-p3", "hard", "Consider the statements about **USB**:\n1. It is hot-swappable.\n2. It supplies electrical power to connected devices.\n3. It sends data as a serial stream.\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three define USB: hot-swappable, bus-powered (5 V), and **serial** (the S in USB — Universal Serial Bus, one bit at a time).",
        "The full form itself confirms statement 3.", 35)
    S.q("hm-por-p4", "easy", "Which port carries **video only** and **no audio**?",
        ["HDMI", "VGA", "DisplayPort", "Thunderbolt"], "VGA",
        "**VGA** is the analog video-only standard — the 15-pin blue connector. HDMI and DisplayPort carry audio too.",
        "VGA = Video Graphics Array — video's in the name.", 20)
    S.q("hm-por-p4", "medium", "Which statement comparing **VGA and HDMI** is correct?",
        ["Both carry audio", "VGA is digital and HDMI is analog", "VGA is analog video-only; HDMI is digital audio + video", "HDMI works only with printers"], "VGA is analog video-only; HDMI is digital audio + video",
        "VGA = old analog, picture only. HDMI = modern digital, picture **and** sound in one cable — that is why one HDMI wire replaces a VGA plus an audio cable.",
        "The cable count proves the exam line.", 25)
    S.q("hm-por-p1", "hard", "Consider the statements:\n1. A serial port sends one bit at a time.\n2. The parallel (LPT) port was traditionally used for printers.\n3. A VGA cable carries stereo audio.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are the serial/parallel classics. Statement 3 is wrong — **VGA is video-only**; audio needs a separate cable.",
        "VGA never carries sound — the standing trap.", 35)
    return S


def build_storage():
    S = Sub("hm-storage")
    S.notes = """### Primary vs secondary storage
**Primary memory** (RAM, cache) is fast but small and (for RAM) volatile. **Secondary storage** is large, permanent and cheaper per GB — everything below is secondary.

### The three technologies
| Family | How it stores | Examples |
|---|---|---|
| **Magnetic** | Magnetised spots on spinning platters or tape | **HDD** (hard disk), old floppy, **magnetic tape (LTO)** |
| **Optical** | Tiny pits read by a **laser** | **CD, DVD, Blu-ray** |
| **Flash (solid-state)** | Floating-gate memory chips, no moving parts | **SSD, pen drive, memory card, smartphone storage** |

### Capacities to memorise (the exam's favourite row)
| Disc | Capacity (single layer) | Laser |
|---|---|---|
| **CD** | **700 MB** | infrared/red |
| **DVD** | **4.7 GB** (dual-layer ≈ 8.5 GB) | red |
| **Blu-ray** | **25 GB** (dual-layer ≈ 50 GB) | **blue-violet** (shorter wavelength → tighter pits → more data) |

Ladder for one-mark questions: **CD (0.7 GB) < DVD (4.7 GB) < Blu-ray (25 GB)**.

### HDD vs SSD (asked almost every year)
| | HDD | SSD |
|---|---|---|
| Parts | Spinning **magnetic platters** + moving heads | **Flash chips**, no moving parts |
| Speed | Slower (heads must seek) | Much faster |
| Shock / noise | Sensitive, some noise | Shock-resistant, silent |
| Cost per GB | Cheaper | Costlier |

### Access methods
- **Random (direct) access** — jump straight to any address: RAM, HDD, SSD, disc with a file system.
- **Sequential access** — read through in order, like a cassette: **magnetic tape**. That is why tape is cheap and perfect for **archival backups**, not for daily use.

### Backup ideas
- **Cloud storage/backup** — your files copied to internet servers (anywhere access).
- **Tape libraries** — banks and research labs still archive petabytes on tape.
- The 3-2-1 habit: three copies, two media, one off-site — a good phrase for one-liners.

### Everyday capacity anchors (for rejecting silly options)
- One MP3 song ≈ 4–8 MB; a 90-minute movie ≈ 1–4 GB; a phone ≈ 64–256 GB; a laptop SSD ≈ 512 GB–1 TB; a data-centre shelf ≈ many TB.
- So 'a CD holds 4.7 GB' should feel wrong instantly — that is DVD territory.

### One-line differentiators exams quote
- **Floppy disk** — the 1.44 MB magnetic ancestor, long obsolete but still asked for its capacity.
- **Memory card** — flash storage for cameras and phones (SD, microSD).
- **Blu-ray's name** comes from its blue-violet laser, not from any brand.
- **Formatting** prepares a disk's file system; it does not add capacity.

### Quick revision
- Magnetic = HDD, tape; optical = CD/DVD/Blu-ray (laser-read pits); flash = SSD, pen drive.
- CD 700 MB → DVD 4.7 GB → Blu-ray 25 GB (blue-violet laser); DVD dual ≈ 8.5 GB.
- SSD: no moving parts, faster, costlier, shock-proof. HDD: magnetic platters, cheaper per GB.
- Tape = sequential access, archival backup; disk/SSD = random access.
- Cloud backup = copies held on internet servers."""
    S.pattern("hm-sto-p1", "Optical-media capacity matching", "very common",
        "'Capacity of a CD/DVD/Blu-ray?', 'arrange by capacity', 'dual-layer DVD holds', 'which disc uses a blue-violet laser'.",
        None,
        "1. One row: CD = 700 MB, DVD = 4.7 GB (dual ≈ 8.5 GB), Blu-ray = 25 GB (dual ≈ 50 GB).\n2. Ordering questions run CD < DVD < Blu-ray.\n3. The blue-violet (shorter-wavelength) laser is Blu-ray's identifying fact.",
        "A **single-layer DVD** stores about —",
        "**4.7 GB** (a dual-layer DVD ≈ 8.5 GB). The 700 MB figure belongs to a CD; 25 GB to a single-layer Blu-ray.")
    S.pattern("hm-sto-p2", "HDD vs SSD vs flash", "very common",
        "'Which storage has no moving parts?', 'why is an SSD faster?', 'a pen drive uses which memory?', 'HDD stores data on…'.",
        None,
        "1. HDD = spinning magnetic platters + heads; SSD/pen drive = flash chips, no moving parts.\n2. SSD's speed comes from zero mechanical seek time; it is also silent and shock-resistant.\n3. Flash is non-volatile — data stays without power, unlike RAM.",
        "Why is an **SSD** faster than an **HDD**?",
        "The SSD has **no mechanical parts** — no platters to spin up, no heads to seek — so access takes microseconds instead of milliseconds.")
    S.pattern("hm-sto-p3", "Backup and access methods", "common",
        "'Which medium for archival backup?', 'sequential access example', 'storing backups on internet servers is called'.",
        None,
        "1. Archival = magnetic tape (LTO): cheapest per TB, sequential access.\n2. Sequential = read in order (tape, cassette); random/direct = jump to any address (disk, SSD).\n3. Copies on internet servers = cloud storage/backup.",
        "Which storage medium uses **sequential access**, reading data strictly in order?",
        "**Magnetic tape** — like a cassette, the drive must wind past everything before the needed block. Disks and SSDs give random (direct) access.")
    S.pattern("hm-sto-p4", "Media odd-one-out and matching", "common",
        "'Which is NOT an optical medium?', 'match disc to capacity', 'which is a magnetic storage device?'.",
        None,
        "1. Optical family = CD, DVD, Blu-ray (laser-read). Anything else (HDD, pen drive, tape) breaks the family.\n2. Magnetic family = HDD, floppy, tape. Flash family = SSD, pen drive, memory card.\n3. For matching, pair by the capacity row first, then by technology.",
        "Which of the following is **NOT** an optical storage medium?",
        "**Hard disk** — it is magnetic. CD, DVD and Blu-ray are all read by lasers, which defines optical storage.")

    S.q("hm-sto-p1", "easy", "The storage capacity of a standard **CD-ROM** is about —",
        ["700 MB", "4.7 GB", "25 GB", "1.44 MB"], "700 MB",
        "A standard CD holds about **700 MB**. 4.7 GB is a single-layer DVD, 25 GB a single-layer Blu-ray, and 1.44 MB was the old floppy.",
        "CD-700, DVD-4.7, BD-25.", 20)
    S.q("hm-sto-p1", "easy", "A **single-layer DVD** stores approximately —",
        ["700 MB", "4.7 GB", "25 GB", "64 GB"], "4.7 GB",
        "**4.7 GB** per layer — about seven CDs' worth. Dual-layer DVDs reach roughly 8.5 GB.",
        "DVD = 4.7 GB single layer.", 20)
    S.q("hm-sto-p1", "medium", "Which disc uses a **blue-violet laser**, letting it store far more data than a DVD?",
        ["CD-ROM", "DVD-R", "Blu-ray Disc", "Floppy disk"], "Blu-ray Disc",
        "**Blu-ray**'s blue-violet laser has a shorter wavelength, so pits can be packed tighter — 25 GB on a single layer (hence the name 'Blu-ray').",
        "Blue laser = Blu-ray.", 25)
    S.q("hm-sto-p1", "medium", "Arrange by **increasing capacity** (single layer): A. DVD  B. CD  C. Blu-ray",
        ["B, A, C", "A, B, C", "C, A, B", "B, C, A"], "B, A, C",
        "CD (700 MB) < DVD (4.7 GB) < Blu-ray (25 GB) — **B, A, C**.",
        "0.7 → 4.7 → 25.", 25)
    S.q("hm-sto-p1", "hard", "A **dual-layer DVD** stores roughly —",
        ["8.5 GB", "4.7 GB", "17 GB", "700 MB"], "8.5 GB",
        "Two layers of about 4.7 GB and 3.8 GB give a dual-layer DVD roughly **8.5 GB** — nearly double the single-layer figure.",
        "Two layers ≈ 4.7 + 3.8 ≈ 8.5 GB.", 30)
    S.q("hm-sto-p2", "easy", "Which storage device has **no moving parts**?",
        ["Hard disk drive", "DVD drive", "SSD (flash) drive", "Magnetic tape"], "SSD (flash) drive",
        "An **SSD** is pure flash chips — nothing spins or seeks. HDDs, DVD drives and tapes are all mechanical.",
        "No moving parts = solid state.", 20)
    S.q("hm-sto-p2", "easy", "A **pen drive** stores data on —",
        ["Magnetic platters", "Flash memory chips", "Optical pits", "Paper tape"], "Flash memory chips",
        "Pen drives (and memory cards, SSDs) use **flash memory** — non-volatile chips that keep data without power.",
        "Pen drive = flash in your pocket.", 20)
    S.q("hm-sto-p2", "easy", "A traditional **hard disk (HDD)** stores data on —",
        ["Magnetised spinning platters", "Flash chips", "Laser-etched discs", "ROM gates"], "Magnetised spinning platters",
        "The HDD's arms read and write **magnetic patterns on spinning platters** — a mechanical, cheaper-per-GB design.",
        "Hard disk = hard platters that spin.", 20)
    S.q("hm-sto-p2", "medium", "Which is a reason an **HDD** is still preferred over an SSD in some systems?",
        ["It is faster", "It is cheaper per GB for large capacities", "It has no moving parts", "It uses less power always"], "It is cheaper per GB for large capacities",
        "HDDs lose on speed and shock-resistance but win clearly on **cost per terabyte** — the reason bulk storage still ships on spinning disks.",
        "Speed buys SSD; bulk buys HDD.", 25)
    S.q("hm-sto-p3", "easy", "Banks and research labs archive huge volumes on **magnetic tape** because it is —",
        ["The fastest medium", "Very cheap per TB and durable for long-term storage", "A random-access medium", "The only optical medium"], "Very cheap per TB and durable for long-term storage",
        "Tape wins on **cost and longevity**, not speed — perfect for archives that are rarely read.",
        "Archive on tape; work on disk.", 25)
    S.q("hm-sto-p3", "easy", "Keeping backup copies of files on **internet servers** so they are reachable anywhere is called —",
        ["Defragmentation", "Cloud storage/backup", "Disk imaging to tape only", "Formatting"], "Cloud storage/backup",
        "**Cloud backup** copies your data to remote servers over the internet — accessible from any device with a login.",
        "Backup in the 'sky' = cloud.", 20)
    S.q("hm-sto-p3", "medium", "Which storage medium gives **random (direct) access**?",
        ["Magnetic tape", "Hard disk", "Audio cassette", "Punched paper tape"], "Hard disk",
        "A hard disk's heads jump straight to any track — **random access**. Tape must be wound through everything in between — sequential.",
        "Tape winds; disks jump.", 25)
    S.q("hm-sto-p4", "easy", "Which of the following is **NOT** an optical storage medium?",
        ["CD", "DVD", "Blu-ray Disc", "Pen drive"], "Pen drive",
        "A **pen drive** is flash storage — no laser, no pits. CD, DVD and Blu-ray are all read optically.",
        "Laser family: CD-DVD-BD. Flash family: pen drive, card, SSD.", 20)
    S.q("hm-sto-p4", "hard", "Match the medium to its technology:\nA. HDD  B. Blu-ray  C. Pen drive  D. LTO tape",
        ["A-magnetic platters, B-optical laser, C-flash chips, D-magnetic tape",
         "A-flash chips, B-magnetic platters, C-optical laser, D-magnetic tape",
         "A-magnetic tape, B-flash chips, C-optical laser, D-magnetic platters",
         "A-magnetic platters, B-optical laser, C-magnetic tape, D-flash chips"],
        "A-magnetic platters, B-optical laser, C-flash chips, D-magnetic tape",
        "HDD spins magnetised platters; Blu-ray is read by a blue-violet laser; the pen drive is flash chips; LTO is archival magnetic tape — one example of each family.",
        "Spin, shine, chips, wind.", 40)
    S.q("hm-sto-p2", "hard", "Consider the statements:\n1. SSDs are more shock-resistant than HDDs.\n2. HDDs store data magnetically.\n3. Flash memory loses its data as soon as power is cut.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are standard. Statement 3 is wrong — **flash is non-volatile**; it keeps data without power (that is the whole point of a pen drive).",
        "Flash remembers; RAM forgets.", 35)
    return S
