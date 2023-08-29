a)
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print("*",end=" ")
            print()
        for i in range(1,N):
            for j in range(N-i):
                print("*",end=" ")
            print()


b)

class Solution:
    def printTriangle(self, N):
         for i in range(N):
             p=1
             for j in range(i+1):
                 if(i%2==0):
                     if(j%2==0):
                         print(p,end=" ")
                     else:
                         print(p-1,end=" ")
                 else:
                     if(j%2==0):
                         print(p-1,end=" ")
                     else:
                         print(p,end=" ")
             print()
                     
