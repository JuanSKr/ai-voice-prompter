from hugchat import hugchat
from hugchat.login import Login
import Config as acc


def prompter(voice_prompt):
    sign = Login(acc.HUG_MAIL, acc.HUG_PASS)
    cookies = sign.login()

    cookies_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookies_path_dir)

    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    print("Starting prompter...")

    query_result = chatbot.query(voice_prompt, web_search=True)
    print(query_result)
