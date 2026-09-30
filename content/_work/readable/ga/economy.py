"""Readable rewrite of GA > Indian Economy. Content lives in _eco_p1.._eco_p3 (SUBS dict per part).
Run: python economy.py  (patches content/core/topics/ga/economy.json in place; idempotent)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _parts_driver import run  # noqa: E402

run("economy", ["_eco_p1", "_eco_p2", "_eco_p3"])
