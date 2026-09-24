import { getApp, getApps, initializeApp } from 'firebase/app';
import { GoogleAuthProvider, getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

/* Firebase (Spark free tier): Auth for Google + email-link login, one Firestore doc
   per user (user_progress/{uid}) for progress sync. Without the NEXT_PUBLIC_FIREBASE_*
   env vars the site runs in preview mode: gates open, progress stays in localStorage. */

const cfg = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

export const authConfigured = Boolean(cfg.apiKey && cfg.authDomain && cfg.projectId && cfg.appId);

const app = authConfigured ? (getApps().length ? getApp() : initializeApp(cfg)) : null;

export const auth = app ? getAuth(app) : null;
export const db = app ? getFirestore(app) : null;
export const googleProvider = new GoogleAuthProvider();
