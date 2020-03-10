# Source: https://leetcode.com/problems/max-area-of-island/

# Level: Medium
#
# Date: 05th August 2019


"""Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# Solution
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currentMax = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxVal = findMax(grid, row, col)
                    currentMax = max(currentMax, maxVal)

        return currentMax


def findMax(grid, row, col):
    maxRowSize = len(grid) - 1
    maxColSize = len(grid[0]) - 1
    queue = [[row, col]]
    count = 0

    while len(queue) != 0:
        currentPositionRow, currentPositionColumn = queue.pop(0)

        if grid[currentPositionRow][currentPositionColumn] != 1:
            continue

        count += 1
        grid[currentPositionRow][currentPositionColumn] = 2

        if currentPositionRow - 1 >= 0 and grid[currentPositionRow - 1][currentPositionColumn] == 1:
            queue.append([currentPositionRow - 1, currentPositionColumn])

        if currentPositionRow + 1 <= maxRowSize and grid[currentPositionRow + 1][currentPositionColumn] == 1:
            queue.append([currentPositionRow + 1, currentPositionColumn])

        if currentPositionColumn - 1 >= 0 and grid[currentPositionRow][currentPositionColumn - 1] == 1:
            queue.append([currentPositionRow, currentPositionColumn - 1])

        if currentPositionColumn + 1 <= maxColSize and grid[currentPositionRow][currentPositionColumn + 1] == 1:
            queue.append([currentPositionRow, currentPositionColumn + 1])

    return count
