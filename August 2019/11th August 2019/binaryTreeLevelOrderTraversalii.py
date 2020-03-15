# Source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Level: Easy
#
# Date: 11th August 2019


"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
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
    def levelOrderBottom(self, rootNode: TreeNode) -> List[List[int]]:
        if rootNode is None:
            return []

        queue = [rootNode]

        output = [[rootNode.val]]

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

            queue = siblings
            if len(collector) > 0:
                output.append(collector)

        return output[::-1]
