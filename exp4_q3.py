lists = []
arr = int(input("How many values: "))
for i in range(arr):
    value = int(input(f"Enter the value {i + 1}: "))
    lists.append(value)

for i in range(len(lists)):
    if lists[i] % 2 != 0:
        lists[i] = lists[i] + 5

print("Updated list:", lists)