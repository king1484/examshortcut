"""Networking pattern builders."""
from _lib import Sub


def build_types_topologies():
    S = Sub("nw-types-topologies")
    S.notes = __import__("nw_notes").NW_TYPES_TOPOLOGIES
    S.pattern("nw-t1", "Network type by span", "very common",
        "A situation is described (school lab, city cable, worldwide web, one person's Bluetooth) and PAN/LAN/MAN/WAN is asked — or 'the Internet is the largest ___'.",
        None,
        "1. Line up the ladder: PAN (~10 m, one person) < LAN (building/campus) < MAN (city) < WAN (country/world).\n2. Match the situation's span, not its technology.\n3. Standard facts: Internet = largest WAN; school lab = LAN; Bluetooth headset = PAN.",
        "A computer lab of one school connected by a switch forms a —",
        "**LAN (Local Area Network)** — a single-building privately owned network.")
    S.pattern("nw-t2", "Topology identification by description", "very common",
        "The layout is described (every node to a central device; every node to every other; a single backbone; a circle) and the topology is asked.",
        None,
        "1. Central device with all nodes hanging off = **Star**.\n2. Every node linked to every other = **Mesh**.\n3. One shared backbone cable with terminators = **Bus**; closed circle of neighbours = **Ring**; stars joined on a backbone = **Tree**.",
        "In which topology is every computer connected to a central hub or switch?",
        "**Star topology** — one cable break isolates only that node, but the central device is the single point of failure.")
    S.pattern("nw-t3", "Mesh link count (numeric)", "common",
        "'How many links are needed for a full mesh of n computers?' — pure arithmetic on n(n-1)/2.",
        None,
        "1. Use links = n x (n-1) / 2 — every node talks to the other n-1, and each line would be counted twice.\n2. Never use n squared; halve the product.\n3. Check: n = 4 gives 6, n = 5 gives 10, n = 6 gives 15.",
        "How many cable links are needed for a full mesh of 6 computers?",
        "6 x 5 / 2 = **15 links**.")
    S.pattern("nw-t4", "Topology strengths and failure points", "common",
        "A statement about which topology is cheapest, most reliable, has a single point of failure, or what happens when a cable breaks.",
        None,
        "1. Star: one cable break = one node only; **central hub/switch failure = whole network down**.\n2. Bus: backbone break = total failure; cheapest.\n3. Mesh: most reliable, most cable (costliest).\n4. Ring: one broken node/link can stop the ring (token passing).",
        "In a star topology, failure of the central hub results in —",
        "**The whole network stops communicating** — every node depends on the hub; the individual cables are irrelevant.")
    S.pattern("nw-t5", "IEEE standards and LAN jargon", "occasional",
        "'Wi-Fi is IEEE ___' or 'Ethernet works on which standard' — matching 802.x numbers to technologies.",
        None,
        "1. **Ethernet (wired) = IEEE 802.3**; **Wi-Fi (wireless) = IEEE 802.11**; **Bluetooth = 802.15**.\n2. The recurring trap: pairing Wi-Fi with 802.3.\n3. LAN = Ethernet/Wi-Fi family; the Internet = a WAN built of many networks.",
        "Wi-Fi networks are standardised under IEEE —",
        "**802.11** — 802.3 is wired Ethernet, 802.15 is Bluetooth.")
    return S


def build_devices():
    S = Sub("nw-devices")
    S.notes = __import__("nw_notes").NW_DEVICES
    S.pattern("nw-d1", "Hub vs switch vs router", "very common",
        "A behaviour is described (sends to all ports, forwards to the right port, connects two networks and picks a path) and the device is asked.",
        None,
        "1. **Hub**: broadcasts every bit to every port — no intelligence (Layer 1).\n2. **Switch**: learns MAC addresses, forwards frames to the correct port only (Layer 2).\n3. **Router**: connects DIFFERENT networks and routes packets by IP address (Layer 3).\n4. 'Which device is more intelligent than a hub?' = switch; 'which joins two networks?' = router.",
        "Which device forwards data only to the intended port instead of all ports?",
        "**A switch** — it reads MAC addresses; a hub would broadcast to every port.")
    S.pattern("nw-d2", "Modem, repeater, bridge, gateway functions", "common",
        "'A modem is used for', 'device that regenerates a weak signal', 'device that converts between protocols' — function-to-device matching.",
        None,
        "1. **Modem = MOdulator-DEModulator**: computer's digital signal to the analog line and back.\n2. **Repeater**: regenerates weak signals to extend range (Layer 1).\n3. **Bridge**: joins two LAN segments (Layer 2).\n4. **Gateway**: translates between different protocol systems — the entry/exit door.",
        "The device that regenerates and retransmits a weakening signal is a —",
        "**Repeater** — it restores the clean digital signal so the cable can run farther.")
    S.pattern("nw-d3", "Device-to-layer matching", "common",
        "'A router works on which OSI layer?', 'a hub operates at layer ___' — device and OSI layer pairs.",
        None,
        "1. Hub, repeater = **Layer 1 (Physical)**.\n2. Switch, bridge, NIC = **Layer 2 (Data Link)**.\n3. **Router = Layer 3 (Network)** — it reads IP addresses.\n4. Gateway spans up to the Application layer.",
        "A router operates on which layer of the OSI model?",
        "**Layer 3 (Network)** — routing decisions use IP addresses; switching by MAC happens on Layer 2.")
    S.pattern("nw-d4", "NIC and MAC-address facts", "common",
        "'A MAC address is ___ bits', 'where is the MAC address stored', 'MAC vs IP difference' questions.",
        None,
        "1. MAC = **48-bit physical address** burnt into the NIC by the maker (like 1A:2B:3C:4D:5E:6F).\n2. MAC is permanent; IP is logical and changes with the network.\n3. Switches work on MAC (Layer 2); routers on IP (Layer 3).",
        "The physical address burnt into a network interface card is the —",
        "**MAC address** — 48 bits, factory-fixed; the IP address is only a logical label assigned by software.")
    return S


