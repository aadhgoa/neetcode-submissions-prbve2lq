class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda interval: interval[1])

        removals = 0

        previous_end = intervals[0][1]

        for start, end in intervals[1:]:

            if start < previous_end:

                # Overlap detected
                removals += 1

            else:

                previous_end = end

        return removals