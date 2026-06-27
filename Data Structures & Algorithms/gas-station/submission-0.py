class Solution:
    def canCompleteCircuit(
        self,
        gas: List[int],
        cost: List[int]
    ) -> int:
        """
        Goal:
        Find the starting gas station from which
        we can complete the entire circular route.

        Greedy Idea:

        If total gas < total cost,
        completing the circuit is impossible.

        Otherwise,
        there is exactly one valid starting station.
        """

        # Overall feasibility check
        if sum(gas) < sum(cost):
            return -1

        # Current fuel remaining while
        # testing a starting station
        current_fuel = 0

        # Current candidate starting station
        starting_station = 0

        for station in range(len(gas)):

            # Fuel gained - Fuel spent
            current_fuel += (
                gas[station]
                - cost[station]
            )

            # Cannot reach next station
            if current_fuel < 0:

                # Every station between
                # starting_station and station
                # is also impossible.
                starting_station = station + 1

                # Restart fuel calculation
                current_fuel = 0

        return starting_station