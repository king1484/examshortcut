# -*- coding: utf-8 -*-
"""Topic 8: networking. Mesh-link counts and IP classifications verified numerically."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

# ---- verification ----
def mesh(n): return n * (n - 1) // 2
assert mesh(6) == 15 and mesh(5) == 10 and mesh(8) == 28 and mesh(10) == 45
def cls(a):
    if 1 <= a <= 126: return "A"
    if 128 <= a <= 191: return "B"
    if 192 <= a <= 223: return "C"
    if 224 <= a <= 239: return "D"
    return "E"
assert cls(10) == "A" and cls(172) == "B" and cls(192) == "C" and cls(193) == "C" and cls(225) == "D"
assert cls(126) == "A" and cls(128) == "B" and cls(191) == "B" and cls(223) == "C"
assert 2**7 - 2 == 126 and 2**16 - 2 == 65534 and 2**8 - 2 == 254

T = {
  "id": "networking",
  "sectionId": "computer",
  "title": "Networking: Devices, Topologies & Protocols",
  "order": 8,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 3},
  "summary": "Network types and topologies, devices (hub/switch/router), the OSI model, IP addressing and TCP/UDP with port numbers. Device-to-layer matching and IP-class identification are CKT regulars.",
  "subtopics": [
    {
      "id": "nw-types-topologies",
      "title": "Network types and topologies",
      "concept": """**By reach:**

| Type | Span | Example |
|---|---|---|
| PAN (Personal) | ~10 m around one person | Bluetooth headset link |
| LAN (Local) | Building/campus; Ethernet/Wi-Fi; privately owned | Office/lab network |
| MAN (Metropolitan) | City | Cable TV/city ISP network |
| WAN (Wide) | Countries/continents; leased lines | The Internet is the largest WAN |

A **VPN** builds an encrypted private tunnel over a public network. Networks run as **client-server** (dedicated servers) or **peer-to-peer** (equal machines).

**Topologies** (physical layout):

| Topology | Structure | Notes |
|---|---|---|
| Bus | One backbone cable with terminators | Cheap; backbone failure kills all; collisions |
| Star | All nodes wired to a central hub/switch | **Most common** (modern Ethernet); one cable failure is local, but the hub/switch is a single point of failure |
| Ring | Each node joined to exactly two neighbours | Token passing; one break can halt the loop |
| Mesh | Every pair of nodes directly linked | Most reliable, costliest; full-mesh links = n(n-1)/2 |
| Tree | Hierarchy of stars | Used in large LANs |
| Hybrid | Mix of the above | Real-world networks |

Wireless: **Wi-Fi** = IEEE **802.11** family (n/ac/ax = Wi-Fi 4/5/6); **Bluetooth** = 802.15, ~10 m PAN; infrared needs line of sight.""",
      "formulas": [],
      "tricks": [
        {"title": "Mesh half-row sum", "body": "Full-mesh links for n nodes = **n(n-1)/2**: 6 nodes -> 6x5/2 = 15. Half of n rows of (n-1) - compute, don't memorise per-n.", "example": {"q": "How many links in a full mesh of 8 computers?", "solution": "8x7/2 = 28."}},
        {"title": "PLMW span ladder", "body": "**P**AN < **L**AN < **M**AN < **W**AN - Personal, Local, Metropolitan, Wide. The Internet is the WAN of WANs.", "example": {"q": "A network limited to one office building is a?", "solution": "LAN."}},
        {"title": "Star = spine", "body": "Modern offices run **star** topology around a switch. If a question says 'central device fails, whole network down', it is describing star's weakness.", "example": {"q": "In which topology is the central hub a single point of failure?", "solution": "Star."}}
      ],
      "mistakes": [
        "Using the bus topology's weaknesses for star questions.",
        "Counting mesh links as n^2 - duplicates don't count; it's n(n-1)/2.",
        "Calling Wi-Fi 'IEEE 802.3' - 802.3 is wired Ethernet; Wi-Fi is 802.11."
      ]
    },
    {
      "id": "nw-devices",
      "title": "Network devices",
      "concept": """| Device | OSI layer | Job |
