"""Readable rewrite of Computer > Internet & E-mail (all 4 subtopics).

Plain English, short sentences, tables for facts. Every fact is kept from the old notes.
Old pattern ids are kept; new ids continue each prefix (ie-n5.., ie-s5.., ie-m5.., ie-b5..).
Run: python internet_email.py  (patches content/core/topics/computer/internet-email.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "computer" / "internet-email.json"


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


SUBS = {}

# =====================================================================
# 1. Internet, WWW, URL and DNS
# =====================================================================
SUBS["ie-internet-basics"] = dict(
    concept=(
        "The **Internet** is a worldwide network of networks. It grew out of **ARPANET** (1969). "
        "The **World Wide Web** is one service on the Internet: linked web pages, invented by **Tim Berners-Lee** in 1989 at CERN. "
        "A **URL** is the address of a page. **DNS** turns a name like ssc.gov.in into a numeric IP address."
    ),
    notes=r"""### Internet and the Web
The **Internet** is a worldwide **network of networks**. Millions of computers and phones connect through it and swap data.

- It grew out of **ARPANET**, a 1969 project of the US Department of Defense.
- The first two ARPANET nodes were at **UCLA** and **Stanford**.
- **TCP/IP** became its standard protocol suite on 1 January 1983.

The **World Wide Web (WWW)** is a **service that runs on the Internet**. It is a set of linked pages that you read in a browser. **Tim Berners-Lee** invented it in **1989** at **CERN**. E-mail, FTP, VoIP and streaming are other services on the same Internet.

> **Tip:** Internet is the road system. The Web is one kind of traffic on it. The Internet is older (1969); the Web came later (1989).

### Parts of a URL
A **URL (Uniform Resource Locator)** is the address of one page or file. Read it from left to right.

| Part | Example | Meaning |
|---|---|---|
| Protocol | HTTPS | The rules used for the talk. HTTPS is the secure, encrypted version. |
| Subdomain | www | The host prefix. |
| Domain | ssc.gov.in | The name of the server. |
| Top-level domain (TLD) | .in | The ending. It shows the type or country. |
| Port | 443 | The door number on the server. |
| Path | /exams/ | The folder on the server. |
| File | index.html | The exact page. |

### Common domain endings
| Ending | Meaning |
|---|---|
| .com | commercial |
| .org | organisation |
| .edu | education |
| .gov | government |
| .in | India |

### DNS, DHCP and ISP
Three helpers make a connection work. Each has one job.

| Helper | Job |
|---|---|
| **ISP** (Internet Service Provider) | Sells you the connection. Examples: Jio, Airtel, BSNL. |
| **DNS** (Domain Name System) | Turns a domain name into an IP address. It is the phonebook of the Internet. |
| **DHCP** | Assigns an IP address to your device. |
| **Web server** | Stores pages and sends them to browsers. |

An **IP address** is the number that machines use. IPv4 has four blocks, each from 0 to 255. One example is 142.250.183.14.

> **Watch:** DNS resolves names. DHCP assigns addresses. Exams swap these two on purpose.

### What happens when you open a page
1. You type a URL in the browser.
2. **DNS** finds the IP address of that domain.
3. Your request travels over **TCP/IP** to the **web server**.
4. The server sends the page back.
5. The browser draws the page from its HTML.

Every DNS, URL or ISP question is one stop on this trip.

