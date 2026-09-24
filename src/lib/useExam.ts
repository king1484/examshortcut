'use client';
import { useEffect, useState } from 'react';
import { getExamInfo, type ExamInfo } from './exams';

const KEY = 'es-exam';

export function getSelectedExamId(): string | null {
  try { return localStorage.getItem(KEY); } catch { return null; }
}

export function setSelectedExam(id: string | null) {
  try {
    if (id) localStorage.setItem(KEY, id); else localStorage.removeItem(KEY);
    window.dispatchEvent(new Event('es-exam'));
    window.dispatchEvent(new Event('es-store')); // lets cloud sync pick it up
  } catch {}
}

/** The exam the visitor is preparing for (null until they pick one). */
export function useSelectedExam(): ExamInfo | null {
  const [exam, setExam] = useState<ExamInfo | null>(null);
  useEffect(() => {
    const update = () => setExam(getExamInfo(getSelectedExamId()));
    update();
    window.addEventListener('es-exam', update);
    window.addEventListener('storage', update);
    return () => { window.removeEventListener('es-exam', update); window.removeEventListener('storage', update); };
  }, []);
  return exam;
}
