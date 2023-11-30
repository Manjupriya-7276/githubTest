Find the repeating and missing number:
Brutforce approach:
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        m=-1
        r=-1
        for i in range(1,n+1):
            count=0
            for j in range(n):
                if i==arr[j]:
                    count+=1
            if count==2:
                r=i
            elif count==0:
                m=i
            if r!=-1 and m!=-1:
                break
        return [r,m]
            
                
