class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left = 0
        mySet = set()
        
        for right in range(len(nums)):
            if nums[right] in mySet:
                return True
            
            mySet.add(nums[right])
            
            if right - left == k:
                mySet.remove(nums[left])
                left += 1
            
        return False
            
            
                
        