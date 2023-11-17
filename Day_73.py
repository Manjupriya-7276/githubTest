Majority element (Element that appear more than n//3 times)

Brutforce approach
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m=len(nums)
        ls=[]
        for i in range(len(nums)):
            count=0
            if len(ls)==0 or nums[0]!=nums[i]:
                for j in range(len(nums)):
                    if(nums[i]==nums[j]):
                        count+=1
                if count>(m//3):
                    ls.append(nums[i])
                if len(ls)==2:
                    break
        return ls


Better approach:
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}
        ls=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for i , freq in hashmap.items():
            if freq>(len(nums)//3):
                ls.append(i)
        return ls

Optimal approach
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_1=0
        count_2=0
        ele_1=float('-inf')
        ele_2=float('-inf')
        ls=[]
        for i in range(len(nums)):
            if count_1==0 and nums[i]!=ele_2:
                count_1+=1
                ele_1=nums[i]
            elif count_2==0 and nums[i]!=ele_1:
                count_2+=1
                ele_2=nums[i]
            elif nums[i]==ele_1:
                count_1+=1
            elif nums[i]==ele_2:
                count_2+=1
            else:
                count_1-=1
                count_2-=1
        count_1=0
        count_2=0
        for i in range(len(nums)):
            if nums[i]==ele_1:
                count_1+=1
            if nums[i]==ele_2:
                count_2+=1
        if count_1>(len(nums)//3):
            ls.append(ele_1)
        if count_2>(len(nums)//3):
            ls.append(ele_2)
        ls.sort()
        return ls
    


        
            
            


        
