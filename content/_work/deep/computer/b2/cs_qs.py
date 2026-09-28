"""Cyber security practice questions."""


def add_malware(S):
    S.q("cs-m1", "easy", "A program that attaches itself to a file and spreads when the file is shared and run is a —",
        ["Virus", "Firewall", "Compiler", "Browser"], "Virus",
        "**Virus** = needs a host file and a run to spread.",
        "Virus rides a host.", 20)
    S.q("cs-m1", "medium", "Which malware can spread by itself across a network WITHOUT needing a host file?",
        ["Worm", "Virus", "Trojan horse", "Adware"], "Worm",
        "**Worm** self-replicates standalone — no host, no user click needed.",
        "Worm crawls alone.", 25)
    S.q("cs-m1", "medium", "A 'free' PDF-reader downloaded from an unknown site secretly opens a backdoor for hackers. It does not copy itself. This is a —",
        ["Trojan horse", "Worm", "Virus", "Rootkit"], "Trojan horse",
        "**Trojan** — disguised as useful software and never self-replicates; the backdoor is its payload.",
        "Gift horse with soldiers inside.", 25)
    S.q("cs-m1", "hard", "Which statement is TRUE?",
        ["A virus needs a host file; a worm does not",
         "A worm needs a host file; a virus does not",
         "Both always need host files",
         "A trojan horse replicates fastest"],
        "A virus needs a host file; a worm does not",
        "The classic distinction: **virus = host-dependent; worm = independent**; trojan never replicates at all.",
        "Virus waits, worm walks.", 35)
    S.q("cs-m2", "easy", "Malware that locks your files and demands money to release them is —",
        ["Ransomware", "Spyware", "Adware", "Worm"], "Ransomware",
        "**Ransomware** holds data hostage — encrypt now, demand payment later (WannaCry, 2017).",
        "Ransom = money demand.", 20)
    S.q("cs-m2", "medium", "Which defence lets a ransomware victim recover WITHOUT paying?",
        ["Recent offline backups", "Sharing the ransom with friends", "Restarting the computer many times",
         "Turning off the monitor"],
        "Recent offline backups",
        "Backups kept **offline** (disconnected) escape the encryption — restore instead of paying.",
        "Backup beats ransom.", 25)
    S.q("cs-m2", "hard", "WannaCry, which crippled systems worldwide in 2017, was an outbreak of —",
        ["Ransomware", "Adware", "A browser hijacker", "A keylogger only"], "Ransomware",
        "**WannaCry (2017)** = the named ransomware epidemic exams quote.",
        "WannaCry wanted money.", 30)
    S.q("cs-m3", "medium", "Which malware records every key pressed on a keyboard?",
        ["Keylogger", "Adware", "Worm", "Rootkit"], "Keylogger",
        "**Keylogger** captures keystrokes — passwords included — as you type.",
        "Every key, logged.", 25)
    S.q("cs-m3", "medium", "Software that quietly collects information about a user and sends it to a third party is —",
        ["Spyware", "Shareware", "Firmware", "Malware-free trialware"], "Spyware",
        "**Spyware** spies — gathers your data in secret and ships it out.",
        "Spy = spyware.", 25)
    S.q("cs-m3", "easy", "Programs that flood your screen with unwanted advertisements are called —",
        ["Adware", "Hardware", "Groupware", "Worms"], "Adware",
        "**Adware** = advertisement-software; annoying more than damaging.",
        "Ad + ware.", 20)
    S.q("cs-m4", "medium", "A network of infected computers remotely controlled by an attacker is a —",
        ["Botnet", "Intranet", "Ethernet", "Internet"], "Botnet",
        "**Botnet** — an army of 'zombie' machines commanded together, owners unaware.",
        "Robots in a net.", 25)
    S.q("cs-m4", "hard", "Botnets are MOST commonly used to launch —",
        ["DDoS attacks and mass spam", "Print jobs", "Screen savers", "Software updates"],
        "DDoS attacks and mass spam",
        "A botnet's muscle powers **DDoS floods and spam campaigns** — thousands of machines acting as one.",
        "Zombies flood and spam.", 30)
    S.q("cs-m4", "medium", "Malware that hides deep in a system and conceals its own presence while giving an attacker administrator-level access is a —",
        ["Rootkit", "Keylogger", "Adware", "Worm"], "Rootkit",
        "**Rootkit** = root (admin) + kit — hides itself and hands over admin control.",
        "Root = admin, kit = tools.", 30)


