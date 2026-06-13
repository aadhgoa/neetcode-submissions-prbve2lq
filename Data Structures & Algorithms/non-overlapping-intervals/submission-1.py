class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Sort by ending time
        intervals.sort(key=lambda interval: interval[1])

        total_intervals = len(intervals)

        # dp[i] =
        # maximum number of non-overlapping intervals
        # ending with interval i
        dp = [1] * total_intervals

        for current_index in range(total_intervals):

            for previous_index in range(current_index):

                # Non-overlapping condition
                if (
                    intervals[previous_index][1]
                    <=
                    intervals[current_index][0]
                ):

                    dp[current_index] = max(
                        dp[current_index],
                        1 + dp[previous_index]
                    )

        max_intervals_kept = max(dp)

        return total_intervals - max_intervals_kept