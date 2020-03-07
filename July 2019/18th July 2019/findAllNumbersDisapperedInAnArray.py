# Source: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Level: Easy

# Date: 18th July 2019, 2019

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {}
        duplicates = []

        for num in nums:
            hashMap[num] = True

        for num in range(1, len(nums) + 1):
            if num not in hashMap:
                duplicates.append(num)

        return duplicates
        # OR 1 liner #return set(range(1, len(nums) + 1)) - set(nums)
