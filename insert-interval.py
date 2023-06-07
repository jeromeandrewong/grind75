from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        [newFirst, newLast] = newInterval
        left = []
        right = []
        for interval in intervals:
            [currStart, currEnd] = interval
            if currEnd < newFirst:
                left.append(interval)
            elif currStart > newLast:
                right.append(interval)
            else:
                newFirst = min(currStart, newFirst)
                newLast = max(currEnd, newLast)
        return left + [[newFirst, newLast]] + right
