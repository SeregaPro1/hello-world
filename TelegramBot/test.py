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

bot = Bot(token='6387525467:AAHnuNG4cQcYABM-BzsJUzJ0hzmIp-i2Pek')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MyStates(StatesGroup):  # создание state для работы с пользователем через aiogram
    STARTED = State()
    NAME = State()
    AGE = State()
    QUESTION = State()
    CHAT = State()
    YTLINK = State()


# Создание объекта CallbackData для обработки данных коллбэка
callback = callback_data.CallbackData("button", "action")


# Функция, которая будет вызываться при нажатии на кнопку "Функция 1"
async def function1_callback(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Введите запрос")
    await MyStates.QUESTION.set()


@dp.message_handler(state=MyStates.QUESTION)
async def process_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text
    for i in search(f"{data['question']}", tld='co.in', num=10, stop=10, pause=2):
        await message.reply(i)

# Функция, которая будет вызываться при нажатии на кнопку "Функция 2"
async def function2_callback(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Вы выбрали функцию 2!")


# Обработчики коллбэков
@dp.callback_query_handler(callback.filter(action="function1"))
async def process_function1_callback(callback_query: types.CallbackQuery):
    await function1_callback(callback_query)


@dp.callback_query_handler(callback.filter(action="function2"))
async def process_function2_callback(callback_query: types.CallbackQuery):
    await function2_callback(callback_query)


# Обработчик команды для инициализации меню с кнопками
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Функция 1", callback_data=callback.new(action="function1"))
    button2 = InlineKeyboardButton(text="Функция 2", callback_data=callback.new(action="function2"))
    keyboard.row(button1, button2)
    await message.answer("Выберите функцию:", reply_markup=keyboard)

# Регистрируем обработчик команды /start
dp.register_message_handler(start_command, commands=['start'])

# Запускаем бота

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
