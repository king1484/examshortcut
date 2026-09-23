from _lib import *
from fractions import Fraction as Fr

# ------------------------------------------------------------------ checks
assert Fr(1, 12) + Fr(1, 24) == Fr(3, 24) and Fr(24, 3) == 8          # S1
assert Fr(1, 10) - Fr(1, 15) == Fr(1, 30)                             # S2
assert Fr(1, 12) / 3 == Fr(1, 36) and Fr(36, 2) == 18                 # S3
assert 15 * 20 == 300 and 300 / 25 == 12                              # S4
assert Fr(1, 8) - Fr(1, 12) == Fr(1, 24) and Fr(1, 12) / Fr(1, 24) == 2  # S5 ratio 2:1
assert 1200 * Fr(1, 3) == 400
assert Fr(1, 10) + Fr(1, 20) == Fr(3, 20) and Fr(20, 3) == 6 + Fr(2, 3)   # E1
assert Fr(1, 6) + Fr(1, 12) + Fr(1, 18) == Fr(11, 36)                 # E2
assert Fr(1, 12) + Fr(1, 24) == Fr(1, 8)                              # E3
assert 12 * 15 == 180 and 180 / 20 == 9                               # E4
assert Fr(1, 12) / 4 == Fr(1, 48) and 48 / 3 == 16                    # E5
assert Fr(4, 15) == Fr(4, 15) and 20 * Fr(11, 15) == Fr(44, 3)        # M1
assert Fr(1, 8) + Fr(1, 12) - Fr(1, 6) == Fr(1, 24)                   # M2
assert Fr(1, 8) + Fr(1, 12) + Fr(1, 16) == Fr(13, 48) and Fr(13, 48) / 2 == Fr(13, 96)  # M3
assert Fr(6, 1) * Fr(5, 2) == 15                                       # M4 A: 2/5 in 6 days -> full 15
assert Fr(9, 1) * Fr(4, 3) == 12                                       # M4 B: 3/4 in 9 days -> full 12
assert Fr(1, 15) + Fr(1, 12) == Fr(3, 20)                              # M4 together
assert 500 * 27 == 13500 and 13500 - 1500 == 12000 and 12000 / 800 == 15  # M5
assert Fr(1, 12) / Fr(1, 18) == Fr(3, 2) and 840 * Fr(3, 5) == 504     # M6
assert Fr(1, 6) + Fr(1, 12) == Fr(1, 4) and 4 * Fr(1, 4) == 1          # M7 4 cycles of 2 days
assert 45 * 16 == 720 and 720 - 180 == 540 and Fr(540, 81) == Fr(20, 3)  # H1
assert Fr(1, 12) + Fr(1, 16) == Fr(7, 48) and Fr(7, 48) * 4 == Fr(7, 12)  # H2
assert 1 - Fr(7, 12) == Fr(5, 12) and Fr(7, 48) - Fr(1, 24) == Fr(5, 48)
assert Fr(5, 12) / Fr(5, 48) == 4 and 4 + 4 == 8
assert 3 * 12 - 12 == 24 and Fr(1, 12) + Fr(1, 36) == Fr(1, 9)         # H3

