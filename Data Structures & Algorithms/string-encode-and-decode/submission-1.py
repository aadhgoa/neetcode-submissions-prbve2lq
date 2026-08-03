class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        
        for word in strs:
            encoded_word = f"{len(word)}#{word}"
            encoded_string.append(encoded_word)
        
        return ''.join(encoded_string)

    def decode(self, s: str) -> List[str]:
        #5#HELLO5#WORLD
        result = []

        length_word = len(s)
        start = 0

        while start < length_word:
            end = start

            while s[end] != '#':
                end += 1
            
            word_length = int(s[start:end])

            word = s[end+1:end+word_length+1]
            
            result.append(word)

            start=end+word_length+1

        return result
