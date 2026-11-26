numbers = [1, 2, 2, 3, 4, 4, 5]
list = []

for item in numbers:
    if item not in list:
        list.append(item)

print(list)  
