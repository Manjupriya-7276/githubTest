Brutforce approach:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count>len(nums)//2:
                return nums[i]
        return -1

Better approach:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        print (hashmap)
        for i,freq in hashmap.items():
            if(freq>len(nums)//2):
                return i
        return -1
      
optimize approach:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        element=0
        for i in range(len(nums)):
            if count==0:
                count=1
                element=nums[i]
            elif nums[i]==element:
                count+=1
            else:
                count-=1
        return element
        

optimal approach:(my code)(valid only when 2 different numbers are given)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=nums[0]
        i=0
        j=0
        count=0
        for i in range(len(nums)):
            if nums[i]==n:
                count=count+1
            else:
                j=i
            i=i+1
        rem=len(nums)-count
        if(count>rem):
            return n
        else:
            return nums[j]
        
