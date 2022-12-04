#======================================================================================
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных 
# индексов.
# Fn = F(n+2)−F(n+1)
# F−n = (−1)n+1Fn.
#======================================================================================

number = int(input('Введите число: '))
fib1 = 1
fib2 = 1
neg_fib1 = 1
neg_fib2 = -1
i = 0
list = [neg_fib1, neg_fib2]

while i < number - 2:
    fib_sum = neg_fib1 - neg_fib2
    neg_fib1 = neg_fib2
    neg_fib2 = fib_sum
    list.append(neg_fib2)
    i = i + 1
list.reverse()
list.append(0)
list.append(fib1)
list.append(fib2)
i = 0

while i < number - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    list.append(fib2)
    i = i + 1
print(list)