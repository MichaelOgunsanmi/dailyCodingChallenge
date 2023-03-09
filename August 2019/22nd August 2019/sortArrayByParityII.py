# Source: https://leetcode.com/problems/sort-array-by-parity-ii/
#
# Date: 22nd August 2019


"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


# Solution
from typing import List


class Solution:
    def sortArrayByParityII(self, inputArray: List[int]) -> List[int]:
        evenPointer = 0
        findNextEven = 0

        while evenPointer < len(inputArray) and findNextEven < len(inputArray):
            if inputArray[evenPointer] % 2 != 0:
                findNextEven = findEven(inputArray, min(evenPointer, findNextEven))

                if findNextEven == -1:
                    return inputArray

                inputArray[findNextEven], inputArray[evenPointer] = inputArray[evenPointer], inputArray[findNextEven]

            evenPointer += 2

        return inputArray


def findEven(inputArray, currentIndex):
    while currentIndex < len(inputArray):
        if inputArray[currentIndex] % 2 == 0 and currentIndex % 2 != 0:
            return currentIndex

        currentIndex += 1

    return -1
