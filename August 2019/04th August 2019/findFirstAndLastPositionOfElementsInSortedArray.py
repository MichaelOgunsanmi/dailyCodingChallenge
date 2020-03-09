# Source: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Level: Medium
#
# Date: 04th August 2019


"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


# Solution
from typing import List


class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #         try:
    #             firstOcc = nums.index(target)
    #             secondOcc = lastOcc = len(nums) - 1 - nums[::-1].index(target)
    #         except ValueError:
    #             firstOcc = -1
    #             secondOcc = -1

    #         return [firstOcc, secondOcc]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = binarySearch(nums, target)

        if index == -1:
            return [-1, -1]

        leftOccurrence = leftSide(nums, target, 0, index - 1)
        if leftOccurrence == -1:
            leftOccurrence = index

        rightOccurrence = rightSide(nums, target, index + 1, len(nums) - 1)
        if rightOccurrence == -1:
            rightOccurrence = index

        return [leftOccurrence, rightOccurrence]


def leftSide(nums, target, leftIndex, rightIndex):
    while leftIndex <= rightIndex:
        middleIndex = leftIndex + int((rightIndex - leftIndex) / 2)

        if nums[middleIndex] == target:
            if middleIndex - 1 >= 0 and nums[middleIndex - 1] == target:
                return leftSide(nums[:middleIndex], target, leftIndex, middleIndex - 1)
            return middleIndex
        elif nums[middleIndex] < target:
            leftIndex = middleIndex + 1
        else:
            rightIndex = middleIndex - 1

    return -1


def rightSide(nums, target, leftIndex, rightIndex):
    while leftIndex <= rightIndex:
        middleIndex = leftIndex + int((rightIndex - leftIndex) / 2)

        if nums[middleIndex] == target:
            if middleIndex + 1 < len(nums) and nums[middleIndex + 1] == target:
                return rightSide(nums, target, middleIndex + 1, rightIndex)
            return middleIndex
        elif nums[middleIndex] < target:
            leftIndex = middleIndex + 1
        else:
            rightIndex = middleIndex - 1

    return -1


def binarySearch(nums, target):
    leftIndex = 0
    rightIndex = len(nums) - 1

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + int((rightIndex - leftIndex) / 2)

        if nums[middleIndex] == target:
            return middleIndex
        elif nums[middleIndex] < target:
            leftIndex = middleIndex + 1
        else:
            rightIndex = middleIndex - 1

    return -1
