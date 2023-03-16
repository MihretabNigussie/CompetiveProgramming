class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'prqs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        res = []
        def backtrack(idx, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return
             
            for character in dict[digits[idx]]:
                backtrack(idx+1, comb+character)
        if digits:   
            backtrack(0,'')
        return res
        