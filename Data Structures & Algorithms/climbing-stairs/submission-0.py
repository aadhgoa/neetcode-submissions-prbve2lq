class Solution:
    def climbStairs(self, n: int) -> int:
        
        # #Base Case
        # if n <= 2:
        #     return n

        # dp = [0] * (n+1)

        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-2] + dp[i-1]


        # return dp[n]

        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one += two
            two = temp
        return one