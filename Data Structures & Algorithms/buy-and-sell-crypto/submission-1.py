class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # l -> buying day
        # r -> selling day
        #
        # Start with first possible transaction
        l, r = 0, 1

        # Stores maximum profit found
        maxProfit = 0

        # Traverse through prices
        while r < len(prices):

            # Valid transaction:
            # Buy low, sell high
            if prices[l] < prices[r]:

                # Current profit
                profit = prices[r] - prices[l]

                # Update maximum profit
                maxProfit = max(maxProfit, profit)

            else:
                # Found smaller buying price
                #
                # Move buy pointer to current day
                l = r

            # Always move selling pointer forward
            r += 1

        return maxProfit