import speech_recognition as sr
import Prompter


class Listener:
    def __init__(self):
        pass

    def voicePrompter(self):
        recognizer = sr.Recognizer()
        user_language = "en"
        listening_keyword = "echo"

        while True:
            try:
                with sr.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)
                    text = recognizer.recognize_google(audio, language=user_language)
                    text = text.lower()

                    if text == listening_keyword:
                        print("Listening...")
                        arx = True
                        while arx:
                            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                            prompt_audio = recognizer.listen(mic)
                            prompt_text = recognizer.recognize_google(
                                prompt_audio, language=user_language
                            )
                            prompt_text = prompt_text.lower()
                            arx = False
                            print(prompt_text)
                            Prompter.prompter(prompt_text)

            except sr.UnknownValueError:
                continue
