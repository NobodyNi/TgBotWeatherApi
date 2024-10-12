from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_weather

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message()
async def process_get_weather(message: Message):
    city = message.text
    get_weather_data = get_weather(city)
    await message.answer(get_weather_data)

