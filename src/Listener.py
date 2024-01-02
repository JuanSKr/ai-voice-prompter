import speech_recognition as sr
import Prompter

class Listener:
    LISTENING_KEYWORD = "echo"
    USER_LANGUAGE = "en"

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio = None
        self.text = None

    def voicePrompter(self):
        while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    self.audio = self.recognizer.listen(mic)
                    self.text = self.recognizer.recognize_google(self.audio, language=self.USER_LANGUAGE)
                    self.text = self.text.lower()

                    if self.text == self.LISTENING_KEYWORD:
                        print("Listening...")
                        is_listening = True
                        while is_listening:
                            self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                            prompt_audio = self.recognizer.listen(mic)
                            prompt_text = self.recognizer.recognize_google(
                                prompt_audio, language=self.USER_LANGUAGE
                            )
                            prompt_text = prompt_text.lower()
                            is_listening = False
                            print(prompt_text)
                            Prompter.prompter(prompt_text)

            except sr.UnknownValueError:
                print("An error occurred while recognizing the speech. Please try again.")
                continue
