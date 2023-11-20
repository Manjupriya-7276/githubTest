Largest Subarray with 0 Sum

class Solution:
    def maxLen(self, n, arr):
        length=0
        for i in range(n):
            s=0
            for j in range(i+1,n):
                s+=arr[j]
                if s==0:
                    length=max(length,j-i+1)
        return length
