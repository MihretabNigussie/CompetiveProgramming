class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def sieve(n):
            is_prime = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2

            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime

        
        lst = sieve(right)[left:]
        
        lst2 = [i for i in range(left, right+1)]
        # print(lst)
        
        right = len(lst)-1
        ans = []
        diff = float(inf)
        while right >= 0:
            if lst[right]:
                break
            right -= 1
        # print(lst2[right])
        
        for left in range(right -1,-1 ,-1):
            if lst[left]:
                print(lst2[left], diff, lst2[right] - lst2[left])
                if diff >= lst2[right] - lst2[left]:
                    ans = [lst2[left] , lst2[right]]
                    diff = ans[1] - ans[0]
                right = left
                
        if ans:
            return ans
        return [-1,-1]
            
                
                
            
        
        
            
            
                
            
