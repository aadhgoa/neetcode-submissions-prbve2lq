class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize with negative infinity
        # because array can contain all negative values
        INFINITY = float(-math.inf)

        # Running sum of current subarray
        curr_sum = 0

        # Stores maximum subarray sum found so far
        max_sum = INFINITY

        # Traverse through array
        for num in nums:

            # Extend current subarray
            curr_sum += num

            # Update maximum answer
            max_sum = max(max_sum, curr_sum)

            # If current sum becomes negative,
            # discard it completely
            #
            # Negative sum will only reduce
            # future subarray sums
            if curr_sum < 0:
                curr_sum = 0

        return max_sum