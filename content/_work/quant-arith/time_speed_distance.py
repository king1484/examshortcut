from _lib import *
from fractions import Fraction as Fr

# ------------------------------------------------------------------ checks
assert F(90 * 5, 18) == 25 and Fr(150, 25) == 6                          # S1
assert F(72 * 5, 18) == 20 and 20 * 10 == 200 and 20 * 30 == 600 and 600 - 200 == 400  # S2
assert Fr(16 + 12, 2) == 14 and Fr(16 - 12, 2) == 2                      # S3
assert Fr(2 * 30 * 60, 90) == 40                                         # S4
assert F(150 * 5, 18) == Fr(125, 3) and Fr(350 * 3, 125) == Fr(42, 5)    # S5 = 8.4 s
assert F(54 * 5, 18) == 15                                               # E1
assert Fr(240, 60) == 4                                                  # E2
assert Fr(120, 15) == 8                                                  # E3
assert Fr(20 + 12, 2) == 16 and Fr(20 - 12, 2) == 4                      # E4
assert Fr(2 * 40 * 60, 100) == 48                                        # E5
assert Fr(300, 15) == 20 and F(20 * 18, 5) == 72                         # M1
assert Fr(400, 25) == 16 and F(16 * 18, 5) == Fr(288, 5)                 # M2 = 57.6 km/h
assert F(72 * 5, 18) == 20 and F(54 * 5, 18) == 15                       # M3 parts
assert F(72 * 5, 18) - F(54 * 5, 18) == 5 and Fr(200 + 200, 5) == 80     # M3 = 80 s
assert Fr(30, 2) == 15 and Fr(30, 3) == 10 and Fr(15 + 10, 2) == Fr(25, 2) and Fr(15 - 10, 2) == Fr(5, 2)  # M4
assert Fr(1, 1) / 3 == Fr(1, 3) and 60 * 1 == 60                         # M5: late t/3 = 20 -> t = 60
assert F(45 * 5, 18) == Fr(25, 2) and F(5 * 5, 18) == Fr(25, 18)         # M6 parts
assert Fr(50 * 5, 18) == Fr(125, 9) and Fr(250 * 9, 125) == 18           # M6 = 18 s
assert Fr(20, 5) == 4 and Fr(180, 4) == 45                               # M7: B = 4 m/s, A's time 45 s
# H1: d/5 - d/6 = 1/5 h -> d = 6
assert Fr(1, 5) - Fr(1, 6) == Fr(1, 30) and Fr(1, 30) * 30 * 1 == Fr(6, 30) * 5 and 6 * Fr(1, 30) == Fr(1, 5)
# H2: meet in 100/(20+30) = 2 h -> bird 120 km
assert Fr(100, 50) == 2 and 60 * 2 == 120
# H3: 12/u + 18/v = 3; 24/u + 12/v = 4 -> u = 8, v = 12
assert Fr(12, 8) + Fr(18, 12) == 3 and Fr(24, 8) + Fr(12, 12) == 4
assert Fr(8 + 12, 2) == 10 and Fr(12 - 8, 2) == 2

