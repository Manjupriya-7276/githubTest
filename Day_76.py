Largest Subarray with 0 Sum
Brutforce approach
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

Optimal approach:
class Solution:
    def maxLen(self, n, arr):
        hashmap={}
        maxlen=0
        s=0
        for i in range(n):
            s+=arr[i]
            if s==0:
                maxlen=max(maxlen,i+1)
            else:
                if s in hashmap:
                    maxlen=max(maxlen,i-hashmap[s])
                else:
                    hashmap[s]=i
        return maxlen
