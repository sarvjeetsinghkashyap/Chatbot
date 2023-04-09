import openai
import subprocess
import random
import time
import json

""" ANSI color codes """
color = [{   
    "BLACK": "\033[0;30m",
    "RED": "\033[0;31m",
    "GREEN": "\033[0;32m",
    "BROWN": "\033[0;33m",
    "BLUE": "\033[0;34m",
    "PURPLE": "\033[0;35m",
    "CYAN": "\033[0;36m",
    "LIGHT_GRAY": "\033[0;37m",
    "DARK_GRAY": "\033[1;30m",
    "LIGHT_RED": "\033[1;31m",
    "LIGHT_GREEN": "\033[1;32m",
    "YELLOW": "\033[1;33m",
    "LIGHT_BLUE": "\033[1;34m",
    "LIGHT_PURPLE": "\033[1;35m",
    "LIGHT_CYAN": "\033[1;36m",
    "LIGHT_WHITE": "\033[1;37m",
    "BOLD": "\033[1m",
    "FAINT": "\033[2m",
    "ITALIC": "\033[3m",
    "UNDERLINE": "\033[4m",
    "BLINK": "\033[5m",
    "NEGATIVE": "\033[7m",
    "CROSSED": "\033[9m",
    "END": "\033[0m"
}]

subprocess.call('cls', shell=True)

openai.api_key = open("api", "r").read().strip("\n")
with open('user.json', 'r') as f:
    botconfig = json.load(f)
user = botconfig['user']

message_history = [{"role": "user", "content": "i'm giving you a name '" + botconfig['BotName'] + "', he is my " + botconfig['Bot'] + ", he is " + botconfig['BotNature'] + ", he start every conversation " + botconfig['ConStart'] + " and he correct spelling mistakes in a very funny way, Now act like him and answer all my queries in " + botconfig['BotNature'] + " way, by the way i'm " + botconfig['user'] + "and i am a " + botconfig['gender'] + " remember he calls me " + botconfig['sname'] + ", also he ask my profit in stock market everytime"}]

def chat(inp, role="user"):
    message_history.append({"role": role, "content": inp})
    
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=message_history,
    )
    
    reply_content = completion.choices[0].message.content
    # print(reply_content)
    message_history.append({"role": "assistant", "content": reply_content})
    if reply_content.startswith("Sarvjeet: "):
        # Remove "ChatGPT: " from the beginning of the response string
        reply_content = reply_content[len("Sarvjeet: "):]
    elif reply_content.startswith("ChatGPT: "):
        # Remove "ChatGPT: " from the beginning of the response string
        reply_content = reply_content[len("ChatGPT: "):]
    return reply_content

process_list = ["Hain??", "Kya? Ruk ikmint.", "Yo Sir pate gya","Achha...","Ruk...","Processing...","Ese kamma ma dmag kat chalda...."]
end_list = ["Guun Khale","Bye Kutti.","Bye Surri"]
    
while True:
    # Coloring the code with ANSI Color Codes e.g, \033[1;32m for Green and \033[1;0m for White
    user_input = input(color[0]["GREEN"] + user + " >: " + color[0]["END"])
    
    if 'exit' in user_input:
        print(color[0]["GREEN"] + botconfig['BotSname'] + "   >: " + color[0]["CYAN"] + random.choice(end_list) + color[0]["END"])
        time.sleep(3)
        subprocess.call('cls', shell=True)
        break
    else:
        print()
        print(color[0]["GREEN"] + botconfig['BotSname'] + "   >: " + color[0]["CYAN"] + random.choice(process_list))
        print("          " + chat(user_input))
        print(color[0]["END"])