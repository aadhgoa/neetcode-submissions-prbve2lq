class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i] = Can substring s[i:]
                be segmented using words from wordDict?

        Goal:
        Find dp[0]
        """

        # dp[i] tells whether
        # substring starting at i can be formed
        dp = [False] * (len(s) + 1)

        # Empty string is always valid
        #
        # Example:
        # After consuming all characters,
        # we've successfully formed words.
        dp[len(s)] = True

        # Traverse from right to left
        #
        # We need future answers
        # before computing current answer.
        for start_index in range(len(s) - 1, -1, -1):

            # Try every dictionary word
            for word in wordDict:

                # Check if word fits
                #
                # Avoid index out of bounds
                if start_index + len(word) <= len(s):

                    # Check if word matches
                    # current substring
                    if (
                        s[start_index:start_index + len(word)]
                        == word
                    ):

                        # If remaining substring
                        # can be segmented,
                        # current position is valid
                        dp[start_index] = dp[
                            start_index + len(word)
                        ]

                # No need to continue
                # once we found one valid split
                if dp[start_index]:
                    break

        return dp[0]