subtopics = [
 sub("tsd-basics", "Speed, Distance, Time & Unit Conversion",
  md(r"The spine of the whole topic:",
     "",
     r"$$\text{Speed} = \frac{\text{Distance}}{\text{Time}}, \qquad D = S \times T$$",
     "",
     r"**Unit conversion:** $1\ \text{km/h} = \frac{5}{18}\ \text{m/s}$ and $1\ \text{m/s} = \frac{18}{5}\ \text{km/h}$. Memorise the friends: 36 km/h = 10 m/s, 54 = 15, 72 = 20, 90 = 25 m/s.",
     "",
     r"**Average speed** is total distance ÷ total time — never the average of speeds unless times are equal.",
     "",
     r"Equal distances at speeds a and b: $\text{avg} = \frac{2ab}{a+b}$ (harmonic mean, always below the arithmetic mean)."),
  [formula("Basic relation", r"S = \frac{D}{T}, \quad D = S \times T"),
   formula("km/h to m/s", r"\text{km/h} \times \frac{5}{18} = \text{m/s}"),
   formula("Equal-distance average", r"\bar{S} = \frac{2ab}{a + b}"),
   formula("General average speed", r"\bar{S} = \frac{D_1 + D_2}{T_1 + T_2}")],
  [trick("Convert first, always",
         "Train lengths are in metres, times in seconds — get to m/s before anything else.",
         "Convert 90 km/h into m/s and find the time a 150 m train takes to cross a pole.",
         r"$90 \times \frac{5}{18} = 25$ m/s ⇒ $150/25 = 6$ seconds."),
   trick("Harmonic mean for round trips",
         "Same distance out and back ⇒ 2ab/(a+b) in one line.",
         "A car goes to a town at 40 km/h and returns at 60 km/h. The average speed for the whole trip is:",
         r"$\frac{2 \times 40 \times 60}{100} = 48$ km/h."),
   trick("Early/late differences are time equations",
         "Both speeds cover the SAME distance; equate the expressions.",
         r"Walking at $\frac{3}{4}$ of his usual speed a man is 20 minutes late. His usual time is:",
         r"New time $= \frac{4}{3}t$ ⇒ late by $\frac{t}{3} = 20$ ⇒ $t = 60$ minutes.")],
  [r"Averaging two speeds arithmetically for equal DISTANCES (must use 2ab/(a+b)).",
   "Forgetting the 5/18 conversion and dividing metres by km/h.",
   r"In early/late problems, using $\frac{3}{4}t$ as the new time when it is $\frac{4}{3}t$.",
   "Mixing minutes and hours inside one equation."]),

 sub("tsd-relative", "Relative Speed",
  md(r"How fast one moving object closes the gap with another:",
     "",
     r"$$\text{opposite directions: } S_{\text{rel}} = S_1 + S_2 \qquad \text{same direction: } S_{\text{rel}} = S_1 - S_2$$",
     "",
     r"Use relative speed whenever the question is 'cross', 'overtake', 'meet' or 'catch up'. The distance to cover is the combined lengths (trains) or the initial gap (chases, meetings).",
     "",
     r"**Meeting point:** two objects start towards each other → meet time $= \frac{\text{gap}}{S_1 + S_2}$, regardless of individual lengths."),
  [formula("Relative speed", r"S_{\text{rel}} = S_1 \pm S_2"),
   formula("Meeting time", r"t = \frac{\text{initial gap}}{S_1 + S_2}"),
   formula("Overtake time", r"t = \frac{\text{gap or combined length}}{S_1 - S_2}"),
   formula("Time after meeting (opposite starts)", r"\frac{\text{speed of other}}{\text{own speed}} = \frac{\text{time to B from meet}}{\text{time to A from meet}}")],
  [trick("Subtract for the same direction",
         "Overtaking uses the difference; the length is both trains together.",
         "Two trains run in the same direction at 72 km/h and 54 km/h. The faster train, 200 m long, completely crosses the slower one in:",
         r"$S_{\text{rel}} = 20 - 15 = 5$ m/s ⇒ $t = \frac{200}{5} = 40$ s (treating the slower train as a point for the faster's length — add its length if given)."),
   trick("Add for opposite directions",
         "Closing speed is the sum even if one object is a walking man.",
         r"A 250 m train at 45 km/h crosses a man walking at 5 km/h in the opposite direction in:",
         r"$S_{\text{rel}} = 50$ km/h $= \frac{125}{9}$ m/s ⇒ $t = 250 \times \frac{9}{125} = 18$ s."),
   trick("Distance flown till meeting",
         "Find the meeting time first; any third object's distance = its speed × that time.",
         "Two trains 100 km apart approach each other at 20 km/h and 30 km/h. A bird flying at 60 km/h shuttles between them until they meet. The total distance the bird covers is:",
         r"Meet time $= \frac{100}{50} = 2$ h ⇒ bird covers $60 \times 2 = 120$ km (no need to sum the shuttles!).")],
  [r"Adding speeds when both move the same way (must subtract).",
   "Using only one train's length when two trains cross each other.",
   "Applying relative speed to a stationary pole (relative speed = train's own speed).",
   "Summing an infinite shuttle zigzag instead of multiplying speed by the meeting time."]),

 sub("tsd-trains", "Trains Crossing Poles, Platforms & Trains",
  md(r"A moving train must cover its OWN length to pass a point, and its length PLUS the obstacle's to pass anything long.",
     "",
     r"$$\text{cross pole/man: } t = \frac{L_{\text{train}}}{S} \qquad \text{cross platform/train: } t = \frac{L_1 + L_2}{S_{\text{rel}}}$$",
     "",
     r"Pole crossing gives the train's length directly: $L = S \times t$. Comparing pole time with platform time exposes the platform length.",
     "",
     "Convert the speed to m/s first, set up the length equation, solve. Two equations (pole + platform) solve for both length and speed."),
  [formula("Pole / man", r"L_{\text{train}} = S \times t"),
   formula("Platform / bridge", r"L_{\text{train}} + L_{\text{platform}} = S \times t"),
   formula("Train vs train", r"L_1 + L_2 = S_{\text{rel}} \times t"),
   formula("Two-equation extraction", r"\frac{t_{\text{platform}}}{t_{\text{pole}}} = \frac{L + P}{L}")],
  [trick("Pole first: it's the train's own length",
         "The pole crossing IS the definition of the train's length in motion.",
         "A 300 m long train crosses a pole in 15 seconds. Its speed in km/h is:",
         r"$S = \frac{300}{15} = 20$ m/s $= 20 \times \frac{18}{5} = 72$ km/h."),
   trick("Subtract the pole equation",
         "Platform time minus pole time covers exactly the platform.",
         "A train at 72 km/h crosses a pole in 10 seconds and a platform in 30 seconds. The platform's length is:",
         r"$L = 20 \times 10 = 200$ m; $L + P = 20 \times 30 = 600$ ⇒ $P = 400$ m."),
   trick("Man in the other train",
         "A man is a point — only the crossing train's length matters.",
         "A train 180 m long crosses a 220 m long platform in 25 seconds. Its speed is:",
         r"$S = \frac{180 + 220}{25} = 16$ m/s $= 57.6$ km/h.")],
  [r"Forgetting to include the train's own length when crossing a platform or another train.",
   "Adding the platform length when crossing a pole.",
   "Leaving the speed in km/h while lengths are in metres.",
   "Using the relative speed of a stationary object as the train's speed MINUS zero incorrectly in same-direction cases (it is simply the train's speed)."]),

 sub("tsd-boats", "Boats & Streams",
  md(r"Two speeds to track: downstream (with the current) and upstream (against it).",
     "",
     r"$$u = b + s \ (\text{downstream}), \qquad v = b - s \ (\text{upstream})$$",
     r"$$b = \frac{u + v}{2}, \qquad s = \frac{u - v}{2}$$",
     "",
     r"**Downstream/upstream time ratio for equal distances** $= v : u$ — the slower leg takes longer.",
     "",
     r"Rowing questions with two trips are solved with $t = \frac{d_1}{u} + \frac{d_2}{v}$; two such equations solve for b and s together."),
  [formula("Effective speeds", r"u = b + s, \quad v = b - s"),
   formula("Boat & stream from trips", r"b = \frac{u + v}{2}, \quad s = \frac{u - v}{2}"),
   formula("Time for two legs", r"t = \frac{d_1}{b + s} + \frac{d_2}{b - s}"),
   formula("Swimmer/boat carried by stream", r"\text{drift} = s \times \text{time}")],
  [trick("Halve the sum, halve the difference",
         "Down and up speeds give boat and stream in one line each.",
         "A boat's downstream speed is 16 km/h and upstream speed 12 km/h. Find the boat's speed in still water and the stream speed.",
         r"$b = \frac{16 + 12}{2} = 14$ km/h, $s = \frac{16 - 12}{2} = 2$ km/h."),
   trick("Extract u and v from trip times",
         "Each trip is one equation; the pair is linear in 1/u and 1/v.",
         "A boat covers 30 km downstream in 2 hours and returns in 3 hours. Find the speed of the stream.",
         r"$u = 15$, $v = 10$ ⇒ $s = \frac{5}{2} = 2.5$ km/h."),
   trick("Two double-trip equations",
         "Two journeys pin down both speeds exactly.",
         "A boat goes 12 km upstream and 18 km downstream in 3 hours, and 24 km upstream and 12 km downstream in 4 hours. Its speed in still water is:",
         r"Let $u, v$ be up/down speeds: $\frac{12}{u} + \frac{18}{v} = 3$ and $\frac{24}{u} + \frac{12}{v} = 4$; solving gives $u = 8$, $v = 12$ ⇒ $b = 10$ km/h, $s = 2$ km/h.")],
  [r"Swapping u and v ($b - s$ is upstream, the slower one).",
   r"Recovering b as $\frac{u - v}{2}$ instead of $\frac{u + v}{2}$.",
   "Adding the distances before dividing (legs have different effective speeds — never merge them).",
   "Ignoring the stream when the question asks for the boat's own speed."]),

 sub("tsd-races", "Races & Handicaps",
  md(r"In a race of L metres, 'A beats B by x metres' means when A finishes L, B has covered only L − x.",
     "",
     r"$$\frac{S_A}{S_B} = \frac{L}{L - x}$$",
     "",
     r"'A beats B by t seconds': A finishes t seconds earlier — B needs t more seconds for the remaining metres.",
     "",
     r"A **dead heat** means both finish together (no beating margin). Start handicaps ('A gives B a start of 20 m') simply shorten B's race to L − 20."),
  [formula("Beating margin in metres", r"\frac{S_A}{S_B} = \frac{L}{L - x}"),
   formula("Beating margin in time", r"\text{B's remaining time} = t \Rightarrow S_B = \frac{x}{t}"),
   formula("Speeds from 'by x m or t s'", r"S_B = \frac{x}{t}, \quad S_A = S_B \cdot \frac{L}{L - x}"),
   formula("Start handicap", r"\text{B runs } L - \text{start}")],
  [trick("Translate 'beats by x m' into a speed ratio",
         "Same finishing time ⇒ distances are in the speed ratio.",
         "In a 200 m race A beats B by 20 metres. The ratio of their speeds is:",
         r"$S_A : S_B = 200 : 180 = 10 : 9$."),
   trick("'By x metres or t seconds' reveals both speeds",
         "B's last x metres took t seconds — that's B's speed for free.",
         "In a 200 m race A beats B by 20 m or 5 seconds. B's speed is:",
         r"$S_B = \frac{20}{5} = 4$ m/s (and A's time $= \frac{180}{4} = 45$ s, so $S_A = \frac{200}{45}$ m/s)."),
   trick("Handle the handicap",
         "A start shortens one runner's distance; recompute the ratio.",
         "A gives B a start of 20 m in a 200 m race and they finish together. The ratio of their speeds is:",
         r"$S_A : S_B = 200 : 180 = 10 : 9$.")],
  [r"Reading 'beats by 20 m' as B running 20 m (B runs L − 20 when A runs L).",
   "Confusing a time margin with a distance margin.",
   "Applying the start on the wrong runner ('A gives B a start' ⇒ B begins ahead, running less).",
   "Dividing race length by the wrong runner's time when extracting speeds."]),
]

