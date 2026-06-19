from voice.speak import speak
from voice.listen import listen

speak("Jarvis activated")

while True:
    cmd = listen()

    if not cmd:
        continue   # ⚠️ IMPORTANT FIX (avoid None crash)

    cmd = cmd.lower()

    if "hello" in cmd:
        speak("Hello boss")

    elif "time" in cmd:
        speak("Time module not connected yet")

    elif "exit" in cmd or "quit" in cmd:
        speak("Shutting down")
        break