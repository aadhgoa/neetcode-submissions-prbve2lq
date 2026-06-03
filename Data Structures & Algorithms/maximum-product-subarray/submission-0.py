class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        currMin, currMax = 1, 1

        for n in nums:
            temp = currMax * n
            currMax = max(temp, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            res = max(res, currMax)
        
        return res

