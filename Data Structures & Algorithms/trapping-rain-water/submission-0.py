class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        left, right = 0, length - 1

        left_max, right_max = 0,0

        water = 0

        while left < right:
            if height[left] < height[right]:
                if left_max < height[left]:
                    left_max = height[left]
                
                else:
                    water += left_max - height[left]
                
                left += 1

            else:
                if right_max < height[right]:
                    right_max = height[right]
                
                else:
                    water += right_max - height[right]

                right -= 1

        
        return water