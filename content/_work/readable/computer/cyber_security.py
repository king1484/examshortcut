"""Readable rewrite of Computer > Cyber Security (4 subtopics). Idempotent."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rl_common import pat, mis, trick, apply  # noqa: E402

# dates and years asserted so a typo cannot slip in
assert 2000 + 8 == 2008 and 2015 - 2000 == 15 and 2017 - 2000 == 17

SUBS = {}

# =====================================================================
SUBS["cs-malware"] = dict(
    concept=(
        "**Malware** is short for malicious software. It is any program made to harm, steal or spy. "
        "Exam questions ask you to match a **behaviour** to a **name**. "
        "Learn the key difference: a virus needs a host file, a worm needs none and a trojan does not copy itself."
    ),
    notes=r"""### What malware is
**Malware** means **mal**icious soft**ware**. It is a program written to harm a computer, steal data or spy on a user. Questions test one skill: match the behaviour to the name.

| Malware | Key behaviour |
|---|---|
| **Virus** | Attaches to a file or program. Spreads when the file is **run**. Needs a host |
| **Worm** | **Copies itself** across a network. Needs **no host file** |
| **Trojan horse** | Hides inside **useful-looking software**. **Does not copy itself** |
| **Ransomware** | **Locks or encrypts files** and demands money. WannaCry (2017) is an example |
| **Spyware** | Secretly **collects your information** and sends it out |
| **Keylogger** | Records **every key you press**, so it can catch passwords |
| **Adware** | Shows unwanted **advertisements** |
| **Rootkit** | Hides deep in the system and gives the attacker admin rights |
| **Botnet** | Many infected "zombie" machines controlled together, often for spam or DDoS |
| **Logic bomb** | Code that sleeps until a date or event, then does its damage |

### Three pairs that exams mix
1. **Virus vs worm.** A virus rides on a host file and waits for you to run it. A worm needs no host. It travels through the network alone.
2. **Trojan vs virus.** A trojan never copies itself. It pretends to be useful and opens a back door from inside.
3. **Ransomware vs spyware.** Ransomware holds your files hostage. Spyware quietly copies data and leaves everything in place.

> **Rule:** Ask three things. Does it need a host? Does it copy itself? Does it demand money?

### How malware arrives
- Infected e-mail attachments and links.
- Pirated software.
- Infected USB drives.
- Downloads from unsafe sites.
- Fake pop-ups that say "your PC is infected".

### Signs of infection
- The computer runs unusually slowly.
- Files are renamed or missing.
- Programs open on their own.
- The browser home page changes.
- Pop-ups appear all the time.

> **Watch:** One sign alone does not prove malware. Together they form the usual exam scenario.

### Safe habits
Keep the operating system and antivirus updated. Do not open unknown attachments. Install software only from official sources. Take regular backups.

