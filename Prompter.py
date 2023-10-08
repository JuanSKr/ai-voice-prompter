from hugchat import hugchat
from hugchat.login import Login
import Config as acc
import Listener as voice

voice_prompt = voice.voiceTest()

sign = Login(acc.HUG_MAIL, acc.HUG_PASS)
cookies = sign.login()

cookies_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookies_path_dir)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

query_result = chatbot.query("Responde en español " + voice_prompt, web_search=True)
answer = query_result
print(query_result)
