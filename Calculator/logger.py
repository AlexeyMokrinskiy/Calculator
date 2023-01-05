import os
os.chdir(os.path.dirname(__file__))
from datetime import datetime


def result_logger(data, result):
    first_value, operation, second_value = data
    if operation == 1:
        data_str = f'{str(first_value)} + {str(second_value)}'
    if operation == 2:
        data_str = f'{str(first_value)} - {str(second_value)}'
    if operation == 3:
        data_str = f'{str(first_value)} * {str(second_value)}'
    if operation == 4:
        data_str = f'{str(first_value)} / {str(second_value)}'
    time = datetime.now().strftime('%d.%m.%y %H:%M')
    with open('log', 'a', encoding='UTF-8') as file:
        file.write('{}--> операция: {} результат: {}\n'.format(time, data_str, result))