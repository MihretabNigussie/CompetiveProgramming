class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()
        words.sort()
        longest = ''
        
        for word in words:
            
            if len(word) == 1 or trie.search(word[:-1]):
                
                trie.insert(word)
                if len(word) > len(longest):
                    
                    longest = word
                elif len(word) == len(longest):
                    
                    if word < longest:
                        longest = word
        return longest
        
        
        
        
        
        
        
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
        for char in word:
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                
                return False
            current = current.children[idx]
        
        return True if current.is_end else False
                
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

