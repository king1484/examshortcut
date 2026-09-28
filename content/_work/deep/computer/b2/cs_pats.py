"""Cyber security pattern builders."""
from _lib import Sub


def build_malware():
    S = Sub("cs-malware")
    S.notes = __import__("cs_notes").CS_MALWARE
    S.pattern("cs-m1", "Malware identification by behaviour", "very common",
              "A behaviour is described ('self-replicates without a host', 'disguises as useful software', 'encrypts files for ransom') and the malware is asked.",
              None,
              "1. Needs a host file = **Virus**; self-replicates alone over the network = **Worm**.\n2. Disguised as useful software, does not replicate = **Trojan horse**.\n3. Locks files and demands money = **Ransomware**; watches silently = Spyware/Keylogger.",
              "A program that enters a computer disguised as a free game and does not replicate is a:",
              "**Trojan horse** — the disguise is its signature; replication belongs to virus/worm."),
    S.pattern("cs-m2", "Ransomware scenarios", "common",
              "'Files are locked and money is demanded', 'WannaCry' or any hostage-style scenario.",
              None,
              "1. Encrypt-and-demand-money = **Ransomware** — the fastest identification in the topic.\n2. Defence = **offline backups**; paying the ransom is never advised.\n3. WannaCry (2017) is the named example exams use.",
              "A hospital finds all its patient records encrypted with a demand for money to unlock them. This is:",
              "**Ransomware** — data taken hostage; restored from backups, not by paying."),
    S.pattern("cs-m3", "Spyware, keylogger and adware", "common",
              "'Records every keystroke', 'secretly collects browsing data', 'shows endless advertisements' — the quiet watchers.",
              None,
              "1. Records keystrokes = **Keylogger** (passwords captured as you type).\n2. Secretly gathers and sends your information = **Spyware**.\n3. Throws unwanted ads = **Adware**. All three spy or annoy — none of them locks files.",
              "Ravi suspects his typed passwords are being captured as he types them. Which malware fits?",
              "**Keylogger** — it records every keystroke, so even a strong password leaks."),
    S.pattern("cs-m4", "Botnet and zombies", "occasional",
              "'A network of infected computers controlled by an attacker', 'zombie machines used for spam/DDoS'.",
              None,
              "1. **Botnet = many infected 'zombie' machines remotely commanded as one** — owners usually unaware.\n2. Botnets are the muscle behind **DDoS floods and mass spam**.\n3. The controller is the 'bot herder'; your slow machine may be someone's soldier.",
              "Thousands of infected home computers are ordered together to flood one server. The infected network is a:",
              "**Botnet** — the army of zombies that powers DDoS attacks."),
    return S


def build_attacks():
    S = Sub("cs-attacks")
    S.notes = __import__("cs_notes").CS_ATTACKS
    S.pattern("cs-a1", "Phishing family (mail, voice, SMS, pharming)", "very common",
              "A fake-bank-mail / fake-call / fake-SMS / correct-URL-fake-site scenario asking for the attack's name, or 'vishing/smishing mean ___'.",
              None,
              "1. Bait by **e-mail or fake site** = Phishing; by **phone call** = Vishing; by **SMS** = Smishing.\n2. **Correct URL still lands on a fake site** = Pharming (address hijacked, no user mistake).\n3. Aimed at ONE chosen person = **Spear phishing**. All are social engineering — attacking the person, not the machine.",
              "A caller claiming to be from the bank asks for the OTP sent to Meena's phone. This fraud is:",
              "**Vishing** — voice phishing; a real bank never asks for OTPs."),
    S.pattern("cs-a2", "DoS, DDoS and botnet floods", "common",
              "'Server is flooded with requests and genuine users are shut out', 'attack from thousands of machines at once'.",
              None,
              "1. Flood from **one source** = **DoS**; from **many machines at once** (usually a botnet) = **DDoS**.\n2. The aim is **denial of service**, not data theft — the service drowns.\n3. DDoS question almost always names 'distributed/thousands of computers' — that word IS the answer key.",
              "A shopping site crashes as thousands of hijacked machines hammer it with fake requests together. This is:",
              "**DDoS** — Distributed Denial of Service; 'distributed' = many sources at once."),
    S.pattern("cs-a3", "Man-in-the-Middle and eavesdropping", "occasional",
              "'Communication between A and B is read/changed by a hidden third party', risks of open public Wi-Fi.",
              None,
              "1. **MITM = attacker sits silently between two parties**, reading or altering the exchange — neither side notices.\n2. Classic setting: **open public Wi-Fi** without encryption.\n3. Defence: encrypted connections (**HTTPS/VPN**) — the middle man sees only ciphertext.",
              "On free airport Wi-Fi, an attacker secretly reads the data exchange between Amit and the site he is using. This attack is:",
              "**Man-in-the-Middle (MITM)** — the hidden listener between two ends."),
    S.pattern("cs-a4", "Classic named attacks (salami, diddling, logic bomb, SQLi)", "common",
              "'Tiny amounts stolen from many accounts', 'records changed during entry', 'code that waits for a date', 'commands typed into a login box'.",
              None,
              "1. **Salami attack** = many tiny thefts (paise from lakhs of accounts).\n2. **Data diddling** = data changed before/during entry.\n3. **Logic bomb** = sleeps until a trigger (date/event).\n4. **SQL injection** = database commands typed into a web form; **Brute force** = trying every password.",
              "A bank clerk's program quietly takes one rupee from thousands of accounts into his own. This is a:",
              "**Salami attack** — slicing tiny amounts off very many accounts."),
    return S


