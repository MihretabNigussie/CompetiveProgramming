class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        set1 = set()
        set2 = set()
        
        for i in nums1:
            if i not in nums2:
                set1.add(i)
        for i in nums2:
            if i not in nums1:
                set2.add(i)
                
        return [list(set1), list(set2)]
        