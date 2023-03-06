class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        left = 0
        count = {}
        for i in s1:
            count[i] = 1 + count.get(i, 0)
        count2 = {}
        for right in range(len(s2)):
            count2[s2[right]] = 1 + count2.get(s2[right], 0)
          
            if right - left + 1 == len(s1):
                if count == count2:
                    return True
                
                count2[s2[left]] = count2[s2[left]] - 1
                if not count2[s2[left]]:
                    count2.pop(s2[left])
                left += 1
        return False