class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        count2 = Counter(t)
        if count == count2:
            return True
        return False