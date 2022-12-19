import complex_calculator
import fractions_calculator
import logger

first_number = ''
second_number = ''
symbol = ''
result = ''
s = 0

def menu():
    global s
    print('Это калькулятор для работы с рациональными и комплексными числами.')
    print('Если вы хотите работать с рациональными числами, пожалуйста,\n' +
    'записывайте числитель и знаменатель через запятую (2, 3).')
    print('Если вы хотите работать с комплексными числами, указывайте "j"\n' +
    'в качестве мнимого числа (2 + 7j).')
    s = int(input('Пожалуйста, введите 1 для работы с рациональными числами\n' +
    'или 2 для работы с комплексными числами: '))
    get_values()
    print_result()

def get_values():
    global s
    global first_number
    global second_number
    global symbol
    first_number = (input('Введите первое число: '))
    symbol = (input('Введите математическую операцию (+, -, *, /): '))
    second_number = (input('Введите второе число: '))
    if s == 1:
        fractions_calculator.init(first_number, second_number, symbol)
    elif s == 2:
        complex_calculator.init(first_number, second_number, symbol)

def print_result():
    global s
    global result
    if s == 1:
        result = fractions_calculator.calculate()
        print('Ответ: ' + str(fractions_calculator.calculate()))
        logger.logging(first_number, symbol, second_number, result)
    elif s == 2:
        result = complex_calculator.calculate()
        print('Ответ: ' + str(complex_calculator.calculate()))
        logger.logging(first_number, symbol, second_number, result)

    