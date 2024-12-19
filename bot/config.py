import os
from dotenv import load_dotenv

# Загрузка переменных из файла .env
load_dotenv()

# Получение токена бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка наличия токена
if not BOT_TOKEN:
    raise ValueError("Токен Telegram бота не найден! Убедитесь, что он указан в файле .env")
