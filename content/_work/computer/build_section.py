# -*- coding: utf-8 -*-
"""Section index: computer"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import _dump, OUT_SECTION, TOPIC_IDS

S = {
  "id": "computer",
  "name": "Computer Knowledge",
  "short": "Computer",
  "tier1": {"questions": 0, "marks": 0},
  "tier2": {"questions": 20, "marks": 60},
  "overview": """Computer Knowledge appears **only in Tier 2**. It is **Section III (Module I) of Paper I**, the Computer Knowledge Test (CKT): **20 questions x 3 marks = 60 marks in 15 minutes** (20 minutes for candidates allowed a scribe). It runs in Session I straight after Section II (Reasoning + GA).

| Item | Detail |
|---|---|
| Questions / marks | 20 / 60 (3 marks each) |
| Time | 15 minutes |
| Negative marking | **1 mark per wrong answer** (same as Sections I and II) |
| Nature | Mandatory but **qualifying** - marks do NOT count towards merit |
| Minimum to qualify | UR 30%, OBC/EWS 25%, all others 20% (18, 15 and 12 of 60 marks) |
| Merit | Decided by Sections I and II of Paper I only |

**Higher bar for some posts:** where Computer Proficiency is an essential qualification, a higher CKT qualifying standard is applied. These posts include ASO (CSS/MEA/AFHQ), Assistant SFIO, Assistant in GSI and IMD, Inspector (CGST/Central Excise), Preventive Officer, Examiner, Executive Assistant (CBIC) and Postal/Sorting Assistant. Treat 30% as the floor, not the target.

**Official syllabus (four blocks):**
1. **Computer basics** - organisation of a computer, CPU, input/output devices, computer memory, memory organisation, back-up devices, ports, Windows Explorer, keyboard shortcuts.
2. **Software** - Windows operating system, basics of MS Word, MS Excel and PowerPoint.
3. **Working with the Internet and e-mail** - web browsing and searching, downloading and uploading, managing an e-mail account, e-banking.
4. **Networking and cyber security** - networking devices and protocols, network and information security threats (hacking, virus, worms, Trojans etc.) and preventive measures.

Recent papers are almost entirely **direct factual recall**: shortcut keys (hyperlink, bookmark, Excel date), full forms, which generation used which technology, device and protocol identification, and statements about malware. Office questions, especially MS Word, form the largest block.""",
  "strategy": """## The one-line plan

**Qualify with a wide margin, then stop.** CKT marks do not enter the merit list, but failing it cancels your whole Tier 2. Aim for **45+ of 60** so that the higher Computer Proficiency bar for ASO, Inspector and Postal Assistant posts is never a risk.

## Priority order (maximum return first)

1. **Keyboard shortcuts** - 2-4 questions per paper, pure memory. Learn the Windows, Word, Excel, PowerPoint, browser and F1-F12 tables.
2. **MS Word, MS Excel, MS PowerPoint** - the largest block. Cover extensions, tabs and features, Excel functions and cell references, error values, and views and transitions.
3. **Computer fundamentals + hardware and memory** - generations, CPU units, input/output devices, memory hierarchy and units, ports, and number-system conversions (practise these until they take 30 seconds).
4. **Internet and e-mail** - protocols, CC/BCC, URL parts, browsers vs search engines, e-banking (NEFT/RTGS/IMPS/UPI).
5. **Networking** - LAN/MAN/WAN, topologies, devices by OSI layer, IP classes, port numbers.
6. **Cyber security** - malware types, attack names (phishing, vishing, pharming, DDoS), preventive tools, key IT Act sections.
7. **Software and OS** - system vs application vs utility software, OS functions, booting, file systems.

## Time plan inside the 15 minutes

- **First pass (about 8 minutes):** answer every question you know instantly (about 25 seconds each).
- **Second pass (about 5 minutes):** return to questions where you can confidently rule out two options, and work the number conversions.
- **Last 2 minutes:** review marked answers. Do not guess blindly.

## Attempt strategy

- With **1 negative mark against 3 positive**, a pure guess from four options has an expected value of zero (0.25 x 3 - 0.75 x 1). Guess only after ruling out at least one option; ruling out two makes it clearly worthwhile.
- 15 sure answers (45 marks) clear every qualifying standard comfortably, so accuracy matters more than attempts.
- Read the application named in the question. Ctrl+D, Shift+F3, F5 and Ctrl+H mean different things in Word, Excel, PowerPoint and browsers.

## Six-week preparation plan (alongside the main sections)

| Week | Focus |
|---|---|
| 1 | Fundamentals, generations, CPU, hardware and memory, number systems |
| 2 | Windows and OS, software types, keyboard shortcuts (Windows + function keys) |
| 3 | MS Word + Word shortcuts |
| 4 | MS Excel + PowerPoint + their shortcuts |
| 5 | Internet, e-mail, e-banking, networking |
| 6 | Cyber security + two full CKT mocks per week and shortcut revision |

Spend 20 minutes a day on this section. That is enough to qualify, and it leaves the rest of your time for the merit sections.""",
  "topics": list(TOPIC_IDS)
}

assert S["topics"] == ["computer-fundamentals", "hardware-memory", "software-os", "ms-word",
                       "ms-excel", "ms-powerpoint", "internet-email", "networking",
                       "cyber-security", "keyboard-shortcuts"]
for t in S["topics"]:
    assert os.path.exists(os.path.join(OUT_SECTION, "..", "topics", "computer", t + ".json")), t
# expected value of a blind guess: 0.25*3 - 0.75*1 == 0
assert abs(0.25 * 3 - 0.75 * 1) < 1e-12
assert [round(60 * p) for p in (0.30, 0.25, 0.20)] == [18, 15, 12]
_dump(S, os.path.join(OUT_SECTION, "computer.json"))
