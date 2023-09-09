a)
class Solution:
    def armstrongNumber (self, n):
        sum=0
        temp=n
        while temp>0:
            digits=temp%10
            sum+=digits*digits*digits
            temp=temp//10
            
        if(sum==n):
            return "Yes"
        else:
            return "No"


b)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        while(temp>0):
            digit=temp%10
            rev=(rev*10)+digit
            temp=temp//10
        if(rev==x):
            return True
        else:
            return False
