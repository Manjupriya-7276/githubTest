t=int(input())
deg=0
for _ in range(t):
    n=int(input())
    terms=list(map(int,input().split()))
    for i in range(n):
        if(terms[i]!=0):
            deg=i
    print(deg)
            
