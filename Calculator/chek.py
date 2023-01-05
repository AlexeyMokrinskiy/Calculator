def check_operation():
    try:
        input_number = int(input('\n->: '))
        if 0 < input_number < 5:
            return input_number
        print('Ошибка ввода. Это должно быть число от 1 до 4')
        return check_operation()
    except ValueError:
        print('Ошибка ввода. Это должно быть число от 1 до 4')
        return check_operation()

def check_choise():
    try:
        input_number = int(input('\n->: '))
        if 0 < input_number < 3:
            return input_number
        print('Ошибка ввода. 1 или 2')
        return check_operation()
    except ValueError:
        print('Ошибка ввода. Это должно быть число от 1 до 2')
        return check_operation()