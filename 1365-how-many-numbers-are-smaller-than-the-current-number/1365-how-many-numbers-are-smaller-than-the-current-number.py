class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        lst = []
        
        lst2 = sorted(nums)
        
        for i in nums:
            lst.append(lst2.index(i))
        
        return lst
            
        
        
        