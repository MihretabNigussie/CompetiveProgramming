class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        p1, p2 = len(a)-1, len(b)-1
        rem = '0'

        while p1 >= 0 and p2 >= 0:

            if a[p1] == '1' and b[p2] == '1':
                if rem == '1':
                    ans += '1'
                else:
                    ans += '0'
                rem = '1'
            elif a[p1] == '0' and b[p2] == '0':
                ans += rem
                rem = '0'
            else:
                if rem == '1':
                    ans += '0'
                    rem = '1'
                else:
                    ans += '1'
            p1 -= 1
            p2 -= 1


        while p1 >= 0:
            if a[p1] == '1' and rem == '1':
                ans += '0'
                rem = '1'

            elif rem == '0' and a[p1] == '0':
                ans += '0'
            else:
                ans += '1'
                rem = '0'
            p1 -= 1


        while p2 >= 0:
            if b[p2] == '1' and rem == '1':
                ans += '0'
                rem = '1'
            elif rem == '0' and b[p2] == '0':
                ans += '0'
            else:
                ans += '1'
                rem = '0'
            p2 -= 1
        if rem == '1':
            ans += '1'
        return ans[::-1]