subtopics = [
 sub("tw-basics", "Work Rates & the LCM Method",
  md(r"Think of a whole job as 1 unit. A person who finishes in T days works at rate $\frac{1}{T}$ per day.",
     "",
     r"$$\text{combined rate} = \frac{1}{T_1} + \frac{1}{T_2} + \cdots, \qquad T_{\text{together}} = \frac{1}{\text{combined rate}}$$",
     "",
     r"**LCM method (no fractions):** take total work = LCM of the given days. If A takes 12 and B takes 24, set work = 24 units; A does 2/day, B does 1/day; together 3/day ⇒ 8 days. Whole numbers only — faster and safer.",
     "",
     r"**Symmetry shortcut:** two workers of times a and b together take $\frac{ab}{a+b}$ days."),
  [formula("One-day work", r"\frac{1}{T}"),
   formula("Combined time (two workers)", r"T = \frac{ab}{a + b}"),
   formula("Combined time (three workers)", r"T = \frac{abc}{ab + bc + ca}"),
   formula("Work done", r"W = \text{rate} \times \text{time}")],
  [trick("LCM units, not fractions",
         "Set the job to the LCM of the individual times; rates become small integers.",
         "A finishes a job in 10 days and B in 20 days. Working together, they finish in:",
         "Work = 20 units. A: 2/day, B: 1/day ⇒ 3/day ⇒ $20/3 = 6\\frac{2}{3}$ days."),
   trick("The ab/(a+b) reflex",
         "For exactly two workers, one formula — no addition of fractions.",
         "A does a job in 6 days, B in 12 days. Together they need:",
         r"$\frac{6 \times 12}{6 + 12} = 4$ days. (Sanity: less than either alone ✓.)"),
   trick("Three workers through the LCM",
         "Same method, three rates.",
         "A, B and C take 6, 12 and 18 days respectively. Working together, they complete the work in:",
         r"Work = 36 units; rates 6, 3, 2 ⇒ 11/day ⇒ $36/11 = 3\frac{3}{11}$ days.")],
  [r"Adding the days ($12 + 24 = 36$) instead of adding the rates.",
   r"For three workers, applying $\frac{ab}{a+b}$ pairwise instead of the three-way formula.",
   "Forgetting the combined time must be less than the smallest individual time.",
   "Mixing units — one rate in days, another in hours."]),

 sub("tw-efficiency", "Efficiency, 'Twice as Good' & Ratio Cases",
  md(r"Efficiency is rate. **Efficiency is inversely proportional to time**: twice as efficient ⇒ half the days.",
     "",
     r"$$\frac{\text{efficiency}_A}{\text{efficiency}_B} = \frac{\text{time}_B}{\text{time}_A}$$",
     "",
     r"If A is k times as good as B and together they take T days: rate $= (k+1)$ units ⇒ B alone takes $(k+1)T$ days, A alone takes $\frac{(k+1)T}{k}$ days.",
     "",
     "Convert every 'twice as good / half as efficient' statement into a rate ratio first — everything else is arithmetic."),
  [formula("Efficiency ⇄ time", r"\frac{E_A}{E_B} = \frac{T_B}{T_A}"),
   formula("k-times worker", r"T_B = (k+1)T, \quad T_A = \frac{(k+1)T}{k}"),
   formula("Efficiency ratio from times", r"E_A : E_B = \frac{1}{T_A} : \frac{1}{T_B}")],
  [trick("Rate units from the efficiency ratio",
         "Let B = 1 unit/day, A = k units/day; total = (k+1)/day.",
         "A is twice as efficient as B, and together they finish a job in 12 days. B alone would take:",
         "Units: A + B = 3/day = whole job in 12 ⇒ job = 36 units ⇒ B alone = **36 days** (A: 18)."),
   trick("Invert, never scale",
         "'A is 3 times as good' ⇒ A's days = B's days ÷ 3.",
         "A is 3 times as efficient as B and together they complete the work in 12 days. A alone takes:",
         "4 units/day ⇒ job = 48 ⇒ A = 48/3 = **16 days**."),
   trick("Days-difference cases",
         "'B takes 24 days more than A' plus an efficiency ratio pins both times.",
         "A is 3 times as fast as B and takes 24 days less than B. Together they would finish the work in:",
         "Times x and 3x with 3x − x = 24 ⇒ x = 12, so A = 12, B = 36; together $\\frac{36}{4} = 9$ days.")],
  [r"Scaling days when told efficiency scales ('twice as good' means HALF the days, not double).",
   "Adding efficiencies as days.",
   r"Using $kT$ for the stronger worker's time instead of $\frac{(k+1)T}{k}$.",
   "Ignoring that 'x times as fast' and 'x% more efficient' set up different ratios."]),

 sub("tw-pipes", "Pipes & Cisterns",
  md(r"Inlets fill (+rate), outlets/leaks drain (−rate). Treat the tank as 1 unit (or LCM litres).",
     "",
     r"$$\text{net rate} = \sum_{\text{inlets}} \frac{1}{T_i} - \sum_{\text{outlets}} \frac{1}{T_j}, \qquad \text{time} = \frac{1}{\text{net rate}}$$",
     "",
     r"**Two pipes, one filling one emptying:** net time $= \frac{ab}{b - a}$ (a = fill time, b > a = empty time).",
     "",
     "Stage-based problems: compute the work already done in the first stage, then re-solve the remainder with the new set of pipes."),
  [formula("Net filling rate", r"\frac{1}{T} = \sum \frac{1}{T_i^{\,+}} - \sum \frac{1}{T_j^{\,-}}"),
   formula("Fill + drain pair", r"T = \frac{ab}{b - a}"),
   formula("Work done in stage 1", r"W_1 = \text{rate}_1 \times t_1"),
   formula("Tank as LCM units", r"\text{tank} = \text{LCM of times; rates in units/hour}")],
  [trick("Sign discipline",
         "Empty pipes subtract. Write + and − before adding anything.",
         "Two pipes fill a tank in 8 hours and 12 hours; a third empties it in 6 hours. With all three open, the tank fills in:",
         r"$\frac{1}{8} + \frac{1}{12} - \frac{1}{6} = \frac{3 + 2 - 4}{24} = \frac{1}{24}$ ⇒ **24 hours**."),
   trick("Stage the problem",
         "Finish stage 1 first, then treat the remainder as a fresh tank.",
         "Pipes A (12 h) and B (16 h) fill a tank. Both run for 4 hours, then a drain (24 h) is also opened. The tank is full after how many more hours?",
         r"In 4 h: $\frac{7}{48} \times 4 = \frac{7}{12}$ done. New rate $= \frac{7}{48} - \frac{1}{24} = \frac{5}{48}$, so the remainder takes $\frac{5}{12} \div \frac{5}{48} = 4$ h ⇒ total **8 hours**."),
   trick("Fill-and-drain pair formula",
         "One inlet, one outlet: net time = ab/(b − a).",
         "A pipe fills a tank in 10 hours; a leak empties the full tank in 15 hours. With both, the tank fills in:",
         r"$\frac{10 \times 15}{15 - 10} = 30$ hours.")],
  [r"Adding an outlet's rate instead of subtracting it.",
   "Forgetting the tank may already be part-full when a new pipe opens.",
   r"Using $\frac{ab}{a+b}$ for a fill-drain pair (that formula is for two inlets).",
   "Reporting the stage-1 time instead of the total time."]),

 sub("tw-man-days", "Men–Days–Hours Chain & Provisions",
  md(r"Work is the product of every resource: $\text{Work} = M \times D \times H \times E$ (men, days, hours/day, efficiency).",
     "",
     r"$$\frac{M_1 D_1 H_1 E_1}{W_1} = \frac{M_2 D_2 H_2 E_2}{W_2}$$",
     "",
     r"**Same work ⇒ equal products:** $M_1 D_1 = M_2 D_2$. More men ⇒ fewer days (inverse proportion).",
     "",
     r"**Provisions problems:** stock = men × days. After t days, remaining stock feeds the new headcount: $\text{days} = \frac{M_1 D_{\text{left}}}{M_2}$.",
     "",
     "Consumption questions (garrison, fodder, food stores) are men-days problems in disguise."),
  [formula("MDH chain", r"M_1 D_1 H_1 E_1 = M_2 D_2 H_2 E_2 \quad (W_1 = W_2)"),
   formula("Men × days constant", r"M_1 D_1 = M_2 D_2"),
   formula("Provisions remaining", r"\text{days} = \frac{M_1 (D_{\text{total}} - t)}{M_2}"),
   formula("Piece of work", r"\text{days for } \tfrac{k}{n} \text{ of work} = \frac{k}{n} T")],
  [trick("Multiply resources, equate products",
         "Everything inverse-proportional lands in the numerator; direct-proportional in the denominator.",
         "15 men complete a work in 20 days. In how many days will 25 men complete the same work?",
         r"$15 \times 20 = 25 \times D$ ⇒ $D = 12$ days."),
   trick("Provisions after reinforcement",
         "Stock left = original men × days left; then divide by the new headcount.",
         "A garrison of 500 men has provisions for 27 days. After 3 days, 300 more men join. The provisions will now last:",
         r"Stock left $= 500 \times 24 = 12000$ man-days ⇒ $\frac{12000}{800} = 15$ days."),
   trick("Work left after a share is done",
         "First find what fraction remains, then apply men-days to that remainder.",
         "45 men start a job they would finish in 16 days. After 4 days, 36 more men join. The remaining work now takes:",
         r"Left $= \frac{540}{81} = 6\frac{2}{3}$ days."),
   ],
  [r"Putting more men in the numerator of the chain equation (more men ⇒ fewer days ⇒ denominator).",
   "Forgetting to subtract elapsed days in provisions problems.",
   "Counting efficiency twice — E belongs inside the product once.",
   "Applying men-days to the whole work instead of the remaining work."]),

 sub("tw-cases", "Joining / Leaving Mid-work, Alternate Days & Wages",
  md(r"Three classic twists, one method — compute the work actually done by each worker:",
     "",
     r"- **A leaves after t days:** work done $= \frac{t}{T_A}$; the rest is finished by B alone.",
     r"- **Alternate days:** pair the days. A 2-day cycle does $\frac{1}{T_A} + \frac{1}{T_B}$; count complete cycles, then handle the leftover.",
     r"- **Wages:** money splits in the ratio of work actually done — i.e. the ratio of daily rates when all work the full time.",
     "",
     r"Wage ratio for full-time co-workers: $A : B = \frac{1}{T_A} : \frac{1}{T_B} = T_B : T_A$."),
  [formula("Work done by A in t days", r"\frac{t}{T_A}"),
   formula("Remaining work", r"1 - \frac{t}{T_A}"),
   formula("Two-day cycle", r"\frac{1}{T_A} + \frac{1}{T_B} \text{ per 2 days}"),
   formula("Wage split", r"w_A = \text{total} \times \frac{1/T_A}{1/T_A + 1/T_B}")],
  [trick("Subtract the finished part",
         "Whoever continues inherits only the remainder.",
         "A can do a work in 15 days and B in 20 days. A works for 4 days and leaves. B alone finishes the rest in:",
         r"A did $\frac{4}{15}$; left $= \frac{11}{15}$ ⇒ B needs $20 \times \frac{11}{15} = 14\frac{2}{3}$ days."),
   trick("Count full cycles, then the tail",
         "Alternate days: measure progress per 2-day cycle.",
         "A takes 6 days and B takes 12 days for a job. They work on alternate days, A starting. The job is finished in:",
         r"Per 2 days: $\frac{1}{6} + \frac{1}{12} = \frac{1}{4}$ ⇒ 4 cycles = 8 days exactly."),
   trick("Wages follow work, not days alone",
         "Rate ratio × equal days = work ratio.",
         "A alone does a work in 12 days, B in 18 days. They work together and earn ₹840. A's share is:",
         r"$A : B = \frac{1}{12} : \frac{1}{18} = 3 : 2$ ⇒ A gets $840 \times \frac{3}{5} = 504$, i.e. ₹504.")],
  [r"Splitting wages by days instead of by work done when efficiencies differ.",
   "In alternate-day problems, forgetting who works the final partial day.",
   "Applying the remaining work to both workers ('B finishes 11/15' — not both B and A).",
   "Counting a 2-day cycle as 1 day when pairing alternate workers."]),
]

