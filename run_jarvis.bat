@echo off
REM Launch Jarvis using the project's virtualenv Python (Windows)
SET SCRIPT_DIR=%~dp0
"%SCRIPT_DIR%venv\Scripts\python.exe" "%SCRIPT_DIR%main.py"
