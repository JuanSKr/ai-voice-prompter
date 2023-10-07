import speech_recognition
import pyttsx3


def startToListen():
    recognizer = speech_recognition.Recognizer()

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language="es")
                text = text.lower()

                if text == "prueba":
                    print("Listening...")
                    transcript()
        except speech_recognition.UnknownValueError:
            continue


def transcript():
    recognizer = speech_recognition.Recognizer()

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language="es")
                text = text.lower()

                print(f"Voice: {text}")
        except speech_recognition.UnknownValueError:
            continue


startToListen()
