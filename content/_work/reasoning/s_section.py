# write content/ssc-cgl/sections/reasoning.json
import json, os
import common as C

for tid in C.TOPIC_IDS:
    assert os.path.exists(os.path.join(C.CONTENT, 'ssc-cgl', 'topics', 'reasoning', tid + '.json')), tid
assert len(C.TOPIC_IDS) == 20

overview = (
    "General Intelligence & Reasoning carries **25 questions for 50 marks in Tier 1** (2 marks each, 0.5 negative) and "
    "**30 questions for 90 marks in Tier 2** (Paper 1, Section I, 3 marks each, 1 negative). It is the most scoring section "
    "of CGL because almost every question is a fixed pattern with a mechanical method.\n\n"
    "The syllabus falls into three families:\n\n"
    "| Family | Topics | Tier 1 share |\n|---|---|---|\n"
    "| **Verbal / number patterns** | analogy, classification, series, coding-decoding, mathematical operations, missing number, dictionary order | 13-16 Qs |\n"
    "| **Logical arrangement** | blood relations, direction & distance, order & ranking, seating arrangement, syllogism, Venn diagrams, statement-conclusion | 7-9 Qs |\n"
    "| **Non-verbal (figures)** | counting figures, mirror & water images, paper folding, embedded figures, cube & dice, figure series | 0-4 Qs |\n\n"
    "Recent Tier 1 papers (2024-2025) lean heavily on letter-cluster series, word and number analogies, coding analogies, "
    "odd-one-out, blood relations and symbol-operation equations; figure questions have become rare in Tier 1 but still "
    "appear in Tier 2.")

strategy = (
    "## Study order\n\n"
    "1. **Letter & number foundations first** — memorise letter positions (A=1 … Z=26, EJOTY = 5, 10, 15, 20, 25) and the opposite "
    "pairs (A-Z, B-Y …). These power analogy, series, coding and classification, which together are about half the paper.\n"
    "2. **Analogy → classification → series → coding-decoding** — the same letter-gap skills in four formats.\n"
    "3. **Mathematical operations → missing number** — BODMAS with swapped signs; number patterns in grids.\n"
    "4. **Blood relations → direction → order-ranking → seating** — draw every time; never solve in your head.\n"
    "5. **Syllogism → Venn diagrams → statement-conclusion** — use the minimal diagram and the definite/possible test.\n"
    "6. **Dictionary order**, then the **figure topics** last (counting figures, mirror/water, paper folding, embedded, cube & dice, figure series).\n\n"
    "## Time plan (Tier 1)\n\n"
    "Aim for **15-17 minutes** for all 25 questions, leaving time for Quant. First pass: take every letter-series, analogy, "
    "coding and odd-one-out question (20-30 s each). Second pass: blood relations, seating, operations (45-60 s). "
    "Skip any figure or puzzle that crosses 75 seconds and come back only if time remains.\n\n"
    "## Attempt strategy\n\n"
    "- Target **22-24 attempts** with 90%+ accuracy in Tier 1; reasoning is where 45+/50 is realistic.\n"
    "- Verify each answer against **all** given pairs or terms — most distractors satisfy only the first pair.\n"
    "- Guess only when you have cut the options to two; blind guesses cost 0.5 marks (1 mark in Tier 2).\n"
    "- In Tier 2, expect more syllogism, seating, dice and figure questions: practise the figure topics with a timer.\n\n"
    "## Revision loop\n\n"
    "After each mock, tag every wrong answer by topic and by *reason* (concept gap, calculation slip, misread). Redo the "
    "topic practice set for any topic with two or more errors before the next mock.")

sec = {'id': 'reasoning', 'name': 'General Intelligence & Reasoning', 'short': 'Reasoning',
       'tier1': {'questions': 25, 'marks': 50}, 'tier2': {'questions': 30, 'marks': 90},
       'overview': overview, 'strategy': strategy, 'topics': list(C.TOPIC_IDS)}
p = os.path.join(C.SECTION_DIR, 'reasoning.json')
with open(p, 'w', encoding='utf-8') as f:
    json.dump(sec, f, ensure_ascii=False, indent=1)
print('wrote', p)
