import telebot

TOKEN = '5146009144:AAHbCToCum5a34ap9weGSJTqBlZCSI8Fr_4'

bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True)