class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Add one to the number represented by the digits array.

        Idea:
        Start from the last digit and simulate addition
        exactly like we do by hand.

        Case 1:
        Digit < 9
            Increment it and return.

        Case 2:
        Digit == 9
            It becomes 0 and carry continues.

        Case 3:
        All digits are 9
            Example:
            999 + 1 = 1000
        """

        # Start from the least significant digit
        for current_index in range(len(digits) - 1, -1, -1):

            # No carry needed
            if digits[current_index] < 9:
                digits[current_index] += 1
                return digits

            # Carry generated
            #
            # Example:
            # 1299
            #    ↑
            #
            # 1299 + 1
            #
            # Last 9 becomes 0
            digits[current_index] = 0

        # If we reach here,
        # every digit was 9.
        #
        # Example:
        # 999
        #
        # becomes
        #
        # 000
        #
        # Need to add a leading 1.
        return [1] + digits