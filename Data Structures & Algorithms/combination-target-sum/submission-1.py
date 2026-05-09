class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        # Backtracking function
        def backtracking(start, current_combination, current_sum):

            # If target achieved, store the combination
            if current_sum == target:
                result.append(current_combination[:])
                return

            # If sum exceeds target, stop exploring
            if current_sum > target:
                return


            # Try every number starting from 'start'
            for i in range(start, len(nums)):

                # Choose current number
                current_combination.append(nums[i])

                # Since same element can be reused,
                # we pass 'i' again instead of 'i + 1'
                backtracking(
                    i,
                    current_combination,
                    current_sum + nums[i]
                )

                # Backtrack -> remove last chosen element
                current_combination.pop() 

        # Start backtracking
        backtracking(
            0,
            [],
            0
        )

        return result