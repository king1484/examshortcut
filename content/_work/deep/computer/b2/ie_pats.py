"""Internet & email pattern builders."""
from _lib import Sub


def build_internet_basics():
    S = Sub("ie-internet-basics")
    S.notes = __import__("ie_notes").IE_INTERNET_BASICS
    S.pattern("ie-n1", "Internet vs WWW and ARPANET history", "very common",
        "'The Internet is', 'WWW was invented by', 'the year of ARPANET' or a statement question mixing the Internet with the Web.",
        None,
        "1. Internet = the global network of networks, born from **ARPANET (1969)**.\n2. WWW = the hyperlinked-page service, invented by **Tim Berners-Lee, 1989, CERN**.\n3. The Web is a service ON the Internet (with e-mail, FTP); the two words are not interchangeable.",
        "The World Wide Web was invented in 1989 by:",
        "**Tim Berners-Lee** at CERN — the Internet itself is older, growing from ARPANET of 1969.")
    S.pattern("ie-n2", "URL anatomy", "very common",
        "A URL is given and a part is asked: the protocol, the domain, the country code, the path — or the full form of URL.",
        None,
        "1. Split at the slashes: https:// + domain + path.\n2. The part before the first single slash after the address is the protocol; the name before the first single slash is the domain; what follows is the path.\n3. Ending codes: .com commercial, .org organisation, .gov government, .edu education, .in India.",
        "In https://www.mysite.in/exams/ssc.html, the domain name is:",
        "**www.mysite.in** — https is the protocol, /exams/ssc.html is the path to the page.")
    S.pattern("ie-n3", "DNS, DHCP and ISP roles", "common",
        "'DNS converts ___ to ___', 'which server assigns IP addresses', 'who provides the Internet connection' — role-matching of the three servers.",
        None,
        "1. **DNS = Domain Name System**: domain name to IP address (the phonebook).\n2. **DHCP = Dynamic Host Configuration Protocol**: ASSIGNS IP addresses to devices.\n3. **ISP** sells the connection. The swap of DNS and DHCP jobs is the planted error.",
        "The server that converts a website name into its IP address is the:",
        "**DNS server** — assigning addresses is DHCP's job; resolving names is DNS's.")
    S.pattern("ie-n4", "Internet full forms and firsts", "common",
        "'Full form of HTTP/HTML/URL/ISP/VoIP' or wrongly matched pairs where one word of the expansion is changed.",
        None,
        "1. HTTP = HyperText Transfer Protocol; HTML = HyperText Markup Language; URL = Uniform Resource Locator; ISP = Internet Service Provider; VoIP = Voice over Internet Protocol; WWW = World Wide Web.\n2. Check word by word — 'Hyper Transfer Text Protocol' style traps are common.\n3. HTML is a MARKUP language, not a programming language.",
        "The full form of HTML is:",
        "**HyperText Markup Language** — the language in which web pages are written; it is a markup language, not a programming language.")
    return S


def build_browsers_search():
    S = Sub("ie-browsers-search")
    S.notes = __import__("ie_notes").IE_BROWSERS_SEARCH
    S.pattern("ie-s1", "Browser vs search engine", "very common",
        "'Which one is a browser/search engine?' or odd-one-out among Chrome, Firefox, Google, Safari — with Google planted among browsers.",
        None,
        "1. Browsers (programs): Chrome, Edge, Firefox, Safari, Opera.\n2. Search engines (websites): Google, Bing, Yahoo, DuckDuckGo.\n3. The classic trap: Google listed among browsers or Chrome listed among search engines.",
        "Which of the following is a WEB BROWSER?",
        "**Chrome** (like Edge, Firefox, Safari) — Google and Bing are search engines, programs that live inside browsers.")
    S.pattern("ie-s2", "Browser shortcut recall", "very common",
        "'Shortcut to open a new tab / history / downloads / bookmark' — with Ctrl+H and Ctrl+J swapped in the options.",
        None,
        "1. Ctrl+T new Tab, Ctrl+N new window, Ctrl+Shift+N incognito, **Ctrl+H History**, **Ctrl+J downloads**, Ctrl+D bookmark, Ctrl+F find on page, F5 refresh.\n2. H before J: History first, downloads (J) second.\n3. Ctrl+D is bookmark in browsers but fill-down in Excel — context decides.",
        "The keyboard shortcut that opens the downloads list in Chrome is:",
        "**Ctrl+J** — Ctrl+H opens History instead.")
    S.pattern("ie-s3", "Download, upload, cache and cookies", "common",
        "'Downloading means', 'what does the browser cache store', 'cookies are ___' — direction or definition matching.",
        None,
        "1. **Download** = server to your device; **upload** = your device to server; streaming = play while it arrives.\n2. Cache = copies kept for faster revisits; history = list of visits.\n3. **Cookies = small text files** a site saves (login, preferences, tracking) — passive files, not viruses.",
        "Receiving a file from a web server to your computer is called:",
        "**Downloading** — sending one the other way is uploading.")
    S.pattern("ie-s4", "Incognito and privacy features", "common",
        "'Incognito mode ___', 'private browsing saves ___' — what is forgotten, what is NOT hidden.",
        None,
        "1. Incognito/private windows **forget history and cookies after closing** — good for shared computers.\n2. They do NOT hide you from websites, the office network or the ISP, and bookmarks you make stay.\n3. Cookies cleared = stored logins lost in that window.",
        "Which statement about Chrome's Incognito mode is TRUE?",
        "**Browsing history and cookies of that window are deleted when it closes** — but your ISP and the websites still see the visit.")
    return S


