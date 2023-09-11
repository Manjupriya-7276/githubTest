a)
class Solution:
    def factorial (self, N):
        fact=1
        for i in range(1,N+1):
            fact=fact*i
        return(fact)
 b)
class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        i=2
        if(n==0):
            return 0
        if(n==1):
            return 1
        else:
            while i<=n:
                c=a+b
                a=b
                b=c
                i=i+1
            return b

