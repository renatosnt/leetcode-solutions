class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # tamanho das componentes conexas (com valor 1)
        ans = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i, j))
            
            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                    ans = max(ans, temp)
        return ans