"""Internet & email practice questions. Numeric facts asserted here."""


def add_internet_basics(S):
    S.q("ie-n1", "easy", "The Internet is best described as a —",
        ["Global network of interconnected computer networks", "Single large computer in America",
         "Software installed on every PC", "Government department of India"],
        "Global network of interconnected computer networks",
        "The Internet is a **network of networks** — no single owner, no single computer.",
        "Network of networks.", 20)
    S.q("ie-n1", "medium", "The World Wide Web (WWW) and the Internet are —",
        ["Different: WWW is a service that runs on the Internet",
         "Two names of the same thing",
         "Different: the Internet runs on the WWW",
         "Unrelated technologies"],
        "Different: WWW is a service that runs on the Internet",
        "**Internet = the infrastructure; WWW = hyperlinked pages carried on it** — along with e-mail, FTP and other services.",
        "Road system vs traffic on it.", 30)
    S.q("ie-n1", "medium", "ARPANET, the ancestor of the Internet, was launched in —",
        ["1969", "1989", "1979", "1991"], "1969",
        "**ARPANET, 1969** — a US Defence project. 1989 is the WWW's year.",
        "ARPANET 1969, WWW 1989.", 25)
    S.q("ie-n1", "hard", "Which service does NOT run on the Internet?",
        ["Punch-card data entry", "E-mail", "File transfer (FTP)", "Voice calls (VoIP)"],
        "Punch-card data entry",
        "E-mail, FTP and VoIP are all Internet services; **punch cards are 1960s input media**, older than the networks.",
        "Punch cards predate networks.", 35)
    S.q("ie-n2", "easy", "URL stands for —",
        ["Uniform Resource Locator", "Universal Remote Link", "United Router Line", "Uniform Report List"],
        "Uniform Resource Locator",
        "**URL = Uniform Resource Locator** — the address of a web resource.",
        "Address = URL.", 20)
    S.q("ie-n2", "medium", "In the URL https://www.gov.in/schemes/2026.html, the part '/schemes/2026.html' is the —",
        ["Path to the page on the server", "Protocol", "Domain name", "E-mail address"],
        "Path to the page on the server",
        "https = protocol, www.gov.in = domain, and everything after is the **path** to the exact file.",
        "After the domain, the path.", 25)
    S.q("ie-n2", "medium", "The '.in' ending of a domain name indicates —",
        ["A website registered in India", "An insurance company", "An internal network", "A video site"],
        "A website registered in India",
        ".in is **India's country code**; .com is commercial, .org organisation, .gov government, .edu education.",
        "Country codes end addresses.", 25)
    S.q("ie-n3", "medium", "DNS translates —",
        ["Domain names into IP addresses", "IP addresses into domain names only",
         "Images into text", "Passwords into usernames"],
        "Domain names into IP addresses",
        "**DNS = the Internet's phonebook**: you give a name, it returns the numeric IP the machines use.",
        "Name in, number out.", 25)
    S.q("ie-n3", "medium", "Which server ASSIGNS an IP address to a device joining a network?",
        ["DHCP", "DNS", "ISP", "HTTP"], "DHCP",
        "**DHCP (Dynamic Host Configuration Protocol) assigns IPs**; DNS only translates names — the classic swap.",
        "DHCP hands out addresses.", 25)
    S.q("ie-n3", "easy", "The company that provides your Internet connection is called an —",
        ["ISP", "ICU", "IPK", "IRS"], "ISP",
        "**ISP = Internet Service Provider** (Jio, Airtel, BSNL).",
        "Provider = ISP.", 20)
    S.q("ie-n4", "easy", "HTTP stands for —",
        ["HyperText Transfer Protocol", "High Transfer Text Program", "HyperText Terminal Process",
         "Host Transfer Type Protocol"],
        "HyperText Transfer Protocol",
        "**HTTP = HyperText Transfer Protocol** — the rules for moving web pages; HTTPS is its secure version.",
        "HyperText moves by protocol.", 20)
    S.q("ie-n4", "medium", "Which pair is wrongly matched?",
        ["VoIP — Voice over Internet Protocol", "URL — Uniform Resource Locator", "ISP — Internet Service Provider",
         "HTML — Hyper Transfer Markup Language"],
        "HTML — Hyper Transfer Markup Language",
        "HTML = **HyperText Markup Language** — 'Hyper Transfer' is the planted error.",
        "Markup, not transfer.", 30)


