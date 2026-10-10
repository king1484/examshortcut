"""Unattended shift-analysis job. Scheduled by Windows Task Scheduler, no Claude Code needed.

    py -3.12 scripts/shift-collector/run.py [--deploy] [--date YYYY-MM-DD] [--force]

1. Picks the exam day(s) to work on (today, plus yesterday until 12:00 IST for late reviews).
2. collect.py  -> YouTube reviews (+ transcripts) and web articles.
3. synthesize.py -> open-weights LLM writes content/shift-analysis/<exam>/<date>.json.
4. If a day file changed and --deploy is given: publish.ps1 (build, then wrangler deploy).
"""
import argparse, datetime as dt, json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
END_IST = {1: (11, 0), 2: (14, 30), 3: (18, 0)}
LOGDIR = os.path.join(HERE, "logs")


def log(msg):
    line = f"{dt.datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line, flush=True)
    os.makedirs(LOGDIR, exist_ok=True)
    with open(os.path.join(LOGDIR, dt.datetime.now(IST).strftime("%Y-%m-%d") + ".log"), "a", encoding="utf8") as f:
        f.write(line + "\n")


def run(cmd, timeout):
    env = {**os.environ, "PYTHONIOENCODING": "utf8"}
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf8", errors="replace", timeout=timeout, env=env)
    tail = (p.stderr or "").strip().splitlines()[-25:]
    for l in tail:
        log("   " + l[:200])
    return p.returncode, p.stdout


def day_file(date):
    return os.path.join(ROOT, "content", "shift-analysis", "ssc-cgl-2026", date + ".json")


def shifts_state(date):
    f = day_file(date)
    if not os.path.exists(f):
        return {}
    return {s["shift"]: s for s in json.load(open(f, encoding="utf8"))["shifts"]}


def todo(date, now):
    """True if any shift of `date` has ended and is not yet a complete 'reported' entry."""
    d = dt.date.fromisoformat(date)
    st = shifts_state(date)
    for n, (h, m) in END_IST.items():
        ended = now >= dt.datetime.combine(d, dt.time(h, m), IST) + dt.timedelta(minutes=20)
        if ended and st.get(n, {}).get("status") not in ("reported", "not-held"):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--deploy", action="store_true")
    ap.add_argument("--force", action="store_true", help="work on --date even if all shifts look done")
    a = ap.parse_args()
    now = dt.datetime.now(IST)
    exams = json.load(open(os.path.join(ROOT, "content", "shift-analysis", "exams.json"), encoding="utf8"))
    win = next(e["window"] for e in exams if e["slug"] == "ssc-cgl-2026")
    today = now.date()
    cands = [a.date] if a.date else [today.isoformat()] + ([(today - dt.timedelta(days=1)).isoformat()] if now.hour < 12 else [])
    cands = [c for c in cands if win["start"] <= c <= win["end"]]
    lock = os.path.join(HERE, "run.lock")
    if os.path.exists(lock) and time.time() - os.path.getmtime(lock) < 3 * 3600:
        log("another run is active, exiting"); return 0
    open(lock, "w").write(str(os.getpid()))
    try:
        changed = []
        for date in cands:
            if not (a.force or todo(date, now)):
                log(f"{date}: nothing due"); continue
            log(f"{date}: collecting")
            rc, out = run([sys.executable, "-X", "utf8", os.path.join(HERE, "collect.py"), "--date", date], 1500)
            log("   " + out.strip().splitlines()[-1] if out.strip() else f"   collect rc={rc}")
            if rc != 0:
                raise RuntimeError(f'Collector failed for {date} (exit {rc})')
            before = open(day_file(date), "rb").read() if os.path.exists(day_file(date)) else b""
            rc, _ = run([sys.executable, "-X", "utf8", os.path.join(HERE, "synthesize.py"), "--date", date], 3000)
            after = open(day_file(date), "rb").read() if os.path.exists(day_file(date)) else b""
            log(f"{date}: synthesize rc={rc} changed={before != after}")
            if rc not in (0, 2, 3):
                raise RuntimeError(f'Synthesis failed for {date} (exit {rc})')
            if rc == 0 and before != after:
                changed.append(date)
        if changed and a.deploy:
            log("publishing: build + deploy")
            p = subprocess.run(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", os.path.join(HERE, "publish.ps1")],
                               capture_output=True, text=True, encoding="utf8", errors="replace", timeout=3000)
            for l in (p.stdout + p.stderr).strip().splitlines()[-8:]:
                log("   " + l[:200])
            log(f"publish rc={p.returncode}")
            return p.returncode
        if changed:
            log("changed (not deployed, run with --deploy): " + ", ".join(changed))
        return 0
    finally:
        try:
            os.remove(lock)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