pyq = [
 pat("Train crossing a pole or a man", "very common",
     "Length of train given, time to pass a point asked (or vice versa).",
     r"$L = S \times t$ with S in m/s. Convert with 5/18 first."),
 pat("Train crossing a platform, bridge or another train", "very common",
     "Two lengths involved; time for the train to completely cross.",
     r"$t = \frac{L_1 + L_2}{S_{\text{rel}}}$. Pole + platform times together solve for both L and S."),
 pat("Boats & streams", "very common",
     "Downstream/upstream times, boat or stream speed asked; sometimes two double trips.",
     "u = b + s, v = b − s; invert the pair. Two trip equations are linear in 1/u and 1/v."),
 pat("Relative speed — meeting or overtaking", "common",
     "Two vehicles move towards or along each other; find meeting time or crossing time.",
     "Opposite: add; same direction: subtract. Distance = gap or sum of lengths."),
 pat("Average speed for legs of a journey", "common",
     "Out-and-back or multi-leg trips; the trap is averaging the speeds.",
     "Total distance ÷ total time; equal legs ⇒ 2ab/(a+b)."),
 pat("Speed change with early/late arrival", "common",
     "Walking slower/faster makes the person late/early by known minutes.",
     "Same distance both ways: set up the two time expressions; the difference is the delay."),
 pat("Races and starts", "common",
     "'A beats B by x m / t s', or start handicaps; find speeds or ratios.",
     "Distances covered in equal time are in the speed ratio; convert margins directly."),
 pat("Unit conversion embedded in other questions", "common",
     "Any train/m/s question quietly needs km/h ⇄ m/s.",
     "5/18 and 18/5 — know the 36/54/72/90 table by heart."),
]

