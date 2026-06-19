from voice.speak import speak
from voice.listen import listen
from gui.dashboard import set_status
import datetime
import webbrowser
import random

try:
    from ollama import chat
except:
    chat = None


# =========================
# 🎵 MUSIC
# =========================
def handle_music():
    speak("Which song do you want?")
    query = listen()

    if query:
        speak(f"Playing {query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        set_status(f"JARVIS: Playing {query}")
    else:
        speak("Song not detected")
        set_status("JARVIS: Song not detected")


# =========================
# 🌤 WEATHER
# =========================
def handle_weather():
    speak("Tell me city name")
    city = listen()

    if city:
        webbrowser.open(f"https://www.google.com/search?q=weather+{city}")
        speak(f"Showing weather for {city}")
        set_status(f"JARVIS: Weather for {city}")
    else:
        speak("City not detected")
        set_status("JARVIS: City not detected")


# =========================
# 🌐 GOOGLE
# =========================
def handle_google():
    speak("Opening Google")
    webbrowser.open("https://google.com")
    set_status("JARVIS: Google opened")


# =========================
# 📺 YOUTUBE
# =========================
def handle_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://youtube.com")
    set_status("JARVIS: YouTube opened")


# =========================
# 🤖 CHATGPT
# =========================
def handle_chatgpt():
    speak("Opening ChatGPT")
    webbrowser.open("https://chatgpt.com")
    set_status("JARVIS: ChatGPT opened")


# =========================
# ⏰ TIME
# =========================
def handle_time():
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"Time is {now}")
    set_status(f"JARVIS: Time is {now}")


# =========================
# 😂 JOKE
# =========================
def handle_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the computer go to the doctor? Because it caught a virus.",
        "There are ten types of people in the world.",
        "I would tell you a UDP joke, but you might not get it."
    ]

    joke = random.choice(jokes)
    speak(joke)
    set_status(f"JARVIS: {joke}")


# =========================
# 🪙 COIN
# =========================
def handle_coin():
    result = random.choice(["Heads", "Tails"])
    speak(result)
    set_status(f"JARVIS: {result}")


# =========================
# 🎲 DICE
# =========================
def handle_dice():
    result = random.randint(1, 6)
    speak(f"You got {result}")
    set_status(f"JARVIS: Dice {result}")


# =========================
# 💀 EXIT
# =========================
def handle_exit():
    speak("Goodbye boss")
    set_status("JARVIS QUIT")
    return "EXIT"


# =========================
# 🤖 OLLAMA AI
# =========================
def get_ai_response(prompt: str):

    if chat is None:
        return None

    try:
        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": "You are Jarvis AI assistant. Give short useful answers."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        print("AI ERROR:", e)
        return None


# =========================
# 🧠 MAIN PROCESS
# =========================
def process(command: str):

    if not command:
        return

    command = command.lower().strip()
    print("DEBUG:", command)

    # =====================
    # EXIT
    # =====================
    if any(x in command for x in ["exit", "quit", "shutdown", "goodbye"]):
        return handle_exit()

    # =====================
    # MUSIC
    # =====================
    if any(x in command for x in ["play music", "play song", "song", "music"]):
        handle_music()
        return

    # =====================
    # WEATHER
    # =====================
    if "weather" in command:
        handle_weather()
        return

    # =====================
    # GOOGLE
    # =====================
    if "google" in command:
        handle_google()
        return

    # =====================
    # YOUTUBE
    # =====================
    if "youtube" in command:
        handle_youtube()
        return

    # =====================
    # CHATGPT
    # =====================
    if "chatgpt" in command or "open ai" in command:
        handle_chatgpt()
        return

    # =====================
    # TIME
    # =====================
    if "time" in command:
        handle_time()
        return

    # =====================
    # JOKE
    # =====================
    if "joke" in command:
        handle_joke()
        return

    # =====================
    # COIN
    # =====================
    if "coin" in command or "toss" in command:
        handle_coin()
        return

    # =====================
    # DICE
    # =====================
    if "dice" in command:
        handle_dice()
        return

    # =====================
    # 🤖 AI FALLBACK (SAFE)
    # =====================
    response = get_ai_response(command)

    if response is None:
        response = "I did not understand"

    print("AI RESPONSE:", response)
    print("SPEAK FUNCTION CALLED")

    speak(response)
    set_status(f"JARVIS: {response}")

    return response