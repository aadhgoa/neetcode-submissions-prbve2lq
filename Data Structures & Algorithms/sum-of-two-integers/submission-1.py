class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Add two integers without using + or -.

        Idea:
        Simulate binary addition one bit at a time.

        For each bit:
            sum_bit = a_bit XOR b_bit XOR carry

        Carry occurs when at least
        two of the three bits are 1.
        """

        result = 0

        # Stores carry from previous bit position
        carry = 0

        # Used for handling negative numbers
        thirty_two_bit_mask = 0xFFFFFFFF

        # Process all 32 bits
        for bit_position in range(32):

            # Extract current bit from a
            a_bit = (a >> bit_position) & 1

            # Extract current bit from b
            b_bit = (b >> bit_position) & 1

            # Sum bit without carry propagation
            #
            # XOR behaves like binary addition
            # when carry is ignored
            current_sum_bit = (
                a_bit ^
                b_bit ^
                carry
            )

            # Compute carry for next position
            #
            # Carry exists if at least
            # two bits are 1
            carry = (
                a_bit +
                b_bit +
                carry
            ) >= 2

            # Set bit in result
            if current_sum_bit:
                result |= (
                    1 << bit_position
                )

        # Handle negative numbers
        #
        # Python integers are unlimited length,
        # but the problem assumes 32-bit signed integers.
        if result > 0x7FFFFFFF:

            result = ~(
                result ^ thirty_two_bit_mask
            )

        return result