# agent/voice_alert.py

def speak(message):
    """
    Voice alerts:
    - Works locally with pyttsx3
    - Disabled on Streamlit Cloud
    """

    try:
        import pyttsx3

        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()

    except Exception:
        # Cloud fallback: just log message
        print(f"[VOICE ALERT DISABLED] {message}")