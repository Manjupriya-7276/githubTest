def selection_sort(a,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if(a[j]<a[min_index]):
                min_index=j
            if(min_index != i):
                a[i],a[min_index]=a[min_index],a[i]
                
            

n=int(input("Enter no of elements in the array:"))
a=[]
for i in range(n):
    t=list(map(int,input("Enter array elements:").split()))
    a.extend(t)
    
selection_sort(a,n)
print(a)

