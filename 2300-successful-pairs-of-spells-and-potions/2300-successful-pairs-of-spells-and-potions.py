class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        lst = []
        length = len(potions)
        
        for spell in spells:
            left, right = -1, length
            
            while left + 1 < right:
                mid = left + (right - left) // 2
                product = potions[mid] * spell
                
                
                if product >= success:
                    right = mid
                else:
                    left = mid
            
            
            lst.append(length - right )
        
        return lst