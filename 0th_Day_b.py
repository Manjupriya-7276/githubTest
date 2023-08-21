import math
def area(r):
    a=math.pi*pow(r,2)
    return a
r=int(input("Enter radius:"))
m=area(r)
print("Area of a circle is",m)


py=3.14
r=int(input("Enter radius:"))
a=py*r*r
print("Area of a circle is",a)



num=int(input("Enter the number:"))

def even(n):
    print("YES")

def odd(n):
    return "NO"
if(num%2==0):
    even(num)
else:
    o=odd(num)
    print(o)

