#======================================================================================
# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# 1 + 2 * 3 => 7;
#======================================================================================

def get_right_expr():
    print('Строчный калькулятор.\nИспользуйте операции +,-,/,*.\nДанный калькулятор' 
    + ' поддерживает только одну или 2 операции')
    expr = input('Введите арифмитеское выражение: ')
    a = expr.split(' ')
    while len(a) != 3 and len(a) != 5:
        expr = input('Ошибка ввода! Попробуйте еще раз: ')
    if len(a) == 3:
        while not (switch_number(a[0]) and switch_number(a[2]) and switch_symbols(a[1])):
            a = input('Ошибка ввода! Попробуйте еще раз: ').split(' ')
        print('Ответ: ' + str(one_symbol(a[1], a[0], a[2])))
    elif len(a) == 5:
        while not (switch_number(a[0]) and switch_number(a[2]) and switch_number(a[4]) 
        and switch_symbols(a[1]) and switch_symbols(a[3])):
            a = input('Ошибка ввода! Попробуйте еще раз: ').split(' ')
        print('Ответ: ' + str(two_symbol(a)))

def switch_number(number):
    try:
        int(number)
        return True
    except Exception:
        return False

def switch_symbols(symbol):
    if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
        return False
    else:
        return True

def one_symbol(symbol, digit_one, digit_two):
    if symbol == '+':
        return (int(digit_one) + int(digit_two))
    elif symbol == '-':
        return (int(digit_one) + int(digit_two))
    elif symbol == '*':
        return (int(digit_one) + int(digit_two))
    elif symbol == '/':
        return (int(digit_one) + int(digit_two))

def has_priority(expr):
    if (expr[1] == '*' or expr[1] == '/') or (expr[3] == '*' or expr[3] == '/'):
        return True   

def two_symbol(expr):
    result = 0
    if (has_priority(expr)):
        first_symbol = False
        second_symbol = False
        if expr[1] == '*' or expr[1] == '/':
            first_symbol = True
        elif expr[3] == '*' or expr[3] == '/':   
            second_symbol = True
        if first_symbol:
            if expr[1] == '*':
                result = int(expr[0]) * int(expr[2])
            elif expr[1] == '/':
                result = int(expr[0]) / int(expr[2])
            result = one_symbol(expr[3], result, expr[4])
            return result
        if second_symbol:
            if expr[3] == '*':
                result = int(expr[2]) * int(expr[4])
            elif expr[3] == '/':
                result = int(expr[2]) / int(expr[4])
            result = one_symbol(expr[1], expr[0], result)
            return result

get_right_expr()