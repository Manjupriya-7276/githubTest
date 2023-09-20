def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        l_list = a[0:mid]  
        r_list = a[mid:len(a)]  
        merge_sort(l_list)
        merge_sort(r_list)
        i = 0
        j = 0
        k = 0
        while i < len(l_list) and j < len(r_list):
            if l_list[i] < r_list[j]:
                a[k] = l_list[i]
                i = i + 1
            else:
                a[k] = r_list[j]
                j = j + 1
            k = k + 1
        while i < len(l_list):
            a[k] = l_list[i]
            i = i + 1
            k = k + 1
        while j < len(r_list):
            a[k] = r_list[j]
            j = j + 1
            k = k + 1

n = int(input("Enter no of elements in an array:"))
a=[]

for i in range(n):
    t=list(map(int,input("Enter the array elements:").split()))
    a.extend(t)
print(a)

merge_sort(a)
print(a)