### Small facts that repeat
- **Bandwidth** is how much data a link can carry. It is measured in bps, Kbps or Mbps.
- **Broadband** is always-on, high-speed access, such as fibre, DSL, 4G or 5G.
- **VoIP** (Voice over Internet Protocol) carries phone calls over the Internet.
- A **website** is a set of related pages under one domain.
- A **web portal** gathers many services on one page.
""",
    tricks=[
        trick("Internet vs WWW",
              "The **Internet** is the hardware network of cables, routers and servers. The **WWW** is the content service of linked pages on top of it. The Internet is older (1969). The Web is 1989.",
              "Who invented the World Wide Web?", ["The Web is the service of linked pages.", "It was created in 1989 at CERN."], "Tim Berners-Lee"),
        trick("DNS is the phonebook",
              "DNS turns names into numbers. It never assigns IPs (that is DHCP) and never sends mail (that is SMTP). Any line that says 'converts domain names into IP addresses' means DNS.",
              "What does DNS do?", ["Look for the words name and IP address.", "Name to number is the phonebook job."], "It resolves domain names into IP addresses."),
    ],
    mistakes=[
        mis("Treating WWW and the Internet as the same thing.", "The Internet is the network. The WWW is one service that runs on it."),
        mis("Saying DNS assigns IP addresses.", "DHCP assigns addresses. DNS resolves names to IP addresses."),
        mis("Dating the Internet to 1989.", "1989 is the Web (Berners-Lee). ARPANET was 1969."),
        mis("Calling HTML a programming language.", "HTML is a markup language. It describes the page."),
        mis("Reading HTTP as the secure protocol.", "HTTPS is the secure, encrypted one."),
    ],
    revision=[
        "Internet = network of networks, from ARPANET (1969). WWW = linked pages, Berners-Lee, 1989, CERN.",
        "TCP/IP became the Internet standard on 1 January 1983.",
        "URL = protocol + subdomain + domain + TLD + port + path + file.",
        "DNS: name to IP. DHCP: gives an IP. ISP: sells the connection.",
        "TLDs: .com commercial, .org organisation, .edu education, .gov government, .in India.",
        "HTTP = HyperText Transfer Protocol. HTML = HyperText Markup Language. VoIP = calls over the Internet.",
    ],
    patterns=[
        pat("ie-n1", "Internet vs WWW and ARPANET history", "very common",
            "The words 'The Internet is', 'WWW was invented by', 'the year of ARPANET', or a statement that mixes the Internet with the Web.",
            ["Match the Internet with ARPANET, 1969.", "Match the WWW with Berners-Lee, 1989, CERN.", "Remember the Web is a service on the Internet.", "Reject any option that treats the two words as equal."],
            "The two dates and the two names are the only facts asked.",
            "The World Wide Web was invented in 1989 by:",
            ["1989 is the Web, not the Internet.", "The Web came from CERN."],
            "Tim Berners-Lee at CERN. The Internet is older, from ARPANET (1969)."),
        pat("ie-n2", "URL anatomy", "very common",
            "A URL is given and one part is asked: protocol, domain, country code or path. Or the full form of URL.",
            ["Split the URL at the slashes.", "The start up to :// is the protocol.", "The name right after it is the domain.", "Everything after the domain is the path."],
            "Each part of a URL has one fixed position.",
            "In https://www.mysite.in/exams/ssc.html, the domain name is:",
            ["https is the protocol.", "/exams/ssc.html is the path.", "What is left is www.mysite.in."],
            "www.mysite.in"),
        pat("ie-n3", "DNS, DHCP and ISP roles", "common",
            "'DNS converts ___ to ___', 'which server assigns IP addresses', 'who provides the Internet connection'.",
            ["Find the verb in the question.", "Convert or resolve a name means DNS.", "Assign an IP address means DHCP.", "Provide the connection means ISP."],
            "Each helper has one job, and options swap the jobs.",
            "The server that converts a website name into its IP address is the:",
            ["The job is name to IP address.", "That is DNS, not DHCP."],
            "DNS server"),
        pat("ie-n4", "Internet full forms and firsts", "common",
            "'Full form of HTTP, HTML, URL, ISP, VoIP' or a pair where one word of the expansion is changed.",
            ["Recall the full form word by word.", "Compare it with each option.", "Reject options with swapped words like 'Hyper Transfer Text'.", "Remember HTML is a markup language."],
            "One changed word makes the option wrong.",
            "The full form of HTML is:",
            ["H stands for HyperText.", "M and L stand for Markup Language."],
            "HyperText Markup Language. It is a markup language, not a programming language."),
        pat("ie-n5", "Domain endings (TLD)", "common",
            "A domain such as .edu, .gov or .org is given and you must name its type. Or the reverse.",
            ["Look at the last part of the domain.", "Match it to its meaning.", "Check the country code .in for India."],
            "Each TLD has one standard meaning.",
            "A website whose address ends in .gov most likely belongs to:",
            ["The ending is .gov.", ".gov means government."],
            "A government body"),
        pat("ie-n6", "Order of steps to open a page", "occasional",
            "'What happens first when you type a URL?' or 'arrange these steps'.",
            ["Start with the URL typed in the browser.", "Next comes the DNS lookup.", "Then the request goes to the web server.", "Last, the browser shows the page."],
            "The IP address must be known before a request can be sent.",
            "After you type a URL, the browser first asks which service for the server's IP address?",
            ["Names are turned into IP addresses by DNS.", "This happens before the request is sent."],
            "DNS"),
    ],
)

# =====================================================================
# 2. Browsers, search engines, downloading and uploading
# =====================================================================
SUBS["ie-browsers-search"] = dict(
    concept=(
        "A **browser** is the program that fetches and shows web pages, such as Chrome, Edge, Firefox, Safari and Opera. "
        "A **search engine** is a website that finds pages, such as Google, Bing, Yahoo and DuckDuckGo. "
        "**Download** means server to your device. **Upload** means your device to a server."
    ),
    notes=r"""### Browser or search engine
