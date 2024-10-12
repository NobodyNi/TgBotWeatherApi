import requests

from config_data.config import Config, load_config
from lexicon.lexicon_ru import LEXICON_RU


def get_weather(city):
    config: Config = load_config()  # загружаем конфиг
    base_url = 'http://api.openweathermap.org/data/2.5/weather'  # url для запроса к API

    # параметры для запроса
    params = {
        'q': city,
        'appid': config.tg_bot.weather_api,
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get(base_url, params=params)  # отправляет get запрос к API с параметрами

    # если город не найден, API возвращает статус 404
    if response.status_code == 404:
        return f"{LEXICON_RU['no_info']} '{city}'"

    response.raise_for_status()  # если есть ошибки кроме 404, вызывает исключение
    data = response.json()       # словарь с данными о погоде

    temperature = data['main']['temp']           # температура
    weather = data['weather'][0]['description']  # погода
    humidity = data['main']['humidity']          # влажность

    return f"{city} - {weather}\nТемпература - {temperature}°C\nВлажность - {humidity}%"
