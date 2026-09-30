"""Readable rewrite of Computer > Networking (all 5 subtopics).

Plain English, short sentences, tables, one method per question type.
Facts are kept exactly as in the old notes. Old pattern ids are kept; new ids continue each prefix.
Run: python networking.py  (patches content/core/topics/computer/networking.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "computer" / "networking.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


# ---- computed facts (asserted against the numbers written in the text) ----
def mesh(n):
    return n * (n - 1) // 2


assert (mesh(4), mesh(5), mesh(6), mesh(8)) == (6, 10, 15, 28)
assert mesh(10) == 45 and mesh(7) == 21
assert 2 ** 8 - 2 == 254 and 2 ** 16 - 2 == 65534 and 2 ** 24 - 2 == 16777214
assert 2 ** 32 == 4294967296 and 48 // 8 == 6 and 128 // 16 == 8

SUBS = {}

# =====================================================================
# 1. Network types and topologies
# =====================================================================
SUBS["nw-types-topologies"] = dict(
    concept=(
        "Networks are named by how far they reach: PAN, LAN, MAN and WAN, from small to large. "
        "A topology is the shape of the wiring: bus, ring, star, mesh, tree or hybrid. "
        "Star is the shape used in modern offices. A full mesh of n computers needs n(n-1)/2 links."
    ),
    notes=r"""### Networks by their reach
Name a network by how far it stretches. The order is PAN, then LAN, then MAN, then WAN.

| Type | Span | Everyday example |
|---|---|---|
| **PAN** (Personal Area Network) | about 10 metres around one person | Bluetooth headset with a phone |
| **LAN** (Local Area Network) | one building or campus | school computer lab, office floor |
| **MAN** (Metropolitan Area Network) | one city | city cable network |
| **WAN** (Wide Area Network) | countries or continents | the **Internet is the largest WAN** |

A LAN is privately owned and fast. A WAN uses leased lines over long distances.

> **Tip:** Match the span in the question, not the technology. "One office building" is always a LAN.

### Topologies, the shape of the wiring
A **topology** is the way computers are laid out and joined. Learn the table row by row.

| Topology | Layout | Strength | Weakness |
|---|---|---|---|
| **Bus** | all nodes tap one backbone cable with terminators | cheapest | backbone break kills all; collisions |
| **Ring** | each node joins exactly two neighbours | orderly token passing | one break can halt the loop |
| **Star** | every node joins a central hub or switch | one cable failure hurts one node only | the central device is a single point of failure |
| **Mesh** | every node joins every other node | most reliable | most cables, costliest |
| **Tree** | hierarchy of stars joined on a bus | scales to large LANs | root failure splits the tree |
| **Hybrid** | a mix of the above | fits real networks | more complex |

> **Rule:** Star is the most common shape today. Mesh is the most reliable.

### Counting mesh links
In a full mesh of n computers, each one has n - 1 links. Every link is counted twice that way, so halve the total.

$$\text{links}=\dfrac{n(n-1)}{2}$$

> **Example:** For 6 computers, $6\times5\div2=15$ links. For 8 computers, $8\times7\div2=28$ links.

Never use $n^2$. Check small cases: 4 computers give 6 links, 5 give 10.

### Client-server, peer-to-peer and VPN
- **Client-server:** dedicated servers serve many client machines.
- **Peer-to-peer:** all machines are equals. Each can share and use resources.
- **VPN:** builds an encrypted private tunnel over a public network.

### Wireless and IEEE standards
- **Ethernet** (wired LAN) is IEEE **802.3**.
- **Wi-Fi** (wireless LAN) is IEEE **802.11**. The versions n, ac and ax are called Wi-Fi 4, 5 and 6.
- **Bluetooth** is IEEE **802.15**. It is a PAN of about 10 metres.
- **Infrared** needs a clear line of sight.

