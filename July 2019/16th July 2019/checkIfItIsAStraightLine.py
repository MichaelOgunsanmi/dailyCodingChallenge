# Source: https://leetcode.com/problems/check-if-it-is-a-straight-line/

# Level: Easy

# Date: 16th July 2019

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
#
#
#
#
#
# Example 1:
#
#
#
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:
#
#
#
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
#
# Constraints:
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xIncrease = coordinates[1][0] - coordinates[0][0]
        yIncrease = coordinates[1][1] - coordinates[0][1]

        if yIncrease != 0 and xIncrease != 0:
            gradient = yIncrease / xIncrease
            intercept = coordinates[1][1] - (coordinates[1][0] * gradient)

        index = 2
        while index < len(coordinates) - 1:
            if yIncrease == 0:
                if coordinates[index][1] != coordinates[1][1]:
                    return False
                else:
                    index += 1
                    continue

            elif xIncrease == 0:
                if coordinates[index][0] != coordinates[1][0]:
                    return False
                else:
                    index += 1
                    continue

            elif coordinates[index][1] != gradient * coordinates[index][0] + intercept:
                return False

            index += 1

        return True