pyq = [
 pat("Two or three people working together", "very common",
     "Individual completion times given; find the combined time (or reverse).",
     "LCM units or ab/(a+b). Three people: rate sum, or abc/(ab+bc+ca)."),
 pat("Pipes & cisterns", "very common",
     "Fill pipes + an outlet/leak; find the fill time or who's open when.",
     "Net rate with signs; stage the problem when pipes open mid-way."),
 pat("Efficiency comparisons", "common",
     "'A is twice/thrice as efficient', or an efficiency ratio like 3 : 4 is given.",
     "Rate ratio first, then units: (k+1) workers' worth of rate = 1/T."),
 pat("A leaves or joins mid-work", "common",
     "Someone works a few days, then leaves; another (or the group) finishes.",
     "Work already done = t/T; apply the remaining fraction to the continuing workers."),
 pat("Alternate days", "common",
     "A and B work on alternate days (someone starts); find total time or work share.",
     "Progress per 2-day cycle; multiply cycles, then finish the tail with whoever's turn it is."),
 pat("Men–days–hours chain", "common",
     "Men, days, hours given in two scenarios (maybe efficiency too) — find the missing one.",
     "M₁D₁H₁E₁ = M₂D₂H₂E₂ for the same work; keep inverses in the numerator."),
 pat("Provisions / consumption", "common",
     "Garrison or hostel stock after reinforcements or early inspection.",
     "Stock in man-days: M × D. Subtract elapsed consumption, divide by new headcount."),
 pat("Wages distribution", "common",
     "Total wage for a joint job; find one worker's share.",
     "Share = rate × days worked, normalized. Equal days ⇒ rate ratio = wage ratio."),
]