> **Watch:** Wi-Fi is not 802.3. The number 802.3 belongs to wired Ethernet.
""",
    tricks=[
        trick("Mesh half-row sum",
              "Full-mesh links for n nodes are n(n-1)/2. Compute it each time. Do not memorise per-n values.",
              "How many links does a full mesh of 8 computers need?",
              ["Each computer has 7 links.", "8 x 7 = 56, and each link is counted twice.", "56 / 2 = 28."], "28 links"),
        trick("PLMW span ladder",
              "PAN < LAN < MAN < WAN: Personal, Local, Metropolitan, Wide. The Internet is the largest WAN.",
              "A network limited to one office building is a?",
              ["One building is a local span.", "Local Area Network."], "LAN"),
        trick("Star means central device",
              "If the question says the central device fails and the whole network stops, it describes star topology.",
              "In which topology is the central hub a single point of failure?",
              ["Every node hangs off the hub.", "If the hub fails, none can talk."], "Star topology"),
    ],
    mistakes=[
        mis("Using the bus topology's weakness (backbone break) for star questions.",
            "Star fails at the central hub or switch. Bus fails at the backbone."),
        mis("Counting mesh links as $n^2$.", "Use n(n-1)/2. Each link is counted once, not twice."),
        mis("Calling Wi-Fi IEEE 802.3.", "802.3 is wired Ethernet. Wi-Fi is 802.11."),
        mis("Calling the Internet a MAN or a LAN.", "The Internet is the largest WAN."),
    ],
    revision=[
        "PAN (10 m) < LAN (building) < MAN (city) < WAN (country or world).",
        "The Internet is the largest WAN.",
        "Bus = one backbone. Ring = circle of neighbours. Star = central hub or switch. Mesh = all to all.",
        "Full-mesh links = n(n-1)/2. Six computers give 15 links.",
        "Star's weakness is the central device. Bus's weakness is the backbone.",
        "Ethernet is 802.3, Wi-Fi is 802.11, Bluetooth is 802.15.",
    ],
    patterns=[
        pat("nw-t1", "Network type by span", "very common",
            "A situation is described (school lab, city cable, worldwide web, one person's Bluetooth) and PAN, LAN, MAN or WAN is asked.",
            ["Line up the ladder: PAN, LAN, MAN, WAN.", "Find the span in the question: person, building, city or world.",
             "Pick the type with that span.", "Remember the Internet is the largest WAN."],
            "The span, not the technology, names the network.",
            "A computer lab of one school connected by a switch forms a",
            ["The lab is inside one building.", "One building means a local span."], "LAN (Local Area Network)"),
        pat("nw-t2", "Topology identification by description", "very common",
            "The layout is described (all nodes to a central device, every node to every other, one backbone, a circle) and the topology is asked.",
            ["Central device with all nodes on it: Star.", "Every node linked to every other: Mesh.",
             "One shared backbone cable with terminators: Bus.", "Closed circle of neighbours: Ring. Stars joined on a backbone: Tree."],
            "Each topology has one giveaway layout phrase.",
            "In which topology is every computer connected to a central hub or switch?",
            ["Central hub or switch is the giveaway.", "One cable break isolates only one node."], "Star topology"),
        pat("nw-t3", "Mesh link count (numeric)", "common",
            "How many links are needed for a full mesh of n computers? It is pure arithmetic.",
            ["Write the formula n(n-1)/2.", "Put in n and multiply n by n - 1.", "Halve the product.", "Check with n = 4 giving 6."],
            "Each line is counted twice if you multiply n by n - 1.",
            "How many cable links are needed for a full mesh of 6 computers?",
            ["6 x 5 = 30.", "30 / 2 = 15."], "15 links", formula=r"$\dfrac{n(n-1)}{2}$"),
        pat("nw-t4", "Topology strengths and failure points", "common",
            "A statement says which topology is cheapest, most reliable, has a single point of failure, or what happens when a cable breaks.",
            ["Star: one cable break hurts one node. Hub failure stops all.", "Bus: backbone break means total failure. It is the cheapest.",
             "Mesh: most reliable, most cable, costliest.", "Ring: one broken node or link can stop the ring."],
            "The weakness of each shape follows from how it is wired.",
            "In a star topology, failure of the central hub results in",
            ["Every node depends on the hub.", "Individual cables do not matter here."], "The whole network stops communicating"),
        pat("nw-t5", "IEEE standards and LAN jargon", "occasional",
            "Wi-Fi is IEEE what, or Ethernet works on which standard. It is matching 802.x numbers to technologies.",
            ["Ethernet (wired) is 802.3.", "Wi-Fi (wireless) is 802.11.", "Bluetooth is 802.15.", "Watch for the trap of pairing Wi-Fi with 802.3."],
            "The 802 family names the wire or the air.",
            "Wi-Fi networks are standardised under IEEE",
            ["Wi-Fi is wireless LAN.", "802.3 is wired, 802.15 is Bluetooth."], "802.11"),
        pat("nw-t6", "Network models, VPN and wireless links", "occasional",
            "Questions ask what a VPN does, how client-server differs from peer-to-peer, or the range of Bluetooth.",
            ["VPN: an encrypted private tunnel over a public network.", "Client-server: dedicated servers serve clients.",
             "Peer-to-peer: all machines are equals.", "Bluetooth is a PAN of about 10 m. Infrared needs line of sight."],
            "Each term has one short definition to recall.",
            "Which technology builds an encrypted private tunnel over a public network?",
            ["The key words are encrypted and private tunnel.", "Public network means the Internet."], "VPN (Virtual Private Network)"),
    ],
)

# =====================================================================
# 2. Network devices
# =====================================================================
SUBS["nw-devices"] = dict(
    concept=(
        "Each network device has one job. A hub broadcasts to all ports. A switch sends to the right port by MAC address. "
        "A router joins different networks by IP address. A modem converts digital and analog signals. "
        "Exams rarely name the device. They describe its job."
    ),
    notes=r"""### The device ladder
Learn each device with its layer and its one job.

| Device | Layer | What it does |
|---|---|---|
| **Repeater** | Physical (1) | regenerates a weak signal to extend range |
| **Hub** | Physical (1) | broadcasts every bit to every port; no intelligence |
| **Bridge** | Data Link (2) | joins two LAN segments and filters by MAC |
| **Switch** | Data Link (2) | learns MAC addresses and sends frames only to the right port |
| **NIC** | Data Link (2) | connects one machine to the network; carries its MAC |
| **Access Point** | Data Link (2) | puts Wi-Fi devices onto the wired LAN |
| **Router** | Network (3) | joins different networks and picks routes by IP |
| **Gateway** | up to Application (7) | converts between different protocol systems |

> **Tip:** Hub is a dumb loudspeaker. Switch is a smart postman. Router is the link between cities.

### Modem and firewall
A **modem** is a MOdulator-DEModulator. It turns the PC's digital data into analog signals for a phone or cable line. It turns analog back to digital.

