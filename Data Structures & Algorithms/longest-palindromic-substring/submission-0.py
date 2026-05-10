class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two Pointer 

        resIdx, resLen = 0, 0

        for i in range(len(s)):

            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1

                l -= 1
                r += 1

            # Even Length
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1

                l -= 1
                r += 1
        
        return s[resIdx : resIdx + resLen]