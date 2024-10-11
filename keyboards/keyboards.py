from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder  # клавиатура с использованием билдера

from lexicon.lexicon_ru import LEXICON_RU

button_city = KeyboardButton(text=LEXICON_RU['city_button'])  # кнопка для ввода города пользователя

kb_builder = ReplyKeyboardBuilder()  # инициализируем билдер для кнопки button_city

kb_builder.row(button_city, width=2)  # добавляем кнопки в билдер с аргументом width=2

# создаем клавиатуру с кнопкой 'Введите город'
# будем сворачивать кнопку после нажатия на нее
kb: ReplyKeyboardMarkup = kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)
