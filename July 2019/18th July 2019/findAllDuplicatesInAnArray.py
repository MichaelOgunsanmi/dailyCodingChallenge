# Source: https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Level: Medium

# Date: 18th July 2019, 2019

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
from typing import List


class Solution:
    def findDuplicates(self, arrayInput: List[int]) -> List[int]:
        hashMap = {}
        duplicates = []

        for element in arrayInput:
            if element in hashMap:
                duplicates.append(element)
                continue

            hashMap[element] = True

        return duplicates
