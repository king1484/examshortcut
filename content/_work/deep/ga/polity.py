"""Phase-2 deep content for ga/polity. Run: py -3 polity.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from po_part1 import build_making, build_preamble, build_frs, build_executive
from po_part2 import build_parliament, build_amendments, build_local, build_bodies


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Match-the-following (articles, schedules, amendments)", "very common",
      "Four pairs are offered — an Article with its subject, a Schedule with its content, or an amendment with its provision — and the candidate picks the fully correct set.",
      "Hold three tables cold: Parts↔article ranges, Schedules 1–12 content, and the amendment ladder (42 Mini-Constitution, 44 property out, 52 defection, 61 vote at 18, 73/74 local bodies, 86 education, 101 GST, 103 EWS, 106 women). Test each pair; one wrong letter usually knocks out three options.",
      "pol-preamble-parts",
      "Which of the following pairs is correctly matched?\n(a) Tenth Schedule — Municipal subjects\n(b) Eleventh Schedule — Panchayat subjects\n(c) Ninth Schedule — Languages\n(d) Eighth Schedule — Anti-defection",
      "(b) — Eleventh Schedule carries the 29 panchayat subjects. Tenth = defection, Ninth = protected laws, Eighth = languages."),
    P("Office ↔ appointment, tenure and removal", "very common",
      "'Who appoints X', 'how is X removed', 'what is X's tenure' — asked for the CEC, CAG, UPSC members, Finance Commission, Attorney-General or the Vice-President.",
      "Recall the removal ladders: CEC/CAG/UPSC chairman — like a Supreme Court judge; other Election Commissioners — on the CEC's recommendation; Vice-President — Rajya Sabha resolution (effective majority, 14 days' notice) concurred in by the Lok Sabha; Governor — holds office at the President's pleasure. Tenure trio: 6 years or 65 (CEC, CAG, UPSC).",
      "pol-bodies",
      "The Comptroller and Auditor-General of India holds office for —",
      "Six years from assuming office, or until 65 years of age, whichever is earlier — and he cannot take any further government office afterwards."),
    P("Borrowed features country mapping", "very common",
      "A feature (DPSP, fundamental duties, joint sitting, concurrent list, writs, impeachment) is named and its source country asked, or four pairs are offered.",
      "Map it: FRs, judicial review, impeachment — USA; DPSP, President's election, 12 RS nominees — Ireland; duties, justice ideal — USSR; liberty-equality-fraternity, Republic — France; strong Centre, residuary with Centre — Canada; concurrent list, joint sitting — Australia; amendment procedure — South Africa; 'procedure established by law' — Japan; parliamentary system, single citizenship — Britain.",
      "pol-making",
      "The idea of **residuary powers with the Union** was borrowed from which constitution?",
      "Canada — like Canada, India leaves unlisted subjects to the Centre, and both appoint provincial/state governors from above."),
    P("Which is NOT a Fundamental Right / DPSP classification", "very common",
      "Options mix real rights with legal/constitutional rights (property under 300A is the classic trap), or ask which directive belongs to the Gandhian/socialist/liberal group.",
      "The six rights run 14–32; property is **not** one — it sits at Article 300A (44th Amendment). DPSP groups: Gandhian 40/43/43B/46/47/48, socialist 38/39/39A/41/42/43A, liberal 44/45/48A/49/50/51. Uniform civil code (44) is the evergreen answer.",
      "pol-fundamental-rights",
      "Which of the following is NOT a Fundamental Right?\n(a) Right against exploitation (b) Right to property (c) Right to constitutional remedies (d) Right to freedom of religion",
      "(b) — property was removed from Part III by the 44th Amendment (1978) and survives as a legal right under Article 300A."),
    P("Amendment → provision one-liner", "very common",
      "A single amendment number (1st, 42nd, 44th, 52nd, 61st, 73rd, 86th, 101st, 103rd, 106th) or a provision is given and the matching half is asked.",
      "Learn the number hooks: 42 = Mini-Constitution, 44 = property out and 'armed rebellion' in, 52 = Tenth Schedule, 61 = vote at 18, 69 = Delhi NCT, 73/74 = PRI and municipalities, 86 = Article 21A, 91 = 15% ministry cap, 101 = GST, 103 = EWS 10%, 106 = women's one-third.",
      "pol-amendments",
      "The voting age in Lok Sabha elections was reduced from 21 to 18 years by which amendment?",
      "The 61st Constitutional Amendment Act, 1989 — it amended Article 326."),
    P("Committee → recommendation (PRI and Assembly committees)", "common",
      "'Which committee recommended a two-tier panchayati raj' or a Constituent Assembly committee is matched with its chairman.",
      "PRI ladder: Balwant Rai Mehta (1957) three-tier, Ashok Mehta (1977) two-tier, G.V.K. Rao (1981) district planning, L.M. Singhvi (1986) constitutional status + Gram Sabha, Thungon (1988) constitutional recognition. Assembly rule: Nehru = union subjects, Patel = provinces and rights, Prasad = procedure/flag, Ambedkar = drafting.",
      "pol-local-bodies-emergency",
      "Which committee first recommended the three-tier Panchayati Raj system?",
      "The Balwant Rai Mehta Committee (1957) — village, block and district tiers; realised in Rajasthan's Nagaur launch of 2 October 1959."),
    P("Statement-based (2-3 statements, pick correct set)", "very common",
      "Two or three numbered statements about an institution, an emergency provision or a procedure are offered and the candidate picks which are correct.",
      "Kill options with one clear error: e.g. 'nominated MPs vote in the President's election' (false), 'joint sitting applies to Money Bills' (false), 'Article 19 auto-suspends in an armed-rebellion emergency' (false — only war/external aggression), 'CAG can accept a post-retirement job' (false). Then check the rest.",
      "pol-parliament-judiciary",
      "Consider: 1. A Money Bill can be introduced only in the Lok Sabha. 2. The Rajya Sabha can amend a Money Bill. Which are correct?",
      "Statement 1 only — the Rajya Sabha must return a Money Bill within 14 days with recommendations; it cannot amend."),
    P("Writ / pardon / ordinance article recall", "common",
      "A situation (illegal detention, an office held without title, a stalled duty) maps to a writ; or an article (123, 161, 213, 72) is matched with ordinance/pardon powers.",
      "Writs: habeas corpus = detention, mandamus = duty, prohibition/certiorari = stop/quash a lower court, quo warranto = office title. Pardon spread: Article 72 (President) covers death, courts-martial, Union law; Article 161 (Governor) has no death pardon. Ordinances: 123 Union, 213 state; lapse six weeks after reassembly.",
      "pol-executive",
      "An ordinance promulgated by the President ceases to operate —",
      "Six weeks after Parliament reassembles, unless approved earlier; under Article 123 ordinances are valid only while Parliament is not in session."),
]

if __name__ == "__main__":
    subs = [build_making(), build_preamble(), build_frs(), build_executive(),
            build_parliament(), build_amendments(), build_local(), build_bodies()]
    apply_topic("polity", subs, PYQ)