def add_attacks(S):
    S.q("cs-a1", "easy", "Fraudulent e-mails that look like your bank's and ask for your password are an example of —",
        ["Phishing", "Debugging", "Booting", "Surfing"], "Phishing",
        "**Phishing** — fishing for your credentials with fake bait mails/sites.",
        "Phishing = fake bait.", 20)
    S.q("cs-a1", "medium", "Phishing carried out over a PHONE CALL is called —",
        ["Vishing", "Smishing", "Pharming", "Spamming"], "Vishing",
        "**Vishing** = Voice phishing; SMS-based phishing is smishing.",
        "V for voice.", 25)
    S.q("cs-a1", "medium", "Phishing messages delivered by SMS are called —",
        ["Smishing", "Vishing", "Pharming", "Snooping"], "Smishing",
        "**Smishing** = SMS phishing — the bait travels by text message.",
        "SM = SMS.", 25)
    S.q("cs-a1", "hard", "Sunil types his bank's web address CORRECTLY, but is still taken to a fake identical site that steals his login. This is —",
        ["Pharming", "Phishing", "Salami attack", "Brute force"], "Pharming",
        "**Pharming** — the address itself is hijacked (DNS poisoning); no user typing mistake occurred.",
        "Pharming farms fakes at the address level.", 35)
    S.q("cs-a2", "medium", "Flooding a server with useless requests so genuine users cannot use it is a —",
        ["Denial of Service attack", "Data diddling attack", "Salami attack", "Logic bomb"], "Denial of Service attack",
        "**DoS** drowns the service — the goal is shutdown, not data theft.",
        "Service denied.", 25)
    S.q("cs-a2", "medium", "A DoS attack launched SIMULTANEOUSLY from thousands of hijacked computers is called —",
        ["DDoS", "DNS", "DHCP", "MITM"], "DDoS",
        "**DDoS** = Distributed DoS — 'distributed' means many sources at once, usually a botnet.",
        "Distributed = many.", 25)
    S.q("cs-a2", "hard", "The army of hijacked machines that powers a DDoS flood is called a —",
        ["Botnet", "Backbone", "Bridge", "Buffer"], "Botnet",
        "The DDoS muscle comes from a **botnet of zombie machines**.",
        "Zombies do the flooding.", 30)
    S.q("cs-a3", "medium", "An attacker secretly positions himself between two parties and reads/alters their messages. This is a —",
        ["Man-in-the-Middle attack", "Denial of Service attack", "Logic bomb", "Salami attack"],
        "Man-in-the-Middle attack",
        "**MITM** — the hidden middleman between sender and receiver.",
        "Middle man listens.", 25)
    S.q("cs-a3", "medium", "Users of open public Wi-Fi are most exposed to which attack?",
        ["Man-in-the-Middle", "Salami attack", "Logic bomb", "Data diddling"],
        "Man-in-the-Middle",
        "Unencrypted traffic on open Wi-Fi is read by anyone in the middle — **MITM territory**; HTTPS/VPN protect you.",
        "Open Wi-Fi, open ears.", 25)
    S.q("cs-a3", "hard", "Which defence makes a man-in-the-middle attack ineffective?",
        ["End-to-end encryption (HTTPS/VPN)", "A bigger monitor", "More RAM", "Turning off Bluetooth"],
        "End-to-end encryption (HTTPS/VPN)",
        "With encryption the middleman intercepts only **ciphertext** he cannot read.",
        "Encrypt the middle away.", 30)
    S.q("cs-a4", "medium", "A program hidden in a payroll system that waits for 1 April and then wipes the database is a —",
        ["Logic bomb", "Worm", "Firewall", "Bot"], "Logic bomb",
        "**Logic bomb** — sleeps until its trigger condition (a date or event), then detonates.",
        "Bomb with a date fuse.", 25)
    S.q("cs-a4", "hard", "Stealing one rupee from each of ten lakh accounts is a —",
        ["Salami attack", "Phishing attack", "DDoS attack", "MITM attack"], "Salami attack",
        "**Salami slicing** — many tiny slices nobody notices, adding up to a fortune.",
        "Thin slices, big total.", 30)
    S.q("cs-a4", "medium", "Entering SQL commands into a website's input box to trick its database is —",
        ["SQL injection", "Data mining", "Web browsing", "Packet switching"], "SQL injection",
        "**SQL injection** — hostile database commands injected through a form field.",
        "Inject commands into the form.", 25)
    S.q("cs-a4", "medium", "Changing figures in a record while they are being entered into a computer system is —",
        ["Data diddling", "Data mining", "Debugging", "Defragmentation"], "Data diddling",
        "**Data diddling** = data altered before/during entry — the record itself lies.",
        "Diddle the data at the door.", 30)


