def insertion_sort(a,n):
    for i in range(1,n):
        y=a[i]
        j=i-1
        while y<a[j] and j>=0:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=y








n=int(input("Enter no of elements in an array:"))
a=[]

for i in range(n):
    t=list(map(int,input("Enter the array elemets:").split()))
    a.extend(t)
print(a)

insertion_sort(a,n)
print(a)

