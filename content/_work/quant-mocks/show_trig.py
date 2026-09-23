import json

d = json.load(open(r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl\topics\quant\trigonometry.json", encoding="utf-8"))
for q in d["practice"] + d["solvedExamples"]:
    print("Q:", q["q"][:150])
    print("   ans:", q["options"][q["answer"]][:60])
