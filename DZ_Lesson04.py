#       Задача 22

n = int(input("Введите n:"))
m = int(input("Введите m:"))

def on_set(s):
    list = []
    for i in range(s):
        g = int(input(f"Введите число {i + 1}: "))
        list.append(g)
    sett = set(list)
    return sett

set_n = on_set(n)
set_m = on_set(m)
lok = set_n & set_m
liste = list(lok)
liste.sort
for i in liste:
    print(i, end=' ')


#       Задача 24


n = int(input("Количество грядок: "))
list_ar = list()
for i in range(n):
    x = int(input(""))
    list_ar.append(x)

count = list()
for i in range(len(list_ar)):
    count.append(list_ar[-1] + list_ar[0] + list_ar[+1])
print(max(count))
