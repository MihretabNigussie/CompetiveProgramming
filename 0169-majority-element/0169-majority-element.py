class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # res, maxCount = 0, 0
        # for i in nums:
        #     count[i] = 1 + count.get(i, 0)
        #     if count[i] > maxCount:
        #         res = i
        #     maxCount = max(count[i], maxCount)
        # return res
        
        dict = Counter(nums)
        max_ = -1
        for key in dict.keys():
            if dict[key] > max_:
                max_ = max(max_, dict[key])
                ans = key
        return ans