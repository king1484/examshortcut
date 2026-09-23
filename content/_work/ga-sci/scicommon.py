# -*- coding: utf-8 -*-
"""Local helpers for the GA science/geography build scripts (imports shared gacommon)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ga"))
from gacommon import Q, save_topic  # noqa: E402,F401


def place(questions, targets):
    """Move each question's correct option to the given index by swapping two options.

    targets: list of ints (same length as questions) or None entries to leave a question as is.
    Only use on questions whose solution text does not refer to option positions.
    """
    assert len(questions) == len(targets)
    for x, t in zip(questions, targets):
        if t is None:
            continue
        a = x["answer"]
        if a == t:
            continue
        opts = x["options"]
        opts[a], opts[t] = opts[t], opts[a]
        x["answer"] = t
    return questions
