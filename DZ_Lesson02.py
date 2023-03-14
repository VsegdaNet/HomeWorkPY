#       Задача 10

coll = int(input("Количество монет - "))
falg = 0
eagle = 0
for i in range(coll):
    nam = int(input('Введите сторону(0 - орел/1 - герб) - '))
    if nam == 0:
        eagle += 1
    elif nam == 1:
        falg += 1
if eagle < falg:
    print(f'Переверните орлов {eagle}')
else:
    print(f"Переверните гербы {falg}")

#       Задача 12

x = int(input('Введите первое число - '))
y = int(input("Введите первое число - "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

#       Задача 14

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1