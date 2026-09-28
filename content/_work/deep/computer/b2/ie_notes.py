"""Internet & email deep notes."""

IE_INTERNET_BASICS = """### Internet and WWW — related but not the same
The **Internet** is a worldwide **network of networks**: millions of computers and phones connected so they can exchange data. It grew out of **ARPANET**, a 1969 project of the US Defence Department (its first two nodes were UCLA and Stanford). The **World Wide Web (WWW)** is a **service that runs on the Internet** — the collection of hyperlinked pages read through a browser. It was invented by **Tim Berners-Lee in 1989** at CERN. E-mail and file transfer are other services on the same Internet. So: Internet = the road system, WWW = one kind of traffic on it.

### URL — the address of a page
A **URL (Uniform Resource Locator)** names every page. Read it in parts:

`https://www.example.in/Results/2026.html`
- **https://** — the protocol (rules for the conversation). HTTPS is the **secure** version (encrypted); plain HTTP is not.
- **www.example.in** — the **domain name** of the server (www = world wide web host prefix, .in = India country code; .com, .org, .gov, .edu are others).
- **/Results/2026.html** — the **path** to the exact page or file on that server.

The **DNS (Domain Name System)** translates the typed name into the server's **IP address** — the numeric identity (like 142.250.183.14) that machines actually use. DNS is the **phonebook of the Internet**: you ask for a name, it returns the number.

### Who does what on the net
| Player | Job |
|---|---|
| **ISP** (Internet Service Provider) | sells you the connection (Jio, Airtel, BSNL) |
| **DNS server** | name to IP address translation |
| **DHCP server** | **assigns** an IP address to your device |
| **Web server** | stores pages and serves them to browsers |

Classic trap: **DNS resolves names; DHCP assigns addresses.**

### Small facts that recur
- **IP address** — a device's numeric address; IPv4 has four blocks of 0-255.
- **TCP/IP** is the standard protocol suite of the Internet (ARPANET adopted it in 1983).
- **Bandwidth** is the data-carrying capacity of a link; **latency** is the delay.
- **VoIP** (Voice over Internet Protocol) carries phone calls over the Internet.
- A **web portal** is a site that gathers many services on one page; a **website** is a set of related web pages under one domain.

### How the pieces cooperate (one page load)
1. You type a **URL** in the browser.
2. **DNS** turns the domain into the server's IP address.
3. Your request travels over TCP/IP to the **web server**, which sends the page back.
4. The browser renders the HTML and displays the page — all in about a second.
Every exam question on DNS, URL or ISP is one stop on this journey, so picture it as a single delivery trip: name translated (DNS), address found (IP), parcel carried (TCP/IP), delivered by the shop (web server).

### Quick revision
- Internet = network of networks (from ARPANET, 1969); WWW = hyperlinked pages (Berners-Lee, 1989).
- URL = protocol + domain + path; https is the secure protocol.
- **DNS: name to IP; DHCP: gives IP; ISP: sells the connection.**
- TCP/IP = the Internet's protocol suite; VoIP = calls over the Internet."""

IE_BROWSERS_SEARCH = """### Browser vs search engine — separate jobs
A **browser** is the **program on your device** that fetches and displays web pages: **Chrome, Microsoft Edge, Firefox, Safari, Opera** (Internet Explorer is retired). A **search engine** is a **website** that indexes the web and finds pages for your words: **Google, Bing, Yahoo, DuckDuckGo**. Google is a search engine; Chrome is a browser; Chrome's address bar can USE Google. Exams love the swap: "Google is a browser — true or false?" False.

### The browser's everyday tools
| Tool | What it keeps |
|---|---|
| **History** | every page you visited |
| **Bookmarks/Favourites** | pages you saved for quick return |
| **Cache** | copies of pages and pictures, so revisits load faster |
| **Cookies** | small text files a site stores on you — logins, preferences, tracking |

Cookies are **not viruses** — they are passive text files; the worry is privacy, not infection. **Incognito / private mode** opens a window that forgets history and cookies when closed — useful on shared computers. It does **not** make you anonymous to the websites or the ISP.

### Keyboard shortcuts of the browser
| Key | Job |
|---|---|
| **Ctrl+T** | new **T**ab |
| **Ctrl+N** | new window |
| **Ctrl+Shift+N** | new **incognito** window (Chrome) |
| **Ctrl+H** | **H**istory panel |
| **Ctrl+J** | **J**ust-downloaded files (downloads list) |
| **Ctrl+D** | **D**rop a bookmark |
| **Ctrl+F** | **F**ind text on the page |
| **F5 / Ctrl+R** | refresh the page |

H before J alphabetically: **History, then downloads** — a common one-mark trap.

### Downloading and uploading
- **Download** = a file travels from a server **to your device** (songs, PDFs, apps). The browser's downloads list (Ctrl+J) tracks them; the Downloads folder stores them.
- **Upload** = a file travels from **your device to a server** (attaching a form, posting a video).
- **Streaming** = watching or listening as the data arrives, without saving the whole file first.

### Using a search engine well
Type specific **keywords**, not full sentences; put quotes around words that must appear together ("solar mission"); a minus sign removes a word. Results mix ads, links, images and videos — the engine ranks pages by relevance, it does not check truth.

### Quick revision
- Chrome/Edge/Firefox/Safari = browsers; Google/Bing/DuckDuckGo = search engines.
- History (Ctrl+H), downloads (Ctrl+J), bookmark (Ctrl+D), new tab (Ctrl+T), incognito Ctrl+Shift+N.
- Cache = speed copies; cookies = site-stored text files (privacy, not viruses).
- Download = server to you; upload = you to server; streaming = play as it arrives."""

