from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:          # автоматическое определение специальных методов для TgBot
    token: str        # для доступа к телеграм боту
    weather_api: str  # для доступа к погоде


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:  # будем возвращать объект типа Config
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'), weather_api=env('WEATHER_API_KEY')))