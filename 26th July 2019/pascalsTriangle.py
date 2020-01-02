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
