# Source: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
#
# Date: 13th August 2019


"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
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
    def largestValues(self, rootNode: TreeNode) -> List[int]:
        if rootNode is None:
            return []

        queue = [rootNode]
        output = [rootNode.val]

        while len(queue) != 0:
            siblings = []
            collector = []

            while len(queue) != 0:
                currentNode = queue.pop(0)

                if currentNode.left is not None:
                    siblings.append(currentNode.left)
                    collector.append(currentNode.left.val)

                if currentNode.right is not None:
                    siblings.append(currentNode.right)
                    collector.append(currentNode.right.val)

            if len(collector) > 0:
                output.append(max(collector))

            queue = siblings

        return output
