import threading

from voice.speak import speak
from voice.listen import listen

from core.brain import process

from gui.dashboard import run_gui, set_status


# =========================
# 🤖 JARVIS LOOP
# =========================
def jarvis_loop(stop_event: threading.Event):

    startup_message = (
        "Jarvis online all systems activate, Iam ready for performing the  operation, Welcome back Boss "
          
    )

    speak(startup_message)
    set_status(startup_message)

    while not stop_event.is_set():

        # =====================
        # 🎤 LISTENING
        # =====================
        set_status("Listening")

        command = listen()

        if not command:
            continue

        # =====================
        # ⚙ PROCESSING
        # =====================
        set_status("Processing")

        # Brain handles everything
        result = process(command)

        # =====================
        # 💀 EXIT
        # =====================
        if result == "EXIT":

            set_status("JARVIS QUIT")

            stop_event.set()

            break

        # =====================
        # 💤 IDLE
        # =====================
        set_status("Idle")


# =========================
# 🚀 MAIN
# =========================
def main():

    stop_event = threading.Event()

    jarvis_thread = threading.Thread(
        target=jarvis_loop,
        args=(stop_event,),
        daemon=True
    )

    jarvis_thread.start()

    # GUI MUST RUN IN MAIN THREAD
    run_gui()

    # Cleanup
    stop_event.set()

    jarvis_thread.join(timeout=2)


if __name__ == "__main__":
    main()