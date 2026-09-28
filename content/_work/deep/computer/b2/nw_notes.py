"""Networking deep notes."""

NW_TYPES_TOPOLOGIES = """### Networks by their reach
| Type | Span | Everyday example |
|---|---|---|
| **PAN** (Personal Area Network) | ~10 metres around one person | Bluetooth headset with a phone |
| **LAN** (Local Area Network) | one building or campus | school computer lab, office floor |
| **MAN** (Metropolitan Area Network) | one city | city cable network |
| **WAN** (Wide Area Network) | country or the world | the **Internet is the largest WAN** |

LANs are privately owned and fast; WANs use leased/telecom links over long distances. The span ladder **PAN < LAN < MAN < WAN** answers most identification questions.

### Topologies — the shape of the wiring
A **topology** is how computers are arranged and connected.
| Topology | Layout | Strength | Weakness |
|---|---|---|---|
| **Bus** | all nodes tap into ONE backbone cable with terminators at both ends | cheapest, least cable | backbone break kills the whole network; collisions |
| **Ring** | each node joins exactly two neighbours, forming a circle | orderly token passing | one broken node/link can break the ring |
| **Star** | every node connects to a **central device** (hub/switch) | one cable failure hurts only one node; easy to extend | the central device is the single point of failure |
| **Mesh** | every node connects to **every other** node | most reliable, no traffic jams | most cables, costliest |
| **Tree** (hierarchical) | star networks joined on a bus | scalable for big campuses | root failure splits the tree |

**Star is the shape used in modern offices** — switches sit at the centre. **Mesh is the most fault-tolerant**.

### Mesh arithmetic — the one formula
In a full mesh of **n** computers, every computer connects to the other n-1 computers, so each of the n nodes has n-1 lines; counting every line twice (A-B and B-A) gives:

links = **n x (n-1) / 2**

For n = 4: 4x3/2 = 6 links. For n = 5: 10. For n = 6: 15. This is the classic numeric question of the topic — halve the product, never use n squared.

### Standards that name the wires
- **Ethernet (wired LAN) = IEEE 802.3**; **Wi-Fi (wireless LAN) = IEEE 802.11**; **Bluetooth = IEEE 802.15**.
- Trap: calling Wi-Fi "802.3" — 802.3 is the wired Ethernet standard.

### Quick revision
- PAN (10 m) < LAN (building) < MAN (city) < WAN (country/world); Internet = biggest WAN.
- Bus = one backbone; Ring = circle of neighbours; **Star = central hub/switch**; Mesh = all-to-all.
- **Mesh links = n(n-1)/2** (6 computers = 15 links).
- Star's weakness = central device; Bus's weakness = backbone break.
- Ethernet 802.3, Wi-Fi 802.11, Bluetooth 802.15."""

NW_DEVICES = """### The device ladder — hub to gateway
| Device | Layer | What it does |
|---|---|---|
| **Hub** | Physical (1) | joins many machines; **broadcasts every bit to every port** — no intelligence |
| **Switch** | Data Link (2) | **learns MAC addresses** and sends frames only to the right port |
| **Router** | Network (3) | **joins different networks and chooses routes using IP addresses** |
| **Repeater** | Physical (1) | **regenerates a weak signal** to extend the cable's range |
| **Bridge** | Data Link (2) | joins **two LAN segments**, filtering local traffic |
| **Gateway** | up to Application | a **protocol converter** between different systems ("entry/exit door" of a network) |
| **Modem** | — | **MOdulator-DEModulator**: digital data of the PC to the analog phone line and back |
| **NIC** (Network Interface Card) | 2 | the card that connects one machine to the network; carries its **MAC address** |
| **Access Point** | 2 | lets wireless devices join a wired network (Wi-Fi) |

### The one-line differences exams ask
- **Hub vs Switch**: hub shouts to everyone; a **switch forwards only to the destination port** — faster and safer.
- **Switch vs Router**: a switch moves traffic **inside** one network (by MAC); a **router moves traffic between networks by IP** and picks the best path — your home router joins your LAN to the Internet.
- **Repeater vs Amplifier**: a repeater regenerates the clean digital signal; an amplifier would boost the noise along with it.
- **Gateway vs Router**: a router selects routes; a **gateway translates between different protocol worlds** (e.g. a mail network to a phone network).
- **Modem**: the name is the definition — modulate (digital to analog) + demodulate (analog to digital).

### MAC address — the burnt-in identity
Every NIC carries a **48-bit physical address** (written like 1A:2B:3C:4D:5E:6F) fixed by the maker. The **MAC is physical and permanent**; the **IP is logical and assigned**. Switches read MACs; routers read IPs.

### Reading a device question in the exam
Find the **verb** first: "sends to all ports" = hub; "sends only to the destination" = switch; "connects two different networks / chooses a path" = router; "regenerates a weak signal" = repeater; "converts protocols" = gateway; "digital to analog and back" = modem. Exams rarely name the device — they name its job. And when the layer is asked, remember the ladder: no brain (L1) < MAC reader (L2) < IP reader (L3).

### Quick revision
- Hub = broadcast (L1); **Switch = learns MAC, sends to the right port (L2)**; **Router = routes between networks by IP (L3)**.
- Repeater regenerates signals (L1); Bridge joins two LANs (L2); Gateway = protocol converter.
- **Modem = modulator + demodulator** (digital to analog and back).
- NIC carries the **48-bit MAC address**; MAC permanent, IP assigned."""

