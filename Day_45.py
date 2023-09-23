class Solution:

	def print2largest(self,arr, n):
		# code here
		if n<2:
            return None
		max=arr[0]
		sec_max=-1
		for i in range(0,len(arr)):
		    if (arr[i]>max):
		        sec_max=max
		        max=arr[i]
		    else:
		        if(arr[i]>sec_max and arr[i]<max):
		            sec_max=arr[i]
        return sec_max