A **browser** is a program on your device. It fetches and shows web pages.

- Browsers: **Chrome, Microsoft Edge, Firefox, Safari, Opera**.
- Internet Explorer is retired.

A **search engine** is a website. It keeps an index of the web and finds pages for your words.

- Search engines: **Google, Bing, Yahoo, DuckDuckGo**.

> **Watch:** Google is a search engine. Chrome is a browser. Exams put Google among browsers on purpose.

### Web words
| Word | Meaning |
|---|---|
| Webpage | One document, written in HTML |
| Website | A set of related pages |
| Home page | The opening page of a site |
| Portal | One site that bundles many services, such as news, mail and shopping |
| Hyperlink | A link that jumps to another page |

**HTML** is HyperText Markup Language. It builds the page. Hyperlinks join the pages.

### What the browser keeps
| Tool | What it keeps |
|---|---|
| **History** | Every page you visited |
| **Bookmarks** | Pages you saved for a quick return |
| **Cache** | Copies of pages and pictures, so revisits load faster |
| **Cookies** | Small text files a site stores, for logins, preferences and tracking |

Cookies are **not viruses**. They are passive text files. The worry is privacy.

**Incognito (private) mode** forgets history and cookies when you close the window. It is good for shared computers. It does **not** hide you from websites or the ISP.

### Browser shortcuts
| Key | Job |
|---|---|
| Ctrl+T | New tab |
| Ctrl+W | Close tab |
| Ctrl+Shift+T | Reopen the closed tab |
| Ctrl+N | New window |
| Ctrl+Shift+N | New incognito window |
| Ctrl+D | Bookmark the page |
| Ctrl+H | History |
| Ctrl+J | Downloads |
| F5 or Ctrl+R | Refresh |
| Ctrl+F5 | Hard refresh |
| Ctrl+F | Find on the page |
| Ctrl+L or Alt+D | Go to the address bar |
| Ctrl+Enter | Adds the www prefix and .com ending |
| Ctrl + plus, minus, 0 | Zoom in, out, reset |
| F11 | Full screen |
| Ctrl+S, Ctrl+U, Ctrl+P | Save page, view source, print |

> **Tip:** H is for History. J is the Just-downloaded list. The two are often swapped in options.

### Download, upload and streaming
- **Download:** a file moves from a server **to your device**. Songs, PDFs and apps are examples.
- **Upload:** a file moves from **your device to a server**. Attaching a form or posting a video are examples.
- **Streaming:** you play the data as it arrives, without saving the whole file first.

The direction is always seen from **your** machine.

### Searching well
Type keywords, not full sentences. These tricks narrow the results.

| Trick | Effect |
|---|---|
| "exact phrase" | Finds the words together |
| minus sign, as in -word | Removes a word |
| site:ssc.gov.in | Searches only that site |
| OR | Widens the search |

