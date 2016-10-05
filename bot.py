#!/usr/bin/python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Updater - связь с telegram
#CommandHandler - обработчик команд
#MessageHandler - обработчик сообщений
#Filters - фильтрует сообщения, кроме текстовых

def start(bot, update):	# Пишет в консоль о вызове старт в клиенте telegram
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text="Привет, человек! Я бот, который помогает")

def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)
    
def run_bot():
    
    updater = Updater("195034229:AAG8LDc4Q-O0NL991wza6ovbwQKVZ1zT2Rk")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling() # опрашивает telegram на наличие сообщений
    updater.idle()

if __name__ == '__main__':
    run_bot()