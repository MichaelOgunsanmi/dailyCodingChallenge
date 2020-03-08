# Source: https://leetcode.com/problems/flood-fill/
#
# Level: Easy
#
# Date: 01st August 2019


"""An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0
to 65535).

Given a coordinate (startingRow, startingColumn) representing the starting pixel (row and column) of the flood fill,
and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting
pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the
newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
startingRow = 1, startingColumn = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (startingRow, startingColumn) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= startingRow < image.length and 0 <= startingColumn < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

# Solution
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], startingRow: int, startingColumn: int, newColor: int) -> List[
        List[int]]:
        maxRowSize = len(image) - 1
        maxColSize = len(image[0]) - 1
        queue = [[startingRow, startingColumn]]
        mainColor = image[startingRow][startingColumn]

        if newColor == mainColor:
            return image

        while len(queue) != 0:
            currentPositionRow, currentPositionColumn = queue.pop(0)
            image[currentPositionRow][currentPositionColumn] = newColor

            if currentPositionRow - 1 >= 0 and image[currentPositionRow - 1][currentPositionColumn] == mainColor:
                if [currentPositionRow - 1, currentPositionColumn] not in queue:
                    queue.append([currentPositionRow - 1, currentPositionColumn])

            if currentPositionRow + 1 <= maxRowSize and image[currentPositionRow + 1][
                currentPositionColumn] == mainColor:
                if [currentPositionRow + 1, currentPositionColumn] not in queue:
                    queue.append([currentPositionRow + 1, currentPositionColumn])

            if currentPositionColumn - 1 >= 0 and image[currentPositionRow][currentPositionColumn - 1] == mainColor:
                if [currentPositionRow, currentPositionColumn - 1] not in queue:
                    queue.append([currentPositionRow, currentPositionColumn - 1])

            if currentPositionColumn + 1 <= maxColSize and image[currentPositionRow][
                currentPositionColumn + 1] == mainColor:
                if [currentPositionRow, currentPositionColumn + 1] not in queue:
                    queue.append([currentPositionRow, currentPositionColumn + 1])

        return image
