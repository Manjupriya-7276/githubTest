class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        if k > 0:
            nums[:] = nums[-k:] + nums[:-k]


or

nums=[1,2,3,4,5,6]
k=3
n = len(nums)
for i in range(0, k):
    temp = nums[0]
    for j in range(0, n - 1):
        nums[j] = nums[j + 1]
    nums[n - 1] = temp
print(nums)
