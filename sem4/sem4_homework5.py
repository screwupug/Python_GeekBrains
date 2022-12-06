# ======================================================================================
# Даны два файла, в каждом из которых находится запись многочлена. Задача - 
# сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)
# ======================================================================================

import re

def read_file():
    data = open('mnogochlen.txt')
    lines = data.readlines()
    return lines

def parce(s):
    a = re.findall('\d+\^', s)
    lst = []
    for i in range(0, len(a), 1):
        b = (re.findall('\d\d', str(a[i])))
        for j in b:
            lst.append(int(j))
    return lst

def sum(a, b):
    lst = []
    for i in range(0, len(a), 1):
        lst.append(a[i] + b[i])
    return lst

def mnogochlen(result, k):
    d = ''
    while (k > 0):
        for i in result:
            d += (str(i)) + '^' + (str(k)) + ' + '
            k -= 1
    final = d[0:len(d) - 2] + ('= 0')
    return final

lines = read_file()
line1 = lines[0]
line2 = lines[1]
result = sum(parce(line1), parce(line2))
k = len(result)
n = mnogochlen(result, k)

data = open('result.txt', 'a')
data.write(n + '\n')



