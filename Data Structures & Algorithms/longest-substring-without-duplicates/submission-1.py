class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Stores characters currently inside window
        charSet = set()

        # Left pointer of sliding window
        left = 0

        # Stores maximum substring length
        result = 0

        # Right pointer expands window
        for r in range(len(s)):

            # If duplicate character found,
            # shrink window from left side
            #
            # Continue removing characters
            # until duplicate disappears
            while s[r] in charSet:

                # Remove left character
                charSet.remove(s[left])

                # Shrink window
                left += 1

            # Add current character
            charSet.add(s[r])

            # Window now contains unique characters
            #
            # Current window size:
            # r - left + 1
            result = max(result, r - left + 1)

        return result