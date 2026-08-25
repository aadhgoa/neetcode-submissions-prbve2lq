"""
Pattern: Frequency Counting

Anagram:
- Same characters
- Same frequency of each character
- Order does NOT matter
"""


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Anagrams must have same length
        #
        # Example:
        # "cat" and "cats"
        #
        # Cannot be anagrams
        if len(s) != len(t):
            return False

        # Store frequency of each character in s
        char_count_s = defaultdict(int)

        # Store frequency of each character in t
        char_count_t = defaultdict(int)

        # Count characters in first string
        #
        # Example:
        # "eat"
        #
        # {
        #   'e': 1,
        #   'a': 1,
        #   't': 1
        # }
        for char in s:
            char_count_s[char] += 1

        # Count characters in second string
        #
        # Example:
        # "tea"
        #
        # {
        #   't': 1,
        #   'e': 1,
        #   'a': 1
        # }
        for char in t:
            char_count_t[char] += 1

        # Two strings are anagrams if
        # every character has the same frequency
        return char_count_s == char_count_t