A **firewall** is a rule filter in hardware or software. It allows or blocks traffic by rule. It can work at several layers.

### The one-line differences
- **Hub vs switch:** a hub shouts to everyone. A switch sends only to the destination port. It is faster and safer.
- **Switch vs router:** a switch moves data inside one network by MAC. A router moves data between networks by IP.
- **Repeater vs amplifier:** a repeater regenerates a clean digital signal. An amplifier boosts the noise too.
- **Gateway vs router:** a router chooses routes. A gateway translates between protocol worlds.

> **Note:** Your home router joins your LAN to the Internet.

### MAC address, the burnt-in identity
Every NIC carries a **48-bit physical address**, for example 1A:2B:3C:4D:5E:6F. The maker fixes it.

- **MAC:** physical and permanent. Switches read it.
- **IP:** logical and assigned. Routers read it.

### A home network in four steps
Follow one message from a laptop to a website. This shows where each device sits.

1. The laptop's **NIC** puts the data on the network. It carries the laptop's MAC address.
2. An **access point** takes the Wi-Fi signal and passes it to the wired LAN.
3. A **switch** sends the frames to the router's port only, using its MAC table.
4. The **router** reads the IP address and forwards the packets to the Internet.

A **modem** sits between the router and the phone or cable line. It converts digital and analog signals.

### Reading a device question
Find the verb first. Then name the device.

| Job in the question | Device |
|---|---|
| sends to all ports | hub |
| sends only to the destination port | switch |
| connects two different networks, chooses a path | router |
| regenerates a weak signal | repeater |
| converts protocols | gateway |
| digital to analog and back | modem |

> **Watch:** When a layer is asked, use the ladder. No address is layer 1. MAC is layer 2. IP is layer 3.
""",
    tricks=[
        trick("Hub, switch, router ladder",
              "Hub hears and shouts to all (layer 1). Switch is selective, by MAC (layer 2). Router routes between networks by IP (layer 3). 'Broadcasts to all' means hub. 'MAC address table' means switch. 'Connects two different networks' means router.",
              "Which device forwards data only to the intended port using MAC addresses?",
              ["Selective forwarding is the switch's job.", "The MAC table decides the port."], "Switch"),
        trick("Modem is modulator plus demodulator",
              "The full form is the answer. Digital data is modulated onto an analog carrier and demodulated back. 'Digital to analog conversion' in a question means modem.",
              "Which device converts digital signals to analog and back?",
              ["Modulate means digital to analog.", "Demodulate means analog to digital."], "Modem"),
    ],
    mistakes=[
        mis("Saying a hub forwards data selectively.", "That is the switch. A hub always broadcasts to every port."),
        mis("Placing the router at the Data Link layer.", "A router reads IP addresses, so it sits at the Network layer (3)."),
        mis("Confusing a gateway with a router.", "A gateway converts protocols. A router selects routes."),
        mis("Thinking the MAC address changes with the network.", "MAC is permanent and physical. The IP is the one that is assigned."),
    ],
    revision=[
        "Hub broadcasts (layer 1). Switch learns MAC and sends to the right port (layer 2). Router routes between networks by IP (layer 3).",
        "Repeater regenerates a signal (layer 1). Bridge joins two LANs (layer 2).",
        "Gateway is a protocol converter.",
        "Modem is a modulator plus a demodulator (digital to analog and back).",
        "NIC carries the 48-bit MAC address.",
        "MAC is permanent and physical. IP is logical and assigned.",
    ],
    patterns=[
        pat("nw-d1", "Hub vs switch vs router", "very common",
            "A behaviour is described (sends to all ports, forwards to the right port, connects two networks and picks a path) and the device is asked.",
            ["Sends to all ports: hub (layer 1).", "Sends to the right port by MAC: switch (layer 2).",
             "Joins different networks by IP: router (layer 3).", "More intelligent than a hub: switch."],
            "The job words point to exactly one device.",
            "Which device forwards data only to the intended port instead of all ports?",
            ["Forwarding to one port needs a MAC table.", "Hubs broadcast to every port."], "A switch"),
        pat("nw-d2", "Modem, repeater, bridge, gateway functions", "common",
            "A modem is used for, a device that regenerates a weak signal, or a device that converts between protocols. It is function-to-device matching.",
            ["Modem: digital signal to analog and back.", "Repeater: regenerates weak signals.",
             "Bridge: joins two LAN segments.", "Gateway: translates between protocol systems."],
            "Each device is named after its single job.",
            "The device that regenerates and retransmits a weakening signal is a",
            ["Regenerating a signal is the repeater's job.", "It restores the clean signal so the cable can run farther."], "Repeater"),
        pat("nw-d3", "Device-to-layer matching", "common",
            "A router works on which OSI layer, or a hub operates at layer what. It is a device and layer pair.",
            ["Hub and repeater: layer 1 (Physical).", "Switch, bridge and NIC: layer 2 (Data Link).",
             "Router: layer 3 (Network).", "Gateway reaches up to the Application layer."],
            "The address type a device reads fixes its layer.",
            "A router operates on which layer of the OSI model?",
            ["A router uses IP addresses.", "IP addresses belong to layer 3, the Network layer."], "Layer 3 (Network)"),
        pat("nw-d4", "NIC and MAC-address facts", "common",
            "A MAC address is how many bits, where it is stored, or how MAC differs from IP.",
            ["MAC is a 48-bit physical address.", "The maker burns it into the NIC.",
             "MAC is permanent. IP is assigned and changes.", "Switches use MAC. Routers use IP."],
            "MAC identifies the card. IP identifies the place in a network.",
            "The physical address burnt into a network interface card is the",
            ["A burnt-in, factory-fixed address is physical.", "The IP is only a logical label."], "MAC address (48 bits)"),
        pat("nw-d5", "Firewall and access point", "occasional",
            "A device that allows or blocks traffic by rules, or a device that lets Wi-Fi devices join a wired LAN.",
            ["Allows or blocks traffic by rules: firewall.", "Joins wireless clients to a wired LAN: access point.",
             "A firewall can be hardware or software.", "An access point works at layer 2."],
            "Both devices guard or open a door to the network.",
            "Which device filters traffic by rules to allow or block it?",
            ["Rule-based allow or block is filtering.", "That is a firewall."], "Firewall"),
        pat("nw-d6", "One-line device differences", "common",
            "Statements compare two devices: switch vs router, repeater vs amplifier, gateway vs router.",
            ["Switch: inside one network, by MAC. Router: between networks, by IP.", "Repeater regenerates a clean signal. An amplifier also boosts noise.",
             "Router selects routes. Gateway translates protocols.", "Pick the option that matches the job."],
            "Each pair differs in one key job.",
            "Which device translates between different protocol systems?",
            ["A router only chooses routes.", "Protocol translation is the gateway's job."], "Gateway"),
    ],
)

# =====================================================================
# 3. OSI and TCP/IP
# =====================================================================
SUBS["nw-osi"] = dict(
    concept=(
        "The OSI model splits network work into 7 layers, so each layer can be built and replaced on its own. "
        "The TCP/IP model has 4 layers, and the real Internet runs on it. "
        "Most exam questions ask the layer count, the order, or which layer does a given job."
    ),
    notes=r"""### Why a reference model exists
