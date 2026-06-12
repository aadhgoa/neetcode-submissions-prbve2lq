class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Find the largest start point
        # Used to create the mapping array
        max_start = max(interval[0] for interval in intervals)

        # mp[i] stores the farthest end
        # of any interval starting at i
        #
        # Example:
        # [1,5] -> mp[1] = 6
        #
        # Using end + 1 allows us to distinguish
        # between "no interval" and interval ending at 0.
        mp = [0] * (max_start + 1)

        # Record the farthest ending interval
        # for each start position
        for start, end in intervals:
            mp[start] = max(
                mp[start],
                end + 1
            )

        result = []

        # Current merged interval end
        current_end = -1

        # Current merged interval start
        current_start = -1

        # Sweep through all possible start positions
        for position in range(len(mp)):

            # Found interval(s) starting here
            if mp[position] != 0:

                # Start a new merged interval
                if current_start == -1:
                    current_start = position

                # Extend current interval
                current_end = max(
                    current_end,
                    mp[position] - 1
                )

            # If we've reached the current interval's end,
            # close the merged interval
            if current_end == position:

                result.append([
                    current_start,
                    current_end
                ])

                current_start = -1
                current_end = -1

        # Handle interval still open after sweep
        if current_start != -1:
            result.append([
                current_start,
                current_end
            ])

        return result