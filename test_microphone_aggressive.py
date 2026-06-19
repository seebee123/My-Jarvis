"""Aggressive microphone diagnostics - more sensitive to quiet speech."""
import speech_recognition as sr

print("Aggressive Microphone Test (HIGH SENSITIVITY)\n")

r = sr.Recognizer()
# More sensitive: lower threshold to catch quieter speech
r.energy_threshold = 1000  # Default is ~4000; lower = more sensitive

try:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise (5 seconds)...")
        r.adjust_for_ambient_noise(source, duration=5)
        print(f"Dynamic threshold: {r.energy_threshold}")
        print(f"\nListening for 15 seconds...")
        print("Try speaking CLEARLY and a bit LOUDER than normal.\n")
        
        audio = r.listen(source, timeout=15, phrase_time_limit=15)
        print(f"✓ Audio captured: {len(audio.frame_data)} bytes")

    print("\nSending to Google Speech Recognition...\n")
    try:
        text = r.recognize_google(audio)
        print(f"✓ SUCCESS: '{text}'")
    except sr.UnknownValueError:
        print("✗ Could not understand audio")
        print("\nTroubleshooting tips:")
        print("  1. Speak LOUDER and more CLEARLY")
        print("  2. Move closer to the microphone")
        print("  3. Reduce background noise (fan, music, etc.)")
        print("  4. Try a different microphone if available")
    except sr.RequestError as e:
        print(f"✗ API Error: {e}")
        print("\nThis likely means:")
        print("  - No internet connection")
        print("  - Google API temporarily unavailable")
        print("  - API quota exceeded")

except Exception as e:
    print(f"✗ Unexpected error: {e}")