solved = []
assert Fr(1, 12) + Fr(1, 24) == Fr(1, 8)
solved.append(Q("tw-s01", "A can finish a work in 12 days and B in 24 days. Working together, they will finish it in:",
  ["6 days", "7 days", "8 days", "9 days"], 2, 8,
  md(r"LCM method: work = 24 units; A does 2/day, B 1/day ⇒ 3/day ⇒ $24/3 = 8$ days."),
  "ab/(a+b) = 12×24/36 = 8 days.",
  "easy", "tw-basics", "combined work", 25))

assert Fr(1, 10) - Fr(1, 15) == Fr(1, 30)
solved.append(Q("tw-s02", "A pipe can fill a tank in 10 hours and another pipe can empty it in 15 hours. If both are opened, the tank will be filled in:",
  ["24 hours", "28 hours", "30 hours", "32 hours"], 2, 30,
  md(r"$\frac{1}{10} - \frac{1}{15} = \frac{3 - 2}{30} = \frac{1}{30}$ ⇒ **30 hours**."),
  "Fill-drain pair: ab/(b−a) = 150/5 = 30 h.",
  "easy", "tw-pipes", "fill and drain", 30))

assert Fr(1, 12) / 3 == Fr(1, 36)
solved.append(Q("tw-s03", "A is twice as efficient as B, and together they complete a work in 12 days. B alone can complete it in:",
  ["18 days", "24 days", "30 days", "36 days"], 3, 36,
  md(r"Rates: A $= 2k$, B $= k$ ⇒ $3k = \frac{1}{12}$ ⇒ $k = \frac{1}{36}$.",
     r"B alone takes $\frac{1}{k} = 36$ days (A takes 18)."),
  "(k+1)T = 3 × 12 = 36 days for B.",
  "medium", "tw-efficiency", "efficiency ratio", 35))

