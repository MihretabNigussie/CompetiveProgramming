class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        mySet = set()
        
        for i in nums:
            i = str(i)
            mySet.add(i)
            i = i[::-1]
            while i[0] == '0':
                i = i[1:]
            mySet.add(i)
        
        return len(mySet)
            