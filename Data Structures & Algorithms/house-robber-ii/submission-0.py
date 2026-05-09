class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robHouse(nums[1:]), self.robHouse(nums[:-1]))
    
    def robHouse(self, nums: List[int])-> int:
        rob1, rob2 = 0, 0

        for value in nums:
            maxRob = max(rob1 + value, rob2)

            rob1 = rob2
            rob2 = maxRob

        return rob2