from aiogram import Bot, Dispatcher, executor, types
from rich.logging import RichHandler
from SimpleQIWI import *
import logging
import config
import requests

from openweathermap import Parser_Weather
from database import DataBase
from make_qrcode import QR_Code
from my_qiwi import MY_QIWI
from convert_coin import Coin_Convert

requests.post(f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={str(config.ADMIN_ID)}&text=Welcome!")

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")

db = DataBase("database_users.db")

my_qiwi = MY_QIWI()

cc = Coin_Convert()

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    if message.chat.type == "private":
        bot_FN = await bot.get_me()
        await message.answer(f"Hi {message.from_user.first_name},\n\tMy name\'s {bot_FN.first_name}")

        if db.get_user(user_id = message.from_user.id) == 0:
            db.add_user(message.from_user.id, message.from_user.first_name, message.from_user.username)

        elif db.get_user(user_id = message.from_user.id) == 1:
            pass
    else:
        pass



@dp.message_handler(commands=['weather'])
async def get_weather(message: types.Message):
    city_name = message.text[9:]

    try:
        pw = Parser_Weather()
        await message.answer(pw.get_weather(city_name))
    except:
        if city_name == "":
            await message.answer("/weather <i>город</i>\nНазовите имя города")
        elif city_name != "":
            await message.answer("/weather <i>город</i>\nНазовите имя города правильно!")
        else:
            pass



@dp.message_handler(commands=['qrcode'])
async def get_weather(message: types.Message):
    qr_text = message.text[8:]
    qr_name = f"@{message.from_user.username}---{message.from_user.id}.png"
    QR_Code(qr_text, qr_name)

    photo = open(f"qr_codes\\@{message.from_user.username}---{message.from_user.id}.png", "rb")
    await bot.send_photo(message.chat.id, photo)
    photo.close()



@dp.message_handler(commands=['balance'])
async def get_balance_qiwi(message: types.Message):
    if message.from_user.id == config.ADMIN_ID:
    	if message.chat.type == "private":
    		await message.answer(my_qiwi.get_balance_qiwi())
    	elif message.chat.type != "private":
    		pass  	
    elif message.from_user.id != config.ADMIN_ID:
        pass



@dp.message_handler(commands=["qiwiPay", "qiwi_pay"])
async def QIWI_Pay(message: types.Message):
    Qpay = message.text.split()
    if message.from_user.id == config.ADMIN_ID:
        if message.chat.type == "private":
            try:
                my_qiwi.qiwi_pay(Qpay[1], Qpay[2], Qpay[3])
            except:
                await message.answer("/qiwiPay <i>сумма номерь комментарии</i>")



# @dp.message_handler(commands=["qiwiKey", "qiwi_key"])
# async def QIWI_Pay(message: types.Message):
#     Qbill = message.text.split()
#     if message.from_user.id == config.ADMIN_ID:
#         if message.chat.type == "private":
#             try:
#                 await message.answer(f"<b>KEY: </b><code>{my_qiwi.qiwi_create_key(Qbill[1])}</code>")
#             except:
#                 await message.answer("/qiwiKey <i>сумма</i>")
#             return my_qiwi.qiwi_create_key



# @dp.message_handler(commands=["qiwiBill", "qiwi_bill"])
# async def QIWI_Pay(message: types.Message):
#     if message.from_user.id == config.ADMIN_ID:
#         if message.chat.type == "private":
#             try:
#                 msg = await bot.send_message(message.from_user.id, "🔃Ждем платежа!")
#                 await bot.edit_message_text(chat_id = msg.chat.id, message_id=msg.message_id, text=f"<b>{my_qiwi.qiwi_bill()}</b>")
#             except:
#                 pass



@dp.message_handler(commands=["getCoins", "get_coins"])
async def get_coins(message: types.Message):
    await message.answer(cc.get_coins())



@dp.message_handler(commands=["getUsersDataBase", "get_users_database", "get_user_db"])
async def get_users_db(message: types.Message):
    db.get_users('users.json')

    file = open("users.json", "rb")
    await bot.send_document(message.from_user.id, file, caption="<b>Users DataBase</b>")
    file.close()


@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer(message.text)
    # print(message)
    pass




if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)