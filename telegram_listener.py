import telebot
import os
import sys
import time

from const import TELEGRAM_TOKEN, TELEGRAM_COMMANDS, TELEGRAM_BACK, PAYMENT_CRED
from telebot import types

import module.telegram as tg
import module.picture_manager as pm

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def build_reply_keyboard(kb_texts:list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #Keyboard object creation
    buttons = []
    for kb_text in kb_texts:
        buttons.append(types.KeyboardButton(text=kb_text)) #Button objects creation
    keyboard.add(*buttons) #Adding buttons in keyboard
    return keyboard

MENU_KEYBOARD = build_reply_keyboard(TELEGRAM_COMMANDS) #main menu keyboard

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Welcoming text", reply_markup=MENU_KEYBOARD)

#TELEGRAM_COMMANDS Cheatsheet
#0 - /find - Find by image 🖼️
#1 - /buy - Buy premium 💳

@bot.message_handler(content_types=["text"])
def main_handler(msg):
    if msg.text in TELEGRAM_COMMANDS:
        if msg.text == TELEGRAM_COMMANDS[0]: # /find command
            if check_for_premium(msg):
                kb = build_reply_keyboard(TELEGRAM_BACK)
                send = bot.send_message(msg.chat.id, "Send me a photo of the person, which you want to find", reply_markup=kb)
                bot.register_next_step_handler(send, get_image)
        elif msg.text == TELEGRAM_COMMANDS[1]: # /buy command
            pass

def get_image(msg): #second step of /find command
    if msg.text in TELEGRAM_BACK:
        bot.send_message(msg.chat.id, "Returning back to menu", reply_markup=MENU_KEYBOARD)
    if msg.photo:
        print(msg.photo)
        bot.send_message(msg.chat.id, "Processing your image", reply_markup=MENU_KEYBOARD)

def check_for_premium(msg):
    user = tg.User(msg.chat.id)
    if user.premium:
        return True
    bot.send_message(msg.chat.id, "Sorry, but you get the limit for requests per month\nYou can buy more requests via Buy premium 💳 button!")
    return False

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