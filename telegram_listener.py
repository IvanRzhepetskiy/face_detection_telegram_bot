import telebot
import os
import sys
import time

from const import TELEGRAM_TOKEN, TELEGRAM_COMMANDS
from telebot import types

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])
def start(msg):
    kb = build_reply_keyboard(TELEGRAM_COMMANDS)
    bot.send_message(msg.chat.id, "Welcoming text", reply_markup=kb)

def build_reply_keyboard(kb_texts:list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #Keyboard object creation
    buttons = []
    for kb_text in kb_texts:
        buttons.append(types.KeyboardButton(text=kb_text)) #Button objects creation
    keyboard.add(*buttons) #Adding buttons in keyboard
    return keyboard

def main_loop():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("Exception occurred:", e)
            break
            time.sleep(1)
            os.execv(sys.executable, ['python'] + sys.argv)
            pass
        else:
            break
    while 1:
        time.sleep(2)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print(sys.stderr, '\nExiting by user request.\n')
        sys.exit(0)