Sending data needs many jobs: signals, framing, addressing, delivery, dialogue control, translation and user services. The **OSI (Open Systems Interconnection) model** splits them into **7 layers**. Each layer can be designed and replaced on its own.

### The 7 layers, bottom to top

| # | Layer | Job | Works with |
|---|---|---|---|
| 1 | **Physical** | raw **bits** on the medium | cables, hubs, repeaters |
| 2 | **Data Link** | **frames**, MAC addresses, error detection | Ethernet, switches, bridges, NIC |
| 3 | **Network** | logical addressing and **routing** | IP, routers |
| 4 | **Transport** | end-to-end delivery, ports, reliability | TCP, UDP |
| 5 | **Session** | opens, manages and closes dialogues | NetBIOS, RPC |
| 6 | **Presentation** | format, **encryption**, compression | JPEG, MP3, SSL/TLS |
| 7 | **Application** | user-facing network services | HTTP, FTP, SMTP, DNS |

> **Tip:** Bottom-up: "Please Do Not Throw Sausage Pizza Away". Top-down: "All People Seem To Need Data Processing".

### Data units on the way down
Data changes name at each layer as it moves down the sender's stack.

- Layer 4 makes **segments**.
- Layer 3 makes **packets**.
- Layer 2 makes **frames**.
- Layer 1 sends **bits**.

The receiver does the reverse, from layer 1 up to layer 7.

### How layer questions are asked
- **Device to layer:** hub and repeater are layer 1. Switch and bridge are layer 2. Router is layer 3.
- **Job to layer:** routing is Network (3). Framing and MAC are Data Link (2). Encryption and compression are Presentation (6).
- **Number:** OSI has 7 layers. TCP/IP has 4.

> **Watch:** Encryption is not Application. Routing is not Transport. Test the planted option against its neighbour layer.

### Sorting a layer question
First decide what the question really asks. Then use the matching tool.

| Question asks | What to do |
|---|---|
| a **number** | 7 for OSI, 4 for TCP/IP |
| an **order** | use the mnemonic and count |
| a **job** | match the job to one layer |
| a **worker** (device or protocol) | use the address type or the job |

> **Example:** "Which layer delivers data end to end using ports?" The job is end-to-end delivery. That is Transport (4).

For job questions, compare the planted option with its neighbour. Transport only delivers after the Network layer has found the path. Application serves the user. Presentation prepares the data format for it.

### The TCP/IP model
The real Internet runs on TCP/IP. OSI is the teaching map.

| TCP/IP layer | OSI layers it covers |
|---|---|
| **Application** | 5 + 6 + 7 (Session, Presentation, Application) |
| **Transport** | 4 |
| **Internet** | 3 (Network) |
| **Network Access / Link** | 1 + 2 (Physical, Data Link) |

