#======================================================================================
# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
#======================================================================================

import math

first_dot = []
second_dot = []

for i in range(2):
    first_dot.append(int(input('Введите координаты первой точки: ')))
for i in range(2):
    second_dot.append(int(input('Введите координаты второй точки: ')))
print(first_dot, second_dot)

result = float(math.sqrt(math.pow((second_dot[0] - first_dot[0]), 2) + 
math.pow((second_dot[1] - first_dot[1]), 2)))

print(round(result, 2))