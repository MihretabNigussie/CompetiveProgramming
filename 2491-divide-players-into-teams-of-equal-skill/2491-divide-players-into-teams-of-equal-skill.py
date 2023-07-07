class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        left ,right = 0 , len(skill)-1
        skill.sort()
        temp = skill[left] + skill[right]
        ans = 0
        
        while left < right:
            
            if skill[left] + skill[right] != temp:
                return -1
                
            ans += skill[left] * skill[right]
           
               
            left += 1
            right -= 1
        return ans