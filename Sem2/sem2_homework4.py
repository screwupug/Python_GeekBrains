#======================================================================================
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число. 
#======================================================================================

n = int(input('Введите число: '))
list = []
path = 'file.txt'
data = open(path, 'r')
result = 1

for i in range(-n, n + 1, 1):
    list.append(i)
print(list)

for line in data:
    for i in list:
        if int(line) == i:
            result *= list[i]
print(result)