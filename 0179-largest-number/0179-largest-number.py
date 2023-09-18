class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums.sort(reverse=True,key=lambda x: str(x))
        lst = []
        
        for num in nums:
            lst.append(str(num))
            
        left , right = 0 , len(lst)
        
        while left < right-1:
            for i in range(0,right-1):
                if int(lst[i+1]+lst[i])>int(lst[i]+lst[i+1]):
                     lst[i],lst[i+1]=lst[i+1],lst[i]
            left += 1
            
        ans=''
        for i in lst:
            ans += i
        return str(int(ans))
                