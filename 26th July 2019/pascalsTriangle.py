# Source: https://leetcode.com/problems/pascals-triangle/

# Level: Easy

# Date: 26th July, 2019


# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# 
# Example:
# 
# Input: 5
# Output:
# [
#     [1],
#     [1,1],
#     [1,2,1],
#     [1,3,3,1],
#     [1,4,6,4,1]
# ]
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # method 1
        if numRows <= 1:
            return [[1]] * numRows

        output = [[1]]

        while numRows > 1:
            numRows -= 1

            new = [1]

            index = 1
            while index < len(output[len(output) - 1]):
                new.append(output[len(output) - 1][index] + output[len(output) - 1][index - 1])
                index += 1

            new.append(1)

            output.append(new)

        return output

    #     #method 2
    #     if numRows <= 1:
    #         return [[1]] * numRows
    #
    #     main = []
    #     count = 1
    #     while count <= numRows:
    #         output = []
    #
    #         i = count
    #         j = 1
    #         while i >= j:
    #             output.append(self.genRec(i, j, main))
    #             j += 1
    #
    #         main.append(output)
    #         count += 1
    #
    #     return main
    #
    #
    # def genRec(self, i, j, main):
    #     if j == 1 or i == j:
    #         return 1
    #
    #     return main[i-2][j-2] + main[i-2][j-1]
