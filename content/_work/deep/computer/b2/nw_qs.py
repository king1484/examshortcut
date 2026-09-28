"""Networking practice questions. Numeric answers computed and asserted here."""


def mesh_links(n):
    return n * (n - 1) // 2


def add_types_topologies(S):
    assert mesh_links(4) == 6 and mesh_links(5) == 10 and mesh_links(6) == 15
    S.q("nw-t1", "easy", "A network limited to a single building or campus is a —",
        ["LAN", "WAN", "MAN", "PAN"], "LAN",
        "**LAN = Local Area Network** — one building or campus, privately owned, fast.",
        "Local = one building.", 20)
    S.q("nw-t1", "medium", "The Internet is the largest example of a —",
        ["WAN", "LAN", "PAN", "Intranet"], "WAN",
        "**WAN = Wide Area Network** spanning countries and continents — the Internet is the biggest WAN.",
        "World-wide = WAN.", 20)
    S.q("nw-t1", "medium", "A Bluetooth connection between a phone and a wireless earphone is a —",
        ["PAN", "LAN", "MAN", "WAN"], "PAN",
        "**PAN = Personal Area Network** — about 10 metres around one person.",
        "Personal space = PAN.", 25)
    S.q("nw-t1", "hard", "Arrange by increasing span: 1. MAN 2. PAN 3. WAN 4. LAN",
        ["2, 4, 1, 3", "4, 2, 1, 3", "2, 1, 4, 3", "4, 1, 2, 3"],
        "2, 4, 1, 3",
        "PAN (person) < LAN (building) < MAN (city) < WAN (world).",
        "Person, building, city, world.", 35)
    S.q("nw-t2", "easy", "Which topology connects every node to a central hub or switch?",
        ["Star", "Bus", "Ring", "Mesh"], "Star",
        "**Star topology** — all nodes hang off one central device.",
        "Central device = star.", 20)
    S.q("nw-t2", "medium", "In which topology does every node have a dedicated link to EVERY other node?",
        ["Mesh", "Star", "Bus", "Ring"], "Mesh",
        "**Mesh** = all-to-all links — maximum reliability, maximum cable.",
        "Everyone to everyone.", 25)
    S.q("nw-t2", "medium", "A network where all computers share ONE common backbone cable uses —",
        ["Bus topology", "Star topology", "Mesh topology", "Tree topology"], "Bus topology",
        "**Bus topology** taps every node into one backbone with terminators at both ends.",
        "One road, many stops.", 25)
    S.q("nw-t2", "hard", "Which topology joins several star networks onto a single backbone?",
        ["Tree", "Ring", "Mesh", "Bus"], "Tree",
        "**Tree (hierarchical)** = star networks connected by a bus backbone — scalable for large campuses.",
        "Tree = stars on a branch line.", 35)
    n6 = mesh_links(6)
    assert n6 == 15
    S.q("nw-t3", "medium", "How many links are required for a full mesh of 6 computers?",
        ["15", "30", "12", "36"], "15",
        "n(n-1)/2 = 6x5/2 = **15 links**. 30 forgets the halving; 36 is n squared.",
        "Half of n x (n-1).", 30)
    n8 = mesh_links(8)
    assert n8 == 28
    S.q("nw-t3", "medium", "A full mesh of 8 computers needs how many links?",
        ["28", "64", "56", "16"], "28",
        "8x7/2 = **28**. 56 skips the halving; 64 is 8 squared.",
        "Halve n x (n-1).", 30)
    n10 = mesh_links(10)
    assert n10 == 45
    S.q("nw-t3", "hard", "Adding a 5th computer to a full mesh of 4 requires how many NEW links?",
        ["4", "10", "6", "5"], "4",
        "Mesh of 4 has 6 links, of 5 has 10 — the new computer connects to each existing node: **4 new links**.",
        "New node joins every old node.", 40)
    S.q("nw-t4", "medium", "Which topology has a SINGLE POINT of total failure at its central device?",
        ["Star", "Mesh", "Fully distributed ring", "Partial mesh"], "Star",
        "If the **central hub/switch dies in a star, the whole network dies** — its one weakness.",
        "Everything hangs on the centre.", 25)
    S.q("nw-t4", "medium", "Which topology is the MOST reliable but also the most expensive to cable?",
        ["Mesh", "Bus", "Star", "Ring"], "Mesh",
        "**Mesh** — every node has many alternate paths, so no single cut disconnects anyone; the price is n(n-1)/2 cables.",
        "Reliability costs cables.", 25)
    S.q("nw-t4", "hard", "In a bus topology, what happens if the main backbone cable is cut?",
        ["The entire network stops communicating", "Only the nearest node fails",
         "Traffic reverses direction", "Nothing changes"],
        "The entire network stops communicating",
        "The backbone IS the bus — a cut splits it and no node can reach another (that is why terminators and cable quality matter).",
        "One road cut = no travel.", 35)
    S.q("nw-t5", "medium", "Wired Ethernet is standardised as IEEE —",
        ["802.3", "802.11", "802.15", "802.1"], "802.3",
        "**802.3 = Ethernet (wired LAN)**; 802.11 = Wi-Fi; 802.15 = Bluetooth.",
        "3 = wire.", 25)
    S.q("nw-t5", "hard", "Which pair is wrongly matched?",
        ["Wi-Fi — IEEE 802.3", "Bluetooth — IEEE 802.15", "Ethernet — IEEE 802.3", "Wi-Fi — IEEE 802.11"],
        "Wi-Fi — IEEE 802.3",
        "Wi-Fi is **802.11**; 802.3 is the wired Ethernet standard — the planted swap.",
        "Wireless is not 802.3.", 35)


