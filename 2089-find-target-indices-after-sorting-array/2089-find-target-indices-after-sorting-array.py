class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i, v in enumerate(sorted(nums)):
            if v == target:
                lst.append(i)
        return lst