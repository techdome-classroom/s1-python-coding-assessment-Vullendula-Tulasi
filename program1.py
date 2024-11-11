class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Check if grid is empty
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island_count = 0

        # DFS function to mark all connected land cells as visited
        def dfs(r, c):
            # Base case: if the cell is out of bounds, water, or already visited
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "W" or
                (r, c) in visited
            ):
                return
            # Mark the cell as visited
            visited.add((r, c))

            # Visit all adjacent cells (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Loop through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find an unvisited land cell, start a new DFS
                if grid[r][c] == "L" and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1  # Increase the count for each new island found

        return island_count
