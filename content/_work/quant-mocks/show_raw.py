import json

base = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl\topics\quant"
for t in ["algebra", "interest", "heights-distances", "number-system", "simplification"]:
    d = json.load(open(base + "\\" + t + ".json", encoding="utf-8"))
    print("=" * 8, t)
    for q in d["practice"] + d["solvedExamples"]:
        print(" Q:", q["q"][:160])