solved = []
assert Fr(150, 25) == 6
solved.append(Q("tsd-s01", "A train 150 metres long is running at 90 km/h. The time it takes to cross a pole is:",
  ["5 seconds", "6 seconds", "7 seconds", "8 seconds"], 1, 6,
  md(r"$90$ km/h $= 25$ m/s ⇒ $t = \frac{150}{25} = 6$ seconds."),
  "90 → 25 m/s; 150/25 = 6 s.",
  "easy", "tsd-basics", "pole crossing", 25))

assert Fr(600 - 200, 1) == 400
solved.append(Q("tsd-s02", "A train running at 72 km/h crosses a pole in 10 seconds and a platform in 30 seconds. The length of the platform is:",
  ["300 m", "350 m", "400 m", "500 m"], 2, 400,
  md(r"$72$ km/h $= 20$ m/s. Train $= 20 \times 10 = 200$ m.",
     r"Train + platform $= 20 \times 30 = 600$ ⇒ platform $= 400$ m."),
  "Pole gives L = 200; platform adds 400 m.",
  "medium", "tsd-trains", "pole + platform", 40))

assert Fr(16 + 12, 2) == 14
solved.append(Q("tsd-s03", "The speed of a boat downstream is 16 km/h and upstream is 12 km/h. The speed of the stream is:",
  ["1 km/h", "1.5 km/h", "2 km/h", "2.5 km/h"], 2, 2,
  md(r"$s = \frac{u - v}{2} = \frac{16 - 12}{2} = 2$ km/h (boat in still water: 14 km/h)."),
  "Half the difference: (16 − 12)/2 = 2.",
  "easy", "tsd-boats", "stream speed", 25))

