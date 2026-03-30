from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_char_s = defaultdict(int)
        map_char_t = defaultdict(int)

        for char in s:
            map_char_s[char] += 1

        for char in t:
            map_char_t[char] += 1

        if map_char_s == map_char_t:
            return True

        return False