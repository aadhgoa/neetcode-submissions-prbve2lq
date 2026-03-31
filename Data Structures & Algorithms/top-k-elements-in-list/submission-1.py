from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_num = defaultdict(int)

        result = []

        for number in nums:
            freq_num[number] += 1

        values = list(freq_num)

        values.sort(key=lambda x: freq_num[x], reverse=True)

        return values[:k]
        