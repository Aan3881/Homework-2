#Задача 10: На столе лежат n монеток.
#Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть



nint  =int(input('Введите количество монеток: '))
orel = 0
reshka = 0
for i in range(nint):
    coin = int(input('Введите цифру для решка или орла:'))
    if coin == 1:
        orel += 1
    else:
        reshka += 1
if orel:
    print(f'Количество монет, которые нужно перевернуть: {orel}')
else:
    print(f'Количество монет, которые нужно перевернуть: {reshka}')