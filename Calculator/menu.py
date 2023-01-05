#Основное меню пользователя

import chek

def view_data(data, title):
    print(f'{title} {data}')

def get_value():
    return input('->:')

def input_data():
    print('С какими числами будем работать?\nВведите 1 - для работы с комплексными числами\nВведите 2 - для работы с рациональными числами\nВведите 3 - для работы с простыми числами')
    num_type = get_value()
    if num_type == '1':
        print('Введите первое число (используйте формат: "1 + 2j"):')
        firs_num = get_value()
        print('Введите второе число (используйте формат: "1 + 2j"):')
        second_num = get_value()
        print('Выберите операцию:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление')
        operation = chek.check_operation()
    if num_type == '2':
        print('Введите первое число (используйте формат: "1/2"):')
        firs_num = get_value()
        print('Введите второе число (используйте формат: "1/2"):')
        second_num = get_value()
        print('Выберите операцию:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление')
        operation = chek.check_operation()
    elif num_type == '3':
        print('Введите первое число:')
        firs_num = get_value()
        print('Введите второе число:')
        second_num = get_value()
        print('Выберите операцию:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление')
        operation = chek.check_operation()
    else:
        print('Ошибка ввода. Ввидете цифру от 1 до 3\n\n')
        return input_data()
    return (num_type, firs_num, operation, second_num)