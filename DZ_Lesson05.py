#       Задача 6

list_text = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB"
list = [i for i in list_text]

def RLE(string):
    if not all(symmm.isupper() for symmm in string):
        raise 
    if not string:
        return ""
    current_symmm = string[0]
    current_count = 1
    result = ""
    for symmm in string[1:]:
        if symmm == current_symmm:
            current_count += 1
        else:
            result += current_symmm + str(current_count)
            current_symmm = symmm
            current_count = 1
    result += current_symmm + str(current_count)
    return result
print(RLE(list_text))

#       Задача 3

list_text = ["eat", "tea", "tan", "ate", "nat", "bat"]

allress = []

for i in list_text:
    group = [i2 for i2 in list_text if set(i2) == set(i)]
    if group not in allress:
        allress += [group]

print(allress)
    
    
