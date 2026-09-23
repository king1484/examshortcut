# -*- coding: utf-8 -*-
"""Topic 9: cyber-security"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

T = {
  "id": "cyber-security",
  "sectionId": "computer",
  "title": "Cyber Security",
  "order": 9,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 2},
  "summary": "Malware families (virus, worm, trojan, ransomware), social-engineering attacks (phishing and cousins), preventive measures, and IT Act 2000 sections with CERT-In. Statement-based malware questions appear in nearly every CKT shift.",
  "subtopics": [
    {
      "id": "cs-malware",
      "title": "Malware types",
      "concept": """**Malware** = malicious software. The family table:

| Malware | Behaviour | Spread |
|---|---|---|
| Virus | Attaches itself to a host file/program; corrupts data | Only when the infected file is run/shared |
| Worm | **Self-replicates across networks without any host file or user action** | Automatically over the network |
| Trojan (horse) | **Disguises as useful software**; opens backdoors, steals data | Does NOT self-replicate; user installs it |
| Ransomware | Encrypts the victim's files and demands ransom (WannaCry, 2017) | Mail attachments, exploits |
| Spyware | Secretly collects user activity/data | Bundled installs, drive-by |
| Keylogger | Records every keystroke (passwords, OTPs) | Often part of spyware/trojans |
| Adware | Forces unwanted advertisements | Freeware bundles |
| Rootkit | Hides deep in the OS with admin rights, concealing other malware | Exploits |
| Botnet | Network of infected 'zombie' machines under a attacker's control (used for DDoS/spam) | Worm/trojan infection |
| Logic bomb | Dormant code that fires on a trigger (date, event) | Planted insider/trojan |

WannaCry (2017) - global ransomware outbreak hitting unpatched Windows via the EternalBlue exploit - is the stock example question.""",
      "formulas": [],
      "tricks": [
        {"title": "V-W-T triangle", "body": "**Virus needs a Vehicle (host file); Worm Wanders alone; Trojan Tricks you into installing.** Replication + host = virus; replication without host = worm; disguise without replication = trojan.", "example": {"q": "Which malware self-replicates without needing a host file?", "solution": "Worm."}},
        {"title": "Ransom = Ransomware", "body": "Encrypts your files, demands money -> ransomware (WannaCry). 'Keystrokes recorded' -> keylogger. 'Hides with admin rights' -> rootkit. 'Zombie army' -> botnet.", "example": {"q": "WannaCry (2017) was an example of?", "solution": "Ransomware."}}
      ],
      "mistakes": [
        "Saying a trojan self-replicates - only viruses and worms replicate; a trojan relies on disguise.",
        "Saying a worm needs a host file - the worm is host-free by definition.",
        "Calling ransomware a 'data thief' - its business model is encryption + extortion."
      ]
    },
    {
      "id": "cs-attacks",
      "title": "Cyber attacks and social engineering",
      "concept": """| Attack | How it works |
|---|---|
| Phishing | Fake e-mail/site mimicking a bank or service to harvest credentials |
| Spear phishing | Phishing targeted at one person/organisation |
| Vishing / Smishing | Phishing by **V**oice calls / **SM**S |
| Pharming | Redirects users to fake sites by **poisoning DNS/host files - no click needed** |
| DoS / DDoS | Flooding a server with traffic; DDoS = Distributed, from a botnet of many machines |
| Man-in-the-Middle (MITM) | Attacker secretly intercepts/relays communication between two parties (open Wi-Fi sniffing) |
| SQL Injection | Malicious SQL typed into input fields to manipulate the database |
| Brute force / Dictionary | Trying every possible password / a wordlist of likely passwords |
| Social engineering | Manipulating humans (urgency, authority) - the 'human hacking' umbrella |
| Spoofing | Faking an identity: e-mail, IP, caller ID, website |
| Sniffing/Eavesdropping | Passive capture of network traffic |
| Identity theft | Stealing personal data to impersonate (Sec 66C IT Act) |
| Website defacement | Replacing a site's content (electronic vandalism) |
| Salami attack | Stealing tiny amounts (rounding offs) that accumulate large |
| Zero-day | Attack through a vulnerability the vendor has not yet patched |""",
      "formulas": [],
      "tricks": [
        {"title": "The -ishing family", "body": "**Phi**shing = fake mail/site; **Vi**shing = Voice; **SMi**shing = SMS; **Phar**ming = fake site with NO click (DNS poisoned). If the victim 'entered a real-looking site without clicking any link', think pharming.", "example": {"q": "A fake banking site reached via a corrupted DNS entry is?", "solution": "Pharming."}},
        {"title": "MITM = postman reading letters", "body": "Man-in-the-Middle: both parties think they talk to each other; the attacker relays (and reads/edits) everything - classic on open Wi-Fi. Pure listening without relaying = sniffing.", "example": {"q": "Attacker secretly relaying messages between a user and the bank is?", "solution": "Man-in-the-Middle attack."}}
      ],
      "mistakes": [
        "Confusing pharming with phishing - pharming needs no victim click; DNS is poisoned.",
        "Calling DDoS a single-machine attack - the D means distributed (botnet).",
        "Believing strong passwords alone stop phishing - awareness + 2FA are needed; no password resists a fake site."
      ]
    },
    {
      "id": "cs-prevention",
      "title": "Preventive measures and security tools",
      "concept": """| Measure | What it does |