NW_OSI = """### Why a reference model exists
Moving data from one machine to another needs many different jobs: signalling, framing, addressing, delivery, dialogue control, translation, and the user's service. The **OSI (Open Systems Interconnection) model** splits these into **7 layers**, so each layer can be designed and replaced independently.

### The 7 layers — bottom to top
| # | Layer | One-line job | Works with |
|---|---|---|---|
| 1 | **Physical** | raw **bits on cables/signals** | cables, hubs, repeaters |
| 2 | **Data Link** | **frames**, MAC addresses, error detection | switches, bridges, NIC |
| 3 | **Network** | **IP addressing and routing** | routers, IP |
| 4 | **Transport** | **end-to-end delivery**, segmentation, ports | TCP, UDP |
| 5 | **Session** | opens, manages, closes **dialogues** | session setup tokens |
| 6 | **Presentation** | **translation, encryption, compression** | formats, SSL/TLS |
| 7 | **Application** | the **user-facing services** | HTTP, FTP, SMTP, browsers |

Mnemonics, top-down: "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing". Bottom-up: "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way".

### How the layers are tested
- **Device-to-layer**: hub/repeater = 1, switch/bridge = 2, **router = 3**.
- **Function-to-layer**: routing = Network (3); framing/MAC = Data Link (2); **encryption and compression = Presentation (6)**; mail/web services = Application (7).
- **Number questions**: 7 layers (OSI) vs 4 layers (TCP/IP). The middle is Transport in both.
- Data flows DOWN the sender's stack (7 to 1), across the wire, and UP the receiver's stack (1 to 7).

### The TCP/IP model — the practical cousin
| TCP/IP layer | OSI layers it swallows |
|---|---|
| **Application** | 5 + 6 + 7 (Session, Presentation, Application) |
| **Transport** | 4 |
| **Internet** | 3 (Network) |
| **Network Access / Link** | 1 + 2 (Physical, Data Link) |

The Internet actually runs on TCP/IP; OSI is the teaching map. "Which model has 4 layers?" — TCP/IP.

### Reading a layer question in the exam
First decide what the question is really asking: a **number** (7 layers, 4 in TCP/IP), an **order** (which sits above which), a **function** (what does this layer do), or a **worker** (which device or protocol lives here). For function questions, test the planted option against its neighbour: routing is NOT Transport (Transport only delivers end to end after Network has found the path), and encryption is NOT Application (Application serves the user; Presentation prepares the data format for it).

### Quick revision
- OSI = **7 layers**: Physical, Data Link, Network, Transport, Session, Presentation, Application.
- Router L3, Switch L2, Hub L1; routing = Network; encryption/compression = Presentation.
- Transport layer = TCP/UDP and ports; Session = dialogues.
- **TCP/IP model = 4 layers** (Network Access, Internet, Transport, Application)."""

