T=int(input())
for i in range(T):
    X,A,B=map(int,input().split())
    if (A+(B*2)>=X):
        print("QUALIFY")
    else:
        print("NOTQUALIFY")
    