def add_devices(S):
    S.q("nw-d1", "easy", "Which network device broadcasts incoming data to ALL its ports?",
        ["Hub", "Switch", "Router", "Gateway"], "Hub",
        "A **hub shouts to everyone**; it cannot read addresses (Layer 1 only).",
        "Hub = loudspeaker.", 20)
    S.q("nw-d1", "medium", "Which device reads MAC addresses and sends frames only to the correct port?",
        ["Switch", "Hub", "Repeater", "Modem"], "Switch",
        "**Switch (Layer 2)** learns which MAC lives on which port — no wasted broadcasting.",
        "Switch = smart delivery.", 25)
    S.q("nw-d1", "medium", "Which device connects two DIFFERENT networks and selects the best path for packets?",
        ["Router", "Hub", "Switch", "Repeater"], "Router",
        "**Router (Layer 3)** works on IP addresses and chooses routes between networks.",
        "Router = route chooser.", 25)
    S.q("nw-d1", "hard", "Your home Wi-Fi router joins your family's devices to the Internet. In networking terms it is acting as a —",
        ["Router connecting a LAN to a WAN", "Repeater extending a cable", "Hub broadcasting frames",
         "Modem modulating analog signals"],
        "Router connecting a LAN to a WAN",
        "The home box routes between your **LAN** and the ISP's network (**WAN/Internet**), besides serving Wi-Fi.",
        "Home = LAN to WAN door.", 35)
    S.q("nw-d2", "easy", "A modem is a short form of —",
        ["Modulator-Demodulator", "Mode Manager", "Modern Terminal", "Module Demander"],
        "Modulator-Demodulator",
        "**MOdulator-DEModulator** — converts the computer's digital signals to the phone line's analog form and back.",
        "MO + DEMO = modem.", 20)
    S.q("nw-d2", "medium", "Which device regenerates a weak signal to extend the length of a network run?",
        ["Repeater", "Router", "Gateway", "Bridge"], "Repeater",
        "**Repeater (Layer 1)** rebuilds the clean signal so it can travel farther.",
        "Repeat = say it again, fresh.", 25)
    S.q("nw-d2", "medium", "A gateway differs from a router mainly because it —",
        ["Converts between different protocol systems", "Works only on copper cables",
         "Cannot connect to the Internet", "Is always a wireless device"],
        "Converts between different protocol systems",
        "A **gateway is a protocol converter** — the entry/exit door between different worlds; a router only selects routes.",
        "Gateway = translator door.", 30)
    S.q("nw-d2", "hard", "Which device joins TWO LAN segments and filters traffic between them at Layer 2?",
        ["Bridge", "Repeater", "Modem", "Hub"], "Bridge",
        "**Bridge (Layer 2)** connects two segments and holds local traffic back — an ancestor of the switch.",
        "Bridge between two banks.", 30)
    S.q("nw-d3", "easy", "A hub operates at which OSI layer?",
        ["Layer 1 (Physical)", "Layer 2 (Data Link)", "Layer 3 (Network)", "Layer 4 (Transport)"],
        "Layer 1 (Physical)",
        "A hub only repeats electrical signals — **Layer 1**, no addressing at all.",
        "Dumbest device = lowest layer.", 20)
    S.q("nw-d3", "medium", "A switch operates at which OSI layer?",
        ["Layer 2 (Data Link)", "Layer 1 (Physical)", "Layer 3 (Network)", "Layer 7 (Application)"],
        "Layer 2 (Data Link)",
        "**Layer 2** — switches read MAC addresses inside frames.",
        "MAC = Layer 2.", 25)
    S.q("nw-d3", "hard", "Which sequence of devices is in ASCENDING order of intelligence?",
        ["Hub, Switch, Router", "Router, Switch, Hub", "Switch, Hub, Router", "Hub, Router, Switch"],
        "Hub, Switch, Router",
        "Hub (no brain, L1) < Switch (MAC, L2) < Router (IP routing, L3).",
        "Climb the layers.", 35)
    S.q("nw-d4", "medium", "A MAC address is a —",
        ["48-bit physical address fixed by the manufacturer", "32-bit logical address assigned by DHCP",
         "128-bit hexadecimal address", "16-bit port number"],
        "48-bit physical address fixed by the manufacturer",
        "**MAC = 48 bits, burnt into the NIC**; 32-bit logical describes an IPv4 address.",
        "MAC = maker's mark.", 25)
    S.q("nw-d4", "medium", "Which address CHANGES when a laptop moves from your home network to office Wi-Fi?",
        ["IP address", "MAC address", "NIC serial number", "None of these"],
        "IP address",
        "The **IP is logical and network-dependent**; the MAC stays burnt into the card forever.",
        "IP follows the network.", 25)


