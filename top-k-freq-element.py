from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k: num, v: counter
        count = {}
        # array of array, index of arr + 1 == freq of the num
        freq = [[] for i in range(len(nums))]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c - 1].append(n)

        res = []
        print(freq, count)
        for i in range(len(freq), 0, -1):
            for n in freq[i - 1]:
                res.append(n)
                if len(res) == k:
                    return res
