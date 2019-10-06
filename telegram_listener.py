import telebot
import os
import sys
import time

from const import TELEGRAM_TOKEN, TELEGRAM_COMMANDS, TELEGRAM_BACK, PAYMENT_CRED, RESPONSES, RU_LANGUAGE_SET
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

MENU_KEYBOARD = {"en":build_reply_keyboard(TELEGRAM_COMMANDS["en"]), "ru":build_reply_keyboard(TELEGRAM_COMMANDS["ru"])} #main menu keyboard

@bot.message_handler(commands=["start"])
def start(msg):
    print(msg.from_user.language_code)
    msg = language_set(msg)
    print(msg.from_user.language_code)
    bot.send_message(msg.chat.id, RESPONSES[msg.from_user.language_code]["welcome"], reply_markup=MENU_KEYBOARD[msg.from_user.language_code])

#TELEGRAM_COMMANDS Cheatsheet
#0 - /find - Find by image 🖼️
#1 - /buy - Buy premium 💳

@bot.message_handler(content_types=["text"])
def main_handler(msg):
    print(msg.from_user.language_code)
    msg = language_set(msg)
    if msg.text in TELEGRAM_COMMANDS[msg.from_user.language_code]:
        if msg.text == TELEGRAM_COMMANDS[msg.from_user.language_code][0]: # /find command
            if check_for_premium(msg):
                kb = build_reply_keyboard(TELEGRAM_BACK[msg.from_user.language_code])
                send = bot.send_message(msg.chat.id, RESPONSES[msg.from_user.language_code]["find"], reply_markup=kb)
                bot.register_next_step_handler(send, get_image)
        elif msg.text == TELEGRAM_COMMANDS[msg.from_user.language_code][1]: # /buy command
            pass

def get_image(msg): #second step of /find command
    msg = language_set(msg)
    if msg.text in TELEGRAM_BACK[msg.from_user.language_code]:
        bot.send_message(msg.chat.id, RESPONSES[msg.from_user.language_code]["return_back"], reply_markup=MENU_KEYBOARD[msg.from_user.language_code])
    if msg.photo:
        print(msg.photo)
        bot.send_message(msg.chat.id, RESPONSES[msg.from_user.language_code]["processing"], reply_markup=MENU_KEYBOARD[msg.from_user.language_code])
        photo_cred = bot.get_file(msg.photo[1].file_id)
        picture = "https://api.telegram.org/file/bot{}/{}".format(TELEGRAM_TOKEN, photo_cred.file_path) #url .jpg picture
        quant_faces = pm.find_faces(picture)
        # Face-phrases
        # 0 - No faces
        # 1 - One face
        # 2 - More than one
        if quant_faces == 1:
            bot.send_message(msg.chat.id, RESPONSES[msg.from_user.language_code]["face"][1])
            pm.search_face(picture)
        elif quant_faces == 2:
            bot.send_message(msg.chat.id, RESPONSES[msg.form_user.language_code]["face"][2])
        else:
            bot.send_message(msg.chat.id, RESPONSES[msg.from_user.language_code]["face"][0])

def language_set(msg):
    if msg.from_user.language_code in RU_LANGUAGE_SET:
        msg.from_user.language_code = "ru"
    else:
        msg.from_user.language_code = "en"
    return msg

def check_for_premium(msg):
    user = tg.User(msg.chat.id)
    if user.premium:
        return True
    bot.send_message(msg.chat.id, RESPONSES[msg.from_user.language_code]["no_premium"])
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