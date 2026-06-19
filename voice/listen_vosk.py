import json
import pyaudio
from vosk import Model, KaldiRecognizer

def listen_vosk():
    model = Model("model")  # <-- download model folder

    recognizer = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8192
    )

    print("Listening...")

    while True:
        data = stream.read(4096, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")

            if text:
                print("User:", text)
                return text.lower()

        else:
            partial = json.loads(recognizer.PartialResult())
            if partial.get("partial"):
                print("...", partial["partial"])
