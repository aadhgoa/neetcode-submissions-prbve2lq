class Solution:
    def hammingWeight(self, n: int) -> int:

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