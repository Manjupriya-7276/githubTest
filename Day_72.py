Pascal triangle 


optimal approach
class Solution:
    def generate_row(self,row):
        ans=1
        ansrow=[1]
        for col in range(1,row):
            ans=ans*(row-col)
            ans=ans//col
            ansrow.append(ans)
        return ansrow
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for row in range(1,numRows+1):
            ans.append(self.generate_row(row))
        return ans