> **Rule:** Which model has 4 layers? TCP/IP.
""",
    tricks=[
        trick("OSI mnemonics",
              "Bottom-up: Please Do Not Throw Sausage Pizza Away (Physical, Data link, Network, Transport, Session, Presentation, Application). Top-down: All People Seem To Need Data Processing.",
              "Which OSI layer comes directly above the Network layer?",
              ["Bottom-up order: Physical, Data Link, Network, Transport.", "Transport follows Network."], "Transport (layer 4)"),
        trick("Layer-device pairs",
              "Router is layer 3. Switch and bridge are layer 2. Hub and repeater are layer 1. Use the address type: IP is 3, MAC is 2, no address is 1.",
              "At which OSI layer does a router operate?",
              ["A router reads IP addresses.", "IP belongs to the Network layer."], "Layer 3 (Network)"),
    ],
    mistakes=[
        mis("Counting 4 or 5 OSI layers.", "OSI has 7 layers. TCP/IP has 4."),
        mis("Putting encryption at the Application layer.", "Encryption, formatting and compression sit in Presentation (6)."),
        mis("Saying the Session layer routes packets.", "Routing is the Network layer (3). Session manages dialogues."),
        mis("Placing TCP and UDP at the Network layer.", "TCP and UDP are Transport layer (4). IP is Network layer (3)."),
    ],
    revision=[
        "OSI has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application.",
        "Router is layer 3, switch is layer 2, hub is layer 1.",
        "Routing is Network. Encryption and compression are Presentation.",
        "Transport layer holds TCP and UDP and uses ports. Session manages dialogues.",
        "Data units: segments (4), packets (3), frames (2), bits (1).",
        "TCP/IP has 4 layers: Network Access, Internet, Transport, Application.",
    ],
    patterns=[
        pat("nw-o1", "OSI layer count and order", "very common",
            "How many layers does the OSI model have, an ordering question, or the layer directly above or below another.",
            ["Recall the 7 layers from Physical (1) to Application (7).", "Use a mnemonic to fix the order.",
             "Transport is the 4th, the middle layer.", "Count up or down from the layer given."],
            "The order never changes, so a mnemonic is enough.",
            "How many layers are there in the OSI reference model?",
            ["OSI is the 7-layer model.", "The 4-layer model is TCP/IP."], "7"),
        pat("nw-o2", "Function-to-layer matching", "very common",
            "Routing is done at which layer, encryption or compression is a which-layer function, or framing and MAC addressing belong to which layer.",
            ["Bits on cables: Physical (1).", "Frames and MAC: Data Link (2). Routing: Network (3).",
             "Delivery and ports: Transport (4). Dialogues: Session (5).", "Encryption and compression: Presentation (6). User services: Application (7)."],
            "Each layer owns one clear job.",
            "Encryption and data compression are functions of which OSI layer?",
            ["Data format work sits below the Application.", "That layer is Presentation."], "Presentation (layer 6)"),
        pat("nw-o3", "Device and protocol-to-layer matching", "common",
            "A switch works at which layer, HTTP is a which-layer protocol, or TCP sits in which layer.",
            ["Hub and repeater are layer 1; switch and bridge layer 2; router layer 3.", "TCP and UDP are layer 4.",
             "HTTP, FTP and SMTP are layer 7. IP is layer 3.", "Match the job before the name."],
            "A device or protocol lives at the layer of its job.",
            "TCP and UDP work at which layer of the OSI model?",
            ["They deliver data end to end.", "They use port numbers."], "Transport (layer 4)"),
        pat("nw-o4", "TCP/IP model vs OSI", "common",
            "The TCP/IP model has how many layers, which OSI layers merge into TCP/IP Application, or mapping the four TCP/IP layers.",
            ["TCP/IP has 4 layers.", "Network Access covers OSI 1 and 2. Internet is 3.",
             "Transport is 4.", "Application covers OSI 5, 6 and 7."],
            "TCP/IP merges the top three and bottom two OSI layers.",
            "How many layers does the TCP/IP model have?",
            ["Network Access, Internet, Transport, Application.", "That makes four."], "4"),
        pat("nw-o5", "Data unit at each layer", "occasional",
            "What is the data unit at layer 2, or data is called packets at which layer.",
            ["Layer 4: segments.", "Layer 3: packets.", "Layer 2: frames. Layer 1: bits.", "Data moves down the sender and up the receiver."],
            "Each layer wraps data and gives it a new name.",
            "Data is called a frame at which OSI layer?",
            ["Frames carry MAC addresses.", "MAC belongs to Data Link."], "Data Link (layer 2)"),
    ],
)

# =====================================================================
# 4. IP addressing
# =====================================================================
SUBS["nw-ip"] = dict(
    concept=(
        "An IPv4 address has 32 bits, written as four numbers from 0 to 255. The first number decides the class. "
        "IPv6 has 128 bits, written in hexadecimal with colons. "
        "127.0.0.1 is loopback, and 192.168.x.x is a private range."
    ),
    notes=r"""### IPv4, the 32-bit address
An **IPv4 address** has **32 bits**. It is written as four numbers from 0 to 255 with dots, like 192.168.1.1. Each number is an **octet** (8 bits). The first octet decides the class.

| Class | First octet | Default mask | Hosts per network | Use |
|---|---|---|---|---|
| **A** | 1 - 126 | 255.0.0.0 (/8) | 1,67,77,214 | huge networks |
| **B** | 128 - 191 | 255.255.0.0 (/16) | 65,534 | large organisations |
| **C** | 192 - 223 | 255.255.255.0 (/24) | 254 | small networks |
| **D** | 224 - 239 | none | none | multicasting |
| **E** | 240 - 255 | none | none | experimental or research |

> **Tip:** Anchor the ruler at 1, 128, 192, 224 and 240. Drop the given number between them.

### Usable hosts
Two addresses in each network are reserved: the network address and the broadcast address.

> **Example:** Class C has 256 addresses. Take away 2. That leaves **254 usable hosts**.

