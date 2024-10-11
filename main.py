import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

logger = logging.getLogger(__name__)  # инициализируем логгер


# функция конфигурирования и запуска бота
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')  # информацию о начале запуска бота

    config: Config = load_config()  # загружаем конфиг в переменную config

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()  # инициализируем диспетчер

    # регистриуем роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # пропуск апдейтов и запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())