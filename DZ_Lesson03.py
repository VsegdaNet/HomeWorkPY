#       Задача 16

import random

num1 = int(input("Введите число: "))
num2 = int(input("Какое число: "))
list = [random.randint(1,10) for _ in range(num1)]
count = 0
for i in list:
    if i == num2:
        count += 1
print(list)
print(count)

num1 = int(input("Введите число: "))
num2 = int(input("Какое число: "))
list = [random.randint(1,10) for _ in range(num1)]
res = list.count(num2)
print(list)
print(res)


#       Задача 16


num1 = int(input("Введите число: "))
num2 = int(input("Какое число: "))
list = [i for i in range(1,num1)]
res = min(list,key=lambda x: abs(x-num2))
print(list)
print(res)


#       Задача 16

import re
my_dict = {1 : 'AEIOULNSTR', 2 : 'DG', 3 : 'BCMP', 4 : 'FHVWY', 5 : 'K', 8 : 'JX', 10 : 'QZ',}
my_dict1 = {1 : 'АВЕИНОРСТ', 2 : 'ДКЛМПУ', 3 : 'БГЁЬЯ', 4 : 'ЙЫ', 5 : 'ЖЗХЦЧ', 8 : 'ШЭЮ', 10 : 'ФЩЪ'}

def getext(text):
	return bool(re.search('[а-яА-Я]', text))

text = input().upper()
res = 0
if getext(text):
	for i in text:
		for j, g in my_dict1.items():
			if i in g:
				res += sum([j])
else:
	for i in text:
		for j, g in my_dict.items():
			if i in g:
				res += sum([j])			
print(res)
    
