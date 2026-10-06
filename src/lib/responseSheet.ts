// Reads a saved SSC / TCS iON (Digialm) candidate response sheet in the browser.
// Nothing is uploaded: the caller hands in the HTML text and gets counts back.
// The sheet is a stable HTML layout: `.section-cntnr` blocks hold `.question-pnl` panels, each option
// is a `td.rightAns` (SSC's key) or `td.wrngAns`, and the candidate's pick sits in the `.menu-tbl` row
// labelled "Chosen Option". Both letters (A-D) and digits (1-4) are accepted for the chosen option.

export interface ParsedQ {
  n: number;
  section: string;
  /** 1-based index of the option the candidate chose, or null if skipped */
  chosen: number | null;
  /** 1-based index of the correct option, or null if the sheet carries no key for this question */
  correct: number | null;
  status: string;
}

export interface SheetParse {
  questions: ParsedQ[];
  /** marking scheme stated in the sheet's own note, if present */
  scheme: { plus: number; minus: number } | null;
  candidate: { name?: string; roll?: string; date?: string; time?: string; subject?: string };
  warnings: string[];
}

const clean = (s: string | null | undefined) => (s ?? '').replace(/\s+/g, ' ').trim();

/** "A" / "b" / "3" -> 1-based index, anything else -> null */
export function optionIndex(raw: string): number | null {
  const v = clean(raw).replace(/[.)]$/, '');
  if (/^[1-9]$/.test(v)) return Number(v);
  if (/^[A-Ia-i]$/.test(v)) return v.toUpperCase().charCodeAt(0) - 64;
  return null;
}

function frac(s: string): number | null {
  const m = s.replace(/\s+/g, '').match(/^(\d+(?:\.\d+)?)(?:\/(\d+(?:\.\d+)?))?$/);
  if (!m) return null;
  return m[2] ? Number(m[1]) / Number(m[2]) : Number(m[1]);
}

/** Label/value cells of the small status table. The sheet's markup is sloppy, so cells are paired by position. */
function pairs(scope: Element): Map<string, string> {
  const out = new Map<string, string>();
  let label: string | null = null;
  scope.querySelectorAll('td').forEach((td) => {
    const t = clean(td.textContent);
    if (!t) return;
    if (t.endsWith(':')) { label = t.slice(0, -1).trim(); return; }
    if (label) { out.set(label, t); label = null; }
  });
  return out;
}

export function parseSheet(html: string): SheetParse {
  const stripped = html.replace(/data:image\/[a-z+]+;base64,[A-Za-z0-9+/=]+/gi, '');
  const doc = new DOMParser().parseFromString(stripped, 'text/html');
  const warnings: string[] = [];

  const info = doc.querySelector('.main-info-pnl');
  const candidate: SheetParse['candidate'] = {};
  info?.querySelectorAll('tr').forEach((tr) => {
    const cells = Array.from(tr.children).filter((c) => c.tagName === 'TD' || c.tagName === 'TH');
    if (cells.length < 2) return;
    const label = clean(cells[0].textContent).replace(/:$/, '').toLowerCase();
    const value = clean(cells[1].textContent);
    if (label === 'candidate name') candidate.name = value;
    else if (label === 'roll number') candidate.roll = value;
    else if (label === 'test date') candidate.date = value;
    else if (label === 'test time') candidate.time = value;
    else if (label === 'subject') candidate.subject = value;
  });

  const note = clean((info ?? doc.body)?.textContent);
  const cm = note.match(/correct answer will carry\s*([\d.]+(?:\s*\/\s*[\d.]+)?)\s*mark/i);
  const nm = note.match(/incorrect answer will carry\s*([\d.]+(?:\s*\/\s*[\d.]+)?)\s*negative/i);
  const plus = cm ? frac(cm[1]) : null;
  const minus = nm ? frac(nm[1]) : null;
  const scheme = plus != null ? { plus, minus: minus ?? 0 } : null;

  let groups = Array.from(doc.querySelectorAll('.grp-cntnr > .section-cntnr'));
  if (!groups.length) groups = Array.from(doc.querySelectorAll('.section-cntnr'));
  const panelsOf = groups.length
    ? groups.map((g, i) => ({ name: clean(g.querySelector('.section-lbl')?.textContent).replace(/^Section\s*:?\s*/i, '') || `Section ${i + 1}`, panels: Array.from(g.querySelectorAll('.question-pnl')) }))
    : [{ name: 'All questions', panels: Array.from(doc.querySelectorAll('.question-pnl')) }];

  const questions: ParsedQ[] = [];
  let seq = 0;
  for (const g of panelsOf) {
    for (const p of g.panels) {
      seq++;
      const numCell = Array.from(p.querySelectorAll('table.questionRowTbl td.bold')).find((c) => /^Q\.\s*\d+/i.test(clean(c.textContent)));
      const n = numCell ? Number(clean(numCell.textContent).match(/(\d+)/)?.[1]) : seq;
      const optionCells = Array.from(p.querySelectorAll('td.rightAns, td.wrngAns'));
      const right = optionCells.findIndex((c) => c.classList.contains('rightAns'));
      const menu = p.querySelector('table.menu-tbl');
      const meta = menu ? pairs(menu) : new Map<string, string>();
      const chosen = optionIndex(meta.get('Chosen Option') ?? '');
      questions.push({
        n, section: g.name, chosen,
        correct: right >= 0 ? right + 1 : null,
        status: clean(meta.get('Status')) || (chosen ? 'Answered' : 'Not Answered'),
      });
    }
  }

  if (!questions.length) warnings.push('No questions were found. This does not look like a saved response sheet.');
  const noKey = questions.filter((q) => q.correct == null).length;
  if (questions.length && noKey === questions.length) {
    warnings.push('This sheet has no correct-answer markings, so marks cannot be worked out from it. Use the score calculator and enter your counts instead.');
  } else if (noKey) {
    warnings.push(`${noKey} question${noKey === 1 ? '' : 's'} carried no correct-answer marking (for example a dropped question) and ${noKey === 1 ? 'is' : 'are'} left out of the marks.`);
  }
  return { questions, scheme, candidate, warnings };
}

export interface SectionScore { name: string; total: number; correct: number; wrong: number; skipped: number; unscored: number; marks: number }

export function scoreSheet(qs: ParsedQ[], plus: number, minus: number): { sections: SectionScore[]; all: SectionScore } {
  const map = new Map<string, SectionScore>();
  const blank = (name: string): SectionScore => ({ name, total: 0, correct: 0, wrong: 0, skipped: 0, unscored: 0, marks: 0 });
  const all = blank('Total');
  for (const q of qs) {
    const s = map.get(q.section) ?? blank(q.section);
    map.set(q.section, s);
    for (const t of [s, all]) {
      t.total++;
      if (q.correct == null) t.unscored++;
      else if (q.chosen == null) t.skipped++;
      else if (q.chosen === q.correct) { t.correct++; t.marks += plus; }
      else { t.wrong++; t.marks -= minus; }
    }
  }
  return { sections: [...map.values()], all };
}
