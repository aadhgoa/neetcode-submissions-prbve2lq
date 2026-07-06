class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_map = {}

        for index, number in enumerate(nums):
            complement = target - number

            if complement in index_map:
                return [index_map[complement], index]

            index_map[number] = index
        
        return []
        