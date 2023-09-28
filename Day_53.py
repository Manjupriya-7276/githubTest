n=int(input("Enter no of elements to bre entered:"))
a=[]
for i in range(n):
    ele=int(input("Enter the element :"))
    a.append(ele)
print(a)
x=int(input("Enter the element to be searched:"))
found=0
for i in a:
    if(i==x):
        found=1
        break
if(found):
    print("YES")
else:
    print("NO")
    
    
    
