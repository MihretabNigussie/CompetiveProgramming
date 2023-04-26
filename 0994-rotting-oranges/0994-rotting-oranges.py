class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def orangesRotting(grid):
            # initialize variables
            m, n = len(grid), len(grid[0])
            fresh, rotten = 0, deque()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fresh += 1
                    elif grid[i][j] == 2:
                        rotten.append((i, j))

            # start BFS
            queue = deque()
            queue.extend(rotten)
            minutes = 0
            while queue:
                # process each level
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for r, c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                            grid[r][c] = 2
                            fresh -= 1
                            queue.append((r, c))

                # increment time
                if queue:
                    minutes += 1

            return minutes if fresh == 0 else -1
        
        return orangesRotting(grid)