def add_osi(S):
    S.q("nw-o1", "easy", "The OSI reference model has how many layers?",
        ["7", "4", "5", "6"], "7",
        "**OSI = 7 layers**; the TCP/IP model has 4.",
        "Seven floors in OSI.", 20)
    S.q("nw-o1", "medium", "Which is the correct order of OSI layers from BOTTOM to TOP?",
        ["Physical, Data Link, Network, Transport, Session, Presentation, Application",
         "Application, Presentation, Session, Transport, Network, Data Link, Physical",
         "Physical, Network, Data Link, Transport, Session, Presentation, Application",
         "Data Link, Physical, Transport, Network, Session, Presentation, Application"],
        "Physical, Data Link, Network, Transport, Session, Presentation, Application",
        "Bottom-up: **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way.",
        "Please Do Not Throw Sausage Pizza Away.", 30)
    S.q("nw-o1", "medium", "Which OSI layer sits DIRECTLY above the Transport layer?",
        ["Session", "Presentation", "Application", "Network"], "Session",
        "Order above Transport: **Session (5), Presentation (6), Application (7)**.",
        "Session is 5.", 25)
    S.q("nw-o2", "easy", "Routing of packets is the job of which OSI layer?",
        ["Network", "Data Link", "Transport", "Session"], "Network",
        "**Network (Layer 3)** handles IP addressing and routing.",
        "Routing = Layer 3.", 20)
    S.q("nw-o2", "medium", "Framing and MAC addressing are functions of the —",
        ["Data Link layer", "Network layer", "Physical layer", "Application layer"],
        "Data Link layer",
        "**Data Link (Layer 2)** wraps bits into frames and uses MAC addresses; switches live here.",
        "Frames and MAC = 2.", 25)
    S.q("nw-o2", "medium", "Encryption and compression of data are handled by the —",
        ["Presentation layer", "Application layer", "Session layer", "Network layer"],
        "Presentation layer",
        "**Presentation (Layer 6)** = translation, encryption, compression — the format preparer.",
        "Presentation dresses the data.", 25)
    S.q("nw-o2", "hard", "Which statement about the Transport layer is TRUE?",
        ["It provides end-to-end delivery using ports (TCP/UDP)",
         "It routes packets between networks",
         "It encrypts data before sending",
         "It generates electrical signals"],
        "It provides end-to-end delivery using ports (TCP/UDP)",
        "Transport (4) = segmentation, ports, TCP/UDP. Routing is Layer 3, encryption Layer 6, signals Layer 1.",
        "Ports and TCP live on 4.", 35)
    S.q("nw-o3", "easy", "At which OSI layer does a ROUTER work?",
        ["Layer 3 (Network)", "Layer 1 (Physical)", "Layer 2 (Data Link)", "Layer 5 (Session)"],
        "Layer 3 (Network)",
        "Routers read IP addresses and route — **Layer 3**.",
        "Router = 3.", 20)
    S.q("nw-o3", "medium", "HTTP, FTP and SMTP belong to which OSI layer?",
        ["Application", "Transport", "Network", "Session"], "Application",
        "User-facing services sit on **Layer 7 (Application)**.",
        "Mail and web on top.", 25)
    S.q("nw-o3", "medium", "IP as a protocol operates at the —",
        ["Network layer", "Transport layer", "Data Link layer", "Session layer"],
        "Network layer",
        "**IP = Internet Protocol, Layer 3** — addressing and routing; TCP/UDP sit above it on Layer 4.",
        "IP = Layer 3.", 25)
    S.q("nw-o4", "easy", "The TCP/IP model has how many layers?",
        ["4", "7", "5", "6"], "4",
        "**TCP/IP = 4 layers**: Network Access, Internet, Transport, Application.",
        "Four in practice.", 20)
    S.q("nw-o4", "medium", "Which OSI layers are merged into the Application layer of the TCP/IP model?",
        ["Session, Presentation, Application (5-7)", "Physical and Data Link (1-2)",
         "Transport and Network (3-4)", "None"],
        "Session, Presentation, Application (5-7)",
        "TCP/IP's **Application swallows OSI 5+6+7**; its Network Access layer takes 1+2.",
        "Top three become one.", 30)


