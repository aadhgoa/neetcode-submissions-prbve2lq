class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        INFINITY = float(-math.inf)
        curr_sum = 0
        max_sum = INFINITY

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum
        
        