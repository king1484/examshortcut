# -*- coding: utf-8 -*-
"""Topic 7: internet-email"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

T = {
  "id": "internet-email",
  "sectionId": "computer",
  "title": "Internet, Browsers & E-mail",
  "order": 7,
  "importance": "high",
  "avgQuestions": {"tier1": 0, "tier2": 3},
  "summary": "Internet history and structure, browsers vs search engines, URL/DNS, e-mail mechanics (To/CC/BCC, SMTP/POP3/IMAP) and India's e-banking rails (UPI, NEFT, RTGS). Full forms and the browser-vs-engine trap are asked every year.",
  "subtopics": [
    {
      "id": "ie-internet-basics",
      "title": "Internet, WWW, URL and DNS",
      "concept": """The **Internet** is a global 'network of networks' that grew out of **ARPANET** (1969, US DoD project; first nodes UCLA and Stanford). The **TCP/IP** protocol suite became its standard on 1 January 1983. The **World Wide Web** is one service running on the Internet - the system of interlinked web pages invented by **Tim Berners-Lee in 1989 at CERN** (with the first browser/editor, WorldWideWeb). Other services: e-mail, FTP, VoIP, streaming.

An **ISP** (Internet Service Provider - Jio, Airtel, BSNL) sells you connectivity and assigns an **IP address**. The **DNS (Domain Name System)** is the Internet's phonebook: it converts a name like www.ssc.gov.in into its numeric IP address (this translation is its exam definition).

**URL (Uniform Resource Locator)** parts: `https://www.ssc.gov.in:443/exams/index.html` = protocol + subdomain + domain + top-level domain (TLD .in) + port + path + file. Common TLDs: .com (commercial), .org (organisation), .edu (education), .gov (government), .in (India). **Bandwidth** = data-carrying capacity (bps/Kbps/Mbps); broadband = always-on high-speed access (fibre, DSL, 4G/5G).""",
      "formulas": [],
      "tricks": [
        {"title": "Internet vs WWW", "body": "The **Internet = hardware network** (cables, routers, servers); the **WWW = content service** (hyperlinked pages) riding on it. Invented later (1989) by ONE man - Berners-Lee; the Internet is older (1969 ARPANET).", "example": {"q": "Who invented the World Wide Web?", "solution": "Tim Berners-Lee (CERN, 1989)."}},
        {"title": "DNS = phonebook", "body": "DNS translates names to numbers - never 'assigns IPs' (that is DHCP) and never 'sends mail' (that is SMTP). Any question phrased 'converts domain names into IP addresses' = DNS.", "example": {"q": "What does DNS do?", "solution": "Resolves domain names into IP addresses."}}
      ],
      "mistakes": [
        "Treating WWW and the Internet as the same thing.",
        "Saying DNS assigns IP addresses - DHCP assigns; DNS resolves names to IPs.",
        "Dating the Internet to 1989 - that is the WWW; ARPANET was 1969."
      ]
    },
    {
      "id": "ie-browsers-search",
      "title": "Browsers, search engines, downloading and uploading",
      "concept": """A **browser** is the client software that fetches and displays web pages: Chrome, Microsoft Edge, Firefox, Safari, Opera. A **search engine** is a website that indexes the web and finds pages: Google, Bing, Yahoo, DuckDuckGo. (Google is NOT a browser; Chrome is NOT a search engine - the most repeated trap.)

A **webpage** is one document (HTML); a **website** is a collection of related pages; the **home page** is a site's opening page; a **portal** bundles services (news, mail, shopping). Pages are written in **HTML** (HyperText Markup Language) and linked by **hyperlinks**.

**Downloading** = copying files FROM a server to your device; **uploading** = sending files FROM your device TO a server (e.g. attaching to e-mail, posting videos). **Cookies** are small text files a site stores in your browser (sessions, preferences, tracking); the **cache** keeps copies of pages/images for faster reloads.