assert Fr(2 * 40 * 60, 100) == 48
solved.append(Q("tsd-s04", "A car covers a distance at 40 km/h and returns along the same route at 60 km/h. Its average speed for the whole journey is:",
  ["45 km/h", "48 km/h", "50 km/h", "52 km/h"], 1, 48,
  md(r"Equal distances: $\bar{S} = \frac{2 \times 40 \times 60}{40 + 60} = 48$ km/h."),
  "Harmonic mean 48, NOT the average 50.",
  "easy", "tsd-basics", "average speed", 30))

assert Fr(350 * 3, 125) == Fr(42, 5)
solved.append(Q("tsd-s05", "Two trains of lengths 150 m and 200 m run towards each other at 60 km/h and 90 km/h. The time they take to completely cross each other is:",
  ["8.4 seconds", "9 seconds", "10.2 seconds", "12 seconds"], 0, Fr(42, 5),
  md(r"$S_{\text{rel}} = 150$ km/h $= \frac{125}{3}$ m/s.",
     r"$t = \frac{350}{125/3} = \frac{1050}{125} = 8.4$ seconds."),
  "Opposite directions: speeds add; lengths add: 350/(125/3) = 8.4 s.",
  "medium", "tsd-relative", "opposite trains", 45))

# ------------------------------------------------------------------ practice
P = []

assert F(54 * 5, 18) == 15
P.append(Q("tsd-q01", "A speed of 54 km/h expressed in m/s is:",
  ["12 m/s", "15 m/s", "18 m/s", "20 m/s"], 1, 15,
  md(r"$54 \times \frac{5}{18} = 15$ m/s."),
  "54 → 15 is a table value.",
  "easy", "tsd-basics", "unit conversion", 20))

assert Fr(240, 60) == 4
P.append(Q("tsd-q02", "A bus travels 240 km at a uniform speed of 60 km/h. The journey takes:",
  ["3 hours", "3.5 hours", "4 hours", "4.5 hours"], 2, 4,
  md(r"$T = \frac{240}{60} = 4$ hours."),
  "240/60 = 4 h.",
  "easy", "tsd-basics", "basic DST", 20))

