"""Notes, patterns and topic PYQ patterns for reasoning/mirror-water-image."""
from _lib import P, PYQ

NOTES, PATTERNS = {}, {}

# ======================================================================= mirror-image
NOTES["mirror-image"] = r"""### What a vertical mirror does
Stand in front of a mirror and raise your right hand: the image raises the hand on the **other** side. A vertical mirror swaps **left and right** and keeps **top and bottom**. Whether the mirror is on the left or the right of the object, the image looks the same; only its position changes.

For a word, number or code this does **two** things together:
1. The **order** is reversed: the last character comes first.
2. **Each character** is flipped left-right: R, E, S, N, 2, 4, 7 face the other way.

Top stays top. A letter is never upside down in a mirror image.

### Symmetric letters and digits
Capital letters with a vertical line of symmetry look the same in a mirror:
**A H I M O T U V W X Y** (and the digits 0 and 8).

Every other capital looks reversed: B C D E F G J K L N P Q R S Z.

- A word looks **exactly the same** in a mirror only if it reads the same backwards **and** every letter is in the list above. Examples: MOM, WOW, TOOT, MAAM.
- A letter looks the same letter by letter only if it is in the list. For single-letter counting, order does not matter.

### Four-step check for option questions
1. **First character of the image = last character of the word.** Reject options that start with the wrong character.
2. Check one **asymmetric** character (R, E, S, 4, 7...). It must face the other way.
3. Make sure **top stays top**. If a letter is upside down, that option is a water image or a 180° turn.
4. Check the middle characters only if two options are still left.

### The usual wrong options
- **Water image:** order kept, letters upside down. (Wrong axis.)
- **180° turn:** order reversed **and** letters upside down. This is a mirror image plus a water image.
- **Reversed only:** order reversed, but letters not flipped.
- **Flipped only:** letters flipped, but order kept.

### Figures
For a line figure, every point moves to the same distance on the **other side** of the mirror line. Things on the left go to the right; heights do not change. Pick one clear feature (a dot, a shaded corner, a short tail) and check where it lands.
- A feature in the **top-left** corner goes to the **top-right** in a mirror image.
- If it went to the bottom-left, that is a water image; bottom-right is a 180° turn.

### Worked example
Mirror image of **REASON**. The image reads N O S A E R from left to right. A and O are symmetric and look the same. N, S, E and R face the other way. An option showing N O S A E R with upside-down letters is a 180° turn, not a mirror image.

### Quick revision
- Mirror: order reversed + each character flipped left-right; top stays top.
- Symmetric capitals: A H I M O T U V W X Y; digits 0 and 8.
- Same word in a mirror = palindrome made only of symmetric letters.
- Figures: left ↔ right, height unchanged; track one corner feature.
- Upside-down option = water image or 180° turn, never a mirror image.
"""

PATTERNS["mirror-image"] = [
    P("mi-p1", "Mirror image of a word", "very common",
      "A word in capitals with four image options; mirror placed vertically on one side.",
      "1. The image starts with the last letter.\n2. Every letter is flipped left-right; symmetric letters look unchanged.\n3. Nothing is upside down.\n\n**Why:** a vertical mirror only swaps left and right.",
      "Which describes the mirror image of REASON?",
      "Letters in the order N O S A E R, with N, S, E, R facing the other way and A, O unchanged."),
    P("mi-p2", "Mirror image of a number or code", "common",
      "A number, or a mix of letters and digits, with image options.",
      "1. Reverse the order.\n2. Flip each character left-right; 0 and 8 stay the same.\n3. Digits like 2, 3, 4, 5, 7 face the other way.\n\n**Why:** digits follow the same rule as letters.",
      "What is the order of characters in the mirror image of 4R95J?",
      "Reversed: J 5 9 R 4, each flipped left-right."),
    P("mi-p3", "Mirror image of a figure", "very common",
      "A line figure with a vertical mirror line (often marked M) beside it.",
      "1. Pick a clear feature: dot, shaded part or tail.\n2. Move it to the other side at the same height.\n3. Reject options where it moved up or down.\n\n**Why:** a vertical mirror keeps heights and swaps sides.",
      "A figure has a dot in its top-left corner. Where is the dot in its mirror image?",
      "Top-right corner. Bottom-left would be the water image, bottom-right a 180° turn."),
    P("mi-p4", "Letters that look the same in a mirror", "common",
      "How many letters of a word, or which letters, look unchanged in a mirror.",
      "1. Tick letters from A H I M O T U V W X Y.\n2. Count the ticks (repeated letters count each time).\n\n**Why:** only these capitals have a vertical line of symmetry.",
      "How many letters of MATHEMATICS look the same in a mirror?",
      "M, A, T, H, M, A, T, I = **8**. E, C and S look reversed."),
    P("mi-p5", "Word that looks the same in a mirror", "occasional",
      "Which word (or number) will look exactly the same in a vertical mirror.",
      "1. The word must read the same backwards.\n2. Every letter must be symmetric (A H I M O T U V W X Y).\n\n**Why:** the mirror reverses order and flips each letter, so both must be undone.",
      "Which looks the same in a mirror: NOON, TOOT or DEED?",
      "**TOOT**. NOON and DEED are palindromes, but N, D and E are not symmetric."),
]

