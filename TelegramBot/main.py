from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor, callback_data
import sqlite3
from googlesearch import search
import openai
from pytube import YouTube


def create_db():  # создание и подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT NOT NULL,
                       chat_id INTEGER NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS query_history
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       query TEXT NOT NULL,
                       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()


def add_user(username, chat_id):  # добавление username and user_id в базу данных

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? OR chat_id=?", (username, chat_id))
    existing_user = cursor.fetchone()

    if existing_user is None:
        cursor.execute("INSERT INTO users (username, chat_id) VALUES (?, ?)", (username, chat_id))
        conn.commit()

    conn.commit()
    conn.close()


def add_query_to_history(query):  # добавление истории запросов в базу данных

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO query_history (query) VALUES (?)", (query,))
    conn.commit()


# openai.api_key = "sk-95Ez2Z1rtgegrRTFFDSTVTdsdfsgdv3422kjhLghnh53QiT8F"


class MyStates(StatesGroup):  # создание state для работы с пользователем через aiogram
    STARTED = State()
    NAME = State()
    AGE = State()
    QUESTION = State()
    CHAT = State()
    YTLINK = State()


bot = Bot(token='6387525467:AAHnuNG4cQcYABM-BzsJUzJ0hzmIp-i2Pek')  # подключение к Телеграм боту
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
callback = callback_data.CallbackData("button", "action")


@dp.message_handler(Command('start'))  # создание команды /start
async def cmd_start(message: types.Message):  # функция start
    username = message.from_user.username
    chat_id = message.chat.id
    add_user(username, chat_id)

    await message.reply("Привет! Я RinerGPT bot. Как тебя зовут?")  # выводит собщение пользователю
    await MyStates.NAME.set()  # input in aiogram


@dp.message_handler(state=MyStates.NAME)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data: # обработка input в память
        data['name'] = message.text
    await message.reply('Сколько тебе лет?')
    await MyStates.AGE.set()


@dp.message_handler(state=MyStates.AGE)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await state.finish()
    await message.reply(f"Приятно познакомиться, {data['name']}! Тебе {data['age']} лет.")


@dp.message_handler(Command('download'))
async def cmd_download(message: types.Message):
    await message.reply('Вставьте сслыку')
    await MyStates.YTLINK.set()


@dp.message_handler(state=MyStates.YTLINK)
async def process_download(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['download'] = message
    yt = YouTube(f"{data['download']}")
    ys = yt.streams.get_highest_resolution()
    await message.reply('Downloading...')
    ys.download("Downloads\\")
    await message.reply('Downloading completed!')


@dp.message_handler(Command('search'))
async def cmd_search(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Введите запрос")
    await MyStates.QUESTION.set()


@dp.message_handler(state=MyStates.QUESTION)
async def process_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text

        query = f"{data['question']}"  # добавление запроса в базу данных
        add_query_to_history(query)

    for i in search(f"{data['question']}", tld='co.in', num=10, stop=10, pause=2):
        await message.reply(i)


# Обработка коллбэков
@dp.callback_query_handler(callback.filter(action="search"))
async def process_function1_callback(callback_query: types.CallbackQuery):
    await cmd_search(callback_query)


# @dp.message_handler(Command('chatgpt'))
# async def cmd_chatgpt(message: types.Message):
#     await message.reply('Начните диалог')
#
#
# @dp.message_handler(state=MyStates.CHAT)
# async def process_chat(messege: types.Message, state: FSMContext):
#     while True:
#         await MyStates.CHAT.set()
#         async with state.proxy() as data:
#             data['chat'] = messege.text
#         message = ("User: " + data['chat'])
#         if message == 'quit':
#             break
#         chat = openai.ChatCompletion.create(model='gpt-3.5-turbo')
#         reply = chat.choices.message.content
#         await messege.reply(f"ChatGPT: {reply}")


@dp.message_handler(Command('menu'))
async def cmd_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Поиск", callback_data=callback.new(action="search"))
    button2 = InlineKeyboardButton(text="Функция 2", callback_data=callback.new(action="function2"))
    keyboard.row(button1, button2)
    await message.answer("Выберите функцию:", reply_markup=keyboard)


if __name__ == '__main__':  # запуск бота
    create_db()

    executor.start_polling(dp, skip_updates=True)