The engine ranks pages by relevance. It does not check whether they are true.
""",
    tricks=[
        trick("Browser is the car, engine is the GPS",
              "Chrome, Edge, Firefox, Safari and Opera are browsers, the program you install. Google, Bing, Yahoo and DuckDuckGo are search engines, the websites you visit inside a browser.",
              "Which of these is a web browser: Google, Chrome, Yahoo, Bing?", ["Google, Yahoo and Bing are search engines.", "Chrome is the program that opens pages."], "Chrome"),
        trick("Ctrl-letter map",
              "T is a new Tab. W closes the tab. D is a Bookmark (Drop a pin). H is History. J is the downloads list. N is a new window, and Shift+N makes it incognito. F5 refreshes.",
              "Which shortcut reopens a closed tab?", ["Ctrl+T opens a new tab.", "Adding Shift with T brings back the closed one."], "Ctrl+Shift+T"),
        trick("Up or down",
              "**Upload** sends a file up to the server. **Download** brings it down to you. The direction is always relative to your machine.",
              "Saving an e-mail attachment to your PC is called:", ["The file moves from the server to your PC."], "Downloading"),
    ],
    mistakes=[
        mis("Calling Google a browser or Chrome a search engine.", "Chrome is the browser. Google is the search engine you use inside it."),
        mis("Mixing up Ctrl+H and Ctrl+J.", "Ctrl+H is History. Ctrl+J is the downloads list."),
        mis("Thinking cookies are viruses.", "Cookies are passive text files. They are a privacy issue, not malware."),
        mis("Believing incognito hides you from the ISP.", "Incognito only forgets history and cookies on your device."),
        mis("Reading upload and download from the server's side.", "Judge the direction from your own device."),
    ],
    revision=[
        "Chrome, Edge, Firefox, Safari, Opera are browsers. Google, Bing, Yahoo, DuckDuckGo are search engines.",
        "Ctrl+T new tab, Ctrl+W close tab, Ctrl+Shift+T reopen tab, Ctrl+N window, Ctrl+Shift+N incognito.",
        "Ctrl+D bookmark, Ctrl+H history, Ctrl+J downloads, Ctrl+F find, F5 refresh, Ctrl+F5 hard refresh.",
        "Cache = copies for speed. Cookies = site text files (privacy, not viruses).",
        "Download = server to you. Upload = you to server. Streaming = play as it arrives.",
        "Search tricks: quotes for an exact phrase, minus to exclude, site: to limit, OR to widen.",
    ],
    patterns=[
        pat("ie-s1", "Browser vs search engine", "very common",
            "'Which is a browser or a search engine?' or an odd-one-out list of Chrome, Firefox, Google and Safari.",
            ["List the browsers: Chrome, Edge, Firefox, Safari, Opera.", "List the engines: Google, Bing, Yahoo, DuckDuckGo.", "Pick the name from the group the question asks for."],
            "Google planted among browsers is the classic trap.",
            "Which of the following is a web browser?",
            ["Bing and Google are search engines.", "Chrome is an installed program that opens pages."],
            "Chrome"),
        pat("ie-s2", "Browser shortcut recall", "very common",
            "'Shortcut to open a new tab, history, downloads or bookmark', with Ctrl+H and Ctrl+J swapped in the options.",
            ["Recall the letter: T tab, N window, D bookmark, H history, J downloads.", "Add Shift for the incognito or reopen versions.", "Watch for Excel, where Ctrl+D means fill down."],
            "One letter decides each shortcut.",
            "The shortcut that opens the downloads list in Chrome is:",
            ["Downloads is the J key.", "Ctrl+H opens History instead."],
            "Ctrl+J"),
        pat("ie-s3", "Download, upload, cache and cookies", "common",
            "'Downloading means', 'what does the cache store', 'cookies are ___'.",
            ["Check the direction of the file first.", "Cache means copies kept for speed.", "Cookies are small text files, not viruses."],
            "Each word has one plain definition.",
            "Receiving a file from a web server to your computer is called:",
            ["The file moves toward your device.", "That direction is download."],
            "Downloading. The opposite direction is uploading."),
        pat("ie-s4", "Incognito and privacy features", "common",
            "'Incognito mode ___', 'private browsing saves ___'. Sort what is forgotten from what is not hidden.",
            ["Recall that history and cookies vanish on closing.", "Recall that websites, the office network and the ISP still see you.", "Bookmarks you make stay."],
            "Incognito cleans your device, not the network.",
            "Which statement about Chrome's Incognito mode is TRUE?",
            ["It forgets history and cookies after closing.", "It does not hide the visit from the ISP or the website."],
            "Browsing history and cookies of that window are deleted when it closes."),
        pat("ie-s5", "Search operators", "occasional",
            "A search box example with quotes, a minus sign, site: or OR, and a question on its effect.",
            ["Quotes keep words together.", "A minus sign removes a word.", "site: limits to one website.", "OR widens the search."],
            "Each symbol changes the search in one fixed way.",
            "Which search text restricts results to the website ssc.gov.in?",
            ["The site: operator limits results to one website.", "It goes before the domain."],
            "site:ssc.gov.in"),
        pat("ie-s6", "Web terms: webpage, website, portal", "occasional",
            "'A collection of related pages is', 'the opening page of a site is', 'a site bundling news and mail is'.",
            ["One document is a webpage.", "A set of pages is a website.", "The opening page is the home page.", "A site with many services is a portal."],
            "The words differ by size and purpose.",
            "A collection of related web pages under one domain is called a:",
            ["One page is a webpage.", "Many related pages together are a website."],
            "Website"),
    ],
)

# =====================================================================
# 3. E-mail
# =====================================================================
SUBS["ie-email-basics"] = dict(
    concept=(
        "**E-mail** sends messages between accounts on mail servers. An address is username@domain, and **@** separates the two. "
        "**CC** copies are visible to all. **BCC** copies are hidden. "
        "**SMTP** sends mail. **POP3** downloads it to one device. **IMAP** keeps it on the server and syncs all devices."
    ),
    notes=r"""### What e-mail is
