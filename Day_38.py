a)
n=int(input("Enter the number:"))
l=list()
while n!=0:
    r=n%2
    l.append(r)
    n=n//2
l.reverse()

for i in l:
    print(i,end="")


b)
n=int(input("Enter the number:"))
l=list()
while n!=0:
    r=n%2
    l.append(r)
    n=n//2
l.reverse()

for i in l:
    print(i,end="")
    