# ======================================================================= water-image
NOTES["water-image"] = r"""### What water does
A lake below a hill shows the hill upside down. The water surface is a **horizontal** mirror below the object. It swaps **top and bottom** and keeps **left and right**. A question may also say "the mirror is placed horizontally below" or "along the line MN below the figure". All of these mean a water image.

For a word, number or code:
1. The **order stays the same**: the first character is still first.
2. **Each character** is turned upside down (flipped top to bottom, not spun round).

### Symmetric letters and digits
Capitals with a horizontal line of symmetry look the same in water:
**B C D E H I K O X** (and the digits 0, 3 and 8).

- A word looks exactly the same in water if **every** letter is in this list. The order does not matter here because water keeps the order. Examples: CHOICE, BOX, HIDE, CODE, DECIDE.
- Letters such as A, M, T, U, V, W, Y are symmetric in a mirror but **not** in water. M upside down looks like W.

### Four-step check for option questions
1. **First character stays first.** An option starting with the last character is a mirror image or a 180° turn.
2. Check one letter that is not in the list (A, R, T, 4, 7). It must be upside down.
3. Left-facing parts must still face left. For example, the bowl of R stays on the right side.
4. Compare the rest only if two options are still left.

### Mirror + water = half turn
A mirror image followed by a water image (in either order) is the same as turning the object through **180°**. The order is reversed and every character is upside down. The letters H, I, N, O, S, X, Z and the digits 0 and 8 look the same after a half turn. So SOS, NOON and XOX look unchanged after a half turn.

### Figures
Every point moves to the same distance on the other side of the horizontal line. Things at the top go to the bottom; left and right do not change.
- A feature in the **top-left** goes to the **bottom-left**.
- Top-right is the mirror image (wrong axis); bottom-right is a 180° turn.

### Worked example
Water image of **BUDGET**. The order stays B U D G E T. B, D and E are symmetric in water and look unchanged. U, G and T appear upside down (T looks like ⊥). An option that begins with T is not a water image.

### Quick revision
- Water: order kept + each character upside down; left stays left.
- Symmetric in water: B C D E H I K O X; digits 0, 3, 8.
- Same word in water = every letter in that list (no palindrome needed).
- Mirror + water = 180° turn: reversed order + upside down.
- Figures: top ↔ bottom, left and right unchanged.
"""

PATTERNS["water-image"] = [
    P("wi-p1", "Water image of a word", "very common",
      "A word in capitals; mirror placed horizontally below it.",
      "1. Keep the order.\n2. Turn each letter upside down; B C D E H I K O X look unchanged.\n3. Left-right direction of each letter stays.\n\n**Why:** a horizontal mirror only swaps top and bottom.",
      "Which describes the water image of BUDGET?",
      "Order B U D G E T; U, G, T upside down; B, D, E look unchanged."),
    P("wi-p2", "Water image of a number or code", "common",
      "A number or letter-digit code with water image options.",
      "1. Keep the order.\n2. Turn each character upside down; 0, 3, 8 look unchanged.\n3. 6 upside down is not 9 (9 is a half turn of 6).\n\n**Why:** water is a flip, not a rotation.",
      "Which digits of 83602 look unchanged in water?",
      "8, 3 and 0. 6 and 2 appear upside down."),
    P("wi-p3", "Water image of a figure", "very common",
      "A line figure with a horizontal line MN below it.",
      "1. Pick a clear feature.\n2. Move it to the other side of the horizontal line; keep its left-right position.\n3. Reject options where it moved sideways.\n\n**Why:** water keeps left and right.",
      "A figure has a shaded triangle in its top-right corner. Where is it in the water image?",
      "Bottom-right corner."),
    P("wi-p4", "Letters or words unchanged in water", "common",
      "How many letters look the same in water, or which word looks the same.",
      "1. Tick letters from B C D E H I K O X.\n2. For a whole word, every letter must be ticked.\n\n**Why:** these letters have a horizontal line of symmetry.",
      "Which word looks the same in water: CHOICE or CHANCE?",
      "**CHOICE**: every letter is in B C D E H I K O X. CHANCE has A and N."),
    P("wi-p5", "Mirror image followed by water image", "occasional",
      "The mirror image of a word is seen again in water (or the reverse).",
      "1. Mirror then water = a 180° turn.\n2. Reverse the order and turn every character upside down.\n\n**Why:** swapping left-right and then top-bottom is a half turn.",
      "How does the word SUN look after a mirror image followed by a water image?",
      "Turned through 180°: N U S order, each letter upside down. N and S look the same, U looks like ∩."),
]