def add_browsers_search(S):
    S.q("ie-s1", "easy", "Which of the following is a search engine?",
        ["Google", "Chrome", "Firefox", "Safari"], "Google",
        "**Google indexes and finds pages** — a search engine. Chrome, Firefox and Safari are browsers.",
        "Engine finds; browser shows.", 20)
    S.q("ie-s1", "medium", "Which option lists ONLY web browsers?",
        ["Chrome, Edge, Firefox", "Google, Bing, Yahoo", "Gmail, Yahoo Mail, Outlook", "Java, Python, C++"],
        "Chrome, Edge, Firefox",
        "All three are browser programs. Option B lists search engines, C lists e-mail services, D lists programming languages.",
        "Programs that show pages.", 25)
    S.q("ie-s2", "easy", "Ctrl+T in a browser opens —",
        ["A new tab", "A new window", "The history panel", "A download"],
        "A new tab",
        "**Ctrl+T = new Tab** (T for tab); Ctrl+N opens a new window.",
        "T = tab.", 20)
    S.q("ie-s2", "medium", "Which shortcut opens the BROWSING HISTORY panel?",
        ["Ctrl+H", "Ctrl+J", "Ctrl+K", "Ctrl+L"], "Ctrl+H",
        "**Ctrl+H = History**; Ctrl+J opens the downloads list — the standard trap pair.",
        "H for History.", 25)
    S.q("ie-s2", "medium", "In Chrome, an incognito window opens with —",
        ["Ctrl+Shift+N", "Ctrl+N", "Ctrl+I", "Ctrl+Shift+P"], "Ctrl+Shift+N",
        "**Ctrl+Shift+N** opens Incognito in Chrome; plain Ctrl+N is a normal new window.",
        "Shifted N = private.", 25)
    S.q("ie-s2", "hard", "Match: 1. Ctrl+D 2. Ctrl+F 3. Ctrl+J — a. find on page b. bookmark c. downloads",
        ["1-b, 2-a, 3-c", "1-a, 2-b, 3-c", "1-c, 2-a, 3-b", "1-b, 2-c, 3-a"],
        "1-b, 2-a, 3-c",
        "Ctrl+**D**rops a bookmark, Ctrl+**F**inds on the page, Ctrl+**J** opens downloads.",
        "D bookmark, F find, J downloads.", 35)
    S.q("ie-s3", "easy", "Sending a file from your computer to a web server is —",
        ["Uploading", "Downloading", "Streaming", "Browsing"], "Uploading",
        "**Upload = you to server; download = server to you.**",
        "Up = away from you.", 20)
    S.q("ie-s3", "medium", "The browser cache exists mainly to —",
        ["Speed up revisits by storing copies of pages", "Store your passwords securely",
         "Block viruses", "Compress your downloads"],
        "Speed up revisits by storing copies of pages",
        "**Cache = local copies** of pages and images, so a second visit loads without refetching everything.",
        "Cache = quick drawer.", 25)
    S.q("ie-s3", "medium", "Which statement about cookies is TRUE?",
        ["They are small text files a website stores on your device",
         "They are viruses that damage files",
         "They are programs that run in background",
         "They store the pages for offline use"],
        "They are small text files a website stores on your device",
        "**Cookies = passive text files** (logins, preferences, tracking) — a privacy topic, never a virus.",
        "Cookies remember, they don't harm.", 30)
    S.q("ie-s4", "medium", "Private (incognito) browsing on a shared computer mainly ensures that —",
        ["History and cookies of that session are deleted when the window closes",
         "The ISP cannot see your activity",
         "Websites cannot see your visit at all",
         "Viruses cannot enter"],
        "History and cookies of that session are deleted when the window closes",
        "Incognito forgets **locally** — websites and the ISP still see the traffic.",
        "Local forgetfulness only.", 30)
    S.q("ie-s4", "medium", "Which action does NOT need an Internet connection?",
        ["Reading a page saved earlier from the cache/Offline", "Sending an e-mail", "Searching on Google",
         "Downloading a song"],
        "Reading a page saved earlier from the cache/Offline",
        "Only the locally saved copy can be read offline; sending, searching and downloading all need the net.",
        "Local = no net needed.", 25)
    S.q("ie-s3", "hard", "Watching a video as it arrives, without saving the whole file first, is —",
        ["Streaming", "Uploading", "Bookmarking", "Caching"], "Streaming",
        "**Streaming plays while the data flows in** — the file need not be stored first.",
        "Stream, don't store.", 25)


