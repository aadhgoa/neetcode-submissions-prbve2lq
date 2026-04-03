class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedText = ''

        for char in s:
            if char.isalnum():
                cleanedText += char.lower()

        length_str = len(cleanedText)

        for char_start in range(length_str):
            char_end = length_str - 1 - char_start

            if cleanedText[char_start] != cleanedText[char_end]:
                return False
            
        
        return True
        