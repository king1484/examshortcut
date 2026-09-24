"""Phase-2 deep content for quant/number-system. Run: py -3 number-system.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
import ns_types, ns_div, ns_rem, ns_unit, ns_fac, ns_frac


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Missing digits for divisibility (11, 72, 88, 99)", "very common",
      "A number with one or two blanks (x, y) and the words 'is divisible by'. The options are digits or x + y.",
      "Split a composite divisor into co-prime parts (72 = 8 × 9, 88 = 8 × 11). Apply the rule with fewest choices first — the last-three-digits rule of 8 or the alternating-sum rule of 11 — then the digit-sum rule. List the few cases; the asked quantity is usually the same in all of them.",
      "ns-divisibility", "If 8x6y4 is divisible by 88, find x + y.",
      r"Rule of 8: 6y4 → y = 2 or 6. Rule of 11: $18 - (x + y) \in \{0, 11\}$ → $x + y = 7$."),
    P("Remainder when the new divisor is a factor of the old one", "very common",
      "'A number divided by 527 leaves 64. What is the remainder when it is divided by 17?'",
      "Check that the new divisor divides the old one. If it does, just divide the old remainder by the new divisor. This is a 20-second question.",
      "ns-remainders", "N ÷ 195 leaves 47. Find N ÷ 15.",
      r"$195 = 15 \times 13$; $47 \bmod 15 = 2$."),
    P("Remainder of large powers and products", "very common",
      r"Huge powers such as $5^{70}$, $67^{67} + 67$ or products like $1021 \times 1023 \times 1025$ divided by a small number.",
      "Replace every number by its remainder (negative remainders are allowed). For powers, find a small power that leaves 1 or −1 and split the exponent. If the final result is negative, add the divisor.",
      "ns-remainders", r"Remainder of $67^{67} + 67$ divided by 68?",
      r"$67 \equiv -1$, so $(-1)^{67} + 67 = 66$."),
    P("Unit digit of powers, products and sums", "very common",
      r"'Find the unit digit of $7^{95} \times 3^{58}$' or of a sum/difference of powers or a factorial sum.",
      "Keep only the unit digit of each base and the exponent mod 4 (remainder 0 means the 4th power). Multiply or add the unit digits. For a negative difference add 10. Factorials from 5! end in 0.",
      "ns-unit-digit", r"Unit digit of $2137^{754}$?",
      r"$754 \bmod 4 = 2$ → $7^2 = 49$ → **9**."),
    P("Number of factors, odd/even factors, sum of factors", "very common",
      "'How many factors does 720 have?', 'how many even factors …', 'sum of all factors of 360'.",
      "Prime-factorise. Number of factors = product of (power + 1). Odd factors: drop the 2. Sum of factors = product of brackets (1 + p + … + p^a).",
      "ns-factors", "How many odd factors does 3600 have?",
      r"$3600 = 2^4 \times 3^2 \times 5^2$ → odd factors $= 3 \times 3 = 9$."),
    P("Trailing zeros and highest power in n!", "common",
      "'How many zeros are at the end of 125!?', 'largest n such that $3^n$ divides 100!'.",
      "Successively divide n by 5 (for zeros) or by the prime p and add all quotients. For a composite like 12 find the exponent of each prime part and take the smallest after dividing by the needed power.",
      "ns-factors", "Zeros at the end of 125!?",
      r"$25 + 5 + 1 = 31$."),
    P("Algebraic divisibility of a^n ± b^n", "common",
      r"Expressions like $17^{25} + 23^{25}$ or $7^{24} - 1$ with 'is divisible by'.",
      "Odd power sum → divisible by (a + b). Difference → always divisible by (a − b), and by (a + b) too when the power is even. Match these with the options.",
      "ns-divisibility", r"$19^{32} - 11^{32}$ is divisible by?",
      "Even power difference → both 19 − 11 = 8 and 19 + 11 = 30."),
    P("Recurring decimals to fractions and their sums", "common",
      r"Barred decimals like $2.4\overline{7}$ or $0.\overline{6} + 0.\overline{7} + 0.\overline{8}$.",
      "Pure recurring: repeating digits over 9s. Mixed: (all digits − non-repeating digits) over (9s then 0s). Convert every term to a fraction before adding.",
      "ns-fractions-decimals", r"$0.4\overline{7} + 0.3\overline{5} = ?$",
      r"$\frac{43}{90} + \frac{32}{90} = \frac{75}{90} = \frac{5}{6}$."),
    P("Counting multiples in a range and series sums", "common",
      "'How many numbers between 200 and 600 are divisible by 4, 5 and 6?', 'sum of all three-digit multiples of 7'.",
      "Use floor division: multiples of k from a to b = ⌊b/k⌋ − ⌊(a−1)/k⌋. 'And' means LCM; 'or' means inclusion–exclusion. For sums use n/2 × (first + last).",
      "ns-types-counting", "How many integers from 1 to 1000 are divisible by neither 4 nor 6?",
      r"$1000 - (250 + 166 - 83) = 667$."),
    P("Two-digit numbers with reversed digits", "occasional",
      "'If the digits are reversed the number increases by 27', 'a number is 4 times the sum of its digits'.",
      "Write the number as 10a + b. Difference with the reverse is 9(a − b); sum with the reverse is 11(a + b). Or test the options quickly.",
      "ns-types-counting", "A two-digit number is 4 times its digit sum; adding 27 reverses it. Find it.",
      r"$b = 2a$ and $b - a = 3$ → 36."),
]

if __name__ == "__main__":
    subs = [m.build() for m in (ns_types, ns_div, ns_rem, ns_unit, ns_fac, ns_frac)]
    apply_topic("number-system", subs, PYQ)
