from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
	keyboard = [
	
	[KeyboardButton(text = "Пюрешка")],
	[KeyboardButton(text = "Котлетки")],
	[KeyboardButton(text = "Салатик")] 

	], resize_keyboard = True) 