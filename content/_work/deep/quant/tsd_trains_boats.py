"""Phase-2 deep content for quant/time-speed-distance — trains + boats modules."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F

from _lib import Sub


def build_trains():
    S = Sub("tsd-trains")

    S.notes = r"""### What "crossing" means
A train "crosses" an object when its **front end reaches** the object and its **back end leaves it**. So the distance travelled during a crossing is always measured from the train's own front to its own back over the object:

- pole, man, signal post, tree — a point object → distance = **train's own length** $L$;
- platform, bridge, tunnel — distance = $L + \text{platform length}$;
- another train — distance = $L_1 + L_2$.

Then simply $t = \dfrac{\text{distance}}{\text{speed}}$ (or the relative speed, if both move).

### Pole / man / signal: the train's own length
$$t = \frac{L}{S} \qquad \text{or} \qquad L = S \times t$$
A 180 m train crossing a pole in 9 s runs at $\frac{180}{9} = 20$ m/s $= 72$ km/h. Every train question that gives a pole crossing is handing you the train's length-speed pair for free.

### Platform / bridge: add the platform
$$t = \frac{L + P}{S}$$
Two-step strategy: get $S$ (or $L$) from the pole crossing first, then use the platform crossing for the remaining unknown. A train crosses a pole in 12 s and a 270 m platform in 30 s: in the extra $30 - 12 = 18$ s it covers exactly the extra 270 m → $S = 15$ m/s $= 54$ km/h, and $L = 15 \times 12 = 180$ m. This "subtract the times, the difference is the platform" trick avoids writing two equations.

### Train vs train
- **Opposite directions**: $t = \dfrac{L_1 + L_2}{S_1 + S_2}$ — the gap closes fast.
- **Same direction**: $t = \dfrac{L_1 + L_2}{|S_1 - S_2|}$ — slow, uses the difference.
- Crossing a **point** on the other train (or a man on it): only the crossing train's own length is used, at the relative speed.

### Two crossings → solve two unknowns
When neither $L$ nor $S$ is given directly, two crossings give two equations. Bridges of 200 m and 400 m crossed in 20 s and 30 s:
$$\frac{L + 200}{S} = 20, \qquad \frac{L + 400}{S} = 30$$
Subtract: $\frac{200}{S} = 10$ → $S = 20$ m/s, $L = 20 \times 20 - 200 = 200$ m. Any two fixed structures work the same way — subtract first, the train length drops out.

### Common traps
- Using only the train's length when a platform is mentioned (or only the platform — both are wrong).
- Forgetting the other train's length when two trains cross each other.
- Dividing metres by a km/h speed — convert with $\frac{5}{18}$ first.
- In same-direction crossings, adding the speeds instead of subtracting.

### Quick revision
- Point object: $t = L/S$. Platform: $t = (L+P)/S$. Two trains: $t = (L_1+L_2)/(S_1 \pm S_2)$.
- Pole in $t_p$ s and platform $P$ in $t$ s → $S = \frac{P}{t - t_p}$, $L = S\, t_p$.
- Two bridges: subtract the two equations — $\Delta L / \Delta t = S$.
- km/h → m/s × 5/18 before dividing lengths.
"""

    S.pattern("tsd-p9", "Train crossing a pole / man / signal", "very common",
        "A single train crosses a pole, a man standing, or a signal post; length, speed or time is asked.",
        r"L = S \times t",
        r"""1. A pole is a point: the train covers only its own length.
2. Any two of $L$, $S$, $t$ determine the third: $L = St$, $S = L/t$, $t = L/S$.
3. Convert with $\frac{5}{18}$ if the units disagree.

