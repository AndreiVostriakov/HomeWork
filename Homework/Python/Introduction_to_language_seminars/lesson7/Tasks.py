# def our_print():
#     print("123")

# name_func = our_print
# name_func()

# ///////////////////////////////////////////

# numbers = [1, 14, 6, 10, 3, 2, 5]
# print(list(filter(lambda x: x > 5, numbers)))

# //////////////////////////////////////////

# def our_func(func, numbers):
#     return (el for el in numbers if func(el))

# numbers = [1, 14, 6, 10, 3, 2, 5]
# # print(list(filter(lambda x: x > 5, numbers)))
# print(list(our_func(lambda x: x > 5, numbers)))

# //////////////////////////////////////////

# def stopwatch(func):
#     import time
#     def decorator():
#         start_time = time.time()
#         func()
#         print(f"Время выполнения {time.time() - start_time}")
#     return decorator

# @stopwatch
# def our_math_str():
#     num = '132'
#     result = int(num) + int(num * 2) + int(num * 3)
#     print(result)    

# @stopwatch
# def our_math_int():
#     num = 132
#     result = num + num * 1000 + num + num * 1000000 + num * 1000 + num
#     print(result)
    
# our_math_str()
# our_math_int()

# /////////////////////////////////////////////////////////

# def our_form(func):
#     def decorator(*args):
#         for arg in args:
#             print(f"{arg} + ", end="")
#         print("\b\b= ", end="")
#         func(*args)
#     return decorator

# @our_form
# def sum(a, b):
#     print(a + b)

# @our_form
# def sum4(a, b, c, d):
#     print(a + b + c + d)

# sum(3, 51)
# sum4(4, 6, 1, 0)

# /////////////////////////////////////////////////////////

# def greetings(hello):
#     def our_greetings(func):
#         def decorator():
#             name = func()
#             print(f"{hello}, {name}")
#         return decorator
#     return our_greetings

# @greetings("Привет")
# def get_name():
#     return input("Как тебя зовут?\n")

# get_name()

# /////////////////////////////////////////////////////////

import telebot, requests, time

bot = telebot.TeleBot("6066087134:AAEq2ju8FBfGfKXNqfqObNFxgY8eC-drzOw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def greetings(message):
	# print(message)
	text = message.text
	if "Привет" in text:
		bot.reply_to(message, f"Привет, {message.from_user.first_name}")
	elif text == "погода":
		req = requests.get("https://wttr.in/?0T")
		bot.reply_to(message, req.text)
	elif text == "кошак":
		req = requests.get(f"https://cataas.com/cat?{time.time()}")
		bot.send_photo(message.from_user.id, req.content)

bot.polling()