def add_ip(S):
    hosts_c = 2 ** 8 - 2
    assert hosts_c == 254
    S.q("nw-p1", "easy", "The IP address 130.10.5.2 belongs to which class?",
        ["Class B", "Class A", "Class C", "Class D"], "Class B",
        "First octet 130 lies in **128-191 = Class B**.",
        "128-191 = B.", 25)
    S.q("nw-p1", "medium", "Which class does the address 196.20.5.1 belong to?",
        ["Class C", "Class B", "Class A", "Class E"], "Class C",
        "First octet 196 is in **192-223 = Class C** — the small-network class.",
        "192-223 = C.", 25)
    S.q("nw-p1", "medium", "Class D IP addresses are used for —",
        ["Multicasting", "Experimental research", "Small office networks", "Loopback testing"],
        "Multicasting",
        "**Class D (224-239) = multicast groups**; Class E (240-255) is experimental.",
        "D distributes to many.", 25)
    S.q("nw-p1", "hard", "The first octet of a Class A address runs from —",
        ["1 to 126", "1 to 127", "128 to 191", "192 to 223"], "1 to 126",
        "Class A = **1-126**; the 127 block is reserved for loopback, not ordinary Class A use.",
        "Stop at 126; 127 loops.", 30)
    S.q("nw-p2", "easy", "The address 127.0.0.1 refers to —",
        ["The local machine itself (loopback)", "A Google server", "The network's router", "A Class B broadcast"],
        "The local machine itself (loopback)",
        "**127.0.0.1 = localhost** — a machine talking to itself for testing.",
        "Loopback = look at yourself.", 20)
    S.q("nw-p2", "medium", "Which of these is a PRIVATE IP address?",
        ["192.168.1.1", "8.8.8.8", "172.32.10.1", "203.0.113.5"], "192.168.1.1",
        "Private ranges: **10.x.x.x, 172.16-31.x.x, 192.168.x.x**. Note 172.32 is outside 16-31, hence public.",
        "Home routers = 192.168.", 30)
    S.q("nw-p2", "medium", "The typical default address typed to open a home router's settings page is —",
        ["192.168.1.1", "127.0.0.1", "10.0.0.255", "169.254.9.9"], "192.168.1.1",
        "Home routers commonly sit at **192.168.1.1** — a private Class C address.",
        "The router's home door.", 25)
    bits6 = 128
    assert bits6 == 128 and 32 * 2 == 64
    S.q("nw-p3", "easy", "An IPv4 address is how many bits long?",
        ["32", "64", "128", "16"], "32",
        "**IPv4 = 32 bits** — four octets of 8 bits each.",
        "4 octets x 8 bits.", 20)
    S.q("nw-p3", "medium", "An IPv6 address is written as —",
        ["Eight hexadecimal groups separated by colons", "Four decimal numbers separated by dots",
         "Six binary groups separated by dashes", "Twelve octal numbers"],
        "Eight hexadecimal groups separated by colons",
        "**IPv6 = 128 bits in 8 hex groups with colons**, e.g. 2001:0db8::7334; IPv4 is dotted decimal.",
        "Colons and hex = IPv6.", 25)
    S.q("nw-p3", "medium", "IPv6 was developed mainly because —",
        ["IPv4 addresses were running out", "IPv4 was too secure", "IPv4 had no ports",
         "IPv4 cables were slow"],
        "IPv4 addresses were running out",
        "32 bits give about **4.3 billion addresses** — too few for the connected world; 128 bits give a practically endless supply.",
        "More devices than addresses.", 25)
    S.q("nw-p4", "medium", "Which statement about MAC and IP addresses is TRUE?",
        ["MAC is physical and fixed; IP is logical and assignable",
         "MAC is logical; IP is burnt into the NIC",
         "Both are burnt into the NIC",
         "Both change with every network"],
        "MAC is physical and fixed; IP is logical and assignable",
        "**MAC = 48-bit hardware identity; IP = software-assigned logical address** that changes with the network.",
        "MAC permanent, IP portable.", 30)
    S.q("nw-p4", "medium", "A Class C network provides how many USABLE host addresses?",
        ["254", "256", "255", "65,534"], "254",
        "256 total minus the **network address** and the **broadcast address** = **254 usable**.",
        "256 minus two reserved.", 30)
    S.q("nw-p4", "hard", "A device address reads 00:1A:2B:3C:4D:5E with colons and hexadecimal pairs. This is a —",
        ["MAC address", "IPv4 address", "IPv6 address", "Port number"],
        "MAC address",
        "Six hexadecimal pairs = **48-bit MAC** (IPv6 would show eight groups; IPv4 four decimal numbers).",
        "Six pairs = MAC.", 30)


