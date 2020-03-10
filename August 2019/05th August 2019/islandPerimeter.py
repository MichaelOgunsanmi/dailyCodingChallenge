# Source: https://leetcode.com/problems/island-perimeter/

# Level: Easy
#
# Date: 05th August 2019


"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a
square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the
island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""

# Solution
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        rowSize = len(grid)
        colSize = len(grid[0])

        for row in range(rowSize):
            for column in range(colSize):
                if grid[row][column] == 1:
                    if row - 1 < 0:
                        count += 1
                    if row + 1 == rowSize:
                        count += 1
                    if column - 1 < 0:
                        count += 1
                    if column + 1 == colSize:
                        count += 1

                    if row - 1 >= 0 and grid[row - 1][column] == 0:
                        count += 1
                    if row + 1 < rowSize and grid[row + 1][column] == 0:
                        count += 1
                    if column - 1 >= 0 and grid[row][column - 1] == 0:
                        count += 1
                    if column + 1 < colSize and grid[row][column + 1] == 0:
                        count += 1

        return count
