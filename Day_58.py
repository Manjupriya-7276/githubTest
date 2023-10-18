count the subarray sum equals k

brutforce approach

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            sums=0
            for j in range(i,len(nums)):
                sums+=nums[j]
                if sums==k:
                    count=count+1
        return count
            