### Special addresses
- **127.0.0.1** is loopback or localhost. A machine talks to itself. Pinging it tests your own TCP/IP stack.
- **0.0.0.0** is the unspecified address.
- **255.255.255.255** is the broadcast address.
- **Private ranges** are not routed on the Internet: 10.0.0.0/8, 172.16.0.0 to 172.31.255.255, and 192.168.0.0/16.

> **Watch:** 127 is not a Class A network. Class A ends at 126. Home routers use 192.168.x.x, which is private.

### IPv6, the 128-bit address
IPv4 has about 4.3 billion addresses. That is too few for the connected world. **IPv6 uses 128 bits**. It is written as **eight groups of hexadecimal digits** with colons, for example 2001:0db8::7334. A double colon can shorten a run of zeros.

### MAC and IP compared

| | MAC address | IP address |
|---|---|---|
| Type | physical, burnt into the NIC | logical, assigned |
| Size | 48 bits | IPv4 32 bits, IPv6 128 bits |
| Changes | never | changes with the network |
| Used by | switches (layer 2) | routers (layer 3) |

**DHCP** gives IP addresses automatically. A **static** address is set by hand.

### Worked class checks
Cover everything after the first dot. Look at the first octet only.

| Address | First octet | Class |
|---|---|---|
| 10.0.0.5 | 10 | A |
| 130.10.5.2 | 130 | B |
| 196.1.2.3 | 196 | C |
| 225.5.4.1 | 225 | D (multicast) |
| 245.0.0.1 | 245 | E |

> **Rule:** 127.x.x.x is never a Class A host address. It is loopback.

### Checking a private address
A private address starts with 10, or with 172 and a second number from 16 to 31, or with 192.168. A 172 address with second number 32 or more is public.
""",
    tricks=[
        trick("Class ruler",
              "Remember the cut-points 1, 128, 192, 224, 240. A starts at 1, B at 128, C at 192, D (multicast) at 224, E at 240. The number 127 is loopback, between A and B.",
              "What is the class of 172.16.0.1?",
              ["Read only the first octet: 172.", "172 lies in 128 to 191."], "Class B"),
        trick("Loopback is 127",
              "127.0.0.1 is localhost. Pinging it tests your own TCP/IP stack, not the cable. Any question with 127.x wants loopback.",
              "Pinging 127.0.0.1 tests what?",
              ["127.0.0.1 is the machine itself.", "It never leaves the computer."], "The local machine's own TCP/IP setup"),
        trick("IPv4 vs IPv6 size",
              "IPv4 is 32 bits in dotted decimal. IPv6 is 128 bits in colon-separated hexadecimal. If addresses are running out, IPv6 is the fix.",
              "How many bits does an IPv6 address have?",
              ["IPv4 has 32 bits.", "IPv6 has 128 bits."], "128"),
    ],
    mistakes=[
        mis("Calling 127.0.0.1 a Class A host address.", "127 is reserved for loopback. Class A networks end at 126."),
        mis("Calling 192.168.1.1 a public address.", "It is the classic private home-router address."),
        mis("Confusing the MAC address with the IP address.", "MAC is 48-bit, physical and burnt in. IP is logical and assigned."),
        mis("Reading the whole address to find the class.", "Only the first octet decides the class."),
        mis("Giving all 256 addresses of Class C as usable hosts.", "Two are reserved, so 254 are usable."),
    ],
    revision=[
        "IPv4 has 32 bits in four octets from 0 to 255. IPv6 has 128 bits in hexadecimal with colons.",
        "Classes by first octet: A 1-126, B 128-191, C 192-223, D 224-239, E 240-255.",
        "127.0.0.1 is loopback.",
        "Private ranges: 10.x, 172.16 to 172.31.x, 192.168.x.",
        "A Class C network has 254 usable hosts.",
        "MAC is 48-bit and physical. IP is logical.",
        "DHCP gives IP addresses automatically.",
    ],
    patterns=[
        pat("nw-p1", "IP class identification", "very common",
            "An address is given (10.0.0.5, 130.10.5.2, 196.1.2.3, 225.5.4.1) and its class is asked, or the range of a class is asked.",
            ["Read only the first octet.", "1-126 is A, 128-191 is B, 192-223 is C.",
             "224-239 is D (multicast). 240-255 is E.", "Treat 127 as loopback, not Class A."],
            "The first octet alone fixes the class.",
            "The IP address 196.20.5.1 belongs to which class?",
            ["The first octet is 196.", "196 lies between 192 and 223."], "Class C"),
        pat("nw-p2", "Private ranges and loopback", "very common",
            "Which is a private IP address, what is 127.0.0.1, or which address is reserved for testing or localhost.",
            ["Private: 10.x.x.x, 172.16 to 172.31.x.x, 192.168.x.x.", "Home routers use 192.168.x.x.",
             "127.0.0.1 is loopback (localhost).", "169.254.x.x appears when automatic addressing fails (APIPA)."],
            "Private and loopback ranges are reserved and never routed on the Internet.",
            "The address 127.0.0.1 is used for",
            ["127 is the reserved loopback block.", "The computer talks to itself."], "Loopback testing (localhost)"),
        pat("nw-p3", "IPv4 vs IPv6 facts", "common",
            "IPv4 has how many bits, IPv6 is written in what form, how many groups in an IPv6 address, or why IPv6 was needed.",
            ["IPv4: 32 bits, four decimal octets, about 4.3 billion addresses.", "IPv6: 128 bits, eight hexadecimal groups with colons.",
             "IPv6 was needed because IPv4 addresses ran out."],
            "More bits mean a far larger address space.",
            "An IPv6 address is how many bits long?",
            ["IPv6 has eight groups.", "Eight groups of 16 bits make 128 bits."], "128 bits"),
        pat("nw-p4", "MAC vs IP and usable-host counts", "common",
            "Difference between MAC and IP, how many hosts a Class C network can have, or which address changes when you move networks.",
            ["MAC: 48-bit, physical, permanent.", "IP: logical, assigned, changes with the network.",
             "Class C: 256 - 2 = 254 usable hosts.", "Class B: 65,534. Class A: 1,67,77,214."],
            "Two addresses in every network are reserved.",
            "How many usable host addresses does a Class C network provide?",
            ["Class C has 256 addresses.", "Take away the network and broadcast addresses: 254."], "254"),
        pat("nw-p5", "Default masks and special addresses", "occasional",
            "The default mask of a class, the broadcast address, or the unspecified address.",
            ["Class A: 255.0.0.0 (/8). Class B: 255.255.0.0 (/16).", "Class C: 255.255.255.0 (/24).",
             "0.0.0.0 is unspecified.", "255.255.255.255 is the broadcast address."],
            "The mask shows how many leading bits name the network.",
            "What is the default subnet mask of a Class B network?",
            ["Class B has a /16 prefix.", "Two full octets of 255."], "255.255.0.0"),
        pat("nw-p6", "DHCP and static addressing", "occasional",
            "Which protocol assigns IP addresses automatically, or how static addressing differs from it.",
            ["DHCP gives IP addresses automatically.", "Static addressing sets them by hand.",
             "DHCP uses ports 67 and 68."],
            "Automatic assignment saves manual setup.",
            "Which protocol assigns IP addresses automatically to devices?",
            ["Automatic assignment is the job of DHCP.", "Its full form is Dynamic Host Configuration Protocol."], "DHCP"),
    ],
)

# =====================================================================
# 5. Protocols and ports
# =====================================================================
SUBS["nw-protocols"] = dict(
    concept=(
        "The IP address finds the computer. The port number finds the service on it. "
        "Learn the main ports: HTTP 80, HTTPS 443, FTP 21, SSH 22, Telnet 23, SMTP 25, DNS 53, POP3 110, IMAP 143. "
        "TCP is reliable and connection-oriented. UDP is fast and connectionless."
    ),
    notes=r"""### Ports, numbered doors on a machine