def add_prevention(S):
    S.q("cs-v1", "easy", "A hardware or software barrier that filters traffic between your network and the Internet by rules is a —",
        ["Firewall", "Compiler", "Plotter", "Router table"], "Firewall",
        "**Firewall** = the rule-based doorman of a network.",
        "Wall of rules.", 20)
    S.q("cs-v1", "medium", "A firewall primarily decides —",
        ["Which network traffic to allow or block", "Which files to delete", "Which printer to use",
         "Which wallpaper to show"],
        "Which network traffic to allow or block",
        "Its whole job is **allow/block on traffic** passing the boundary — nothing about files or printing.",
        "Traffic in, traffic out.", 25)
    S.q("cs-v1", "hard", "Which statement about a firewall is TRUE?",
        ["It filters the doorway but does not clean an infection inside",
         "It removes viruses from the hard disk",
         "It replaces the need for backups",
         "It encrypts every file automatically"],
        "It filters the doorway but does not clean an infection inside",
        "**Firewall filters traffic**; cleaning inside files is the antivirus's job.",
        "Doorman, not doctor.", 35)
    S.q("cs-v2", "easy", "Software that scans the computer to find and remove viruses is —",
        ["Antivirus", "Antenna", "Assembler", "Application suite"], "Antivirus",
        "**Antivirus** scans, detects and removes malware.",
        "Anti = against viruses.", 20)
    S.q("cs-v2", "medium", "Why must antivirus software be updated regularly?",
        ["New malware and new signatures appear every day", "Updates make the computer faster",
         "Old versions stop the Internet", "Updates change the wallpaper"],
        "New malware and new signatures appear every day",
        "Antivirus matches **signatures**; without updates it cannot recognise yesterday's new malware.",
        "New germs, new medicine.", 25)
    S.q("cs-v2", "hard", "In an odd-one-out list, which item does NOT belong with the others?",
        ["Firewall", "Virus", "Trojan horse", "Worm"], "Firewall",
        "Virus, trojan, worm are **malware (attacks)**; a firewall is **protection** — the odd one out.",
        "Three attacks, one defence.", 25)
    S.q("cs-v3", "easy", "Two-factor authentication means —",
        ["Password plus a second proof such as an OTP", "Typing the password twice",
         "Two people sharing one password", "Two browsers logged in"],
        "Password plus a second proof such as an OTP",
        "**2FA = something you know + something you have/are** — password plus OTP or fingerprint.",
        "Two locks, one door.", 20)
    S.q("cs-v3", "medium", "Which is the STRONGEST password?",
        ["K7#mQx9!pLz2", "sunita1990", "12345678", "password"],
        "K7#mQx9!pLz2",
        "Long + mixed character types + not a personal fact = strong; the rest are the top of every 'worst passwords' list.",
        "Long, mixed, personal-free.", 25)
    S.q("cs-v3", "medium", "A caller says he is from your bank and asks for the OTP you just received. You should —",
        ["Refuse — banks never ask for OTPs", "Share it, he sounds genuine", "Share only half of it",
         "Share it if he knows your name"],
        "Refuse — banks never ask for OTPs",
        "**No genuine bank ever asks for OTP/PIN/CVV** — an OTP shared is money gone.",
        "OTP is never shared.", 20)
    S.q("cs-v3", "hard", "Why does 2FA defeat a thief who has stolen your password?",
        ["He still lacks the second factor (OTP/biometric)", "The password automatically changes",
         "The computer shuts down", "Stolen passwords work only on Fridays"],
        "He still lacks the second factor (OTP/biometric)",
        "2FA's whole design: **knowing the password alone is not enough** — the second proof is missing.",
        "One key opens nothing.", 30)
    S.q("cs-v4", "easy", "Readable, unscrambled data is called —",
        ["Plaintext", "Ciphertext", "Hypertext", "Notepad"], "Plaintext",
        "**Plaintext** = the readable original; scrambling turns it into ciphertext.",
        "Plain before cipher.", 20)
    S.q("cs-v4", "easy", "Data scrambled into unreadable form is called —",
        ["Ciphertext", "Plaintext", "Wikitext", "Context"], "Ciphertext",
        "**Ciphertext** = the encrypted form; decryption with the key returns plaintext.",
        "Cipher = code.", 20)
    S.q("cs-v4", "medium", "AES, the widely used modern encryption standard, expands to —",
        ["Advanced Encryption Standard", "American Electronic Security",
         "Applied Email Safety", "Automatic Encrypted System"],
        "Advanced Encryption Standard",
        "**AES = Advanced Encryption Standard** — the world's workhorse cipher.",
        "Advanced, not American.", 25)
    S.q("cs-v4", "medium", "The padlock symbol with https:// in the browser's address bar means —",
        ["The connection to the site is encrypted", "The site is government-approved",
         "The site has no advertisements", "The page will load faster"],
        "The connection to the site is encrypted",
        "**https = HTTP inside an encrypted TLS/SSL tunnel** — the padlock certifies the tunnel, not the site's honesty.",
        "Padlock = locked line.", 25)


