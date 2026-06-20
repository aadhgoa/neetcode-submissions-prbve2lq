from collections import Counter, defaultdict

class Solution:
    def minWindow(self, source_string: str, target_string: str) -> str:
        """
        Find the smallest substring of source_string
        containing all characters of target_string.
        """

        if not source_string or not target_string:
            return ""

        # Required character frequencies
        required_char_count = Counter(target_string)

        # Current window character frequencies
        window_char_count = defaultdict(int)

        # Number of character requirements satisfied
        characters_matched = 0

        # Total unique character requirements
        total_requirements = len(required_char_count)

        # Best window found so far
        best_window = [-1, -1]
        best_window_length = float("inf")

        left_pointer = 0

        # Expand window
        for right_pointer in range(len(source_string)):

            current_character = source_string[right_pointer]

            window_char_count[current_character] += 1

            # Requirement satisfied for this character
            if (
                current_character in required_char_count
                and
                window_char_count[current_character]
                ==
                required_char_count[current_character]
            ):
                characters_matched += 1

            # Window is valid
            while characters_matched == total_requirements:

                current_window_length = (
                    right_pointer
                    - left_pointer
                    + 1
                )

                # Update best answer
                if current_window_length < best_window_length:

                    best_window = [
                        left_pointer,
                        right_pointer
                    ]

                    best_window_length = (
                        current_window_length
                    )

                # Remove leftmost character
                left_character = source_string[left_pointer]

                window_char_count[left_character] -= 1

                # Window no longer satisfies requirement
                if (
                    left_character in required_char_count
                    and
                    window_char_count[left_character]
                    <
                    required_char_count[left_character]
                ):
                    characters_matched -= 1

                # Shrink window
                left_pointer += 1

        start_index, end_index = best_window

        return (
            source_string[start_index:end_index + 1]
            if best_window_length != float("inf")
            else ""
        )