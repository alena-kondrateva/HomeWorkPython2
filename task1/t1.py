# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.

# 6782 -> 23
# 0,56 -> 11

num = input('Введите вещественное число: ')

sum = 0
for n in num:
    if n != '.':
        sum += int(n)
print(sum)
