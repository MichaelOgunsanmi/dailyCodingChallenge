# Source: https://leetcode.com/problems/spiral-matrix/submissions/

# Level: Medium

# Date: 26th July, 2019

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        horizontalMax = len(matrix[0])
        horizontalMin = -1
        verticalMax = len(matrix)
        verticalMin = 0
        output = []

        i = 0
        j = 0
        while len(output) < len(matrix) * len(matrix[0]):
            while j < horizontalMax:
                output.append(matrix[i][j])
                j += 1
            horizontalMax -= 1
            j -= 1
            i += 1

            if len(output) == len(matrix) * len(matrix[0]):
                break

            while i < verticalMax:
                output.append(matrix[i][j])
                i += 1
            verticalMax -= 1
            i -= 1
            j -= 1

            if len(output) == len(matrix) * len(matrix[0]):
                break

            while j > horizontalMin:
                output.append(matrix[i][j])
                j -= 1
            horizontalMin += 1
            j += 1
            i -= 1

            if len(output) == len(matrix) * len(matrix[0]):
                break

            while i > verticalMin:
                output.append(matrix[i][j])
                i -= 1
            verticalMin += 1
            i += 1
            j += 1

        return output
