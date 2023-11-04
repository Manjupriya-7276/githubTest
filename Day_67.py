Longest consective sequence



Better approach:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        max_count = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue  # Skip duplicates
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1

        return max(max_count, count)

optimized approach:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=set()
        longest=1
        for i in range(len(nums)):
            s.add(nums[i])
        
        for j in s:
            if j-1 not in s:
                cnt=1
                x=j
                while x+1 in s:
                    x=x+1
                    cnt+=1
                longest=max(longest,cnt)
        return longest   
