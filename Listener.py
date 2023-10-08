import speech_recognition as sr
import time
import Prompter

keep_listen = True


def voicePrompter():
    arx: bool

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language="es")
                text = text.lower()

                if text == "prueba":
                    print("Starting arx")
                    print("Listening...")
                    arx = True
                    while arx:
                        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                        prompt_audio = recognizer.listen(mic)
                        prompt_text = recognizer.recognize_google(
                            prompt_audio, language="es"
                        )
                        prompt_text = prompt_text.lower()
                        arx = False
                        print(prompt_text)
                        Prompter.prompter(prompt_text)

        except sr.UnknownValueError:
            continue


voicePrompter()
