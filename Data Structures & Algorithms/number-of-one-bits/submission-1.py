class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        # Stores number of 1 bits
        res = 0

        # Continue until all bits are processed
        while n:

            # n % 2 checks last bit
            #
            # Even number -> last bit = 0
            # Odd number  -> last bit = 1
            #
            # Add 1 if last bit is set
            res += n % 2

            # Right shift by 1
            #
            # Removes last bit
            #
            # Example:
            # 1011 -> 101
            n = n >> 1

        return res
        """

        # Stores number of set bits (1s)

        res = 0

        # Continue until all set bits are removed

        while n:

            # Remove the RIGHTMOST set bit

            #

            # Example:

            # n = 101100

            #

            # n - 1 = 101011

            #

            # AND operation:

            # 101100

            # 101011

            # ------

            # 101000

            #

            # Rightmost 1 gets removed

            n &= (n - 1)

            # Count removed set bit

            res += 1

        return res