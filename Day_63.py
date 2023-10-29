Stock Buy and Sell

My aprroach(Not run for all test Cases)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=min(prices)
        for i in range(len(prices)):
            if(prices[i]==m):
                ind=i
        maxi=prices[ind]
        for j in range(ind,len(prices)):
            if prices[j]>maxi:
                maxi=prices[j]
        trans=maxi-prices[ind]
        return trans

Brutforce approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                p=prices[j]-prices[i]
                if p>maxi:
                    maxi=p
        return maxi

optimal approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins=prices[0]
        maxs=0
        for i in range(len(prices)):
            if prices[i]<mins:
                mins=prices[i]
            maxs=max(prices[i]-mins,maxs)
        return maxs

        







        