Why: crossing a point object begins when the engine reaches it and ends when the guard's van leaves it — exactly one train-length of travel.""",
        "A 210 m long train crosses a pole in 12 seconds. The length of a platform it crosses in 30 seconds at the same speed is:",
        r"$S = \frac{210}{12} = 17.5$ m/s. Platform: $17.5 \times 30 = 525$ m total → platform $= 525 - 210 = 315$ m.")
    S.pattern("tsd-p10", "Train crossing a platform / bridge / tunnel", "very common",
        "A train crosses a structure of given length; time, speed or the structure's length is asked (often paired with a pole crossing).",
        r"t = \frac{L + P}{S}, \qquad S = \frac{P}{t_{\text{plat}} - t_{\text{pole}}}",
        r"""1. Write the distance as $L + P$ — the train must travel its own length plus the platform.
2. If a pole crossing is also given, subtract the two times: the extra time covers exactly the platform length → $S = \frac{P}{\Delta t}$.
3. Then $L = S \times t_{\text{pole}}$ if needed.

Why: during the extra time between the two crossings, the engine end travels exactly one platform-length more.""",
        "A train crosses a platform of length 180 m in 20 seconds and a pole in 8 seconds. The length of the train is:",
        r"$\frac{L + 180}{L/8} = 20$ → $8L + 1440 = 20L$ → $L = 120$ m. (Speed $= 15$ m/s.)")
    S.pattern("tsd-p11", "Two trains crossing each other", "very common",
        "Two trains cross each other — opposite or same direction; the crossing time or a length/speed ratio is asked.",
        r"t = \frac{L_1 + L_2}{S_1 + S_2}\ (\text{opp}), \qquad t = \frac{L_1 + L_2}{|S_1 - S_2|}\ (\text{same})",
        r"""1. Distance is always the SUM of both lengths.
2. Opposite directions → add the speeds; same direction → subtract.
3. If equal lengths cross in $t_o$ s opposite and $t_s$ s in the same direction, the speed ratio is $\frac{t_s + t_o}{t_s - t_o}$.

Why: the last point follows from $x+y = v_o t_o$ and $x+y = v_s t_s$, so $v_o/v_s = t_s/t_o$, and $\frac{v_o - v_s}{v_o + v_s} = \frac{t_s - t_o}{t_s + t_o}$.""",
        "Two trains of equal length cross each other completely in 12 seconds when moving in opposite directions and in 36 seconds when moving in the same direction. The ratio of their speeds is:",
        r"$\frac{v_{\text{fast}}}{v_{\text{slow}}} = \frac{36 + 12}{36 - 12} = \frac{48}{24} = 2:1$.")
    S.pattern("tsd-p12", "Two crossings → two unknowns", "common",
        "Neither the train's length nor its speed is given directly; two different crossings (two bridges, or a man and a platform) provide two equations.",
        r"\frac{L + A}{S} = t_1, \qquad \frac{L + B}{S} = t_2",
        r"""1. Set up one equation per crossing.
2. Subtract them — the unknown length $L$ cancels or drops to $\Delta L = S\,\Delta t$.
3. Back-substitute to get $L$.

Why: subtracting eliminates one unknown immediately; the structures' length difference is covered in the time difference.""",
        "A train crosses two bridges of lengths 200 m and 400 m in 20 seconds and 30 seconds respectively. The length of the train is:",
        r"Subtract: $\frac{400 - 200}{30 - 20} = 20$ m/s. Then $L = 20 \times 20 - 200 = 200$ m.")

    # ---- practice (tsd-trains) ----
    assert F(180, 9) * F(18, 5) == 72
    S.q("tsd-p9", "easy",
        "A 180 m long train crosses a signal post in 9 seconds. Its speed is:",
        ["72 km/h", "64 km/h", "80 km/h", "76 km/h"], "72 km/h",
        r"$S = \frac{180}{9} = 20$ m/s $= 20 \times \frac{18}{5} = 72$ km/h.",
        "20 m/s is a table value: 72 km/h.", 25)
    assert F(300, 20) * F(18, 5) == 54
    S.q("tsd-p10", "easy",
        "A 120 m long train crosses a 180 m long platform in 20 seconds. The speed of the train is:",
        ["54 km/h", "50 km/h", "58 km/h", "60 km/h"], "54 km/h",
        r"$S = \frac{120 + 180}{20} = 15$ m/s $= 54$ km/h.",
        None, 30)
    assert F(300, 25) == 12
    S.q("tsd-p11", "easy",
        "Two trains of lengths 120 m and 180 m run towards each other on parallel tracks at 36 km/h and 54 km/h. They cross each other completely in:",
        ["12 seconds", "10 seconds", "14 seconds", "15 seconds"], "12 seconds",
        r"$S_{\text{rel}} = 36 + 54 = 90$ km/h $= 25$ m/s. $\frac{120 + 180}{25} = 12$ seconds.",
        None, 30)
    s = F(270, 18)
    assert s * F(12) == 180
    S.q("tsd-p10", "medium",
        "A train running at 54 km/h crosses a pole in 12 seconds and a platform in 30 seconds. The length of the platform is:",
        ["270 m", "240 m", "300 m", "250 m"], "270 m",
        r"$S = 54 \times \frac{5}{18} = 15$ m/s. Train length $= 15 \times 12 = 180$ m. Platform $= 15 \times 30 - 180 = 270$ m.",
        None, 40)
    assert F(63 * 5, 18) * 12 == 210
    S.q("tsd-p9", "medium",
        "A train running at 63 km/h crosses a pole in 12 seconds. The length of the train is:",
        ["210 m", "200 m", "220 m", "225 m"], "210 m",
        r"$S = 63 \times \frac{5}{18} = 17.5$ m/s. $L = 17.5 \times 12 = 210$ m.",
        None, 30)
    assert F(300, 5) == 60
    S.q("tsd-p11", "medium",
        "Two trains of lengths 180 m and 120 m run in the same direction on parallel tracks at 72 km/h and 54 km/h. The faster train crosses the slower one completely in:",
        ["60 seconds", "50 seconds", "70 seconds", "55 seconds"], "60 seconds",
        r"$S_{\text{rel}} = 72 - 54 = 18$ km/h $= 5$ m/s. $\frac{180 + 120}{5} = 60$ seconds.",
        None, 40)
    S_q = F(400 - 200, 30 - 20)
    assert S_q == 20 and S_q * 20 - 200 == 200
    S.q("tsd-p12", "medium",
        "A train crosses two bridges of lengths 200 m and 400 m in 20 seconds and 30 seconds respectively. The length of the train is:",
        ["200 m", "150 m", "250 m", "300 m"], "200 m",
        r"Subtracting the two crossings: $\frac{400 - 200}{30 - 20} = 20$ m/s. Then $L = 20 \times 20 - 200 = 200$ m.",
        None, 45)
    Lm = F(10 * 300, 25 - 10)
    assert Lm == 200
    S.q("tsd-p12", "medium",
        "A train crosses a man standing on a platform in 10 seconds and crosses the 300 m long platform completely in 25 seconds. The length of the train is:",
        ["200 m", "150 m", "250 m", "180 m"], "200 m",
        r"$\frac{L}{10} = \frac{L + 300}{25}$ → $25L = 10L + 3000$ → $L = 200$ m (speed 20 m/s).",
        None, 45)
    assert F(36 + 12, 36 - 12) == 2
    S.q("tsd-p11", "hard",
        "Two trains of equal length take 12 seconds to cross each other completely when moving in opposite directions, and 36 seconds when moving in the same direction. The ratio of the speeds of the two trains is:",
        ["2 : 1", "3 : 1", "3 : 2", "4 : 3"], "2 : 1",
        r"$\frac{v_{\text{fast}}}{v_{\text{slow}}} = \frac{t_s + t_o}{t_s - t_o} = \frac{36 + 12}{36 - 12} = \frac{48}{24} = \frac21$.",
        None, 55)
    tot = F(54 + 72) * F(5, 18) * 12
    assert tot == 420 and tot - 150 == 270
    S.q("tsd-p11", "hard",
        "Train A of length 150 m running at 54 km/h crosses train B moving in the opposite direction at 72 km/h in 12 seconds. The length of train B is:",
        ["270 m", "250 m", "300 m", "280 m"], "270 m",
        r"""$S_{\text{rel}} = 54 + 72 = 126$ km/h $= 35$ m/s.
Total $= 35 \times 12 = 420$ m → $L_B = 420 - 150 = 270$ m.""",
        None, 55)
    return S


