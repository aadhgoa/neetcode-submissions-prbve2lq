class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = [str(digit) for digit in digits]

        num_int = int("".join(num_str))

        num_int += 1

        num_plus_one_string = [int(digit) for digit in str(num_int)]

        return num_plus_one_string