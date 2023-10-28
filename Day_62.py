Maximum subarray

Brutforce Approach:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-1
        for i in range(len(nums)):
           sums=0
           for j in range(i,len(nums)):
               sums+=nums[j]
               maxi=max(sums,maxi)
        return maxi
        
Optimal approach (Kadane's Algorithm)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        maxi=-sys.maxsize-1
        for i in range(len(nums)):
            sums=sums+nums[i]
            if sums > maxi:
                maxi=sums
            if sums<0:
                sums=0
        return maxi


To generate the maximum subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        maxi=-sys.maxsize-1
        start_index=-1
        end_index=-1
        for i in range(len(nums)):
            if sums==0:
                start=i
            sums=sums+nums[i]
            if sums > maxi:
                maxi=sums
                start_index=start
                end_index=i
            if sums<0:
                sums=0
        for i in range(start_index,end_index+1):
            print(nums[i])
        return maxi