def build_boats():
    S = Sub("tsd-boats")

    S.notes = r"""### Downstream and upstream
A current of speed $s$ pushes a boat whose own speed in still water is $b$:
$$u = b + s \ \text{(downstream)}, \qquad v = b - s \ \text{(upstream)}$$
Memorise the recovery formulas — almost every answer routes through them:
$$b = \frac{u + v}{2}, \qquad s = \frac{u - v}{2}$$
Downstream 15 and upstream 10 → boat 12.5 km/h, stream 2.5 km/h. Since $b > s$ for forward progress, $u > v$ always: the bigger of the two given speeds is downstream.

### Trip questions
Each leg is plain $D = S \times T$ with the leg's effective speed. 42 km upstream in a boat with $b = 18$, $s = 6$: time $= \frac{42}{12} = 3.5$ h. Name the two leg speeds first, then divide — that is the whole method.

### Round trips
A trip down and back the same distance takes longer than the same distance in still water, because the stream steals more time going up than it gives going down. Two shapes appear:
1. **Both times given, equal distances**: $\frac{d}{u} + \frac{d}{v} = T_{\text{total}}$, or if the times differ, $d = u\,t_1 = v\,t_2$. Downstream 4 h and upstream 6 h for the same distance with downstream speed 6 km/h → $d = 24$ km, $v = 4$, $s = 1$.
2. **Stream given, one time known**: work the missing leg speed out of $b \pm s$.

Also worth knowing: for equal distance both ways, the average speed is $\frac{2uv}{u+v}$ — the harmonic mean again, always less than $b$.

### Two double trips → two linear equations
The hardest common shape: two journeys with different mixes of up- and downstream distances and their total times. With $a = \frac1v$ and $c = \frac1u$ as unknowns, each trip gives one linear equation — e.g. 8 km up and 16 km down in 4 h, 3 km up and 8 km down in 1¾ h:
$$\frac{8}{v} + \frac{16}{u} = 4, \qquad \frac{3}{v} + \frac{8}{u} = \frac74$$
Doubling the second and subtracting gives $\frac{2}{v} = \frac12$ → $v = 4$, then $u = 8$ → $b = 6$, $s = 2$. Substituting reciprocals turns a messy pair into a clean one.

### Still-water and drifting objects
A floating log, a cork or a swimmer who stops rowing moves at exactly the stream's speed. Two consequences:
- time to drift distance $d$ = $\frac{d}{s}$ (1 km wide river crossed straight with $b = 4$, $s = 3$ takes 15 min, drifting 0.75 km);
- **downstream time = still-water time + drift time** for the same stretch: $t_d = \frac{d}{b} + \frac{d}{s}$, and $t_u = \frac{d}{b} - \frac{d}{s}$.

### Common traps
- Swapping $u$ and $v$ (downstream is always the FASTER leg).
- Reporting $b$ when the stream was asked, or vice versa — check the question.
- Adding speeds on the return leg.
- Missing that a floating object's speed is $s$, not zero.

### Quick revision
- $u = b + s$, $v = b - s$; $b = \frac{u+v}{2}$, $s = \frac{u-v}{2}$.
- Leg time = leg distance ÷ leg speed; label each leg fast/slow first.
- Equal-distance round trip: $\bar S = \frac{2uv}{u+v}$; $t_u > t_d$ always.
- Two trips → equations in $\frac1u, \frac1v$.
- Log/cork speed = $s$; upstream and downstream times differ by $t_u - t_d = \frac{2ds}{b^2 - s^2}$.
"""

    S.pattern("tsd-p13", "Boat and stream from u and v", "very common",
        "Downstream and upstream speeds are given; the boat's still-water speed or the stream's speed is asked.",
        r"b = \frac{u + v}{2}, \qquad s = \frac{u - v}{2}",
        r"""1. Identify which speed is downstream (the larger one).
2. Average the two for the boat; take the half-difference for the stream.
3. Sanity check: $b$ must exceed $s$.

Why: $u = b + s$ and $v = b - s$ add and subtract to isolate $b$ and $s$.""",
        "A boat goes downstream at 15 km/h and upstream at 10 km/h. The speed of the stream is:",
        r"$s = \frac{15 - 10}{2} = 2.5$ km/h (boat: $\frac{25}{2} = 12.5$ km/h).")
    S.pattern("tsd-p14", "Single leg — time or distance", "very common",
        "Boat speed and stream speed (or both leg speeds) are known; the time for one downstream/upstream leg, or the distance covered in a given time, is asked.",
        r"t = \frac{D}{b \pm s}",
        r"""1. Decide the direction: downstream uses $b + s$, upstream uses $b - s$.
2. Time = leg distance ÷ leg speed (or distance = speed × time).
3. Keep units consistent before dividing.

Why: each leg is just straight $D = S \times T$ with the current added or removed.""",
        "A boat's speed in still water is 18 km/h and the stream runs at 6 km/h. The time it takes to go 42 km upstream is:",
        r"$v = 18 - 6 = 12$ km/h → $t = \frac{42}{12} = 3.5$ hours.")
    S.pattern("tsd-p15", "Round trip / equal-distance legs", "common",
        "The same distance is covered both ways; total time, the stream speed, or the distance is asked from partial information.",
        r"\frac{d}{u} + \frac{d}{v} = T, \qquad d = u\,t_1 = v\,t_2",
        r"""1. Equal distance on both legs: equate the two expressions for $d$ ($u t_1 = v t_2$) when the times differ.
2. Otherwise use the total-time equation $\frac{d}{u} + \frac{d}{v} = T$.
3. Finish with $b = \frac{u+v}{2}$, $s = \frac{u-v}{2}$.

Why: the same $d$ anchors both legs, giving one equation per unknown.""",
        "A boat covers a certain distance downstream in 4 hours and returns upstream in 6 hours. If its downstream speed is 6 km/h, the speed of the stream is:",
        r"$d = 6 \times 4 = 24$ km; $v = \frac{24}{6} = 4$ km/h; $s = \frac{6 - 4}{2} = 1$ km/h.")
    S.pattern("tsd-p16", "Drifting objects / two double trips", "common",
        "A log/cork drifts with the stream, or two journeys with different up/down mixes and total times are given; the boat speed (or stream speed) is asked.",
        r"\text{drift time} = \frac{d}{s}; \qquad \frac{A}{v} + \frac{B}{u} = T_1, \ \frac{C}{v} + \frac{D}{u} = T_2",
        r"""1. Drift: a floating object moves at the stream's speed; time = distance ÷ s. A rower crossing straight takes $t = \frac{\text{width}}{b}$ and drifts $s \times t$.
2. Two double trips: substitute $a = \frac1v$, $c = \frac1u$ to get two linear equations; solve for $u, v$, then $b, s$.
3. Scale one equation to match a coefficient, then subtract.

Why: reciprocals linearise the equations, and the drift is independent of the rowing.""",
        "A man can row 8 km upstream and 16 km downstream in 4 hours; he can also row 3 km upstream and 8 km downstream in 1 hour 45 minutes. His speed in still water is:",
        r"""In $\frac1u, \frac1v$: $8\cdot\frac1v + 16\cdot\frac1u = 4$ and $3\cdot\frac1v + 8\cdot\frac1u = \frac74$.
Twice the second minus the first gives $\frac1v = \frac14$ → $v = 4$; then $\frac1u = \frac18$ → $u = 8$.
So $b = \frac{4+8}{2} = 6$ km/h.""")

    # ---- practice (tsd-boats) ----
    assert F(18 - 12, 2) == 3
    S.q("tsd-p13", "easy",
        "A boat's downstream speed is 18 km/h and its upstream speed is 12 km/h. The speed of the stream is:",
        ["3 km/h", "2.5 km/h", "3.5 km/h", "4 km/h"], "3 km/h",
        r"$s = \frac{18 - 12}{2} = 3$ km/h (boat: 15 km/h).",
        None, 25)
    assert F(24, 12) == 2
    S.q("tsd-p14", "easy",
        "A boat's speed in still water is 10 km/h and the stream flows at 2 km/h. The time taken to travel 24 km downstream is:",
        ["2 hours", "2.4 hours", "3 hours", "1.5 hours"], "2 hours",
        r"$u = 10 + 2 = 12$ km/h → $t = \frac{24}{12} = 2$ hours.",
        None, 25)
    assert F(30, 15) == 2
    S.q("tsd-p14", "easy",
        "A swimmer swims at 12 km/h in still water and the current runs at 3 km/h. The time she takes to swim 30 km downstream is:",
        ["2 hours", "2.5 hours", "3 hours", "1.75 hours"], "2 hours",
        r"$u = 12 + 3 = 15$ km/h → $t = \frac{30}{15} = 2$ hours.",
        None, 25)
    u = F(6)
    d = u * 4
    v = d / 6
    s = (u - v) / 2
    assert d == 24 and v == 4 and s == 1
    S.q("tsd-p15", "medium",
        "A boat covers a certain distance downstream in 4 hours and returns the same distance upstream in 6 hours. If the downstream speed is 6 km/h, the speed of the stream is:",
        ["1 km/h", "1.5 km/h", "0.5 km/h", "2 km/h"], "1 km/h",
        r"$d = 6 \times 4 = 24$ km → $v = \frac{24}{6} = 4$ km/h → $s = \frac{6 - 4}{2} = 1$ km/h.",
        None, 40)
    assert F(42, 12) * 2 == 7
    S.q("tsd-p14", "medium",
        "A boat's speed in still water is 18 km/h and the stream flows at 6 km/h. The time taken to travel 42 km upstream is:",
        ["3.5 hours", "3 hours", "4 hours", "4.5 hours"], "3.5 hours",
        r"$v = 18 - 6 = 12$ km/h → $t = \frac{42}{12} = 3.5$ hours.",
        None, 30)
    assert F(15, 60) * 3 == F(3, 4)
    S.q("tsd-p16", "medium",
        "A river 1 km wide flows at 3 km/h. A rower who can row at 4 km/h in still water crosses straight to the opposite bank. How far does he drift with the current while crossing?",
        ["0.75 km", "1 km", "0.5 km", "1.25 km"], "0.75 km",
        r"Crossing time $= \frac{1}{4}$ h $= 15$ min. Drift $= 3 \times \frac{1}{4} = 0.75$ km.",
        None, 45)
    sv = F(12, 6)
    assert sv == 2 and 5 * sv == 10
    S.q("tsd-p13", "medium",
        "A boat's downstream speed is 12 km/h, and the boat's speed in still water is 5 times the speed of the stream. The boat's speed in still water is:",
        ["10 km/h", "12 km/h", "8 km/h", "9 km/h"], "10 km/h",
        r"$b + s = 12$ with $b = 5s$ → $6s = 12$ → $s = 2$, $b = 10$ km/h.",
        None, 40)
    assert 5 + 3 == 8
    S.q("tsd-p14", "medium",
        "The stream flows at 3 km/h. A boat takes 4 hours to row 20 km upstream. The boat's speed in still water is:",
        ["8 km/h", "7 km/h", "9 km/h", "10 km/h"], "8 km/h",
        r"$v = \frac{20}{4} = 5$ km/h → $b = v + s = 5 + 3 = 8$ km/h.",
        None, 30)
    dr = F(7 * 48, 14)
    assert dr == 24
    S.q("tsd-p15", "medium",
        "A boat's downstream speed is 8 km/h and its upstream speed is 6 km/h. It rows a certain distance and returns to the start, taking 7 hours in all. The one-way distance is:",
        ["24 km", "21 km", "28 km", "20 km"], "24 km",
        r"$\frac{d}{8} + \frac{d}{6} = 7$ → $\frac{14d}{48} = 7$ → $d = 24$ km (3 h down + 4 h up).",
        None, 45)
    u = F(8)
    v = F(4)
    assert (v + u) / 2 == 6
    S.q("tsd-p16", "hard",
        "A man can row 8 km upstream and 16 km downstream in 4 hours, and he can row 3 km upstream and 8 km downstream in 1 hour 45 minutes. His speed in still water is:",
        ["6 km/h", "7 km/h", "5 km/h", "8 km/h"], "6 km/h",
        r"""Let $a = \frac1u$, $c = \frac1v$: $8c + 16a = 4$ and $3c + 8a = \frac74$.
Doubling the second: $6c + 16a = \frac72$. Subtracting: $2c = \frac12$ → $c = \frac14$ → $v = 4$.
Then $8 \times \frac14 + 16a = 4$ → $a = \frac18$ → $u = 8$. Boat $= \frac{4+8}{2} = 6$ km/h.""",
        "Substitute reciprocals first — never clear denominators the brute-force way.", 60)
    return S
