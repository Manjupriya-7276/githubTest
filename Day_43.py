class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        #e code her
        if low<high:
            p=self.partition(arr,low,high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
    
    def partition(self,arr,low,high):
        # code here
        pivot=arr[high]
        i=low
        j=high-1
        while True:
            while i<=j and arr[i]<=pivot:
                i=i+1
            while i<=j and arr[j]>=pivot:
                j=j-1
            if i>j:
                break
            else:
                arr[i],arr[j]=arr[j],arr[i]
        arr[high],arr[i]=arr[i],arr[high]
        return i
    
