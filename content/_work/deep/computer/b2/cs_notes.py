"""Cyber security deep notes."""

CS_MALWARE = """### Malware — hostile software
**Malware** (MALicious softWARE) is any program written to harm, steal or spy. Exams test one skill: matching the malware's **behaviour** to its **name**.

| Malware | Signature behaviour |
|---|---|
| **Virus** | attaches itself to a file/program and spreads when that file is **run** — needs a host |
| **Worm** | **self-replicates on its own** across networks — needs **no host file** |
| **Trojan horse** | hides inside **useful-looking software** (free game, "update"); **does not replicate** |
| **Ransomware** | **locks/encrypts your files and demands money** (e.g. WannaCry, 2017) |
| **Spyware** | secretly **collects your information** and sends it out |
| **Keylogger** | records **every keystroke** — passwords typed are captured (a spyware cousin) |
| **Adware** | floods the screen with unwanted **advertisements** |
| **Botnet** | many infected "zombie" machines remotely **controlled as one army** (for spam/DDoS) |
| **Rootkit** | buries itself deep in the system, **hides its presence**, grants attacker admin rights |

### The three distinctions exams plant
1. **Virus vs Worm**: a virus rides on a host file and waits for you to run it; a **worm needs no host** — it crawls through the network by itself.
2. **Trojan vs Virus**: a trojan **never replicates** — it waits, disguised as legitimate software, and opens the door from inside (backdoor).
3. **Ransomware vs Spyware**: ransomware takes your files hostage for money; spyware takes copies quietly and leaves everything in place.

### How malware arrives
Infected email attachments and links, pirated software, infected USB drives, drive-by downloads from unsafe sites, and fake "your PC is infected" pop-ups. Once inside, malware may slow the machine, corrupt or delete files, steal data, or enlist the machine into a botnet without the owner noticing anything beyond sluggishness.

### Symptoms of an infected machine
Unexplained slowness, files renamed or missing, programs opening on their own, browser home page changed, sudden pop-ups, the fan and disk working when you do nothing. None of these proves malware alone — but together they are the exam's favourite scenario line.

### Quick revision
- **Virus needs a host; Worm needs none; Trojan replicates not.**
- **Ransomware = lock and demand money** (WannaCry 2017); Spyware spies; Keylogger records keystrokes.
- **Botnet = army of zombie machines**; Rootkit = hidden admin-level intruder.
- Malware spreads by attachments, pirated software, unsafe downloads."""

CS_ATTACKS = """### Attacks on people and systems
Beyond malware, exams list named **attacks** — methods of cheating users or breaking services. Group them by target.

### Attacks that target PEOPLE (social engineering)
- **Phishing**: a fake mail/site dressed as your bank or company, asking for passwords, OTPs, card details. "Phish" = fishing for victims with bait.
- **Spear phishing**: phishing **aimed at one specific person or office**, with personal details to look genuine.
- **Vishing** (Voice) and **smishing** (SMS): the same bait delivered by **phone call** or **SMS**.
- **Pharming**: even a **correctly typed URL** lands you on a fake site — the attacker poisons the DNS/server side.
- **Social engineering** is the umbrella: manipulating **people** (fear, urgency, authority — "your account will be blocked in 1 hour") instead of breaking code.

### Attacks that target SERVICES
- **DoS** (Denial of Service): flooding a server with useless requests so genuine users are shut out.
- **DDoS** (Distributed DoS): the flood comes from **many machines at once**, usually a botnet.
- **Man-in-the-Middle (MITM)**: the attacker secretly sits **between two parties**, reading or altering what they exchange (e.g. on open Wi-Fi).

### Classic named attacks from exam history
| Attack | Trick |
|---|---|
| **Salami slicing/salami attack** | stealing **tiny amounts from very many accounts** — paise shaved off, hard to notice |
| **Data diddling** | changing data **before or during entry** into the system (false figures) |
| **Logic bomb** | malicious code that **sleeps until a trigger** — a date or event — then detonates |
| **SQL injection** | typing database commands into a web form's input box to read the database |
| **Brute force** | trying **every possible password** combination until one works |
| **Eavesdropping** | passively **listening** to data as it travels |

### Telling the twins apart
Phishing asks the **user** to hand over data; pharming needs no user mistake — the **address itself is hijacked**. DoS asks nothing of users — it **drowns the server**. MITM does not flood or fake a site — it **listens in the middle** of a real conversation. Salami steals **small and often**; data diddling **alters records**; a logic bomb waits for its **trigger**.

### Quick revision
- **Phishing = mail bait; Vishing = voice; Smishing = SMS; Pharming = fake site despite correct URL.**
- **DoS/DDoS = flood the server** (DDoS from a botnet); **MITM = listen between two parties**.
- **Salami = tiny thefts, many accounts; Logic bomb = waits for a trigger; SQL injection = commands in a form.**
- Social engineering = attacking the person, not the machine."""