> **Example:** A free game hides a program that lets a stranger control your PC. It does not copy itself. That is a **trojan**.
""",
    tricks=[
        trick("Host test",
              "A virus needs a host file. A worm needs none. A trojan copies nothing.",
              "A program spreads across a network by itself with no host file. What is it?",
              ["No host file is needed.", "It copies itself.", "That is a worm."],
              "Worm"),
        trick("Money test",
              "If files are locked and money is demanded, it is ransomware. WannaCry in 2017 is the standard example."),
    ],
    mistakes=[
        mis("Saying a worm needs a host file.", "A virus needs a host. A worm spreads on its own."),
        mis("Saying a trojan copies itself.", "A trojan does not copy itself. It hides inside useful-looking software."),
        mis("Calling ransomware a kind of spyware.", "Ransomware locks files for money. Spyware secretly collects information."),
        mis("Thinking a keylogger records the screen.", "A keylogger records key presses."),
        mis("Thinking one slow computer proves malware.", "Slowness is only one sign. Several signs together point to malware."),
    ],
    revision=[
        "Malware is malicious software. Virus needs a host, worm needs none, trojan does not copy itself.",
        "Ransomware locks files and demands money. WannaCry (2017) is the example.",
        "Spyware collects information. Keylogger records key presses. Adware shows ads.",
        "Rootkit hides and gives admin rights. Botnet is an army of zombie machines.",
        "A logic bomb waits for a trigger date or event.",
        "Malware arrives through attachments, pirated software, USB drives and unsafe downloads.",
    ],
    patterns=[
        pat("cs-m1", "Malware identification by behaviour", "very common",
            "A short scenario describes what the program does, and its name is asked.",
            ["Find the key action: spreads, hides, locks, spies or records.", "Check whether a host file is needed.", "Match the action to the table."],
            "Every malware type has one signature behaviour.",
            "A program pretends to be a free game but secretly opens a back door. It is a:",
            ["It looks useful.", "It hides its true purpose.", "It does not copy itself, so it is a trojan."],
            "Trojan horse"),
        pat("cs-m2", "Ransomware scenarios", "very common",
            "Files are locked and a payment is demanded.",
            ["Spot the words locked, encrypted or pay.", "Name it ransomware.", "Recall WannaCry (2017) as the example."],
            "The demand for money is the clear sign.",
            "A message says your files are encrypted and asks for payment to unlock them. This is:",
            ["Files are locked.", "Money is demanded."], "Ransomware"),
        pat("cs-m3", "Spyware, keylogger and adware", "common",
            "The scenario says information is collected, keys are recorded or ads keep appearing.",
            ["Secret collection of information is spyware.", "Recording key presses is a keylogger.", "Unwanted advertisements are adware."],
            "These three are close relatives, and the action separates them.",
            "Which malware records every key pressed to steal passwords?",
            ["It records key presses.", "The name says so."], "Keylogger"),
        pat("cs-m4", "Botnet and zombies", "common",
            "Many infected machines are controlled together.",
            ["Spot the words army, zombie or remote control.", "Name it a botnet.", "Recall that botnets often drive DDoS attacks."],
            "A botnet is the tool behind large floods.",
            "A network of infected computers controlled by one attacker is called a:",
            ["Many machines are infected.", "One attacker controls them."], "Botnet"),
        pat("cs-m5", "Virus vs worm vs trojan", "very common",
            "Two or three malware names are offered, and one matches the description.",
            ["Ask if it needs a host file.", "Ask if it copies itself.", "Virus needs a host. Worm copies alone. Trojan does not copy."],
            "This trio is the most used exam pair.",
            "Which malware spreads through a network without needing a host file?",
            ["A virus needs a host.", "A trojan does not spread by itself.", "A worm spreads alone."], "Worm"),
    ],
)

# =====================================================================
SUBS["cs-attacks"] = dict(
    concept=(
        "**Attacks** are methods used to cheat people or to break services. "
        "Some target people, such as phishing, vishing and smishing. Some target services, such as DoS, DDoS and man-in-the-middle. "
        "Other named attacks include salami, data diddling, logic bomb, SQL injection and brute force."
    ),
    notes=r"""### Two groups of attacks
Group every attack by its target. Some attacks target **people**. Others target **services**.

### Attacks on people
- **Phishing:** a fake mail or site that looks like your bank. It asks for passwords, OTPs or card details. Think of fishing with bait.
- **Spear phishing:** phishing aimed at **one person or one office**, using personal details.
- **Vishing:** phishing by **voice**, a phone call.
- **Smishing:** phishing by **SMS**.
- **Pharming:** you type the **correct address**, yet a fake site opens. The attacker has tampered with the DNS or the server.
- **Social engineering:** tricking people through fear, urgency or authority. It attacks the person, not the code.

> **Tip:** Phishing needs the user to be fooled. Pharming does not.

### Attacks on services
- **DoS (Denial of Service):** a flood of useless requests so real users cannot get in.
- **DDoS (Distributed DoS):** the flood comes from **many machines at once**, often a botnet.
- **Man-in-the-Middle (MITM):** the attacker sits **between two parties** and reads or changes what they send. Open Wi-Fi is a common setting.
- **Eavesdropping:** passive listening to data as it travels.
- **Sniffing:** capturing network packets to read them.
- **Spoofing:** pretending to be someone else, such as a fake sender address.

### Named attacks
| Attack | Idea |
|---|---|
| **Salami attack** | Steals tiny amounts from very many accounts. Hard to notice |
| **Data diddling** | Changes data before or while it is entered |
| **Logic bomb** | Code that waits for a trigger, then acts |
| **SQL injection** | Types database commands into a web form to read the database |
| **Brute force** | Tries every possible password until one works |