|---|---|---|
| NIC (Network Interface Card) | 2 | Connects a machine to the network; carries the burned-in 48-bit MAC address |
| Repeater | 1 | Regenerates a weakened signal to extend range |
| Hub | 1 | Multi-port repeater: **broadcasts every bit to every port**; no intelligence, half-duplex |
| Bridge | 2 | Joins two LAN segments, filtering by MAC |
| Switch | 2 | Learns a MAC-address table and forwards frames **only to the destination port**; full duplex |
| Router | 3 | Routes packets **between different networks** using IP addresses; the home gateway to the Internet |
| Gateway | up to 7 | Converts between different protocol architectures ('entrance/exit door' of a network) |
| Modem | - | **MO**dulator-**DEM**odulator: converts digital <-> analog for phone/cable lines |
| Access Point | 2 | Bridges Wi-Fi clients onto the wired LAN |
| Firewall | - | Hardware/software rule-filter that allows or blocks traffic (can sit at several layers) |

Memory hooks: **hub = dumb loudspeaker; switch = smart postman (MAC table); router = intercity network connector (IP).**""",
      "formulas": [],
      "tricks": [
        {"title": "Hub-Switch-Router ladder", "body": "**Hub** hears and shouts to all (layer 1); **S**witch = **S**elective, by MAC (layer 2, same network); **R**outer = **R**outes between networks by IP (layer 3). Exam verbs: 'broadcasts to all' -> hub; 'MAC address table' -> switch; 'connects two different networks' -> router.", "example": {"q": "Which device forwards data only to the intended port using MAC addresses?", "solution": "Switch."}},
        {"title": "Modem = modulator + demodulator", "body": "The full form itself is the answer: digital computer data is modulated onto an analog carrier and demodulated back. 'Digital to analog conversion' in a question = modem.", "example": {"q": "Device that converts digital signals to analog and back?", "solution": "Modem."}}
      ],
      "mistakes": [
        "Saying a hub forwards selectively - that is the switch; hubs always broadcast.",
        "Placing the router at the Data Link layer - routers work on IP (Network layer, 3).",
        "Confusing gateway (protocol converter) with router (route selector)."
      ]
    },
    {
      "id": "nw-osi",
      "title": "OSI and TCP/IP reference models",
      "concept": """**OSI (Open Systems Interconnection)** - 7 layers, top-down:

| # | Layer | Function | Works with |
|---|---|---|---|
| 7 | Application | User-facing network services | HTTP, FTP, SMTP, DNS |
| 6 | Presentation | Format, **encryption**, compression | JPEG, MP3, SSL/TLS concepts |
| 5 | Session | Opens/manages/closes dialogues | NetBIOS, RPC |
| 4 | Transport | End-to-end delivery, ports, reliability | **TCP, UDP** (data units: segments) |
| 3 | Network | Logical addressing, **routing** | IP, **routers** (packets) |
| 2 | Data Link | Framing, MAC addressing, error detect | Ethernet, **switches/bridges** (frames) |
| 1 | Physical | Raw **bits** on the medium | Cables, hubs, repeaters |

**TCP/IP model** compresses these into 4: Application (7+6+5), Transport (4), Internet (3), Network Access/Link (2+1) - it is what the real Internet runs.

