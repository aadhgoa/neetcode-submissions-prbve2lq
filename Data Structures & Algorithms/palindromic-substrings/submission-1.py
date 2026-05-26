class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        for i in range(len(s)):

            # Odd length palindromes
            #
            # Example:
            # "aba"
            l = r = i
            res += self.countPalindrome(s, l, r)

            # Even length palindromes
            #
            # Example:
            # "abba"
            l = i
            r = i + 1
            res += self.countPalindrome(s, l, r)

        return res

    def countPalindrome(self, s, l, r):

        # Counts palindromes expanding from center
        res = 0

        while (
            l >= 0 and
            r < len(s) and
            s[l] == s[r]
        ):

            # Valid palindrome found
            res += 1

            # Expand outward
            l -= 1
            r += 1

        return res