from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        count2 = Counter(t)
        for j in count.keys():
            if len(s) != len(t) or j not in count2 or count[j] != count2[j]:
                return False
        return True