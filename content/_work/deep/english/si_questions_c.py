# Sentence-improvement practice questions, part C: si-precision-fixes, si-structure-inversion.
from _lib import Q

QS = []
P = "si-precision-fixes"
V = "si-structure-inversion"

STEM = "Select the most appropriate option to substitute the highlighted segment in the given sentence. If no substitution is required, select 'No substitution required'."

# ------------------------------------------------- si-precision-fixes (8)
QS += [
 Q("si-precision-fixes-p01", P, "sip1", STEM + "\n\nThe child is very fond **of** his grandmother.",
   ["for", "No substitution required", "with", "at"], 1,
   "The fixed pair is **fond of** → the original is standard → No substitution required. 'Fond for', 'fond with' and 'fond at' are not English.",
   "fond of — learn the pair; do not repair a correct sentence.", "easy", 30),
 Q("si-precision-fixes-p02", P, "sip1", STEM + "\n\nThe committee does not approve **for** the proposal.",
   ["of", "No substitution required", "with", "to"], 0,
   "The fixed pair is approve **of** → does not approve **of the proposal**. 'Agree with/to' tempts by meaning, but the verb here is *approve*.",
   "approve of; agree with a person / to a plan.", "medium", 35),
 Q("si-precision-fixes-p03", P, "sip2", STEM + "\n\nHe returned after **an hour** with the medicine.",
   ["a hour", "No substitution required", "the hour", "an hours"], 1,
   "**Hour** begins with a vowel sound (the h is silent) → **an hour** is correct → No substitution required. 'A hour' follows the spelling instead of the sound.",
   "an hour, an honest — silent h.", "easy", 30),
 Q("si-precision-fixes-p04", P, "sip2", STEM + "\n\nThe temple was built near **a ancient** trading route.",
   ["No substitution required", "an ancient", "a ancients", "the ancients"], 1,
   "**Ancient** begins with a vowel sound → **an ancient** trading route. Only the article needs repair; the smallest change wins.",
   "a/an by sound: ancient → an.", "easy", 30),
 Q("si-precision-fixes-p05", P, "sip3", STEM + "\n\nPlease **revert back** to my mail by Friday.",
   ["revert to", "No substitution required", "revert back to", "reversing to"], 0,
   "**Revert** already means 'come back' → the echo *back* is redundant: 'please **revert to** my mail'. 'Reverting to' breaks the request form; the original keeps the echo.",
   "revert, return, repeat — cut the echo word.", "medium", 35),
 Q("si-precision-fixes-p06", P, "sip3", STEM + "\n\nHe **wrote back a reply** immediately after reading the notice.",
   ["wrote a reply", "No substitution required", "wrote back reply", "had wrote"], 0,
   "**Wrote a reply** — 'back' echoes the idea already inside *reply* → the clean form is 'wrote a reply immediately'. 'Had wrote' uses the wrong participle.",
   "one idea, one word; wrote = put in writing.", "medium", 35),
 Q("si-precision-fixes-p07", P, "sip4", STEM + "\n\nThe doctor's **advise** was to rest for a week.",
   ["advice", "No substitution required", "advises", "advising"], 0,
   "The slot is a noun (the subject of 'was') → the doctor's **advice**. *Advise* is the verb; 'advising' would wreck the structure.",
   "advice = noun; advise = verb.", "medium", 35),
 Q("si-precision-fixes-p08", P, "sip4", STEM + "\n\nThe new rule will **affect** every contract worker.",
   ["No substitution required", "effect", "effect on", "affecting"], 0,
   "The slot needs the verb 'to influence' → **affect** is correct → No substitution required. *Effect* is the noun; 'effect on' turns the verb slot into a noun phrase.",
   "affect = verb; effect = noun.", "medium", 35),
]

