from aiogram import types, Dispatcher
from config import ADMIN_ID, GROUP_CHAT_ID
from keyboards import main_menu, gear_menu, tour_menu

async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот компании ПРО ГОРЫ ⛰️", reply_markup=main_menu)

async def menu_handler(message: types.Message):
    if message.text == "Прокат снаряжения":
        await message.answer("Выберите категорию снаряжения:", reply_markup=gear_menu)
    elif message.text == "Активные туры":
        await message.answer("Выберите тип тура:", reply_markup=tour_menu)
    elif message.text.startswith("⬅"):
        await message.answer("Главное меню", reply_markup=main_menu)
    else:
        await message.answer("Спасибо! Ваша заявка принята.")
        text = f"📩 Новая заявка от @{message.from_user.username or message.from_user.full_name}:
{message.text}"
        await message.bot.send_message(ADMIN_ID, text)
        await message.bot.send_message(GROUP_CHAT_ID, text)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(menu_handler)
