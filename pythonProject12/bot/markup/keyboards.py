from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from bot.database import Database

db = Database()

web = WebAppInfo(url='https://gabriellegal.com/results/')


def choose_language():
    kb = [[KeyboardButton(text="🇺🇸 English"),
           KeyboardButton(text="🇷🇺 Русский"),
           KeyboardButton(text="🇪🇸Español"), ]]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard


def languages():
    kb = [
        [KeyboardButton(text="🇺🇸 English"),
         KeyboardButton(text="🇷🇺 Русский"),
         KeyboardButton(text="🇪🇸 Español")],
        [KeyboardButton(text="🇺🇿 O'zbekcha"),  # Узбекский
         KeyboardButton(text="🇺🇦 Українська"),  # Украинский
         KeyboardButton(text="🇰🇿 Қазақ")],  # Казахский],
         [KeyboardButton(text="🇰🇬 Кыргызча"),  # Киргизский
          KeyboardButton(text="🇹🇯 Тоҷикӣ"),  # Таджикский
          KeyboardButton(text="🇦🇲 Հայերեն")],  # Армянский],
          [KeyboardButton(text="🇬🇪 ქართული"),  # Грузинский
           KeyboardButton(text="🇧🇾 Беларуская"),  # Белорусский
           KeyboardButton(text="🇦🇿 Azərbaycanca"),  # Азербайджанский
           ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard

def services_kb(tg_id):
    button_rus = [

            [InlineKeyboardButton(text="Связь с юристом \U0001F464", callback_data="qwer")],
            [InlineKeyboardButton(text="Обратиться за помощью \U0001F917", callback_data="qwer")],
            [InlineKeyboardButton(text="Задать вопрос \U0001F914", callback_data="consulting")],
            [InlineKeyboardButton(text="Перейти на сайт \U0001F4BB", callback_data="qwer")],
            [InlineKeyboardButton(text="Результаты \U0001F4CA", web_app=web)],
            [InlineKeyboardButton(text="Область, которую мы ведем \U0001F4DD", callback_data="qwer")],
            [InlineKeyboardButton(text="Наши контакты \U0001F4DE", callback_data="qwer")]

    ]
    button_esp = [
        [InlineKeyboardButton(text="Contactar con un abogado \U0001F464", callback_data="qwer")],
        [InlineKeyboardButton(text="Pedir ayuda \U0001F917", callback_data="qwer")],
        [InlineKeyboardButton(text="Hacer una pregunta \U0001F914", callback_data="consulting")],
        [InlineKeyboardButton(text="Ir al sitio web \U0001F4BB", callback_data="qwer")],
        [InlineKeyboardButton(text="Resultados \U0001F4CA", web_app=web)],
        [InlineKeyboardButton(text="Nuestras áreas de práctica \U0001F4DD", callback_data="qwer")],
        [InlineKeyboardButton(text="Nuestros contactos \U0001F4DE", callback_data="qwer")]

    ]
    button = [
        [InlineKeyboardButton(text="Contact a lawyer \U0001F464", callback_data="qwer")],
        [InlineKeyboardButton(text="Ask for help \U0001F917", callback_data="qwer")],
        [InlineKeyboardButton(text="Ask a question \U0001F914", callback_data="consulting")],
        [InlineKeyboardButton(text="Go to website \U0001F4BB", callback_data="qwer")],
        [InlineKeyboardButton(text="Results \U0001F4CA", web_app=web)],
        [InlineKeyboardButton(text="Our practice areas \U0001F4DD", callback_data="qwer")],
        [InlineKeyboardButton(text="Our contacts \U0001F4DE", callback_data="qwer")]
    ]
    if db.get_user_language(tg_id) == 'Eng':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Rus':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button_rus
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Esp':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button_esp
        )
        return keyboard


def ph_num_kb(tg_id):
    button_rus = [[KeyboardButton(text="📲Отправить номер телефона", request_contact=True)]]
    button_esp = [[KeyboardButton(text="📲Enviar número de contacto", request_contact=True)]]
    button = [[KeyboardButton(text="📲Send Phone Number", request_contact=True)]]
    if db.get_user_language(tg_id) == 'Esp':
        keyboard = ReplyKeyboardMarkup(
            keyboard=button_esp,
            resize_keyboard=True
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Rus':
        keyboard = ReplyKeyboardMarkup(
            keyboard=button_rus,
            resize_keyboard=True
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Eng':
        keyboard = ReplyKeyboardMarkup(
            keyboard=button,
            resize_keyboard=True
        )
        return keyboard


def back_kb(tg_id):
    button = [[InlineKeyboardButton(text="◀️Back", callback_data='back')]]
    button_esp = [[InlineKeyboardButton(text="◀️Volver", callback_data='back')]]
    button_rus = [[InlineKeyboardButton(text="◀️Назад", callback_data='back')]]
    if db.get_user_language(tg_id) == 'Esp':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button_esp
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Rus':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button_rus
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Eng':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button
        )
        return keyboard


def end_chat(tg_id):
    button = [[InlineKeyboardButton(text="◀️Back", callback_data='back1')]]
    button_esp = [[InlineKeyboardButton(text="◀️Volver", callback_data='back1')]]
    button_rus = [[InlineKeyboardButton(text="◀️Назад", callback_data='back1')]]
    if db.get_user_language(tg_id) == 'Esp':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button_esp
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Rus':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button_rus
        )
        return keyboard
    elif db.get_user_language(tg_id) == 'Eng':
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=button
        )
        return keyboard