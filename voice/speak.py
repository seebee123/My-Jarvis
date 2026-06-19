import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

lock = threading.Lock()


def speak(text: str):
    print("Jarvis:", text)

    try:
        with lock:

            # 🔥 IMPORTANT: break long text
            chunks = text.split(". ")

            for chunk in chunks:
                if chunk.strip():
                    engine.say(chunk.strip())

            engine.runAndWait()

    except Exception as e:
        print("TTS ERROR:", e)