assert 15 * 20 == 300 and 300 / 25 == 12
solved.append(Q("tw-s04", "If 15 men can complete a work in 20 days, then 25 men will complete the same work in:",
  ["10 days", "12 days", "14 days", "15 days"], 1, 12,
  md(r"$15 \times 20 = 25 \times D$ ⇒ $D = 12$ days."),
  "Men × days constant: 300/25 = 12.",
  "easy", "tw-man-days", "men-days", 25))

assert Fr(1, 8) - Fr(1, 12) == Fr(1, 24)
solved.append(Q("tw-s05", "A can do a work in 12 days. With B's help the work is done in 8 days. If total wages are ₹1,200, B's share (both working the whole time) is:",
  ["₹300", "₹400", "₹450", "₹600"], 1, 400,
  md(r"B's rate $= \frac{1}{8} - \frac{1}{12} = \frac{1}{24}$.",
     r"$A : B = \frac{1}{12} : \frac{1}{24} = 2 : 1$ ⇒ B gets $1200 \times \frac{1}{3} = 400$, i.e. ₹400."),
  "Rate ratio 2 : 1 ⇒ B takes a third of the wages.",
  "medium", "tw-cases", "wages", 40))

# ------------------------------------------------------------------ practice
P = []

assert Fr(1, 10) + Fr(1, 20) == Fr(3, 20)
P.append(Q("tw-q01", "A completes a job in 10 days and B in 20 days. Working together, they complete it in:",
  ["$5\\frac{1}{3}$ days", "$6\\frac{2}{3}$ days", "7 days", "$7\\frac{1}{2}$ days"], 1, Fr(20, 3),
  md(r"$\frac{ab}{a+b} = \frac{10 \times 20}{30} = \frac{20}{3} = 6\frac{2}{3}$ days."),
  "LCM: 20 units, 3/day ⇒ 6⅔ days.",
  "easy", "tw-basics", "combined work", 25))

