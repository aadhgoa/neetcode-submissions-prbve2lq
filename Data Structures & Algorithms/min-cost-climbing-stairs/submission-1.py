class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        dp[i] =
        Minimum cost required to reach step i.

        We can reach step i from:
            - step i-1
            - step i-2
        """

        total_steps = len(cost)

        # dp[i] = minimum cost to reach step i
        #
        # Note:
        # Step n represents the "top"
        # (just beyond the last stair)
        min_cost_to_reach = [0] * (total_steps + 1)

        # Build DP from bottom to top
        for current_step in range(2, total_steps + 1):

            # Option 1:
            # Come from previous step
            cost_from_previous_step = (
                min_cost_to_reach[current_step - 1]
                + cost[current_step - 1]
            )

            # Option 2:
            # Come from two steps below
            cost_from_two_steps_below = (
                min_cost_to_reach[current_step - 2]
                + cost[current_step - 2]
            )

            min_cost_to_reach[current_step] = min(
                cost_from_previous_step,
                cost_from_two_steps_below
            )

        return min_cost_to_reach[total_steps]