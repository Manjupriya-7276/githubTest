a)
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(1,i+2):
                print(j,end=" ")
            print()

b)
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(1,i+2):
                print(i+1,end=" ")
            print()

c)
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i,N):
                print("*",end=" ")
            print()
d)
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            p=1
            for j in range(i,N):
                print(p,end=" ")
                p+=1
            print()

