class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
        
            current = root
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in current.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    idx = ord(char) - ord('a')
                    if not current.children[idx]:
                        return False
                    current = current.children[idx]

            return current.is_end
        return dfs(0, self.root)

        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)