from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                return True
        return False