# ------------------------------------------------- si-structure-inversion (9)
QS += [
 Q("si-structure-inversion-p01", V, "siv1", STEM + "\n\nNo sooner **did the inspector leave** than the clerks started chatting.",
   ["No substitution required", "the inspector had left", "did the inspector left", "the inspector left"], 0,
   "'No sooner **did the inspector leave** than…' satisfies the full frame: inversion (did + subject + base) with the partner *than* → No substitution required. 'The inspector had left' and 'the inspector left' drop the inversion; 'did the inspector left' pairs *did* with a past form.",
   "no sooner did + base…than — check all three parts before repairing.", "hard", 50),
 Q("si-structure-inversion-p02", V, "siv1", STEM + "\n\nHardly **the results had been announced** when the servers crashed.",
   ["the results had announce", "had the results been announced", "No substitution required", "the results have been announced"], 1,
   "Fronted **Hardly** demands inversion: hardly **had the results been announced** when…. The original keeps statement order; 'the results had announce' breaks the participle and the order.",
   "hardly + had + subject + been + participle…when.", "medium", 45),
 Q("si-structure-inversion-p03", V, "siv1", STEM + "\n\nNo sooner **the train had left** the platform than the TTE began checking tickets.",
   ["had the train left", "No substitution required", "the train left", "the train had leave"], 0,
   "**No sooner** demands helper-first order: no sooner **had the train left** than…. The original hides the helper after the subject; 'the train left' loses both the inversion and the perfect; 'had leave' breaks the participle.",
   "no sooner + had + subject + participle…than.", "medium", 45),
 Q("si-structure-inversion-p04", V, "siv2", STEM + "\n\nSeldom **we see** such discipline in a government office.",
   ["we saw", "No substitution required", "do we see", "we have seen"], 2,
   "Fronted **Seldom** forces inversion with do-support: seldom **do we see** such discipline. The other options keep statement order and only shuffle tense.",
   "seldom / never / rarely at the front → do/did or helper first.", "medium", 40),
 Q("si-structure-inversion-p05", V, "siv2", STEM + "\n\nNever **I have** witnessed such a peaceful poll in this constituency.",
   ["have I witnessed", "I had witnessed", "No substitution required", "I have witness"], 0,
   "Fronted **Never** pulls the helper before the subject: never **have I witnessed**. The tense stays present perfect — only the order changes; 'I have witness' breaks the participle.",
   "never + helper + subject + participle.", "easy", 35),
 Q("si-structure-inversion-p06", V, "siv3", STEM + "\n\n**Being a rainy day**, the mela was cancelled by the committee.",
   ["It being a rainy day", "No substitution required", "Being rainy day", "Been a rainy day"], 0,
   "The mela cannot *be* a rainy day — the opener dangles. The absolute construction gives it its own subject: **It being a rainy day**, the mela was cancelled.",
   "-ing opener without a doer → It being…", "medium", 45),
 Q("si-structure-inversion-p07", V, "siv3", STEM + "\n\nHaving eaten our lunch, **the train** departed from platform three.",
   ["we boarded the train", "No substitution required", "the train was departed", "boarding the train"], 0,
   "Who ate the lunch? Not the train. The doer must head the main clause: **we boarded the train**. 'The train was departed' is not English in this sense and still dangles.",
   "-ing opener borrows the main subject — name the doer.", "medium", 45),
 Q("si-structure-inversion-p08", V, "siv4", STEM + "\n\nThe training module covers **typing, to file papers, and how to draft mails**.",
   ["No substitution required", "typing, filing papers, and drafting mails", "typing, filing papers, and to draft mails", "typing, to file papers and draft mails"], 1,
   "Every item after *covers* must share one shape → the uniform -ing list: **typing, filing papers, and drafting mails**. The options that keep a to-item or a how-to clause leave the line broken.",
   "lists stay parallel: match the first item's shape.", "medium", 45),
 Q("si-structure-inversion-p09", V, "siv4", STEM + "\n\nShe is **not only intelligent but also she works hard**.",
   ["not only intelligent but also hardworking", "No substitution required", "not only intelligent but works hard also", "not only an intelligent but also hard work"], 0,
   "The correlative must join equal shapes: **not only intelligent but also hardworking** — two adjectives. The original pairs an adjective with a full clause; the decoys break the pair order or the word class.",
   "not only X but also Y — X and Y must be the same kind.", "hard", 50),
]