Encapsulation journey: data -> segments (L4) -> packets (L3) -> frames (L2) -> bits (L1).""",
      "formulas": [],
      "tricks": [
        {"title": "OSI mnemonics", "body": "Bottom-up: \"**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way\" (Physical, Data link, Network, Transport, Session, Presentation, Application). Top-down: \"**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing\".", "example": {"q": "Which OSI layer comes directly above the Network layer?", "solution": "Transport (P-D-N-T: layer 4)."}},
        {"title": "Layer-device pairs", "body": "**R**outer = layer **3** (both R words rhyme with 'routing/IP'); **Switch/Bridge** = layer 2 (frames/MAC); **Hub/Repeater** = layer 1 (bits). Any 'works at which layer' question resolves by the device's address type: IP = 3, MAC = 2, no address = 1.", "example": {"q": "At which OSI layer does a router operate?", "solution": "Layer 3 - Network."}}
      ],
      "mistakes": [
        "Counting 4 or 5 OSI layers - the model has 7 (the TCP/IP model has 4).",
        "Putting encryption at the Application layer - classic encryption/formatting sits in Presentation (6).",
        "Saying the Session layer routes packets - routing is Network (3)."
      ]
    },
    {
      "id": "nw-ip",
      "title": "IP addressing: IPv4 classes and IPv6",
      "concept": """**IPv4** = 32-bit address, four octets 0-255 in dotted decimal (192.168.1.1). The first octet fixes the class:

| Class | First octet | Default mask | Hosts/network | Use |
|---|---|---|---|---|
| A | 1 - 126 | 255.0.0.0 (/8) | 1,67,77,214 | Huge networks |
| B | 128 - 191 | 255.255.0.0 (/16) | 65,534 | Large organisations |
| C | 192 - 223 | 255.255.255.0 (/24) | 254 | Small networks |
| D | 224 - 239 | - | - | Multicasting |
| E | 240 - 255 | - | - | Experimental/R&D |

Special addresses: **127.0.0.1 = loopback/localhost** (test your own stack); 0.0.0.0 = unspecified; 255.255.255.255 = broadcast. **Private ranges** (not routed on the Internet): 10.0.0.0/8, 172.16.0.0-172.31.255.255, **192.168.0.0/16** (home routers).

**IPv6** = **128-bit**, written as eight hex groups with colons (2001:0db8::7334), solving IPv4 exhaustion. **MAC address** = 48-bit hardware address of the NIC (physical, layer 2) versus the IP (logical, layer 3). **DHCP** auto-assigns IPs; static addressing sets them by hand.""",
      "formulas": [],
      "tricks": [
        {"title": "Class ruler", "body": "Remember three cut-points: **1 - 126 - 128 - 191 - 192 - 223**. A starts at 1, B at 128, C at 192, D (multicast) at 224. 127 is the loopback no-man's land between A and B.", "example": {"q": "Class of 172.16.0.1?", "solution": "B (first octet 172 lies in 128-191)."}},
        {"title": "Loopback = 127", "body": "**127.0.0.1 = localhost** - pinging it tests your own TCP/IP stack, never the cable. Any question with 127.x wants 'loopback'.", "example": {"q": "Pinging 127.0.0.1 tests?", "solution": "The local machine's own TCP/IP configuration."}},
        {"title": "IPv4 vs IPv6 size", "body": "IPv4 = **32-bit** dotted decimal; IPv6 = **128-bit** colon-hex. 'Runs out of addresses' questions -> IPv6 as the fix.", "example": {"q": "How many bits does an IPv6 address have?", "solution": "128."}}
      ],
      "mistakes": [
        "Placing 127.0.0.1 in Class A usage - 127 is reserved loopback; Class A networks proper end at 126.",
        "Calling 192.168.1.1 a public address - it is the classic private home-router address.",
        "Confusing MAC (48-bit, physical, burnt into NIC) with IP (logical, assignable)."
      ]
    },
    {
      "id": "nw-protocols",
      "title": "Protocols and port numbers; TCP vs UDP",
      "concept": """| Protocol | Port | Purpose |
|---|---|---|
| HTTP | 80 | Web pages (plain) |
| HTTPS | **443** | Web over TLS/SSL encryption |
| FTP | 21 (control) / 20 (data) | File transfer |
| SSH | 22 | Secure remote login (encrypted successor of Telnet) |
| Telnet | 23 | Plain-text remote login (insecure) |
| SMTP | 25 | Sending e-mail |
| DNS | 53 | Name-to-IP resolution |
| DHCP | 67/68 | Automatic IP assignment |
| POP3 | 110 | Receive e-mail (download) |
| IMAP | 143 | Receive e-mail (sync) |
| SNMP | 161 | Network management/monitoring |
| RDP | 3389 | Windows remote desktop |