def build_email_basics():
    S = Sub("ie-email-basics")
    S.notes = __import__("ie_notes").IE_EMAIL_BASICS
    S.pattern("ie-m1", "CC/BCC visibility scenario", "very common",
        "A mail-sending scenario asks who can see whom: 'addresses in BCC are visible to ___', or the field to use so receivers don't see each other.",
        None,
        "1. **CC receivers are visible to everyone** (To and CC).\n2. **BCC receivers are hidden** — To/CC people never see them; BCC people see To/CC but not each other.\n3. Bulk mails to strangers go in BCC to protect addresses.",
        "Ravi sends a mail to 200 customers with all addresses in BCC. If a customer presses Reply All, the reply goes to:",
        "**Only the sender** — the BCC list is hidden and other receivers are not disclosed.")
    S.pattern("ie-m2", "Protocol direction: SMTP vs POP3 vs IMAP", "very common",
        "'Protocol used to SEND e-mail', 'which protocol downloads mail to one device', 'which protocol keeps mail synced on the server' — direction matching.",
        None,
        "1. **SMTP = sending** (Simple Mail Transfer Protocol).\n2. **POP3 = receiving, downloads to one device** (usually removes from server).\n3. **IMAP = receiving, stays on server, syncs everywhere**.\n4. Reversed pairs (SMTP as receiver, POP as sender) are the standard traps.",
        "Which protocol is used to SEND an e-mail from the client to the mail server?",
        "**SMTP** — Simple Mail Transfer Protocol. POP3 and IMAP only fetch incoming mail.")
    S.pattern("ie-m3", "E-mail address and fields anatomy", "common",
        "'In rani@gmail.com, the part before @ is', 'what separates user and domain', or identification of Subject/Attachment/Signature fields.",
        None,
        "1. Address = **username @ domain**; @ is the separator ('at').\n2. Subject = one-line summary; attachment = clipped file (paperclip); signature = fixed sign-off.\n3. The domain after @ names the mail service (gmail.com).",
        "In the address kiran.verma@yahoo.in, the username is:",
        "**kiran.verma** — the @ separates the username from the domain (yahoo.in).")
    S.pattern("ie-m4", "Reply, Reply All, Forward, Spam, Draft", "common",
        "A scenario on which action answers whom, or the meaning of spam / draft / forwarding.",
        None,
        "1. **Reply** = only to the sender; **Reply All** = sender plus everyone in To/CC; **Forward** = passes the mail to new receivers.\n2. **Spam** = junk mail, parked in the Spam folder by the filter.\n3. **Draft** = written but not sent yet.",
        "Swati received a circular sent to her whole class. She wants only the teacher to read her answer. She should use —",
        "**Reply** (to the sender) — Reply All would reach every classmate who was on To/CC.")
    return S


def build_ebanking():
    S = Sub("ie-ebanking")
    S.notes = __import__("ie_notes").IE_EBANKING
    S.pattern("ie-b1", "NEFT / RTGS / IMPS / UPI comparison", "very common",
        "'Which rail has a minimum of 2 lakh', 'which is instant 24x7 by UPI ID', 'full form of NEFT/RTGS/UPI' — the rails' styles mixed in options.",
        None,
        "1. **NEFT** = batches, half-hourly slots, NO minimum.\n2. **RTGS** = real-time gross settlement, **minimum 2,00,000 rupees**.\n3. **IMPS** = instant inside banking apps, 24x7.\n4. **UPI** = instant app-to-app by UPI ID or QR, built by **NPCI**.\n5. The recurring trap: giving NEFT the 2-lakh minimum (it belongs to RTGS).",
        "A customer must transfer 25,00,000 rupees immediately, transaction by transaction. The suitable system is:",
        "**RTGS** — real-time, transaction-wise, built for high-value transfers (minimum 2 lakh).")
    S.pattern("ie-b2", "OTP, PIN, CVV and 2FA safety", "very common",
        "'Full form of OTP/CVV', 'a caller from the bank asks your OTP — what do you do', or which combination makes an e-transaction two-factor.",
        None,
        "1. **OTP = One Time Password** — one transaction, one use, short life.\n2. **CVV = Card Verification Value** — the 3-digit number on the card's back.\n3. **PIN = Personal Identification Number**.\n4. **2FA** = password PLUS OTP/biometric — two independent locks.\n5. Banks NEVER ask for OTP/PIN/CVV by call, SMS or mail — the asker is a fraudster.",
        "A caller says he is from your bank and asks for the OTP that just arrived. You should:",
        "**Refuse and disconnect — real banks never ask for OTPs**; this is a vishing fraud attempt.")
    S.pattern("ie-b3", "IFSC, MICR and SWIFT codes", "common",
        "'IFSC has how many characters', 'which code is used for international transfer', 'the 9-digit code on a cheque is'.",
        None,
        "1. **IFSC = Indian Financial System Code, 11 characters** — 4 letters (bank) + 0 + 6 (branch); used in NEFT/RTGS/IMPS.\n2. **MICR = 9 digits**, the magnetic-ink strip at the cheque's bottom.\n3. **SWIFT** = the code system for INTERNATIONAL transfers.",
        "The number of characters in an IFSC code is:",
        "**11** — e.g. SBIN0001234: SBIN (State Bank of India) + 0 + 001234 (branch).")
    S.pattern("ie-b4", "ATM and net-banking basics", "common",
        "'ATM stands for', 'which of these can be done at an ATM', 'mobile banking vs net banking' — service identification.",
        None,
        "1. **ATM = Automated Teller Machine** — cash, balance, mini statement, PIN change, 24x7.\n2. Net banking = bank's website; mobile banking = bank's app.\n3. ATM transactions need the card + PIN; the PIN is never written on the card.",
        "The full form of ATM is:",
        "**Automated Teller Machine** — the 24x7 machine for cash withdrawal, balance enquiry and mini statements.")
    return S
