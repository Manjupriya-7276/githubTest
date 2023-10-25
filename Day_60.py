
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

Brutforce approach(Quick sort)

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


Better Approach:

class Solution:
    def sortColors(self, nums):
        cnt0=0
        cnt1=0
        cnt2=0

        for i in nums:
            if i==0:
                cnt0+=1
            elif i==1:
                cnt1+=1
            elif i==2:
                cnt2+=1

        for i in range(cnt0):
            nums[i]=0
        for i in range(cnt0,cnt0+cnt1):
            nums[i]=1
        for i in range(cnt0+cnt1,len(nums)):
            nums[i]=2

Optimal Approach:

class Solution:
    def sortColors(self, nums):
        low=0
        mid=0
        high=len(nums)-1
        while(mid<=high):
            if(nums[mid]==0):
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1



        
