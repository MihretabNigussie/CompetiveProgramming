class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def build(n):
            def inverts(string):
                ans = ''
                for i in string:
                    if i == '0':
                        ans += '1'
                    else:
                        ans += '0'
                return ans
            if n == 1:
                return '0'
            answer = build(n-1)
            
            return  answer  + '1' + inverts(answer)[::-1]
        

        return build(n)[k-1]
        
        