def build_osi():
    S = Sub("nw-osi")
    S.notes = __import__("nw_notes").NW_OSI
    S.pattern("nw-o1", "OSI layer count and order", "very common",
        "'How many layers does the OSI model have?', correct ordering questions, or the layer that sits directly above/below another.",
        None,
        "1. OSI = **7 layers**: Physical, Data Link, Network, Transport, Session, Presentation, Application (bottom to top).\n2. Mnemonic top-down: All People Seem To Need Data Processing.\n3. Transport is the middle (4th); Application is 7th, Physical 1st.",
        "How many layers are there in the OSI reference model?",
        "**7** — the TCP/IP model has only 4; the count mix-up is the standard trap.")
    S.pattern("nw-o2", "Function-to-layer matching", "very common",
        "'Routing is done at which layer?', 'encryption/compression is a ___ layer function', 'framing and MAC addressing belong to ___'.",
        None,
        "1. Bits/cables = Physical (1); frames, MAC = Data Link (2); **addressing and routing = Network (3)**; end-to-end delivery, ports = Transport (4); dialogues = Session (5); **translation, encryption, compression = Presentation (6)**; user services = Application (7).\n2. The planted traps: encryption at Application, routing at Transport.\n3. Ports and TCP/UDP live in Transport, never Network.",
        "Encryption and data compression are functions of which OSI layer?",
        "**Presentation (Layer 6)** — it prepares data formats before the Application's services use them.")
    S.pattern("nw-o3", "Device/protocol-to-layer matching", "common",
        "'A switch works at which layer', 'HTTP is a ___ layer protocol', 'TCP sits in which layer'.",
        None,
        "1. Hub/repeater L1; switch/bridge L2; **router L3**; TCP/UDP L4.\n2. HTTP, FTP, SMTP = Application (7); IP = Network (3).\n3. Match the job before the name: a router routes (3), a switch switches frames (2).",
        "TCP and UDP work at which layer of the OSI model?",
        "**Transport (Layer 4)** — end-to-end delivery, segmentation and port numbers.")
    S.pattern("nw-o4", "TCP/IP model vs OSI", "common",
        "'The TCP/IP model has how many layers', 'which OSI layers merge into TCP/IP Application', or mapping the four TCP/IP layers.",
        None,
        "1. TCP/IP = **4 layers**: Network Access (1+2), Internet (3), Transport (4), Application (5+6+7).\n2. OSI's top three merge into TCP/IP's Application.\n3. The Internet runs on TCP/IP; OSI is the reference map.",
        "How many layers does the TCP/IP model have?",
        "**4** — Network Access, Internet, Transport and Application (the last swallowing OSI layers 5-7).")
    return S


