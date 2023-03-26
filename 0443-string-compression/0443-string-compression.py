class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left , right = 0,0
        
        length = len(chars)

        for i, char in enumerate(chars):

            if (i + 1) == length or char != chars[i+1]:
                chars[right] = char
                right += 1

                if i > left:
                    repeated_times = i - left + 1

                    for num in str(repeated_times):
                        chars[right] = num
                        right += 1

                left = i + 1

        return right


    
        