**E-mail (electronic mail)** sends messages between accounts on **mail servers**.

An address has two parts joined by **@** (read "at"): username, then domain. Take ray.kiran@gmail.com.

- **ray.kiran** is the username.
- **gmail.com** is the domain, the mail service.

Gmail, Outlook and Yahoo Mail are mail services.

### Fields of a new mail
| Field | Meaning |
|---|---|
| **To** | The main receivers |
| **CC** (Carbon Copy) | Extra receivers. Everyone sees all To and CC addresses. |
| **BCC** (Blind Carbon Copy) | Hidden receivers. To and CC people cannot see them. |
| **Subject** | A one-line summary |
| **Attachment** | A file sent along, shown by a paperclip. Size is limited. |
| **Signature** | A fixed sign-off block |

> **Rule:** CC is visible to all. BCC is hidden from the To and CC receivers. Use BCC for mass mails to protect addresses.

If a mail was sent to a hidden BCC list, Reply All reaches only the sender.

### The three protocols
| Protocol | Job | How it works |
|---|---|---|
| **SMTP** (Simple Mail Transfer Protocol), port 25 | Sends mail | Pushes mail from client to server, and between servers |
| **POP3** (Post Office Protocol v3), port 110 | Receives mail | Downloads to one device, usually removing it from the server |
| **IMAP** (Internet Message Access Protocol), port 143 | Receives mail | Mail stays on the server and syncs on all devices |

**MIME** (Multipurpose Internet Mail Extensions) lets e-mail carry attachments, images and non-English text.

> **Tip:** SMTP Sends. POP Picks up on one device. IMAP is In sync everywhere.

### Mail actions
- **Compose** writes a new mail. **Send** sends it.
- **Reply** answers only the sender.
- **Reply All** answers the sender and everyone in To and CC.
- **Forward** passes the mail to new people.

### Mail folders
| Folder | Holds |
|---|---|
| Inbox | Received mail |
| Outbox | Mail waiting to be sent |
| Sent | Mail already sent |
| Drafts | Unfinished mail |
| Spam or Junk | Mail the filter marked as junk |
| Trash or Bin | Deleted mail |

Never click links in spam.

### The journey of one mail
1. You press Send. Your mail server uses **SMTP** to push the mail to the server named after the @ domain.
2. The receiver's server keeps it in her mailbox.
3. Her app fetches it with **IMAP** or **POP3**.