assert Fr(1, 6) + Fr(1, 12) + Fr(1, 18) == Fr(11, 36)
P.append(Q("tw-q02", "A, B and C can do a piece of work in 6, 12 and 18 days respectively. All three working together finish it in:",
  ["$2\\frac{6}{11}$ days", "$3\\frac{3}{11}$ days", "$4\\frac{1}{11}$ days", "$5\\frac{3}{11}$ days"], 1, Fr(36, 11),
  md(r"$\frac{1}{6} + \frac{1}{12} + \frac{1}{18} = \frac{6 + 3 + 2}{36} = \frac{11}{36}$ ⇒ $3\frac{3}{11}$ days."),
  "LCM 36: rates 6 + 3 + 2 = 11/day ⇒ 36/11 days.",
  "easy", "tw-basics", "combined work", 30))

assert Fr(1, 12) + Fr(1, 24) == Fr(1, 8)
P.append(Q("tw-q03", "Two pipes can fill a tank in 12 hours and 24 hours respectively. If both are opened together, the tank is filled in:",
  ["6 hours", "7 hours", "8 hours", "9 hours"], 2, 8,
  md(r"$\frac{12 \times 24}{12 + 24} = 8$ hours."),
  "ab/(a+b) = 288/36 = 8 h.",
  "easy", "tw-pipes", "two inlets", 25))

assert 12 * 15 == 180 and 180 / 20 == 9
P.append(Q("tw-q04", "12 men can complete a piece of work in 15 days. In how many days will 20 men complete the same work?",
  ["8 days", "9 days", "10 days", "12 days"], 1, 9,
  md(r"$12 \times 15 = 20 \times D$ ⇒ $D = 9$ days."),
  "180 man-days ÷ 20 men = 9 days.",
  "easy", "tw-man-days", "men-days", 25))

assert Fr(1, 12) / 4 == Fr(1, 48)
P.append(Q("tw-q05", "A is 3 times as efficient as B, and together they finish a work in 12 days. A alone will finish it in:",
  ["14 days", "16 days", "18 days", "20 days"], 1, 16,
  md(r"Rates $3k + k = 4k = \frac{1}{12}$ ⇒ $k = \frac{1}{48}$; A $= \frac{1}{3k} = 16$ days."),
  "(k+1)T/k = 4×12/3 = 16 days.",
  "easy", "tw-efficiency", "k-times worker", 30))

