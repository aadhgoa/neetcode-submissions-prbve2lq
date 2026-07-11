"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(
        self,
        intervals: List[Interval]
    ) -> int:
        """
        Sweep Line Algorithm

        Convert every meeting into two events:

            Start -> +1 room needed

            End   -> -1 room released

        Sweep through time and track
        the maximum number of rooms
        needed simultaneously.
        """

        events = []

        # ------------------------------------
        # Create start and end events
        # ------------------------------------
        for meeting in intervals:

            # Meeting starts
            events.append(
                (meeting.start, 1)
            )

            # Meeting ends
            events.append(
                (meeting.end, -1)
            )

        # ------------------------------------
        # Sort events
        #
        # If start time == end time,
        # process END first.
        #
        # Example:
        #
        # Meeting A: 1 - 5
        # Meeting B: 5 - 8
        #
        # Only one room is needed.
        # ------------------------------------
        events.sort(
            key=lambda event:
            (event[0], event[1])
        )

        current_rooms = 0
        maximum_rooms = 0

        # Sweep through timeline
        for _, room_change in events:

            current_rooms += room_change

            maximum_rooms = max(
                maximum_rooms,
                current_rooms
            )

        return maximum_rooms