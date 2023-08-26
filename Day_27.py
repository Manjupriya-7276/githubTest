a)
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i,N-1):
                print(" ",end="")
            for j in range(i):
                print("*",end="")
            for j in range(i+1):
                print("*",end="")
            print()
            

b)
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i):
                print(" ",end="")
            for j in range(i,N-1):
                print("*",end="")
            for j in range(i,N):
                print("*",end="")
            print()
