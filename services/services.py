import requests

from config_data.config import Config, load_config


def get_weather(city):
    config: Config = load_config()
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': config.tg_bot.weather_api,
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()

    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']

    return f"{city} - {weather}\nТемпература - {temperature}°C\nВлажность - {humidity}%"

