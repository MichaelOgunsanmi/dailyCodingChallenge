# Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/
#
# Date: 22nd August 2019


"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm? What if nums1's size is small
compared to nums2's size? Which algorithm is better? What if elements of nums2 are stored on disk, and the memory is
limited such that you cannot load all elements into the memory at once?
"""


# Solution
from typing import List


class Solution:
    def intersect(self, firstArray: List[int], secondArray: List[int]) -> List[int]:
        if len(firstArray) == 0 or len(secondArray) == 0: 
            return []

        hashMap = {}

        if len(firstArray) < len(secondArray):
            for num in firstArray:
                hashMap[num] = hashMap.get(num, 0) + 1
            main = secondArray
        else:
            for num in secondArray:
                hashMap[num] = hashMap.get(num, 0) + 1

            main = firstArray

        output = []
        for num in main:
            if num in hashMap and hashMap[num] > 0:
                output.append(num)
                hashMap[num] -= 1

        return output
