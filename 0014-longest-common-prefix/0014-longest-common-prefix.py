class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = Trie()
        
        shortestStr = min(strs, key = len)
        trie.insert(shortestStr)
        
        ans = len(shortestStr)
        
        
        for string in strs:
            
            ans = min(ans, trie.search(string))
        
        return shortestStr[:ans]
            
            

        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        current = self.root
        for char in word:
            
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for index , char in enumerate(word):
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:

                return index
            current = current.children[idx]
        
        return len(word)
                
        

    
        
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)