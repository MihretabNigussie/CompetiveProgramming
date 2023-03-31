class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True for i in range(n)]
        is_prime[0] =  False
        is_prime[1] = False
        i = 2
        counter = n -2
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    if is_prime[j]:
                        is_prime[j] = False
                        counter -= 1
                    j += i
            i += 1


        return counter
