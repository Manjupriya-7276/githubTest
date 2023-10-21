Two sum

Brutforce approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                r=nums[i]+nums[j]
                if(r==target):
                    return[i,j]

Better Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        l=[]
        for i in range(len(nums)):
            res=target-nums[i]
            if res in my_dict:
                return [my_dict[res],i]
            my_dict[nums[i]]=i


optimal approach
class Solution(object):
    def twoSum(self, nums, target): 
        nums_with_index = [(num,i) for i,num in enumerate(nums)]
        nums_with_index.sort()
        left,right = 0,len(nums)-1
        while left < right:
            if nums_with_index[left][0] + nums_with_index[right][0] == target:
                return [nums_with_index[left][1],nums_with_index[right][1]]
            elif nums_with_index[left][0] + nums_with_index[right][0] < target:
                left +=1
            else:
                right -=1
        return []

optimal approach when the answer to be given is yes or no ,not as index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i=0
        j=len(nums)-1
        while(i<j):
            res=nums[i]+nums[j]
            if res==target:
                return "yes"
            elif res<target:
                i=i+1
            else:
                j=j-1
        return "no"
                
