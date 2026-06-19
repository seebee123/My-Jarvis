import speech_recognition as sr
from voice.state import is_speaking

def listen():

    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            # 🚨 wait until speaking finishes
            if is_speaking.is_set():
                return None

            print("Listening...")

            r.adjust_for_ambient_noise(source, duration=0.5)

            audio = r.listen(source, timeout=6, phrase_time_limit=6)

            query = r.recognize_google(audio)

            print("User:", query)

            return query.lower().strip()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

    except sr.WaitTimeoutError:
        return None

    except Exception as e:
        print("LISTEN ERROR:", e)
        return None