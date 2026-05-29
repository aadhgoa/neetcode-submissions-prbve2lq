class Solution:
    def countBits(self, n: int) -> List[int]:

        # dp[i] = number of 1 bits in i
        #
        # Example:
        # dp[5] = number of 1s in binary(101) = 2
        dp = [0] * (n + 1)

        # Largest power of 2 seen so far
        #
        # Starts with:
        # 1 -> binary 1
        offset = 1

        # Build answers from 1 to n
        for i in range(1, n + 1):

            # Found next power of 2
            #
            # Example:
            # i = 2, 4, 8, 16 ...
            #
            # Update offset
            if offset * 2 == i:
                offset = i

            # Key relation:
            #
            # i = offset + remainder
            #
            # Example:
            # 13 = 8 + 5
            #
            # binary:
            # 13 = 1101
            #  8 = 1000
            #  5 = 0101
            #
            # So:
            # countBits(13)
            # = 1 + countBits(5)
            #
            dp[i] = 1 + dp[i - offset]

        return dp