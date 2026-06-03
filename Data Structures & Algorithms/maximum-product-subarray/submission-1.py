class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Maximum Product Subarray

        Key Challenge:
        Negative numbers can flip signs.

        Example:
        [-2, 3, -4]

        (-2 * 3) = -6
        (-6 * -4) = 24

        A very negative product can suddenly become
        the maximum product after multiplying by
        another negative number.

        Therefore, we must track BOTH:
        - maximum product ending here
        - minimum product ending here
        """

        # Handles cases where all numbers are negative
        # or array has only one element
        result = max(nums)

        # Maximum product ending at current position
        currMax = 1

        # Minimum product ending at current position
        currMin = 1

        for num in nums:

            # Save current max before updating
            #
            # Needed because currMax changes first
            tempMax = currMax * num

            # Three choices:
            #
            # 1. Start new subarray with num
            # 2. Extend previous max product
            # 3. Extend previous min product
            #
            # Previous min may become max
            # if num is negative
            currMax = max(
                num,
                tempMax,
                currMin * num
            )

            # Same logic for minimum product
            currMin = min(
                num,
                tempMax,
                currMin * num
            )

            # Update global answer
            result = max(result, currMax)

        return result