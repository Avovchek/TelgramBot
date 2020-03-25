import os
import dotenv


class Config:
    MODE = os.getenv('debug')
    BOT_TOKEN = os.getenv('853007726:AAG1ws8cmSnzv-de5LQoaw9h8UDP_W5CcDU')
    UTL = os.getenv('HEROKU_URL')

def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name

    text = """Hello, {0}

    This is the starter template for other bots built with <b>python</b>. 

    No bots cooked so far.

    Enjoy cooking with <a href = 'https://github.com/VadimCpp/pyfirstbotbot'>this template</a>!""".format(first_name)

    return text

