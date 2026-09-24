'use client';
import { createClient, type SupabaseClient } from '@supabase/supabase-js';

/* Accounts exist only to sync personal progress across devices. Everything public
   (notes, calculators, cutoffs, open mocks) works without one. When the env vars are
   missing the site runs in local-only mode and auth gates let everyone through. */
const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

export const supabase: SupabaseClient | null =
  url && key ? createClient(url, key, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } }) : null;

export const authConfigured = !!supabase;
