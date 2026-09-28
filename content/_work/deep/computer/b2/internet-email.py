"""Phase-2 deep content for computer/internet-email. Run: py -3 internet-email.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from ie_pats import (build_internet_basics, build_browsers_search, build_email_basics,
                     build_ebanking)
import ie_qs


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Full form / abbreviation", "very common",
      "'Full form of HTTP/HTML/URL/ISP/SMTP/ATM/IFSC/OTP' or a wrongly matched pair where one word of an expansion is changed.",
      "Expand letter by letter from family tables: web family (HTTP, HTML, URL, WWW), mail family (SMTP, POP3, IMAP, e-mail @), banking family (NEFT, RTGS, UPI, NPCI, IFSC, MICR, OTP, CVV, PIN, ATM). The planted error is one swapped word, e.g. 'Hyper Transfer Markup Language' for HTML.",
      "ie-internet-basics",
      "The full form of SMTP is:",
      "Simple Mail Transfer Protocol — the sending protocol of e-mail."),
    P("Browser vs search engine trap", "very common",
      "'Which is a browser?' with Google planted among Chrome/Firefox, or 'which is a search engine?' with Chrome planted among Bing/Yahoo.",
      "Browsers are programs installed on your device (Chrome, Edge, Firefox, Safari, Opera); search engines are websites reached through them (Google, Bing, Yahoo, DuckDuckGo). The famous trap: Google called a browser, or Chrome called a search engine.",
      "ie-browsers-search",
      "Which of the following is a web browser?",
      "Chrome — the program that shows pages; Google is the search engine inside it."),
    P("CC/BCC visibility scenario", "very common",
      "A mail scenario: who can see whose address, what Reply All reaches, or which field protects a bulk list of receivers.",
      "CC is a visible copy (everyone in To/CC sees all those addresses); BCC is blind (To/CC never see the BCC list, and BCC receivers are hidden from each other). Bulk mails to strangers go in BCC; Reply All on a BCC'd mail reaches only the sender.",
      "ie-email-basics",
      "A mail to 200 customers uses BCC for all addresses. Reply All by one customer reaches:",
      "Only the sender — the BCC list stays hidden."),
    P("Protocol-to-purpose matching", "very common",
      "'Protocol used to send e-mail', 'which protocol syncs mail across devices', 'protocol that moves web pages', 'protocol of file transfer' — directions matched.",
      "Fix the map: SMTP sends mail; POP3 downloads to one device; IMAP syncs on the server; HTTP/HTTPS move web pages (443 = secure); FTP transfers files; DHCP assigns IPs; DNS resolves names. Sending questions always answer SMTP.",
      "ie-email-basics",
      "Which protocol is used to send e-mail from a client to the mail server?",
      "SMTP — Simple Mail Transfer Protocol; POP3 and IMAP only receive."),
    P("E-banking rails and limits", "very common",
      "'Minimum of 2 lakh belongs to which system?', 'which is instant 24x7', 'full form of NEFT/RTGS/UPI', 'UPI is run by ___' — the rails mixed in options.",
      "NEFT = batch transfers, no minimum; RTGS = real-time, transaction-wise, minimum 2,00,000 rupees; IMPS = instant inside banking apps; UPI = instant by UPI ID/QR, built by NPCI. The recurring trap gives NEFT the 2-lakh floor that belongs to RTGS.",
      "ie-ebanking",
      "A transfer of 5,00,000 rupees is needed immediately, transaction by transaction. Which system fits?",
      "RTGS — real-time gross settlement, designed for high-value transfers (minimum 2 lakh)."),
    P("URL anatomy", "common",
      "A URL is printed and a part is asked: protocol, domain, country code or path; or the full form of URL.",
      "Split at slashes: protocol (https://) + domain (www.site.in) + path (/folder/page.html). Country codes: .in India, .uk UK; generic: .com, .org, .gov, .edu. DNS converts the whole domain to an IP address.",
      "ie-internet-basics",
      "In https://www.mysite.in/exams/ssc.html, 'www.mysite.in' is the:",
      "Domain name — https is the protocol; /exams/ssc.html is the path."),
    P("Security-code identification", "common",
      "'Which code has 11 characters', 'the 9-digit cheque code', 'the 3-digit number on the card', 'which code for international transfers'.",
      "Line them up: IFSC = 11 characters (4 bank letters + 0 + 6 branch) for domestic transfers; MICR = 9 digits on the cheque strip; CVV = 3 digits on the card back; PIN = your secret at machines; OTP = one-time password; SWIFT = international transfers.",
      "ie-ebanking",
      "The number of characters in an IFSC code is:",
      "11 — for example SBIN0001234: bank (SBIN) + 0 + branch (001234)."),
]

if __name__ == "__main__":
    subs = []
    for build, add in ((build_internet_basics, ie_qs.add_internet_basics),
                       (build_browsers_search, ie_qs.add_browsers_search),
                       (build_email_basics, ie_qs.add_email_basics),
                       (build_ebanking, ie_qs.add_ebanking)):
        S = build()
        add(S)
        subs.append(S)
    apply_topic("internet-email", subs, PYQ)
