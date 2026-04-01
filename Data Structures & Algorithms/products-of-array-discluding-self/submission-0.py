class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)

        result = [0] * length
        prefix = [0] * length
        suffix = [0] * length


        prefix[0] = suffix[length-1] = 1

        for num in range(1, length):
            prefix[num] = nums[num - 1] * prefix[num - 1]
        
        for num in range(length-2, -1, -1):
            suffix[num] = nums[num + 1] * suffix[num + 1]

        for num in range(length):
            result[num] = prefix[num] * suffix[num]

        return result

        