**Search tips:** quotes "exact phrase", minus -exclude, site:ssc.gov.in restricts to a site, OR widens. **Browser shortcuts:** Ctrl+T new tab, Ctrl+W close tab, Ctrl+Shift+T reopen closed tab, Ctrl+N window, Ctrl+Shift+N incognito/private, Ctrl+D bookmark, Ctrl+H history, Ctrl+J downloads, F5 refresh, Ctrl+F5 hard refresh, Ctrl+F find in page, Ctrl+L/Alt+D address bar, Ctrl+Enter adds www...com, Ctrl+plus/minus/0 zoom, F11 full screen, Ctrl+S save page, Ctrl+U view source, Ctrl+P print.""",
      "formulas": [],
      "tricks": [
        {"title": "Browser vs engine", "body": "**Browser = the car; search engine = the GPS you ask inside it.** Chrome/Edge/Firefox/Safari/Opera = cars. Google/Bing/Yahoo/DuckDuckGo = GPS. If it is a program you install, browser; if it is a website you visit, engine.", "example": {"q": "Which of these is a web browser - Google, Chrome, Yahoo, Bing?", "solution": "Chrome (the rest are search engines)."}},
        {"title": "Ctrl-letter browser map", "body": "**T**ab new, **W**ipe (close) tab, **D**rop a bookmark, **H**istory, **J**unk... no - **J**etisoned files (Downloads), **N**ormal window, **N+Shift** No-trace (incognito). F5 = freshen.", "example": {"q": "Shortcut to reopen a closed tab?", "solution": "Ctrl+Shift+T."}},
        {"title": "Up vs Down", "body": "**Upload = YOU send up** (to the server); **Download = server sends down** to you. The direction is always relative to YOUR machine.", "example": {"q": "Saving an e-mail attachment to your PC is?", "solution": "Downloading."}}
      ],
      "mistakes": [
        "Calling Google a browser or Chrome a search engine.",
        "Confusing Ctrl+H (history) with Ctrl+J (downloads) - H comes before J alphabetically: History before Downloads? No: History=H, Downloads=J is pure memory; the mnemonic is 'H = havens visited (history)'.",
        "Thinking cookies are viruses - cookies are passive text files (privacy issue, not malware)."
      ]
    },
    {
      "id": "ie-email-basics",
      "title": "E-mail: structure, To/CC/BCC and protocols",
      "concept": """**E-mail** (electronic mail) exchanges messages between accounts on mail servers. An address = `username@domain` - the **@** separates user from domain (ray.kiran@gmail.com).

**Fields:** **To** - primary recipients; **CC (Carbon Copy)** - secondary recipients visible to all; **BCC (Blind Carbon Copy)** - hidden recipients: the To/CC people cannot see who was BCC'd (use BCC for mass mails to protect privacy). Others: Subject, body, **attachment** (paperclip; files sent along, size-limited), signature, priority.

**Folders/actions:** Compose, Send, Reply (to sender), Reply All (sender + everyone on To/CC), Forward (pass on), Inbox (received), Outbox (pending), Sent, Drafts (unfinished), Spam/Junk (filtered mail), Trash/Bin. **MIME** (Multipurpose Internet Mail Extensions) is the standard that lets e-mail carry attachments, images and non-English text.

**Protocols:** **SMTP (Simple Mail Transfer Protocol, port 25)** - SENDS mail between clients and servers. **POP3 (Post Office Protocol v3, port 110)** - downloads mail to one device, usually removing it from the server. **IMAP (Internet Message Access Protocol, port 143)** - mail stays on the server and **syncs across many devices**. Webmail (Gmail in a browser) vs mail clients (Outlook, Thunderbird). Filters/labels sort automatically; autoresponders reply when you are away.""",
      "formulas": [],
      "tricks": [
        {"title": "CC vs BCC", "body": "**CC = Carbon Copy - Everyone sees. BCC = Blind - eyes covered**, so To/CC recipients cannot see the blind list. 'Who was secretly copied?' - nobody but the sender knows.", "example": {"q": "A receiver of the mail can see the addresses in which field(s)?", "solution": "To and CC - never BCC."}},
        {"title": "SMTP Sends, POP Picks, IMAP In-sync", "body": "**S**MTP = **S**end (outgoing). **P**OP3 = **P**ick up on one device (downloads, server emptied). **IMAP = In All devices** (server copy stays, everything syncs).", "example": {"q": "Which protocol lets you read the same mail on phone and laptop?", "solution": "IMAP."}},
        {"title": "@ = at", "body": "In ray@gmail.com the @ separates 'who' from 'where' - user at domain. Options without @, or with a space/comma, are dead giveaways.", "example": {"q": "Which character separates the username from the domain in e-mail?", "solution": "@ (at the rate)."}}
      ],
      "mistakes": [
        "Saying CC recipients are hidden - that is BCC; CC is fully visible.",
        "Making SMTP the receiving protocol - SMTP only sends; POP3/IMAP receive.",
        "Using Reply All when a mass mail was BCC'd - your reply reaches the sender, not the hidden list (and Reply-All storms are bad netiquette)."
      ]
    },
    {
      "id": "ie-ebanking",
      "title": "e-Banking and digital payments",
      "concept": """**e-Banking/net banking** = banking through the bank's secured website/app; **mobile banking** via apps; **ATM** (Automated Teller Machine) for cash, balance, mini-statement, PIN change.

