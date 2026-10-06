# One-time setup: schedule the unattended shift-analysis job in Windows Task Scheduler.
#   .\register-task.ps1            -> collect + analyse, build, deploy (full auto)
#   .\register-task.ps1 -NoDeploy  -> collect + analyse only (files written, nothing published)
# Remove with: Unregister-ScheduledTask -TaskName ExamShortcutShiftAnalysis -Confirm:$false
param([switch]$NoDeploy)
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = (Get-Command py).Source
$flag = if ($NoDeploy) { '' } else { '--deploy' }
$arg = "-3.12 -X utf8 `"$here\run.py`" $flag"
$action = New-ScheduledTaskAction -Execute $py -Argument $arg -WorkingDirectory (Split-Path -Parent (Split-Path -Parent $here))

# IST times: ~45 min after each shift ends (11:00, 14:30, 18:00), a retry an hour later, a late pass, and a next-morning refresh.
$times = '08:30', '11:45', '12:45', '15:15', '16:15', '18:45', '19:45', '21:30'
$triggers = $times | ForEach-Object { New-ScheduledTaskTrigger -Daily -At $_ }
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -WakeToRun -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 2) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName ExamShortcutShiftAnalysis -Action $action -Trigger $triggers -Settings $settings -Description 'Collects SSC CGL shift reviews, analyses them with an LLM and updates examshortcut.in' -Force | Out-Null
Write-Output "registered: $($times -join ', ') (local time)  deploy=$(-not $NoDeploy)"
