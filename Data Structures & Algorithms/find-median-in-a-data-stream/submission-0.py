"""
Numbers keep arriving continuously, and we need the median quickly at any time.
"""

class MedianFinder:

    def __init__(self):
        # ---------------------------------------------------

        # Max Heap for smaller half

        # Python has only min heap,

        # so we store negative values

        # ---------------------------------------------------

        self.small = []

        # ---------------------------------------------------

        # Min Heap for larger half

        # ---------------------------------------------------

        self.large = []

    def addNum(self, num: int) -> None:
        # ---------------------------------------------------

        # STEP 1:

        # Push into max heap (small)

        # ---------------------------------------------------
        heapq.heappush(self.small, -num)

        # ---------------------------------------------------

        # STEP 2:

        # Ensure ordering property:

        #

        # Every element in small heap

        # should be <= every element in large heap

        # ---------------------------------------------------
        if (

            self.small

            and self.large

            and (-self.small[0] > self.large[0])

        ):

            value = -heapq.heappop(self.small)

            heapq.heappush(self.large, value)
        
        # ---------------------------------------------------

        # STEP 3:

        # Balance heap sizes

        # Difference should not exceed 1

        # ---------------------------------------------------

        # small heap too large

        if len(self.small) > len(self.large) + 1:

            value = -heapq.heappop(self.small)

            heapq.heappush(self.large, value)

        # large heap too large

        if len(self.large) > len(self.small) + 1:

            value = heapq.heappop(self.large)

            heapq.heappush(self.small, -value)
        

    def findMedian(self) -> float:
        # ---------------------------------------------------

        # Odd number of elements

        # ---------------------------------------------------

        if len(self.small) > len(self.large):

            return -self.small[0]

        if len(self.large) > len(self.small):

            return self.large[0]

        # ---------------------------------------------------

        # Even number of elements

        # ---------------------------------------------------

        return (

            (-self.small[0] + self.large[0]) / 2

        )
        
        