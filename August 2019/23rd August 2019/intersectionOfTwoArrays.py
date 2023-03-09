# Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/
#
# Date: 23rd August 2019


"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


# Solution
from typing import List


class Solution:
    def intersection(self, firstArray: List[int], secondArray: List[int]) -> List[int]:
        if len(firstArray) == 0 or len(secondArray) == 0:
            return []

        hashMap = {}

        if len(firstArray) < len(secondArray):
            for num in firstArray:
                hashMap[num] = True
            main = secondArray
        else:
            for num in secondArray:
                hashMap[num] = True

            main = firstArray

        output = []
        for num in main:
            if num in hashMap:
                output.append(num)
                hashMap.pop(num)

        return output

        # method 2
        # return list(set(firstArray).intersection(secondArray))
