class MyCircularQueue:

    def __init__(self, k: int):
        self.lst = deque()
        self.length = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.lst.append(value)
            return True
        
        return False
        

    def deQueue(self) -> bool:
        if self.lst:
            self.lst.popleft()
            return True
        return False
            

    def Front(self) -> int:
        return self.lst[0] if self.lst else -1

    def Rear(self) -> int:
        return self.lst[-1] if self.lst else -1

    def isEmpty(self) -> bool:
        return len(self.lst) == 0

    def isFull(self) -> bool:
        return len(self.lst) == self.length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()