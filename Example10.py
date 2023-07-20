"""На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
5 -> 1 0 1 1 0
2"""
N = int(input('Введите количество монет N = '))
n = 0
m = 0
for i in range(N):
    x = int(input())
    if x == 0:
        n += 1
    if x == 1:
        m += 1
if n < m:
    res = n
else:
    res = m
print(f'Минимальное количество монет, которое нужно перевернуть {res} раз')