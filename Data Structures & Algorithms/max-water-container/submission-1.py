class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #voulume = max(distance) * height

        """
        Approach:

        2 pointer 

        distance between the 2 pointers 

        and the value whichever is min and check the result to find the max 
        """


        result = 0

        length = len(heights)

        start = 0
        end = length - 1

        while start < end:
            width = end - start
            length = min(heights[start], heights[end])

            volume = width * length

            result = max(result, volume)

            if heights[start] < heights[end]:
                start += 1
            
            else:
                end -= 1

        return result



        