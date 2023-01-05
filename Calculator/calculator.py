#Модуль вычислений

def sum(first_value, second_value):
    return first_value + second_value

def sub(first_value, second_value):
    return first_value - second_value

def mult(first_value, second_value):
    return first_value * second_value

def div(first_value, second_value):
    return first_value / second_value

def calc_block(data):
    first_value, operation, second_value = data
    if operation  == 1:
        return sum(first_value, second_value)
    if   operation == 2:
        return sub(first_value, second_value)
    if   operation == 3:
        return mult(first_value, second_value)
    if (operation == 4) and (second_value != 0):
        return div(first_value, second_value)
    else:
        return 'Ошибка деления на 0!'

