"""Log all alt-rule violations across classification/series question builders without asserting."""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import classification_checks as cc

problems = []


def soft(fn_name):
    orig = getattr(cc, fn_name)

    def wrapped(*a, **k):
        try:
            return orig(*a, **k)
        except AssertionError as e:
            problems.append(f"{fn_name}: {e}")
            return a[1] if len(a) > 1 else None
    setattr(cc, fn_name, wrapped)


soft("alt_num")
soft("alt_letters")
soft("one_breaks")
soft("only_fits")

from _lib import load  # noqa: E402
d = load("classification")

for mod in ("classification_1", "classification_2", "classification_3"):
    m = importlib.import_module(mod)
    try:
        m.apply(d)
    except Exception as e:
        problems.append(f"{mod}.apply crashed: {type(e).__name__}: {e}")

print(f"{len(problems)} problems")
for p in problems:
    print(" -", p)
