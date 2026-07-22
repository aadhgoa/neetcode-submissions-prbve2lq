class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Dynamic Programming

        To reach the current step, we can come from:

            1. One step below
            2. Two steps below

        Therefore,

            ways(current) =
                ways(previous_step)
                +
                ways(two_steps_before)

        This is the Fibonacci pattern.
        """

        # Base cases:
        #
        # ways(0) = 1
        # ways(1) = 1
        ways_to_previous_step = 1
        ways_to_two_steps_before = 1

        # Compute answers from step 2 to step n
        for _ in range(n - 1):

            current_ways = (
                ways_to_previous_step
                + ways_to_two_steps_before
            )

            # Shift the window forward
            ways_to_two_steps_before = ways_to_previous_step
            ways_to_previous_step = current_ways

        return ways_to_previous_step