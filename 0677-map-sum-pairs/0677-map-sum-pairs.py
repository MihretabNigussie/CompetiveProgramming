class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dict = {}
        

    def insert(self, key: str, val: int) -> None:
        delta = val
        
        if key in self.dict:
            delta= val - self.dict[key]
            
        current = self.root
        self.dict[key] = val
        
        for char in key:
            
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                
                current.children[idx] = TrieNode()
                
            
            
            current = current.children[idx]
            current.prefixCount += delta
        

    def sum(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                return 0
            current = current.children[idx]
        
        return current.prefixCount
        
        
        
class TrieNode:
    def __init__(self):
        self.prefixCount = 0
        self.children = [None for _ in range(26)]


        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)