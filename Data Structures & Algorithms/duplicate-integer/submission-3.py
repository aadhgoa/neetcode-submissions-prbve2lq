class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # HashSet to store numbers we've already seen
        # Set lookup is O(1) on average
        seen = set()

        # Traverse each number in the array
        for num in nums:

            # If number already exists in set,
            # we found a duplicate
            if num in seen:
                return True

            # Otherwise add current number
            # to the set for future checks
            seen.add(num)

        # Completed traversal without finding duplicates
        return False