|---|---|
| Antivirus/anti-malware | Scans, detects, quarantines malware (Windows Defender - built-in; Norton, McAfee, Kaspersky, Quick Heal, Avast) - needs regular virus-definition updates |
| Firewall | Monitors incoming/outgoing traffic against allow/deny rules; hardware or software |
| Updates/patches | Close known vulnerabilities (WannaCry spread through unpatched systems) |
| Strong passwords | Long, mixed-case + digits + symbols, unique per site; avoid names/DOB; passphrase style |
| 2FA/MFA + OTP | A second factor beyond the password |
| Backups | Regular offline/off-site copies defeat ransomware |
| Encryption | Renders stolen data unreadable; HTTPS for web |
| VPN | Encrypted tunnel on public Wi-Fi |
| Digital signature | Verifies sender authenticity + message integrity (issued via Certifying Authorities) |
| Biometrics | Fingerprint/face/iris authentication |
| CAPTCHA | Human-vs-bot test on forms |
| Safe habits | Don't click unknown links/attachments; scan USB drives; avoid pirated software; log out; lock screen (Win+L) |

Antivirus is reactive/detective; a **firewall is preventive/gatekeeping** - exam options often swap their roles.""",
      "formulas": [],
      "tricks": [
        {"title": "AV detects, FW decides", "body": "**Antivirus = detective** (scans files for malware already arriving); **Firewall = gatekeeper** (allows/blocks traffic by rules). 'Filters network traffic' -> firewall; 'removes virus from a file' -> antivirus.", "example": {"q": "Which tool filters network traffic based on defined rules?", "solution": "Firewall."}},
        {"title": "2FA two doors", "body": "Two-factor = knowledge (password) + possession/inherence (OTP, token, fingerprint). One stolen password opens only the first door.", "example": {"q": "Password + OTP at login is an example of?", "solution": "Two-factor authentication."}}
      ],
      "mistakes": [
        "Treating antivirus as the network gatekeeper - that is the firewall's role.",
        "Thinking updated antivirus alone guarantees safety - zero-days and phishing bypass it.",
        "Writing passwords on sticky notes or reusing one password everywhere - both kill the 'strong password' measure."
      ]
    },
    {
      "id": "cs-it-act",
      "title": "IT Act 2000, offences and authorities",
      "concept": """The **Information Technology Act, 2000** is India's cyber-law framework - passed in 2000, **in force from 17 October 2000**, based on the UNCITRAL model law on e-commerce, and **amended in 2008** (adding 66C, 66D, 66F etc.).

| Section | Offence |
|---|---|
| Sec 43 | Penalty (up to Rs. 1 crore) for unauthorised access/damage to computer, data, virus injection |
| Sec 65 | Tampering with computer **source documents** - up to 3 years |
| Sec 66 | Computer-related offences (dishonesty/franchise of Sec 43 acts) |
| Sec 66C | **Identity theft** - up to 3 years + fine |
| Sec 66D | **Cheating by personation** using a computer (online fraud) - up to 3 years |
| Sec 66E | Violation of privacy (publishing private images) - up to 3 years |
| Sec 66F | **Cyber terrorism** - may extend to life imprisonment |
| Sec 67 | Publishing/transmitting obscene material electronically (first conviction up to 3 years + Rs. 5 lakh fine) |
| Sec 72 | Breach of confidentiality and privacy by a empowered body |

