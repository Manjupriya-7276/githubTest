Count the number of Beautiful subarrays

Brutforce approach:
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            xor=0
            for j in range(i,len(nums)):
                xor=xor^nums[j]
                if xor==0:
                    count+=1
        return count

Optimal approach:
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        xr=0
        mpp=defaultdict(int)
        mpp[xr]=1
        cnt=0

        for i in range(len(nums)):
            xr=xr^nums[i]
            x=xr^0
            cnt+=mpp[x]
            mpp[xr]+=1
        return cnt