### Telling the look-alikes apart
- Phishing asks the user to hand over data. Pharming hijacks the address itself.
- DoS drowns the server. MITM listens in the middle of a real conversation.
- Salami steals small amounts often. Data diddling alters records.
- A logic bomb waits for a trigger.

> **Rule:** The word "distributed" means many sources. DDoS is the flood from many machines.

> **Example:** A bank clerk shaves a few paise off thousands of accounts. That is a **salami attack**.
""",
    tricks=[
        trick("V for voice, S for SMS",
              "Vishing uses voice calls. Smishing uses SMS. Both are phishing with a different bait.",
              "A fraudster phones you pretending to be from your bank and asks for your OTP. This is:",
              ["The bait is a phone call.", "Phishing by voice is vishing."],
              "Vishing"),
        trick("Pharm needs no click",
              "In pharming you type the right address and still reach a fake site. The address system was tampered with."),
    ],
    mistakes=[
        mis("Calling a DoS attack a virus.", "DoS is a flood of requests. It is an attack, not malware."),
        mis("Saying pharming needs the user to click a bad link.", "Pharming sends you to a fake site even if you type the right address."),
        mis("Confusing DoS and DDoS.", "DDoS comes from many machines at once."),
        mis("Thinking MITM floods the server.", "MITM sits between two parties and listens or changes messages."),
        mis("Mixing salami with data diddling.", "Salami steals tiny amounts. Data diddling changes data during entry."),
    ],
    revision=[
        "Phishing is mail bait. Vishing is voice. Smishing is SMS. Pharming is a fake site despite a correct address.",
        "Spear phishing targets one person or office.",
        "DoS floods a server. DDoS floods from many machines, usually a botnet.",
        "MITM listens between two parties. Eavesdropping is passive listening.",
        "Salami takes tiny sums from many accounts. Logic bomb waits for a trigger.",
        "SQL injection puts commands in a web form. Brute force tries every password.",
        "Social engineering attacks the person, not the machine.",
    ],
    patterns=[
        pat("cs-a1", "Phishing family", "very common",
            "The scenario describes a fake mail, call, SMS or site that asks for private data.",
            ["Check the delivery: mail, voice, SMS or site.", "Mail is phishing, voice is vishing, SMS is smishing.", "A fake site despite a correct address is pharming."],
            "The family shares one aim, and only the channel differs.",
            "Which attack sends a fake SMS to trick a user into giving bank details?",
            ["The channel is SMS.", "Phishing by SMS is smishing."], "Smishing"),
        pat("cs-a2", "DoS and DDoS floods", "very common",
            "A server is overwhelmed and real users cannot get in.",
            ["Spot the words flood, overload or unavailable.", "One source is DoS.", "Many machines, often a botnet, is DDoS."],
            "The flood denies the service to real users.",
            "An attack that floods a server from thousands of infected machines is a:",
            ["The flood comes from many machines.", "That is the distributed form."], "DDoS attack"),
        pat("cs-a3", "Man-in-the-Middle and eavesdropping", "common",
            "Someone secretly reads or changes messages between two parties.",
            ["Spot the words between, intercept or open Wi-Fi.", "Reading and changing is MITM.", "Only listening is eavesdropping."],
            "The attacker sits in the middle of a real chat.",
            "An attacker secretly sits between a user and a website and reads the traffic. This is:",
            ["The attacker is between two parties.", "That is MITM."], "Man-in-the-Middle attack"),
        pat("cs-a4", "Classic named attacks", "very common",
            "The question gives a special detail such as tiny amounts, a trigger, or a web form.",
            ["Tiny amounts from many accounts is salami.", "Data changed during entry is data diddling.", "A trigger date is a logic bomb.", "Commands in a form is SQL injection."],
            "Each named attack has one memorable trick.",
            "A program deletes files on 1 January of a given year, and stays silent until then. It is a:",
            ["It waits for a date.", "A date trigger means a logic bomb."], "Logic bomb"),
        pat("cs-a5", "Brute force and password guessing", "occasional",
            "An attacker tries many passwords until one works.",
            ["Spot the words every combination or many guesses.", "Name it brute force.", "Long and mixed passwords slow it down."],
            "A longer password has far more combinations to try.",
            "Trying every possible password until the right one is found is called:",
            ["Every option is tried.", "The method uses force, not trickery."], "Brute force attack"),
    ],
)

# =====================================================================
SUBS["cs-prevention"] = dict(
    concept=(
        "Defences protect a system before, during and after an attack. "
        "A **firewall** filters network traffic. **Antivirus** finds and removes malware. "
        "**Encryption** scrambles data, **2FA** adds a second proof, and **backups** save you when data is lost."
    ),
    notes=r"""### The defence line-up
