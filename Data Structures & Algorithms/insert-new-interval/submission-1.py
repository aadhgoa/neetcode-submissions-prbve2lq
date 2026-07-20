class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:
        """
        Insert a new interval into a sorted,
        non-overlapping interval list.

        Merge overlaps if necessary.
        """

        # Stores final intervals
        result = []

        for current_interval in intervals:

            # Case 1:
            # New interval comes completely BEFORE
            # current interval
            #
            # Example:
            # new = [2,5]
            # curr = [7,9]
            #
            # No overlap possible anymore.
            if newInterval[1] < current_interval[0]:

                result.append(newInterval)

                # Remaining intervals are already sorted
                return result + intervals[intervals.index(current_interval):]

            # Case 2:
            # New interval comes completely AFTER
            # current interval
            #
            # Example:
            # curr = [1,3]
            # new  = [5,7]
            #
            # No overlap.
            elif newInterval[0] > current_interval[1]:

                result.append(current_interval)

            # Case 3:
            # Overlapping intervals
            #
            # Example:
            # [1,5] and [4,8]
            #
            # Merge into:
            # [1,8]
            else:

                newInterval = [
                    min(
                        newInterval[0],
                        current_interval[0]
                    ),
                    max(
                        newInterval[1],
                        current_interval[1]
                    ),
                ]

        # If new interval belongs at end
        result.append(newInterval)

        return result