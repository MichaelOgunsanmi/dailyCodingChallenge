# Source: https://leetcode.com/problems/minesweeper/

# Level: Medium
#
# Date: 06th August 2019


"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an
unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right,
and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square,
and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the
board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'. If an empty square ('E') with no adjacent
mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be
revealed recursively. If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit
('1' to '8') representing the number of adjacent mines. Return the board when no more squares will be revealed.


Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:



Note:

The range of the input matrix's height and width is [1,50]. The click position will only be an unrevealed square ('M'
or 'E'), which also means the input board contains at least one clickable square. The input board won't be a stage
when game is over (some mines have been revealed). For simplicity, not mentioned rules should be ignored in this
problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases
that you will win the game or flag any squares. """


# Solution
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        queue = [click]
        maxRowSize = len(board) - 1
        maxColSize = len(board[0]) - 1

        while len(queue) != 0:
            validPoints = []
            mineCount = 0

            currentPositionRow, currentPositionColumn = queue.pop(0)

            if hasLeft(currentPositionRow, currentPositionColumn) and hasTop(currentPositionRow, currentPositionColumn):
                row = currentPositionRow - 1
                col = currentPositionColumn - 1
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if hasTop(currentPositionRow, currentPositionColumn):
                row = currentPositionRow - 1
                col = currentPositionColumn
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if hasRight(currentPositionRow, currentPositionColumn, maxColSize) and hasTop(currentPositionRow, currentPositionColumn):
                row = currentPositionRow - 1
                col = currentPositionColumn + 1
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if hasLeft(currentPositionRow, currentPositionColumn):
                row = currentPositionRow
                col = currentPositionColumn - 1
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if hasRight(currentPositionRow, currentPositionColumn, maxColSize):
                row = currentPositionRow
                col = currentPositionColumn + 1
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if hasLeft(currentPositionRow, currentPositionColumn) and hasBottom(currentPositionRow, currentPositionColumn, maxRowSize):
                row = currentPositionRow + 1
                col = currentPositionColumn - 1
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if hasBottom(currentPositionRow, currentPositionColumn, maxRowSize):
                row = currentPositionRow + 1
                col = currentPositionColumn
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if hasRight(currentPositionRow, currentPositionColumn, maxColSize) and hasBottom(currentPositionRow, currentPositionColumn, maxRowSize):
                row = currentPositionRow + 1
                col = currentPositionColumn + 1
                if isMine(row, col, board):
                    mineCount += 1
                elif shouldBeChecked(row, col, board, queue):
                    validPoints.append([row, col])

            if mineCount == 0:
                board[currentPositionRow][currentPositionColumn] = 'B'
                queue.extend(validPoints)
            else:
                board[currentPositionRow][currentPositionColumn] = str(mineCount)

        return board


def hasLeft(currentPositionRow, currentPositionColumn):
    return currentPositionColumn - 1 >= 0


def hasTop(currentPositionRow, currentPositionColumn):
    return currentPositionRow - 1 >= 0


def hasBottom(currentPositionRow, currentPositionColumn, maxRowSize):
    return currentPositionRow + 1 <= maxRowSize


def hasRight(currentPositionRow, currentPositionColumn, maxColSize):
    return currentPositionColumn + 1 <= maxColSize


def isMine(row, col, board):
    return board[row][col] == 'M'


def shouldBeChecked(row, col, board, queue):
    return board[row][col] == 'E' and ([row, col] not in queue)
