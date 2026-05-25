"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Sort meetings based on start time
        #
        # After sorting,
        # overlapping meetings will become adjacent
        intervals.sort(key=lambda i: i.start)

        # Traverse from second meeting onward
        for i in range(1, len(intervals)):

            # Previous meeting
            i1 = intervals[i - 1]

            # Current meeting
            i2 = intervals[i]

            # Overlap condition:
            #
            # If previous meeting ends AFTER
            # current meeting starts,
            # person cannot attend both
            #
            # Example:
            # [1,5] and [4,8]
            #
            # 5 > 4 -> overlap
            if i1.end > i2.start:
                return False

        # No overlaps found
        return True