class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return all elements of the matrix in spiral order.

        Idea:
        Maintain four boundaries:

            top
            bottom
            left
            right

        Traverse:

            1. Top Row      (Left  -> Right)
            2. Right Column (Top   -> Bottom)
            3. Bottom Row   (Right -> Left)
            4. Left Column  (Bottom -> Top)

        After each traversal,
        shrink the corresponding boundary.
        """

        if not matrix:
            return []

        result = []

        # Current boundaries of the unvisited matrix
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # Continue while there are still rows and columns left
        while top <= bottom and left <= right:

            # ----------------------------------------
            # 1. Traverse the top row
            # ----------------------------------------
            for column in range(left, right + 1):
                result.append(matrix[top][column])

            # Top row has been processed
            top += 1

            # ----------------------------------------
            # 2. Traverse the right column
            # ----------------------------------------
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])

            # Right column has been processed
            right -= 1

            # ----------------------------------------
            # 3. Traverse the bottom row
            #
            # Only if rows remain.
            # ----------------------------------------
            if top <= bottom:

                for column in range(right, left - 1, -1):
                    result.append(matrix[bottom][column])

                # Bottom row has been processed
                bottom -= 1

            # ----------------------------------------
            # 4. Traverse the left column
            #
            # Only if columns remain.
            # ----------------------------------------
            if left <= right:

                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])

                # Left column has been processed
                left += 1

        return result