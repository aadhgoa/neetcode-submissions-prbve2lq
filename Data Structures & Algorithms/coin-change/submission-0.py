class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Coin Change (Minimum Coins)

        dp[a] = minimum number of coins needed
                to make amount 'a'

        Goal:
        Find dp[amount]
        """

        # Initialize all amounts as impossible
        #
        # Worst case:
        # Need more than 'amount' coins
        # (acts like infinity)
        dp = [amount + 1] * (amount + 1)

        # Base case:
        # 0 coins needed to make amount 0
        dp[0] = 0

        # Build solutions from 1 -> amount
        for a in range(1, amount + 1):

            # Try every coin
            for c in coins:

                # Coin can contribute only if
                # remaining amount is valid
                if a - c >= 0:

                    # Either:
                    # keep current answer
                    #
                    # OR
                    # use coin c
                    dp[a] = min(
                        dp[a],
                        1 + dp[a - c]
                    )

        # If still infinity,
        # amount cannot be formed
        return (
            dp[amount]
            if dp[amount] != amount + 1
            else -1
        )