assert 20 * Fr(11, 15) == Fr(44, 3)
P.append(Q("tw-q06", "A can do a work in 15 days and B in 20 days. A works for 4 days and then leaves. B alone completes the remaining work in:",
  ["$12\\frac{1}{2}$ days", "$13\\frac{1}{3}$ days", "$14\\frac{2}{3}$ days", "$15\\frac{1}{2}$ days"], 2, Fr(44, 3),
  md(r"A did $\frac{4}{15}$; remaining $= \frac{11}{15}$.",
     r"B's time $= 20 \times \frac{11}{15} = 14\frac{2}{3}$ days."),
  "Remainder 11/15 at B's 1/20 per day ⇒ 44/3 days.",
  "medium", "tw-cases", "leaving mid-work", 40))

assert Fr(1, 8) + Fr(1, 12) - Fr(1, 6) == Fr(1, 24)
P.append(Q("tw-q07", "Two pipes fill a tank in 8 hours and 12 hours, while a third pipe empties the full tank in 6 hours. With all three open, the empty tank is filled in:",
  ["20 hours", "22 hours", "24 hours", "26 hours"], 2, 24,
  md(r"$\frac{1}{8} + \frac{1}{12} - \frac{1}{6} = \frac{3 + 2 - 4}{24} = \frac{1}{24}$ ⇒ 24 hours."),
  "Net rate = 1/24 ⇒ 24 h.",
  "medium", "tw-pipes", "fill-fill-drain", 35))

assert Fr(13, 48) / 2 == Fr(13, 96)
P.append(Q("tw-q08", "A and B together can do a work in 8 days, B and C in 12 days, and A and C in 16 days. All three together will complete it in:",
  ["$6\\frac{6}{13}$ days", "$7\\frac{5}{13}$ days", "$7\\frac{11}{13}$ days", "$8\\frac{4}{13}$ days"], 1, Fr(96, 13),
  md(r"$2(A+B+C) = \frac{1}{8} + \frac{1}{12} + \frac{1}{16} = \frac{13}{48}$ ⇒ rate $= \frac{13}{96}$.",
     r"Time $= \frac{96}{13} = 7\frac{5}{13}$ days."),
  "Pairwise rates add to 2× the trio rate ⇒ 96/13 days.",
  "medium", "tw-basics", "pairwise rates", 45))

assert Fr(1, 15) + Fr(1, 12) == Fr(3, 20)
P.append(Q("tw-q09", r"A can do $\frac{2}{5}$ of a work in 6 days and B can do $\frac{3}{4}$ of the same work in 9 days. Working together, they complete the work in:",
  ["$5\\frac{1}{3}$ days", "$6\\frac{2}{3}$ days", "$7\\frac{1}{3}$ days", "8 days"], 1, Fr(20, 3),
  md(r"A: full work in $\frac{6 \times 5}{2} = 15$ days; B: $\frac{9 \times 4}{3} = 12$ days.",
     r"Together: $\frac{1}{15} + \frac{1}{12} = \frac{3}{20}$ ⇒ $6\frac{2}{3}$ days."),
  "Scale each to full-work time first (15 and 12), then combine.",
  "medium", "tw-basics", "partial work scaling", 40))

assert 13500 - 1500 == 12000 and 12000 / 800 == 15
P.append(Q("tw-q10", "A garrison of 500 men has provisions for 27 days. After 3 days, 300 more men join. The provisions will now last for:",
  ["12 days", "15 days", "18 days", "20 days"], 1, 15,
  md(r"Stock left $= 500 \times (27 - 3) = 12000$ man-days.",
     r"$\frac{12000}{800} = 15$ days."),
  "24 days of stock spread over 800 men ⇒ 15 days.",
  "medium", "tw-man-days", "provisions", 40))

assert Fr(1, 12) / Fr(1, 18) == Fr(3, 2) and 840 * Fr(3, 5) == 504
P.append(Q("tw-q11", "A alone completes a work in 12 days and B alone in 18 days. They work together and receive ₹840 as total wages. A's share is:",
  ["₹420", "₹480", "₹504", "₹560"], 2, 504,
  md(r"$A : B = \frac{1}{12} : \frac{1}{18} = 3 : 2$ ⇒ $A = 840 \times \frac{3}{5} = 504$, i.e. ₹504."),
  "Equal days ⇒ wage ratio = rate ratio = 3 : 2.",
  "medium", "tw-cases", "wages", 35))

