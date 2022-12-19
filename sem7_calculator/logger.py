

def logging(first_number, symbol, second_number, result):
    with open('log.txt', 'a') as file:
        file.write(f'{first_number} {symbol} {second_number} = {result}\n')