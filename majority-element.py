from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, count = None, 0
        for i in nums:
            if count == 0:
                maj = i
            count += 1 if maj == i else -1
        return maj