def add_protocols(S):
    S.q("nw-r1", "easy", "HTTPS uses which default port?",
        ["443", "80", "21", "25"], "443",
        "**HTTPS = 443**; plain HTTP uses 80.",
        "Secure = 443.", 20)
    S.q("nw-r1", "medium", "SMTP sends mail through port —",
        ["25", "110", "143", "21"], "25",
        "**SMTP = 25**; POP3 receives on 110 and IMAP on 143.",
        "Mail out = 25.", 25)
    S.q("nw-r1", "medium", "Which pair of ports belongs to FTP?",
        ["21 and 20", "80 and 443", "22 and 23", "53 and 110"], "21 and 20",
        "**FTP: 21 = control commands, 20 = data** — the two-channel protocol.",
        "Commands first, data second.", 30)
    S.q("nw-r1", "hard", "Match: 1. DNS 2. Telnet 3. POP3 — a. 23 b. 110 c. 53",
        ["1-c, 2-a, 3-b", "1-a, 2-c, 3-b", "1-c, 2-b, 3-a", "1-b, 2-a, 3-c"],
        "1-c, 2-a, 3-b",
        "DNS = 53, Telnet = 23, POP3 = 110.",
        "53, 23, 110.", 35)
    S.q("nw-r2", "easy", "Which transport protocol is CONNECTION-ORIENTED and reliable?",
        ["TCP", "UDP", "IP", "ICMP"], "TCP",
        "**TCP** opens a connection, numbers segments and retransmits losses — reliable delivery.",
        "TCP = tracked.", 20)
    S.q("nw-r2", "medium", "Live video streaming and online gaming normally use —",
        ["UDP", "TCP", "FTP", "SMTP"], "UDP",
        "**UDP** is fast and never pauses to retransmit — one lost frame beats a frozen picture.",
        "Live = UDP.", 25)
    S.q("nw-r2", "medium", "Downloading a large software file from the Internet should use —",
        ["TCP", "UDP", "DHCP", "ARP"], "TCP",
        "A file must arrive complete and in order — **TCP's reliability** is worth its slowness.",
        "Files need all bytes = TCP.", 25)
    S.q("nw-r2", "hard", "Which service typically runs its queries over UDP?",
        ["DNS name lookups", "Sending e-mail with SMTP", "Uploading files with FTP", "Loading a page over HTTPS"],
        "DNS name lookups",
        "A single quick query-and-reply fits **UDP** (port 53); mail, FTP and HTTPS ride on reliable TCP.",
        "Quick question = UDP.", 35)
    S.q("nw-r3", "easy", "Which protocol is used to transfer files between computers over a network?",
        ["FTP", "SMTP", "POP3", "DHCP"], "FTP",
        "**FTP = File Transfer Protocol** — control on port 21, data on 20.",
        "F = File.", 20)
    S.q("nw-r3", "medium", "Which service automatically assigns IP addresses to devices joining a network?",
        ["DHCP", "DNS", "FTP", "SNMP"], "DHCP",
        "**DHCP = Dynamic Host Configuration Protocol** — hands each device its IP settings.",
        "DHCP hands addresses.", 25)
    S.q("nw-r3", "medium", "HTTPS differs from HTTP because it —",
        ["Encrypts the traffic using TLS/SSL", "Uses a different type of cable",
         "Only works on intranets", "Sends no headers"],
        "Encrypts the traffic using TLS/SSL",
        "HTTPS = **HTTP inside an encrypted TLS/SSL tunnel** (port 443) — same web, locked line.",
        "S = secure tunnel.", 25)
    S.q("nw-r4", "medium", "Which remote-login protocol sends data, including passwords, WITHOUT encryption?",
        ["Telnet", "SSH", "HTTPS", "SFTP"], "Telnet",
        "**Telnet (23) is plaintext** — SSH (22) is its encrypted modern replacement.",
        "Telnet = no lock.", 25)
    S.q("nw-r4", "medium", "UDP stands for —",
        ["User Datagram Protocol", "Unified Data Protocol", "Universal Delivery Process",
         "User Data Program"],
        "User Datagram Protocol",
        "**UDP = User Datagram Protocol** — connectionless, no delivery guarantee, very fast.",
        "Datagram = fire and forget.", 20)
    S.q("nw-r4", "hard", "Arrange the ports in ASCENDING order: 1. SMTP 2. SSH 3. HTTP 4. FTP-control",
        ["4, 2, 1, 3", "2, 4, 1, 3", "2, 1, 4, 3", "4, 1, 2, 3"],
        "4, 2, 1, 3",
        "FTP 21 < SSH 22 < SMTP 25 < HTTP 80 = **4, 2, 1, 3**.",
        "21, 22, 25, 80.", 40)
