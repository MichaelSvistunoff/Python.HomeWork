# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Enter number A: '))
b = int(input('Enter number B: '))

def DegreeOf(x, y):
    if y == 1:
        return x
    if y != 1:
        return x * DegreeOf(x, y - 1)

print(DegreeOf(a, b))

# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input('Enter number A: '))
b = int(input('Enter number B: '))

def Sum(a, b):
    if a == 0:
        return b
    return Sum(a-1, b+1)

print(Sum(a, b))