def build_prevention():
    S = Sub("cs-prevention")
    S.notes = __import__("cs_notes").CS_PREVENTION
    S.pattern("cs-v1", "Firewall purpose", "very common",
              "'A firewall is used for', 'which device/software filters traffic between networks by rules', hardware-or-software barrier statements.",
              None,
              "1. **Firewall = rule-based barrier** between your network and the outside — allows or blocks traffic.\n2. It **filters the doorway**; it does not scan or clean infected files.\n3. Can be hardware, software or both.",
              "The security system that monitors and filters data entering or leaving a network according to rules is a:",
              "**Firewall** — the doorman of the network."),
    S.pattern("cs-v2", "Antivirus vs firewall roles", "common",
              "'Which removes an infection already inside', odd-one-out items where one role is swapped between firewall and antivirus.",
              None,
              "1. **Antivirus scans, detects and removes malware**, chiefly by signature matching — so **updates are compulsory**.\n2. **Firewall filters traffic; antivirus cleans inside** — the swap is the classic trap.\n3. Neither replaces the other; a protected machine keeps both.",
              "Which tool detects and removes a virus that has already entered a computer?",
              "**Antivirus** — firewall could not have let it in if configured well, but only antivirus cleans inside."),
    S.pattern("cs-v3", "Password hygiene and 2FA", "very common",
              "'Strong password' pick-the-best-option, 'two-factor authentication means ___', scenarios where a password alone failed.",
              None,
              "1. Strong = **long, mixed (letters+digits+symbols), no name/birthdate/123456, unique per account**.\n2. **2FA = password + a second proof** (OTP, fingerprint) — a stolen password alone is not enough.\n3. Never share OTP/PIN; banks never ask for them — any such message is fraud.",
              "Which of these is the STRONGEST password?",
              "A long mix of letters, digits and symbols unique to that account — not a name, birthdate or 123456."),
    S.pattern("cs-v4", "Encryption basics (plaintext, ciphertext, AES, https)", "common",
              "'Scrambled unreadable data is called ___', 'plaintext to ciphertext', 'the padlock/https means ___', 'AES is a ___'.",
              None,
              "1. Readable original = **plaintext**; scrambled form = **ciphertext**; reversing = decryption, done with the **key**.\n2. **AES** = Advanced Encryption Standard, the widely used modern standard.\n3. **https + padlock = encrypted web session** — the S stands for Secure.",
              "Data that has been scrambled so that unauthorised people cannot read it is called:",
              "**Ciphertext** — the encrypted form; plaintext is the readable original."),
    return S


def build_it_act():
    S = Sub("cs-it-act")
    S.notes = __import__("cs_notes").CS_IT_ACT
    S.pattern("cs-l1", "IT Act basics (year, origin, amendment)", "very common",
              "'The IT Act was passed in ___', 'in force from 17 October 2000', 'based on which UN model law', 'the 2008 amendment'.",
              None,
              "1. **IT Act 2000, in force 17 October 2000** — India's cyber law.\n2. Based on the **UNCITRAL model law** on e-commerce (UN Commission on International Trade Law).\n3. **Amended 2008** (effective 2009) — added identity theft (66C/66D), cyber-terrorism (66F), CERT-In backing.",
              "India's Information Technology Act came into force on:",
              "**17 October 2000** — based on the UNCITRAL model law; amended in 2008."),
    S.pattern("cs-l2", "Section-to-offence matching", "very common",
              "'Section 66 deals with ___', 'identity theft is which section', 'which section was struck down' — 43/65/66/66C/66D/67/72 and 66A.",
              None,
              "1. **43** unauthorised access/damage penalty; **65** source-code tampering; **66** hacking (computer-related offences).\n2. **66C identity theft; 66D cheating by personation; 67 obscene material; 72 breach of privacy.**\n3. **66A (offensive messages) was STRUCK DOWN in 2015** — Shreya Singhal case. Any option using 66A as live law is wrong.",
              "Under which section of the IT Act is identity theft punished?",
              "**Section 66C** — fraudulent use of another's password, digital signature or biometric."),
    S.pattern("cs-l3", "Authorities: CERT-In, NCIIPC, MeitY, helpline", "common",
              "'CERT-In stands for / works under ___', 'critical infrastructure is protected by ___', 'the cyber-fraud helpline number'.",
              None,
              "1. **CERT-In** (Indian Computer Emergency Response Team) = national incident-response agency, **under MeitY**.\n2. **NCIIPC** protects **critical information infrastructure** (power, banking, telecom).\n3. Report fraud on **1930** or **cybercrime.gov.in**; personal-data privacy now also under the **DPDP Act 2023**.",
              "CERT-In, India's cyber incident response agency, functions under which ministry?",
              "**MeitY** — Ministry of Electronics and Information Technology."),
    S.pattern("cs-l4", "Digital signature and e-record legality", "occasional",
              "'A digital signature is used for ___', 'which section gives digital signatures legal status', authentication/integrity statements.",
              None,
              "1. **Digital signature (Sec 3)** = electronic equivalent of a handwritten signature.\n2. It proves **who signed (authentication)** and that the document was **not altered (integrity)** — not secrecy.\n3. Signed with the signer's **private key**, verified with the **public key**; Certificate Authorities issue the credentials.",
              "A digital signature primarily guarantees:",
              "**Authenticity of the sender and integrity of the document** — the file cannot be altered unnoticed; it is not encryption for secrecy."),
    return S