def add_email_basics(S):
    S.q("ie-m1", "easy", "In an e-mail, CC stands for —",
        ["Carbon Copy", "Correct Copy", "Common Contact", "Copy Content"], "Carbon Copy",
        "**CC = Carbon Copy** — a visible duplicate to extra receivers; BCC = Blind Carbon Copy.",
        "Old carbon-paper name.", 20)
    S.q("ie-m1", "medium", "Receivers in the To and CC fields —",
        ["Cannot see the BCC list", "Can see the BCC list", "Receive no mail at all",
         "Are automatically BCC'd"],
        "Cannot see the BCC list",
        "**BCC is blind**: To/CC receivers never see those addresses; each BCC receiver doesn't see the others either.",
        "Blind = invisible list.", 25)
    S.q("ie-m1", "medium", "To mail 500 members of an association without exposing their addresses, use —",
        ["BCC for all addresses", "CC for all addresses", "To for all addresses", "Five separate mails"],
        "BCC for all addresses",
        "**BCC hides the list from everyone** — the standard bulk-mail etiquette.",
        "Bulk = blind.", 25)
    S.q("ie-m2", "easy", "Which protocol is used to SEND e-mail?",
        ["SMTP", "POP3", "IMAP", "HTTP"], "SMTP",
        "**SMTP = Simple Mail Transfer Protocol** — it pushes mail out; POP3/IMAP only fetch.",
        "SMTP Sends.", 20)
    S.q("ie-m2", "medium", "Which protocol downloads incoming mail to a single device, usually removing it from the server?",
        ["POP3", "SMTP", "IMAP", "FTP"], "POP3",
        "**POP3 = Post Office Protocol** — pick up the mail like a letter-box: one download, one device.",
        "POP Picks it off the server.", 25)
    S.q("ie-m2", "medium", "Meera reads her mail on her phone, tablet and laptop, and every device shows the same mailbox. Her account uses —",
        ["IMAP", "POP3", "SMTP", "FTP"], "IMAP",
        "**IMAP keeps mail on the server and syncs all devices**; POP3 would strand messages on one machine.",
        "IMAP = In-sync everywhere.", 25)
    S.q("ie-m2", "hard", "Which pair is correctly matched?",
        ["Sending mail — SMTP", "Sending mail — IMAP", "Receiving mail — SMTP", "Browsing web pages — POP3"],
        "Sending mail — SMTP",
        "SMTP sends; POP3 and IMAP receive; web pages travel by HTTP, not POP3.",
        "Only SMTP pushes.", 35)
    S.q("ie-m3", "easy", "In the e-mail address ramesh.k@gmail.com, the part 'ramesh.k' is the —",
        ["Username", "Domain name", "Protocol", "Password"], "Username",
        "**username @ domain** — ramesh.k is the user, gmail.com the mail service.",
        "Before @ = user.", 20)
    S.q("ie-m3", "medium", "The symbol that separates the username from the domain in an e-mail address is —",
        ["@ (at)", "# (hash)", "& (ampersand)", "~ (tilde)"], "@ (at)",
        "**@ means 'at'** — user at this service. It has been the e-mail separator since the 1970s.",
        "@ = at.", 20)
    S.q("ie-m3", "medium", "Which field of an e-mail carries the files clipped to the message?",
        ["Attachment", "Subject", "CC", "Signature"], "Attachment",
        "**Attachments** (paperclip icon) carry files; Subject is the one-line summary; Signature is the sign-off.",
        "Paperclip = attachment.", 20)
    S.q("ie-m4", "easy", "Unsolicited junk e-mail is called —",
        ["Spam", "Scam", "Sniffing", "Skimming"], "Spam",
        "**Spam = junk mail**; the filter parks it in the Spam folder.",
        "Junk = spam.", 20)
    S.q("ie-m4", "medium", "A mail that is written but not yet sent is stored as a —",
        ["Draft", "Archive", "Signature", "Bounce"], "Draft",
        "**Draft** = the waiting room of unsent mail.",
        "Unsent = draft.", 20)
    S.q("ie-m4", "hard", "Reply All on a mail addressed to you and 40 classmates reaches —",
        ["The sender and everyone on To/CC", "Only the sender", "Only the classmates", "Everyone on BCC too"],
        "The sender and everyone on To/CC",
        "**Reply All = sender + To + CC list**; BCC members were never disclosed and stay out.",
        "All visible people.", 35)


