# Source: https://leetcode.com/problems/search-a-2d-matrix-ii/
#
# Date: 17th August 2019


"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


# Solution


class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rowStart = 0
        colStart = 0
        rowEnd = len(matrix) - 1
        colEnd = len(matrix[0]) - 1

        within = False

        while not within:
            if rowStart > rowEnd:
                return False

            firstElement = matrix[rowStart][colStart]
            lastElement = matrix[rowStart][colEnd]

            if firstElement <= target <= lastElement:
                break

            rowStart += 1

        while not within:
            if rowEnd < rowStart:
                return False

            firstElement = matrix[rowEnd][colStart]
            lastElement = matrix[rowEnd][colEnd]

            if firstElement <= target <= lastElement:
                break

            rowEnd -= 1

        while not within:
            if colStart > colEnd:
                return False

            firstElement = matrix[rowStart][colStart]
            lastElement = matrix[rowEnd][colStart]

            if firstElement <= target <= lastElement:
                break

            colStart += 1

        while not within:
            if colEnd < colStart:
                return False

            firstElement = matrix[rowStart][colEnd]
            lastElement = matrix[rowEnd][colEnd]

            if firstElement <= target <= lastElement:
                break

            colEnd -= 1

        while rowStart <= rowEnd:
            leftPoint = colStart
            rightPoint = colEnd
            while leftPoint <= rightPoint:
                midCol = leftPoint + int((rightPoint - leftPoint) / 2)
                middleValue = matrix[rowStart][midCol]

                if middleValue == target:
                    return True
                elif middleValue < target:
                    leftPoint += 1
                else:
                    rightPoint -= 1

            rowStart += 1

        return False
