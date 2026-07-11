import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
s=float((a+b+c)/2)
z=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of the triangle is:",z)