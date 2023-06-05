from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        subaarrSum = maxSum = nums[0]
        for num in nums[1:]:
            subaarrSum = max(subaarrSum + num, num)
            maxSum = max(subaarrSum, maxSum)
        return maxSum


#  -2,1,-3,4,-1,2,1,-5,4
