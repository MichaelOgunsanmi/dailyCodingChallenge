# Source: https://leetcode.com/problems/transpose-matrix/

# Level: Easy

# Date: 16th July, 2019

# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
#
#
#
#
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#
#
# Note:
#
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000
from typing import List


class Solution:
    def transpose(self, inputArray: List[List[int]]) -> List[List[int]]:
        rows = len(inputArray)
        columns = len(inputArray[0])

        transposedMatrix = [[0] * rows for i in range(columns)]

        for row in range(rows):
            for column in range(columns):
                transposedMatrix[column][row] = inputArray[row][column]

        return transposedMatrix
