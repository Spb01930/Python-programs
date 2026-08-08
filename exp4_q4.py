lists = []
n = int(input("How many terms: "))

a = 0
b = 1

for i in range(n):
    lists.append(a)
    c = a + b
    a = b
    b = c
print("The Fibonacci series:", lists)