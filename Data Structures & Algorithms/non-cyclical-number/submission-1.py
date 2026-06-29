class Solution:
    def isHappy(self, number: int) -> bool:
        """
        A Happy Number eventually becomes 1
        after repeatedly replacing the number
        with the sum of the squares of its digits.

        If a number repeats, we've entered
        a cycle and will never reach 1.
        """

        # Stores all previously seen numbers
        visited_numbers = set()

        while number not in visited_numbers:

            # Mark current number as visited
            visited_numbers.add(number)

            # Compute next number in sequence
            number = self.calculate_sum_of_digit_squares(number)

            # Happy number found
            if number == 1:
                return True

        # Number repeated → cycle detected
        return False

    def calculate_sum_of_digit_squares(
        self,
        number: int
    ) -> int:
        """
        Example:

        82

        8² + 2²

        = 64 + 4

        = 68
        """

        digit_square_sum = 0

        while number:

            # Extract last digit
            digit = number % 10

            # Add square of digit
            digit_square_sum += digit * digit

            # Remove last digit
            number //= 10

        return digit_square_sum