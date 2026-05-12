class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)

        cols = len(grid[0])

        islands = 0


        def dfs(row, col):

            # out of bound
            if (

                row < 0 or row >= rows or

                col < 0 or col >= cols or

                grid[row][col] == "0"

            ):

                return
            
            # Mark visited

            grid[row][col] = "0"

            # Explore 4 directions

            dfs(row + 1, col)

            dfs(row - 1, col)

            dfs(row, col + 1)

            dfs(row, col - 1)
        
        for r in range(rows):

            for c in range(cols):

                # Found new island

                if grid[r][c] == "1":

                    islands += 1

                    dfs(r, c)

        return islands
            