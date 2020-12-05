class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check_bounds(i, j):
            try:
                if i >= 0 and i < len(grid) and j >=0 and j < len(grid[0]) and grid[i][j] == "1":
                    return True
            except:
                return False
        
        def bfs(i, j):
            q = []
            q.append((i,j))
            grid[i][j] = "0"
            while len(q):
                curr = q.pop()
                if check_bounds(curr[0] + 1, curr[1]):
                    grid[curr[0] + 1][curr[1]] = "0"
                    q.append((curr[0] + 1, curr[1]))
                    
                if check_bounds(curr[0] - 1, curr[1]):
                    grid[curr[0] - 1][curr[1]] = "0"
                    q.append((curr[0] - 1, curr[1]))
                    
                if check_bounds(curr[0], curr[1]+1):
                    grid[curr[0]][curr[1]+1] = "0"
                    q.append((curr[0], curr[1]+1))
                    
                if check_bounds(curr[0], curr[1]-1):
                    grid[curr[0]][curr[1]-1] = "0"
                    q.append((curr[0], curr[1]-1))
            
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands
        
            
        
