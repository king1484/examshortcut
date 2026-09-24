-- ExamShortcut: one row of synced progress per user.
-- Run once in Supabase → SQL editor.
create table if not exists public.user_progress (
  user_id uuid primary key references auth.users (id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.user_progress enable row level security;

drop policy if exists "own progress: read" on public.user_progress;
drop policy if exists "own progress: insert" on public.user_progress;
drop policy if exists "own progress: update" on public.user_progress;
drop policy if exists "own progress: delete" on public.user_progress;

create policy "own progress: read"   on public.user_progress for select using (auth.uid() = user_id);
create policy "own progress: insert" on public.user_progress for insert with check (auth.uid() = user_id);
create policy "own progress: update" on public.user_progress for update using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own progress: delete" on public.user_progress for delete using (auth.uid() = user_id);
