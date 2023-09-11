Recursion:
A)
n=int(input("Enter the number:"))
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
res=factorial(n)
print(res)

B)
m=int(input("Enter num:"))

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
for n in range(m):
    print(fib(n))
