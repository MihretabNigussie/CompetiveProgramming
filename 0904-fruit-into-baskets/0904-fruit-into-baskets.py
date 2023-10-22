class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       
        dict = defaultdict(int)
        
        left , count = 0, 0
        ans = 0
        
        for i in range(len(fruits)):
            
            dict[fruits[i]] += 1
            count += 1
    
            while len(dict) > 2:
                fruit = fruits[left]
                dict[fruit] -= 1

                count -= 1
                left += 1
                if not dict[fruit]:
                    dict.pop(fruit)
            ans = max(ans, count)
        return ans