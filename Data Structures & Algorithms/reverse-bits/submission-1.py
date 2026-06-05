'''
Take bit from position i

Put it at position (31 - i)
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse all 32 bits of an unsigned integer.

        Example:

        Input:
        00000000000000000000000000001010

        Output:
        01010000000000000000000000000000
        """

        # Stores reversed number
        result = 0

        # Process all 32 bits
        for bit_position in range(32):

            # Extract current bit from n
            #
            # Example:
            # n = 1010
            #
            # i = 1
            #
            # (1010 >> 1) = 0101
            # 0101 & 1 = 1
            current_bit = (n >> bit_position) & 1

            # Place extracted bit
            # in its reversed position
            #
            # Original position: i
            # Reversed position: 31 - i
            result |= (
                current_bit
                << (31 - bit_position)
            )

        return result