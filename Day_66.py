Brutforce Approach:

def leaders(self, A, N):
        l=[]
        for i in range(N):
            flag=1
            for j in range(i+1,N):
                if A[i]<A[j]:
                    flag=0
                    break
            if(flag):
                l.append(A[i])
        return l



optimized approach:

def leaders(self, A, N):
        maxi=A[N-1]
        leader=[]
        leader.append(A[N-1])
        for i in range(N-2,-1,-1):
            if A[i]>maxi:
                leader.append(A[i])
                maxi=A[i]
        return reversed(leader)
            
