# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

import random

numberCoins = int(input('Enter coins number: '))
coinHeadSide = 0
coins = []

for i in range(numberCoins):
    coins.append(random.randint(0, 1))
print(f'Your coins row is: {coins}')

coinHeadSide = sum(coins)
print(coinHeadSide)

coinBackSide = numberCoins - coinHeadSide

if coinHeadSide == coinBackSide:
    print(f'There is no difference what coins to turn. You need to turn {coinHeadSide}')
elif coinHeadSide == numberCoins or coinHeadSide == 0:
    print('All the coins have the same side. You do not need to do anything! .. or You do not have any coins')
elif coinHeadSide < coinBackSide:
    print(f'You need to turn the coins which are head is up - {coinHeadSide}')
else:
    print(f'You need to turn the coins which are back is up - {coinBackSide}')
    
# 5 -> 1 0 1 1 0
# 2

# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Enter summary of numbers: '))
p = int(input('Enter pdoduct of numbers: '))

solutions = 0
for i in range(s):
    if i * (s - i) == p:
        print (f'Petya guessed the numbers: {i} and {s-i}')
        solutions = 1
        break
if solutions == 0:
    print('There are no correct solutions!')
    
# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
# 5
# 1 2 4

# 17
# 1 2 4 8 16

n = int(input('Enter N number: '))
fst = 1

while fst <= n:
    print(fst)
    fst *= 2