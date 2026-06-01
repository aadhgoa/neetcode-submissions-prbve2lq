class Solution:
    def coinChange(self, coins: List[int], amount: int):

        # min_coins[target_amount] =
        # minimum coins needed to make target_amount
        min_coins = [amount + 1] * (amount + 1)

        # Base case:
        # 0 coins needed to make amount 0
        min_coins[0] = 0

        # Build solutions from 1 to amount
        for target_amount in range(1, amount + 1):

            # Try every available coin
            for coin in coins:

                # Coin can contribute only if
                # remaining amount is non-negative
                if target_amount >= coin:

                    remaining_amount = target_amount - coin

                    min_coins[target_amount] = min(
                        min_coins[target_amount],
                        1 + min_coins[remaining_amount]
                    )

        return (
            min_coins[amount]
            if min_coins[amount] != amount + 1
            else -1
        )