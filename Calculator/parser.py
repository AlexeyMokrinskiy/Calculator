#Парсер

from fractions import Fraction

def pars(data):
    num_type, first_value, operation, second_value = data

    if num_type == '1':
        first_value = complex(first_value)
        second_value = complex(second_value)
    elif num_type == '2':
        a = first_value
        first_value = Fraction(int(a[0: a.index(
            '/')]), int(a[a.index('/')+1:len(a)]))
        b = second_value
        second_value = Fraction(int(b[0: b.index(
            '/')]), int(b[b.index('/')+1:len(b)]))
    elif num_type == '3':
        first_value = int(first_value)
        second_value = int(second_value)
    else:
        print('Ошибка ввода')
        return pars(data)
    return (first_value, operation, second_value)