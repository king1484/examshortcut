import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _build import build  # noqa: E402

build(2026)
