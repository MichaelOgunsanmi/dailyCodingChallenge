# Source: https://leetcode.com/problems/squares-of-a-sorted-array/

# Level: Easy
#
# Date: 04th August 2019


"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

"""

# Solution
from typing import List


class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        frontPointer = 0
        backPointer = len(arr) - 1
        output = []

        while frontPointer <= backPointer:
            if abs(arr[frontPointer]) > abs(arr[backPointer]):
                val = arr[frontPointer]
                frontPointer += 1
            else:
                val = arr[backPointer]
                backPointer -= 1

            output.append(val * val)

        return output[::-1]
