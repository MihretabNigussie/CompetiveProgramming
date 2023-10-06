class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        dict = Counter(nums)
        mySet = set()
        
        but = len(nums) / 3
        
        for num in nums:
            
            if dict[num] > but:
                
                mySet.add(num)
        return list(mySet)