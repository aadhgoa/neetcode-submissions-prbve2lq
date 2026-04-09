from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        left = 0

        s1_counter = Counter(s1)
        window_counter = Counter()

        for right in range(len(s2)):
            window_counter[s2[right]] += 1

            if right - left + 1 > len(s1):
                window_counter[s2[left]] -= 1

                if window_counter[s2[left]] == 0:
                    del window_counter[s2[left]]

                left += 1

            if window_counter == s1_counter:
                return True

        return False
        