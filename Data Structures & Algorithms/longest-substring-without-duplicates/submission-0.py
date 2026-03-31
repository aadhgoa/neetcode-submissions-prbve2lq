class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_dict = {}
        left = 0
        max_length = 0

        for right_char, char in enumerate(s):
            
            if char in char_dict and char_dict[char] >= left:
                left = char_dict[char] + 1
            
            char_dict[char] = right_char
            window_length = right_char - left + 1

            max_length = max(max_length, window_length)
        
        return max_length


        