import speech_recognition as sr
import time

keep_listen = True


def startToListen():
    global keep_listen

    recognizer = sr.Recognizer()

    while keep_listen:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language="es")
                text = text.lower()

                if text == "prueba":
                    print("Listening...")
                    transcript()
        except sr.UnknownValueError:
            continue


def transcript():
    global keep_listen

    recognizer = sr.Recognizer()
    inactivity_timeout = 5
    last_audio_time = time.time()

    while keep_listen:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)

            try:
                audio = recognizer.listen(
                    mic,
                    timeout=inactivity_timeout,
                    phrase_time_limit=inactivity_timeout,
                )
                text = recognizer.recognize_google(audio, language="es")
                text = text.lower()
                print(f"Voice: {text}")

                last_audio_time = time.time()
            except sr.UnknownValueError:
                if time.time() - last_audio_time >= inactivity_timeout:
                    print("Listening has been stopped for inactivity.")
                    keep_listen = False


startToListen()
