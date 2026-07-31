from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_freq = defaultdict(int)

        for num in nums:
            count_freq[num] += 1


        keys = list(count_freq)

        keys.sort(key=lambda x: count_freq[x], reverse=True)

        return keys[:k]