
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

optimal approach(Quick sort)

class Solution:
    def pivot_place(self,nums,lowerbound,upperbound):
        pivot=nums[lowerbound]
        i=lowerbound+1
        j=upperbound
        while(True):
            while i<=j and nums[i]<=pivot:
                i=i+1
            while i<=j and nums[j]>=pivot:
                j=j-1
            if i>j:
                break
            else:
                nums[i],nums[j]=nums[j],nums[i]
        nums[lowerbound],nums[j]=nums[j],nums[lowerbound]
        return j

    def quick_sort(self,nums,lowerbound,upperbound):
        if(lowerbound<upperbound):
            p=self.pivot_place(nums,lowerbound,upperbound)
            self.quick_sort(nums,lowerbound,p-1)
            self.quick_sort(nums,p+1,upperbound)

    def sortColors(self, nums):
        n=len(nums)
        self.quick_sort(nums,0,n-1)
        print(nums)


        
