#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6659889999:AAG0lh0iCAadzKB9dsHMh4G9D-7Wz_ZZZXs'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('privet-kartinki-27.jpg', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🔑 Мой github.com")
	item2 = types.KeyboardButton("✉️ Мой телеграм")
	item3 = types.KeyboardButton("🗣 Страница в ВК")
	item4 = types.KeyboardButton("🐻 Погладить мишку")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Пушистый привет тебе мой друг, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🔑 Мой github.com':
			bot.send_message(message.chat.id, 'https://github.com/AdelNuriev-qa')
		elif message.text == '✉️ Мой телеграм':
			bot.send_message(message.chat.id, 'https://t.me/adel_nuriev')
		elif message.text == '🗣 Страница в ВК':
			bot.send_message(message.chat.id, 'https://vk.com/id416704353')
		elif message.text == '🐻 Погладить мишку':
			bot.send_message(message.chat.id, 'https://cs8.pikabu.ru/post_img/big/2016/02/20/6/1455956176173244043.jpg')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😥')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
