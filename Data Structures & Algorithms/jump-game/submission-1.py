class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Goal initially is the last index
        #
        # We want to know:
        # Can we reach this position?
        goal = len(nums) - 1

        # Traverse backwards
        #
        # Start from last index
        # Move toward index 0
        for i in range(len(nums) - 1, -1, -1):

            # If from current index we can reach
            # the current goal,
            # then current index becomes new goal
            #
            # Meaning:
            # "If I can jump to the goal from here,
            # then now I only need to reach HERE."
            if i + nums[i] >= goal:
                goal = i

        # If goal becomes 0,
        # start index can reach end
        return goal == 0