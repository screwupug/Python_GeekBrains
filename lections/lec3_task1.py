path = 'numbers.txt'
data = open(path, 'r')

def f(x):
    return int(x)**2

list = [(int(line), f(line)) for line in data if int(line) % 2 == 0]
print(list)