assert Fr(120, 15) == 8
P.append(Q("tsd-q03", "A train 120 m long is running at 54 km/h. The time it takes to pass a signal post is:",
  ["6 seconds", "8 seconds", "10 seconds", "12 seconds"], 1, 8,
  md(r"$54$ km/h $= 15$ m/s ⇒ $t = \frac{120}{15} = 8$ seconds."),
  "15 m/s; 120/15 = 8 s.",
  "easy", "tsd-trains", "pole crossing", 25))

assert Fr(20 - 12, 2) == 4
P.append(Q("tsd-q04", "A boat's downstream speed is 20 km/h and its upstream speed is 12 km/h. The speed of the boat in still water is:",
  ["14 km/h", "15 km/h", "16 km/h", "18 km/h"], 2, 16,
  md(r"$b = \frac{20 + 12}{2} = 16$ km/h (stream = 4 km/h)."),
  "Half the sum = 16.",
  "easy", "tsd-boats", "boat speed", 25))

assert Fr(2 * 40 * 60, 100) == 48
P.append(Q("tsd-q05", "A man rides to his office at 40 km/h and returns by the same route at 60 km/h. His average speed for the round trip is:",
  ["46 km/h", "48 km/h", "50 km/h", "52 km/h"], 1, 48,
  md(r"$\bar{S} = \frac{2 \times 40 \times 60}{100} = 48$ km/h."),
  "2ab/(a+b) = 48; 50 is the trap.",
  "easy", "tsd-basics", "average speed", 25))

assert F(20 * 18, 5) == 72
P.append(Q("tsd-q06", "A 300 m long train crosses a pole in 15 seconds. The speed of the train is:",
  ["64 km/h", "68 km/h", "70 km/h", "72 km/h"], 3, 72,
  md(r"$S = \frac{300}{15} = 20$ m/s $= 72$ km/h."),
  "20 m/s → ×18/5 = 72 km/h.",
  "medium", "tsd-trains", "pole crossing", 30))

assert Fr(400, 25) == 16
P.append(Q("tsd-q07", "A train 180 m long crosses a 220 m long platform in 25 seconds. The speed of the train is:",
  ["54 km/h", "56 km/h", "57.6 km/h", "60 km/h"], 2, Fr(288, 5),
  md(r"$S = \frac{180 + 220}{25} = 16$ m/s $= 57.6$ km/h."),
  "400 m in 25 s = 16 m/s = 57.6 km/h.",
  "medium", "tsd-trains", "platform crossing", 35))

assert Fr(200, 5) == 40
P.append(Q("tsd-q08", "Two trains, each 200 m long, run in the same direction at 72 km/h and 54 km/h. The time the faster train takes to completely cross the slower one is:",
  ["60 seconds", "70 seconds", "80 seconds", "90 seconds"], 2, 80,
  md(r"$S_{\text{rel}} = 72 - 54 = 18$ km/h $= 5$ m/s (same direction ⇒ subtract).",
     r"Combined length $= 400$ m ⇒ $t = \frac{400}{5} = 80$ seconds."),
  "Same direction ⇒ subtract: 5 m/s; both lengths: 400/5 = 80 s.",
  "medium", "tsd-relative", "overtake man", 40))

assert Fr(30, 2) == 15 and Fr(30, 3) == 10
P.append(Q("tsd-q09", "A boat covers 30 km downstream in 2 hours and returns upstream in 3 hours. The speed of the stream is:",
  ["2 km/h", "2.5 km/h", "3 km/h", "3.5 km/h"], 1, Fr(5, 2),
  md(r"$u = 15$, $v = 10$ ⇒ $s = \frac{15 - 10}{2} = 2.5$ km/h."),
  "Down 15, up 10 ⇒ stream 2.5.",
  "medium", "tsd-boats", "trip times", 30))

assert Fr(1, 1) / 3 == Fr(1, 3)
P.append(Q("tsd-q10", r"Walking at $\frac{3}{4}$ of his usual speed, a man reaches his office 20 minutes late. His usual time for the journey is:",
  ["40 minutes", "50 minutes", "60 minutes", "80 minutes"], 2, 60,
  md(r"New time $= \frac{4}{3}t$ ⇒ delay $= \frac{t}{3} = 20$ ⇒ $t = 60$ minutes."),
  "Delay = t/3 = 20 ⇒ usual time 1 hour.",
  "medium", "tsd-basics", "early/late", 30))

