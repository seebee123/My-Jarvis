# Jarvis - AI Voice Assistant

A Python voice assistant with PyQt6 GUI that listens for voice commands and responds with text-to-speech.

## Features
- 🎤 Real-time speech recognition (Google Speech Recognition API)
- 🔊 Text-to-speech responses (pyttsx3)
- 🖥️ PyQt6 dashboard GUI
- 🔄 Multi-threaded (voice loop + GUI)
- 📝 Command recognition and response

## Quick Start

### 1. Install Dependencies
```powershell
venv\Scripts\python -m pip install -r requirements.txt
```

### 2. Run the Application
```powershell
.\run_jarvis.ps1
```

Or using Python directly:
```powershell
venv\Scripts\python main.py
```

## Commands

Once running, speak clearly into your microphone:

- **"hello"** → Responds with "Hello boss"
- **"your name"** → Responds with "I am Jarvis"
- **"exit"** / **"quit"** → Gracefully shuts down

## Troubleshooting

### Issue: "Could not understand audio" keeps repeating

#### Step 1: Test Your Microphone
```powershell
venv\Scripts\python test_microphone.py
```
When prompted, **speak clearly** for 10 seconds. The script will show:
- Noise energy threshold
- Whether audio was captured
- Whether speech was recognized

#### Step 2: Check Microphone Hardware
- ✅ Is your microphone plugged in and enabled?
- ✅ Is the microphone set as the default input device (Windows Sound Settings)?
- ✅ Is the microphone volume turned up?
- ✅ Try testing the microphone in another app (e.g., Voice Recorder, Discord)

#### Step 3: Check Audio Permissions
- Go to **Settings** → **Privacy & Security** → **Microphone**
- Ensure Python has microphone access
- If Python is blocked, toggle it off and back on

#### Step 4: Improve Speech Recognition
Edit `voice/listen.py` and adjust these parameters:

```python
# Current defaults:
timeout=10              # Seconds to wait for speech to START
phrase_time_limit=15    # Seconds to listen for the ENTIRE phrase
```

For quieter microphones, increase `phrase_time_limit`:
```python
listen(phrase_time_limit=20)  # Listen for up to 20 seconds
```

#### Step 5: Enable Verbose Diagnostics
Edit `main.py` and change:
```python
command = listen()
```
to:
```python
command = listen(verbose=True)
```

This will print debug info including noise thresholds.

### Issue: Network error / API error

The app uses **Google Speech Recognition API**, which requires:
- ✅ Active internet connection
- ✅ API quota not exceeded (usually generous for testing)

If you see `Could not request results from the recognition service`, try:
1. Check your internet connection
2. Wait a few minutes and retry
3. Consider using offline recognition (requires additional setup)

## Project Structure

```
jarvis/
├── main.py                 # Main entry point (GUI + voice loop)
├── requirements.txt        # Pinned dependencies
├── run_jarvis.ps1         # PowerShell launcher
├── run_jarvis.bat         # Windows batch launcher
├── test_microphone.py     # Microphone diagnostics
├── voice/
│   ├── listen.py          # Speech recognition (Google)
│   ├── speak.py           # Text-to-speech (pyttsx3)
│   └── __init__.py
├── gui/
│   ├── dashboard.py       # PyQt6 GUI window
│   └── __init__.py
├── config/
│   └── settings.py        # Configuration
├── modules/
│   ├── system_monitor.py  # (stub for future use)
│   └── __init__.py
└── assets/                # (placeholder for images, etc.)
```

## Python Version
- **Required**: Python 3.11+ (project uses venv with Python 3.11)
- **Included**: VS Code configured to use `venv\Scripts\python.exe`

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| PyQt6 | 6.11.0 | GUI framework |
| SpeechRecognition | 3.10.1 | Audio capture & Google API |
| pyttsx3 | 2.90 | Text-to-speech (Windows SAPI5) |

## Contributing

To add new commands:
1. Edit `main.py` → `jarvis_loop()` function
2. Add a new `elif "keyword" in command:` block
3. Call `speak()` to respond and `set_status()` to update the GUI

Example:
```python
elif "weather" in command:
    speak("I cannot check the weather yet")
    set_status("Weather check not implemented")
```

## License
Personal project

---

**Tip:** For best results, speak in a clear, quiet environment. Ambient noise can reduce recognition accuracy.
