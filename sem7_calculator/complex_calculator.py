first_number = ''
second_number = ''
symbol = ''

def init(x, y, s):
    global first_number
    global second_number
    global symbol
    first_number = x
    second_number = y
    symbol = s

def calculate():
    if symbol == '+':
        return complex(first_number.replace(' ', '')) + complex(second_number.replace(' ', ''))
    elif symbol == '-':
        return complex(first_number.replace(' ', '')) - complex(second_number.replace(' ', ''))
    elif symbol == '*':
        return complex(first_number.replace(' ', '')) * complex(second_number.replace(' ', ''))
    elif symbol == '/':
        return complex(first_number.replace(' ', '')) / complex(second_number.replace(' ', ''))