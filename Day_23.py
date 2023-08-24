n=int(input())
for _ in range(n):
    t=list(map(int,input().split()))
    t.remove(max(t))
    print(max(t))
