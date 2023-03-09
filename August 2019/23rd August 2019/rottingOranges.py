# Source: https://leetcode.com/problems/rotting-oranges/
#
# Date: 23rd August 2019


"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible,
return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]] Output: -1 Explanation:  The orange in the bottom left corner (row 2, column 0) is
never rotten, because rotting only happens 4-directionally. Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

# Solution
import collections
from typing import List


class Solution:
    def orangesRotting(self, arrayInput: List[List[int]]) -> int:
        rowSize, colSize = len(arrayInput), len(arrayInput[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for rowIndex, row in enumerate(arrayInput):
            for colIndex, colValue in enumerate(row):
                if colValue == 2:
                    queue.append((rowIndex, colIndex, 0))

        def neighbors(row, col):
            for currentRow, currentCol in ((row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)):
                if 0 <= currentRow < rowSize and 0 <= currentCol < colSize:
                    yield currentRow, currentCol

        minutes = 0
        while queue:
            row, col, minutes = queue.popleft()
            for currentRow, currentCol in neighbors(row, col):
                if arrayInput[currentRow][currentCol] == 1:
                    arrayInput[currentRow][currentCol] = 2
                    queue.append((currentRow, currentCol, minutes + 1))

        if any(1 in row for row in arrayInput):
            return -1
        return minutes
