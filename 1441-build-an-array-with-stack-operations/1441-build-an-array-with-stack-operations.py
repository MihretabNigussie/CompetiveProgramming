class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        add = "Push"
        target1 = set(target)
        discard = ["Push", "Pop"]
        lst = []
        stack = []
        
        for i in range(1, n+1):
            
            if target == stack:
                return lst 
            
            if i in target1:
                lst.append(add)
                stack.append(i)
            else:
                lst += discard
            
        return lst
                