# Source: https://leetcode.com/problems/largest-perimeter-triangle/
#
# Date: 22nd August 2019


"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3
of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""


# Solution
from typing import List


class Solution:
    def largestPerimeter(self, inputArray: List[int]) -> int:
        inputArray.sort()

        index = len(inputArray) - 3
        perimeter = sum(inputArray[index:])

        while index >= 0:
            if inputArray[index] + inputArray[index + 1] > inputArray[index + 2]:
                return perimeter
            else:
                perimeter -= inputArray[index + 2]
                index -= 1
                perimeter += inputArray[index]

        return 0
