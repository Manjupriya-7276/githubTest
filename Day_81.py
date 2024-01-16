Count Inversion

Brutforce approach:
class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if(a[i]>a[j] and i<j):
                    count=count+1
        return count
