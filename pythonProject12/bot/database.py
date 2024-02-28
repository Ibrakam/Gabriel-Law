import sqlite3
from datetime import datetime

conn = sqlite3.connect('telegram_bot.db')  # Создание файла базы данных
cursor = conn.cursor()  # Создание объекта курсора

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    tg_id,
    name TEXT,
    language TEXT,
    phone_number TEXT,
    time TEXT
)""")


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('telegram_bot.db', check_same_thread=False)  # Создание файла базы данных
        self.cursor = self.conn.cursor()  # Создание объекта курсора

    def add_user(self, tg_id, name, language, phone_number):
        with self.conn:
            return self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (tg_id, name, language,
                                                                                    phone_number, datetime.now()))

    def get_all_users(self):
        with self.conn:
            return self.cursor.execute("SELECT * FROM users").fetchall()

    def get_user_name(self, tg_id):
        with self.conn:
            data = self.cursor.execute("SELECT name FROM users WHERE tg_id = ?", (tg_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    def get_user_phone_number(self, tg_id):
        with self.conn:
            data = self.cursor.execute("SELECT phone_number FROM users WHERE tg_id = ?", (tg_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    def get_user_language(self, tg_id):
        with self.conn:
            data = self.cursor.execute("SELECT language FROM users WHERE tg_id = ?", (tg_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    def check_user(self, tg_id):
        with self.conn:
            data = self.cursor.execute("SELECT tg_id FROM users WHERE tg_id = ?", (tg_id,)).fetchone()
            if data:
                return True
            else:
                return False

    def update_phone_num(self, tg_id, phone_number):
        with self.conn:
            return self.cursor.execute("UPDATE users SET phone_number = ? WHERE tg_id = ?", (phone_number, tg_id))