The IP address finds the computer. The **port number** finds the service on it. Learn this classic set.

| Protocol | Port | Job |
|---|---|---|
| **HTTP** | **80** | web pages (plain) |
| **HTTPS** | **443** | web pages, encrypted with TLS/SSL |
| **FTP** | **21** (control), 20 (data) | file transfer |
| **SSH** | **22** | secure remote login |
| **Telnet** | **23** | remote login, not encrypted |
| **SMTP** | **25** | sending e-mail |
| **DNS** | **53** | name to IP resolution |
| **DHCP** | 67 / 68 | automatic IP assignment |
| **POP3** | **110** | receiving e-mail (download) |
| **IMAP** | **143** | receiving e-mail (sync) |
| **SNMP** | 161 | network management |
| **RDP** | 3389 | Windows remote desktop |

> **Tip:** 21, 22, 23 climb in order: FTP, SSH, Telnet. Then 25 is SMTP. 80 and 443 are the web pair. 110 and 143 bring mail in.

### TCP vs UDP
| | **TCP** | **UDP** |
|---|---|---|
| Full form | Transmission Control Protocol | User Datagram Protocol |
| Connection | connection-oriented (handshake first) | connectionless (just send) |
| Delivery | guaranteed and ordered | no guarantee |
| Speed | slower | faster, low overhead |
| Used by | web, e-mail, file transfer | DNS queries, DHCP, streaming, VoIP, gaming |

The TCP handshake has three steps: SYN, SYN-ACK, ACK.

> **Example:** Live cricket streaming uses UDP. One lost frame is better than a paused match.

### One web visit, step by step
1. **DNS** turns the name into an IP address.
2. **TCP** opens the connection.
3. **HTTPS** (port 443) asks for the page and delivers it encrypted.

For e-mail, SMTP sends. POP3 or IMAP receive.

### Reading a protocol question
Decide what the question asks. Then use the matching tool.

- **Direction:** send mail is SMTP. Receive mail is POP3 or IMAP.
- **Number:** recall the port anchors. If unsure, eliminate by neighbourhood.
- **Style:** reliable means TCP. Fast means UDP.
- **Full form:** spell it out from the name.

> **Tip:** For TCP or UDP, ask what a lost packet costs. A corrupted file is bad, so use TCP. One blurred video frame is fine, so use UDP.

### Full forms to memorise
- HTTP: HyperText Transfer Protocol. HTTPS: secure HTTP over TLS/SSL.
- FTP: File Transfer Protocol. SMTP: Simple Mail Transfer Protocol.
- POP: Post Office Protocol. IMAP: Internet Message Access Protocol.
- DNS: Domain Name System. DHCP: Dynamic Host Configuration Protocol. SSH: Secure Shell.

