# New practice questions for synonyms-antonyms. In every item opts[0] is the correct answer;
# QA() moves it to a deterministic position. TARGET records the headword each question asks,
# so the build script can check that no headword is asked twice in practice.
from _lib import QA

TARGET = {}
SYN = "Select the word which is nearest in meaning to the given word.  "
ANT = "Select the word which is most opposite in meaning to the given word.  "
SSYN = "Select the word which is nearest in meaning to the word in CAPITALS.\n\n"
SANT = "Select the word which is most opposite in meaning to the word in CAPITALS.\n\n"


def mk(qid, sub, pat, target, q, opts, solution, shortcut=None, diff="medium", t=25):
    TARGET[qid] = target.lower()
    return QA(qid, sub, pat, q, opts, solution, shortcut=shortcut, diff=diff, t=t)


def QS_SA():
    qs = []
    A = qs.append
    RM = "syn-root-word-method"
    EL = "syn-elimination"
    PF = "ant-prefix-flip"
    ST = "syn-ant-strategy"

    # ---------------- syn-root-word-method (srm) ----------------
    A(mk("syn-root-word-method-p01", RM, "srm-p1", "malicious", SYN + "MALICIOUS",
         ["spiteful", "kind-hearted", "careless", "honest"],
         "mal = bad → intending harm → **spiteful**. The other options fail the direction check: a mal- word must be negative.",
         "mal = bad (malnutrition).", "medium", 25))
    A(mk("syn-root-word-method-p02", RM, "srm-p2", "magnanimous", SYN + "MAGNANIMOUS",
         ["generous", "miserly", "short-tempered", "fearful"],
         "magn (great) + anim (mind, spirit) → great-spirited = **generous**, ready to forgive. Miserly is the opposite direction.",
         "magn = great, anim = spirit.", "hard", 30))
    A(mk("syn-root-word-method-p03", RM, "srm-p2", "amicable", SYN + "AMICABLE",
         ["friendly", "hostile", "rude", "gloomy"],
         "am/amic = friend (as in amiable) → **friendly**. An amicable settlement is a friendly one; hostile fails the direction check.",
         "amic = friend.", "medium", 25))
    A(mk("syn-root-word-method-p04", RM, "srm-p3", "portable", SYN + "PORTABLE",
         ["easy to carry", "heavy", "fragile", "costly"],
         "port = carry → **easy to carry** (transport, export share the root).",
         "port = carry.", "easy", 20))
    A(mk("syn-root-word-method-p05", RM, "srm-p1", "benefactor", SYN + "BENEFACTOR",
         ["one who gives money or help", "one who receives help", "an opponent", "a spectator"],
         "bene = good + factor (doer) → one who does good = **one who gives money or help**. The direction check removes everything negative.",
         "bene = good (benefit).", "medium", 25))
    A(mk("syn-root-word-method-p06", RM, "srm-p3", "inspect", SYN + "INSPECT",
         ["examine closely", "ignore", "repair", "reject"],
         "spect = look → to look into = **examine closely** (spectator, spectacle share the root).",
         "spect = look.", "easy", 20))
    A(mk("syn-root-word-method-p07", RM, "srm-p3", "chronological", SYN + "CHRONOLOGICAL",
         ["arranged in time order", "arranged alphabetically", "arranged at random", "arranged by place"],
         "chron = time → **arranged in time order** (a chronology of events).",
         "chron = time.", "medium", 25))
    A(mk("syn-root-word-method-p08", RM, "srm-p4", "restive", SYN + "RESTIVE",
         ["restless", "calm", "lazy", "sleepy"],
         "**Restive** = restless, hard to control. It merely looks like 'rest' — a false-root word, so 'calm' is the trap.",
         "Restive ≠ restful.", "hard", 30))
    A(mk("syn-root-word-method-p09", RM, "srm-p4", "enervate", SYN + "ENERVATE",
         ["weaken", "energise", "irritate", "excite"],
         "**Enervate** = to drain of strength = weaken. It looks like 'energy' but points the other way; 'energise' is the planted trap.",
         "Enervate takes energy away.", "hard", 30))
    A(mk("syn-root-word-method-p10", RM, "srm-p3", "circumvent", SYN + "CIRCUMVENT",
         ["to get around by clever means", "to surround completely", "to conquer by force", "to support openly"],
         "circum = around + vent = come → to come around a rule = **get around it by clever means**.",
         "circum = around (circumference).", "medium", 30))

    # ---------------- syn-elimination (sel) ----------------
    A(mk("syn-elimination-p01", EL, "sel-p2", "trivial", SYN + "TRIVIAL",
         ["unimportant", "serious", "complex", "vital"],
         "**Trivial** = of very little importance. Serious and vital sit at the wrong end of the importance scale.",
         "Degree: trivial is the low end.", "easy", 20))
    A(mk("syn-elimination-p02", EL, "sel-p3", "hostile", SYN + "HOSTILE",
         ["unfriendly", "friendly", "shy", "calm"],
         "**Hostile** = showing enmity → unfriendly. The charge must stay negative.",
         "Charge: negative.", "easy", 20))
    A(mk("syn-elimination-p03", EL, "sel-p2", "deluge", SYN + "DELUGE",
         ["flood", "drizzle", "drought", "mist"],
         "**Deluge** = a great flood of water — the extreme end. Drizzle, drought and mist are the same class but the wrong degree.",
         "Deluge = drenched.", "medium", 25))
    A(mk("syn-elimination-p04", EL, "sel-p1", "release", SYN + "RELEASE",
         ["set free", "freedom", "capture", "tighten"],
         "The stem is a verb, so **set free** matches the slot; 'freedom' is the noun decoy; capture and tighten reverse the meaning.",
         "Match the part of speech.", "medium", 25))
    A(mk("syn-elimination-p05", EL, "sel-p1", "abolish", SYN + "ABOLISH",
         ["do away with", "establish", "approve", "shorten"],
         "**Abolish** = to do away with (a law, a system) — a verb; 'establish' is its opposite.",
         "Abolish ends systems.", "medium", 25))
    A(mk("syn-elimination-p06", EL, "sel-p3", "cautious", SYN + "CAUTIOUS",
         ["careful", "careless", "bold", "hasty"],
         "**Cautious** = careful to avoid danger. Careless, bold and hasty carry the opposite charge.",
         "Cautious = careful.", "medium", 20))
    A(mk("syn-elimination-p07", EL, "sel-p4", "laconic", SSYN + "His LACONIC reply contained exactly two words.",
         ["using very few words", "lengthy", "talkative", "loud"],
         "A two-word reply → **using very few words**. The sentence fixes the sense; lengthy and talkative point the other way.",
         "Laconic = tight-lipped.", "hard", 30))
    A(mk("syn-elimination-p08", EL, "sel-p4", "alleviated", SSYN + "The new medicine ALLEVIATED the patient's pain within an hour.",
         ["lessened", "increased", "caused", "hid"],
         "A medicine that helps within an hour → **lessened** the pain. Increased and caused reverse the sense.",
         "Alleviate = lighten.", "medium", 25))

    # ---------------- ant-prefix-flip (apf) ----------------
    A(mk("ant-prefix-flip-p01", PF, "apf-p1", "scarce", ANT + "SCARCE",
         ["plentiful", "tiny", "weak", "short"],
         "Scale = quantity. The far end of scarce is **plentiful**; tiny, weak and short are unrelated scales.",
         "Quantity scale: scarce ↔ plentiful.", "easy", 20))
    A(mk("ant-prefix-flip-p02", PF, "apf-p1", "accept", ANT + "ACCEPT",
         ["refuse", "agree", "offer", "except"],
         "Complementary pair: accept ↔ **refuse**. 'Except' only looks like 'accept' — a spelling trap, not an opposite.",
         "accept ↔ refuse.", "easy", 20))
    A(mk("ant-prefix-flip-p03", PF, "apf-p2", "invaluable", ANT + "INVALUABLE",
         ["worthless", "priceless", "expensive", "valuable"],
         "**Invaluable** = extremely valuable (priceless), so its true opposite is **worthless**. Priceless, expensive and valuable are all synonym traps built on the prefix flip.",
         "Invaluable ≠ not valuable.", "hard", 30))
    A(mk("ant-prefix-flip-p04", PF, "apf-p2", "inflammable", ANT + "INFLAMMABLE",
         ["fireproof", "flammable", "easily lit", "heated"],
         "**Inflammable** = easily set on fire (the same as flammable), so the opposite is **fireproof**. Flammable is the famous false-flip trap.",
         "Inflammable burns.", "hard", 30))
    A(mk("ant-prefix-flip-p05", PF, "apf-p3", "superfluous", ANT + "SUPERFLUOUS",
         ["essential", "surplus", "extra", "spare"],
         "**Superfluous** = more than needed. Surplus, extra and spare all mean the same — strike the synonyms first; what truly reverses it is **essential**.",
         "Strike synonyms, keep the opposite.", "hard", 30))
    A(mk("ant-prefix-flip-p06", PF, "apf-p1", "maximum", ANT + "MAXIMUM",
         ["minimum", "largest", "greatest", "highest"],
         "Scale = amount. The other end of maximum is **minimum**; the other three are synonyms.",
         "max ↔ min.", "easy", 20))
    A(mk("ant-prefix-flip-p07", PF, "apf-p4", "optimist", ANT + "OPTIMIST",
         ["pessimist", "realist", "idealist", "romantic"],
         "The -ist nouns pair up: optimist ↔ **pessimist**. A realist and an idealist differ in outlook but are not opposites of an optimist.",
         "opti ↔ pessi.", "easy", 20))
    A(mk("ant-prefix-flip-p08", PF, "apf-p4", "ascend", ANT + "ASCEND",
         ["descend", "climb", "rise", "mount"],
         "Direction pair: ascend ↔ **descend**. Climb, rise and mount are synonym decoys.",
         "a ↔ de (up ↔ down).", "medium", 20))
    A(mk("ant-prefix-flip-p09", PF, "apf-p3", "abandon", ANT + "ABANDON",
         ["retain", "desert", "forsake", "quit"],
         "Desert, forsake and quit all mean the same as **abandon** — strike the synonyms first; the word that truly reverses it is **retain** (to keep).",
         "Strike synonyms, keep the opposite.", "medium", 25))

    # ---------------- syn-ant-strategy (sas) ----------------
    A(mk("syn-ant-strategy-p01", ST, "sas-p1", "serviceable", SSYN + "The old tractor was still SERVICEABLE after twenty years.",
         ["fit for use", "attractive", "costly", "decorative"],
         "Still working after twenty years → **fit for use**. The sentence, not the word's rarity, decides.",
         "service → serves its purpose.", "medium", 25))
    A(mk("syn-ant-strategy-p02", ST, "sas-p1", "coherent", SSYN + "The witness gave a clear and COHERENT account of the accident.",
         ["logical and connected", "confusing", "brief", "false"],
         "An account that hangs together → **logical and connected**. Confusing points the other way; brief and false are different ideas altogether.",
         "cohere = stick together.", "medium", 25))
    A(mk("syn-ant-strategy-p03", ST, "sas-p2", "barren", SANT + "In the dry summer the fields lay BARREN.",
         ["fertile", "dry", "empty", "bare"],
         "**Barren** = bearing no crop; its true opposite is **fertile**. Dry, empty and bare all mean the same as barren — strike the synonyms first.",
         "barren ↔ fertile.", "medium", 25))
    A(mk("syn-ant-strategy-p04", ST, "sas-p2", "clement", SANT + "The judge was known for his CLEMENT decisions.",
         ["harsh", "gentle", "mild", "forgiving"],
         "**Clement** = mild, merciful. Gentle, mild and forgiving are synonyms; the reverse of mercy is **harsh**.",
         "clement ↔ inclement weather.", "hard", 30))
    A(mk("syn-ant-strategy-p05", ST, "sas-p3", "economical", SYN + "ECONOMICAL",
         ["careful with money", "extravagant", "rich", "greedy"],
         "**Economical** = avoiding waste → careful with money. Extravagant is the opposite charge.",
         "Economical ≠ expensive.", "easy", 20))
    A(mk("syn-ant-strategy-p06", ST, "sas-p3", "victorious", ANT + "VICTORIOUS",
         ["defeated", "triumphant", "winning", "successful"],
         "Command word = opposite. Strike the synonym decoys (triumphant, winning, successful) → **defeated**.",
         "victory ↔ defeat.", "easy", 20))
    A(mk("syn-ant-strategy-p07", ST, "sas-p4", "audible", SSYN + "Even in the last row the lecturer's voice was clearly AUDIBLE.",
         ["able to be heard", "visible", "silent", "vague"],
         "aud = hear, and the sentence confirms it → **able to be heard**. Root and context point the same way.",
         "aud = hear (audience).", "easy", 20))
    A(mk("syn-ant-strategy-p08", ST, "sas-p4", "sparse", SSYN + "The hill village had a SPARSE population scattered over many slopes.",
         ["thinly scattered", "dense", "unhealthy", "shifting"],
         "Scattered over many slopes → **thinly scattered**. Dense is the opposite; the other two are unrelated.",
         "Sparse ↔ dense.", "medium", 25))
    A(mk("syn-ant-strategy-p09", ST, "sas-p3", "amateur", SYN + "AMATEUR",
         ["non-professional", "expert", "professional", "skilled"],
         "**Amateur** = one who plays for pleasure, not pay → non-professional. Expert, professional and skilled all point the other way.",
         "Amateur ≠ paid.", "medium", 25))
    A(mk("syn-ant-strategy-p10", ST, "sas-p1", "immediate", SSYN + "The injection had an IMMEDIATE effect on the fever.",
         ["instant", "delayed", "sudden", "brief"],
         "Effect right after the injection → **instant**. Delayed is the opposite; sudden means unexpected, brief means short — different ideas.",
         "immediate = no gap.", "medium", 20))
    A(mk("syn-ant-strategy-p11", ST, "sas-p3", "proposed", SYN + "PROPOSED",
         ["put forward", "rejected", "withdrawn", "opposed"],
         "**Proposed** = put forward (a plan, a name). Rejected, withdrawn and opposed reverse or block the act.",
         "propose ↔ dispose.", "easy", 20))
    A(mk("syn-ant-strategy-p12", ST, "sas-p2", "gaunt", SANT + "His GAUNT face showed the months he had spent in hospital.",
         ["plump", "thin", "haggard", "pale"],
         "**Gaunt** = thin and bony. Thin and haggard are synonym decoys; pale is a different idea; the true opposite is **plump**.",
         "Gaunt ↔ well-fleshed.", "hard", 30))

    return qs
