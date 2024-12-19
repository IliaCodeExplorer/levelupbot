from aiogram import types
from aiogram.dispatcher import Dispatcher

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["start"])
    async def start_command(message: types.Message):
        await message.answer("Привет! Я ваш образовательный бот. Напишите /help, чтобы узнать больше.")

    @dp.message_handler(commands=["help"])
    async def help_command(message: types.Message):
        await message.answer("Список доступных команд:\n/start - Начало работы\n/help - Помощь")
