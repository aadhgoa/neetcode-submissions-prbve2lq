class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets whose sum equals 0.

        Pattern:
        1. Sort the array.
        2. Fix one number at index i.
        3. Use two pointers (left, right) to find the remaining two numbers.
        4. Skip duplicates to avoid repeated triplets.

        Example:
        nums = [-1, 0, 1, 2, -1, -4]

        Sorted:
        [-4, -1, -1, 0, 1, 2]

        Answer:
        [[-1, -1, 2], [-1, 0, 1]]
        """

        # Sorting enables the two-pointer approach
        nums.sort()

        # Stores all unique triplets
        result = []

        # Fix one element at a time
        for i in range(len(nums)):

            # Skip duplicate first elements
            #
            # Example:
            # [-1, -1, 0, 1]
            #
            # If we already processed the first -1,
            # skip the second -1 to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers search the remaining array
            left = i + 1
            right = len(nums) - 1

            while left < right:

                # Current triplet sum
                total = nums[i] + nums[left] + nums[right]

                # Found a valid triplet
                if total == 0:

                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    # Move both pointers inward
                    left += 1
                    right -= 1

                    # Skip duplicate values on the left
                    #
                    # Example:
                    # [-1, -1, 0, 1, 1]
                    #
                    # Avoid generating same triplet again.
                    while (
                        left < right and
                        nums[left] == nums[left - 1]
                    ):
                        left += 1

                    # Skip duplicate values on the right
                    while (
                        left < right and
                        nums[right] == nums[right + 1]
                    ):
                        right -= 1

                # Sum too small
                #
                # Need a larger value
                elif total < 0:
                    left += 1

                # Sum too large
                #
                # Need a smaller value
                else:
                    right -= 1

        return result