class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = []
        current = ""
        for i in path + '/':
            if i == '/':
                if current == '..':
                    if lst:
                        lst.pop()
                elif current != "" and current != '.':
                    lst.append(current)
                current = ""
            else:
                current += i
        return '/' + '/'.join(lst)