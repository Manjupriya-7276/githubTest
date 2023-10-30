Rearrange array elements by sign


Brutforce approach
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        m=[]
        n=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                m.append(nums[i])
            else:
                n.append(nums[i])
        
        for i in range(len(m)):
            nums[i*2]=m[i]
        for i in range(len(n)):
            nums[i*2+1]=n[i]
        return nums

optimal approach:
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        m=[0]*len(nums)
        p=0
        n=1
        for i in range(len(nums)):
            if nums[i]>0:
                m[p]=nums[i]
                p=p+2
            else:
                m[n]=nums[i]
                n=n+2
        return m

  
