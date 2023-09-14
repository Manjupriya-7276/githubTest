def bubble_sort(a,n):
    last=n
    for p in range(n-1):
        exchange=0
        for i in range(last-1):
            if(a[i]>a[i+1]):
                a[i],a[i+1]=a[i+1],a[i]
                exchange=exchange+1
        if(exchange==0):
            exit
        else:
            last=last-1

n=int(input("Enter no of elements in the array:"))
a=[]

for i in range(n):
    t=list(map(int,input("Enter the array elements:").split()))
    a.extend(t)
print(a)

bubble_sort(a,n)
print(a)
