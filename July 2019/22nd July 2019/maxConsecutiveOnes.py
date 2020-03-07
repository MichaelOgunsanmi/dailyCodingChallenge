# Source: https://leetcode.com/problems/max-consecutive-ones/

# Level: Easy

# Date: 22nd July 2019, 2019

# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        currentCount = 0

        for num in nums:
            if num == 0:
                count = max(count, currentCount)
                currentCount = 0
                continue

            currentCount += 1

        return max(count, currentCount)
