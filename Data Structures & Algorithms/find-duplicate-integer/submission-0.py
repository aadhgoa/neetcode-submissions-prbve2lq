class Solution:
    def findDuplicate(self, nums):
        # ----------------------------------------
        # STEP 1: Detect cycle using slow & fast
        # ----------------------------------------

        slow = nums[0]  # start at first value
        fast = nums[0]  # start at first value

        while True:
            # Move slow by 1 step
            slow = nums[slow]

            # Move fast by 2 steps
            fast = nums[nums[fast]]

            # If they meet → cycle exists
            if slow == fast:
                break

        # ----------------------------------------
        # STEP 2: Find entry point of cycle
        # ----------------------------------------

        slow = nums[0]  # reset slow to start

        # Move both one step at a time
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # The meeting point is the duplicate number
        return slow