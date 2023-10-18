Longest subarray with sum equals k

brute force approach

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        length=0
        for i in range(len(arr)):
            s=0
            for j in range(i,len(arr)):
                s=s+arr[j]
                if(s==k):
                    length=max(length,j-i+1)
        return length


Better approach (when positives and negatives are there , cant optimize more than this)

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        presum_Map={}
        maxlen=0
        sum=0
        for i in range(len(arr)):
            sum=sum+arr[i]
            
            if sum==k:
                maxlen=max(maxlen,i+1)
            
            rem=sum-k
            
            if rem in presum_Map:
                length=i-presum_Map[rem]
                maxlen=max(maxlen,length)
            if sum not in presum_Map:
                presum_Map[rem]=i
        return maxlen

optimal approach (when positives and zerors are there)

def lenOfLongSubarr(self, arr, n, k):
        maxlen=0
        sum=arr[0]
        i=j=0
        while(j < n):
            
            while i<=j and sum > k:
                sum=sum-arr[i]
                i=i+1
                
                
            if sum==k:
                maxlen=max(maxlen,j-i+1)
            
            
            j=j+1
            
            if j<n:
                sum=sum+arr[j]
            
        return maxlen
                




