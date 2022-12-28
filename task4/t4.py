# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input('Введите число: '))

my_list = []
for i in range(n):
    my_list.append(randint(-n, n))
print(my_list)

x = open('task4/file.txt','r')
result = my_list[int(x.readline())] * my_list[int(x.readline(2))]
print(result)