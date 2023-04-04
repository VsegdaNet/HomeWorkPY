#       Задача 34 


def str_line(str_list):
    str = str_list.lower().split()
    a = lambda x: sum(1 for i in  x if i in 'аоуыэеёиюя')
    temp = a(str[0])
    for i in str:
        if a(i) != temp:
            return 'Пам парам'
            break
    return 'Парам пам-пам'

h = str_line('пара-ра-рам рам-пам-папам па-ра-па-да')
print(h)

#       Задача 36


def print_operation_table(operation, num_rows=6, num_columns=6):
    res = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in res:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)