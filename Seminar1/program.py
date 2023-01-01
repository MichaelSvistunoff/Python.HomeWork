# Задача 2 [task-2]
# Найдите сумму цифр трехзначного числа.  
# Пример:  
# 123 -> 6 (1 + 2 + 3)  
# 100 -> 1 (1 + 0 + 0)

number = int(input('Enter your number between 100 and 999: '))

if number > 99 and number <1000:
    def sum_of_digits(number):
        count = 0
        while number > 0:
            count = count + number % 10
            number //= 10
        return count

    print(sum_of_digits(number))
else:
    print('Your input is incorrect')

# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов.Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?  
# Пример:  
# 6 -> 1 4 1  
# 24 -> 4 16 4  
# 60 -> 10 40 10

summ = int(input('Enter the summary of origami: '))

one_child_boy = summ // 6
one_child_girl = one_child_boy * 4

print(f'Katya made {one_child_girl} origamis, Petya and Seryioja - {one_child_boy} and {one_child_boy}')

# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.  
# Пример:  
# 385916 -> yes  
# 123456 -> no

number = int(input('Enter your number: '))

if number > 99999 and number < 1000000:
    sum_one = 0
    sum_two = 0

    for i in range(6):
        if i < 3:
            sum_one = sum_one + number // 10 ** i % 10
        else:
            sum_two = sum_two + number // 10 ** i % 10
    if sum_one == sum_two:
        print('YES! Your ticket is lucky!')
    else:
        print('Your ticket is not lucky...')
else:
    print("You've inputed incorrect number!")
    
# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).  
# Пример:  
# 3 2 4 -> yes  
# 3 2 1 -> no

n = int(input('Chocolat n-size: '))
m = int(input('Chocolat m-size: '))
k = int(input('Chocolat k-pics: '))

if k < n * m and (k % n == 0) or (k % m == 0):
    print('YES! You may slice your chocolat!')
else:
    print('NO! You can not slice your chokolat')