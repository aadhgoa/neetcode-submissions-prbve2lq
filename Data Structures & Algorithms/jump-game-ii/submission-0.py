class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Goal:
        Find the minimum number of jumps
        required to reach the last index.

        Greedy Idea:
        Treat every jump as one BFS level.

        Current window:
            All indices reachable using the
            current number of jumps.

        Next window:
            Farthest indices reachable after
            taking one more jump.
        """

        # Number of jumps taken
        minimum_jumps = 0

        # Current reachable window
        #
        # Initially we are only at index 0
        left_boundary = 0
        right_boundary = 0

        # Continue until the last index
        # becomes reachable
        while right_boundary < len(nums) - 1:

            # Farthest index reachable
            # from current window
            farthest_reachable_index = 0

            # Explore every position in
            # current window
            for current_index in range(
                left_boundary,
                right_boundary + 1
            ):

                farthest_reachable_index = max(
                    farthest_reachable_index,
                    current_index + nums[current_index]
                )

            # Move to next BFS level
            left_boundary = right_boundary + 1
            right_boundary = farthest_reachable_index

            # One jump completed
            minimum_jumps += 1

        return minimum_jumps