assert Fr(1, 6) + Fr(1, 12) == Fr(1, 4)
P.append(Q("tw-q12", "A can finish a work in 6 days and B in 12 days. They work on alternate days, A starting on the first day. The work is completed in:",
  ["7 days", "8 days", "9 days", "$8\\frac{1}{2}$ days"], 1, 8,
  md(r"Per 2 days: $\frac{1}{6} + \frac{1}{12} = \frac{1}{4}$ of the work.",
     r"4 cycles (8 days) complete exactly $4 \times \frac{1}{4} = 1$ ⇒ finished on day 8."),
  "Cycle rate 1/4 ⇒ exactly 4 cycles = 8 days.",
  "medium", "tw-cases", "alternate days", 40))

assert Fr(540, 81) == Fr(20, 3)
P.append(Q("tw-q13", "45 men would complete a piece of work in 16 days. They work for 4 days, after which 36 more men join them. The remaining work is now completed in:",
  ["$5\\frac{1}{3}$ days", "$6\\frac{2}{3}$ days", "$7\\frac{1}{3}$ days", "8 days"], 1, Fr(20, 3),
  md(r"Total work $= 720$ man-days; done in 4 days $= 180$.",
     r"Remaining $= 540$ with 81 men ⇒ $\frac{540}{81} = 6\frac{2}{3}$ days."),
  "540 man-days ÷ 81 men = 6⅔ days.",
  "hard", "tw-man-days", "reinforcement", 50))

assert Fr(5, 12) / Fr(5, 48) == 4
P.append(Q("tw-q14", "Pipes A and B can fill a tank in 12 hours and 16 hours respectively. Both are opened together for 4 hours; then a drain pipe C, which can empty the full tank in 24 hours, is also opened. The total time taken to fill the tank is:",
  ["7 hours", "$7\\frac{1}{2}$ hours", "8 hours", "9 hours"], 2, 8,
  md(r"In 4 h, A + B fill $\frac{7}{48} \times 4 = \frac{7}{12}$; remaining $= \frac{5}{12}$.",
     r"New net rate $= \frac{7}{48} - \frac{1}{24} = \frac{5}{48}$ ⇒ time $= \frac{5}{12} \times \frac{48}{5} = 4$ h.",
     "Total = 4 + 4 = **8 hours**."),
  "Stage 1 does 7/12; stage 2 rate 5/48 finishes the rest in exactly 4 h.",
  "hard", "tw-pipes", "staged pipes", 55))

assert Fr(1, 12) + Fr(1, 36) == Fr(1, 9)
P.append(Q("tw-q15", "A is 3 times as fast a worker as B and takes 24 days less than B for the same work. If they work together, the work is completed in:",
  ["8 days", "9 days", "10 days", "12 days"], 1, 9,
  md(r"Times: $x$ and $3x$ with $3x - x = 24$ ⇒ $x = 12$ (A = 12, B = 36).",
     r"Together: $\frac{1}{12} + \frac{1}{36} = \frac{4}{36} = \frac{1}{9}$ ⇒ 9 days."),
  "Difference of times = 2 units = 24 ⇒ A 12, B 36; ab/(a+b) = 9.",
  "hard", "tw-efficiency", "efficiency + days difference", 50))

topic = {
 "id": "time-work", "sectionId": "quant", "title": "Time & Work", "order": 10,
 "importance": "high", "avgQuestions": {"tier1": 1, "tier2": 2},
 "summary": "Rates, LCM units and the men-days chain solve nearly every question: combined work, efficiency ratios, pipes and cisterns, mid-work join/leave, alternate days, provisions and wages. One slot is near-guaranteed in Tier 1, with staged pipe problems and wage splits rising in Tier 2.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
