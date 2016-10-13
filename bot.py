#!/usr/bin/python3

# version 0.1
# Добавляем функцию подсчета слов
# Usage: /wcount word1 word2 ...

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, datetime
import ephem

#Updater - связь с telegram
#CommandHandler - обработчик команд
#MessageHandler - обработчик сообщений
#Filters - фильтрует сообщения, кроме текстовых

def start(bot, update):	# Пишет в консоль о вызове старт в клиенте telegram
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text="Привет, человек! Я бот, который помогает")

def get_answer(user_key,user_dict):
	return user_dict[user_key]	

dialog={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся", 
"добрый день":"здравствуйте"}

def talk_to_me(bot, update):
    #print('Пришло сообщение: %s' % update.message.text)
    user_input = (((update.message.text).lower()).rstrip()).lstrip()
    bot.sendMessage(update.message.chat_id, get_answer(user_input,dialog))
    
def word_count(bot,update,args):
	count = str(len(args))
	bot.sendMessage(update.message.chat_id, "В фразе " + count + " слов")

def division(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		return "Division by zero"
# Функция для арифметических действий с проверкой деления на 0
# Предполагает, что операторов только 2 и все символы разделены пробелом
def calc(bot,update,args):
	if len(args) == 0:
		bot.sendMessage(update.message.chat_id, "Usage: /calc arg1 operation arg2 =")
	
	a = float(args[0])
	b = float(args[2])
	if str(args[1]) == '+':
		c = a+b
	elif str(args[1]) == '-':
			c = a-b
	elif str(args[1]) == '*':
			c = a*b
	elif str(args[1]) == '/':
			c = division(a,b)

	bot.sendMessage(update.message.chat_id, c)
	
	# Калькулятор с распознаванием текстового ввода чисел
	
def wicalc(bot,update,args):
	nums = {"один":1, "два":2, "три":3, "четыре":4, "пять":5, "шесть":6, "семь":7, "восемь":8, "девять":9, "десять":10}
	operations = ["минус", "плюс", "умножить", "разделить"]
	l=list()
	for i in args:
		if i in nums.keys():
			l.append(nums[i])
		if i in operations:
			math_operation = i
	
	if math_operation == "минус":
		result = l[0]-l[1]
	elif math_operation == "плюс":
		result = l[0]+l[1]
	elif math_operation == "умножить":
		result = l[0]*l[1]
	elif math_operation == "разделить":
		result = division(l[0],l[1])
	
	bot.sendMessage(update.message.chat_id, result)

def fullmoon(bot,update,args):
	bot.sendMessage(update.message.chat_id, str(ephem.next_full_moon(args[-1])))

def hmdays(bot,update,args):
	ng = datetime(2017,1,1)
	now = datetime.now()
	num = {1:"день", 2:"дня", 3: "дня", 4: "дня", 5: "дней", 6: "дней", 7: "дней", 8: "дней", 9: "дней", 0: "дней"}
	days = ((str(ng - now)).split())[0]
	i=days[-1]
	if int(i) in num.keys():
		quantity = str(num[int(i)])
	print(quantity)
	bot.sendMessage(update.message.chat_id, days + ' ' + quantity)

def logger(log_data):
	log_file = 'bot.log'
	with open(log_file, 'a', encoding='utf-8') as f:
		f.write(log_data)
		f.close()
	

def run_bot():
    
    updater = Updater("195034229:AAG8LDc4Q-O0NL991wza6ovbwQKVZ1zT2Rk")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("wcount", word_count, pass_args=True))
    dp.add_handler(CommandHandler("calc", calc, pass_args=True))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler("wicalc", wicalc, pass_args=True))
    dp.add_handler(CommandHandler("fullmoon", fullmoon, pass_args=True))
    dp.add_handler(CommandHandler("hmdays", hmdays, pass_args=True))
    updater.start_polling() # опрашивает telegram на наличие сообщений
    updater.idle()

if __name__ == '__main__':
    run_bot()
