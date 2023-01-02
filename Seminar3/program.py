import random

# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.  

# Ввод: 5  
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

n = int(input('Enter number of row: '))

row = []
for i in range(1, n):
    row.append(random.randint(1, n/2))
print(f'Your array: {row}')

x = int(input('Enter number you need to check: '))
count = 0
for i in range(0, len(row)):
    if row[i] == x:
        count += 1
print(f'Your number {x} meets {count} times in your row')

# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, 
# выведите наименьший по величине.  
# Ввод: 10  
# Ввод: 7  
# 1 2 1 8 9 6 5 4 3 4  
# Вывод: 6

n = int(input('Enter number of row: '))
row = []

for i in range(1, n):
    row.append(random.randint(1, n))
print(f'Your array: {row}')

number = 0
x = int(input('Enter number you need to check: '))

for i in range(0, len(row)):
    if (x - row[i]) < x - number and x - row[i] > 0:
        number = i
print(row[number])

# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:  
# A, E, I, O, U, L, N, S, T, R – 1 очко;  
# D, G – 2 очка;  
# B, C, M, P – 3 очка;  
# F, H, V, W, Y – 4 очка;  
# K – 5 очков;  
# J, X – 8 очков;  
# Q, Z – 10 очков.  

# А русские буквы оцениваются так:  
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;  
# Д, К, Л, М, П, У – 2 очка;  
# Б, Г, Ё, Ь, Я – 3 очка;  
# Й, Ы – 4 очка;  
# Ж, З, Х, Ц, Ч – 5 очков;  
# Ш, Э, Ю – 8 очков;  
# Ф, Щ, Ъ – 10 очков.  

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.  
# Ввод: ноутбук  
# Вывод: 12