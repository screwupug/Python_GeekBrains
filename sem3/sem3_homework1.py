#======================================================================================
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
#  списка, стоящих на нечётной позиции.
#======================================================================================

list = [2, 3, 5, 9, 3]
result = 0;

for i in range(1, len(list), 1):
    if i % 2 != 0:
        result += list[i]
print(result)