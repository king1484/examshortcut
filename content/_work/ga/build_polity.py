# -*- coding: utf-8 -*-
"""Assembles and saves the polity topic file."""
from gacommon import Q, save_topic
from polity_concepts import C_MAKING, C_PREAMBLE, C_FR, C_EXEC, C_PARL, C_AMD, C_LOCAL
from polity_concepts2 import C_BODIES
from polity_questions import SOLVED, PRACTICE

topic = {
    "id": "polity",
    "sectionId": "ga",
    "title": "Indian Polity & Constitution",
    "order": 5,
    "importance": "high",
    "avgQuestions": {"tier1": 3, "tier2": 3},
    "summary": "The Constitution — its making, Preamble, Parts and Schedules, Rights, the three organs of government, amendments and constitutional bodies. CGL consistently asks 3-4 factual one-liners here, the single most predictable GA block.",
    "subtopics": [
        {
            "id": "pol-making",
            "title": "Making of the Constitution & borrowed features",
            "concept": C_MAKING,
            "formulas": [],
            "tricks": [
                {
                    "title": "Committee-chairman pairing",
                    "body": "**Nehru** took the *Union/States/Constitution* committees (the 'national' subjects), **Patel** took *Provinces and Rights* (the 'practical' subjects), **Prasad** took *procedure and flag*, **Ambedkar** took the *Drafting* pen.",
                    "example": {
                        "q": "Who chaired the Advisory Committee on Fundamental Rights and Minorities?",
                        "solution": "Sardar Patel — 'Rights' belong to Patel's practical cluster.",
                    },
                },
                {
                    "title": "Borrowed features speed-pair",
                    "body": "UK-Parliament • USA-Rights • Ireland-Duties-of-state (DPSP) • Canada-Centre-strong • Australia-List-3 • USSR-Duties-of-citizens • France-Republic • Germany-Emergency-rights • Japan-law-procedure.",
                    "example": {
                        "q": "Fundamental Duties are inspired by which constitution?",
                        "solution": "USSR (Russia); the DPSP counterpart from Ireland.",
                    },
                },
            ],
            "mistakes": [
                "Confusing adoption date (26 Nov 1949) with enforcement date (26 Jan 1950).",
                "Assuming Ambedkar presided over the Assembly — Rajendra Prasad did; Ambedkar chaired only the Drafting Committee.",
                "Attributing joint sitting to Canada instead of Australia.",
            ],
        },
        {
            "id": "pol-preamble-parts",
            "title": "Preamble, Parts and the 12 Schedules",
            "concept": C_PREAMBLE,
            "formulas": [],
            "tricks": [
                {
                    "title": "Schedule story-line",
                    "body": "1-Names, 2-Salaries, 3-Oaths, 4-RS seats, 5-Areas(SC/ST), 6-Tribal NE, 7-Three Lists, 8-Languages, 9-Land laws, 10-Defection, 11-Panchayat(29), 12-Municipality(18).",
                    "example": {
                        "q": "Which Schedule contains anti-defection provisions?",
                        "solution": "The 10th Schedule (added by the 52nd Amendment, 1985).",
                    },
                },
                {
                    "title": "Preamble keyword count",
                    "body": "Sovereign-Socialist-Secular-Democratic-Republic = 5 descriptors; J-L-E-F = Justice-Liberty-Equality-Fraternity, with only Justice split three ways (social-economic-political).",
                    "example": {
                        "q": "Which Preamble ideal is described in three parts?",
                        "solution": "Justice — social, economic and political (Russian Revolution inspiration).",
                    },
                },
            ],
            "mistakes": [
                "Saying the Preamble was amended by the 44th — it was the 42nd (1976).",
                "Listing 18 languages — the count has been 22 since the 92nd Amendment (2003).",
                "Mixing up the 9th Schedule (land reform laws) with the 10th (defection).",
            ],
        },
        {
            "id": "pol-fundamental-rights",
            "title": "Fundamental Rights, DPSP and Fundamental Duties",
            "concept": C_FR,
            "formulas": [],
            "tricks": [
                {
                    "title": "FR article blocks",
                    "body": "14-18 Equality • 19-22 Freedom • 23-24 Exploitation • 25-28 Religion • 29-30 Culture-Education • 32 Remedies. Count blocks as 5+4+2+4+2+1.",
                    "example": {
                        "q": "Under which article is the abolition of untouchability placed?",
                        "solution": "Article 17 — the first article of the Equality block (14-18).",
                    },
                },
                {
                    "title": "Duty amendment pair",
                    "body": "42nd gave 10 duties; 86th added the 11th (education of 6-14 year-olds). Same 86th also inserted Art. 21A — one amendment, twin gifts.",
                    "example": {
                        "q": "Which amendment added the 11th Fundamental Duty?",
                        "solution": "The 86th Amendment, 2002.",
                    },
                },
            ],
            "mistakes": [
                "Treating the Right to Property as a Fundamental Right — it is now Art. 300A, a legal right.",
                "Thinking all FRs suspend in a national emergency — Arts. 20 and 21 never suspend.",
                "Believing DPSPs are enforceable in court — they are non-justiciable.",
            ],
        },
        {
            "id": "pol-executive",
            "title": "Union and State Executive",
            "concept": C_EXEC,
            "formulas": [],
            "tricks": [
                {
                    "title": "Electoral college contrast",
                    "body": "President = elected MPs + elected MLAs (no nominated). Vice-President = ALL MPs of both Houses, including the 12 nominated. 'Vice' reaches where 'President' does not.",
                    "example": {
                        "q": "Do nominated members of the Rajya Sabha vote in the Vice-Presidential election?",
                        "solution": "Yes — they are excluded only from the President's electoral college.",
                    },
                },
                {
                    "title": "Pardon ladder",
                    "body": "President's Art. 72 pardons court-martial and death sentences; the Governor's Art. 161 covers neither. 'Governor = softer ladder'.",
                    "example": {
                        "q": "Can a Governor pardon a death sentence?",
                        "solution": "No — only the President can (Art. 72).",
                    },
                },
            ],
            "mistakes": [
                "Saying the President takes oath from the Vice-President — the CJI administers it.",
                "Assuming the VP's removal starts in the Lok Sabha — it starts in the Rajya Sabha (Art. 67(b)).",
                "Forgetting the 91st Amendment's 15% minister cap and attributing it to anti-defection's 52nd.",
            ],
        },
        {
            "id": "pol-parliament-judiciary",
            "title": "Parliament and the Judiciary",
            "concept": C_PARL,
            "formulas": [],
            "tricks": [
                {
                    "title": "Committee trio numbers",
                    "body": "PAC 22 (opposition chair), CPU 22 (15+7), Estimates 30 (all LS). 'Estimates = 30, exclusively LS.'",
                    "example": {
                        "q": "Which parliamentary committee examines the CAG's reports?",
                        "solution": "The Public Accounts Committee (22 members, opposition chairperson by convention).",
                    },
                },
                {
                    "title": "Writ first letters",
                    "body": "**H-M-P-C-Q**: Habeas(body), Mandamus(command), Prohibition(stop-before), Certiorari(quash-after), Quo warranto(by what authority). Prohibition stops a case early; certiorari quashes after.",
                    "example": {
                        "q": "Which writ stops a subordinate court from exceeding jurisdiction before it decides?",
                        "solution": "Prohibition (certiorari operates after the order is passed).",
                    },
                },
            ],
            "mistakes": [
                "Believing a joint sitting can resolve a Constitutional Amendment Bill — Art. 108 excludes it.",
                "Saying the Rajya Sabha can be dissolved — it is permanent, with one-third retiring every two years.",
                "Assuming the sanctioned SC strength is 31 — it rose to 34 in 2019.",
            ],
        },
        {
            "id": "pol-amendments",
            "title": "Important Constitutional Amendments",
            "concept": C_AMD,
            "formulas": [],
            "tricks": [
                {
                    "title": "Amendment decade clusters",
                    "body": "1950s structural (1st, 7th) • 1970s power (24, 42, 44) • 1980s politics (52 anti-defection, 61 voting age) • 1990s grass-roots (73, 74) + language (71, 92) • 2000s rights (86, 91, 97) • 2010s-20s economy-equality (101 GST, 102 OBC, 103 EWS, 104 seats, 105 OBC-identify, 106 women).",
                    "example": {
                        "q": "Which amendment lowered the voting age from 21 to 18?",
                        "solution": "The 61st Amendment, 1988 (Art. 326).",
                    },
                },
                {
                    "title": "42 vs 44 tug-of-war",
                    "body": "Whatever the 42nd tightened, the 44th loosened: term 6→5 years, 'internal disturbance'→'armed rebellion', property FR→300A legal right.",
                    "example": {
                        "q": "Which amendment changed the ground for National Emergency from 'internal disturbance' to 'armed rebellion'?",
                        "solution": "The 44th Amendment, 1978.",
                    },
                },
            ],
            "mistakes": [
                "Attributing EWS (10%) to the 102nd — it is the 103rd; the 102nd made NCBC constitutional.",
                "Assuming the 106th applies at once — it awaits delimitation after a census.",
                "Thinking NJAC still operates — the 99th Amendment was struck down in 2015.",
            ],
        },
        {
            "id": "pol-local-bodies-emergency",
            "title": "Panchayati Raj, Municipalities and Emergency",
            "concept": C_LOCAL,
            "formulas": [],
            "tricks": [
                {
                    "title": "Committee tier-count rhyme",
                    "body": "Balwant-3 (1957), Ashok-2 (1977), Rao-district (1985), Singhvi-Constitution (1986). Decade rhyme: 57-77-85-86.",
                    "example": {
                        "q": "Which committee's report led to the Nagaur (Rajasthan) launch of Panchayati Raj on 2 October 1959?",
                        "solution": "The Balwant Rai Mehta Committee (three-tier recommendation).",
                    },
                },
                {
                    "title": "Emergency digits",
                    "body": "352-National (3 proclamations: 62, 71, 75), 356-President's Rule (Kerala 1959 first), 360-Financial (zero uses). Approvals: 1 month + every 6 months.",
                    "example": {
                        "q": "Which State first faced President's Rule in 1959?",
                        "solution": "Kerala (the elected E.M.S. Namboodiripad government was dismissed).",
                    },
                },
            ],
            "mistakes": [
                "Saying the 73rd Amendment created the Panchayats in 1959 — the 1959 date is only Rajasthan's launch; constitutional status came in 1992.",
                "Mixing 11th Schedule (29 subjects, panchayats) with 12th (18, municipalities).",
                "Claiming a Financial Emergency was declared in 1991 — Art. 360 has never been used.",
            ],
        },
        {
            "id": "pol-bodies",
            "title": "Constitutional & Statutory Bodies (with current heads)",
            "concept": C_BODIES,
            "formulas": [],
            "tricks": [
                {
                    "title": "Article blocks for bodies",
                    "body": "76-AG • 280-FC • 148-CAG • 315-UPSC • 324-EC. Descending ladder: 324 > 315 > 280 > 148 > 76 reads 'EC-UPSC-FC-CAG-AG'.",
                    "example": {
                        "q": "Under which article is the Comptroller and Auditor General appointed?",
                        "solution": "Article 148 (term: 6 years or age 65).",
                    },
                },
                {
                    "title": "Statutory vs constitutional filter",
                    "body": "If the source is a dated Act (1993 NHRC, 2003 CVC, 2005 CIC, 2013 Lokpal) it is statutory; if the source is an Article number it is constitutional; NITI Aayog (Cabinet resolution, 2015) is neither.",
                    "example": {
                        "q": "Name one high-profile advisory body that is neither constitutional nor statutory.",
                        "solution": "NITI Aayog.",
                    },
                },
            ],
            "mistakes": [
                "Calling NITI Aayog a statutory body — it is an executive-resolution body.",
                "Saying the 15th FC still governs transfers — from FY 2026-27 the 16th FC (41% share, 2026-31) applies.",
                "Confusing the CAG's examiners — CAG reports are examined by the Public Accounts Committee, not the Estimates Committee.",
            ],
        },
    ],
    "pyqPatterns": [
        {
            "pattern": "Match-the-following (articles, schedules, amendments)",
            "frequency": "very common",
            "howToSpot": "Four pairs given, one correct — e.g. Schedule with subject, amendment with provision.",
            "approach": "Eliminate pairs you know are wrong; the surviving option is the answer. Focus on 42nd/44th/73rd/101st/103rd/106th.",
        },
        {
            "pattern": "Current head of a constitutional body",
            "frequency": "very common",
            "howToSpot": "'Who is the present CJI/CEC/CAG/Attorney General?'",
            "approach": "Memorise the current-heads table; update after every appointment news cycle.",
        },
        {
            "pattern": "Borrowed features country mapping",
            "frequency": "very common",
            "howToSpot": "'X feature is taken from which country?'",
            "approach": "Use the 10-country speed-pair list; watch for Canada-vs-Australia and Ireland-vs-USSR traps.",
        },
        {
            "pattern": "Which is NOT a Fundamental Right / DPSP classification",
            "frequency": "common",
            "howToSpot": "One odd option inside a list of rights (usually property, or a duty disguised as a right).",
            "approach": "Remember property left Part III in 1978; check the article block numbers.",
        },
        {
            "pattern": "Amendment → provision one-liner",
            "frequency": "very common",
            "howToSpot": "Direct ask: 'The ... Amendment lowered voting age / added GST / reserved seats for women.'",
            "approach": "Learn the amendment table as year+keyword flashcards.",
        },
        {
            "pattern": "Committee → recommendation (PRI and Assembly committees)",
            "frequency": "common",
            "howToSpot": "'Which committee recommended two-tier panchayati raj?'",
            "approach": "Tier-count mnemonic (Balwant-3, Ashok-2) plus Assembly-committee chairman clusters.",
        },
        {
            "pattern": "Statement-based (2-3 statements, pick correct set)",
            "frequency": "common",
            "howToSpot": "'Consider the following statements...' with options like '1 and 2 only'.",
            "approach": "Test each statement against a known article; usually one statement is an absolute (always/only) trap.",
        },
        {
            "pattern": "Writ / pardon / ordinance article recall",
            "frequency": "common",
            "howToSpot": "Single-fact questions on Art. 32, 72/161, 123, 213, 226.",
            "approach": "Anchor each power to its article; note President-vs-Governor differences.",
        },
    ],
    "solvedExamples": SOLVED,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    save_topic(topic)
