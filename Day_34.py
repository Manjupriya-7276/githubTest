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
