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
            
