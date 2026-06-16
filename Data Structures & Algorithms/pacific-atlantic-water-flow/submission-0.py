class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        PACIFIC ATLANTIC WATER FLOW

        Key Insight:
        ----------------------------------------------------
        Don't start DFS from every cell and ask:

            "Can this cell reach an ocean?"

        Instead reverse the problem:

            "Starting from an ocean,
             which cells can I reach?"

        Water normally flows:

            Higher Height -> Lower Height

        Since we are traversing backwards from the ocean,
        we move:

            Lower Height -> Higher Height (or Equal Height)

        Therefore:

            next_height >= current_height

        Pacific touches:
            - Top Row
            - Left Column

        Atlantic touches:
            - Bottom Row
            - Right Column

        Answer:
            Cells reachable from BOTH oceans.
        ----------------------------------------------------
        """

        total_rows = len(heights)
        total_cols = len(heights[0])

        # Cells reachable from Pacific Ocean
        pacific_reachable = set()

        # Cells reachable from Atlantic Ocean
        atlantic_reachable = set()

        def dfs(row, col, reachable_cells):
            """
            Mark all cells reachable from a given ocean.

            We only move to cells that have
            height >= current cell height.

            Why?

            Normal water flow:
                High -> Low

            Reverse DFS:
                Low -> High
            """

            reachable_cells.add((row, col))

            directions = [
                (1, 0),   # Down
                (-1, 0),  # Up
                (0, 1),   # Right
                (0, -1)   # Left
            ]

            for row_offset, col_offset in directions:

                next_row = row + row_offset
                next_col = col + col_offset

                # Skip cells outside the grid
                if (
                    next_row < 0
                    or next_row >= total_rows
                    or next_col < 0
                    or next_col >= total_cols
                ):
                    continue

                # Already visited
                if (next_row, next_col) in reachable_cells:
                    continue

                # Reverse water flow condition
                #
                # We can move only if the next cell
                # is higher or equal in height.
                #
                # Example:
                #
                # Current = 3
                # Next    = 5
                #
                # Water could flow:
                # 5 -> 3
                #
                # Therefore while traversing backwards:
                # 3 -> 5 is allowed.
                if heights[next_row][next_col] < heights[row][col]:
                    continue

                dfs(
                    next_row,
                    next_col,
                    reachable_cells
                )

        # --------------------------------------------------
        # Pacific Ocean DFS
        #
        # Pacific touches:
        #   Top Row
        #   Left Column
        # --------------------------------------------------

        for col in range(total_cols):
            dfs(0, col, pacific_reachable)

        for row in range(total_rows):
            dfs(row, 0, pacific_reachable)

        # --------------------------------------------------
        # Atlantic Ocean DFS
        #
        # Atlantic touches:
        #   Bottom Row
        #   Right Column
        # --------------------------------------------------

        for col in range(total_cols):
            dfs(
                total_rows - 1,
                col,
                atlantic_reachable
            )

        for row in range(total_rows):
            dfs(
                row,
                total_cols - 1,
                atlantic_reachable
            )

        # --------------------------------------------------
        # Intersection
        #
        # Cell must be reachable
        # from BOTH oceans.
        # --------------------------------------------------

        result = []

        for row in range(total_rows):
            for col in range(total_cols):

                if (
                    (row, col) in pacific_reachable
                    and
                    (row, col) in atlantic_reachable
                ):
                    result.append([row, col])

        return result