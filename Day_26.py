class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(1,i+2):
                print(j,end=" ")
            print()
