class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Container With Most Water

        Goal:
        Find two lines that can hold the maximum amount of water.

        Area Formula:
            width × height

        where:
            width  = distance between lines
            height = shorter of the two lines

        Key Insight:
        Start with the widest container and shrink intelligently
        using two pointers.
        """

        # Stores maximum area found so far
        result = 0

        # Start with widest possible container
        left = 0
        right = len(heights) - 1

        while left < right:

            # Distance between lines
            width = right - left

            # Water level is limited by shorter line
            height = min(
                heights[left],
                heights[right]
            )

            # Current container area
            area = width * height

            # Update best answer
            result = max(result, area)

            # Move pointer at shorter line
            #
            # Why?
            #
            # Area depends on:
            # width × min(height_left, height_right)
            #
            # Width is definitely decreasing.
            #
            # Only chance to increase area is
            # finding a taller shorter-side wall.
            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return result