def add_ebanking(S):
    assert len("SBIN0001234") == 11
    assert len("123456789") == 9
    rtgs_min = 200000
    assert rtgs_min == 2 * 100000
    S.q("ie-b1", "easy", "NEFT stands for —",
        ["National Electronic Funds Transfer", "Net Easy Financial Transfer",
         "New Electronic Fast Transfer", "National E-Finance Transaction"],
        "National Electronic Funds Transfer",
        "**NEFT = National Electronic Funds Transfer** — batch-wise transfers run by RBI.",
        "National Electronic.", 20)
    S.q("ie-b1", "medium", "Which transfer system has a MINIMUM transaction of 2,00,000 rupees?",
        ["RTGS", "NEFT", "UPI", "IMPS"], "RTGS",
        "**RTGS = Real Time Gross Settlement** — built for high-value transfers; minimum 2 lakh. NEFT has no minimum.",
        "2-lakh floor = RTGS.", 25)
    S.q("ie-b1", "medium", "Which of these moves money INSTANTLY, 24x7, using just a UPI ID or QR code?",
        ["UPI", "RTGS", "NEFT", "Cheque clearing"], "UPI",
        "**UPI = Unified Payments Interface** — instant app-to-app transfer built by NPCI.",
        "Scan and pay = UPI.", 20)
    S.q("ie-b1", "hard", "Match: 1. NEFT 2. RTGS 3. UPI — a. batch transfers, no minimum b. real-time, minimum 2 lakh c. instant payments by NPCI",
        ["1-a, 2-b, 3-c", "1-b, 2-a, 3-c", "1-a, 2-c, 3-b", "1-c, 2-b, 3-a"],
        "1-a, 2-b, 3-c",
        "NEFT = batches (no minimum), RTGS = real-time with the 2-lakh floor, UPI = NPCI's instant rail.",
        "Batches, floor, instant.", 40)
    S.q("ie-b1", "medium", "UPI is operated by —",
        ["NPCI", "SEBI", "TRAI", "IRDAI"], "NPCI",
        "**NPCI (National Payments Corporation of India)** built and runs UPI, IMPS, RuPay and NEFT systems.",
        "NPCI = payments umbrella.", 25)
    S.q("ie-b2", "easy", "OTP stands for —",
        ["One Time Password", "Only Text Password", "Online Transfer Pin", "One Time Pin-code"],
        "One Time Password",
        "**OTP = One Time Password** — valid for one login or one transaction, for a short time.",
        "One use, one password.", 20)
    S.q("ie-b2", "medium", "The 3-digit security number printed on the back of a debit/credit card is the —",
        ["CVV", "PIN", "OTP", "IFSC"], "CVV",
        "**CVV = Card Verification Value** — never share it; it pairs with the card number for online payments.",
        "Back of card = CVV.", 25)
    S.q("ie-b2", "medium", "Login by password PLUS an OTP sent to your phone is an example of —",
        ["Two-factor authentication", "Password strength", "Data encryption", "Phishing"],
        "Two-factor authentication",
        "**2FA = two independent proofs** — something you know (password) plus something you receive or are (OTP, fingerprint).",
        "Two locks, two doors.", 25)
    S.q("ie-b2", "hard", "A caller claiming to be from your bank asks for the OTP you just received. The correct action is —",
        ["Refuse and disconnect; banks never ask for OTPs", "Share it to verify your account",
         "Share only the last 3 digits", "Send it by SMS for safety"],
        "Refuse and disconnect; banks never ask for OTPs",
        "No genuine bank asks for OTP, PIN, CVV or password — this is **vishing** (voice phishing).",
        "Asked OTP = fraud call.", 30)
    S.q("ie-b2", "medium", "The secret number typed at the ATM along with the card is the —",
        ["PIN", "CVV", "OTP", "CIN"], "PIN",
        "**PIN = Personal Identification Number** — card + PIN authorise ATM transactions.",
        "PIN at the machine.", 20)
    S.q("ie-b3", "medium", "An IFSC code contains how many characters?",
        ["11", "9", "10", "16"], "11",
        "**IFSC = 11 characters**: 4 letters of the bank + 0 + 6 characters of the branch (SBIN0001234).",
        "4 + 1 + 6 = 11.", 25)
    S.q("ie-b3", "medium", "The 9-digit magnetic-ink code printed at the bottom of a cheque is the —",
        ["MICR code", "IFSC code", "SWIFT code", "PIN"], "MICR code",
        "**MICR = Magnetic Ink Character Recognition** — 9 digits that speed up cheque clearing.",
        "Cheque strip = MICR.", 25)
    S.q("ie-b3", "medium", "For an international wire transfer to your account, the sender needs the —",
        ["SWIFT code", "MICR code", "CVV", "Aadhaar number"], "SWIFT code",
        "**SWIFT codes identify banks worldwide** for cross-border transfers; IFSC works only inside India.",
        "Abroad = SWIFT.", 25)
    S.q("ie-b3", "hard", "In the IFSC code SBIN0001234, the first four letters identify the —",
        ["Bank", "Branch", "City", "Account holder"], "Bank",
        "SBIN = State Bank of India; the 0 is a separator; **0001234 identifies the branch**.",
        "Bank first, branch last.", 30)
    S.q("ie-b4", "easy", "ATM stands for —",
        ["Automated Teller Machine", "Automatic Transfer Mode", "Any Time Money", "Automated Transaction Manager"],
        "Automated Teller Machine",
        "**ATM = Automated Teller Machine** — a 'teller' is the person behind the counter; the machine does that job.",
        "Machine teller.", 20)
    S.q("ie-b4", "medium", "Which of these can NOT be done at a normal ATM?",
        ["Opening a new fixed deposit instantly", "Cash withdrawal", "Balance enquiry", "Mini statement"],
        "Opening a new fixed deposit instantly",
        "ATMs handle cash, balance, mini statements and PIN changes; **fixed deposits need the branch, app or net banking**.",
        "ATM = cash point, not an FD desk.", 30)
    S.q("ie-b4", "medium", "Banking done through the bank's official app on a phone is called —",
        ["Mobile banking", "Micro banking", "ATM banking", "Postal banking"], "Mobile banking",
        "**Net banking = website; mobile banking = app** — both run from the same account.",
        "App on phone = mobile banking.", 20)
