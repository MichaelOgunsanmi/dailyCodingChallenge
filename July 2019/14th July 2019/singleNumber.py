# Source: https://leetcode.com/problems/single-number/solution/

# Level: Easy

# Date: 14th July 2019

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for num in hashMap:
            if hashMap[num] == 1:
                return num