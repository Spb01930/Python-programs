lists = []

arr = int(input("How many values: "))

for i in range(arr):
    value = int(input(f"Enter the value {i + 1}: "))
    lists.append(value)

print(f"The array is: {lists}")

n = len(lists)
for i in range(n):
    for j in range(0, n - i - 1):
        if lists[j] > lists[j + 1]:
            temp = lists[j]
            lists[j] = lists[j + 1]
            lists[j + 1] = temp

print("Sorted array:", lists)

second_largest = lists[-2]
second_smallest = lists[1]

print(f"The second largest number: {second_largest}")
print(f"The second smallest number: {second_smallest}")
