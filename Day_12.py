t=int(input())
for _ in range(t):
    A,B=map(int,input().split())
    x=A*10
    y=B*5
    if(x==y):
        print("ANY")
    elif(x<y):
        print("SECOND")
    else:
        print("First")
