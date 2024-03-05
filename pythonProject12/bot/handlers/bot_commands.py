import asyncio
import os

from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import InputFile, WebAppInfo

from bot.markup.keyboards import choose_language, services_kb, ph_num_kb, back_kb, end_chat, languages
from aiogram.fsm.context import FSMContext
from bot.services.States import Form
from bot.database import Database


router = Router()

data = Database()

users = {}

local = 'https://i.postimg.cc/qvfSKq3m/header-Logo-1.png'
print(data.get_all_users())

"""Some functions"""
# Functions


"""Command Handlers"""


# Handlers
@router.message(CommandStart(), F.text)
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if data.check_user(user_id):
        if data.get_user_language(user_id) == 'Eng':
            await message.answer('Hi', reply_markup=languages())
            await message.answer_photo(photo=local, caption='List of services', reply_markup=services_kb(user_id))
        elif data.get_user_language(user_id) == 'Rus':
            await message.answer('Привет', reply_markup=languages())
            await message.answer_photo(photo=local, caption='Список услуг', reply_markup=services_kb(user_id))
        elif data.get_user_language(user_id) == 'Esp':
            await message.answer('Hola', reply_markup=languages())
            await message.answer_photo(photo=local, caption='Lista de servicios', reply_markup=services_kb(user_id))
    else:
        await message.answer_photo(photo=local, caption='''<b>Hello! Welcome to Gabriel Law Insurance Company! 🛡️\nWe are glad to see you here!</b>

<b>Привет! Добро пожаловать в компанию страхования Gabriel Law! 🛡️\nМы рады видеть вас здесь!</b>

<b>¡Hola! ¡Bienvenido a la compañía de seguros Gabriel Law! 🛡️\n¡Nos alegra verte aquí!</b>
    ''', reply_markup=languages(), parse_mode='HTML')
    await state.set_state(Form.waiting_for_lang)