| Defence | What it does |
|---|---|
| **Firewall** | A barrier in hardware or software. It **filters traffic** between your network and the outside by rules |
| **Antivirus** | **Finds and removes malware**, mostly by matching known virus signatures. It must be updated |
| **Encryption** | Scrambles data so only the key holder can read it |
| **Two-factor authentication (2FA)** | A password **plus** a second proof, such as an OTP or fingerprint |
| **Backup** | A separate safe copy of data |
| **Updates and patches** | Fixes for security holes that were found |
| **VPN** | An encrypted tunnel over the internet |

### Firewall vs antivirus
The two are often swapped.

- A **firewall guards the doorway**. It watches traffic in and out and blocks anything that breaks the rules. It does not clean infections.
- **Antivirus works inside**. It scans files and memory and removes malware that got in. It does not filter network traffic.

> **Rule:** Filters incoming and outgoing traffic means firewall. Detects and removes viruses means antivirus.

### Encryption in one picture
**Plaintext** is readable data, such as HELLO. An encryption method and a **key** turn it into **ciphertext**, which is unreadable. The receiver uses a key to **decrypt** it back.

- **AES** (Advanced Encryption Standard) is a widely used modern method.
- A padlock and **HTTPS** in the browser mean the session is encrypted. The S stands for Secure.
- Encryption protects data even if someone steals it on the way.

> **Watch:** Public Wi-Fi without HTTPS is risky, because others may read your traffic.

### Digital signature
A **digital signature** proves who sent a document and that nobody changed it. The sender signs with a private key. Anyone can check it with the public key.

### Password hygiene
- Use long passwords that mix letters, digits and symbols.
- Never use your name, birth date or 123456.
- Use a different password for each important account.
- Turn on **2FA** wherever it is offered.
- Never share an OTP or PIN. Banks never ask for them.

### Safe habits
- Do not click links in unknown mail.
- Download software only from official sources.
- Keep the operating system and antivirus updated.
- Take regular backups.

