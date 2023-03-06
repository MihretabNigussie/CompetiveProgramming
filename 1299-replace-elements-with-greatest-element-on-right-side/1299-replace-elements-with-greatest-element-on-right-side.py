class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lst = [-1]
        res = -1
        for i in range(len(arr)-1, 0, -1):
            res = max(arr[i], res)
            lst.append(res)
        lst.sort(reverse=True)
        return lst