@router.message(Form.menu)
async def main_menu(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if data.get_user_language(user_id) == 'Eng':
        await message.answer('List of services', reply_markup=services_kb(user_id))
    elif data.get_user_language(user_id) == 'Rus':
        await message.answer('Список услуг', reply_markup=services_kb(user_id))
    elif data.get_user_language(user_id) == 'Esp':
        await message.answer('Lista de servicios', reply_markup=services_kb(user_id))

@router.message(Form.waiting_for_lang)
async def choose_lang(message: types.Message, state: FSMContext):
    if message.text == '🇺🇸 English':
        users[message.from_user.id] = 'Eng'
        await message.answer('Enter your name')
        await state.set_state(Form.waiting_for_name)
    elif message.text == '🇷🇺 Русский':
        users[message.from_user.id] = 'Rus'
        await message.answer('Введите ваше имя')
        await state.set_state(Form.waiting_for_name)
    elif message.text == '🇪🇸Español':
        users[message.from_user.id] = 'Esp'
        await state.set_state(Form.waiting_for_name)
        await message.answer('Introduzca su nombre')
    else:
        await message.answer('Choose your language')
        await state.set_state(Form.waiting_for_lang)


@router.message(Form.waiting_for_name)
async def get_name(message: types.Message, state: FSMContext):
    if users[message.from_user.id] == 'Eng':
        data.add_user(message.from_user.id, message.text, 'Eng', None)
        await message.answer(photo=local, caption='List of services', reply_markup=services_kb(message.from_user.id))
        print(data.get_all_users())
    elif users[message.from_user.id] == 'Rus':
        data.add_user(message.from_user.id, message.text, 'Rus', None)
        await message.answer_photo(photo=local, caption='Список услуг', reply_markup=services_kb(message.from_user.id))
    elif users[message.from_user.id] == 'Esp':
        data.add_user(message.from_user.id, message.text, 'Esp', None)
        await message.answer_photo(photo=local, caption='Lista de servicios',
                                   reply_markup=services_kb(message.from_user.id))
    users.clear()


@router.callback_query(F.data.in_(['consulting', 'qwer', 'back', 'back1']))
async def call_services(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    if call.data == 'consulting':
        if data.get_user_language(user_id) == 'Eng':
            await call.message.answer('Please send your phone number', reply_markup=ph_num_kb(user_id))
        elif data.get_user_language(user_id) == 'Rus':
            await call.message.answer('Пожалуйста отправтье свой номер', reply_markup=ph_num_kb(user_id))
        elif data.get_user_language(user_id) == 'Esp':
            await call.message.answer('Por favor enviar su numero', reply_markup=ph_num_kb(user_id))
        await state.set_state(Form.waiting_for_phone)
    elif call.data == 'qwer':
        await call.message.edit_caption(caption='Some service', reply_markup=back_kb(user_id))
    elif call.data == 'back':
        if data.get_user_language(user_id) == 'Eng':
            await call.message.edit_caption(caption='List of services', reply_markup=services_kb(user_id))
        elif data.get_user_language(user_id) == 'Rus':
            await call.message.edit_caption(caption='Список услуг', reply_markup=services_kb(user_id))
        elif data.get_user_language(user_id) == 'Esp':
            await call.message.edit_caption(caption='Lista de servicios', reply_markup=services_kb(user_id))
    elif call.data == 'back1':
        if data.get_user_language(user_id) == 'Eng':
            await call.message.answer_photo(photo=local, caption='List of services', reply_markup=services_kb(user_id))
        elif data.get_user_language(user_id) == 'Rus':
            await call.message.answer_photo(photo=local, caption='Список услуг', reply_markup=services_kb(user_id))
        elif data.get_user_language(user_id) == 'Esp':
            await call.message.answer_photo(photo=local, caption='Lista de servicios', reply_markup=services_kb(user_id))


@router.message(Form.waiting_for_phone)
async def get_phone(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    ph = message.contact.phone_number
    print(ph)
    data.update_phone_num(message.from_user.id, ph)
    await message.answer('Type your incident here…', reply_markup=end_chat(user_id))
    await state.set_state(Form.dialog)

    # await message.answer('List of services', reply_markup=services_kb())


@router.message(Form.dialog)
async def get_text(message: types.Message, state: FSMContext):
    reply = None
    await message.bot.send_message(chat_id=583411442, text=f'''<b>New message 🛎️

Client name:</b> {data.get_user_name(message.from_user.id)}
<b>Client phone number:</b> {data.get_user_phone_number(message.from_user.id)}

<b>Client’s question:</b>{message.text}''', reply_to_message_id=reply, parse_mode='HTML')
    await message.bot.send_message(chat_id=570250712, text=f'''<b>New message 🛎️

Client name:</b> {data.get_user_name(message.from_user.id)}
<b>Client phone number:</b> {data.get_user_phone_number(message.from_user.id)}

<b>Client’s question:</b>{message.text}''', reply_to_message_id=reply, parse_mode='HTML')
    await message.answer('Ваше сообщение передано специалисту, скоро с вами свяжемся')
    await message.bot.send_message(chat_id=889121031, text=f'''<b>New message 🛎️

Client name:</b> {data.get_user_name(message.from_user.id)}
<b>Client phone number:</b> {data.get_user_phone_number(message.from_user.id)}

<b>Client’s question:</b>{message.text}''', reply_to_message_id=reply, parse_mode='HTML')
    await message.answer('Ваше сообщение передано специалисту, скоро с вами свяжемся')
    user_id = message.from_user.id
    if data.get_user_language(user_id) == 'Eng':
        await message.answer_photo(photo=local, caption='List of services', reply_markup=services_kb(user_id))
    elif data.get_user_language(user_id) == 'Rus':
        await message.answer_photo(photo=local, caption='Список услуг', reply_markup=services_kb(user_id))
    elif data.get_user_language(user_id) == 'Esp':
        await message.answer_photo(photo=local, caption='Lista de servicios', reply_markup=services_kb(user_id))