def add_it_act(S):
    S.q("cs-l1", "easy", "India's Information Technology Act was enacted in —",
        ["2000", "1990", "2010", "2005"], "2000",
        "**IT Act, 2000** — in force from 17 October 2000.",
        "Cyber law born in 2000.", 20)
    S.q("cs-l1", "medium", "The IT Act, 2000 was based on the model law of —",
        ["UNCITRAL", "UNESCO", "UNICEF", "NATO"], "UNCITRAL",
        "**UNCITRAL** — the UN Commission on International Trade Law — recommended legal recognition of e-records.",
        "Trade law, not education.", 25)
    S.q("cs-l1", "medium", "The IT Act received its major amendment in —",
        ["2008", "2002", "2015", "1999"], "2008",
        "The **2008 amendment** (effective 2009) added 66C identity theft, 66D cheating, 66F cyber-terrorism and CERT-In's statutory role.",
        "First big revision in 2008.", 25)
    S.q("cs-l2", "medium", "Hacking (computer-related offences) is punished under which section of the IT Act?",
        ["Section 66", "Section 21", "Section 80", "Section 101"], "Section 66",
        "**Sec 66** = computer-related offences — the 'hacking' section with dishonest intent.",
        "66 = hacking.", 25)
    S.q("cs-l2", "medium", "Tampering with computer source code is an offence under —",
        ["Section 65", "Section 43", "Section 72", "Section 67"], "Section 65",
        "**Sec 65 = source code tampering**; 43 is unauthorised access/damage; 67 is obscenity.",
        "65 = source code.", 25)
    S.q("cs-l2", "hard", "Which section of the IT Act was STRUCK DOWN by the Supreme Court in 2015?",
        ["Section 66A", "Section 66C", "Section 67", "Section 65"], "Section 66A",
        "**66A ('offensive messages') died in Shreya Singhal v. Union of India (2015)** — free speech prevailed; the others remain live law.",
        "66A is dead law.", 35)
    S.q("cs-l2", "medium", "Publishing or transmitting obscene material in electronic form is punished under —",
        ["Section 67", "Section 65", "Section 66C", "Section 72"], "Section 67",
        "**Sec 67 = obscene electronic material** — 67A/67B variants were added in 2008.",
        "67 = obscenity.", 25)
    S.q("cs-l3", "medium", "CERT-In, the agency that responds to cyber security incidents in India, works under —",
        ["MeitY", "RBI", "ISRO", "Election Commission"], "MeitY",
        "**CERT-In functions under MeitY** (Ministry of Electronics and IT).",
        "IT ministry runs CERT-In.", 25)
    S.q("cs-l3", "hard", "Which body protects India's CRITICAL information infrastructure such as power grids and banking systems?",
        ["NCIIPC", "CERT-In", "TRAI", "SEBI"], "NCIIPC",
        "**NCIIPC** (under Sec 70A) guards critical infrastructure; CERT-In handles incident response generally.",
        "Critical = NCIIPC.", 30)
    S.q("cs-l3", "easy", "The national helpline number for reporting cyber fraud in India is —",
        ["1930", "100", "181", "139"], "1930",
        "**1930** — the national cyber-crime helpline (and cybercrime.gov.in online).",
        "1930 = cyber helpline.", 20)
    S.q("cs-l4", "medium", "A digital signature is created with the signer's —",
        ["Private key and verified with the public key", "Public key and verified with the private key",
         "Aadhaar number", "Fingerprint scanner only"],
        "Private key and verified with the public key",
        "**Sign with your private key; anyone verifies with your public key** — secrecy of the private key is everything.",
        "Private signs, public checks.", 30)
    S.q("cs-l4", "medium", "A digital signature mainly provides —",
        ["Authentication and integrity of the document", "Free storage", "Faster download", "Anonymity"],
        "Authentication and integrity of the document",
        "It proves **who signed** and that **nothing changed after signing** — not secrecy, not speed.",
        "Who + unaltered.", 25)
    S.q("cs-l4", "easy", "Which section of the IT Act gives legal recognition to digital signatures?",
        ["Section 3", "Section 9", "Section 33", "Section 90"], "Section 3",
        "**Sec 3 = authentication by digital (electronic) signature.**",
        "3 signs.", 20)
