class Solution:
    def leftRotate(self, nums, n, d):
        # code here
        n=len(arr)
        d=d%n
        if d==0:
            return None
        else:
            nums[:]=nums[d:]+nums[:d]