> **Watch:** Telnet sends everything in plain text. SSH (22) is the encrypted replacement.
""",
    tricks=[
        trick("Port anchors",
              "Memorise six first: 80 HTTP, 443 HTTPS, 25 SMTP, 53 DNS, 110 POP3, 21 FTP. Then 22 SSH and 23 Telnet. Telnet is the insecure one.",
              "What is the default port of HTTPS?",
              ["HTTPS is the secure web protocol.", "Its port is 443."], "443"),
        trick("TCP tracks, UDP does not",
              "TCP tracks every packet, so it is reliable but slower. UDP is unreliable but quick. 'Guaranteed delivery' in a question means TCP.",
              "Live cricket video streaming mainly uses which protocol?",
              ["Speed matters more than perfect delivery.", "Retransmission would pause the match."], "UDP"),
    ],
    mistakes=[
        mis("Giving HTTP the port 443.", "443 is HTTPS. Plain HTTP is 80."),
        mis("Choosing TCP for live streaming.", "The expected answer is UDP, because speed comes first."),
        mis("Saying Telnet is secure.", "SSH (22) is encrypted. Telnet (23) sends plain text."),
        mis("Using SMTP to receive mail.", "SMTP sends mail. POP3 and IMAP receive it."),
    ],
    revision=[
        "HTTP 80, HTTPS 443, FTP 21, SSH 22, Telnet 23, SMTP 25, DNS 53, POP3 110, IMAP 143.",
        "TCP is reliable and connection-oriented (web, mail, FTP). UDP is fast and connectionless (streaming, games, VoIP).",
        "Telnet is plain text. SSH (22) is its encrypted replacement.",
        "HTTPS is HTTP plus TLS/SSL encryption.",
        "SMTP sends mail. POP3 and IMAP receive mail.",
        "DNS resolves names to IP addresses. DHCP assigns IP addresses.",
    ],
    patterns=[
        pat("nw-r1", "Port-number matching", "very common",
            "HTTPS works on which port, the port of SMTP, FTP, DNS or POP3, or a matched pair with one number shifted.",
            ["Recall the anchors: HTTP 80, HTTPS 443, FTP 21, SSH 22, Telnet 23, SMTP 25, DNS 53, POP3 110, IMAP 143.",
             "Watch for 443 given to HTTP or 80 given to HTTPS.", "Use the climbing run 21, 22, 23.", "Eliminate by neighbourhood if unsure."],
            "Port numbers are fixed facts, so anchors beat guessing.",
            "HTTPS uses which port number by default?",
            ["HTTPS is secure web traffic.", "The port is 443. Plain HTTP uses 80."], "443"),
        pat("nw-r2", "TCP vs UDP selection", "very common",
            "Which protocol is used for live streaming or file transfer, which is connection-oriented, or reliability-versus-speed statements.",
            ["Ask what a lost packet would cost.", "A corrupted file is costly: TCP.",
             "One blurred frame is fine: UDP.", "Live streaming, gaming, VoIP, DNS queries: UDP."],
            "Reliability needs TCP. Speed needs UDP.",
            "Which transport protocol suits a live cricket stream?",
            ["Speed matters more than perfect delivery.", "TCP retransmission would only pause the match."], "UDP"),
        pat("nw-r3", "Protocol purpose identification", "common",
            "Which protocol transfers files, sends e-mail or resolves names. It is purpose matching.",
            ["File transfer: FTP. Send mail: SMTP.", "Receive mail: POP3 or IMAP. Web pages: HTTP or HTTPS.",
             "Names to IPs: DNS. Remote login: Telnet (plain) or SSH (secure).", "DHCP assigns IP addresses."],
            "Each protocol was built for one purpose.",
            "Which protocol is used to transfer files between computers?",
            ["File transfer is the purpose.", "FTP uses port 21 for control and 20 for data."], "FTP (File Transfer Protocol)"),
        pat("nw-r4", "Protocol full forms and security", "common",
            "Full form of FTP, TCP, UDP or DHCP, which remote-login protocol is secure, or Telnet-versus-SSH statements.",
            ["Spell out the full form from the name.", "Telnet (23) sends plain text.",
             "SSH (22) is the encrypted replacement.", "HTTPS is HTTP over TLS/SSL."],
            "The S in SSH and HTTPS means secure.",
            "Which protocol provides an encrypted remote login?",
            ["Telnet on port 23 sends passwords as plain text.", "SSH is the encrypted one."], "SSH (Secure Shell), port 22"),
        pat("nw-r5", "Mail protocol direction", "common",
            "Which protocol sends mail, which downloads it, or which keeps mail in sync across devices.",
            ["Sending: SMTP (port 25).", "Downloading: POP3 (port 110).", "Syncing: IMAP (port 143).", "All three run over TCP."],
            "Sending and receiving use different protocols.",
            "Which protocol is used to send e-mail?",
            ["Sending is the direction asked.", "SMTP is the sender; POP3 and IMAP receive."], "SMTP (port 25)"),
        pat("nw-r6", "Less common ports and services", "occasional",
            "Ports 67/68, 161 or 3389, or which service uses them.",
            ["DHCP uses 67 and 68.", "SNMP (network management) uses 161.", "RDP (Windows remote desktop) uses 3389.", "FTP data port is 20."],
            "These ports appear less often but are fixed facts.",
            "Windows Remote Desktop uses which port?",
            ["RDP means Remote Desktop Protocol.", "Its port is 3389."], "3389"),
    ],
)


# ---------------------------------------------------------------------
def long_lines(text, limit=24):
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
