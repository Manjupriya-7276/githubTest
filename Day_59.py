Two sum

Brutforce approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                r=nums[i]+nums[j]
                if(r==target):
                    return[i,j]
                    
                
