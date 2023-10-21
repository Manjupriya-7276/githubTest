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

my approach optimal : works when positives and zeros are given

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = nums[0]
        i = 0
        j = 0
        mapp = {}
        count = 0
        while j < len(nums):
            if sums == k:
                count += 1
                mapp[sums] = count

            if sums >= k:
                sums -= nums[i]
                i += 1
                if i > j:
                    j = i  # Ensure i and j do not cross

            else:
                j += 1
                if j < len(nums):
                    sums += nums[j]
                else:
                    break  # Prevent going out of bounds

        return count


optimal approach :

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



