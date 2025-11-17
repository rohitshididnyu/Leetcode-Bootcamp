from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
         
        # finding fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c]==1:
                    fresh +=1
        dire = [(1,0),(0,1),(0,-1),(-1,0)]

        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                (r,c) = queue.popleft()
                print(queue)
                for (dr,dc) in dire:
                    nr = r+dr
                    nc = c+dc
                    if 0 <= nc < cols and 0 <=nr < rows and grid[nr][nc] == 1:
                        grid[nr][nc]= 2
                        fresh -= 1
                        queue.append((nr,nc))
            minutes += 1
        if fresh ==0:
            return minutes
        else:
            return -1