# ======================================================================= clock-mirror
NOTES["clock-mirror"] = r"""### Why the 11:60 rule works
A clock seen in a vertical mirror has its hands swapped across the 12–6 line. A hand 20 minutes past 12 on the right side appears 20 minutes before 12 on the left. So the **actual time and the image time always add up to 12:00**.

$$\text{image} = 11{:}60 - \text{actual}$$

Writing 12:00 as 11:60 saves you from borrowing. The rule works both ways: actual = 11:60 − image.

Examples:
- 3:45 → 11:60 − 3:45 = **8:15**
- 10:10 → **1:50**
- 7:05 → **4:55**

### Special times
- **12:00 and 6:00** look the same in a mirror. These are the only two such times, because both hands then lie on the 12–6 line.
- **Times between 12:00 and 1:00** (like 12:20): use 23:60 − time → 11:40. Or treat 12:20 as 0:20 and do 11:60 − 0:20 = 11:40.
- **Whole hours:** h:00 → (12 − h):00. So 4:00 → 8:00.
- **With seconds:** use 11:59:60 − time. So 2:25:40 → 9:34:20.

### Reading a clock face in a mirror
When a figure shows a mirrored clock without numbers:
1. The 12 mark is still at the top.
2. Read the time the hands seem to show (the image time).
3. Actual time = 11:60 − image time.
A hand pointing to the 2 o'clock position in the image was really pointing to the 10 o'clock position.

### Two-step questions
- "The mirror shows 4:20. What will the actual time be after 1 hour 15 minutes?" First find the actual time: 11:60 − 4:20 = 7:40. Then add: 7:40 + 1:15 = **8:55**.
- Mirror of a mirror gives back the actual time.

### Traps in the options
- **12:00 − time done wrongly:** 12 − 3 = 9 and 60 − 45 = 15 gives 9:15 for 3:45. The hour must drop by one when the minutes are not zero, so the answer is 8:15.
- **Half-turn time:** 3:45 + 6:00 = 9:45 is where the hands are after a 180° turn, not a mirror image.
- **Hours mirrored, minutes kept** (8:45): only half the job.

### Why the hour drops by one
Take 3:45. The hour hand is three-quarters of the way from 3 to 4. In the mirror it sits three-quarters of the way from 9 to 8, so it is past 8, not past 9. The image shows 8:15, not 9:15. Whenever the minutes are not zero, the image hour is 11 − h, not 12 − h.

### Worked example
The mirror image of a clock shows 5:35. Find the actual time.
Actual = 11:60 − 5:35 = 6:25. Check: 5:35 + 6:25 = 12:00. An option of 7:25 comes from forgetting to borrow; 11:35 is the half-turn time.

### Check
Add your answer to the given time. The sum must be exactly 12:00 (or 24:00 for 12:xx times).

### Quick revision
- Image = 11:60 − actual; actual = 11:60 − image.
- 12:xx → 23:60 − time; with seconds → 11:59:60 − time.
- 12:00 and 6:00 look unchanged.
- Mirrored clock face: read it as it looks, then take 11:60 minus that.
- Check: given + answer = 12:00.
"""

