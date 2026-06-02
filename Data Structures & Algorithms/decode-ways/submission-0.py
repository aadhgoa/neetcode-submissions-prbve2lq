class Solution:
    def numDecodings(self, s: str) -> int:
        """
        dp[i] = number of ways to decode
                substring starting at index i

        Optimization:
        Instead of storing entire DP array,
        keep only the next two states.

        dp1 -> dp[i + 1]
        dp2 -> dp[i + 2]
        """

        # dp[i + 2]
        dp2 = 0

        # dp[i + 1]
        #
        # Empty string has one valid decoding
        dp1 = 1

        # Current state dp[i]
        current_ways = 0

        # Traverse from right to left
        for i in range(len(s) - 1, -1, -1):

            # Strings starting with 0
            # cannot be decoded
            if s[i] == "0":
                current_ways = 0

            else:
                # Take single digit
                current_ways = dp1

            # Check if two-digit decoding is valid
            #
            # Valid:
            # 10-26
            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or (
                        s[i] == "2"
                        and s[i + 1] in "0123456"
                    )
                )
            ):
                current_ways += dp2

            # Shift window
            #
            # dp[i] becomes dp1
            # dp[i + 1] becomes dp2
            dp2 = dp1
            dp1 = current_ways

        return dp1