**Webmail** is a mail service used in a browser, like Gmail. A **mail client** is an installed app, like Outlook or Thunderbird. **Filters and labels** sort mail automatically. **Autoresponders** reply for you when you are away.
""",
    tricks=[
        trick("CC vs BCC",
              "**CC** is a Carbon Copy that everybody sees. **BCC** is Blind, so To and CC receivers cannot see the blind list.",
              "The receiver of a mail can see the addresses in which fields?", ["To and CC are shown to all.", "BCC is hidden."], "To and CC, never BCC"),
        trick("SMTP sends, POP picks, IMAP in-sync",
              "**S**MTP = **S**end (outgoing). **P**OP3 = **P**ick up on one device (server copy usually removed). **IMAP** = in all devices (server copy stays, everything syncs).",
              "Which protocol lets you read the same mail on phone and laptop?", ["The mail must stay on the server.", "That is IMAP."], "IMAP"),
        trick("At sign",
              "In ray@gmail.com the @ separates who from where: user at domain. An option with no @, or with a space or comma, is wrong.",
              "Which character separates the username from the domain in an e-mail address?", ["The character reads as 'at'."], "@"),
    ],
    mistakes=[
        mis("Saying CC receivers are hidden.", "BCC is hidden. CC is fully visible."),
        mis("Making SMTP the receiving protocol.", "SMTP only sends. POP3 and IMAP receive."),
        mis("Thinking Reply All reaches the hidden BCC list.", "Reply All reaches the sender and the To and CC people. BCC stays hidden."),
        mis("Thinking POP3 keeps mail synced on many devices.", "IMAP does that. POP3 downloads to one device."),
        mis("Using Reply when the whole group must see your answer.", "Reply goes only to the sender. Use Reply All for everyone."),
    ],
    revision=[
        "Address = username @ domain. The @ separates the two.",
        "CC is visible to all. BCC is hidden from To and CC receivers.",
        "SMTP sends (port 25). POP3 downloads to one device (port 110). IMAP syncs everywhere (port 143).",
        "Reply = sender only. Reply All = sender plus To and CC. Forward = new receivers.",
        "Folders: Inbox, Outbox, Sent, Drafts, Spam, Trash.",
        "MIME lets e-mail carry attachments, images and non-English text.",
    ],
    patterns=[
        pat("ie-m1", "CC/BCC visibility scenario", "very common",
            "A sending scenario asks who can see whom, or which field to use so receivers do not see each other.",
            ["CC receivers are visible to everyone.", "BCC receivers are hidden from To and CC people.", "BCC receivers do not see each other either.", "Use BCC for bulk mails to protect addresses."],
            "The hidden list stays hidden even when someone replies.",
            "Ravi sends a mail to 200 customers with all addresses in BCC. If a customer presses Reply All, the reply goes to:",
            ["BCC addresses are hidden from the other receivers.", "So Reply All has only the sender to answer."],
            "Only the sender"),
        pat("ie-m2", "Protocol direction: SMTP vs POP3 vs IMAP", "very common",
            "'Protocol used to SEND e-mail', 'downloads mail to one device', 'keeps mail synced on the server'.",
            ["Sending means SMTP.", "Downloading to one device means POP3.", "Staying on the server and syncing means IMAP.", "Reject options with the roles reversed."],
            "Each protocol has one direction, and options swap them.",
            "Which protocol is used to SEND an e-mail from the client to the mail server?",
            ["Sending is done by one protocol only.", "POP3 and IMAP only fetch incoming mail."],
            "SMTP (Simple Mail Transfer Protocol)"),
        pat("ie-m3", "E-mail address and fields anatomy", "common",
            "'In rani@gmail.com, the part before @ is', 'what separates user and domain', or naming Subject, Attachment or Signature.",
            ["Split the address at @.", "Before @ is the username.", "After @ is the domain.", "Match the field to its plain meaning."],
            "The @ is the only separator.",
            "In the address kiran.verma@yahoo.in, the username is:",
            ["Split at the @ sign.", "The part before it is the username."],
            "kiran.verma"),
        pat("ie-m4", "Reply, Reply All, Forward, Spam, Draft", "common",
            "A scenario about who receives your answer, or the meaning of spam, draft or forward.",
            ["Reply goes to the sender only.", "Reply All goes to the sender and all in To and CC.", "Forward passes the mail to new receivers.", "A draft is written but not sent."],
            "Choose the action by who must read your answer.",
            "Swati received a circular sent to her whole class. She wants only the teacher to read her answer. She should use:",
            ["The teacher is the sender.", "Only Reply goes to the sender alone."],
            "Reply"),
        pat("ie-m5", "Mail folders", "common",
            "'Unsent mail is kept in', 'mail waiting to be sent is in', 'junk mail goes to'.",
            ["Received mail is in the Inbox.", "Waiting to be sent is the Outbox.", "Unfinished mail is in Drafts.", "Filtered junk is in Spam."],
            "Each folder holds one state of a mail.",
            "A mail that was written but not sent is found in the:",
            ["Not sent and not finished means it is saved as a draft.", "Drafts holds such mail."],
            "Drafts folder"),
        pat("ie-m6", "MIME and port numbers", "occasional",
            "'Standard that allows attachments and images', or 'default port of SMTP, POP3 or IMAP'.",
            ["Attachments, images and non-English text point to MIME.", "Recall the ports: SMTP 25, POP3 110, IMAP 143.", "Match each protocol to its own port."],
            "Three numbers and one full form cover this pattern.",
            "The default port number of POP3 is:",
            ["SMTP is 25.", "POP3 is 110.", "IMAP is 143."],
            "110"),
    ],
)

# =====================================================================
# 4. e-Banking and digital payments
# =====================================================================
SUBS["ie-ebanking"] = dict(
    concept=(
        "**e-Banking** means banking through the bank's secure website or app. "
        "**NEFT** settles in batches with no minimum. **RTGS** is real time with a minimum of Rs. 2 lakh. **IMPS** and **UPI** are instant and run 24x7. "
        "Banks never ask for your PIN, OTP or password."
    ),
    notes=r"""### Banking from a distance