NW_IP = """### IPv4 — the 32-bit address
An **IPv4 address** is **32 bits** written as four numbers 0-255 separated by dots: 192.168.1.1. Each of the four blocks is an **octet** (8 bits). The leading numbers decide the **class**:

| Class | First octet | Default mask | Use |
|---|---|---|---|
| **A** | 1 - 126 | 255.0.0.0 | giant networks |
| **B** | 128 - 191 | 255.255.0.0 | medium networks |
| **C** | 192 - 223 | 255.255.255.0 | small networks (most common) |
| **D** | 224 - 239 | — | **multicasting** |
| **E** | 240 - 255 | — | experimental/research |

Class ruler: **1(A), 128(B), 192(C), 224(D), 240(E)**. Note 127 is NOT a class-A start — see below.

### Special addresses
- **127.0.0.1 = loopback / localhost** — a machine talking to itself; the whole 127 block is reserved.
- **Private (non-routable) ranges**: **10.0.0.0 - 10.255.255.255**, **172.16.0.0 - 172.31.255.255**, **192.168.0.0 - 192.168.255.255**. Home routers hand out 192.168.x.x — that is why 192.168.1.1 is a private address, never a public one.
- Hosts per network: Class C gives 256 addresses minus network & broadcast = **254 usable hosts**.

### IPv6 — the 128-bit successor
IPv4 offers about 4.3 billion addresses — too few for a connected planet. **IPv6 uses 128 bits**, written as **eight groups of hexadecimal digits separated by colons** (e.g. 2001:0db8:85a3:0000:0000:8a2e:0370:7334, which can be shortened with :: ). Benefits: a huge address space, built-in auto-configuration, better security support.

### MAC vs IP — the twins that get swapped
| | MAC address | IP address |
|---|---|---|
| Type | **physical**, burnt into the NIC | **logical**, assigned by network/DHCP |
| Size | **48 bits** | IPv4 **32 bits** / IPv6 128 bits |
| Changes | never (factory-fixed) | changes with the network |
| Used by | switches (L2) | routers (L3) |

### Reading an address question in the exam
For a class question, cover everything after the first dot — the answer lives only in the **first octet**. Anchor the ruler at 1, 128, 192, 224, 240 and drop the given number between the anchors. For "which is private" questions, check the three ranges like passwords: does it start with 10, or 172 with a second number 16-31, or 192.168? A 172 address with second number 32 or more is public — that is the planted trap. And loopback 127.x is its own reserved world, never listed as "Class A hosts".

### Quick revision
- IPv4 = **32 bits**, four octets 0-255; IPv6 = **128 bits**, hexadecimal, colon-separated.
- Classes by first octet: A 1-126, B 128-191, C 192-223, D 224-239, E 240-255.
- **127.0.0.1 = loopback**; private ranges 10.x, 172.16-31.x, 192.168.x.
- Class C network = **254 usable hosts**; MAC = 48-bit physical, IP = logical."""

NW_PROTOCOLS = """### Ports — numbered doors on a machine
While the IP address finds the computer, the **port number** finds the service (door) on it. The classic exam set:

| Protocol | Port | Job |
|---|---|---|
| **HTTP** | **80** | web pages (plain) |
| **HTTPS** | **443** | web pages **encrypted** (TLS/SSL) |
| **FTP** | **21** (control; 20 = data) | file transfer |
| **SSH** | **22** | secure remote login |
| **Telnet** | **23** | remote login (NOT encrypted) |
| **SMTP** | **25** | sending e-mail |
| **DNS** | **53** | name to IP resolution |
| **POP3** | **110** | receiving e-mail (download) |
| **IMAP** | **143** | receiving e-mail (sync) |

Anchor pairs: 80/443 web, 21/23/25 climbing odd numbers (FTP, Telnet, SMTP), 53 DNS, 110/143 mail-in.

### TCP vs UDP — the two delivery styles
| | **TCP** (Transmission Control Protocol) | **UDP** (User Datagram Protocol) |
|---|---|---|
| Connection | **connection-oriented** (handshake first) | **connectionless** (just send) |
| Reliability | guaranteed, ordered, error-checked | **no guarantee** — fast but unsafe |
| Speed | slower | faster |
| Used by | **web (HTTP/HTTPS), e-mail (SMTP), file transfer (FTP)** | **live streaming, gaming, VoIP, DNS queries, DHCP** |

Memory hook: **TCP = Tracked, Careful, Precise; UDP = Untracked, Dashes**. Live cricket streaming chooses UDP — one lost frame is better than a paused match.

### The protocols behind one web visit
1. **DNS** (UDP 53) turns the name into an IP.
2. **TCP** opens the connection.
3. **HTTPS** (TCP 443) requests and delivers the page encrypted.
For e-mail: SMTP sends, POP3/IMAP receive — over TCP.

### Full forms worth memorising
HTTP HyperText Transfer Protocol; HTTPS secure HTTP over TLS/SSL; FTP File Transfer Protocol; SMTP Simple Mail Transfer Protocol; POP Post Office Protocol; IMAP Internet Message Access Protocol; TCP Transmission Control Protocol; UDP User Datagram Protocol; DNS Domain Name System; DHCP Dynamic Host Configuration Protocol; SSH Secure Shell.

### Reading a protocol question in the exam
Ask first: is the question about a **direction** (send mail = SMTP, receive = POP3/IMAP), a **number** (port), a **style** (reliable or fast), or a **full form**? For port questions, if you cannot recall the exact number, eliminate by neighbourhood — 21-22-23 are the file/remote trio, 25 is the mail sender, 80/443 the web pair, 110/143 the mail-in pair. For TCP-or-UDP questions, ask what a lost packet would cost: a corrupted file (use TCP) or one blurred frame (UDP is fine).

### Quick revision
- HTTP 80, **HTTPS 443**, FTP 21, SSH 22, Telnet 23, SMTP 25, DNS 53, POP3 110, IMAP 143.
- **TCP = reliable, connection-oriented** (web, mail, FTP); **UDP = fast, connectionless** (streaming, games, VoIP).
- Telnet is plaintext; **SSH (22) is its encrypted replacement**.
- HTTPS = HTTP + TLS/SSL encryption."""
