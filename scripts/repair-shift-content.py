"""Withhold invalid figures and interview prompts in published automatic reports."""
import json
import sys
import datetime as dt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'shift-collector'))
from quality import sanitize_shift

changes = []
for file in (Path(__file__).parent.parent / 'content/shift-analysis').glob('*/*.json'):
    day = json.loads(file.read_text(encoding='utf8'))
    repaired = [sanitize_shift(s) if s.get('auto') else s for s in day.get('shifts', [])]
    if repaired != day.get('shifts') or day.get('correctionNote'):
        day['shifts'] = repaired
        day['correctionNote'] = '10 October 2026: invalid attempt figures, review-interview prompts and sources labelled for another shift were withheld where found. No replacement answers or estimates were invented.'
        # Rebuild overview text from retained fields so FAQs cannot repeat a withheld figure.
        label = dt.date.fromisoformat(day['date']).strftime('%d %B %Y').lstrip('0')
        usable = [s for s in repaired if s.get('status') in ('partial', 'reported')]
        levels = '; '.join(f"Shift {s['shift']}: {s.get('overall', 'not reported')}" for s in usable)
        ranges = '; '.join(f"Shift {s['shift']}: {s['goodAttempts']}" for s in usable if s.get('goodAttempts') and s['goodAttempts'] != 'Not reliably reported')
        pending = [str(s['shift']) for s in repaired if s.get('status') == 'pending']
        coverage = 'Read the individual shift pages for source coverage, recalled topics and correction notes.'
        if pending:
            coverage += ' No usable analysis is published for Shift ' + ', '.join(pending) + '; more evidence is needed.'
        day['intro'] = f"Candidate reviews for {label} describe the difficulty as follows: {levels}. These reports are unofficial and may disagree. {coverage} Attempt ranges describe candidate reports, not recommended attempts or safe-score predictions."
        day['faqs'] = [
            {'q': f'What difficulty was reported on {label}?', 'a': levels + '. These are unofficial candidate-review summaries.'},
            {'q': f'What attempt ranges were retained for {label}?', 'a': (ranges + '. ' if ranges else 'No reliable range is retained. ') + 'Invalid figures were withheld. The remaining figures are reported attempts, not official statistics or recommended targets.'},
            {'q': f'Is the analysis for {label} complete and official?', 'a': coverage + ' The analysis is not an official paper or SSC statement.'},
        ]
        file.write_text(json.dumps(day, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
        changes.append(file.name)
print('Corrected:', ', '.join(changes) or 'no changes needed')
