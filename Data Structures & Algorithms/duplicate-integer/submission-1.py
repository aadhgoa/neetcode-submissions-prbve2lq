class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        number = set()

        for num in nums:
            if num in number:
                return True
            number.add(num)
        
        return False
        