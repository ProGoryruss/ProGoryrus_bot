import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")
USER_ID = 1776837741
GROUP_CHAT_ID = -1398353005

bot = telebot.TeleBot(TOKEN)

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("📦 Прокат снаряжения", "🏕 Активные туры")

equipment_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
equipment_menu.row("🎿 Лыжи", "🧗 Альпинизм")
equipment_menu.row("🔙 Назад в меню")

tours_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
tours_menu.row("🚶 Походы", "🛶 Рафтинг")
tours_menu.row("🔙 Назад в меню")

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Привет! 👋\nВыбери интересующий раздел:", reply_markup=main_menu)

@bot.message_handler(func=lambda msg: msg.text == "📦 Прокат снаряжения")
def show_equipment(msg):
    bot.send_message(msg.chat.id, "Выбери категорию снаряжения:", reply_markup=equipment_menu)

@bot.message_handler(func=lambda msg: msg.text == "🏕 Активные туры")
def show_tours(msg):
    bot.send_message(msg.chat.id, "Выбери активность:", reply_markup=tours_menu)

@bot.message_handler(func=lambda msg: msg.text == "🔙 Назад в меню")
def back_to_menu(msg):
    bot.send_message(msg.chat.id, "Главное меню:", reply_markup=main_menu)

@bot.message_handler(func=lambda msg: msg.text in ["🎿 Лыжи", "🧗 Альпинизм", "🚶 Походы", "🛶 Рафтинг"])
def handle_category(msg):
    category = msg.text
    bot.send_message(msg.chat.id, f"Пожалуйста, отправьте свою заявку на '{category}'.\nНапишите ФИО, даты и телефон:")

    bot.register_next_step_handler(msg, lambda m: process_application(m, category))

def process_application(msg, category):
    application_text = f"📩 Новая заявка на {category}\n\n👤 {msg.from_user.full_name}\n📝 {msg.text}"
    bot.send_message(USER_ID, application_text)
    bot.send_message(GROUP_CHAT_ID, application_text)
    bot.send_message(msg.chat.id, "Спасибо! Ваша заявка отправлена. ✅", reply_markup=main_menu)

bot.polling()
