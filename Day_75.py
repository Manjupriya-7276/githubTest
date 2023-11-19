4 sum : Brutforce approach
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s=set()
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                            if nums[i]+nums[j]+nums[k]+nums[l]==target:
                                four=[nums[i],nums[j],nums[k],nums[l]]
                                s.add(tuple(four))
        m=list(s)
        return m
Better approach:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s=set()
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                hashmap=set()
                for k in range(j+1,len(nums)):
                    fourth=target-(nums[i]+nums[j]+nums[k])
                    if fourth in hashmap:
                        t=[nums[i],nums[j],nums[k],fourth]
                        t.sort()
                        s.add(tuple(t))
                    hashmap.add(nums[k])
        m=list(s)
        return m
                    



                
        