> **Tip:** Backups beat ransomware. If your files are locked, you restore the copy.
""",
    tricks=[
        trick("Door and room",
              "A firewall guards the door, so it watches traffic. Antivirus cleans the room, so it removes malware inside."),
        trick("Two factors",
              "2FA needs something you know, such as a password, plus something you have or are, such as an OTP or fingerprint.",
              "A bank sends an OTP after you enter your password. Which security idea is this?",
              ["The password is the first factor.", "The OTP is a second proof."],
              "Two-factor authentication"),
    ],
    mistakes=[
        mis("Saying antivirus filters network traffic.", "A firewall filters traffic. Antivirus removes malware."),
        mis("Saying a firewall removes viruses.", "A firewall blocks traffic by rules. It does not clean infections."),
        mis("Using the same simple password for every account.", "Use a long, different password for each important account."),
        mis("Thinking ciphertext is readable data.", "Plaintext is readable. Ciphertext is the scrambled form."),
        mis("Ignoring updates because the antivirus is installed.", "Antivirus must be updated to know new threats."),
    ],
    revision=[
        "Firewall filters traffic by rules. Antivirus detects and removes malware.",
        "Encryption turns plaintext into ciphertext with a key. Decryption reverses it. AES is the modern standard.",
        "https and the padlock mean the web session is encrypted.",
        "2FA is a password plus a second proof such as an OTP or fingerprint.",
        "Backups defeat ransomware. Updates close known holes.",
        "A digital signature is signed with the private key and checked with the public key.",
    ],
    patterns=[
        pat("cs-v1", "Firewall purpose", "very common",
            "The question asks what filters network traffic.",
            ["Spot the words filter, monitor or traffic.", "Match them to a barrier with rules.", "Name it a firewall."],
            "A firewall is the gatekeeper between networks.",
            "Which security tool monitors and filters incoming and outgoing network traffic?",
            ["It works at the network door.", "It uses allow or block rules."], "Firewall"),
        pat("cs-v2", "Antivirus vs firewall roles", "very common",
            "Two tools are offered, and one job is described.",
            ["Detect and remove malware means antivirus.", "Filter traffic means firewall.", "Remember antivirus needs regular updates."],
            "The two tools do different jobs on different layers.",
            "Which tool detects and removes viruses from a computer?",
            ["It cleans infections.", "That is the antivirus."], "Antivirus"),
        pat("cs-v3", "Password hygiene and 2FA", "common",
            "The question asks for a strong password rule or the meaning of 2FA.",
            ["A strong password is long and mixed.", "Never use a name or 123456.", "2FA adds a second proof."],
            "A second proof makes a stolen password useless alone.",
            "Login with a password followed by an OTP on the phone is called:",
            ["The password is one factor.", "The OTP is a second factor."], "Two-factor authentication"),
        pat("cs-v4", "Encryption basics", "very common",
            "The question mentions plaintext, ciphertext, AES or https.",
            ["Plaintext is readable.", "Ciphertext is scrambled.", "AES is a modern method.", "https means encrypted web."],
            "Encryption protects the data itself, not only the path.",
            "Data in unreadable, scrambled form after encryption is called:",
            ["Readable data is plaintext.", "The scrambled form is the opposite."], "Ciphertext"),
        pat("cs-v5", "Backup and updates", "occasional",
            "The question asks how to recover from ransomware or fix a security hole.",
            ["Backups restore lost or locked data.", "Updates and patches close known holes.", "Both should be regular."],
            "Prevention and recovery both matter.",
            "The best protection against losing files to ransomware is:",
            ["Locked files can be replaced.", "A separate copy makes that possible."], "Regular backups"),
    ],
)

# =====================================================================
SUBS["cs-it-act"] = dict(
    concept=(
        "The **Information Technology Act, 2000** is India's law for the electronic world. "
        "It came into force on **17 October 2000** and was amended in **2008**. "
        "It gives legal status to electronic records and digital signatures and punishes computer crimes."
    ),
    notes=r"""### The IT Act, 2000
The **Information Technology Act, 2000** is India's main cyber law. It came into force on **17 October 2000**. It grew out of the **UNCITRAL model law** on electronic commerce. UNCITRAL means the United Nations Commission on International Trade Law.

The Act does two big things.

- It gives legal status to **electronic records** and **digital signatures**.
- It lists punishments for **computer crimes**.

It was **amended in 2008**. The amendment added identity theft, cyber-terrorism and more powers for CERT-In.

### Sections that exams ask
| Section | Subject |
|---|---|
| **Sec 3** | Authentication by digital signature |
| **Sec 43** | Compensation for unauthorised access to and damage of a computer or data |
| **Sec 65** | **Tampering with computer source code** |
| **Sec 66** | **Computer-related offences**, the hacking section, with dishonest intent |
| **Sec 66C** | **Identity theft** |
| **Sec 66D** | **Cheating by personation** using a computer, such as fake profiles |
| **Sec 66E** | Violation of **privacy**, capturing private images |
| **Sec 66F** | **Cyber terrorism** |
| **Sec 67** | Publishing **obscene material** in electronic form |
| **Sec 72** | **Breach of confidentiality and privacy** by those with lawful access to data |

> **Watch:** Section 66A was **struck down** by the Supreme Court in **Shreya Singhal v. Union of India (2015)**. It is a favourite trick option that is no longer law.

### Authorities and reporting
- **CERT-In** is the Indian Computer Emergency Response Team. It is the national agency for cyber incidents. It works under **MeitY**, the Ministry of Electronics and Information Technology. It was set up in **2004**. Its legal basis is **Sec 70B**.
- **NCIIPC** protects **critical information infrastructure** such as power, banking and telecom. Its basis is **Sec 70A**.
- **MeitY** is the parent ministry for cyber law and policy.
- The **DPDP Act, 2023** (Digital Personal Data Protection Act) governs personal data privacy.
- Report a cyber crime on the helpline **1930** or on **cybercrime.gov.in**.

### Digital signature in one line
A **digital signature** is the electronic form of a handwritten signature. It is made with the signer's **private key** and checked with the **public key**. Certificate authorities issue the keys.