IE_EMAIL_BASICS = """### What e-mail is
**E-mail (electronic mail)** sends messages between accounts stored on **mail servers**. An address has two parts joined by **@** ("at"): `rani.sharma@gmail.com` — **username @ domain**. The domain here belongs to Gmail (Google's mail service); Outlook and Yahoo Mail are others. @ is the separator — a favourite full-form/identification question.

### The fields of a compose window
| Field | Meaning |
|---|---|
| **To** | the main receivers |
| **CC** (Carbon Copy) | extra receivers — **everyone can see** all To and CC addresses |
| **BCC** (Blind Carbon Copy) | hidden receivers — **To and CC people cannot see** the BCC list; each BCC receiver also can't see the others |
| **Subject** | one-line summary of the mail |
| **Attachment** | files clipped to the mail (paperclip icon) |
| **Signature** | sender's fixed sign-off block |

**The CC/BCC rule:** CC is a visible copy; BCC is a blind copy. When a mail was sent with addresses in BCC, **Reply All reaches only the sender** — the hidden list stays hidden.

### The three protocols
| Protocol | Direction | How it works |
|---|---|---|
| **SMTP** (Simple Mail Transfer Protocol) | **sending** (and passing between servers) | pushes your mail out |
| **POP3** (Post Office Protocol v3) | **receiving** | downloads mail to ONE device, usually deleting it from the server |
| **IMAP** (Internet Message Access Protocol) | **receiving** | mail **stays on the server**, synced across all your devices |

Memory hook: **SMTP Sends, POP Picks (down), IMAP In-sync.** If the question says "protocol used to SEND e-mail" — SMTP, every time.

### Everyday mail actions
- **Reply** answers only the sender; **Reply All** answers the sender and everyone in To/CC; **Forward** sends a received mail to new people.
- **Spam** = junk or unsolicited mail; the filter parks it in the Spam folder — never click its links.
- **Draft** = a mail written but not sent; it waits until you finish it.
- **Cc etiquette**: use CC to keep someone informed; use BCC for bulk mails so receivers' addresses stay private.

### The journey of one e-mail
1. Rani writes a mail and presses Send. Her mail server uses **SMTP** to push it across the Internet to the server named after the **@domain**.
2. The receiver's server holds the mail in her mailbox.
3. When the receiver opens her app, **IMAP** (or POP3) fetches or syncs it to her device.
So one mail may touch three protocols: SMTP out, IMAP in, and the two servers talking to each other by SMTP. Exams compress this story into one line — "SMTP is used to send" — but the full journey is worth one drawing in your rough notes.

### Quick revision
- Address = username @ domain; @ separates the two.
- **CC visible to all; BCC hidden** from To and CC receivers.
- **SMTP sends; POP3 downloads to one device; IMAP syncs everywhere.**
- Reply = sender; Reply All = everyone in To/CC; Forward = new receivers.
- Spam = junk mail; Draft = unsent mail."""

IE_EBANKING = """### Banking from a distance
**e-Banking (net banking)** = banking through the bank's secured **website**; **mobile banking** = the same through an **app**. The **ATM (Automated Teller Machine)** works round the clock for cash withdrawal, balance enquiry, mini statement and PIN change. All of them sit on the same idea: instructions travel over secure networks instead of paper slips at a counter.

### The money-transfer rails of India
| Rail | Full form | Style |
|---|---|---|
| **NEFT** | National Electronic Funds Transfer | moves in **batches** (half-hourly slots); **no minimum**; 24x7 since 2019 |
| **RTGS** | Real Time Gross Settlement | **real-time, transaction by transaction**; **minimum 2,00,000 rupees** |
| **IMPS** | Immediate Payment Service | **instant**, runs inside mobile/internet banking, 24x7 |
| **UPI** | Unified Payments Interface | instant app-to-app transfer by **UPI ID or QR** (PhonePe, GPay, Paytm); built by **NPCI** (National Payments Corporation of India) |

RTGS's rule is asked again and again: **minimum 2 lakh rupees** — NEFT has no minimum.

### The codes on a cheque and beyond
| Code | Size | Job |
|---|---|---|
| **IFSC** (Indian Financial System Code) | **11 characters** | identifies the exact bank branch for NEFT/RTGS/IMPS (e.g. SBIN0001234: 4 letters bank, 0, 6 characters branch) |
| **MICR** (Magnetic Ink Character Recognition) | **9 digits** | the cheque number strip at the bottom; speeds cheque clearing |
| **SWIFT** | — | the code system for **international** wire transfers |

### Safety: OTP, PIN, CVV and two factors
- **PIN** = Personal Identification Number (your secret at ATM/UPI); **CVV** = the 3-digit Card Verification Value printed on the card's back; **OTP** = One Time Password, valid for one login/transaction only.
- **Two-factor authentication (2FA)** = password **plus** something else (OTP or fingerprint) — two locks instead of one.
- Real banks **never ask** for PIN, OTP, CVV or passwords by phone, SMS or mail — any such caller is a fraudster. Report cyber-fraud on the national helpline **1930**; IFSC-like codes should never be typed on a link received from a stranger.

### Quick revision
- NEFT = batches, no minimum; **RTGS = real-time, minimum 2 lakh**; IMPS/UPI = instant, 24x7; UPI by NPCI.
- **IFSC = 11 characters** (branch identity); **MICR = 9 digits** (cheque strip); SWIFT = international.
- OTP = one-time password; CVV = 3 digits on card back; 2FA = password + OTP/biometric.
- Banks never ask for OTP/PIN/CVV; cyber-fraud helpline = 1930."""
