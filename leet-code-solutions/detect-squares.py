class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        
        count = 0
        px, py= point
        
        for x, y in self.points:
            
            if abs(px - x) == abs(py - y) and x != px and y != py:
                count += self.counter[(x, py)] * self.counter[(px, y)]
            
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)