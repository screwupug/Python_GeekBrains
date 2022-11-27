#======================================================================================
# На вход 2 числа, проверить является ли одно число квадратом другого
#======================================================================================

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

# if second_number == first_number**2:
#     print(f'Число {second_number} является квадратом числа {first_number}')
# elif first_number == second_number**2:
#      print(f'Число {first_number} является квадратом числа {second_number}')
# else:
#      print('Нет квадратов')    

## Можно записать намного короче 
print(first_number == second_number**2 or 
second_number == first_number**2) ## Думаю что в принт встроен булиан
