class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        dict={}
        l=[]
        for x in a:
            if x not in dict:
                dict[x]=0
            else:
                dict[x]+=1
        for y in b:
            if y not in dict:
                dict[y]=0
            else:
                dict[y]=1
        for item in dict:
            l.append(item)
        l.sort()
        return l
        
        

            
