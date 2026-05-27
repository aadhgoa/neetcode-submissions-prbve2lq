class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Binary search boundaries
        left = 0
        right = len(nums) - 1

        # Continue while search space exists
        while left <= right:

            # Middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Check if LEFT half is sorted
            #
            # Example:
            # [4,5,6,7,0,1,2]
            #  left----mid
            #
            # 4 <= 7 -> left half sorted
            if nums[left] <= nums[mid]:

                # Check if target lies inside sorted left half
                #
                # target must satisfy:
                # nums[left] <= target < nums[mid]
                if nums[left] <= target < nums[mid]:

                    # Search left half
                    right = mid - 1

                else:
                    # Search right half
                    left = mid + 1

            # Otherwise RIGHT half must be sorted
            else:

                # Check if target lies in sorted right half
                #
                # nums[mid] < target <= nums[right]
                if nums[mid] < target <= nums[right]:

                    # Search right half
                    left = mid + 1

                else:
                    # Search left half
                    right = mid - 1

        # Target not found
        return -1