"""Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
10 -> 1 2 4 8"""

N = int(input('Введите число N = '))
i = 1
while i <= N:
    print(i, end = ' ')
    i = i * 2
