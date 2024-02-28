from aiogram.filters.state import State, StatesGroup


class Form(StatesGroup):
    waiting_for_lang = State()
    waiting_for_name = State()
    waiting_for_phone = State()
    dialog = State()
    menu = State()