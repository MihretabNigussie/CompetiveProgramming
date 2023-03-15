class NumArray:

    def __init__(self, nums: List[int]):
        self.lst = []
        curSum = 0
        for i in nums:
            curSum += i
            self.lst.append(curSum)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.lst[right] - self.lst[left-1]
        else:
            return self.lst[right]
        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)