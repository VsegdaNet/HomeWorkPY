
#       Задача 2

b = 123
third = b % 10
second = b % 100 // 10
first = b // 100
res = first + second + third
print(f"{b} -> {res} ({first} + {second} + {third})")

#       Задача 4

f = int(input('Введите количество журавликов'))
petr = f / 6
sergey = f / 6
katerina = f / 6 * 4
print(f"{f} -> {petr}  {sergey}  {katerina}")


#       Задача 6

n = 385916
first = n // 1000
second = n % 1000

first_one = first % 10
first_two = first % 100 // 10
first_free = first // 100

second_one = second // 100
second_two = second % 100 // 10
second_free = second % 10

sum_first = first_one + first_two + first_free
sum_second = second_one + second_two + second_free

if sum_first == sum_second:
    print(f"{n} -> yes")
else:
    print(f"{n} -> no")

#       Задача 8

n = int(input("Введите число n - "))
m = int(input("Введите число m - "))
k = int(input("Введите число k - "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