assert F(45 * 5, 18) == Fr(25, 2) and F(5 * 5, 18) == Fr(25, 18)
P.append(Q("tsd-q11", "A train 250 m long, running at 45 km/h, crosses a man walking at 5 km/h in the opposite direction in:",
  ["15 seconds", "16 seconds", "18 seconds", "20 seconds"], 2, 18,
  md(r"$S_{\text{rel}} = 50$ km/h $= \frac{125}{9}$ m/s.",
     r"$t = 250 \times \frac{9}{125} = 18$ seconds."),
  "Opposite directions add: 50 km/h; 250 ÷ (125/9) = 18 s.",
  "medium", "tsd-relative", "train vs man", 35))

assert Fr(20, 5) == 4
P.append(Q("tsd-q12", "In a 200 m race A beats B by 20 metres or 5 seconds. The speed of B is:",
  ["3.5 m/s", "4 m/s", "4.5 m/s", "5 m/s"], 1, 4,
  md(r"B covers his last 20 m in 5 s ⇒ $S_B = \frac{20}{5} = 4$ m/s."),
  "Margin-in-time ÷ margin-in-distance = 4 m/s.",
  "medium", "tsd-races", "beats by time", 30))

assert 6 * Fr(1, 30) == Fr(1, 5)
P.append(Q("tsd-q13", "Walking at 5 km/h a student misses a bus by 7 minutes, while walking at 6 km/h he reaches the stop 5 minutes early. The distance to the bus stop is:",
  ["5 km", "5.5 km", "6 km", "7 km"], 2, 6,
  md(r"Time gap between the two speeds $= 7 + 5 = 12$ min $= \frac{1}{5}$ h.",
     r"$\frac{d}{5} - \frac{d}{6} = \frac{d}{30} = \frac{1}{5}$ ⇒ $d = 6$ km."),
  "12-minute spread over speeds 5 and 6 ⇒ d/30 = 1/5 ⇒ 6 km.",
  "hard", "tsd-basics", "early-late distance", 50))

assert 60 * 2 == 120
P.append(Q("tsd-q14", "Two trains 100 km apart start moving towards each other at 20 km/h and 30 km/h. A bird flies at 60 km/h, shuttling back and forth between the trains until they meet. The total distance the bird covers is:",
  ["100 km", "110 km", "120 km", "150 km"], 2, 120,
  md(r"Meet time $= \frac{100}{20 + 30} = 2$ hours.",
     r"Bird flies $60 \times 2 = 120$ km — no summation of zigzags needed."),
  "Speed × meeting time = 60 × 2 = 120 km.",
  "hard", "tsd-relative", "shuttle till meeting", 45))

assert Fr(12, 8) + Fr(18, 12) == 3
P.append(Q("tsd-q15", "A boat goes 12 km upstream and 18 km downstream in 3 hours; it goes 24 km upstream and 12 km downstream in 4 hours. The speed of the boat in still water is:",
  ["8 km/h", "9 km/h", "10 km/h", "12 km/h"], 2, 10,
  md(r"Let the upstream and downstream speeds be $u$ and $v$: $\frac{12}{u} + \frac{18}{v} = 3$ and $\frac{24}{u} + \frac{12}{v} = 4$.",
     r"Solving: $u = 8$, $v = 12$ ⇒ $b = \frac{8 + 12}{2} = 10$ km/h (stream 2 km/h)."),
  "Two trip equations → u = 8, v = 12 → boat 10 km/h.",
  "hard", "tsd-boats", "double trip equations", 60))

topic = {
 "id": "time-speed-distance", "sectionId": "quant", "title": "Time, Speed & Distance", "order": 11,
 "importance": "high", "avgQuestions": {"tier1": 2, "tier2": 2},
 "summary": "Trains, relative speed, boats & streams, average-speed traps and races — two dependable slots per Tier 1 shift and more in Tier 2. Everything hangs on D = S×T, the 5/18 conversion, and the add/subtract rule for relative speed.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
