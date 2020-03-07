# Source: https://leetcode.com/problems/spiral-matrix-ii/submissions/

# Level: Medium

# Date: 27th July 2019, 2019


# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#     [ 1, 2, 3 ],
#     [ 8, 9, 4 ],
#     [ 7, 6, 5 ]
# ]
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        matrix = [[0] * n for i in range(n)]
        horizontalMax = len(matrix[0])
        horizontalMin = -1
        verticalMax = len(matrix)
        verticalMin = 0
        val = 1

        i = 0
        j = 0
        while val < (n * n) + 1:
            while j < horizontalMax:
                matrix[i][j] = val
                val += 1
                j += 1
            horizontalMax -= 1
            j -= 1
            i += 1

            while i < verticalMax:
                matrix[i][j] = val
                val += 1
                i += 1
            verticalMax -= 1
            i -= 1
            j -= 1

            while j > horizontalMin:
                matrix[i][j] = val
                val += 1
                j -= 1
            horizontalMin += 1
            j += 1
            i -= 1

            while i > verticalMin:
                matrix[i][j] = val
                val += 1
                i -= 1
            verticalMin += 1
            i += 1
            j += 1

        return matrix
