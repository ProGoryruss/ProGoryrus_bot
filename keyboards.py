from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Прокат снаряжения"), KeyboardButton("Активные туры"))

gear_menu = ReplyKeyboardMarkup(resize_keyboard=True)
gear_menu.row("Одежда и обувь", "Палатки")
gear_menu.row("Рюкзаки и баулы", "Спальные мешки")
gear_menu.row("Трекинговые палки", "Коврики")
gear_menu.row("Кемпинговая мебель", "Приготовление пищи")
gear_menu.row("Аксессуары", "Велосумки")
gear_menu.add("Альпинистское снаряжение", "⬅ Главное меню")

tour_menu = ReplyKeyboardMarkup(resize_keyboard=True)
tour_menu.row("Однодневный хайкинг", "Походы с ночевкой")
tour_menu.row("Восхождения на вершины", "Виа Феррата и активности на скалах")
tour_menu.row("Спелео туры", "Каньонинг")
tour_menu.row("Автомобильные туры", "Конные прогулки")
tour_menu.add("⬅ Главное меню")
