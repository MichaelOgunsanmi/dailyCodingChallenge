# Source: https://leetcode.com/problems/move-zeroes/

# Level: Easy

# Date: 19th July 2019, 2019

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
from typing import List


class Solution:
    def moveZeroes(self, arrayInput: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstPointerIndex = 0
        secondPointerIndex = 1

        while secondPointerIndex != len(arrayInput):
            if arrayInput[firstPointerIndex] == 0:
                if arrayInput[secondPointerIndex] != 0:
                    arrayInput[firstPointerIndex], arrayInput[secondPointerIndex] = arrayInput[secondPointerIndex], arrayInput[firstPointerIndex]
                    firstPointerIndex += 1
                secondPointerIndex += 1
            else:
                firstPointerIndex += 1
                secondPointerIndex += 1