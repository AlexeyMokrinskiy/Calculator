from calculator import calc_block
from logger import result_logger as write_log
import parser
import menu
import chek
from telebot import TeleBot, types
import os
os.chdir(os.path.dirname(__file__))
import codecs
import datetime

TOKEN = '5930763566:AAF_os-oyampNxM10McpayMKBgxfo6UJMTM'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=('С какими числами будем работать?\nВведите 1 - для работы с комплексными числами\nВведите 2 - для работы с рациональными числами\nВведите 3 - для работы с простыми числами'))
    

@bot.message_handler()
def answer(msg: types.Message):

    num_tupe = msg.text
    if num_tupe == '1':
        bot.send_message(chat_id=msg.from_user.id, text='Работанм с комплексными числами')
        new_msg = bot.send_message(chat_id=msg.from_user.id, text='Введите первое и второе число через пробел')
        bot.register_next_step_handler(msg, operation, msg)

    elif num_tupe == '2':
        bot.send_message(chat_id=msg.from_user.id, text='Работанм с рациональными числами')
        new_msg = bot.send_message(chat_id=msg.from_user.id, text='Введите первое и второе число через пробел')
        bot.register_next_step_handler(msg, operation, msg)

    elif num_tupe == '3':
        bot.send_message(chat_id=msg.from_user.id, text='Работанм с простыми числами')
        new_msg = bot.send_message(chat_id=msg.from_user.id, text='Введите первое и второе число через пробела')
        bot.register_next_step_handler(new_msg, operation, msg)
    elif num_tupe == '4':
        with open('log', 'r', encoding = 'utf-8') as file:
            result = file.read()
            bot.send_message(msg.chat.id, result)

def operation(msg, numtype):
    oper_msg = bot.send_message(chat_id=msg.from_user.id, text='Выберите операцию:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление')
    bot.register_next_step_handler(oper_msg, counter, msg, numtype)

def counter(oper, numbers, numtype):
    tmp = numbers.text.split()
    lst = [numtype.text, tmp[0], int(oper.text), tmp[1]]
    print(lst)
    result = parser.pars(lst)
    final_result = calc_block(result)
    
    bot.send_message(oper.chat.id, str(final_result))
    res = write_log(lst[1:], final_result)

bot.polling()