**Payment systems (NPCI - National Payments Corporation of India, 2008 - runs most retail rails):**

| System | Nature | Key facts |
|---|---|---|
| NEFT | National Electronic Funds Transfer | Batch/half-hourly settlement; no minimum; available 24x7 since Dec 2019 |
| RTGS | Real Time Gross Settlement | **Minimum Rs. 2 lakh**; settles individually, real time; 24x7 since Dec 2020 |
| IMPS | Immediate Payment Service | Instant 24x7 transfers via mobile/MMID; no RTGS-style minimum |
| UPI | Unified Payments Interface (2016) | Instant app-to-app transfer using a VPA (name@bank); 24x7; BHIM app; QR payments |

**Security tokens:** **IFSC** (Indian Financial System Code) - 11 characters identifying the bank branch (e.g. SBIN0001234); **MICR** 9-digit cheque code; **OTP** (One Time Password) and **2FA** (two-factor authentication: something you know + something you receive/are). Safety rules: banks NEVER ask for PIN/OTP/password; check https + padlock before paying; avoid public Wi-Fi for transactions; unknown links = phishing (see cyber-security topic).""",
      "formulas": [],
      "tricks": [
        {"title": "NEFT vs RTGS", "body": "**RTGS = Really To Go, in batches of one, 2 lakh+** (real-time, gross = one-by-one, big amounts). **NEFT = Nice Easy Batches** (settlement in half-hourly batches, any amount).", "example": {"q": "Minimum amount for RTGS?", "solution": "Rs. 2 lakh."}},
        {"title": "IFSC 11", "body": "IFSC = **11 characters** (4 bank code + 0 + 6 branch code), used on NEFT/RTGS/UPI branch routing. MICR is the 9-digit cheque strip.", "example": {"q": "How many characters does an IFSC code have?", "solution": "11."}},
        {"title": "2FA two keys", "body": "Two-factor = password (know) + OTP/biometric (have/are). One stolen password is not enough - that is the whole point.", "example": {"q": "Entering a password followed by an SMS OTP is an example of?", "solution": "Two-factor authentication."}}
      ],
      "mistakes": [
        "Giving NEFT the 2-lakh minimum - RTGS has it; NEFT has no minimum.",
        "Saying IMPS is only for banks abroad - IMPS is an Indian instant retail rail.",
        "Sharing OTPs on calls 'from the bank' - real banks never ask; that is vishing."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Full form / abbreviation", "frequency": "very common", "howToSpot": "'URL/SMTP/IMAP/DNS full form', 'HTML is used for?'.", "approach": "Table recall; watch letter-order traps (HTML = HyperText Markup Language, not 'Marking')."},
    {"pattern": "Browser vs search engine trap", "frequency": "very common", "howToSpot": "Options mixing Chrome/Google/Bing/Firefox asking 'which is a browser?'.", "approach": "Installed program = browser (Chrome, Edge, Firefox, Safari, Opera); website service = engine (Google, Bing, Yahoo, DDG)."},
    {"pattern": "CC/BCC visibility scenario", "frequency": "common", "howToSpot": "'Recipients in which field are not visible to others?'", "approach": "To/CC visible to everyone; BCC hidden from all other recipients."},
    {"pattern": "Protocol-to-purpose matching", "frequency": "common", "howToSpot": "'Which protocol sends e-mail?', 'which receives and deletes from server?'.", "approach": "SMTP sends; POP3 downloads (single device); IMAP syncs (multi-device); HTTP serves pages; FTP moves files."},
    {"pattern": "E-banking rails and limits", "frequency": "common", "howToSpot": "'Minimum RTGS transfer?', 'UPI is operated by?'", "approach": "RTGS 2-lakh/real-time; NEFT batched/no minimum; UPI = NPCI, VPA-based instant."}
  ],
  "solvedExamples": [
    Q("ie-se01",
      "Which of the following is a web browser?",
      ["Google", "Bing", "Microsoft Edge", "DuckDuckGo"], 2,
      "Microsoft Edge is browser software that displays web pages. Google, Bing and DuckDuckGo are search engines - websites that index the web.",
      "Installed program = browser; website you search inside = engine. Edge/Chrome/Firefox/Safari/Opera are the usual browser options.",
      "easy", "ie-browsers-search", "browser vs search engine", 30),
    Q("ie-se02",
      "An e-mail is sent with the addresses of four colleagues placed in the BCC field. Which statement is correct?",
      ["All four can see each other's addresses", "The To recipients can see the BCC addresses", "The four receive copies whose addresses are hidden from other recipients", "BCC recipients do not receive attachments"], 2,
      "Blind Carbon Copy hides its recipient list: each BCC recipient gets the full mail (including attachments), but To/CC recipients cannot see who was blind-copied.",
      "'Blind' = nobody sees the list. The mail itself (with attachments) still arrives.",
      "medium", "ie-email-basics", "CC/BCC visibility", 40),
    Q("ie-se03",
      "Which protocol is used to SEND e-mail from a client to a mail server?",
      ["POP3", "IMAP", "SMTP", "HTTP"], 2,
      "SMTP (Simple Mail Transfer Protocol) handles outgoing mail. POP3 and IMAP fetch incoming mail (POP3 downloads, IMAP syncs), and HTTP serves web pages.",
      "S in SMTP = Send; the receiving protocols are POP3/IMAP.",
      "easy", "ie-email-basics", "protocol purpose", 30),
    Q("ie-se04",
      "Match: (a) NEFT (b) RTGS (c) UPI with (i) instant app-based transfer via VPA (ii) batch settlement, no minimum (iii) real-time gross settlement, minimum Rs. 2 lakh",
      ["a-ii, b-iii, c-i", "a-iii, b-ii, c-i", "a-ii, b-i, c-iii", "a-i, b-iii, c-ii"], 0,
      "NEFT settles in half-hourly batches with no minimum amount (a-ii); RTGS settles each transaction individually in real time with a Rs. 2-lakh floor (b-iii); UPI is the instant VPA/QR app rail run by NPCI (c-i).",
      "RTGS grabs the 2-lakh rule; NEFT is the batch rail; UPI is the phone-first instant one.",
      "medium", "ie-ebanking", "payment-system matching", 45)
  ],
  "practice": [
    Q("ie-q01",
      "The World Wide Web was invented in 1989 by:",
      ["Vint Cerf", "Tim Berners-Lee", "Bill Gates", "Larry Page"], 1,
      "Tim Berners-Lee proposed the WWW at CERN in 1989 and wrote the first browser. Vint Cerf co-designed TCP/IP; Larry Page co-founded Google.",
      "Web = Berners-Lee, 1989, CERN. Internet (1970s TCP/IP) = Cerf and Kahn.",
      "easy", "ie-internet-basics", "internet history", 30),
    Q("ie-q02",
      "ARPANET, the precursor of today's Internet, was launched in:",
      ["1949", "1959", "1969", "1979"], 2,
      "ARPANET went live in 1969 connecting UCLA and Stanford Research Institute, funded by the US Department of Defense.",
      "ARPANET 1969 - the 60s birth of the network.",
      "medium", "ie-internet-basics", "internet history", 35),
    Q("ie-q03",
      "The service that translates a domain name like www.ssc.gov.in into an IP address is:",
      ["DHCP", "DNS", "FTP", "ISP"], 1,
      "DNS (Domain Name System) resolves human-friendly names to numeric IP addresses. DHCP assigns IP addresses automatically; FTP transfers files; the ISP is your access provider.",
      "DNS = the Internet's phonebook: name in, number out.",
      "easy", "ie-internet-basics", "DNS function", 30),
    Q("ie-q04",
      "In the URL https://www.ssc.gov.in, the component '.in' is the:",
      ["Protocol", "Sub-domain", "Top-level domain (country code)", "File name"], 2,
      ".in is the country-code top-level domain for India. 'https' is the protocol, 'www' the sub-domain/host, 'ssc' the registered domain name.",
      "Read right to left: .in = TLD, .gov = second level, ssc = the name.",
      "medium", "ie-internet-basics", "URL anatomy", 40),
    Q("ie-q05",
      "Which of the following is NOT a web browser?",
      ["Opera", "Safari", "Yahoo", "Mozilla Firefox"], 2,
      "Yahoo is a web portal/search engine, not browser software. Opera, Safari and Firefox are browsers.",
      "Scan for the service/brand that you cannot install as a program - that is the odd one.",
      "easy", "ie-browsers-search", "browser vs search engine", 30),
    Q("ie-q06",
      "Receiving a file from a web server to your computer is called:",
      ["Uploading", "Downloading", "Streaming", "Hosting"], 1,
      "Downloading copies data from the server down to your device; uploading sends it the other way; streaming plays without saving the whole file.",
      "Down to you = download; up to the server = upload.",
      "easy", "ie-browsers-search", "download vs upload", 25),
    Q("ie-q07",
      "The browser shortcut to open a new tab is:",
      ["Ctrl+N", "Ctrl+T", "Ctrl+W", "Ctrl+Tab"], 1,
      "Ctrl+T opens a new tab; Ctrl+N a new window; Ctrl+W closes the current tab; Ctrl+Tab cycles through open tabs.",
      "T = Tab, N = window. Ctrl+W wipes the tab.",
      "easy", "ie-browsers-search", "browser shortcuts", 30),
    Q("ie-q08",
      "The standard that allows e-mails to carry attachments such as images and documents is:",
      ["SMTP", "MIME", "TCP", "UDP"], 1,
      "MIME (Multipurpose Internet Mail Extensions) extends e-mail to carry multimedia, attachments and non-ASCII text. SMTP is the transport protocol for mail.",
      "MIME = Multimedia Included (Mail Extensions).",
      "medium", "ie-email-basics", "email standards", 35),
    Q("ie-q09",
      "In an e-mail address kiran.ray@nic.in, the part before @ is the:",
      ["Domain name", "Username", "Protocol", "Password"], 1,
      "The format is username@domain: 'kiran.ray' is the user's mailbox name on the domain 'nic.in'.",
      "Who@where - the left side is the person.",
      "easy", "ie-email-basics", "email address structure", 25),
    Q("ie-q10",
      "Which e-mail protocol keeps messages on the server so that the same mailbox stays in sync across a phone, tablet and laptop?",
      ["POP3", "SMTP", "IMAP", "FTP"], 2,
      "IMAP stores mail on the server and synchronises state across devices. POP3 traditionally downloads and removes mail (single-device model), SMTP sends, FTP moves files.",
      "Many devices, one mailbox = IMAP.",
      "medium", "ie-email-basics", "POP3 vs IMAP", 40),
    Q("ie-q11",
      "The minimum amount that can be transferred through RTGS is:",
      ["Rs. 10,000", "Rs. 50,000", "Rs. 1 lakh", "Rs. 2 lakh"], 3,
      "RTGS (Real Time Gross Settlement) is meant for large-value transfers - the floor is Rs. 2 lakh, settled individually and instantly. NEFT carries smaller amounts in batches with no minimum.",
      "RTGS = 'Really Two-lakh Gross Settlement'.",
      "medium", "ie-ebanking", "payment system limits", 35),
    Q("ie-q12",
      "UPI, the instant real-time payment system, is developed and operated by:",
      ["RBI", ["SEBI"][0], "NPCI", "SBI"], 2,
      "UPI (2016) is built and operated by the National Payments Corporation of India (NPCI), the umbrella organisation for retail payments (it also runs IMPS, RuPay, BHIM). RBI regulates but does not operate UPI.",
      "NPCI runs the retail rails: UPI, IMPS, RuPay, AePS. RBI is the regulator.",
      "medium", "ie-ebanking", "digital payments", 35),
    Q("ie-q13",
      "An IFSC code used in electronic fund transfers contains how many characters?",
      ["9", "10", "11", "12"], 2,
      "The Indian Financial System Code is 11 characters: 4 letters for the bank, a zero, and 6 characters identifying the branch (e.g. SBIN0007245).",
      "IFSC = 11; MICR cheque code = 9 digits.",
      "medium", "ie-ebanking", "banking codes", 35),
    Q("ie-q14",
      "Small text files a website stores in your browser to remember sessions and preferences are called:",
      ["Cookies", "Breadcrumbs", "Applets", "Plugins"], 0,
      "Cookies hold site-specific data (login sessions, carts, preferences, tracking IDs). They are plain text files - not programs and not viruses.",
      "Website's memory of you = cookie.",
      "easy", "ie-browsers-search", "web concepts", 30),
    Q("ie-q15",
      "The keyboard shortcut to bookmark (favourite) the current page in all major browsers is:",
      ["Ctrl+B", "Ctrl+D", "Ctrl+M", "Ctrl+K"], 1,
      "Ctrl+D adds the current page to bookmarks/favourites. (Ctrl+B is bold in Office; in some browsers it toggles the bookmarks BAR, which is why the safe exam answer for bookmarking a page is Ctrl+D.)",
      "D = Drop a favourite: Ctrl+D.",
      "easy", "ie-browsers-search", "browser shortcuts", 30)
  ]
}

validate_and_dump_topic(T)
