
#       Задача 3


a1 = int(input('Введите число: '))
d = int(input('Введите число: '))
n = int(input('Введите число: '))
for i in range(n):
    print(a1 + i * d)


#       Задача 32

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)