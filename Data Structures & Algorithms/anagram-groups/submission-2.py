from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group words that are anagrams.

        Key Idea:
        Two words are anagrams if their sorted
        characters are identical.

        Example:
            "eat" -> "aet"
            "tea" -> "aet"
            "ate" -> "aet"

        All of them share the same key.
        """

        # Maps:
        # sorted_word -> list of original words
        grouped_anagrams = defaultdict(list)

        for word in strs:

            # Create a canonical representation
            # by sorting the characters.
            sorted_word = "".join(sorted(word))

            # Add the original word to its group.
            grouped_anagrams[sorted_word].append(word)

        return list(grouped_anagrams.values())