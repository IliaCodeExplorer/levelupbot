from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import F
import asyncio
from bot.config import BOT_TOKEN

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Привет! Я ваш образовательный бот. Напишите /help, чтобы узнать больше.")

# Обработчик команды /help
@dp.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer("Список доступных команд:\n/start - Начало работы\n/help - Помощь")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