Note: **Sec 66A** (punishing 'offensive messages') was struck down by the Supreme Court in *Shreya Singhal v. Union of India* (2015) as unconstitutional.

**Authorities/portals:** **CERT-In** (Indian Computer Emergency Response Team, 2004, under MeitY) - the national incident-response and warning body; **NCIIPC** protects critical information infrastructure; **cybercrime.gov.in** is the national reporting portal and **1930** the cyber-fraud helpline (freezing defrauded money quickly).""",
      "formulas": [],
      "tricks": [
        {"title": "Section story-line", "body": "**43** = damage fine, **65** = source code, **66** = computer crime, **66C** = identity (C for Credential theft), **66D** = cheating by personation (D for Donning a false identity), **66F** = terrorism (F for Fearsome), **67** = obscene.", "example": {"q": "Under which IT Act section is identity theft punished?", "solution": "Section 66C."}},
        {"title": "2000-17-10", "body": "IT Act passed and effective in **2000** (in force 17 October 2000), UNCITRAL-based, amended **2008**. CERT-In follows in **2004**.", "example": {"q": "The IT Act came into force in the year?", "solution": "2000."}},
        {"title": "Helpline 1930", "body": "Money lost to online fraud? Dial **1930** fast and report at cybercrime.gov.in - the hotline aims to freeze the siphoned money in the banking chain.", "example": {"q": "National cybercrime reporting helpline number?", "solution": "1930."}}
      ],
      "mistakes": [
        "Saying the IT Act was enacted in 2008 - 2008 is the AMENDMENT; the Act is 2000.",
        "Quoting Sec 66A as current law - it was struck down in 2015 (Shreya Singhal case).",
        "Mixing CERT-In (incident response, MeitY) with NCIIPC (critical-infrastructure protection)."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Malware identification", "frequency": "very common", "howToSpot": "'Which program disguises as useful software?' / statement-based 'which are true about a worm?'.", "approach": "Replicates + host file = virus; replicates alone = worm; disguise, no replication = trojan; encrypts for money = ransomware; records keys = keylogger."},
    {"pattern": "Phishing-family matching", "frequency": "common", "howToSpot": "'Fraud call asking for OTP' / 'fake website via DNS poisoning'.", "approach": "Mail/site = phishing; voice = vishing; SMS = smishing; no-click DNS redirect = pharming; targeted mail = spear phishing."},
    {"pattern": "Preventive-measure odd-one-out", "frequency": "common", "howToSpot": "'Which is NOT a security measure?' or matching tool-to-role (firewall vs antivirus).", "approach": "Firewall filters traffic by rules; antivirus detects/removes malware; updates patch holes; 2FA adds a second factor."},
    {"pattern": "IT Act sections/authorities", "frequency": "common", "howToSpot": "'Identity theft is punished under?' / 'CERT-In stands for?'.", "approach": "Drill the section table (43/65/66/66C/66D/66F/67) and pair CERT-In with incident response, 1930 with fraud reporting."},
    {"pattern": "Attack-mechanism statements", "frequency": "occasional", "howToSpot": "Two-statement questions on DDoS, MITM or SQL injection.", "approach": "DDoS = many sources flooding; MITM = secret relay; SQLi = input fields touching the database; brute force = every combination."}
  ],
  "solvedExamples": [
    Q("cs-se01",
      "Which of the following statements is correct?",
      ["A trojan horse replicates itself rapidly across networks", "A worm needs a host file to attach itself to", "A virus attaches to a host program and spreads when it is executed", "Ransomware deletes files permanently without any demand"], 2,
      "A virus lives inside a host file/program and activates on execution. Trojans do not self-replicate, worms need no host file, and ransomware encrypts files to demand ransom rather than simply deleting them.",
      "The V-W-T triangle: Virus-vehicle, Worm-wanders, Trojan-tricks. Match each option's verb against it.",
      "medium", "cs-malware", "malware statement analysis", 45),
    Q("cs-se02",
      "A fraudster phones a user pretending to be a bank officer and asks for the OTP. This is an example of:",
      ["Phishing", "Vishing", "Smishing", "Pharming"], 1,
      "Voice-based fraud calls are vishing (voice phishing). Phishing uses fake e-mails/sites, smishing uses SMS, and pharming redirects browsers without any call or click.",
      "Voice on the line = vishing. SMS = smishing. E-mail/site = phishing.",
      "easy", "cs-attacks", "attack-type identification", 35),
    Q("cs-se03",
      "Which section of the IT Act 2000 (post-2008 amendment) specifically deals with identity theft?",
      ["Sec 65", "Sec 66C", "Sec 67", "Sec 72"], 1,
      "Section 66C punishes identity theft - fraudulent use of another person's password, digital signature or unique identification feature.",
      "66C = Credential/identity theft; 65 = source code; 67 = obscene content.",
      "medium", "cs-it-act", "IT Act sections", 40),
    Q("cs-se04",
      "The primary role of CERT-In is to:",
      ["Sell antivirus licences", "Act as the national incident-response team for cyber security threats", "Issue Aadhaar numbers", "Regulate telecom tariffs"], 1,
      "CERT-In (Indian Computer Emergency Response Team, set up 2004 under MeitY) handles cyber-incident reporting, response, alerts and vulnerability management for India.",
      "CERT = Computer Emergency Response Team - the name itself says incident response.",
      "easy", "cs-it-act", "cyber authorities", 35)
  ],
  "practice": [
    Q("cs-q01",
      "Which malicious program can self-replicate across a network WITHOUT needing a host file or user action?",
      ["Virus", "Worm", "Trojan horse", "Adware"], 1,
      "Worms travel and multiply on their own over network connections. Viruses need a host file, trojans need a user to install them and never self-replicate.",
      "Worm = Wanders alone. If 'no host file / no user action' appears, it is a worm.",
      "easy", "cs-malware", "malware identification", 30),
    Q("cs-q02",
      "A program that appears to be a free game but silently opens a backdoor for attackers is a:",
      ["Worm", "Trojan horse", "Rootkit", "Cookie"], 1,
      "The trojan's essence is disguise: useful-looking software that performs hidden malicious actions (backdoors, data theft). It does not self-replicate.",
      "Looks useful, works evil = trojan horse.",
      "easy", "cs-malware", "malware identification", 30),
    Q("cs-q03",
      "WannaCry, the global outbreak of May 2017 that encrypted systems and demanded bitcoin payments, was:",
      ["Adware", ["Spyware"][0], "Ransomware", "A logic bomb"], 2,
      "WannaCry was ransomware - it encrypted victims' files and demanded ransom (in bitcoin), spreading via the EternalBlue exploit against unpatched Windows.",
      "Encrypt + demand money = ransomware; WannaCry is the stock example.",
      "easy", "cs-malware", "malware examples", 30),
    Q("cs-q04",
      "A hardware or software component that records every key pressed on a keyboard to steal passwords is called a:",
      ["Keylogger", "Sniffer", "Spammer", "Cracker"], 0,
      "Keyloggers capture keystrokes (often as spyware/trojan payloads), exposing passwords and OTPs. A sniffer passively captures network packets instead.",
      "Key-strokes recorded = keylogger; network packets read = sniffer.",
      "easy", "cs-malware", "malware identification", 30),
    Q("cs-q05",
      "Sending e-mails that imitate a legitimate bank to trick users into revealing passwords is:",
      ["Phishing", "Pharming", "Spamming", "Defacement"], 0,
      "Phishing uses counterfeit messages/sites to 'fish' for credentials. Pharming needs no lure - DNS is poisoned so even correct URLs land on fake sites. Spamming is bulk unsolicited mail; defacement vandalises pages.",
      "Fake mail asking for credentials = phishing, the umbrella term.",
      "easy", "cs-attacks", "attack-type identification", 30),
    Q("cs-q06",
      "In which attack is a user redirected to a fake website purely by corrupting DNS records, without clicking any link?",
      ["Spear phishing", "Pharming", "Vishing", "Salami attack"], 1,
      "Pharming poisons the DNS/host entries so the genuine-looking domain resolves to the attacker's server - the user need do nothing wrong.",
      "No click + fake site = pharming (phishing needs the victim's click).",
      "medium", "cs-attacks", "attack-type identification", 40),
    Q("cs-q07",
      "A Distributed Denial of Service (DDoS) attack works by:",
      ["Encrypting the victim's hard disk", "Flooding a target server with traffic from many compromised machines", "Stealing the administrator's password", "Injecting SQL into a form"], 1,
      "A botnet of 'zombie' systems swamps the target with requests so genuine users cannot be served. Nothing is encrypted (ransomware) or stolen directly - availability alone is attacked.",
      "DDoS = Distributed (many machines) + Denial (availability lost).",
      "medium", "cs-attacks", "attack mechanics", 40),
    Q("cs-q08",
      "An attacker who secretly relays and possibly alters communication between a user and a banking site is performing a:",
      ["Brute force attack", "Man-in-the-Middle attack", "Salami attack", "Logic bomb"], 1,
      "In MITM the attacker sits between the two endpoints, intercepting/relaying traffic - a classic danger of unencrypted links and open Wi-Fi.",
      "Secretly standing between two parties = man-in-the-middle.",
      "medium", "cs-attacks", "attack mechanics", 40),
    Q("cs-q09",
      "Entering a single quote followed by SQL code into a login form to manipulate the database is:",
      ["SQL injection", "Cross-site scripting", "Dictionary attack", "Spoofing"], 0,
      "SQL injection feeds crafted SQL through input fields so the database executes attacker logic - usually a symptom of unvalidated input.",
      "Database + input field = SQL injection.",
      "medium", "cs-attacks", "attack mechanics", 40),
    Q("cs-q10",
      "Trying every possible character combination to guess a password is a:",
      ["Dictionary attack", "Brute force attack", "Phishing attack", "Social engineering"], 1,
      "Brute force exhausts all combinations; a dictionary attack tries only likely words from a list. Phishing and social engineering target people, not the algorithm.",
      "Every combination = brute force; wordlist only = dictionary.",
      "easy", "cs-attacks", "attack mechanics", 30),
    Q("cs-q11",
      "Which of the following is primarily a PREVENTIVE network security tool that allows or blocks traffic based on defined rules?",
      ["Antivirus", "Firewall", "Disk defragmenter", "Chatbot"], 1,
      "A firewall inspects incoming/outgoing traffic against allow/deny rules and blocks unauthorised connections. Antivirus reacts to malware found in files.",
      "Rule-based gatekeeper = firewall.",
      "easy", "cs-prevention", "security tools", 30),
    Q("cs-q12",
      "Requiring a password plus an OTP sent to the registered mobile is an example of:",
      ["Single sign-on", "Two-factor authentication", "Digital watermarking", "Encryption"], 1,
      "Two-factor authentication combines two different evidence types - something you know (password) and something you receive (OTP). A leaked password alone then cannot breach the account.",
      "Two different proofs = 2FA.",
      "easy", "cs-prevention", "security practices", 30),
    Q("cs-q13",
      "The Information Technology Act, which governs cyber activities in India, came into force in:",
      ["1998", "2000", "2005", "2008"], 1,
      "The IT Act was passed in 2000 (in force from 17 October 2000), based on the UNCITRAL model law; the 2008 amendment added identity theft (66C) and cyber terrorism (66F) provisions.",
      "Act = 2000; amendment = 2008.",
      "easy", "cs-it-act", "IT Act basics", 30),
    Q("cs-q14",
      "Under the IT Act, cyber terrorism is dealt with in:",
      ["Section 66C", "Section 66D", "Section 66F", "Section 67"], 2,
      "Section 66F covers cyber terrorism - acts threatening India's sovereignty, integrity or security through computers - punishable with imprisonment that may extend to life.",
      "66F = Fearsome (terrorism); 66C identity, 66D personation-cheating.",
      "medium", "cs-it-act", "IT Act sections", 40),
    Q("cs-q15",
      "The national helpline number for reporting online financial fraud in India is:",
      ["181", "1098", "1930", "100"], 2,
      "1930 is the cybercrime financial-fraud helpline (paired with the cybercrime.gov.in portal) for fast freezing of defrauded money. 181 is the women's helpline, 1098 childline, 100 police.",
      "Money gone online? Dial 1930 immediately.",
      "medium", "cs-it-act", "cyber reporting", 35)
  ]
}

validate_and_dump_topic(T)
