class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        heights.append(0)

        for count in range(len(heights)):
            
            while stack and heights[count] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if not stack:
                    w = count

                else:
                    w = count - stack[-1] - 1

                area = h * w

                max_area = max(max_area, area)

            
            stack.append(count)

        return max_area


