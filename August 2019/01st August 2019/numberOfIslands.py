# Source: https://leetcode.com/problems/number-of-islands/
#
# Level: Medium
#
# Date: 01st August 2019


"""Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

# Solution
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        numberOfIslands = 0
        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    markIslands(grid, row, column)
                    numberOfIslands += 1

        return numberOfIslands


def markIslands(grid, row, column):
    maxRowSize = len(grid) - 1
    maxColSize = len(grid[0]) - 1
    queue = [[row, column]]

    while len(queue) != 0:
        currentPositionRow, currentPositionColumn = queue.pop(0)
        grid[currentPositionRow][currentPositionColumn] = 2

        if currentPositionRow - 1 >= 0 and grid[currentPositionRow - 1][currentPositionColumn] == "1" and [currentPositionRow - 1, currentPositionColumn] not in queue:
            queue.append([currentPositionRow - 1, currentPositionColumn])

        if currentPositionRow + 1 <= maxRowSize and grid[currentPositionRow + 1][currentPositionColumn] == "1" and [currentPositionRow + 1, currentPositionColumn] not in queue:
            queue.append([currentPositionRow + 1, currentPositionColumn])

        if currentPositionColumn - 1 >= 0 and grid[currentPositionRow][currentPositionColumn - 1] == "1" and [currentPositionRow, currentPositionColumn - 1] not in queue:
            queue.append([currentPositionRow, currentPositionColumn - 1])

        if currentPositionColumn + 1 <= maxColSize and grid[currentPositionRow][currentPositionColumn + 1] == "1" and [currentPositionRow, currentPositionColumn + 1] not in queue:
            queue.append([currentPositionRow, currentPositionColumn + 1])
