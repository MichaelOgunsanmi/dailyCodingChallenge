# Source: https://leetcode.com/problems/search-a-2d-matrix/
#
# Date: 17th August 2019


"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


# Solution
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # solution1
        #         if len(matrix) == 0 or len(matrix[0]) == 0:
        #             return False
        #         rowStart = 0
        #         colStart = 0
        #         rowEnd = len(matrix) - 1
        #         colEnd = len(matrix[0]) - 1

        #         within = False

        #         while not within:
        #             if rowStart > rowEnd:
        #                 return False

        #             firstElement = matrix[rowStart][colStart]
        #             lastElement = matrix[rowStart][colEnd]

        #             if firstElement <= target <= lastElement:
        #                 break

        #             rowStart += 1

        #         while rowStart <= rowEnd:
        #             leftPoint = colStart
        #             rightPoint = colEnd
        #             while leftPoint <= rightPoint:
        #                 midCol = leftPoint + int ((rightPoint - leftPoint) / 2)
        #                 middleValue = matrix[rowStart][midCol]

        #                 if middleValue == target:
        #                     return True
        #                 elif middleValue < target:
        #                     leftPoint += 1
        #                 else:
        #                     rightPoint -= 1

        #             rowStart += 1

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        maxRowSize = len(matrix)
        maxColSize = len(matrix[0])
        leftPoint = 0
        rightPoint = (maxRowSize * maxColSize) - 1

        while leftPoint <= rightPoint:
            midPoint = leftPoint + int((rightPoint - leftPoint) / 2)
            rowMiddleIndex = midPoint // maxColSize
            colMiddleIndex = midPoint % maxColSize

            middleValue = matrix[rowMiddleIndex][colMiddleIndex]

            if middleValue == target:
                return True
            elif middleValue < target:
                leftPoint += 1
            else:
                rightPoint -= 1

        return False
