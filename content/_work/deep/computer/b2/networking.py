"""Phase-2 deep content for computer/networking. Run: py -3 networking.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from nw_pats import (build_types_topologies, build_devices, build_osi, build_ip,
                     build_protocols)
import nw_qs


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Device identification by job", "very common",
      "'Which device sends data to all ports', 'which device connects two different networks', 'which device regenerates a weak signal' — a behaviour is described and the device named.",
      "Climb the ladder: hub = broadcasts to every port (Layer 1); switch = learns MAC addresses, sends only to the right port (Layer 2); router = joins different networks and routes by IP (Layer 3); repeater = regenerates signals; modem = modulator-demodulator; gateway = protocol converter. Match the verb in the question to the one-line job.",
      "nw-devices",
      "Which device forwards a data packet towards the correct network using IP addresses?",
      "Router — it works on Layer 3, reading IP addresses and choosing the best path between networks."),
    P("OSI layer count, order and functions", "very common",
      "'How many layers in the OSI model', 'routing/encryption/framing is a ___ layer function', 'a router/switch works at which layer', correct-order statements.",
      "Fix the map: 7 layers — Physical (bits), Data Link (frames, MAC), Network (IP, routing), Transport (TCP/UDP, ports), Session (dialogues), Presentation (translation, encryption, compression), Application (HTTP, FTP, SMTP). Devices: hub 1, switch 2, router 3. The planted traps: encryption at Application, routing at Transport.",
      "nw-osi",
      "In the OSI model, routing of packets is the function of which layer?",
      "Network (Layer 3) — IP addressing and route selection; Transport (4) only delivers end to end."),
    P("IP class identification", "very common",
      "An address is printed (10.0.0.5, 130.10.5.2, 196.1.2.3, 225.1.1.1) and its class asked; or the first-octet range of a class; or 'which is a private address'; 'what is 127.0.0.1'.",
      "Read the FIRST octet only against the ruler 1(A) - 128(B) - 192(C) - 224(D) - 240(E); 127 = loopback. Private ranges: 10.x.x.x, 172.16-31.x.x, 192.168.x.x. Multicast = Class D. One octet decides everything — do not read the second number.",
      "nw-ip",
      "The IP address 130.10.5.2 belongs to which class?",
      "Class B — the first octet 130 lies between 128 and 191."),
    P("Port-number matching", "very common",
      "'HTTPS works on which port', 'SMTP port', 'FTP uses which ports', or a matched pair where one number is shifted.",
      "Anchors: HTTP 80, HTTPS 443, FTP 21 (data 20), SSH 22, Telnet 23, SMTP 25, DNS 53, POP3 110, IMAP 143. The classic trap swaps 80 and 443, or pairs POP3 with 143 (that is IMAP). Climb 21-22-23 for FTP-SSH-Telnet.",
      "nw-protocols",
      "Data transfer of the World Wide Web over an encrypted connection uses which default port?",
      "443 — HTTPS; plain HTTP uses port 80."),
    P("TCP vs UDP selection", "very common",
      "'Which protocol for live streaming / file download', 'which is connection-oriented', statements about reliability and speed.",
      "TCP = connection-oriented, reliable, ordered — web pages, e-mail, file transfer. UDP = connectionless, fast, no guarantee — live streaming, gaming, VoIP, DNS queries. The recurring answer: live video = UDP; downloading a file = TCP.",
      "nw-protocols",
      "Which protocol would a live video streaming service prefer?",
      "UDP — speed matters more than perfect delivery; TCP's retransmissions would only pause the stream."),
    P("Topology identification", "common",
      "'Every computer connected to a central hub', 'every node connected to every other node', 'all computers share a single backbone' — the layout described and the topology asked.",
      "Central device with all nodes = Star; every node to every other = Mesh; one shared backbone with terminators = Bus; circle of neighbours = Ring; stars joined on a backbone = Tree. Also know failure points: star dies with its hub, bus dies with its backbone, mesh is the most reliable.",
      "nw-types-topologies",
      "In which topology does every node have a direct link to every other node?",
      "Mesh — the most reliable topology, needing n(n-1)/2 links."),
    P("Mesh link count (numeric)", "occasional",
      "'How many links are required for a mesh of 5/6/8 computers' — pure arithmetic.",
      "links = n x (n-1) / 2. For n = 4 give 6; n = 5 give 10; n = 6 give 15; n = 8 give 28. The trap option is n squared or the unhalved n(n-1).",
      "nw-types-topologies",
      "How many cable links are needed for a full mesh of 6 computers?",
      "6 x 5 / 2 = 15 links."),
]

if __name__ == "__main__":
    subs = []
    for build, add in ((build_types_topologies, nw_qs.add_types_topologies),
                       (build_devices, nw_qs.add_devices),
                       (build_osi, nw_qs.add_osi),
                       (build_ip, nw_qs.add_ip),
                       (build_protocols, nw_qs.add_protocols)):
        S = build()
        add(S)
        subs.append(S)
    apply_topic("networking", subs, PYQ)
