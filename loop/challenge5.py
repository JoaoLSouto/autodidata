# [8, 19, 148, 4] * [9, 1, 33, 83]

list1 = [8, 19, 148, 4] 
list2 = [9, 1, 33, 83]
list3 = []

for item1 in list1:
    for item2 in list2:
        list3.append(item1*item2)

print(list3)