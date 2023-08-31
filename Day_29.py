a)
class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j,end=' ')
            print('  '*((2*N)-(2*i)),end="")
            for k in range(1,i+1):
                print(i+1-k,end=" ")
            print()
b)
 def printTriangle(self, N):
        p=1
        for i in range(N):
            for j in range(i+1):
                print(p,end=" ")
                p=p+1
            print()