CS_PREVENTION = """### The defence line-up
| Defence | What it does |
|---|---|
| **Firewall** | a barrier (hardware/software) that **monitors and filters traffic** between your network and the outside, by rules — allow or block |
| **Antivirus** | **detects and removes malware**, mainly by matching **virus signatures** — so it must be **updated regularly** |
| **Encryption** | scrambles data so only the key-holder can read it — **plaintext (readable) to ciphertext (scrambled)**; reading back is decryption |
| **Two-factor authentication (2FA)** | password **plus** a second proof — OTP on phone, fingerprint — so a stolen password alone is useless |
| **Backup** | a safe copy of data kept separately, so ransomware or disk failure cannot erase you |
| **Updates/patches** | fixes for newly discovered security holes — unpatched systems stay open doors |

### Firewall vs antivirus — the roles exams swap
A **firewall guards the doorway**: it watches network traffic in and out and blocks what breaks the rules — it does not clean infections. **Antivirus works inside**: it scans files and memory and removes malware that got in — it does not filter network traffic. A machine can have both, and each answers a different exam line: "which filters incoming/outgoing traffic?" = firewall; "which detects and removes viruses?" = antivirus.

### Encryption — the one diagram
**Plaintext** (HELLO) is fed with a **key** through an encryption algorithm to produce unreadable **ciphertext**; the receiver applies the key to decrypt. **AES** (Advanced Encryption Standard) is the widely used modern standard. When you see the **padlock and https://** in a browser, the web session is encrypted — the S means Secure. Encryption protects data even if it is stolen in transit; it is why open public Wi-Fi without HTTPS is risky.

### Password hygiene and safe habits
- Long passwords mixing letters, digits and symbols; **never name, birthdate, or 123456**; different password for each important account; changed periodically.
- **2FA everywhere it is offered** — the OTP is the second lock.
- Never share OTPs/PINs; banks never ask for them. Do not click links in unknown mails; download software only from official sources; keep the OS and antivirus updated; take backups.

### Quick revision
- **Firewall filters traffic by rules; antivirus finds and removes malware; they are not the same job.**
- **Encryption: plaintext + key = ciphertext; decryption reverses it; AES = the standard; https = encrypted web.**
- **2FA = password + OTP/biometric** — a stolen password alone fails.
- Backups defeat ransomware; updates close known holes."""

CS_IT_ACT = """### The Information Technology Act, 2000
India's law for the electronic world is the **IT Act, 2000**, in force from **17 October 2000**. It grew out of the **UNCITRAL model law** (United Nations Commission on International Trade Law) on electronic commerce, which recommended that countries give legal recognition to electronic records and signatures. The Act legalised **electronic records and digital signatures** and created punishments for computer crimes. It was **amended in 2008** (effective 2009), adding identity theft, cyber-terrorism provisions and the CERT-In mandate.

### Sections the exams keep asking
| Section | Subject |
|---|---|
| **Sec 3** | authentication by **digital (electronic) signature** |
| **Sec 43** | penalty/compensation for **unauthorised access and damage** to computer, data (hacking-type harm) |
| **Sec 65** | **tampering with computer source code** |
| **Sec 66** | **computer-related offences** — the "hacking" section (dishonest intent) |
| **Sec 66C** | **identity theft** (fraudulent use of password/digital signature/biometric) |
| **Sec 66D** | **cheating by personation** using a computer resource (fake profiles) |
| **Sec 67** | publishing/transmitting **obscene material** in electronic form |
| **Sec 72** | **breach of confidentiality and privacy** (by those with lawful access to data) |

**Section 66A** (punishment for "offensive messages") was **struck down by the Supreme Court in Shreya Singhal v. Union of India (2015)** as violative of free speech — a favourite trick option presented as still-valid law.

### The watchdogs
- **CERT-In** (Indian Computer Emergency Response Team) — the national incident-response agency under **MeitY** (Ministry of Electronics and IT); set up 2004, statutory backing via Sec 70B after the 2008 amendment.
- **NCIIPC** (National Critical Information Infrastructure Protection Centre) — protects **critical infrastructure** (power, banking, telecom) under Sec 70A.
- **MeitY** is the parent ministry for cyber laws and policy; the **DPDP Act, 2023** (Digital Personal Data Protection Act) now governs personal-data privacy alongside the IT Act.
- Reporting: national cyber-crime helpline **1930** and the portal **cybercrime.gov.in**.

### Digital signature in one line
A **digital signature** (Sec 3) is the electronic equivalent of a handwritten signature: created with the signer's **private key** and verified by anyone with the **public key** (Certificate Authorities issue the keys). It proves **who** signed and that the document was **not altered** — authentication plus integrity.

### Quick revision
- **IT Act 2000, effective 17 Oct 2000, based on UNCITRAL; amended 2008.**
- 65 = source code; **66 = hacking; 66C = identity theft; 66D = online cheating; 67 = obscenity**; 43 = unauthorised access penalty; **66A struck down 2015**.
- **CERT-In = incident response under MeitY; NCIIPC = critical infrastructure**; helpline 1930.
- Digital signature = private key signs, public key verifies (Sec 3)."""
