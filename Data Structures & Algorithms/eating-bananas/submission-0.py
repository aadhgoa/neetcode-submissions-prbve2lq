class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) //2

            #Calculate total hours needed at speed = mid

            hours = 0

            for pile in piles:
                # ceil(pile/mid)

                hours += (pile + mid - 1) // mid

            # If we can finish within h hours
            if hours <= h:
                right = mid #try smaller speed 

            else:
                left = mid + 1 #need faster speed

        return left
