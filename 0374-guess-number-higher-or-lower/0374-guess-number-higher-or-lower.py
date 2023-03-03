# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left , right = 1, n
        while left <= right:
            myGuess = left + (right - left)// 2
            if guess(myGuess) == -1:
                right = myGuess - 1
            elif guess(myGuess) == 1:
                left = myGuess + 1
            else:
                return myGuess