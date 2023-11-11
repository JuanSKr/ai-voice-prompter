from hugchat import hugchat
from hugchat.login import Login
import Config as acc

class Prompter:
    def __init__(self):
        self.sign = Login(acc.HUG_MAIL, acc.HUG_PASS)
        self.cookies = None
        self.cookies_path_dir = "../cookies_snapshot"
        self.chatbot = None
        self.query_result = None

    def prompter(self, voice_prompt):
        self.cookies = self.sign.login()
        self.sign.saveCookiesToDir(self.cookies_path_dir)
        self.chatbot = hugchat.ChatBot(cookies=self.cookies.get_dict())
        print("Starting prompter...")
        self.query_result = self.chatbot.query(voice_prompt, web_search=True)
        print(self.query_result)