**e-Banking (net banking)** is banking through the bank's secure **website**. **Mobile banking** uses the bank's **app**.

An **ATM (Automated Teller Machine)** gives cash, balance enquiry, a mini statement and PIN change.

All of them work by sending instructions over secure networks, not paper slips.

### Money-transfer systems of India
**NPCI (National Payments Corporation of India)** was set up in 2008. It runs most retail payment systems.

| System | Full form | Key facts |
|---|---|---|
| **NEFT** | National Electronic Funds Transfer | Settles in batches (half-hourly). No minimum. 24x7 since December 2019. |
| **RTGS** | Real Time Gross Settlement | Real time, one transfer at a time. **Minimum Rs. 2 lakh.** 24x7 since December 2020. |
| **IMPS** | Immediate Payment Service | Instant, 24x7, through mobile or internet banking. |
| **UPI** | Unified Payments Interface (2016) | Instant app-to-app transfer. 24x7. |

> **Watch:** The 2 lakh minimum belongs to RTGS. NEFT has no minimum.

### Which system to pick
Ask two questions. Is the amount large? Must it move at once?

| Need | System |
|---|---|
| Any amount, batch settlement is fine | NEFT |
| Large amount (Rs. 2 lakh or more), real time | RTGS |
| Instant, through mobile or internet banking | IMPS |
| Instant, using a VPA or QR | UPI |

> **Example:** Sending Rs. 5,00,000 in real time is an RTGS job. Sending Rs. 500 to a friend by QR is UPI.

### UPI in short
- UPI uses a **VPA** (virtual payment address) in the form name@bank.
- You can also pay by **QR** code.
- **BHIM** is one UPI app.
- NPCI built UPI.

### Bank codes
| Code | Size | Job |
|---|---|---|
| **IFSC** (Indian Financial System Code) | **11 characters** | Identifies the bank branch |
| **MICR** (Magnetic Ink Character Recognition) | **9 digits** | Cheque strip that speeds clearing |
| **SWIFT** | Not asked | Code for international transfers |

An IFSC such as SBIN0001234 has three parts. SBIN is the bank (4 letters). Then comes 0. Then 001234 is the branch (6 characters).

### PIN, CVV, OTP and two factors
- **PIN** is your secret number at an ATM or UPI app.
- **CVV** is the 3-digit Card Verification Value on the back of the card.
- **OTP** is a One Time Password. It works for one login or one payment only.
- **Two-factor authentication (2FA)** needs two proofs: something you know (password) and something you have or are (OTP, fingerprint).

One stolen password is not enough. That is the point of 2FA.

### Safe habits
- Banks **never ask** for PIN, OTP, CVV or password by call, SMS or mail. The caller is a fraudster.
- Check HTTPS and the padlock before you pay.
- Avoid public Wi-Fi for transactions.
- Unknown links are phishing. Do not tap them.
- Report cyber-fraud on the national helpline **1930**.

