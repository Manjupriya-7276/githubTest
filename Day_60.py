
Brutforce approach(selection sort)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            min_value=i
            for j in range(i+1,len(nums)):
                if nums[min_value]>nums[j]:
                    min_value=j
            if i!=min_value:
                nums[i],nums[min_value]=nums[min_value],nums[i]
        return nums
