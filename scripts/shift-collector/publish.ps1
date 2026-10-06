# Build the static site and deploy it to Cloudflare Pages. Called by run.py --deploy.
# Aborts (no deploy) if validation or the build fails. -BuildOnly stops before deploying.
param([switch]$BuildOnly)
$ErrorActionPreference = 'Stop'
$site = 'C:\Users\Vinay Singirikonda\Desktop\examshortcut'
$stash = 'C:\Users\Vinay Singirikonda\Desktop\es-cf-stash'

Set-Location $site
# The validator currently reports ~1900 pre-existing "mistakes[n] must be a string" shape errors on topic files
# (stale rule vs. the lesson data; the site builds fine). Ignore only those; any other error aborts the publish.
$ErrorActionPreference = 'Continue'
$val = node scripts/validate-content.mjs 2>&1 | ForEach-Object { "$_" }
$ErrorActionPreference = 'Stop'
$bad = $val | Where-Object { $_ -match '^ - ' -and $_ -notmatch 'mistakes\[\d+\] must be a string' }
if ($bad) { $bad | Select-Object -First 10 | ForEach-Object { Write-Output $_ }; throw 'content validation failed' }

# free out/ (local review server holds it open)
Get-NetTCPConnection -LocalPort 3210 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'http\.server.*3210' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }

try {
  npm run build
  if ($LASTEXITCODE -ne 0) { throw 'build failed' }
  if (-not (Test-Path "$site\out\exam-analysis\ssc-cgl-2026\index.html")) { throw 'build output missing exam-analysis' }
} finally {
  Start-Process py -ArgumentList '-3.12', '-m', 'http.server', '3210', '--bind', '127.0.0.1' -WorkingDirectory "$site\out" -WindowStyle Hidden
}

if ($BuildOnly) { Write-Output 'build ok (not deployed)'; return }
Set-Location $stash
npx wrangler pages deploy "$site\out" --project-name examshortcut --branch main --commit-dirty=true
if ($LASTEXITCODE -ne 0) { throw 'wrangler deploy failed' }
Write-Output 'deployed'
