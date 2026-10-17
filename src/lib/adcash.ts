import { isPublicAdPage } from './advertising';

// Issued for ExamShortcut's manual Display 300x250 zone on 17 October 2026.
export const ADCASH_ZONE_ID = '12327298';
export const ADCASH_LIBRARY_URL = 'https://acscdn.com/script/aclib.js';
export const ADCASH_BANNER_SCRIPT = `aclib.runBanner({ zoneId: '${ADCASH_ZONE_ID}' });`;

export function canRequestAdcash(hostname: string, pathname: string): boolean {
  return ['examshortcut.in', 'www.examshortcut.in'].includes(hostname)
    && isPublicAdPage(pathname);
}
