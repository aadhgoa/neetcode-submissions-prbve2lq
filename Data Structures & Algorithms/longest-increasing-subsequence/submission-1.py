class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        LIS[i] =
        Length of the Longest Increasing Subsequence
        starting from index i.
        """

        # Every number itself forms
        # an increasing subsequence of length 1
        longest_subsequence_length = [1] * len(nums)

        # Process from right to left
        #
        # Why?
        #
        # LIS[i] depends on LIS[j]
        # where j > i
        for current_index in range(
            len(nums) - 1,
            -1,
            -1
        ):

            # Check every element to the right
            for next_index in range(
                current_index + 1,
                len(nums)
            ):

                # Can extend increasing subsequence
                if nums[current_index] < nums[next_index]:

                    longest_subsequence_length[
                        current_index
                    ] = max(
                        longest_subsequence_length[
                            current_index
                        ],
                        1 +
                        longest_subsequence_length[
                            next_index
                        ]
                    )

        return max(longest_subsequence_length)