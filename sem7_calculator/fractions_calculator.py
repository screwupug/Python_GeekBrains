from fractions import Fraction


first_number = []
second_number = []
symbol = ''

def init(x, y, s):
    global first_number
    global second_number
    global symbol
    first_number = str(x).split(', ')
    second_number = str(y).split(', ')
    symbol = s


def calculate():
    if symbol == '+':
        return Fraction(int(first_number[0]), int(first_number[1])) + Fraction(int(second_number[0]), int(second_number[1]))
    elif symbol == '-':
        return Fraction(int(first_number[0]), int(first_number[1])) - Fraction(int(second_number[0]), int(second_number[1]))
    elif symbol == '*':
        return Fraction(int(first_number[0]), int(first_number[1])) * Fraction(int(second_number[0]), int(second_number[1]))
    elif symbol == '/':
        return Fraction(int(first_number[0]), int(first_number[1])) / Fraction(int(second_number[0]), int(second_number[1]))