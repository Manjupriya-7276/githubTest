t=int(input())
for _ in range(t):
    c,x,y=map(int,input().split())
    z=c-x
    min_amt=z*y
    print(min_amt)
