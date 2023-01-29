# Домашнее задание Семинар 1

<details>
    <summary>
        Задача 2
    </summary>

    Найдите сумму цифр трехзначного числа.  
    Пример:  
    123 -> 6 (1 + 2 + 3)  
    100 -> 1 (1 + 0 + 0)
</details>

<details>
    <summary>
        Задача 4
    </summary>

    Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?  
    Пример:  
    6 -> 1 4 1  
    24 -> 4 16 4  
    60 -> 10 40 10
</details>

<details>
    <summary>
        Задача 6
    </summary>
    
    Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.  
    Пример:  
    385916 -> yes  
    123456 -> no
</details>

<details>
    <summary>
        Задача 8 
    </summary>

    Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).  
    Пример:  
    3 2 4 -> yes  
    3 2 1 -> no
</details>

# Домашнее задание Семинар 2

<details>
    <summary>
        Задача 10
    </summary>

    На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
    Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
    Выведите минимальное количество монет, которые нужно перевернуть.

    5 -> 1 0 1 1 0  
    2
</details>

<details>
    <summary>
        Задача 12
    </summary>

    Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
    Помогите Кате отгадать задуманные Петей числа.
</details>

<details>
    <summary>
        Задача 14
    </summary>

    Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
    5  
    1 2 4

    17  
    1 2 4 8 16
</details>

# Домашнее задание Семинар 3

<details>
    <summary>
        Задача 16
    </summary>

    Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
    Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
    Заполните массив случайными натуральными числами от 1 до N/2.
    Выведите, сколько раз X встречается в массиве.  
    Ввод: 5  
    Ввод: 1

    1 2 1 2 2
    Вывод: 2
</details>

<details>
    <summary>
        Задача 18
    </summary>

    Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
    Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
    Заполните массив случайными натуральными числами от 1 до N.
    Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.  
    Ввод: 10  
    Ввод: 7  
    1 2 1 8 9 6 5 4 3 4  
    Вывод: 6
</details>

<details>
    <summary>
        Задача 20
    </summary>

    В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
    В случае с английским алфавитом очки распределяются так:  
    A, E, I, O, U, L, N, S, T, R – 1 очко;  
    D, G – 2 очка;  
    B, C, M, P – 3 очка;  
    F, H, V, W, Y – 4 очка;  
    K – 5 очков;  
    J, X – 8 очков;  
    Q, Z – 10 очков.  

    А русские буквы оцениваются так:  
    А, В, Е, И, Н, О, Р, С, Т – 1 очко;  
    Д, К, Л, М, П, У – 2 очка;  
    Б, Г, Ё, Ь, Я – 3 очка;  
    Й, Ы – 4 очка;  
    Ж, З, Х, Ц, Ч – 5 очков;  
    Ш, Э, Ю – 8 очков;  
    Ф, Щ, Ъ – 10 очков.

    Напишите программу, которая вычисляет стоимость введенного пользователем слова.
    Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.  
    Ввод: ноутбук  
    Вывод: 12
</details>

# Домашнее задание Семинар 4

<details>
    <summary>
        Задача 22:
    </summary>

    Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
    Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
    Пользователь вводит 2 числа.
    n - кол-во элементов первого набора.
    m - кол-во элементов второго набора.
    Значения генерируются случайным образом.

    Input: 11 6
    (значения сгенерированы случайным образом
    2 4 6 8 10 12 10 8 6 4 2
    3 6 9 12 15 18)

    Output: 11 6
    6 12
</details>

<details>
    <summary>
        Задача 24
    </summary>

    В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
    В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

    Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

    Input: 4
    (значения сгенерированы случайным образом
    4 2 3 1 )

    Output: 9
</details>

# Домашнее задание Семинар 5

<details>
    <summary>
        Задача 26
    </summary>
    
    Напишите программу, которая на вход принимает два числа A и B, 
    и возводит число А в целую степень B с помощью рекурсии.
</details>

<details>
    <summary>
        Задача 28
    </summary>

    Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
    Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
</details>

# Задачи на повторение по материалам предыдущих семинаров (по желанию)

<details>
    <summary>
        Задача 101
    </summary>

    Вычислить число π c заданной точностью d

    Пример: 
    при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001
</details>

<details>
    <summary>
        Задача 102
    </summary>

    Задайте натуральное число N. Напишите программу,  
    которая составит список простых множителей числа N.
</details>

<details>
    <summary>
        Задача 103 
    </summary>
    
    Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

    Пример:  k=2 

    Возможные варианты многочленов:
    2*x*x + 4*x + 5 = 0 
    x*x + 5 = 0 
    10*x*x = 0
</details>

<details>
    <summary>
        Задача 104
    </summary>

    Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена 
    (полученные в результате работы программы из задачи 103). 
    Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.
</details>

<details>
    <summary>
        Задача 105
    </summary>

    Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
</details>

<details>
    <summary>
        Задача 106
    </summary>

    Создайте программу для игры с конфетами человек против человека.
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)
</details>

<details>
    <summary>
        Задача 107
    </summary>

    Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)
</details>

<details>
    <summary>
        Задача 108
    </summary>
    
    Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)
    метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
    метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
    Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).
</details>

# Домашнее задание Семинар 6

<details>
    <summary>
        Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
    </summary>

    Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.

    **Функции справочника:**  
    - Показать все записи  
    - Найти запись по вхождению частей имени  
    - Найти запись по телефону  
    - Добавить новый контакт  
    - Удалить контакт  
    - Изменить номер телефона у контакта

    **Пример работы программы:**

    При запуске программы пользователю выдается меню:

    Введите номер действия:  
    1. Показать все записи  
    2. Найти запись по вхождению частей имени  
    3. Найти запись по телефону  
    4. Добавить новый контакт  
    5. Удалить контакт  
    6. Изменить номер телефона у контакта  
    7. Выход

    После выбора действия выполняется функция, реализующая это действие.  
    После завершения работы функции пользователь возвращается в меню.
    
</details>

# Домашнее задание Семинар 7

<details>
    <summary>
        Продолжить работу над справочником автобусного парка.
    </summary>

    Создани справочника автобусного парка с возможностью добавления, редактирования, удаления данных и показом детализации по ним.
    
</details>