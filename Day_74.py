3 SUM : BRUTFORCE APPROACH:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lists=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i!=j and i!=k and j!=k:
                        if (nums[i]+nums[j]+nums[k])==0:
                            triplet=[nums[i],nums[j],nums[k]]
                            triplet.sort()
                            if triplet not  in lists:
                                lists.append(triplet)
        return lists
BETTER APPROACH:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=set()
        for i in range(len(nums)):
            hashmap=set()
            for j in range(i+1,len(nums)):
                ele3=-(nums[i]+nums[j])
                if ele3 in hashmap:
                    temp=[nums[i],nums[j],ele3]
                    temp.sort()
                    s.add(tuple(temp))
                hashmap.add(nums[j])
        res=list(s)
        return res
        

        
