from aiogram import Bot, Dispatcher, executor, types
import logging
import config
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# уровень логов
logging.basicConfig(level=logging.INFO)

# инициализация ботов
bot = Bot(token=config.token)
dp = Dispatcher(bot)

#buttons


menu_bt=KeyboardButton('/Меню')
button_menu=ReplyKeyboardMarkup(resize_keyboard=True)
button_menu.add(menu_bt)

doner_1=KeyboardButton('порция')
doner_2=KeyboardButton('средний')
doner_3=KeyboardButton('большой')
doner_menu=ReplyKeyboardMarkup(resize_keyboard=True)
doner_menu.add(doner_1).add(doner_2).insert(doner_3)

# приветствие
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):  # приветствие и кнопка сделать заказ
    await message.reply(
        "Добро пожаловать!!!\nВ Дон Ридо КАРАГАНДА\nХалал-Кафе быстрого питания\nНевозможно отказаться\n🍴Сеть кафе🖖🏽4 точки в городе\n🛵Доставка с 10:00 до 22:00",
        reply_markup=button_menu
    )

@dp.message_handler(commands=['Меню'])
async def menu(message: types.Message):
    await message.reply(reply_markup=doner_menu)


# long polling
if __name__ == '__main__':
    executor.start_polling(dp)
