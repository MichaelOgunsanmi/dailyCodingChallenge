# Source: https://leetcode.com/problems/prison-cells-after-n-days/
#
# Date: 21st August 2019


"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied,
else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)



Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""


# Solution
from typing import List


class Solution:
    def prisonAfterNDays(self, oldCells: List[int], days: int) -> List[int]:
        if days == 0:
            return oldCells

        if len(oldCells) < 3:
            return [0, 0]

        cellsHashMap = {}

        count = 1

        while count < 15:
            index = 1
            newCells = [0]

            while index < len(oldCells) - 1:
                if oldCells[index - 1] == oldCells[index + 1]:
                    newCells.append(1)
                else:
                    newCells.append(0)

                index += 1

            newCells.append(0)

            hashMapCount = count
            if count == 14:
                hashMapCount = 0

            cellsHashMap[hashMapCount] = newCells
            oldCells = newCells

            if count == days:
                return cellsHashMap[hashMapCount]

            count += 1

        return cellsHashMap[days % 14]
