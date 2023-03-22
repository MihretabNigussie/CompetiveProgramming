class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        len1= len(word1)
        len2 = len(word2)
        string = ''
        pointer1 , pointer2 = 0,0
        
        while pointer1 < len1 and pointer2 < len2:
            if word1[pointer1] < word2[pointer2]:
                string += word2[pointer2]
                pointer2 += 1
            elif word1[pointer1] > word2[pointer2]:
                string += word1[pointer1]
                pointer1 += 1
            else:
                if word1[pointer1:] > word2[pointer2:]:
                    string += word1[pointer1]
                    pointer1 += 1
                else:
                    string += word2[pointer2]
                    pointer2 += 1
                    
        return string + word1[pointer1:] + word2[pointer2:]
                    
        