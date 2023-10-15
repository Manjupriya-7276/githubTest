
class Solution:
    def missingNumber(self,array,n):
        # code here
        array_sum=(n*(n+1))//2
        current_sum=sum(array)
        return array_sum-current_sum
            
        
        
