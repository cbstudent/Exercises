class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        cntFresh = 0
        n = len(grid)
        m = len(grid[0])
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cntFresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        result = 0
                
        while q:
            for _ in range(len(q)):
                
                i,j = q.pop(0)
                
                for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        cntFresh -= 1
                        q.append((x,y))
            result += 1
        
        if cntFresh == 0:
            return max(0, result-1)
        else:
            return -1
