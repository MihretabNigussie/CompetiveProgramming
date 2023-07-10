class DataStream:

    def __init__(self, value: int, k: int):
        self.lst = deque()
        self.value = value
        self.k = k
        self.dict = defaultdict(int)

    def consec(self, num: int) -> bool:
        
        if len(self.lst) >= self.k:
            temp = self.lst.popleft()
            if temp == self.value:
                self.dict[self.value] -= 1
                
        self.lst.append(num)
        if num == self.value:
            self.dict[num] += 1
        
        if len(self.lst) < self.k or self.dict[self.value] < self.k: 
            return False
        return True


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)