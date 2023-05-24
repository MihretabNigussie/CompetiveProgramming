class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        sums = 0
        
        if k <= numOnes:
            return k
        else:
            sums = numOnes
            k -= (numOnes + numZeros)
            if k >= 0:
                sums -= k
        return sums
            