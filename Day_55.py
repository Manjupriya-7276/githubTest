better approach:1
using hash array

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maxi=max(nums)
        hash=[0]*(maxi+1)
        for i in nums:
            hash[i]+=1
        for i in nums:
            if hash[i]==1:
                return i
        return -1


better approach : 2
using hashmap

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for i , freq in hashmap.items():
            if(freq==1):
                return i
        return -1

optimal approach
Taking XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorr=0
        for i in nums:
            xorr=xorr^i
        return xorr
