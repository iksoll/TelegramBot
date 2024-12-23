import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

API = '7744640638:AAEl2BL86p8fpjuqk-jQXZI1gCSuy9xC7BI'
bot = Bot(token=API)
dp = Dispatcher()

#выводит сообщение при команде start
@dp.message(Command('start'))
async def echo(message: types.Message):
    await message.answer("привет, я бот ЕКТС")

#ссылка на сайт колледжа
@dp.message(Command('ects'))
async def echo(message: types.Message):
    await message.answer("сайт колледжа")
    await message.answer("https://www.ects.ru/")

#ссылка на страницу изменения в расписании
@dp.message(Command('changes'))
async def echo(message: types.Message):
    await message.answer("изменения в расписании\n")
    await message.answer("https://www.ects.ru/page281.htm")

#повторяет написанный текст
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_start():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(on_start())