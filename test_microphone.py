"""Microphone diagnostic script to test speech recognition."""
import speech_recognition as sr

print("Testing microphone and speech recognition...\n")

r = sr.Recognizer()

try:
    print("Attempting to capture audio from default microphone...")
    with sr.Microphone() as source:
        print(f"Adjusting for ambient noise (3 seconds)...")
        r.adjust_for_ambient_noise(source, duration=3)
        print(f"Noise energy threshold: {r.energy_threshold}")
        print(f"Listening for 10 seconds - please speak clearly...")
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        print(f"Audio captured: {len(audio.frame_data)} bytes")

    print("\nAttempting Google Speech Recognition...")
    try:
        text = r.recognize_google(audio)
        print(f"✓ Recognized: {text}")
    except sr.UnknownValueError:
        print("✗ Could not understand audio")
    except sr.RequestError as e:
        print(f"✗ API error: {e}")

except Exception as e:
    print(f"✗ Error: {e}")
