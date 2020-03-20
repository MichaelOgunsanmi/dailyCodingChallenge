# Source: https://leetcode.com/problems/triangle/
#
# Date: 16th August 2019


"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the
row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

# Solution
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        totalSum = [[triangle[0][0]], []]

        for i in range(1, len(triangle)):
            totalSum[1] = [float('inf')] * len(triangle[i])
            for j in range(len(triangle[i - 1])):
                totalSum[1][j] = min(totalSum[1][j], totalSum[0][j] + triangle[i][j])
                totalSum[1][j + 1] = min(totalSum[1][j + 1], totalSum[0][j] + triangle[i][j + 1])

            totalSum[0], totalSum[1] = totalSum[1], []

        return min(totalSum[0])
