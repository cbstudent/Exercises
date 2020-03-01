class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
        pacific_visited = [[False for _ in range(n)] for _ in range(m)]
        
        result = []
        
        for i in range(m):
            self.dfs(matrix, i, 0, pacific_visited, m, n)
            self.dfs(matrix, i, n-1, atlantic_visited, m, n)
        for j in range(n):
            self.dfs(matrix, 0, j, pacific_visited, m, n)
            self.dfs(matrix, m-1, j, atlantic_visited, m, n)
            
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i,j])
        return result
                
                
    def dfs(self, matrix, i, j, visited, m, n):
        visited[i][j] = True
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dir in directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)
