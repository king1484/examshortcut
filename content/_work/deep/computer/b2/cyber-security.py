"""Phase-2 deep content for computer/cyber-security. Run: py -3 cyber-security.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from cs_pats import build_malware, build_attacks, build_prevention, build_it_act
import cs_qs


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Malware identification", "very common",
      "'A program that replicates itself is ___', 'which malware disguises as useful software', 'files locked for ransom' — behaviour described, malware named.",
      "Match the behaviour: needs a host file = virus; self-replicates alone = worm; disguised as useful software, no replication = trojan; locks files for money = ransomware; spies = spyware; records keystrokes = keylogger; shows ads = adware; army of zombie machines = botnet. The plant swaps virus and worm — check who needs the host.",
      "cs-malware",
      "Which type of malware spreads on its own through a network without a host file?",
      "Worm — viruses ride on host files; worms crawl the network independently."),
    P("Phishing-family matching", "very common",
      "A fraud scenario by e-mail, phone call, SMS, or a correct URL landing on a fake site — the attack's name is asked; 'full form / meaning of vishing, smishing'.",
      "Follow the channel: e-mail/fake site = phishing; phone call = vishing; SMS = smishing; correct address, fake destination = pharming; aimed at one chosen victim = spear phishing. All of them are social engineering — attacking the person, and the fix is never sharing OTP/PIN.",
      "cs-attacks",
      "An SMS claiming your account will be blocked asks you to open a link and enter your bank password. This is:",
      "Smishing — phishing delivered by SMS; the link leads to a credential-stealing fake."),
    P("Preventive-measure odd-one-out", "common",
      "'Which of these is NOT a security measure', 'which measure protects against ransomware', lists where one protection role is swapped (firewall cleaning viruses, antivirus filtering traffic).",
      "Fix the roles: firewall = filters network traffic by rules at the doorway; antivirus = scans and removes malware inside (needs updates); encryption = scrambles data (plaintext to ciphertext, AES, https padlock); 2FA = password + OTP/biometric; backups = the ransomware antidote. The plant: crediting the firewall with cleaning infections.",
      "cs-prevention",
      "Which of the following does a firewall do?",
      "Filters incoming and outgoing network traffic by rules — it does not scan or clean files inside."),
    P("IT Act sections and authorities", "common",
      "'Hacking is punished under which section', 'identity theft section', 'which section was struck down', 'CERT-In works under ___', 'the IT Act was enacted in ___'.",
      "Memorise the ladder: 43 unauthorised access, 65 source code, 66 hacking, 66C identity theft, 66D online cheating, 67 obscenity, 72 privacy; 66A struck down in 2015 (Shreya Singhal). Act = 2000 (from 17 Oct, UNCITRAL-based, amended 2008). CERT-In under MeitY; NCIIPC guards critical infrastructure; helpline 1930.",
      "cs-it-act",
      "Identity theft (misusing another's password or digital signature) is an offence under which section of the IT Act?",
      "Section 66C — added by the 2008 amendment."),
    P("Attack-mechanism statements", "common",
      "'Which statement about a salami attack / logic bomb / DoS is true', a scenario (tiny thefts, waiting code, flooded server, hidden listener) matched to its attack name.",
      "Anchor the classics: salami = many tiny thefts; data diddling = records changed at entry; logic bomb = code that waits for a trigger; SQL injection = commands typed into a form; DoS/DDoS = flooding (DDoS from many machines); MITM = secretly reading between two parties, typical on open Wi-Fi.",
      "cs-attacks",
      "A malicious program lies dormant in a bank's system until 1 April and then deletes all records. This is a:",
      "Logic bomb — malware waiting for a trigger event before it detonates."),
    P("Encryption and password basics", "common",
      "'Scrambled data is called ___', 'https/padlock means ___', 'AES full form', 'strongest password' and 2FA meaning.",
      "Plaintext = readable, ciphertext = scrambled; decryption needs the key; AES = Advanced Encryption Standard; https + padlock = encrypted connection (TLS/SSL). Strong password = long, mixed characters, not personal; 2FA = password plus a second proof so a stolen password alone fails.",
      "cs-prevention",
      "The padlock icon next to https:// in a browser indicates:",
      "The connection to that site is encrypted — data travels as unreadable ciphertext."),
]

if __name__ == "__main__":
    subs = []
    for build, add in ((build_malware, cs_qs.add_malware),
                       (build_attacks, cs_qs.add_attacks),
                       (build_prevention, cs_qs.add_prevention),
                       (build_it_act, cs_qs.add_it_act)):
        S = build()
        add(S)
        subs.append(S)
    apply_topic("cyber-security", subs, PYQ)