def build_ip():
    S = Sub("nw-ip")
    S.notes = __import__("nw_notes").NW_IP
    S.pattern("nw-p1", "IP class identification", "very common",
        "An address is given (10.0.0.5, 130.10.5.2, 196.1.2.3, 225.5.4.1) and its class is asked — or the first-octet range of a class is asked.",
        None,
        "1. Read the FIRST octet only: 1-126 = A, 128-191 = B, 192-223 = C, 224-239 = D (multicast), 240-255 = E.\n2. 127 is loopback, not Class A usage.\n3. Anchor the ruler: 1, 128, 192, 224, 240.",
        "The IP address 196.20.5.1 belongs to which class?",
        "**Class C** — the first octet 196 lies between 192 and 223.")
    S.pattern("nw-p2", "Private ranges and loopback", "very common",
        "'Which is a private IP address', 'what is 127.0.0.1', 'which address is reserved for testing/localhost'.",
        None,
        "1. Private ranges: **10.x.x.x, 172.16-31.x.x, 192.168.x.x** — home routers use 192.168.x.x.\n2. **127.0.0.1 = loopback/localhost** — the machine testing itself.\n3. 169.254.x.x = auto-configuration failure (APIPA) — optional extra.",
        "The address 127.0.0.1 is used for —",
        "**Loopback testing (localhost)** — the computer communicates with itself without touching the network.")
    S.pattern("nw-p3", "IPv4 vs IPv6 facts", "common",
        "'IPv4 has how many bits', 'IPv6 addresses are written in ___', 'how many groups in an IPv6 address', or why IPv6 was needed.",
        None,
        "1. IPv4 = **32 bits**, four dotted decimal octets (0-255), about 4.3 billion addresses.\n2. IPv6 = **128 bits**, **8 groups of hexadecimal** digits separated by colons.\n3. The need: IPv4 addresses ran out — 4.3 billion is less than the connected world.",
        "An IPv6 address is how many bits long?",
        "**128 bits** — eight hexadecimal groups, e.g. 2001:0db8:85a3::8a2e:0370:7334.")
    S.pattern("nw-p4", "MAC vs IP and usable-host counts", "common",
        "'Difference between MAC and IP address', 'how many hosts can a Class C network have', 'which address changes when you shift networks'.",
        None,
        "1. MAC = 48-bit, physical, burnt in, permanent; IP = logical, assigned, changes with network.\n2. Class C hosts: 256 addresses minus network and broadcast = **254 usable**.\n3. Class B: 65,534 usable; Class A: 1,67,77,214 usable.",
        "How many usable host addresses does a Class C network provide?",
        "**254** — 256 total minus the network address and the broadcast address.")
    return S


def build_protocols():
    S = Sub("nw-protocols")
    S.notes = __import__("nw_notes").NW_PROTOCOLS
    S.pattern("nw-r1", "Port-number matching", "very common",
        "'HTTPS works on which port', 'port of SMTP/FTP/DNS/POP3', or a matched pair with one number shifted.",
        None,
        "1. Anchors: **HTTP 80, HTTPS 443, FTP 21, SSH 22, Telnet 23, SMTP 25, DNS 53, POP3 110, IMAP 143**.\n2. The classic trap: 443 for plain HTTP or 80 for HTTPS.\n3. Remember 21-22-23 climbing (FTP, SSH, Telnet) and 25 as the mail sender's door.",
        "HTTPS uses which port number by default?",
        "**443** — plain HTTP uses 80; the S (secure) doubles the number in exam memory: 80 becomes 443.")
    S.pattern("nw-r2", "TCP vs UDP selection", "very common",
        "'Which protocol is used for live streaming / file transfer', 'which is connection-oriented', reliability-vs-speed statements.",
        None,
        "1. **TCP**: connection-oriented, reliable, ordered — web, e-mail, FTP.\n2. **UDP**: connectionless, fast, no delivery guarantee — **live streaming, gaming, VoIP, DNS queries**.\n3. The classic exam answer: live video streaming = UDP; downloading a file = TCP.",
        "Which transport protocol suits a live cricket stream?",
        "**UDP** — speed matters more than perfect delivery; TCP's retransmissions would only pause the match.")
    S.pattern("nw-r3", "Protocol purpose identification", "common",
        "'Which protocol transfers files', 'which protocol sends e-mail', 'which service resolves names' — purpose matching across the famous protocols.",
        None,
        "1. File transfer = **FTP**; send mail = **SMTP**; receive mail = POP3/IMAP; web pages = **HTTP/HTTPS**; names = **DNS**; remote login = Telnet (plain) / SSH (secure).\n2. FTP has two ports: 21 control, 20 data.\n3. DHCP assigns IP addresses automatically.",
        "Which protocol is used to transfer files between computers?",
        "**FTP (File Transfer Protocol)** — control on port 21, data on port 20.")
    S.pattern("nw-r4", "Protocol full forms and security", "common",
        "'Full form of FTP/TCP/UDP/DHCP', 'which remote-login protocol is secure', or Telnet-vs-SSH statements.",
        None,
        "1. FTP = File Transfer Protocol; TCP = Transmission Control Protocol; UDP = User Datagram Protocol; DHCP = Dynamic Host Configuration Protocol; SSH = Secure Shell.\n2. **Telnet (23) sends everything in plaintext; SSH (22) is the encrypted replacement**.\n3. HTTPS = HTTP over TLS/SSL.",
        "Which protocol provides an ENCRYPTED remote login?",
        "**SSH (Secure Shell), port 22** — Telnet on port 23 sends passwords as plain text.")
    return S
