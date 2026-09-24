'use client';
import { supabase } from './supabase';

/* Local-first progress. Everything is written to localStorage as before; when the
   visitor is logged in, those keys are mirrored to one jsonb row (user_progress.data).
   On login the cloud copy and this browser's copy are merged, so nothing done before
   logging in is lost. */

export const SYNC_KEYS = [
  'es-mistakes', 'es-bookmarks', 'es-topic-scores', 'es-studied', 'es-attempts',
  'es-study-plan', 'es-post-planner', 'es-dest-history', 'es-vocab-known', 'es-exam', 'es-daily',
] as const;

type Data = Record<string, unknown>;

function readLocal(): Data {
  const out: Data = {};
  for (const k of SYNC_KEYS) {
    try {
      const v = localStorage.getItem(k);
      if (v == null) continue;
      try { out[k] = JSON.parse(v); } catch { out[k] = v; } // es-exam is a bare string
    } catch {}
  }
  return out;
}

function writeLocal(d: Data) {
  for (const k of SYNC_KEYS) {
    if (!(k in d)) continue;
    try { localStorage.setItem(k, typeof d[k] === 'string' ? (d[k] as string) : JSON.stringify(d[k])); } catch {}
  }
  window.dispatchEvent(new Event('es-exam'));
}

const isObj = (v: unknown): v is Record<string, unknown> => !!v && typeof v === 'object' && !Array.isArray(v);

/** Merge two copies of one key. Maps are unioned; per-key special cases keep the better value. */
function mergeKey(key: string, cloud: unknown, local: unknown): unknown {
  if (cloud === undefined) return local;
  if (local === undefined) return cloud;
  if (key === 'es-attempts' && isObj(cloud) && isObj(local)) {
    const out: Record<string, unknown[]> = {};
    for (const id of new Set([...Object.keys(cloud), ...Object.keys(local)])) {
      const all = [...((cloud[id] as { at: number }[]) ?? []), ...((local[id] as { at: number }[]) ?? [])];
      const seen = new Set<number>();
      out[id] = all.filter((a) => (seen.has(a.at) ? false : (seen.add(a.at), true))).sort((a, b) => a.at - b.at);
    }
    return out;
  }
  if (key === 'es-topic-scores' && isObj(cloud) && isObj(local)) {
    const out: Record<string, unknown> = { ...cloud };
    for (const [k, v] of Object.entries(local)) {
      const c = cloud[k] as { best: number; at: number } | undefined, l = v as { best: number; at: number };
      out[k] = !c ? l : { ...(l.at >= c.at ? l : c), best: Math.max(c.best, l.best) };
    }
    return out;
  }
  if (Array.isArray(cloud) && Array.isArray(local)) {
    const seen = new Set<string>();
    return [...cloud, ...local].filter((x) => { const s = JSON.stringify(x); return seen.has(s) ? false : (seen.add(s), true); });
  }
  if (isObj(cloud) && isObj(local) && key !== 'es-study-plan' && key !== 'es-post-planner' && key !== 'es-daily') {
    return { ...cloud, ...local };
  }
  return local; // single-value settings: this browser wins
}

export async function pullAndMerge(userId: string) {
  if (!supabase) return;
  const { data, error } = await supabase.from('user_progress').select('data').eq('user_id', userId).maybeSingle();
  if (error) { console.warn('[sync] pull failed', error.message); return; }
  const cloud = (data?.data ?? {}) as Data;
  const local = readLocal();
  const merged: Data = {};
  for (const k of SYNC_KEYS) {
    const v = mergeKey(k, cloud[k], local[k]);
    if (v !== undefined) merged[k] = v;
  }
  writeLocal(merged);
  await push(userId, merged);
  window.dispatchEvent(new Event('es-store'));
}

let lastPushed = '';
async function push(userId: string, d: Data = readLocal()) {
  if (!supabase) return;
  const body = JSON.stringify(d);
  if (body === lastPushed) return;
  const { error } = await supabase.from('user_progress').upsert({ user_id: userId, data: d, updated_at: new Date().toISOString() });
  if (error) console.warn('[sync] push failed', error.message);
  else lastPushed = body;
}

/** Mirror every local write to the cloud (debounced). Returns an unsubscribe. */
export function startAutoPush(userId: string) {
  let t: ReturnType<typeof setTimeout> | undefined;
  const schedule = () => { clearTimeout(t); t = setTimeout(() => void push(userId), 2500); };
  const onHide = () => { if (document.visibilityState === 'hidden') void push(userId); };
  window.addEventListener('es-store', schedule);
  document.addEventListener('visibilitychange', onHide);
  return () => { clearTimeout(t); window.removeEventListener('es-store', schedule); document.removeEventListener('visibilitychange', onHide); };
}

export function resetSyncState() { lastPushed = ''; }
