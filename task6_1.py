"""
OC: Windows 10 x64
Python v 3.9
"""

import sys

#  Задача 1 к первому уроку.(сумма и произведение цифр трехзначного числа)

u_num = int(input('Введите трехзначное число: '))
f_num = u_num // 100
s_num = u_num // 10 % 10
t_num = u_num % 10
summ = f_num + s_num + t_num
mult = f_num * s_num * t_num
print(f'Сумма = {summ}')
print(f'Произведение = {mult}')

expenses1 = 0
var_list1 = (u_num, f_num, s_num, t_num, summ, mult)
for el in var_list1:
    expenses1 += sys.getrefcount(el)
print(f'Затраты памяти на переменные составили: {expenses1} байт.')

'''
Введите трехзначное число: 224
Сумма = 8
Произведение = 16
Затраты памяти на переменные составили: 399 байт.
-------
Введите трехзначное число: 666
Сумма = 18
Произведение = 216
Затраты памяти на переменные составили: 93 байт.
-------
Введите трехзначное число: 927
Сумма = 18
Произведение = 126
Затраты памяти на переменные составили: 172 байт.
'''

# Задача 3 ко второму уроку.(обратное число от введённого натурального)

num = int(input('Введите натуральное число: \n'))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num //= 10
print(f'Получилось число: {result}')

expenses2 = sys.getrefcount(num) + sys.getrefcount(result)
print(f'Затраты памяти на переменные составили {expenses2} байт.')

'''
Введите натуральное число: 
450
Получилось число: 54
Затраты памяти на переменные составили 318 байт.
-------
Введите натуральное число: 
325468453468635410
Получилось число: 14536864354864523
Затраты памяти на переменные составили 317 байт.
-------
Введите натуральное число: 
4424518884
Получилось число: 4888154244
Затраты памяти на переменные составили 317 байт.

'''

'''
Согласно затраченной памяти мы видим, что не смотря на то, что в первой задаче число всегда трехзначное,
память потребляются по разному, можно сделать вывод что решение перегружено переменными и не является 
оптимальным. Во второй же задаче всего 2 переменные, что приводит к тому, что
независимо от длины введённого числа, затраты всегда константны или близки к константным. Однако наличие
цикла while делает потребление памяти не самым маленьким. Обе задачи могут быть оптимизированы, но 
изначальное решение второй задачи выглядит более оптимальным, чем первой.
'''