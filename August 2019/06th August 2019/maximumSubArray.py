# Source: https://leetcode.com/problems/maximum-subarray/

# Level: Easy
#
# Date: 06th August 2019


"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
"""

# Solution
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -pow(2, 31)

        maximumSubArray = nums[0]
        index = 1

        while index < len(nums):
            nums[index] = max(nums[index - 1] + nums[index], nums[index])

            maximumSubArray = max(maximumSubArray, nums[index])

            index += 1

        return maximumSubArray
