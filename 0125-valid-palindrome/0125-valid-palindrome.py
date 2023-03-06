class Solution:
    def isPalindrome(self, s: str) -> bool:
        collected=""
        for character in s:
            if character.isalnum():
                collected+=character.lower()
                
        return collected==collected[::-1]