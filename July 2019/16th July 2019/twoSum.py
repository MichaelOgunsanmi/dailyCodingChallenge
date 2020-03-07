# Source: https://leetcode.com/problems/two-sum/

# Level: Easy

# Date: 16th July 2019, 2019

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List


class Solution:
    def twoSum(self, inputArray: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, value in enumerate(inputArray):
            compliment = target - value
            if compliment in hashMap:
                return [hashMap[compliment], index]
            hashMap[value] = index
