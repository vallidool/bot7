import os
import aiogram

TOKEN = os.getenv('TOKEN')

bot = aiogram.Bot(TOKEN)
dp = aiogram.Dispatcher(bot)

@dp.message_handler()
async def echo(msg: aiogram.types.Message):
    await msg.answer(msg.text)

if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
