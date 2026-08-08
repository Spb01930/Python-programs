list1 = [2, 3, 4, 5, 7]
list2 = ["A", "B", "C", "D", "E"]

a = []

for i in range(len(list1)):
    a.append(str(list1[i]))
    a.append(list2[i])

print(a)