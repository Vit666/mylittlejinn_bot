from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
	await message.answer("Выберите что-нибудь покушать", reply_markup = menu)

@dp.message_handler(Text(equals = ["Пюрешка", "Котлетки", "Салатик"]))
async def get_food(message: Message):
	await message.answer(f"Вы выбрали {message.text}. Спасибо",
		reply_markup = ReplyKeyboardRemove())