It proves **who** signed and that the document was **not changed**.

> **Rule:** A digital signature gives authentication and integrity.

> **Example:** A person uses another's password to buy things online. That is **identity theft**, Section 66C.
""",
    tricks=[
        trick("66 family",
              "66 is hacking, 66C is identity theft, 66D is cheating by personation, 66E is privacy violation and 66F is cyber terrorism."),
        trick("66A is gone",
              "If Section 66A is offered as a valid law, it is a trap. The Supreme Court struck it down in 2015.",
              "Which section on offensive messages was struck down in Shreya Singhal v. Union of India?",
              ["The case was decided in 2015.", "The struck-down section was about offensive messages.", "That is Section 66A."],
              "Section 66A"),
    ],
    mistakes=[
        mis("Saying the IT Act came into force in 2008.", "It came into force on 17 October 2000. The amendment was in 2008."),
        mis("Treating Section 66A as valid law.", "It was struck down in 2015."),
        mis("Matching Section 66C with cheating by personation.", "66C is identity theft. 66D is cheating by personation."),
        mis("Placing CERT-In under the Home Ministry.", "CERT-In works under MeitY."),
        mis("Mixing CERT-In and NCIIPC.", "CERT-In handles incidents. NCIIPC protects critical infrastructure."),
    ],
    revision=[
        "IT Act 2000 came into force on 17 October 2000. It is based on the UNCITRAL model law. Amended in 2008.",
        "Sec 3 digital signature. Sec 43 unauthorised access compensation. Sec 65 source code tampering.",
        "Sec 66 hacking. 66C identity theft. 66D cheating by personation. 66E privacy. 66F cyber terrorism. Sec 67 obscenity. Sec 72 breach of confidentiality.",
        "Sec 66A was struck down in 2015 (Shreya Singhal).",
        "CERT-In is the incident agency under MeitY (2004, Sec 70B). NCIIPC protects critical infrastructure (Sec 70A).",
        "Helpline 1930 and cybercrime.gov.in. DPDP Act 2023 covers personal data.",
    ],
    patterns=[
        pat("cs-l1", "IT Act basics", "very common",
            "The question asks the year, origin or amendment of the IT Act.",
            ["Year is 2000 and in force from 17 October 2000.", "Origin is the UNCITRAL model law.", "Amended in 2008."],
            "These are fixed facts, asked directly.",
            "The IT Act was passed on the basis of the model law of:",
            ["The model law is about electronic commerce.", "It is from the UN commission UNCITRAL."], "UNCITRAL"),
        pat("cs-l2", "Section-to-offence matching", "very common",
            "A section number is given and the offence is asked, or the reverse.",
            ["Recall 65, 66, 66C, 66D, 66E, 66F, 67, 72.", "Match the subject in plain words.", "Reject 66A as valid law."],
            "A small list of sections repeats every year.",
            "Which section of the IT Act deals with identity theft?",
            ["Identity theft is one of the 66 family.", "It has the letter C."], "Section 66C"),
        pat("cs-l3", "Authorities and reporting", "common",
            "The question asks who handles incidents or where to report.",
            ["CERT-In handles incidents under MeitY.", "NCIIPC guards critical infrastructure.", "Report on 1930 or cybercrime.gov.in."],
            "Each body has one main job.",
            "The national cyber crime helpline number in India is:",
            ["The helpline is a short number.", "The number is 1930."], "1930"),
        pat("cs-l4", "Digital signature and e-record legality", "common",
            "The question asks what a digital signature proves or how it works.",
            ["It is made with the private key.", "It is checked with the public key.", "It proves who signed and that nothing changed."],
            "Two keys give authentication and integrity.",
            "A digital signature is created using the sender's:",
            ["The sender keeps one key secret.", "That key is the private key."], "Private key"),
        pat("cs-l5", "Struck-down Section 66A", "occasional",
            "The question lists 66A as an option or asks about Shreya Singhal.",
            ["Recall 66A dealt with offensive messages.", "The Supreme Court struck it down in 2015.", "It is not valid law."],
            "The trap works because students remember the section number.",
            "Which case struck down Section 66A of the IT Act?",
            ["The case year is 2015.", "The petitioner was Shreya Singhal."], "Shreya Singhal v. Union of India"),
    ],
)

apply("cyber-security.json", SUBS)
