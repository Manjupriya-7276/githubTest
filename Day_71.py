Subarray sum equals K
Optimal approach:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       presum=0
       mapp=defaultdict(int)
       count=0
       mapp[0]=1
       for i in range(len(nums)):
           presum=presum+nums[i]

           remove=presum-k

           count=count+mapp[remove]

           mapp[presum] += 1

       return count

