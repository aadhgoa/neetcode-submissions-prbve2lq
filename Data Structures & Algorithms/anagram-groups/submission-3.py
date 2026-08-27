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

            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            key = tuple(count)

            grouped_anagrams[key].append(word)

        return list(grouped_anagrams.values())