# Source: https://leetcode.com/problems/set-mismatch/

# Level: Easy

# Date: 13th July 2019

# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in
# the set got duplicated to another number in the set, which results in repetition of one number and loss of another
# number.
#
# Given an array nums representing the data status of this set after the error. Your task is to firstly find the
# number occurs twice and then find the number that is missing. Return them in the form of an array.
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashMap = {}
        highestNumber = len(nums)

        for num in nums:
            if hashMap.get(num) is not None:
                duplicate = num
            hashMap[num] = 1

        for num in range(1, highestNumber+1):
            if num not in hashMap:
                missing = num
                break

        return [duplicate, missing]
