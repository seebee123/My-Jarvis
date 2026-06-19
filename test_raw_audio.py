"""Raw audio capture test - no speech recognition needed."""
import pyaudio
import struct

print("Raw Audio Capture Test\n")
print("This test captures audio WITHOUT using speech recognition.\n")

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, frames_per_buffer=CHUNK)

print("Recording for 10 seconds...")
print("Speak into your microphone NOW:\n")

frames = []
max_level = 0
for i in range(0, int(RATE / CHUNK * 10)):
    data = stream.read(CHUNK)
    frames.append(data)
    
    # Unpack and find max level
    audio_data = struct.unpack(f'{CHUNK}h', data)
    level = max(abs(x) for x in audio_data)
    max_level = max(max_level, level)
    
    # Show volume indicator
    bars = '█' * int(level / 500)
    print(f"  {bars} {level}")

stream.stop_stream()
stream.close()
p.terminate()

print("\n✓ Recording complete!")
print(f"Captured {len(frames)} chunks of audio")
print(f"Max audio level: {max_level}")

if max_level < 100:
    print("\n❌ PROBLEM: Microphone captured very little sound!")
    print("   Likely causes:")
    print("   1. Microphone is muted")
    print("   2. Microphone volume is too low")
    print("   3. Microphone isn't connected")
elif max_level < 1000:
    print("\n⚠️  WARNING: Audio level is quite low")
    print("   Try speaking LOUDER or moving closer to microphone")
else:
    print("\n✓ Audio level looks good!")
    print("   Speech recognition might work now")
