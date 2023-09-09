A)
class Solution:
    def isPrime(self, N):
        if N <= 1:
            return 0
        if N <= 3:
            return 1

        if N % 2 == 0 or N % 3 == 0:
            return 0

        i = 5
        while i * i <= N:
            if N % i == 0 or N % (i + 2) == 0:
                return 0
            i += 6

        return 1
B)
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        x_str=str(x)
        rev_str=x_str[::-1].lstrip("0")
        rev_int=int(rev_str)*sign
        if (rev_int < -2**31 or rev_int>2**31-1):
            return 0
        else:
            return rev_int

        
