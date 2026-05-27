class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Minimum possible eating speed
        #
        # At least 1 banana/hour
        left = 1

        # Maximum possible eating speed
        #
        # If Koko eats the largest pile in 1 hour
        right = max(piles)

        # Binary search on answer space
        #
        # We are searching for:
        # minimum valid eating speed
        while left < right:

            # Candidate eating speed
            mid = (left + right) // 2

            # Total hours needed
            # if eating speed = mid
            hours = 0

            for pile in piles:

                # Hours needed for current pile
                #
                # ceil(pile / mid)
                #
                # Example:
                # pile = 7
                # speed = 3
                #
                # ceil(7/3) = 3
                #
                # Optimized ceil formula:
                hours += (pile + mid - 1) // mid

            # If Koko can finish within h hours,
            # this speed is valid
            if hours <= h:

                # Try smaller speed
                # to minimize answer
                right = mid

            else:
                # Too slow
                # Need faster speed
                left = mid + 1

        # Smallest valid speed
        return left