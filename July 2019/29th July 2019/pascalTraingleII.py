# Source: https://leetcode.com/problems/pascals-triangle-ii/
#
# Level: Easy
#
# Date: 29th July 2019, 2019


"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

"""


# Solution
from typing import List


def genRec(j, main):
    if j == 1 or j == len(main) + 1:
        return 1

    return main[j - 2] + main[j - 1]


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return [1] * rowIndex

        prevRow = []
        count = 1
        while count <= rowIndex + 1:
            currentRow = []

            i = count
            j = 1
            while i >= j:
                currentRow.append(genRec(j, prevRow))
                j += 1

            prevRow = currentRow
            count += 1

        return prevRow
