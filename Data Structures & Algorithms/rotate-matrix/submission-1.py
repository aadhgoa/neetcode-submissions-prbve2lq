class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix 90 degrees clockwise.

        Trick:

        1. Reverse rows (top ↔ bottom)
        2. Transpose matrix (swap across diagonal)

        This achieves a clockwise rotation in-place.
        """

        # ---------------------------------
        # Step 1:
        # Reverse rows
        #
        # Top row becomes bottom row
        # Bottom row becomes top row
        # ---------------------------------

        matrix.reverse()

        # ---------------------------------
        # Step 2:
        # Transpose matrix
        #
        # Swap:
        # matrix[row][col]
        # matrix[col][row]
        #
        # Only process upper triangle
        # to avoid double swapping.
        # ---------------------------------

        matrix_size = len(matrix)

        for row in range(matrix_size):

            for col in range(
                row + 1,
                matrix_size
            ):

                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col]
                )