#======================================================================================
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел 
# от 1 до N.
#======================================================================================

n = int(input('Введите число: '))
list = []

sum = 1
counter = 1

while counter < n + 1:
    sum *= counter
    list.append(sum)
    counter += 1
print(list)