class Solution:

    def encode(self, strs: List[str]) -> str:
        
        string = []

        for word in strs:
            string.append(f"{len(word)}#{word}")

        return "".join(string)


    def decode(self, s: str) -> List[str]:

        words = []

        start = 0

        while start < len(s):
            end = start

            while s[end] != '#':
                end += 1

            length = int(s[start:end])

            word = s[end + 1 : end + 1 + length]

            words.append(word)

            start = end + 1 +length

        return words