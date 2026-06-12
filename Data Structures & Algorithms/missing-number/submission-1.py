class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Missing Number

        Numbers are from:
        [0, n]

        Exactly one number is missing.
        """

        # Start with n
        #
        # Example:
        # nums = [3,0,1]
        #
        # n = 3
        #
        # Expected numbers:
        # 0 + 1 + 2 + 3
        #
        # We start with n because
        # loop only goes from 0 to n-1
        result = len(nums)

        # Add expected index value
        # Subtract actual value
        for index in range(len(nums)):

            result += index - nums[index]

        return result