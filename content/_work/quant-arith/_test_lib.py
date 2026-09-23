from _lib import parse, F, _eq
cases = ["₹1,250", "12.5%", r"$\frac{3}{4}$", r"$12\frac{1}{2}$%", "45 km/h", "3 : 4", "2:3:5",
         "₹12,40,000", "7 days", r"$33\frac{1}{3}\%$", "-4", "150 m", "0.25", "18 minutes", r"$\dfrac{7}{12}$"]
for c in cases:
    print(repr(c), "->", parse(c))
assert _eq(parse("4:6"), (F(2), F(3)))
print("ok")
