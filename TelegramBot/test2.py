import logging
from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6387525467:AAHnuNG4cQcYABM-BzsJUzJ0hzmIp-i2Pek")
dp = Dispatcher(bot)

# Каталог
mainkey = types.InlineKeyboardMarkup()
key = types.InlineKeyboardButton(text="Приват ", callback_data='vip')
mainkey.row(key)
# вернуться в каталог, покупка
startkey = types.InlineKeyboardMarkup()
back1 = types.InlineKeyboardButton(text="Вернуться назад", callback_data="back")
buy1 = types.InlineKeyboardButton(text="Приобрести доступ 💳", callback_data="buy")
startkey.row(back1, buy1)


@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    await message.answer(f"Приветствую тебя, {message.from_user.username}")
    await message.answer("Чтобы ознакомиться с тарифами, выбери необходимый, нажав на соотвествующую кнопку",
                         reply_markup=mainkey)


@dp.callback_query_handler(lambda c: c.data == 'vip')
async def call_back(call: types.CallbackQuery):
    await call.message.edit_text("Приватка - это канал с частыми обновлениями и тд ", reply_markup=startkey)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)