**TCP (Transmission Control Protocol)** - connection-oriented, 3-way handshake (SYN, SYN-ACK, ACK), guaranteed ordered delivery: web, e-mail, file transfer. **UDP (User Datagram Protocol)** - connectionless, no delivery guarantee, faster/lower overhead: DNS queries, DHCP, video/audio streaming, VoIP, online gaming. Standards: Ethernet = IEEE 802.3, Wi-Fi = 802.11, Bluetooth = 802.15.""",
      "formulas": [],
      "tricks": [
        {"title": "Port anchors", "body": "Memorise six: **80 HTTP, 443 HTTPS, 25 SMTP, 53 DNS, 110 POP3, 21 FTP** - these cover most CKT options. Then '22 SSH, 23 Telnet' (Telnet = the insecure 23).", "example": {"q": "Default port of HTTPS?", "solution": "443."}},
        {"title": "TCP = Tracked, UDP = Untracked", "body": "**T**CP **T**racks every packet (reliable, slower - web/mail/files); **U**DP is **U**nreliable but quick (streaming, gaming, DNS). 'Guaranteed delivery' in the question = TCP.", "example": {"q": "Live cricket video streaming mainly uses?", "solution": "UDP (speed over retransmission)."}}
      ],
      "mistakes": [
        "Giving HTTP the 443 port - 443 is HTTPS; plain HTTP is 80.",
        "Choosing TCP for live streaming in the classic question - the intended answer is UDP (speed first).",
        "Saying Telnet is secure - SSH (22) is the encrypted one; Telnet (23) sends everything in clear text."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Device identification by job", "frequency": "very common", "howToSpot": "'Which device connects two different networks?' / 'forwards using MAC table?'.", "approach": "Router = between networks (IP); switch = within a LAN by MAC; hub = broadcast to all; repeater = signal booster; modem = digital-analog; gateway = protocol conversion."},
    {"pattern": "OSI layer count/function/device", "frequency": "very common", "howToSpot": "'How many layers in OSI?' / 'router works at which layer?'.", "approach": "7 layers; device by address type (no address = 1, MAC = 2, IP = 3); encryption = Presentation; routing = Network."},
    {"pattern": "IP class identification", "frequency": "common", "howToSpot": "'Which class does 172.16.5.4 belong to?' / 'which range is Class C?'.", "approach": "First-octet ruler 1-126 / 128-191 / 192-223 / 224-239 / 240-255; 127 = loopback, 192.168.x = private."},
    {"pattern": "Port-number matching", "frequency": "common", "howToSpot": "'Port 443 is used by?' or a match-the-columns of protocols and ports.", "approach": "Anchor six ports (80/443/25/53/110/21) and pair the rest logically (22/23 secure-insecure login, 67/68 DHCP)."},
    {"pattern": "TCP vs UDP selection", "frequency": "common", "howToSpot": "'Which protocol for streaming?' / 'connection-oriented protocol?'.", "approach": "Reliability/ordered/connection = TCP; speed/no-guarantee/streaming = UDP."}
  ],
  "solvedExamples": [
    Q("nw-se01",
      "A fully connected mesh network is made with 6 computers. How many duplex links are required?",
      ["12", "15", "30", "21"], 1,
      "Full mesh links = n(n-1)/2 = 6x5/2 = 15. (n(n-1) = 30 counts every link twice, once from each end.)",
      "Apply n(n-1)/2 directly; the 30 option is the 'forgot to halve' trap.",
      "medium", "nw-types-topologies", "mesh link computation", 45),
    Q("nw-se02",
      "Which device connects two different networks and routes packets between them using IP addresses?",
      ["Hub", "Switch", "Router", "Repeater"], 2,
      "A router works at the Network layer, reading IP addresses to forward packets between distinct networks (e.g. your LAN to the Internet). Hubs broadcast at the physical layer, switches forward frames by MAC within one LAN, repeaters only regenerate signals.",
      "'Two DIFFERENT networks + IP' = router, every time.",
      "easy", "nw-devices", "device identification", 35),
    Q("nw-se03",
      "Match the OSI layer with its function: (a) Transport (b) Data Link (c) Presentation - (i) MAC addressing and framing (ii) encryption and compression (iii) end-to-end delivery using ports",
      ["a-iii, b-i, c-ii", "a-ii, b-iii, c-i", "a-iii, b-ii, c-i", "a-i, b-iii, c-ii"], 0,
      "Transport (layer 4) gives end-to-end delivery with port numbers (a-iii). Data Link (2) frames data and uses MAC addresses (b-i). Presentation (6) handles format, encryption and compression (c-ii).",
      "Port = Transport, MAC/frame = Data Link, encrypt = Presentation - three clean anchors.",
      "medium", "nw-osi", "layer-function matching", 45),
    Q("nw-se04",
      "The IP addresses 10.0.0.5, 172.20.1.9 and 192.168.0.10 belong respectively to which classes?",
      ["A, B, C", "A, C, B", "B, A, C", "C, B, A"], 0,
      "First octets: 10 falls in 1-126 (Class A), 172 in 128-191 (Class B), 192 in 192-223 (Class C). All three are also private-range addresses.",
      "Apply the ruler to the first octet only; ignore the rest of the address.",
      "medium", "nw-ip", "IP class identification", 45)
  ],
  "practice": [
    Q("nw-q01",
      "A network confined to a single office building is classified as a:",
      ["WAN", "MAN", "LAN", "VAN"], 2,
      "A LAN (Local Area Network) covers a room, building or campus. MANs span cities, WANs span countries/continents.",
      "Local = LAN; City = MAN; Wide/world = WAN.",
      "easy", "nw-types-topologies", "network types", 25),
    Q("nw-q02",
      "In which topology is every node connected to every other node by a dedicated link?",
      ["Star", "Ring", "Bus", "Mesh"], 3,
      "Full mesh gives each pair of nodes its own direct link - maximum reliability at maximum cable cost (n(n-1)/2 links).",
      "'Every pair directly connected' = mesh.",
      "easy", "nw-types-topologies", "topology identification", 30),
    Q("nw-q03",
      "Which network device broadcasts received data to all connected ports without any addressing intelligence?",
      ["Switch", "Router", "Hub", "Gateway"], 2,
      "A hub is a multi-port repeater - it blindly repeats every bit to every port. Switches consult a MAC table; routers consult IP routes.",
      "Dumb broadcast = hub; smart selection = switch.",
      "easy", "nw-devices", "device identification", 30),
    Q("nw-q04",
      "The number of layers in the OSI reference model is:",
      ["4", "5", "6", "7"], 3,
      "OSI has 7 layers (Application to Physical). The TCP/IP model that the Internet actually uses has 4.",
      "OSI 7, TCP/IP 4 - don't swap them.",
      "easy", "nw-osi", "OSI basics", 25),
    Q("nw-q05",
      "At which layer of the OSI model does a switch primarily operate?",
      ["Physical", "Data Link", "Network", "Transport"], 1,
      "Switches forward frames using MAC (hardware) addresses, which belong to the Data Link layer (2). Routers use IP at layer 3.",
      "MAC-address device = layer 2; IP device = layer 3.",
      "medium", "nw-osi", "layer-device mapping", 35),
    Q("nw-q06",
      "Encryption and data compression in the OSI model are the responsibility of the:",
      ["Session layer", "Application layer", "Presentation layer", "Transport layer"], 2,
      "Presentation (layer 6) translates data formats and applies encryption/compression (JPEG, MP3, TLS concepts). Session manages dialogues, Transport moves segments.",
      "Encrypt/compress/translate = Presentation.",
      "medium", "nw-osi", "layer functions", 35),
    Q("nw-q07",
      "How many links are needed for a full mesh topology with 5 computers?",
      ["5", "8", "10", "20"], 2,
      "n(n-1)/2 = 5x4/2 = 10 links.",
      "Five nodes -> 5x4/2; the 20 option is the un-halved trap for those using n(n-1) with n=5... actually 20 = n x (n-1), another halving slip - always divide by 2.",
      "easy", "nw-types-topologies", "mesh link computation", 35),
    Q("nw-q08",
      "The IP address 127.0.0.1 is used for:",
      ["Broadcast to all hosts", "Loopback testing of the local machine", "Default gateway", "Multicasting"], 1,
      "127.x.x.x (typically 127.0.0.1 = localhost) loops packets back to the sender's own TCP/IP stack for self-testing.",
      "127 = loopback = 'talk to yourself'.",
      "easy", "nw-ip", "special IP addresses", 30),
    Q("nw-q09",
      "An IPv4 address is how many bits long?",
      ["16", "32", "64", "128"], 1,
      "IPv4 = 32 bits (four octets). IPv6 expanded this to 128 bits written in hexadecimal.",
      "v4 -> 32, v6 -> 128.",
      "easy", "nw-ip", "IP basics", 25),
    Q("nw-q10",
      "Which of the following is a private IP address commonly used by home routers?",
      ["172.32.10.1", "192.168.1.1", "169.254.1.1", "8.8.8.8"], 1,
      "192.168.0.0/16 is reserved for private networks - the default address of most home routers. 172.32 lies outside the private 172.16-172.31 block, 169.254.x.x is APIPA/link-local, and 8.8.8.8 is Google's public DNS.",
      "The private trio: 10.x, 172.16-31.x, 192.168.x. Everything else is public.",
      "medium", "nw-ip", "private IP ranges", 40),
    Q("nw-q11",
      "The default port number for HTTPS traffic is:",
      ["21", "80", "443", "8080"], 2,
      "HTTPS runs over TLS on port 443; 80 is plain HTTP, 21 is FTP control, 8080 is a common alternate proxy port.",
      "443 = the padlock port.",
      "easy", "nw-protocols", "port numbers", 30),
    Q("nw-q12",
      "Which protocol is normally used by live audio/video streaming where speed matters more than perfect delivery?",
      ["TCP", "UDP", "FTP", "SMTP"], 1,
      "UDP is connectionless with no retransmission overhead, so realtime media, VoIP and gaming prefer it. TCP guarantees ordered delivery (web, mail, downloads).",
      "Speed-first, drop-tolerant = UDP.",
      "medium", "nw-protocols", "TCP vs UDP", 35),
    Q("nw-q13",
      "A modem's function is to:",
      ["Route packets between networks", "Convert digital signals to analog and back", "Store web pages", "Filter traffic by rules"], 1,
      "MOdulator-DEModulator: it turns the computer's digital bits into analog carrier tones (and vice versa) for transmission over telephone/cable plant. Routing is a router; rule-filtering is a firewall.",
      "Digital <-> analog conversion is the modem's whole identity.",
      "easy", "nw-devices", "device identification", 30),
    Q("nw-q14",
      "The Wi-Fi wireless LAN standard family is designated by IEEE:",
      ["802.3", "802.11", "802.15", "802.16"], 1,
      "IEEE 802.11 covers Wi-Fi (a/b/g/n/ac/ax). 802.3 is wired Ethernet, 802.15 Bluetooth/PAN, 802.16 WiMAX.",
      "Wi-Fi has '11' in its number: 802.11.",
      "easy", "nw-protocols", "IEEE standards", 30),
    Q("nw-q15",
      "In a star topology, failure of the central hub/switch:",
      ["Has no effect on other nodes", "Brings down communication between all nodes", "Affects only the node next to the hub", "Converts the network to a ring"], 1,
      "Every node's cable meets at the central device, so its failure isolates the entire network - star's well-known single point of failure (individual cable breaks, however, affect only one node).",
      "Centre dies, star dies - that weakness is the exam favourite.",
      "medium", "nw-types-topologies", "topology properties", 35)
  ]
}

validate_and_dump_topic(T)
