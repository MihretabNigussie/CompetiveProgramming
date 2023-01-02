class Solution:
    def sortColors(self, dumps) -> None:
        """
        Do not return anything, modify dumps in-place instead.
        """
        for i in range(len(dumps)):
            for j in range(i+1, len(dumps)):
                if dumps[i] > dumps[j]:
                    dumps[i] , dumps[j] = dumps[j] , dumps[i]
