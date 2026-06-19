# Launch Jarvis using the project's virtualenv Python (PowerShell)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
& "$scriptDir\venv\Scripts\python.exe" "$scriptDir\main.py"
