TELEGRAM_TOKEN = "918331839:AAHw68zMJ6DvQW0120wbiwBPPeoLazI3-qc"
TELEGRAM_COMMANDS = {"en":["/find - Find by image 🖼️", "/buy - Buy premium 💳", "/settings - Settings ⚙️"], 
                    "ru":["/find - Найти по фото 🖼️", "/buy - Купить премиум 💳", "/settings - Настройки ⚙️"]}
TELEGRAM_BACK = {"en": ["Back to main menu 🔙"], 
                "ru": ["Назад в главное меню 🔙"]}
PAYMENT_CRED = ("btk: btkwallet", "paypal: paypalwallet", "wmz: wmzwallet")

RU_LANGUAGE_SET = ["ru", "ru-RU", "ru-BY", "ru-KG", "ru-KG", "ru-KZ", "ru-MD", "ru-UA"]

RESPONSES = {"en": {
                    "welcome": "Hello! I'm Vk Finder, you can find people with me just by the picture!",
                    "find": "Send me a photo of the person, which you want to find.",
                    "return_back": "Returning back to menu...",
                    "processing": "Processing your image!",
                    "face": (
                        "Sorry, but i cant see faces on photo. Please, send another one",
                        "Picture has one face. Perfect!",
                        "Picture has more than one face, please crop it or send another one"),
                    "no_premium": "Sorry, but you get the limit for requests per month\nYou can buy more requests via Buy premium 💳 button!"},
             "ru": {
                    "welcome": "Привет! Я - Vk Finder, со мной ты сможешь найти человека просто по фотографии!",
                    "find": "Отправь мне фотографию человека, которого ты хочешь найти.",
                    "return_back": "Назад в меню...",
                    "processing": "Идёт обработка фотографии!",
                    "face": (
                        "Упс, я не могу найти лицо на фотографии. Пожалуйста, отправь более чёткое изображение",
                        "На фотографии одно лицо, отлично!",
                        "На фотографии больше одного лица, пожалуйста, обрежь её или отправь другую"),
                    "no_premium": "Кажется, лимит по запросам в месяц исчерпан\nТы можешь купить больше запросов с помощью кнопки Купить премиум 💳!"}
            }
