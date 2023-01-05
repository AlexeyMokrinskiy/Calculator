from calculator import calc_block
from logger import result_logger as write_log
import parser
import menu
import chek

def button_click():
    a = parser.pars(menu.input_data())
    calc_result = calc_block(a)
    menu.view_data(calc_result, 'Результат:')
    write_log(a, calc_result)
    print('\nПродолжить?\n1 - Да\n2 - Нет')
    next = chek.check_choise()
    if next == 1:
        button_click()
    if next == 2:
        print('До сидания!')
        
button_click()