> **Tip:** If anyone asks for your OTP, refuse. No real bank needs it from you.
""",
    tricks=[
        trick("NEFT vs RTGS",
              "**RTGS** is real time, one by one, for large sums: minimum Rs. 2 lakh. **NEFT** settles in half-hourly batches, for any amount.",
              "What is the minimum amount for RTGS?", ["RTGS is meant for large transfers.", "The floor is 2 lakh."], "Rs. 2 lakh"),
        trick("IFSC is 11",
              "IFSC has **11 characters**: 4 letters for the bank, a zero, then 6 characters for the branch. MICR is the 9-digit cheque strip.",
              "How many characters does an IFSC code have?", ["4 for the bank, 1 zero, 6 for the branch.", "4 + 1 + 6 = 11."], "11"),
        trick("2FA needs two keys",
              "Two-factor means a password (you know) plus an OTP or fingerprint (you have or are). One stolen password is not enough.",
              "Entering a password and then an SMS OTP is an example of:", ["Password is one factor.", "The OTP is a second factor."], "Two-factor authentication"),
    ],
    mistakes=[
        mis("Giving NEFT the 2 lakh minimum.", "RTGS has the minimum. NEFT has none."),
        mis("Saying IMPS works only for foreign banks.", "IMPS is an Indian instant payment service, 24x7."),
        mis("Sharing an OTP with a caller who says he is from the bank.", "Real banks never ask. Refuse and disconnect."),
        mis("Counting IFSC as 9 characters.", "IFSC has 11 characters. MICR has 9 digits."),
        mis("Confusing CVV with PIN.", "CVV is the 3 digits on the card back. PIN is your secret number."),
    ],
    revision=[
        "NEFT = batches, no minimum. RTGS = real time, minimum Rs. 2 lakh. IMPS and UPI = instant, 24x7.",
        "NPCI (2008) runs most retail payment systems and built UPI (2016).",
        "UPI address (VPA) looks like name@bank. Payments also work by QR.",
        "IFSC = 11 characters (branch). MICR = 9 digits (cheque). SWIFT = international.",
        "OTP = one time password. CVV = 3 digits on the card back. 2FA = password plus OTP or biometric.",
        "Banks never ask for OTP, PIN or CVV. Cyber-fraud helpline: 1930.",
    ],
    patterns=[
        pat("ie-b1", "NEFT / RTGS / IMPS / UPI comparison", "very common",
            "'Which system has a minimum of 2 lakh', 'which is instant 24x7 by UPI ID', 'full form of NEFT, RTGS, UPI'.",
            ["NEFT means batches and no minimum.", "RTGS means real time and minimum Rs. 2 lakh.", "IMPS means instant, inside banking apps.", "UPI means instant app-to-app, built by NPCI."],
            "The systems differ by style, and options mix the styles.",
            "A customer must transfer 25,00,000 rupees immediately, transaction by transaction. The suitable system is:",
            ["Immediate and one by one means real time gross settlement.", "The amount is above the 2 lakh minimum."],
            "RTGS"),
        pat("ie-b2", "OTP, PIN, CVV and 2FA safety", "very common",
            "'Full form of OTP or CVV', 'a caller from the bank asks your OTP, what do you do', or which pair makes two-factor.",
            ["OTP is a One Time Password.", "CVV is the Card Verification Value, 3 digits.", "2FA is a password plus an OTP or biometric.", "Never share PIN, OTP or CVV with anyone."],
            "Banks never ask for these, so the asker is a fraudster.",
            "A caller says he is from your bank and asks for the OTP that just arrived. You should:",
            ["Real banks never ask for OTPs.", "This is a vishing fraud attempt."],
            "Refuse and disconnect"),
        pat("ie-b3", "IFSC, MICR and SWIFT codes", "common",
            "'IFSC has how many characters', 'which code is used for international transfer', 'the 9-digit code on a cheque'.",
            ["IFSC is 11 characters.", "MICR is 9 digits, on the cheque.", "SWIFT is for international transfers."],
            "Each code has one size and one job.",
            "The number of characters in an IFSC code is:",
            ["SBIN0001234 has 4 letters, one 0 and 6 branch characters.", "4 + 1 + 6 = 11."],
            "11"),
        pat("ie-b4", "ATM and net-banking basics", "common",
            "'ATM stands for', 'which of these can be done at an ATM', 'mobile banking vs net banking'.",
            ["ATM means Automated Teller Machine.", "Net banking uses the bank's website.", "Mobile banking uses the bank's app.", "ATM needs the card and PIN."],
            "These are plain definitions.",
            "The full form of ATM is:",
            ["A is Automated.", "T is Teller and M is Machine."],
            "Automated Teller Machine"),
        pat("ie-b5", "UPI facts", "common",
            "'UPI address format', 'who built UPI', 'year of UPI', or an odd-one-out list of payment systems.",
            ["A UPI address is a VPA, written name@bank.", "UPI works by VPA or QR, app to app.", "NPCI built UPI. It launched in 2016.", "BHIM is a UPI app."],
            "UPI needs no account number or IFSC for each payment.",
            "Which of these is in the format of a UPI virtual payment address?",
            ["A VPA looks like name@bank.", "So priya@examplebank fits."],
            "priya@examplebank"),
        pat("ie-b6", "Safe online payment habits", "common",
            "'Which is a safe practice', 'what to do on an unknown link', 'is public Wi-Fi fine for banking'.",
            ["Check HTTPS and the padlock before paying.", "Avoid public Wi-Fi for transactions.", "Treat unknown links as phishing.", "Never share PIN, OTP or password."],
            "Most fraud needs your cooperation, so refusing stops it.",
            "Which is a safe practice while paying online?",
            ["Sharing OTPs and tapping unknown links are unsafe.", "Checking HTTPS and the padlock is safe."],
            "Check HTTPS and the padlock before paying"),
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
