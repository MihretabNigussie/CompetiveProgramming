class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        a , b =  inf , inf
        
        for i in nums:
            
            
            if a >= i:
                a = i
            elif b >= i:
                b = i
            else:
                return True
        
        return False