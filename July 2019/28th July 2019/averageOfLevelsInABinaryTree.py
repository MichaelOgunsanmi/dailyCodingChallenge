# Source: https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Level: Easy

# Date: 28th July 2019, 2019

"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
3
/ \
    9  20
/ \
    15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

"""

# Solution

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        currentNode = root
        queue = [currentNode]
        output = []

        while len(queue) > 0:
            currentSum = 0
            currentCount = 0
            currentLevel = []
            while len(queue) > 0:
                currentNode = queue.pop(0)

                if currentNode.left is not None:
                    currentLevel.append(currentNode.left)

                if currentNode.right is not None:
                    currentLevel.append(currentNode.right)

                currentSum += currentNode.val
                currentCount += 1

            queue = currentLevel
            output.append(currentSum / currentCount)

        return output
