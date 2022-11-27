#======================================================================================
# На вход 5 чисел, найти максимальное число и вывести в консоль
#======================================================================================

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третья число: '))
fourth_number = int(input('Введите четвертое число: '))
fifth_number = int(input('Введите пятое число: '))

list = [first_number, second_number, third_number, fourth_number, fifth_number]
# max_number = max(list)
# print(max_number)

# Alternative 
max_number = list[0]
for i in range(1, len(list)): # так записывается цикл for 
    if list[i] > max_number:
        max_number = list[i]
print(max_number)