PATTERNS["clock-mirror"] = [
    P("cm-p1", "Mirror time from actual time", "very common",
      "A clock shows a time; what time does its mirror image show?",
      "1. Subtract from 11:60.\n2. Check that the sum is 12:00.\n\n**Why:** each hand is reflected across the 12–6 line, so actual + image = 12 hours.",
      "A clock shows 3:45. What does its mirror image show?",
      "11:60 − 3:45 = **8:15**.", formula=r"\text{image}=11{:}60-\text{actual}"),
    P("cm-p2", "Actual time from mirror reading", "common",
      "The mirror image shows a time; find the actual time.",
      "1. Use the same rule: 11:60 − image time.\n\n**Why:** reflecting twice gives back the original, so the rule works in both directions.",
      "A clock looks like 2:25 in a mirror. What is the actual time?",
      "11:60 − 2:25 = **9:35**."),
    P("cm-p3", "Special cases: 12:xx and seconds", "occasional",
      "Time between 12 and 1, a whole-hour time, or a time with seconds.",
      "1. 12:xx → 23:60 − time.\n2. Seconds → 11:59:60 − time.\n3. 12:00 and 6:00 map to themselves.\n\n**Why:** the sum is still 12 hours; only the borrowing changes.",
      "What is the mirror image of 12:35?",
      "23:60 − 12:35 = **11:25**."),
    P("cm-p4", "Mirrored clock face", "common",
      "A drawn clock (often without numbers) is said to be a mirror image; find the actual time.",
      "1. Read the time the hands appear to show.\n2. Actual = 11:60 − that time.\n\n**Why:** reading the picture gives the image time; the rule converts it back.",
      "A mirrored clock face appears to show 2:30. What is the actual time?",
      "11:60 − 2:30 = **9:30**."),
    P("cm-p5", "Mirror time with elapsed time", "occasional",
      "The mirror time is given and the question asks the actual time some minutes later (or earlier).",
      "1. Convert the mirror reading to the actual time first.\n2. Then add or subtract the elapsed time.\n\n**Why:** time passes on the real clock; converting after adding gives a wrong answer.",
      "A mirror shows 4:20. What will the actual time be 1 hour 15 minutes later?",
      "Actual 11:60 − 4:20 = 7:40; 7:40 + 1:15 = **8:55**."),
]

# ======================================================================= topic PYQ patterns
PYQS = [
    PYQ("Mirror image of word / number", "very common",
        "A word, number or code with four image options; mirror on one side.",
        "Order reversed + each character flipped left-right. Check the first character (= last of the word) and one asymmetric letter.",
        "mirror-image", "What is the first character (from the left) in the mirror image of EXAM25?",
        "The last character, **5**, flipped left-right."),
    PYQ("Water image of word / number", "common",
        "Same, but the mirror is below (water or line MN below).",
        "Order kept; each character upside down. B C D E H I K O X and 0, 3, 8 look unchanged.",
        "water-image", "Which letters of BUDGET look unchanged in water?",
        "B, D, E (3 letters)."),
    PYQ("Mirror image of a figure", "very common",
        "A line figure with a vertical mirror line beside it.",
        "Track one corner feature: left ↔ right, height unchanged. Reject upside-down options.",
        "mirror-image", "A dot is at the bottom-left of a figure. Where is it in the mirror image?",
        "Bottom-right."),
    PYQ("Water image of a figure", "common",
        "A line figure with a horizontal line below it.",
        "Track one feature: top ↔ bottom, left and right unchanged.",
        "water-image", "A dot is at the bottom-left of a figure. Where is it in the water image?",
        "Top-left."),
    PYQ("Clock mirror time", "very common",
        "Time seen in a mirror, or actual time from a mirror reading.",
        "11:60 − time, both ways. 12:xx uses 23:60. Check: sum = 12:00.",
        "clock-mirror", "A clock shows 7:05. What does the mirror show?",
        "11:60 − 7:05 = **4:55**."),
    PYQ("Mirrored clock face or elapsed time", "occasional",
        "A drawn mirrored clock, or the actual time some minutes after a mirror reading.",
        "Read the image time, convert with 11:60 − time, then add or subtract elapsed time.",
        "clock-mirror", "A mirror shows 9:10. What is the actual time 30 minutes later?",
        "Actual 2:50; plus 30 minutes = **3:20**."),
    PYQ("Symmetric letters count", "common",
        "How many letters of a word look the same in a mirror or in water.",
        "Mirror list: A H I M O T U V W X Y. Water list: B C D E H I K O X. Count each occurrence.",
        "mirror-image", "How many letters of MATHEMATICS look the same in a mirror?",
        "M A T H M A T I = **8**."),
    PYQ("Word unchanged in mirror / water", "occasional",
        "Which word looks exactly the same in its image.",
        "Mirror: palindrome of symmetric letters (WOW, TOOT). Water: every letter in B C D E H I K O X (CHOICE).",
        "water-image", "Which looks the same in water: DECIDE or DEFINE?",
        "**DECIDE**: every letter is in B C D E H I K O X."),
]
