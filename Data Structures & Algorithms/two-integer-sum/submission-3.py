class Solution:
    def twoSum(self, nums: List[int], target: int):
        """
        Use a HashMap to remember numbers we've already seen.

        For every number:
            complement = target - current_number

        If the complement has already been seen,
        we've found the answer.

        Otherwise, store the current number and
        continue searching.
        """

        # Maps:
        # number -> index
        seen_numbers = {}

        for current_index, current_number in enumerate(nums):

            # Number needed to reach the target
            complement = target - current_number

            # If we've already seen the complement,
            # we've found the required pair.
            if complement in seen_numbers:
                return [
                    seen_numbers[complement],
                    current_index
                ]

            # Store the current number for future lookups.
            seen_numbers[current_number] = current_index

        return []