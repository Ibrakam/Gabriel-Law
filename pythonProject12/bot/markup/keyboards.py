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


def services_kb(tg_id):
    button_rus = [
        [InlineKeyboardButton(text="🌐О нас", callback_data='qwer'),
         InlineKeyboardButton(text="☎️Контакты", callback_data='qwer')],
        [InlineKeyboardButton(text="🗺Практические области", callback_data='qwer'),
         InlineKeyboardButton(text="🚘ДТП", callback_data='qwer')],
        [InlineKeyboardButton(text="🌎Области, которые мы обслуживаем", callback_data='qwer'),
         InlineKeyboardButton(text="🗂Результаты", web_app=web)],
        [InlineKeyboardButton(text="📝Консультации", callback_data='consulting')],

    ]
    button_esp = [
        [InlineKeyboardButton(text="🌐Nosotros", callback_data='qwer'),
         InlineKeyboardButton(text="☎️Contactos", callback_data='qwer')],
        [InlineKeyboardButton(text="🗺Areas de práctica", callback_data='qwer'),
         InlineKeyboardButton(text="🚘Accidentes de coche", callback_data='qwer')],
        [InlineKeyboardButton(text="🌎Zonas que nos atienden", callback_data='qwer'),
         InlineKeyboardButton(text="🗂Resultados", web_app=web)],
        [InlineKeyboardButton(text="📝Consultas", callback_data='consulting')],
    ]
    button = [
        [InlineKeyboardButton(text="🌐About", callback_data='qwer'),
         InlineKeyboardButton(text="☎️Contacts", callback_data='qwer')
         ],
        [InlineKeyboardButton(text="🗺Practice Areas", callback_data='qwer'),
         InlineKeyboardButton(text="🚘Car Accidents", callback_data='qwer')
         ],
        [InlineKeyboardButton(text="🌎Areas We Serve", callback_data='qwer'),
         InlineKeyboardButton(text="🗂Results", web_app=web)],
        [InlineKeyboardButton(text="📝Consulting", callback_data='consulting')],
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