"""Readable rewrite of GA > Current Affairs (how to prepare). Content lives in _ca_p1, _ca_p2 (SUBS dict per part).
Run: python current_affairs.py  (patches content/core/topics/ga/current-affairs.json in place; idempotent)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _parts_driver import run  # noqa: E402

run("current-affairs", ["_ca_p1", "_ca_p2"])
