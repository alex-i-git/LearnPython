#!/usr/bin/python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)
    
def main():
    
    updater = Updater("API_KEY")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()